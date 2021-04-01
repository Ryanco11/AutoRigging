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

    # set b's parent to a
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)


    print("complete mesh validation, start setting weights")


    ###chairfy which bone need to be used
    ###define geomtory for each bone
    ###apply weight to each bone