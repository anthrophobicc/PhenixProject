# Passe « caméra réelle » sur les rushes déjà rendus, en 2D (aucun rendu 3D) : caméra à l'épaule, aberration
# chromatique, halo autour des zones claires, étalonnage, vignettage, grain. Écrit rushes-film/.
# Usage : blender -b -P filmer.py   (Blender ne sert ici que d'interpréteur Python avec numpy)
import bpy, os, math
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
SRC, DST = os.path.join(ICI, "rushes"), os.path.join(ICI, "rushes-film")
os.makedirs(DST, exist_ok=True)
images = sorted(f for f in os.listdir(SRC) if f.endswith(".jpg"))
rng = np.random.default_rng(3)

def lire(chemin):
    im = bpy.data.images.load(chemin); w, h = im.size
    a = np.empty(w * h * 4, dtype=np.float32); im.pixels.foreach_get(a); bpy.data.images.remove(im)
    return a.reshape(h, w, 4)[..., :3]

def ecrire(a, chemin):
    h, w = a.shape[:2]
    rgba = np.ones((h, w, 4), dtype=np.float32); rgba[..., :3] = np.clip(a, 0, 1)
    im = bpy.data.images.new("sortie", w, h); im.pixels.foreach_set(rgba.ravel())
    im.filepath_raw = chemin; im.file_format = "JPEG"; bpy.context.scene.render.image_settings.quality = 95
    im.save(); bpy.data.images.remove(im)

def echantillonner(c, yy, xx):   # bilinéaire
    h, w = c.shape
    yy = np.clip(yy, 0, h - 1.001); xx = np.clip(xx, 0, w - 1.001)
    y0, x0 = yy.astype(np.int32), xx.astype(np.int32); fy, fx = yy - y0, xx - x0
    return (c[y0, x0] * (1 - fx) + c[y0, x0 + 1] * fx) * (1 - fy) + (c[y0 + 1, x0] * (1 - fx) + c[y0 + 1, x0 + 1] * fx) * fy

def flou(a, k):   # flou rapide : réduction, moyenne glissante, agrandissement
    h, w = a.shape[:2]; p = a[: h // k * k, : w // k * k].reshape(h // k, k, w // k, k, 3).mean(axis=(1, 3))
    for axe in (0, 1):
        for _ in range(3): p = (np.roll(p, 1, axe) + p + np.roll(p, -1, axe)) / 3
    p = np.repeat(np.repeat(p, k, 0), k, 1)
    out = np.zeros_like(a); out[: p.shape[0], : p.shape[1]] = p; return out

# tremblement d'épaule : somme de sinus lents de phases aléatoires (en pixels)
phases = rng.uniform(0, 2 * math.pi, 8)
def tremble(f):
    t = f / 30
    dx = 3.0 * math.sin(1.3 * t + phases[0]) + 1.6 * math.sin(2.9 * t + phases[1]) + 0.7 * math.sin(6.1 * t + phases[2])
    dy = 2.6 * math.sin(1.1 * t + phases[3]) + 1.4 * math.sin(3.4 * t + phases[4]) + 0.6 * math.sin(5.3 * t + phases[5])
    return dx, dy

premiere = lire(os.path.join(SRC, images[0])); H, W = premiere.shape[:2]
gy, gx = np.mgrid[0:H, 0:W].astype(np.float32)
cy, cx = (H - 1) / 2, (W - 1) / 2
r2 = ((gy - cy) / H) ** 2 + ((gx - cx) / H) ** 2
vignette = (1 - 0.55 * np.clip(r2 / 0.42, 0, 1) ** 1.6)[..., None]
ZOOM = 1.035   # léger recadrage pour que le tremblement ne montre jamais de bord

for i, nom in enumerate(images):
    a = lire(os.path.join(SRC, nom))
    dx, dy = tremble(i)
    out = np.empty_like(a)
    for c, ab in enumerate((1.0018, 1.0, 0.9982)):   # rouge et bleu légèrement décalés vers les bords
        s = 1 / (ZOOM * ab)
        out[..., c] = echantillonner(a[..., c], cy + (gy - cy) * s + dy, cx + (gx - cx) * s + dx)
    lum = out @ np.array([0.2126, 0.7152, 0.0722], dtype=np.float32)
    clair = out * np.clip((lum - 0.72) / 0.28, 0, 1)[..., None]
    out = out + 0.35 * flou(clair, 8) + 0.2 * flou(clair, 24)               # halo
    out = 0.035 + out * 0.95                                                 # noirs un peu relevés
    out = out + 0.06 * (out - out ** 2) * (2 * out - 1) * -1                 # contraste doux
    out = out * np.array([1.03, 1.01, 0.95], dtype=np.float32)              # chaud, légèrement vert
    out = out * vignette
    g = rng.normal(0, 1, (H, W)).astype(np.float32)
    out = out + (0.028 * (0.6 + 0.8 * (1 - lum)))[..., None] * g[..., None]   # grain, plus visible dans les ombres
    ecrire(out, os.path.join(DST, nom))
    if i % 50 == 0: print("image", i, flush=True)
print("fini :", len(images), "images dans", DST)
