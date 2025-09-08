---
url: https://developer.rhino3d.com/guides/rhinoscript/multidimensional-arrays/
scraped_at: 2025-09-08T15:42:23.163267
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

[Multidimensional
Arrays](https://developer.rhino3d.com/guides/rhinoscript/multidimensional-
arrays/)

  * Overview
  * Rectangular
  * Ragged
  * Resizing

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Multidimensional Arrays

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

VBScript supports two kinds of multidimensional arrays, called rectangular and
ragged. Why are there two types of multidimensional arrays? What is the
difference between the (x)(y) and (x,y) notation? We will cover these
questions as well as talk about resizing multidimensional arrays.

## Rectangular

A rectangular array is, well, “rectangular.” For example:

    
    
    Dim MyArray(3,2)
    

and you get:

    
    
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    (2,0) (2,1) (2,2)
    (3,0) (3,1) (3,2)
    

which makes a nice rectangle. A three-dimensional array makes a rectangular
prism, and so on up into the higher dimensions.

## Ragged

A common practice used by RhinoScript is to simulate multidimensional arrays
by making an array of arrays known as ragged or nested arrays. For example:

    
    
    Dim MyArray
    MyArray = Array(Array(1, 2, 3), Array(4, 5), Array(6, 7, 8, 9))
    

And so dereferencing the outer array gives you the inner array, which can then
be dereferenced itself:

    
    
    Rhino.Print MyArray(2)(0) ' 6
    

But, you notice something about the indices if we write them out as before:

    
    
    (0)(0) (0)(1) (0)(2)
    (1)(0) (1)(1)
    (2)(0) (2)(1) (2)(2) (2)(3)
    

The indices make a ragged pattern, not a straight rectangular pattern. It is
possible to create ragged higher dimensional, but allocating all the sub-
arrays can be difficult.

Thus, in VBScript if you say:

    
    
    MyArray(2,3)
    

then you are talking to a rectangular two-dimensional array. And, if you say:

    
    
    MyArray(2)(3)
    

then you are talking to a one dimensional array that contains another one
dimensional array.

## Resizing

The `ReDim` statement is used to size or resize a dynamic array that has
already been formally declared using a `Private`, `Public`, or `Dim` statement
with empty parentheses (without dimension subscripts). You can use the `ReDim`
statement repeatedly to change the number of elements and dimensions in an
array.

If you use the `Preserve` keyword, you can resize only the last array
dimension, and you can’t change the number of dimensions at all. For example,
if your array has only one dimension, you can resize that dimension because it
is the last and only dimension. However, if your array has two or more
dimensions, you can change the size of only the last dimension and still
preserve the contents of the array.

#### WARNING

If you make an array smaller than it was originally, data in the eliminated
elements is lost.

The following example shows how you can increase the size of the last
dimension of a dynamic array without erasing any existing data contained in
the array.

    
    
    ReDim arr(10, 10, 10)
    ...
    ReDim Preserve arr(10, 10, 15)
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/multidimensional-
arrays/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/multidimensional-
arrays/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

