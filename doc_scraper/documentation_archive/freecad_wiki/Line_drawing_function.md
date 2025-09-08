---
url: https://wiki.freecad.org/Line_drawing_function
title: Line drawing function
scraped_at: 2025-09-08 16:42:11
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 The main script
  * 3 Detailed explanation
  * 4 Testing the script
  * 5 Registering the script
  * 6 So you want more?

# Line drawing function

  * [Page](/Line_drawing_function "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Line_drawing_function&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Line_drawing_function)
  * [Edit](/index.php?title=Line_drawing_function&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Line_drawing_function&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Line_drawing_function.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Line_drawing_function&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Line_drawing_function)
  * [Edit](/index.php?title=Line_drawing_function&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Line_drawing_function&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Line_drawing_function&action=history)

General

  * [What links here](/Special:WhatLinksHere/Line_drawing_function "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Line_drawing_function "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Line_drawing_function&oldid=1604471 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Line_drawing_function&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Line_drawing_function&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Line+drawing+function&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Line+drawing+function&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Line_drawing_function/id "Line drawing function \(3% translated\)")
  * [Deutsch](/Line_drawing_function/de "Linienzeichnungsfunktion \(100% translated\)")
  * English
  * [Türkçe](/Line_drawing_function/tr "Line drawing function \(3% translated\)")
  * [español](/Line_drawing_function/es "Line drawing function \(12% translated\)")
  * [français](/Line_drawing_function/fr "Fonction - tracer une ligne \(100% translated\)")
  * [italiano](/Line_drawing_function/it "Funzione per disegnare delle linee \(35% translated\)")
  * [polski](/Line_drawing_function/pl "Funkcja rysowania linii \(100% translated\)")
  * [română](/Line_drawing_function/ro "Funcția de Desenare a liniei \(12% translated\)")
  * [svenska](/Line_drawing_function/sv "Line drawing function \(12% translated\)")
  * [čeština](/Line_drawing_function/cs "Line drawing function \(3% translated\)")
  * [русский](/Line_drawing_function/ru "Функция рисования линии \(100% translated\)")

## Introduction

This page shows how advanced functionality can easily be created in Python. In
this exercise, we will build a new tool that draws a line. This tool can then
be linked to a FreeCAD command, and that command can be called by any element
in the interface, like a menu item or a toolbar button.

## The main script

First we will write a script containing all our functionality. Then we will
save this in a file and import it in FreeCAD to make all its classes and
functions available. Launch your favorite code editor and type the following
lines:

    
    
    import FreeCADGui, Part
    from pivy.coin import *
    
    class line:
    
        """This class will create a line after the user clicked 2 points on the screen"""
    
        def __init__(self):
            self.view = FreeCADGui.ActiveDocument.ActiveView
            self.stack = []
            self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
    
        def getpoint(self, event_cb):
            event = event_cb.getEvent()
            if event.getState() == SoMouseButtonEvent.DOWN:
                pos = event.getPosition()
                point = self.view.getPoint(pos[0], pos[1])
                self.stack.append(point)
                if len(self.stack) == 2:
                    l = Part.LineSegment(self.stack[0], self.stack[1])
                    shape = l.toShape()
                    Part.show(shape)
                    self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
    

Top

## Detailed explanation

    
    
    import Part, FreeCADGui
    from pivy.coin import *
    

In Python when you want to use functions from another module you need to
import it. In our case we will need functions from the [Part](/Part_Workbench
"Part Workbench") module, for creating the line, and from the Gui module
`FreeCADGui`, for accessing the [3D view](/3D_view "3D view"). We also need
the complete contents of the Coin library so we can directly use all Coin
objects like `SoMouseButtonEvent`, etc.

    
    
    class line:
    

Here we define our main class. Why do we use a class and not a function? The
reason is that we need our tool to stay "alive" while we are waiting for the
user to click on the screen. A function ends when its task has been done, but
an object (a class defines an object) stays alive until it is destroyed.

    
    
    """This class will create a line after the user clicked 2 points on the screen"""
    

In Python, every class or function can have a documentation string
(docstring). This is particularly useful in FreeCAD, because when you call
that class in the interpreter, the description string will be displayed as a
tooltip.

    
    
    def __init__(self):
    

Python classes can always contain an `__init__` function, which is executed
when the class is called to create an object. Here we will put everything we
want to happen when our line tool begins.

    
    
    self.view = FreeCADGui.ActiveDocument.ActiveView
    

In a class you usually want to prepend `self.` to variable names to make the
variables easily accessible to all functions inside and outside the class.
Here we will use `self.view` to access and manipulate the active 3D view.

    
    
    self.stack = []
    

Here we create an empty list that will contain the 3D points sent by the
`getpoint()` function.

    
    
    self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
    

This is the important part. Since we are dealing with a
[Coin3D](https://github.com/coin3d/coin/wiki) scene, we use a Coin callback
mechanism that allows a function to be called every time a certain scene event
happens. In our case we are creating a callback for
[SoMouseButtonEvent](https://coin3d.github.io/Coin/html/classSoMouseButtonEvent.html)
events, and we bind it to the `getpoint()` function. Now every time a mouse
button is pressed or released the `getpoint()` function will be executed.

Note that there is also an alternative to `addEventCallbackPivy()` called
`addEventCallback()` which does not rely on pivy. But since pivy is a very
efficient and natural way to access any part of a Coin scene, it is the better
choice.

Top

    
    
    def getpoint(self, event_cb):
    

Now we define the `getpoint()` function that will be executed when a mouse
button is pressed in a 3D view. This function will receive an argument that we
will call `event_cb`. From this event callback we can access the event object,
which contains several pieces of information (more info
[here](/Code_snippets#Observe_mouse_events_in_the_3D_viewer_via_Python "Code
snippets")).

    
    
    if event.getState() == SoMouseButtonEvent.DOWN:
    

The `getpoint()` function will be called when a mouse button is pressed or
released. But we only want to pick a 3D point when a button is pressed,
otherwise we would end up with two 3D points very close together. So we must
check for that here.

    
    
    pos = event.getPosition()
    

Here we get the screen coordinates of the mouse cursor.

    
    
    point = self.view.getPoint(pos[0], pos[1])
    

This function gives us a FreeCAD vector (x,y,z) containing the 3D point that
lies on the focal plane, just under our mouse cursor. If you are in camera
view, imagine a ray coming from the camera, passing through the mouse cursor,
and hitting the focal plane. That is the location of our 3D point. If we are
in orthogonal view, the ray is parallel to the view direction.

    
    
    self.stack.append(point)
    

We add our new point to the stack.

    
    
    if len(self.stack) == 2:
    

Do we have enough points already? if yes, then let's draw the line!

    
    
    l = Part.LineSegment(self.stack[0], self.stack[1])
    

Here we use the `LineSegment()` function from the Part module that creates a
line from two FreeCAD vectors. The line is not bound to any object in our
active document, so nothing appears on the screen.

    
    
    shape = l.toShape()
    

The FreeCAD document can only accept shapes from the Part module. Shapes are
the most generic type of the Part module. So we must convert our line to a
shape before adding it to the document.

    
    
    Part.show(shape)
    

The Part module has a very handy `show()` function that creates a new object
in the document and binds a shape to it. We could also have created a new
object in the document first and then bound the shape to it manually.

    
    
    self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
    

Since we are done with our line we remove the callback mechanism here.

Top

## Testing the script

Now let's save our script in a folder where the FreeCAD Python interpreter can
find it. When importing modules, the interpreter will look in the following
places: the Python installation paths, the FreeCAD bin folder, and all FreeCAD
Mod (module) folders. So the best solution is to create a new folder in one of
the Mod folders. Let's create a MyScripts folder there and save our script in
it as exercise.py.

Now everything is ready. Let's start FreeCAD, create a new document, and in
the Python interpreter issue:

    
    
    import exercise
    

If no error message appears our exercise script has been loaded successfully.
We can now check its contents with:

    
    
    dir(exercise)
    

The command `dir()` is a built-in Python command that lists the contents of a
module. We can check that our `line()` class is there with:

    
    
    'line' in dir(exercise)
    

Now let's test it:

    
    
    exercise.line()
    

Click two times in the 3D view and bingo: here is our line! To repeat it just
type `exercise.line()` again.

Top

## Registering the script

For our new line tool to be really useful, and to avoid having to type all
that stuff, it should have a button in the interface. One way to do this is to
transform our new MyScripts folder into a full FreeCAD workbench. This is
easy, all that is needed is to put a file called InitGui.py inside the
MyScripts folder. InitGui.py will contain the instructions to create a new
workbench, and add our new tool to it. Besides that we will also need to
change our exercise code a bit, so the `line()` tool is recognized as an
official FreeCAD command. Let's start by creating an InitGui.py file, and
writing the following code in it:

    
    
    class MyWorkbench (Workbench):
    
        MenuText = "MyScripts"
    
        def Initialize(self):
            import exercise
            commandslist = ["line"]
            self.appendToolbar("My Scripts", commandslist)
    
    Gui.addWorkbench(MyWorkbench())
    

By now you probably understand the above script. We create a new class that we
call `MyWorkbench`, we give it a title `MenuText`, and we define an
`Initialize()` function that will be executed when the workbench is loaded
into FreeCAD. In that function, we load the contents of our exercise file, and
append the FreeCAD commands found inside to a command list. Then, we make a
toolbar called "My Scripts" and we assign our command list to it. Currently,
of course, we only have one tool, so our command list contains only one
element. Then, once our workbench is ready, we add it to the main interface.

But this still won't work because a FreeCAD command must be formatted in a
certain manner to work, we will need to change our `line()` tool. Our new
exercise.py script should look like this:

    
    
    import FreeCADGui, Part
    from pivy.coin import *
    
    class line:
    
        """This class will create a line after the user clicked 2 points on the screen"""
    
        def Activated(self):
            self.view = FreeCADGui.ActiveDocument.ActiveView
            self.stack = []
            self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
    
        def getpoint(self, event_cb):
            event = event_cb.getEvent()
            if event.getState() == SoMouseButtonEvent.DOWN:
                pos = event.getPosition()
                point = self.view.getPoint(pos[0], pos[1])
                self.stack.append(point)
                if len(self.stack) == 2:
                    l = Part.LineSegment(self.stack[0], self.stack[1])
                    shape = l.toShape()
                    Part.show(shape)
                    self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
    
        def GetResources(self):
            return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}
    
    FreeCADGui.addCommand('line', line())
    

What we did here is transform our `__init__()` function into an `Activated()`
function. When FreeCAD commands are run, they automatically execute the
`Activated()` function. We also added a `GetResources()` function, that
informs FreeCAD where it can find the icon for the tool, and what will be the
name and tooltip of our tool. Any jpg, png or svg image will work as an icon,
it can be any size, but it is best to use a size that is close to the final
aspect, like 16x16, 24x24 or 32x32. Then we add the `line()` class as an
official FreeCAD command with the `addCommand()` method.

That's it, now we just need to restart FreeCAD and we'll have a nice new
workbench with our brand new line tool!

Top

## So you want more?

If you liked this exercise, why not try to improve this little tool? There are
many things that can be done, for example:

  * Add user feedback: until now we did a very bare tool, the user might be a bit lost when using it. So we could add some feedback, telling the user what to do next. You could issue messages to the FreeCAD console. Have a look in the `FreeCAD.Console` module.
  * Add a possibility to type the 3D points coordinates manually. Look at the Python `input()` function for example.
  * Add the possibility to add more than 2 points.
  * Add events for other things: Now we just check for Mouse button events, what if we would also do something when the mouse is moved, like displaying current coordinates?
  * Give a name to the created object.

Don't hesitate to ask questions or share ideas on the
[forum](https://forum.freecad.org)!

Top

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), Line drawing function, [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

