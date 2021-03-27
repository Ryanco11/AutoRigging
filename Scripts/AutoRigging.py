import bpy

import bpy

a = bpy.data.objects['Armature1']
b = bpy.data.objects['Sphere']

bpy.ops.object.select_all(action='DESELECT') # deselect all object

a.select_set(True)
b.select_set(True)     # select the object for the 'parenting'

bpy.context.view_layer.objects.active = a    # the active object will be the parent of all selected object

bpy.ops.object.parent_set(type='ARMATURE_AUTO', keep_transform=True)
# Now The parent of b is a






bpy.ops.object.select_all(action='DESELECT') # deselect all object

#select and active Sphere
b = bpy.data.objects['Sphere']
b.select_set(True)
bpy.context.view_layer.objects.active = b

#clear all vertex group weight in Sphere
mode = bpy.context.active_object.mode
bpy.ops.object.mode_set(mode='OBJECT')
ob = bpy.context.active_object
selectedVerts = [v for v in ob.data.vertices if v.select]
for v in selectedVerts:
    for i, g in enumerate(v.groups):
        v.groups[i].weight=0