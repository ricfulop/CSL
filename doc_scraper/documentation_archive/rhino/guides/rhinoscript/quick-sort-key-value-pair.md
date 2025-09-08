---
url: https://developer.rhino3d.com/guides/rhinoscript/quick-sort-key-value-pair/
scraped_at: 2025-09-08T15:42:55.416172
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

[Quick Sort Key Value
Pairs](https://developer.rhino3d.com/guides/rhinoscript/quick-sort-key-value-
pair/)

  * Overview
  * Quick Sort
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Quick Sort Key Value Pairs

__

Windows only

by [David Rutten](https://discourse.mcneel.com/u/davidrutten/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The .NET Framework’s `SortedList` class provides a hash table with
automatically sorted key-value pairs. The available methods and properties for
`SortedList` are very similar to the ones available in
[ArrayList](https://developer.rhino3d.com/guides/rhinoscript/sorting-vbs-
arrays-with-net/).

The following sample code creates a `SortedList` and populates it with some
key-value pairs:

    
    
    Set SortedList = CreateObject("System.Collections.Sortedlist")
    SortedList.Add "First", "Hello"
    SortedList.Add "Second", ","
    SortedList.Add "Third", "Rhino"
    SortedList.Add "Fourth", "!"
    
    For i = 0 To SortedList.Count - 1
      Rhino.Print SortedList.GetKey(i) & vbTab & SortedList.GetByIndex(i)
    Next
    

**NOTE** : `SortedList` only sorts the list by keys. It is not possible to
sort the list by values.

## Quick Sort

VBScript and RhinoScript do not expose procedures for sorting multiple arrays.
The .NET framework does, but only a single Key-Value pair. The algorithm
outlined on below can be easily extended to work for any number of value
arrays. It is a standard implementation of the
[QuickSort](http://en.wikipedia.org/wiki/Quicksort) algorithm.

QuickSort works through a [Divide and
Conquer](http://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) approach
and it’s one of the fastest sorting algorithms available. However, this
implementation uses the recursive approach which may result in stack overflow
errors on large datasets. QuickSort works best on randomized arrays, if the
array is already almost sorted the solution will take more steps.

This implementation comes as a collection of three procedures, but it can be
easily packaged into one.

First, the big one. This is the actual recursive algorithm:

    
    
    Sub QuickSort(ByRef A(), ByRef B(), ByVal min, ByVal max)
      Dim i : i = min
      Dim k : k = max
    
      If (max - min) >= 1 Then
        Dim pivot : pivot = A(min)
    
        While (k > i)
          While (A(i) <= pivot And i <= max And k > i)
            i = i+1
          Wend
    
          While (A(k) > pivot And k >= min And k >= i)
            k = k-1
          Wend
    
          If (k > i) Then Call SwapElements(A, B, i, k)
        Wend
    
        Call SwapElements(A, B, min, k)
        Call QuickSort(A, B, min, k-1)
        Call QuickSort(A, B, k+1, max)
      End If
    End Sub
    

It depends on the `SwapElement()` subroutine, which could have been written
inline, but since it is called twice, it is placed in a a separate subroutine:

    
    
    Sub SwapElements(ByRef A(), ByRef B(), ByVal i0, ByVal i1)
      Dim loc_A : loc_A = A(i0)
      Dim loc_B : loc_B = B(i0)
    
      A(i0) = A(i1)
      B(i0) = B(i1)
      A(i1) = loc_A
      B(i1) = loc_B
    End Sub
    

Finally, there’s a wrapper procedure that makes calling this function slightly
easier:

    
    
    Function SortByKey(ByRef Keys(), ByRef Values())
      Call QuickSort(Keys, Values, 0, Ubound(Keys))
    End Function
    

## Related Topics

  * [Sorting VBS Arrays with .NET](https://developer.rhino3d.com/guides/rhinoscript/sorting-vbs-arrays-with-net/)
  * [Quicksort on Wikipedia](http://en.wikipedia.org/wiki/Quicksort)
  * [Divide and conquer algorithms on Wikipedia](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithms)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/quick-
sort-key-value-pair/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/quick-
sort-key-value-pair/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

