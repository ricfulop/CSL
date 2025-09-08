---
url: https://freecad.github.io/SourceDoc/d2/d57/group__draftfunctions.html
scraped_at: 2025-09-08T14:51:58.991137
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Namespaces | Functions | Variables

draftfunctions

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Draft](../../d1/d35/group__DRAFT.html)

Modules with functions for use with scripted objects and GuiCommands. More...

##  Namespaces  
  
---  
namespace | [array](../../d7/df9/namespacearray.html)  
| Provides functions to create non-parametric arrayed copies.  
  
namespace | [cut](../../d4/daf/namespacecut.html)  
| Provides functions to create a cut object from two objects.  
  
namespace | [downgrade](../../d0/df6/namespacedowngrade.html)  
| Provides functions to downgrade objects by different methods.  
  
namespace | [draftify](../../d8/dfe/namespacedraftify.html)  
| Provides functions to transform sketches into
[Draft](../../d4/d1a/namespaceDraft.html) objects.  
  
namespace | [dxf](../../d4/dab/namespacedxf.html)  
| Provides functions to return the DXF representation of shapes.  
  
namespace | [extrude](../../df/df3/namespaceextrude.html)  
| Provides functions to create an extrusion object from a profile.  
  
namespace | [fuse](../../d3/d37/namespacefuse.html)  
| Provides functions to create a fusion of two shapes.  
  
namespace | [heal](../../de/df9/namespaceheal.html)  
| Provides functions to repair certain objects from old versions.  
  
namespace | [join](../../d7/dd2/namespacejoin.html)  
| Provides functions to join wires together into a single wire.  
  
namespace | [mirror](../../d7/d5b/namespacemirror.html)  
| Provides functions to produce a mirrored object.  
  
namespace | [move](../../db/d10/namespacemove.html)  
| Provides functions to move objects from one position to another.  
  
namespace | [offset](../../d8/da3/namespaceoffset.html)  
| Provides functions to create offsets of different shapes.  
  
namespace | [rotate](../../d7/d25/namespacerotate.html)  
| Provides functions to rotate shapes around a center and axis.  
  
namespace | [scale](../../da/dc3/namespacescale.html)  
| Provides functions to scale shapes.  
  
namespace | [split](../../dc/dfb/namespacesplit.html)  
| Provides functions to split wires into separate wire objects.  
  
namespace | [svg](../../d9/dbe/namespacesvg.html)  
| Provides functions to return the SVG representation of shapes.  
  
namespace | [svgshapes](../../da/d8f/namespacesvgshapes.html)  
| Provides functions to return the SVG representation of some shapes.  
  
namespace | [svgtext](../../d3/d19/namespacesvgtext.html)  
| Provides functions to return the SVG representation of text elements.  
  
  
##  Functions  
  
---  
def | [draftfunctions.array.array](../../d2/d57/group__draftfunctions.html#gadf79960ae21167271a07cc16e0a58027) (objectslist, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None)  
def | [draftfunctions.move.copy_moved_edge](../../d2/d57/group__draftfunctions.html#ga3922e2cc6ed7e9cb1c93f6226922e73f) ([object](../../dc/dd8/classobject.html), edge_index, vector)  
def | [draftfunctions.move.copy_moved_edges](../../d2/d57/group__draftfunctions.html#ga73be57b46917993128fa3784697024d3) (arguments)  
def | [draftfunctions.rotate.copy_rotated_edge](../../d2/d57/group__draftfunctions.html#gac94fa90639a8f9b3018079697a984991) ([object](../../dc/dd8/classobject.html), edge_index, angle, center, axis)  
def | [draftfunctions.rotate.copy_rotated_edges](../../d2/d57/group__draftfunctions.html#gacd1c2653ca92dbad2c87bc0758f5ca28) (arguments)  
def | [draftfunctions.scale.copy_scaled_edge](../../d2/d57/group__draftfunctions.html#gacfa4a432df41da7183fa4d67082afbe4) (obj, edge_index, [scale](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10), center)  
def | [draftfunctions.scale.copy_scaled_edges](../../d2/d57/group__draftfunctions.html#gac59d9b5d86c38c42b59625f7feef2a68) (arguments)  
def | [draftfunctions.cut.cut](../../d2/d57/group__draftfunctions.html#ga98c2a2e7e72a313654650b5e241e1f26) (object1, object2)  
def | [draftfunctions.downgrade.downgrade](../../d2/d57/group__draftfunctions.html#ga5204afb7992c5e5a5e4971a5e21051f7) (objects, delete=False, force=None)  
def | [draftfunctions.draftify.draftify](../../d2/d57/group__draftfunctions.html#ga42fd321bf362162d928a99207a127d4e) (objectslist, makeblock=False, delete=True)  
def | [draftfunctions.draftify.draftify_shape](../../d2/d57/group__draftfunctions.html#ga4abdb8a69913c60c9ec19c300e056acc) (shape)  
def | [draftfunctions.extrude.extrude](../../d2/d57/group__draftfunctions.html#ga896df274177d62887a429e42964095e3) (obj, vector, solid=False)  
def | [draftfunctions.svg.format_point](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a) (coords, action='L')  
def | [draftfunctions.fuse.fuse](../../d2/d57/group__draftfunctions.html#gacd63813f0fd809809117c5b7c6d3eab1) (object1, object2)  
def | [draftfunctions.svg.get_arrow](../../d2/d57/group__draftfunctions.html#gad0c5f4b0f8bd030fe07ce7888b4de3c6) (obj, arrowtype, point, arrowsize, color, linewidth, angle=0)  
def | [draftfunctions.svgshapes.get_circle](../../d2/d57/group__draftfunctions.html#ga863618a060532a94639ba3cda58ef49d) (plane, fill, stroke, linewidth, lstyle, edge)  
def | [draftfunctions.svgshapes.get_discretized](../../d2/d57/group__draftfunctions.html#gad1f8c64191307ca88d266845f45e7290) (edge, plane)  
def | [draftfunctions.dxf.get_dxf](../../d2/d57/group__draftfunctions.html#ga90ba94edeb5cbf46870b8d1b10c2fa81) (obj, direction=None)  
def | [draftfunctions.svgshapes.get_ellipse](../../d2/d57/group__draftfunctions.html#ga6b46140c1f08ae819c29290fe9166ed3) (plane, fill, stroke, linewidth, lstyle, edge)  
def | [draftfunctions.svg.get_line_style](../../d2/d57/group__draftfunctions.html#ga2dcc2f8d9735fb301723edb4bb281337) (line_style, scale)  
def | [draftfunctions.svg.get_overshoot](../../d2/d57/group__draftfunctions.html#gae21f92b52a2afee8c5292d737556e48f) (point, shootsize, color, linewidth, angle=0)  
def | [draftfunctions.svgshapes.get_path](../../d2/d57/group__draftfunctions.html#gab86383da15f203f9678b68148e7d5e84) (obj, plane, fill, pathdata, stroke, linewidth, lstyle, fill_opacity=None, edges=[], wires=[], pathname=None)  
def | [draftfunctions.svg.get_pattern](../../d2/d57/group__draftfunctions.html#ga2152e008a9d7effdee6f2d6e15876ecc) (pat)  
def | [draftfunctions.svg.get_print_color](../../d2/d57/group__draftfunctions.html#ga6e2f37e1614888b89c9af5a451de7c71) (obj)  
def | [draftfunctions.svgshapes.get_proj](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e) (vec, plane=None)  
def | [draftfunctions.svg.get_svg](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5) (obj, scale=1, linewidth=0.35, fontsize=12, fillstyle="shape color", direction=None, linestyle=None, color=None, linespacing=None, techdraw=False, rotation=0, fillspaces=False, override=True)  
def | [draftfunctions.svgtext.get_text](../../d2/d57/group__draftfunctions.html#ga3785091650337fe5169c6181d1cc71d0) (plane, techdraw, tcolor, fontsize, fontname, angle, base, text, linespacing=0.5, align="center", flip=True)  
def | [draftfunctions.svg.getArrow](../../d2/d57/group__draftfunctions.html#ga1d49353fdfcd9f576d8155e7e7c80b4b) (obj, arrowtype, point, arrowsize, color, linewidth, angle=0)  
def | [draftfunctions.svgshapes.getCircle](../../d2/d57/group__draftfunctions.html#ga72cb5605a599c3e687ab08d86b2501cc) (plane, fill, stroke, linewidth, lstyle, edge)  
def | [draftfunctions.svgshapes.getDiscretized](../../d2/d57/group__draftfunctions.html#ga68258a215202f02c01dc3b0f47791ebf) (edge, plane)  
def | [draftfunctions.dxf.getDXF](../../d2/d57/group__draftfunctions.html#ga627306a5ef4c17e991ae65c7a98a6898) (obj, direction=None)  
def | [draftfunctions.svgshapes.getEllipse](../../d2/d57/group__draftfunctions.html#gab22bd7595bc834d3bcd09f85961163f3) (plane, fill, stroke, linewidth, lstyle, edge)  
def | [draftfunctions.svg.getLineStyle](../../d2/d57/group__draftfunctions.html#gaaa57d4eb618d7d775ecae628c1bbeffc) (linestyle, scale)  
def | [draftfunctions.svg.getOvershoot](../../d2/d57/group__draftfunctions.html#ga7be23f0a96f4507a8a25d60143ff1224) (point, shootsize, color, linewidth, angle=0)  
def | [draftfunctions.svgshapes.getPath](../../d2/d57/group__draftfunctions.html#ga36789b0e79a1612c2420c50806e918b0) (obj, plane, fill, pathdata, stroke, linewidth, lstyle, fill_opacity, edges=[], wires=[], pathname=None)  
def | [draftfunctions.svg.getPattern](../../d2/d57/group__draftfunctions.html#ga9814766327c319b343e4e1e6064b90d5) (pat)  
def | [draftfunctions.svgshapes.getProj](../../d2/d57/group__draftfunctions.html#ga8101bc4fc8fa7eba53b0312546178d6d) (vec, plane=None)  
def | [draftfunctions.svg.getSVG](../../d2/d57/group__draftfunctions.html#gafc5b11e972efd1ebb72e945dc36e8d6a) (obj, scale=1, linewidth=0.35, fontsize=12, fillstyle="shape color", direction=None, linestyle=None, color=None, linespacing=None, techdraw=False, rotation=0, fillSpaces=False, override=True)  
def | [draftfunctions.svgtext.getText](../../d2/d57/group__draftfunctions.html#ga898571506aacbbc685cd35b2a45658d7) (plane, techdraw, tcolor, fontsize, fontname, angle, base, text, linespacing=0.5, align="center", flip=True)  
def | [draftfunctions.heal.heal](../../d2/d57/group__draftfunctions.html#gaf5fdfa7422ea2d49b9097b6a1a52d5fb) (objlist=None, delete=True, reparent=True)  
def | [draftfunctions.join.join_two_wires](../../d2/d57/group__draftfunctions.html#ga8b7573fa746b69be82d73768bb04a557) (wire1, wire2)  
def | [draftfunctions.join.join_wires](../../d2/d57/group__draftfunctions.html#ga5354f8b322314e22e3f93f7a54371858) (wires, joinAttempts=0)  
def | [draftfunctions.mirror.mirror](../../d2/d57/group__draftfunctions.html#gaac82986b1321dcbfc93ed023e26d37c2) (objlist, p1, p2)  
def | [draftfunctions.move.move](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f) (objectslist, vector, copy=False)  
def | [draftfunctions.move.move_edge](../../d2/d57/group__draftfunctions.html#gab30cec2f612e2ef4ffcbb924311a99a0) ([object](../../dc/dd8/classobject.html), edge_index, vector)  
def | [draftfunctions.move.move_vertex](../../d2/d57/group__draftfunctions.html#gabf9889375ebf33577848f5fa2c2f4552) ([object](../../dc/dd8/classobject.html), vertex_index, vector)  
def | [draftfunctions.offset.offset](../../d2/d57/group__draftfunctions.html#ga15bf04dc2feebf4fe453ff6b9a3a7492) (obj, delta, copy=False, bind=False, sym=False, occ=False)  
def | [draftfunctions.array.polarArray](../../d2/d57/group__draftfunctions.html#ga4857d7b09a812f72c38762d140ae1625) (objectslist, center, angle, num)  
def | [draftfunctions.array.rectArray](../../d2/d57/group__draftfunctions.html#gae0643813f550064418f49422d4d91a12) (objectslist, xvector, yvector, xnum, ynum)  
def | [draftfunctions.array.rectArray2](../../d2/d57/group__draftfunctions.html#ga29d7d4b92cebde4989632a2adf167f0b) (objectslist, xvector, yvector, zvector, xnum, ynum, znum)  
def | [draftfunctions.rotate.rotate](../../d2/d57/group__draftfunctions.html#ga0429017dad7951a61c04221ce72b32fb) (objectslist, angle, center=App.Vector(0, 0, 0), axis=App.Vector(0, 0, 1), copy=False)  
def | [draftfunctions.rotate.rotate_edge](../../d2/d57/group__draftfunctions.html#gaf66ee29eea1d43bb3bc9a72a39306580) ([object](../../dc/dd8/classobject.html), edge_index, angle, center, axis)  
def | [draftfunctions.rotate.rotate_vector_from_center](../../d2/d57/group__draftfunctions.html#ga183986f7cd09d522dd82a38b522c2353) (vector, angle, axis, center)  
def | [draftfunctions.rotate.rotate_vertex](../../d2/d57/group__draftfunctions.html#gaf6c1a6aebf12f4e79a5766e3accfc9a0) ([object](../../dc/dd8/classobject.html), vertex_index, angle, center, axis)  
def | [draftfunctions.scale.scale](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10) (objectslist, scale=App.Vector(1, 1, 1), center=App.Vector(0, 0, 0), copy=False)  
def | [draftfunctions.scale.scale_edge](../../d2/d57/group__draftfunctions.html#gaf6f6d2fc2c6268c37e18418710dda5c5) (obj, edge_index, [scale](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10), center)  
def | [draftfunctions.scale.scale_vector_from_center](../../d2/d57/group__draftfunctions.html#ga2cd4c3d5877a9514b471589548d292a7) (vector, [scale](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10), center)  
def | [draftfunctions.scale.scale_vertex](../../d2/d57/group__draftfunctions.html#ga5385cccd74ea9fb4238c0ca17999b18c) (obj, vertex_index, [scale](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10), center)  
def | [draftfunctions.split.split](../../d2/d57/group__draftfunctions.html#ga23d2785b69d3a2f6b9347d0e95515447) (wire, newPoint, edgeIndex)  
def | [draftfunctions.split.split_closed_wire](../../d2/d57/group__draftfunctions.html#ga23c12c1c523cdb3f7209e0db692f373a) (wire, edgeIndex)  
def | [draftfunctions.split.split_open_wire](../../d2/d57/group__draftfunctions.html#gafc191032e1c328346d1c042ed97c8002) (wire, newPoint, edgeIndex)  
def | [draftfunctions.upgrade.upgrade](../../d2/d57/group__draftfunctions.html#ga5f09a8d57bed7988f62a3e3aa27705e4) (objects, delete=False, force=None)  
  
##  Variables  
  
---  
def | [draftfunctions.move.copyMovedEdges](../../d2/d57/group__draftfunctions.html#ga056cd438a305a602a4b6c38a4c36ada3) = [copy_moved_edges](../../d2/d57/group__draftfunctions.html#ga73be57b46917993128fa3784697024d3)  
def | [draftfunctions.rotate.copyRotatedEdges](../../d2/d57/group__draftfunctions.html#gaaf4ed2048dce5828f2299c9965db917f) = [copy_rotated_edges](../../d2/d57/group__draftfunctions.html#gacd1c2653ca92dbad2c87bc0758f5ca28)  
def | [draftfunctions.scale.copyScaledEdge](../../d2/d57/group__draftfunctions.html#gab5804824e101f21c36f1262006edb2dd) = [copy_scaled_edge](../../d2/d57/group__draftfunctions.html#gacfa4a432df41da7183fa4d67082afbe4)  
def | [draftfunctions.scale.copyScaledEdges](../../d2/d57/group__draftfunctions.html#gaef2ed3d411461e9c86e822dd82aae367) = [copy_scaled_edges](../../d2/d57/group__draftfunctions.html#gac59d9b5d86c38c42b59625f7feef2a68)  
|
[draftfunctions.draftify.DraftGeomUtils](../../d2/d57/group__draftfunctions.html#gacb9e1fc20ef39b4f8825bbdfb141ecc3)
= lz.LazyLoader("DraftGeomUtils", globals(), "DraftGeomUtils")  
def | [draftfunctions.join.joinTwoWires](../../d2/d57/group__draftfunctions.html#ga10ccd4d9f9b0556fc69fedc7d2cbf63f) = [join_two_wires](../../d2/d57/group__draftfunctions.html#ga8b7573fa746b69be82d73768bb04a557)  
def | [draftfunctions.join.joinWires](../../d2/d57/group__draftfunctions.html#ga7934e895e1ada748edbb80006a3b66ce) = [join_wires](../../d2/d57/group__draftfunctions.html#ga5354f8b322314e22e3f93f7a54371858)  
def | [draftfunctions.move.moveEdge](../../d2/d57/group__draftfunctions.html#gad1ff86016303d3e55c16b9b93b7d2d1f) = [move_edge](../../d2/d57/group__draftfunctions.html#gab30cec2f612e2ef4ffcbb924311a99a0)  
def | [draftfunctions.move.moveVertex](../../d2/d57/group__draftfunctions.html#ga6344bf6a3359333cf20fac7726b718c4) = [move_vertex](../../d2/d57/group__draftfunctions.html#gabf9889375ebf33577848f5fa2c2f4552)  
|
[draftfunctions.draftify.Part](../../d2/d57/group__draftfunctions.html#gae7045498a54b1a9ac35a0cf9f2b71533)
= lz.LazyLoader("Part", globals(), "Part")  
def | [draftfunctions.rotate.rotateEdge](../../d2/d57/group__draftfunctions.html#gad30d2eff6c7172b4eec9afad72f3f645) = [rotate_edge](../../d2/d57/group__draftfunctions.html#gaf66ee29eea1d43bb3bc9a72a39306580)  
def | [draftfunctions.rotate.rotateVectorFromCenter](../../d2/d57/group__draftfunctions.html#gad45a0c4570c3c5d3c2609327a4325b38) = [rotate_vector_from_center](../../d2/d57/group__draftfunctions.html#ga183986f7cd09d522dd82a38b522c2353)  
def | [draftfunctions.rotate.rotateVertex](../../d2/d57/group__draftfunctions.html#ga5a7795065a46af4f48ba7542ae93b16e) = [rotate_vertex](../../d2/d57/group__draftfunctions.html#gaf6c1a6aebf12f4e79a5766e3accfc9a0)  
def | [draftfunctions.scale.scaleEdge](../../d2/d57/group__draftfunctions.html#gaaef53afc6e49cd532c6f330bb3e2be3e) = [scale_edge](../../d2/d57/group__draftfunctions.html#gaf6f6d2fc2c6268c37e18418710dda5c5)  
def | [draftfunctions.scale.scaleVectorFromCenter](../../d2/d57/group__draftfunctions.html#gae02f52fb5b4265f0cf592a3d9c3937ca) = [scale_vector_from_center](../../d2/d57/group__draftfunctions.html#ga2cd4c3d5877a9514b471589548d292a7)  
def | [draftfunctions.scale.scaleVertex](../../d2/d57/group__draftfunctions.html#ga60d2b70bcd137308fc3b4f1c941a171e) = [scale_vertex](../../d2/d57/group__draftfunctions.html#ga5385cccd74ea9fb4238c0ca17999b18c)  
def | [draftfunctions.split.splitClosedWire](../../d2/d57/group__draftfunctions.html#ga618d6b4066fcb0c482e65a95ccafa9ac) = [split_closed_wire](../../d2/d57/group__draftfunctions.html#ga23c12c1c523cdb3f7209e0db692f373a)  
def | [draftfunctions.split.splitOpenWire](../../d2/d57/group__draftfunctions.html#gaae2356b6acf0d07e5c3c8d45239b9d0f) = [split_open_wire](../../d2/d57/group__draftfunctions.html#gafc191032e1c328346d1c042ed97c8002)  
  
## Detailed Description

Modules with functions for use with scripted objects and GuiCommands.

## Function Documentation

## ◆ array()

def draftfunctions.array.array  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _arg1_ ,   
|  |  | _arg2_ ,   
|  |  | _arg3_ ,   
|  |  | _arg4_ = `None`,   
|  |  | _arg5_ = `None`,   
|  |  | _arg6_ = `None`  
| ) | |   
      
    
    This function creates an array of independent objects.
    Use make_array() to create a parametric array object.
    
    Creates an array of the given objects (that can be an object or a list
    of objects).
    
    In case of rectangular array, xnum of iterations in the x direction
    at xvector distance between iterations, and same for y and z directions
    with yvector and ynum and zvector and znum.
    
    In case of polar array, center is a vector, totalangle is the angle
    to cover (in degrees) and totalnum is the number of objects, including
    the original.
    
    Use
    ---
    array(objectslist, xvector, yvector, xnum, ynum) for rectangular array
    
    array(objectslist, xvector, yvector, zvector, xnum, ynum, znum) for rectangular array
    
    array(objectslist, center, totalangle, totalnum) for polar array
    

References
[draftfunctions.array.polarArray()](../../d2/d57/group__draftfunctions.html#ga4857d7b09a812f72c38762d140ae1625),
[draftfunctions.array.rectArray()](../../d2/d57/group__draftfunctions.html#gae0643813f550064418f49422d4d91a12),
and
[draftfunctions.array.rectArray2()](../../d2/d57/group__draftfunctions.html#ga29d7d4b92cebde4989632a2adf167f0b).

Referenced by
[App::Document.getPathsByOutList()](../../d8/d3e/classApp_1_1Document.html#a6c4fd3b7f7700be4e25980669d35a108),
[nlohmann::detail.hash()](../../dc/df0/namespacenlohmann_1_1detail.html#a679e5e522ac6afa5d5923292fab450b8),
[nlohmann::detail::json_sax_dom_parser< BasicJsonType
>.start_array()](../../dc/d68/classnlohmann_1_1detail_1_1json__sax__dom__parser.html#a056b895d011efaf48ea096c024aca0d4),
and [nlohmann::detail::json_sax_dom_callback_parser< BasicJsonType
>.start_array()](../../d6/d69/classnlohmann_1_1detail_1_1json__sax__dom__callback__parser.html#a5255b98ba8282e3625968f91cff9d3d0).

## ◆ copy_moved_edge()

def draftfunctions.move.copy_moved_edge  | ( |  | _object_ ,   
---|---|---|---  
|  |  | _edge_index_ ,   
|  |  | _vector_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

Referenced by
[draftfunctions.move.copy_moved_edges()](../../d2/d57/group__draftfunctions.html#ga73be57b46917993128fa3784697024d3).

## ◆ copy_moved_edges()

def draftfunctions.move.copy_moved_edges  | ( |  | _arguments_| ) |   
---|---|---|---|---|---  
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.move.copy_moved_edge()](../../d2/d57/group__draftfunctions.html#ga3922e2cc6ed7e9cb1c93f6226922e73f).

## ◆ copy_rotated_edge()

def draftfunctions.rotate.copy_rotated_edge  | ( |  | _object_ ,   
---|---|---|---  
|  |  | _edge_index_ ,   
|  |  | _angle_ ,   
|  |  | _center_ ,   
|  |  | _axis_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.rotate.rotate_vector_from_center()](../../d2/d57/group__draftfunctions.html#ga183986f7cd09d522dd82a38b522c2353).

Referenced by
[draftfunctions.rotate.copy_rotated_edges()](../../d2/d57/group__draftfunctions.html#gacd1c2653ca92dbad2c87bc0758f5ca28).

## ◆ copy_rotated_edges()

def draftfunctions.rotate.copy_rotated_edges  | ( |  | _arguments_| ) |   
---|---|---|---|---|---  
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.rotate.copy_rotated_edge()](../../d2/d57/group__draftfunctions.html#gac94fa90639a8f9b3018079697a984991).

## ◆ copy_scaled_edge()

def draftfunctions.scale.copy_scaled_edge  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _edge_index_ ,   
|  |  | _scale_ ,   
|  |  | _center_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.scale.scale_vector_from_center()](../../d2/d57/group__draftfunctions.html#ga2cd4c3d5877a9514b471589548d292a7).

Referenced by
[draftfunctions.scale.copy_scaled_edges()](../../d2/d57/group__draftfunctions.html#gac59d9b5d86c38c42b59625f7feef2a68).

## ◆ copy_scaled_edges()

def draftfunctions.scale.copy_scaled_edges  | ( |  | _arguments_| ) |   
---|---|---|---|---|---  
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.scale.copy_scaled_edge()](../../d2/d57/group__draftfunctions.html#gacfa4a432df41da7183fa4d67082afbe4).

## ◆ cut()

def draftfunctions.cut.cut  | ( |  | _object1_ ,   
---|---|---|---  
|  |  | _object2_  
| ) | |   
      
    
    Return a cut object made from the difference of the 2 given objects.
    
    Parameters
    ----------
    object1: Part::Feature
        Any object with a `Part::TopoShape`.
    
    object2: Part::Feature
        Any object with a `Part::TopoShape`.
    
    Returns
    -------
    Part::Cut
        The resulting cut object.
    
    None
        If there is a problem and the new object can't be created.
    

Referenced by
[MRichTextEdit.MRichTextEdit()](../../d0/d27/classMRichTextEdit.html#af11103ab97f1027cfe3beffe3f65f860).

## ◆ downgrade()

def draftfunctions.downgrade.downgrade  | ( |  | _objects_ ,   
---|---|---|---  
|  |  | _delete_ = `False`,   
|  |  | _force_ = `None`  
| ) | |   
      
    
    Downgrade the given objects.
    
    This is a counterpart to `upgrade`.
    
    Parameters
    ----------
    objects: Part::Feature or list
        A single object to downgrade or a list
        containing various such objects.
    
    delete: bool, optional
        It defaults to `False`.
        If it is `True`, the old objects are deleted, and only the resulting
        object is kept.
    
    force: str, optional
        It defaults to `None`.
        Its value can be used to force a certain method of downgrading.
        It can be any of: `'explode'`, `'shapify'`, `'subtr'`, `'splitFaces'`,
        `'cut2'`, `'getWire'`, `'splitWires'`, or `'splitCompounds'`.
    
    Returns
    -------
    tuple
        A tuple containing two lists, a list of new objects
        and a list of objects to be deleted.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    ugrade
    

## ◆ draftify()

def draftfunctions.draftify.draftify  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _makeblock_ = `False`,   
|  |  | _delete_ = `True`  
| ) | |   
      
    
    draftify(objectslist,[makeblock],[delete])
    
    Turn each object of the given list (objectslist can also be a single 
    object) into a Draft parametric wire. 
    
    TODO: support more objects
    
    Parameters
    ----------
    objectslist :
    
    makeblock : bool
        If makeblock is True, multiple objects will be grouped in a block.
    
    delete : bool
        If delete = False, old objects are not deleted
    

References
[draftfunctions.draftify.draftify_shape()](../../d2/d57/group__draftfunctions.html#ga4abdb8a69913c60c9ec19c300e056acc).

## ◆ draftify_shape()

def draftfunctions.draftify.draftify_shape  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
  
Referenced by
[draftfunctions.draftify.draftify()](../../d2/d57/group__draftfunctions.html#ga42fd321bf362162d928a99207a127d4e).

## ◆ extrude()

def draftfunctions.extrude.extrude  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _vector_ ,   
|  |  | _solid_ = `False`  
| ) | |   
      
    
    extrude(object, vector, [solid])
    
    Create a Part::Extrusion object from a given object.
    
    Parameters
    ----------
    obj :
    
    vector : Base.Vector
        The extrusion direction and module.
    
    solid : bool
        TODO: describe.
    

## ◆ format_point()

def draftfunctions.svg.format_point  | ( |  | _coords_ ,   
---|---|---|---  
|  |  | _action_ = `'L'`  
| ) | |   
      
    
    Return a string with a formatted point.

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftfunctions.svg.get_arrow()](../../d2/d57/group__draftfunctions.html#gad0c5f4b0f8bd030fe07ce7888b4de3c6),
[draftfunctions.svg.get_overshoot()](../../d2/d57/group__draftfunctions.html#gae21f92b52a2afee8c5292d737556e48f),
[draftfunctions.svgshapes.get_path()](../../d2/d57/group__draftfunctions.html#gab86383da15f203f9678b68148e7d5e84),
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e),
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1),
and
[DraftVecUtils.scaleTo()](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3).

Referenced by
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5).

## ◆ fuse()

def draftfunctions.fuse.fuse  | ( |  | _object1_ ,   
---|---|---|---  
|  |  | _object2_  
| ) | |   
      
    
    fuse(oject1, object2)
    
    Returns an object made from the union of the 2 given objects. 
    If the objects are coplanar, a special Draft Wire is used, otherwise we use
    a standard Part fuse.

## ◆ get_arrow()

def draftfunctions.svg.get_arrow  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _arrowtype_ ,   
|  |  | _point_ ,   
|  |  | _arrowsize_ ,   
|  |  | _color_ ,   
|  |  | _linewidth_ ,   
|  |  | _angle_ = `0`  
| ) | |   
      
    
    Get the SVG representation from an arrow.

Referenced by
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
and
[draftfunctions.svg.getArrow()](../../d2/d57/group__draftfunctions.html#ga1d49353fdfcd9f576d8155e7e7c80b4b).

## ◆ get_circle()

def draftfunctions.svgshapes.get_circle  | ( |  | _plane_ ,   
---|---|---|---  
|  |  | _fill_ ,   
|  |  | _stroke_ ,   
|  |  | _linewidth_ ,   
|  |  | _lstyle_ ,   
|  |  | _edge_  
| ) | |   
      
    
    Get the SVG representation from a circular edge.

References
[draftfunctions.svgshapes.get_discretized()](../../d2/d57/group__draftfunctions.html#gad1f8c64191307ca88d266845f45e7290),
and
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e).

Referenced by
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
[draftfunctions.svgshapes.getCircle()](../../d2/d57/group__draftfunctions.html#ga72cb5605a599c3e687ab08d86b2501cc),
and
[draftfunctions.svgshapes.getDiscretized()](../../d2/d57/group__draftfunctions.html#ga68258a215202f02c01dc3b0f47791ebf).

## ◆ get_discretized()

def draftfunctions.svgshapes.get_discretized  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _plane_  
| ) | |   
      
    
    Get a discretized edge on a plane.

References
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e).

Referenced by
[draftfunctions.svgshapes.get_circle()](../../d2/d57/group__draftfunctions.html#ga863618a060532a94639ba3cda58ef49d),
and
[draftfunctions.svgshapes.getDiscretized()](../../d2/d57/group__draftfunctions.html#ga68258a215202f02c01dc3b0f47791ebf).

## ◆ get_dxf()

def draftfunctions.dxf.get_dxf  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _direction_ = `None`  
| ) | |   
      
    
    Return a DXF entity from the given object.
    
    If direction is given, the object is projected in 2D.
    

References
[draftfunctions.dxf.get_dxf()](../../d2/d57/group__draftfunctions.html#ga90ba94edeb5cbf46870b8d1b10c2fa81),
and
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687).

Referenced by
[draftfunctions.dxf.get_dxf()](../../d2/d57/group__draftfunctions.html#ga90ba94edeb5cbf46870b8d1b10c2fa81),
and
[draftfunctions.dxf.getDXF()](../../d2/d57/group__draftfunctions.html#ga627306a5ef4c17e991ae65c7a98a6898).

## ◆ get_ellipse()

def draftfunctions.svgshapes.get_ellipse  | ( |  | _plane_ ,   
---|---|---|---  
|  |  | _fill_ ,   
|  |  | _stroke_ ,   
|  |  | _linewidth_ ,   
|  |  | _lstyle_ ,   
|  |  | _edge_  
| ) | |   
      
    
    Get the SVG representation from an elliptical edge.

References
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e).

Referenced by
[draftfunctions.svgshapes.getEllipse()](../../d2/d57/group__draftfunctions.html#gab22bd7595bc834d3bcd09f85961163f3).

## ◆ get_line_style()

def draftfunctions.svg.get_line_style  | ( |  | _line_style_ ,   
---|---|---|---  
|  |  | _scale_  
| ) | |   
      
    
    Return a linestyle scaled by a factor.

Referenced by
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
and
[draftfunctions.svg.getLineStyle()](../../d2/d57/group__draftfunctions.html#gaaa57d4eb618d7d775ecae628c1bbeffc).

## ◆ get_overshoot()

def draftfunctions.svg.get_overshoot  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _shootsize_ ,   
|  |  | _color_ ,   
|  |  | _linewidth_ ,   
|  |  | _angle_ = `0`  
| ) | |   
      
    
    Get the SVG representation of a dimension line overshoot.

Referenced by
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
and
[draftfunctions.svg.getOvershoot()](../../d2/d57/group__draftfunctions.html#ga7be23f0a96f4507a8a25d60143ff1224).

## ◆ get_path()

def draftfunctions.svgshapes.get_path  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _plane_ ,   
|  |  | _fill_ ,   
|  |  | _pathdata_ ,   
|  |  | _stroke_ ,   
|  |  | _linewidth_ ,   
|  |  | _lstyle_ ,   
|  |  | _fill_opacity_ = `None`,   
|  |  | _edges_ = `[]`,   
|  |  | _wires_ = `[]`,   
|  |  | _pathname_ = `None`  
| ) | |   
      
    
    Get the SVG representation from an object's edges or wires.
    
    TODO: the `edges` and `wires` must not default to empty list `[]`
    but to `None`. Verify that the code doesn't break with this change.
    
    `edges` and `wires` are mutually exclusive. If no `wires` are provided,
    sort the `edges`, and use them. If `wires` are provided, sort the edges
    in these `wires`, and use them.
    

References
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e).

Referenced by
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
and
[draftfunctions.svgshapes.getPath()](../../d2/d57/group__draftfunctions.html#ga36789b0e79a1612c2420c50806e918b0).

## ◆ get_pattern()

def draftfunctions.svg.get_pattern  | ( |  | _pat_| ) |   
---|---|---|---|---|---  
      
    
    Get an SVG pattern.

Referenced by
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
and
[draftfunctions.svg.getPattern()](../../d2/d57/group__draftfunctions.html#ga9814766327c319b343e4e1e6064b90d5).

## ◆ get_print_color()

def draftfunctions.svg.get_print_color  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    returns the print color of the parent layer, if available

Referenced by
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5).

## ◆ get_proj()

def draftfunctions.svgshapes.get_proj  | ( |  | _vec_ ,   
---|---|---|---  
|  |  | _plane_ = `None`  
| ) | |   
      
    
    Get a projection of the vector in the plane's u and v directions.
    
    TODO: check if the same function for SVG and DXF projection can be used
    so that this function is not just duplicated code.
    This function may also be present elsewhere, like `WorkingPlane`
    or `DraftGeomUtils`, so we should avoid code duplication.
    
    Parameters
    ----------
    vec: Base::Vector3
        An arbitrary vector that will be projected on the U and V directions.
    
    plane: WorkingPlane.Plane
        An object of type `WorkingPlane`.
    

References
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc).

Referenced by
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[draftfunctions.svgshapes.get_circle()](../../d2/d57/group__draftfunctions.html#ga863618a060532a94639ba3cda58ef49d),
[draftfunctions.svgshapes.get_discretized()](../../d2/d57/group__draftfunctions.html#gad1f8c64191307ca88d266845f45e7290),
[draftfunctions.svgshapes.get_ellipse()](../../d2/d57/group__draftfunctions.html#ga6b46140c1f08ae819c29290fe9166ed3),
[draftfunctions.svgshapes.get_path()](../../d2/d57/group__draftfunctions.html#gab86383da15f203f9678b68148e7d5e84),
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
[draftfunctions.svgshapes.getDiscretized()](../../d2/d57/group__draftfunctions.html#ga68258a215202f02c01dc3b0f47791ebf),
and
[draftfunctions.svgshapes.getProj()](../../d2/d57/group__draftfunctions.html#ga8101bc4fc8fa7eba53b0312546178d6d).

## ◆ get_svg()

def draftfunctions.svg.get_svg  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _scale_ = `1`,   
|  |  | _linewidth_ = `0.35`,   
|  |  | _fontsize_ = `12`,   
|  |  | _fillstyle_ = `"shape color"`,   
|  |  | _direction_ = `None`,   
|  |  | _linestyle_ = `None`,   
|  |  | _color_ = `None`,   
|  |  | _linespacing_ = `None`,   
|  |  | _techdraw_ = `False`,   
|  |  | _rotation_ = `0`,   
|  |  | _fillspaces_ = `False`,   
|  |  | _override_ = `True`  
| ) | |   
      
    
    Return a string containing an SVG representation of the object.
    
    Paramaeters
    -----------
    scale: float, optional
        It defaults to 1.
        It allows scaling line widths down, so they are resolution-independent.
    
    linewidth: float, optional
        It defaults to 0.35.
    
    fontsize: float, optional
        It defaults to 12, which is interpreted as `pt` unit (points).
        It is used if the given object contains any text.
    
    fillstyle: str, optional
        It defaults to 'shape color'.
    
    direction: Base::Vector3, optional
        It defaults to `None`.
        It is an arbitrary projection vector or a `WorkingPlane.Plane`
        instance.
    
    linestyle: optional
        It defaults to `None`.
    
    color: optional
        It defaults to `None`.
    
    linespacing: float, optional
        It defaults to `None`.
    
    techdraw: bool, optional
        It defaults to `False`.
        If it is `True`, it sets some options for generating SVG strings
        for displaying inside TechDraw.
    
    rotation: float, optional
        It defaults to 0.
    
    fillspaces: bool, optional
        It defaults to `False`.
    
    override: bool, optional
        It defaults to `True`.
    

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftfunctions.svg.format_point()](../../d2/d57/group__draftfunctions.html#ga8f27938b7ca9e7515f875ef70690525a),
[draftfunctions.svg.get_arrow()](../../d2/d57/group__draftfunctions.html#gad0c5f4b0f8bd030fe07ce7888b4de3c6),
[draftfunctions.svgshapes.get_circle()](../../d2/d57/group__draftfunctions.html#ga863618a060532a94639ba3cda58ef49d),
[draftfunctions.svg.get_line_style()](../../d2/d57/group__draftfunctions.html#ga2dcc2f8d9735fb301723edb4bb281337),
[draftfunctions.svgshapes.get_path()](../../d2/d57/group__draftfunctions.html#gab86383da15f203f9678b68148e7d5e84),
[draftfunctions.svg.get_pattern()](../../d2/d57/group__draftfunctions.html#ga2152e008a9d7effdee6f2d6e15876ecc),
[draftfunctions.svg.get_print_color()](../../d2/d57/group__draftfunctions.html#ga6e2f37e1614888b89c9af5a451de7c71),
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e),
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
[WorkingPlane.plane](../../d8/d4a/namespaceWorkingPlane.html#acd818647b5d80bd53b91ee7d60184f68),
and
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1).

Referenced by
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5),
and
[draftfunctions.svg.getSVG()](../../d2/d57/group__draftfunctions.html#gafc5b11e972efd1ebb72e945dc36e8d6a).

## ◆ get_text()

def draftfunctions.svgtext.get_text  | ( |  | _plane_ ,   
---|---|---|---  
|  |  | _techdraw_ ,   
|  |  | _tcolor_ ,   
|  |  | _fontsize_ ,   
|  |  | _fontname_ ,   
|  |  | _angle_ ,   
|  |  | _base_ ,   
|  |  | _text_ ,   
|  |  | _linespacing_ = `0.5`,   
|  |  | _align_ = `"center"`,   
|  |  | _flip_ = `True`  
| ) | |   
      
    
    Get the SVG representation of a textual element.

Referenced by
[draftfunctions.svgtext.getText()](../../d2/d57/group__draftfunctions.html#ga898571506aacbbc685cd35b2a45658d7).

## ◆ getArrow()

def draftfunctions.svg.getArrow  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _arrowtype_ ,   
|  |  | _point_ ,   
|  |  | _arrowsize_ ,   
|  |  | _color_ ,   
|  |  | _linewidth_ ,   
|  |  | _angle_ = `0`  
| ) | |   
      
    
    Get the SVG representation from an arrow. DEPRECATED.

References
[draftfunctions.svg.get_arrow()](../../d2/d57/group__draftfunctions.html#gad0c5f4b0f8bd030fe07ce7888b4de3c6).

## ◆ getCircle()

def draftfunctions.svgshapes.getCircle  | ( |  | _plane_ ,   
---|---|---|---  
|  |  | _fill_ ,   
|  |  | _stroke_ ,   
|  |  | _linewidth_ ,   
|  |  | _lstyle_ ,   
|  |  | _edge_  
| ) | |   
      
    
    Get the SVG representation from a circular edge.

References
[draftfunctions.svgshapes.get_circle()](../../d2/d57/group__draftfunctions.html#ga863618a060532a94639ba3cda58ef49d).

Referenced by
[importIFCHelper.get2DShape()](../../d6/d78/namespaceimportIFCHelper.html#a5604c6416a97e1beb1dc51b7ee69822b).

## ◆ getDiscretized()

def draftfunctions.svgshapes.getDiscretized  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _plane_  
| ) | |   
      
    
    Get a discretized edge on a plane. DEPRECATED.

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftfunctions.svgshapes.get_circle()](../../d2/d57/group__draftfunctions.html#ga863618a060532a94639ba3cda58ef49d),
[draftfunctions.svgshapes.get_discretized()](../../d2/d57/group__draftfunctions.html#gad1f8c64191307ca88d266845f45e7290),
and
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e).

## ◆ getDXF()

def draftfunctions.dxf.getDXF  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _direction_ = `None`  
| ) | |   
      
    
    Return DXF string of the object. DEPRECATED. Use 'get_dxf'.

References
[draftfunctions.dxf.get_dxf()](../../d2/d57/group__draftfunctions.html#ga90ba94edeb5cbf46870b8d1b10c2fa81).

Referenced by
[importDXF.export()](../../d7/dbf/namespaceimportDXF.html#ae90d02ee42cc3c2b7daa7138cc8d02a4),
and
[importDXF.getViewBlock()](../../d7/dbf/namespaceimportDXF.html#ad545751e708656a74476e35e19513202).

## ◆ getEllipse()

def draftfunctions.svgshapes.getEllipse  | ( |  | _plane_ ,   
---|---|---|---  
|  |  | _fill_ ,   
|  |  | _stroke_ ,   
|  |  | _linewidth_ ,   
|  |  | _lstyle_ ,   
|  |  | _edge_  
| ) | |   
      
    
    Get the SVG representation from an elliptical edge. DEPRECATED.

References
[draftfunctions.svgshapes.get_ellipse()](../../d2/d57/group__draftfunctions.html#ga6b46140c1f08ae819c29290fe9166ed3).

## ◆ getLineStyle()

def draftfunctions.svg.getLineStyle  | ( |  | _linestyle_ ,   
---|---|---|---  
|  |  | _scale_  
| ) | |   
      
    
    Return a Line style. DEPRECATED. Use get_line_style.

References
[draftfunctions.svg.get_line_style()](../../d2/d57/group__draftfunctions.html#ga2dcc2f8d9735fb301723edb4bb281337).

## ◆ getOvershoot()

def draftfunctions.svg.getOvershoot  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _shootsize_ ,   
|  |  | _color_ ,   
|  |  | _linewidth_ ,   
|  |  | _angle_ = `0`  
| ) | |   
      
    
    Get the SVG representation of a dimension line overshoot. DEPRECATED.

References
[draftfunctions.svg.get_overshoot()](../../d2/d57/group__draftfunctions.html#gae21f92b52a2afee8c5292d737556e48f).

## ◆ getPath()

def draftfunctions.svgshapes.getPath  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _plane_ ,   
|  |  | _fill_ ,   
|  |  | _pathdata_ ,   
|  |  | _stroke_ ,   
|  |  | _linewidth_ ,   
|  |  | _lstyle_ ,   
|  |  | _fill_opacity_ ,   
|  |  | _edges_ = `[]`,   
|  |  | _wires_ = `[]`,   
|  |  | _pathname_ = `None`  
| ) | |   
      
    
    Get the SVG representation from a path. DEPRECATED.

References
[draftfunctions.svgshapes.get_path()](../../d2/d57/group__draftfunctions.html#gab86383da15f203f9678b68148e7d5e84).

Referenced by
[SpreadsheetGui::DlgSheetConf.prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3).

## ◆ getPattern()

def draftfunctions.svg.getPattern  | ( |  | _pat_| ) |   
---|---|---|---|---|---  
      
    
    Get an SVG pattern. DEPRECATED.

References
[draftfunctions.svg.get_pattern()](../../d2/d57/group__draftfunctions.html#ga2152e008a9d7effdee6f2d6e15876ecc).

## ◆ getProj()

def draftfunctions.svgshapes.getProj  | ( |  | _vec_ ,   
---|---|---|---  
|  |  | _plane_ = `None`  
| ) | |   
      
    
    Get a projection of a vector. DEPRECATED.

References
[draftfunctions.svgshapes.get_proj()](../../d2/d57/group__draftfunctions.html#ga6c24cc9f0e4e0ebdafffbfc582db0c2e).

## ◆ getSVG()

def draftfunctions.svg.getSVG  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _scale_ = `1`,   
|  |  | _linewidth_ = `0.35`,   
|  |  | _fontsize_ = `12`,   
|  |  | _fillstyle_ = `"shape color"`,   
|  |  | _direction_ = `None`,   
|  |  | _linestyle_ = `None`,   
|  |  | _color_ = `None`,   
|  |  | _linespacing_ = `None`,   
|  |  | _techdraw_ = `False`,   
|  |  | _rotation_ = `0`,   
|  |  | _fillSpaces_ = `False`,   
|  |  | _override_ = `True`  
| ) | |   
      
    
    Return SVG string of the object. DEPRECATED. Use 'get_svg'.

References
[draftfunctions.svg.get_svg()](../../d2/d57/group__draftfunctions.html#gaed46c753cc93af2cc0b280b3ffa377f5).

## ◆ getText()

def draftfunctions.svgtext.getText  | ( |  | _plane_ ,   
---|---|---|---  
|  |  | _techdraw_ ,   
|  |  | _tcolor_ ,   
|  |  | _fontsize_ ,   
|  |  | _fontname_ ,   
|  |  | _angle_ ,   
|  |  | _base_ ,   
|  |  | _text_ ,   
|  |  | _linespacing_ = `0.5`,   
|  |  | _align_ = `"center"`,   
|  |  | _flip_ = `True`  
| ) | |   
      
    
    Get the SVG representation of a textual element. DEPRECATED.

References
[draftfunctions.svgtext.get_text()](../../d2/d57/group__draftfunctions.html#ga3785091650337fe5169c6181d1cc71d0).

Referenced by
[Gui::Dialog::ParameterText.changeValue()](../../d4/d55/classGui_1_1Dialog_1_1ParameterText.html#a5fed4d148b1859b5ebc22186fc4a2221),
[Gui::PropertyEditor::PropertyEditor.contextMenuEvent()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#acc178ef7986ad83af1780aac8bf70e14),
[SpreadsheetGui::DlgBindSheet.DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[Spreadsheet::Cell.getStringContent()](../../d5/d22/classSpreadsheet_1_1Cell.html#a9b25d18f3a96cdb96b1f47cb0411f32c),
[Gui::Dialog::DlgMacroExecuteImp.on_createButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a47eb382b837c65c8e46d41158aeb0b80),
[Gui::Dialog::DlgMacroExecuteImp.on_duplicateButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#ae0df9f58ffc728ac2e5739c615183c54),
[Gui::Dialog::DlgCustomToolbars.on_newButton_clicked()](../../db/d86/classGui_1_1Dialog_1_1DlgCustomToolbars.html#a9a609505ad7089dadd723056f20394c2),
[Gui::Dialog::DlgMacroExecuteImp.on_renameButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a1a9680d49cf27716db1db489c384456e),
[Gui::Dialog::DlgCustomToolbars.on_renameButton_clicked()](../../db/d86/classGui_1_1Dialog_1_1DlgCustomToolbars.html#a2807e6098165f73952648d0ce27bbee3),
[Gui::Dialog::ParameterValue.onCreateBoolItem()](../../de/d4f/classGui_1_1Dialog_1_1ParameterValue.html#a743a80c892b5f5766de5fd46a4b14b35),
[Gui::Dialog::ParameterValue.onCreateFloatItem()](../../de/d4f/classGui_1_1Dialog_1_1ParameterValue.html#a6efbe37553a3a30db6d32abd4f0179d6),
[Gui::Dialog::ParameterValue.onCreateIntItem()](../../de/d4f/classGui_1_1Dialog_1_1ParameterValue.html#a7b67084f1f154d0a47c02187ed5c34d4),
[Gui::Dialog::ParameterGroup.onCreateSubgroup()](../../de/d18/classGui_1_1Dialog_1_1ParameterGroup.html#a7fdd9aea3daeae63084ff8769fa561b7),
[Gui::Dialog::ParameterValue.onCreateTextItem()](../../de/d4f/classGui_1_1Dialog_1_1ParameterValue.html#abbb9c04fd10373e1a136888d43c358d9),
[Gui::Dialog::ParameterValue.onCreateUIntItem()](../../de/d4f/classGui_1_1Dialog_1_1ParameterValue.html#a0aa3e96edafaf6033e9d2cb6260b4052),
and
[MRichTextEdit.textLink()](../../d0/d27/classMRichTextEdit.html#adacb62d89f970e019f2658116ed76a0a).

## ◆ heal()

def draftfunctions.heal.heal  | ( |  | _objlist_ = `None`,   
---|---|---|---  
|  |  | _delete_ = `True`,   
|  |  | _reparent_ = `True`  
| ) | |   
      
    
    heal([objlist],[delete],[reparent])
    
    Recreate Draft objects that are damaged, for example if created from an
    earlier version. If ran without arguments, all the objects in the document 
    will be healed if they are damaged.
    
    Parameters
    ----------
    objlist : list
    
    delete : Base.Vector or list of Base.Vector
        If delete is True, the damaged objects are deleted (default).
    
    reparent : bool
        If reparent is True (default), new objects go at the very same place 
        in the tree than their original.
    

## ◆ join_two_wires()

def draftfunctions.join.join_two_wires  | ( |  | _wire1_ ,   
---|---|---|---  
|  |  | _wire2_  
| ) | |   
      
    
    join_two_wires(object, object): joins two wires if they share a common
    point as a start or an end.
    

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

Referenced by
[draftfunctions.join.join_wires()](../../d2/d57/group__draftfunctions.html#ga5354f8b322314e22e3f93f7a54371858).

## ◆ join_wires()

def draftfunctions.join.join_wires  | ( |  | _wires_ ,   
---|---|---|---  
|  |  | _joinAttempts_ = `0`  
| ) | |   
      
    
    join_wires(objects): merges a set of wires where possible, if any of those
    wires have a coincident start and end point

References
[draftfunctions.join.join_two_wires()](../../d2/d57/group__draftfunctions.html#ga8b7573fa746b69be82d73768bb04a557),
and
[draftfunctions.join.join_wires()](../../d2/d57/group__draftfunctions.html#ga5354f8b322314e22e3f93f7a54371858).

Referenced by
[draftfunctions.join.join_wires()](../../d2/d57/group__draftfunctions.html#ga5354f8b322314e22e3f93f7a54371858).

## ◆ mirror()

def draftfunctions.mirror.mirror  | ( |  | _objlist_ ,   
---|---|---|---  
|  |  | _p1_ ,   
|  |  | _p2_  
| ) | |   
      
    
    Create a mirror object from the provided list and line.
    
    It creates a `Part::Mirroring` object from the given `objlist` using
    a plane that is defined by the two given points `p1` and `p2`,
    and either
    
    - the Draft working plane normal, or
    - the negative normal provided by the camera direction
      if the working plane normal does not exist and the graphical interface
      is available.
    
    If neither of these two is available, it uses as normal the +Z vector.
    
    Parameters
    ----------
    objlist: single object or a list of objects
        A single object or a list of objects.
    
    p1: Base::Vector3
        Point 1 of the mirror plane. It is also used as the `Placement.Base`
        of the resulting object.
    
    p2: Base::Vector3
        Point 1 of the mirror plane.
    
    Returns
    -------
    None
        If the operation fails.
    
    list
        List of `Part::Mirroring` objects, or a single one
        depending on the input `objlist`.
    
    To Do
    -----
    Implement a mirror tool specific to the workbench that does not
    just use `Part::Mirroring`. It should create a derived object,
    that is, it should work similar to `Draft.offset`.
    

## ◆ move()

def draftfunctions.move.move  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _vector_ ,   
|  |  | _copy_ = `False`  
| ) | |   
      
    
    move(objects,vector,[copy])
    
    Move the objects contained in objects (that can be an object or a
    list of objects) in the direction and distance indicated by the given
    vector. 
    
    Parameters
    ----------
    objectslist : list
    
    vector : Base.Vector
        Delta Vector to move the clone from the original position. 
    
    copy : bool
        If copy is True, the actual objects are not moved, but copies
        are created instead. 
    
    Return
    ----------
    The objects (or their copies) are returned.
    

Referenced by [nlohmann::basic_json< ObjectType, ArrayType, StringType,
BooleanType, NumberIntegerType, NumberUnsignedType, NumberFloatType,
AllocatorType, JSONSerializer, BinaryType
>.accept()](../../d9/dcc/classnlohmann_1_1basic__json.html#a47fb596473649332185aedb0a8a6ccc5),
[App::ObjectIdentifier.addComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ac9f36b9763a88ccb797bfa63b90635b7),
[Sketcher::SketchObject.addConstraint()](../../d9/dad/classSketcher_1_1SketchObject.html#a18199c2f789ba7c3e9a72f7f3d14dd08),
[Sketcher::SketchObject.addConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#ae83cf708e98c5825d92c054f81837163),
[Sketcher::SketchObject.addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[Sketcher::SketchObject.addCopyOfConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#ae855d43b68feffdb57a0489777e2b9ad),
[Sketcher::SketchObject.addGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#aa396c8e47c8be25854a016dd6330b295),
[Gui::SelectionSingleton.addSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab2e9be9afea962a0ed8e7f73b5214b02),
[Gui::SelectionSingleton.addSelections()](../../d4/dca/classGui_1_1SelectionSingleton.html#aaf2687725c90321113035fce692c27ac),
[Sketcher::SketchObject.addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[App::PropertyXLinkSubList.addValue()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a91e5e534b886db50520e0b006556b76a),
[Path::Area.addWire()](../../d8/dfc/classPath_1_1Area.html#add006cb76dc7c842a3c56e53124b1f51),
[App::PropertyLinkSub.adjustLink()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac5e4b8833d9c02383d6ce017ca6a7730),
[App::PropertyXLink.adjustLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a33bbd1956612a56e1967fdd7d6c533ff),
[App::PropertyXLinkSubList.adjustLink()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a2fbece18bdf273d6c6d427c6cce98da7),
[App::PropertyExpressionEngine.afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[App::PropertyXLinkContainer.afterRestore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a00e6240a9cf8e5b7dbf0cf287cbd4db1),
[nlohmann::detail::json_sax_dom_parser< BasicJsonType
>.binary()](../../dc/d68/classnlohmann_1_1detail_1_1json__sax__dom__parser.html#acc05c450d515f0f95c37401bf23c8db3),
[nlohmann::detail::json_sax_dom_callback_parser< BasicJsonType
>.binary()](../../d6/d69/classnlohmann_1_1detail_1_1json__sax__dom__callback__parser.html#a66f5515cddef5074c9499f21c26ac099),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.binary()](../../d9/dcc/classnlohmann_1_1basic__json.html#ab085777bbfbfac5a472120b991ef5cf3),
[Path::Area.build()](../../d8/dfc/classPath_1_1Area.html#a14cdd0bbdcc7ed326244217da15ad6db),
[Gui::PropertyEditor::PropertyEditor.buildUp()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#a00d6964123d5c1c51b41538befbe5ca6),
[Sketcher::SketchObject.carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[Sketcher::SketchObject.changeConstraintsLocking()](../../d9/dad/classSketcher_1_1SketchObject.html#ac693bddc46ae81ee5490ebe387604b50),
[App::PropertyLinkBase.checkLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b),
[Gui::SelectionSingleton.clearCompleteSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a30167ec497bab08a49322dbd8b1b9565),
[GEOMUtils.CompsolidToCompound()](../../db/daf/namespaceGEOMUtils.html#aefca7717b993c0391fd85ac900e1a61e),
[nlohmann::detail::external_constructor< value_t::array
>.construct()](../../d4/d91/structnlohmann_1_1detail_1_1external__constructor_3_01value__t_1_1array_01_4.html#a50474d6624957a630a1d398cac1e7bfa),
[nlohmann::detail::external_constructor< value_t::binary
>.construct()](../../d3/d09/structnlohmann_1_1detail_1_1external__constructor_3_01value__t_1_1binary_01_4.html#a1c478157dc8bad20f09572c5b2406150),
[nlohmann::detail::external_constructor< value_t::object
>.construct()](../../d7/d38/structnlohmann_1_1detail_1_1external__constructor_3_01value__t_1_1object_01_4.html#a1e044961affbd6417386d6e9f1d545e9),
[nlohmann::detail::external_constructor< value_t::string
>.construct()](../../da/dac/structnlohmann_1_1detail_1_1external__constructor_3_01value__t_1_1string_01_4.html#a74f56b9ca1d4e8db9751353d76668322),
[Gui::PropertyEditor::PropertyEditor.contextMenuEvent()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#acc178ef7986ad83af1780aac8bf70e14),
[Sketcher::PythonConverter.convert()](../../d3/d98/classSketcher_1_1PythonConverter.html#a3b6867ec3c74a3b96982fa0b307eed91),
[Base.convertTo()](../../db/d07/namespaceBase.html#aac148583ab806ad7c6629c7e45329167),
[Sketcher::SketchObject.convertToNURBS()](../../d9/dad/classSketcher_1_1SketchObject.html#a23e6660388fbe498a07b07a8c4f065fe),
[Part::GeometryDefaultExtension< T
>.copy()](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a49228714a23571610faeb9fb93562ee1),
[Part::GeometryMigrationExtension.copy()](../../d7/d36/classPart_1_1GeometryMigrationExtension.html#a95f1f53ca540224440d49d066326793f),
[Sketcher::ExternalGeometryExtension.copy()](../../d5/dea/classSketcher_1_1ExternalGeometryExtension.html#a1cd06df03561f548a60300d91f1f3eae),
[Sketcher::SketchGeometryExtension.copy()](../../d7/db4/classSketcher_1_1SketchGeometryExtension.html#ae2ba34b2e5a3a7ab5ef84bb0a17fa01e),
[Sketcher::SolverGeometryExtension.copy()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#a6184d82abdb99fcf4e4cfe438be8ec24),
[SketcherGui::ViewProviderSketchGeometryExtension.copy()](../../d3/d23/classSketcherGui_1_1ViewProviderSketchGeometryExtension.html#a0517aa03a098957c06d5ffbcb5ffe82c),
[App::PropertyLinkSub.CopyOnImportExternal()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a048f449b304bded2a609bc32bc3d3107),
[App::PropertyLinkSubList.CopyOnImportExternal()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a7d7f8cd3cb3ce4405391586167328afc),
[Spreadsheet::PropertySheet.CopyOnImportExternal()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a91a6447d90678a4b4b73a6b701de9588),
[App::PropertyLinkSub.CopyOnLabelChange()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a09c96d3556fa092d37d9f597fbf468c5),
[App::PropertyLinkSubList.CopyOnLabelChange()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a832033ed5b5810a9add720cd72ca6cef),
[Spreadsheet::PropertySheet.CopyOnLabelChange()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a68bfc954ffc13f24216d11faae444da4),
[App::PropertyLinkList.CopyOnLinkReplace()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4406a63b9428c6313f37413a0a8b3821),
[App::PropertyLinkSub.CopyOnLinkReplace()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a24386974f021c3d8d5c3679276b403bb),
[App::PropertyLinkSubList.CopyOnLinkReplace()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ae849b6086e5b7731cefac897c3c5b3ec),
[Spreadsheet::PropertySheet.CopyOnLinkReplace()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac7b0e47414a39b37f4bb3f6d8d0ded22),
[App::PropertyXLink.copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[nlohmann::detail::iterator_input_adapter_factory< IteratorType, Enable
>.create()](../../d4/d8c/structnlohmann_1_1detail_1_1iterator__input__adapter__factory.html#a1d3a80249cf837448966319310be9ec4),
[nlohmann::detail::iterator_input_adapter_factory< IteratorType, enable_if_t<
is_iterator_of_multibyte< IteratorType >::value >
>.create()](../../da/d6d/structnlohmann_1_1detail_1_1iterator__input__adapter__factory_3_01IteratorType_00_01enable__if__0e86378a778d78dd2284e92dc30f4902.html#aae2354d80ae95214a9da99c495003f6c),
[Sketcher::SketchObject.delAllExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#ae20c5b24ce66380931e7da7299dabd6e),
[Sketcher::SketchObject.delConstraint()](../../d9/dad/classSketcher_1_1SketchObject.html#a01809dda308d8664dd04c2d61ed8fa73),
[Sketcher::SketchObject.delConstraintOnPoint()](../../d9/dad/classSketcher_1_1SketchObject.html#a4ee7c657fbca65cf10d310348671575f),
[Sketcher::SketchObject.delConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a7e276986a399ec82e36fa246027b066d),
[Sketcher::SketchObject.delConstraintsToExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#acf7fe62d1ecf4baadf75203a67964c5c),
[Sketcher::SketchObject.delExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a51f4b69d9928669abe729269157d2224),
[Sketcher::SketchObject.delGeometriesExclusiveList()](../../d9/dad/classSketcher_1_1SketchObject.html#ab5a3748762c070a9eb006c467947fc3f),
[Sketcher::SketchObject.delGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a40dfaae474c808c67807476529431053),
[App::DocumentObjectT.DocumentObjectT()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6afcac6fac9a081c8db420dbb01a877),
[PartDesignGui::ViewProviderBody.dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[PartDesignGui::ViewProviderSubShapeBinder.dropObjectEx()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#abdd84ec90fe95fc762d7cc1d7331b5b1),
[nlohmann::ordered_map< Key, T, IgnoredLess, Allocator
>.erase()](../../d6/da7/structnlohmann_1_1ordered__map.html#a583c8976bbf0c137ff8e2439878f3058),
[Sketcher::Sketch.extractGeoListFacade()](../../d9/d9b/classSketcher_1_1Sketch.html#a655b06bbd8171e4cdff81070a0e1730c),
[App::ObjectIdentifier::Component.FC_DEFAULT_CTORS()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a70f440629467801d72f7480f4f3f87e9),
[App::ObjectIdentifier.FC_DEFAULT_CTORS()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a0251f583f4962e4da5b5db149200cc19),
[App::ObjectIdentifier::String.FC_DEFAULT_CTORS()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7691f0d9365d5c72fbfbf9a945b3e857),
[Sketcher::SketchObject.fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a43c1d2127f6883712935706a98e1cf4a),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.from_bson()](../../d9/dcc/classnlohmann_1_1basic__json.html#a4e02793f2691aa29ab7cb69fddafbf5c),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.from_cbor()](../../d9/dcc/classnlohmann_1_1basic__json.html#a44dd5635fb2da4710f6cd6e42b72773f),
[nlohmann::detail.from_json()](../../dc/df0/namespacenlohmann_1_1detail.html#a5b24896e5f5db6af06d939dde4b63fe1),
[nlohmann::detail.from_json_array_impl()](../../dc/df0/namespacenlohmann_1_1detail.html#a464e1246f3df7edea79c3f81ab701edd),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.from_msgpack()](../../d9/dcc/classnlohmann_1_1basic__json.html#adbcab52fca1e25b3311ef14e71a57590),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.from_ubjson()](../../d9/dcc/classnlohmann_1_1basic__json.html#aa81f62db69978b90ff701f05c72e03a7),
[nlohmann::detail::span_input_adapter.get()](../../da/d7e/classnlohmann_1_1detail_1_1span__input__adapter.html#a20f57e8bfcf0afb40e8c02f34080784e),
[SketcherGui::EditModeGeometryCoinConverter.getBSplineGeoIds()](../../d7/dcb/classSketcherGui_1_1EditModeGeometryCoinConverter.html#ae1afcef9f9880154f891c6da7e0befaf),
[SMESH_subMesh.getCollection()](../../de/d76/classSMESH__subMesh.html#aa6cac454ba9d774f0e5a69161e55295f),
[Sketcher.getGeoListFacade()](../../d1/d23/namespaceSketcher.html#a0c940157061bff5dcef36f21e7bdfeba),
[Sketcher::SketchObject.getGeoListFacade()](../../d9/dad/classSketcher_1_1SketchObject.html#aba5ef05c14ae6f58cdb210c7be3be0ba),
[Sketcher::GeoListModel< T
>.getGeoListModel()](../../df/d90/classSketcher_1_1GeoListModel.html#a71e09c068b8615ee11e904a02ac33be0),
[App::PropertyLinkSubList.getLinks()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#afeb6881f95c7f7f897fb2bfd0ee3895b),
[App::PropertyXLinkSubList.getLinks()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a474c20d3ad36ebec314c141803e0ca3b),
[App::Document.getLinksTo()](../../d8/d3e/classApp_1_1Document.html#a68fa1555a634a2da10ba434f64fbf2f2),
[App::SubObjectT.getNewElementName()](../../dd/d78/classApp_1_1SubObjectT.html#a3f4df581957c8dbc1ffaee6d315ea452),
[App::SubObjectT.getOldElementName()](../../dd/d78/classApp_1_1SubObjectT.html#a91100833ef50109008ae5deff6cd2441),
[PartDesign::Transformed.getRemainingSolids()](../../dd/de1/classPartDesign_1_1Transformed.html#a66375862e5e8a57099cdab311b10b540),
[App::PropertyExpressionEngine.hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[Spreadsheet::PropertySheet.hasSetValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585),
[App::Expression.importSubNames()](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1),
[Sketcher::SketchObject.increaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#a3daba3e80990ea7e01b8b4a9bde2217a),
[nlohmann::ordered_map< Key, T, IgnoredLess, Allocator
>.insert()](../../d6/da7/structnlohmann_1_1ordered__map.html#a2dafd3fdc7dbd3233bb8c85824ee7cb0),
[Sketcher::SketchObject.insertBSplineKnot()](../../d9/dad/classSketcher_1_1SketchObject.html#a48c6d4c74904307c87c4e8f65a9e89af),
[MeshCore::MeshProjection.isPointInsideDistance()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a1bc07b7339c80de0c54cc14bf844a3d2),
[Gui::MainWindow.loadWindowSettings()](../../d5/d2f/classGui_1_1MainWindow.html#a00d4bad121cc286443a7f7f628f519f8),
[Part::FaceMakerCheese.makeFace()](../../d0/d37/classPart_1_1FaceMakerCheese.html#a319db8e00dd1aaf35e0425f7243c71b8),
[Part::TopoShape.makeHelix()](../../d8/ded/classPart_1_1TopoShape.html#a5b7da990bce73f4ece22e50a4270ff9e),
[Part::TopoShape.makeLongHelix()](../../d8/ded/classPart_1_1TopoShape.html#a8c50989f95b412850bdd8226be6523ba),
[Part::TopoShape.makeOffset2D()](../../d8/ded/classPart_1_1TopoShape.html#a65ecb4128e9aacf3c48c3fe0a51b9658),
[Part::TopoShape.makeSpiralHelix()](../../d8/ded/classPart_1_1TopoShape.html#a0604f7c336ad5c2c2339599acde30089),
[App::ObjectIdentifier::Component.MapComponent()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#acceec2bae5724de3e15000d1747fe0e6),
[Sketcher::SketchObject.modifyBSplineKnotMultiplicity()](../../d9/dad/classSketcher_1_1SketchObject.html#ae318b60c226c883e53725f9ebef29991),
[Gui::Flag.mouseMoveEvent()](../../dc/dd0/classGui_1_1Flag.html#a03078ff2e2826982ccc394b84271b68e),
[CArea.move()](../../d3/d52/classCArea.html#a9212214a922fb3be415cceb1db4133cf),
[Base::Matrix4D.move()](../../d5/db4/classBase_1_1Matrix4D.html#ac26497380187a175bcd5e43a0c81740f),
[nlohmann::detail::json_ref< BasicJsonType
>.moved_or_copied()](../../da/d10/classnlohmann_1_1detail_1_1json__ref.html#ae39e523218bf05cac3fb5b5b1cd5efb6),
[Sketcher::SketchObject.moveDatumsToEnd()](../../d9/dad/classSketcher_1_1SketchObject.html#a5e54927411f1ca4754a05bad0354d173),
[Gui::SelectionSingleton.notify()](../../d4/dca/classGui_1_1SelectionSingleton.html#a50ab2367fb54a9eba65380550698d811),
[App::LinkBaseExtension.onExtendedDocumentRestored()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a5805b7a58266b550e7bf7e3569c8ed34),
[Gui::PropertyView.onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[App::Application.openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[App::Application.openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.operator+=()](../../d9/dcc/classnlohmann_1_1basic__json.html#a40226d9c84fcb9cb948ae0c27b842c57),
[nlohmann::json_pointer< BasicJsonType
>.operator/=()](../../da/de8/classnlohmann_1_1json__pointer.html#a0fd4fa3951d134f54622856ccf8f1021),
[App::ObjectIdentifier.operator<<()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae4dc019b4c1ee75d7dd83a6265850d85),
[App::DocumentObjectT.operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#a43092ac909db57e859c9a45bcc323ea3),
[Gui::SelectionChanges.operator=()](../../d5/d50/classGui_1_1SelectionChanges.html#ac0754615341fa526129b06cd4b17033e),
[App::SubObjectT.operator=()](../../dd/d78/classApp_1_1SubObjectT.html#a783148f9c5cd3c7d9019c933c63ca212),
[Gui::ViewProviderT.operator=()](../../df/d5a/classGui_1_1ViewProviderT.html#affee3dc7e0ef5f41393548e443a2f1d8),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.parse()](../../d9/dcc/classnlohmann_1_1basic__json.html#ad832c70af0989389a9a104c21d2d1c5c),
[StdCmdExpression.pasteExpressions()](../../d2/dae/classStdCmdExpression.html#abab137615ab802f7688ff0b623022b9f),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.patch()](../../d9/dcc/classnlohmann_1_1basic__json.html#adcc786998f220a5b3083ee8a37c4553e),
[Sketcher::SketchObject.port_reversedExternalArcs()](../../d9/dad/classSketcher_1_1SketchObject.html#a7a63cf359bdc3559fb9911559f4d1cd7),
[TechDraw::DrawViewDetail.projectEdgesOntoFace()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#afceac336ba70bc54258f0badf3d6997d),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.push_back()](../../d9/dcc/classnlohmann_1_1basic__json.html#ab9e0253c92736db021840105d374c4c4),
[nlohmann::json_pointer< BasicJsonType
>.push_back()](../../da/de8/classnlohmann_1_1json__pointer.html#ac228b13596d3c34185da9fe61b570194),
[App::PropertyLinkBase.registerLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f),
[App::ObjectIdentifier.relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
[Sketcher::SketchObject.removeAxesAlignment()](../../d9/dad/classSketcher_1_1SketchObject.html#a7fdd15d230c082e02baefe0866420af9),
[Part::TopoShape.removeSplitter()](../../d8/ded/classPart_1_1TopoShape.html#ab9d3825efabdaeda72666474c7a767ff),
[Gui::ViewProviderDocumentObject.replaceObject()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a75216597b08f62e670dc98bf829c8254),
[Gui::Dialog::DlgPreferencesImp.resizeEvent()](../../db/dee/classGui_1_1Dialog_1_1DlgPreferencesImp.html#a94cfb985133fe74f1b7e91468662a14f),
[App::ObjectIdentifier.resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4503f7d6916abae555ddb15db1eed9ea),
[Part::PropertyGeometryList.Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[App::PropertyLinkSub.Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList.Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink.Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[Sketcher::PropertyConstraintList.Restore()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#aa6e11dd2fcd1f2307c14e3df94e4fbe7),
[Gui::SelectionSingleton.rmvPreselect()](../../d4/dca/classGui_1_1SelectionSingleton.html#a6357390d36e13dab925fed0813d7a602),
[Gui::SelectionSingleton.rmvSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab437512db2d990024017af75b4c33fb7),
[nlohmann::basic_json< ObjectType, ArrayType, StringType, BooleanType,
NumberIntegerType, NumberUnsignedType, NumberFloatType, AllocatorType,
JSONSerializer, BinaryType
>.sax_parse()](../../d9/dcc/classnlohmann_1_1basic__json.html#a12b382c6407da5543827ce4b24bb5008),
[Gui::SelectionChanges.SelectionChanges()](../../d5/d50/classGui_1_1SelectionChanges.html#a6cde5b5491442d97274a684db4e0f840),
[Gui::SelectionSingleton.selStackGoBack()](../../d4/dca/classGui_1_1SelectionSingleton.html#a8004fda7a31b115d35867bd39231af18),
[Gui::SelectionSingleton.selStackGoForward()](../../d4/dca/classGui_1_1SelectionSingleton.html#ac7caa9d275e0e233b4158aca3c1c3c4c),
[Gui::SelectionSingleton.selStackPush()](../../d4/dca/classGui_1_1SelectionSingleton.html#a32204ef30c2905001311162bedf9683b),
[Sketcher::SketchObject.setActive()](../../d9/dad/classSketcher_1_1SketchObject.html#a5580d6b9dc3b06e64005fe0deb51d07c),
[App::ObjectIdentifier.setComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a470c9df4f63a6d9ddad2d71ce7affa25),
[Sketcher::SketchObject.setConstruction()](../../d9/dad/classSketcher_1_1SketchObject.html#addc566d5b284054914f8d28751fa89ec),
[Spreadsheet::Cell.setContent()](../../d5/d22/classSpreadsheet_1_1Cell.html#a4d07e67e0412f933cb7306ee3e6b962c),
[Sketcher::SketchObject.setDatum()](../../d9/dad/classSketcher_1_1SketchObject.html#a8d93ffeacf035c3a09279b3bb3bbfa47),
[Sketcher::SketchObject.setDatumsDriving()](../../d9/dad/classSketcher_1_1SketchObject.html#acdacf3c7ba5461b771fe342fb70b134f),
[App::ObjectIdentifier.setDocumentName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0),
[App::ObjectIdentifier.setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
[Sketcher::SketchObject.setDriving()](../../d9/dad/classSketcher_1_1SketchObject.html#a392970c1962255ea0f2242353894231d),
[App::PropertyExpressionEngine.setExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af0f2f778f8e840efb832ef621441a3e9),
[Spreadsheet::PropertySheet.setExpressions()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a3bd4947db4629f272d4e29c95d74297f),
[Part::Geometry.setExtension()](../../dc/df0/classPart_1_1Geometry.html#aff618e15ec41db4a3a4c4a71294ca2e4),
[Sketcher::ExternalGeometryFacade.setExtension()](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#aa1b75b5a4905cbdff468ccc165c73a44),
[Sketcher::GeometryFacade.setExtension()](../../d1/d73/classSketcher_1_1GeometryFacade.html#ac21e26d2b7ccd5db48410d5a485c92ba),
[Sketcher::SketchObject.setGeometryId()](../../d9/dad/classSketcher_1_1SketchObject.html#ac2eb0fa691db5fd2384a171a23e3c3cf),
[App::LinkBaseExtension.setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[PartDesign::SubShapeBinder.setLinks()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a121c18838a25b1982d6732ec125f4eec),
[Spreadsheet::PropertySheet.setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
[Gui::SelectionSingleton.setPreselect()](../../d4/dca/classGui_1_1SelectionSingleton.html#a4606b917610c1a4ba91821e5405973ab),
[App::PropertyLinkSub.setPyObject()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9965507bfcc6e28d251ffb62f234df77),
[App::PropertyXLink.setPyObject()](../../d2/de2/classApp_1_1PropertyXLink.html#adb26821a0a3916e6252bc6b4f0c5637e),
[App::PropertyXLinkSubList.setPyObject()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a7160ec1120efe0609b40286324fc861f),
[App::PropertyListsT< T, ListT, ParentT
>.setPyValues()](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyXLinkSubList.setSubListValues()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a41195d6938e517464945473cc5074134),
[App::PropertyXLink.setSubName()](../../d2/de2/classApp_1_1PropertyXLink.html#a576472096f84a71a74169e29ac6eb41b),
[App::PropertyXLink.setSubValues()](../../d2/de2/classApp_1_1PropertyXLink.html#ab317a05477f1ee776d1c4f765b70b1cd),
[App::PropertyXLink.setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a0aee61347281a5a90b7553e4d5c76b47),
[App::PropertyLinkSub.setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a448d3ecccc89f3da177ecd35eb92b248),
[App::PropertyXLinkSubList.setValue()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a3800e6c7a9eeb19855cfd1fe3febafa1),
[Sketcher::PropertyConstraintList.setValues()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#ab633bd319a1005d72c5fd638c865c13c),
[App::PropertyXLinkSubList.setValues()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a82210325a201b5eff6a3107024a698cb),
[App::PropertyLinkSubList.setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a80bd9cad2a6b8ee3f81125eba1c82e06),
[Part::PropertyGeometryList.setValues()](../../db/dca/classPart_1_1PropertyGeometryList.html#a15044e8f3bad6a86fc71956c9dce8762),
[Sketcher::SketchObject.setVirtualSpace()](../../d9/dad/classSketcher_1_1SketchObject.html#a145ffeddf548de6f7376a1f1a180d272),
[App::ObjectIdentifier::Component.SimpleComponent()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a7d80f658926d2e4b5dba9f35de242b75),
[App::ObjectIdentifier.SimpleComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a771b13f5d53fb64d967b57d27bfb718d),
[Gui::SelectionSingleton.slotDeletedObject()](../../d4/dca/classGui_1_1SelectionSingleton.html#a71d83e67e4de7417667efa24dc4c7ed5),
[TechDraw::ShapeExtractor.stripInfiniteShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#aa9cc8fac9131902ea6cfb9b8e51361b9),
[App::LinkBaseExtension.syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f),
[nlohmann::detail.to_json()](../../dc/df0/namespacenlohmann_1_1detail.html#a4aa1ca6b7c61bf19d1f30ea5b669f68e),
[Sketcher::SketchObject.toggleActive()](../../d9/dad/classSketcher_1_1SketchObject.html#a21af5660e155b4d7f2185bab7c31eb74),
[Sketcher::SketchObject.toggleConstruction()](../../d9/dad/classSketcher_1_1SketchObject.html#aa258782e7f208a5e28f0b39937d62f5f),
[Sketcher::SketchObject.toggleDriving()](../../d9/dad/classSketcher_1_1SketchObject.html#a5127694bcd6a2f20e35545e6d374c026),
[Sketcher::SketchObject.toggleVirtualSpace()](../../d9/dad/classSketcher_1_1SketchObject.html#a3a0a4982245d089c659ccdf0bf2cb2e5),
[Sketcher::SketchObject.transferConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a8d36181fad0a534e8dd7b5e74e84ea2f),
[Sketcher::SketchObject.transferFilletConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a618d3720b583b93238a18fec74007377),
[Sketcher::SketchObject.trim()](../../d9/dad/classSketcher_1_1SketchObject.html#a55c244742ef90c7bc339e6c0285e2027),
[App::PropertyLinkBase.tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[App::PropertyLinkBase.tryReplaceLinkSubs()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc),
[App::PropertyXLinkContainer.updateDeps()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a83acea46b0d063043f43d99de26dfe29),
[Sketcher::Sketch.updateExtension()](../../d9/d9b/classSketcher_1_1Sketch.html#a5e4d8aa678c9d9837a6e3da48a47056e),
[App::PropertyLinkBase.updateLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a352aa734ca82348678cc710b1eead0ef),
[Gui::SelectionSingleton.updateSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a6bbc09a0201b9d16f2451271893f7067),
[Sketcher::SketchObject.updateSolverExtension()](../../d9/dad/classSketcher_1_1SketchObject.html#a67d3c8789e2471adbd30dc62ee3671f5),
[App::PropertyXLinkSubList.upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
[Sketcher::SketchObject.validateConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a74d7cf794e5f4de558e5800d6aa9ee46),
[Sketcher::SketchObject.validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9),
and
[Gui::ViewProviderT.ViewProviderT()](../../df/d5a/classGui_1_1ViewProviderT.html#ac3accb4bb9c8d194101315d697ca22e0).

## ◆ move_edge()

def draftfunctions.move.move_edge  | ( |  | _object_ ,   
---|---|---|---  
|  |  | _edge_index_ ,   
|  |  | _vector_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.move.moveVertex](../../d2/d57/group__draftfunctions.html#ga6344bf6a3359333cf20fac7726b718c4).

## ◆ move_vertex()

def draftfunctions.move.move_vertex  | ( |  | _object_ ,   
---|---|---|---  
|  |  | _vertex_index_ ,   
|  |  | _vector_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

## ◆ offset()

def draftfunctions.offset.offset  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _delta_ ,   
|  |  | _copy_ = `False`,   
|  |  | _bind_ = `False`,   
|  |  | _sym_ = `False`,   
|  |  | _occ_ = `False`  
| ) | |   
      
    
    offset(object,delta,[copymode],[bind])
    
    Offset the given wire by applying the given delta Vector to its first
    vertex.
    
    Parameters
    ----------
    obj :
    
    delta : Base.Vector or list of Base.Vector
        If offsetting a BSpline, the delta must not be a Vector but a list
        of Vectors, one for each node of the spline.
    
    copy : bool
        If copymode is True, another object is created, otherwise the same
        object gets offsetted.
    
    copy : bool
        If bind is True, and provided the wire is open, the original
        and the offset wires will be bound by their endpoints, forming a face.
    
    sym : bool
        if sym is True, bind must be true too, and the offset is made on both
        sides, the total width being the given delta length.
    

References
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1).

Referenced by
[geoff_geometry::SpanVertex.Add()](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#ae7b34f81a45d3be1bbf99a39d1302869),
[geoff_geometry::SpanVertex.AddSpanID()](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#a5b60496cd4670562beb836e0142c955b),
[e57::BitpackIntegerEncoder< RegisterT
>.BitpackIntegerEncoder()](../../d0/db0/classe57_1_1BitpackIntegerEncoder.html#a523224c647a31c4e88780ab7d8ecd154),
[PartDesignGui::TaskExtrudeParameters.changeEvent()](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#a0b700d673793ec0abe46c0799db30494),
[geoff_geometry.CPTOL()](../../de/d5d/namespacegeoff__geometry.html#a27c7ba9f7d80266e47e9e3bd71adcee8),
[TechDrawGui::QGIFace.dashRemain()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#aeb8b88116d46993d4ba7ae274e8b12ed),
[AdaptivePath::Adaptive2d.Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
[geoff_geometry::SpanVertex.Get()](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#a07ddcb13cd56ed4b2ae26cd5c3bb8262),
[geoff_geometry::Kurve.Get()](../../d3/ddd/classgeoff__geometry_1_1Kurve.html#a8050872ff4d4a4a149899d1b4c8654b4),
[Spreadsheet::Sheet.getColumn()](../../d0/da8/classSpreadsheet_1_1Sheet.html#aaa23efb9abee897e4bbb7a07a0255769),
[geoff_geometry::SpanVertex.GetIndex()](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#aea25a82476f22229961fc54e4c42a14c),
[TechDraw::DrawViewBalloon.getOriginOffset()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a27905f37307418edb8330d322a83fc40),
[Spreadsheet::Sheet.getRow()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1a8e1ef690173ad142dfbaf0d96da3fb),
[geoff_geometry::SpanVertex.GetSpanID()](../../de/dc5/classgeoff__geometry_1_1SpanVertex.html#adb4ce4e6d8d58671a364db5b4fa470d1),
[PartDesign::PolarPattern.getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[geoff_geometry::Span.Offset()](../../d9/d68/classgeoff__geometry_1_1Span.html#a4ee832d19cdc8b89fe66779e613277ff),
[TechDrawGui::QGIFace.offsetDash()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#a3d9968904c380714a084c4f9ac7c49ce),
[geoff_geometry::Kurve.OffsetMethod1()](../../d3/ddd/classgeoff__geometry_1_1Kurve.html#aafcb3b53aab8b315807445a26d004dd0),
[PartGui::OffsetWidget.OffsetWidget()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ae7bb4b5d03b3c78115b8e3943bb318d1),
[e57::BufferView.seek()](../../d0/d93/classe57_1_1BufferView.html#a856151bb984ecb3c309aae4f445acc83),
[e57::CheckedFile.seek()](../../da/d5b/classe57_1_1CheckedFile.html#aeb789d2de5cafd9856cf52e67ff61a0b),
[zipios::ZipCDirEntry.setLocalHeaderOffset()](../../dd/d8d/classzipios_1_1ZipCDirEntry.html#a40a00c9d83cfd4ceb6166bc6f7428fd0),
and
[e57::SourceDestBufferImpl.setNextInt64()](../../d2/dcb/classe57_1_1SourceDestBufferImpl.html#a52271b6baab250dab2a41a4d3f3a9aeb).

## ◆ polarArray()

def draftfunctions.array.polarArray  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _center_ ,   
|  |  | _angle_ ,   
|  |  | _num_  
| ) | |   
  
Referenced by
[draftfunctions.array.array()](../../d2/d57/group__draftfunctions.html#gadf79960ae21167271a07cc16e0a58027).

## ◆ rectArray()

def draftfunctions.array.rectArray  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _xvector_ ,   
|  |  | _yvector_ ,   
|  |  | _xnum_ ,   
|  |  | _ynum_  
| ) | |   
  
Referenced by
[draftfunctions.array.array()](../../d2/d57/group__draftfunctions.html#gadf79960ae21167271a07cc16e0a58027).

## ◆ rectArray2()

def draftfunctions.array.rectArray2  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _xvector_ ,   
|  |  | _yvector_ ,   
|  |  | _zvector_ ,   
|  |  | _xnum_ ,   
|  |  | _ynum_ ,   
|  |  | _znum_  
| ) | |   
  
Referenced by
[draftfunctions.array.array()](../../d2/d57/group__draftfunctions.html#gadf79960ae21167271a07cc16e0a58027).

## ◆ rotate()

def draftfunctions.rotate.rotate  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _angle_ ,   
|  |  | _center_ = `App.Vector(0,0,0)`,   
|  |  | _axis_ = `App.Vector(0,0,1)`,   
|  |  | _copy_ = `False`  
| ) | |   
      
    
    rotate(objects,angle,[center,axis,copy])
    
    Rotates the objects contained in objects (that can be a list of objects
    or an object) of the given angle (in degrees) around the center, using
    axis as a rotation axis.
    
    Parameters
    ----------
    objectlist : list
    
    angle : list
    
    center : Base.Vector
    
    axis : Base.Vector
        If axis is omitted, the rotation will be around the vertical Z axis.
    
    copy : bool
        If copy is True, the actual objects are not moved, but copies
        are created instead.
    
    Return
    ----------
    The objects (or their copies) are returned.
    

References
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1),
and
[DraftVecUtils.tup()](../../dc/dc3/group__DRAFTVECUTILS.html#gada8f1f6ff2e9aca9a3ff9384ae3bbd27).

Referenced by
[TechDraw::CenterLine.calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine.calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDraw::CenterLine.calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[TechDraw::CenterLine.calcEndPointsNoRef()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ac096a3e174023e9aa7efaab88e4df343),
and
[geoff_geometry::Matrix.Rotate()](../../d6/d56/classgeoff__geometry_1_1Matrix.html#a4fc9736ebbb9ceecdb70fcf84a49bd28).

## ◆ rotate_edge()

def draftfunctions.rotate.rotate_edge  | ( |  | _object_ ,   
---|---|---|---  
|  |  | _edge_index_ ,   
|  |  | _angle_ ,   
|  |  | _center_ ,   
|  |  | _axis_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.rotate.rotateVertex](../../d2/d57/group__draftfunctions.html#ga5a7795065a46af4f48ba7542ae93b16e).

## ◆ rotate_vector_from_center()

def draftfunctions.rotate.rotate_vector_from_center  | ( |  | _vector_ ,   
---|---|---|---  
|  |  | _angle_ ,   
|  |  | _axis_ ,   
|  |  | _center_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1).

Referenced by
[draftfunctions.rotate.copy_rotated_edge()](../../d2/d57/group__draftfunctions.html#gac94fa90639a8f9b3018079697a984991),
and
[draftfunctions.rotate.rotate_vertex()](../../d2/d57/group__draftfunctions.html#gaf6c1a6aebf12f4e79a5766e3accfc9a0).

## ◆ rotate_vertex()

def draftfunctions.rotate.rotate_vertex  | ( |  | _object_ ,   
---|---|---|---  
|  |  | _vertex_index_ ,   
|  |  | _angle_ ,   
|  |  | _center_ ,   
|  |  | _axis_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.rotate.rotate_vector_from_center()](../../d2/d57/group__draftfunctions.html#ga183986f7cd09d522dd82a38b522c2353).

## ◆ scale()

def draftfunctions.scale.scale  | ( |  | _objectslist_ ,   
---|---|---|---  
|  |  | _scale_ = `App.Vector(1,1,1)`,   
|  |  | _center_ = `App.Vector(0,0,0)`,   
|  |  | _copy_ = `False`  
| ) | |   
      
    
    scale(objects, scale, [center], copy)
    
    Scales the objects contained in objects (that can be a list of objects or
    an object) of the given  around given center.
    
    Parameters
    ----------
    objectlist : list
    
    scale : Base.Vector
        Scale factors defined by a given vector (in X, Y, Z directions).
    
    objectlist : Base.Vector
        Center of the scale operation.
    
    copy : bool
        If copy is True, the actual objects are not scaled, but copies
        are created instead.
    
    Return
    ----------
    The objects (or their copies) are returned.
    

References
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[draftfunctions.scale.scale_vertex()](../../d2/d57/group__draftfunctions.html#ga5385cccd74ea9fb4238c0ca17999b18c).

Referenced by [e57::BitpackIntegerEncoder< RegisterT
>.BitpackIntegerEncoder()](../../d0/db0/classe57_1_1BitpackIntegerEncoder.html#a523224c647a31c4e88780ab7d8ecd154),
[Gui::NavigationStyle.boxZoom()](../../d2/d1c/classGui_1_1NavigationStyle.html#ade23e825d12376624eca886517e55737),
[TechDraw::CenterLine.calcEndPoints()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a34df15a8a959516ecc49512c3ec5a73c),
[TechDraw::CenterLine.calcEndPoints2Lines()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a54d1cc5e3f8aa8923c2c28bdbe25c262),
[TechDraw::CenterLine.calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[TechDraw::CenterLine.calcEndPointsNoRef()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ac096a3e174023e9aa7efaab88e4df343),
[TechDrawGui::TaskRichAnno.calcTextStartPos()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae1abe86bd3bc257ecd36cc0212763a37),
[TechDrawGui::QGCustomImage.centerAt()](../../d5/d80/classTechDrawGui_1_1QGCustomImage.html#a512f7a68f6a5f33530afd4645de3df3c),
[TechDrawGui::QGCustomSvg.centerAt()](../../d4/d3c/classTechDrawGui_1_1QGCustomSvg.html#a15be98398781ce5ca13cf164093055af),
[StdMeshers_Regular_1D.computeInternalParameters()](../../df/d00/classStdMeshers__Regular__1D.html#a454d87137ba61dc2b61d5d35f3fe8de7),
[TechDrawGui::QGILeaderLine.draw()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab20089120a1417e5a55af3e140e7acbd),
[TechDrawGui::QGIViewBalloon.drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[TechDrawGui::QGIViewPart.drawMatting()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a8ee1ae8bd3c4894661e9911784534607),
[TechDrawGui::QGIViewPart.drawSectionLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a513e571f325b7c7cac09bdec0d1c512d),
[TechDraw::DrawViewDimExtent.execute()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[DrawingGui::OrthoViews.get_configs()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#acbd3de6fa94b9f7fed2a9809ef7bb9a2),
[TechDrawGui::TaskDetail.getAnchorScene()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ac47e200bf1be3381e59b3c6c4610494d),
[DrawingGui::orthoview.getScale()](../../db/df8/classDrawingGui_1_1orthoview.html#a9883f3bdebf677ddfaefaa132b6a9ec1),
[Gui::AxisOrigin.getScale()](../../dd/de4/classGui_1_1AxisOrigin.html#acf4e5d0d7f2f01f0600653118f74cb53),
[SketcherGui::ViewProviderSketch.getScaleFactor()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a98a854b6d2621eb48c51614b4cea53df),
[Gui::SoAutoZoomTranslation.getScaleFactor()](../../d6/d91/classGui_1_1SoAutoZoomTranslation.html#a5db6d50fe9266d31701f616c02e10523),
[SketcherGui::SoZoomTranslation.getScaleFactor()](../../d2/d20/classSketcherGui_1_1SoZoomTranslation.html#ab57ca8a4da9467471afcd9acf760031f),
[SketcherGui::SoDatumLabel.GLRender()](../../d3/d9d/classSketcherGui_1_1SoDatumLabel.html#a4852d28cbd11ff9224b8382c455cbe84),
[TechDrawGui::QGCustomImage.imageSize()](../../d5/d80/classTechDrawGui_1_1QGCustomImage.html#a355e147cbe20053fa392c36ed7bd41d0),
[SMESH_Pattern.Load()](../../d0/d7d/classSMESH__Pattern.html#aada1481358a8eedfa7a175da392b9308),
[TechDraw::DrawGeomHatch.makeEdgeOverlay()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#ad42d700267fb44056f1c72515659170c),
[TechDrawGui::TaskCosVertex.onTrackerFinished()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a70cc99622328e6c5e42c84caec735981),
[TechDrawGui::TaskLeaderLine.onTrackerFinished()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a3834c86229e7732145d671a0546087ea),
[Gui::NavigationStyle.processMotionEvent()](../../d2/d1c/classGui_1_1NavigationStyle.html#a9608fd3806bca107ca1f98352b25b63a),
[e57::ReaderImpl.ReadData3D()](../../df/d86/classe57_1_1ReaderImpl.html#a90fd267ad0f1044368258120935286ad),
[TechDraw::DrawViewDimension.saveArrowPositions()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ac705aa8a3de64d63e4d07323ae6f23ea),
[Base::Matrix4D.scale()](../../d5/db4/classBase_1_1Matrix4D.html#aa0838e1c628e3f405a83904679acec56),
[Base::Rotation.setValue()](../../d4/d18/classBase_1_1Rotation.html#a62c0b4012cb383de60d0e4a225c39550),
[AdaptivePath.SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962),
[Path::Command.toGCode()](../../d7/d2e/classPath_1_1Command.html#ac42dc79f20af29520dddda80a0a87e0a),
[geoff_geometry::Circle.Transform()](../../d7/dec/classgeoff__geometry_1_1Circle.html#aa9c96a90d069b0aec2d402dfc2c43229),
[RotTransDragger.valueChangedCB()](../../dd/d12/classRotTransDragger.html#afe82092011c23d0855706d1959be8392),
and
[DrawingGui::SvgView.wheelEvent()](../../dd/d77/classDrawingGui_1_1SvgView.html#a209449ea76bcd47effcab14a59f0707e).

## ◆ scale_edge()

def draftfunctions.scale.scale_edge  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _edge_index_ ,   
|  |  | _scale_ ,   
|  |  | _center_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.scale.scale_vertex()](../../d2/d57/group__draftfunctions.html#ga5385cccd74ea9fb4238c0ca17999b18c).

## ◆ scale_vector_from_center()

def draftfunctions.scale.scale_vector_from_center  | ( |  | _vector_ ,   
---|---|---|---  
|  |  | _scale_ ,   
|  |  | _center_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

Referenced by
[draftfunctions.scale.copy_scaled_edge()](../../d2/d57/group__draftfunctions.html#gacfa4a432df41da7183fa4d67082afbe4),
and
[draftfunctions.scale.scale_vertex()](../../d2/d57/group__draftfunctions.html#ga5385cccd74ea9fb4238c0ca17999b18c).

## ◆ scale_vertex()

def draftfunctions.scale.scale_vertex  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _vertex_index_ ,   
|  |  | _scale_ ,   
|  |  | _center_  
| ) | |   
      
    
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    

References
[draftfunctions.scale.scale_vector_from_center()](../../d2/d57/group__draftfunctions.html#ga2cd4c3d5877a9514b471589548d292a7).

Referenced by
[draftfunctions.scale.scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10),
and
[draftfunctions.scale.scale_edge()](../../d2/d57/group__draftfunctions.html#gaf6f6d2fc2c6268c37e18418710dda5c5).

## ◆ split()

def draftfunctions.split.split  | ( |  | _wire_ ,   
---|---|---|---  
|  |  | _newPoint_ ,   
|  |  | _edgeIndex_  
| ) | |   
  
References
[draftfunctions.split.split_closed_wire()](../../d2/d57/group__draftfunctions.html#ga23c12c1c523cdb3f7209e0db692f373a),
and
[draftfunctions.split.split_open_wire()](../../d2/d57/group__draftfunctions.html#gafc191032e1c328346d1c042ed97c8002).

Referenced by
[Robot::Robot6Axis.readKinematic()](../../dc/d5f/classRobot_1_1Robot6Axis.html#af56737a00a0584143e73eebfb7ef48f1).

## ◆ split_closed_wire()

def draftfunctions.split.split_closed_wire  | ( |  | _wire_ ,   
---|---|---|---  
|  |  | _edgeIndex_  
| ) | |   
  
Referenced by
[draftfunctions.split.split()](../../d2/d57/group__draftfunctions.html#ga23d2785b69d3a2f6b9347d0e95515447).

## ◆ split_open_wire()

def draftfunctions.split.split_open_wire  | ( |  | _wire_ ,   
---|---|---|---  
|  |  | _newPoint_ ,   
|  |  | _edgeIndex_  
| ) | |   
  
Referenced by
[draftfunctions.split.split()](../../d2/d57/group__draftfunctions.html#ga23d2785b69d3a2f6b9347d0e95515447).

## ◆ upgrade()

def draftfunctions.upgrade.upgrade  | ( |  | _objects_ ,   
---|---|---|---  
|  |  | _delete_ = `False`,   
|  |  | _force_ = `None`  
| ) | |   
      
    
    Upgrade the given objects.
    
    This is a counterpart to `downgrade`.
    
    Parameters
    ----------
    objects: Part::Feature or list
        A single object to upgrade or a list
        containing various such objects.
    
    delete: bool, optional
        It defaults to `False`.
        If it is `True`, the old objects are deleted, and only the resulting
        object is kept.
    
    force: str, optional
        It defaults to `None`.
        Its value can be used to force a certain method of upgrading.
        It can be any of: `'makeCompound'`, `'closeGroupWires'`,
        `'makeSolid'`, `'closeWire'`, `'turnToParts'`, `'makeFusion'`,
        `'makeShell'`, `'makeFaces'`, `'draftify'`, `'joinFaces'`,
        `'makeSketchFace'`, `'makeWires'`.
    
    Returns
    -------
    tuple
        A tuple containing two lists, a list of new objects
        and a list of objects to be deleted.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    downgrade
    

References
[draftgeoutils.geometry.is_straight_line()](../../d9/dfd/group__draftgeoutils.html#gaca3c302955adc40b70eb1d12fc43c083).

## Variable Documentation

## ◆ copyMovedEdges

def draftfunctions.move.copyMovedEdges =
[copy_moved_edges](../../d2/d57/group__draftfunctions.html#ga73be57b46917993128fa3784697024d3)  
---  
  
## ◆ copyRotatedEdges

def draftfunctions.rotate.copyRotatedEdges =
[copy_rotated_edges](../../d2/d57/group__draftfunctions.html#gacd1c2653ca92dbad2c87bc0758f5ca28)  
---  
  
## ◆ copyScaledEdge

def draftfunctions.scale.copyScaledEdge =
[copy_scaled_edge](../../d2/d57/group__draftfunctions.html#gacfa4a432df41da7183fa4d67082afbe4)  
---  
  
## ◆ copyScaledEdges

def draftfunctions.scale.copyScaledEdges =
[copy_scaled_edges](../../d2/d57/group__draftfunctions.html#gac59d9b5d86c38c42b59625f7feef2a68)  
---  
  
## ◆ DraftGeomUtils

draftfunctions.draftify.DraftGeomUtils = lz.LazyLoader("DraftGeomUtils",
globals(), "DraftGeomUtils")  
---  
  
## ◆ joinTwoWires

def draftfunctions.join.joinTwoWires =
[join_two_wires](../../d2/d57/group__draftfunctions.html#ga8b7573fa746b69be82d73768bb04a557)  
---  
  
## ◆ joinWires

def draftfunctions.join.joinWires =
[join_wires](../../d2/d57/group__draftfunctions.html#ga5354f8b322314e22e3f93f7a54371858)  
---  
  
## ◆ moveEdge

def draftfunctions.move.moveEdge =
[move_edge](../../d2/d57/group__draftfunctions.html#gab30cec2f612e2ef4ffcbb924311a99a0)  
---  
  
## ◆ moveVertex

def draftfunctions.move.moveVertex =
[move_vertex](../../d2/d57/group__draftfunctions.html#gabf9889375ebf33577848f5fa2c2f4552)  
---  
  
Referenced by
[draftfunctions.move.move_edge()](../../d2/d57/group__draftfunctions.html#gab30cec2f612e2ef4ffcbb924311a99a0).

## ◆ Part

draftfunctions.draftify.Part = lz.LazyLoader("Part", globals(), "Part")  
---  
  
## ◆ rotateEdge

def draftfunctions.rotate.rotateEdge =
[rotate_edge](../../d2/d57/group__draftfunctions.html#gaf66ee29eea1d43bb3bc9a72a39306580)  
---  
  
## ◆ rotateVectorFromCenter

def draftfunctions.rotate.rotateVectorFromCenter =
[rotate_vector_from_center](../../d2/d57/group__draftfunctions.html#ga183986f7cd09d522dd82a38b522c2353)  
---  
  
## ◆ rotateVertex

def draftfunctions.rotate.rotateVertex =
[rotate_vertex](../../d2/d57/group__draftfunctions.html#gaf6c1a6aebf12f4e79a5766e3accfc9a0)  
---  
  
Referenced by
[draftfunctions.rotate.rotate_edge()](../../d2/d57/group__draftfunctions.html#gaf66ee29eea1d43bb3bc9a72a39306580).

## ◆ scaleEdge

def draftfunctions.scale.scaleEdge =
[scale_edge](../../d2/d57/group__draftfunctions.html#gaf6f6d2fc2c6268c37e18418710dda5c5)  
---  
  
## ◆ scaleVectorFromCenter

def draftfunctions.scale.scaleVectorFromCenter =
[scale_vector_from_center](../../d2/d57/group__draftfunctions.html#ga2cd4c3d5877a9514b471589548d292a7)  
---  
  
## ◆ scaleVertex

def draftfunctions.scale.scaleVertex =
[scale_vertex](../../d2/d57/group__draftfunctions.html#ga5385cccd74ea9fb4238c0ca17999b18c)  
---  
  
## ◆ splitClosedWire

def draftfunctions.split.splitClosedWire =
[split_closed_wire](../../d2/d57/group__draftfunctions.html#ga23c12c1c523cdb3f7209e0db692f373a)  
---  
  
## ◆ splitOpenWire

def draftfunctions.split.splitOpenWire =
[split_open_wire](../../d2/d57/group__draftfunctions.html#gafc191032e1c328346d1c042ed97c8002)  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

