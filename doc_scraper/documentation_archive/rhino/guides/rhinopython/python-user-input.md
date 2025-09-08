---
url: https://developer.rhino3d.com/guides/rhinopython/python-user-input/
scraped_at: 2025-09-08T15:37:51.053547
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[How to get user input in a
script](https://developer.rhino3d.com/guides/rhinopython/python-user-input/)

  * Overview
  * The GET methods
    * Command Line gets
    * Interactive gets
    * Geometry Gets
  * Special Dialogs
  * File System dialogs
  * Eto Custom Dialog Framework
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

How to get user input in a script

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Prompting the user of a script for the input of a value, selecting a layer,
picking a point or selecting a Rhino object is important to many interactive
scripts. Many input methods will also validate the user input to make sure
only the proper input is accepted.

The RhinoscriptSyntax module contains many ways to interactively prompt for
several different types of input. There are three main styles of input that
are contained in Rhinosciptsyntax:

  * [**Get methods**](https://developer.rhino3d.com/guides/rhinopython/python-user-input/#the-get-methods). These are methods that work with the command line, wait for mouse input or prompt for specific input.
  * [**Special Dialogs**](https://developer.rhino3d.com/guides/rhinopython/python-user-input/#special-dialogs). There are some simple specific dialogs to prompt for input
  * [**File system dialogs**](https://developer.rhino3d.com/guides/rhinopython/python-user-input/#file-system-dialogs). Browsing, saving and opening files on the system with Python.
  * [**Eto Custom Dialog Framework**](https://developer.rhino3d.com/guides/rhinopython/python-user-input/#eto-custom-dialog-framework). A cross-platform dialog framework to create more custom modal and non-modal dialog box classes that can be used in scripts.

## The GET methods

Get are basic ways to prompt for specifc user feedback on the commandline and
mouse input. Good examples of a Get might be get a point, a string, or a
distance. There are 25 get methods that can

  1. **Commandline Gets** \- [GetReal](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetReal), [GetString](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetString), [GetInteger](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetInteger), [GetBoolean](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetBoolean)
  2. **Interactive Gets** \- [GetPoint](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPoint)([s](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPoints)), [GetPointCoordinates](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPointCoordinates), [GetLine](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetLine), [GetDistance](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetDistance), [GetAngle](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetAngle), [GetPolyline](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPolyline), [GetRectangle](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetRectangle), [GetBox](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetBox), [GetCursorPos](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetCursorPos).
  3. **Geometry Gets** \- [GetObject](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetObject), [GetCurveObject](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetCurveObject), [GetSurfaceObject](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetSurfaceObject), [GetEdgeCurves](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetEdgeCurves), [GetMeshFaces](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetMeshFaces), [GetMeshVertices](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetMeshVertices), [GetPointOnCurve](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPointOnCurve), [GetPointOnMesh](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPointOnMesh), [GetPointOnSurface](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-GetPointOnSurface).

### Command Line gets

The simplest Get function is to ask for a specific value on the command line.
For instance a Get method may prompting for a _number_ on the command line
with `rs.GetReal()`.

#### Getreal()

    
    
    import rhinoscriptsyntax as rs
    
    # GetReal prompts on the command line with optional defaults and a minimum allowable value
    radius = rs.GetReal("Radius of new circle", 3.14, 1.0)
    if radius: rs.AddCircle( (0,0,0), radius )
    

![https://developer.rhino3d.com/images/getreal.png](https://developer.rhino3d.com/images/getreal.png)

rs.GetReal() accepts any number, including decimals. In some cases your code
may need only whole numbers- in this case use `rs.GetInteger()`

The other command line gets are
[GetString](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetString),
[GetInteger](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetInteger), and
[GetBoolean](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetBoolean). They all work essentially the same as
[GetReal](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetReal).

### Interactive gets

#### GetPoint()

Some Get functions will prompt on the commandline and also allow for input
from the mouse. A typical interactive get is rs.GetPoint()` to ask the user
for a single point location. AS an example, let’s say you would like to prompt
for the center of a circle. The default prompt of GetPoint is “Pick point”,
but you can specify a different prompt, for example, “Set center point”
depending on what you wish to convey to the user.

    
    
    pt = rs.GetPoint("Set center point")
    

If the function succeeds, a Rhino point is returned, which can be treated as a
list of three numbers representing the world x, y and z coordinates of the
point.

    
    
    import rhinoscriptsyntax as rs
    pt = rs.GetPoint("Click to get information about a point location")
    if pt is not None:# note it is a good idea to check if there is a result you can use
        print "That point has an x coordinate of " + str(pt[0]) # when you build a string that includes elements that are not text, convert to a string with str()
    

#### GetPoints()

Use `rs.GetPoints()` to ask the user for multiple point locations. As in
rs.GetPoint(), all parameters are optional. Note that there is a separate
prompt for the first point, and a second one for subsequent points.

You need to set the parameters in order, separated by commas. If you do not
want to specify a parameter at all, and accept the default, you can leave it
out but you must then specify any following parameters explicitly using the
parameter name. For example, this will not work to set a custom first prompt:

    
    
    import rhinoscriptsyntax as rs
    
    pts = rs.GetPoints(  "Set the first point", "Set the next point")
    

Why? because the function has two parameters that come before the first
prompt, ‘draw_lines’ and ‘in_plane’. If you leave these out, you must specify
what parameters you are setting explicitly in order for it to be recognized:

    
    
    import rhinoscriptsyntax as rs
    pts = rs.GetPoints(  message1= "Set the first point", message2= "Set the next point")
    

You could also make sure to set the other parameters even if you don’t care
what they are i.e. defaults are OK:

    
    
    import rhinoscriptsyntax as rs
    pts = rs.GetPoints( None, None, "Set the first point", "Set the next point")
    

Many of the interactive get functions also allow a first point to be placed.
This way a rubber band line is drawn from the point to the cusor, emulating a
drawn line.

    
    
    import rhinoscriptsyntax as rs
    
    point1 = rs.GetPoint("Pick first point")
    
    #By adding the first point to this prompt, a line is interactively drawn.
    point2 = rs.GetPoint("Pick second point", point1)
    

The interactive gets have more options on how the input is filtered from the
mouse. For details on all the Get functions in RhinoScriptSyntax for Python go
to the [RhinoScriptSyntax User interface
methods](https://developer.rhino3d.com/api/rhinoscriptsyntax/#userinterface).
Additional interactive gets include:
[GetLine](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetLine),
[GetDistance](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetDistance),
[GetAngle](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetAngle),
[GetPolyline](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetPolyline),
[GetRectangle](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetRectangle),
[GetBox](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetBox),
[GetCursorPos](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetCursorPos).

### Geometry Gets

Geometry gets are used to pick geometry off the screen or related geometry off
an existing objects. Be aware the Gemetry gets can pass very different values
back from the functions. So, take special note on what is being returned by
these functions. In addition to object identifiers there may be additional
information on what was selected and how it was selected.

#### GetObject()

The basic get for an Object in the scene is the `GetObject()` function.
GetObject will return the _Guid_ of the object selected. Guids are identifiers
of existing geometry items that can be used in other RhinoScriptSyntax
functions to identify the objects.

    
    
    import rhinoscriptsyntax as rs
    objectId = rs.GetObject("Pick any object")
    if objectId: print objectID
    

Like other Geometry gets, there are optional arguments to filter out unwanted
selection by type. The example below will only allow curves and surfaces to be
selected.

    
    
    objectId = rs.GetObject("Pick a curve or surface", rs.filter.curve | rs.filter.surface)
    if objectId: print objectID
    

Additional geometry gets are:
[GetCurveObject](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetCurveObject),
[GetSurfaceObject](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetSurfaceObject),
[GetEdgeCurves](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetEdgeCurves),
[GetMeshFaces](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetMeshFaces),
[GetMeshVertices](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetMeshVertices),
[GetPointOnCurve](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetPointOnCurve),
[GetPointOnMesh](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetPointOnMesh),
[GetPointOnSurface](https://developer.rhino3d.com/api/rhinoscriptsyntax/#collapse-
GetPointOnSurface).

## Special Dialogs

The Dialog methods in RhinoScript syntax are used to prompt of with generic
custom information. Dialogs can be used to draw more attention to a required
interaction with the user. Dialogs generally interrupt the workflow - the
script cannot continue until the dialog is dealt with by the user.

#### MessageBox()

The simplest dialog box is the `rs.MessageBox()` function. The rs.MessageBox()
comes with many options to customize the buttons based on your needs:

    
    
    import rhinoscriptsyntax as rs
    
    rs.MessageBox("Hello Rhino!") # Simple message dialog
    rs.MessageBox("Hello Rhino!", 4 | 32) # A Yes, No dialog
    rs.MessageBox("Hello Rhino!", 2 | 48) # An Abort, Retry dialog
    

![https://developer.rhino3d.com/images/yes_no-
dialog.png](https://developer.rhino3d.com/images/yes_no-dialog.png)

Note that rs.MessageBox() returns a value - you can set a variable to record
the result from a message box so that you can tell which button the user has
clicked.

    
    
    import rhinoscriptsyntax as rs
    
    button = rs.MessageBox("Hello Rhino!", 2 | 48) # An Abort, Retry dialog
    

The value of ‘button’ in the code above will tell the script which button was
clicked and it can proceed appropriately. See the Rhino IronPython Help for
details on the available buttons and the return codes from rs.MessageBox()

#### ListBox()

Some of the more advanced dialogs can be populated with custom selections:

    
    
    import rhinoscriptsyntax as rs
    
    options = ('First Pick', 'Second Pick', 'Third Pick')
    
    if options:
        result = rs.ListBox(options, "Pick an option")
        if result: rs.MessageBox( result + " was selected" )
    

Will result in:

![https://developer.rhino3d.com/images/dialog-
listbox.png](https://developer.rhino3d.com/images/dialog-listbox.png)

#### Pre-defined dialog box methods:

**CheckListBox** \- Displays a list of strings in a checkable list. The user
can pick multiple items.  
![https://developer.rhino3d.com/images/dialog-
checklistbox.png](https://developer.rhino3d.com/images/dialog-
checklistbox.png)

**ComboListBox** \- Displays a list of strings in a combo list.

![https://developer.rhino3d.com/images/dialog-
combolistbox.png](https://developer.rhino3d.com/images/dialog-
combolistbox.png)

**EditBox** \- Displays a dialog box with a multi-line edit control.

![https://developer.rhino3d.com/images/dialog-
editbox.png](https://developer.rhino3d.com/images/dialog-editbox.png)

**PopupMenu** \- Displays a context-like popup menu.

![https://developer.rhino3d.com/images/dialog-
popupbox.png](https://developer.rhino3d.com/images/dialog-popupbox.png)

**PropertyListBox** \- Displays a list of items and values in a property list.

![https://developer.rhino3d.com/images/dialog-
propertybox.png](https://developer.rhino3d.com/images/dialog-propertybox.png)

**RealBox** \- Displays a dialog box prompting the user to enter a number.

![https://developer.rhino3d.com/images/dialog-
realbox.png](https://developer.rhino3d.com/images/dialog-realbox.png)

**StringBox** \- Displays a dialog box prompting the user to enter a string.

![https://developer.rhino3d.com/images/dialog-
stringbox.png](https://developer.rhino3d.com/images/dialog-stringbox.png)

**GetLayer** \- Displays dialog box prompting the user to select a layer

![https://developer.rhino3d.com/images/getlayer.png](https://developer.rhino3d.com/images/getlayer.png)

For details on all the dialog box functions in RhinoScriptSyntax for Python go
to the [RhinoScriptSyntax User interface
methods](https://developer.rhino3d.com/api/RhinoScriptSyntax/win/#userinterface)

## File System dialogs

Working with files and folders on the computer take a special class of
dialogs.

    
    
    import rhinoscriptsyntax as rs
    
    filename = rs.OpenFileName()
    if filename: rs.MessageBox(filename)
    

![RunPythonScript](https://developer.rhino3d.com/images/openfile_dialog.png)

#### Additional File System Dialogs

Method |  |  | Description  
---|---|---|---  
BrowseForFolder |  |  | Displays a Windows browse-for-folder dialog box.  
OpenFileName |  |  | Displays a Windows file open dialog box.  
OpenFileNames |  |  | Displays a Windows file open dialog box.  
SaveFileName |  |  | Displays a Windows file save dialog box.  
  
For a complete detailed sample see the [How to read and write a simple file
guide](https://developer.rhino3d.com/guides/rhinopython/python-reading-
writing/).

## [Eto Custom Dialog
Framework](https://developer.rhino3d.com/guides/rhinopython/eto-forms-python/)

Eto is an open source cross-platform dialog box framework available in Rhino
6. Eto can be used to create advanced dialog boxes from within C#, C++ and
Rhino.Python.

If the pre-defined dialogs above are not enough for your purposes, a Eto
dialog might be the right solution.

As an example, here is a custom collapsing dialog that uses many controls:

![https://developer.rhino3d.com/images/dialog-
collapse.png](https://developer.rhino3d.com/images/dialog-collapse.png)

Eto is very powerful, but that power comes with more sophisticated Python
syntax. Understanding how best to write, organize and use Eto dialogs will
take some work. To start learning about the Eto framework in Python, go to the
[Eto Forms in Python](https://developer.rhino3d.com/guides/rhinopython/eto-
forms-python/) guide.

## Related Topics

  * [Reading and Writing files with Python](https://developer.rhino3d.com/guides/rhinopython/python-reading-writing/)
  * [RhinoScriptSyntax User interface methods](https://developer.rhino3d.com/api/RhinoScriptSyntax/win/#userinterface)
  * [Eto Forms in Python](https://developer.rhino3d.com/guides/rhinopython/eto-forms-python/) guide

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
user-input/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
user-input/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

