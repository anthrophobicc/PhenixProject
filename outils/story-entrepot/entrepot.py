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

# Béton du sol : dalles de 4 m avec leurs joints, fissures, taches d'huile et d'humidité, mousse dans les creux, et des
# flaques (zones lisses et sombres qui reflètent).
def beton():
    m, n, l, b = nouveau("béton")
    pos = n.new("ShaderNodeNewGeometry").outputs["Position"]
    def bruit(echelle, detail=6, vec=None):
        t = n.new("ShaderNodeTexNoise"); t.inputs["Scale"].default_value = echelle; t.inputs["Detail"].default_value = detail
        l.new(vec or pos, t.inputs["Vector"]); return t
    def plage(src, a, b_, c=0.0, d=1.0):
        r = n.new("ShaderNodeMapRange"); r.inputs["From Min"].default_value = a; r.inputs["From Max"].default_value = b_
        r.inputs["To Min"].default_value = c; r.inputs["To Max"].default_value = d; l.new(src, r.inputs["Value"]); return r.outputs["Result"]
    def calcul(op, a, b_):
        k = n.new("ShaderNodeMath"); k.operation = op
        for i, v in ((0, a), (1, b_)):
            if isinstance(v, float): k.inputs[i].default_value = v
            else: l.new(v, k.inputs[i])
        return k.outputs[0]
    def melange(fac, c1, c2):
        mx = n.new("ShaderNodeMix"); mx.data_type = "RGBA"; l.new(fac, mx.inputs[0])
        for i, c in ((6, c1), (7, c2)):
            if isinstance(c, str): mx.inputs[i].default_value = (*lin(c), 1)
            else: l.new(c, mx.inputs[i])
        return mx.outputs[2]
    couleur = melange(plage(bruit(0.22, 9).outputs["Fac"], 0.3, 0.75), "#4C4943", "#7C786F")
    couleur = melange(plage(bruit(4.0, 4).outputs["Fac"], 0.35, 0.65, 0.0, 0.25), couleur, "#A8A398")       # poussière claire
    couleur = melange(calcul("MULTIPLY", plage(bruit(0.7, 6).outputs["Fac"], 0.52, 0.68), 0.85), couleur, "#2A2824")   # huile, humidité
    mousse = plage(bruit(0.5, 8).outputs["Fac"], 0.58, 0.7)
    couleur = melange(calcul("MULTIPLY", mousse, 0.8), couleur, "#47532C")
    brk = n.new("ShaderNodeTexBrick"); brk.offset = 0.0; l.new(pos, brk.inputs["Vector"])
    brk.inputs["Scale"].default_value = 1.0; brk.inputs["Mortar Size"].default_value = 0.012; brk.inputs["Mortar Smooth"].default_value = 0.4
    brk.inputs["Brick Width"].default_value = 4.0; brk.inputs["Row Height"].default_value = 4.0
    deform = n.new("ShaderNodeVectorMath"); deform.operation = "MULTIPLY_ADD"
    l.new(bruit(1.2, 4).outputs["Color"], deform.inputs[0]); deform.inputs[1].default_value = (0.35, 0.35, 0.35); l.new(pos, deform.inputs[2])
    vor = n.new("ShaderNodeTexVoronoi"); vor.feature = "DISTANCE_TO_EDGE"; vor.inputs["Scale"].default_value = 0.5
    l.new(deform.outputs[0], vor.inputs["Vector"])
    fissure = calcul("MULTIPLY", plage(vor.outputs["Distance"], 0.0, 0.012, 1.0, 0.0), plage(bruit(0.3).outputs["Fac"], 0.44, 0.52))
    creux = calcul("MAXIMUM", brk.outputs["Fac"], fissure)
    couleur = melange(creux, couleur, melange(mousse, "#1C1A16", "#3C4824"))
    flaque = bruit(0.22, 3)
    masque = plage(flaque.outputs["Fac"], 0.6, 0.64)
    couleur = melange(masque, couleur, "#1A1B1C")
    l.new(couleur, b.inputs["Base Color"])
    rug = calcul("MAXIMUM", plage(bruit(60, 3).outputs["Fac"], 0.3, 0.7, 0.68, 0.92), creux)
    sec = calcul("SUBTRACT", 1.0, masque)
    l.new(calcul("ADD", calcul("MULTIPLY", rug, sec), calcul("MULTIPLY", masque, 0.03)), b.inputs["Roughness"])
    grain = n.new("ShaderNodeBump"); l.new(bruit(70, 4).outputs["Fac"], grain.inputs["Height"])
    l.new(calcul("MULTIPLY", sec, 0.12), grain.inputs["Strength"])
    relief = n.new("ShaderNodeBump"); relief.inputs["Distance"].default_value = 0.02
    l.new(calcul("SUBTRACT", 1.0, creux), relief.inputs["Height"]); l.new(calcul("MULTIPLY", sec, 0.7), relief.inputs["Strength"])
    l.new(grain.outputs["Normal"], relief.inputs["Normal"]); l.new(relief.outputs["Normal"], b.inputs["Normal"])
    return m

# Briques : appareil courant, joints en creux, restes d'enduit par plaques, encrassement et humidité en bas du mur.
def briques(nom):
    m, n, l, b = nouveau(nom)
    sep = n.new("ShaderNodeSeparateXYZ"); l.new(n.new("ShaderNodeNewGeometry").outputs["Position"], sep.inputs[0])
    add = n.new("ShaderNodeMath"); add.operation = "ADD"; l.new(sep.outputs[0], add.inputs[0]); l.new(sep.outputs[1], add.inputs[1])
    uv = n.new("ShaderNodeCombineXYZ"); l.new(add.outputs[0], uv.inputs[0]); l.new(sep.outputs[2], uv.inputs[1])
    brk = n.new("ShaderNodeTexBrick"); l.new(uv.outputs[0], brk.inputs["Vector"])
    for k, v in (("Scale", 1.0), ("Brick Width", 0.23), ("Row Height", 0.076), ("Mortar Size", 0.009), ("Mortar Smooth", 0.25), ("Bias", 0.0)):
        brk.inputs[k].default_value = v
    brk.inputs["Color1"].default_value = (*lin("#6A3B2A"), 1); brk.inputs["Color2"].default_value = (*lin("#955A40"), 1)
    brk.inputs["Mortar"].default_value = (*lin("#77736A"), 1)
    pl = n.new("ShaderNodeTexNoise"); pl.inputs["Scale"].default_value = 0.4; pl.inputs["Detail"].default_value = 12; pl.inputs["Roughness"].default_value = 0.65
    l.new(uv.outputs[0], pl.inputs["Vector"])
    enduit = n.new("ShaderNodeMapRange"); enduit.inputs["From Min"].default_value = 0.52; enduit.inputs["From Max"].default_value = 0.54
    l.new(pl.outputs["Fac"], enduit.inputs["Value"])
    mx = n.new("ShaderNodeMix"); mx.data_type = "RGBA"; l.new(enduit.outputs["Result"], mx.inputs[0]); l.new(brk.outputs["Color"], mx.inputs[6])
    mx.inputs[7].default_value = (*lin("#8C8578"), 1)
    bas = n.new("ShaderNodeMapRange"); bas.inputs["From Min"].default_value = 0.0; bas.inputs["From Max"].default_value = 2.0
    bas.inputs["To Min"].default_value = 0.65; bas.inputs["To Max"].default_value = 0.0; l.new(sep.outputs[2], bas.inputs["Value"])
    sale = n.new("ShaderNodeMix"); sale.data_type = "RGBA"; l.new(bas.outputs["Result"], sale.inputs[0]); l.new(mx.outputs[2], sale.inputs[6])
    sale.inputs[7].default_value = (*lin("#26221D"), 1)
    l.new(sale.outputs[2], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.88
    joint = n.new("ShaderNodeMath"); joint.operation = "SUBTRACT"; joint.inputs[0].default_value = 1.0; l.new(brk.outputs["Fac"], joint.inputs[1])
    hauteur = n.new("ShaderNodeMath"); hauteur.operation = "MAXIMUM"; l.new(joint.outputs[0], hauteur.inputs[0]); l.new(enduit.outputs["Result"], hauteur.inputs[1])
    fin = n.new("ShaderNodeTexNoise"); fin.inputs["Scale"].default_value = 40; l.new(uv.outputs[0], fin.inputs["Vector"])
    bp1 = n.new("ShaderNodeBump"); bp1.inputs["Strength"].default_value = 0.15; l.new(fin.outputs["Fac"], bp1.inputs["Height"])
    bp = n.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.6; bp.inputs["Distance"].default_value = 0.01
    l.new(hauteur.outputs[0], bp.inputs["Height"]); l.new(bp1.outputs["Normal"], bp.inputs["Normal"]); l.new(bp.outputs["Normal"], b.inputs["Normal"])
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
MUR = briques("mur")
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

# ---------------------------------------------------------------- l'entrepôt : murs de briques, brèche, vitres cassées, toit percé
for nom, a, b, c, pos in [("mur gauche", 0.4, LY, LZ, (-LX / 2, 0, LZ / 2)), ("mur droit", 0.4, LY, LZ, (LX / 2, 0, LZ / 2)),
                          ("mur avant", LX, 0.4, LZ, (0, -LY / 2, LZ / 2))]:
    boite(nom, a, b, c, pos, MUR)
# mur du fond : une brèche dans le bas, puis une rangée de hautes fenêtres
BR0, BR1, BRH = -8.8, -6.0, 2.3
boite("fond bas gauche", BR0 + LX / 2, 0.4, 3.2, ((BR0 - LX / 2) / 2, LY / 2, 1.6), MUR)
boite("fond bas droit", LX / 2 - BR1, 0.4, 3.2, ((BR1 + LX / 2) / 2, LY / 2, 1.6), MUR)
boite("linteau", BR1 - BR0, 0.4, 3.2 - BRH, ((BR0 + BR1) / 2, LY / 2, (BRH + 3.2) / 2), MUR)
boite("fond haut", LX, 0.4, 1.2, (0, LY / 2, LZ - 0.6), MUR)
BRIQUE = bruite("brique", "#6A3B2A", "#9A5E44", 9.0, rugo=(0.75, 0.95), relief=0.3)
def brique(nom, pos, rz=0.0, rx=0.0):
    ob = boite(nom, 0.23, 0.11, 0.07, pos, BRIQUE); ob.rotation_euler = (rx, random.uniform(-0.2, 0.2) if rx else 0, rz)
    return ob
for k in range(80):   # bords déchiquetés : des briques dépassent dans la brèche
    z = random.uniform(0, BRH)
    if k % 3 == 0: brique(f"brique bord g {k}", (BR0 + random.uniform(0.05, 0.5) * (1 - z / BRH * 0.6), LY / 2 + random.uniform(-0.12, 0.12), z))
    elif k % 3 == 1: brique(f"brique bord d {k}", (BR1 - random.uniform(0.05, 0.5) * (1 - z / BRH * 0.6), LY / 2 + random.uniform(-0.12, 0.12), z))
    else: brique(f"brique linteau {k}", (random.uniform(BR0, BR1), LY / 2 + random.uniform(-0.12, 0.12), BRH - random.uniform(0.0, 0.35)))
for k in range(150):  # le tas de briques tombées, des deux côtés de la brèche
    x = random.gauss((BR0 + BR1) / 2, 1.0); y = LY / 2 + random.gauss(0, 1.1)
    if abs(y - LY / 2) < 0.22 and not (BR0 < x < BR1): continue
    brique(f"brique tombée {k}", (x, y, 0.035 + abs(random.gauss(0, 0.12)) * max(0, 1 - abs(x - (BR0 + BR1) / 2) / 2)),
           random.uniform(0, 6.28), random.choice((0, 0, math.radians(90))))
for i in range(9):
    x = -18 + i * 4.5
    boite(f"trumeau {i}", 1.3, 0.4, 4.6, (x, LY / 2, 3.2 + 2.3), MUR)
    for j in range(1, 4):  # meneaux des vitres
        boite(f"meneau {i}-{j}", 0.05, 0.08, 4.6, (x + 0.65 + j * 0.8, LY / 2 - 0.1, 5.5), ACIER_SALE)
    for j in range(1, 5):
        boite(f"traverse {i}-{j}", 3.2, 0.08, 0.05, (x + 2.25, LY / 2 - 0.1, 3.2 + j * 0.92), ACIER_SALE)

# vitres : verre sale, beaucoup de carreaux cassés ou absents. Le verre laisse passer l'ombre (le soleil entre).
def verre():
    m, n, l, b = nouveau("verre sale")
    b.inputs["Base Color"].default_value = (*lin("#B4BEB4"), 1); b.inputs["Transmission Weight"].default_value = 1.0
    b.inputs["IOR"].default_value = 1.5
    br = n.new("ShaderNodeTexNoise"); br.inputs["Scale"].default_value = 3.0; br.inputs["Detail"].default_value = 8
    r = n.new("ShaderNodeMapRange"); r.inputs["To Min"].default_value = 0.08; r.inputs["To Max"].default_value = 0.6
    l.new(br.outputs["Fac"], r.inputs["Value"]); l.new(r.outputs["Result"], b.inputs["Roughness"])
    lp = n.new("ShaderNodeLightPath"); tr = n.new("ShaderNodeBsdfTransparent"); mx = n.new("ShaderNodeMixShader")
    l.new(lp.outputs["Is Shadow Ray"], mx.inputs[0]); l.new(b.outputs[0], mx.inputs[1]); l.new(tr.outputs[0], mx.inputs[2])
    l.new(mx.outputs[0], n["Material Output"].inputs["Surface"])
    return m
VERRE = verre()
YV = LY / 2 - 0.1
for i in range(9):
    x = -18 + i * 4.5
    for c in range(4):
        for rg in range(5):
            x0, z0 = x + 0.65 + c * 0.8, 3.2 + rg * 0.92
            t = random.random()
            if t < 0.32: continue                                  # carreau absent
            if t < 0.55:                                           # carreau cassé : il reste un éclat dans un coin
                cx, cz = random.choice(((x0, z0), (x0 + 0.8, z0), (x0, z0 + 0.92), (x0 + 0.8, z0 + 0.92)))
                sx, sz = (0.8 if cx == x0 else -0.8), (0.92 if cz == z0 else -0.92)
                a1, a2, a3 = random.uniform(0.25, 0.9), random.uniform(0.25, 0.9), random.uniform(0.1, 0.45)
                bm = bmesh.new()
                bm.faces.new([bm.verts.new(v) for v in ((cx, YV, cz), (cx + sx * a1, YV, cz), (cx + sx * a3, YV, cz + sz * a3 * 1.4), (cx, YV, cz + sz * a2))])
                me = bpy.data.meshes.new("éclat"); bm.to_mesh(me); bm.free()
                ob = objet(f"éclat {i}-{c}-{rg}", me, VERRE); ob.modifiers.new("épaisseur", "SOLIDIFY").thickness = 0.005
            else:
                boite(f"carreau {i}-{c}-{rg}", 0.79, 0.005, 0.91, (x0 + 0.4, YV, z0 + 0.46), VERRE)

# dehors : de l'herbe, des buissons et des arbres, qu'on voit par la brèche et par les fenêtres
EXT = bruite("herbe dehors", "#34421E", "#6B6A36", 0.5, rugo=(0.7, 0.95), relief=0.3)
for nom, x0, x1, y0, y1 in (("dehors fond", -80, 80, LY / 2 + 0.2, 80), ("dehors avant", -80, 80, -80, -LY / 2 - 0.2),
                            ("dehors gauche", -80, -LX / 2 - 0.2, -LY / 2 - 0.2, LY / 2 + 0.2), ("dehors droit", LX / 2 + 0.2, 80, -LY / 2 - 0.2, LY / 2 + 0.2)):
    dalle(nom, x0, x1, y0, y1, 0.0, EXT)
ECORCE = bruite("écorce", "#2E261E", "#4A3E30", 6.0, rugo=(0.8, 1.0), relief=0.5)
def feuillage():
    m, n, l, b = nouveau("feuillage")
    br = n.new("ShaderNodeTexNoise"); br.inputs["Scale"].default_value = 2.0
    rp = n.new("ShaderNodeValToRGB"); e = rp.color_ramp.elements
    e[0].color = (*lin("#22381A"), 1); e[1].color = (*lin("#5E7A2E"), 1)
    l.new(br.outputs["Fac"], rp.inputs["Fac"]); l.new(rp.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.6; b.inputs["Subsurface Weight"].default_value = 0.2
    fin = n.new("ShaderNodeTexVoronoi"); fin.inputs["Scale"].default_value = 18
    bp = n.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.8
    l.new(fin.outputs["Distance"], bp.inputs["Height"]); l.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m
FEUILLAGE = feuillage()
NUAGES = bpy.data.textures.new("nuages", "CLOUDS"); NUAGES.noise_scale = 0.6
def masse(nom, centre, rayon):
    bm = bmesh.new(); bmesh.ops.create_icosphere(bm, subdivisions=3, radius=rayon)
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    ob = objet(nom, me, FEUILLAGE); ob.location = centre; lisser(ob)
    dp = ob.modifiers.new("relief", "DISPLACE"); dp.texture = NUAGES; dp.strength = rayon * 0.45; dp.texture_coords = "GLOBAL"
    return ob
for i in range(16):
    x, y, h = random.uniform(-32, 32), random.uniform(LY / 2 + 4, LY / 2 + 22), random.uniform(8, 15)
    bm = bmesh.new(); bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=0.35, radius2=0.12, depth=h * 0.7)
    me = bpy.data.meshes.new(f"tronc {i}"); bm.to_mesh(me); bm.free()
    objet(f"tronc {i}", me, ECORCE).location = (x, y, h * 0.35)
    for k in range(6):
        masse(f"houppier {i}-{k}", Vector((x + random.uniform(-2, 2), y + random.uniform(-2, 2), h * random.uniform(0.6, 0.95))), random.uniform(1.6, 3.0))
for i in range(10):   # buissons devant la brèche et le long du mur
    masse(f"buisson {i}", Vector((random.uniform(-14, 4), LY / 2 + random.uniform(0.8, 3.5), 0.3)), random.uniform(0.5, 1.1))

# toit : tôles ondulées entre les fermes, plusieurs ont disparu (le soleil passe), deux pendent
def tole():
    m, n, l, b = nouveau("tôle ondulée")
    pos = n.new("ShaderNodeNewGeometry").outputs["Position"]
    onde = n.new("ShaderNodeTexWave"); onde.bands_direction = "X"; onde.inputs["Scale"].default_value = 0.66
    onde.inputs["Distortion"].default_value = 0.0; l.new(pos, onde.inputs["Vector"])
    rouille = n.new("ShaderNodeTexNoise"); rouille.inputs["Scale"].default_value = 1.2; rouille.inputs["Detail"].default_value = 10
    l.new(pos, rouille.inputs["Vector"])
    rp = n.new("ShaderNodeValToRGB"); e = rp.color_ramp.elements; e[0].position = 0.45; e[1].position = 0.65
    e[0].color = (*lin("#4E5052"), 1); e[1].color = (*lin("#6A4228"), 1)
    l.new(rouille.outputs["Fac"], rp.inputs["Fac"]); l.new(rp.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Metallic"].default_value = 0.6; b.inputs["Roughness"].default_value = 0.7
    bp = n.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.9
    l.new(onde.outputs["Fac"], bp.inputs["Height"]); l.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m
TOLE = tole()
TROU_TABLE, TROU_EAU = (-4, 6), (0, 12)   # le soleil tombe sur la table par le premier ; l'eau de pluie passe par le second
TROUS = {TROU_TABLE, TROU_EAU}
while len(TROUS) < 11:
    TROUS.add((random.randrange(-16, 16, 4), random.randrange(-6, 15, 3)))
for x0 in range(-20, 20, 4):
    for y0 in range(-15, 15, 3):
        if (x0, y0) not in TROUS: boite(f"tôle {x0} {y0}", 3.98, 2.98, 0.012, (x0 + 2, y0 + 1.5, LZ + 0.006), TOLE)
for k, (x0, y0) in enumerate(sorted(TROUS - {TROU_TABLE, TROU_EAU})[:2]):   # tôles qui pendent, accrochées par un bord
    th = math.radians(random.uniform(35, 65))
    p = boite(f"tôle pendante {k}", 3.98, 2.98, 0.012, (x0 + 2, y0 + 1.49 * math.cos(th), LZ - 1.49 * math.sin(th)), TOLE)
    p.rotation_euler.x = -th
for i in range(9):  # fermes du toit et poteaux
    y = -12 + i * 3
    boite(f"ferme {i}", LX, 0.22, 0.5, (0, y, LZ - 0.45), ACIER_SALE)
    if i % 2 == 0:
        for x in (-8, 8): boite(f"poteau {i} {x}", 0.32, 0.32, LZ, (x, y, LZ / 2), ACIER_SALE)
for x in range(-16, 17, 8): boite(f"panne {x}", 0.16, LY, 0.3, (x, 0, LZ - 0.8), ACIER_SALE)

# ---------------------------------------------------------------- les câbles sous-marins
# De vrais câbles de liaison sous-marine : armure de fils d'acier en hélice, jute goudronnée, ou gaine noire nue. Ils
# entrent par les trous du toit, sortent du plafond, du mur du fond ou des murs latéraux, descendent de partout en
# chaînette et convergent vers la tranchée derrière la table, où ils plongent.
def mat_cable(nom, genre):
    m, n, l, b = nouveau(nom)
    sep = n.new("ShaderNodeSeparateXYZ"); l.new(n.new("ShaderNodeTexCoord").outputs["UV"], sep.inputs[0])
    att = n.new("ShaderNodeAttribute"); att.attribute_type = "OBJECT"; att.attribute_name = "longueur"
    def calcul(op, *e):
        k = n.new("ShaderNodeMath"); k.operation = op
        for i, v in enumerate(e):
            if isinstance(v, (int, float)): k.inputs[i].default_value = v
            else: l.new(v, k.inputs[i])
        return k.outputs[0]
    fils, pas = {"armé": (24, 0.45), "jute": (12, 0.32), "gaine": (1, 1.0)}[genre]
    # phase = fils × (tour + longueur parcourue / pas) : des fils enroulés en hélice
    phase = calcul("MULTIPLY", calcul("MULTIPLY_ADD", calcul("MULTIPLY", sep.outputs[0], att.outputs["Fac"]), 1.0 / pas, sep.outputs[1]), fils)
    profil = calcul("SINE", calcul("MULTIPLY", calcul("FRACT", phase), math.pi))
    br = n.new("ShaderNodeTexNoise"); br.inputs["Scale"].default_value = 2.5; br.inputs["Detail"].default_value = 8
    def mix(fac, c1, c2):
        mx = n.new("ShaderNodeMix"); mx.data_type = "RGBA"; l.new(fac, mx.inputs[0])
        for i, c in ((6, c1), (7, c2)):
            if isinstance(c, str): mx.inputs[i].default_value = (*lin(c), 1)
            else: l.new(c, mx.inputs[i])
        return mx.outputs[2]
    goudron = n.new("ShaderNodeMapRange"); goudron.inputs["From Min"].default_value = 0.42; goudron.inputs["From Max"].default_value = 0.6
    l.new(br.outputs["Fac"], goudron.inputs["Value"])
    if genre == "armé":
        c = mix(goudron.outputs["Result"], "#8C8E8F", "#2B241C")
        c = mix(calcul("MULTIPLY", calcul("SUBTRACT", 1.0, profil), 0.6), c, "#1A1814")
        l.new(calcul("SUBTRACT", 0.9, calcul("MULTIPLY", goudron.outputs["Result"], 0.7)), b.inputs["Metallic"])
        l.new(calcul("ADD", 0.35, calcul("MULTIPLY", goudron.outputs["Result"], 0.4)), b.inputs["Roughness"])
        force = 0.7
    elif genre == "jute":
        c = mix(goudron.outputs["Result"], "#5A4631", "#2A2018")
        c = mix(calcul("MULTIPLY", calcul("SUBTRACT", 1.0, profil), 0.5), c, "#17120D")
        b.inputs["Roughness"].default_value = 0.88; force = 0.8
    else:
        c = mix(calcul("MULTIPLY", goudron.outputs["Result"], 0.3), "#0C0C0E", "#1E1D1C")
        b.inputs["Roughness"].default_value = 0.34; b.inputs["Coat Weight"].default_value = 0.25; force = 0.0
    # poussière déposée sur le dessus
    nz = n.new("ShaderNodeSeparateXYZ"); l.new(n.new("ShaderNodeNewGeometry").outputs["Normal"], nz.inputs[0])
    dessus = n.new("ShaderNodeMapRange"); dessus.inputs["From Min"].default_value = 0.4; dessus.inputs["From Max"].default_value = 1.0
    dessus.inputs["To Max"].default_value = 0.55; l.new(nz.outputs[2], dessus.inputs["Value"])
    c = mix(calcul("MULTIPLY", dessus.outputs["Result"], br.outputs["Fac"]), c, "#6E6A60")
    l.new(c, b.inputs["Base Color"])
    fin = n.new("ShaderNodeTexNoise"); fin.inputs["Scale"].default_value = 90
    bp1 = n.new("ShaderNodeBump"); bp1.inputs["Strength"].default_value = 0.15; l.new(fin.outputs["Fac"], bp1.inputs["Height"])
    bp = n.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = force; bp.inputs["Distance"].default_value = 0.004
    l.new(profil, bp.inputs["Height"]); l.new(bp1.outputs["Normal"], bp.inputs["Normal"]); l.new(bp.outputs["Normal"], b.inputs["Normal"])
    return m
CABLES_SM = {g: mat_cable(f"câble {g}", g) for g in ("armé", "jute", "gaine")}

def chainette(Lh, h):   # paramètre a tel que a (ch(Lh / a) - 1) = h
    lo, hi = 0.01, 5000.0
    for _ in range(90):
        a = (lo * hi) ** 0.5
        if a * (math.cosh(min(Lh / a, 700)) - 1) > h: lo = a
        else: hi = a
    return a

def descente(T, d, Lh, h, n=60):
    # chaînette dont le point bas est T (posé au sol, tangent au sol), qui remonte de h sur Lh à l'opposé de d ;
    # points répartis le long du câble, du haut vers le bas
    a = chainette(Lh, h); s_tot = a * math.sinh(Lh / a)
    return [T - d * x + Vector((0, 0, a * (math.cosh(x / a) - 1))) for x in (a * math.asinh(s_tot * (1 - i / n) / a) for i in range(n + 1))]

def hor(v): return Vector((v.x, v.y, 0))
def haut_plafond(p, r):
    if any(abs(p.y - (-12 + 3 * i)) < 0.11 + r for i in range(9)): return LZ - 0.7 - r     # sous une ferme
    if any(abs(p.x - x) < 0.08 + r for x in range(-16, 17, 8)): return LZ - 0.95 - r        # sous une panne
    return LZ + 0.02                                                                        # à travers la tôle

TROUS_CABLES = sorted(TROUS - {TROU_EAU})
def ancre():
    t = random.random()
    if t < 0.35:   # par un trou du toit, depuis dehors
        x0, y0 = random.choice(TROUS_CABLES)
        return Vector((random.uniform(x0 + 0.6, x0 + 3.4), random.uniform(y0 + 0.5, y0 + 2.5), LZ + 2.0)), "trou"
    if t < 0.72:   # du plafond, au-dessus et derrière la table
        p = Vector((random.uniform(-11, 11), random.uniform(1.5, 14), 0)); return p, "plafond"
    if t < 0.88:   # du mur du fond
        x = random.uniform(-16, 16); z = random.choice((random.uniform(1.2, 2.9), random.uniform(8.0, 8.6)))
        if BR0 - 0.3 < x < BR1 + 0.3 and z < 3: z = 2.9
        return Vector((x, LY / 2 - 0.05, z)), "mur"
    cote = random.choice((-1, 1))
    return Vector((cote * (LX / 2 - 0.05), random.uniform(-1, 13), random.uniform(3, 8.5))), "mur"

Y0, Y1 = FY - FDY + 0.3, FY + FDY - 0.2
occupe = {-1: [], 1: []}
def place_libre(cote, y, r):
    for k in range(600):
        for yy in (y + k * 0.01, y - k * 0.01):
            if Y0 <= yy - r and yy + r <= Y1 and all(abs(yy - a) > r + b_ + 0.015 for a, b_ in occupe[cote]):
                occupe[cote].append((yy, r)); return yy
    return None

SOL_Y = []   # aucun câble ne court au sol de bout en bout
n_cables = 0
for i in range(int(os.environ.get("CABLES", "75"))):
    A, origine = ancre()
    genre = random.choices(("armé", "jute", "gaine"), (0.45, 0.25, 0.3))[0]
    r = random.uniform(0.022, 0.048) if random.random() < 0.85 else random.uniform(0.06, 0.085)
    if origine == "plafond": A.z = haut_plafond(A, r)
    if abs(A.x - FX) < FDX + 1.0: continue                          # pas juste au-dessus de la tranchée
    cote = 1 if A.x > FX else -1
    yk = place_libre(cote, min(max(A.y - random.uniform(0.0, 2.5), Y0), Y1), r)
    if yk is None: continue
    e = Vector((FX + cote * FDX, yk, 0))
    vers = (hor(A) - e).normalized()
    if vers.x * cote < 0.35:                                         # arriverait trop en biais sur le bord
        occupe[cote].pop(); continue
    posee = random.uniform(0.3, 1.1)
    T = e + vers * posee; T.z = r
    Lh = (hor(A) - hor(T)).length
    d = -vers
    pts = descente(T, d, Lh, A.z - r)
    pts += [T.lerp(e + Vector((0, 0, r)), k / 4) for k in range(1, 4)] + plongee(e, -d, r, 0)
    ob = tube(f"câble {n_cables}", pts, r, CABLES_SM[genre], res=4 if r > 0.04 else 3)
    ob["longueur"] = sum((pts[k + 1] - pts[k]).length for k in range(len(pts) - 1))
    n_cables += 1
print("câbles :", n_cables)

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

# cailloux et feuilles mortes semés sur le sol (des copies d'une poignée de modèles : léger en mémoire)
CAILLOU = bruite("caillou", "#56524A", "#8E887C", 5.0, rugo=(0.7, 0.95), relief=0.4)
def mat_feuille_morte():
    m, n, l, b = nouveau("feuille morte")
    br = n.new("ShaderNodeTexNoise"); br.inputs["Scale"].default_value = 30
    rp = n.new("ShaderNodeValToRGB"); e = rp.color_ramp.elements
    e[0].color = (*lin("#4A3220"), 1); e[1].color = (*lin("#8E6A36"), 1)
    l.new(br.outputs["Fac"], rp.inputs["Fac"]); l.new(rp.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.75
    return m
FEUILLE_MORTE = mat_feuille_morte()

def collection(nom, objets):
    # modèle pour les semis : il doit être dans la scène et visible au rendu, sinon ses copies disparaissent aussi ;
    # on le range 100 m sous terre (le décalage de la collection ramène les copies au niveau du sol)
    c = bpy.data.collections.new(nom); sc.collection.children.link(c); c.instance_offset = (0, 0, -100)
    for o in objets:
        sc.collection.objects.unlink(o); c.objects.link(o); o.location = (0, 0, -100)
    return c

cailloux = []
for k in range(7):
    bm = bmesh.new(); bmesh.ops.create_icosphere(bm, subdivisions=2, radius=1.0)
    for v in bm.verts: v.co *= random.uniform(0.75, 1.2)
    for v in bm.verts: v.co.z *= random.uniform(0.45, 0.7); v.co.x *= random.uniform(0.8, 1.3)
    me = bpy.data.meshes.new(f"caillou {k}"); bm.to_mesh(me); bm.free()
    o = objet(f"caillou {k}", me, CAILLOU); lisser(o); cailloux.append(o)
COLL_CAILLOUX = collection("cailloux", cailloux)
feuilles = []
for k in range(4):
    # feuille dans le plan YZ (sa normale suit X, l'axe que le semis aligne sur le sol), un peu recroquevillée
    bm = bmesh.new()
    contour = [(0.0, 0.0, -0.05), (0.02, 0.35, 0.22), (0.06, 0.75, 0.18), (0.0, 1.0, 0.0), (0.06, 0.75, -0.18), (0.02, 0.35, -0.22)]
    bm.faces.new([bm.verts.new((x * random.uniform(0.5, 1.5), z, y)) for x, y, z in contour])
    me = bpy.data.meshes.new(f"feuille morte {k}"); bm.to_mesh(me); bm.free()
    o = objet(f"feuille morte {k}", me, FEUILLE_MORTE); feuilles.append(o)
COLL_FEUILLES = collection("feuilles mortes", feuilles)

def semis(nom, x0, x1, y0, y1, nb, coll, taille, alea, aplati):
    em = dalle(nom, x0, x1, y0, y1, 0.001, None); em.show_instancer_for_render = False
    st = bpy.data.particles.new(nom); st.type = "HAIR"; st.count = nb; st.hair_length = 1.0   # la taille des copies est multipliée par cette longueur
    st.emit_from = "FACE"; st.distribution = "RAND"; st.use_emit_random = True
    st.render_type = "COLLECTION"; st.instance_collection = coll; st.use_collection_pick_random = True
    st.particle_size = taille; st.size_random = alea
    st.use_rotations = True; st.rotation_mode = "NOR"; st.phase_factor_random = 2.0
    if not aplati: st.rotation_factor_random = 0.6
    ps = em.modifiers.new("semis", "PARTICLE_SYSTEM").particle_system; ps.settings = st; ps.seed = random.randint(0, 9999)
ZONES = [(-LX / 2 + 0.2, LX / 2 - 0.2, -LY / 2 + 0.2, FY - FDY), (-LX / 2 + 0.2, LX / 2 - 0.2, FY + FDY, LY / 2 - 0.2),
         (-LX / 2 + 0.2, FX - FDX, FY - FDY, FY + FDY), (FX + FDX, LX / 2 - 0.2, FY - FDY, FY + FDY)]
for i, (x0, x1, y0, y1) in enumerate(ZONES):
    aire = (x1 - x0) * (y1 - y0)
    semis(f"gravillons {i}", x0, x1, y0, y1, int(aire * 40), COLL_CAILLOUX, 0.022, 0.9, False)
    semis(f"feuilles {i}", x0, x1, y0, y1, int(aire * 14), COLL_FEUILLES, 0.075, 0.5, True)
semis("feuilles devant", -4, 5, -10, 0.6, 2500, COLL_FEUILLES, 0.08, 0.5, True)   # sur le trajet de la caméra
semis("cailloux du fond", -LX / 2 + 0.2, LX / 2 - 0.2, LY / 2 - 1.6, LY / 2 - 0.2, 1400, COLL_CAILLOUX, 0.05, 0.9, False)
semis("feuilles du fond", -LX / 2 + 0.2, LX / 2 - 0.2, LY / 2 - 2.5, LY / 2 - 0.2, 2500, COLL_FEUILLES, 0.07, 0.5, True)
semis("feuilles de la brèche", BR0 - 2.5, BR1 + 2.5, LY / 2 - 4.0, LY / 2 - 0.2, 1500, COLL_FEUILLES, 0.07, 0.5, True)

# néons qui pendent des fermes, certains ne tiennent plus que par une suspente
CAOUTCHOUC = principled("caoutchouc", "#141414", 0, 0.8)
DIFFUSEUR = principled("diffuseur", "#C9C4B6", 0, 0.5)
for i in range(10):
    yb, xb = random.choice((-3, 0, 3, 6, 9)), random.uniform(-7, 7)
    zb = LZ - 0.7 - random.uniform(1.0, 2.6)
    casse = random.random() < 0.4
    th = math.radians(random.uniform(40, 75)) if casse else 0.0
    p0 = Vector((xb - 0.6, yb, zb))
    g = groupe(f"néon {i}", *(p0 + Vector((0.6 * math.cos(th), 0, -0.6 * math.sin(th))))[:2], 0.0)
    g.location.z = zb - 0.6 * math.sin(th); g.rotation_euler = (0, th, 0)
    piece(f"néon {i} corps", 1.25, 0.16, 0.06, (0, 0, 0), ACIER_SALE, g)
    piece(f"néon {i} diffuseur", 1.2, 0.12, 0.02, (0, 0, -0.035), DIFFUSEUR, g)
    for x in ((-0.6,) if casse else (-0.6, 0.6)):
        tube(f"suspente {i} {x}", [Vector((xb + x, yb, zb + 0.03)), Vector((xb + x, yb, LZ - 0.7))], 0.003, ACIER_SALE, res=1)

def pneu(nom, pos, rz=0.0, couche=True):
    bm = bmesh.new(); R, r = 0.32, 0.11
    anneaux = [[bm.verts.new(((R + r * math.cos(b)) * math.cos(a), (R + r * math.cos(b)) * math.sin(a), r * math.sin(b) * 0.9))
                for b in (2 * math.pi * j / 12 for j in range(12))] for a in (2 * math.pi * i / 36 for i in range(36))]
    for i in range(36):
        for j in range(12):
            bm.faces.new([anneaux[i][j], anneaux[(i + 1) % 36][j], anneaux[(i + 1) % 36][(j + 1) % 12], anneaux[i][(j + 1) % 12]])
    me = bpy.data.meshes.new(nom); bm.to_mesh(me); bm.free()
    o = objet(nom, me, CAOUTCHOUC); lisser(o); o.location = pos; o.rotation_euler = (0 if couche else math.radians(90), 0, rz)
    return o
for zone in (PRES_G, PRES_D, FOND_Z, AVANT_G):
    poser(2, zone, lambda x, y: [pneu(f"pneu {x:.1f} {k}", (x + random.uniform(-0.04, 0.04), y + random.uniform(-0.04, 0.04), 0.1 + k * 0.2))
                                for k in range(random.randint(1, 5))], 0.5)
    poser(1, zone, lambda x, y: pneu(f"pneu debout {x:.1f}", (x, y, 0.42), random.uniform(0, 6.28), False), 0.5)

# briques et morceaux de béton tombés, jusque sur le trajet de la caméra (en restant sous elle)
for k in range(140):
    x, y = random.uniform(-4.5, 5.5), random.uniform(-10, 0.3)
    if abs(x - 0.7) < 0.35 and y < -8.8: continue
    if -0.8 < x < 1.1 and -0.4 < y < 0.5: continue   # pas sous la table
    if random.random() < 0.5: brique(f"brique au sol {k}", (x, y, 0.035), random.uniform(0, 6.28), random.choice((0, 0, math.radians(90))))
    else:
        bm = bmesh.new(); bmesh.ops.create_icosphere(bm, subdivisions=1, radius=1.0); t = random.uniform(0.04, 0.12)
        for v in bm.verts: v.co *= t * random.uniform(0.7, 1.3); v.co.z *= 0.6
        me = bpy.data.meshes.new(f"bloc {k}"); bm.to_mesh(me); bm.free()
        o = objet(f"bloc {k}", me, GRAVATS); o.location = (x, y, t * 0.3); o.rotation_euler = (random.uniform(0, 0.5), 0, random.uniform(0, 6.28))

# une échelle appuyée contre le mur du fond, près de la brèche
g = groupe("échelle", -4.6, LY / 2 - 0.2 - 0.8, 0.0, 0.0, math.radians(-12))
for sx in (-0.22, 0.22): piece(f"échelle montant {sx}", 0.05, 0.04, 3.6, (sx, 0, 1.8), BOIS_VIEUX, g)
for k in range(11): piece(f"échelle barreau {k}", 0.44, 0.03, 0.03, (0, 0, 0.3 + k * 0.3), BOIS_VIEUX, g)

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

# ---------------------------------------------------------------- lumière : HDRI, soleil, air poussiéreux
w = bpy.data.worlds.new("monde"); sc.world = w; w.use_nodes = True
wn, wl = w.node_tree.nodes, w.node_tree.links
# vraie lumière du jour : l'HDRI « forêt » fourni avec Blender (ciel, arbres) et un soleil réel
env = wn.new("ShaderNodeTexEnvironment")
env.image = bpy.data.images.load(os.path.join(bpy.utils.system_resource("DATAFILES"), "studiolights", "world", "forest.exr"))
mp_w = wn.new("ShaderNodeMapping"); wl.new(wn.new("ShaderNodeTexCoord").outputs["Generated"], mp_w.inputs["Vector"])
mp_w.inputs["Rotation"].default_value = (0, 0, math.radians(float(os.environ.get("HDRI_ROT", "90"))))
wl.new(mp_w.outputs["Vector"], env.inputs["Vector"]); wl.new(env.outputs["Color"], wn["Background"].inputs["Color"])
wn["Background"].inputs["Strength"].default_value = float(os.environ.get("HDRI_FORCE", "1.0"))
# l'air poussiéreux ne remplit que l'intérieur : un brouillard sur tout le monde absorberait le soleil avant qu'il arrive
air = bpy.data.materials.new("air poussiéreux"); air.use_nodes = True; an = air.node_tree.nodes
an.remove(an["Principled BSDF"])
vol = an.new("ShaderNodeVolumePrincipled"); vol.inputs["Density"].default_value = float(os.environ.get("BRUME", "0.008"))
vol.inputs["Color"].default_value = (*lin("#D8D6CF"), 1); vol.inputs["Anisotropy"].default_value = 0.65
air.node_tree.links.new(vol.outputs[0], an["Material Output"].inputs["Volume"])
boite("air", LX - 0.42, LY - 0.42, LZ - 0.02, (0, 0, LZ / 2), air)

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
# soleil haut derrière l'entrepôt : il passe par les trous du toit (l'un tombe sur la table) et par les fenêtres,
# et dessine des rayons dans la poussière en venant vers la caméra
soleil = lampe("soleil", "SUN", (0, 20, 10), float(os.environ.get("SOLEIL", "4.5")), lin("#FFE7C9"), rot=(math.radians(39), 0, math.radians(195)))
soleil.data.angle = math.radians(0.8)
lampe("reflet appareil", "AREA", (-0.6, 0.9, 1.6), 12, GRIS, cible=(0.02, 0, TZ), taille=0.8)

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
    sc.render.use_persistent_data = True   # la scène reste chargée d'une image à l'autre
    print("Cycles :", [(dev.name, dev.type) for dev in prefs.devices if dev.use])
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920
sc.render.resolution_percentage = POURCENT
sc.view_settings.view_transform = "AgX"
try: sc.view_settings.look = "AgX - Base Contrast"
except Exception: pass
sc.view_settings.exposure = float(os.environ.get("EXPO", "0.55"))
sc.render.image_settings.file_format = "JPEG"; sc.render.image_settings.quality = 93

if os.environ.get("CAM_TEST"):
    v = [float(x) for x in os.environ["CAM_TEST"].split(",")]
    for ad in (cam.animation_data, point.animation_data, cam_d.animation_data): ad.action = None
    cam.location = v[0:3]; point.location = v[3:6]; cam_d.lens = v[6]; cam_d.dof.use_dof = False
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
