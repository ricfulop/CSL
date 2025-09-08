---
url: https://developer.rhino3d.com/guides/rhinopython/python-canceling-scripts/
scraped_at: 2025-09-08T15:37:09.975478
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

[Canceling a Python script in
Rhino](https://developer.rhino3d.com/guides/rhinopython/python-canceling-
scripts/)

  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Canceling a Python script in Rhino

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

In Rhino 6, when a script is running and it is not waiting for user input, it
can be cancelled by pressing the ESC. In Rhino.Python this is done by adding a
`scriptcontext.escape_test` test.

The following script is not be cancelled by pressing the ESC key.

    
    
    def TightLoopEscapeTest():
      for i in range(10000):
    
    TightLoopEscapeTest()
    

By `scriptcontext.escape_test` function the loop can now be canceled:

    
    
    import scriptcontext
    
    def TimeConsumingTask():    
        for i in range(10000):
            # Was escape key pressed?
            if (scriptcontext.escape_test(False)):
                print "TimeConsumingTask cancelled."
                break
            print i
    
    TimeConsumingTask()
    

It might be necessary to press the `ESC` key a couple times to catch the
`scriptcontext.escape_test` test in the correct state.

## Related Topics

  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Your First Python Script in Rhino (Windows)](https://developer.rhino3d.com/guides/rhinopython/your-first-python-script-in-rhino-windows/)
  * [Running Scripts](https://developer.rhino3d.com/guides/rhinopython/python-running-scripts/)
  * [Canceling Scripts](https://developer.rhino3d.com/guides/rhinopython/python-canceling-scripts/)
  * [Editing Scripts](https://developer.rhino3d.com/guides/rhinopython/python-editing-scripts)
  * [Scripting Options](https://developer.rhino3d.com/guides/rhinopython/python-scripting-options)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
canceling-scripts/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
canceling-scripts/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

