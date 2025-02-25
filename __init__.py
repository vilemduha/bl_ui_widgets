bl_info = {
    "name": "BL UI Widgets",
    "description": "UI Widgets to draw in the 3D view",
    "author": "Jayanam",
    "version": (0, 6, 3, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "category": "Object"}

# Blender imports
import bpy

from bpy.props import *

from . drag_panel_op import DP_OT_draw_operator

addon_keymaps = []

def register():
    
    bpy.utils.register_class(DP_OT_draw_operator)
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='3D View', space_type='VIEW_3D')
   
        kmi = km.keymap_items.new("object.dp_ot_draw_operator", 'F', 'PRESS', shift=True, ctrl=True)
        
        addon_keymaps.append((km, kmi))
   
def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
   
    bpy.utils.unregister_class(DP_OT_draw_operator)
    
if __name__ == "__main__":
    register()
