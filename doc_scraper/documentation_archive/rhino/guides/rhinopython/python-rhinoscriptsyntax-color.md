---
url: https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-color/
scraped_at: 2025-09-08T15:37:28.945585
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

[Colors in Python](https://developer.rhino3d.com/guides/rhinopython/python-
rhinoscriptsyntax-color/)

  * Colors
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Colors in Python

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

## Colors

Colors in Rhino are represented as zero-based, one-dimensional arrays that
contain four values. The first 3 values are the Red, Green and Blue channels.
Each channel may contain a value from 0 to 255. The fourth value is the Alpha
Channel. This control transparency of the color. 0 is completely transparent
and the default value of 255 is completely opaque.

    
    
    color contains (Red, Green, Blue, Alpha)
    

Use the `CreateColor()` function to create a new color structure:

    
    
    import rhinoscriptsyntax as rs
    
    color1 = rs.CreateColor(128, 128, 128) # Creates a medium grey color.
    

The `CreateColor()` function assumes the alpha value is 255 by default.

    
    
    import rhinoscriptsyntax as rs
    
    col = rs.CreateColor(43,45,56)
    
    print (col.R)
    print (col.G)
    print (col.B)
    

Unlike many other Rhino types, colors are immutable. This means you cannot set
one channel by itself, but must always create a new color when trying to make
a color. Setting one channel will not work, for instance `color1.B = 56` will
throw an error.

Here is a table of commonly used colors:

Color |  | Red |  | Green |  | Blue  
---|---|---|---|---|---|---  
Black |  | 0 |  | 0 |  | 0  
White |  | 255 |  | 255 |  | 255  
Medium Gray |  | 128 |  | 128 |  | 128  
Aqua |  | 0 |  | 128 |  | 128  
Navy Blue |  | 0 |  | 0 |  | 128  
Green |  | 0 |  | 255 |  | 0  
Orange |  | 255 |  | 165 |  | 0  
Yellow |  | 255 |  | 255 |  | 0  
  
For more colors see an [Online RGB Color
table](http://www.rapidtables.com/web/color/RGB_Color.htm#color-table).

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
rhinoscriptsyntax-color/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
rhinoscriptsyntax-color/index.md) [
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

