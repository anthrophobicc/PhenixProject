# Story « l'entrepôt » : un entrepôt abandonné, gris, poussiéreux ; des centaines de câbles (électricité, réseau, câbles
# sous-marins) tombent du toit et des murs, courent au sol et plongent dans une fosse derrière une table ordinaire ; un seul
# câble propre en ressort et monte vers un Phenix 001 intact posé sur la table. Au fond, un filet d'eau de pluie tombe du
# toit. Quand la caméra s'approche, le Phenix s'allume : démarrage, puis les compteurs du monde entier montent.
# Plan unique de 15 s, 1080 × 1920. Concept : l'appareil est un prototype en conception.
# Usage : blender -b -P entrepot.py -- test <pourcentage> <image,image,...>   (ent-NNNN.jpg)
#         blender -b -P entrepot.py -- anim <pourcentage>                     (rushes/fNNNNN.jpg)
# MOTEUR=cycles pour un rendu Cycles sur la carte graphique (par défaut : Eevee).
import bpy, bmesh, math, os, sys, random
import numpy as np
from mathutils import Vector, Matrix

ICI = os.path.dirname(os.path.abspath(__file__))
COMM = os.path.dirname(ICI)
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
MODE = args[0] if args else "test"
POURCENT = int(args[1]) if len(args) > 1 else 50
MM = 0.001
FPS, FIN = 30, 450
H = 16 * MM          # épaisseur du boîtier
TZ = 0.76            # dessus de la table
random.seed(7)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, FIN

def lin(h):  # couleur hexadécimale sRGB → linéaire
    h = h.lstrip("#"); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)

# ---------------------------------------------------------------- écran : suite d'images, une par image du film
# Rafraîchissement complet d'une encre électronique : l'image s'inverse, passe au noir, au blanc, puis la page apparaît.
# Les compteurs se mettent à jour par rafraîchissement partiel, toutes les 3 images.
ALLUMAGE = 176       # le Phenix se réveille
def suite_ecran():
    src = os.path.join(ICI, "ecrans-entrepot"); dossier = os.path.join(ICI, "seq-entrepot")
    cache = {}
    def px(nom):
        if nom not in cache:
            im = bpy.data.images.load(os.path.join(src, nom + ".png"))
            w, h = im.size; a = np.empty(w * h * 4, dtype=np.float32); im.pixels.foreach_get(a)
            cache[nom] = a.reshape(h, w, 4); bpy.data.images.remove(im)
        return cache[nom]
    papier = np.array([0xE4, 0xE1, 0xD8]) / 255; encre = np.array([0x1C, 0x1B, 0x18]) / 255
    def flash(f, ancien, nouveau):
        return [(f, "inv-" + ancien), (f + 2, "noir"), (f + 5, "blanc"), (f + 8, nouveau)]
    A = ALLUMAGE
    etapes = [(1, "veille")] + flash(A, "veille", "boot-0") + [(A + 10, "boot-1"), (A + 20, "boot-2"), (A + 30, "boot-3"), (A + 40, "boot-4")]
    etapes += flash(A + 52, "boot-4", "compte-00") + [(A + 60 + 3 * i, f"compte-{i:02d}") for i in range(1, 60)]
    os.makedirs(dossier, exist_ok=True)
    for f in os.listdir(dossier): os.remove(os.path.join(dossier, f))
    fichiers = {}
    for _, nom in etapes:
        if nom in fichiers: continue
        if nom.startswith("inv-"):
            a = px(nom[4:]).copy(); a[..., :3] = papier + encre - a[..., :3]
        elif nom in ("noir", "blanc"):
            a = np.ones_like(px("veille")); a[..., :3] = encre if nom == "noir" else papier
        else:
            a = px(nom)
        chemin = os.path.join(dossier, "_" + nom + ".png"); h, w = a.shape[:2]
        im = bpy.data.images.new(nom, w, h); im.pixels.foreach_set(a.ravel()); im.filepath_raw = chemin
        im.file_format = "PNG"; im.save(); bpy.data.images.remove(im)
        fichiers[nom] = chemin
    for f in range(1, FIN + 1):
        nom = [n for d, n in etapes if d <= f][-1]
        cible = os.path.join(dossier, f"{f:04d}.png")
        try: os.link(fichiers[nom], cible)
        except OSError:
            import shutil; shutil.copyfile(fichiers[nom], cible)
if os.environ.get("ECRANS", "1") == "1": suite_ecran()

# ---------------------------------------------------------------- matériaux
def nouveau(nom):
    m = bpy.data.materials.new(nom); m.use_nodes = True
    return m, m.node_tree.nodes, m.node_tree.links, m.node_tree.nodes["Principled BSDF"]

def principled(nom, couleur, metal=0.0, rugo=0.5, coat=0.0):
    m, n, l, b = nouveau(nom)
    b.inputs["Base Color"].default_value = (*lin(couleur), 1)
    b.inputs["Metallic"].default_value = metal; b.inputs["Roughness"].default_value = rugo
    if coat: b.inputs["Coat Weight"].default_value = coat; b.inputs["Coat Roughness"].default_value = 0.08
    return m

def metal_brosse(nom, clair, fonce, metal=1.0, rugo=(0.22, 0.36)):
    m, n, l, b = nouveau(nom); b.inputs["Metallic"].default_value = metal
    coord = n.new("ShaderNodeTexCoord"); mp = n.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (2.0, 1400.0, 1400.0)
    l.new(coord.outputs["Object"], mp.inputs["Vector"])
    stries = n.new("ShaderNodeTexNoise"); stries.inputs["Scale"].default_value = 1.0; stries.inputs["Detail"].default_value = 6
    l.new(mp.outputs["Vector"], stries.inputs["Vector"])
    r = n.new("ShaderNodeMapRange"); r.inputs["To Min"].default_value = rugo[0]; r.inputs["To Max"].default_value = rugo[1]
    r.inputs["From Min"].default_value = 0.2; r.inputs["From Max"].default_value = 0.8
    l.new(stries.outputs["Fac"], r.inputs["Value"]); l.new(r.outputs["Result"], b.inputs["Roughness"])
    teinte = n.new("ShaderNodeMix"); teinte.data_type = "RGBA"
    teinte.inputs[6].default_value = (*lin(fonce), 1); teinte.inputs[7].default_value = (*lin(clair), 1)
    l.new(stries.outputs["Fac"], teinte.inputs[0]); l.new(teinte.outputs[2], b.inputs["Base Color"])
    return m

# Matière « bruitée » : deux teintes mélangées par un bruit, rugosité variable, relief léger.
def bruite(nom, c1, c2, echelle, rugo=(0.6, 0.9), relief=0.2, detail=8, metal=0.0, espace="Object"):
    m, n, l, b = nouveau(nom); b.inputs["Metallic"].default_value = metal
    coord = n.new("ShaderNodeTexCoord")
    gros = n.new("ShaderNodeTexNoise"); gros.inputs["Scale"].default_value = echelle; gros.inputs["Detail"].default_value = detail
    gros.inputs["Roughness"].default_value = 0.6
    fin = n.new("ShaderNodeTexNoise"); fin.inputs["Scale"].default_value = echelle * 40; fin.inputs["Detail"].default_value = 3
    l.new(coord.outputs[espace], gros.inputs["Vector"]); l.new(coord.outputs[espace], fin.inputs["Vector"])
    rampe = n.new("ShaderNodeValToRGB")
    rampe.color_ramp.elements[0].position = 0.35; rampe.color_ramp.elements[1].position = 0.7
    rampe.color_ramp.elements[0].color = (*lin(c1), 1); rampe.color_ramp.elements[1].color = (*lin(c2), 1)
    l.new(gros.outputs["Fac"], rampe.inputs["Fac"]); l.new(rampe.outputs["Color"], b.inputs["Base Color"])
    rug = n.new("ShaderNodeMapRange"); rug.inputs["To Min"].default_value = rugo[0]; rug.inputs["To Max"].default_value = rugo[1]
    l.new(fin.outputs["Fac"], rug.inputs["Value"]); l.new(rug.outputs["Result"], b.inputs["Roughness"])
    if relief:
        bp = n.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = relief
        l.new(fin.outputs["Fac"], bp.inputs["Height"]); l.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m

# Béton du sol : taches sombres, poussière claire, et des flaques (zones lisses et sombres qui reflètent).
def beton():
    m, n, l, b = nouveau("béton")
    coord = n.new("ShaderNodeTexCoord")
    taches = n.new("ShaderNodeTexNoise"); taches.inputs["Scale"].default_value = 0.35; taches.inputs["Detail"].default_value = 10
    grain = n.new("ShaderNodeTexNoise"); grain.inputs["Scale"].default_value = 60; grain.inputs["Detail"].default_value = 4
    flaque = n.new("ShaderNodeTexNoise"); flaque.inputs["Scale"].default_value = 0.22; flaque.inputs["Detail"].default_value = 3
    for t in (taches, grain, flaque): l.new(coord.outputs["Object"], t.inputs["Vector"])
    rampe = n.new("ShaderNodeValToRGB")
    e = rampe.color_ramp.elements; e[0].position = 0.3; e[1].position = 0.72
    e[0].color = (*lin("#2A2A28"), 1); e[1].color = (*lin("#6B6A64"), 1)
    l.new(taches.outputs["Fac"], rampe.inputs["Fac"])
    mousse = n.new("ShaderNodeTexNoise"); mousse.inputs["Scale"].default_value = 0.5; mousse.inputs["Detail"].default_value = 8
    l.new(coord.outputs["Object"], mousse.inputs["Vector"])
    mm = n.new("ShaderNodeMapRange"); mm.inputs["From Min"].default_value = 0.56; mm.inputs["From Max"].default_value = 0.68
    l.new(mousse.outputs["Fac"], mm.inputs["Value"])
    vert = n.new("ShaderNodeMix"); vert.data_type = "RGBA"
    l.new(mm.outputs["Result"], vert.inputs[0]); l.new(rampe.outputs["Color"], vert.inputs[6])
    vert.inputs[7].default_value = (*lin("#46532C"), 1)
    masque = n.new("ShaderNodeMapRange"); masque.inputs["From Min"].default_value = 0.6; masque.inputs["From Max"].default_value = 0.64
    l.new(flaque.outputs["Fac"], masque.inputs["Value"])
    mouille = n.new("ShaderNodeMix"); mouille.data_type = "RGBA"
    l.new(masque.outputs["Result"], mouille.inputs[0]); l.new(vert.outputs[2], mouille.inputs[6])
    mouille.inputs[7].default_value = (*lin("#1A1B1C"), 1)
    l.new(mouille.outputs[2], b.inputs["Base Color"])
    rg = n.new("ShaderNodeMapRange"); rg.inputs["To Min"].default_value = 0.72; rg.inputs["To Max"].default_value = 0.95
    l.new(grain.outputs["Fac"], rg.inputs["Value"])
    rf = n.new("ShaderNodeMix"); rf.data_type = "FLOAT"
    l.new(masque.outputs["Result"], rf.inputs[0]); l.new(rg.outputs["Result"], rf.inputs[2]); rf.inputs[3].default_value = 0.04
    l.new(rf.outputs[0], b.inputs["Roughness"])
    bp = n.new("ShaderNodeBump")
    sec = n.new("ShaderNodeMapRange"); sec.inputs["To Min"].default_value = 0.25; sec.inputs["To Max"].default_value = 0.0
    l.new(masque.outputs["Result"], sec.inputs["Value"]); l.new(sec.outputs["Result"], bp.inputs["Strength"])
    l.new(grain.outputs["Fac"], bp.inputs["Height"]); l.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m

def encre(nom, dossier):
    m, n, l, b = nouveau(nom)
    b.inputs["Roughness"].default_value = 0.7
    b.inputs["Coat Weight"].default_value = 0.12; b.inputs["Coat Roughness"].default_value = 0.3
    b.inputs["Specular IOR Level"].default_value = 0.15
    tex = n.new("ShaderNodeTexImage"); tex.interpolation = "Cubic"
    img = bpy.data.images.load(os.path.join(dossier, "0001.png")); img.source = "SEQUENCE"
    tex.image = img
    tex.image_user.frame_duration = FIN; tex.image_user.frame_start = 1; tex.image_user.frame_offset = 0
    tex.image_user.use_auto_refresh = True
    l.new(tex.outputs["Color"], b.inputs["Base Color"])
    # une encre électronique n'émet pas de lumière, mais l'éclairage de lecture intégré la rend lisible dans le noir
    l.new(tex.outputs["Color"], b.inputs["Emission Color"]); b.inputs["Emission Strength"].default_value = 0.0
    return m, b

def decalque(nom, image, couleur, alpha, metal=0.6, rugo=0.55):
    m, n, l, b = nouveau(nom)
    b.inputs["Base Color"].default_value = (*lin(couleur), 1)
    b.inputs["Metallic"].default_value = metal; b.inputs["Roughness"].default_value = rugo
    tex = n.new("ShaderNodeTexImage"); tex.image = bpy.data.images.load(image); tex.extension = "CLIP"
    k = n.new("ShaderNodeMath"); k.operation = "MULTIPLY"; k.inputs[1].default_value = alpha
    l.new(tex.outputs["Alpha"], k.inputs[0]); l.new(k.outputs[0], b.inputs["Alpha"])
    return m

def emissif(nom, couleur, force):
    m, n, l, b = nouveau(nom)
    b.inputs["Base Color"].default_value = (0, 0, 0, 1)
    b.inputs["Emission Color"].default_value = (*lin(couleur), 1); b.inputs["Emission Strength"].default_value = force
    return m, b

ACIER = metal_brosse("acier brossé", "#D2D1CB", "#9C9B95", rugo=(0.18, 0.30))
LUNETTE = principled("lunette", "#1E1D1B", 0, 0.35, coat=1.0)
SOCLE = principled("croix", "#2C2B28", 0, 0.42)
FLECHE = principled("flèches", "#CFCBC2", 0, 0.38)
OK = principled("bouton vert", "#7FB070", 0, 0.32, coat=0.6)
TROU = principled("trou", "#050505", 0, 0.9)
GAINE_PROPRE = principled("câble propre", "#D8D5CD", 0, 0.45)
NICKEL = principled("nickel", "#D8D8DA", 1.0, 0.16)
GRAVURE = principled("gravure", "#3C3B37", 0.7, 0.55)
LOGO = decalque("logo", os.path.join(ICI, "logo-hd.png"), "#2A2926", 0.7)
DEL, DEL_B = emissif("témoin vert", "#5CFF8A", 0.0)
BETON = beton()
MUR = bruite("mur", "#3A3A38", "#5E5D58", 0.4, relief=0.3)
TOIT = bruite("toit", "#1E1F20", "#34353A", 0.3)
ACIER_SALE = bruite("poutres", "#2B2C2E", "#4A4238", 0.8, rugo=(0.45, 0.8), metal=0.7)
BOIS = bruite("table", "#5A4A3A", "#8C8272", 2.0, rugo=(0.7, 0.95), relief=0.15)  # bois sous une couche de poussière
MODULE = bruite("module", "#2E3033", "#4B4E52", 6.0, rugo=(0.35, 0.6), metal=0.8, relief=0.1)
GAINES = [bruite(f"gaine {i}", c1, c2, 3.0, rugo=(0.45, 0.75), relief=0.1) for i, (c1, c2) in
          enumerate([("#0D0D0E", "#1C1C1E"), ("#121314", "#26272A"), ("#16150F", "#2E2A20"), ("#1B1D20", "#34373C")])]
JAUNE = principled("repère jaune", "#8A6A12", 0, 0.6)
CIEL, _ = emissif("ciel gris", "#B9C0C6", 2.2)

# ---------------------------------------------------------------- géométrie
def objet(nom, me, mat, parent=None):
    ob = bpy.data.objects.new(nom, me); sc.collection.objects.link(ob)
    if mat: ob.data.materials.append(mat)
    if parent: ob.parent = parent
    return ob

def lisser(ob):
    for p in ob.data.polygons: p.use_smooth = True
    ob.modifiers.new("normales", "WEIGHTED_NORMAL").keep_sharp = True

def boite(nom, lx, ly, lz, pos, mat):
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co.x *= lx; v.co.y *= ly; v.co.z *= lz
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    ob = objet(nom, me, mat); ob.location = pos
    return ob

def pave(nom, lx, ly, lz, rayon, chanfrein, mat, parent=None, seg=16, seg_c=5):
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co.x *= lx; v.co.y *= ly; v.co.z *= lz
    vert = [e for e in bm.edges if abs(e.verts[0].co.z - e.verts[1].co.z) > lz * 0.9]
    bmesh.ops.bevel(bm, geom=vert, offset=rayon, segments=seg, profile=0.5, affect="EDGES")
    if chanfrein > 0:
        bord = [e for e in bm.edges if abs(e.verts[0].co.z - e.verts[1].co.z) < 1e-9 and abs(abs(e.verts[0].co.z) - lz / 2) < 1e-9]
        bmesh.ops.bevel(bm, geom=bord, offset=chanfrein, segments=seg_c, profile=0.5, affect="EDGES")
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    ob = objet(nom, me, mat, parent); lisser(ob)
    return ob

def bouton(nom, r, h, mat, parent, biseau, seg=64):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg, radius1=r, radius2=r, depth=h)
    haut = [e for e in bm.edges if all(abs(v.co.z - h / 2) < 1e-9 for v in e.verts)]
    if biseau: bmesh.ops.bevel(bm, geom=haut, offset=biseau, segments=4, profile=0.5, affect="EDGES")
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    ob = objet(nom, me, mat, parent); lisser(ob)
    return ob

def plaque(nom, lx, ly, mat, parent=None):
    bm = bmesh.new(); bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.5)
    for v in bm.verts: v.co.x *= lx; v.co.y *= ly
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    uv = me.uv_layers.new(name="UV").data
    for poly in me.polygons:
        for li in poly.loop_indices:
            co = me.vertices[me.loops[li].vertex_index].co
            uv[li].uv = (co.x / lx + 0.5, co.y / ly + 0.5)
    return objet(nom, me, mat, parent)

def fleche(nom, pts, h, mat, parent):
    bm = bmesh.new()
    f = bm.faces.new([bm.verts.new((x, y, 0)) for x, y in pts])
    ext = bmesh.ops.extrude_face_region(bm, geom=[f])
    for v in [e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)]: v.co.z += h
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    return objet(nom, me, mat, parent)

POLICE = bpy.data.fonts.load("C:/Windows/Fonts/consolab.ttf") if os.path.exists("C:/Windows/Fonts/consolab.ttf") else None
ENCRE, ENCRE_B = encre("encre", os.path.join(ICI, "seq-entrepot"))

def phenix001(nom, x, y, rz):
    racine = bpy.data.objects.new(nom, None); sc.collection.objects.link(racine)
    racine.location = (x, y, TZ + H / 2); racine.rotation_euler = (0, 0, math.radians(rz))
    haut = H / 2
    pave(nom + " corps", 100 * MM, 48 * MM, H, 9 * MM, 1.4 * MM, ACIER, racine)
    lunette = pave(nom + " lunette", 62 * MM, 40 * MM, 0.8 * MM, 3.5 * MM, 0.25 * MM, LUNETTE, racine, 10, 3)
    lunette.location = (-15 * MM, 0, haut + 0.2 * MM)
    ecran = plaque(nom + " écran", 56 * MM, 34 * MM, ENCRE, racine); ecran.location = (-15 * MM, 0, haut + 0.61 * MM)
    cx, cy = 32 * MM, 0
    socle = bouton(nom + " croix", 11 * MM, 1.4 * MM, SOCLE, racine, 0.5 * MM); socle.location = (cx, cy, haut)
    for i, ang in enumerate((0, 90, 180, 270)):
        a = math.radians(ang)
        rot = lambda px, py: (cx + px * math.cos(a) - py * math.sin(a), cy + px * math.sin(a) + py * math.cos(a))
        pts = [rot(0, 7.8 * MM), rot(-2.4 * MM, 5.2 * MM), rot(2.4 * MM, 5.2 * MM)]
        f = fleche(nom + f" flèche {i}", pts, 0.2 * MM, FLECHE, racine); f.location = (0, 0, haut + 0.69 * MM)
    ok = bouton(nom + " ok", 4.2 * MM, 2.2 * MM, OK, racine, 0.7 * MM); ok.location = (cx, cy, haut + 0.5 * MM)
    for i, bx in enumerate((22 * MM, 42 * MM)):
        b = bouton(nom + f" bouton {i}", 2.3 * MM, 1.6 * MM, SOCLE, racine, 0.45 * MM); b.location = (bx, -16.5 * MM, haut + 0.1 * MM)
    trou = bouton(nom + " dragonne", 1.9 * MM, 0.2 * MM, TROU, racine, 0.05 * MM); trou.location = (44.5 * MM, 18 * MM, haut)
    lg = plaque(nom + " logo", 4.6 * MM, 4.6 * MM, LOGO, racine); lg.location = (23.3 * MM, 18.1 * MM, haut + 0.01 * MM)
    t = bpy.data.curves.new(nom + " 001", "FONT"); t.body = "001"; t.size = 2.6 * MM; t.space_character = 1.25
    if POLICE: t.font = POLICE
    num = objet(nom + " 001", t, GRAVURE, racine); num.location = (26.8 * MM, 17.2 * MM, haut + 0.01 * MM)
    temoin = bouton(nom + " témoin", 0.9 * MM, 0.3 * MM, DEL, racine, 0.2 * MM); temoin.location = (38.5 * MM, 18.1 * MM, haut + 0.05 * MM)
    port = pave(nom + " port", 8.9 * MM, 3.1 * MM, 1.0 * MM, 1.5 * MM, 0, TROU, racine, 10)
    port.rotation_euler = (math.radians(90), 0, 0); port.location = (0, -24 * MM + 0.48 * MM, 0)
    return racine

P = phenix001("Phenix", 0.02, 0.0, -7)
bpy.context.view_layer.update()

# prise USB-C branchée dans le port avant
def prise(nom, appareil):
    r = bpy.data.objects.new(nom, None); sc.collection.objects.link(r)
    r.rotation_euler = appareil.rotation_euler.copy()
    coque = pave(nom + " coque", 8.25 * MM, 2.4 * MM, 6.6 * MM, 1.15 * MM, 0.2 * MM, NICKEL, r, 10, 2)
    coque.rotation_euler = (math.radians(-90), 0, 0); coque.location = (0, 3.3 * MM, 0)
    gaine = pave(nom + " gaine", 12.2 * MM, 6.4 * MM, 17 * MM, 3.0 * MM, 1.2 * MM, GAINE_PROPRE, r, 12, 4)
    gaine.rotation_euler = (math.radians(-90), 0, 0); gaine.location = (0, -8.8 * MM, 0)
    bm = bmesh.new(); bmesh.ops.create_cone(bm, cap_ends=True, segments=40, radius1=2.7 * MM, radius2=1.95 * MM, depth=8 * MM)
    me = bpy.data.meshes.new(nom + " manchon"); bm.to_mesh(me); bm.free()
    manchon = objet(nom + " manchon", me, GAINE_PROPRE, r); lisser(manchon)
    manchon.rotation_euler = (math.radians(90), 0, 0); manchon.location = (0, -21 * MM, 0)
    return r
pr = prise("prise", P); pr.location = P.matrix_world @ Vector((0, -24 * MM - 0.25 * MM, 0))
bpy.context.view_layer.update()
rot = pr.rotation_euler.to_matrix()
SORTIE = Matrix.Translation(pr.location) @ rot.to_4x4() @ Vector((0, -24.8 * MM, 0))
DIR = (rot @ Vector((0, -1, 0))).normalized()

# ---------------------------------------------------------------- la tranchée derrière la table
# Une tranchée ouverte part de derrière la table vers le fond. Les câbles y arrivent des deux côtés et y plongent ;
# un seul câble propre en ressort, côté table, et monte jusqu'au Phenix.
LX, LY, LZ = 40, 30, 9
FX, FY, FDX, FDY = 0.1, 6.2, 0.5, 5.3   # centre et demi-dimensions de la tranchée
FOND = -1.3
PC = Vector((FX, FY, 0))

def dalle(nom, x0, x1, y0, y1, z, mat):
    bm = bmesh.new(); bm.faces.new([bm.verts.new(c) for c in ((x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z))])
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    return objet(nom, me, mat)

for nom, x0, x1, y0, y1 in (("sol avant", -LX / 2, LX / 2, -LY / 2, FY - FDY), ("sol arrière", -LX / 2, LX / 2, FY + FDY, LY / 2),
                            ("sol gauche", -LX / 2, FX - FDX, FY - FDY, FY + FDY), ("sol droit", FX + FDX, LX / 2, FY - FDY, FY + FDY)):
    dalle(nom, x0, x1, y0, y1, 0.0, BETON)
dalle("fond de fosse", FX - FDX, FX + FDX, FY - FDY, FY + FDY, FOND, principled("fond de fosse", "#0A0A0A", 0, 0.9))
EP, HP = 0.15, -FOND - 0.002
for nom, lx, ly, x, y in (("paroi gauche", EP, 2 * FDY + 2 * EP, FX - FDX - EP / 2, FY), ("paroi droite", EP, 2 * FDY + 2 * EP, FX + FDX + EP / 2, FY),
                          ("paroi avant", 2 * FDX, EP, FX, FY - FDY - EP / 2), ("paroi arrière", 2 * FDX, EP, FX, FY + FDY + EP / 2)):
    boite(nom, lx, ly, HP, (x, y, FOND / 2 - 0.001), BETON)
for nom, lx, ly, x, y in (("cornière g", 0.006, 2 * FDY, FX - FDX + 0.003, FY), ("cornière d", 0.006, 2 * FDY, FX + FDX - 0.003, FY),
                          ("cornière av", 2 * FDX, 0.006, FX, FY - FDY + 0.003), ("cornière ar", 2 * FDX, 0.006, FX, FY + FDY - 0.003)):
    boite(nom, lx, ly, 0.08, (x, y, -0.04), ACIER_SALE)

def tube(nom, pts, rayon, mat, res=None):
    propres = [pts[0]]
    for p in pts[1:]:
        if (p - propres[-1]).length > 1e-4: propres.append(p)
    cu = bpy.data.curves.new(nom, "CURVE"); cu.dimensions = "3D"; cu.twist_mode = "MINIMUM"
    cu.bevel_depth = rayon; cu.use_fill_caps = True
    cu.bevel_resolution = res if res is not None else (4 if rayon > 0.06 else 3 if rayon > 0.03 else 2)
    sp = cu.splines.new("POLY"); sp.points.add(len(propres) - 1); sp.use_smooth = True
    for p, co in zip(sp.points, propres): p.co = (co.x, co.y, co.z, 1.0)
    return objet(nom, cu, mat)

def bez(p0, p1, p2, p3, n):
    return [p0 * (1 - t) ** 3 + p1 * (3 * (1 - t) ** 2 * t) + p2 * (3 * (1 - t) * t * t) + p3 * t ** 3 for t in (i / n for i in range(n + 1))]

def catmull(pts, n):
    P = [pts[0] * 2 - pts[1]] + pts + [pts[-1] * 2 - pts[-2]]; out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for j in range(n):
            t = j / n
            out.append(0.5 * (2 * p1 + (p2 - p0) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (3 * p1 - p0 - 3 * p2 + p3) * t ** 3))
    return out + [pts[-1]]

def plongee(e, n, r, lift, nb=8):
    # passe par-dessus le bord de la fosse (arc autour de l'arête : les câbles empilés s'enroulent les uns sur les autres)
    # puis descend le long de la paroi
    rho = r + lift
    arc = [e + Vector((0, 0, rho * math.cos(a))) - n * (rho * math.sin(a)) for a in (math.pi / 2 * i / nb for i in range(nb + 1))]
    return arc + [arc[-1] + Vector((0, 0, FOND + 0.05))]

# ---------------------------------------------------------------- le câble propre : du Phenix, par-dessus le bord arrière de la table, jusqu'à la fosse
RC = 2.0 * MM
X_DOS = 0.17
table_pts = [SORTIE, SORTIE + DIR * 0.015, SORTIE + DIR * 0.045, Vector((0.10, -0.075, 0)), Vector((0.135, 0.02, 0)),
             Vector((0.155, 0.2, 0)), Vector((0.168, 0.38, 0)), Vector((X_DOS, 0.446, 0))]
for p in table_pts[2:]: p.z = TZ + RC
coin = Vector((X_DOS, 0.446, TZ - 0.004)); rho = RC + 0.004
arc = [coin + Vector((0, rho * math.sin(a), rho * math.cos(a))) for a in (math.pi / 2 * i / 8 for i in range(1, 9))]
pied = Vector((X_DOS + 0.03, 0.72, RC)); bord_av = Vector((FX + 0.15, FY - FDY, 0))
chute = bez(arc[-1], arc[-1] + Vector((0, 0, -0.42)), Vector((X_DOS + 0.02, 0.6, RC)), pied, 30)
au_sol = bez(pied, pied + Vector((0.005, 0.05, 0)), bord_av + Vector((0, -0.12, RC)), bord_av + Vector((0, -0.06, RC)), 10)
tube("câble propre", catmull(table_pts, 16) + arc + chute[1:] + au_sol[1:] + plongee(bord_av, Vector((0, -1, 0)), RC, 0), RC, GAINE_PROPRE, res=4)

# ---------------------------------------------------------------- les centaines de câbles
# Ils viennent des deux côtés, en nappes propres : chaque câble reste dans son plan (une tranche en y qui lui est
# propre), donc rien ne se croise. Trois façons d'arriver :
#  - par le toit : le câble court du mur latéral sous la tôle, au-dessus des fermes, puis se détache et descend en
#    chaînette jusqu'au sol ;
#  - par le mur : il part du mur latéral et descend en une longue chaînette ;
#  - par le sol : il court au sol depuis le pied du mur.
# Tous finissent au sol, passent le bord de la tranchée et y plongent. Une dizaine de câbles géants, armés comme des
# câbles sous-marins.
def chainette(Lh, h):   # paramètre a tel que a (ch(Lh / a) - 1) = h
    lo, hi = 0.01, 5000.0
    for _ in range(90):
        a = (lo * hi) ** 0.5
        if a * (math.cosh(min(Lh / a, 700)) - 1) > h: lo = a
        else: hi = a
    return a

def descente(T, d, Lh, h, r, n=48):
    # chaînette dont le point bas est T (posé au sol, tangent au sol), qui remonte de h sur Lh à l'opposé de d ;
    # points répartis le long du câble, du haut vers le bas
    a = chainette(Lh, h); s_tot = a * math.sinh(Lh / a)
    pts = []
    for i in range(n + 1):
        x = a * math.asinh((s_tot * (1 - i / n)) / a)
        pts.append(T - d * x + Vector((0, 0, a * (math.cosh(x / a) - 1))))
    return pts

INTERDIT = [(-12 + 3 * i, 0.12) for i in range(9)] + [(y, 0.3) for y in (-12, -6, 0, 6, 12)]   # fermes, poteaux
def libre(y, r): return all(abs(y - c) > m + r for c, m in INTERDIT)

Y0, Y1 = FY - FDY + 0.25, FY + FDY - 0.15
n_cables = 0
SOL_Y = []   # câbles posés au sol de bout en bout : le décor les évite
for cote in (-1, 1):   # -1 : gauche, 1 : droite
    d = Vector((-cote, 0, 0))                      # sens de marche : vers la tranchée
    rive = FX + cote * FDX                         # bord de la tranchée de ce côté
    mur = cote * (LX / 2 + 0.2)
    y = Y0
    geants = set(random.sample(range(40), 5))
    for g in range(400):
        if y > Y1: break
        geant = g in geants
        if geant: nb, r0 = 1, random.uniform(0.05, 0.085)
        else:
            nb = random.choice((3, 4, 5, 6, 8, 10, 12))
            r0 = random.uniform(0.008, 0.018) if random.random() < 0.65 else random.uniform(0.018, 0.032)
        origine = "toit" if geant or random.random() < 0.7 else random.choice(("mur", "sol"))
        mat = JAUNE if random.random() < 0.06 else random.choice(GAINES)
        posee = random.uniform(0.4, 2.2)                              # longueur posée au sol avant la tranchée
        x_haut = rive + cote * max(posee + 1.2, random.uniform(2.2, 8.5))   # où la nappe quitte le toit
        if abs(abs(x_haut) - 8) < 0.35: x_haut += cote * 0.7          # pas à travers la panne
        z_mur = random.uniform(2.6, 5.5)
        for k in range(nb):
            r = r0 * (random.uniform(0.92, 1.08) if nb > 1 else 1)
            while y <= Y1 and not libre(y + r, r): y += 0.02
            if y > Y1: break
            yk = y + r; y = yk + r * 1.04
            T = Vector((rive + cote * posee, yk, r))
            e = Vector((rive, yk, 0))
            if origine == "toit":
                z_haut = LZ - 0.195 + r                                # entre le dessus des fermes et la tôle
                Lh = abs(x_haut - T.x)
                chute = descente(T, d, Lh, z_haut - r, r)
                f = min(0.35, Lh * 0.2)                                # arrondi au point où le câble se détache
                j = next(i for i, p in enumerate(chute) if (p - chute[0]).length > f)
                coude = [Vector((x_haut + cote * f, yk, z_haut)), Vector((x_haut, yk, z_haut)), chute[j]]
                arrondi = [coude[0] * (1 - t) ** 2 + coude[1] * (2 * (1 - t) * t) + coude[2] * t * t for t in (i / 8 for i in range(9))]
                pts = [Vector((mur, yk, z_haut))] + arrondi + chute[j + 1:]
            elif origine == "mur":
                pts = descente(T, d, abs(mur - T.x), z_mur, r)
            else:
                pts = [Vector((mur, yk, r)), T]; SOL_Y.append(yk)
            pts += [T.lerp(e + Vector((0, 0, r)), i / 4) for i in range(1, 4)] + plongee(e, -d, r, 0)
            tube(f"câble {n_cables}", pts, r, mat)
            n_cables += 1
        y += 0 if random.random() < 0.35 else random.uniform(0.04, 0.35)   # écart entre deux nappes
print("câbles :", n_cables)

# ---------------------------------------------------------------- l'entrepôt
murs =[("mur gauche", 0.4, LY, LZ, (-LX / 2, 0, LZ / 2)), ("mur droit", 0.4, LY, LZ, (LX / 2, 0, LZ / 2)),
        ("mur avant", LX, 0.4, LZ, (0, -LY / 2, LZ / 2))]
for nom, a, b, c, pos in murs: boite(nom, a, b, c, pos, MUR)
# mur du fond : bas plein, puis une rangée de hautes fenêtres sur ciel gris
boite("fond bas", LX, 0.4, 3.2, (0, LY / 2, 1.6), MUR)
boite("fond haut", LX, 0.4, 1.2, (0, LY / 2, LZ - 0.6), MUR)
for i in range(9):
    x = -18 + i * 4.5
    boite(f"trumeau {i}", 1.3, 0.4, 4.6, (x, LY / 2, 3.2 + 2.3), MUR)
    for j in range(1, 4):  # meneaux des vitres
        boite(f"meneau {i}-{j}", 0.05, 0.08, 4.6, (x + 0.65 + j * 0.8, LY / 2 - 0.1, 5.5), ACIER_SALE)
    for j in range(1, 5):
        boite(f"traverse {i}-{j}", 3.2, 0.08, 0.05, (x + 2.25, LY / 2 - 0.1, 3.2 + j * 0.92), ACIER_SALE)
ciel = plaque("ciel", LX, LZ, CIEL); ciel.visible_shadow = False; ciel.rotation_euler = (math.radians(90), 0, 0); ciel.location = (0, LY / 2 + 1.5, LZ / 2)
# fenêtres hautes des murs latéraux
for cote in (-1, 1):
    ciel_l = plaque(f"ciel latéral {cote}", LY, 2.0, CIEL); ciel_l.visible_shadow = False; ciel_l.rotation_euler = (math.radians(90), 0, math.radians(90))
    ciel_l.location = (cote * (LX / 2 + 0.3), 0, 7.2)
    boite(f"jour latéral {cote}", 0.5, LY - 2, 1.6, (cote * LX / 2, 0, 7.2), None).hide_render = True
toit = plaque("toit", LX, LY, TOIT); toit.location = (0, 0, LZ); toit.rotation_euler = (math.radians(180), 0, 0)
for i in range(9):  # fermes du toit et poteaux
    y = -12 + i * 3
    boite(f"ferme {i}", LX, 0.22, 0.5, (0, y, LZ - 0.45), ACIER_SALE)
    if i % 2 == 0:
        for x in (-8, 8): boite(f"poteau {i} {x}", 0.32, 0.32, LZ, (x, y, LZ / 2), ACIER_SALE)
for x in range(-16, 17, 8): boite(f"panne {x}", 0.16, LY, 0.3, (x, 0, LZ - 0.8), ACIER_SALE)
# un trou dans le toit, au fond : la lumière et le filet d'eau passent par là
trou_toit = plaque("trou du toit", 1.4, 1.0, CIEL); trou_toit.visible_shadow = False; trou_toit.location = (3.2, 13.3, LZ + 0.05); trou_toit.rotation_euler = (math.radians(180), 0, 0)

# ---------------------------------------------------------------- la table
table = pave("plateau", 1.5, 0.8, 0.04, 0.01, 0.004, BOIS, None, 4, 2); table.location = (0.1, 0.05, TZ - 0.02)
for sx in (-1, 1):
    for sy in (-1, 1):
        boite(f"pied {sx}{sy}", 0.05, 0.05, TZ - 0.04, (0.1 + sx * 0.68, 0.05 + sy * 0.33, (TZ - 0.04) / 2), BOIS)
boite("ceinture", 1.4, 0.7, 0.08, (0.1, 0.05, TZ - 0.08), BOIS)

# ---------------------------------------------------------------- le filet d'eau de pluie et sa flaque
def eau():
    m, n, l, b = nouveau("eau")
    b.inputs["Base Color"].default_value = (0.85, 0.9, 0.95, 1); b.inputs["Roughness"].default_value = 0.05
    b.inputs["Transmission Weight"].default_value = 1.0; b.inputs["IOR"].default_value = 1.33
    b.inputs["Emission Color"].default_value = (*lin("#CFD8E0"), 1); b.inputs["Emission Strength"].default_value = 0.6
    coord = n.new("ShaderNodeTexCoord"); mp = n.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (6, 6, 0.8)
    l.new(coord.outputs["Object"], mp.inputs["Vector"])
    bruit = n.new("ShaderNodeTexNoise"); bruit.inputs["Scale"].default_value = 8; bruit.inputs["Detail"].default_value = 2
    l.new(mp.outputs["Vector"], bruit.inputs["Vector"])
    for f, z in ((1, 0.0), (FIN, 30.0)):  # le motif descend : l'eau tombe
        mp.inputs["Location"].default_value = (0, 0, z); mp.inputs["Location"].keyframe_insert("default_value", frame=f)
    r = n.new("ShaderNodeMapRange"); r.inputs["From Min"].default_value = 0.42; r.inputs["From Max"].default_value = 0.6
    l.new(bruit.outputs["Fac"], r.inputs["Value"]); l.new(r.outputs["Result"], b.inputs["Alpha"])
    return m, mp
EAU, EAU_MP = eau()
filet = bouton("filet d'eau", 0.012, LZ, EAU, None, 0, seg=12); filet.location = (3.2, 13.3, LZ / 2)
flaque = bouton("flaque", 1.1, 0.004, principled("eau calme", "#0E1012", 0, 0.02), None, 0, seg=48)
flaque.location = (3.2, 13.3, 0.002); flaque.scale = (1.0, 0.7, 1.0)

# poussière en suspension, près de la table : de petites particules qui dérivent lentement
POUSS, _ = emissif("poussière", "#E8E6E0", 1.2)
for i in range(160):
    bm = bmesh.new(); bmesh.ops.create_icosphere(bm, subdivisions=1, radius=random.uniform(0.0006, 0.0018))
    me = bpy.data.meshes.new(f"grain {i}"); bm.to_mesh(me); bm.free()
    g = objet(f"grain {i}", me, POUSS)
    p0 = Vector((random.uniform(-1.2, 1.2), random.uniform(-1.6, 1.0), random.uniform(0.7, 2.4)))
    g.location = p0; g.keyframe_insert("location", frame=1)
    g.location = p0 + Vector((random.uniform(-0.08, 0.08), random.uniform(-0.05, 0.05), random.uniform(-0.12, 0.02))); g.keyframe_insert("location", frame=FIN)
    for fc in g.animation_data.action.fcurves:
        for k in fc.keyframe_points: k.interpolation = "LINEAR"

# ---------------------------------------------------------------- ce qu'on laisse dans un entrepôt abandonné
# Fûts rouillés (debout, couchés), palettes empilées, caisses, tuyauterie le long du mur du fond, une chaise près de
# la table, planches et gravats au sol. Rien entre les nappes de câbles au sol : le décor est devant et au fond.
ROUILLE = bruite("rouille", "#4A2E1C", "#8A5632", 4.0, rugo=(0.55, 0.9), relief=0.3, metal=0.5)
FUTS = [bruite("fût bleu", "#2B4058", "#6A4428", 2.5, rugo=(0.4, 0.8), relief=0.2, metal=0.5),
        bruite("fût rouge", "#5E2620", "#6E4A2E", 2.5, rugo=(0.4, 0.8), relief=0.2, metal=0.5),
        bruite("fût gris", "#4C4E4C", "#6E5034", 2.5, rugo=(0.4, 0.8), relief=0.2, metal=0.5), ROUILLE]
BOIS_VIEUX = bruite("bois vieux", "#5E4E3A", "#9A8B70", 3.0, rugo=(0.7, 0.95), relief=0.25)
GRAVATS = bruite("gravats", "#4A4945", "#7A7870", 6.0, relief=0.4)

def libre_au_sol(x, y, m):   # hors du couloir de la caméra, de la table, de la tranchée et des câbles posés au sol
    if (-0.8 - m < x < 2.0 + m) and y < 0.8 + m: return False
    if abs(x - FX) < FDX + 2.6 + m and FY - FDY - 0.3 - m < y < FY + FDY + 0.3 + m: return False
    return all(abs(y - ys) > m + 0.05 for ys in SOL_Y)

def groupe(nom, x, y, rz, z=0.0, rx=0.0):
    g = bpy.data.objects.new(nom, None); sc.collection.objects.link(g)
    g.location = (x, y, z); g.rotation_euler = (rx, 0, rz)
    return g

def piece(nom, lx, ly, lz, pos, mat, parent):
    ob = boite(nom, lx, ly, lz, pos, mat); ob.parent = parent
    return ob

def fut(nom, x, y, couche=False):
    mat = random.choice(FUTS)
    g = groupe(nom, x, y, random.uniform(0, 6.28), 0.29 if couche else 0.0, math.radians(90) if couche else 0.0)
    corps = bouton(nom + " corps", 0.285, 0.88, mat, g, 0.012, seg=40); corps.location = (0, 0, 0.44 if not couche else 0)
    for dz in (-0.25, 0.0, 0.25, 0.43, -0.43):
        c = bouton(nom + f" cercle {dz}", 0.293, 0.025, mat, g, 0.004, seg=40)
        c.location = (0, 0, (0.44 if not couche else 0) + dz)

def palette(nom, x, y, rz, z=0.0):
    g = groupe(nom, x, y, rz, z)
    for i in range(5): piece(f"{nom} dessus {i}", 1.2, 0.1, 0.022, (0, -0.35 + i * 0.175, 0.133), BOIS_VIEUX, g)
    for i in range(3): piece(f"{nom} bloc {i}", 1.2, 0.1, 0.078, (0, -0.35 + i * 0.35, 0.083), BOIS_VIEUX, g)
    for i in range(3): piece(f"{nom} dessous {i}", 1.2, 0.1, 0.022, (0, -0.35 + i * 0.35, 0.011), BOIS_VIEUX, g)

def pile_palettes(nom, x, y):
    rz = random.uniform(-0.3, 0.3)
    for k in range(random.randint(1, 5)):
        palette(f"{nom} {k}", x + random.uniform(-0.04, 0.04), y + random.uniform(-0.04, 0.04), rz + random.uniform(-0.06, 0.06), k * 0.146)

def caisse(nom, x, y, z=0.0, c=None):
    c = c or random.uniform(0.5, 0.9)
    ob = pave(nom, c, c * random.uniform(0.8, 1.0), c * 0.8, 0.01, 0.006, BOIS_VIEUX, None, 3, 2)
    ob.location = (x, y, z + c * 0.4); ob.rotation_euler.z = random.uniform(0, 6.28)
    return c

def chaise(nom, x, y, rz):
    g = groupe(nom, x, y, rz)
    piece(nom + " assise", 0.42, 0.42, 0.03, (0, 0, 0.45), BOIS_VIEUX, g)
    for sx in (-1, 1):
        for sy in (-1, 1): piece(nom + f" pied {sx}{sy}", 0.03, 0.03, 0.45, (sx * 0.19, sy * 0.19, 0.225), BOIS_VIEUX, g)
        piece(nom + f" montant {sx}", 0.03, 0.03, 0.45, (sx * 0.19, 0.19, 0.69), BOIS_VIEUX, g)
    for dz in (0.62, 0.82): piece(nom + f" barreau {dz}", 0.4, 0.025, 0.06, (0, 0.19, dz), BOIS_VIEUX, g)

def poser(nb, zone, fabrique, marge):
    n = 0
    for _ in range(nb * 30):
        if n >= nb: break
        x, y = random.uniform(*zone[0]), random.uniform(*zone[1])
        if libre_au_sol(x, y, marge): fabrique(x, y); n += 1

AVANT_G, AVANT_D, FOND_Z = ((-7, -1.6), (-9, 0.4)), ((2.8, 8), (-9, 0.4)), ((-17, 17), (11.9, 14.2))
PRES_G, PRES_D = ((-3.4, -1.4), (-7.5, 0.4)), ((2.4, 4.4), (-7.5, 0.4))   # au bord du cadre, sur le trajet de la caméra
for zone in (AVANT_G, AVANT_D, FOND_Z, PRES_G, PRES_D):
    poser(3, zone, lambda x, y: [fut(f"fût {x:.1f}", x + dx, y + dy) for dx, dy in ((0, 0), (0.6, 0.1), (0.3, 0.55))[:random.randint(1, 3)]], 1.0)
    poser(2, zone, lambda x, y: fut(f"fût couché {x:.1f}", x, y, True), 0.7)
    poser(2, zone, lambda x, y: pile_palettes(f"palettes {x:.1f}", x, y), 1.0)
    poser(2, zone, lambda x, y: caisse(f"caisse {x:.1f}", x, y), 0.6)
poser(3, FOND_Z, lambda x, y: [caisse(f"caisses {x:.1f}", x, y, c=0.8), caisse(f"caisse dessus {x:.1f}", x, y, 0.64, 0.6)], 0.7)
chaise("chaise", -0.95, -0.15, math.radians(200))

# tuyauterie le long du mur du fond, sous les fenêtres, qui redescend dans le sol aux deux bouts ; descentes d'eau
for i, (z, r) in enumerate(((2.75, 0.09), (2.45, 0.05), (2.25, 0.035))):
    yw = LY / 2 - 0.2 - r - 0.08
    x0, x1 = -17.5 + i * 0.4, 17.5 - i * 0.4
    tube(f"tuyau {i}", [Vector((x0, yw, 0)), Vector((x0, yw, z - 0.3)), Vector((x0 + 0.3, yw, z)), Vector((x1 - 0.3, yw, z)),
                        Vector((x1, yw, z - 0.3)), Vector((x1, yw, 0))], r, ROUILLE, res=3)
    for x in range(-16, 17, 2):   # colliers de fixation
        coll = bouton(f"collier {i} {x}", r * 1.25, 0.04, ACIER_SALE, None, 0.004, seg=16)
        coll.rotation_euler = (0, math.radians(90), 0); coll.location = (x + 0.3 * i, yw, z)
for x in (-13.5, -4.5, 4.5, 13.5):
    tube(f"descente {x}", [Vector((x, LY / 2 - 0.3, LZ - 0.6)), Vector((x, LY / 2 - 0.3, 0.3)), Vector((x, LY / 2 - 0.55, 0.05))], 0.06, ROUILLE, res=2)

# planches et gravats au sol
for i in range(40):
    x, y = random.uniform(-12, 12), random.uniform(-9, 14)
    if not libre_au_sol(x, y, 0.5): continue
    pl = boite(f"planche {i}", random.uniform(0.6, 1.8), random.uniform(0.08, 0.16), 0.022, (x, y, 0.011), BOIS_VIEUX)
    pl.rotation_euler.z = random.uniform(0, 6.28)
for i in range(160):
    x, y = random.uniform(-15, 15), random.uniform(-10, 14.3)
    if not libre_au_sol(x, y, 0.1): continue
    bm = bmesh.new(); bmesh.ops.create_icosphere(bm, subdivisions=1, radius=1.0)
    s = random.uniform(0.03, 0.14)
    for v in bm.verts: v.co *= s * random.uniform(0.7, 1.3); v.co.z *= 0.55
    me = bpy.data.meshes.new(f"gravat {i}"); bm.to_mesh(me); bm.free()
    g = objet(f"gravat {i}", me, GRAVATS); g.location = (x, y, s * 0.25); g.rotation_euler.z = random.uniform(0, 6.28)

# moisissure sur les murs : coulures sombres verdâtres qui descendent des fenêtres et du toit
def moisir(m, couleur, echelle):
    n, l = m.node_tree.nodes, m.node_tree.links
    b = n["Principled BSDF"]; lien = b.inputs["Base Color"].links[0]; src = lien.from_socket
    coord = n.new("ShaderNodeTexCoord"); mp = n.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (echelle, echelle, echelle * 0.12)
    l.new(coord.outputs["Object"], mp.inputs["Vector"])
    br = n.new("ShaderNodeTexNoise"); br.inputs["Scale"].default_value = 1.0; br.inputs["Detail"].default_value = 6
    l.new(mp.outputs["Vector"], br.inputs["Vector"])
    mr = n.new("ShaderNodeMapRange"); mr.inputs["From Min"].default_value = 0.5; mr.inputs["From Max"].default_value = 0.7
    l.new(br.outputs["Fac"], mr.inputs["Value"])
    mx = n.new("ShaderNodeMix"); mx.data_type = "RGBA"
    l.new(mr.outputs["Result"], mx.inputs[0]); l.new(src, mx.inputs[6]); mx.inputs[7].default_value = (*lin(couleur), 1)
    l.remove(lien); l.new(mx.outputs[2], b.inputs["Base Color"])
moisir(MUR, "#252B1E", 3.0)
moisir(TOIT, "#1A1D16", 2.0)

# poussière dans l'air, sur tout le trajet de la caméra
for i in range(420):
    bm = bmesh.new(); bmesh.ops.create_icosphere(bm, subdivisions=1, radius=random.uniform(0.0008, 0.0025))
    me = bpy.data.meshes.new(f"poussière {i}"); bm.to_mesh(me); bm.free()
    g = objet(f"poussière {i}", me, POUSS)
    p0 = Vector((random.uniform(-2.5, 3.0), random.uniform(-9.0, 2.0), random.uniform(0.1, 3.5)))
    g.location = p0; g.keyframe_insert("location", frame=1)
    g.location = p0 + Vector((random.uniform(-0.12, 0.12), random.uniform(-0.08, 0.08), random.uniform(-0.15, 0.03))); g.keyframe_insert("location", frame=FIN)
    for fc in g.animation_data.action.fcurves:
        for k in fc.keyframe_points: k.interpolation = "LINEAR"

# ---------------------------------------------------------------- la verdure : la nature a repris l'entrepôt
# Touffes d'herbe dans les fissures du béton (au pied des murs, au premier plan, au pied de la table), lierre qui pend
# devant les fenêtres du fond et sous les fermes, et qui grimpe le long des trumeaux.
def mat_herbe():
    m, n, l, b = nouveau("herbe")
    info = n.new("ShaderNodeHairInfo"); rampe = n.new("ShaderNodeValToRGB"); e = rampe.color_ramp.elements
    e[0].color = (*lin("#3F5A22"), 1); e[1].color = (*lin("#8C8F48"), 1)
    l.new(info.outputs["Random"], rampe.inputs["Fac"]); l.new(rampe.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.55
    return m
HERBE = mat_herbe()

def reglages_herbe(nom, longueur, densite):
    st = bpy.data.particles.new(nom)
    st.type = "HAIR"; st.hair_length = longueur; st.use_advanced_hair = False
    st.emit_from = "FACE"; st.distribution = "RAND"; st.use_emit_random = True
    st.render_type = "PATH"
    st.child_type = "INTERPOLATED"; st.child_percent = 4; st.rendered_child_count = int(os.environ.get("BRINS", "8"))
    st.child_length = 0.35; st.child_length_threshold = 0.55
    st.roughness_endpoint = 0.35 * longueur; st.roughness_2 = 0.01; st.roughness_1 = 0.01; st.child_radius = 0.06; st.clump_factor = 0.4
    st.root_radius = 1.0; st.tip_radius = 0.0; st.radius_scale = 0.0025; st.use_close_tip = True
    st.material = 1; st.display_step = 2; st.render_step = 3
    st["densite"] = densite
    return st
HERBE_RASE, HERBE_HAUTE = reglages_herbe("herbe rase", 0.12, 320), reglages_herbe("herbe haute", 0.38, 140)

def touffe(nom, cx, cy, rx, ry, reglages):
    bm = bmesh.new(); bmesh.ops.create_circle(bm, cap_ends=True, segments=14, radius=1.0)
    for v in bm.verts:
        k = random.uniform(0.75, 1.15)   # contour irrégulier
        v.co.x = cx + v.co.x * rx * k; v.co.y = cy + v.co.y * ry * k; v.co.z = 0.002
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    ob = objet(nom, me, HERBE); ob.show_instancer_for_render = False   # on ne rend que les brins
    ps = ob.modifiers.new("herbe", "PARTICLE_SYSTEM").particle_system
    ps.settings = reglages.copy(); ps.seed = random.randint(0, 9999)
    ps.settings.count = max(20, int(math.pi * rx * ry * reglages["densite"]))
    return ob

def dans_le_passage(x, y, m):   # couloir de la caméra, table, tranchée
    return ((-0.6 - m < x < 1.8 + m) and y < 0.6 + m) or (abs(x - FX) < FDX + 2.4 + m and FY - FDY - 0.3 - m < y < FY + FDY + 0.3 + m)

semer = touffe
for i in range(26):   # au pied du mur du fond, sous les fenêtres : herbes hautes
    semer(f"touffe fond {i}", random.uniform(-18, 18), LY / 2 - 0.2 - random.uniform(0.2, 0.7), random.uniform(0.4, 1.4), random.uniform(0.2, 0.5), HERBE_HAUTE)
for i in range(70):   # dans les fissures du sol
    x, y = random.uniform(-14, 14), random.uniform(-10, 13)
    rx = random.uniform(0.12, 0.6)
    if dans_le_passage(x, y, rx): continue
    semer(f"touffe {i}", x, y, rx, rx * random.uniform(0.3, 0.8), HERBE_HAUTE if random.random() < 0.25 else HERBE_RASE)
for i, (x, y, rx) in enumerate(((-1.5, -8.6, 0.5), (2.6, -7.9, 0.45), (-1.1, -6.2, 0.35), (2.4, -5.0, 0.4), (-1.6, -3.2, 0.3), (2.3, -2.4, 0.3))):
    semer(f"touffe premier plan {i}", x, y, rx, rx * 0.6, HERBE_RASE)   # au premier plan, flou au début du plan
for sx in (-1, 1):
    for sy in (-1, 1):
        semer(f"touffe pied {sx}{sy}", 0.1 + sx * 0.7, 0.05 + sy * 0.35, 0.09, 0.07, HERBE_RASE)

# lierre : une tige et des feuilles, toutes les feuilles dans un seul objet
def mat_feuille():
    m, n, l, b = nouveau("feuille")
    coord = n.new("ShaderNodeTexCoord"); bruit = n.new("ShaderNodeTexNoise"); bruit.inputs["Scale"].default_value = 3.0
    l.new(coord.outputs["Object"], bruit.inputs["Vector"])
    rampe = n.new("ShaderNodeValToRGB"); e = rampe.color_ramp.elements
    e[0].color = (*lin("#3C5E22"), 1); e[1].color = (*lin("#86A444"), 1)
    l.new(bruit.outputs["Fac"], rampe.inputs["Fac"]); l.new(rampe.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.45
    tr = n.new("ShaderNodeBsdfTranslucent"); l.new(rampe.outputs["Color"], tr.inputs["Color"])
    mx = n.new("ShaderNodeMixShader"); mx.inputs[0].default_value = 0.3
    sortie = n["Material Output"]
    l.new(b.outputs[0], mx.inputs[1]); l.new(tr.outputs[0], mx.inputs[2]); l.new(mx.outputs[0], sortie.inputs["Surface"])
    return m
FEUILLE = mat_feuille()
TIGE = principled("tige", "#3B3524", 0, 0.7)
bm_f = bmesh.new()
def liane(nom, depart, longueur, sens, mur_y=None):
    # sens : 1 pour une liane qui grimpe, -1 pour une liane qui pend
    pts, p = [], depart.copy()
    pas = 0.05; ph = random.uniform(0, 6.28)
    for i in range(int(longueur / pas) + 1):
        pts.append(p.copy())
        p += Vector((0.012 * math.sin(ph + i * 0.35), 0, sens * pas))
        if mur_y is None: p.y += 0.008 * math.cos(ph + i * 0.27)
    tube(nom, pts, 0.004, TIGE, res=1)
    for i, q in enumerate(pts):
        for _ in range(2 if random.random() < 0.6 else 1):
            if random.random() < 0.1: continue
            lg = random.uniform(0.06, 0.12) * (0.6 + 0.4 * min(1, i / 6))
            phi = random.uniform(0, 2 * math.pi)
            a = Vector((math.cos(phi), math.sin(phi), 0)) * 0.8 + Vector((0, 0, -0.45))
            if mur_y is not None and a.y > 0: a.y = -a.y    # côté pièce, pas dans le mur
            a.normalize()
            b_ = a.cross(Vector((0, 0, 1)))
            b_ = b_.normalized() if b_.length > 1e-4 else Vector((1, 0, 0))
            nrm = a.cross(b_).normalized()
            w = lg * 0.75
            vs = [q, q + a * (lg * 0.45) + b_ * (w / 2) + nrm * (lg * 0.08), q + a * lg, q + a * (lg * 0.45) - b_ * (w / 2) + nrm * (lg * 0.08)]
            bm_f.faces.new([bm_f.verts.new(v) for v in vs])
for i in range(18):   # devant les fenêtres du fond, du haut des fenêtres vers le bas
    liane(f"lierre fenêtre {i}", Vector((random.uniform(-18, 18), LY / 2 - 0.28, LZ - 1.2)), random.uniform(1.0, 4.2), -1, LY / 2 - 0.2)
for i in range(9):    # qui grimpe le long des trumeaux
    x = -18 + random.randrange(9) * 4.5 + random.uniform(-0.5, 0.5)
    liane(f"lierre trumeau {i}", Vector((x, LY / 2 - 0.26, 0.0)), random.uniform(1.5, 5.0), 1, LY / 2 - 0.2)
for i in range(12):   # qui pend sous les fermes, entre les nappes de câbles
    liane(f"lierre ferme {i}", Vector((random.uniform(-6, 6), random.choice((3, 6, 9)), LZ - 0.72)), random.uniform(1.0, 3.8), -1)
me = bpy.data.meshes.new("feuilles"); bm_f.to_mesh(me); bm_f.free()
lisser(objet("feuilles", me, FEUILLE))

# ---------------------------------------------------------------- lumière : ciel gris, air poussiéreux
w = bpy.data.worlds.new("monde"); sc.world = w; w.use_nodes = True
wn = w.node_tree.nodes
wn["Background"].inputs["Color"].default_value = (*lin("#8E979C"), 1); wn["Background"].inputs["Strength"].default_value = 0.2
vol = wn.new("ShaderNodeVolumePrincipled"); vol.inputs["Density"].default_value = float(os.environ.get("BRUME", "0.012"))
vol.inputs["Color"].default_value = (*lin("#C9CED3"), 1); vol.inputs["Anisotropy"].default_value = 0.6
w.node_tree.links.new(vol.outputs[0], wn["World Output"].inputs["Volume"])

def lampe(nom, typ, pos, puissance, couleur, cible=None, taille=1.0, rot=None):
    l = bpy.data.lights.new(nom, typ); l.energy = puissance; l.color = couleur
    if typ == "AREA": l.shape = "RECTANGLE"; l.size = taille; l.size_y = taille * 0.6
    if typ == "SPOT": l.spot_size = math.radians(taille); l.spot_blend = 0.6
    ob = bpy.data.objects.new(nom, l); sc.collection.objects.link(ob); ob.location = pos
    if rot: ob.rotation_euler = rot
    if cible is not None:
        v = bpy.data.objects.new(nom + " visée", None); sc.collection.objects.link(v); v.location = cible
        c = ob.constraints.new("TRACK_TO"); c.target = v; c.track_axis = "TRACK_NEGATIVE_Z"; c.up_axis = "UP_Y"
    return ob
GRIS = lin("#D5DCE2")
# le jour gris qui entre par les fenêtres du fond, rasant, et fait les rayons dans l'air
soleil = lampe("jour", "SUN", (0, 20, 10), 6.0, lin("#FFE2BC"), rot=(math.radians(62), 0, math.radians(180 + 18)))
soleil.data.angle = math.radians(8)
lampe("fenêtres fond", "AREA", (0, 13.5, 5.5), 1800, GRIS, cible=(0, 0, 1), taille=30)
lampe("fenêtres côté", "AREA", (-18.5, 0, 7.2), 700, GRIS, cible=(0, 0, 1), taille=20)
lampe("puits de jour", "SPOT", (3.2, 13.3, 8.9), 2500, GRIS, cible=(3.2, 13.3, 0), taille=18)
# un peu de jour sur la table et le module, venu d'une verrière au-dessus
lampe("verrière", "AREA", (-1.2, 1.5, 8.5), 900, GRIS, cible=(0.05, 0.05, TZ), taille=2.5)
lampe("reflet appareil", "AREA", (-0.6, 0.9, 1.6), 18, GRIS, cible=(0.02, 0, TZ), taille=0.8)

# le témoin vert et l'éclairage de lecture de l'écran s'allument au réveil
def clef(prise_n, frame, valeur):
    prise_n.default_value = valeur; prise_n.keyframe_insert("default_value", frame=frame)
A = ALLUMAGE
for f, v in ((1, 0.0), (A - 6, 0.0), (A - 5, 40.0), (A - 3, 0.0), (A - 1, 40.0), (A + 60, 25.0), (A + 90, 6.0), (FIN, 6.0)):
    clef(DEL_B.inputs["Emission Strength"], f, v)
for f, v in ((1, 0.0), (A, 0.0), (A + 8, 0.35), (FIN, 0.35)):
    clef(ENCRE_B.inputs["Emission Strength"], f, v)
lueur = lampe("lueur témoin", "POINT", P.matrix_world @ Vector((38.5 * MM, 18 * MM, H)), 0.0, lin("#5CFF8A"))
lueur.data.shadow_soft_size = 0.002
for f, v in ((1, 0.0), (A - 6, 0.0), (A - 5, 0.12), (A - 3, 0.0), (A - 1, 0.12), (A + 90, 0.03), (FIN, 0.03)):
    lueur.data.energy = v; lueur.data.keyframe_insert("energy", frame=f)

# ---------------------------------------------------------------- caméra : un seul plan
# Plan large au ras du sol, de loin : la table, minuscule, et les câbles qui tombent de partout derrière elle. On avance
# au ras du sol, on monte vers le plateau quand le Phenix se réveille, puis on s'approche jusqu'à lire son écran.
cam_d = bpy.data.cameras.new("caméra"); cam_d.sensor_fit = "VERTICAL"; cam_d.sensor_height = 36
cam_d.dof.use_dof = True; cam_d.clip_start = 0.01; cam_d.clip_end = 200
cam = bpy.data.objects.new("caméra", cam_d); sc.collection.objects.link(cam); sc.camera = cam
point = bpy.data.objects.new("visée", None); sc.collection.objects.link(point)
cam_d.dof.focus_object = point
c = cam.constraints.new("TRACK_TO"); c.target = point; c.track_axis = "TRACK_NEGATIVE_Z"; c.up_axis = "UP_Y"
ECRAN = P.matrix_world @ Vector((-15 * MM, 1.0 * MM, H / 2 + 0.6 * MM))
def depuis(cible, az, el, d):
    az, el = math.radians(az), math.radians(el)
    return cible + d * Vector((math.sin(az) * math.cos(el), -math.cos(az) * math.cos(el), math.sin(el)))
# (image, position caméra, visée, focale, ouverture)
CLES = [
    (1,   Vector((0.75, -9.6, 0.26)), Vector((0.15, 0.6, 3.7)), 22, 8.0),
    (120, Vector((0.6, -4.4, 0.34)), Vector((0.12, 0.5, 2.0)), 24, 5.6),
    (220, Vector((0.38, -1.35, 1.12)), Vector((0.05, 0.05, 0.86)), 32, 4.0),
    (300, depuis(ECRAN, -10, 38, 0.62), ECRAN, 40, 3.2),
    (FIN, depuis(ECRAN, -4, 50, 0.215), ECRAN + Vector((0, 0.002, 0)), 50, 4.5),
]
for f, pos, vis, foc, ouv in CLES:
    cam.location = pos; cam.keyframe_insert("location", frame=f)
    point.location = vis; point.keyframe_insert("location", frame=f)
    cam_d.lens = foc; cam_d.keyframe_insert("lens", frame=f)
    cam_d.dof.aperture_fstop = ouv; cam_d.dof.keyframe_insert("aperture_fstop", frame=f)
for ad in (cam.animation_data, point.animation_data, cam_d.animation_data):
    for fc in ad.action.fcurves:
        for k in fc.keyframe_points: k.interpolation = "BEZIER"; k.handle_left_type = k.handle_right_type = "AUTO_CLAMPED"
        fc.update()

# ---------------------------------------------------------------- rendu
sc.render.engine = "BLENDER_EEVEE_NEXT"
ee = sc.eevee
ee.taa_render_samples = int(os.environ.get("ECHANTILLONS", "48"))
ee.use_raytracing = True
ee.ray_tracing_options.resolution_scale = os.environ.get("RT_RES", "2")
ee.shadow_ray_count = 1; ee.shadow_step_count = 6
ee.volumetric_tile_size = os.environ.get("VOL_TUILE", "8")
ee.volumetric_samples = int(os.environ.get("VOL_ECH", "64"))
ee.volumetric_end = 60
ee.use_volumetric_shadows = True
if os.environ.get("MOTEUR") == "cycles":
    sc.render.engine = "CYCLES"
    prefs = bpy.context.preferences.addons["cycles"].preferences
    prefs.compute_device_type = "CUDA"; prefs.get_devices()
    for dev in prefs.devices: dev.use = dev.type == "CUDA"
    cy = sc.cycles; cy.device = "GPU"
    cy.samples = int(os.environ.get("ECHANTILLONS", "128")); cy.use_denoising = True; cy.denoiser = "OPENIMAGEDENOISE"
    cy.max_bounces = 6; cy.volume_bounces = 1; cy.volume_step_rate = 4.0
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920
sc.render.resolution_percentage = POURCENT
sc.view_settings.view_transform = "AgX"
try: sc.view_settings.look = "AgX - Base Contrast"
except Exception: pass
sc.view_settings.exposure = float(os.environ.get("EXPO", "0.55"))
sc.render.image_settings.file_format = "JPEG"; sc.render.image_settings.quality = 93

if MODE == "test":
    for f in [int(x) for x in (args[2] if len(args) > 2 else "1").split(",")]:
        sc.frame_set(f)
        sc.render.filepath = os.path.join(ICI, f"ent-{f:04d}.jpg")
        bpy.ops.render.render(write_still=True)
elif MODE == "blend":
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(ICI, "entrepot.blend"))
else:
    sortie = os.path.join(ICI, "rushes")
    os.makedirs(sortie, exist_ok=True)
    sc.render.filepath = os.path.join(sortie, "f#####")
    sc.render.use_overwrite = False
    bpy.ops.render.render(animation=True)
