import os
import sys
import bpy
import re

unweighted_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh'
weghted_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh'

source_weight_model_path = r'/Users/ryancosean/Desktop/AvatarFBX/latest_model/model/body_zhongmo_0107.FBX'
source_unweighted_model_path = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/UnweightedMesh/A/bladric.fbx'

#delete all default stuff
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


#import target mesh
bpy.ops.import_scene.fbx( filepath = source_unweighted_model_path )

#import source mesh
#avoid mess up targe mesh name
bpy.ops.import_scene.fbx( filepath = source_weight_model_path )

#apply weight

#object mode

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
# # bpy.ops.object.select_by_type(type='MESH')
# # bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
bpy.ops.export_scene.fbx(filepath="/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/weighted_baldric.FBX", use_selection = True)


#save blend file
bpy.ops.wm.save_mainfile(filepath = r'/Users/ryancosean/Documents/PycharmProjects/AutoRigging/AutoRigging/CommandLine/WeightedMesh/A/Test.blend')