import bpy
import re

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



#transfer body weight to cloth

bpy.ops.paint.weight_paint_toggle()
bpy.ops.object.data_transfer(use_reverse_transfer=True,data_type=('VGROUP_WEIGHTS'),layers_select_src=('NAME'),layers_select_dst=('ALL'))


#remove unused vertex group
ob = bpy.context.active_object
ob.update_from_editmode()

vgroup_used = {i: False for i, k in enumerate(ob.vertex_groups)}
vgroup_names = {i: k.name for i, k in enumerate(ob.vertex_groups)}

for v in ob.data.vertices:
    for g in v.groups:
        if g.weight > 0.0:
            vgroup_used[g.group] = True
            vgroup_name = vgroup_names[g.group]
            armatch = re.search('((.R|.L)(.(\d){1,}){0,1})(?!.)', vgroup_name)
            if armatch != None:
                tag = armatch.group()
                mirror_tag =  tag.replace(".R", ".L") if armatch.group(2) == ".R" else tag.replace(".L", ".R")
                mirror_vgname = vgroup_name.replace(tag, mirror_tag)
                for i, name in sorted(vgroup_names.items(), reverse=True):
                    if mirror_vgname == name:
                        vgroup_used[i] = True
                        break
for i, used in sorted(vgroup_used.items(), reverse=True):
    if not used:
        ob.vertex_groups.remove(ob.vertex_groups[i])