---
url: https://developer.rhino3d.com/guides/compute/custom-endpoints/
scraped_at: 2025-09-08T15:43:18.497489
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

[Extending Compute with Custom
Endpoints](https://developer.rhino3d.com/guides/compute/custom-endpoints/)

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

Extending Compute with Custom Endpoints

__

Windows only

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) and [Will
Pearson](https://discourse.mcneel.com/u/will/) (Last updated: Wednesday,
February 3, 2021)

By default Compute exposes a long list of endpoints, designed to expose
functionality in RhinoCommon as well as enabling Grasshopper definitions and
Python scripts to be solved. It’s also possible to extend Compute with your
own custom endpoints by registering functions in a Rhino plug-in. Compute
handles the serialization.

First define a static class in your plug-in and add the new function as a
static method (you can add more than one!).

    
    
    static class MyCustomComputeFunctions
    {
      public static double Add(double, x, double y, double z) { return x+y+z; }
    
      public static double AdjustedArea(Curve curve, double adjuster)
      {
        var amp = Rhino.Geometry.AreaMassProperties.Compute(curve);
        return amp.Area * adjuster;
      }
    }
    

Then, in the `OnLoad` method of the plug-in’s `PlugIn` class, register the
function. This code is called once when the plug-in is loaded by Rhino.

    
    
    protected override LoadReturnCode OnLoad(ref string errorMessage)
    {
      Rhino.Runtime.HostUtils.RegisterComputeEndPoint("Rhino.CustomEndPoint", typeof(MyCustomComputeFunctions));
    
      return base.OnLoad(ref errorMessage);
    }
    

You will need to install your plug-in in Rhino, both locally for testing and
on any servers where Compute runs.

Once this is complete, you should be able to open the `/sdk` endpoint in a
browser and see the new functions listed at the bottom of the page.

__Note __

Check out the [ComputePlugIn sample](https://github.com/mcneel/rhino-
developer-samples/tree/7/compute/cs/ComputePlugIn) in the Rhino Developer
Samples repository.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/custom-
endpoints/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/custom-
endpoints/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

