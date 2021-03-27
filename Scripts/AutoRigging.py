import bpy

a = bpy.data.objects['Armature1']
b = bpy.data.objects['Sphere']

bpy.ops.object.select_all(action='DESELECT') # deselect all object

a.select_set(True)
b.select_set(True)     # select the object for the 'parenting'

bpy.context.view_layer.objects.active = a    # the active object will be the parent of all selected object

bpy.ops.object.parent_set(type='ARMATURE')
# Now The parent of b is a
