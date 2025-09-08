---
url: https://developer.rhino3d.com/guides/rhinoscript/optional-arguments/
scraped_at: 2025-09-08T15:42:25.306299
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

[Optional
Arguments](https://developer.rhino3d.com/guides/rhinoscript/optional-
arguments/)

  * Overview
  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Optional Arguments

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
November 22, 2019)

## Overview

It is not uncommon to want to make an argument of a VBScript function or
subroutine optional. In VBScript, the `Optional` keyword, which allows some
arguments to be left out in Visual Basic, is not implemented. This means that
you must declare every argument that you want to use.

What you can do is pass null values to your functions. For example:

    
    
    Function SomeArgs(one, two, three, four)
      SomeArgs = one & two & three & four
    End Function
    
    Call SomeArgs(1, 2, 3, Null)
    

## Discussion

To work around this limitation, you can use an array-based approach to
simulate optional arguments. To see how to use the array-based approach for
creating subroutines with optional arguments, consider the following example:

    
    
    Sub MySubroutine(arrArgs)
    
      ' Declare local variables
      Dim v1, v2, v3, v4
    
      ' Initialize the local variables with default values
      v1 = 1 : v2 = 2 : v3 = 3 : v4 = 4
    
      Select Case UBound(arrArgs)
        Case 0
          v1 = arrArgs(0)  
        Case 1
          v1 = arrArgs(0)
          v2 = arrArgs(1)
        Case 2
          v1 = arrArgs(0)
          v2 = arrArgs(1)
          v3 = arrArgs(2)
        Case 3
          v1 = arrArgs(0)
          v2 = arrArgs(1)
          v3 = arrArgs(2)
          v4 = arrArgs(3)
        Case Else
          Exit Sub
      End Select
    
      Rhino.Print "v1  = " & CStr(v1)
      Rhino.Print "v2  = " & CStr(v2)
      Rhino.Print "v3  = " & CStr(v3)
      Rhino.Print "v4  = " & CStr(v4)
    
    End Sub
    

Notice in the subroutine declaration, only defined one argument has been
defined:

    
    
     Sub MySubroutine(arrArgs)
    

The argument will be an array of values we would like to pass into the
subroutine. The next few lines declare local variables and initializes them to
default values (simple numbers, in this case). Next, use the `UBound()`
function to determine the number of arguments passed. Then assign the array
elements to the local variables:

    
    
    Select Case UBound(arrArgs)
      Case 0
        v1 = arrArgs(0)
      Case 1
        v1 = arrArgs(0)
        v2 = arrArgs(1)
      Case 2
        v1 = arrArgs(0)
        v2 = arrArgs(1)
        v3 = arrArgs(2)
      Case 3
        v1 = arrArgs(0)
        v2 = arrArgs(1)
        v3 = arrArgs(2)
        v4 = arrArgs(3)
      Case Else
        Exit Sub
    End Select
    

Since the array is zero-based, the first case branch assigns the first element
to our v1 variable. As more arguments to the function are needed, one can
easily add more case branches.

To call this subroutine, create an array of the size based on the number of
arguments you want to pass into the function, and then populate this array
with the values you want to pass to the function:

    
    
    ' Create the array to pass to MySubroutine
    Dim arrArgs
    
    ' Call the subroutine with two arguments
    Redim arrArgs(1)
    arrArgs(0) = Value1
    arrArgs(1) = Value2
    
    Call MySubroutine(arrArgs)
    

Alternatively…

    
    
    ' Call MySubroutine with three arguments
    Call MySubroutine(Array(Value1, Value2, Value3))
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/optional-
arguments/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/optional-
arguments/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

