---
url: https://developer.rhino3d.com/guides/rhinopython/using-rhinocommon-from-python/
scraped_at: 2025-09-08T15:36:44.855784
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

[Using RhinoCommon from
Python](https://developer.rhino3d.com/guides/rhinopython/using-rhinocommon-
from-python/)

  * Overview

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Using RhinoCommon from Python

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Friday, September 3, 2021)

## Overview

Along with the RhinoScript style functions you will be able to use all of the
classes in the .NET Framework, including the classes available in RhinoCommon.
As a matter of fact, if you look at the source for the rhinoscriptsyntax
functions, they are just python scripts that use RhinoCommon. This allows you
to do some pretty amazing things inside of a python script. Many of the
features that once could only be done in a .NET plugin can now be done in a
python script

For example, you can implement some custom drawing while a user is picking a
point with the following script. This script draws a Red and Blue line
connected to the point under the mouse cursor while the user is picking a
point.

    
    
    import Rhino
    import System.Drawing
    
    def GetPointDynamicDrawFunc( sender, args ):
      pt1 = Rhino.Geometry.Point3d(0,0,0)
      pt2 = Rhino.Geometry.Point3d(10,10,0)
      args.Display.DrawLine(pt1, args.CurrentPoint, System.Drawing.Color.Red, 2)
      args.Display.DrawLine(pt2, args.CurrentPoint, System.Drawing.Color.Blue, 2)
    
    # Create an instance of a GetPoint class and add a delegate for the DynamicDraw event
    gp = Rhino.Input.Custom.GetPoint()
    gp.DynamicDraw += GetPointDynamicDrawFunc
    gp.Get()
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/using-
rhinocommon-from-python/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/using-
rhinocommon-from-python/index.md) [
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

