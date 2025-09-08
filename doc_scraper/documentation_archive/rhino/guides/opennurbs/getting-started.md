---
url: https://developer.rhino3d.com/guides/opennurbs/getting-started/
scraped_at: 2025-09-08T15:38:07.234731
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

[Getting Started](https://developer.rhino3d.com/guides/opennurbs/getting-
started/)

  * Prerequisites
  * openNURBS public SDK
  * Supported C++ Compilers
  * Read and Write
  * 3DM File Versions
  * Examples
  * Answers to frequently asked questions:
    * ON_Mesh
    * ON_Brep
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Getting Started

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Tuesday,
March 25, 2025)

## Prerequisites

openNURBS is intended for _skilled_ C++ developers. Please read [What is
openNURBS?](https://developer.rhino3d.com/guides/opennurbs/what-is-opennurbs/)
if you have not already. It is also presumed that you have an application that
wishes to access _3DM_ files outside of Rhinoceros.

## openNURBS public SDK

To download the public C++ SDK and example 3DM files, visit
<https://www.rhino3d.com/opennurbs>.

## Supported C++ Compilers

The openNURBS C++ toolkit has been successfully used with the following
compilers:

  * A version of _Microsoft Visual Studio_ that includes the Visual Studio 2019 (v142) platform toolset. Thus, you can use either Visual Studio 2022 or Visual Studio 2019. To build openNURBS and the examples with _Microsoft Visual Studio_ , use the solution _opennurbs_public.sln_.

To use C++ opennurbs in your Visual Studio project:

    1. Open opennurbs_public.sln in Visual Studio, select the platform and configuration, and rebuild all.
    2. In your project’s stdafx.h, put the following lines. This will include all the header files you need to call C++ opennurbs and automatically link in the correct libraries:
    
    // defining OPENNURBS_PUBLIC_INSTALL_DIR enables automatic linking using pragmas
    #define OPENNURBS_PUBLIC_INSTALL_DIR "<MY_INSTALLPATH>"
    // uncomment the next line if you want to use opennurbs as a DLL
    //#define OPENNURBS_IMPORTS
    #include "<MY_INSTALLPATH>/opennurbs_public.h"
    

  * _Apple Xcode 9.2_ (9C40b): To build openNURBS and the examples with _Xcode 9.2_ (or later), use the workspace _opennurbs_public.xcworkspace_.

  * _Other C++ compilers_ The compiler must support the C++14 standard. A _makefile_ is provided as a starting point. The openNURBS C++ source code is clean and simple. If you are using a C++ compiler that supports the C++14 standard and run into some toolkit code that causes problems, please [let us know](http://discourse.mcneel.com/category/opennurbs). We’ll attempt to change the code to accommodate the compiler.

## Read and Write

Use `ONX_Model::Read()` and `ONX_Model::Write()` to add support for reading
and writing 3DM files to your application. See _example_read.cpp_ and
_example_write.cpp_ for more details.

  1. Compile the openNURBS Toolkit library. To compile the example programs you must link with the openNURBS Toolkit library.
  2. Study _example_read\example_read.cpp_. All the openNURBS geometry classes are derived from the `ON_Geometry` class. If you need generic attribute information, there is probably an `ON_Geometry` member function that will answer your query. See the `Dump()` function in _example_read.cpp_ for code that demonstrates how to use the `Cast()` function to get at the actual class definitions.
  3. Study _example_write\example_write.cpp_. If you want to write points, meshes, NURBS curves, NURBS surfaces, or trimmed NURBS surfaces, you should be able to cut and paste most of what you need from the functions in _example_write.cpp_. If you want to write trimmed surfaces or b-reps, then please study _example_brep.cpp_.
  4. Study _example_brep\example_brep.cpp_. If you want to write solid models or more general b-reps, then first work through _example_write.cpp_ and then work through _example_brep.cpp_.
  5. The comments in the openNURBS Toolkit header files are the primary source of documentation. I suggest that you use a development environment that has high quality tags capabilities and a good class browser.
  6. In the code you write include only _opennurbs.h_. The _opennurbs.h_ header file includes the necessary openNURBS toolkit header files in the appropriate order.
  7. Other items to note: 
     1. _Strings_ The `ON_wString` class has `wchar_t` elements. When using Microsoft Visual Studio on Windows, `sizeof(wchar_t)=2` and `ON_wString` content is UTF-16 encoded. When using Apple XCode on Mac OS, `sizeof(wchar_t)=4` and `ON_wString` content is UTF-32 encoded.
     2. All memory allocations and frees are done through `onmalloc()`, `onfree()`, and `onrealloc()`. The source that ships with openNURBS has `onmalloc()` call `malloc()` and `onfree()` call `free()`. 1\. If you want to use Open GL to render openNURBS geometry, you may want to include _opennurbs_gl.h_ after _opennurbs.h_ and add _opennurbs_gl.cpp_ to your openNURBS library. See _example_gl.cpp_ for details. 1\. The openNURBS Toolkit works correctly on both big and little endian CPUs.

## 3DM File Versions

  1. _Version 1 3DM files_. The openNURBS toolkit will read version 1 files. Rhino 1.0 and other applications using the old Rhino I/O toolkit create version 1 files.
  2. _Version 2 3DM files_. The openNURBS toolkit will read and write version 2 files. Rhino 2.0 and applications using an openNURBS toolkit released on or after December 2000 create version 2 files. (Rhino 1.0 and the old Rhino I/O toolkit will not read version 2 files.)
  3. _Version 3 3DM files_. The openNURBS toolkit will read and write version 3 files. Rhino 3.0 and applications using an openNURBS toolkit released on or after October 2002 create version 3 files. (Rhino’s 1.0 and 2.0 will not read version 3 files.)
  4. _Version 4 3DM files_. The openNURBS toolkit will read and write version 4 files. Rhino 4.0 and applications using an openNURBS toolkit released on or after September 2006 create version 4 files. (Rhino’s 1.0, 2.0 and 3.0 will not read version 4 files.)
  5. _Version 5 3DM files_. The openNURBS toolkit will read and write version 5 files. Rhino 5 and applications using an openNURBS toolkit released on or after September 2009 create version 5 files. (Rhino’s 1.0, 2.0, 3.0 and 4.0 will not read version 5 files.)
  6. _Version 6 3DM files_. The openNURBS toolkit will read and write version 6 files. Rhino 6 and applications using an openNURBS toolkit released on or after January 2018 create version 6 files. (Rhino’s 1.0, 2.0, 3.0, 4.0 and 5 will not read version 6 files.)
  7. _Version 7 3DM files_. The openNURBS toolkit will read and write version 7 files. Rhino 7 and applications using an openNURBS toolkit released on or after November 2020 create version 7 files. (Rhino’s 1.0, 2.0, 3.0, 4.0, 5 and 6 will not read version 7 files.)
  8. _Version 8 3DM files_. The openNURBS toolkit will read and write version 8 files. Rhino 8 and applications using an openNURBS toolkit released on or after October 2023 create version 8 files. (Rhino’s 1.0, 2.0, 3.0, 4.0, 5, 6, and 7 will not read version 8 files.)

Sample 3DM files are availble from <https://www.rhino3d.com/opennurbs>

## Examples

This is an overview of the examples included with the openNURBS toolkit:

  * _example_read\example_read.cpp_ : Create a program by compiling _example_read.cpp_ and statically linking with the openNURBS library. The code in _example_read.cpp_ illustrates how to read an openNURBS _.3dm_ file.
  * _example_write\example_write.cpp_ : Create a program by compiling _example_write.cpp_ and linking with the openNURBS library. The code in _example_write.cpp_ illustrates how to write layers, units system and tolerances, viewports, spotlights, points, meshes, NURBs curves, NURBs surfaces, trimmed NURBs surfaces, texture and bump map information, render material name, and material definitions to an openNURBS _.3dm_ file. The bitmap _example_write\example_texture.bmp_ is referenced by a rendering material texture in one of the 3DM files created by _example_write_.
  * _example_test\example_test.cpp_ : Create a program by compiling _example_test.cpp_ and linking with the openNURBS library. The example_test program can be used to validate your opennurbs installation.
  * _example_brep\example_brep.cpp_ : Create a program by compiling _example_brep.cpp_ and linking with the openNURBS library. The code in _example_write.cpp_ illustrates how to write a solid model.
  * _example_userdata\example_userdata.cpp_ : Create a program by compiling _example_userdata.cpp_ and linking with the openNURBS library. The code in _example_userdata_ demonstrates how to create and manage arbitrary user defined information in _.3dm_ files.
  * _The Open GL example_ : This code is a crude sketch of a starting point for using OpenGL to display opennurbs geometry. Start with simple mesh objects and work up. We do not provide support for using OpenGL.

## Answers to frequently asked questions:

### ON_Mesh

#### Vertex ordering in ON_Mesh faces

All faces in a `ON_Mesh` are stored with vertices listed in counter-clockwise
order. In particular, for quads the vertices are ordered as:

![Vertex Ordering](https://developer.rhino3d.com/images/opennurbs-getting-
started-01.png)

The quads may be non-planar.

The definition of `void ON_GL( const ON_Mesh& )` in _opennurbs_gl.cpp_
demonstrates how to go through an `ON_Mesh` and render all the quads as two
triangles.

### ON_Brep

#### Orientation of ON_Brep faces

The UV orientation of surfaces in a Brep is arbitrary. If the `BOOL
ON_BrepFace::m_bRev` member is `FALSE`, then the face’s orientation agrees
with the surface’s natural $$Du \times Dv$$ orientation. When the member is
`TRUE`, the face’s orientation is opposite the surface’s natural $$Du \times
Dv$$ orientation.

If your application cannot handle `ON_BrepFaces` that have a `TRUE` `m_bRev`
flag, then call `ON_Brep::FlipReversedSurfaces()`. See the comments in
`ON_Brep::FlipReversedSurfaces()` and `ON_Brep::SwapFaceParameters()` for
details.

#### Trimming loop order and nesting

The `ON_BrepLoop::m_type` member records the type of boundary (inner, outer,
etc.). A `ON_BrepFace` has exactly one outer loop and it is the first loop
referenced in the `ON_BrepFace::m_li[]` array. The inner loops all define
“holes” in the `ON_BrepFace`. All the inner holes lie inside of the outer
loop. A `ON_BrepFace` is always path connected. In particular, inner loops are
not “nested.”

#### Surfaces in Rhino are read as ON_Breps

Internally, Rhino stores all surfaces as some type of b-rep and the openNURBS
toolkit reads these objects as b-reps. To see if an entire

`ON_Brep` is really just a surface, use:

`BOOL ON_Brep::IsSurface()`

If `ON_Brep::IsSurface()` returns `TRUE`, then the b-rep geometry is the same
as the surface `ON_Brep::m_S[0]`.

To see of a particular face in a b-rep is really just a surface, use:

`BOOL ON_Brep::FaceIsSurface( face_index )`

If `ON_Brep::FaceIsSurface( face_index )` returns `TRUE`, then the face’s
geometry is the same as the surface `ON_Brep::m_S[face.m_si]`.

## Related Topics

  * [What is openNURBS?](https://developer.rhino3d.com/guides/opennurbs/what-is-opennurbs/)
  * [What is Rhino3dmIO?](https://developer.rhino3d.com/guides/opennurbs/what-is-rhino3dmio/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/getting-
started/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/getting-
started/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

