# Story « l'entrepôt » : un entrepôt abandonné, gris, poussiéreux ; des centaines de câbles (électricité, réseau, câbles
# sous-marins) arrivent de partout vers un petit module suspendu, et de là un seul câble propre descend vers un Phenix 001
# intact posé sur une table ordinaire. Au fond, un filet d'eau de pluie tombe du toit. Quand la caméra s'approche, le Phenix
# s'allume : démarrage, puis les compteurs de fiches et de cartes du monde entier montent.
# Plan unique de 15 s, 1080 × 1920. Concept : l'appareil est un prototype en conception.
# Usage : blender -b -P entrepot.py -- test <pourcentage> <image,image,...>   (3d/ent-NNNN.jpg)
#         blender -b -P entrepot.py -- anim <pourcentage>                     (video/rushes-entrepot/fNNNNN.jpg)
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
    masque = n.new("ShaderNodeMapRange"); masque.inputs["From Min"].default_value = 0.6; masque.inputs["From Max"].default_value = 0.64
    l.new(flaque.outputs["Fac"], masque.inputs["Value"])
    mouille = n.new("ShaderNodeMix"); mouille.data_type = "RGBA"
    l.new(masque.outputs["Result"], mouille.inputs[0]); l.new(rampe.outputs["Color"], mouille.inputs[6])
    mouille.inputs[7].default_value = (*lin("#1A1B1C"), 1)
    l.new(mouille.outputs[2], b.inputs["Base Color"])
    rg = n.new("ShaderNodeMapRange"); rg.inputs["To Min"].default_value = 0.72; rg.inputs["To Max"].default_value = 0.95
    l.new(grain.outputs["Fac"], rg.inputs["Value"])
    rf = n.new("ShaderNodeMix"); rf.data_type = "FLOAT"
    l.new(masque.outputs["Result"], rf.inputs[0]); l.new(rg.outputs["Result"], rf.inputs[2]); rf.inputs[3].default_value = 0.04
    l.new(rf.outputs[0], b.inputs["Roughness"])
    bp = n.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.25
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

def courbe(nom, pts, rayon, mat, res=12, tangente0=None):
    cu = bpy.data.curves.new(nom, "CURVE"); cu.dimensions = "3D"
    cu.bevel_depth = rayon; cu.bevel_resolution = 4 if rayon > 0.01 else 3; cu.resolution_u = res
    cu.use_fill_caps = True
    sp = cu.splines.new("BEZIER"); sp.bezier_points.add(len(pts) - 1)
    for bp, co in zip(sp.bezier_points, pts):
        bp.co = co; bp.handle_left_type = bp.handle_right_type = "AUTO"
    if tangente0 is not None:
        b0 = sp.bezier_points[0]; b0.handle_left_type = b0.handle_right_type = "FREE"
        d = (Vector(pts[1]) - Vector(pts[0])).length * 0.5
        b0.handle_right = Vector(pts[0]) + tangente0 * d; b0.handle_left = Vector(pts[0]) - tangente0 * d
    return objet(nom, cu, mat)

# ---------------------------------------------------------------- le module suspendu et le câble propre
HUB = Vector((0.05, 0.35, 3.1))
module = pave("module", 0.46, 0.46, 0.62, 0.05, 0.02, MODULE); module.location = HUB
for i, dz in enumerate((-0.2, 0.0, 0.2)):
    bague = pave(f"bague {i}", 0.5, 0.5, 0.035, 0.06, 0.004, ACIER_SALE); bague.location = HUB + Vector((0, 0, dz))
temoin_hub = bouton("témoin module", 0.012, 0.01, DEL, None, 0.003); temoin_hub.rotation_euler = (math.radians(90), 0, 0)
temoin_hub.location = HUB + Vector((0.12, -0.232, -0.12))
presse = bouton("presse-étoupe", 0.028, 0.06, NICKEL, None, 0.004); presse.location = HUB + Vector((0, 0, -0.34))
RC = 2.0 * MM
dessus = Vector((0.13, 0.13, TZ + RC))
pts = [SORTIE, SORTIE + DIR * 0.045 + Vector((0, 0, RC * 0.3 - (SORTIE.z - TZ - RC))),
       Vector((0.10, -0.05, TZ + RC)), Vector((0.12, 0.07, TZ + RC)), dessus + Vector((0, 0.03, 0.02)),
       Vector((0.12, 0.24, TZ + 0.55)), Vector((0.08, 0.33, 1.9)), HUB + Vector((0, 0, -0.38))]
pts[1].z = TZ + RC
courbe("câble propre", pts, RC, GAINE_PROPRE, res=24, tangente0=DIR)

# ---------------------------------------------------------------- les centaines de câbles
# Des faisceaux arrivent de toutes les directions : des murs, des poutres du toit, du sol au loin. Chaque faisceau
# compte 1 à 8 câbles côte à côte ; une douzaine sont des câbles géants, armés comme des câbles sous-marins.
def depart():
    zone = random.random()
    if zone < 0.55:   # murs
        cote = random.choice(("g", "d", "f", "a"))
        if cote in ("g", "d"): return Vector((-19.8 if cote == "g" else 19.8, random.uniform(-13, 13), random.uniform(3.5, 8.6)))
        return Vector((random.uniform(-18, 18), 14.8 if cote == "f" else -14.8, random.uniform(3.5, 8.6)))
    if zone < 0.9:    # toit
        a = random.uniform(0, 2 * math.pi); r = random.uniform(5, 18)
        return Vector((math.cos(a) * r, math.sin(a) * r * 0.8, 8.9))
    a = random.uniform(0, 2 * math.pi); r = random.uniform(9, 16)   # sol, au loin
    return Vector((math.cos(a) * r, math.sin(a) * r * 0.8, 0.0))
n_cables = 0
for fx in range(52):
    S = depart()
    geant = fx < 12
    nb = 1 if geant else random.choice((1, 2, 3, 3, 4, 5, 6, 8))
    arrivee = HUB + Vector((random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), random.uniform(0.12, 0.31)))
    lateral = (arrivee - S).cross(Vector((0, 0, 1)))
    lateral = lateral.normalized() if lateral.length > 1e-6 else Vector((1, 0, 0))
    long = (arrivee - S).length
    fleche_v = random.uniform(0.08, 0.2) * long if S.z > 1 else 0.0
    for k in range(nb):
        r = random.uniform(0.07, 0.13) if geant else random.uniform(0.012, 0.045)
        dec = lateral * (k - nb / 2) * r * 2.3 + Vector((0, 0, random.uniform(-0.03, 0.03)))
        s = S + dec
        milieu = (s + arrivee) / 2 + dec * 0.6
        milieu.z = max(3.4, min(s.z, arrivee.z) - fleche_v + random.uniform(-0.2, 0.2)) if S.z > 1 else 0.05 + r
        if S.z <= 1:  # câble qui court au sol puis remonte vers le module
            pied = arrivee + (s - arrivee).normalized() * 2.5; pied.z = r
            chemin = [s + Vector((0, 0, r)), (s + pied) / 2 + Vector((0, 0, r - s.z)), pied, arrivee + Vector((0, 0, -0.9)) + dec * 0.3, arrivee]
            for c in chemin[1:3]: c.z = r
        else:
            approche = arrivee + (milieu - arrivee).normalized() * 0.6 + Vector((0, 0, 0.25))
            chemin = [s, milieu, approche, arrivee]
        mat = JAUNE if (not geant and random.random() < 0.05) else random.choice(GAINES)
        courbe(f"câble {n_cables}", chemin, r, mat, res=16 if geant else 10)
        n_cables += 1
print("câbles :", n_cables)

# ---------------------------------------------------------------- l'entrepôt
LX, LY, LZ = 40, 30, 9
sol = plaque("sol", LX, LY, BETON)
murs = [("mur gauche", 0.4, LY, LZ, (-LX / 2, 0, LZ / 2)), ("mur droit", 0.4, LY, LZ, (LX / 2, 0, LZ / 2)),
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
ciel = plaque("ciel", LX, LZ, CIEL); ciel.rotation_euler = (math.radians(90), 0, 0); ciel.location = (0, LY / 2 + 1.5, LZ / 2)
# fenêtres hautes des murs latéraux
for cote in (-1, 1):
    ciel_l = plaque(f"ciel latéral {cote}", LY, 2.0, CIEL); ciel_l.rotation_euler = (math.radians(90), 0, math.radians(90))
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
trou_toit = plaque("trou du toit", 1.4, 1.0, CIEL); trou_toit.location = (4.2, 11.5, LZ + 0.05); trou_toit.rotation_euler = (math.radians(180), 0, 0)

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
filet = bouton("filet d'eau", 0.012, LZ, EAU, None, 0, seg=12); filet.location = (4.2, 11.5, LZ / 2)
flaque = bouton("flaque", 1.1, 0.004, principled("eau calme", "#0E1012", 0, 0.02), None, 0, seg=48)
flaque.location = (4.2, 11.5, 0.002); flaque.scale = (1.0, 0.7, 1.0)

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

# ---------------------------------------------------------------- lumière : ciel gris, air poussiéreux
w = bpy.data.worlds.new("monde"); sc.world = w; w.use_nodes = True
wn = w.node_tree.nodes
wn["Background"].inputs["Color"].default_value = (*lin("#7E878F"), 1); wn["Background"].inputs["Strength"].default_value = 0.12
vol = wn.new("ShaderNodeVolumePrincipled"); vol.inputs["Density"].default_value = float(os.environ.get("BRUME", "0.012"))
vol.inputs["Color"].default_value = (*lin("#C9CED3"), 1); vol.inputs["Anisotropy"].default_value = 0.35
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
soleil = lampe("jour", "SUN", (0, 20, 10), 1.6, GRIS, rot=(math.radians(62), 0, math.radians(180 + 18)))
soleil.data.angle = math.radians(8)
lampe("fenêtres fond", "AREA", (0, 13.5, 5.5), 1800, GRIS, cible=(0, 0, 1), taille=30)
lampe("fenêtres côté", "AREA", (-18.5, 0, 7.2), 700, GRIS, cible=(0, 0, 1), taille=20)
lampe("puits de jour", "SPOT", (4.2, 11.5, 8.9), 2500, GRIS, cible=(4.2, 11.5, 0), taille=18)
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
# On découvre la toile de câbles vers le module, on descend le long du câble propre, puis on s'approche du Phenix
# qui se réveille, jusqu'à pouvoir lire son écran.
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
    (1,   Vector((1.6, -5.2, 1.5)), HUB + Vector((0, 0, 0.6)), 20, 5.6),
    (110, Vector((0.9, -3.3, 1.6)), HUB + Vector((0, 0, -0.3)), 24, 5.6),
    (200, Vector((0.35, -1.45, 1.35)), Vector((0.06, 0.12, 1.25)), 32, 4.0),
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
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920
sc.render.resolution_percentage = POURCENT
sc.view_settings.view_transform = "AgX"
try: sc.view_settings.look = "AgX - Base Contrast"
except Exception: pass
sc.view_settings.exposure = float(os.environ.get("EXPO", "0"))
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
