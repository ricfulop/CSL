---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-variable-hoisting/
scraped_at: 2025-09-08T15:41:56.181820
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

[VBScript Variable
Hoisting](https://developer.rhino3d.com/guides/rhinoscript/vbscript-variable-
hoisting/)

  * Problem
  * Solution
  * Details

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Variable Hoisting

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Consider the following VBScript code, which does not work:

    
    
    Option Explicit
    s = "Hello"
    

Now, consider the following working code:

    
    
    Option Explicit
    s = "Hello"
    Dim s
    

Why can a variable be used before declaring it in VBScript?

## Solution

Consider this code:

    
    
    Dim s
    s = Foo(123)
    
    Function Foo(x)
      Foo = x + 345
    End Function
    

Here the function is being used before it is declared. Similarly, variables
can be used before they are declared. The behaviour is by design. Variable
declarations and functions are logically “hoisted” to the top of their scope
in VBScript.

Also, declaring a variable twice in the same script block is illegal, but
redefinition in another block is legal. Procedures may be redeclared at will
except if the procedure is in a class, in which case redeclaration is illegal.

The following is legal in VBScript:

    
    
    s = Foo(123)
    If Blah Then
      Function Foo(x)
        Foo = x + 345
      End Function
    End If
    

## Details

This is not recommended, but it _is_ legal:

    
    
    Dim i
    For i = 1 To 2
      Rhino.Print c
    Next
    Const c = 10
    

And this works too:

    
    
    For i = 1 To 2
      Rhino.Print c
      Dim i
    Next
    Const c = 10
    

But, this fails with a “name redefined” error:

    
    
    For i = 1 To 2
      Rhino.Print c
      Const c = 10
      Dim i
    Next
    

In conclusion, in VBScript:

  * Variable declarations are logically hoisted to the top of the scope.
  * Constants are evaluated at code compilation time; the constants’ values are injected into the code.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
variable-hoisting/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
variable-hoisting/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

