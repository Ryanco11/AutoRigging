import bpy

unweighted_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh'
weghted_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh'

source_weight_model_path = r'/Users/ryancosean/Desktop/AvatarFBX/latest_model/model/body_zhongmo_0107.FBX'
source_unweighted_model_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh/A/bladric.fbx'

#delete all default stuff
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


#import source mesh
source_mesh = bpy.ops.import_scene.fbx( filepath = source_unweighted_model_path )

#import target mesh
#import secondly, avoid mess up targe mesh name
target_mesh = bpy.ops.import_scene.fbx( filepath = source_weight_model_path )



#select weight apply order
    #object mode , deselect all
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
    #select all mesh
bpy.ops.object.select_by_type(type='MESH')
    #active source mesh
bpy.context.view_layer.objects.active = bpy.data.objects['QT0054Z']




#apply weight
bpy.ops.paint.weight_paint_toggle()
bpy.ops.object.data_transfer(use_reverse_transfer=True,data_type=('VGROUP_WEIGHTS'),layers_select_src=('NAME'),layers_select_dst=('ALL'))


#object mode
bpy.ops.object.mode_set(mode='OBJECT')

#deselect all
bpy.ops.object.select_all(action='DESELECT')

#select target mesh
a = bpy.data.objects['Bip001']
a.select_set(True)
#select target mesh's child
children = [ob for ob in bpy.data.objects if ob.parent == a]
for c in children:
    c.select_set(True)

#export target weighted fbx
bpy.ops.export_scene.fbx(filepath="/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/weighted_baldric.FBX", use_selection = True)





#save blend file
bpy.ops.wm.save_mainfile(filepath = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/Test.blend')
