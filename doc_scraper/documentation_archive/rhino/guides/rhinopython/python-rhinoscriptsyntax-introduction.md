---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-introduction/
scraped_at: 2025-09-08T15:37:26.069837
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

[RhinoScriptSyntax in
Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-introduction/)

  * Overview
  * Importing RhinoScriptSyntax
  * Geometry

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

RhinoScriptSyntax in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Thursday, October 24, 2019)

## Overview

The RhinoScriptSyntax module contains hundreds of easy-to-use functions that
perform a variety of operations on Rhino. The library allows Python to be
aware of Rhino’s:

  * Geometry
  * Commands
  * Document objects
  * Application methods

To make these methods easy-to-use, all RhinoScriptSyntax methods return simple
Python variables or Python List-based data structures. Thus, once you are
familiar with Python, you will be able to use any and all functions in the
RhinoScriptSyntax methods library. For the whole namespace, see the
[Rhinoscriptsyntax API
reference](https://developer.rhino3d.com/api/RhinoScriptSyntax/).

## Importing RhinoScriptSyntax

Before using RhinoScriptSyntax a line must be added to the top of each Python
file to allow access to RhinoScriptSyntax:

    
    
    import rhinoscriptsyntax as rs
    

The `import` above not only imports the library, but also renames the module
to `rs.`. This is done to just make it easier to type when accessing the
methods in RhinoScriptSyntax. Access to the methods can now be made by
starting methods with ‘rs.’. For example, accessing the `AddCircle()` method
in the RhinoScriptSyntax module can be used to create a circle:

    
    
    import rhinoscriptsyntax as rs
    
    centerpoint = [1, 2, 4]
    rs.AddCircle( centerpoint, 5.0 )
    

## Geometry

Rhino is a 3D modeler, therefore creating and modifying geometry is key to
developing in Rhino. Here are the primitive geometry types of Rhino:

  * [Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/)
  * [List of Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-list-points/)
  * [Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-line/)
  * [Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-plane/)
  * [Rhino Geometry Objects](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/)

Creating, accessing and manipulating geometry is one of the first places
RhinoScriptSyntax is used. Simple geometry such as points, lines, and planes
can be described with lists in Python. More complicated geometry objects such
as NURBS curves, Surfaces and Poly-surfaces can be created by Rhino and
referenced by an object ID in RhinoScriptSyntax.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-introduction/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-introduction/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

