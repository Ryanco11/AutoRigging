import os

import bpy
import bmesh

full_weight_source_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh/B'
full_weight_target_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/B'
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

# import target mesh
    source_mesh = bpy.ops.import_scene.fbx(filepath = source_fbx_path)

# vaildate target fbx
    # check mesh count
    bpy.ops.object.select_by_type(type='MESH')
    print("mesh count is : " + str(len(bpy.context.selected_objects)))
    if len(bpy.context.selected_objects) > 1:
        print("mutliple mesh existing")
        return
    elif len(bpy.context.selected_objects) == 0:
        print("no mesh found in target fbx")
        return

    # check vertex group count
    selection_names = bpy.context.selected_objects
    print(selection_names[0].name)
    mesh_root_name = selection_names[0].name
    a = bpy.data.objects[mesh_root_name]
    print("vertex group count is : " + str(len(a.vertex_groups)))
    print("vertex group name is : " + a.vertex_groups[0].name)
    # if len(a.vertex_groups) > 1:
    #     print("mutliple vg existing")
    #     return
    if len(bpy.context.selected_objects) == 0:
        print("no vg found in target fbx")
        return

    # check fbx armature count
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

# import body mesh
    body_mesh = bpy.ops.import_scene.fbx(filepath = body_mesh_path)

# deselect all object
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')


    print("complete mesh validation, start setting weights")


    #######define geomtory for each bone
    ###apply weight to each bone