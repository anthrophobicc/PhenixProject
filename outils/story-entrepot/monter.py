# Monte les images de rushes/ en une vidéo MP4 (H.264, 30 images/s), sans passer par ffmpeg.
# Usage : blender -b -P monter.py [-- dossier sortie.mp4]   (par défaut : rushes/ vers entrepot.mp4)
import bpy, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
RUSHES = os.path.join(ICI, args[0] if args else "rushes")
SORTIE = os.path.join(ICI, args[1] if len(args) > 1 else "entrepot.mp4")
images = sorted(f for f in os.listdir(RUSHES) if f.endswith(".jpg"))

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.sequence_editor_create()
bande = sc.sequence_editor.sequences.new_image("rushes", os.path.join(RUSHES, images[0]), 1, 1)
for f in images[1:]: bande.elements.append(f)
premiere = bpy.data.images.load(os.path.join(RUSHES, images[0]))
sc.render.resolution_x, sc.render.resolution_y = premiere.size
sc.render.resolution_percentage = 100
sc.render.fps = 30
sc.frame_start, sc.frame_end = 1, len(images)
sc.render.image_settings.file_format = "FFMPEG"
ff = sc.render.ffmpeg
ff.format = "MPEG4"; ff.codec = "H264"; ff.constant_rate_factor = os.environ.get("QUALITE", "HIGH"); ff.ffmpeg_preset = "GOOD"; ff.audio_codec = "NONE"
sc.render.filepath = SORTIE
sc.render.use_file_extension = False
bpy.ops.render.render(animation=True)
print("vidéo :", sc.render.filepath, len(images), "images")
