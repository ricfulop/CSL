---
url: https://developer.rhino3d.com/guides/rhinoscript/calculating-permutations/
scraped_at: 2025-09-08T15:42:12.226083
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

[Calculating
Permutations](https://developer.rhino3d.com/guides/rhinoscript/calculating-
permutations/)

  * Overview
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Calculating Permutations

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The permutation of a set is the number of ways that the items in the set can
be uniquely ordered. For example, the permutations of the set $${1, 2, 3}$$
are: $${1, 2, 3}$$, $${1, 3, 2}$$, $${2, 1, 3}$$, $${2, 3, 1}$$, $${3, 1,
2}$$, and $${3, 2, 1}$$.

For $$N$$ objects, the number of permutations is $$N$$ (N factorial, or $$1 *
2 * 3 * N$$).

## Example

There are a number of methods for calculating permutation sets. The
implementation below uses an ordered, or lexicographic, permutation algorithm.
This algorithm is based on a a permutation algorithm from the book _Practical
Algorithms in C++_ by Bryan Flamig.

    
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' TestPermute - the Main subroutine
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub TestPermute
      Dim arr, n
      'arr = Array("One", "Two", "Three", "Four")
      'arr = Array(1, "Two", 3, "Four")
      arr = Array(1, 2, 3, 4)
      n = UBound(arr) + 1
      Rhino.ClearCommandHistory
      Call Rhino.Print(PermuteCount(n))
      Call Permute(arr, 0, n)
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Permute
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub Permute(ByRef arr, ByVal start, ByVal n)
      Dim i, j
      Call PermutePrint(arr)
      If (start < n) Then
        For i = n-2 To start Step -1
          For j = i+1 To n-1
            Call PermuteSwap(arr, i, j)
            Call Permute(arr, i+1, n)
          Next
          Call PermuteRotate(arr, i, n)
        Next
      End If
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' PermutePrint
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub PermutePrint(ByRef arr)
      Dim s, v
      s = ""
      For Each v In arr
        s = s & CStr(v) & vbTab
      Next
      Rhino.Print s
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' PermuteSwap
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub PermuteSwap(ByRef arr, ByVal i, ByVal j)
      Dim tmp
      tmp = arr(i)
      arr(i) = arr(j)
      arr(j) = tmp
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' PermuteRotate
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub PermuteRotate(ByRef arr, ByVal start, ByVal n)
      Dim tmp, i
      tmp = arr(start)
      For i = start To n-2
        arr(i) = arr(i+1)
      Next
      arr(n-1) = tmp
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' PermuteCount (e.g. Factorial)
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function PermuteCount(ByVal n)
      If n <= 1 Then
        PermuteCount = 1
      Else
        PermuteCount = n * PermuteCount(n-1)
      End If
    End Function
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/calculating-
permutations/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/calculating-
permutations/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

