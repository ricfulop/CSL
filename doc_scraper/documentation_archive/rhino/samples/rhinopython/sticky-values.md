---
url: https://developer.rhino3d.com/samples/rhinopython/sticky-values/
scraped_at: 2025-09-08T15:47:04.017834
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

Sticky Values

This module contains a standard python dictionary called sticky which sticks
around.

Python

    
    
    import rhinoscriptsyntax as rs
    import scriptcontext
    
    
    stickyval = 0
    # restore stickyval if it has been saved
    if scriptcontext.sticky.has_key("my_key"):
        stickyval = scriptcontext.sticky["my_key"]
    nonstickyval = 12
    
    print "sticky =", stickyval
    print "nonsticky =", nonstickyval
    
    val = rs.GetInteger("give me an integer")
    if val:
        stickyval = val
        nonstickyval = val
    
    # save the value for use in the future
    scriptcontext.sticky["my_key"] = stickyval
    

The `scriptcontext` module contains a standard python dictionary called sticky
which “sticks” around during the running of Rhino. This dictionary can be used
to save settings between execution of your scripts and then get at those saved
settings the next time you run your script or from a completely different
script.

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

