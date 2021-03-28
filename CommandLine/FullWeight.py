import os

import bpy
import bmesh

full_weight_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh/A'
#for each fbx in folder A
def LoopFBX(full_weight_path):
    # r=root, d=directories, f = files
    count = 0;
    for r, d, f in os.walk(full_weight_path):
        f.sort()
        for file in f:
            if file.lower().endswith(".fbx"):
                SetFullWeight(os.path.join(r, file))
                # print(os.path.join(r, file))

def SetFullWeight(source_fbx_path):
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
    a = bpy.data.objects[selection_names[0].name]
    print("vertex group count is : " + str(len(a.vertex_groups)))
    print("vertex group name is : " + a.vertex_groups[0].name)
    if len(a.vertex_groups) > 1:
        print("mutliple vg existing")
        return
    elif len(bpy.context.selected_objects)  == 0:
        print("no vg found in target fbx")
        return

    print("complete mesh validation, start setting weights")



    #set vertex group weight to 1 (most of time, it just has only one vertex group)




    # ob = bpy.ops.context.active_object
    # try:
    #     assert ob.vertex_groups
    #     print("vertex group count is : " + str(len(ob.vertex_groups)))
    # except:
    #     print("mesh has no vertex group")
    #     return
    #
    # for v in ob.data.vertices:
    #     # print(v.index)
    #     for grp in ob.vertex_groups:
    #         weight = grp.weight(v.index)
    #         # print('weight=', weight)
    #         try:
    #             grp.add([vgVerts.index], weight = 0.5)
    #         except:
    #             # print('err')
    #             continue
    # ob.data.update()



    # select and active Sphere
    # b = bpy.data.objects['QT0031Z']
    # b.select_set(True)
    # bpy.context.view_layer.objects.active = b
    #
    # bpy.ops.object.mode_set(mode='EDIT')
    # bpy.ops.mesh.select_all(action='SELECT')
    # bpy.ops.object.mode_set(mode='OBJECT')
    #
    # # clear all vertex group weight in Sphere
    # mode = bpy.context.active_object.mode
    # bpy.ops.object.mode_set(mode='OBJECT')
    # ob = bpy.context.active_object
    # selectedVerts = [v for v in ob.data.vertices if v.select]
    # for v in selectedVerts:
    #     for i, g in enumerate(v.groups):
    #         v.groups[i].weight = 1

    #export to target folder








# delete all default stuff
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)




LoopFBX(full_weight_path)



#save blend file
bpy.ops.wm.save_mainfile(filepath = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/TestFullWeight.blend')
