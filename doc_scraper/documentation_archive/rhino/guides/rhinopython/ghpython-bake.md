---
url: https://developer.rhino3d.com/guides/rhinopython/ghpython-bake/
scraped_at: 2025-09-08T15:37:13.885184
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

[Custom GhPython Baking
Component](https://developer.rhino3d.com/guides/rhinopython/ghpython-bake/)

  * Basic GHPython Component
  * The Python code
  * Advanced Options for Baking
    * Baking colors materials and other properties
    * Adding Key-Value text to the object
    * Changing Object Attributes:
  * Next Steps
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Custom GhPython Baking Component

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Monday, July 6, 2020)

Many times it is useful to create a custom component in Grasshopper to bake
both geometry and other properties into Rhino in the same component. This
guide will cover the varying calls to create these custom components using
GhPython.

There are a few different ways to approach baking. This guide set’s up the
simplest approach. At the end of this guide is a section on some of the
variations possible to fit other bake situations.

For more details any of the concepts in this guide, more details can be found
in:

  1. [GHPython editor basics guide](https://developer.rhino3d.com/guides/rhinopython/ghpython-component/)
  2. [RhinoScriptSyntax and Python Guide](http://developer.rhino3d.com/guides/rhinopython/)
  3. RhinoCommon API please refer to the [McNeel RhinoCommon Developer site](http://developer.rhino3d.com/guides/rhinocommon).

## Basic GHPython Component

Start with a standard [GHPython
Component](https://developer.rhino3d.com/guides/rhinopython/ghpython-
component/).

![https://developer.rhino3d.com/images/ghpython-
bake.png](https://developer.rhino3d.com/images/ghpython-bake.png)

[Download this sample Gh file
here….](https://github.com/mcneel/rhino.inside/raw/master/Autodesk/Revit/doc/samples/Python%20Bake.gh)

In this case we use 3 inputs. Change the names of input and output and the
Type hint by right clicking on each input:

  * `G`: Geometry to bake (Guid)
  * `L`: Layer name to bake to (str).
  * `B`: Activate toggle to bake (bool)

To test this component. the Box Param is the easiest geometry type to use for
testing. Add a Layer name using a panel as input. Use a Button or a Switch to
toggle `True` and `False`.

## The Python code

Here is the code for this component. In this case, the geometry is baked to
Rhino on the default layer, then through Python we switch the layer to the one
input.

    
    
    """Provides a scripting component.
        Inputs:
            G: Geometry to bake
            L: Layer name for bake
            B: Bake Activate
        Output:
            a: The a output variable"""
    
    __author__ = "ScottD"
    __version__ = "2019.08.10"
    
    import rhinoscriptsyntax as rs
    import scriptcontext
    import Rhino
    
    
    if B:
    
        print(type(G)) #debug message to Python output
    
        #we obtain the reference in the Rhino doc
        doc_object = scriptcontext.doc.Objects.Find(G)
        print(type(doc_object))
    
        attributes = doc_object.Attributes
        print('the type of attributes is: ' + str(type(attributes)))     #debug message to Python output
    
        geometry = doc_object.Geometry
        print('the type of geometry is: ' + str(type(doc_object)))     #debug message to Python output
    
        #we change the scriptcontext
        scriptcontext.doc = Rhino.RhinoDoc.ActiveDoc
    
        #we add both the geometry and the attributes to the Rhino doc
        rhino_brep = scriptcontext.doc.Objects.Add(geometry, attributes)
        print('the Rhino doc ID is: ' + str(rhino_brep))     #debug message to Python output
    
        #we can for example change the layer in Rhino...
        if not rs.IsLayer(L):
            rs.AddLayer(L)
        rs.ObjectLayer(rhino_brep, L)
    
        #we put back the original Grasshopper document as default
        scriptcontext.doc = ghdoc
        a = G
    

There are various key lines of code to be understand:

Line | Description  
---|---  
17 | Standard `if` statement to activate the bake once the `B` is set to `TRUE`.  
22 | The doc.Objects.Find method will attempt to take the Object ID and find the actual Rhino Geometry Object.  
25 | Split off the object's Attributes. The attributes of an object include such properties as color, layer, linetype, render material, and group membership, amongst others. The Advanced section below covers object attributes some more.  
31 | Split off the object's Geometry. Used when baking the object into Rhino.  
32 | Grasshopper has its own document. Rhino has its own document also. Make sure the script is talking to the Rhino Document for the following functions.  
35 | Add the object to the Rhino document. This is the actual Bake. Take note that if it has been baked previous, there will now be two objects.  
39-40 | Check to see if the layer name exists in Rhino. If it does not, then create a new layer with that name.  
41 | Change the Rhino object's layer to the requested layer name.  
44 | Switch the script context back to the Grasshopper document.  
45 | Pass the original component input object to the component output if it is needed in any downstream processes.  
  
Hopefully this code will serve as a template in taking objects from
Grasshopper into Rhino. There are a multitude of variations on this theme. The
following section looks at various ways to use more advanced options to better
fit the situation.

## Advanced Options for Baking

Beyond simply changing an objects layer after adding the new object to Rhino.
There are many other properties that can be changed. Here is a discussion of
some of the possibilities.

### Baking colors materials and other properties

In the sample above using the layername to specify where the object ultimately
lands is quite simple. Here are some other properties that may want to be
changed:

Object name | [rs.ObjectName(object-id, name)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-ObjectName)  
---|---  
Display color | [rs.ObjectColorSource(object_ids, source=None)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-ObjectColorSource)  
[rs.ObjectColor(object_ids,
color=None)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-
ObjectColor)  
Print color | [rs.ObjectPrintColorSource(object_ids, source=None)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-ObjectPrintColorSource)  
[rs.ObjectPrintColor(object_ids,
color=None)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-
ObjectPrintColor)  
Unlock object | [rs.UnlockObject(object_id)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-UnlockObject)  
Lock object | [rs.LockObject(object_id)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-LockObject)  
Hide object | [rs.HideObject(object_id)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-HideObject)  
Set Material | [rs.ObjectMaterialSource(object_ids, source=None)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-ObjectMaterialSource)  
[rs.ObjectMaterialIndex(object_id,
material_index=None)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-
ObjectMaterialIndex)  
  
### Adding Key-Value text to the object

Additional text data can be stored as a Key:Value pair on the Rhino object.
THe Keys and Values can be retrieved later in Rhino.

[rs.SetUserText(object_id, key, value=None,
attach_to_geometry=False)](https://developer.rhino3d.com/api/RhinoScriptSyntax/#object-
ObjectMaterialSource)

For more information on [RhinoScript User Text help
topic](https://developer.rhino3d.com/api/rhinoscript/user_data_methods/user_data_methods.htm).

### Changing Object Attributes:

Through the RhinoCommon functions, the attributes of an object can be set. See
the [Object Attribute Class for more
details….](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_DocObjects_ObjectAttributes.htm)

## Next Steps

That lays out the basics of the GhPython component. Next is a look into the
component Python editor for Grasshopper.

## Related Topics

  * [Your first script with Python in Grasshopper](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Editing Python in Grasshopper](https://developer.rhino3d.com/guides/rhinopython/python-running-scripts/)
  * [Python Guide for Rhino](https://developer.rhino3d.com/guides/rhinopython/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/ghpython-
bake/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/ghpython-
bake/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

