---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-line/
scraped_at: 2025-09-08T15:37:30.048422
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

[Lines in Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-line/)

  * Lines
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Lines in Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Lines

3-D lines, or chords, are represented as zero-based, one-dimensional arrays
that contain two elements: the starting 3-D point and the ending 3-D point. A
3-D line is represented by a start pint and an ednpoint.

line1 = ((1.0, 2.0, 3.0), (4.0, 5.0, 6.0))

To add the line to the current Rhino file, and see it drawn on screen, you can
use the `AddLine` method in RhinoscriptSytnax:

    
    
    import rhinoscriptsyntax as rs
    
    startPoint = (1.0, 2.0, 3.0)
    endPoint = (4.0, 5.0, 6.0)
    
    lineID = rs.AddLine(startPoint,endPoint)
    
    print(lineID)
    

When adding geometry to Rhino, rhinoscriptsyntax will return an ‘Object ID’
for the added object. The Rhino file has the object added as geometry in the
file. Just like an object added using a Rhino command, it has an ID that is a
unique reference to this object. This makes it possible and easy to get access
to the specific object later in the script. Saving this ID in a variable or a
list is what allows it to be used later to select and manipulate the object.

RhinoScript contains a number of methods to manipulate lines. See [Lines and
Planes](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-line-plane-methods/) for details.

## Related Topics

  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python Points](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-points/)
  * [Python Vectors](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)
  * [Python Lines](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-lines)
  * [Python Planes](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-planes)
  * [Python Objects](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-objects/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-line/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-line/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

