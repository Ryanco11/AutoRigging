import bpy

print('Try')

bpy.ops.object.select_all(action='DESELECT')


#Select mesh firsy
bpy.data.objects['Cube'].select_set(True)

#select the ARMATURE
bpy.data.objects['Armature1'].select_set(True)

#apply ARMATURE to the mesh
bpy.ops.object.parent_set(type='ARMATURE_AUTO')



vertex_in_range = []


