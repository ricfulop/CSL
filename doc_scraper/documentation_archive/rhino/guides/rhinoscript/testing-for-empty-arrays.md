---
url: https://developer.rhino3d.com/guides/rhinoscript/testing-for-empty-arrays/
scraped_at: 2025-09-08T15:43:05.349613
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

[Testing for Empty
Arrays](https://developer.rhino3d.com/guides/rhinoscript/testing-for-empty-
arrays/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Testing for Empty Arrays

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

It is often necessary to analyze an array to determine whether or not it is
empty; that is, if it has any space to store elements. Consider the following
test…

    
    
    Sub Main()
      Dim arr
      arr = Array()
      If IsArray(arr) Then
        Rhino.Print("This should not print")
      End If    
    End Sub
    

…which does not seem to work.

## Solution

When you execute this statement:

    
    
    arr = Array()
    

you are declaring an array that has an upper bounds of -1. Because this
variable is an array, it will pass the `IsArray()` test. What the above code
needs is an additional test condition to see if the upper bounds of the array
is greater than -1:

    
    
    Sub Main()
      Dim arr
      arr = Array()
      If IsArray(arr) And UBound(arr) >= 0 Then
        Rhino.Print("This should not print")
      End If    
    End Sub
    

Now the code works as expected. But, what if the code looked like this?

    
    
    Sub Main()
      Dim arr()
       If IsArray(arr) And UBound(arr) >= 0 Then
        Rhino.Print("This should not print")
      End If    
    End Sub
    

Notice that the above code gives you an “Script out of range: UBound” error.
This is because, although the variable is an array, it has not been
dimensioned. Thus the call to `UBound()` fails. So, we need a better test -
one that will test for both types of array declarations. Consider the
following function:

    
    
    Function IsArrayDimmed(arr)
      IsArrayDimmed = False
      If IsArray(arr) Then
        On Error Resume Next
        Dim ub : ub = UBound(arr)
        If (Err.Number = 0) And (ub >= 0) Then IsArrayDimmed = True
      End If  
    End Function
    

Notice how the function above provides error checking. If an error occurs when
calling `UBound()`, it is caught. Thus, the function knows when an array has
not been dimensioned. Also, if `UBound()` returns a value of -1, we know that
the array has no space to store elements. We can test this with the following
function:

    
    
    Sub Main()
      Dim arr0
      Dim arr1()
      Dim arr2(3)
      Dim arr3 : arr3 = Array()
      Dim arr4 : arr4 = Array(1,2,3)
      Rhino.Print "Arr0 dimmed = " &  IsArrayDimmed(arr0)
      Rhino.Print "Arr1 dimmed = " &  IsArrayDimmed(arr1)
      Rhino.Print "Arr2 dimmed = " &  IsArrayDimmed(arr2)
      Rhino.Print "Arr3 dimmed = " &  IsArrayDimmed(arr3)
      Rhino.Print "Arr4 dimmed = " &  IsArrayDimmed(arr4)
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/testing-
for-empty-arrays/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/testing-
for-empty-arrays/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

