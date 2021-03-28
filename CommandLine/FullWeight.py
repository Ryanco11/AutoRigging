import os

import bpy
import bmesh

full_weight_source_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh/A'
full_weight_target_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A'
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
    source_mesh = bpy.ops.import_scene.fbx(filepath=source_fbx_path)

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
    b = bpy.data.objects[mesh_root_name]
    b.select_set(True)
    bpy.context.view_layer.objects.active = b

    #select all vertices, ready for vg assign
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    # clear all vertex group weight in Sphere
    mode = bpy.context.active_object.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    ob = bpy.context.active_object
    selectedVerts = [v for v in ob.data.vertices if v.select]
    for v in selectedVerts:
        for i, g in enumerate(v.groups):
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

    #export target weighted fbx
    bpy.ops.export_scene.fbx(filepath="/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/" + file_name, use_selection = True)
    print(file_name)



LoopFBX(full_weight_source_path)



#save blend file
bpy.ops.wm.save_mainfile(filepath = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/TestFullWeight.blend')
