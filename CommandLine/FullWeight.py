import os

import bpy
import bmesh

full_weight_source_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh/A'
full_weight_target_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A'

body_mesh_path = r'/Users/ryancosean/Desktop/AvatarFBX/latest_model/model/body_zhongmo_0107.FBX'

#for each fbx in folder A
def LoopFBX(full_weight_source_path):
    # r=root, d=directories, f = files
    count = 0;
    for r, d, f in os.walk(full_weight_source_path):
        f.sort()
        for file in f:
            if file.lower().endswith(".fbx"):
                SetFullWeight(os.path.join(r, file), file)
                # print(os.path.join(r, file))

def SetFullWeight(source_fbx_path, file_name):

# delete all default stuff
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

# import source fbx
    source_mesh = bpy.ops.import_scene.fbx( filepath = body_mesh_path )
# delete source mesh
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete(use_global=False)

# import target mesh
    source_mesh = bpy.ops.import_scene.fbx(filepath=source_fbx_path)


###set target mesh parent to source armature
    a = bpy.data.objects['Bip001']
    #select the only mesh in scene
    bpy.ops.object.select_by_type(type='MESH')
    selection_names = bpy.context.selected_objects
    b = bpy.data.objects[selection_names[0].name]

    bpy.ops.object.select_all(action='DESELECT') # deselect all object

    a.select_set(True)
    b.select_set(True)     # select the object for the 'parenting'

    bpy.context.view_layer.objects.active = a    # the active object will be the parent of all selected object

    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
# Now The parent of b is a



    #active mesh object
    c = bpy.data.objects[selection_names[0].name]
    group = c.vertex_groups.new( name = 'Bip001_Spine1' )
    bpy.context.view_layer.objects.active = c
    Verts = [i.index for i in bpy.context.active_object.data.vertices]
    group.add( Verts, 1, 'REPLACE' )
    # c.save


###
    # modifier = b.modifiers.new(type='ARMATURE', name="Armature")
    # modifier.object = a
    # bpy.context.scene.objects.link(b)
    # bpy.context.scene.objects.active = b

    # ob = bpy.context.object
    # ob.modifiers.new(name = 'Bip001', type = 'ARMATURE')

    # ob = bpy.data.objects['MyObject']
    # a = bpy.data.objects['MyArmature']

    b.modifiers.new(name = 'Skeleton', type = 'ARMATURE')
    b.modifiers['Skeleton'].object = a
###









# deselect all object
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

# vaildate target fbx
    #check mesh count
    bpy.ops.object.select_by_type(type='MESH')
    print("mesh count is : " + str(len(bpy.context.selected_objects)))
    if len(bpy.context.selected_objects) > 1:
        print("mutliple mesh existing")
        return
    elif len(bpy.context.selected_objects)  == 0:
        print("no mesh found in target fbx")
        return

    #check vertex group count
    selection_names = bpy.context.selected_objects
    print(selection_names[0].name)
    mesh_root_name = selection_names[0].name
    a = bpy.data.objects[mesh_root_name]
    print("vertex group count is : " + str(len(a.vertex_groups)))
    print("vertex group name is : " + a.vertex_groups[0].name)
    if len(a.vertex_groups) > 1:
        print("mutliple vg existing")
        return
    elif len(bpy.context.selected_objects)  == 0:
        print("no vg found in target fbx")
        return

    #check fbx armature count
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='ARMATURE')
    print("ARMATURE count is : " + str(len(bpy.context.selected_objects)))

    if len(bpy.context.selected_objects) > 1:
        print("mutliple ARMATURE existing")
        return
    elif len(bpy.context.selected_objects) == 0:
        print("no ARMATURE found in target fbx")
        return


    print("armature_name is : " + bpy.context.selected_objects[0].name)
    armature_name = bpy.context.selected_objects[0].name
#####check armature is parent#####


    print("complete mesh validation, start setting weights")

#set vertex group weight to 1 (most of time, it just has only one vertex group)

    # deselect all object
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    d = bpy.data.objects[mesh_root_name]
    d.select_set(True)
    bpy.context.view_layer.objects.active = d

    #select all vertices, ready for vg assign
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    print("Selected all vertex")

    # set all vertex group weight in Sphere
    # mode = bpy.context.active_object.mode
    # bpy.ops.object.mode_set(mode='OBJECT')
    ob = bpy.context.active_object
    print(ob.name)
    selectedVerts = [v for v in ob.data.vertices if v.select]
    for v in selectedVerts:
        for i, g in enumerate(v.groups):
            print("Weight Setted 0.5")
            v.groups[i].weight = 0.5

# export to target folder
    #object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    #deselect all
    bpy.ops.object.select_all(action='DESELECT')

    #select target mesh
    a = bpy.data.objects[armature_name]
    a.select_set(True)
    #select target mesh's child
    children = [ob for ob in bpy.data.objects if ob.parent == a]
    for c in children:
        c.select_set(True)
        print("child name : " + c.name)

    #export target weighted fbx
    bpy.ops.export_scene.fbx(filepath="/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/" + file_name)
    print("file name: " + file_name + " fbx has exported")



LoopFBX(full_weight_source_path)



#save blend file
bpy.ops.wm.save_mainfile(filepath = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/TestFullWeight.blend')
