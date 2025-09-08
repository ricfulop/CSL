---
url: https://wiki.freecad.org/Creating_a_simple_part_with_PartDesign
title: Creating a simple part with PartDesign
scraped_at: 2025-09-08 16:43:11
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Using Part Design workbench, tracing the sketch
  * 2 Using Pad and Pocket features
  * 3 Changing color and transparency
  * 4 Manually move the part
  * 5 Displaying reference dimensions in the sketch
  * 6 Editing one or more dimensions
  * 7 Center the hole

# Creating a simple part with PartDesign

  * [Page](/Creating_a_simple_part_with_PartDesign "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Creating_a_simple_part_with_PartDesign&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Creating_a_simple_part_with_PartDesign)
  * [Edit](/index.php?title=Creating_a_simple_part_with_PartDesign&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Creating_a_simple_part_with_PartDesign&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Creating_a_simple_part_with_PartDesign.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Creating_a_simple_part_with_PartDesign&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Creating_a_simple_part_with_PartDesign)
  * [Edit](/index.php?title=Creating_a_simple_part_with_PartDesign&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Creating_a_simple_part_with_PartDesign&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Creating_a_simple_part_with_PartDesign&action=history)

General

  * [What links here](/Special:WhatLinksHere/Creating_a_simple_part_with_PartDesign "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Creating_a_simple_part_with_PartDesign "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Creating_a_simple_part_with_PartDesign&oldid=1536390 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Creating_a_simple_part_with_PartDesign&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Creating_a_simple_part_with_PartDesign&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Creating+a+simple+part+with+PartDesign&action=page&filter=&language=en)This is
the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Creating+a+simple+part+with+PartDesign&language=&task=view "Start translation for this language")
  * [Deutsch](/Creating_a_simple_part_with_PartDesign/de "Erstellen eines einfachen Bauteils mit PartDesign \(100% translated\)")
  * English
  * [Türkçe](/Creating_a_simple_part_with_PartDesign/tr "Parça Tasarım ile basit bir parça oluşturma \(1% translated\)")
  * [español](/Creating_a_simple_part_with_PartDesign/es "Crear una pieza simple con PartDesign \(4% translated\)")
  * [français](/Creating_a_simple_part_with_PartDesign/fr "PartDesign Tutoriel pour créer une pièce simple \(100% translated\)")
  * [italiano](/Creating_a_simple_part_with_PartDesign/it "Creare una parte semplice con PartDesign \(100% translated\)")
  * [polski](/Creating_a_simple_part_with_PartDesign/pl "Projekt Części: tworzenie podstawowych brył \(100% translated\)")
  * [português do Brasil](/Creating_a_simple_part_with_PartDesign/pt-br "Criando uma peça simples com Part Design \(100% translated\)")
  * [română](/Creating_a_simple_part_with_PartDesign/ro "Crearea unei piese simple cu PartDesign \(8% translated\)")
  * [русский](/Creating_a_simple_part_with_PartDesign/ru "Создание простой детали в PartDesign \(100% translated\)")

![](/images/0/06/Freecad.svg) Tutorial  
---  
Topic  
Modeling  
Level  
Beginner  
Time to complete  
1 hour  
Authors  
GlouGlou  
FreeCAD version  
0.17 or above  
Example files  
See also  
[Creating a simple part with Part WB](/Creating_a_simple_part_with_Part_WB
"Creating a simple part with Part WB"), [Creating a simple part with Draft and
Part WB](/Creating_a_simple_part_with_Draft_and_Part_WB "Creating a simple
part with Draft and Part WB")  
  
  
[![](/images/c/ce/GGTuto1_Vue.PNG)](/index.php?title=File:GGTuto1_Vue.PNG&filetimestamp=20180404144733&)

This tutorial aims to teach FreeCAD beginners a few basic features through an
example. After covering the basics in the [User hub](/User_hub "User hub"),
you will be able to model a first part step by step.

**We will cover in this tutorial in particular:**

  * Using [Part Design workbench](/PartDesign_Workbench "PartDesign Workbench"), tracing the sketch.
  * Using Pad and Pocket features.
  * Changing color and transparency.
  * Moving the part manually.
  * Displaying reference dimensions in the sketch.
  * Editing one or more dimensions.
  * Using external geometry feature and using a reference plane to centre a hole.

### Using [Part Design workbench](/PartDesign_Workbench "PartDesign
Workbench"), tracing the sketch

Create a new document and switch to the
[![](/images/3/39/Workbench_PartDesign.svg)](/index.php?title=File:Workbench_PartDesign.svg&filetimestamp=20240405092932&)
**Part Design workbench** using either the [workbench
selector](/Getting_started#Exploring_the_interface "Getting started")
(labelled 10 in the linked image) or by going to the _View → Workbench_ menu.
FreeCAD will start with toolbars at the top, the combo view to the left and
the 3D view at the right.

**Create body:**

Press
[![](/images/1/10/PartDesign_Body.svg)](/index.php?title=File:PartDesign_Body.svg&filetimestamp=20191125185840&)
[Create body](/PartDesign_Body "PartDesign Body"). _**Note:** do not confuse
the Body, which icon is blue, with the Part container which icon is yellow._
In the Model tab under the Combo View sidebar, a new object labelled "Body"
appears under the document label, which is currently "Unnamed" since we
haven't saved our document yet. The Body is a container in which Part Design
features are sequentially arranged to form a single solid. It contains its own
reference axes and planes. It will be highlighted in light blue in the Model
tree, which means that it is active, that is to say that we can edit the
elements it contains as well as add new elements to it. If it's not
highlighted, double-click it or right-click and select _Toggle active body_ in
the contextual menu. In front of the Body label, there is a blue icon
identical to the one above, and an arrow or a plus sign, depending on your
operating system. Clicking on the arrow or plus sign in front of Body expands
its content. At this point, it only contains an element labelled _Origin_. In
front of this _Origin_ is also an arrow or plus sign. Click on it to expand
its content. It reveals the aforementioned reference axes and planes as shown
in the image below:

[![](/images/e/e8/PartDesign_Body_tree_Unnamed.png)](/index.php?title=File:PartDesign_Body_tree_Unnamed.png&filetimestamp=20180723202230&)

_The newly created active Body with its content expanded._

The _Origin_ is greyed out, which indicates that its content is not visible in
the 3D view. You can make _Origin'_ s content visible in the 3D view by
selecting _Origin_ and pressing the spacebar on your keyboard. _Origin_ will
now show black in the tree. Press the spacebar again to hide its content in
the 3D view. Click again on the arrow or plus sign in front of _Origin_ to
collapse its content in the Model tree.

Before we continue, let's take the opportunity to rename the Body.

**Rename body:**

In the Model tree, click on the Body with the right mouse button. Select
Rename and type a name, for example "Body part1" and press Enter to validate.

**Create sketch:**

We will now trace the sketch which defines the general shape of the part. A
sketch is a diagram describing a profile to be applied to a feature in order
to produce a shape. It can be either "positive" or "additive", like a pad for
example; or "negative" or "subtractive", like a pocket.

Here, since the part's general shape is regular along the Y axis, we will
create the Pad along this axis.

Press
[![](/images/f/f1/Sketcher_NewSketch.svg)](/index.php?title=File:Sketcher_NewSketch.svg&filetimestamp=20231231201726&)
[New sketch](/Sketcher_NewSketch "Sketcher NewSketch"). The Combo View now
switches to the **Tasks** tab and displays the _Select feature_ dialog. This
dialog expects the selection of a plane to which to attach our sketch, and
lists the available planes. Select _XZ_Plane (Base plane)_ and press OK. The
interface now changes, the Sketcher now takes over and its toolbars appear
above the 3D view. We find ourselves on the XZ plane of the body to trace the
sketch.

To aid with sketching, set the following options in "Edit controls" in the
Tasks panel to the left:

  * Show grid: checked
  * Grid size: 10 mm
  * Auto constraints: checked

We will trace the following sketch:

[![](/images/8/8d/GGTuto1_0.PNG)](/index.php?title=File:GGTuto1_0.PNG&filetimestamp=20180404143737&)

**Let's start with the first segments:**

Select the
[![](/images/3/32/Sketcher_Line.svg)](/index.php?title=File:Sketcher_Line.svg&filetimestamp=20170323210839&)
[Line](/Sketcher_CreateLine "Sketcher CreateLine") tool. Click on the origin
point, first making sure that a small red dot appears besides and to the right
of the mouse pointer. Click next on the X axis about 10 squares to the right
or at about 100 mm. If the segment is not exactly 100 mm at this point, it
does not matter, we will later give it a fixed dimension that will constrain
this length.

Do the same for the other segments, try to aim at the points that you have
created which must light up in yellow. Which means that these points will be
coincident. You should get pretty much this:

[![](/images/9/9e/GGTuto1_1.PNG)](/index.php?title=File:GGTuto1_1.PNG&filetimestamp=20180404145042&)

Note the small red lines above and beside the segments you have drawn: these
are horizontal and vertical constraints. Your lines are forced to stay either
horizontal or vertical. Note also the symbol in the form of a small arc on the
left: it means that the point is fixed to the Z axis.

Now pick different line segments with the left mouse button and while keeping
the left button pressed, drag the mouse to try to move them: some are free,
others not.

**Applying constraints:**

At the top of the combo box, in the Tasks panel, you can read the number of
degrees of freedom of the already sketched elements: it must be about 6, the
objective of the constraints is to reduce the number of degrees of freedom to
0.

The slanted line should be free to rotate at this time: we will give it an
angle constraint to fix it.

Click on the slanted line, then the bottom line; once selected these lines
will turn dark green; then click the
[![](/images/3/3b/Constraint_InternalAngle.svg)](/index.php?title=File:Constraint_InternalAngle.svg&filetimestamp=20231231195514&)
[Constrain internal angle](/Sketcher_ConstrainAngle "Sketcher ConstrainAngle")
icon.

[![](/images/a/ab/GGTuto1_2.PNG)](/index.php?title=File:GGTuto1_2.PNG&filetimestamp=20180424031258&)

Enter a value of 30°. Both lines have a fixed angle now. The constraint was
created to the left of the sketch; with the mouse, move it inside the profile.

We will now constrain the bottom line with a dimension: select it then click
on
[![](/images/0/00/Constraint_HorizontalDistance.svg)](/index.php?title=File:Constraint_HorizontalDistance.svg&filetimestamp=20231231195335&)
[Constrain horizontal distance](/Sketcher_ConstrainDistanceX "Sketcher
ConstrainDistanceX").

Enter a value of 100 mm. The vertical line on the right now aligns exactly
with the grid's 10th square to the right of the origin.

Let's set the overall height to the profile by selecting the highest point on
the left then the origin point. Click on
[![](/images/9/97/Constraint_VerticalDistance.svg)](/index.php?title=File:Constraint_VerticalDistance.svg&filetimestamp=20231231200028&)
[constrain vertical distance](/Sketcher_ConstrainDistanceY "Sketcher
ConstrainDistanceY"), enter a value of 50 mm.

Do the same for the horizontal length of the sloped line with another 50 mm
horizontal distance constraint.

Move the dimensions away from the profile for better visibility. You should
now have something like this:

[![](/images/6/66/GGTuto1_3.PNG)](/index.php?title=File:GGTuto1_3.PNG&filetimestamp=20180404145419&)

Notice that the number of degrees of freedom reduced to 2. These are the ends
still open.

**Tracing the arc**

Click on
[![](/images/0/08/Sketcher_Arc.svg)](/index.php?title=File:Sketcher_Arc.svg&filetimestamp=20170323210906&)
[Arc](/Sketcher_CreateArc "Sketcher CreateArc"), position the center at
approximately x = 80 y = 30; then click to define the first starting point of
the arc on the upper horizontal line's right end point; then click to define
the end of the arc to the right vertical line's upper end point (make sure the
points are highlighted in yellow before clicking).

Give the radius a radius constraint: select the arc, then click on
[![](/images/b/b2/Constraint_Radius.svg)](/index.php?title=File:Constraint_Radius.svg&filetimestamp=20231231195846&)
[Constrain radius](/Sketcher_ConstrainRadius "Sketcher ConstrainRadius") then
enter a value of 20 mm.

Now let's make the arc tangent to the lines it's connected to: select the arc,
then the top line, then click on
[![](/images/5/56/Constraint_Tangent.svg)](/index.php?title=File:Constraint_Tangent.svg&filetimestamp=20231231195942&)
[Constrain tangent](/Sketcher_ConstrainTangent "Sketcher ConstrainTangent"). A
_Constraint substitution_ message appears, click OK. Do the same for the
tangent constraint on the other side of the arc.

We proceeded in two stages to create the sketch, but we could also have traced
the profile completely before constraining it fully.

  
**Fully constrained sketch:**

If you worked well, you should get this:

[![](/images/7/7a/GGTuto1_4.PNG)](/index.php?title=File:GGTuto1_4.PNG&filetimestamp=20180404145610&)

The sketch has become green, which means that it is fully constrained. There
is no longer any ambiguity, everything is perfectly defined. This is confirmed
by the solver message at the top left. Also note that the center of the arc
has moved slightly, indeed giving these last three constraints, FreeCAD has
calculated the true position of the center.

If your sketch is not yet green, one or more points are not coincident (2
points can be superimposed yet not be coincident). Make a small window
(capture window) around a point to select, and create a
[![](/images/e/ea/Constraint_PointOnPoint.svg)](/index.php?title=File:Constraint_PointOnPoint.svg&filetimestamp=20231231195749&)
[Coincident constraint](/Sketcher_ConstrainCoincident "Sketcher
ConstrainCoincident"). _Note: don't mistake the Coincident constraint for the
Sketcher Point; while their icons are very similar, the latter has a larger
icon; it adds a lone point in the sketch._

Proceed in the same way with all the points.

If your sketch is still not green, verify that all lines (but the slanted one)
have either a
[![](/images/f/f2/Constraint_Horizontal.svg)](/index.php?title=File:Constraint_Horizontal.svg&filetimestamp=20231231195319&)
[Horizontal](/Sketcher_ConstrainHorizontal "Sketcher ConstrainHorizontal") or
[![](/images/c/c0/Constraint_Vertical.svg)](/index.php?title=File:Constraint_Vertical.svg&filetimestamp=20231231200018&)
[Vertical](/Sketcher_ConstrainVertical "Sketcher ConstrainVertical")
constraint, and add if necessary.

### Using Pad and Pocket features

Click on Close in the Tasks tab, at the top left corner. We automatically exit
the Sketcher workbench, and the Part Design workbench is activated again. The
Combo View switches back to the Model tab. If you left your _Body part1_
expanded, you will see a new **Sketch** element below _Origin_ , and nested
under the Body.

At this point, let's save our document. Give it a name (for example
"tutorial1", or any name that you find relevant). It is good practice to save
your document often, for example after completing a sketch or a feature.

Click on
[![](/images/b/b1/Std_ViewIsometric.svg)](/index.php?title=File:Std_ViewIsometric.svg&filetimestamp=20240704204910&)
**Isometric view** then
[![](/images/6/66/Std_ViewFitAll.svg)](/index.php?title=File:Std_ViewFitAll.svg&filetimestamp=20240704204734&)
[Fit all](/Std_ViewFitAll "Std ViewFitAll"), which gives a centered 3D
isometric view.

Click on
[![](/images/f/f8/PartDesign_Pad.svg)](/index.php?title=File:PartDesign_Pad.svg&filetimestamp=20240522201513&)
[Pad](/PartDesign_Pad "PartDesign Pad"), enter a length of 30 mm. Click OK,
the shape is completed. In the Model tree, a **Pad** object (that we call
feature) appears instead of the Sketch. In fact, it has claimed Sketch, since
it is based on it; clicking on the arrow or plus sign in front of _Pad_ to
expand it will reveal the Sketch underneath, which was automatically made
hidden (its label is grayed out).

Note that the shape created forms a solid.

[![](/images/5/59/GGTuto1_5.PNG)](/index.php?title=File:GGTuto1_5.PNG&filetimestamp=20180409012958&)

**Creating the hole**

Click on the top (square) side of the part and click the
[![](/images/f/f1/Sketcher_NewSketch.svg)](/index.php?title=File:Sketcher_NewSketch.svg&filetimestamp=20231231201726&)
icon to create a new sketch. FreeCAD creates a new sketch attached to this
face. So we are on a plane parallel to the absolute plane XY, but offset in
height from the height of the piece, i.e. 50 mm.

You can switch the 3D window to an isometric view
[![](/images/b/b1/Std_ViewIsometric.svg)](/index.php?title=File:Std_ViewIsometric.svg&filetimestamp=20240704204910&)
or stay in top view
[![](/images/b/bd/Std_ViewTop.svg)](/index.php?title=File:Std_ViewTop.svg&filetimestamp=20240704205120&).
At any time, you can return to Sketch view (the view is oriented to face the
sketch plane) using the
[![](/images/f/f7/Sketcher_ViewSketch.svg)](/index.php?title=File:Sketcher_ViewSketch.svg&filetimestamp=20231231201925&)
[Sketcher ViewSketch](/Sketcher_ViewSketch "Sketcher ViewSketch") icon.

Note that the origin of this new sketch is that of the body. They may be
different, but here are confounded with the absolute origin.

With the
[![](/images/f/f3/Sketcher_Circle.svg)](/index.php?title=File:Sketcher_Circle.svg&filetimestamp=20170323210933&)
[Circle](/Sketcher_CreateCircle "Sketcher CreateCircle") tool, click roughly
in the center of the face and make a circle of any radius.

Select the circle then create a
[![](/images/b/b2/Constraint_Radius.svg)](/index.php?title=File:Constraint_Radius.svg&filetimestamp=20231231195846&)
[Radius constraint](/Sketcher_ConstrainRadius "Sketcher ConstrainRadius"),
enter a value of 5 mm.

Select the center of the circle then create a
[![](/images/8/85/Sketcher_ConstrainLock.svg)](/index.php?title=File:Sketcher_ConstrainLock.svg&filetimestamp=20240101173404&)
[Lock constraint](/Sketcher_ConstrainLock "Sketcher ConstrainLock"); double-
click on the horizontal dimension and enter -65 mm (here we indicate a
position relative to the origin of the sketch). Do the same for the vertical
dimension (15 mm). The circle takes its correct position and the sketch
becomes green, indicating it is fully constrained:

[![](/images/1/1b/GGTuto1_6.PNG)](/index.php?title=File:GGTuto1_6.PNG&filetimestamp=20180409013213&)

Close the sketch; in the Model tree, a new **Sketch001** object has appeared
below Pad. While Sketch001 is still selected, click on
[![](/images/9/93/PartDesign_Pocket.svg)](/index.php?title=File:PartDesign_Pocket.svg&filetimestamp=20170324053209&)
[Pocket](/PartDesign_Pocket "PartDesign Pocket").

Pocket is a feature called "subtractive", it removes material from our part,
here in the form of a cylinder since the sketch is a circle. Set "Through all"
to completely cut the part. Press OK to complete. In the Model tree, a new
element labelled **Pocket** appears at the bottom of the Body part1, and
claims Sketch001.

### Changing color and transparency

It is possible to change the color of the part, it is often useful to
distinguish a part among others. The transparency of the piece can also be
modified, which is useful for visualizing its internals.

Select the **Body part1** body; make sure that the Model tab of the Combo View
is selected and go to the lower part of the Combo View, then click on the View
tab; locate the _Shape Color_ property; you may need to use the vertical
scroll bar to the right to find it. _You can also widen the Property column:
hover your mouse pointer over the separating line between the_ Property _and_
Value _headers; when the pointer turns into a double-sided arrow, press and
hold your left mouse button and drag sideways, then release._ In the right
column, click on the gray square, which opens the **Select Color** dialog.
Pick another color then click OK. Next, again in the View tab, change the
value of Transparency, for example to 50 and press Enter to complete (0 =
totally opaque, 100 = totally transparent).

The hole is now visible inside the part. This is often useful for seeing the
hidden or internal faces of the model.

You can also vary "Line Color" and "Line Width" to change the line thickness
and the color of the part outline.

### Manually move the part

Go to the _View_ menu and select _Toggle axis cross_. These are the absolute
axes. You should see in the 3D view, the 3 axes X, Y, Z in red, green and
blue. This landmark will help us to orient ourselves in space. This landmark
is fixed and immutable, it is either the view that rotates or the object that
rotates in this space.

Select the Body; at the bottom of the Combo View on the left, you can see this
(the _Data_ tab needs to be on the foreground, you may need to click on the
_Data_ tab to make it visible):

[![](/images/f/f9/GGTuto1_10.PNG)](/index.php?title=File:GGTuto1_10.PNG&filetimestamp=20180415051258&)

Click on the three small dots, i.e., the ellipsis (if they don't appear, click
on the Value section of the **Placement** field); this opens a new dialog in
the Tasks panel. Using the arrows you can vary the position and angles of the
part. It is actually the position of the body (so its origin) that moves in
space, the orientation of the 3D view does not change.

Another method: in the Combo View, select the Body and click on the right
button of the mouse, then select _Transform_. A view like this appears:

[![](/images/c/c0/GGTuto1_11.PNG)](/index.php?title=File:GGTuto1_11.PNG&filetimestamp=20180415052048&)

Hold and drag the cones along the axes or the spheres to move the body in all
directions.

Validate. Then reset angles and coordinates to 0.

### Displaying reference dimensions in the sketch

It may be useful to know the dimensions of some parts of the sketch, from the
internal calculation of FreeCAD. It can be used just for reference, or use
them later to set other dimensions for example.

In the Model tree, if necessary expand _Body part1_ then _Pad_ to show the
first Sketch. Double-click on it (or right-click and select _Edit sketch_ in
the contextual menu) then click on
[![](/images/f/fd/Sketcher_ToggleConstraint.svg)](/index.php?title=File:Sketcher_ToggleConstraint.svg&filetimestamp=20231231200147&)
[Toggle Constraint](/Sketcher_ToggleDrivingConstraint "Sketcher
ToggleDrivingConstraint"). (**Note:** depending on your computer display
resolution, this icon may not be visible. At the right end of the Constraints
toolbar, you may find a » button. Click on it to expand and access collapsed
icons.) From now on, we can create reference dimensions rather than
dimensional constraints: they will be blue and will have no influence on the
shapes of the sketch from which they come, they are calculated automatically.

You can display these dimensions for example:

[![](/images/0/03/GGTuto1_7.PNG)](/index.php?title=File:GGTuto1_7.PNG&filetimestamp=20180415024239&)

We can see for example that the arc has a length of 20 since it's tangent with
the edges.

We can also see that FreeCAD calculates the left face (50-50xTAN 30 °), as
well as the distance dimension of the axis of the arc with the origin.

### Editing one or more dimensions

During modeling, you can vary the dimensions of the model. It's very simple:
for the thickness of the piece, double-click Pad, then enter a new value, 40mm
for example. In the lower part of the combo view, you can change this value as
well. Validate, the shape of the object has changed.

Do the same for the total length of the piece: double-click on Sketch, then
double-click on the 100 mm dimensional constraint, change it to 110 mm then
validate.

We can see that the piece was enlarged, but the hole is no longer centered in
the middle of the top face. That's because it has been constrained to the
sketch origin. Which does not necessarily correspond to what one would like,
the hole should remain in the center, whatever the size of the face.

  

### Center the hole

**First method using external geometry.**

Edit again the sketch of the hole and erase its horizontal and vertical
distance constraints.

Then click on
[![](/images/b/b2/Sketcher_External.svg)](/index.php?title=File:Sketcher_External.svg&filetimestamp=20240101091332&)
[External Geometry](/Sketcher_External "Sketcher External").

We will now create two lines in the sketch, but extracted from a shape (or
feature) external to this one and previously defined: that of the Pad.

Click on a vertical edge at the top of the part. For example, the edge slope
side.

A new magenta line will appear above the edge. Repeat for the other edge, on
the rounded side.

We can now use these lines (and especially their end points) to centre the
circle, however we must add two construction lines: for example the diagonals.

Click on
[![](/images/5/54/Sketcher_ToggleConstruction.svg)](/index.php?title=File:Sketcher_ToggleConstruction.svg&filetimestamp=20240228175128&)
[Construction Mode](/Sketcher_ToggleConstruction "Sketcher
ToggleConstruction"), we switch to construction mode: the lines will be blue
and will be discarded outside of the sketch editing mode. They will allow to
fix the center of the circle. Create the diagonals in the same way that you
drew the first lines. Make sure all points are coincident.

Then select the center of the circle, then the two blue diagonal lines and
click on
[![](/images/6/64/Constraint_PointOnObject.svg)](/index.php?title=File:Constraint_PointOnObject.svg&filetimestamp=20231231195734&)
[Point on object](/Sketcher_ConstrainPointOnObject "Sketcher
ConstrainPointOnObject"), the circle must be centred at the intersection of
the diagonals, that is at the center of the face. The sketch must be green,
completely constrained (it is essential). Note that besides the radius of the
circle, it is no longer necessary to create dimensional constraints.

Please note that in addition to switching the the toolbar to construction
mode, the
[![](/images/5/54/Sketcher_ToggleConstruction.svg)](/index.php?title=File:Sketcher_ToggleConstruction.svg&filetimestamp=20240228175128&)
[Construction Mode](/Sketcher_ToggleConstruction "Sketcher
ToggleConstruction") button can also switch individual Sketcher elements to
construction mode if they have been selected. If you accidentally switch an
element to construction mode, you may get an error when you exit the sketch.

[![](/images/9/98/GGTuto1_8.PNG)](/index.php?title=File:GGTuto1_8.PNG&filetimestamp=20180415032841&)

Leave the sketch, we see that the circle is well centred. (The pocket feature
was not deleted, but modified). If you change the dimensions of the part
again, the thickness or the length, the circle will remain centered on the
face.

**Avoid construction lines:**

It is often possible to avoid creating construction lines. You can edit the
sketch again, erase the construction lines and use a
[![](/images/d/dc/Constraint_Symmetric.svg)](/index.php?title=File:Constraint_Symmetric.svg&filetimestamp=20231231195931&)
[Symmetric constraint](/Sketcher_ConstrainSymmetric "Sketcher
ConstrainSymmetric") between the two opposite vertices of the external
geometry lines and the centre of the circle (select points in this order):

[![](/images/b/b8/GGTuto1_12.PNG)](/index.php?title=File:GGTuto1_12.PNG&filetimestamp=20180416033300&)

We get exactly the same result for the position of the hole. In fact, thanks
to the constraints available in the Sketcher workbench, there are many
possible methods. This example shows that it is often better to choose the
simplest method, thus limiting the number of objects created as well as the
errors that might result.

**Second method using a datum plane.**

Here is another, faster method that is possible since version 0.17: the use of
a datum plane and its attachment.

Start by erasing the "Pocket" function as well as the sketch of the hole.
Select the top face and click
[![](/images/2/27/PartDesign_Point.svg)](/index.php?title=File:PartDesign_Point.svg&filetimestamp=20240405093024&)
[Datum point](/PartDesign_Point "PartDesign Point"): create a datum point in
the active body. The attachment mode chosen must be "Center of mass".

As the face is rectangular, its center of mass corresponds to the center of
its diagonals. Validate, and a datum point is created.

Select the top face again and while holding down the CTRL key, select the
point you just created in the Model tree, release CTRL and click
[![](/images/e/e5/PartDesign_Plane.svg)](/index.php?title=File:PartDesign_Plane.svg&filetimestamp=20170324054826&)
[Datum plane](/PartDesign_Plane "PartDesign Plane"). A reference plane is
created with the origin of the point. Click OK.

It is now very easy to center the circle! Select from the Model tree or in the
3D view the plane you created, and click on
[![](/images/f/f1/Sketcher_NewSketch.svg)](/index.php?title=File:Sketcher_NewSketch.svg&filetimestamp=20231231201726&)
[Create a sketch](/Sketcher_NewSketch "Sketcher NewSketch"), a sketch is
created with as origin, the origin of the plane. Then just trace the 5 mm
radius circle on this origin, then validate (the sketch must be green
imperatively).

You get with "Pocket", as created previously, the hole and it will always be
centered.

[![](/images/9/98/GGTuto1_9.PNG)](/index.php?title=File:GGTuto1_9.PNG&filetimestamp=20180415043948&)

This tutorial is completed, save this file, you can have fun exploring various
features. Change other dimensions, make other shapes, put other holes on other
faces, it is when making mistakes that we progress!

You can also continue with this other tutorial of a slightly more complicated
part:

[Basic Part Design Tutorial](/Basic_Part_Design_Tutorial "Basic Part Design
Tutorial")

  

Expand[![](/images/3/39/Workbench_PartDesign.svg)](/index.php?title=File:Workbench_PartDesign.svg&filetimestamp=20240405092932&)
[PartDesign](/PartDesign_Workbench "PartDesign Workbench")

  * **Structure tools:** [Part](/Std_Part "Std Part"), [Group](/Std_Group "Std Group")
  * **Helper tools:** [Create body](/PartDesign_Body "PartDesign Body"), [Create sketch](/PartDesign_NewSketch "PartDesign NewSketch"), [Attach sketch](/Sketcher_MapSketch "Sketcher MapSketch"), [Edit sketch](/Sketcher_EditSketch "Sketcher EditSketch"), [Validate sketch](/Sketcher_ValidateSketch "Sketcher ValidateSketch"), [Check geometry](/Part_CheckGeometry "Part CheckGeometry"), [Create a shape binder](/PartDesign_ShapeBinder "PartDesign ShapeBinder"), [Create a sub-object(s) shape binder](/PartDesign_SubShapeBinder "PartDesign SubShapeBinder"), [Create a clone](/PartDesign_Clone "PartDesign Clone"), [Create a datum plane](/PartDesign_Plane "PartDesign Plane"), [Create a datum line](/PartDesign_Line "PartDesign Line"), [Create a datum point](/PartDesign_Point "PartDesign Point"), [Create a local coordinate system](/PartDesign_CoordinateSystem "PartDesign CoordinateSystem")

* * *

  * **Modeling tools:**
    * **Additive tools:** [Pad](/PartDesign_Pad "PartDesign Pad"), [Revolution](/PartDesign_Revolution "PartDesign Revolution"), [Additive loft](/PartDesign_AdditiveLoft "PartDesign AdditiveLoft"), [Additive pipe](/PartDesign_AdditivePipe "PartDesign AdditivePipe"), [Additive helix](/PartDesign_AdditiveHelix "PartDesign AdditiveHelix"), [Additive box](/PartDesign_AdditiveBox "PartDesign AdditiveBox"), [Additive cylinder](/PartDesign_AdditiveCylinder "PartDesign AdditiveCylinder"), [Additive sphere](/PartDesign_AdditiveSphere "PartDesign AdditiveSphere"), [Additive cone](/PartDesign_AdditiveCone "PartDesign AdditiveCone"), [Additive ellipsoid](/PartDesign_AdditiveEllipsoid "PartDesign AdditiveEllipsoid"), [Additive torus](/PartDesign_AdditiveTorus "PartDesign AdditiveTorus"), [Additive prism](/PartDesign_AdditivePrism "PartDesign AdditivePrism"), [Additive wedge](/PartDesign_AdditiveWedge "PartDesign AdditiveWedge")
    * **Subtractive tools:** [Pocket](/PartDesign_Pocket "PartDesign Pocket"), [Hole](/PartDesign_Hole "PartDesign Hole"), [Groove](/PartDesign_Groove "PartDesign Groove"), [Subtractive loft](/PartDesign_SubtractiveLoft "PartDesign SubtractiveLoft"), [Subtractive pipe](/PartDesign_SubtractivePipe "PartDesign SubtractivePipe"), [Subtractive helix](/PartDesign_SubtractiveHelix "PartDesign SubtractiveHelix"), [Subtractive box](/PartDesign_SubtractiveBox "PartDesign SubtractiveBox"), [Subtractive cylinder](/PartDesign_SubtractiveCylinder "PartDesign SubtractiveCylinder"), [Subtractive sphere](/PartDesign_SubtractiveSphere "PartDesign SubtractiveSphere"), [Subtractive cone](/PartDesign_SubtractiveCone "PartDesign SubtractiveCone"), [Subtractive ellipsoid](/PartDesign_SubtractiveEllipsoid "PartDesign SubtractiveEllipsoid"), [Subtractive torus](/PartDesign_SubtractiveTorus "PartDesign SubtractiveTorus"), [Subtractive prism](/PartDesign_SubtractivePrism "PartDesign SubtractivePrism"), ‎[Subtractive wedge](/PartDesign_SubtractiveWedge "PartDesign SubtractiveWedge")
    * **Boolean:** [Boolean operation](/PartDesign_Boolean "PartDesign Boolean")

* * *

  * **Dress-up tools:** [Fillet](/PartDesign_Fillet "PartDesign Fillet"), [Chamfer](/PartDesign_Chamfer "PartDesign Chamfer"), [Draft](/PartDesign_Draft "PartDesign Draft"), [Thickness](/PartDesign_Thickness "PartDesign Thickness")
  * **Transformation tools:** [Mirrored](/PartDesign_Mirrored "PartDesign Mirrored"), [Linear Pattern](/PartDesign_LinearPattern "PartDesign LinearPattern"), [Polar Pattern](/PartDesign_PolarPattern "PartDesign PolarPattern"), [Create MultiTransform](/PartDesign_MultiTransform "PartDesign MultiTransform"), [Scaled](/PartDesign_Scaled "PartDesign Scaled")

* * *

  * **Extras:** [Sprocket](/PartDesign_Sprocket "PartDesign Sprocket"), [Involute gear](/PartDesign_InvoluteGear "PartDesign InvoluteGear"), [Shaft design wizard](/PartDesign_WizardShaft "PartDesign WizardShaft")
  * **Context menu:** [Set tip](/PartDesign_MoveTip "PartDesign MoveTip"), [Move object to other body](/PartDesign_MoveFeature "PartDesign MoveFeature"), [Move object after other object](/PartDesign_MoveFeatureInTree "PartDesign MoveFeatureInTree"), [Appearance](/Std_SetAppearance "Std SetAppearance"), [Color per face](/Part_ColorPerFace "Part ColorPerFace")
  * **Preferences:** [Preferences](/PartDesign_Preferences "PartDesign Preferences"), [Fine tuning](/Fine-tuning "Fine-tuning")

Expand[![](/images/9/91/Workbench_Sketcher.svg)](/index.php?title=File:Workbench_Sketcher.svg&filetimestamp=20231231194727&)
[Sketcher](/Sketcher_Workbench "Sketcher Workbench")

  * **General:** [Create sketch](/Sketcher_NewSketch "Sketcher NewSketch"), [Edit sketch](/Sketcher_EditSketch "Sketcher EditSketch"), [Attach sketch](/Sketcher_MapSketch "Sketcher MapSketch"), [Reorient sketch](/Sketcher_ReorientSketch "Sketcher ReorientSketch"), [Validate sketch](/Sketcher_ValidateSketch "Sketcher ValidateSketch"), [Merge sketches](/Sketcher_MergeSketches "Sketcher MergeSketches"), [Mirror sketch](/Sketcher_MirrorSketch "Sketcher MirrorSketch"), [Leave sketch](/Sketcher_LeaveSketch "Sketcher LeaveSketch"), [View sketch](/Sketcher_ViewSketch "Sketcher ViewSketch"), [View section](/Sketcher_ViewSection "Sketcher ViewSection"), [Toggle grid](/Sketcher_Grid "Sketcher Grid"), [Toggle snap](/Sketcher_Snap "Sketcher Snap"), [Configure rendering order](/Sketcher_RenderingOrder "Sketcher RenderingOrder"), [Stop operation](/Sketcher_StopOperation "Sketcher StopOperation")

* * *

  * **Sketcher geometries:** [Point](/Sketcher_CreatePoint "Sketcher CreatePoint"), [Polyline](/Sketcher_CreatePolyline "Sketcher CreatePolyline"), [Line](/Sketcher_CreateLine "Sketcher CreateLine"), [Arc](/Sketcher_CreateArc "Sketcher CreateArc"), [Arc by 3 points](/Sketcher_Create3PointArc "Sketcher Create3PointArc"), [Arc of ellipse](/Sketcher_CreateArcOfEllipse "Sketcher CreateArcOfEllipse"), [Arc of hyperbola](/Sketcher_CreateArcOfHyperbola "Sketcher CreateArcOfHyperbola"), [Arc of parabola](/Sketcher_CreateArcOfParabola "Sketcher CreateArcOfParabola"), [Circle](/Sketcher_CreateCircle "Sketcher CreateCircle"), [Circle by 3 points](/Sketcher_Create3PointCircle "Sketcher Create3PointCircle"), [Ellipse](/Sketcher_CreateEllipseByCenter "Sketcher CreateEllipseByCenter"), [Ellipse by 3 points](/Sketcher_CreateEllipseBy3Points "Sketcher CreateEllipseBy3Points"), [Rectangle](/Sketcher_CreateRectangle "Sketcher CreateRectangle"), [Centered rectangle](/Sketcher_CreateRectangle_Center "Sketcher CreateRectangle Center"), [Rounded rectangle](/Sketcher_CreateOblong "Sketcher CreateOblong"), [Triangle](/Sketcher_CreateTriangle "Sketcher CreateTriangle"), [Square](/Sketcher_CreateSquare "Sketcher CreateSquare"), [Pentagon](/Sketcher_CreatePentagon "Sketcher CreatePentagon"), [Hexagon](/Sketcher_CreateHexagon "Sketcher CreateHexagon"), [Heptagon](/Sketcher_CreateHeptagon "Sketcher CreateHeptagon"), [Octagon](/Sketcher_CreateOctagon "Sketcher CreateOctagon"), [Regular polygon](/Sketcher_CreateRegularPolygon "Sketcher CreateRegularPolygon"), [Slot](/Sketcher_CreateSlot "Sketcher CreateSlot"), [Arc slot](/Sketcher_CreateArcSlot "Sketcher CreateArcSlot"), [B-spline by control points](/Sketcher_CreateBSpline "Sketcher CreateBSpline"), [Periodic B-spline by control points](/Sketcher_CreatePeriodicBSpline "Sketcher CreatePeriodicBSpline"), [B-spline by knots](/Sketcher_CreateBSplineByInterpolation "Sketcher CreateBSplineByInterpolation"), [Periodic B-spline by knots](/Sketcher_CreatePeriodicBSplineByInterpolation "Sketcher CreatePeriodicBSplineByInterpolation"), [Toggle construction geometry](/Sketcher_ToggleConstruction "Sketcher ToggleConstruction")

* * *

  * **Sketcher constraints:**
    * **Dimensional constraints:** [Dimension](/Sketcher_Dimension "Sketcher Dimension"), [Horizontal distance](/Sketcher_ConstrainDistanceX "Sketcher ConstrainDistanceX"), [Vertical distance](/Sketcher_ConstrainDistanceY "Sketcher ConstrainDistanceY"), [Distance](/Sketcher_ConstrainDistance "Sketcher ConstrainDistance"), [Auto radius/diameter](/Sketcher_ConstrainRadiam "Sketcher ConstrainRadiam"), [Radius](/Sketcher_ConstrainRadius "Sketcher ConstrainRadius"), [Diameter](/Sketcher_ConstrainDiameter "Sketcher ConstrainDiameter"), [Angle](/Sketcher_ConstrainAngle "Sketcher ConstrainAngle"), [Lock](/Sketcher_ConstrainLock "Sketcher ConstrainLock")
    * **Geometric constraints:** [Coincident (unified)](/Sketcher_ConstrainCoincidentUnified "Sketcher ConstrainCoincidentUnified"), [Coincident](/Sketcher_ConstrainCoincident "Sketcher ConstrainCoincident"), [Point on object](/Sketcher_ConstrainPointOnObject "Sketcher ConstrainPointOnObject"), [Horizontal/vertical](/Sketcher_ConstrainHorVer "Sketcher ConstrainHorVer"), [Horizontal](/Sketcher_ConstrainHorizontal "Sketcher ConstrainHorizontal"), [Vertical](/Sketcher_ConstrainVertical "Sketcher ConstrainVertical"), [Parallel](/Sketcher_ConstrainParallel "Sketcher ConstrainParallel"), [Perpendicular](/Sketcher_ConstrainPerpendicular "Sketcher ConstrainPerpendicular"), [Tangent or collinear](/Sketcher_ConstrainTangent "Sketcher ConstrainTangent"), [Equal](/Sketcher_ConstrainEqual "Sketcher ConstrainEqual"), [Symmetric](/Sketcher_ConstrainSymmetric "Sketcher ConstrainSymmetric"), [Block](/Sketcher_ConstrainBlock "Sketcher ConstrainBlock")
    * **Other constraints:** [Refraction (Snell's law)](/Sketcher_ConstrainSnellsLaw "Sketcher ConstrainSnellsLaw")
    * **Constraint tools:** [Toggle driving/reference constraint](/Sketcher_ToggleDrivingConstraint "Sketcher ToggleDrivingConstraint"), [Activate/deactivate constraint](/Sketcher_ToggleActiveConstraint "Sketcher ToggleActiveConstraint")

* * *

  * **Sketcher tools:** [Fillet](/Sketcher_CreateFillet "Sketcher CreateFillet"), [Chamfer](/Sketcher_CreateChamfer "Sketcher CreateChamfer"), [Trim](/Sketcher_Trimming "Sketcher Trimming"), [Split](/Sketcher_Split "Sketcher Split"), [Extend](/Sketcher_Extend "Sketcher Extend"), [External geometry](/Sketcher_External "Sketcher External"), [Carbon copy](/Sketcher_CarbonCopy "Sketcher CarbonCopy"), [Select origin](/Sketcher_SelectOrigin "Sketcher SelectOrigin"), [Select horizontal axis](/Sketcher_SelectHorizontalAxis "Sketcher SelectHorizontalAxis"), [Select vertical axis](/Sketcher_SelectVerticalAxis "Sketcher SelectVerticalAxis"), [Array transform](/Sketcher_Translate "Sketcher Translate"), [Polar transform](/Sketcher_Rotate "Sketcher Rotate"), [Scale transform](/Sketcher_Scale "Sketcher Scale"), [Offset geometry](/Sketcher_Offset "Sketcher Offset"), [Symmetry](/Sketcher_Symmetry "Sketcher Symmetry"), [Remove axes alignment](/Sketcher_RemoveAxesAlignment "Sketcher RemoveAxesAlignment"), [Delete all geometry](/Sketcher_DeleteAllGeometry "Sketcher DeleteAllGeometry"), [Delete all constraints](/Sketcher_DeleteAllConstraints "Sketcher DeleteAllConstraints")

* * *

  * **Sketcher B-spline tools:** [Convert geometry to B-spline](/Sketcher_BSplineConvertToNURBS "Sketcher BSplineConvertToNURBS"), [Increase B-spline degree](/Sketcher_BSplineIncreaseDegree "Sketcher BSplineIncreaseDegree"), [Decrease B-spline degree](/Sketcher_BSplineDecreaseDegree "Sketcher BSplineDecreaseDegree"), [Increase knot multiplicity](/Sketcher_BSplineIncreaseKnotMultiplicity "Sketcher BSplineIncreaseKnotMultiplicity"), [Decrease knot multiplicity](/Sketcher_BSplineDecreaseKnotMultiplicity "Sketcher BSplineDecreaseKnotMultiplicity"), [Insert knot](/Sketcher_BSplineInsertKnot "Sketcher BSplineInsertKnot"), [Join curves](/Sketcher_JoinCurves "Sketcher JoinCurves")

* * *

  * **Sketcher visual:** [Select unconstrained DoF](/Sketcher_SelectElementsWithDoFs "Sketcher SelectElementsWithDoFs"), [Select associated constraints](/Sketcher_SelectConstraints "Sketcher SelectConstraints"), [Select associated geometry](/Sketcher_SelectElementsAssociatedWithConstraints "Sketcher SelectElementsAssociatedWithConstraints"), [Select redundant constraints](/Sketcher_SelectRedundantConstraints "Sketcher SelectRedundantConstraints"), [Select conflicting constraints](/Sketcher_SelectConflictingConstraints "Sketcher SelectConflictingConstraints"), [Show/hide circular helper for arcs](/Sketcher_ArcOverlay "Sketcher ArcOverlay"), [Show/hide B-spline degree](/Sketcher_BSplineDegree "Sketcher BSplineDegree"), [Show/hide B-spline control polygon](/Sketcher_BSplinePolygon "Sketcher BSplinePolygon"), [Show/hide B-spline curvature comb](/Sketcher_BSplineComb "Sketcher BSplineComb"), [Show/hide B-spline knot multiplicity](/Sketcher_BSplineKnotMultiplicity "Sketcher BSplineKnotMultiplicity"), [Show/hide B-spline control point weight](/Sketcher_BSplinePoleWeight "Sketcher BSplinePoleWeight"), [Show/hide internal geometry](/Sketcher_RestoreInternalAlignmentGeometry "Sketcher RestoreInternalAlignmentGeometry"), [Switch virtual space](/Sketcher_SwitchVirtualSpace "Sketcher SwitchVirtualSpace")

* * *

  * **Additional:** [Sketcher Dialog](/Sketcher_Dialog "Sketcher Dialog"), [Preferences](/Sketcher_Preferences "Sketcher Preferences"), [Sketcher scripting](/Sketcher_scripting "Sketcher scripting")

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

