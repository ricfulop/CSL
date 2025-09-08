---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/
scraped_at: 2025-09-08T15:37:32.961211
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

[Rhino objects in
Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-objects/)

  * Objects
  * Geometry and Attributes
  * Example
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Rhino objects in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Objects

Rhino can create and manipulate a number of objects, including points, point
clouds, curves, surfaces, B-reps, meshes, lights, annotations, and references.
Each object in the Rhino document is identified by a globally unique
identifier, or GUID, that is generated and assigned to objects when they are
created. Object identifiers are saved in the 3dm file, so an object’s
identifier will be the same between editing sessions.

To view an object’s unique identifier, use Rhino’s `Properties` command.

For convenience, RhinoScriptSyntax returns object identifiers in the form of a
string. For example, an object’s identifier will look something like the
following:

`F6E01514-3264-4598-8A07-A58BFE739C38`

The majority of RhinoScriptSyntax’s object manipulation methods require one or
more object identifiers to be acquired before the method can be executed.

## Geometry and Attributes

Rhino objects consist of two components: the object’s geometry and the
object’s attributes.

The types of geometry support by Rhino include points, point clouds, curves,
surfaces, polysurfaces, extrusions, meshes, annotations and dimensions.

The attributes of an object include such properties as color, layer, linetype,
render material, and group membership, amongst others.

## Example

The following example uses Object IDs to create reference geometry:

    
    
    import rhinoscriptsyntax as rs
    
    startPoint = (1.0, 2.0, 0.0)
    endPoint = (4.0, 5.0, 0.0)
    
    line1ID = rs.AddLine(startPoint,endPoint) # Adds a line to the Rhino Document and returns an ObjectID
    
    startPoint2 = (1.0, 4.0, 0.0)
    endPoint2 = (4.0, 2.0, 0.0)
    
    line2ID = rs.AddLine(startPoint2,endPoint2) # Returns another ObjectID
    
    int1 = rs.LineLineIntersection(line1ID,line2ID) # passing the ObjectIDs to the function.
    
    print(int1)
    

## Related Topics

  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/)
  * [Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-lines)
  * [Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-planes)
  * [Rhino NURBs Geometry](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-nurbs/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-objects/index.md) [
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

