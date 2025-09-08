---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-passing-parameters/
scraped_at: 2025-09-08T15:42:02.213952
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

[VBScript Passing
Parameters](https://developer.rhino3d.com/guides/rhinoscript/vbscript-passing-
parameters/)

  * Overview
  * Passing By Value
  * Passing By Reference
  * ByRef & Temporary Variables
  * Summary

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Passing Parameters

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

In VBScript, there are two ways values can be passed: `ByVal` and `ByRef`.
Using `ByVal`, we can pass arguments as values whereas with the use of
`ByRef`, we can pass arguments are references. This is the obvious bit, but,
how do these two differ in practice?

## Passing By Value

Consider the following code snippet:

    
    
    Function GetValue(ByVal var)
      var = var + 1
    End Function
    
    Dim x: x = 5
    
    'Pass the variable x to the GetValue function ByVal
    Call GetValue(x)
    
    Call Rhino.Print("x = " & CStr(x))
    

When you run the block of code above, you will get the following output:

    
    
    x = 5
    

In other words, when we passed the variable `x` (`ByVal`) to the function
`GetValue`, we were simply passing a copy of the variable `x`. When `GetValue`
executes, var stores a copy of the variable `x` and increments itself by 1.
Therefore, because what we are passing to `GetValue` is a copy of `x`, it
cannot be modified.

## Passing By Reference

Now, let’s look at another way of passing variables: By Reference.

Consider the following code snippet:

    
    
    Function GetReference(ByRef var)
      var = var + 1
    End Function
    
    Dim x: x = 5
    
    'Pass the variable x to the GetReference function ByRef
    Call GetReference(x)
    
    Call Rhino.Print("x = " & CStr(x))
    

When you run the block of code above, you will get the following output:

    
    
    x = 6
    

Variable `x` was increment by 1. But why was `x` incremented? Only var must
have incremented by 1, and not `x`? Well, that is the core concept behind
passing variables by reference.

When the function `GetReference` executes, var becomes a reference of `x`, and
therefore, any changes made to var would impact `x`. So if `var` increments
itself by 1, so would `x`. If `var` becomes 0 (zero), so would `x`.

Let’s look at another example:

    
    
    Function GetReference(ByRef arrArray)
      ReDim Preserve arrArray(UBound(arrArray)+1)
      arrArray(UBound(arrArray)) = 2
    End Function
    
    Dim newArray: newArray = Array(0, 1)
    Call GetReference(newArray)
    

Will the size of `newArray` increase? Look at:

    
    
    ' new size: 2
    Call Rhino.Print(UBound(newArray))
    
    ' new elements: 0, 1, 2
    For x = LBound(newArray) To UBound(newArray)
      Call Rhino.Print(newArray(x))
    Next
    

Since `newArray` was passed as a reference to the `GetReference` function, the
change made to `arrArray` was reflected upon `newArray` as well. Thus, sizes
of both arrays incremented by 1.

Is there a way to pass variables `ByRef` and still avoid this? Yes, there is.
The answer lies in passing temporary variables…

## ByRef & Temporary Variables

The advantage of using this approach is that you can pass temporary variables
to n number of functions accepting arguments as reference, without having the
base (original) variables modified. This is a good (and recommended) approach,
since your original variables stay intact and you do not lose track of them
when working with extensive function libraries. Please see a simple
demonstration of this approach below:

    
    
    Function GetReference(ByRef var)
      var = var + 1
    End Function
    
    Dim x: x = 5
    Dim y: y = x
    
    Call GetReference(y)
    
    ' Returns 5 (x remains unchanged)
    Call Rhino.Print(x)
    ' Returns 6   
    Call Rhino.Print(y)
    

Above, you will notice that as `y` became a temporary variable and was passed
to `GetReference`, only it was modified. The variable `x` was unchanged. Thus,
it’s recommended to use temporary variables when passing variables as
reference.

## Summary

Here is a summary:

  * (ByVal) Arguments do not change when passed by value.
  * (ByRef) If the function parameter is modified, it will have the same impact on the parameter that was passed by reference.
  * (ByRef) Because the passed parameters can be changed, we can pass multiple values from functions.
  * (ByRef) In a large function library, it can be hard to tell where the value was changed and what function the variable was supposed to perform.

* * *

# Related Topics

  * [ByRef vs ByVal](https://developer.rhino3d.com/guides/rhinoscript/byref-vs-byval/)
  * [Sub Statement (VBScript) on MSDN](http://msdn.microsoft.com/en-us/library/tt223ahx%28v=vs.85%29.aspx)
  * [Function Statement (VBScript) on MSDN](http://msdn.microsoft.com/en-us/library/x7hbf8fa%28v=vs.85%29.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
passing-parameters/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
passing-parameters/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

