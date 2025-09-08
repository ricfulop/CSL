---
url: https://developer.rhino3d.com/guides/rhinopython/python-remote-local-module/
scraped_at: 2025-09-08T15:37:52.163008
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

[Creating a script and
module](https://developer.rhino3d.com/guides/rhinopython/python-remote-local-
module/)

  * Overview
  * A complete script example
  * How it works

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Creating a script and module

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

## Overview

A Python script normally can be full of functions that can be imported as a
library of functions in other scripts, or a python script can be a command
that runs in Rhino.

There is a way to have Python definitions be both a library of functions and a
direct command.

The key is to add these statements to the end of the file:

    
    
    if __name__ == '__main__':
        CreateCircle()  # Put the a call to the main function in the file.    
    

## A complete script example

Here is a complete Python sample that shows how the `if __name__ ==
'__main__':` statement can be added to a Python script:

    
    
    # Create a circle from a center point and a circumference.
    import rhinoscriptsyntax as rs
    import math
    
    def CreateCircle(circumference=None):
        center = rs.GetPoint("Center point of circle")
        if center:
            plane = rs.MovePlane(rs.ViewCPlane(), center)
            length = circumference
            if length is None: length = rs.GetReal("Circle circumference")
            if length and length>0:
                radius = length/(2*math.pi)
                objectId = rs.AddCircle(plane, radius)
                rs.SelectObject(objectId)
                return length
        return None
    
    # Check to see if this file is being executed as the "Main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if __name__ == '__main__':
        CreateCircle()
    

The CreateCricle file above will run as a script to create a circle. But it
can be used in the _UseModule.py_ script as an imported module, as follows:

    
    
    # This script uses a function defined in the CircleFromLength.py
    # script file
    import CircleFromLength
    
    # call the function a few times just for fun using the
    # optional parameter
    length = CircleFromLength.CreateCircle()
    if length is not None and length>0.0:
        for i in range(4):
            CircleFromLength.CreateCircle(length)
    

## How it works

When the Python interpreter reads a source file, it executes all of the code
found in it.

Before executing the code, it will define a few special variables. If Python
is running the file as the main program then Python will create a `__name__`
variable with the value of _**main**_. If python is importing the file as an
import into an already running _**main**_ the `__name__` variable will be set
to the module’s name in the modules scope.

One of the reasons for doing this is that sometimes you write a module (a .py
file) where it can be executed directly. Alternatively, it can also be
imported and used in another module. By doing the main check, you can have
that code only execute when you want to run the module as a program and not
have it execute when someone just wants to import your module and call your
functions themselves.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
remote-local-module/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
remote-local-module/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

