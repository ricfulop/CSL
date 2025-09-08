---
url: https://wiki.freecad.org/Creating_a_simple_part_with_Draft_and_Part_WB
title: Creating a simple part with Draft and Part WB
scraped_at: 2025-09-08 16:43:08
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction Toggle Introduction subsection
    * 1.1 The tutorial covers
  * 2 The model to make
  * 3 Creating the 2D profile Toggle Creating the 2D profile subsection
    * 3.1 Creating the fillet
    * 3.2 Creating the chamfer
  * 4 Why extruding can fail
  * 5 Extruding the profile
  * 6 Creating the through hole
  * 7 Making a sketch out of the 2D profile
  * 8 Quality of models
  * 9 Wrapping up

# Creating a simple part with Draft and Part WB

  * [Page](/Creating_a_simple_part_with_Draft_and_Part_WB "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Creating_a_simple_part_with_Draft_and_Part_WB&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Creating_a_simple_part_with_Draft_and_Part_WB)
  * [Edit](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Creating_a_simple_part_with_Draft_and_Part_WB.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Creating_a_simple_part_with_Draft_and_Part_WB)
  * [Edit](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&action=history)

General

  * [What links here](/Special:WhatLinksHere/Creating_a_simple_part_with_Draft_and_Part_WB "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Creating_a_simple_part_with_Draft_and_Part_WB "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&oldid=1536389 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Creating_a_simple_part_with_Draft_and_Part_WB&action=info "More information about this page")

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Creating_a_simple_part_with_Draft_and_Part_WB&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Creating+a+simple+part+with+Draft+and+Part+WB&action=page&filter=&language=en)This
is the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Creating+a+simple+part+with+Draft+and+Part+WB&language=&task=view "Start translation for this language")
  * [Deutsch](/Creating_a_simple_part_with_Draft_and_Part_WB/de "Erstellen eines einfachen Bauteils mit den Arbeitsbereichen Draft und Part \(4% translated\)")
  * English
  * [français](/Creating_a_simple_part_with_Draft_and_Part_WB/fr "Créer une simple pièce avec les ateliers Draft et Part \(100% translated\)")
  * [italiano](/Creating_a_simple_part_with_Draft_and_Part_WB/it "Creazione di una parte semplice con gli Ambienti Draft e Part \(1% translated\)")
  * [polski](/Creating_a_simple_part_with_Draft_and_Part_WB/pl "Tworzenie prostej części za pomocą środowiska pracy Rysunek Roboczy i Część \(100% translated\)")
  * [português do Brasil](/Creating_a_simple_part_with_Draft_and_Part_WB/pt-br "Criando uma peça simples com as bancadas Draft e Part \(100% translated\)")
  * [русский](/Creating_a_simple_part_with_Draft_and_Part_WB/ru "Создание простой детали с помощью верстаков Draft и Part \(25% translated\)")

![](/images/0/06/Freecad.svg) Tutorial  
---  
Topic  
Modeling  
Level  
Beginner  
Time to complete  
1.5 hours  
Authors  
heda  
FreeCAD version  
0.19 or above  
Example files  
See also  
[Creating a simple part with Part WB](/Creating_a_simple_part_with_Part_WB
"Creating a simple part with Part WB"), [Creating a simple part with
PartDesign](/Creating_a_simple_part_with_PartDesign "Creating a simple part
with PartDesign")  
  
  
  
## Introduction

This tutorial aims to be used as a first introduction to the [Draft
Workbench](/Draft_Workbench "Draft Workbench")
[![](/images/8/8d/Switch_DraftWorkbench.JPG)](/index.php?title=File:Switch_DraftWorkbench.JPG&filetimestamp=20170227183950&)
in FreeCAD. The tutorial uses a _2D shape_ to create a _3D solid_ , the latter
is accomplished through the [Part Workbench](/Part_Workbench "Part
Workbench"). The reader is recommended to first work through the sister
tutorial _[Creating a simple part with Part
WB](/Creating_a_simple_part_with_Part_WB "Creating a simple part with Part
WB")_ , which is creating the same model with a different technique, while at
the same time covering more of the basics of FreeCAD’s user interface. This
tutorial expects the user to be briefly familiar with both the user interface
and some workflows available in FreeCAD. The tutorial is composed such that
the aim is not necessarily to show the most efficient way to use the program,
but rather to make the reader aware of different functionalities available in
FreeCAD, how to use them, and where to find them.

### The tutorial covers

  * The model to make
  * Creating the 2D profile
  * Why extruding can fail
  * Extruding the profile
  * Creating the through hole
  * Making a sketch out of the 2D profile
  * Quality of models
  * Wrapping up

## The model to make

[![](/images/thumb/c/ce/GGTuto1_Vue.PNG/372px-
GGTuto1_Vue.PNG)](/index.php?title=File:GGTuto1_Vue.PNG&filetimestamp=20180404144733&)
[![](/images/4/47/T101pwb01-02_dims.png)](/index.php?title=File:T101pwb01-02_dims.png&filetimestamp=20220605100016&)

## Creating the 2D profile

Create a new document and save it directly under a new name. Change the view
to [![](/images/b/bd/Std_ViewTop.svg)](/Std_ViewTop "Std ViewTop")
[Top](/Std_ViewTop "Std ViewTop") view and switch to the
[![](/images/9/91/Workbench_Draft.svg)](/Draft_Workbench "Draft Workbench")
[Draft Workbench](/Draft_Workbench "Draft Workbench"), your screen should look
like below. If the grid does not show, toggle it on/off with
[![](/images/c/c9/Draft_ToggleGrid.svg)](/Draft_ToggleGrid "Draft ToggleGrid")
[Toggle Grid](/Draft_ToggleGrid "Draft ToggleGrid").

[![](/images/6/6a/T101dwb01-01draftgrid.png)](/index.php?title=File:T101dwb01-01draftgrid.png&filetimestamp=20220605101916&)

To start off the profile, draw a random
[![](/images/d/da/Draft_Rectangle.svg)](/Draft_Rectangle "Draft Rectangle")
[Rectangle](/Draft_Rectangle "Draft Rectangle") on the xy-plane by clicking 2
points in the [3D view](/3D_view "3D view") forming any diagonal of a
rectangle. A _task panel_ will open once the command is invoked, this time we
are not going to use it at all, but you could of course enter the coordinates
for the rectangle directly. Your 3D view should now have a rectangle drawn,
similar to the below picture.

[![](/images/3/3a/T101dwb01-02rectangleraw.png)](/index.php?title=File:T101dwb01-02rectangleraw.png&filetimestamp=20220605101938&)

When working in the **Draft Workbench** one almost always draws on a 2D plane.
That 2D plane is called the _[Working plane](/Draft_SelectPlane "Draft
SelectPlane")_ , and, if default settings are used, it will always
automatically align itself to the current 3D view. So, until the 2D profile is
completed, it is best to simply keep the Top view (camera position) and not
play around with rotating the view. If you happened to have changed it, just
change back to the Top view before starting any new command in the **Draft
Workbench**.

The side view of our final model has the outer contour of 100 x 50 mm, and it
would be nice if the lower left corner was placed in the global zero position.
This can be accomplished through the _Property editor_. Make sure the created
**Rectangle** is selected, then change the _Position_ of the rectangle to
**(0, 0, 0)** , modify the _height_ to **50** mm and the _length_ to **100**
mm as per the images below.

[![](/images/d/d2/T101dwb01-03rectangleprops.png)](/index.php?title=File:T101dwb01-03rectangleprops.png&filetimestamp=20220605101955&)

The **Rectangle** is finished and it should look like this after applying
[![](/images/6/66/Std_ViewFitAll.svg)](/Std_ViewFitAll "Std ViewFitAll") [Fit
all](/Std_ViewFitAll "Std ViewFitAll") to the view.

[![](/images/5/5a/T101dwb01-04rectangledone.png)](/index.php?title=File:T101dwb01-04rectangledone.png&filetimestamp=20220605102015&)

Next we will break up the rectangle into its four edges, this is done by first
selecting the **Rectangle** and then invoking the command
[![](/images/8/84/Draft_Downgrade.svg)](/Draft_Downgrade "Draft Downgrade")
[Draft Downgrade](/Draft_Downgrade "Draft Downgrade"), the filled face will
disappear and the object in the _Tree View_ is now a **Wire** instead of a
**Rectangle** , shown in the left picture below. Invoking **Draft Downgrade**
once more will break up the _wire_ into its _edges_ , shown in the middle
picture below.

[![](/images/d/d8/T101dwb01-05rectangledowngrade.png)](/index.php?title=File:T101dwb01-05rectangledowngrade.png&filetimestamp=20220605102039&)

The observant will notice that the object icon in the Tree View already for
the wire changed to a _blue box_. This blue box is the icon used for generic
geometric objects (Part Workbench geometric objects to be specific, but that
is for advanced readers). Select the left vertical edge and invoke the command
[![](/images/b/ba/Draft_Upgrade.svg)](/Draft_Upgrade "Draft Upgrade") [Draft
Upgrade](/Draft_Upgrade "Draft Upgrade"), the former _edge_ will now have a
different icon and has changed _label_ to **Line**. It is now a **Draft
Workbench** object where one can edit for example the _start point_ and the
_end point_ through the _Property editor_ , this is not possible with the
_edge_ objects.

### Creating the fillet

Start by selecting the upper right corner edges, use menu **Edit → Box
selection** [![](/images/8/8d/Std_BoxSelection.svg)](/Std_BoxSelection "Std
BoxSelection") [Box selection](/Std_BoxSelection "Std BoxSelection"), hold
down the
[![](/images/0/04/Mouse_LMB.svg)](/index.php?title=File:Mouse_LMB.svg&filetimestamp=20181210182920&)
**Left Mouse Button** and drag _from right to left_ and release the **LMB**.
When dragging _from right to left_ the resulting selection includes everything
fully or partially within the selection area. If one drags _from left to
right_ , only objects fully enclosed by the selection area are included in the
resulting selection. The actual selection happens when the left mouse button
is released, and there is no preview of what will be selected.

[![](/images/1/1a/T101dwb02-01filletboxselection.png)](/index.php?title=File:T101dwb02-01filletboxselection.png&filetimestamp=20220605102111&)

With the top right corner edges selected, invoke the command
[![](/images/6/67/Draft_Fillet.svg)](/Draft_Fillet "Draft Fillet")
[Fillet](/Draft_Fillet "Draft Fillet") in the **Draft Workbench**. Check
_Delete original objects_ and change the _radius_ to 20 mm and hit enter.

[![](/images/4/40/T101dwb02-02fillettaskpanel.png)](/index.php?title=File:T101dwb02-02fillettaskpanel.png&filetimestamp=20220605102132&)

The **Fillet** is created and your model should now look like below.

[![](/images/1/1c/T101dwb02-03filletdone.png)](/index.php?title=File:T101dwb02-03filletdone.png&filetimestamp=20220605102156&)

### Creating the chamfer

To make the _chamfer_ we need to have a line with the correct inclination and
also be able to position it correctly. Let us begin with the position, which
is on coordinate _(50, 50, 0)_. In the current profile we do not have a point
there, so let’s create one by making a _temporary help line_. First select the
left vertical **Line** , then create the help line by
[![](/images/5/5b/Std_DuplicateSelection.svg)](/Std_DuplicateSelection "Std
DuplicateSelection") [Duplicate selection](/Std_DuplicateSelection "Std
DuplicateSelection") in **Edit → Duplicate selection** , **Line001** is
created. Use the _Property editor_ and move **Line001** 50 mm in x-direction
using the _Placement_ property. Next duplicate the _lower horizontal edge_ ,
and change the _angle_ of the edge to 30 degrees, once again using the
_Placement_ property. The model should now look like the image below.

[![](/images/2/28/T101dwb03-01chamferhelp.png)](/index.php?title=File:T101dwb03-01chamferhelp.png&filetimestamp=20220801081810&)

Next, move the _angled line_ into position. For this we make use of
[![](/images/3/3c/Draft_Move.svg)](/Draft_Move "Draft Move") [Draft
Move](/Draft_Move "Draft Move") along with the _snap_ functionality in the
**Draft Workbench** , more specifically _end point_ snap. First make sure that
your snap toolbar looks similar to below.

[![](/images/6/6f/T101pwb03-02_snap.png)](/index.php?title=File:T101pwb03-02_snap.png&filetimestamp=20220605100759&)

Then select the _angled line_ , **Edge001** , press **Move** and a _task
panel_ opens up.

[![](/images/9/9f/T101dwb03-03_movetaskpanel.png)](/index.php?title=File:T101dwb03-03_movetaskpanel.png&filetimestamp=20220605102252&)

Make sure that _Copy_ is unchecked. Hover the mouse over the _upper quarter_
of the _angled line_ , once the _white dot_ is displayed at the right spot and
the _end point_ symbol shows, click the
[![](/images/0/04/Mouse_LMB.svg)](/index.php?title=File:Mouse_LMB.svg&filetimestamp=20181210182920&)
**LMB**. Move the mouse to the upper quarter of the help line, once the white
dot and end point symbol appear, click the **LMB**. The sequence is
illustrated below.

[![](/images/0/0d/T101dwb03-04_moveline.png)](/index.php?title=File:T101dwb03-04_moveline.png&filetimestamp=20220605102313&)

The line is now in the correct position, but it is too long. To adjust the
length [![](/images/e/e9/Draft_Trimex.svg)](/Draft_Trimex "Draft Trimex")
[Draft Trimex](/Draft_Trimex "Draft Trimex") will be used. Select the _angled
line_ , **Edge001** , press Trim and then click on the lower part of the
_left-most vertical line_ , **Line** , to use it as the cutting edge. The
projection of the point where the cutting edge is selected onto the edge to be
cut, determines the result. If you select the left-most vertical line near its
top end, the wrong part of the angled line would be trimmed. The image below
shows the **Trim** command invoked, the pre-selected vertical line, and the
cursor hovering over the wrong end of that line. If you look carefully you can
see the preview of the result.

[![](/images/4/47/T101dwb03-05_trimline.png)](/index.php?title=File:T101dwb03-05_trimline.png&filetimestamp=20220605102333&)

Also trim the left-most vertical line to form the lower corner of the chamfer.
Select the _angled line_ , **Edge001** , near its top right endpoint for a
correct result. If you make a mistake while trimming, just use
[![](/images/6/60/Std_Undo.svg)](/Std_Undo "Std Undo") [Undo](/Std_Undo "Std
Undo") and [![](/images/7/76/Std_Refresh.svg)](/Std_Refresh "Std Refresh")
[Refresh](/Std_Refresh "Std Refresh") (the latter often called _recompute_)
and try again.

[![](/images/4/43/T101dwb03-06_chamferlowercornerdone.png)](/index.php?title=File:T101dwb03-06_chamferlowercornerdone.png&filetimestamp=20220605102354&)

To trim the _upper horizontal edge_ , the **Fillet** needs to be _downgraded_
so that the upper edge is its own object in the Tree View. If you attempt to
trim it without first having done the downgrade, the trimming function
attempts to trim the arc in the fillet. Because the trimming edge, the _middle
vertical line_ , is perpendicular to the edge to be trimmed, you cannot
control the trim result by picking a correct point on the trimming edge. Here
you need the flip the default solution by holding down the Alt key as you
select the cutting edge.

The profile is ready and shown below with the edges organized in a
[![](/images/c/cd/Std_Group.svg)](/Std_Group "Std Group") [Group](/Std_Group
"Std Group") named **Profile** (or _labeled_ to be precise in FreeCAD lingo),
along with the help line deleted. Groups can be used to organize the features
in your _FreeCAD documents_ , its usage is similar to a folder structure on a
computer’s file system. To move things in and out of the group, use _drag and
drop_ in the Tree View.

[![](/images/8/8c/T101dwb03-07_profiledone.png)](/index.php?title=File:T101dwb03-07_profiledone.png&filetimestamp=20220605102412&)

## Why extruding can fail

Save the document. We will experiment in this paragraph and we want to be able
to go back to the current model.

Let’s jump right in: select all the edges in the _group_ **Profile** , and in
the [![](/images/0/04/Workbench_Part.svg)](/Part_Workbench "Part Workbench")
[Part Workbench](/Part_Workbench "Part Workbench") invoke the command
[![](/images/3/38/Part_Extrude.svg)](/Part_Extrude "Part Extrude")
[Extrude](/Part_Extrude "Part Extrude"). A _task panel_ opens, accept all the
defaults and click OK.

[![](/images/3/30/T101dwb04-01_extrudelineserror.png)](/index.php?title=File:T101dwb04-01_extrudelineserror.png&filetimestamp=20220605102434&)

That did not work out, but it sounds easy enough to fix the error, we just
need to specify a direction. Click OK to get back to the _task panel_ and
select _custom direction_.

[![](/images/f/f3/T101dwb04-02_extrudelineszaxis.png)](/index.php?title=File:T101dwb04-02_extrudelineszaxis.png&filetimestamp=20220605102450&)

Accept the default z-axis and once more click OK.

[![](/images/8/85/T101dwb04-03_extrudelinessheets.png)](/index.php?title=File:T101dwb04-03_extrudelinessheets.png&filetimestamp=20220605102510&)

We managed to make a fence like structure, judging from the Tree View every
edge is treated separately. It is not the filled solid that we want. Hit
[Undo](/Std_Undo "Std Undo"), and let’s try something else.

Scrolling all the way to the bottom of the **Extrude** _task panel_ there is
an option _Create solid_ , check that option and click OK.

[![](/images/4/4a/T101dwb04-04_extrudelinesfilled.png)](/index.php?title=File:T101dwb04-04_extrudelinesfilled.png&filetimestamp=20220605102528&)

Everything disappeared, clearly that did not work either. Let’s go through why
none of these ways are working. In the first case we got an error that the
direction could not be determined. A flat face has a normal, i.e. direction, a
line does not. Since from our second attempt we know that it worked when
providing a direction, the error simply comes from trying to extrude a line
without knowing a direction. The observant will say that an arc has a normal
(direction), this is true. If you select only the edge that is the arc,
FreeCAD will extrude it, also with default settings.

In the second case it worked, but we also got an extrusion for each edge we
had in our selection. The resulting features however are not what we want,
i.e. a solid.

In the third case we checked _Create solid_ , and ended up with everything
disappearing. The objects in the Tree View have a different icon as well,
there is a _white exclamation_ mark on a red background, that particular
_overlay icon_ means that the object has an error that has to be tended to.
One can read up on the different types of [overlay
icons](/Tree_view#Overlay_icons "Tree view") on the wiki.

Hovering over any of the Tree View objects with the overlay icon a tool tip is
displayed, it says _Wire is not closed_.

[![](/images/7/7c/T101dwb04-05_extrudelineserrortooltip.png)](/index.php?title=File:T101dwb04-05_extrudelineserrortooltip.png&filetimestamp=20220605102552&)

In our case the error is not fixable. It is _geometrically impossible_ to
create a solid out of an extruded single line. An extruded line simply becomes
a sheet, or _shell_ in FreeCAD lingo. In other words, this is not a FreeCAD
limitation, it is a fundamental outcome of geometrical theory. The reason why
the 3D view goes completely blank is that the created features, or objects in
the Tree View, have errors in the produced _shape_ , and thus contain nothing
to render. FreeCAD does however create the new document objects (in this case
extrusions) and thus hides any geometry/object used for making the new
document objects. That is why the screen goes blank when trying to make a
solid out of a line, or lines.

The tool tip says it all, in order to extrude into a solid one needs a _closed
wire, or a face_. A face is, per definition, simply a closed wire that is
filled. One way to create a closed wire out of our profile edges is to select
them all and apply [![](/images/b/ba/Draft_Upgrade.svg)](/Draft_Upgrade "Draft
Upgrade") [Draft Upgrade](/Draft_Upgrade "Draft Upgrade"). If applied once it
becomes a wire, while at the same time it consumes the individual edges from
the Tree View. If applied twice it becomes a face, either of those allows for
a successful solid extrusion.

Before going on to the next paragraph: open the previous version of the
document.

## Extruding the profile

Another way to create the closed wire is with the
[![](/images/2/2a/Part_Builder.svg)](/Part_Builder "Part Builder") [Shape
builder](/Part_Builder "Part Builder") command from the Part Workbench, which
allows for making a wire without consuming the individual edges. **Part Shape
builder** is a powerful tool to create any geometric entity in FreeCAD that
can be used further to create complex solids, the simplest example is creating
a line between two vertices. Click **Part Shape builder** to bring up the
_task panel_.

[![](/images/1/10/T101dwb05-01_shapebuildertaskpanel.png)](/index.php?title=File:T101dwb05-01_shapebuildertaskpanel.png&filetimestamp=20220605102614&)

We can use either _Wire from edges_ or _Face from edges_. Multiple selections
have to be made with the Ctrl key pressed down. Let’s use _Face from edges_ ,
once that option is selected one can also select _Planar_ , do that as well.
Then select all edges in the profile, the order does not matter (in this case)
and click Create, and then Close to come back to the Tree View. The _face_ has
been created.

[![](/images/e/ed/T101dwb05-02_shapebuilderfacedone.png)](/index.php?title=File:T101dwb05-02_shapebuilderfacedone.png&filetimestamp=20220605102636&)

Select the **Face** and invoke **Part Extrude** , set the extrusion _length_
to **30** mm and click OK.

[![](/images/b/b4/T101dwb05-03_extrusiondone.png)](/index.php?title=File:T101dwb05-03_extrusiondone.png&filetimestamp=20220605102654&)

## Creating the through hole

To make the through hole we need a _cylinder_ correctly _positioned_ to make a
boolean _cut_ with.

Create a cylinder, and position it correctly. In this case the _radius_ is 5
mm, the _height_ is set to 60 mm. For the placement, first it is _rotated_ -90
degrees around the x-axis, then positioned at _(65, -5, 15)_. The negative 5
in the y-direction is because the height is 10 mm longer than needed.

[![](/images/7/79/T101dwb05-04_cylinderplaced.png)](/index.php?title=File:T101dwb05-04_cylinderplaced.png&filetimestamp=20220605102715&)

It does not hurt to make the height of the cylinder longer than needed. For a
simple model like this it will not matter if the cylinder is the exact height
of the profile. It is however good practice to avoid co-planar faces to
prevent numerical errors in the geometric kernel that can sometimes result in
strange effects, or failures in subsequent operations.

With a final boolean cut, and after changing the appearance of the resulting
object, the model is completed.

[![](/images/b/b8/T101dwb05-05_modelcomplete.png)](/index.php?title=File:T101dwb05-05_modelcomplete.png&filetimestamp=20220605102739&)

## Making a sketch out of the 2D profile

Using the **Draft Workbench** is one way of creating a 2D profile. In the
**Draft Workbench** a wire can be made in 3D space. FreeCAD provides another
tool to make 2D profiles – the
[![](/images/9/91/Workbench_Sketcher.svg)](/Sketcher_Workbench "Sketcher
Workbench") [Sketcher Workbench](/Sketcher_Workbench "Sketcher Workbench").
Using a _sketch_ is a more versatile way to create a 2D profile. Any 2D
profile made in the **Draft Workbench** can be converted to an _unconstrained_
sketch.

Start by hiding the **Cut** feature and make the edges in the profile visible.
Select the edges and from the **Draft Workbench** press the toolbar button
[![](/images/b/b2/Draft_Draft2Sketch.svg)](/Draft_Draft2Sketch "Draft
Draft2Sketch") [Draft to Sketch](/Draft_Draft2Sketch "Draft Draft2Sketch").
You should see the same as in the image below.

[![](/images/5/5e/T101dwb06-01_draft2sketch.png)](/index.php?title=File:T101dwb06-01_draft2sketch.png&filetimestamp=20220605102806&)

Next, hide the original edges and double-click the **Sketch** object in the
Tree View, bringing you to the following state, i.e. the _Sketcher task panel_
opened.

[![](/images/1/1a/T101dwb06-02_sketchedit.png)](/index.php?title=File:T101dwb06-02_sketchedit.png&filetimestamp=20220605102824&)

This is how it looks when one _edits a sketch_. Since this is not a tutorial
for using the Sketcher just go ahead and close it. If you want an introduction
to sketching, which is a core workflow in any 3D parametric CAD, please follow
the sister tutorial _[Creating a simple part with
PartDesign](/Creating_a_simple_part_with_PartDesign "Creating a simple part
with PartDesign")_.

With the **Sketch** closed and selected, from the **Part Workbench** use
Extrude in the same way as before. The basic block of the simple model is
ready once again.

[![](/images/1/12/T101dwb06-03_sketchextruded.png)](/index.php?title=File:T101dwb06-03_sketchextruded.png&filetimestamp=20220605102848&)

## Quality of models

Sooner or later when working with 3D parametric CAD you will come across a
broken model, either one you have made yourself, or a model that you have
imported. A broken model can work for its purpose, but more often than not,
there are subsequent operations that simply will not work. To repair a broken
model one has to know what to repair, this is where the built-in quality check
tools in FreeCAD come in.

First let us check the quality of the recently created **Extrude001**. With
the **Part Workbench** active, first select **Extrude001** and then use the
command [![](/images/6/64/Part_CheckGeometry.svg)](/Part_CheckGeometry "Part
CheckGeometry") [Check geometry](/Part_CheckGeometry "Part CheckGeometry").
Check all settings checkboxes except the top one, and click the Run check
button.

[![](/images/a/a9/T101dwb07-01_geocheck.png)](/index.php?title=File:T101dwb07-01_geocheck.png&filetimestamp=20220605102933&)

Our model is OK, no errors are reported. There is also a listing of the models
content, or in FreeCAD lingo, the content of the _shape_ , i.e. how it is put
together from ground up. Here one can see that apparently to make a _solid_
one also needs a _shell_ , and the shell is made out of _faces_ , and so on.
In other words, you can create any solid by simply starting out by making
points, or _vertices_ , from those one makes _edges_ , and from those one
creates _wires_ , and out of the wires one makes _faces_ which are then
stitched into a _shell_ , from which one finally arrives at a _solid_. A solid
can only be made from a watertight shell. A not watertight shell is a common
source of troublesome CAD models, it can for example happen with imported
geometry created in a different software, especially when using the commonly
available neutral file formats.

Another check one can do is related to the **Sketch**. Close the _task panel_
for the geometry check. Select the **Sketch** , expand **Extrude001** in the
Tree View if needed in order to see the sketch object. Switch to the
[![](/images/9/91/Workbench_Sketcher.svg)](/Sketcher_Workbench "Sketcher
Workbench") [Sketcher Workbench](/Sketcher_Workbench "Sketcher Workbench"),
use the command
[![](/images/d/d3/Sketcher_ValidateSketch.svg)](/Sketcher_ValidateSketch
"Sketcher ValidateSketch") [Validate sketch](/Sketcher_ValidateSketch
"Sketcher ValidateSketch"), a _task panel_ opens. In the _task panel_ , click
the Find button for _Missing coincidences_. It highlights and reports _6_ of
them, i.e. all the points where the edges meet.

[![](/images/f/f1/T101dwb07-02_sketchvalidate.png)](/index.php?title=File:T101dwb07-02_sketchvalidate.png&filetimestamp=20220605102955&)

Click OK in the pop-up dialog and then click the Fix button to heal the
_Missing coincidences_. If you close the _task panel_ , and go into _edit
mode_ of the **Sketch** , it reports _12 degrees of freedom_ , as opposed to
the earlier _24_. That was achieved through adding _coincident constraints_ to
the endpoints of the edges.

The observant reader notices that when using edges from Draft those had to be
joined into a closed wire to make a solid extrusion, whereas in Sketcher that
was apparently not needed. The logic here is that the sketch is one object,
and the extrusion of one object is treated as if it was a closed wire (in this
case).

Finally it should be pointed out that, although creating subsequent objects
from sketches with _open vertices_ can work, it is _best practice_ to _not
have any_ , as well as to have a _fully constrained sketch_ (as opposed to an
under-constrained sketch). The reason why it works here is that the _sketch_
is created from a Draft profile constructed in such a way that the endpoints
of the edges match without any gaps. If you draw by hand in a sketch, and also
try to match endpoints by hand, it is virtually guaranteed that endpoints will
not match, i.e. the gaps (although not really visible on the screen) will be
large enough that the geometric kernel cannot consider the edges to be
geometrically joined.

## Wrapping up

Having gone through the tutorial you have become somewhat familiar with the
basic functionality of FreeCAD, along with the core workbenches **Part** and
**Draft**. You are also aware of the existence of the **Sketcher Workbench** ,
which for many experienced users is the sole tool used to create 2D profiles
later utilized in solid feature operations. The use of _sketches_ is a core
concept in the **PartDesign Workbench**. It is suggested that you learn
_sketches_ and **PartDesign Workbench** next if your focus is on creating
solids. The sister-tutorial _[Creating a simple part with
PartDesign](/Creating_a_simple_part_with_PartDesign "Creating a simple part
with PartDesign")_ makes the same model as this tutorial. If your focus is
modeling buildings your next learning should be the **Draft** and **Arch**
workbenches.

At last, FreeCAD is made by volunteers in their spare time. If you want to
further advance FreeCAD’s capabilities, consider [contributing](/Help_FreeCAD
"Help FreeCAD") to FreeCAD, for example by improving the documentation.

  

