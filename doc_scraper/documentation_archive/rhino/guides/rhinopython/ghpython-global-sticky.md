---
url: https://developer.rhino3d.com/guides/rhinopython/ghpython-global-sticky/
scraped_at: 2025-09-08T15:37:11.850719
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

[Creating Global Sticky
Variables](https://developer.rhino3d.com/guides/rhinopython/ghpython-global-
sticky/)

  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Creating Global Sticky Variables

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

Sometimes there is a need to share information between Grasshopper and
Rhino.Python. This can be done through a global [sticky
variable](http://developer.rhino3d.com/samples/rhinopython/sticky-values/)
creating a definition wide global sticky variable. Both Rhino.Python and
gh.python use the same Python instance, so the Python sticky is shared between
the two.

With a global sticky variable all the components in a definition can access
the information.

As an example, here is a definition that creates a simple sticky variable and
passes it to another component that is not connected:

![https://developer.rhino3d.com/images/sticky-
ghpython.png](https://developer.rhino3d.com/images/sticky-ghpython.png)

    
    
    import scriptcontext as rs
    
    rs.sticky["someName"] = x #"x" is the input for the component
    

The scriptcontext.sticky creates a global variable names “someName”. This can
be referenced in another component using this code:

    
    
    import scriptcontext as rs
    
    a = rs.sticky["someName"] #output the value of the sticky
    

Within Rhino.Python, the same value can be accessed the same way through
[Rhino.Python sticky](http://developer.rhino3d.com/samples/rhinopython/sticky-
values/).

## Related Topics

  * [Your first script with Python in Grasshopper](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Editing Python in Grasshopper](https://developer.rhino3d.com/guides/rhinopython/python-running-scripts/)
  * [Python Guide for Rhino](https://developer.rhino3d.com/guides/rhinopython/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/ghpython-
global-sticky/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/ghpython-
global-sticky/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

