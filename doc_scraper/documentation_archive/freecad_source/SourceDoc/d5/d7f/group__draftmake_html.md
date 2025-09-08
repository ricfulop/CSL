---
url: https://freecad.github.io/SourceDoc/d5/d7f/group__draftmake.html
scraped_at: 2025-09-08T14:52:01.944233
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Namespaces | Functions | Variables

draftmake

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Draft](../../d1/d35/group__DRAFT.html)

Modules with functions to create the custom scripted objects. More...

##  Namespaces  
  
---  
namespace | [make_arc_3points](../../d4/d51/namespacemake__arc__3points.html)  
| Provides functions to create Arc objects by using 3 points.  
  
namespace | [make_array](../../d5/dfa/namespacemake__array.html)  
| Provides functions to create Array objects.  
  
namespace | [make_bezcurve](../../d6/dbd/namespacemake__bezcurve.html)  
| Provides functions to create BezCurve objects.  
  
namespace | [make_block](../../d9/df0/namespacemake__block.html)  
| Provides functions to create Block objects.  
  
namespace | [make_bspline](../../df/dbf/namespacemake__bspline.html)  
| Provides functions to create BSpline objects.  
  
namespace | [make_circle](../../dd/d94/namespacemake__circle.html)  
| Provides functions to create [Circle](../../d8/d53/classCircle.html)
objects.  
  
namespace | [make_circulararray](../../d2/d32/namespacemake__circulararray.html)  
| Provides functions to create circular Array objects.  
  
namespace | [make_clone](../../d2/d1f/namespacemake__clone.html)  
| Provides functions to create Clone objects.  
  
namespace | [make_copy](../../dc/d69/namespacemake__copy.html)  
| Provides functions to create copies of objects.  
  
namespace | [make_dimension](../../d5/d6d/namespacemake__dimension.html)  
| Provides functions to create Linear or AngularDimension objects.  
  
namespace | [make_drawingview](../../de/d38/namespacemake__drawingview.html)  
| Provides functions to create DrawingView objects.  
  
namespace | [make_ellipse](../../d1/dc6/namespacemake__ellipse.html)  
| Provides functions to create Ellipse objects.  
  
namespace | [make_facebinder](../../d8/dd7/namespacemake__facebinder.html)  
| Provides functions to create Facebinder objects.  
  
namespace | [make_fillet](../../d7/d40/namespacemake__fillet.html)  
| Provides functions to create Fillet objects between two lines.  
  
namespace | [make_label](../../d5/d1a/namespacemake__label.html)  
| Provides functions to create Label objects.  
  
namespace | [make_layer](../../d4/db2/namespacemake__layer.html)  
| Provides functions to create Layer objects.  
  
namespace | [make_line](../../d6/db9/namespacemake__line.html)  
| Provides functions to create two-point Wire objects.  
  
namespace | [make_orthoarray](../../d1/d73/namespacemake__orthoarray.html)  
| Provides functions to create orthogonal 2D and 3D Arrays.  
  
namespace | [make_patharray](../../d4/db9/namespacemake__patharray.html)  
| Provides functions to create PathArray objects.  
  
namespace | [make_point](../../df/de9/namespacemake__point.html)  
| Provides functions to create [Point](../../dc/d4f/classPoint.html) objects.  
  
namespace | [make_pointarray](../../de/d6f/namespacemake__pointarray.html)  
| Provides functions to create PointArray objects.  
  
namespace | [make_polararray](../../d7/d92/namespacemake__polararray.html)  
| Provides functions to create polar Array objects.  
  
namespace | [make_polygon](../../d0/d4d/namespacemake__polygon.html)  
| Provides functions to create Polygon objects.  
  
namespace | [make_rectangle](../../d6/dc5/namespacemake__rectangle.html)  
| This module provides the code for [Draft](../../d4/d1a/namespaceDraft.html)
[make_rectangle](../../d6/dc5/namespacemake__rectangle.html "This module
provides the code for Draft make_rectangle function.") function.  
  
namespace | [make_shape2dview](../../d0/d3e/namespacemake__shape2dview.html)  
| Provides functions to create Shape2DView objects.  
  
namespace | [make_shapestring](../../d9/d48/namespacemake__shapestring.html)  
| Provides functions to create ShapeString objects.  
  
namespace | [make_sketch](../../da/d07/namespacemake__sketch.html)  
| Provides functions to create Sketch objects from
[Draft](../../d4/d1a/namespaceDraft.html) objects.  
  
namespace | [make_text](../../de/d96/namespacemake__text.html)  
| Provides functions to create Text objects.  
  
namespace | [make_wire](../../d5/d74/namespacemake__wire.html)  
| Provides functions to create multipoint Wire objects.  
  
namespace | [make_wpproxy](../../d3/d49/namespacemake__wpproxy.html)  
| Provides functions to create WorkingPlaneProxy objects.  
  
  
##  Functions  
  
---  
def | [draftmake.make_text.convert_draft_texts](../../d5/d7f/group__draftmake.html#ga6c2540ed08c8d3d7260500c5ba302762) (textslist=None)  
def | [draftmake.make_text.convertDraftTexts](../../d5/d7f/group__draftmake.html#ga0ec764744a07ab78818bc6725120bc62) (textslist=[])  
def | [draftmake.make_layer.get_layer_container](../../d5/d7f/group__draftmake.html#ga455220c5d2ce1ef7b98e5b3586accfb4) ()  
def | [draftmake.make_layer.getLayerContainer](../../d5/d7f/group__draftmake.html#gaaaa1a3be8af82b547a4634085ff165c9) ()  
def | [draftmake.make_dimension.make_angular_dimension](../../d5/d7f/group__draftmake.html#ga8a37a6cb68456be519d0760cfa21eec3) (center=App.Vector(0, 0, 0), angles=None, dim_line=App.Vector(10, 10, 0), normal=None)  
def | [draftmake.make_arc_3points.make_arc_3points](../../d5/d7f/group__draftmake.html#ga1bfea9a483fbd43c522eeace0d367bf9) (points, placement=None, face=False, support=None, map_mode="Deactivated", primitive=False)  
def | [draftmake.make_array.make_array](../../d5/d7f/group__draftmake.html#ga9ba986971c0a13c851edf604bdc46461) (base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)  
def | [draftmake.make_bezcurve.make_bezcurve](../../d5/d7f/group__draftmake.html#gac86f3f114342fc87447d73296bd01983) (pointslist, closed=False, placement=None, face=None, support=None, degree=None)  
def | [draftmake.make_block.make_block](../../d5/d7f/group__draftmake.html#ga31e0a402c1ca17e8355f911e9c17b868) (objectslist)  
def | [draftmake.make_bspline.make_bspline](../../d5/d7f/group__draftmake.html#gae17b8880a5cbd21e6d2d33006d6e6fa8) (pointslist, closed=False, placement=None, face=None, support=None)  
def | [draftmake.make_circle.make_circle](../../d5/d7f/group__draftmake.html#ga8010a7e29529e73931cd92c538291b37) (radius, placement=None, face=None, startangle=None, endangle=None, support=None)  
def | [draftmake.make_circulararray.make_circular_array](../../d5/d7f/group__draftmake.html#ga08ad7fd5f30051467cc0eb3105aeb233) (base_object, r_distance=100, tan_distance=50, number=3, symmetry=1, axis=App.Vector(0, 0, 1), center=App.Vector(0, 0, 0), use_link=True)  
def | [draftmake.make_clone.make_clone](../../d5/d7f/group__draftmake.html#gaf3c8bb728ae3b221d0bb75551441d7d2) (obj, delta=None, forcedraft=False)  
def | [draftmake.make_copy.make_copy](../../d5/d7f/group__draftmake.html#ga750bbbb32d9866ec99c54885e25106fb) (obj, force=None, reparent=False, simple_copy=False)  
def | [draftmake.make_dimension.make_dimension](../../d5/d7f/group__draftmake.html#ga8f30314f405bf41d43b3b88f32673557) (p1, p2, p3=None, p4=None)  
def | [draftmake.make_drawingview.make_drawing_view](../../d5/d7f/group__draftmake.html#ga3048804d3459bb898e632560ad59687f) (obj, page, lwmod=None, tmod=None, otherProjection=None)  
def | [draftmake.make_ellipse.make_ellipse](../../d5/d7f/group__draftmake.html#gac417e9391cb09d94d5213f4a80c6530e) (majradius, minradius, placement=None, face=None, support=None)  
def | [draftmake.make_facebinder.make_facebinder](../../d5/d7f/group__draftmake.html#ga278850e8b4a6e9ee4d07efbcfe3b4f8f) (selectionset, name="Facebinder")  
def | [draftmake.make_fillet.make_fillet](../../d5/d7f/group__draftmake.html#gaa8147f19ce895e817cd0dfd4f481f94b) (objs, radius=100, chamfer=False, delete=False)  
def | [draftmake.make_label.make_label](../../d5/d7f/group__draftmake.html#ga37b0335b2fb7c62a52973adac8bd5e49) (target_point=App.Vector(0, 0, 0), placement=App.Vector(30, 30, 0), target_object=None, subelements=None, label_type="Custom", custom_text="Label", direction="Horizontal", distance=-10, points=None)  
def | [draftmake.make_layer.make_layer](../../d5/d7f/group__draftmake.html#ga0fe0767f646a6dbd0e6d39fdb8ba5f9c) (name=None, line_color=None, shape_color=None, line_width=2.0, draw_style="Solid", transparency=0)  
def | [draftmake.make_line.make_line](../../d5/d7f/group__draftmake.html#ga84268745b00f160b3e33476e21f1bef6) (first_param, last_param=None)  
def | [draftmake.make_dimension.make_linear_dimension](../../d5/d7f/group__draftmake.html#ga88dfef93f94d642e4ed11d49602f2154) (p1, p2, dim_line=None)  
def | [draftmake.make_dimension.make_linear_dimension_obj](../../d5/d7f/group__draftmake.html#ga356340565c645f30b44ee0850cfabbd5) (edge_object, i1=1, i2=2, dim_line=None)  
def | [draftmake.make_orthoarray.make_ortho_array](../../d5/d7f/group__draftmake.html#ga5a89f3570166a65608f68e429d7e333a) (base_object, v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10), n_x=2, n_y=2, n_z=1, use_link=True)  
def | [draftmake.make_orthoarray.make_ortho_array2d](../../d5/d7f/group__draftmake.html#ga0ecfdfae965604647a629fec9eceacfb) (base_object, v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), n_x=2, n_y=2, use_link=True)  
def | [draftmake.make_patharray.make_path_array](../../d5/d7f/group__draftmake.html#gad515633e5d4a8cbeb79a5ffd09f8b438) (base_object, path_object, count=4, extra=App.Vector(0, 0, 0), subelements=None, align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0), force_vertical=False, vertical_vector=App.Vector(0, 0, 1), use_link=True)  
def | [draftmake.make_patharray.make_path_twisted_array](../../d5/d7f/group__draftmake.html#ga618ffac3e3eb6a996aec128d4d941a58) (base_object, path_object, count=15, rot_factor=0.25, use_link=True)  
def | [draftmake.make_point.make_point](../../d5/d7f/group__draftmake.html#ga94d6bea3b61d351b732fa1251b457c30) (X=0, Y=0, Z=0, color=None, name="Point", point_size=5)  
def | [draftmake.make_pointarray.make_point_array](../../d5/d7f/group__draftmake.html#ga90c6d9fd96802f5d39c190005c119660) (base_object, point_object, extra=None, use_link=True)  
def | [draftmake.make_polararray.make_polar_array](../../d5/d7f/group__draftmake.html#ga9d22a1b896188df054a05541be890f12) (base_object, number=5, angle=360, center=App.Vector(0, 0, 0), use_link=True)  
def | [draftmake.make_polygon.make_polygon](../../d5/d7f/group__draftmake.html#ga087c000b1db0e3cac0785b367c341438) (nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)  
def | [draftmake.make_dimension.make_radial_dimension_obj](../../d5/d7f/group__draftmake.html#gaad63b661e6b8c58118304c0cb3062fb3) (edge_object, index=1, mode="radius", dim_line=None)  
def | [draftmake.make_orthoarray.make_rect_array](../../d5/d7f/group__draftmake.html#gac4fff292a6b44371b497fb4bbdcee35f) (base_object, d_x=10, d_y=10, d_z=10, n_x=2, n_y=2, n_z=1, use_link=True)  
def | [draftmake.make_orthoarray.make_rect_array2d](../../d5/d7f/group__draftmake.html#ga6e73a1cf376526d3aa345b68d1cba54f) (base_object, d_x=10, d_y=10, n_x=2, n_y=2, use_link=True)  
def | [draftmake.make_rectangle.make_rectangle](../../d5/d7f/group__draftmake.html#ga49a72193cb54e734871a96fb23ed360d) (length, height=0, placement=None, face=None, support=None)  
def | [draftmake.make_shape2dview.make_shape2dview](../../d5/d7f/group__draftmake.html#ga24d4bda57265196059d94eb35fd9140e) (baseobj, projectionVector=None, facenumbers=[])  
def | [draftmake.make_shapestring.make_shapestring](../../d5/d7f/group__draftmake.html#gafa8400a76d9dc03ae691b0f532d1ff72) (String, FontFile, Size=100, Tracking=0)  
def | [draftmake.make_sketch.make_sketch](../../d5/d7f/group__draftmake.html#gaaf5211b1c0c5f62d13897195ec2d1e6b) (objects_list, autoconstraints=False, addTo=None, delete=False, name="Sketch", radiusPrecision=-1, tol=1e-3)  
def | [draftmake.make_text.make_text](../../d5/d7f/group__draftmake.html#ga52973a85f9ac210d43f4162ab895809c) (string, placement=None, screen=False)  
def | [draftmake.make_wire.make_wire](../../d5/d7f/group__draftmake.html#ga1a8f33557281f53792c6e201edc6f36c) (pointslist, closed=False, placement=None, face=None, support=None, bs2wire=False)  
def | [draftmake.make_wpproxy.make_workingplaneproxy](../../d5/d7f/group__draftmake.html#gaaf46f35e0f52d2bfc88541c5c3c097c4) (placement)  
def | [draftmake.make_dimension.makeAngularDimension](../../d5/d7f/group__draftmake.html#ga77542e026ce72bf7790c0efb20c0ac08) (center, angles, p3, normal=None)  
def | [draftmake.make_array.makeArray](../../d5/d7f/group__draftmake.html#gad494dbca880ff38a77d0a034168a9623) (baseobject, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, name="Array", use_link=False)  
def | [draftmake.make_dimension.makeDimension](../../d5/d7f/group__draftmake.html#gac97d62e2909df825462b2308ece9c94d) (p1, p2, p3=None, p4=None)  
def | [draftmake.make_label.makeLabel](../../d5/d7f/group__draftmake.html#ga6cd2e1e0230302cc176c3cd6f9460abb) (targetpoint=None, target=None, direction=None, distance=None, labeltype=None, placement=None)  
def | [draftmake.make_layer.makeLayer](../../d5/d7f/group__draftmake.html#gad489d054cd1baebc31e5dc637a8777d8) (name=None, linecolor=None, drawstyle=None, shapecolor=None, transparency=None)  
def | [draftmake.make_patharray.makePathArray](../../d5/d7f/group__draftmake.html#ga67f067adb8d096afe5d6dcd616facb2f) (baseobject, pathobject, count, xlate=None, align=False, pathobjsubs=[], use_link=False)  
def | [draftmake.make_pointarray.makePointArray](../../d5/d7f/group__draftmake.html#gaadbed89ef29e6f261fb9f33ab94814ea) (base, ptlst)  
def | [draftmake.make_text.makeText](../../d5/d7f/group__draftmake.html#ga35bf9de0ba32134b91bc630ffd1a88df) (stringlist, point=App.Vector(0, 0, 0), screen=False)  
  
##  Variables  
  
---  
|
[draftmake.make_clone.clone](../../d5/d7f/group__draftmake.html#ga2ea88076151455eec7167f2db9de0905)
=
[make_clone](../../d5/d7f/group__draftmake.html#gaf3c8bb728ae3b221d0bb75551441d7d2)  
|
[draftmake.make_bezcurve.makeBezCurve](../../d5/d7f/group__draftmake.html#ga695c51cb94dbcb2b9897ac78db6aed5d)
=
[make_bezcurve](../../d5/d7f/group__draftmake.html#gac86f3f114342fc87447d73296bd01983)  
|
[draftmake.make_block.makeBlock](../../d5/d7f/group__draftmake.html#ga68c6b4285e6be8a4a2063fa4fb0f6c3b)
=
[make_block](../../d5/d7f/group__draftmake.html#ga31e0a402c1ca17e8355f911e9c17b868)  
|
[draftmake.make_bspline.makeBSpline](../../d5/d7f/group__draftmake.html#gac721bcf77f8bfb6aa837d04302750bfb)
=
[make_bspline](../../d5/d7f/group__draftmake.html#gae17b8880a5cbd21e6d2d33006d6e6fa8)  
|
[draftmake.make_circle.makeCircle](../../d5/d7f/group__draftmake.html#gaf865fcca329d8fe830712cd4b373e4c2)
=
[make_circle](../../d5/d7f/group__draftmake.html#ga8010a7e29529e73931cd92c538291b37)  
def | [draftmake.make_drawingview.makeDrawingView](../../d5/d7f/group__draftmake.html#gad4b55161bc380f40bbe3bd61a89b6ff6) = [make_drawing_view](../../d5/d7f/group__draftmake.html#ga3048804d3459bb898e632560ad59687f)  
|
[draftmake.make_ellipse.makeEllipse](../../d5/d7f/group__draftmake.html#ga7bd14a7c5925eae9d25f9ce0fe2e2ac7)
=
[make_ellipse](../../d5/d7f/group__draftmake.html#gac417e9391cb09d94d5213f4a80c6530e)  
|
[draftmake.make_facebinder.makeFacebinder](../../d5/d7f/group__draftmake.html#ga3fd639a053b38a6d8300beac77ae79b4)
=
[make_facebinder](../../d5/d7f/group__draftmake.html#ga278850e8b4a6e9ee4d07efbcfe3b4f8f)  
|
[draftmake.make_line.makeLine](../../d5/d7f/group__draftmake.html#ga2f9bb9203dd028afe44a769648a613c1)
=
[make_line](../../d5/d7f/group__draftmake.html#ga84268745b00f160b3e33476e21f1bef6)  
|
[draftmake.make_point.makePoint](../../d5/d7f/group__draftmake.html#ga96f03ef79d8600c9f0933617dc999cc5)
=
[make_point](../../d5/d7f/group__draftmake.html#ga94d6bea3b61d351b732fa1251b457c30)  
|
[draftmake.make_polygon.makePolygon](../../d5/d7f/group__draftmake.html#ga06c3352643ebd03dc8bef1bd689c120e)
=
[make_polygon](../../d5/d7f/group__draftmake.html#ga087c000b1db0e3cac0785b367c341438)  
|
[draftmake.make_rectangle.makeRectangle](../../d5/d7f/group__draftmake.html#gaa8ac34e9941baa9d76b5bb4aa0a7d7af)
=
[make_rectangle](../../d5/d7f/group__draftmake.html#ga49a72193cb54e734871a96fb23ed360d)  
|
[draftmake.make_shape2dview.makeShape2DView](../../d5/d7f/group__draftmake.html#ga6c89fe6cce6812061f316a5f2f680c33)
=
[make_shape2dview](../../d5/d7f/group__draftmake.html#ga24d4bda57265196059d94eb35fd9140e)  
|
[draftmake.make_shapestring.makeShapeString](../../d5/d7f/group__draftmake.html#gaf576da9e17922b723812ce57316017ca)
=
[make_shapestring](../../d5/d7f/group__draftmake.html#gafa8400a76d9dc03ae691b0f532d1ff72)  
|
[draftmake.make_sketch.makeSketch](../../d5/d7f/group__draftmake.html#gabc51be126cf3c4ffa30010545be926bc)
=
[make_sketch](../../d5/d7f/group__draftmake.html#gaaf5211b1c0c5f62d13897195ec2d1e6b)  
|
[draftmake.make_wire.makeWire](../../d5/d7f/group__draftmake.html#gabf54f92c33dfce8f34ed29eac3e71312)
=
[make_wire](../../d5/d7f/group__draftmake.html#ga1a8f33557281f53792c6e201edc6f36c)  
def | [draftmake.make_wpproxy.makeWorkingPlaneProxy](../../d5/d7f/group__draftmake.html#gaf81ce638145aa048b69e46eca079f30b) = [make_workingplaneproxy](../../d5/d7f/group__draftmake.html#gaaf46f35e0f52d2bfc88541c5c3c097c4)  
|
[draftmake.make_layer.view_group](../../d5/d7f/group__draftmake.html#ga52463183610ad0645ef2760da8d4ff0b)
= App.ParamGet("User parameter:BaseApp/Preferences/View")  
  
## Detailed Description

Modules with functions to create the custom scripted objects.

## Function Documentation

## ◆ convert_draft_texts()

def draftmake.make_text.convert_draft_texts  | ( |  | _textslist_ = `None`| ) |   
---|---|---|---|---|---  
      
    
    Convert the given Annotation to a Draft text.
    
    In the past, the `Draft Text` object didn't exist; text objects
    were of type `App::Annotation`. This function was introduced
    to convert those older objects to a `Draft Text` scripted object.
    
    This function was already present at splitting time during v0.19.
    
    Parameters
    ----------
    textslist: list of objects, optional
        It defaults to `None`.
        A list containing `App::Annotation` objects or a single of these
        objects.
        If it is `None` it will convert all objects in the current document.
    

Referenced by
[draftmake.make_text.convertDraftTexts()](../../d5/d7f/group__draftmake.html#ga0ec764744a07ab78818bc6725120bc62).

## ◆ convertDraftTexts()

def draftmake.make_text.convertDraftTexts  | ( |  | _textslist_ = `[]`| ) |   
---|---|---|---|---|---  
      
    
    Convert Text. DEPRECATED. Use 'convert_draft_texts'.

References
[draftmake.make_text.convert_draft_texts()](../../d5/d7f/group__draftmake.html#ga6c2540ed08c8d3d7260500c5ba302762).

## ◆ get_layer_container()

def draftmake.make_layer.get_layer_container  | ( | | ) |   
---|---|---|---|---  
      
    
    Return a group object to put layers in.
    
    Returns
    -------
    App::DocumentObjectGroupPython
        The existing group object named `'LayerContainer'`
        of type `LayerContainer`.
        If it doesn't exist it will create it with this default Name.
    

Referenced by
[draftmake.make_layer.getLayerContainer()](../../d5/d7f/group__draftmake.html#gaaaa1a3be8af82b547a4634085ff165c9),
and
[draftmake.make_layer.make_layer()](../../d5/d7f/group__draftmake.html#ga0fe0767f646a6dbd0e6d39fdb8ba5f9c).

## ◆ getLayerContainer()

def draftmake.make_layer.getLayerContainer  | ( | | ) |   
---|---|---|---|---  
      
    
    Get the Layer container. DEPRECATED. Use 'get_layer_container'.

References
[draftmake.make_layer.get_layer_container()](../../d5/d7f/group__draftmake.html#ga455220c5d2ce1ef7b98e5b3586accfb4).

## ◆ make_angular_dimension()

def draftmake.make_dimension.make_angular_dimension  | ( |  | _center_ = `App.Vector(0, 0, 0)`,   
---|---|---|---  
|  |  | _angles_ = `None`,   
|  |  | _dim_line_ = `App.Vector(10, 10, 0)`,   
|  |  | _normal_ = `None`  
| ) | |   
      
    
    Create an angular dimension from the given center and angles.
    
    Parameters
    ----------
    center: Base::Vector3, optional
        It defaults to the origin `Vector(0, 0, 0)`.
        Center of the dimension line, which is a circular arc.
    
    angles: list of two floats, optional
        It defaults to `[0, 90]`.
        It is a list of two angles, given in degrees, that determine
        the aperture of the dimension line, that is, of the circular arc.
        It is drawn counter-clockwise.
        ::
            angles = [0 90]
            angles = [330 60]  # the arc crosses the X axis
            angles = [-30 60]  # same angle
    
    dim_line: Base::Vector3, optional
        It defaults to `Vector(10, 10, 0)`.
        This is a point through which the extension of the dimension line
        will pass. This defines the radius of the dimension line,
        the circular arc.
    
    normal: Base::Vector3, optional
        It defaults to `None`, in which case the `normal` is taken
        from the currently active `App.DraftWorkingPlane.axis`.
    
        If the working plane is not available, then the `normal`
        defaults to +Z or `Vector(0, 0, 1)`.
    
    Returns
    -------
    App::FeaturePython
        A scripted object of type `'AngularDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).
    
    None
        If there is a problem it will return `None`.
    

Referenced by
[draftmake.make_dimension.makeAngularDimension()](../../d5/d7f/group__draftmake.html#ga77542e026ce72bf7790c0efb20c0ac08).

## ◆ make_arc_3points()

def draftmake.make_arc_3points.make_arc_3points  | ( |  | _points_ ,   
---|---|---|---  
|  |  | _placement_ = `None`,   
|  |  | _face_ = `False`,   
|  |  | _support_ = `None`,   
|  |  | _map_mode_ = `"Deactivated"`,   
|  |  | _primitive_ = `False`  
| ) | |   
      
    
    Draw a circular arc defined by three points in the circumference.
    
    Parameters
    ----------
    points: list of Base::Vector3
        A list that must be three points.
    
    placement: Base::Placement, optional
        It defaults to `None`.
        It is a placement, comprised of a `Base` (`Base::Vector3`),
        and a `Rotation` (`Base::Rotation`).
        If it exists it moves the center of the new object to the point
        indicated by `placement.Base`, while `placement.Rotation`
        is ignored so that the arc keeps the same orientation
        with which it was created.
    
        If both `support` and `placement` are given,
        `placement.Base` is used for the `AttachmentOffset.Base`,
        and again `placement.Rotation` is ignored.
    
    face: bool, optional
        It defaults to `False`.
        If it is `True` it will create a face in the closed arc.
        Otherwise only the circumference edge will be shown.
    
    support: App::PropertyLinkSubList, optional
        It defaults to `None`.
        It is a list containing tuples to define the attachment
        of the new object.
    
        A tuple in the list needs two elements;
        the first is an external object, and the second is another tuple
        with the names of sub-elements on that external object
        likes vertices or faces.
        ::
            support = [(obj, ("Face1"))]
            support = [(obj, ("Vertex1", "Vertex5", "Vertex8"))]
    
        This parameter sets the `Support` property but it only really affects
        the position of the new object when the `map_mode`
        is set to other than `'Deactivated'`.
    
    map_mode: str, optional
        It defaults to `'Deactivated'`.
        It defines the type of `'MapMode'` of the new object.
        This parameter only works when a `support` is also provided.
    
        Example: place the new object on a face or another object.
        ::
            support = [(obj, ("Face1"))]
            map_mode = 'FlatFace'
    
        Example: place the new object on a plane created by three vertices
        of an object.
        ::
            support = [(obj, ("Vertex1", "Vertex5", "Vertex8"))]
            map_mode = 'ThreePointsPlane'
    
    primitive: bool, optional
        It defaults to `False`. If it is `True`, it will create a Part
        primitive instead of a Draft object.
        In this case, `placement`, `face`, `support`, and `map_mode`
        are ignored.
    
    Returns
    -------
    Part::Part2DObject or Part::Feature
        The new arc object.
        Normally it returns a parametric Draft object (`Part::Part2DObject`).
        If `primitive` is `True`, it returns a basic `Part::Feature`.
    
    None
        Returns `None` if there is a problem and the object cannot be created.
    

## ◆ make_array()

def draftmake.make_array.make_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _arg1_ ,   
|  |  | _arg2_ ,   
|  |  | _arg3_ ,   
|  |  | _arg4_ = `None`,   
|  |  | _arg5_ = `None`,   
|  |  | _arg6_ = `None`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a Draft Array of the given object.
    
    Rectangular array
    -----------------
    make_array(object, xvector, yvector, xnum, ynum)
    make_array(object, xvector, yvector, zvector, xnum, ynum, znum)
    
    xnum of iterations in the x direction
    at xvector distance between iterations, same for y direction
    with yvector and ynum, same for z direction with zvector and znum.
    
    Polar array
    -----------
    make_array(object, center, totalangle, totalnum) for polar array, or
    
    center is a vector, totalangle is the angle to cover (in degrees)
    and totalnum is the number of objects, including the original.
    
    Circular array
    --------------
    make_array(object, rdistance, tdistance, axis, center, ncircles, symmetry)
    
    In case of a circular array, rdistance is the distance of the
    circles, tdistance is the distance within circles, axis the rotation-axis,
    center the center of rotation, ncircles the number of circles
    and symmetry the number of symmetry-axis of the distribution.
    
    To Do
    -----
    The `Array` class currently handles three types of arrays,
    orthogonal, polar, and circular. In the future, probably they should be
    split in separate classes so that they are easier to manage.
    

## ◆ make_bezcurve()

def draftmake.make_bezcurve.make_bezcurve  | ( |  | _pointslist_ ,   
---|---|---|---  
|  |  | _closed_ = `False`,   
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _support_ = `None`,   
|  |  | _degree_ = `None`  
| ) | |   
      
    
    make_bezcurve(pointslist, [closed], [placement])
    
    Creates a Bezier Curve object from the given list of vectors.
    
    Parameters
    ----------
    pointlist : [Base.Vector]
        List of points to create the polyline.
        Instead of a pointslist, you can also pass a Part Wire.
        TODO: Change the name so!
    
    closed : bool
        If closed is True or first and last points are identical, 
        the created BSpline will be closed.
    
    placement : Base.Placement
        If a placement is given, it is used.
    
    face : Bool
        If face is False, the rectangle is shown as a wireframe, 
        otherwise as a face.   
    
    support : 
        TODO: Describe
    
    degree : int
        Degree of the BezCurve
    

## ◆ make_block()

def draftmake.make_block.make_block  | ( |  | _objectslist_| ) |   
---|---|---|---|---|---  
      
    
    make_block(objectslist)
    
    Creates a Draft Block from the given objects.
    
    Parameters
    ----------
    objectlist : list
        Major radius of the ellipse.

## ◆ make_bspline()

def draftmake.make_bspline.make_bspline  | ( |  | _pointslist_ ,   
---|---|---|---  
|  |  | _closed_ = `False`,   
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _support_ = `None`  
| ) | |   
      
    
    make_bspline(pointslist, [closed], [placement])
    
    Creates a B-Spline object from the given list of vectors.
    
    Parameters
    ----------
    pointlist : [Base.Vector]
        List of points to create the polyline.
        Instead of a pointslist, you can also pass a Part Wire.
        TODO: Change the name so!
    
    closed : bool
        If closed is True or first and last points are identical, 
        the created BSpline will be closed.
    
    placement : Base.Placement
        If a placement is given, it is used.
    
    face : Bool
        If face is False, the rectangle is shown as a wireframe, 
        otherwise as a face.   
    
    support : 
        TODO: Describe
    

## ◆ make_circle()

def draftmake.make_circle.make_circle  | ( |  | _radius_ ,   
---|---|---|---  
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _startangle_ = `None`,   
|  |  | _endangle_ = `None`,   
|  |  | _support_ = `None`  
| ) | |   
      
    
    make_circle(radius, [placement, face, startangle, endangle])
    or make_circle(edge,[face]):
    
    Creates a circle object with given parameters. 
    
    Parameters
    ----------
    radius : the radius of the circle.
    
    placement : 
        If placement is given, it is used. 
    
    face : Bool
        If face is False, the circle is shown as a wireframe, 
        otherwise as a face. 
    
    startangle : start angle of the arc (in degrees)
    
    endangle : end angle of the arc (in degrees)
        if startangle and endangle are equal, a circle is created, 
        if they are different an arc is created
    
    edge : edge.Curve must be a 'Part.Circle'
        the circle is created from the given edge
    
    support : 
        TODO: Describe
    

## ◆ make_circular_array()

def draftmake.make_circulararray.make_circular_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _r_distance_ = `100`,   
|  |  | _tan_distance_ = `50`,   
|  |  | _number_ = `3`,   
|  |  | _symmetry_ = `1`,   
|  |  | _axis_ = `App.Vector(0, 0, 1)`,   
|  |  | _center_ = `App.Vector(0, 0, 0)`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a circular array from the given object.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    r_distance: float, optional
        It defaults to `100`.
        Radial distance to the next ring of circular arrays.
    
    tan_distance: float, optional
        It defaults to `50`.
        The tangential distance between two elements located
        in the same circular ring.
        The tangential distance together with the radial distance
        determine how many copies are created.
    
    number: int, optional
        It defaults to 3.
        The number of layers or rings of repeated objects.
        The original object stays at the center, and is counted
        as a layer itself. So, if you want at least one layer of circular
        copies, this number must be at least 2.
    
    symmetry: int, optional
        It defaults to 1.
        It indicates how many lines of symmetry the entire circular pattern
        has. That is, with 1, the array is symmetric only after a full
        360 degrees rotation.
    
        When it is 2, the array is symmetric at 0 and 180 degrees.
        When it is 3, the array is symmetric at 0, 120, and 240 degrees.
        When it is 4, the array is symmetric at 0, 90, 180, and 270 degrees.
        Et cetera.
    
    axis: Base::Vector3, optional
        It defaults to `App.Vector(0, 0, 1)` or the `+Z` axis.
        The unit vector indicating the axis of rotation.
    
    center: Base::Vector3, optional
        It defaults to `App.Vector(0, 0, 0)` or the global origin.
        The point through which the `axis` passes to define
        the axis of rotation.
    
    use_link: bool, optional
        It defaults to `True`.
        If it is `True` the produced copies are not `Part::TopoShape` copies,
        but rather `App::Link` objects.
        The Links repeat the shape of the original `base_object` exactly,
        and therefore the resulting array is more memory efficient.
    
        Also, when `use_link` is `True`, the `Fuse` property
        of the resulting array does not work; the array doesn't
        contain separate shapes, it only has the original shape repeated
        many times, so there is nothing to fuse together.
    
        If `use_link` is `False` the original shape is copied many times.
        In this case the `Fuse` property is able to fuse
        all copies into a single object, if they touch each other.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    make_ortho_array, make_polar_array, make_path_array, make_point_array
    

## ◆ make_clone()

def draftmake.make_clone.make_clone  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _delta_ = `None`,   
|  |  | _forcedraft_ = `False`  
| ) | |   
      
    
    clone(obj,[delta,forcedraft])
    
    Makes a clone of the given object(s).
    The clone is an exact, linked copy of the given object. If the original
    object changes, the final object changes too.
    
    Parameters
    ----------
    obj :
    
    delta : Base.Vector
        Delta Vector to move the clone from the original position.
    
    forcedraft : bool
        If forcedraft is True, the resulting object is a Draft clone
        even if the input object is an Arch object.

## ◆ make_copy()

def draftmake.make_copy.make_copy  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _force_ = `None`,   
|  |  | _reparent_ = `False`,   
|  |  | _simple_copy_ = `False`  
| ) | |   
      
    
    make_copy(object, [force], [reparent], [simple_copy])
    
    Make an exact copy of an object and return it.
    
    Parameters
    ----------
    obj :
        Object to copy.
    
    force :
        Obsolete, not used anymore.
    
    reparent :
        Group the new object in the same group of the old one.
    
    simple_copy :
        Create a simple copy of the object (a new non parametric
        Part::Feature with the same Shape as the given object).
    

## ◆ make_dimension()

def draftmake.make_dimension.make_dimension  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_ ,   
|  |  | _p3_ = `None`,   
|  |  | _p4_ = `None`  
| ) | |   
      
    
    Create one of three types of dimension objects.
    
    In all dimensions the p3 parameter defines a point through which
    the dimension line will go through.
    
    The current line width and color will be used.
    
    Linear dimension
    ----------------
    - (p1, p2, p3): a simple linear dimension from p1 to p2
    
    - (object, i1, i2, p3): creates a linked dimension to the provided
      object (edge), measuring the distance between its vertices
      indexed i1 and i2
    
    Circular dimension
    ------------------
    - (arc, i1, mode, p3): creates a linked dimension to the given arc
      object, i1 is the index of the arc edge that will be measured;
      mode is either "radius" or "diameter".
    

## ◆ make_drawing_view()

def draftmake.make_drawingview.make_drawing_view  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _page_ ,   
|  |  | _lwmod_ = `None`,   
|  |  | _tmod_ = `None`,   
|  |  | _otherProjection_ = `None`  
| ) | |   
      
    
    make_drawing_view(object,page,[lwmod,tmod])
    
    This function is OBSOLETE, since TechDraw substituted the Drawing Workbench.
    Add a View of the given object to the given page. 
    
    Parameters
    ----------
    lwmod : 
        modifies lineweights (in percent), 
    
    tmod :
        modifies text heights (in percent). 
    
    The Hint scale, X and Y of the page are used.
        TODO: Document it properly
    

References
[draftmake.make_drawingview.make_drawing_view()](../../d5/d7f/group__draftmake.html#ga3048804d3459bb898e632560ad59687f),
and
[ArchPanel.makePanelView()](../../df/d76/namespaceArchPanel.html#a0b3f9a371623f4ec62107576f94a1228).

Referenced by
[draftmake.make_drawingview.make_drawing_view()](../../d5/d7f/group__draftmake.html#ga3048804d3459bb898e632560ad59687f).

## ◆ make_ellipse()

def draftmake.make_ellipse.make_ellipse  | ( |  | _majradius_ ,   
---|---|---|---  
|  |  | _minradius_ ,   
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _support_ = `None`  
| ) | |   
      
    
    make_ellipse(majradius, minradius, [placement], [face], [support])
    
    Makes an ellipse with the given major and minor radius, and optionally
    a placement.
    
    Parameters
    ----------
    majradius : 
        Major radius of the ellipse.
    
    minradius : 
        Minor radius of the ellipse.
    
    placement : Base.Placement
        If a placement is given, it is used.
    
    face : Bool
        If face is False, the rectangle is shown as a wireframe, 
        otherwise as a face.   
    
    support : 
        TODO: Describe.
    

## ◆ make_facebinder()

def draftmake.make_facebinder.make_facebinder  | ( |  | _selectionset_ ,   
---|---|---|---  
|  |  | _name_ = `"Facebinder"`  
| ) | |   
      
    
    make_facebinder(selectionset, [name])
    
    Creates a Facebinder object from a selection set.
    
    Parameters
    ----------
    selectionset :
        Only faces will be added.
    
    name : string (default = "Facebinder")
        Name of the created object
    

## ◆ make_fillet()

def draftmake.make_fillet.make_fillet  | ( |  | _objs_ ,   
---|---|---|---  
|  |  | _radius_ = `100`,   
|  |  | _chamfer_ = `False`,   
|  |  | _delete_ = `False`  
| ) | |   
      
    
    Create a fillet between two lines or Part.Edges.
    
    Parameters
    ----------
    objs: list
        List of two objects of type wire, or edges.
    
    radius: float, optional
        It defaults to 100. The curvature of the fillet.
    
    chamfer: bool, optional
        It defaults to `False`. If it is `True` it no longer produces
        a rounded fillet but a chamfer (straight edge)
        with the value of the `radius`.
    
    delete: bool, optional
        It defaults to `False`. If it is `True` it will delete
        the pair of objects that are used to create the fillet.
        Otherwise, the original objects will still be there.
    
    Returns
    -------
    Part::Part2DObjectPython
        The object of Proxy type `'Fillet'`.
        It returns `None` if it fails producing the object.
    

## ◆ make_label()

def draftmake.make_label.make_label  | ( |  | _target_point_ = `App.Vector(0, 0, 0)`,   
---|---|---|---  
|  |  | _placement_ = `App.Vector(30, 30, 0)`,   
|  |  | _target_object_ = `None`,   
|  |  | _subelements_ = `None`,   
|  |  | _label_type_ = `"Custom"`,   
|  |  | _custom_text_ = `"Label"`,   
|  |  | _direction_ = `"Horizontal"`,   
|  |  | _distance_ = `-10`,   
|  |  | _points_ = `None`  
| ) | |   
      
    
    Create a Label object containing different types of information.
    
    The current color and text height and font specified in preferences
    are used.
    
    Parameters
    ----------
    target_point: Base::Vector3, optional
        It defaults to the origin `App.Vector(0, 0, 0)`.
        This is the point which is pointed to by the label's leader line.
        This point can be adorned with a marker like an arrow or circle.
    
    placement: Base::Placement, Base::Vector3, or Base::Rotation, optional
        It defaults to `App.Vector(30, 30, 0)`.
        If it is provided, it defines the base point of the textual
        label.
        The input could be a full placement, just a vector indicating
        the translation, or just a rotation.
    
    target_object: Part::Feature or str, optional
        It defaults to `None`.
        If it exists it should be an object which will be used to provide
        information to the label, as long as `label_type` is different
        from `'Custom'`.
    
        If it is a string, it must be the `Label` of that object.
        Since a `Label` is not guaranteed to be unique in a document,
        it will use the first object found with this `Label`.
    
    subelements: str, optional
        It defaults to `None`.
        If `subelements` is provided, `target_object` should be provided
        as well, otherwise it is ignored.
    
        It should be a string indicating a subelement name, either
        `'VertexN'`, `'EdgeN'`, or `'FaceN'` which should exist
        within `target_object`.
        In this case `'N'` is an integer that indicates the specific number
        of vertex, edge, or face in `target_object`.
    
        Both `target_object` and `subelements` are used to link the label
        to a particular object, or to the particular vertex, edge, or face,
        and get information from them.
        ::
            make_label(..., target_object=App.ActiveDocument.Box)
            make_label(..., target_object="My box", subelements="Face3")
    
        These two parameters can be can be obtained from the `Gui::Selection`
        module.
        ::
            sel_object = Gui.Selection.getSelectionEx()[0]
            target_object = sel_object.Object
            subelements = sel_object.SubElementNames[0]
    
    label_type: str, optional
        It defaults to `'Custom'`.
        It indicates the type of information that will be shown in the label.
        See the get_label_types function in label.py for supported types.
    
        Only `'Custom'` allows you to manually set the text
        by defining `custom_text`. The other types take their information
        from the object included in `target`.
    
        - `'Position'` will show the base position of the target object,
          or of the indicated `'VertexN'` in `target`.
        - `'Length'` will show the `Length` of the target object's `Shape`,
          or of the indicated `'EdgeN'` in `target`.
        - `'Area'` will show the `Area` of the target object's `Shape`,
          or of the indicated `'FaceN'` in `target`.
    
    custom_text: str, or list of str, optional
        It defaults to `'Label'`.
        If it is a list, each element in the list represents a new text line.
    
        It is the text that will be displayed by the label when
        `label_type` is `'Custom'`.
    
    direction: str, optional
        It defaults to `'Horizontal'`.
        It can be `'Horizontal'`, `'Vertical'`, or `'Custom'`.
        It indicates the direction of the straight segment of the leader line
        that ends up next to the textual label.
    
        If `'Custom'` is selected, the leader line can be manually drawn
        by specifying the value of `points`.
        Normally, the leader line has only three points, but with `'Custom'`
        you can specify as many points as needed.
    
    distance: int, float, Base::Quantity, optional
        It defaults to -10.
        It indicates the length of the horizontal or vertical segment
        of the leader line.
    
        The leader line is composed of two segments, the first segment is
        inclined, while the second segment is either horizontal or vertical
        depending on the value of `direction`.
        ::
            T
            |
            |
            o------- L text
    
        The `oL` segment's length is defined by `distance`
        while the `oT` segment is automatically calculated depending
        on the values of `placement` (L) and `distance` (o).
    
        This `distance` is oriented, meaning that if it is positive
        the segment will be to the right and above of the textual
        label, depending on if `direction` is `'Horizontal'` or `'Vertical'`,
        respectively.
        If it is negative, the segment will be to the left
        and below of the text.
    
    points: list of Base::Vector3, optional
        It defaults to `None`.
        It is a list of vectors defining the shape of the leader line;
        the list must have at least two points.
        This argument must be used together with `direction='Custom'`
        to display this custom leader.
    
        However, notice that if the Label's `StraightDirection` property
        is later changed to `'Horizontal'` or `'Vertical'`,
        the custom point list will be overwritten with a new,
        automatically calculated three-point list.
    
        For the object to use custom points, `StraightDirection`
        must remain `'Custom'`, and then the `Points` property
        can be overwritten by a suitable list of points.
    
    Returns
    -------
    App::FeaturePython
        A scripted object of type `'Label'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).
    
    None
        If there is a problem it will return `None`.
    

## ◆ make_layer()

def draftmake.make_layer.make_layer  | ( |  | _name_ = `None`,   
---|---|---|---  
|  |  | _line_color_ = `None`,   
|  |  | _shape_color_ = `None`,   
|  |  | _line_width_ = `2.0`,   
|  |  | _draw_style_ = `"Solid"`,   
|  |  | _transparency_ = `0`  
| ) | |   
      
    
    Create a Layer object in the active document.
    
    If a layer container named `'LayerContainer'` does not exist,
    it is created with this name.
    
    A layer controls the view properties of the objects inside the layer,
    so all parameters except for `name` only apply if the graphical interface
    is up.
    
    Parameters
    ----------
    name: str, optional
        It is used to set the layer's `Label` (user editable).
        It defaults to `None`, in which case the `Label`
        is set to `'Layer'` or to its translation in the current language.
    
    line_color: tuple, optional
        It defaults to `None`, in which case it uses the value of the parameter
        `User parameter:BaseApp/Preferences/View/DefaultShapeLineColor`.
        If it is given, it should be a tuple of three
        floating point values from 0.0 to 1.0.
    
    shape_color: tuple, optional
        It defaults to `None`, in which case it uses the value of the parameter
        `User parameter:BaseApp/Preferences/View/DefaultShapeColor`.
        If it is given, it should be a tuple of three
        floating point values from 0.0 to 1.0.
    
    line_width: float, optional
        It defaults to 2.0.
        It determines the width of the edges of the objects contained
        in the layer.
    
    draw_style: str, optional
        It defaults to `'Solid'`.
        It determines the style of the edges of the objects contained
        in the layer.
        If it is given, it should be 'Solid', 'Dashed', 'Dotted',
        or 'Dashdot'.
    
    transparency: int, optional
        It defaults to 0.
        It should be an integer value from 0 (completely opaque)
        to 100 (completely transparent).
    
    Return
    ------
    App::FeaturePython
        A scripted object of type `'Layer'`.
        This object does not have a `Shape` attribute.
        Modifying the view properties of this object will affect the objects
        inside of it.
    
    None
        If there is a problem it will return `None`.
    

References
[draftmake.make_layer.get_layer_container()](../../d5/d7f/group__draftmake.html#ga455220c5d2ce1ef7b98e5b3586accfb4).

## ◆ make_line()

def draftmake.make_line.make_line  | ( |  | _first_param_ ,   
---|---|---|---  
|  |  | _last_param_ = `None`  
| ) | |   
      
    
    makeLine(first_param, p2)
    
    Creates a line from 2 points or from a given object.
    
    Parameters
    ----------
    first_param : 
        Base.Vector -> First point of the line (if p2 is None)
        Part.LineSegment -> Line is created from the given Linesegment
        Shape -> Line is created from the give Shape
    
    last_param : Base.Vector
        Second point of the line, if not set the function evaluates 
        the first_param to look for a Part.LineSegment or a Shape
    

## ◆ make_linear_dimension()

def draftmake.make_dimension.make_linear_dimension  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_ ,   
|  |  | _dim_line_ = `None`  
| ) | |   
      
    
    Create a free linear dimension from two main points.
    
    Parameters
    ----------
    p1: Base::Vector3
        First point of the measurement.
    
    p2: Base::Vector3
        Second point of the measurement.
    
    dim_line: Base::Vector3, optional
        It defaults to `None`.
        This is a point through which the extension of the dimension line
        will pass.
        This point controls how close or how far the dimension line is
        positioned from the measured segment that goes from `p1` to `p2`.
    
        If it is `None`, this point will be calculated from the intermediate
        distance betwwen `p1` and `p2`.
    
    Returns
    -------
    App::FeaturePython
        A scripted object of type `'LinearDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).
    
    None
        If there is a problem it will return `None`.
    

## ◆ make_linear_dimension_obj()

def draftmake.make_dimension.make_linear_dimension_obj  | ( |  | _edge_object_ ,   
---|---|---|---  
|  |  | _i1_ = `1`,   
|  |  | _i2_ = `2`,   
|  |  | _dim_line_ = `None`  
| ) | |   
      
    
    Create a linear dimension from an object.
    
    Parameters
    ----------
    edge_object: Part::Feature
        The object which has an edge which will be measured.
        It must have a `Part::TopoShape`, and at least one element
        in `Shape.Vertexes`, to be able to measure a distance.
    
    i1: int, optional
        It defaults to `1`.
        It is the index of the first vertex in `edge_object` from which
        the measurement will be taken.
        The minimum value should be `1`, which will be interpreted
        as `'Vertex1'`.
    
        If the value is below `1`, it will be set to `1`.
    
    i2: int, optional
        It defaults to `2`, which will be converted to `'Vertex2'`.
        It is the index of the second vertex in `edge_object` that determines
        the endpoint of the measurement.
    
        If it is the same value as `i1`, the resulting measurement will be
        made from the origin `(0, 0, 0)` to the vertex indicated by `i1`.
    
        If the value is below `1`, it will be set to the last vertex
        in `edge_object`.
    
        Then to measure the first and last, this could be used
        ::
            make_linear_dimension_obj(edge_object, i1=1, i2=-1)
    
    dim_line: Base::Vector3
        It defaults to `None`.
        This is a point through which the extension of the dimension line
        will pass.
        This point controls how close or how far the dimension line is
        positioned from the measured segment in `edge_object`.
    
        If it is `None`, this point will be calculated from the intermediate
        distance betwwen the vertices defined by `i1` and `i2`.
    
    Returns
    -------
    App::FeaturePython
        A scripted object of type `'LinearDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).
    
    None
        If there is a problem it will return `None`.
    

References
[draftmake.make_dimension.make_linear_dimension_obj()](../../d5/d7f/group__draftmake.html#ga356340565c645f30b44ee0850cfabbd5).

Referenced by
[draftmake.make_dimension.make_linear_dimension_obj()](../../d5/d7f/group__draftmake.html#ga356340565c645f30b44ee0850cfabbd5).

## ◆ make_ortho_array()

def draftmake.make_orthoarray.make_ortho_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _v_x_ = `App.Vector(10, 0, 0)`,   
|  |  | _v_y_ = `App.Vector(0, 10, 0)`,   
|  |  | _v_z_ = `App.Vector(0, 0, 10)`,   
|  |  | _n_x_ = `2`,   
|  |  | _n_y_ = `2`,   
|  |  | _n_z_ = `1`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create an orthogonal array from the given object.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    v_x, v_y, v_z: Base::Vector3, optional
        The vector indicating the vector displacement between two elements
        in the specified orthogonal direction X, Y, Z.
    
        By default:
        ::
            v_x = App.Vector(10, 0, 0)
            v_y = App.Vector(0, 10, 0)
            v_z = App.Vector(0, 0, 10)
    
        Given that this is a vectorial displacement
        the next object can appear displaced in one, two or three axes
        at the same time.
    
        For example
        ::
            v_x = App.Vector(10, 5, 0)
    
        means that the next element in the X direction will be displaced
        10 mm in X, 5 mm in Y, and 0 mm in Z.
    
        A traditional "rectangular" array is obtained when
        the displacement vector only has its corresponding component,
        like in the default case.
    
        If these values are entered as single numbers instead
        of vectors, the single value is expanded into a vector
        of the corresponding direction, and the other components are assumed
        to be zero.
    
        For example
        ::
            v_x = 15
            v_y = 10
            v_z = 1
        becomes
        ::
            v_x = App.Vector(15, 0, 0)
            v_y = App.Vector(0, 10, 0)
            v_z = App.Vector(0, 0, 1)
    
    n_x, n_y, n_z: int, optional
        The number of copies in the specified orthogonal direction X, Y, Z.
        This number includes the original object, therefore, it must be
        at least 1.
    
        The values of `n_x` and `n_y` default to 2,
        while `n_z` defaults to 1.
        This means the array is a planar array by default.
    
    use_link: bool, optional
        It defaults to `True`.
        If it is `True` the produced copies are not `Part::TopoShape` copies,
        but rather `App::Link` objects.
        The Links repeat the shape of the original `base_object` exactly,
        and therefore the resulting array is more memory efficient.
    
        Also, when `use_link` is `True`, the `Fuse` property
        of the resulting array does not work; the array doesn't
        contain separate shapes, it only has the original shape repeated
        many times, so there is nothing to fuse together.
    
        If `use_link` is `False` the original shape is copied many times.
        In this case the `Fuse` property is able to fuse
        all copies into a single object, if they touch each other.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    make_ortho_array2d, make_rect_array, make_rect_array2d, make_polar_array,
    make_circular_array, make_path_array, make_point_array
    

## ◆ make_ortho_array2d()

def draftmake.make_orthoarray.make_ortho_array2d  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _v_x_ = `App.Vector(10, 0, 0)`,   
|  |  | _v_y_ = `App.Vector(0, 10, 0)`,   
|  |  | _n_x_ = `2`,   
|  |  | _n_y_ = `2`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a 2D orthogonal array from the given object.
    
    This works the same as `make_ortho_array`.
    The Z component is ignored so it only considers vector displacements
    in X and Y directions.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    v_x, v_y: Base::Vector3, optional
        Vectorial displacement of elements
        in the corresponding X and Y directions.
        See `make_ortho_array`.
    
    n_x, n_y: int, optional
        Number of elements
        in the corresponding X and Y directions.
        See `make_ortho_array`.
    
    use_link: bool, optional
        If it is `True`, create `App::Link` array.
        See `make_ortho_array`.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    make_ortho_array, make_rect_array, make_rect_array2d, make_polar_array,
    make_circular_array, make_path_array, make_point_array
    

## ◆ make_path_array()

def draftmake.make_patharray.make_path_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _path_object_ ,   
|  |  | _count_ = `4`,   
|  |  | _extra_ = `App.Vector(0, 0, 0)`,   
|  |  | _subelements_ = `None`,   
|  |  | _align_ = `False`,   
|  |  | _align_mode_ = `"Original"`,   
|  |  | _tan_vector_ = `App.Vector(1, 0, 0)`,   
|  |  | _force_vertical_ = `False`,   
|  |  | _vertical_vector_ = `App.Vector(0, 0, 1)`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Make a Draft PathArray object.
    
    Distribute copies of a `base_object` along `path_object`
    or `subelements` from `path_object`.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    path_object: Part::Feature or str
        Path object like a polyline, B-Spline, or bezier curve that should
        contain edges.
        Just like `base_object` it can also be `Label`.
    
    count: int, float, optional
        It defaults to 4.
        Number of copies to create along the `path_object`.
        It must be at least 2.
        If a `float` is provided, it will be truncated by `int(count)`.
    
    extra: Base.Vector3, optional
        It defaults to `App.Vector(0, 0, 0)`.
        It translates each copy by the value of `extra`.
        This is useful to adjust for the difference between shape centre
        and shape reference point.
    
    subelements: list or tuple of str, optional
        It defaults to `None`.
        It should be a list of names of edges that must exist in `path_object`.
        Then the path array will be created along these edges only,
        and not the entire `path_object`.
        ::
            subelements = ['Edge1', 'Edge2']
    
        The edges must be contiguous, meaning that it is not allowed to
        input `'Edge1'` and `'Edge3'` if they do not touch each other.
    
        A single string value is also allowed.
        ::
            subelements = 'Edge1'
    
    align: bool, optional
        It defaults to `False`.
        If it is `True` it will align `base_object` to tangent, normal,
        or binormal to the `path_object`, depending on the value
        of `tan_vector`.
    
    align_mode: str, optional
        It defaults to `'Original'` which is the traditional alignment.
        It can also be `'Frenet'` or `'Tangent'`.
    
        - Original. It does not calculate curve normal.
          `X` is curve tangent, `Y` is normal parameter, Z is the cross
          product `X` x `Y`.
        - Frenet. It defines a local coordinate system along the path.
          `X` is tangent to curve, `Y` is curve normal, `Z` is curve binormal.
          If normal cannot be computed, for example, in a straight path,
          a default is used.
        - Tangent. It is similar to `'Original'` but includes a pre-rotation
          to align the base object's `X` to the value of `tan_vector`,
          then `X` follows curve tangent.
    
    tan_vector: Base::Vector3, optional
        It defaults to `App.Vector(1, 0, 0)` or the +X axis.
        It aligns the tangent of the path to this local unit vector
        of the object.
    
    force_vertical: Base::Vector3, optional
        It defaults to `False`.
        If it is `True`, the value of `vertical_vector`
        will be used when `align_mode` is `'Original'` or `'Tangent'`.
    
    vertical_vector: Base::Vector3, optional
        It defaults to `App.Vector(0, 0, 1)` or the +Z axis.
        It will force this vector to be the vertical direction
        when `force_vertical` is `True`.
    
    use_link: bool, optional
        It defaults to `True`, in which case the copies are `App::Link`
        elements. Otherwise, the copies are shape copies which makes
        the resulting array heavier.
    
    Returns
    -------
    Part::FeaturePython
        The scripted object of type `'PathArray'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    

Referenced by
[draftmake.make_patharray.makePathArray()](../../d5/d7f/group__draftmake.html#ga67f067adb8d096afe5d6dcd616facb2f).

## ◆ make_path_twisted_array()

def draftmake.make_patharray.make_path_twisted_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _path_object_ ,   
|  |  | _count_ = `15`,   
|  |  | _rot_factor_ = `0.25`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a Path twisted array.

## ◆ make_point()

def draftmake.make_point.make_point  | ( |  | _X_ = `0`,   
---|---|---|---  
|  |  | _Y_ = `0`,   
|  |  | _Z_ = `0`,   
|  |  | _color_ = `None`,   
|  |  | _name_ = `"Point"`,   
|  |  | _point_size_ = `5`  
| ) | |   
      
    
     make_point(x, y, z, [color(r, g, b), point_size]) or
        make_point(Vector, color(r, g, b), point_size])
    
    Creates a Draft Point in the current document.
    
    Parameters
    ----------
    X : 
        float -> X coordinate of the point
        Base.Vector -> Ignore Y and Z coordinates and create the point
            from the vector.
    
    Y : float
        Y coordinate of the point
    
    Z : float
        Z coordinate of the point
    
    color : (R, G, B)
        Point color as RGB
        example to create a colored point:
        make_point(0,0,0,(1,0,0)) # color = red
        example to change the color, make sure values are floats:
        p1.ViewObject.PointColor =(0.0,0.0,1.0)
    

## ◆ make_point_array()

def draftmake.make_pointarray.make_point_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _point_object_ ,   
|  |  | _extra_ = `None`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Make a Draft PointArray object.
    
    Distribute copies of a `base_object` in the points
    defined by `point_object`.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    point_object: Part::Feature or str
        An object that is a type of container for holding points.
        This object must have one of the following properties `Geometry`,
        `Links`, or `Components`, which themselves must contain objects
        with `X`, `Y`, and `Z` properties.
    
        This object could be:
    
        - A `Sketcher::SketchObject`, as it has a `Geometry` property.
          The sketch can contain different elements but it must contain
          at least one `Part::GeomPoint`.
    
        - A `Part::Compound`, as it has a `Links` property. The compound
          can contain different elements but it must contain at least
          one object that has `X`, `Y`, and `Z` properties,
          like a `Draft Point` or a `Part::Vertex`.
    
        - A `Draft Block`, as it has a `Components` property. This `Block`
          behaves essentially the same as a `Part::Compound`. It must
          contain at least a point or vertex object.
    
    extra: Base::Placement, Base::Vector3, or Base::Rotation, optional
        It defaults to `None`.
        If it is provided, it is an additional placement that is applied
        to each copy of the array.
        The input could be a full placement, just a vector indicating
        the additional translation, or just a rotation.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'PointArray'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    

Referenced by
[draftmake.make_pointarray.makePointArray()](../../d5/d7f/group__draftmake.html#gaadbed89ef29e6f261fb9f33ab94814ea).

## ◆ make_polar_array()

def draftmake.make_polararray.make_polar_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _number_ = `5`,   
|  |  | _angle_ = `360`,   
|  |  | _center_ = `App.Vector(0, 0, 0)`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a polar array from the given object.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    number: int, optional
        It defaults to 5.
        The number of copies produced in the polar pattern.
    
    angle: float, optional
        It defaults to 360.
        The magnitude in degrees swept by the polar pattern.
    
    center: Base::Vector3, optional
        It defaults to the origin `App.Vector(0, 0, 0)`.
        The vector indicating the center of rotation of the array.
    
    use_link: bool, optional
        It defaults to `True`.
        If it is `True` the produced copies are not `Part::TopoShape` copies,
        but rather `App::Link` objects.
        The Links repeat the shape of the original `obj` exactly,
        and therefore the resulting array is more memory efficient.
    
        Also, when `use_link` is `True`, the `Fuse` property
        of the resulting array does not work; the array doesn't
        contain separate shapes, it only has the original shape repeated
        many times, so there is nothing to fuse together.
    
        If `use_link` is `False` the original shape is copied many times.
        In this case the `Fuse` property is able to fuse
        all copies into a single object, if they touch each other.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    make_ortho_array, make_circular_array, make_path_array, make_point_array
    

## ◆ make_polygon()

def draftmake.make_polygon.make_polygon  | ( |  | _nfaces_ ,   
---|---|---|---  
|  |  | _radius_ = `1`,   
|  |  | _inscribed_ = `True`,   
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _support_ = `None`  
| ) | |   
      
    
    makePolgon(edges,[radius],[inscribed],[placement],[face])
    
    Creates a polygon object with the given number of edges and radius.
    
    Parameters
    ----------
    edges : int
        Number of edges of the polygon.
    
    radius : 
        Radius of the control circle.
    
    inscribed : bool
        Defines is the polygon is inscribed or not into the control circle.
    
    placement : Base.Placement
        If placement is given, it is used. 
    
    face : bool
        If face is True, the resulting shape is displayed as a face, 
        otherwise as a wireframe.
    
    support : 
        TODO: Describe
    

## ◆ make_radial_dimension_obj()

def draftmake.make_dimension.make_radial_dimension_obj  | ( |  | _edge_object_ ,   
---|---|---|---  
|  |  | _index_ = `1`,   
|  |  | _mode_ = `"radius"`,   
|  |  | _dim_line_ = `None`  
| ) | |   
      
    
    Create a radial or diameter dimension from an arc object.
    
    Parameters
    ----------
    edge_object: Part::Feature
        The object which has a circular edge which will be measured.
        It must have a `Part::TopoShape`, and at least one element
        must be a circular edge in `Shape.Edges` to be able to measure
        its radius.
    
    index: int, optional
        It defaults to `1`.
        It is the index of the edge in `edge_object` which is going to
        be measured.
        The minimum value should be `1`, which will be interpreted
        as `'Edge1'`. If the value is below `1`, it will be set to `1`.
    
    mode: str, optional
        It defaults to `'radius'`; the other option is `'diameter'`.
        It determines whether the dimension will be shown as a radius
        or as a diameter.
    
    dim_line: Base::Vector3, optional
        It defaults to `None`.
        This is a point through which the extension of the dimension line
        will pass. The dimension line will be a radius or diameter
        of the measured arc, extending from the center to the arc itself.
    
        If it is `None`, this point will be set to one unit to the right
        of the center of the arc, which will create a dimension line that is
        horizontal, that is, parallel to the +X axis.
    
    Returns
    -------
    App::FeaturePython
        A scripted object of type `'LinearDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).
    
    None
        If there is a problem it will return `None`.
    

## ◆ make_rect_array()

def draftmake.make_orthoarray.make_rect_array  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _d_x_ = `10`,   
|  |  | _d_y_ = `10`,   
|  |  | _d_z_ = `10`,   
|  |  | _n_x_ = `2`,   
|  |  | _n_y_ = `2`,   
|  |  | _n_z_ = `1`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a rectangular array from the given object.
    
    This function wraps around `make_ortho_array`
    to produce strictly rectangular arrays, in which
    the displacement vectors `v_x`, `v_y`, and `v_z`
    only have their respective components in X, Y, and Z.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    d_x, d_y, d_z: Base::Vector3, optional
        Displacement of elements in the corresponding X, Y, and Z directions.
    
    n_x, n_y, n_z: int, optional
        Number of elements in the corresponding X, Y, and Z directions.
    
    use_link: bool, optional
        If it is `True`, create `App::Link` array.
        See `make_ortho_array`.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    make_ortho_array, make_ortho_array2d, make_rect_array2d, make_polar_array,
    make_circular_array, make_path_array, make_point_array
    

## ◆ make_rect_array2d()

def draftmake.make_orthoarray.make_rect_array2d  | ( |  | _base_object_ ,   
---|---|---|---  
|  |  | _d_x_ = `10`,   
|  |  | _d_y_ = `10`,   
|  |  | _n_x_ = `2`,   
|  |  | _n_y_ = `2`,   
|  |  | _use_link_ = `True`  
| ) | |   
      
    
    Create a 2D rectangular array from the given object.
    
    This function wraps around `make_ortho_array`,
    to produce strictly rectangular arrays, in which
    the displacement vectors `v_x` and `v_y`
    only have their respective components in X and Y.
    The Z component is ignored.
    
    Parameters
    ----------
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.
    
    d_x, d_y: Base::Vector3, optional
        Displacement of elements in the corresponding X and Y directions.
    
    n_x, n_y: int, optional
        Number of elements in the corresponding X and Y directions.
    
    use_link: bool, optional
        If it is `True`, create `App::Link` array.
        See `make_ortho_array`.
    
    Returns
    -------
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.
    
    None
        If there is a problem it will return `None`.
    
    See Also
    --------
    make_ortho_array, make_ortho_array2d, make_rect_array, make_polar_array,
    make_circular_array, make_path_array, make_point_array
    

## ◆ make_rectangle()

def draftmake.make_rectangle.make_rectangle  | ( |  | _length_ ,   
---|---|---|---  
|  |  | _height_ = `0`,   
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _support_ = `None`  
| ) | |   
      
    
    make_rectangle(length, width, [placement], [face])
    
    Creates a Rectangle object with length in X direction and height in Y
    direction.
    
    Parameters
    ----------
    length, height : dimensions of the rectangle
    
    placement : Base.Placement
        If a placement is given, it is used.
    
    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.
    
    Rectangles can also be constructed by giving them a list of four vertices
    as first argument: make_rectangle(list_of_vertices, face=...)
    but you are responsible to check yourself that these 4 vertices are ordered
    and actually form a rectangle, otherwise the result might be wrong. Placement
    is ignored when constructing a rectangle this way (face argument is kept).
    

## ◆ make_shape2dview()

def draftmake.make_shape2dview.make_shape2dview  | ( |  | _baseobj_ ,   
---|---|---|---  
|  |  | _projectionVector_ = `None`,   
|  |  | _facenumbers_ = `[]`  
| ) | |   
      
    
    make_shape2dview(object, [projectionVector], [facenumbers])
    
    Add a 2D shape to the document, which is a 2D projection of the given object. 
    
    Parameters
    ----------
    object : 
        TODO: Describe
    
    projectionVector : Base.Vector
        Custom vector for the projection
    
    facenumbers : [] TODO: Describe
        A list of face numbers to be considered in individual faces mode.
    

## ◆ make_shapestring()

def draftmake.make_shapestring.make_shapestring  | ( |  | _String_ ,   
---|---|---|---  
|  |  | _FontFile_ ,   
|  |  | _Size_ = `100`,   
|  |  | _Tracking_ = `0`  
| ) | |   
      
    
    ShapeString(Text,FontFile,[Height],[Track])
    
    Turns a text string into a Compound Shape
    
    Parameters
    ----------
    majradius : 
        Major radius of the ellipse.

## ◆ make_sketch()

def draftmake.make_sketch.make_sketch  | ( |  | _objects_list_ ,   
---|---|---|---  
|  |  | _autoconstraints_ = `False`,   
|  |  | _addTo_ = `None`,   
|  |  | _delete_ = `False`,   
|  |  | _name_ = `"Sketch"`,   
|  |  | _radiusPrecision_ = `-1`,   
|  |  | _tol_ = `1e-3`  
| ) | |   
      
    
    make_sketch(objects_list, [autoconstraints], [addTo], [delete],
                   [name], [radiusPrecision], [tol])
    
    Makes a Sketch objects_list with the given Draft objects.
    
    Parameters
    ----------
    objects_list: can be single or list of objects of Draft type objects,
        Part::Feature, Part.Shape, or mix of them.
    
    autoconstraints(False): if True, constraints will be automatically added to
        wire nodes, rectangles and circles.
    
    addTo(None) : if set to an existing sketch, geometry will be added to it
        instead of creating a new one.
    
    delete(False): if True, the original object will be deleted.
        If set to a string 'all' the object and all its linked object will be
        deleted.
    
    name('Sketch'): the name for the new sketch object.
    
    radiusPrecision(-1): If <0, disable radius constraint. If =0, add individual
        radius constraint. If >0, the radius will be rounded according to this
        precision, and 'Equal' constraint will be added to curve with equal
        radius within precision.
    
    tol(1e-3): Tolerance used to check if the shapes are planar and coplanar.
        Consider change to tol=-1 for a more accurate analysis.
    

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
and
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

## ◆ make_text()

def draftmake.make_text.make_text  | ( |  | _string_ ,   
---|---|---|---  
|  |  | _placement_ = `None`,   
|  |  | _screen_ = `False`  
| ) | |   
      
    
    Create a Text object containing the given list of strings.
    
    The current color and text height and font specified in preferences
    are used.
    
    Parameters
    ----------
    string: str, or list of str
        String to display on screen.
        If it is a list, each element in the list represents a new text line.
    
    placement: Base::Placement, Base::Vector3, or Base::Rotation, optional
        It defaults to `None`.
        If it is provided, it is the placement of the new text.
        The input could be a full placement, just a vector indicating
        the translation, or just a rotation.
    
    screen: bool, optional
        It defaults to `False`, in which case the text is placed in 3D space
        oriented like any other object, on top of a given plane,
        by the default the XY plane.
        If it is `True`, the text will always face perpendicularly
        to the camera direction, that is, it will be flat on the screen.
    
    Returns
    -------
    App::FeaturePython
        A scripted object of type `'Text'`.
        This object does not have a `Shape` attribute, as the text is created
        on screen by Coin (pivy).
    
    None
        If there is a problem it will return `None`.
    

## ◆ make_wire()

def draftmake.make_wire.make_wire  | ( |  | _pointslist_ ,   
---|---|---|---  
|  |  | _closed_ = `False`,   
|  |  | _placement_ = `None`,   
|  |  | _face_ = `None`,   
|  |  | _support_ = `None`,   
|  |  | _bs2wire_ = `False`  
| ) | |   
      
    
    make_wire(pointslist, [closed], [placement])
    
    Creates a Wire object from the given list of vectors.  If face is
    true (and wire is closed), the wire will appear filled. Instead of
    a pointslist, you can also pass a Part Wire.
    
    Parameters
    ----------
    pointslist : [Base.Vector]
        List of points to create the polyline
    
    closed : bool
        If closed is True or first and last points are identical, 
        the created polyline will be closed.
    
    placement : Base.Placement
        If a placement is given, it is used.
    
    face : Bool
        If face is False, the rectangle is shown as a wireframe, 
        otherwise as a face.   
    
    support : 
        TODO: Describe
    
    bs2wire : bool
        TODO: Describe
    

## ◆ make_workingplaneproxy()

def draftmake.make_wpproxy.make_workingplaneproxy  | ( |  | _placement_| ) |   
---|---|---|---|---|---  
      
    
    make_working_plane_proxy(placement)
    
    Creates a Working Plane proxy object in the current document.
    
    Parameters
    ----------
    placement : Base.Placement
        specify the p.
    

## ◆ makeAngularDimension()

def draftmake.make_dimension.makeAngularDimension  | ( |  | _center_ ,   
---|---|---|---  
|  |  | _angles_ ,   
|  |  | _p3_ ,   
|  |  | _normal_ = `None`  
| ) | |   
      
    
    Create an angle dimension. DEPRECATED. Use 'make_angular_dimension'.

References
[draftmake.make_dimension.make_angular_dimension()](../../d5/d7f/group__draftmake.html#ga8a37a6cb68456be519d0760cfa21eec3).

## ◆ makeArray()

def draftmake.make_array.makeArray  | ( |  | _baseobject_ ,   
---|---|---|---  
|  |  | _arg1_ ,   
|  |  | _arg2_ ,   
|  |  | _arg3_ ,   
|  |  | _arg4_ = `None`,   
|  |  | _arg5_ = `None`,   
|  |  | _arg6_ = `None`,   
|  |  | _name_ = `"Array"`,   
|  |  | _use_link_ = `False`  
| ) | |   
      
    
    Create an Array. DEPRECATED. Use 'make_array'.

## ◆ makeDimension()

def draftmake.make_dimension.makeDimension  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_ ,   
|  |  | _p3_ = `None`,   
|  |  | _p4_ = `None`  
| ) | |   
      
    
    Create a dimension. DEPRECATED. Use 'make_dimension'.

## ◆ makeLabel()

def draftmake.make_label.makeLabel  | ( |  | _targetpoint_ = `None`,   
---|---|---|---  
|  |  | _target_ = `None`,   
|  |  | _direction_ = `None`,   
|  |  | _distance_ = `None`,   
|  |  | _labeltype_ = `None`,   
|  |  | _placement_ = `None`  
| ) | |   
      
    
    Create a Label. DEPRECATED. Use 'make_label'.

## ◆ makeLayer()

def draftmake.make_layer.makeLayer  | ( |  | _name_ = `None`,   
---|---|---|---  
|  |  | _linecolor_ = `None`,   
|  |  | _drawstyle_ = `None`,   
|  |  | _shapecolor_ = `None`,   
|  |  | _transparency_ = `None`  
| ) | |   
      
    
    Create a Layer. DEPRECATED. Use 'make_layer'.

## ◆ makePathArray()

def draftmake.make_patharray.makePathArray  | ( |  | _baseobject_ ,   
---|---|---|---  
|  |  | _pathobject_ ,   
|  |  | _count_ ,   
|  |  | _xlate_ = `None`,   
|  |  | _align_ = `False`,   
|  |  | _pathobjsubs_ = `[]`,   
|  |  | _use_link_ = `False`  
| ) | |   
      
    
    Create PathArray. DEPRECATED. Use 'make_path_array'.

References
[draftmake.make_patharray.make_path_array()](../../d5/d7f/group__draftmake.html#gad515633e5d4a8cbeb79a5ffd09f8b438).

## ◆ makePointArray()

def draftmake.make_pointarray.makePointArray  | ( |  | _base_ ,   
---|---|---|---  
|  |  | _ptlst_  
| ) | |   
      
    
    Create PointArray. DEPRECATED. Use 'make_point_array'.

References
[draftmake.make_pointarray.make_point_array()](../../d5/d7f/group__draftmake.html#ga90c6d9fd96802f5d39c190005c119660).

## ◆ makeText()

def draftmake.make_text.makeText  | ( |  | _stringlist_ ,   
---|---|---|---  
|  |  | _point_ = `App.Vector(0, 0, 0)`,   
|  |  | _screen_ = `False`  
| ) | |   
      
    
    Create Text. DEPRECATED. Use 'make_text'.

## Variable Documentation

## ◆ clone

draftmake.make_clone.clone =
[make_clone](../../d5/d7f/group__draftmake.html#gaf3c8bb728ae3b221d0bb75551441d7d2)  
---  
  
Referenced by
[SMESH_MeshEditor.CreateFlatElementsOnFacesGroups()](../../da/d31/classSMESH__MeshEditor.html#ad20532514a3c45119d9ec10f8b3678dc),
[Sketcher::SketchObject.removeAxesAlignment()](../../d9/dad/classSketcher_1_1SketchObject.html#a7fdd15d230c082e02baefe0866420af9),
[Sketcher::SketchObject.setConstruction()](../../d9/dad/classSketcher_1_1SketchObject.html#addc566d5b284054914f8d28751fa89ec),
[TechDraw::PropertyGeomFormatList.setValues()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#aa486b1faadc067963b4c9771255ddd91),
[Sketcher::SketchObject.toggleConstruction()](../../d9/dad/classSketcher_1_1SketchObject.html#aa258782e7f208a5e28f0b39937d62f5f),
[Sketcher::SketchObject.transferConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a8d36181fad0a534e8dd7b5e74e84ea2f),
and
[Sketcher::SketchObject.trim()](../../d9/dad/classSketcher_1_1SketchObject.html#a55c244742ef90c7bc339e6c0285e2027).

## ◆ makeBezCurve

draftmake.make_bezcurve.makeBezCurve =
[make_bezcurve](../../d5/d7f/group__draftmake.html#gac86f3f114342fc87447d73296bd01983)  
---  
  
## ◆ makeBlock

draftmake.make_block.makeBlock =
[make_block](../../d5/d7f/group__draftmake.html#ga31e0a402c1ca17e8355f911e9c17b868)  
---  
  
## ◆ makeBSpline

draftmake.make_bspline.makeBSpline =
[make_bspline](../../d5/d7f/group__draftmake.html#gae17b8880a5cbd21e6d2d33006d6e6fa8)  
---  
  
## ◆ makeCircle

draftmake.make_circle.makeCircle =
[make_circle](../../d5/d7f/group__draftmake.html#ga8010a7e29529e73931cd92c538291b37)  
---  
  
Referenced by
[Mod.PartDesign.PartDesignTests.TestInvoluteGear.TestInvoluteGear.testCustomizedGearProfile()](../../df/d7e/classMod_1_1PartDesign_1_1PartDesignTests_1_1TestInvoluteGear_1_1TestInvoluteGear.html#af8e24679c5eacf56554922f0aef2724b).

## ◆ makeDrawingView

def draftmake.make_drawingview.makeDrawingView =
[make_drawing_view](../../d5/d7f/group__draftmake.html#ga3048804d3459bb898e632560ad59687f)  
---  
  
## ◆ makeEllipse

draftmake.make_ellipse.makeEllipse =
[make_ellipse](../../d5/d7f/group__draftmake.html#gac417e9391cb09d94d5213f4a80c6530e)  
---  
  
## ◆ makeFacebinder

draftmake.make_facebinder.makeFacebinder =
[make_facebinder](../../d5/d7f/group__draftmake.html#ga278850e8b4a6e9ee4d07efbcfe3b4f8f)  
---  
  
## ◆ makeLine

draftmake.make_line.makeLine =
[make_line](../../d5/d7f/group__draftmake.html#ga84268745b00f160b3e33476e21f1bef6)  
---  
  
Referenced by
[femexamples.constraint_centrif.setup()](../../d1/def/namespacefemexamples_1_1constraint__centrif.html#a8714216d2d1b79c63ba3e4c52a742b4b),
[femexamples.constraint_transform_torque.setup()](../../d7/da4/namespacefemexamples_1_1constraint__transform__torque.html#a08d8ced26576b005f12a8632d88f53ed),
and
[femexamples.truss_3d_cs_circle_ele_seg3.setup()](../../da/d29/namespacefemexamples_1_1truss__3d__cs__circle__ele__seg3.html#a722938de133994bbcf6ae1eafa2bfec0).

## ◆ makePoint

draftmake.make_point.makePoint =
[make_point](../../d5/d7f/group__draftmake.html#ga94d6bea3b61d351b732fa1251b457c30)  
---  
  
## ◆ makePolygon

draftmake.make_polygon.makePolygon =
[make_polygon](../../d5/d7f/group__draftmake.html#ga087c000b1db0e3cac0785b367c341438)  
---  
  
## ◆ makeRectangle

draftmake.make_rectangle.makeRectangle =
[make_rectangle](../../d5/d7f/group__draftmake.html#ga49a72193cb54e734871a96fb23ed360d)  
---  
  
## ◆ makeShape2DView

draftmake.make_shape2dview.makeShape2DView =
[make_shape2dview](../../d5/d7f/group__draftmake.html#ga24d4bda57265196059d94eb35fd9140e)  
---  
  
## ◆ makeShapeString

draftmake.make_shapestring.makeShapeString =
[make_shapestring](../../d5/d7f/group__draftmake.html#gafa8400a76d9dc03ae691b0f532d1ff72)  
---  
  
## ◆ makeSketch

draftmake.make_sketch.makeSketch =
[make_sketch](../../d5/d7f/group__draftmake.html#gaaf5211b1c0c5f62d13897195ec2d1e6b)  
---  
  
Referenced by
[ArchWindowPresets.makeWindowPreset()](../../db/dc4/namespaceArchWindowPresets.html#a6d6fa631154f9cc526e7d9bab201b48d).

## ◆ makeWire

draftmake.make_wire.makeWire =
[make_wire](../../d5/d7f/group__draftmake.html#ga1a8f33557281f53792c6e201edc6f36c)  
---  
  
Referenced by
[femexamples.thermomech_flow1d.setup()](../../de/d40/namespacefemexamples_1_1thermomech__flow1d.html#a4189f8ec5b45f6645fcae656bef6882d).

## ◆ makeWorkingPlaneProxy

def draftmake.make_wpproxy.makeWorkingPlaneProxy =
[make_workingplaneproxy](../../d5/d7f/group__draftmake.html#gaaf46f35e0f52d2bfc88541c5c3c097c4)  
---  
  
## ◆ view_group

draftmake.make_layer.view_group = App.ParamGet("User
parameter:BaseApp/Preferences/View")  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

