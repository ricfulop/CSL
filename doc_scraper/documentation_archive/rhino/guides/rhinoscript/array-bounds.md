---
url: https://developer.rhino3d.com/guides/rhinoscript/array-bounds/
scraped_at: 2025-09-08T15:42:10.121268
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

[Array Dimensions & Upper
Bounds](https://developer.rhino3d.com/guides/rhinoscript/array-bounds/)

  * Overview
  * UBound
  * Jagged Arrays

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Array Dimensions & Upper Bounds

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

In a two-dimensional array, how do you determine the upper bounds of the array
for each dimension? Also, how do you handle jagged arrays? That is, an array
whose elements themselves are arrays? How do I find the upper bounds of two,
three, or n-dimensional array when the array is rectangular or jagged?

## UBound

To determine the upper bounds of an array, use VBScript’s `UBound` method. The
`UBound` method returns the largest available subscript for the indicated
dimension of an array. The syntax for `UBound` is:

    
    
    UBound(arrayname [,dimension])
    

where…

  * `arrayname` _(required)_ is the name of the array variable.
  * `dimension` _(optional)_ is whole number indicating which dimension’s upper bound is returned. Use 1 for the first dimension, 2 for the second, and so on. If dimension is omitted, 1 is assumed.

For example:

    
    
    Dim A(100,3,4)
    UBound(A)    ' 100
    UBound(A, 1) ' 100
    UBound(A, 2) ' 3
    UBound(A, 3) ' 4
    

## Jagged Arrays

What if you do not know an array’s dimensions, which might be the case with a
jagged array? How do you know what dimension values are valid to pass to
`UBound`?

VBScript does not have a function that returns the number of dimensions of an
array. But, by using the `UBound` method and some simple error checking, we
can write our own function that determines the number of dimension of an
array.

Consider the following function:

    
    
    'Description
    '  Returns the dimension of an array.
    'Parameters
    '  arr - Name of the array variable.
    'Returns
    '  The dimension of the array if successful.
    '  Null on error.
    '
    Function GetArrayDim(ByVal arr)
      GetArrayDim = Null
      Dim i
      If IsArray(arr) Then
        For i = 1 To 60
          On Error Resume Next
          UBound arr, i
          If Err.Number <> 0 Then
            GetArrayDim = i-1
            Exit Function
          End If
        Next
        GetArrayDim = i
      End If
    End Function
    

`GetArrayDim` simply calls `UBound` with a different dimension parameter until
an error is thrown. Note, since VBScript allows arrays of up to 60 dimensions,
we must check up to this value.

Now that we have a function that will return the dimensions of an array, we
can write a subroutine that dumps out the dimensions and upper bounds of
either a rectangular or jagged array.

For example:

    
    
    'Description
    '  Prints an array's dimensions and upper bounds to the command line.
    'Parameters
    '  arr - Name of the array variable.
    '
    Sub DumpArrayInfo(arr)
      Dim i, j, d, b
      If IsArray(arr) Then
        For i = 0 To UBound(arr)
          If IsArray(arr(i)) Then
            d = GetArrayDim(arr(i))
            If IsNull(d) Then
              Rhino.Print "Element(" & CStr(i) & ") is not dimensioned"
            Else
              Rhino.Print "Element(" & CStr(i) & ") dimension = " & CStr(d)
              For j = 1 To d
                b = GetArrayUBound(arr(i), j)
                If IsNull(b) Then
                  Rhino.Print "  Dimension(" & CStr(j) & ") has no bounds"
                Else
                  Rhino.Print "  Dimension(" & CStr(j) & ") bounds = " & CStr(b)
                End If
              Next
            End If
          Else
            Rhino.Print "Element(" & CStr(i) & ") is not an array"
          End If
        Next
      End If
    End Sub
    

For every element in an array, `DumpArrayInfo` calls `GetArrayDim` to
determine the dimension of the array element. If `GetArrayDim` returns a valid
result, then the subroutine determines the upper bounds in each dimension of
the array element and prints the results to the Rhino command line.

**NOTE** : `DumpArrayInfo` uses a `UBound` helper function named
`GetArrayUBound` that is a little safer than just using `UBound`…

    
    
    'Description
    '  Safely returns the largest available subscript for
    '  the indicated dimension of an array.
    'Parameters
    '  arr - Name of the array variable.
    '  i   - Number indicating which dimension's upper bound to return.
    'Returns
    '  The upper bounds for the indicated dimension if successful.
    '  Null on error.
    '
    Function GetArrayUBound(ByVal arr, ByVal i)
      GetArrayUBound = Null
      If IsArray(arr) Then
        On Error Resume Next
        b = UBound(arr, i)
        If Err.Number = 0 Then GetArrayUBound = b
      End If
    End Function
    

We can test our array dumping subroutine as follows:

    
    
    Sub TestDumpArrayInfo
    
      ' Declare arrays of various dimensions    
      Dim arr0(6)
      Dim arr1(5,4)
      Dim arr2(3,2,1)
      Dim arr3()
      Dim arr4
    
      ' Create a jagged array
      Dim arr(4)
      arr(0) = arr0
      arr(1) = arr1
      arr(2) = arr2
      arr(3) = arr3
      arr(4) = arr4  
    
      DumpArrayInfo arr
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/array-
bounds/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/array-
bounds/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

