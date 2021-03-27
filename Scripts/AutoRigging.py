import bpy

print('Try')

bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_name(name='Cube', extend=False)

bpy.data.objects['Cube'].select_set(True)
bpy.data.objects['Armature1'].select_set(True)
