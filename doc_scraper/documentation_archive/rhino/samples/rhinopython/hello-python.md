---
url: https://developer.rhino3d.com/samples/rhinopython/hello-python/
scraped_at: 2025-09-08T15:46:50.949005
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

Hello Python

Demonstrates Basic syntax for writing python scripts.

Python

    
    
    # Basic syntax for writing python scripts
    print("Hello Python!")
    
    # <- any line that begins with the pound symbol is a comment
    
    # assign a variable
    x=123
    # print out the type of the variable
    print(type(x))
    # print out the value of the variable
    print(x)
    # combine statements with commas to print a single line
    print("x is a {} and has a value of {}".format(type(x), x))
    
    #loops
    # notice that there is a colon at the end of the first line and
    # and what is executed has some spaces in front of it
    for i in range(1,10):
        print("i={}".format(i))
    
    #conditionals
    x = 8
    for i in range(1,x+1):
        if i%2==0:
            print("{} is even".format(i))
        else:
            print("{} is odd".format(i))
    
    #functions
    def MyFunc(a):
        x = a+2
        print("{}+2={}".format(a,x))
    
    MyFunc(10)
    

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

