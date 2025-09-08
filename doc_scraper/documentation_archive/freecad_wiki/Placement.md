---
url: https://wiki.freecad.org/Placement
title: Placement
scraped_at: 2025-09-08 16:42:38
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview Toggle Overview subsection
    * 1.1 Accessing the Placement Attribute
  * 2 Forms of Placement Toggle Forms of Placement subsection
    * 2.1 Angle, Axis and Position
    * 2.2 Position and Yaw, Pitch and Roll
    * 2.3 Matrix
  * 3 The Placement Dialog
  * 4 Examples
  * 5 Placement.Base vs Shape Definition
  * 6 Using "Center" to Control Axis of Rotation
  * 7 Using Placement in expressions
  * 8 Notes
  * 9 More

# Placement

  * [Page](/Placement "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Placement "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Placement)
  * [Edit](/index.php?title=Placement&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Placement&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Placement.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Placement&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Placement)
  * [Edit](/index.php?title=Placement&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Placement&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Placement&action=history)

General

  * [What links here](/Special:WhatLinksHere/Placement "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Placement "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Placement&oldid=1605035 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Placement&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Placement&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Placement&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Placement&language=&task=view "Start translation for this language")
  * [Deutsch](/Placement/de "Positionierung \(94% translated\)")
  * English
  * [Türkçe](/Placement/tr "Konum \(1% translated\)")
  * [español](/Placement/es "Placement \(14% translated\)")
  * [français](/Placement/fr "Placement \(100% translated\)")
  * [italiano](/Placement/it "Posizionamento \(89% translated\)")
  * [polski](/Placement/pl "Umiejscowienie \(100% translated\)")
  * [română](/Placement/ro "Plasament/Poziționare \(13% translated\)")
  * [čeština](/Placement/cs "Umístění \(2% translated\)")
  * [русский](/Placement/ru "Размещение \(3% translated\)")
  * [中文（中国大陆）](/Placement/zh-cn "方位 \(10% translated\)")
  * [日本語](/Placement/ja "Placement \(2% translated\)")
  * [한국어](/Placement/ko "배치\(Placement\) \(1% translated\)")

## Overview

**Placement** is how FreeCAD specifies the location and attitude (orientation)
of an object in space. Placement can be specified in multiple forms and
manipulated via [scripting](/Python_scripting_tutorial#Vectors_and_placements
"Python scripting tutorial"), the [property editor](/Property_editor "Property
editor") or selecting **Edit → Placement...** to open the [Placement task
panel](/Std_Placement "Std Placement").

### Accessing the Placement Attribute

An object's Placement attributes can be accessed and modified in 3 ways:

[![](/images/thumb/9/9a/PlacementPropertiesv10-800x800.png/600px-
PlacementPropertiesv10-800x800.png)](/index.php?title=File:PlacementPropertiesv10-800x800.png&filetimestamp=20250612182034&)

Placement in property editor

[![](/images/thumb/0/09/PlacePyConv10.png/600px-
PlacePyConv10.png)](/index.php?title=File:PlacePyConv10.png&filetimestamp=20250612182528&)

Scripting Placement as y/p/r and Matrix and its [API](/Placement_API
"Placement API")

[![](/images/2/20/PlacementDialogv10.png)](/index.php?title=File:PlacementDialogv10.png&filetimestamp=20250612182627&)

Placement task panel

## Forms of Placement

The placement is stored internally as a position and a rotation (rotation axis
and angle transformed into a
[quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)).
While there are several forms to specify a rotation, for instance with a
rotation center, this is only used to affect the rotation computation and is
not stored for later operations. Similarly, if a rotation axis of (1,1,1) is
specified, it may be normalized when stored in the quaternion and appear as
(0.58, 0.58, 0.58) when browsing the object later.

### Angle, Axis and Position

**Placement = [Angle, Axis, Position]**

The first form of **Placement** fixes an object's location in space with a
Position, and describes its orientation as a single rotation about an axis.

**Angle = r** is a scalar indicating the amount of rotation of the object
about **Axis**. Entered as degrees, but stored internally as radians.

**Axis = (ax,ay,az)** is a vector describing an axis of rotation (See Note
about axis of rotation). Examples are:

    
    
       (1,0,0)       ==> about **X** axis
       (0,1,0)       ==> about **Y** axis
       (0,0,1)       ==> about **Z** axis
       (0.71,0.71,0) ==> about the line **y=x**
    

Note that it is also possible to translate (move) an object along this axis of
rotation (axial motion) by entering the distance to move in the Axial: 0.0mm
[![](/images/0/0f/SpinBox.svg)](/index.php?title=File:SpinBox.svg&filetimestamp=20200327215243&)
spinbox and clicking Apply axial. (One way to envision axial motion is to
think of an airplane with a propeller spinning on its nose -- the propeller
spins _about_ an axis of rotation while the plane moves _along_ that same
axis.) The values in the vector can be thought of as the relative amount of
motion that will be applied in that direction. For example, in the y=x case
(0.71,0.71,0) the value contained in the Axial spinbox gets applied in equal
measure to the X and Y directions, but no movement happens in the Z direction.

**Position = (x,y,z)** is a Vector describing the point from which the
object's geometry will be calculated (in effect, a "local origin" for the
object). Note that in scripts, Placement.Base is used to denote the Position
component of a placement. The property editor calls this value **Position**
and the Placement task panel calls it **Translation**.

### Position and Yaw, Pitch and Roll

[![](/images/thumb/e/e7/PlacementDialogv10b.png/300px-
PlacementDialogv10b.png)](/index.php?title=File:PlacementDialogv10b.png&filetimestamp=20250612183121&)

Placement task panel: Euler angles
[![](/images/0/0e/ComboBox.svg)](/index.php?title=File:ComboBox.svg&filetimestamp=20200329183052&)
selected

**Placement = [Position, Yaw-Pitch-Roll]**

The second form of **Placement** fixes an object's location in space with a
**Position** (as in the first form), but describes its orientation using [Yaw,
Pitch and Roll angles](https://en.wikipedia.org/wiki/Yaw,_pitch,_and_roll).
These angles are sometimes referred to as [Euler
angles](https://en.wikipedia.org/wiki/Euler_angles) or Tait-Bryan angles. Yaw,
Pitch and Roll are common aviation terms for a body's orientation (or
attitude).

**Position = (x,y,z)** is a Vector describing the point from which the
object's geometry will be calculated (in effect, a "local origin" for the
object).

**Yaw-Pitch-Roll = (y,p,r)** is a tuple that specifies the attitude of the
object. Values for y,p,r specify degrees of rotation about each of the z,y,x
axis (see note).

    
    
    >>> App.ActiveDocument.Cylinder.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
    

App.Rotation(10,20,30) = Euler Angle

**Yaw** = 10 degrees (**Z**)

**Pitch** = 20 degrees (**Y**)

**Roll** = 30 degrees (**X**)

  

[![](/images/1/12/Tache_Placement_Lacet_fr_Mini.gif)](/index.php?title=File:Tache_Placement_Lacet_fr_Mini.gif&filetimestamp=20230821091157&)

**Yaw** is the rotation about the **Z axis** , that is to say a rotation from
left to right.  
(The yaw angle is the **Psi ψ**).

[![](/images/7/7a/Tache_Placement_Tangage_fr_Mini.gif)](/index.php?title=File:Tache_Placement_Tangage_fr_Mini.gif&filetimestamp=20121116135634&)

**Pitch** is rotation about the **Y axis** , that is to say nose-up and nose-
down.  
(The Pitch angle is the **Phi φ**).

[![](/images/c/c0/Tache_Placement_Roulis_fr_Mini.gif)](/index.php?title=File:Tache_Placement_Roulis_fr_Mini.gif&filetimestamp=20121116135119&)

**Roll** is rotation about the **X axis** , that is to say wing up and down.  
(The Roll angle is the **Thêta θ**).

### Matrix

**Placement = Matrix**

The third form of **Placement** describes the object's position and
orientation with a 4x4 affine transformation matrix ([Affine
Transformation](https://en.wikipedia.org/wiki/Affine_transformation)).

**Matrix** =

    
    
      ((r11,r12,r13,t1),
       (r21,r22,r23,t2),
       (r31,r32,r33,t3),
       (0,0,0,1)) , with rij specifying rotation and ti specifying translation.
    

## The Placement Dialog

The Placement Dialog is invoked from the **Edit** menu. It is used to
precisely rotate/translate objects. It is also used when we need to create a
sketch on a "non standard" plane or change a sketch's orientation to a new
plane.

  * The **Translation** section adjusts the object's location in space.
  * The **Center** section adjusts the rotational axis to one that does not pass through the object's reference point.
  * The **Rotation** section adjusts the rotational angle(s) and the method of specifying those angles.

But while the elements within each section generally apply to the purpose of
that section there are also some elements in one section that can affect
elements in another section. For example, clicking the Selected points button
in the **Center** section with 2 points selected in the 3d view results in not
only populating the **Center** coordinate spinboxes with the coordinates of
the midpoint between those 2 selected points, but it also creates a custom
axis along the line defined by those 2 selected points in the **Rotation**
section. In another example, placing a value in the Axial spinbox and clicking
the Apply axial button in the **Translation** section translates (moves) the
object along the axis defined in the **Rotation** section.

The **Apply incremental changes to object placement** tick box is useful when
translations/rotations are to be made relative the object's current
position/attitude, rather than to the original position/attitude. Ticking this
box resets the dialogue input fields to zero, but does not change the object's
orientation or location. Subsequent entries do change the
orientation/location, but are applied from the object's current position.
Enabling this checkbox is also useful when using the Selected points button as
it can sometimes prevent undesired placement changes.

PS: since version 0.17 introduce new object Part, this object have his
placement, and the Placement object created in the Part object is incremented
with the Part Placement. [introduced in 0.17](/Release_notes_0.17 "Release
notes 0.17")

To obtain the Part Placement use this code:

    
    
    import Draft, Part
    sel = FreeCADGui.Selection.getSelection()
    print(sel[0].Placement)
    print(sel[0].getGlobalPlacement())   # return the GlobalPlacement
    print(sel[0].getParentGeoFeatureGroup()) # return the GeoFeatureGroup, ex:  Body or a Part.
    print("____________________")
    

**Selected points** button is used to populate the coordinates in the
**Center** coordinates spinboxes and (when 2 or 3 points are selected)
additionally to create a custom (user-defined) axis of rotation in the
**Rotation** section. A point can be a vertex, but it can also be any point
along an edge or on a face. When you select an edge or face the entire edge or
face is selected, but FreeCAD also remembers which point on that face or edge
the mouse pointer was hovering over when that edge or face was selected. It is
this point's coordinates that get used in the Placement dialog when the
**Selected points** button is clicked. You might be thinking this isn't a very
precise way of selecting a point, and you are correct, but in many cases it is
sufficient that the point selected is guaranteed to be on that edge or face.
In cases where you need to precisely designate a point to be used you should
select a vertex. When there is no vertex in the desired location consider
creating one, perhaps in a temporary sketch attached to that face or edge,
perhaps using a Draft workbench object, such as a line or point, etc.

Let us first consider the simple case of selecting 1 point. The workflow is to
first select the desired point, then click the **Selected points** button. The
coordinates of the selected point will be used to populate the X, Y, and Z
spinboxes within the **Center** section. Now any rotation done on the object
will about this center of rotation.

Now consider the case of selecting 2 points. You would select the 2 desired
points, and then click the **Selected points** button. The coordinates of the
midpoint between the 2 selected points get placed into the X, Y, and Z
spinboxes within the **Center** section. Now any rotation done on the object
will be about this center of rotation. But in addition to setting up the
**Center** section coordinates a custom (user-defined) axis is also added to
the **Axis** element within the **Rotation** section. (Note: if you were in
Euler rotation mode, the mode gets switched to Rotation with an axis mode and
the new custom axis is selected as the current axis of rotation.) Now any
rotation done using the new custom axis will be about this axis of rotation.
As an added bonus, the distance is measured between the 2 selected points, and
this information is given in the Report View. (Note: Hold down the Shift key
while clicking the **Selected points** button to copy the distance measurement
to the clipboard.) By entering this distance into the Axial spinbox in the
**Translation** section and clicking the **Apply axial** button you can
translate (move) the object so that the first selected point now occupies the
coordinates occupied by the second selected point (at the time the **Selected
points** button was clicked).

Now consider the case of selecting 3 points. You would select the 3 desired
points, and then click the **Selected points** button. The coordinates of the
first selected point (order of selection is very important here) get placed
into the X, Y, and Z spinboxes within the **Center** section. Since 3 points
define a plane FreeCAD is able to take advantage of that and use those 3
points to create a new custom (user-defined) axis of rotation that is normal
(perpendicular) to that defined plane. As with 2 selected points, the distance
between points is also shown in the Report View, but this time it is the
distance between the 2nd and 3rd selected points. (Note: Hold down the Shift
key while clicking **Selected points** button -- Shift + Click -- to copy the
angle measurement to the clipboard.) Additionally, the angle between the 2nd
and 3rd points is also measured and displayed in the Report View. By entering
this angle into the **Angle** spinbox within the **Rotation** section we can
very precisely rotate the object such that now the 2nd selected point is in
alignment with the coordinates occupied by the 3rd selected point. (Note: you
might want to increase the number of digits used within the Edit menu ->
Preferences -> General -> Units -> Number of decimals spinbox if you desire
more precision.)

## Examples

Rotations about a single axis:

[![Before Rotation](/images/thumb/9/96/RotationAboutZBefore.png/600px-
RotationAboutZBefore.png)](/index.php?title=File:RotationAboutZBefore.png&filetimestamp=20250612183759&
"Before Rotation")Before Rotation

Before Rotation (top view)

[![After Rotation about Z](/images/thumb/e/e2/RotationAboutZAfter.png/600px-
RotationAboutZAfter.png)](/index.php?title=File:RotationAboutZAfter.png&filetimestamp=20250612183838&
"After Rotation about Z")After Rotation about Z

After Rotation about Z (top view)

[![After Rotation about
y=x](/images/thumb/b/bd/RotationAboutYXAfter.png/600px-
RotationAboutYXAfter.png)](/index.php?title=File:RotationAboutYXAfter.png&filetimestamp=20250612184005&
"After Rotation about y=x")After Rotation about y=x

After Rotation about y=x (right view)

Rotation with offset centre point:

[![Before Rotation](/images/thumb/2/21/RotationOffsetBefore.png/600px-
RotationOffsetBefore.png)](/index.php?title=File:RotationOffsetBefore.png&filetimestamp=20250612184156&
"Before Rotation")Before Rotation

Before Rotation (top view)

[![After Rotation about Z](/images/thumb/7/71/RotationOffsetAfter.png/600px-
RotationOffsetAfter.png)](/index.php?title=File:RotationOffsetAfter.png&filetimestamp=20250612184246&
"After Rotation about Z")After Rotation about Z

After Rotation about Z (top view)

Rotation using Euler angles:

[![Before Rotation](/images/thumb/c/c6/RotationEulerBefore.png/600px-
RotationEulerBefore.png)](/index.php?title=File:RotationEulerBefore.png&filetimestamp=20250612184408&
"Before Rotation")Before Rotation

Before Rotation

[![After Rotation](/images/thumb/c/c4/RotationEulerAfter.png/600px-
RotationEulerAfter.png)](/index.php?title=File:RotationEulerAfter.png&filetimestamp=20250612184452&
"After Rotation")After Rotation

After Rotation

## Placement.Base vs Shape Definition

Placement is not the only way to position a shape in space. Note the Python
console in this image:

[![](/images/thumb/b/be/2Placements800.png/900px-2Placements800.png)](/index.php?title=File:2Placements800.png&filetimestamp=20250612185218&)

2 Shapes with the Same Placement

Both cubes have the same value for Placement, but are in different locations!
This is because the 2 shapes are defined by different vertices (curves in more
complex shapes). For the 2 shapes in the above illustration:

    
    
     >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
     >>> for v in ev: print(v.X,",",v.Y,",",v.Z)
     ...
     0.0,0.0,0.0
     0.0,0.0,10.0
     10.0,0.0,0.0
     10.0,0.0,10.0
     10.0,10.0,0.0
     10.0,10.0,10.0
     0.0,10.0,0.0
     0.0,10.0,10.0
     >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
     >>> for v in e1v: print(v.X,",",v.Y,",",v.Z)
     ...
     20.0,30.0,0.0
     20.0,30.0,10.0
     20.0,20.0,0.0
     20.0,20.0,10.0
     30.0,20.0,0.0
     30.0,20.0,10.0
     30.0,30.0,0.0
     30.0,30.0,10.0
     >>>
    

The Vertices (or Vectors) that define the shape use the Placement.Base
attribute as their origin. So if you want to move a shape 10 units along the
**X** axis, you could add 10 to the **X** coordinates of all the Vertices or
you could set Placement.Base to (10,0,0).

## Using "Center" to Control Axis of Rotation

By default, the axis of rotation isn't really the x/y/z axis. It is a line
parallel to the selected axis, but passing through the reference point
(Placement.Base) of the object to be rotated. This can be changed by using the
Center fields in the Placement dialog or, in scripts, by using the Center
parameter of the FreeCAD.Placement constructor.

For example, suppose we have a box (below) positioned at (20,20,10).

[![](/images/3/34/LocalZBefore2.png)](/index.php?title=File:LocalZBefore2.png&filetimestamp=20130420144151&)Before
Rotation

We wish to spin the box around it's own vertical centre line (ie local Z),
while keeping it the same position. We can easily achieve this by specifying a
Center value equal to the coordinates of the box's central point (25,25,15).

[![](/images/5/59/LocalZAfter2.png)](/index.php?title=File:LocalZAfter2.png&filetimestamp=20130420144250&)After
Rotation

In a script, we would do:

    
    
    import FreeCAD
    obj = App.ActiveDocument.Box                       # our box
    rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)   # 45° about Z
    #rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
    #rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X)
    centre = FreeCAD.Vector(25,25,15)                  # central point of box
    pos = obj.Placement.Base                           # position point of box
    newplace = FreeCAD.Placement(pos,rot,centre)       # make a new Placement object
    obj.Placement = newplace                           # spin the box
    

Same script with the file example
[RotateCoG2.fcstd](https://forum.freecad.org/download/file.php?id=1651)
(discussion on the
[forum](https://forum.freecad.org/viewtopic.php?f=3&t=3950#p31052))

    
    
    import FreeCAD
    obj = App.ActiveDocument.Extrude                    # our box
    rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)    # 45 about Z
    #rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)    # 45° about X and 45° about Z
    #rot = FreeCAD.Rotation(10,20,30)                    # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X)
    centre = FreeCAD.Vector(25,25,0)                    # "centre" of rotation (where local Z cuts XY)
    pos = obj.Placement.Base                            # original placement of obj
    newplace = FreeCAD.Placement(pos,rot,centre)        # make a new Placement object
    obj.Placement = newplace                            # spin the box
    

## Using Placement in expressions

In expressions it is possible to use the components of the placement for
example to access the x-component of the object labeled "Cube":

    
    
    <<Cube>>.Placement.Base.x
    

You can access the angle of the rotation by

    
    
    <<Cube>>.Placement.Rotation.Angle
    

The axis of rotation can be accessed with

    
    
    <<Cube>>.Placement.Rotation.Axis.x
    <<Cube>>.Placement.Rotation.Axis.y
    <<Cube>>.Placement.Rotation.Axis.z
    

where often one of these values is 1 while the others are 0.

You can also use the whole Placement in a single expression:

Right click on Placement property in the property editor, select "show hidden"
then extra properties will show. If you then right click on Placement again
the context menu will include Expression, select Expression then the
Expression dialogue will open and whatever you type will go into the Placement
property rather than its child properties.

To make the placement of "Sketch" equal to that of "Cylinder", you would enter
in that way for Sketch the expression

    
    
    <<Cube>>.Placement
    

[![](/images/a/ab/PlacementInExpression.png)](/index.php?title=File:PlacementInExpression.png&filetimestamp=20201113010932&)Setting
the whole Placement in one expression

**NOTE:** It's also possible to _create_ Placement objects in expressions. See
the [Expressions](/Expressions#Object_creation_functions "Expressions") page
for details.

## Notes

  * The Placement properties in the Data tab are disabled for objects which are attached to some other object. The Attachment Offset has to be edited instead.
  * Axis and Angle can also be expressed as a [quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation).
  * The reference point of an object varies depending on the object. Some examples for common objects:

Object | Reference Point   
---|---  
Part.Box | left (minx), front (miny), bottom (minz) vertex   
Part.Sphere | center of the sphere (ie centre of bounding box)   
Part.Cylinder | center of the bottom face   
Part.Cone | center of bottom face (or apex if bottom radius is 0)   
Part.Torus | center of the torus   
Features derived from Sketches | the Feature inherits the Position of the underlying Sketch. Sketches always start with Position = (0,0,0). This position corresponds to the origin in the sketch.   
  
## More

  * This tutorial: [Aeroplane](/Aeroplane "Aeroplane") covers the mechanics of changing an object's Placement extensively.
  * This [FreeCAD News article](https://blog.freecad.org/2023/01/16/the-rotation-api-in-freecad/?preview_id=343) discusses the Rotation API.

  

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

