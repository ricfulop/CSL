---
url: https://wiki.freecad.org/Creating_a_simple_part_with_Part_WB
title: Creating a simple part with Part WB
scraped_at: 2025-09-08 16:43:06
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction Toggle Introduction subsection
    * 1.1 The tutorial covers
  * 2 The model to make
  * 3 Using the Part Workbench to create and manipulate the primitive building blocks Toggle Using the Part Workbench to create and manipulate the primitive building blocks subsection
    * 3.1 Create the main solid block
    * 3.2 Create the fillet
    * 3.3 Visibility of children
    * 3.4 Create the chamfer
      * 3.4.1 Python console
      * 3.4.2 Expressions
      * 3.4.3 The toolbars
      * 3.4.4 The measurement tool
    * 3.5 Create the hole
  * 4 Changing the color and transparency
  * 5 A different way to locate the hole
  * 6 Making the hole a countersunk hole
  * 7 Making a hollow piece
  * 8 A different way to position the chamfer
  * 9 Editing dimensions, face colors and TNP Toggle Editing dimensions, face colors and TNP subsection
    * 9.1 Reposition the cylinder
    * 9.2 Fixing the colors
    * 9.3 Multiple solids
    * 9.4 TNP
  * 10 Organizing the tree a bit differently
  * 11 Wrapping up

# Creating a simple part with Part WB

  * [Page](/Creating_a_simple_part_with_Part_WB "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Creating_a_simple_part_with_Part_WB&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Creating_a_simple_part_with_Part_WB)
  * [Edit](/index.php?title=Creating_a_simple_part_with_Part_WB&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Creating_a_simple_part_with_Part_WB&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Creating_a_simple_part_with_Part_WB.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Creating_a_simple_part_with_Part_WB&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Creating_a_simple_part_with_Part_WB)
  * [Edit](/index.php?title=Creating_a_simple_part_with_Part_WB&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Creating_a_simple_part_with_Part_WB&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Creating_a_simple_part_with_Part_WB&action=history)

General

  * [What links here](/Special:WhatLinksHere/Creating_a_simple_part_with_Part_WB "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Creating_a_simple_part_with_Part_WB "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Creating_a_simple_part_with_Part_WB&oldid=1536391 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Creating_a_simple_part_with_Part_WB&action=info "More information about this page")

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Creating_a_simple_part_with_Part_WB&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Creating+a+simple+part+with+Part+WB&action=page&filter=&language=en)This is
the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Creating+a+simple+part+with+Part+WB&language=&task=view "Start translation for this language")
  * [Deutsch](/Creating_a_simple_part_with_Part_WB/de "Erstellen eines einfachen Bauteils mit dem Arbeitsbereich Part \(100% translated\)")
  * English
  * [français](/Creating_a_simple_part_with_Part_WB/fr "Créer une simple pièce avec l'atelier Part \(100% translated\)")
  * [italiano](/Creating_a_simple_part_with_Part_WB/it "Creazione di una parte semplice con l'Ambiente Part \(1% translated\)")
  * [polski](/Creating_a_simple_part_with_Part_WB/pl "Środowisko Część: Tworzenie prostej części \(100% translated\)")
  * [português do Brasil](/Creating_a_simple_part_with_Part_WB/pt-br "Criando uma peça simples com a bancada Part \(100% translated\)")
  * [русский](/Creating_a_simple_part_with_Part_WB/ru "Создание простой детали в верстаке Part \(100% translated\)")

![](/images/0/06/Freecad.svg) Tutorial  
---  
Topic  
Modeling  
Level  
Beginner  
Time to complete  
2 hours  
Authors  
heda  
FreeCAD version  
0.19 or above  
Example files  
See also  
[Creating a simple part with
PartDesign](/Creating_a_simple_part_with_PartDesign "Creating a simple part
with PartDesign"), [Creating a simple part with Draft and Part
WB](/Creating_a_simple_part_with_Draft_and_Part_WB "Creating a simple part
with Draft and Part WB")  
  
  
  
## Introduction

This tutorial aims to be used as a first introduction to 3D modeling using the
[Part Workbench](/Part_Workbench "Part Workbench")
[![](/images/1/1a/Switch_PartWorkbench.JPG)](/index.php?title=File:Switch_PartWorkbench.JPG&filetimestamp=20170227183926&)
of FreeCAD. After having finished this tutorial you should be able to make
simple 3D models by using primitives like cubes, cylinders, etc with a
technique called [Constructive Solid
Geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry), short
**CSG** modeling. Another way to create 3D models is by using a 2D shape by
for example extruding or revolving the 2D shape in 3D space. For an
introduction of that technique please follow the sister-tutorial _[Creating a
simple part with PartDesign](/Creating_a_simple_part_with_PartDesign "Creating
a simple part with PartDesign")_. The two tutorials intentionally have exactly
the same model generated, this presents the beginner with a hands on
experience of the two different techniques and how they are implemented in
FreeCAD. The definition of the two techniques can be viewed as strictly
divided from a semantic point of view, however there is nothing directly
hindering a mix of the techniques when creating models. There are some caveats
to watch out for when mixing modeling techniques, those are mainly related to
aspects of how FreeCAD is programmed. There is a [third
tutorial](/Creating_a_simple_part_with_Draft_and_Part_WB "Creating a simple
part with Draft and Part WB") intended as a first introduction to a mixed
modeling example. That tutorial uses the **Draft Workbench** to create a 2D
profile utilized to extrude a solid in the **Part Workbench** to make the same
model as in this tutorial.

Before you start please have a look at how to **[navigate](/Mouse_navigation
"Mouse navigation")** in 3D space. When hoovering over the mouse model
selector in the lower right corner of the FreeCAD window, a cheat-sheet of the
current mouse model appears as in the picture below.

[![](/images/2/2c/T101pwb00-01_navi.png)](/index.php?title=File:T101pwb00-01_navi.png&filetimestamp=20220605095910&)

Many newcomers to CAD programs get stuck while learning the software, if that
happens to you, please go ahead and search the wiki or forum for further
information – chances are that others also have been stuck on the same
specific thing in the past so there is already an answer to your specific
question. Or make a post on the forum with your questions or findings. The
forum has several threads where users are helped to complete all sorts of
different tasks, those threads are often similar to tutorials, and often have
specific illustrations included.

### The tutorial covers

  * The model to make
  * Using the Part Workbench to create and manipulate the primitive building blocks
  * Changing the color and transparency
  * A different way to locate the hole
  * Making the hole a countersunk hole
  * Making a hollow piece
  * A different way to position the chamfer
  * Editing dimensions
  * Organizing the tree a bit differently
  * Wrapping up

## The model to make

[![](/images/thumb/c/ce/GGTuto1_Vue.PNG/372px-
GGTuto1_Vue.PNG)](/index.php?title=File:GGTuto1_Vue.PNG&filetimestamp=20180404144733&)
[![](/images/4/47/T101pwb01-02_dims.png)](/index.php?title=File:T101pwb01-02_dims.png&filetimestamp=20220605100016&)

## Using the Part Workbench to create and manipulate the primitive building
blocks

Create a new document and save it directly under a new name, it is good
practice to make sure that you save the document at regular intervals, or just
before larger operations. Then switch to the **[Part
Workbench](/Part_Workbench "Part Workbench")** using either the [workbench
selector](/Getting_started#Exploring_the_interface "Getting started") (labeled
10 in the linked image) or by going to the **View → Workbench** menu. FreeCAD
will start with toolbars at the top, the combo view to the left and the 3D
view at the right.

### Create the main solid block

Press [![](/images/3/34/Part_Box.svg)](/Part_Box "Part Box") [Box](/Part_Box
"Part Box") to make a default solid cube. The cube appears in the [3D
view](/3D_view "3D view") and also as a new object in the [Tree
view](/Tree_view "Tree view") in the sidebar.

Press [![](/images/b/b1/Std_ViewIsometric.svg)](/Std_ViewIsometric "Std
ViewIsometric") [Isometric](/Std_ViewIsometric "Std ViewIsometric") to see the
cube in 3D.

[![](/images/7/70/T101pwb01-03_cube1.png)](/index.php?title=File:T101pwb01-03_cube1.png&filetimestamp=20220605100125&)

Select the cube in the [Tree view](/Tree_view "Tree view"), it becomes green
in the 3D view. Below the tree view you will now see that the cube by default
is created with the dimensions **Length x Width x Height** as _10 x 10 x 10
mm_. Change those dimensions to **100 x 30 x 50** as per the initial drawing
of the model.

[![](/images/c/c1/T101pwb01-04_cubedims.png)](/index.php?title=File:T101pwb01-04_cubedims.png&filetimestamp=20220605100146&)

When changing a property, like _Length_ through the spinbox, one can either
enter the values, or use the scroll-wheel to tick values up or down. The
arrows for ticking values up or down can of course also be used. In the right
most picture above, the _Height_ property is in edit mode, rolling the scroll
wheel when the mouse is over that cell will change the value by one up or
down.

Click [![](/images/6/66/Std_ViewFitAll.svg)](/Std_ViewFitAll "Std ViewFitAll")
**[Fit all](/Std_ViewFitAll "Std ViewFitAll")** to see the whole cube.

[![](/images/2/29/T101pwb01-05_cube2.png)](/index.php?title=File:T101pwb01-05_cube2.png&filetimestamp=20220605100204&)

### Create the fillet

To make the filleted corner, in the toolbar press
[![](/images/3/30/Part_Fillet.svg)](/Part_Fillet "Part Fillet")
**[Fillet](/Part_Fillet "Part Fillet")** which opens the _task panel_ for
fillets in the [combo view](/Combo_view "Combo view") to the side. Change the
_radius_ spinbox to 20 mm, then in the 3D view, select the width edge to the
upper right and click OK.

[![](/images/f/fb/T101pwb01-06_filletrad.png)](/index.php?title=File:T101pwb01-06_filletrad.png&filetimestamp=20220605100233&)

The _task panel_ closes and you are back to the Tree view which now has a
fillet object instead of the earlier cube.

### Visibility of children

Click the plus sign/caret to expand the children of the fillet, which in this
case is the _cube_ we created earlier, but it is grayed out. Select the cube
and press the space bar – this toggles visibility so the cube is now visible
again and the icon is no longer grayed out. To deselect the cube click in a
blank area in the Tree view or the 3D view.

[![](/images/8/81/T101pwb01-07_fillet.png)](/index.php?title=File:T101pwb01-07_fillet.png&filetimestamp=20220605100253&)

### Create the chamfer

Next is to create the 30 degree _chamfer_ , start by toggling the visibility
of the child cube of the fillet. There is a chamfer tool in [Part
Workbench](/Part_Workbench "Part Workbench"), but instead of using it we will
make the chamfer with another block and a boolean cut.

Create a new [![](/images/3/34/Part_Box.svg)](/Part_Box "Part Box")
**[Box](/Part_Box "Part Box")** with dimensions 60 x 30 x 30. Change the
**placement angle** to -30 degrees.

[![](/images/d/d0/T101pwb01-08_chamfer1.png)](/index.php?title=File:T101pwb01-08_chamfer1.png&filetimestamp=20220605100310&)

The placement angle is using the **placement vector** (Axis) as axis of
rotation. The default is the z-axis, which is not matching our target
direction, changing the placement vector to the **y-axis** produces the
desired orientation of the cutting tool for the chamfer.

[![](/images/1/14/T101pwb01-09_chamfer2.png)](/index.php?title=File:T101pwb01-09_chamfer2.png&filetimestamp=20220605100325&)

The same placement can be attained with other values as well, the simplest
alternative example of a placement that is the same is an angle of +30 degrees
and a y-axis of -1.

#### Python console

Furthermore the position needs to be adjusted, looking at the drawing of the
finished part, there is no direct dimension to use for the intended
translation upwards. Since the upward dimension is the one needed, we have to
calculate it. Let’s make use of the built in **[Python
console](/Python_console "Python console")** for those calculations, it is
basic trigonometry. If the FreeCAD Python console is not visible for you, just
right-click in an empty space in the toolbar area and check the _Python
console_ and it should appear in the workspace, when there you should as well
add the **[report view](/Report_view "Report view")** if not already visible.
The _report view_ most of the times provides useful information or even hints
of what to do next for different commands.

[![](/images/c/cf/T101pwb01-10_pyconsole.png)](/index.php?title=File:T101pwb01-10_pyconsole.png&filetimestamp=20220605100353&)

After importing the
**[math](https://docs.python.org/3/library/math.html#module-math)** module
from the standard libraries in python we can use the formula _(50 -
math.tan(math.radians(30)) * 50)_ to find the distance in z-direction that the
block should be moved. Copy the result of the formula from the Python console
and paste it into the z position for **Cube001**. The _tool_ to use for the
chamfer _cut_ is now properly oriented and positioned.

[![](/images/9/97/T101pwb01-11_chamfer3.png)](/index.php?title=File:T101pwb01-11_chamfer3.png&filetimestamp=20220605100410&)

#### Expressions

One does not have to use the Python console to do the calculation, In most
cases when dealing with numeric parametric values, FreeCAD has a short-cut to
a built-in calculator. It is called **[Expressions](/Expressions
"Expressions")** in FreeCAD, you can enter the _expression mode_ by first
clicking in the spinbox for the z-position, a small blueish circular icon will
appear at the right side.

[![](/images/5/5e/T101pwb01-12_expression1.png)](/index.php?title=File:T101pwb01-12_expression1.png&filetimestamp=20220605100429&)

Clicking that icon opens new window _Formula editor_ where formulas and
expressions can be entered as shown below. Using expressions is a powerful
tool, since one can access parameters from the model, effectively making all
parameters in the model available as variables to be used when creating an
expression. In short, in our formula, instead of entering the number 50 when
in the formula editor, we could enter a _named parameter_ holding the value 50
from the cube, with the benefit that if we change the cube _height_ , the
position of the chamfer will automatically follow. The value of 50 in the
current model is referred to as _Cube.Length_ , i.e. the _Length_ property of
the _Cube_ feature. Further information on this can be found on the wiki.

[![](/images/5/59/T101pwb01-13_expression2.png)](/index.php?title=File:T101pwb01-13_expression2.png&filetimestamp=20220605100448&)

To make the cut, with the Ctrl key pressed down first select the **Fillet** in
the Tree view and then the latest created cube (named **Cube001**) and finally
in the toolbar press the [![](/images/f/fb/Part_Cut.svg)](/Part_Cut "Part
Cut") **[Cut](/Part_Cut "Part Cut")** button. Your Tree view should now again
be a single object in the root called **Cut**.

[![](/images/3/3d/T101pwb01-14_model1.png)](/index.php?title=File:T101pwb01-14_model1.png&filetimestamp=20220605100514&)

#### The toolbars

A sidenote on the toolbars, since they are the typical avenue to invoke
commands. Although there is a basic setting for the layout of the toolbars,
the actual layout on your computer could turn out to be less than ideal. In
such cases it is easy to adjust. Consider the upper section of the below
image. There are two rows of toolbars and only a limited number of the [Part
Workbench](/Part_Workbench "Part Workbench") toolbar buttons are visible. The
simplest way to see more toolbar buttons is to maximize the FreeCAD window,
unless it already is maximized of course.

More common is to adjust the layout of the toolbars to suit your needs and
your specific computer. The repositioning is done with the handle on the left
of each toolbar. You can just click and drag the handle to a new location. In
the lower section of the below image the toolbar positions have been adjusted,
revealing their full content. Changes to toolbar positions are persistent
through sessions.

[![](/images/c/cc/T101pwb01-141_toolbars.png)](/index.php?title=File:T101pwb01-141_toolbars.png&filetimestamp=20220801140324&)

#### The measurement tool

The **[measurement tool](/Part_Workbench#Measure "Part Workbench")** in the
**Part Workbench** can be used to check that our calculation and placement of
the chamfer is correct. Press the
[![](/images/c/c7/Part_Measure_Linear.svg)](/Part_Measure_Linear "Part Measure
Linear") **[Measure Linear](/Part_Measure_Linear "Part Measure Linear")**
button and a _task panel_ opens up, then select the 2 endpoints of one side of
the chamfer.

[![](/images/7/7e/T101pwb01-15_model1measure1.png)](/index.php?title=File:T101pwb01-15_model1measure1.png&filetimestamp=20220605100548&)

It checks out with an x dimension of 50 mm, clear the measurement and close
the dialogue.

### Create the hole

To make the hole, press the
[![](/images/e/e8/Part_Cylinder.svg)](/Part_Cylinder "Part Cylinder")
**[Cylinder](/Part_Cylinder "Part Cylinder")** button, set the _radius_ to 5
mm and _height_ to 50 mm.

[![](/images/5/5d/T101pwb01-16_cyl1.png)](/index.php?title=File:T101pwb01-16_cyl1.png&filetimestamp=20220605100603&)

Next we need to position the hole according to the dimensions in the drawing.
Change the view to [![](/images/b/bd/Std_ViewTop.svg)](/Std_ViewTop "Std
ViewTop") **[Top](/Std_ViewTop "Std ViewTop")** view, then right-click the
**Cylinder** in the Tree view and select **Transform** from the pop-up menu.

[![](/images/7/76/T101pwb01-17_cyl1translate.png)](/index.php?title=File:T101pwb01-17_cyl1translate.png&filetimestamp=20220605100621&)

Change the _Translation increment_ to 5 and use the red and green arrow to
position the cylinder in the right position, moving it 15 mm in y and 65 in x
by dragging the arrow ends with the mouse. Click OK to close the _Transform_
dialogue. To make the hole press the Ctrl key and select the **Cut** and
**Cylinder** in the Tree view, then press the
[![](/images/f/fb/Part_Cut.svg)](/Part_Cut "Part Cut") **[Cut](/Part_Cut "Part
Cut")** button in the toolbar. Your Tree view should once again have a single
object in the root called **Cut001**.

Congratulations, the model is now ready.

[![](/images/1/1e/T101pwb01-18_model1complete.png)](/index.php?title=File:T101pwb01-18_model1complete.png&filetimestamp=20220605100640&)

With the basic model ready, let us explore different ways to alter this model,
some examples are related to the appearance, additional features, or simply a
different way to do the same.

## Changing the color and transparency

There are several different ways one can change the appearance of objects, for
this case, let's use the view tab in the property part of the combo view.
First select the object in the Tree view and then edit any property like line
color, shape color or transparency via the **view tab** (found at the bottom
of the _combo view_).

[![](/images/6/66/T101pwb02-01_appearance1.png)](/index.php?title=File:T101pwb02-01_appearance1.png&filetimestamp=20220605100705&)

Unfortunately when the object is selected it is a bit hard to see how it will
look when tuning the new appearance. To see the final result one has to
deselect the object. Here is the new look of the model, where one now can see
the through hole also in the iso-view. Another way to edit the appearance is
via the **View →[![](/images/d/da/Std_SetAppearance.svg)](/Std_SetAppearance
"Std SetAppearance") Appearance...** menu.

[![](/images/7/78/T101pwb02-02_appearance2.png)](/index.php?title=File:T101pwb02-02_appearance2.png&filetimestamp=20220605100725&)

## A different way to locate the hole

Do a _save-as_ under a new name. Then delete the cut that added the hole and
move the cylinder back to zero position. Your model should look like the below
picture, which is the starting point for using a different technique to locate
the hole at the center of the upper face. Note that the color is back to the
default gray, the change in appearance we did was on the cut object which now
is deleted.

[![](/images/1/1f/T101pwb03-01_cyl.png)](/index.php?title=File:T101pwb03-01_cyl.png&filetimestamp=20220605100745&)

This time the [![](/images/9/91/Workbench_Draft.svg)](/Draft_Workbench "Draft
Workbench") **[Draft Workbench](/Draft_Workbench "Draft Workbench")** will be
used to locate the hole. The hole is as before to be located at the center of
the upper face, which is the same as the midpoint of the diagonal of the upper
face.

Start by switching the workbench to **Draft** , it might be that a _grid_
appears in the 3D view, the grid visibility can be toggled with
[![](/images/c/c9/Draft_ToggleGrid.svg)](/Draft_ToggleGrid "Draft ToggleGrid")
[Toggle Grid](/Draft_ToggleGrid "Draft ToggleGrid") in the toolbar. When
making use of the **[snap](/Draft_Snap "Draft Snap")** functionality in the
**Draft Workbench** it helps to only have the _snap types_ of interest
enabled. This time it is sufficient to leave _endpoint, midpoint and circle
center enabled_ , so the settings for snapping should look something like
below.

[![](/images/6/6f/T101pwb03-02_snap.png)](/index.php?title=File:T101pwb03-02_snap.png&filetimestamp=20220605100759&)

Finding the point to place the center of the cylinder could be done by making
a diagonal as helpline and use the center of the cylinder and midpoint of the
diagonal to identify the points to move between, however it turns out that we
do not even need to make any helplines, we can snap on already existing solid
geometry.

Select the **Cylinder** in the Tree view (it turns green in the 3D view) and
press the [![](/images/3/3c/Draft_Move.svg)](/Draft_Move "Draft Move")
**[Move](/Draft_Move "Draft Move")** button in the toolbar. A _task panel_
opens for moving objects, make sure that _Copy_ is unchecked.

[![](/images/1/1a/T101pwb03-03_move.png)](/index.php?title=File:T101pwb03-03_move.png&filetimestamp=20220605100828&)

Then move the mouse to the upper face of the cylinder so that you see a _white
dot_ in the center of the circle as per the left picture below, this together
with the center symbol next to the mouse pointer means that a left button
mouse click will snap to the white point.

[![](/images/6/67/T101pwb03-04_snapselect.png)](/index.php?title=File:T101pwb03-04_snapselect.png&filetimestamp=20220605100908&)

When you have the white dot on the upper face, click the left mouse button,
and repeat for the upper square face of the main solid, like the right picture
above, and confirm the choice with a left mouse button click. The snap
function makes use of _mass-center_ for any type of face, and in this case the
mass center is the same as the geometrical center that is sought after. You
will by now have noticed that the move of the cylinder is animated, so you
always see what is about to happen.

Repeating the step of the **boolean cut** from earlier once again will make
the through hole that completes the model. Using the **linear measurement
tool** in the Part Workbench, a check that the hole is correctly placed is
done. The measurement can only be done between _points_ , so the measurement
is done from main body zero to the seam point of the cylinder, meaning that
the correct distance is 70 mm instead of the 65 that is on the drawing to
account for the extra radius that is included in the distance.

[![](/images/a/a6/T101pwb03-05_modelmeasure.png)](/index.php?title=File:T101pwb03-05_modelmeasure.png&filetimestamp=20220605100936&)

## Making the hole a countersunk hole

Switch back to the [Part Workbench](/Part_Workbench "Part Workbench") and
create a _cone_ by pressing the [![](/images/3/35/Part_Cone.svg)](/Part_Cone
"Part Cone") **[Cone](/Part_Cone "Part Cone")** button in the toolbar. Change
_radius1_ to 0 mm and _radius2_ to 7 mm – this will give a 2 mm _countersink_
on the radius. Making the _height_ of the cone 7 mm results in a 90 degree top
angle of the cone, or 45 degree countersink angle. Worth to note is that again
one could as well use the [![](/images/8/8c/Part_Chamfer.svg)](/Part_Chamfer
"Part Chamfer") [Chamfer](/Part_Chamfer "Part Chamfer") operation.

When working with FreeCAD you will continuously be faced with several
different ways to achieve seemingly the same result. There is hardly any
absolute truth in what is the right way to achieve a particular end result –
however when looking in a specific context one specific workflow can be more
flexible, allow for later features to actually be used etc. How you build 3D
models will evolve over time as you along the way learn more and more about
the features and capabilities of FreeCAD.

[![](/images/3/39/T101pwb04-01_cone.png)](/index.php?title=File:T101pwb04-01_cone.png&filetimestamp=20220605100958&)

Translate the cone so that it is _concentric_ with the hole and _coplanar_
with the main solid upper surface. Use any method described earlier in this
tutorial to accomplish that.

In the picture below the move is made with _Transform_ and an _increment_
setting of 1 mm, since the cone has a characteristic dimension of 7 mm,
meaning that the earlier increment setting of 5 mm will not allow for correct
positioning. The
[![](/images/e/e3/Std_DrawStyleWireFrame.svg)](/Std_DrawStyle#Wireframe "Std
DrawStyle") **[Wireframe](/Std_DrawStyle#Wireframe "Std DrawStyle")**
rendering is used to easier see that the cone is in the right position.

[![](/images/1/1d/T101pwb04-02_conetranslate.png)](/index.php?title=File:T101pwb04-02_conetranslate.png&filetimestamp=20220605101020&)

To complete the model, let's make use of the
[![](/images/e/ef/Part_Boolean.svg)](/Part_Boolean "Part Boolean")
**[Boolean](/Part_Boolean "Part Boolean")** command instead of first selecting
objects and apply a specific boolean operation. Press the toolbar button and a
_task panel_ opens as per the below picture to the left.

[![](/images/e/eb/T101pwb04-03_boolean.png)](/index.php?title=File:T101pwb04-03_boolean.png&filetimestamp=20220605101040&)

Three items needs to be specified, the _operation type_ , the _first shape_
and the _second shape_. The cone is supposed to be cut, this is called
_Difference_ in this command, instead of _Cut_. The first shape is our
**Cut001** , it is listed under _compounds_ , since it is build from several
solids. The second shape is the **Cone**. Once the correct settings are made
for the command, click the Apply button to execute the operation. This has all
been done in the picture to the right, and there one can also see that a
_compound_ **Cut002** is now listed, this is our final model shape. After
having changed the appearance the final model looks like this.

[![](/images/b/bf/T101pwb04-04_modelcomplete.png)](/index.php?title=File:T101pwb04-04_modelcomplete.png&filetimestamp=20220605101119&)

## Making a hollow piece

Do a _save-as_ under a new name. FreeCAD has all of the typical operations of
a 3D modeller, one of them is
[![](/images/d/d2/Part_Thickness.svg)](/Part_Thickness "Part Thickness")
**[Thickness](/Part_Thickness "Part Thickness")** , which is used to _hollow
out_ parts.

Rotate the view so that the bottom face of the model is visible.

[![](/images/b/b1/T101pwb05-01_frombottom.png)](/index.php?title=File:T101pwb05-01_frombottom.png&filetimestamp=20220605101140&)

Select the _bottom face_ of the model, then in the [Part
Workbench](/Part_Workbench "Part Workbench") select
[![](/images/d/d2/Part_Thickness.svg)](/Part_Thickness "Part Thickness")
**[Thickness](/Part_Thickness "Part Thickness")** and the screen should look
like below.

[![](/images/7/77/T101pwb05-02_thickness_cmd.png)](/index.php?title=File:T101pwb05-02_thickness_cmd.png&filetimestamp=20220605101203&)

Click OK, as you can see there is now a _radius_ on the hollowed out part.

[![](/images/5/54/T101pwb05-03_thickness_dimension.png)](/index.php?title=File:T101pwb05-03_thickness_dimension.png&filetimestamp=20220605101226&)

Moreover, when taking a measurement of the width of the part, it is now 32 mm,
so the _thickness_ has been applied _outwards_. Let’s edit that, double-click
the model in the Tree view and modify the _join-type_ settings to
_intersection_ and the _thickness_ setting to -1.

[![](/images/3/3d/T101pwb05-04_thickness_modify.png)](/index.php?title=File:T101pwb05-04_thickness_modify.png&filetimestamp=20220605101248&)

Now the outer width of the part is 30 mm, same as before and the corners are
all sharp corners.

[![](/images/9/98/T101pwb05-05_thickness_modified.png)](/index.php?title=File:T101pwb05-05_thickness_modified.png&filetimestamp=20220605101312&)

## A different way to position the chamfer

Do a _save-as_ under a new name. Then delete features so that the model looks
like below.

[![](/images/4/48/T101pwb06-01_startingpoint.png)](/index.php?title=File:T101pwb06-01_startingpoint.png&filetimestamp=20220605101333&)

Make a **Cube** with dimensions **30x30x60** , ending up like below.

[![](/images/c/c2/T101pwb06-02_with_cube.png)](/index.php?title=File:T101pwb06-02_with_cube.png&filetimestamp=20220605101358&)

Change the **placement** by first rotating -120 degrees around the Y-axis.

[![](/images/f/fb/T101pwb06-03_rotated_cube.png)](/index.php?title=File:T101pwb06-03_rotated_cube.png&filetimestamp=20220605101419&)

Finally, change the position to **X=50** and **Z=50** and make the _cut_ to
produce the same result as earlier.

[![](/images/7/7a/T101pwb06-04_cube_cut.png)](/index.php?title=File:T101pwb06-04_cube_cut.png&filetimestamp=20220605101448&)

This once again highlights that there are always several ways to produce the
same outcome, which is a recurring theme when it comes to 3D modeling. When it
comes to basic geometries or solids, one can use different workbenches in
FreeCAD as well as different commands and still have the same outer shape of a
solid. You simply need to find your own way to a set of preferred tools and
workflow that you are comfortable in using. Modeling in parametric 3D is a
process of constant learning, and takes practice to master.

## Editing dimensions, face colors and TNP

FreeCAD is a parametric 3D modeler, this allows you to change any _placement_
or _dimension_ and the model will update accordingly. In general this works,
but it is possible to break a model when edited – for example when a fillet is
based on an edge that no longer exists due to editing. When a model breaks
during editing, it is referred to as **TNP,[Topological Naming
Problem](/Topological_naming_problem "Topological naming problem")**.

Go ahead and experiment with changing dimensions and placements to see if you
can break the model, do not forget to recalculate the model after changes if
required. This can be done with the
[![](/images/7/76/Std_Refresh.svg)](/Std_Refresh "Std Refresh")
[Refresh](/Std_Refresh "Std Refresh") button in the toolbar, if the icon is
grayed out it is not needed to refresh the object.

### Reposition the cylinder

Here is an example of the cylinder moved from the center to one side of the
main body by using _Transform_ on the cylinder. As can be seen in the picture,
the cone is still in the original position, not affected by the move of the
cylinder.

[![](/images/b/b3/T101pwb07-01_cylindermoved.png)](/index.php?title=File:T101pwb07-01_cylindermoved.png&filetimestamp=20220605101519&)

When you move the cylinder and break through the outer surface, in version
0.19 you are loosing part of the color settings on your model. FreeCAD reverts
to the user default settings for shape colors and transparency in the 3D view,
however the **Cut002** shape still shows the colors and transparency that it
had before as seen in below picture.

### Fixing the colors

[![](/images/3/30/T101pwb07-02_wrongcolor.png)](/index.php?title=File:T101pwb07-02_wrongcolor.png&filetimestamp=20220605101538&)

Here is one way to get it back. First change _transparency_ one tick up or
down and then back, that brings back the transparency. You can do the same
trick on _shape color_. Another way to get the color back is to _right-click_
**Cut002** in the Tree view and select **Set Colors** in the context menu. In
the _task panel_ that displays, click Set to Default, that brings back the
color to the one set in the view-properties.

[![](/images/d/d4/T101pwb07-03_set_colors.png)](/index.php?title=File:T101pwb07-03_set_colors.png&filetimestamp=20220605101559&)

The **Set Colors** command allows you to select individual faces of a shape
and set a unique color on the selected faces.

### Multiple solids

Another example where the cube that is making the chamfer has been translated
and rotated.

[![](/images/9/9b/T101pwb07-04_3solids.png)](/index.php?title=File:T101pwb07-04_3solids.png&filetimestamp=20220605101618&)

As can be seen when repositioning the chamfer in this way, the end result is
_3 disjoint solids_. [Part Workbench](/Part_Workbench "Part Workbench") allows
this, [PartDesign Workbench](/PartDesign_Workbench "PartDesign Workbench")
does not, either you will get an _multiple solids error_ or it will simply not
render all solids.

### TNP

Going back to the original completed model, let’s explore how the faces are
named.

Here the **[selection view](/Selection_view "Selection view")** has been made
active, just to show clearly what is selected and not, also coloring is
adjusted so that the selection is easier to see.

[![](/images/d/dd/T101pwb07-05_face2and9.png)](/index.php?title=File:T101pwb07-05_face2and9.png&filetimestamp=20220605101651&)

Selecting one side face and the cylinder inner face gives that they are
internally called face _2_ and _9_ , where face _2_ is the side face. Face
numbering can be different for you.

Moving the cylinder so that the cavity ends up on the side face, and doing the
selection of faces now gives a different number for the cylindrical face.

[![](/images/f/f2/T101pwb07-06_newfacenumbers.png)](/index.php?title=File:T101pwb07-06_newfacenumbers.png&filetimestamp=20220605101709&)

Face 2 is the right side of the original face 2, the left side of former face
2 is now face 8. The cylindrical part was face 9, but is now face 7. FreeCAD
reassigns the numbering and the order is not necessarily preserved. The total
face count in the first model is 10, in the version with the cylindrical face
piercing the side face, the total face count is 11. So obviously face
numbering has to change when the so called _topology_ changes. This probably
feels like a minute detail, but turns out to be quite important in parametric
3D CAD. Imagine that you have used the cylindrical face as reference for
another feature, it used to be called face 9, but is now called face 8. The
reference to the intended cylindrical surface is lost. Since FreeCAD, at least
in currently released versions does not keep track of the _intended face_ , it
only keeps track of the _numbered face_ , a model breaks when a reference is
made to a face that later is renumbered. This is called **TNP,[Topological
Naming Problem](/Topological_naming_problem "Topological naming problem")**.

You are encouraged to learn how to avoid broken models due to TNP, further
reading can be done [elsewhere on the wiki](/Topological_naming_problem
"Topological naming problem"), which largely focuses on a _sketch driven_
workflow, the underlying mechanism is the same though. The renumbering
described here for faces goes for all geometrical entities, faces, edges and
vertexes.

## Organizing the tree a bit differently

Do a _save-as_ under a new name. Then delete all the cuts ending up with a
model looking like below.

[![](/images/d/d9/T101pwb08-01_primitives.png)](/index.php?title=File:T101pwb08-01_primitives.png&filetimestamp=20220605101739&)

When using the **Part Workbench** and modelling feature rich solids, the tree
structure of a solid can become hard to decipher. So far we have created one
primitive / feature and applied a boolean operation. In the Part Workbench one
can bundle primitives into one boolean operation. In our case we have the
cylinder, cone and cube that are all a cut boolean operation.

Instead of making a cut for each primitive, we can first apply a boolean
union, [![](/images/e/e4/Part_Fuse.svg)](/Part_Fuse "Part Fuse")
**[Fuse](/Part_Fuse "Part Fuse")** the primitives intended for the boolean
cut, and then make the _cut_ between the **Fillet** and the **Fusion**.

Using this approach, the Tree view ends up looking like below, which is just a
different way of building the same model. Compare this with the original Tree
view, none is better than the other, however when making more complex models,
one approach over the other can have benefits in ease of
modifying/reorganizing the model if needed.

[![](/images/9/9a/T101pwb08-02_fused.png)](/index.php?title=File:T101pwb08-02_fused.png&filetimestamp=20220605101803&)

## Wrapping up

Having gone through the tutorial you are now briefly acquainted with the user
interface of FreeCAD and you have learned the basics in using the **Part
Workbench**. You should now be able to build simple models after your own
liking. The **Part Workbench** is one of the workbenches that can be used to
create solids, the **PartDesign Workbench** is another. The different
workbenches have different capabilities and workflows. Learning FreeCAD in
full, especially considering all add-ons and macros takes years, so keep on
exploring new and different ways of making models – take different tutorials
on the wiki, the learning never stops when working with FreeCAD. It is
suggested that you learn _sketches_ and the **PartDesign Workbench** next if
your focus is on creating solids. If your focus is modelling buildings your
next learning should be the **Draft** and **Arch** workbenches.

At last, FreeCAD is made by volunteers in their spare time. If you want to
further advance FreeCAD’s capabilities, consider [contributing](/Help_FreeCAD
"Help FreeCAD") to FreeCAD, for example by improving the documentation.

