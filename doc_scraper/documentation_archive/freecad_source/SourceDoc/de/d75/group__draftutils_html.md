---
url: https://freecad.github.io/SourceDoc/de/d75/group__draftutils.html
scraped_at: 2025-09-08T14:52:05.999693
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Namespaces | Functions | Variables

draftutils

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Draft](../../d1/d35/group__DRAFT.html)

Utility modules that are used throughout the workbench. More...

##  Classes  
  
---  
class | [draftutils.todo.ToDo](../../da/da9/classdraftutils_1_1todo_1_1ToDo.html)  
  
##  Namespaces  
  
---  
namespace | [groups](../../d5/d3f/namespacegroups.html)  
| Provides utility functions to do operations with groups.  
  
namespace | [gui_utils](../../d9/d55/namespacegui__utils.html)  
| Provides utility functions that deal with GUI interactions.  
  
namespace | [init_draft_statusbar](../../d4/d98/namespaceinit__draft__statusbar.html)  
| Provides the initialization code for the workbench's status bar.  
  
namespace | [init_tools](../../d2/d31/namespaceinit__tools.html)  
| Provides lists of commands to set up toolbars of the workbench.  
  
namespace | [messages](../../dc/dc5/namespacemessages.html)  
| Provides utility functions that wrap around the Console methods.  
  
namespace | [todo](../../d7/d9f/namespacetodo.html)  
| Provides the ToDo static class to run commands with a time delay.  
  
namespace | [translate](../../d3/d32/namespacetranslate.html)  
| Provides utility functions that wrap around the Qt translate function.  
  
namespace | [units](../../dc/def/namespaceunits.html)  
| Provides utility functions to handle quantities and units.  
  
namespace | [utils](../../d6/d84/namespaceutils.html)  
| Provides general utility functions used throughout the workbench.  
  
  
##  Functions  
  
---  
def | [draftutils.gui_utils.autogroup](../../de/d75/group__draftutils.html#ga8f2e288844e0f5b5541369cae030f093) (obj)  
def | [draftutils.utils.compare_objects](../../de/d75/group__draftutils.html#gafb4412c803de5002eeaf01ce143f80b9) (obj1, obj2)  
def | [draftutils.gui_utils.dim_dash](../../de/d75/group__draftutils.html#gada3a166fa5d025f2c2bed4feca118166) (p1, p2)  
def | [draftutils.gui_utils.dim_symbol](../../de/d75/group__draftutils.html#ga1da14e7d5c8414fff08d776db07b6558) (symbol=None, invert=False)  
def | [draftutils.units.display_external](../../de/d75/group__draftutils.html#gac1fd8df42886d027fec6f692b158b211) (internal_value, decimals=None, dim='Length', showUnit=True, unit=None)  
def | [draftutils.utils.epsilon](../../de/d75/group__draftutils.html#ga7ca4044874669855d2291d7990debb22) ()  
def | [draftutils.utils.filter_objects_for_modifiers](../../de/d75/group__draftutils.html#ga9cca671c257ff64d8ce29eead3116f0a) (objects, isCopied=False)  
def | [draftutils.utils.find_doc](../../de/d75/group__draftutils.html#ga30517414bc209fb6f41046dee6461b6d) (doc=None)  
def | [draftutils.utils.find_object](../../de/d75/group__draftutils.html#ga8e52dd8d3dd2b3aeca480516a3112440) (obj, doc=None)  
def | [draftutils.gui_utils.format_object](../../de/d75/group__draftutils.html#gae12ae9fb772391933245e74c4c29e136) (target, origin=None)  
def | [draftutils.gui_utils.get_3d_view](../../de/d75/group__draftutils.html#gad1f55ea6876f55797fdc080ff3d7773a) ()  
def | [draftutils.gui_utils.get_bbox](../../de/d75/group__draftutils.html#ga1dc7f92b96529e39510fa55624160e72) (obj, debug=False)  
def | [draftutils.utils.get_clone_base](../../de/d75/group__draftutils.html#ga4d043914ddb50c2150b893b9f7edc741) (obj, strict=False, recursive=True)  
def | [draftutils.units.get_default_unit](../../de/d75/group__draftutils.html#ga0d7ec14fc8988387fa4bfb8cb91b746b) (dim)  
def | [draftutils.init_tools.get_draft_annotation_commands](../../de/d75/group__draftutils.html#ga47356f3525633e67d82954c73ced9de7) ()  
def | [draftutils.init_tools.get_draft_context_commands](../../de/d75/group__draftutils.html#ga2e27a6ebc21b7222072ef4a4848920b7) ()  
def | [draftutils.init_tools.get_draft_drawing_commands](../../de/d75/group__draftutils.html#gaaeaa1509b48106f3074c10ad751c6c8a) ()  
def | [draftutils.init_tools.get_draft_modification_commands](../../de/d75/group__draftutils.html#gaae36432ef61ded1fe51f4fa83683f4bd) ()  
def | [draftutils.init_tools.get_draft_snap_commands](../../de/d75/group__draftutils.html#ga09c63eaa2c0be4fd0bcd4ef095209670) ()  
def | [draftutils.init_tools.get_draft_snap_tooltips](../../de/d75/group__draftutils.html#ga2270455895fb27dae688e6042ebc7b1a) ()  
def | [draftutils.init_tools.get_draft_utility_commands_menu](../../de/d75/group__draftutils.html#ga4d08e6cee48e20aba658c600b87e02c2) ()  
def | [draftutils.init_tools.get_draft_utility_commands_toolbar](../../de/d75/group__draftutils.html#ga55ba49ff268a051c7e43aa10215e76bc) ()  
def | [draftutils.groups.get_group_contents](../../de/d75/group__draftutils.html#ga25f32b5a5e345a413adc13b0d702254f) (objectslist, walls=False, addgroups=False, spaces=False, noarchchild=False)  
def | [draftutils.groups.get_group_names](../../de/d75/group__draftutils.html#ga1c3d816788e6c9d5580579c98991ca46) (doc=None)  
def | [draftutils.groups.get_movable_children](../../de/d75/group__draftutils.html#ga46ab9ffdc6b3888f9f9a6e46debc1e6f) (objectslist, recursive=True)  
def | [draftutils.utils.get_objects_of_type](../../de/d75/group__draftutils.html#gacc0d5765c8f794e939bf2285d009ab34) (objects, typ)  
def | [draftutils.utils.get_param](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530) ([param](../../de/d75/group__draftutils.html#ga60ef2aed746377cb2ec6826bd7d7a1b2), default=None)  
def | [draftutils.utils.get_param_type](../../de/d75/group__draftutils.html#gafacfb13dcf3a6290dfa25623703c1e02) ([param](../../de/d75/group__draftutils.html#ga60ef2aed746377cb2ec6826bd7d7a1b2))  
def | [draftutils.utils.get_real_name](../../de/d75/group__draftutils.html#ga1ceb579c51b5f1f4747c78baac87d07a) (name)  
def | [draftutils.utils.get_rgb](../../de/d75/group__draftutils.html#gaae54b3e46d1d402a69f707bcbbe2128b) (color, testbw=True)  
def | [draftutils.init_draft_statusbar.get_scales](../../de/d75/group__draftutils.html#ga6d74b9b823c44dd034ab0df1af87f866) (unit_system=0)  
def | [draftutils.gui_utils.get_selection](../../de/d75/group__draftutils.html#ga8196bdfd06b6c271ac4039c2256d3b2f) (gui=App.GuiUp)  
def | [draftutils.gui_utils.get_selection_ex](../../de/d75/group__draftutils.html#ga6b24f6a655e74e0d1e1e013f3187a996) (gui=App.GuiUp)  
def | [draftutils.utils.get_type](../../de/d75/group__draftutils.html#gae98fd9ba514d4b735e2f52ddf54607b9) (obj)  
def | [draftutils.groups.get_windows](../../de/d75/group__draftutils.html#ga67d81fda8653a1fd1892590f6b519298) (obj)  
def | [draftutils.groups.getGroupContents](../../de/d75/group__draftutils.html#ga34d1d4e13fb85f7269caa8e4ee2d0fe1) (objectslist, walls=False, addgroups=False, spaces=False, noarchchild=False)  
def | [draftutils.groups.getGroupNames](../../de/d75/group__draftutils.html#ga03d74c45e33815a40fe54ed5792d7c78) ()  
def | [draftutils.groups.getMovableChildren](../../de/d75/group__draftutils.html#ga4b58928d88c63959cae37ba39f39100d) (objectslist, recursive=True)  
def | [draftutils.init_draft_statusbar.hide_draft_statusbar](../../de/d75/group__draftutils.html#gac0e8c313e17d21241092d7c86148def2) ()  
def | [draftutils.init_draft_statusbar.init_draft_statusbar_scale](../../de/d75/group__draftutils.html#ga93f646640439b1f18198344acf7b3bce) ()  
def | [draftutils.init_draft_statusbar.init_draft_statusbar_snap](../../de/d75/group__draftutils.html#ga4513dd995c3df83b2d848e4b4a39d941) ()  
def | [draftutils.init_tools.init_menu](../../de/d75/group__draftutils.html#gaf5d8a4270f89e875b36d4455729dc9f5) (workbench, menu_list, cmd_list)  
def | [draftutils.init_tools.init_toolbar](../../de/d75/group__draftutils.html#gaa263438b95c4297fb1baaa32026e8013) (workbench, toolbar, cmd_list)  
def | [draftutils.utils.is_clone](../../de/d75/group__draftutils.html#gadbc339c73fd10df484a1ff3e77dbc8fe) (obj, objtype=None, recursive=False)  
def | [draftutils.utils.is_closed_edge](../../de/d75/group__draftutils.html#gacfa15ea8d3449fa2f22b19842e3d4a8c) (edge_index, [object](../../dc/dd8/classobject.html))  
def | [draftutils.groups.is_group](../../de/d75/group__draftutils.html#ga73eabe89d5e43bfbaaf251d5fa1ec2b4) (obj)  
def | [draftutils.init_draft_statusbar.label_to_scale](../../de/d75/group__draftutils.html#ga3d11c3091f5430248c1edf90ac6dca63) (label)  
def | [draftutils.utils.load_svg_patterns](../../de/d75/group__draftutils.html#ga5ede6da8d3035b698c3f882c43cf4d69) ()  
def | [draftutils.gui_utils.load_texture](../../de/d75/group__draftutils.html#gafafb93128d4d59f97fffd3d0c83ec681) (filename, size=None, gui=App.GuiUp)  
def | [draftutils.units.make_format_spec](../../de/d75/group__draftutils.html#gae428916f8b3be3519e13af51e7ea8fd9) (decimals=4, dim='Length')  
def | [draftutils.gui_utils.migrate_text_display_mode](../../de/d75/group__draftutils.html#ga335bdede9357309edd6291864355d60a) (obj_type="Text", mode="3D text", doc=None)  
def | [draftutils.utils.precision](../../de/d75/group__draftutils.html#gab69b9d198a735e396d938b8fc96a1585) ()  
def | [draftutils.utils.print_header](../../de/d75/group__draftutils.html#ga417b1ace9f25755b7cdf1eb107737864) (name, description, debug=True)  
def | [draftutils.utils.print_shape](../../de/d75/group__draftutils.html#ga345aba753e9ec774075c1bdec299633d) (shape)  
def | [draftutils.gui_utils.remove_hidden](../../de/d75/group__draftutils.html#gaba028dfc9b80647b511e41c0d233106f) (objectslist)  
def | [draftutils.init_draft_statusbar.scale_to_label](../../de/d75/group__draftutils.html#gaef14a833a1d3e2b8c62834cf8c1151a7) (scale)  
def | [draftutils.gui_utils.select](../../de/d75/group__draftutils.html#gaca3dfa9c8520968dedf9ca5964291b52) (objs=None, gui=App.GuiUp)  
def | [draftutils.utils.set_param](../../de/d75/group__draftutils.html#ga01641daa7576c696849ca6fcfc3fb350) ([param](../../de/d75/group__draftutils.html#ga60ef2aed746377cb2ec6826bd7d7a1b2), value)  
def | [draftutils.utils.shapify](../../de/d75/group__draftutils.html#ga8d556e0d018860c71069d9f3ac299783) (obj)  
def | [draftutils.init_draft_statusbar.show_draft_statusbar](../../de/d75/group__draftutils.html#gae21abff2e1c825112cba034cc82a3822) ()  
def | [draftutils.utils.string_encode_coin](../../de/d75/group__draftutils.html#ga6671a36b7e113481feb4f990415d694c) (ustr)  
def | [draftutils.utils.svg_patterns](../../de/d75/group__draftutils.html#gad668ee3ba955aea7dcb8fd72a6e148b7) ()  
def | [draftutils.utils.tolerance](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e) ()  
def | [draftutils.translate.translate](../../de/d75/group__draftutils.html#ga401299ca851f4d4ee86937e756dc21d4) (context, text, utf8_decode=False)  
def | [draftutils.utils.type_check](../../de/d75/group__draftutils.html#ga9a7119e1e423a5bdf6a4505663eaf363) (args_and_types, name="?")  
def | [draftutils.groups.ungroup](../../de/d75/group__draftutils.html#ga81fec1f995ea2967d99ab012ed241dcc) (obj)  
def | [draftutils.utils.use_instead](../../de/d75/group__draftutils.html#ga9c0290eb39293ebe5b10cdc018a75310) (function, version="")  
def | [draftutils.utils.utf8_decode](../../de/d75/group__draftutils.html#ga65481f0e89b6495a5ea0c7a428fc7cb7) (text)  
  
##  Variables  
  
---  
dictionary | [draftutils.utils.ANNOTATION_STYLE](../../de/d75/group__draftutils.html#ga4cbd787cd6d880e7b231adfaff0bdde8)  
list | [draftutils.utils.ARROW_TYPES](../../de/d75/group__draftutils.html#gabe84c400a239bc3508311db7c5c568ce) = ["Dot", "[Circle](../../d8/d53/classCircle.html)", "Arrow", "Tick", "Tick-2"]  
list | [draftutils.utils.arrowtypes](../../de/d75/group__draftutils.html#gab4b0fb6667ce0b91b5a70c321c80f3c8) = [ARROW_TYPES](../../de/d75/group__draftutils.html#gabe84c400a239bc3508311db7c5c568ce)  
def | [draftutils.utils.compareObjects](../../de/d75/group__draftutils.html#ga85c68d23cdd776cfc08c646804758520) = [compare_objects](../../de/d75/group__draftutils.html#gafb4412c803de5002eeaf01ce143f80b9)  
def | [draftutils.gui_utils.dimDash](../../de/d75/group__draftutils.html#gad503f093e4e963eee22342a9becb6e38) = [dim_dash](../../de/d75/group__draftutils.html#gada3a166fa5d025f2c2bed4feca118166)  
def | [draftutils.gui_utils.dimSymbol](../../de/d75/group__draftutils.html#gad0a1bfe7e4b1b68cef7e268c165fd09e) = [dim_symbol](../../de/d75/group__draftutils.html#ga1da14e7d5c8414fff08d776db07b6558)  
def | [draftutils.units.displayExternal](../../de/d75/group__draftutils.html#ga08e52251be6c84126ee256279d785a19) = [display_external](../../de/d75/group__draftutils.html#gac1fd8df42886d027fec6f692b158b211)  
list | [draftutils.init_draft_statusbar.draft_scales_arch_imperial](../../de/d75/group__draftutils.html#ga4c08eb99171647758d421560031fa238)  
list | [draftutils.init_draft_statusbar.draft_scales_eng_imperial](../../de/d75/group__draftutils.html#ga6dbc6094794d2b7f70181f15f6534873)  
list | [draftutils.init_draft_statusbar.draft_scales_metrics](../../de/d75/group__draftutils.html#gae3c5b95531fb50c247b325fa83ddd4d8)  
def | [draftutils.utils.filterObjectsForModifiers](../../de/d75/group__draftutils.html#gaf63d4c00a114a066e28135361874baae) = [filter_objects_for_modifiers](../../de/d75/group__draftutils.html#ga9cca671c257ff64d8ce29eead3116f0a)  
def | [draftutils.gui_utils.formatObject](../../de/d75/group__draftutils.html#ga332b5e850e104f8cc60d36b69f11ec4e) = [format_object](../../de/d75/group__draftutils.html#gae12ae9fb772391933245e74c4c29e136)  
def | [draftutils.gui_utils.get3DView](../../de/d75/group__draftutils.html#ga6619cdff6036ee242ec27f1e3d3edb60) = [get_3d_view](../../de/d75/group__draftutils.html#gad1f55ea6876f55797fdc080ff3d7773a)  
def | [draftutils.utils.getCloneBase](../../de/d75/group__draftutils.html#gadfdb4365223a013d4a5bfcf760f541c6) = [get_clone_base](../../de/d75/group__draftutils.html#ga4d043914ddb50c2150b893b9f7edc741)  
def | [draftutils.units.getDefaultUnit](../../de/d75/group__draftutils.html#gae6079889c3c77ef5ea4e00bc151ff487) = [get_default_unit](../../de/d75/group__draftutils.html#ga0d7ec14fc8988387fa4bfb8cb91b746b)  
def | [draftutils.utils.getObjectsOfType](../../de/d75/group__draftutils.html#gaa49d4b57ec1ee5156a791420c5bc3481) = [get_objects_of_type](../../de/d75/group__draftutils.html#gacc0d5765c8f794e939bf2285d009ab34)  
def | [draftutils.utils.getParam](../../de/d75/group__draftutils.html#gaa2e66fde65fd9a8f9424bdd7660b0def) = [get_param](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530)  
def | [draftutils.utils.getParamType](../../de/d75/group__draftutils.html#ga98afed1eba3ce8d18d8a666dd592dcfe) = [get_param_type](../../de/d75/group__draftutils.html#gafacfb13dcf3a6290dfa25623703c1e02)  
def | [draftutils.utils.getRealName](../../de/d75/group__draftutils.html#gabd3fbce3003fa71b67b8b81eef56a43f) = [get_real_name](../../de/d75/group__draftutils.html#ga1ceb579c51b5f1f4747c78baac87d07a)  
def | [draftutils.utils.getrgb](../../de/d75/group__draftutils.html#gac83ffe098e83a06c32597704dfeb7050) = [get_rgb](../../de/d75/group__draftutils.html#gaae54b3e46d1d402a69f707bcbbe2128b)  
def | [draftutils.gui_utils.getSelection](../../de/d75/group__draftutils.html#gaa7be07c4b4fb41c3a5a442a9c5f85e2b) = [get_selection](../../de/d75/group__draftutils.html#ga8196bdfd06b6c271ac4039c2256d3b2f)  
def | [draftutils.gui_utils.getSelectionEx](../../de/d75/group__draftutils.html#ga5e10006927dba21622a83c5f6d42829a) = [get_selection_ex](../../de/d75/group__draftutils.html#ga6b24f6a655e74e0d1e1e013f3187a996)  
def | [draftutils.utils.getType](../../de/d75/group__draftutils.html#ga99f7d10185bcca601667740968742397) = [get_type](../../de/d75/group__draftutils.html#gae98fd9ba514d4b735e2f52ddf54607b9)  
def | [draftutils.utils.isClone](../../de/d75/group__draftutils.html#gab720d4164f304346ac35999d01180f91) = [is_clone](../../de/d75/group__draftutils.html#gadbc339c73fd10df484a1ff3e77dbc8fe)  
def | [draftutils.utils.isClosedEdge](../../de/d75/group__draftutils.html#ga31cfdf9f5e26bdf25c9f0fb8662f9dcb) = [is_closed_edge](../../de/d75/group__draftutils.html#gacfa15ea8d3449fa2f22b19842e3d4a8c)  
def | [draftutils.utils.loadSvgPatterns](../../de/d75/group__draftutils.html#gadca8ee54e0ba10ecfa0f25e6e52ad7ff) = [load_svg_patterns](../../de/d75/group__draftutils.html#ga5ede6da8d3035b698c3f882c43cf4d69)  
def | [draftutils.gui_utils.loadTexture](../../de/d75/group__draftutils.html#gaea738683729f126de679c018263dfd26) = [load_texture](../../de/d75/group__draftutils.html#gafafb93128d4d59f97fffd3d0c83ec681)  
def | [draftutils.units.makeFormatSpec](../../de/d75/group__draftutils.html#gacae5d0978c76a83af2478c816ecc1779) = [make_format_spec](../../de/d75/group__draftutils.html#gae428916f8b3be3519e13af51e7ea8fd9)  
|
[draftutils.utils.param](../../de/d75/group__draftutils.html#ga60ef2aed746377cb2ec6826bd7d7a1b2)
= App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft")  
def | [draftutils.utils.printShape](../../de/d75/group__draftutils.html#gaacea415eb31efbde3d6b74f49dc83926) = [print_shape](../../de/d75/group__draftutils.html#ga345aba753e9ec774075c1bdec299633d)  
|
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4)
= QtCore.QT_TRANSLATE_NOOP  
|
[draftutils.translate.Qtranslate](../../de/d75/group__draftutils.html#gad400e273e5f66ec66c7a982fb2238426)
= QtCore.QCoreApplication.translate  
def | [draftutils.gui_utils.removeHidden](../../de/d75/group__draftutils.html#ga5553481e4c021d47b3a2b3d21707fe51) = [remove_hidden](../../de/d75/group__draftutils.html#gaba028dfc9b80647b511e41c0d233106f)  
def | [draftutils.utils.setParam](../../de/d75/group__draftutils.html#gae5ced51253dff30d35abf88605cb5173) = [set_param](../../de/d75/group__draftutils.html#ga01641daa7576c696849ca6fcfc3fb350)  
def | [draftutils.utils.stringencodecoin](../../de/d75/group__draftutils.html#gac5e8e096a4a95e7b2e8b6b4a046ddb08) = [string_encode_coin](../../de/d75/group__draftutils.html#ga6671a36b7e113481feb4f990415d694c)  
def | [draftutils.utils.svgpatterns](../../de/d75/group__draftutils.html#ga3e0089d0f85039a671da1a13e374a4c3) = [svg_patterns](../../de/d75/group__draftutils.html#gad668ee3ba955aea7dcb8fd72a6e148b7)  
|
[draftutils.todo.todo](../../de/d75/group__draftutils.html#gaa8dda7170290338fe72eab551dd147ac)
= [ToDo](../../da/da9/classdraftutils_1_1todo_1_1ToDo.html)  
def | [draftutils.utils.typecheck](../../de/d75/group__draftutils.html#gad21382f7929418da05fce51aa5323fc7) = [type_check](../../de/d75/group__draftutils.html#ga9a7119e1e423a5bdf6a4505663eaf363)  
  
## Detailed Description

Utility modules that are used throughout the workbench.

## Function Documentation

## ◆ autogroup()

def draftutils.gui_utils.autogroup  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Add a given object to the defined Draft autogroup, if applicable.
    
    This function only works if the graphical interface is available.
    It checks that the `App.draftToolBar` class is available,
    which contains the group to use to automatically store
    new created objects.
    
    Originally, it worked with standard groups (`App::DocumentObjectGroup`),
    and Arch Workbench containers like `'Site'`, `'Building'`, `'Floor'`,
    and `'BuildingPart'`.
    
    Now it works with Draft Layers.
    
    Parameters
    ----------
    obj: App::DocumentObject
        Any type of object that will be stored in the group.
    

## ◆ compare_objects()

def draftutils.utils.compare_objects  | ( |  | _obj1_ ,   
---|---|---|---  
|  |  | _obj2_  
| ) | |   
      
    
    Print the differences between 2 objects.
    
    The two objects are compared through their `TypeId` attribute,
    or by using the `get_type` function.
    
    If they are the same type their properties are compared
    looking for differences.
    
    Neither `Shape` nor `Label` attributes are compared.
    
    Parameters
    ----------
    obj1 : App::DocumentObject
        Any type of scripted object.
    obj2 : App::DocumentObject
        Any type of scripted object.
    

References
[draftutils.utils.get_type()](../../de/d75/group__draftutils.html#gae98fd9ba514d4b735e2f52ddf54607b9),
and
[draftutils.utils.getType](../../de/d75/group__draftutils.html#ga99f7d10185bcca601667740968742397).

## ◆ dim_dash()

def draftutils.gui_utils.dim_dash  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_  
| ) | |   
      
    
    Return a SoSeparator with a line used to make dimension dashes.
    
    It is used by `dim_symbol` to create line end symbols
    like `'Tick-2'`, `'DimOvershoot'`, and `'ExtOvershoot'` dashes.
    
    Parameters
    ----------
    p1: tuple of three floats or Base::Vector3
        A point to define a line vertex.
    
    p2: tuple of three floats or Base::Vector3
        A point to define a line vertex.
    
    Returns
    -------
    Coin.SoSeparator
        A Coin object with a `SoLineSet` created from `p1` and `p2`
        as vertices.
    

Referenced by
[draftutils.gui_utils.dim_symbol()](../../de/d75/group__draftutils.html#ga1da14e7d5c8414fff08d776db07b6558).

## ◆ dim_symbol()

def draftutils.gui_utils.dim_symbol  | ( |  | _symbol_ = `None`,   
---|---|---|---  
|  |  | _invert_ = `False`  
| ) | |   
      
    
    Return the specified dimension symbol.
    
    Parameters
    ----------
    symbol: int, optional
        It defaults to `None`, in which it gets the value from the parameter
        database, `get_param("dimsymbol", 0)`.
    
        A numerical value defines different markers
         * 0, `SoSphere`
         * 1, `SoSeparator` with a `SoLineSet`, a circle (in fact a 24 sided polygon)
         * 2, `SoSeparator` with a `soCone`
         * 3, `SoSeparator` with a `SoFaceSet`
         * 4, `SoSeparator` with a `SoLineSet`, calling `dim_dash`
         * Otherwise, `SoSphere`
    
    invert: bool, optional
        It defaults to `False`.
        If it is `True` and `symbol=2`, the cone will be rotated
        -90 degrees around the Z axis, otherwise the rotation is positive,
        +90 degrees.
    
    Returns
    -------
    Coin.SoNode
        A `Coin.SoSphere`, or `Coin.SoSeparator` (circle, cone, face, line)
        that will be used as a dimension symbol.
    

References
[draftutils.gui_utils.dim_dash()](../../de/d75/group__draftutils.html#gada3a166fa5d025f2c2bed4feca118166),
and
[draftutils.utils.get_param()](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530).

## ◆ display_external()

def draftutils.units.display_external  | ( |  | _internal_value_ ,   
---|---|---|---  
|  |  | _decimals_ = `None`,   
|  |  | _dim_ = `'Length'`,   
|  |  | _showUnit_ = `True`,   
|  |  | _unit_ = `None`  
| ) | |   
      
    
    Return a converted value for display, according to the unit schema.
    
    Parameters
    ----------
    internal_value: float
        A value that will be transformed depending on the other parameters.
    
    decimals: float, optional
        It defaults ot `None`, in which case, the decimals are 2.
    
    dim: str, optional
        It defaults to `'Length'`. It can also be `'Angle'`.
    
    showUnit: bool, optional
        It defaults to `True`.
        If it is `False` it won't show the unit.
    
    unit: str, optional
        A unit string such as `'mm'`, `'cm'`, `'m'`, `'in'`, `'ft'`,
        in which to express the returned value.
    

## ◆ epsilon()

def draftutils.utils.epsilon  | ( | | ) |   
---|---|---|---|---  
      
    
    Return a small number based on the tolerance for use in comparisons.
    
    The epsilon value is used in floating point comparisons. Use with caution.
    ::
        denom = 10**tolerance
        num = 1
        epsilon = num/denom
    
    Returns
    -------
    float
        1/(10**tolerance)
    

References
[draftutils.utils.tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

Referenced by
[MeshCore::LMCylinderFunctor.df()](../../d9/d01/structMeshCore_1_1LMCylinderFunctor.html#a7f47d0b03bba1e716e8beec74ab6dee4),
[Base::Vector3< double
>.DistanceToLine()](../../d1/d13/classBase_1_1Vector3.html#af38176c3192c969e1ae2255a84885b8a),
[Base::Vector3< _Precision
>.epsilon()](../../d1/d13/classBase_1_1Vector3.html#afc0aba7a73e8528bb4a5ffa9d7c1429a),
[PartGui::ArcEngine.evaluate()](../../d8/d2e/classPartGui_1_1ArcEngine.html#a8a07c0c847924c8cf83740e36bfeab44),
[PartGui.evaluateAngularPreSelection()](../../d5/d49/namespacePartGui.html#af0dc1ad1549a7fac118db816447cb551),
[VISCOUS_3D::_LayerEdge.FindIntersection()](../../d9/df6/structVISCOUS__3D_1_1__LayerEdge.html#a32897cfd9a14875af5bbd2de96eb40dc),
[Base::Vector3< _Precision
>.GetAngle()](../../d1/d13/classBase_1_1Vector3.html#aa7649aaf126c62148c8ebc54ad38ce27),
[Base::BoundBox3< _Precision
>.IntersectionPoint()](../../d8/d12/classBase_1_1BoundBox3.html#a49b3e75c0752b639e1efa1a3b2a01e74),
[MeshCore::MeshGeomFacet.IsDegenerated()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#af0daeef7f7d06e0377d914b2e1c83f05),
[geoff_geometry.quadratic()](../../de/d5d/namespacegeoff__geometry.html#a42e3f945a337216dfe27f3fbe24a587d),
[geoff_geometry::Vector3d.setCartesianAxes()](../../d1/d95/classgeoff__geometry_1_1Vector3d.html#a4b380049b7792a2342f71193aeecdeb4),
and
[FemGui::ViewProviderFemPostObject.setRangeOfColorBar()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a78820f7a16d535584c8739470c090795).

## ◆ filter_objects_for_modifiers()

def draftutils.utils.filter_objects_for_modifiers  | ( |  | _objects_ ,   
---|---|---|---  
|  |  | _isCopied_ = `False`  
| ) | |   
  
References
[Gui.getMainWindow()](../../d9/dad/namespaceGui.html#ad7c580188be626079e659ab6514fcd92).

## ◆ find_doc()

def draftutils.utils.find_doc  | ( |  | _doc_ = `None`| ) |   
---|---|---|---|---|---  
      
    
    Return the active document or find a document by name.
    
    Parameters
    ----------
    doc: App::Document or str, optional
        The document that will be searched in the session.
        It defaults to `None`, in which case it tries to find
        the active document.
        If `doc` is a string, it will try to get the document by `Name`.
    
    Returns
    -------
    bool, App::Document
        A tuple containing the information on whether the search
        was successful. In this case, the boolean is `True`,
        and the second value is the document instance.
    
    False, None
        If there is no active document, or the string in `doc`
        doesn't correspond to an open document in the session.
    

Referenced by
[draftutils.utils.find_object()](../../de/d75/group__draftutils.html#ga8e52dd8d3dd2b3aeca480516a3112440).

## ◆ find_object()

def draftutils.utils.find_object  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _doc_ = `None`  
| ) | |   
      
    
    Find object in the document, inclusive by Label.
    
    Parameters
    ----------
    obj: App::DocumentObject or str
        The object to search in `doc`.
        Or if the `obj` is a string, it will search the object by `Label`.
        Since Labels are not guaranteed to be unique, it will get the first
        object with that label in the document.
    
    doc: App::Document or str, optional
        The document in which the object will be searched.
        It defaults to `None`, in which case it tries to search in the
        active document.
        If `doc` is a string, it will search the document by `Name`.
    
    Returns
    -------
    bool, App::DocumentObject
        A tuple containing the information on whether the search
        was successful. In this case, the boolean is `True`,
        and the second value is the object found.
    
    False, None
        If the object doesn't exist in the document.
    

References
[draftutils.utils.find_doc()](../../de/d75/group__draftutils.html#ga30517414bc209fb6f41046dee6461b6d).

## ◆ format_object()

def draftutils.gui_utils.format_object  | ( |  | _target_ ,   
---|---|---|---  
|  |  | _origin_ = `None`  
| ) | |   
      
    
    Apply visual properties from the Draft toolbar or another object.
    
    This function only works if the graphical interface is available
    as the visual properties are attributes of the view provider
    (`obj.ViewObject`).
    
    Parameters
    ----------
    target: App::DocumentObject
        Any type of scripted object.
    
        This object will adopt the applicable visual properties,
        `FontSize`, `TextColor`, `LineWidth`, `PointColor`, `LineColor`,
        and `ShapeColor`, defined in the Draft toolbar
        (`Gui.draftToolBar`) or will adopt
        the properties from the `origin` object.
    
        The `target` is also placed in the construction group
        if the construction mode in the Draft toolbar is active.
    
    origin: App::DocumentObject, optional
        It defaults to `None`.
        If it exists, it will provide the visual properties to assign
        to `target`, with the exception of `BoundingBox`, `Proxy`,
        `RootNode` and `Visibility`.
    

## ◆ get_3d_view()

def draftutils.gui_utils.get_3d_view  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the current 3D view.
    
    Returns
    -------
    Gui::View3DInventor
        Return the current `ActiveView` in the active document,
        or the first `Gui::View3DInventor` view found.
    
        Return `None` if the graphical interface is not available.
    

## ◆ get_bbox()

def draftutils.gui_utils.get_bbox  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _debug_ = `False`  
| ) | |   
      
    
    Return a BoundBox from any object that has a Coin RootNode.
    
    Normally the bounding box of an object can be taken
    from its `Part::TopoShape`.
    ::
        >>> print(obj.Shape.BoundBox)
    
    However, for objects without a `Shape`, such as those
    derived from `App::FeaturePython` like `Draft Text` and `Draft Dimension`,
    the bounding box can be calculated from the `RootNode` of the viewprovider.
    
    Parameters
    ----------
    obj: App::DocumentObject
        Any object that has a `ViewObject.RootNode`.
    
    Returns
    -------
    Base::BoundBox
        It returns a `BoundBox` object which has information like
        minimum and maximum values of X, Y, and Z, as well as bounding box
        center.
    
    None
        If there is a problem it will return `None`.
    

## ◆ get_clone_base()

def draftutils.utils.get_clone_base  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _strict_ = `False`,   
|  |  | _recursive_ = `True`  
| ) | |   
      
    
    Return the object cloned by this object, if any.
    
    Parameters
    ----------
    obj: App::DocumentObject
        Any type of object.
    
    strict: bool, optional
        It defaults to `False`.
        If it is `True`, and this object is not a clone,
        this function will return `False`.
    
    recursive: bool, optional
        It defaults to `True`
        If it is `True`, it call recursively to itself to
        get base object and if it is `False` then it just
        return base object, not call recursively to find
        base object.
    
    Returns
    -------
    App::DocumentObject
        It `obj` is a `Draft Clone`, it will return the first object
        that is in its `Objects` property.
    
        If `obj` has a `CloneOf` property, it will search iteratively
        inside the object pointed to by this property.
    
    obj
        If `obj` is not a `Draft Clone`, nor it has a `CloneOf` property,
        it will return the same `obj`, as long as `strict` is `False`.
    
    False
        It will return `False` if `obj` is not a clone,
        and `strict` is `True`.
    

References
[draftutils.utils.get_clone_base()](../../de/d75/group__draftutils.html#ga4d043914ddb50c2150b893b9f7edc741),
and
[draftutils.utils.get_type()](../../de/d75/group__draftutils.html#gae98fd9ba514d4b735e2f52ddf54607b9).

Referenced by
[draftutils.utils.get_clone_base()](../../de/d75/group__draftutils.html#ga4d043914ddb50c2150b893b9f7edc741).

## ◆ get_default_unit()

def draftutils.units.get_default_unit  | ( |  | _dim_| ) |   
---|---|---|---|---|---  
      
    
    Return default Unit of Measure for a dimension.
    
    It is based on the user preferences.
    

Referenced by
[draftutils.units.make_format_spec()](../../de/d75/group__draftutils.html#gae428916f8b3be3519e13af51e7ea8fd9).

## ◆ get_draft_annotation_commands()

def draftutils.init_tools.get_draft_annotation_commands  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the annotation commands list.

## ◆ get_draft_context_commands()

def draftutils.init_tools.get_draft_context_commands  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the context menu commands list.

## ◆ get_draft_drawing_commands()

def draftutils.init_tools.get_draft_drawing_commands  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the drawing commands list.

References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

## ◆ get_draft_modification_commands()

def draftutils.init_tools.get_draft_modification_commands  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the modification commands list.

References
[draftutils.translate.QT_TRANSLATE_NOOP](../../de/d75/group__draftutils.html#ga9e6796e4394a4a163501246d7390f3c4).

## ◆ get_draft_snap_commands()

def draftutils.init_tools.get_draft_snap_commands  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the snapping commands list.

Referenced by
[draftguitools.gui_snapper.Snapper.init_draft_snap_buttons()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a1a7c4d8075bd991a3d2435c06a5c46f7),
and
[draftutils.init_draft_statusbar.init_draft_statusbar_snap()](../../de/d75/group__draftutils.html#ga4513dd995c3df83b2d848e4b4a39d941).

## ◆ get_draft_snap_tooltips()

def draftutils.init_tools.get_draft_snap_tooltips  | ( | | ) |   
---|---|---|---|---  
      
    
    Return a dictionary with tooltips for the snapping commands.
    
    For the snapping commands in the default toolbar and in the statusbar the
    tooltips from the `GetResources` functions in gui_snaps.py are not used.
    

Referenced by
[draftguitools.gui_snapper.Snapper.init_draft_snap_buttons()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a1a7c4d8075bd991a3d2435c06a5c46f7).

## ◆ get_draft_utility_commands_menu()

def draftutils.init_tools.get_draft_utility_commands_menu  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the utility commands list for the menu.

## ◆ get_draft_utility_commands_toolbar()

def draftutils.init_tools.get_draft_utility_commands_toolbar  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the utility commands list for the toolbar.

## ◆ get_group_contents()

def draftutils.groups.get_group_contents  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _walls_ = `False`,   
|  |  | _addgroups_ = `False`,   
|  |  | _spaces_ = `False`,   
|  |  | _noarchchild_ = `False`  
| ) | |   
      
    
    Return a list of objects from expanding the input groups.
    
    The function accepts any type of object, although it is most useful
    with "groups", as it is meant to unpack the objects inside these groups.
    
    Parameters
    ----------
    objectslist: list
        If any object in the list is considered a group, see the `is_group`
        function, its contents (`obj.Group`) are extracted and added to the
        output list.
    
        Single items that aren't groups are added to the output list
        as is.
    
    walls: bool, optional
        It defaults to `False`.
        If it is `True`, Wall and Structure objects (Arch Workbench)
        are treated as groups; they are scanned for Window, Door,
        and Rebar objects, and these are added to the output list.
    
    addgroups: bool, optional
        It defaults to `False`.
        If it is `True`, the group itself is kept as part of the output list.
    
    spaces: bool, optional
        It defaults to `False`.
        If it is `True`, Arch Spaces are added to the output list even
        when addgroups is False (their contents are always added).
    
    noarchchild: bool, optional
        It defaults to `False`.
        If it is `True`, the objects inside Building and BuildingParts
        (Arch Workbench) aren't added to the output list.
    
    Returns
    -------
    list
        The list of objects from each group present in `objectslist`,
        plus any other individual object given in `objectslist`.
    

References
[draftutils.groups.get_group_contents()](../../de/d75/group__draftutils.html#ga25f32b5a5e345a413adc13b0d702254f),
[draftutils.groups.get_windows()](../../de/d75/group__draftutils.html#ga67d81fda8653a1fd1892590f6b519298),
and
[draftutils.groups.is_group()](../../de/d75/group__draftutils.html#ga73eabe89d5e43bfbaaf251d5fa1ec2b4).

Referenced by
[draftutils.groups.get_group_contents()](../../de/d75/group__draftutils.html#ga25f32b5a5e345a413adc13b0d702254f),
and
[draftutils.groups.getGroupContents()](../../de/d75/group__draftutils.html#ga34d1d4e13fb85f7269caa8e4ee2d0fe1).

## ◆ get_group_names()

def draftutils.groups.get_group_names  | ( |  | _doc_ = `None`| ) |   
---|---|---|---|---|---  
      
    
    Return a list of names of existing groups in the document.
    
    Parameters
    ----------
    doc: App::Document, optional
        It defaults to `None`.
        A document on which to search group names.
        It if is `None` it will search the current document.
    
    Returns
    -------
    list of str
        A list of names of objects that are considered groups.
        See the is_group function.
    
        Otherwise returns an empty list.
    

References
[draftutils.groups.is_group()](../../de/d75/group__draftutils.html#ga73eabe89d5e43bfbaaf251d5fa1ec2b4).

Referenced by
[draftutils.groups.getGroupNames()](../../de/d75/group__draftutils.html#ga03d74c45e33815a40fe54ed5792d7c78),
and
[draftutils.groups.ungroup()](../../de/d75/group__draftutils.html#ga81fec1f995ea2967d99ab012ed241dcc).

## ◆ get_movable_children()

def draftutils.groups.get_movable_children  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _recursive_ = `True`  
| ) | |   
      
    
    Return a list of objects with child objects that move with a host.
    
    Builds a list of objects with all child objects (`obj.OutList`)
    that have their `MoveWithHost` attribute set to `True`.
    This function is mostly useful for Arch Workbench objects.
    
    Parameters
    ----------
    objectslist: list of App::DocumentObject
        A single scripted object or list of objects.
    
    recursive: bool, optional
        It defaults to `True`, in which case the function
        is called recursively to also extract the children of children
        objects.
        Otherwise, only direct children of the input objects
        are added to the output list.
    
    Returns
    -------
    list
        List of children objects that have their `MoveWithHost` attribute
        set to `True`.
    

References
[draftutils.groups.get_movable_children()](../../de/d75/group__draftutils.html#ga46ab9ffdc6b3888f9f9a6e46debc1e6f).

Referenced by
[draftutils.groups.get_movable_children()](../../de/d75/group__draftutils.html#ga46ab9ffdc6b3888f9f9a6e46debc1e6f),
and
[draftutils.groups.getMovableChildren()](../../de/d75/group__draftutils.html#ga4b58928d88c63959cae37ba39f39100d).

## ◆ get_objects_of_type()

def draftutils.utils.get_objects_of_type  | ( |  | _objects_ ,   
---|---|---|---  
|  |  | _typ_  
| ) | |   
      
    
    Return only the objects that match the type in the list of objects.
    
    Parameters
    ----------
    objects : list of App::DocumentObject
        A list of objects which will be tested.
    
    typ : str
        A string that indicates a type. This should be one of the types
        that can be returned by `get_type`.
    
    Returns
    -------
    list of objects
        Only the objects that match `typ` will be added to the output list.
    

References
[draftutils.utils.getType](../../de/d75/group__draftutils.html#ga99f7d10185bcca601667740968742397).

## ◆ get_param()

def draftutils.utils.get_param  | ( |  | _param_ ,   
---|---|---|---  
|  |  | _default_ = `None`  
| ) | |   
      
    
    Return a parameter value from the current parameter database.
    
    The parameter database is located in the tree
    ::
        'User parameter:BaseApp/Preferences/Mod/Draft'
    
    In the case that `param` is `'linewidth'` or `'color'` it will get
    the values from the View parameters
    ::
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'
    
    Parameters
    ----------
    param : str
        A string that indicates a parameter in the parameter database.
    
    default : optional
        It indicates the default value of the given parameter.
        It defaults to `None`, in which case it will use a specific
        value depending on the type of parameter determined
        with `get_param_type`.
    
    Returns
    -------
    int, or str, or float, or bool
        Depending on `param` and its type, by returning `ParameterGrp.GetInt`,
        `ParameterGrp.GetString`, `ParameterGrp.GetFloat`,
        `ParameterGrp.GetBool`, or `ParameterGrp.GetUnsinged`.
    

References
[draftutils.utils.getParamType](../../de/d75/group__draftutils.html#ga98afed1eba3ce8d18d8a666dd592dcfe).

Referenced by
[draftutils.gui_utils.dim_symbol()](../../de/d75/group__draftutils.html#ga1da14e7d5c8414fff08d776db07b6558),
[draftutils.utils.precision()](../../de/d75/group__draftutils.html#gab69b9d198a735e396d938b8fc96a1585),
and
[draftutils.utils.tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

## ◆ get_param_type()

def draftutils.utils.get_param_type  | ( |  | _param_| ) |   
---|---|---|---|---|---  
      
    
    Return the type of the parameter entered.
    
    Parameters
    ----------
    param : str
        A string that indicates a parameter in the parameter database.
    
    Returns
    -------
    str or None
        The returned string could be `'int'`, `'string'`, `'float'`,
        `'bool'`, `'unsigned'`, depending on the parameter.
        It returns `None` for unhandled situations.
    

## ◆ get_real_name()

def draftutils.utils.get_real_name  | ( |  | _name_| ) |   
---|---|---|---|---|---  
      
    
    Strip the trailing numbers from a string to get only the letters.
    
    Parameters
    ----------
    name : str
        A string that may have a number at the end, `Line001`.
    
    Returns
    -------
    str
        A string without the numbers at the end, `Line`.
        The returned string cannot be empty; it will have
        at least one letter.
    

Referenced by
[draftutils.utils.shapify()](../../de/d75/group__draftutils.html#ga8d556e0d018860c71069d9f3ac299783).

## ◆ get_rgb()

def draftutils.utils.get_rgb  | ( |  | _color_ ,   
---|---|---|---  
|  |  | _testbw_ = `True`  
| ) | |   
      
    
    Return an RRGGBB value #000000 from a FreeCAD color.
    
    Parameters
    ----------
    testwb : bool (default = True)
        pure white will be converted into pure black
    

References
[draftutils.utils.getParam](../../de/d75/group__draftutils.html#gaa2e66fde65fd9a8f9424bdd7660b0def).

## ◆ get_scales()

def draftutils.init_draft_statusbar.get_scales  | ( |  | _unit_system_ = `0`| ) |   
---|---|---|---|---|---  
      
    
    returns the list of preset scales accordin to unit system.
    
    Parameters:
    unit_system =   0 : default from user preferences
                    1 : metrics
                    2 : imperial architectural
                    3 : imperial engineering
    

Referenced by
[draftutils.init_draft_statusbar.init_draft_statusbar_scale()](../../de/d75/group__draftutils.html#ga93f646640439b1f18198344acf7b3bce).

## ◆ get_selection()

def draftutils.gui_utils.get_selection  | ( |  | _gui_ = `App.GuiUp`| ) |   
---|---|---|---|---|---  
      
    
    Return the current selected objects.
    
    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.
    
    It wraps around `Gui.Selection.getSelection`
    
    Parameters
    ----------
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.
    
        This value can be set to `False` to simulate
        when the interface is not available.
    
    Returns
    -------
    list of App::DocumentObject
        Returns a list of objects in the current selection.
        It can be an empty list if no object is selected.
    
        If the interface is not available, it returns `None`.
    

## ◆ get_selection_ex()

def draftutils.gui_utils.get_selection_ex  | ( |  | _gui_ = `App.GuiUp`| ) |   
---|---|---|---|---|---  
      
    
    Return the current selected objects together with their subelements.
    
    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.
    
    It wraps around `Gui.Selection.getSelectionEx`
    
    Parameters
    ----------
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.
    
        This value can be set to `False` to simulate
        when the interface is not available.
    
    Returns
    -------
    list of Gui::SelectionObject
        Returns a list of `Gui::SelectionObject` in the current selection.
        It can be an empty list if no object is selected.
    
        If the interface is not available, it returns `None`.
    
    Selection objects
    -----------------
    One `Gui::SelectionObject` has attributes that indicate which specific
    subelements, that is, vertices, wires, and faces, were selected.
    This can be useful to operate on the subelements themselves.
    If `G` is a `Gui::SelectionObject`
     * `G.Object` is the selected object
     * `G.ObjectName` is the name of the selected object
     * `G.HasSubObjects` is `True` if there are subelements in the selection
     * `G.SubObjects` is a tuple of the subelements' shapes
     * `G.SubElementNames` is a tuple of the subelements' names
    
    `SubObjects` and `SubElementNames` should be empty tuples
    if `HasSubObjects` is `False`.
    

## ◆ get_type()

def draftutils.utils.get_type  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Return a string indicating the type of the given object.
    
    Parameters
    ----------
    obj : App::DocumentObject
        Any type of scripted object created with Draft,
        or any other workbench.
    
    Returns
    -------
    str
        If `obj` has a `Proxy`, it will return the value of `obj.Proxy.Type`.
    
        * If `obj` is a `Part.Shape`, returns `'Shape'`
    
        * If `obj` has a `TypeId`, returns `obj.TypeId`
    
        In other cases, it will return `'Unknown'`,
        or `None` if `obj` is `None`.
    

Referenced by
[draftutils.utils.compare_objects()](../../de/d75/group__draftutils.html#gafb4412c803de5002eeaf01ce143f80b9),
and
[draftutils.utils.get_clone_base()](../../de/d75/group__draftutils.html#ga4d043914ddb50c2150b893b9f7edc741).

## ◆ get_windows()

def draftutils.groups.get_windows  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Return the windows and rebars inside a host.
    
    Parameters
    ----------
    obj: App::DocumentObject
        A scripted object of type `'Wall'` or `'Structure'`
        (Arch Workbench).
        This will be searched for objects of type `'Window'` and `'Rebar'`,
        and clones of them, and the found elements will be added
        to the output list.
    
        The function will search recursively all elements under `obj.OutList`,
        in case the windows and rebars are nested under other walls
        and structures.
    
    Returns
    -------
    list
        A list of all found windows and rebars in `obj`.
        If `obj` is itself a `'Window'` or a `'Rebar'`, or a clone of them,
        it will return the same `obj` element.
    

References
[draftutils.groups.get_windows()](../../de/d75/group__draftutils.html#ga67d81fda8653a1fd1892590f6b519298).

Referenced by
[draftutils.groups.get_group_contents()](../../de/d75/group__draftutils.html#ga25f32b5a5e345a413adc13b0d702254f),
and
[draftutils.groups.get_windows()](../../de/d75/group__draftutils.html#ga67d81fda8653a1fd1892590f6b519298).

## ◆ getGroupContents()

def draftutils.groups.getGroupContents  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _walls_ = `False`,   
|  |  | _addgroups_ = `False`,   
|  |  | _spaces_ = `False`,   
|  |  | _noarchchild_ = `False`  
| ) | |   
      
    
    Return a list of objects from groups. DEPRECATED.

References
[draftutils.groups.get_group_contents()](../../de/d75/group__draftutils.html#ga25f32b5a5e345a413adc13b0d702254f).

## ◆ getGroupNames()

def draftutils.groups.getGroupNames  | ( | | ) |   
---|---|---|---|---  
      
    
    Return a list of group names. DEPRECATED.

References
[draftutils.groups.get_group_names()](../../de/d75/group__draftutils.html#ga1c3d816788e6c9d5580579c98991ca46).

## ◆ getMovableChildren()

def draftutils.groups.getMovableChildren  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _recursive_ = `True`  
| ) | |   
      
    
    Return a list of objects with child objects. DEPRECATED.

References
[draftutils.groups.get_movable_children()](../../de/d75/group__draftutils.html#ga46ab9ffdc6b3888f9f9a6e46debc1e6f).

## ◆ hide_draft_statusbar()

def draftutils.init_draft_statusbar.hide_draft_statusbar  | ( | | ) |   
---|---|---|---|---  
      
    
    hides draft statusbar if present
    

References
[Gui.getMainWindow()](../../d9/dad/namespaceGui.html#ad7c580188be626079e659ab6514fcd92).

## ◆ init_draft_statusbar_scale()

def draftutils.init_draft_statusbar.init_draft_statusbar_scale  | ( | | ) |   
---|---|---|---|---  
      
    
    this function initializes draft statusbar scale widget
    

References
[draftutils.init_draft_statusbar.get_scales()](../../de/d75/group__draftutils.html#ga6d74b9b823c44dd034ab0df1af87f866),
[Gui.getMainWindow()](../../d9/dad/namespaceGui.html#ad7c580188be626079e659ab6514fcd92),
and
[draftutils.init_draft_statusbar.scale_to_label()](../../de/d75/group__draftutils.html#gaef14a833a1d3e2b8c62834cf8c1151a7).

## ◆ init_draft_statusbar_snap()

def draftutils.init_draft_statusbar.init_draft_statusbar_snap  | ( | | ) |   
---|---|---|---|---  
      
    
    this function initializes draft statusbar snap widget
    

References
[draftutils.init_tools.get_draft_snap_commands()](../../de/d75/group__draftutils.html#ga09c63eaa2c0be4fd0bcd4ef095209670),
and
[Gui.getMainWindow()](../../d9/dad/namespaceGui.html#ad7c580188be626079e659ab6514fcd92).

## ◆ init_menu()

def draftutils.init_tools.init_menu  | ( |  | _workbench_ ,   
---|---|---|---  
|  |  | _menu_list_ ,   
|  |  | _cmd_list_  
| ) | |   
      
    
    Initialize a menu.
    
    Parameters
    ----------
    workbench: Gui.Workbench
        The workbench. The commands from cmd_list must be available.
    
    menu_list: list of strings
        The main and optional submenu(s). The commands, and additional
        submenus (if any), are added to the last (sub)menu in the list.
    
    cmd_list: list of strings or list of strings and tuples
        See f.e. the return value of get_draft_drawing_commands.
    

## ◆ init_toolbar()

def draftutils.init_tools.init_toolbar  | ( |  | _workbench_ ,   
---|---|---|---  
|  |  | _toolbar_ ,   
|  |  | _cmd_list_  
| ) | |   
      
    
    Initialize a toolbar.
    
    Parameters
    ----------
    workbench: Gui.Workbench
        The workbench. The commands from cmd_list must be available.
    
    toolbar: string
        The name of the toolbar.
    
    cmd_list: list of strings or list of strings and tuples
        See f.e. the return value of get_draft_drawing_commands.
    

## ◆ is_clone()

def draftutils.utils.is_clone  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _objtype_ = `None`,   
|  |  | _recursive_ = `False`  
| ) | |   
      
    
    Return True if the given object is a clone of a certain type.
    
    A clone is of type `'Clone'`, and has a reference
    to the original object inside its `Objects` attribute,
    which is an `'App::PropertyLinkListGlobal'`.
    
    The `Objects` attribute can point to another `'Clone'` object.
    If `recursive` is `True`, the function will be called recursively
    to further test this clone, until the type of the original object
    can be compared to `objtype`.
    
    Parameters
    ----------
    obj : App::DocumentObject
        The clone object that will be tested for a certain type.
    
    objtype : str or list of str
        A type string such as one obtained from `get_type`.
        Or a list of such types.
    
    recursive : bool, optional
        It defaults to `False`.
        If it is `True`, this same function will be called recursively
        with `obj.Object[0]` as input.
    
        This option only works if `obj.Object[0]` is of type `'Clone'`,
        that is, if `obj` is a clone of a clone.
    
    Returns
    -------
    bool
        Returns `True` if `obj` is of type `'Clone'`,
        and `obj.Object[0]` is of type `objtype`.
    
        If `objtype` is a list, then `obj.Objects[0]`
        will be tested against each of the elements in the list,
        and it will return `True` if at least one element matches the type.
    
        If `obj` isn't of type `'Clone'` but has the `CloneOf` attribute,
        it will also return `True`.
    
        It returns `False` otherwise, for example,
        if `obj` is not even a clone.
    

References
[draftutils.utils.getType](../../de/d75/group__draftutils.html#ga99f7d10185bcca601667740968742397),
and
[draftutils.utils.is_clone()](../../de/d75/group__draftutils.html#gadbc339c73fd10df484a1ff3e77dbc8fe).

Referenced by
[draftutils.utils.is_clone()](../../de/d75/group__draftutils.html#gadbc339c73fd10df484a1ff3e77dbc8fe).

## ◆ is_closed_edge()

def draftutils.utils.is_closed_edge  | ( |  | _edge_index_ ,   
---|---|---|---  
|  |  | _object_  
| ) | |   
  
## ◆ is_group()

def draftutils.groups.is_group  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Return True if the given object is considered a group.
    
    Parameters
    ----------
    obj : App::DocumentObject
        The object to check.
    
    Returns
    -------
    bool
        Returns `True` if `obj` is considered a group:
    
        The object is derived from `App::DocumentObjectGroup` but not
        a `'LayerContainer'`.
    
        Or the object is of the type `'Project'`, `'Site'`, `'Building'`,
        `'Floor'`, `'BuildingPart'` or `'Space'` from the Arch Workbench.
        Note that `'Floor'` and `'Building'` are obsolete types.
    
        Otherwise returns `False`.
    

Referenced by
[draftutils.groups.get_group_contents()](../../de/d75/group__draftutils.html#ga25f32b5a5e345a413adc13b0d702254f),
and
[draftutils.groups.get_group_names()](../../de/d75/group__draftutils.html#ga1c3d816788e6c9d5580579c98991ca46).

## ◆ label_to_scale()

def draftutils.init_draft_statusbar.label_to_scale  | ( |  | _label_| ) |   
---|---|---|---|---|---  
      
    
    transform a scale string into scale factor as float
    

References
[Gui.getMainWindow()](../../d9/dad/namespaceGui.html#ad7c580188be626079e659ab6514fcd92),
[draftutils.init_draft_statusbar.label_to_scale()](../../de/d75/group__draftutils.html#ga3d11c3091f5430248c1edf90ac6dca63),
and
[draftutils.init_draft_statusbar.scale_to_label()](../../de/d75/group__draftutils.html#gaef14a833a1d3e2b8c62834cf8c1151a7).

Referenced by
[draftutils.init_draft_statusbar.label_to_scale()](../../de/d75/group__draftutils.html#ga3d11c3091f5430248c1edf90ac6dca63).

## ◆ load_svg_patterns()

def draftutils.utils.load_svg_patterns  | ( | | ) |   
---|---|---|---|---  
      
    
    Load the default Draft SVG patterns and user defined patterns.
    
    The SVG patterns are added as a dictionary to the `App.svgpatterns`
    attribute.
    

References
[importSVG.getContents()](../../d1/d33/namespaceimportSVG.html#adfbd66e58ea47c399ea21fa39fd9c7d9),
and
[draftutils.utils.getParam](../../de/d75/group__draftutils.html#gaa2e66fde65fd9a8f9424bdd7660b0def).

## ◆ load_texture()

def draftutils.gui_utils.load_texture  | ( |  | _filename_ ,   
---|---|---|---  
|  |  | _size_ = `None`,   
|  |  | _gui_ = `App.GuiUp`  
| ) | |   
      
    
    Return a Coin.SoSFImage to use as a texture for a 2D plane.
    
    This function only works if the graphical interface is available
    as the visual properties that can be applied to a shape
    are attributes of the view provider (`obj.ViewObject`).
    
    Parameters
    ----------
    filename: str
        A path to a pixel image file (PNG) that can be used as a texture
        on the face of an object.
    
    size: tuple of two int, or a single int, optional
        It defaults to `None`.
        If a tuple is given, the two values define the width and height
        in pixels to which the loaded image will be scaled.
        If it is a single value, it is used for both dimensions.
    
        If it is `None`, the size will be determined from the `QImage`
        created from `filename`.
    
        CURRENTLY the input `size` parameter IS NOT USED.
        It always uses the `QImage` to determine this information.
    
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.
    
        This value can be set to `False` to simulate
        when the interface is not available.
    
    Returns
    -------
    coin.SoSFImage
        An image object with the appropriate size, number of components
        (grayscale, grayscale and transparency, color,
        color and transparency), and byte data.
    
        It returns `None` if the interface is not available,
        or if there is a problem creating the image.
    

## ◆ make_format_spec()

def draftutils.units.make_format_spec  | ( |  | _decimals_ = `4`,   
---|---|---|---  
|  |  | _dim_ = `'Length'`  
| ) | |   
      
    
    Return a string format specifier with decimals for a dimension.
    
    It is based on the user preferences.
    

References
[draftutils.units.get_default_unit()](../../de/d75/group__draftutils.html#ga0d7ec14fc8988387fa4bfb8cb91b746b).

## ◆ migrate_text_display_mode()

def draftutils.gui_utils.migrate_text_display_mode  | ( |  | _obj_type_ = `"Text"`,   
---|---|---|---  
|  |  | _mode_ = `"3D text"`,   
|  |  | _doc_ = `None`  
| ) | |   
      
    
    Migrate the display mode of objects of certain type.

## ◆ precision()

def draftutils.utils.precision  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the precision value from the parameter database.
    
    It is the number of decimal places that a float will have.
    Example
    ::
        precision=6, 0.123456
        precision=5, 0.12345
        precision=4, 0.1234
    
    Due to floating point operations there may be rounding errors.
    Therefore, this precision number is used to round up values
    so that all operations are consistent.
    By default the precision is 6 decimal places.
    
    Returns
    -------
    int
        get_param("precision", 6)
    

References
[draftutils.utils.get_param()](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530),
and
[draftutils.utils.getParam](../../de/d75/group__draftutils.html#gaa2e66fde65fd9a8f9424bdd7660b0def).

## ◆ print_header()

def draftutils.utils.print_header  | ( |  | _name_ ,   
---|---|---|---  
|  |  | _description_ ,   
|  |  | _debug_ = `True`  
| ) | |   
      
    
    Print a line to the console when something is called, and log it.
    
    Parameters
    ----------
    name: str
        The name of the function or class that is being called.
        This `name` will be logged in the log file, so if there are problems
        the log file can be investigated for clues.
    
    description: str
        Arbitrary text that will be printed to the console
        when the function or class is called.
    
    debug: bool, optional
        It defaults to `True`.
        If it is `False` the `description` will not be printed
        to the console.
        On the other hand the `name` will always be logged.
    

## ◆ print_shape()

def draftutils.utils.print_shape  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Print detailed information of a topological shape.
    
    Parameters
    ----------
    shape : Part::TopoShape
        Any topological shape in an object, usually obtained from `obj.Shape`.
    

## ◆ remove_hidden()

def draftutils.gui_utils.remove_hidden  | ( |  | _objectslist_| ) |   
---|---|---|---|---|---  
      
    
    Return only the visible objects in the list.
    
    This function only works if the graphical interface is available
    as the `Visibility` attribute is a property of the view provider
    (`obj.ViewObject`).
    
    Parameters
    ----------
    objectslist: list of App::DocumentObject
        List of any type of object.
    
    Returns
    -------
    list
        Return a copy of the input list without those objects
        for which `obj.ViewObject.Visibility` is `False`.
    
        If the graphical interface is not loaded
        the returned list is just a copy of the input list.
    

## ◆ scale_to_label()

def draftutils.init_draft_statusbar.scale_to_label  | ( |  | _scale_| ) |   
---|---|---|---|---|---  
      
    
    transform a float number into a 1:X or X:1 scale and return it as label
    

Referenced by
[draftutils.init_draft_statusbar.init_draft_statusbar_scale()](../../de/d75/group__draftutils.html#ga93f646640439b1f18198344acf7b3bce),
and
[draftutils.init_draft_statusbar.label_to_scale()](../../de/d75/group__draftutils.html#ga3d11c3091f5430248c1edf90ac6dca63).

## ◆ select()

def draftutils.gui_utils.select  | ( |  | _objs_ = `None`,   
---|---|---|---  
|  |  | _gui_ = `App.GuiUp`  
| ) | |   
      
    
    Unselects everything and selects only the given list of objects.
    
    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.
    
    Parameters
    ----------
    objs: list of App::DocumentObject, optional
        It defaults to `None`.
        Any type of scripted object.
        It may be a list of objects or a single object.
    
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.
    
        This value can be set to `False` to simulate
        when the interface is not available.
    

Referenced by
[Gui::Flag.contextMenuEvent()](../../dc/dd0/classGui_1_1Flag.html#acdaf0217a9871708627e7c84710876ea),
[Gui::DocumentItem.findItem()](../../df/d15/classGui_1_1DocumentItem.html#ac20f1bb6efdbc301be559e6a0260ca28),
[Gui::DocumentItem.findItemByObject()](../../df/d15/classGui_1_1DocumentItem.html#a1dad1e3b186a241f6ad317cf6c5956ac),
[MeshGui::ViewProviderMesh.getFacetsOfRegion()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ab75cd4c10a9ab91adec07f3b3b8929cd),
[Gui::SoFCColorBar.handleEvent()](../../d0/dc7/classGui_1_1SoFCColorBar.html#a661775740fbc59f1887cfeb93b061692),
[Gui::TreeWidget.itemSearch()](../../de/de0/classGui_1_1TreeWidget.html#abb660e1cddeeee96c9f392c346d46700),
[Gui::PropertyEditor::LinkLabel.onLinkActivated()](../../d5/d5f/classGui_1_1PropertyEditor_1_1LinkLabel.html#afc047f59d622759447d8862f426c88a2),
[SketcherGui::TaskSketcherConstraints.onSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#ad2aa1dfda961213561df408f2bad55df),
[SketcherGui::TaskSketcherElements.onSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#afafa9c58f43f36216447d6c7df146cfc),
[PathScripts.PathFeatureExtensionsGui.TaskPanelExtensionPage.restoreSelection()](../../d0/de3/classPathScripts_1_1PathFeatureExtensionsGui_1_1TaskPanelExtensionPage.html#a178e8a65a2b495e3c44b7d62958e1dd4),
and
[Gui::DocumentItem.showItem()](../../df/d15/classGui_1_1DocumentItem.html#a324eb094c99c6a1e96a14e2de97ab7b2).

## ◆ set_param()

def draftutils.utils.set_param  | ( |  | _param_ ,   
---|---|---|---  
|  |  | _value_  
| ) | |   
      
    
    Set a Draft parameter with the given value.
    
    The parameter database is located in the tree
    ::
        'User parameter:BaseApp/Preferences/Mod/Draft'
    
    In the case that `param` is `'linewidth'` or `'color'` it will set
    the View parameters
    ::
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'
    
    Parameters
    ----------
    param : str
        A string that indicates a parameter in the parameter database.
    
    value : int, or str, or float, or bool
        The appropriate value of the parameter.
        Depending on `param` and its type, determined with `get_param_type`,
        it sets the appropriate value by calling `ParameterGrp.SetInt`,
        `ParameterGrp.SetString`, `ParameterGrp.SetFloat`,
        `ParameterGrp.SetBool`, or `ParameterGrp.SetUnsinged`.
    

References
[draftutils.utils.getParamType](../../de/d75/group__draftutils.html#ga98afed1eba3ce8d18d8a666dd592dcfe).

## ◆ shapify()

def draftutils.utils.shapify  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Transform a parametric object into a static, non-parametric shape.
    
    Parameters
    ----------
    obj : App::DocumentObject
        Any type of scripted object.
    
        This object will be removed, and a non-parametric object
        with the same topological shape (`Part::TopoShape`)
        will be created.
    
    Returns
    -------
    Part::Feature
        The new object that takes `obj.Shape` as its own.
    
        Depending on the contents of the Shape, the resulting object
        will be named `'Face'`, `'Solid'`, `'Compound'`,
        `'Shell'`, `'Wire'`, `'Line'`, `'Circle'`,
        or the name returned by `get_real_name(obj.Name)`.
    
        If there is a problem with `obj.Shape`, it will return `None`,
        and the original object will not be modified.
    

References
[draftutils.utils.get_real_name()](../../de/d75/group__draftutils.html#ga1ceb579c51b5f1f4747c78baac87d07a),
and
[draftutils.utils.getRealName](../../de/d75/group__draftutils.html#gabd3fbce3003fa71b67b8b81eef56a43f).

## ◆ show_draft_statusbar()

def draftutils.init_draft_statusbar.show_draft_statusbar  | ( | | ) |   
---|---|---|---|---  
      
    
    shows draft statusbar if present or initializes it
    

References
[Gui.getMainWindow()](../../d9/dad/namespaceGui.html#ad7c580188be626079e659ab6514fcd92).

## ◆ string_encode_coin()

def draftutils.utils.string_encode_coin  | ( |  | _ustr_| ) |   
---|---|---|---|---|---  
      
    
    Encode a unicode object to be used as a string in coin.
    
    Parameters
    ----------
    ustr : str
        A string to be encoded
    
    Returns
    -------
    str
        Encoded string. If the coin version is >= 4
        it will encode the string to `'utf-8'`, otherwise
        it will encode it to `'latin-1'`.
    

## ◆ svg_patterns()

def draftutils.utils.svg_patterns  | ( | | ) |   
---|---|---|---|---  
      
    
    Return a dictionary with installed SVG patterns.
    
    Returns
    -------
    dict
        Returns `App.svgpatterns` if it exists.
        Otherwise it calls `load_svg_patterns` to create it
        before returning it.
    

References
[draftutils.utils.loadSvgPatterns](../../de/d75/group__draftutils.html#gadca8ee54e0ba10ecfa0f25e6e52ad7ff).

## ◆ tolerance()

def draftutils.utils.tolerance  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the tolerance value from the parameter database.
    
    This specifies a tolerance around a quantity.
    ::
        value + tolerance
        value - tolerance
    
    By default the tolerance is 0.05.
    
    Returns
    -------
    float
        get_param("tolerance", 0.05)
    

References
[draftutils.utils.get_param()](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530),
and
[draftutils.utils.getParam](../../de/d75/group__draftutils.html#gaa2e66fde65fd9a8f9424bdd7660b0def).

Referenced by
[MeshGui::TaskDecimating.accept()](../../d8/d7d/classMeshGui_1_1TaskDecimating.html#a3a3732a74b60c4b3b4e79769d8b91767),
[TechDraw::DrawUtil.angleWithX()](../../da/d23/classTechDraw_1_1DrawUtil.html#afa770b85407535a96f2102f4f4962a7a),
[TechDraw::DrawUtil.checkParallel()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae2defa41adf07b1b8c29937dd2f0a83a),
[AdaptivePath.CleanPath()](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4),
[Part::TopoShape.common()](../../d8/ded/classPart_1_1TopoShape.html#aca3bf41e520b7146aa107799189ccbe1),
[Base::BoundBox2d.Contains()](../../de/db4/classBase_1_1BoundBox2d.html#a1689b66487df7a59438a26af41fe64de),
[Part::TopoShape.cut()](../../d8/ded/classPart_1_1TopoShape.html#a51c2867b0d3d70fc739dfc96908088bd),
[Sketcher::SketchAnalysis.detectDegeneratedGeometries()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#abff3a14cad90b3ac1a76b96d30681f12),
[draftutils.utils.epsilon()](../../de/d75/group__draftutils.html#ga7ca4044874669855d2291d7990debb22),
[TechDraw::DrawViewDimExtent.execute()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[geoff_geometry.FEQ()](../../de/d5d/namespacegeoff__geometry.html#ae6a481104c181645f64637920ecb586a),
[geoff_geometry.FEQZ()](../../de/d5d/namespacegeoff__geometry.html#a07cc9f572d018930c50c0ceee58eb92a),
[SMESH_ElementSearcherImpl.FindElementsByPoint()](../../dd/d4c/structSMESH__ElementSearcherImpl.html#af29a62ee66fb42ce8c0b9dca8c011632),
[ReverseEngineeringGui::SegmentationManual::Private.findGeometry()](../../dc/dc5/classSegmentationManual_1_1Private.html#ab79497cfd7a37b25ceb430dabaadb41a),
[SMESH_NodeSearcherImpl.FindNearPoint()](../../d4/d12/structSMESH__NodeSearcherImpl.html#a560e0aede0b64250f6ef04962d1b8fca),
[GEOMUtils.FixShapeTolerance()](../../db/daf/namespaceGEOMUtils.html#a47d81eba03068e1be1ae49b23d52549d),
[geoff_geometry.FNE()](../../de/d5d/namespacegeoff__geometry.html#afb2e77d69ab3c3801b962bf82b0997d5),
[geoff_geometry.FNEZ()](../../de/d5d/namespacegeoff__geometry.html#a9f93d4337f1914a6ccb9ab73752c85a7),
[TechDraw::DrawUtil.fpCompare()](../../da/d23/classTechDraw_1_1DrawUtil.html#a0b4c5fbe2f0ab262e05b0107c4ed5ca5),
[Part::TopoShape.fuse()](../../d8/ded/classPart_1_1TopoShape.html#a5c4be4ae1ca4bde3c9cde5e7cb6db675),
[Part::TopoShape.generalFuse()](../../d8/ded/classPart_1_1TopoShape.html#afe8c32d70f8f0048759f470d6f76fdba),
[Drawing::ProjectionAlgos.getDXF()](../../db/d32/classDrawing_1_1ProjectionAlgos.html#a82b64c6a0d7094e8719914a129bb431f),
[TechDraw::ProjectionAlgos.getDXF()](../../dd/d7c/classTechDraw_1_1ProjectionAlgos.html#a82b64c6a0d7094e8719914a129bb431f),
[SMESH_MeshAlgos.GetElementSearcher()](../../dd/d76/namespaceSMESH__MeshAlgos.html#a1fd35fba07d1fecd1422452834709ba0),
[TechDraw::DrawViewDimension.getFormattedDimensionValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a92f36b1b5e044976e4a117424b000985),
[SMESH_ElementSearcherImpl.GetPointState()](../../dd/d4c/structSMESH__ElementSearcherImpl.html#a7c4aca594feefb77fccfe2b06fb6793e),
[Drawing::ProjectionAlgos.getSVG()](../../db/d32/classDrawing_1_1ProjectionAlgos.html#ae198d5770093a803827a5887e5089978),
[TechDraw::ProjectionAlgos.getSVG()](../../dd/d7c/classTechDraw_1_1ProjectionAlgos.html#ae198d5770093a803827a5887e5089978),
[Base::BoundBox2d.IsEqual()](../../de/db4/classBase_1_1BoundBox2d.html#ad50960f7b511f1d5aee4b2dd0e670d4e),
[Base::Vector2d.IsEqual()](../../db/da7/classBase_1_1Vector2d.html#a61ca0b11ad1e5e4bb0c1fa11630be960),
[TechDraw::DrawUtil.isFirstVert()](../../da/d23/classTechDraw_1_1DrawUtil.html#aeddf362c89e95abb783486ce927a1f5d),
[TechDraw::DrawUtil.isLastVert()](../../da/d23/classTechDraw_1_1DrawUtil.html#a34287f47151501652cde9f33bc9418bc),
[Base::Vector2d.IsNull()](../../db/da7/classBase_1_1Vector2d.html#a54fb065048001c7be6023e6a430f5ac9),
[geoff_geometry.IsPtsLine()](../../de/d5d/namespacegeoff__geometry.html#abe8260940b3b09e55fa295257d5d320e),
[Part::TangentialArc.isRadiusEqual()](../../d2/d99/classPart_1_1TangentialArc.html#aeca0f831d777e1d6b62093fd57dad644),
[TechDraw::DrawUtil.isSamePoint()](../../da/d23/classTechDraw_1_1DrawUtil.html#ac9679ecb38e1cbbf816f141aadda5700),
[TechDraw::DrawUtil.isZeroEdge()](../../da/d23/classTechDraw_1_1DrawUtil.html#a7605d781e821f5a4915fcec23835f867),
[Path::Area.makeSections()](../../d8/dfc/classPath_1_1Area.html#a6b81c1ac048f21eb931a01e1a9244630),
[TechDraw::GeometryUtils.nextGeom()](../../d5/d83/classTechDraw_1_1GeometryUtils.html#a10818f1e344fda00df1cce6e009ca3f7),
[Path::Area.project()](../../d8/dfc/classPath_1_1Area.html#adad62016dff141074408fc32a0f7aa4b),
[MeshPart::MeshProjection.projectOnMesh()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#ab0dd5abefe9189817d0798f118f88130),
[geoff_geometry::Kurve.Reduce()](../../d3/ddd/classgeoff__geometry_1_1Kurve.html#a6527347f269c894c29f8a7290abfcc28),
[Sketcher::SketchAnalysis.removeDegeneratedGeometries()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a54caaa293a607376706ca5c6a9cb33ab),
[Part::GeomBSplineCurve.removeKnot()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#ab7de2e506e1196e10f78390ff59dc827),
[Part::TopoShape.section()](../../d8/ded/classPart_1_1TopoShape.html#a067ac3ce3c288430452d407504fb450b),
[Part::TopoShape.setFaces()](../../d8/ded/classPart_1_1TopoShape.html#ad64680d8287c9e4514953174a53b260b),
[Part::TopoShape.sewShape()](../../d8/ded/classPart_1_1TopoShape.html#a9ee78de6676f27f0b7e3b883ab4f1779),
[MeshCore::MeshSimplify.simplify()](../../dd/d6a/classMeshCore_1_1MeshSimplify.html#a546b9a143ce8b7e7a2efbce554b8d3a8),
[Simplify.simplify_mesh()](../../de/df0/classSimplify.html#a0e1eb5798e249dbdc5d28e24cc2e2554),
[geoff_geometry.Split()](../../de/d5d/namespacegeoff__geometry.html#a3c62588b49e5573d36c5c4ff5f6fff8f),
[Part::BSplineCurveBiArcs.toBiArcs()](../../d2/d61/classPart_1_1BSplineCurveBiArcs.html#a277260b51bea31a85e98ba580b3fc4df),
and
[Part::GeomBSplineCurve.toBiArcs()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#adde625bf3f9d8655ccd1154b4c99cc3d).

## ◆ translate()

def draftutils.translate.translate  | ( |  | _context_ ,   
---|---|---|---  
|  |  | _text_ ,   
|  |  | _utf8_decode_ = `False`  
| ) | |   
      
    
    Translate the text using the Qt translate function.
    
        It wraps around `QtGui.QApplication.translate`,
        which is the same as `QtCore.QCoreApplication.translate`.
    
        Parameters
        ----------
        context: str
            In C++ it is typically a class name.
            But it can also be any other string to categorize the translation,
            for example, the name of a workbench, tool, or function
            that is being translated. Usually it will be the name
            of the workbench.
    
        text: str
            Text that will be translated. It could be a single word,
            a full sentence, paragraph, or multiple paragraphs with new lines.
            Usually the last endline character '\\n'
            that finishes the string doesn't need to be included
            for translation.
    
        utf8_decode: bool
            It defaults to `False`.
            This must be set to `True` to indicate that the `text`
            is an `'utf8'` encoded string, so it should be returned as such.
            This option is ignored when using Python 3
            as with Python 3 all strings are `'utf8'` by default.
    
        Returns
        -------
        str
            A unicode string returned by `QtGui.QApplication.translate`.
    
            If `utf8_decode` is `True`, the resulting string will be encoded
            in `'utf8'`, and a `bytes` object will be returned.
            ::
                Qtranslate = QtGui.QApplication.translate
                return Qtranslate(context, text, None).encode("utf8")
    
        Unicode strings
        ---------------
        Whether it is Qt4 or Qt5, the `translate` function
        always returns a unicode string.
        The difference is how it handles the input.
    
        Reference: https://pyside.github.io/docs/pyside/PySide/QtCore/
    
        In Qt4 the translate function has a 4th parameter to define the encoding
        of the input string.
    
        >>> QtCore.QCoreApplication.translate(context, text, None, UnicodeUT8)
        >>> QtGui.QApplication.translate(context, text, None, UnicodeUT8)
    
        Reference: https://doc.qt.io/qtforpython/PySide2/QtCore
    
        In Qt5 the strings are always assumed unicode, so the 4th parameter
        is for a different use, and it is not used.
    
        >>> QtCore.QCoreApplication.translate(context, text, None)
        >>> QtGui.QApplication.translate(context, text, None)

References
[draftutils.translate.Qtranslate](../../de/d75/group__draftutils.html#gad400e273e5f66ec66c7a982fb2238426).

## ◆ type_check()

def draftutils.utils.type_check  | ( |  | _args_and_types_ ,   
---|---|---|---  
|  |  | _name_ = `"?"`  
| ) | |   
      
    
    Check that the arguments are instances of certain types.
    
    Parameters
    ----------
    args_and_types : list
        A list of tuples. The first element of a tuple is tested as being
        an instance of the second element.
        ::
            args_and_types = [(a, Type), (b, Type2), ...]
    
        Then
        ::
            isinstance(a, Type)
            isinstance(b, Type2)
    
        A `Type` can also be a tuple of many types, in which case
        the check is done for any of them.
        ::
            args_and_types = [(a, (Type3, int, float)), ...]
    
            isinstance(a, (Type3, int, float))
    
    name : str, optional
        Defaults to `'?'`. The name of the check.
    
    Raises
    ------
    TypeError
        If the first element in the tuple is not an instance of the second
        element, it raises `Draft.name`.
    

## ◆ ungroup()

def draftutils.groups.ungroup  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    Remove the object from any group to which it belongs.
    
    A "group" is any object returned by `get_group_names`.
    
    Parameters
    ----------
    obj: App::DocumentObject or str
        Any type of object.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    

References
[draftutils.groups.get_group_names()](../../de/d75/group__draftutils.html#ga1c3d816788e6c9d5580579c98991ca46).

## ◆ use_instead()

def draftutils.utils.use_instead  | ( |  | _function_ ,   
---|---|---|---  
|  |  | _version_ = `""`  
| ) | |   
      
    
    Print a deprecation message and suggest another function.
    
    This function must be used inside the definition of a function
    that has been considered for deprecation, so we must provide
    an alternative.
    ::
        def old_function():
            use_instead('new_function', 1.0)
    
        def someFunction():
            use_instead('some_function')
    
    Parameters
    ----------
    function: str
        The name of the function to use instead of the current one.
    
    version: float or str, optional
        It defaults to the empty string `''`.
        The version where this command is to be deprecated, if it is known.
        If we don't know when this command will be deprecated
        then we should not give a version.
    

References
[draftutils.utils.use_instead()](../../de/d75/group__draftutils.html#ga9c0290eb39293ebe5b10cdc018a75310).

Referenced by
[draftutils.utils.use_instead()](../../de/d75/group__draftutils.html#ga9c0290eb39293ebe5b10cdc018a75310).

## ◆ utf8_decode()

def draftutils.utils.utf8_decode  | ( |  | _text_| ) |   
---|---|---|---|---|---  
      
    
    Decode the input string and return a unicode string.
    
    Python 2:
    ::
    str -> unicode
    unicode -> unicode
    
    Python 3:
    ::
    str -> str
    bytes -> str
    
    It runs
    ::
    try:
    return text.decode("utf-8")
    except AttributeError:
    return text
    
    Parameters
    ----------
    text : str, unicode or bytes
    A str, unicode, or bytes object that may have unicode characters
    like accented characters.
    
    In Python 2, a `bytes` object can include accented characters,
    but in Python 3 it must only contain ASCII literal characters.
    
    Returns
    -------
    unicode or str
    In Python 2 it will try decoding the `bytes` string
    and return a `'utf-8'` decoded string.
    
    >>> "Aá".decode("utf-8")
    >>> b"Aá".decode("utf-8")
    u'A\xe1'
    
    In Python 2 the unicode string is prefixed with `u`,
    and unicode characters are replaced by their two-digit hexadecimal
    representation, or four digit unicode escape.
    
    >>> "AáBẃCñ".decode("utf-8")
    u'A\xe1B\u1e83C\xf1'
    
    In Python 2 it will always return a `unicode` object.
    
    In Python 3 a regular string is already unicode encoded,
    so strings have no `decode` method. In this case, `text`
    will be returned as is.
    
    In Python 3, if `text` is a `bytes` object, then it will be converted
    to `str`; in this case, the `bytes` object cannot have accents,
    it must only contain ASCII literal characters.
    
    >>> b"ABC".decode("utf-8")
    'ABC'
    
    In Python 3 it will always return a `str` object, with no prefix.
    

Referenced by
[ArchCommands.printWarning()](../../d4/d52/namespaceArchCommands.html#aa246a606bc319851e58c55f66d7693e6),
[ArchCommands.survey()](../../d4/d52/namespaceArchCommands.html#a2a97d8ae69e51460196b4d3e0d6859f1),
[ArchCommands.SurveyTaskPanel.update()](../../d8/d1c/classArchCommands_1_1SurveyTaskPanel.html#a77685c35ce185891696d5ac525070003),
and
[DraftGui.DraftToolBar.validateFile()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a38306af72567582542f7c128bb923f9f).

## Variable Documentation

## ◆ ANNOTATION_STYLE

dictionary draftutils.utils.ANNOTATION_STYLE  
---  
  
**Initial value:**

1= {

2 "FontName": ("font", param.GetString("textfont", "Sans")),

3 "FontSize": ("str",
[str](../../d9/d36/classstr.html)(param.GetFloat("textheight", 100))),

4 "LineSpacing": ("float", 1),

5 "ScaleMultiplier": ("float", 1),

6 "ShowUnit": ("bool", False),

7 "UnitOverride": ("str", ""),

8 "Decimals": ("int", 2),

9 "ShowLines": ("bool", True),

10 "LineWidth": ("int", param.GetInt("linewidth", 1)),

11 "LineColor": ("color", param.GetInt("color", 255)),

12 "ArrowType": ("index", param.GetInt("dimsymbol", 0)),

13 "ArrowSize": ("str",
[str](../../d9/d36/classstr.html)(param.GetFloat("arrowsize", 20))),

14 "DimensionOvershoot": ("str",
[str](../../d9/d36/classstr.html)(param.GetFloat("dimovershoot", 20))),

15 "ExtensionLines": ("str",
[str](../../d9/d36/classstr.html)(param.GetFloat("extlines", 300))),

16 "ExtensionOvershoot": ("str",
[str](../../d9/d36/classstr.html)(param.GetFloat("extovershoot", 20))),

17}

## ◆ ARROW_TYPES

list draftutils.utils.ARROW_TYPES = ["Dot",
"[Circle](../../d8/d53/classCircle.html)", "Arrow", "Tick", "Tick-2"]  
---  
  
## ◆ arrowtypes

list draftutils.utils.arrowtypes =
[ARROW_TYPES](../../de/d75/group__draftutils.html#gabe84c400a239bc3508311db7c5c568ce)  
---  
  
## ◆ compareObjects

def draftutils.utils.compareObjects =
[compare_objects](../../de/d75/group__draftutils.html#gafb4412c803de5002eeaf01ce143f80b9)  
---  
  
## ◆ dimDash

def draftutils.gui_utils.dimDash =
[dim_dash](../../de/d75/group__draftutils.html#gada3a166fa5d025f2c2bed4feca118166)  
---  
  
## ◆ dimSymbol

def draftutils.gui_utils.dimSymbol =
[dim_symbol](../../de/d75/group__draftutils.html#ga1da14e7d5c8414fff08d776db07b6558)  
---  
  
## ◆ displayExternal

def draftutils.units.displayExternal =
[display_external](../../de/d75/group__draftutils.html#gac1fd8df42886d027fec6f692b158b211)  
---  
  
Referenced by
[DraftGui.DraftToolBar.displayPoint()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#ab9273fdf843210eaac76d6c00be3a658),
[DraftGui.DraftToolBar.setRadiusValue()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a052cf9eb38e31c76e468cdf91daa4c7f),
[DraftGui.DraftToolBar.update_cartesian_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a779b9ccf6e5ec7e924d3c637324502d5),
and
[DraftGui.DraftToolBar.update_spherical_coords()](../../d0/d91/classDraftGui_1_1DraftToolBar.html#a23d8918462909f18321ca17435aa66e0).

## ◆ draft_scales_arch_imperial

list draftutils.init_draft_statusbar.draft_scales_arch_imperial  
---  
  
**Initial value:**

1= ["1/16in=1ft", "3/32in=1ft", "1/8in=1ft",

2 "3/16in=1ft", "1/4in=1ft","3/8in=1ft",

3 "1/2in=1ft", "3/4in=1ft", "1in=1ft",

4 "1.5in=1ft", "3in=1ft",

5 [translate](../../d3/d32/namespacetranslate.html "Provides utility functions
that wrap around the Qt translate function.")("draft", "custom"),

6 ]

## ◆ draft_scales_eng_imperial

list draftutils.init_draft_statusbar.draft_scales_eng_imperial  
---  
  
**Initial value:**

1= ["1in=10ft", "1in=20ft", "1in=30ft",

2 "1in=40ft", "1in=50ft", "1in=60ft",

3 "1in=70ft", "1in=80ft", "1in=90ft",

4 "1in=100ft",

5 [translate](../../d3/d32/namespacetranslate.html "Provides utility functions
that wrap around the Qt translate function.")("draft", "custom"),

6 ]

## ◆ draft_scales_metrics

list draftutils.init_draft_statusbar.draft_scales_metrics  
---  
  
**Initial value:**

1= ["1:1000", "1:500", "1:250", "1:200", "1:100",

2 "1:50", "1:25","1:20", "1:10", "1:5","1:2",

3 "1:1",

4 "2:1", "5:1", "10:1", "20:1",

5 [translate](../../d3/d32/namespacetranslate.html "Provides utility functions
that wrap around the Qt translate function.")("draft", "custom"),

6 ]

## ◆ filterObjectsForModifiers

def draftutils.utils.filterObjectsForModifiers =
[filter_objects_for_modifiers](../../de/d75/group__draftutils.html#ga9cca671c257ff64d8ce29eead3116f0a)  
---  
  
## ◆ formatObject

def draftutils.gui_utils.formatObject =
[format_object](../../de/d75/group__draftutils.html#gae12ae9fb772391933245e74c4c29e136)  
---  
  
Referenced by
[Gui::PropertyEditor::LinkLabel.updatePropertyLink()](../../d5/d5f/classGui_1_1PropertyEditor_1_1LinkLabel.html#a444c666ddd0929725b1cea41510868a2).

## ◆ get3DView

def draftutils.gui_utils.get3DView =
[get_3d_view](../../de/d75/group__draftutils.html#gad1f55ea6876f55797fdc080ff3d7773a)  
---  
  
## ◆ getCloneBase

def draftutils.utils.getCloneBase =
[get_clone_base](../../de/d75/group__draftutils.html#ga4d043914ddb50c2150b893b9f7edc741)  
---  
  
## ◆ getDefaultUnit

def draftutils.units.getDefaultUnit =
[get_default_unit](../../de/d75/group__draftutils.html#ga0d7ec14fc8988387fa4bfb8cb91b746b)  
---  
  
## ◆ getObjectsOfType

def draftutils.utils.getObjectsOfType =
[get_objects_of_type](../../de/d75/group__draftutils.html#gacc0d5765c8f794e939bf2285d009ab34)  
---  
  
Referenced by
[MeshPartGui::CrossSections.apply()](../../d1/d27/classMeshPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[PartGui::CrossSections.apply()](../../dc/d84/classPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[PartGui::DlgExtrusion.DlgExtrusion()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a7d11626ecae8d02d4421aa4fdd640dc8),
[PartGui::DlgRevolution.DlgRevolution()](../../d1/d83/classPartGui_1_1DlgRevolution.html#ad75370b34cc9b2f2ddb1439faa282f0d),
[TechDrawGui::DrawGuiUtil.findPage()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a5e81d631634196d2c5fe0d083fd7cb9b),
[Gui::SelectionSingleton.getObjectsOfType()](../../d4/dca/classGui_1_1SelectionSingleton.html#a63067216f55356a1f8c972aaf03aeebc),
and
[PartGui::Mirroring.Mirroring()](../../db/d41/classPartGui_1_1Mirroring.html#a37c415d13595eeeaa2f1a1fa54a5f740).

## ◆ getParam

def draftutils.utils.getParam =
[get_param](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530)  
---  
  
Referenced by
[draftutils.utils.get_rgb()](../../de/d75/group__draftutils.html#gaae54b3e46d1d402a69f707bcbbe2128b),
[draftutils.utils.load_svg_patterns()](../../de/d75/group__draftutils.html#ga5ede6da8d3035b698c3f882c43cf4d69),
[draftutils.utils.precision()](../../de/d75/group__draftutils.html#gab69b9d198a735e396d938b8fc96a1585),
and
[draftutils.utils.tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

## ◆ getParamType

def draftutils.utils.getParamType =
[get_param_type](../../de/d75/group__draftutils.html#gafacfb13dcf3a6290dfa25623703c1e02)  
---  
  
Referenced by
[draftutils.utils.get_param()](../../de/d75/group__draftutils.html#ga88140381e1bab00fca7ede179317e530),
and
[draftutils.utils.set_param()](../../de/d75/group__draftutils.html#ga01641daa7576c696849ca6fcfc3fb350).

## ◆ getRealName

def draftutils.utils.getRealName =
[get_real_name](../../de/d75/group__draftutils.html#ga1ceb579c51b5f1f4747c78baac87d07a)  
---  
  
Referenced by
[draftutils.utils.shapify()](../../de/d75/group__draftutils.html#ga8d556e0d018860c71069d9f3ac299783).

## ◆ getrgb

def draftutils.utils.getrgb =
[get_rgb](../../de/d75/group__draftutils.html#gaae54b3e46d1d402a69f707bcbbe2128b)  
---  
  
## ◆ getSelection

def draftutils.gui_utils.getSelection =
[get_selection](../../de/d75/group__draftutils.html#ga8196bdfd06b6c271ac4039c2256d3b2f)  
---  
  
Referenced by
[MeshPartGui::Tessellation.accept()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#a222ec7598711d0c506f4897d9a996bd1),
[PartDesignGui::DlgActiveBody.DlgActiveBody()](../../dc/dd5/classPartDesignGui_1_1DlgActiveBody.html#a286928f45731d5575f688ae3b871c67f),
[PartDesignGui::TaskFeaturePick.onSelectionChanged()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a0b5fe9b632b02205c54bb88b18a1ed62),
and
[Gui::View3DInventorViewer.viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ getSelectionEx

def draftutils.gui_utils.getSelectionEx =
[get_selection_ex](../../de/d75/group__draftutils.html#ga6b24f6a655e74e0d1e1e013f3187a996)  
---  
  
Referenced by
[ArchSpace.makeSpace()](../../d8/d6a/namespaceArchSpace.html#abab3f050d87b2ff385190dff9cc52d7f),
[Gui::ElementColors::Private.onSelectionChanged()](../../d8/dc9/classElementColors_1_1Private.html#afd57ddb2a0592ad0eef0d2bdcb9066ce),
and
[MeshGui::TaskSmoothing.TaskSmoothing()](../../da/d50/classMeshGui_1_1TaskSmoothing.html#ab51dce40b8a4bd1bc653af4b18f6fda9).

## ◆ getType

def draftutils.utils.getType =
[get_type](../../de/d75/group__draftutils.html#gae98fd9ba514d4b735e2f52ddf54607b9)  
---  
  
Referenced by
[draftutils.utils.compare_objects()](../../de/d75/group__draftutils.html#gafb4412c803de5002eeaf01ce143f80b9),
[Gui::MainWindow.customEvent()](../../d5/d2f/classGui_1_1MainWindow.html#ac554aac5d184489c7efc89f3294aa0f9),
[draftutils.utils.get_objects_of_type()](../../de/d75/group__draftutils.html#gacc0d5765c8f794e939bf2285d009ab34),
and
[draftutils.utils.is_clone()](../../de/d75/group__draftutils.html#gadbc339c73fd10df484a1ff3e77dbc8fe).

## ◆ isClone

def draftutils.utils.isClone =
[is_clone](../../de/d75/group__draftutils.html#gadbc339c73fd10df484a1ff3e77dbc8fe)  
---  
  
## ◆ isClosedEdge

def draftutils.utils.isClosedEdge =
[is_closed_edge](../../de/d75/group__draftutils.html#gacfa15ea8d3449fa2f22b19842e3d4a8c)  
---  
  
## ◆ loadSvgPatterns

def draftutils.utils.loadSvgPatterns =
[load_svg_patterns](../../de/d75/group__draftutils.html#ga5ede6da8d3035b698c3f882c43cf4d69)  
---  
  
Referenced by
[draftutils.utils.svg_patterns()](../../de/d75/group__draftutils.html#gad668ee3ba955aea7dcb8fd72a6e148b7).

## ◆ loadTexture

def draftutils.gui_utils.loadTexture =
[load_texture](../../de/d75/group__draftutils.html#gafafb93128d4d59f97fffd3d0c83ec681)  
---  
  
## ◆ makeFormatSpec

def draftutils.units.makeFormatSpec =
[make_format_spec](../../de/d75/group__draftutils.html#gae428916f8b3be3519e13af51e7ea8fd9)  
---  
  
## ◆ param

draftutils.utils.param = App.ParamGet("User
parameter:BaseApp/Preferences/Mod/Draft")  
---  
  
## ◆ printShape

def draftutils.utils.printShape =
[print_shape](../../de/d75/group__draftutils.html#ga345aba753e9ec774075c1bdec299633d)  
---  
  
## ◆ QT_TRANSLATE_NOOP

draftutils.translate.QT_TRANSLATE_NOOP = QtCore.QT_TRANSLATE_NOOP  
---  
  
Referenced by
[InspectionGui::VisualInspection.accept()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#a9f3542df70a4b485aebffadb7c9d9d6d),
[MeshGui::TaskDecimating.accept()](../../d8/d7d/classMeshGui_1_1TaskDecimating.html#a3a3732a74b60c4b3b4e79769d8b91767),
[MeshGui::TaskSmoothing.accept()](../../da/d50/classMeshGui_1_1TaskSmoothing.html#ad1f9c93ca36a6cd37f27bcb09b06b0cf),
[PartGui::LoftWidget.accept()](../../dc/d7e/classPartGui_1_1LoftWidget.html#a2f5cabdd4168a157209db905a43d3c5f),
[PartGui::SweepWidget.accept()](../../d0/dda/classPartGui_1_1SweepWidget.html#ac9e4d005b6e7ecc3ddae3c22258fd8a5),
[ReenGui::FitBSplineSurfaceWidget.accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
[ReenGui::PoissonWidget.accept()](../../d7/dae/classReenGui_1_1PoissonWidget.html#a947b3b6b4d87c7a8ca5429c9bef3de2e),
[TechDrawGui::TaskActiveView.accept()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a17c1dd2c632f5624c7edc69cacd32a73),
[TechDrawGui::TaskCosmeticLine.accept()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#aae988f7c93fd6f882347775cbb041bb1),
[TechDrawGui::TaskCustomizeFormat.accept()](../../db/dde/classTechDrawGui_1_1TaskCustomizeFormat.html#ac65e54467705d01196d828596c6ed2d0),
[TechDrawGui::TaskWeldingSymbol.accept()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ad91ef56ef584a69a7b67e440066ebec8),
[PartDesignGui::DlgActiveBody.accept()](../../dc/dd5/classPartDesignGui_1_1DlgActiveBody.html#a1932d79f3d3669f8b2f576ead60d0ab7),
[StdCmdDelete.activated()](../../da/dc8/classStdCmdDelete.html#a120710ae4a8c0f26451596002a176ee7),
[StdCmdLinkMakeGroup.activated()](../../d8/db4/classStdCmdLinkMakeGroup.html#afbac678a966340088d0d13603d4865f0),
[StdCmdLinkMake.activated()](../../df/d19/classStdCmdLinkMake.html#a227d693344e3d5329aad38d5ece1606d),
[StdCmdLinkMakeRelative.activated()](../../d1/dc3/classStdCmdLinkMakeRelative.html#a17226f2227a0ad3b9fc8f39eec4577ed),
[StdCmdLinkImport.activated()](../../d6/df0/classStdCmdLinkImport.html#a9f18aa0e471dba1b9fd07ae2d73c1eb0),
[StdCmdLinkImportAll.activated()](../../d1/d95/classStdCmdLinkImportAll.html#a589020e4cea9b86e1167d781473691a9),
[StdCmdMeasurementSimple.activated()](../../d5/d90/classStdCmdMeasurementSimple.html#ac53945e4ee05a762e0719af8b9a28982),
[StdCmdTextDocument.activated()](../../d7/d81/classStdCmdTextDocument.html#a456c9dc491ef85f67c8e28e07b2081bb),
[StdCmdPart.activated()](../../db/d9b/classStdCmdPart.html#ae0c18c37cac347f8164006c0d425379f),
[StdCmdGroup.activated()](../../d0/de4/classStdCmdGroup.html#a44a9faa66df180f400cd830bb538771d),
[CmdSketcherConstrainHorizontal.activated()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#adc766562bb486afb5941fc9bade87c59),
[CmdSketcherConstrainVertical.activated()](../../d7/d37/classCmdSketcherConstrainVertical.html#a0f174c055305b510bc2b3ce16eb6e80b),
[CmdSketcherConstrainLock.activated()](../../d9/dc2/classCmdSketcherConstrainLock.html#a337b578fd38e4359b3177138a91a9162),
[CmdSketcherConstrainBlock.activated()](../../d9/d19/classCmdSketcherConstrainBlock.html#a9aae799a29f3aac8783c1f99d1ebb21e),
[CmdSketcherConstrainCoincident.activated()](../../d0/d76/classCmdSketcherConstrainCoincident.html#a52a709fffac7be283b7b50f8687e8602),
[CmdSketcherConstrainDistance.activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainPointOnObject.activated()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#aa6f7ed1adb19f60b65703fafe91fdda9),
[CmdSketcherConstrainDistanceX.activated()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#a175608d3c6099fc7504de3b5641a01c0),
[CmdSketcherConstrainDistanceY.activated()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a59b776e3be604ff1686d112c0f82334b),
[CmdSketcherConstrainParallel.activated()](../../d3/df0/classCmdSketcherConstrainParallel.html#a4c2b4c186452210ed3e69fb1c5f1afe6),
[CmdSketcherConstrainPerpendicular.activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainTangent.activated()](../../d8/d80/classCmdSketcherConstrainTangent.html#a49b68ec579dfa3ac0410539e34096f90),
[CmdSketcherConstrainRadius.activated()](../../d2/d16/classCmdSketcherConstrainRadius.html#a210220527e41b3ad828269b80a359354),
[CmdSketcherConstrainDiameter.activated()](../../da/dbe/classCmdSketcherConstrainDiameter.html#af5d04e1e2fa404f140625af1b917f186),
[CmdSketcherConstrainRadiam.activated()](../../d6/d18/classCmdSketcherConstrainRadiam.html#aee6c0c85caaecf9e7bcd99dff1efd6bc),
[CmdSketcherConstrainAngle.activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[CmdSketcherConstrainEqual.activated()](../../de/dbe/classCmdSketcherConstrainEqual.html#ac247e0d1e55a27e0e40c204965f758be),
[CmdSketcherConstrainSymmetric.activated()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#afc33b5d3e672956b47801982de4611ef),
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation.add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[PathScripts.PathOp.ObjectOp.addBaseProperty()](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#afa5b04feb00e8b7baa2df14a8ea27009),
[TechDrawGui::TaskCosVertex.addCosVertex()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a7404a47aa9c2477be4ccbd928347df58),
[PathScripts.PathOp.ObjectOp.addOpValues()](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#a0e62a83abe1938d3fc801ece79df35e2),
[ArchStructure.StructSelectionObserver.addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[Gui::ManualAlignment.align()](../../d7/d97/classGui_1_1ManualAlignment.html#a6e935c07614fae01f3aa3d6ab4150dcd),
[SpreadsheetGui::PropertiesDialog.apply()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a5aa7098c11c9d893cb9b30cd6541939d),
[CmdSketcherConstrainHorizontal.applyConstraint()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#a36f07e42457531be9ed67008ba95d021),
[CmdSketcherConstrainVertical.applyConstraint()](../../d7/d37/classCmdSketcherConstrainVertical.html#adf3ea9ac8dd73b137225507c8028e880),
[CmdSketcherConstrainLock.applyConstraint()](../../d9/dc2/classCmdSketcherConstrainLock.html#aa27c938f88973099b74d9474476d4254),
[CmdSketcherConstrainBlock.applyConstraint()](../../d9/d19/classCmdSketcherConstrainBlock.html#a44714bcb118510d4f3edb4ab2c65192d),
[CmdSketcherConstrainCoincident.applyConstraint()](../../d0/d76/classCmdSketcherConstrainCoincident.html#ade167ceeb29989d40bfab4bd2023c698),
[CmdSketcherConstrainDistance.applyConstraint()](../../d4/de5/classCmdSketcherConstrainDistance.html#a9c0f733b397d4f7e05af5f7c70f9debb),
[CmdSketcherConstrainPointOnObject.applyConstraint()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#a70d28fda1de1503aa99cf66b055420d1),
[CmdSketcherConstrainDistanceX.applyConstraint()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#abf16c738ea7247db91721d5d14d279fc),
[CmdSketcherConstrainDistanceY.applyConstraint()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a2df22f90384fbde7d951992c9564d3ad),
[CmdSketcherConstrainParallel.applyConstraint()](../../d3/df0/classCmdSketcherConstrainParallel.html#a8be8ee71d2e5dc2f276abb4d9eba2be9),
[CmdSketcherConstrainPerpendicular.applyConstraint()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#aa62bab542b8f016bd752fdef90110778),
[CmdSketcherConstrainTangent.applyConstraint()](../../d8/d80/classCmdSketcherConstrainTangent.html#a90a8595e30112cb64ddb61088c3af96b),
[CmdSketcherConstrainRadius.applyConstraint()](../../d2/d16/classCmdSketcherConstrainRadius.html#a0529327862aefd7a8d9d0bed9a03571c),
[CmdSketcherConstrainDiameter.applyConstraint()](../../da/dbe/classCmdSketcherConstrainDiameter.html#a2cba7a76a06cffab82d09cdfcddf0065),
[CmdSketcherConstrainRadiam.applyConstraint()](../../d6/d18/classCmdSketcherConstrainRadiam.html#a08e2367864e5c690e2c6607f10af5e7d),
[CmdSketcherConstrainAngle.applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[CmdSketcherConstrainEqual.applyConstraint()](../../de/dbe/classCmdSketcherConstrainEqual.html#a7efdda717363d452685832c9670be199),
[CmdSketcherConstrainSymmetric.applyConstraint()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#af292ec0892fe051d1d5f06fb9440664e),
[PathScripts.PathProfile.ObjectProfile.areaOpProperties()](../../d2/d5f/classPathScripts_1_1PathProfile_1_1ObjectProfile.html#ae1e80b5c38472a4f09675e6ad13a2a2e),
[ArchWall.areSameWallTypes()](../../d2/d8e/namespaceArchWall.html#a289f6e980eba7dd10b74dcfb84dd0c92),
[draftobjects.bspline.BSpline.assureProperties()](../../d5/dee/classdraftobjects_1_1bspline_1_1BSpline.html#a635b33ad1c26cd01a08b7f7409a04fb3),
[Sketcher::SketchAnalysis.autoconstraint()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a593a8426260651db5e7a7fc942b9a647),
[TechDrawGui::QGIViewBalloon.balloonLabelDragFinished()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a287e2445be0351ce418e50714a807ea4),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[MeshGui::ViewProviderMesh.clipMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2163df57149a01e40800e85a88d3ce20),
[ArchSectionPlane.closeViewer()](../../d8/d49/namespaceArchSectionPlane.html#aa159e2389526d677138c754c18152c1c),
[Gui::Dialog::TransformStrategy.commitTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6c3d7160157eac0289a597bb3a44504e),
[ArchBuildingPart.convertFloors()](../../d7/dc5/namespaceArchBuildingPart.html#a16dae69e02051b482503906c88649259),
[TechDrawGui::TaskRichAnno.createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[SketcherGui::DrawSketchHandler.createAutoConstraints()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#aaeb21f657e7a40232d0b9e275295765c),
[TechDrawGui::QGSPage.createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[TechDrawGui::TaskCenterLine.createCenterLine()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a9fb5dd30626ee43ec4671c9ea2ce150b),
[TechDrawGui::TaskCosmeticLine.createCosmeticLine()](../../dc/dff/classTechDrawGui_1_1TaskCosmeticLine.html#a5a6abfc366854b3475bd709ffc38f1c6),
[TechDrawGui::TaskDetail.createDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a301980d3db23b9a4d960227c9c78fa03),
[TechDrawGui::TaskHatch.createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[TechDrawGui::TaskLeaderLine.createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[ArchEquipment.createMeshView()](../../db/d00/namespaceArchEquipment.html#a7325bf277971b5b271fa96eebb2d83c7),
[TechDrawGui::TaskSectionView.createSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ac5902eeba616fd351e4de4546c7634de),
[ReverseEngineeringGui::SegmentationManual.createSegment()](../../dc/d04/classReverseEngineeringGui_1_1SegmentationManual.html#a95ac22eb241f58d992ffe08f784eb5d0),
[Gui::PointMarker.customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[PointsGui::ViewProviderScattered.cut()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#a6e93ecaa9bbca01c9cd9c294ba22f38c),
[PointsGui::ViewProviderStructured.cut()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#a808184849a3543a6d70c263099506c98),
[MeshGui::MeshSplit.cutMesh()](../../d9/de5/classMeshGui_1_1MeshSplit.html#aebb96b9863c72d1248d3372c0a3d6a65),
[TechDrawGui::QGIViewDimension.datumLabelDragFinished()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a7551b2b00434385637e0d6d9d7ec4bee),
[MeshGui::RemoveComponents.deleteSelection()](../../d8/d04/classMeshGui_1_1RemoveComponents.html#a826939ac232bef8ebd5850b7629dd827),
[SpreadsheetGui::SheetTableView.deleteSelection()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a815da32c5d5f77951bce6ddf5e5954f9),
[SketcherGui::ViewProviderSketch.editDoubleClicked()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#abdbeadcb7528aec366231ca51b1ffb46),
[PathScripts.PathToolController.ToolController.ensureUseLegacyTool()](../../d6/d67/classPathScripts_1_1PathToolController_1_1ToolController.html#aed66e1155d86f7e3006e83af1303da96),
[TechDrawGui.execHoleCircle()](../../dc/de6/namespaceTechDrawGui.html#a300c7a5c7d4f155d1349be760b7bb42c),
[draftobjects.bspline.BSpline.execute()](../../d5/dee/classdraftobjects_1_1bspline_1_1BSpline.html#a4c2266ab57f63be33c9fb1df115d94a2),
[draftobjects.ellipse.Ellipse.execute()](../../df/d03/classdraftobjects_1_1ellipse_1_1Ellipse.html#a7730b965c9e41355b00cc6e7ad96770c),
[Sketcher::SketchObject.fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[MeshGui::ViewProviderMesh.fillHole()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a55fed5815a20d06bf57a561b685a82de),
[draftviewproviders.view_wire.ViewProviderWire.flatten()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a15505f930754af9e7bbff1aafe36249b),
[draftutils.init_tools.get_draft_drawing_commands()](../../de/d75/group__draftutils.html#gaaeaa1509b48106f3074c10ad751c6c8a),
[draftutils.init_tools.get_draft_modification_commands()](../../de/d75/group__draftutils.html#gaae36432ef61ded1fe51f4fa83683f4bd),
[Part::FaceMakerSimple.getBriefExplanation()](../../d3/d64/classPart_1_1FaceMakerSimple.html#a32974bfedfccb925fd7a11455b165648),
[Part::FaceMakerBullseye.getBriefExplanation()](../../de/d69/classPart_1_1FaceMakerBullseye.html#a502a5f65083e598683670f8f4acab40c),
[Part::FaceMakerCheese.getBriefExplanation()](../../d0/d37/classPart_1_1FaceMakerCheese.html#a4824c13ac332a67cc0436a07766daf6a),
[Part::FaceMakerExtrusion.getBriefExplanation()](../../d2/d2e/classPart_1_1FaceMakerExtrusion.html#a876a4a000e2cfceda5127cf8ccc72e22),
[InitGui.ArchWorkbench.GetClassName()](../../db/de0/classInitGui_1_1ArchWorkbench.html#a31f172a63690a4e1d54cee23413fc68f),
[InitGui.DraftWorkbench.GetClassName()](../../d0/d4d/classInitGui_1_1DraftWorkbench.html#a39c59d39e245505787b0cfdcb3c5e204),
[ArchMaterial.getDocumentMaterials()](../../dc/d52/namespaceArchMaterial.html#a42965fbf681410521c1d183fd3b5df93),
[ArchBuildingPart.CommandBuildingPart.GetResources()](../../d0/deb/classArchBuildingPart_1_1CommandBuildingPart.html#a18653cc5345f9b4ca7a138d92e9f7b3b),
[ArchCurtainWall.CommandArchCurtainWall.GetResources()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#a615aefaf67e0751a2893a0dbfddb165c),
[ArchGrid.CommandArchGrid.GetResources()](../../d9/d92/classArchGrid_1_1CommandArchGrid.html#ac07b00c2a46ae18d7f96bef7559db294),
[ArchPanel.CommandPanel.GetResources()](../../d9/d86/classArchPanel_1_1CommandPanel.html#ac67a7d85081050a063db28d13ac60cc5),
[ArchPanel.CommandPanelCut.GetResources()](../../de/d5b/classArchPanel_1_1CommandPanelCut.html#a3d360819de7f2aa1728aaadf7a465d74),
[ArchPanel.CommandPanelSheet.GetResources()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#a979a429a1840cd49a1734a1fd25548cf),
[ArchPanel.CommandNest.GetResources()](../../d6/d6a/classArchPanel_1_1CommandNest.html#aa7d0c32d3e92d6cd3483af33240c1289),
[ArchPanel.CommandPanelGroup.GetResources()](../../d6/dbf/classArchPanel_1_1CommandPanelGroup.html#a187a13e71c7c128d3c89c0cbc0acb39f),
[ArchProfile.Arch_Profile.GetResources()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#a10b6bc033bdd90fc7b3549acf3de6aae),
[ArchSchedule.CommandArchSchedule.GetResources()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#a2440fd8a7650e3c5a97246a2de25403b),
[ArchTruss.CommandArchTruss.GetResources()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aae57642c1e900333185ee6dc477c5f8b),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.GetResources()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a07f7db1e2e940c034d5089128b61b102),
[draftguitools.gui_arcs.Arc.GetResources()](../../da/d4f/classdraftguitools_1_1gui__arcs_1_1Arc.html#af9a104d7062b8ac34436e42e850fcc16),
[draftguitools.gui_arcs.Arc_3Points.GetResources()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#a65f314b98d40119d1428571848c09cc8),
[draftguitools.gui_arcs.ArcGroup.GetResources()](../../d2/d47/classdraftguitools_1_1gui__arcs_1_1ArcGroup.html#ac2c2eff69fd918a164d41901417b0040),
[draftguitools.gui_array_simple.Array.GetResources()](../../da/d0e/classdraftguitools_1_1gui__array__simple_1_1Array.html#a930ed24dbae29cb09dd1941fec642564),
[draftguitools.gui_array_simple.LinkArray.GetResources()](../../d3/df7/classdraftguitools_1_1gui__array__simple_1_1LinkArray.html#a31b0a911ae0961e17015f39267060975),
[draftguitools.gui_arrays.ArrayGroup.GetResources()](../../df/d22/classdraftguitools_1_1gui__arrays_1_1ArrayGroup.html#a0abb5cf61472aeaeb39b463769901c1c),
[draftguitools.gui_beziers.BezCurve.GetResources()](../../d2/dce/classdraftguitools_1_1gui__beziers_1_1BezCurve.html#ac072d5dfbf11ca4483c6090aa6ecf34b),
[draftguitools.gui_beziers.CubicBezCurve.GetResources()](../../de/d5e/classdraftguitools_1_1gui__beziers_1_1CubicBezCurve.html#ab3ff58a33156ede1ccedd75654f0da3b),
[draftguitools.gui_beziers.BezierGroup.GetResources()](../../d0/d61/classdraftguitools_1_1gui__beziers_1_1BezierGroup.html#a98cfd612f8668722af3d5bc3f5b36303),
[draftguitools.gui_circles.Circle.GetResources()](../../d0/d11/classdraftguitools_1_1gui__circles_1_1Circle.html#a66d515c17bb02d0d5461e3c405a86abf),
[draftguitools.gui_circulararray.CircularArray.GetResources()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#a404f731569e5e929d2f8a17810d3dbcd),
[draftguitools.gui_clone.Clone.GetResources()](../../df/d67/classdraftguitools_1_1gui__clone_1_1Clone.html#aa78746ca4ae1516171b34731561dd12b),
[draftguitools.gui_dimension_ops.FlipDimension.GetResources()](../../de/d3e/classdraftguitools_1_1gui__dimension__ops_1_1FlipDimension.html#a08721c463ad7a78078d535013f99b835),
[draftguitools.gui_dimensions.Dimension.GetResources()](../../d5/d6a/classdraftguitools_1_1gui__dimensions_1_1Dimension.html#a05b776dd5d0cf43995127f5c1f390738),
[draftguitools.gui_downgrade.Downgrade.GetResources()](../../de/d8b/classdraftguitools_1_1gui__downgrade_1_1Downgrade.html#a5ec564520c9752a4658b4f3bb82474cc),
[draftguitools.gui_draft2sketch.Draft2Sketch.GetResources()](../../dd/d7c/classdraftguitools_1_1gui__draft2sketch_1_1Draft2Sketch.html#afe99430a589801da61f00b2c9a278dde),
[draftguitools.gui_drawing.Drawing.GetResources()](../../db/d99/classdraftguitools_1_1gui__drawing_1_1Drawing.html#acb6b338dae054f6cd5e071599d955122),
[draftguitools.gui_ellipses.Ellipse.GetResources()](../../db/d98/classdraftguitools_1_1gui__ellipses_1_1Ellipse.html#a6f62717aa4e25c9abd0cd7abd9ec5c7f),
[draftguitools.gui_facebinders.Facebinder.GetResources()](../../da/dc9/classdraftguitools_1_1gui__facebinders_1_1Facebinder.html#a120bf01ef18275b0cee949689b543149),
[draftguitools.gui_fillets.Fillet.GetResources()](../../da/d40/classdraftguitools_1_1gui__fillets_1_1Fillet.html#a5cfa6f3e57257d87473fa5eba653b1af),
[draftguitools.gui_grid.ToggleGrid.GetResources()](../../dd/d85/classdraftguitools_1_1gui__grid_1_1ToggleGrid.html#aa723936d2ad70f1cad986bccda056c4a),
[draftguitools.gui_groups.AddToGroup.GetResources()](../../d8/d83/classdraftguitools_1_1gui__groups_1_1AddToGroup.html#ad1b480c6ae563bdc27204bd00b510d44),
[draftguitools.gui_groups.SelectGroup.GetResources()](../../d2/d7d/classdraftguitools_1_1gui__groups_1_1SelectGroup.html#aa4eaae32e6c24e5ed891eaa7e8d2cb9a),
[draftguitools.gui_groups.SetAutoGroup.GetResources()](../../d4/df8/classdraftguitools_1_1gui__groups_1_1SetAutoGroup.html#a67e7c1fba15f368aaa6f354ccb4c4e32),
[draftguitools.gui_groups.AddToConstruction.GetResources()](../../d3/d06/classdraftguitools_1_1gui__groups_1_1AddToConstruction.html#aff69aaa62defd70223f97ff28b7e89fb),
[draftguitools.gui_groups.AddNamedGroup.GetResources()](../../db/d7d/classdraftguitools_1_1gui__groups_1_1AddNamedGroup.html#a408219662ec1a1b2f15f49bdb22b80d4),
[draftguitools.gui_hatch.Draft_Hatch.GetResources()](../../df/d17/classdraftguitools_1_1gui__hatch_1_1Draft__Hatch.html#aba6c7c988daa7eb183eea1bb2f2ac117),
[draftguitools.gui_heal.Heal.GetResources()](../../d5/d39/classdraftguitools_1_1gui__heal_1_1Heal.html#aa1375df1d0407f70778688f2eaf205d9),
[draftguitools.gui_join.Join.GetResources()](../../d4/d50/classdraftguitools_1_1gui__join_1_1Join.html#ac39af52d2e8c4af5a9ac242e8a569c9d),
[draftguitools.gui_labels.Label.GetResources()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a3aa94974613abfd99710ca4dfd45ab15),
[draftguitools.gui_layers.Layer.GetResources()](../../d1/da7/classdraftguitools_1_1gui__layers_1_1Layer.html#a1c5cb2b64224074b19138ec8e7617827),
[draftguitools.gui_line_add_delete.AddPoint.GetResources()](../../d2/d9e/classdraftguitools_1_1gui__line__add__delete_1_1AddPoint.html#aa063aca1699ad0cca061768b1bf3d977),
[draftguitools.gui_line_add_delete.DelPoint.GetResources()](../../df/d89/classdraftguitools_1_1gui__line__add__delete_1_1DelPoint.html#a4ae6e9bb0e6d14aad1ea4c83324d6a19),
[draftguitools.gui_lines.Line.GetResources()](../../da/d8f/classdraftguitools_1_1gui__lines_1_1Line.html#ad5ce5554bf0129b914df1c43a20a8ede),
[draftguitools.gui_lines.Wire.GetResources()](../../d0/d34/classdraftguitools_1_1gui__lines_1_1Wire.html#af6cdace99729e608403719bcca09c7ed),
[draftguitools.gui_lineslope.LineSlope.GetResources()](../../d4/d0f/classdraftguitools_1_1gui__lineslope_1_1LineSlope.html#ad9de101a8b1fd342664ea3aed9d5f496),
[draftguitools.gui_mirror.Mirror.GetResources()](../../d8/dbd/classdraftguitools_1_1gui__mirror_1_1Mirror.html#ac1f77193c2892ee52038070baa99c6ae),
[draftguitools.gui_move.Move.GetResources()](../../d2/df5/classdraftguitools_1_1gui__move_1_1Move.html#a1505a69157797f1026c74f26aa832ff8),
[draftguitools.gui_offset.Offset.GetResources()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#abb9d41454da8534927b401e7b1d00022),
[draftguitools.gui_orthoarray.OrthoArray.GetResources()](../../dc/d0f/classdraftguitools_1_1gui__orthoarray_1_1OrthoArray.html#a697648c622a975e625a3c0ceb1e8a726),
[draftguitools.gui_patharray.PathArray.GetResources()](../../dd/d56/classdraftguitools_1_1gui__patharray_1_1PathArray.html#a39aa07fb4ad1aedaaa529135281a5605),
[draftguitools.gui_patharray.PathLinkArray.GetResources()](../../d7/d19/classdraftguitools_1_1gui__patharray_1_1PathLinkArray.html#addd17d57fce3fd0d3aeea17dd6051f52),
[draftguitools.gui_pathtwistedarray.PathTwistedArray.GetResources()](../../d2/d4f/classdraftguitools_1_1gui__pathtwistedarray_1_1PathTwistedArray.html#a8abea1e8179282fead63f1745e18ac6e),
[draftguitools.gui_pathtwistedarray.PathTwistedLinkArray.GetResources()](../../da/d6c/classdraftguitools_1_1gui__pathtwistedarray_1_1PathTwistedLinkArray.html#a8f33c3f6610a1f216b3b0cda20763609),
[draftguitools.gui_planeproxy.Draft_WorkingPlaneProxy.GetResources()](../../d3/d70/classdraftguitools_1_1gui__planeproxy_1_1Draft__WorkingPlaneProxy.html#a4ac87352a2efbbbc43717b7830764b2a),
[draftguitools.gui_pointarray.PointArray.GetResources()](../../d1/d71/classdraftguitools_1_1gui__pointarray_1_1PointArray.html#a4da1d72c5d255430647ceca56a1d47ab),
[draftguitools.gui_pointarray.PointLinkArray.GetResources()](../../d6/df6/classdraftguitools_1_1gui__pointarray_1_1PointLinkArray.html#afc630e0c39d9cc6ad304823c68af22a9),
[draftguitools.gui_points.Point.GetResources()](../../d7/dc7/classdraftguitools_1_1gui__points_1_1Point.html#a07747299f63df4a0f8c31b9e1de27754),
[draftguitools.gui_polararray.PolarArray.GetResources()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#aef9d35aa99a6c1cac744027002b6f115),
[draftguitools.gui_polygons.Polygon.GetResources()](../../df/d3d/classdraftguitools_1_1gui__polygons_1_1Polygon.html#ad0c395027428289c70da60cba7b1850c),
[draftguitools.gui_rectangles.Rectangle.GetResources()](../../dd/d46/classdraftguitools_1_1gui__rectangles_1_1Rectangle.html#a17fd664bacce4eb6013f7a212132cf34),
[draftguitools.gui_rotate.Rotate.GetResources()](../../d5/d4b/classdraftguitools_1_1gui__rotate_1_1Rotate.html#abc6ef109676ca97f9f1396c4250a01c2),
[draftguitools.gui_scale.Scale.GetResources()](../../d5/d4f/classdraftguitools_1_1gui__scale_1_1Scale.html#aa6faf83373e4c0afcd6e2a19a59c204e),
[draftguitools.gui_selectplane.Draft_SelectPlane.GetResources()](../../dc/d53/classdraftguitools_1_1gui__selectplane_1_1Draft__SelectPlane.html#a0279a2c6bcd225420d83fbc36c8fbab6),
[draftguitools.gui_shape2dview.Shape2DView.GetResources()](../../d5/d96/classdraftguitools_1_1gui__shape2dview_1_1Shape2DView.html#aa38b7b1b4408e6a47c12f9ed7a13c8c6),
[draftguitools.gui_shapestrings.ShapeString.GetResources()](../../db/d17/classdraftguitools_1_1gui__shapestrings_1_1ShapeString.html#acce396bf1af8a030de96011b1d065304),
[draftguitools.gui_snaps.Draft_Snap_Lock.GetResources()](../../dc/d29/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Lock.html#aad4f283b9654d079ec797a9a5645c803),
[draftguitools.gui_snaps.Draft_Snap_Midpoint.GetResources()](../../d9/d96/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Midpoint.html#a1f6a4ed1aa3edfcce689f9d9b01a1017),
[draftguitools.gui_snaps.Draft_Snap_Perpendicular.GetResources()](../../d3/d70/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Perpendicular.html#aa77782c4c28fbd7a2de88de63bf03437),
[draftguitools.gui_snaps.Draft_Snap_Grid.GetResources()](../../dd/d36/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Grid.html#a59a0c25c85a4b662f9169118ab194240),
[draftguitools.gui_snaps.Draft_Snap_Intersection.GetResources()](../../da/d40/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Intersection.html#a71fd2c39d238415c9b9118b31eb52e05),
[draftguitools.gui_snaps.Draft_Snap_Parallel.GetResources()](../../d3/d14/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Parallel.html#a2311cf403783813437eaed2fc8a7ced6),
[draftguitools.gui_snaps.Draft_Snap_Endpoint.GetResources()](../../da/d71/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Endpoint.html#abf6234248d14d57891ba1435204f2542),
[draftguitools.gui_snaps.Draft_Snap_Angle.GetResources()](../../df/d9d/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Angle.html#af017e1e0244c7fa3bf350d3156118388),
[draftguitools.gui_snaps.Draft_Snap_Center.GetResources()](../../d1/d1a/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Center.html#aa15ae7defec1712adf5183c660709258),
[draftguitools.gui_snaps.Draft_Snap_Extension.GetResources()](../../d4/d11/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Extension.html#a411ef37154d791d98751a7d7863c58f3),
[draftguitools.gui_snaps.Draft_Snap_Near.GetResources()](../../d4/d98/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Near.html#adf4b02b66f625323270c6995639e041d),
[draftguitools.gui_snaps.Draft_Snap_Ortho.GetResources()](../../d7/dc3/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Ortho.html#a3373cbb69457699c8483461682ba2125),
[draftguitools.gui_snaps.Draft_Snap_Special.GetResources()](../../d3/d0c/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Special.html#ac9545e45bdbb8ea135cd7efb2faeca39),
[draftguitools.gui_snaps.Draft_Snap_Dimensions.GetResources()](../../d9/d55/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__Dimensions.html#a252566d5474c310e7ec43715897362e9),
[draftguitools.gui_snaps.Draft_Snap_WorkingPlane.GetResources()](../../d6/df2/classdraftguitools_1_1gui__snaps_1_1Draft__Snap__WorkingPlane.html#a034874ff8dcce6c550b9485b0575258b),
[draftguitools.gui_snaps.ShowSnapBar.GetResources()](../../d4/d15/classdraftguitools_1_1gui__snaps_1_1ShowSnapBar.html#a974f2ec03eecdb04c0f03249d7fa4d09),
[draftguitools.gui_splines.BSpline.GetResources()](../../d1/d3f/classdraftguitools_1_1gui__splines_1_1BSpline.html#a8dfcdc7b089fe3693d8047fc054bd807),
[draftguitools.gui_split.Split.GetResources()](../../db/d21/classdraftguitools_1_1gui__split_1_1Split.html#aceb63d1dbfb9c75034c06e4374626733),
[draftguitools.gui_stretch.Stretch.GetResources()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a4de4b8e1274f6a2a1326465c7a063e95),
[draftguitools.gui_styles.ApplyStyle.GetResources()](../../d6/d90/classdraftguitools_1_1gui__styles_1_1ApplyStyle.html#a262ca7b624280853073c35bc28b82308),
[draftguitools.gui_subelements.SubelementHighlight.GetResources()](../../d4/db2/classdraftguitools_1_1gui__subelements_1_1SubelementHighlight.html#ab6ec200a507c7e218ca117fd186d6e69),
[draftguitools.gui_texts.Text.GetResources()](../../d1/d46/classdraftguitools_1_1gui__texts_1_1Text.html#a1e4529b05bb4b7fadbe71dde0415ea04),
[draftguitools.gui_togglemodes.ToggleConstructionMode.GetResources()](../../d5/d96/classdraftguitools_1_1gui__togglemodes_1_1ToggleConstructionMode.html#a6882e23def0e6b4a6a3be2707bec83d2),
[draftguitools.gui_togglemodes.ToggleContinueMode.GetResources()](../../d1/dc5/classdraftguitools_1_1gui__togglemodes_1_1ToggleContinueMode.html#acb092d02692b2da531bd1f893bd203ca),
[draftguitools.gui_togglemodes.ToggleDisplayMode.GetResources()](../../d6/dc5/classdraftguitools_1_1gui__togglemodes_1_1ToggleDisplayMode.html#ace9c5ee6a04b25d100b9e0f9837ca0f2),
[draftguitools.gui_trimex.Trimex.GetResources()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a7ee59cb6da0182075720b0bd0b622857),
[draftguitools.gui_upgrade.Upgrade.GetResources()](../../d2/dd7/classdraftguitools_1_1gui__upgrade_1_1Upgrade.html#aa646e8d32622c16100f86291ce1d4a97),
[draftguitools.gui_wire2spline.WireToBSpline.GetResources()](../../d4/dd5/classdraftguitools_1_1gui__wire2spline_1_1WireToBSpline.html#a2da7e384f7056025256631a8d59b08f9),
[MeshFlatteningCommand.CreateFlatMesh.GetResources()](../../db/d72/classMeshFlatteningCommand_1_1CreateFlatMesh.html#a2414738432a65ffc82b69fd7d6e2c07e),
[MeshFlatteningCommand.CreateFlatFace.GetResources()](../../d4/dbe/classMeshFlatteningCommand_1_1CreateFlatFace.html#a1876fdfeb58d12a02b2e9e160e99854c),
[PathScripts.PathArray.CommandPathArray.GetResources()](../../d4/da0/classPathScripts_1_1PathArray_1_1CommandPathArray.html#a95fb87bca7d7dc5af631131e4ab8f9a8),
[PathScripts.PathCamoticsGui.CommandCamoticsSimulate.GetResources()](../../d3/d30/classPathScripts_1_1PathCamoticsGui_1_1CommandCamoticsSimulate.html#ad67f4c93d880f7ffb167d558256e800f),
[PathScripts.PathComment.CommandPathComment.GetResources()](../../d0/d5f/classPathScripts_1_1PathComment_1_1CommandPathComment.html#ae81a7ab36bee0b81639759b1dc451003),
[PathScripts.PathCopy.CommandPathCopy.GetResources()](../../df/d75/classPathScripts_1_1PathCopy_1_1CommandPathCopy.html#a217c57ca73bdf8e2da30a3d4d7822dc1),
[PathScripts.PathDressupAxisMap.CommandPathDressup.GetResources()](../../df/d57/classPathScripts_1_1PathDressupAxisMap_1_1CommandPathDressup.html#a78242bc546be7b3fd4d789c564e39357),
[PathScripts.PathDressupDogbone.CommandDressupDogbone.GetResources()](../../d9/dcd/classPathScripts_1_1PathDressupDogbone_1_1CommandDressupDogbone.html#a49726a4d9d7351f747d0b0727bae79ee),
[PathScripts.PathDressupDragknife.CommandDressupDragknife.GetResources()](../../da/db4/classPathScripts_1_1PathDressupDragknife_1_1CommandDressupDragknife.html#a4f688ce53830d1a908ad9e54995d8fe5),
[PathScripts.PathDressupLeadInOut.CommandPathDressupLeadInOut.GetResources()](../../d6/d84/classPathScripts_1_1PathDressupLeadInOut_1_1CommandPathDressupLeadInOut.html#a0a2914058e03a0be5d830ab07ce5ba8c),
[PathScripts.PathDressupPathBoundaryGui.CommandPathDressupPathBoundary.GetResources()](../../d5/d5e/classPathScripts_1_1PathDressupPathBoundaryGui_1_1CommandPathDressupPathBoundary.html#aff75f02e995023d3a3b8cfaa8b18bc4c),
[PathScripts.PathDressupRampEntry.CommandPathDressupRampEntry.GetResources()](../../dd/d95/classPathScripts_1_1PathDressupRampEntry_1_1CommandPathDressupRampEntry.html#a807f825e8ea0455a1f9647c45229452a),
[PathScripts.PathDressupTagGui.CommandPathDressupTag.GetResources()](../../d9/dbf/classPathScripts_1_1PathDressupTagGui_1_1CommandPathDressupTag.html#aadb1b98f90c51adc14a14b9658f2a641),
[PathScripts.PathDressupZCorrect.CommandPathDressup.GetResources()](../../d3/d5a/classPathScripts_1_1PathDressupZCorrect_1_1CommandPathDressup.html#a1a9907f6ac58d4aca72f47448fe3bd34),
[PathScripts.PathFixture.CommandPathFixture.GetResources()](../../dc/d61/classPathScripts_1_1PathFixture_1_1CommandPathFixture.html#a89bc38c930216e1e63dd7c1b45cee590),
[PathScripts.PathHop.CommandPathHop.GetResources()](../../de/d08/classPathScripts_1_1PathHop_1_1CommandPathHop.html#a9d24c9eb7b0a09ec362d0c2a892993c9),
[PathScripts.PathInspect.CommandPathInspect.GetResources()](../../d5/d86/classPathScripts_1_1PathInspect_1_1CommandPathInspect.html#affc0195f2ef22ec7c34210af1e279642),
[PathScripts.PathOpGui.CommandSetStartPoint.GetResources()](../../d6/dbd/classPathScripts_1_1PathOpGui_1_1CommandSetStartPoint.html#a0931e683d9e33539098c84e8d97d8ea7),
[PathScripts.PathPlane.CommandPathPlane.GetResources()](../../d7/d45/classPathScripts_1_1PathPlane_1_1CommandPathPlane.html#a4370cb4df35fce6937efaab43856e34c),
[PathScripts.PathPost.CommandPathPost.GetResources()](../../d3/d2b/classPathScripts_1_1PathPost_1_1CommandPathPost.html#adfabeac6bfa1812635689575075a1b15),
[PathScripts.PathSanity.CommandPathSanity.GetResources()](../../d1/d9f/classPathScripts_1_1PathSanity_1_1CommandPathSanity.html#af77027383a73f5a54c057f13f9ea3a1e),
[PathScripts.PathSimpleCopy.CommandPathSimpleCopy.GetResources()](../../d4/d36/classPathScripts_1_1PathSimpleCopy_1_1CommandPathSimpleCopy.html#a73530e2db7c1f4ef34b2fb82503cd000),
[PathScripts.PathStop.CommandPathStop.GetResources()](../../d3/d4b/classPathScripts_1_1PathStop_1_1CommandPathStop.html#a86a7695c5d987bbfb9572b4414c38ddf),
[PathScripts.PathToolBitCmd.CommandToolBitSave.GetResources()](../../df/d30/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitSave.html#a521f4fdd27aaba4fc64e5d3bcd1720bb),
[PathScripts.PathToolControllerGui.CommandPathToolController.GetResources()](../../d2/d0a/classPathScripts_1_1PathToolControllerGui_1_1CommandPathToolController.html#aa14464ebb3d10a2359018dcccaa49bec),
[PathScripts.PathToolLibraryEditor.CommandToolLibraryEdit.GetResources()](../../da/dea/classPathScripts_1_1PathToolLibraryEditor_1_1CommandToolLibraryEdit.html#a0bc805d6d5ecd8cc61ec277fed15dbc7),
[Gui::ViewProviderDocumentObject.getTransactionText()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a6622915272f0a21c7d7dacda5f93df65),
[Part::FaceMakerSimple.getUserFriendlyName()](../../d3/d64/classPart_1_1FaceMakerSimple.html#afa396c0d84f1596b9b829aef6829371e),
[Part::FaceMakerBullseye.getUserFriendlyName()](../../de/d69/classPart_1_1FaceMakerBullseye.html#a3ee7a2b7516f4bc7496f3f9dd55c7b45),
[Part::FaceMakerCheese.getUserFriendlyName()](../../d0/d37/classPart_1_1FaceMakerCheese.html#a5ae4f6a0bb1a6a582fc9ff87183af6fa),
[Part::FaceMakerExtrusion.getUserFriendlyName()](../../d2/d2e/classPart_1_1FaceMakerExtrusion.html#a368e130bfeb1a0608981ce99ab131906),
[PartDesign::Helix.Helix()](../../d3/d78/classPartDesign_1_1Helix.html#af5b3edc469728ac5981e35e29412b61c),
[Gui::Application.importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[PathScripts.PathPocketBase.ObjectPocket.initAreaOp()](../../d8/dbc/classPathScripts_1_1PathPocketBase_1_1ObjectPocket.html#ac272e8d355032255d99c006398b392b8),
[PathScripts.PathDrilling.ObjectDrilling.initCircularHoleOperation()](../../d0/dff/classPathScripts_1_1PathDrilling_1_1ObjectDrilling.html#ac2630db1660ef7d3b94f974f44f42ca8),
[PathScripts.PathHelix.ObjectHelix.initCircularHoleOperation()](../../da/d14/classPathScripts_1_1PathHelix_1_1ObjectHelix.html#aa51fd4ad9134ecd14fe1350610c5032f),
[PathScripts.PathThreadMilling.ObjectThreadMilling.initCircularHoleOperation()](../../dc/d24/classPathScripts_1_1PathThreadMilling_1_1ObjectThreadMilling.html#a20c274b9a7fc79cb4f3bbaa38cab72f5),
[InitGui.OpenSCADWorkbench.Initialize()](../../de/d96/classInitGui_1_1OpenSCADWorkbench.html#aab21a4ec8807422901c98791cee17889),
[InitGui.PathWorkbench.Initialize()](../../d8/d4b/classInitGui_1_1PathWorkbench.html#acb623fe81c56b0115f73c0ab5013b3d9),
[PathScripts.PathFeatureExtensions.initialize_properties()](../../d8/d23/namespacePathScripts_1_1PathFeatureExtensions.html#a121eeb646237cd559fcdc94f56c4fb17),
[PathScripts.PathAdaptive.PathAdaptive.initOperation()](../../da/dec/classPathScripts_1_1PathAdaptive_1_1PathAdaptive.html#a52f7d3346f0395dedf692676fe802ea0),
[PathScripts.PathAreaOp.ObjectOp.initOperation()](../../d5/d6f/classPathScripts_1_1PathAreaOp_1_1ObjectOp.html#a39f874da8d4c63c6def80b0c15664b6a),
[PathScripts.PathCircularHoleBase.ObjectOp.initOperation()](../../d8/d75/classPathScripts_1_1PathCircularHoleBase_1_1ObjectOp.html#a9b64bd9fbb6cbafcad5d2d32cd481be5),
[PathScripts.PathCustom.ObjectCustom.initOperation()](../../db/d1c/classPathScripts_1_1PathCustom_1_1ObjectCustom.html#a467ae55ab260ada612894fa9ee5ecd67),
[PathScripts.PathDeburr.ObjectDeburr.initOperation()](../../d4/dac/classPathScripts_1_1PathDeburr_1_1ObjectDeburr.html#a9ad2daf9eba1f88ac9888ca19b46cd78),
[PathScripts.PathEngrave.ObjectEngrave.initOperation()](../../df/d62/classPathScripts_1_1PathEngrave_1_1ObjectEngrave.html#ab474ccbbe8c5c7c5dff77f8d0801a065),
[PathScripts.PathProbe.ObjectProbing.initOperation()](../../dd/d22/classPathScripts_1_1PathProbe_1_1ObjectProbing.html#a62c23d560eef345aebf6d2924a8f8c80),
[PathScripts.PathVcarve.ObjectVcarve.initOperation()](../../dc/d23/classPathScripts_1_1PathVcarve_1_1ObjectVcarve.html#a83016543c044984db8f1069f267a2238),
[PathScripts.PathMillFace.ObjectFace.initPocketOp()](../../dd/d1f/classPathScripts_1_1PathMillFace_1_1ObjectFace.html#ae7fe759bf383505ee5cec709002949ac),
[PathScripts.PathPocket.ObjectPocket.initPocketOp()](../../df/d6c/classPathScripts_1_1PathPocket_1_1ObjectPocket.html#a966656e292e0304548f7c33950f2320b),
[PathScripts.PathPocketShape.ObjectPocket.initPocketOp()](../../d1/de1/classPathScripts_1_1PathPocketShape_1_1ObjectPocket.html#a4ec4826b9c281b47a076af6692a5266a),
[Sketcher::SketchObject.insertBSplineKnot()](../../d9/dad/classSketcher_1_1SketchObject.html#a48c6d4c74904307c87c4e8f65a9e89af),
[SpreadsheetGui::SheetTableView.insertColumns()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#ab91b636542c4367d2ce281d3ba5e8b58),
[SpreadsheetGui::SheetTableView.insertColumnsAfter()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a8cebcff7b6ae0e8fad3175aa4cf22946),
[SpreadsheetGui::SheetTableView.insertRows()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a29b12a5e738d689dd11833a7cf3b474e),
[SpreadsheetGui::SheetTableView.insertRowsAfter()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#ac591ed9234eab84fa028bce688dc3b56),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.draftlink.DraftLink.linkSetup()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#a5c45909d0f514cef0a03e00b6b1b3035),
[Gui::MainWindow.MainWindow()](../../d5/d2f/classGui_1_1MainWindow.html#a84c74efa977302744093e2027b0dd801),
[ArchAxis.makeAxis()](../../db/d0d/namespaceArchAxis.html#a70adcb27c65b4028ce6335ed7a491edc),
[ArchAxisSystem.makeAxisSystem()](../../d2/dbb/namespaceArchAxisSystem.html#a207b9fe32a32305312f015053743216d),
[ArchBuilding.makeBuilding()](../../d8/def/namespaceArchBuilding.html#a9ff5afad344ac96642ffeef4ce271afe),
[ArchBuildingPart.makeBuilding()](../../d7/dc5/namespaceArchBuildingPart.html#aa95c7be1481a8fe26a63615dcfe4da24),
[ArchFloor.makeFloor()](../../df/d16/namespaceArchFloor.html#a6c27d8dc5a92ad8079677e720e783191),
[ArchFrame.makeFrame()](../../d8/db6/namespaceArchFrame.html#a43a080855e00e52afc61334b48c48290),
[Sketcher::SketchAnalysis.makeMissingEquality()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ac1e651c6ade4f8c14ddf59404282b061),
[Sketcher::SketchAnalysis.makeMissingPointOnPointCoincident()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a58e2ef10380bca8c18c71f5362f9be91),
[Sketcher::SketchAnalysis.makeMissingVerticalHorizontal()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a8a7efd5e380f7f948189430ffbf19955),
[ArchPipe.makePipeConnector()](../../de/d7d/namespaceArchPipe.html#ad0045d91c1268a704a446908729aaa5f),
[ArchStairs.makeRailing()](../../dc/d06/namespaceArchStairs.html#a37c92f2db600fd86adc3ac386c6fa211),
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d),
[ArchRoof.makeRoof()](../../d4/d2a/namespaceArchRoof.html#ad19f0e53e9c0a79c7ac5d7cf86f73c65),
[MeshGui::ViewProviderMesh.markPartCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a6eb548accf81ef25b6aa376ac7fa53a8),
[Sketcher::SketchObject.modifyBSplineKnotMultiplicity()](../../d9/dad/classSketcher_1_1SketchObject.html#ae318b60c226c883e53725f9ebef29991),
[SketcherGui::ViewProviderSketch.mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[SketcherGui::TaskSketcherConstraints.on_listWidgetConstraints_itemChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#aa782aa7f44ac5962f91d0379dd4d6ce7),
[MeshGui::DlgEvaluateMeshImp.on_repairAllTogether_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a37ba0babe8914d5dce379504b9adf12e),
[MeshGui::DlgEvaluateMeshImp.on_repairDegeneratedButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ab3cdbd594788a57c256755a837018d2f),
[MeshGui::DlgEvaluateMeshImp.on_repairDuplicatedFacesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aede555d793810d6cfc2632ecf409e5fa),
[MeshGui::DlgEvaluateMeshImp.on_repairDuplicatedPointsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aef057c023433bea4e835ee2e61dd0d17),
[MeshGui::DlgEvaluateMeshImp.on_repairFoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a492d611b70e28517f204bf25bf76184e),
[MeshGui::DlgEvaluateMeshImp.on_repairIndicesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a3da19b67de1065f6efa4da4a159d9e97),
[MeshGui::DlgEvaluateMeshImp.on_repairNonmanifoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a515dab5e6ea530b164559c860252bfae),
[MeshGui::DlgEvaluateMeshImp.on_repairOrientationButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a69c2e5330dbce392a37614ce7e27d7fe),
[MeshGui::DlgEvaluateMeshImp.on_repairSelfIntersectionButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#acd921ad6e7470851387f97162ff6e288),
[draftobjects.pointarray.PointArray.onDocumentRestored()](../../db/d88/classdraftobjects_1_1pointarray_1_1PointArray.html#a3aa27ea57ab518b166e5bfd1ee79b570),
[PathScripts.PathArray.ObjectArray.onDocumentRestored()](../../d1/dbb/classPathScripts_1_1PathArray_1_1ObjectArray.html#a0934a67fce4c52f38f4197164f290473),
[PathScripts.PathJob.ObjectJob.onDocumentRestored()](../../df/d08/classPathScripts_1_1PathJob_1_1ObjectJob.html#a8442d229e5e7e5b359760f06fa9b4c69),
[PathScripts.PathOp.ObjectOp.onDocumentRestored()](../../d0/dec/classPathScripts_1_1PathOp_1_1ObjectOp.html#a5970ed2765c76cacdd3f026fd0e2858a),
[PathScripts.PathSetupSheet.SetupSheet.onDocumentRestored()](../../d9/dce/classPathScripts_1_1PathSetupSheet_1_1SetupSheet.html#a12a214da7cb6617dc0dc68ced54e42ba),
[PathScripts.PathToolBit.ToolBit.onDocumentRestored()](../../d3/d85/classPathScripts_1_1PathToolBit_1_1ToolBit.html#aa4e42f77024c9843305d5096b7b34d56),
[SpreadsheetGui::SheetView.onMsg()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a0a887941f1f60f16178c6e447d467d53),
[SketcherGui::DrawSketchHandlerCarbonCopy.onSelectionChanged()](../../d8/dcc/classSketcherGui_1_1DrawSketchHandlerCarbonCopy.html#a0abe4b682958afcce6e53de58d3225fa),
[SketcherGui::DrawSketchHandlerExternal.onSelectionChanged()](../../d5/d95/classSketcherGui_1_1DrawSketchHandlerExternal.html#aab1764f7bd2af3f2cf49a7131a443253),
[PartGui::TaskDlgAttacher.open()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#ab33412b8b5fead42d43dc988a02595e8),
[PartGui::FaceColors.open()](../../db/d9e/classPartGui_1_1FaceColors.html#a1244f504665b35ed2f88c0cd86219c96),
[PathScripts.PathAreaOp.ObjectOp.opOnDocumentRestored()](../../d5/d6f/classPathScripts_1_1PathAreaOp_1_1ObjectOp.html#a2ebcc5c8ad37d263278ad16339c01761),
[PathScripts.PathHelix.ObjectHelix.opOnDocumentRestored()](../../da/d14/classPathScripts_1_1PathHelix_1_1ObjectHelix.html#aa2af8868996cd7f6e167e15f1859aeb1),
[PathScripts.PathPocketBase.ObjectPocket.opOnDocumentRestored()](../../d8/dbc/classPathScripts_1_1PathPocketBase_1_1ObjectPocket.html#a9193192d3f298f5e52c98c015dc5cfc1),
[PathScripts.PathSurface.ObjectSurface.opPropertyDefinitions()](../../dd/d92/classPathScripts_1_1PathSurface_1_1ObjectSurface.html#ab45a7769125b5adc1950c16c70833875),
[PathScripts.PathWaterline.ObjectWaterline.opPropertyDefinitions()](../../db/dcc/classPathScripts_1_1PathWaterline_1_1ObjectWaterline.html#a712a47ac304d0d4249cfc0d61233ebb8),
[MeshGui::ViewProviderMesh.partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[StdCmdExpression.pasteExpressions()](../../d2/dae/classStdCmdExpression.html#abab137615ab802f7688ff0b623022b9f),
[TechDrawTools.TaskMoveView.TaskMoveView.pickFromPage()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a6315fd5a894efeaac64d8a3bf4c0420c),
[TechDrawTools.TaskShareView.TaskShareView.pickFromPage()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#afe2a46265f27152125c899865945c706),
[TechDrawTools.TaskMoveView.TaskMoveView.pickToPage()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a8603fbbe2bbd698e77d8313c70d67580),
[TechDrawTools.TaskShareView.TaskShareView.pickToPage()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#acedbfda483a1d58ac4745eeb34dac5b1),
[TechDrawTools.TaskMoveView.TaskMoveView.pickView()](../../da/d16/classTechDrawTools_1_1TaskMoveView_1_1TaskMoveView.html#a86e4e71d2ef6da50142d097b77c08731),
[TechDrawTools.TaskShareView.TaskShareView.pickView()](../../d0/d64/classTechDrawTools_1_1TaskShareView_1_1TaskShareView.html#afe19c1a1a0c84244e474e3b8faadf80f),
[SketcherGui::DrawSketchHandlerBSpline.pressButton()](../../d7/d7f/classSketcherGui_1_1DrawSketchHandlerBSpline.html#aa7b3de965a523113d29f73f4b71fe6c8),
[Gui::PropertyEditor::PropertyEnumItem.PropertyEnumItem()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#aec0bcc67c964940486d2ff02d6def4c1),
[Gui::PropertyEditor::PropertyItem.propertyName()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#afadf30560bb04db7665b7b6fbeb4086b),
[Gui::PropertyEditor::PropertyPlacementItem.PropertyPlacementItem()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#afc98b9316f8b374efa39cc368dd4afde),
[Gui::PropertyEditor::PropertyRotationItem.PropertyRotationItem()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a46fee6e741388a98e84af107a83af6be),
[ArchWindow.recolorize()](../../d3/db7/namespaceArchWindow.html#a8a46c0e437e0f7099531f4bf88290aed),
[DrawSketchHandlerCoincident.releaseButton()](../../d1/da0/classDrawSketchHandlerCoincident.html#a0aa30cef84692d6048db1607abb8b77f),
[DrawSketchHandlerBSplineInsertKnot.releaseButton()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#ad1bd5e637ff894fb66b09fcf914bd49b),
[DrawSketchHandlerCopy.releaseButton()](../../d0/d19/classDrawSketchHandlerCopy.html#ae8955bcf2ad603ca908dbde0ca52042a),
[DrawSketchHandlerRectangularArray.releaseButton()](../../db/da6/classDrawSketchHandlerRectangularArray.html#acad62cdf5d8d411d55beff22a12fac28),
[SketcherGui::DrawSketchHandlerArc.releaseButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#ab283932a602b4b135259d8ec565cbe1a),
[SketcherGui::DrawSketchHandler3PointArc.releaseButton()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#ad9123e0df6dfcbca72fb0a45e63bb822),
[SketcherGui::DrawSketchHandlerArcOfEllipse.releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
[SketcherGui::DrawSketchHandlerCircle.releaseButton()](../../db/daa/classSketcherGui_1_1DrawSketchHandlerCircle.html#aac71ee5f645be6cc4b0ac8cb49777b67),
[SketcherGui::DrawSketchHandler3PointCircle.releaseButton()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a3393a6d51aed0b745e44e60f55e4c96a),
[SketcherGui::DrawSketchHandlerExtend.releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerFillet.releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerLine.releaseButton()](../../dd/d65/classSketcherGui_1_1DrawSketchHandlerLine.html#a9ee080f22c2c3bf2f6e826f4cc36f91a),
[SketcherGui::DrawSketchHandlerLineSet.releaseButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a040aa2a8cc28c52db550115a16ef693c),
[SketcherGui::DrawSketchHandlerPoint.releaseButton()](../../df/da1/classSketcherGui_1_1DrawSketchHandlerPoint.html#a733f6bcea854c88e77f73e0a1b377f53),
[SketcherGui::DrawSketchHandlerRegularPolygon.releaseButton()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a676a473ddbfd8fd7f2e214ffc43352b5),
[SketcherGui::DrawSketchHandlerBox.releaseButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a1ee8ff08af23b1ad1d9fd48170889315),
[SketcherGui::DrawSketchHandlerOblong.releaseButton()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a8e2b792d2ce80795c2808e6276bdd6dc),
[SketcherGui::DrawSketchHandlerSlot.releaseButton()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#aa93e01a33ed89216e53c3c8886b21a35),
[SketcherGui::DrawSketchHandlerSplitting.releaseButton()](../../d1/d6f/classSketcherGui_1_1DrawSketchHandlerSplitting.html#a0766956ef48057437eca84c83e1b3521),
[SketcherGui::DrawSketchHandlerTrimming.releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[SketcherGui::DrawSketchHandlerArcOfHyperbola.releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3),
[SketcherGui::DrawSketchHandlerArcOfParabola.releaseButton()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a17a69b223beded8cad2a7319ef4cffe6),
[SpreadsheetGui::SheetTableView.removeColumns()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#aa41dca227d456e2ffd972fa88c4ff6d2),
[SpreadsheetGui::SheetTableView.removeRows()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a7599cef797de900e763493224292cdea),
[ArchSpace.removeSpaceBoundaries()](../../d8/d6a/namespaceArchSpace.html#aca020b8800ac48fabbf4fce2a0f16cee),
[TechDrawGui::MDIViewPage.saveDXF()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a2bfe93567b8e55b5bcda419d70b57a8e),
[MeshGui::ViewProviderMesh.segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.set_annotation_properties()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a3a0c725c5c8ace91b97928acd80a21ed),
[draftobjects.array.Array.set_circular_properties()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#a10eeca80d80f6c9455e7c1718ab223b6),
[draftobjects.array.Array.set_general_properties()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#a204bf7f6ac75e785206a1c8eb3ba91ac),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.set_graphics_properties()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#a83b7233f0d8d7a9f92be6d815d6ded03),
[draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation.set_graphics_properties()](../../d2/d24/classdraftviewproviders_1_1view__draft__annotation_1_1ViewProviderDraftAnnotation.html#a4f7e938e74b5924f424ac6ba8e41f375),
[draftviewproviders.view_label.ViewProviderLabel.set_graphics_properties()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aea52bc96013cc0acff362393fc454b79),
[draftobjects.label.Label.set_label_properties()](../../d8/db6/classdraftobjects_1_1label_1_1Label.html#ab9528ac2e29f21832ec6a257e9ab78ea),
[draftobjects.label.Label.set_leader_properties()](../../d8/db6/classdraftobjects_1_1label_1_1Label.html#a9a65257907a74c876bbaa4df3ce66f9e),
[draftobjects.array.Array.set_link_properties()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#af92825687023976ca52c5677e5a460c5),
[draftobjects.array.Array.set_ortho_properties()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#a8e99c39005dc8fac36f1a83da16c28f4),
[draftviewproviders.view_layer.ViewProviderLayer.set_override_options()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a184182fc281fa76c7a71f93aec24a0f1),
[draftobjects.array.Array.set_polar_circular_properties()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#a687bd3974d1742f780ff4017e62b80a8),
[draftobjects.array.Array.set_polar_properties()](../../d7/d7e/classdraftobjects_1_1array_1_1Array.html#afc599755231714c59a8c2e706c1be3c8),
[draftobjects.dimension.DimensionBase.set_properties()](../../d7/d7d/classdraftobjects_1_1dimension_1_1DimensionBase.html#a78980d08ebae85714b695743427b678b),
[draftobjects.dimension.LinearDimension.set_properties()](../../dd/d6f/classdraftobjects_1_1dimension_1_1LinearDimension.html#a81a0afaaa4b6e64032707fa5220a9fd5),
[draftobjects.dimension.AngularDimension.set_properties()](../../d9/df3/classdraftobjects_1_1dimension_1_1AngularDimension.html#a196c0be52f79ebe48382a63cc9d1e96a),
[draftobjects.layer.Layer.set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
[draftobjects.pointarray.PointArray.set_properties()](../../db/d88/classdraftobjects_1_1pointarray_1_1PointArray.html#ad13a13f6dae4301b88a2d52476aaa394),
[draftobjects.text.Text.set_properties()](../../d6/daa/classdraftobjects_1_1text_1_1Text.html#a048d67e0f8e3c77c017a8e116fc790ad),
[draftviewproviders.view_text.ViewProviderText.set_properties()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#ab5eb2c696c03083e344f4ed2b4a637eb),
[draftobjects.label.Label.set_target_properties()](../../d8/db6/classdraftobjects_1_1label_1_1Label.html#a262b1948de9887c44a4806b797acc371),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.set_text_properties()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#aa11f4704b7e2a31595db316737964914),
[draftviewproviders.view_label.ViewProviderLabel.set_text_properties()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aacd24c689a19284451eb5273f881d848),
[draftviewproviders.view_dimension.ViewProviderDimensionBase.set_units_properties()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#ad57f1eb425a47842f30b0ec6565b67d4),
[draftviewproviders.view_layer.ViewProviderLayer.set_visual_properties()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#ae2279054f2e1c8da7d1913698839fdf6),
[SpreadsheetGui::WorkbenchHelper.setBackgroundColor()](../../df/d59/classSpreadsheetGui_1_1WorkbenchHelper.html#a84a6cd19ea31a176ad4172e865a59438),
[draftviewproviders.view_base.ViewProviderDraft.setEdit()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#adebff004d86674246b09cb8adf7eb658),
[SpreadsheetGui::WorkbenchHelper.setForegroundColor()](../../df/d59/classSpreadsheetGui_1_1WorkbenchHelper.html#a0c4b0d85871687dc806b5b8f55df043e),
[ArchMaterial.MultiMaterialDelegate.setModelData()](../../dd/dba/classArchMaterial_1_1MultiMaterialDelegate.html#aa36ee69be80adc06480436ec7883804e),
[ArchProfile.Arch_Profile.setPreset()](../../d7/d48/classArchProfile_1_1Arch__Profile.html#ae128806d02925f8e8a82559c8dee3f8f),
[ArchBuildingPart.BuildingPart.setProperties()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a01e29cb1d764fda7df9055fe009dbf35),
[ArchComponent.Component.setProperties()](../../de/d87/classArchComponent_1_1Component.html#a83f183119924946069f3b00947ec9793),
[ArchCurtainWall.CurtainWall.setProperties()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a1c7351250cd02e8b790e5ed84ebe7553),
[ArchGrid.ArchGrid.setProperties()](../../d7/d52/classArchGrid_1_1ArchGrid.html#a229519e55602df9a0561e406eccbcd43),
[ArchPanel.PanelView.setProperties()](../../dd/da0/classArchPanel_1_1PanelView.html#a4d88fc678e1545b9d6758274b79ff6de),
[ArchPanel.PanelCut.setProperties()](../../d6/dbd/classArchPanel_1_1PanelCut.html#ab647ec1cd91fa4c50475f46c709f2283),
[ArchPanel.PanelSheet.setProperties()](../../dc/d22/classArchPanel_1_1PanelSheet.html#a6f1bddeabda97604ae78d870456ce30c),
[ArchReference.ArchReference.setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5),
[ArchTruss.Truss.setProperties()](../../d9/d6f/classArchTruss_1_1Truss.html#a90f32bb2105867d75078e021f1ba771c),
[draftobjects.hatch.Hatch.setProperties()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a48c378dffc98e6b9f7ecac53074128da),
[draftobjects.shape2dview.Shape2DView.setProperties()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#aa3d3c084e10c9697c432ccf1ddee8928),
[ArchBuildingPart.ViewProviderBuildingPart.setProperties()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a16972577fb2b2bebf116c298b7f0f9da),
[ArchComponent.ViewProviderComponent.setProperties()](../../dd/d1b/classArchComponent_1_1ViewProviderComponent.html#abbd3e374ae515673bada8f848fbc98af),
[ArchPanel.ViewProviderPanelCut.setProperties()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a728ad185d4b895a95966a464948c1027),
[ArchPanel.ViewProviderPanelSheet.setProperties()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a36bba4eebef09728a582d6a4b3b71150),
[ArchReference.ViewProviderArchReference.setProperties()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a7f9d1dadc048dd8e345d54d9b06629c9),
[ArchStructure.StructureTaskPanel.setToolFromSelection()](../../df/d40/classArchStructure_1_1StructureTaskPanel.html#aaf6f1a737e2e9b8b1c685ffe4b88c489),
[PathScripts.PathEngrave.ObjectEngrave.setupAdditionalProperties()](../../df/d62/classPathScripts_1_1PathEngrave_1_1ObjectEngrave.html#a59e036d735da0b5cc76f774cbd0aeffd),
[PathScripts.PathVcarve.ObjectVcarve.setupAdditionalProperties()](../../dc/d23/classPathScripts_1_1PathVcarve_1_1ObjectVcarve.html#a3b225d1c7a18d6a72b1a3566426ca8d3),
[PathScripts.PathJob.ObjectJob.setupBaseModel()](../../df/d08/classPathScripts_1_1PathJob_1_1ObjectJob.html#aff8172ca061015629c75fdfc445ce84d),
[PathScripts.PathJob.ObjectJob.setupSetupSheet()](../../df/d08/classPathScripts_1_1PathJob_1_1ObjectJob.html#a55df2d77e0b0bfe6160a1717c1b0efa1),
[PathScripts.PathStock.SetupStockObject()](../../d4/d2c/namespacePathScripts_1_1PathStock.html#af826e373b7dc08bfe3466d5cee3dbf95),
[PathScripts.PathJob.ObjectJob.setupToolTable()](../../df/d08/classPathScripts_1_1PathJob_1_1ObjectJob.html#af071c99b00f3b38721ae2f102838955e),
[CmdSketcherConstrainTangent.substituteConstraintCombinations()](../../d8/d80/classCmdSketcherConstrainTangent.html#a2d02137f9850624259ea7eb10327a17b),
[CmdSketcherConstrainCoincident.substituteConstraintCombinations()](../../d0/d76/classCmdSketcherConstrainCoincident.html#a942503af6ed7fec83fe0b519822ab3cb),
[SketcherGui::ConstraintView.swapNamedOfSelectedItems()](../../df/d7b/classSketcherGui_1_1ConstraintView.html#a2ef795bfde4fc5d342d3bba939346c86),
[MeshGui::MeshSplit.trimMesh()](../../d9/de5/classMeshGui_1_1MeshSplit.html#a3c2f778060142cb84e20ff69540da0a3),
[MeshGui::ViewProviderMesh.trimMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a99db0ab49ba22437ef202c633d752b52),
[TechDrawGui::TaskRichAnno.updateAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#adc9c72650392178995bfd8adf6344831),
[TechDrawGui::TaskDetail.updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[TechDrawGui::TaskHatch.updateHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a885b8fcb16ca312a825e37d5f4ee11b4),
[TechDrawGui::TaskLeaderLine.updateLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0797a29d0a4ef849d5643c1ed982acb2),
[TechDrawGui::TaskSectionView.updateSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ade2a27d8889164e2b81d166289744e35),
[Gui::ViewProviderOrigin.ViewProviderOrigin()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a6e739ce6a596276b5e02d1076cc93282),
[Gui::ViewProviderOriginFeature.ViewProviderOriginFeature()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a658d2656863d9da8c92d9f1d01de056f),
[SandboxGui::Workbench.Workbench()](../../d2/db3/classSandboxGui_1_1Workbench.html#a052a62fb11c36380d04283bff6d47582),
[ArchBuildingPart.ViewProviderBuildingPart.writeCamera()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a3b1b1c7b54a861a46eab90dd1fdbc49c),
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.writeCamera()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#abd46fb66b0e0bd5d23dc238cf427f3a5),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.writeState()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#aa67186706faef974f14da09b45a94ca0).

## ◆ Qtranslate

draftutils.translate.Qtranslate = QtCore.QCoreApplication.translate  
---  
  
Referenced by
[draftutils.translate.translate()](../../de/d75/group__draftutils.html#ga401299ca851f4d4ee86937e756dc21d4).

## ◆ removeHidden

def draftutils.gui_utils.removeHidden =
[remove_hidden](../../de/d75/group__draftutils.html#gaba028dfc9b80647b511e41c0d233106f)  
---  
  
## ◆ setParam

def draftutils.utils.setParam =
[set_param](../../de/d75/group__draftutils.html#ga01641daa7576c696849ca6fcfc3fb350)  
---  
  
## ◆ stringencodecoin

def draftutils.utils.stringencodecoin =
[string_encode_coin](../../de/d75/group__draftutils.html#ga6671a36b7e113481feb4f990415d694c)  
---  
  
## ◆ svgpatterns

def draftutils.utils.svgpatterns =
[svg_patterns](../../de/d75/group__draftutils.html#gad668ee3ba955aea7dcb8fd72a6e148b7)  
---  
  
## ◆ todo

draftutils.todo.todo =
[ToDo](../../da/da9/classdraftutils_1_1todo_1_1ToDo.html)  
---  
  
Referenced by
[MeshCore::MeshRemoveNeedles.Fixup()](../../d1/d17/classMeshCore_1_1MeshRemoveNeedles.html#abac3aefa5c88447d72674b078298e6e0),
[MeshCore::MeshFixCaps.Fixup()](../../dd/ddb/classMeshCore_1_1MeshFixCaps.html#ad50f1421a63196cbd099763be5ce1863),
and
[MeshCore::MeshTopoAlgorithm.OptimizeTopology()](../../d6/d22/classMeshCore_1_1MeshTopoAlgorithm.html#ad1e8f841ba8e056086eb7cb29bb4bc48).

## ◆ typecheck

def draftutils.utils.typecheck =
[type_check](../../de/d75/group__draftutils.html#ga9a7119e1e423a5bdf6a4505663eaf363)  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

