---
url: https://developer.rhino3d.com/guides/rhinopython/primer-101/
scraped_at: 2025-09-08T15:37:37.106161
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

Rhino.Python 101

A full course on Rhino.Python

![https://developer.rhino3d.com/images/primer-
normals.svg](https://developer.rhino3d.com/images/primer-normals.svg)

You’ve just opened the first edition of the Rhino Python primer. This guide
[was originally
written](https://developer.rhino3d.com/guides/rhinoscript/primer-101/) by
[David Rutten](https://discourse.mcneel.com/u/davidrutten/summary) for Rhino 4
and VBscript and has now been translated to encompass [Python for Rhino
6](https://developer.rhino3d.com/guides/rhinopython/). As always, this primer
is intended to teach programming to absolute beginners, people who have
tinkered with programming a bit or expert programmers looking for a quick
introduction to the methods in Rhino.
[Rhinoscript](https://developer.rhino3d.com/guides/rhinoscript/) (VBscript)
has been supported for many years, with a large user group and extensive
support material. As well as giving a basic introduction, this primer looks to
easily transition those familiar with VBscript into the world of Rhino Python.
For this reason, David Rutten’s original primer has been used extensively as
the underlying framework for this Python Primer. Python offers exciting new
potentials for programming in Rhino with Object-Oriented functionality, simple
syntax, access to the .NET framework and a vast number of user-built libraries
to extend Rhino’s functionality. The same powerful methods that were
previously in VBscript are still available, as well as a ton of other exciting
methods and features available natively with Python.

Similar to the previous primers, we have the advantage of using geometric and
visual examples to help teach programming. In many traditional scenarios,
programming is taught with non-visual examples and difficult to understand
engineering problems. For this reason, as well as Python’s easy-to-read
syntax, we should hopefully be able to bring everyone to understand and write
simple programs to help automate and design within Rhino.

![https://developer.rhino3d.com/images/primer-
branchpropagation2.svg](https://developer.rhino3d.com/images/primer-
branchpropagation2.svg)

Programming offers users the powerful ability to automate tasks, make
decisions, perform powerful calculations and geometric manipulations, thus,
essentially acting as a designer’s side kick. This can allow thousands of
computations to occur based on dynamic conditions, something that would take a
human far too long to process. As a tool for iteration, generation, analysis
and design evolution, programming is limitless! Programming also offers a new
language to communicate with the world because almost every discipline, from
the Sciences, Engineering to Art, utilize code as a progressive new medium -
and this primer should hopefully give you an easy introduction into this
powerful language for communicating with the world. (With that example, it
should be noted that programming may be looked at as any other human language
in the sense that it truly takes many hours of practice to become fluent. So
don’t get discouraged if you aren’t an expert in one day!)

I hope we have convinced you of the powerful and exciting potential for this
new opportunity of Python in Rhino. Without further ado, lets dive in!

Good luck!

**Skylar Tibbits**  
[SJET](http://www.sjet.us)  
[[www.scriptedbypurpose.net](https://www.scriptedbypurpose.net)](http://www.scriptedbypurpose.net)

**Arthur van der Harten**  
[Kirkegaard Associates](http://www.kirkegaard.com)  
[[www.perspectivesketch.com](https://www.perspectivesketch.com)](http://www.perspectivesketch.com)

**Steve Baer**  
[Robert McNeel & Associates](http://www.rhino3d.com)

_A special thanks to David Rutten for the inspiration and invaluable work,
pioneering the original[RhinoScript 101
Primer](https://developer.rhino3d.com/guides/rhinoscript/primer-101/). Also
many thanks to Bob McNeel and everyone at Robert McNeel & Associates for their
generous support!_

[__](http://download.rhino3d.com/IronPython/5.0/RhinoPython101/) [Download the
Rhino.Python 101 Primer as a single PDF
](http://download.rhino3d.com/IronPython/5.0/RhinoPython101/)

### Table of Contents

### 1\. [What’s it all
about?](https://developer.rhino3d.com/guides/rhinopython/primer-101/1-whats-
it-all-about/)

1.1
[Macros](https://developer.rhino3d.com/guides/rhinopython/primer-101/1-whats-
it-all-about/#macros)  
1.2
[Scripts](https://developer.rhino3d.com/guides/rhinopython/primer-101/1-whats-
it-all-about/#scripts)  
1.3 [Running
Scripts](https://developer.rhino3d.com/guides/rhinopython/primer-101/1-whats-
it-all-about/#scripts-1)

### 2\. [Python
Essentials](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/)

2.1 [Language
Origin](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/#language-origin)  
2.2 [Flow
Control](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/#flow-control)  
2.3 [Variable
Data](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/#variable-data)  
2.3.1 [Integers and
Doubles](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/#integers-and-doubles/)  
2.3.2 [Booleans](%28/guides/rhinopython/primer-101/2-python-
essentials/#booleans/%29)  
2.3.3 [Strings](%28/guides/rhinopython/primer-101/2-python-
essentials/#strings/%29)  
2.3.4 [None
Variable](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/#none-variable/)  
2.3.5 [Using Variables](%28/guides/rhinopython/primer-101/2-python-
essentials/#using-variables/%29)

### 3\. [Script
Anatomy](https://developer.rhino3d.com/guides/rhinopython/primer-101/3-script-
anatomy/)

3.1 [Programming in
Rhino](https://developer.rhino3d.com/guides/rhinopython/primer-101/3-script-
anatomy/#31-programming-in-rhino)  
3.2 [The
Bones](https://developer.rhino3d.com/guides/rhinopython/primer-101/3-script-
anatomy/#32-the-bones)  
3.3 [The
Buts](https://developer.rhino3d.com/guides/rhinopython/primer-101/3-script-
anatomy/#33-the-guts)  
3.4 [The
Skin](https://developer.rhino3d.com/guides/rhinopython/primer-101/3-script-
anatomy/#34-the-skin)  
3.5 [The
Debugger](https://developer.rhino3d.com/guides/rhinopython/primer-101/3-script-
anatomy/#35-the-debugger)

### 4\. [Operators and
Functions](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/)

4.1 [What on Earth are they and why should I
care?](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#what-on-earth-are-they-and-why-should-i-care)  
4.2
[Careful…](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#careful)  
4.3 [Logical
Operators](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#logical-operators)  
4.4 [Functions and
Procedures](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#functions-and-procedures)  
4.4.1 [A Simple Function
Example](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#a-simple-function-example)  
4.4.2 [Advanced Function
Syntax](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#advanced-function-syntax)  
4.5
[Mutability](https://developer.rhino3d.com/guides/rhinopython/primer-101/4-operators-
and-functions/#mutability)

### 5\. [Conditional
Execution](https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-
execution/)

5.1 [What
if?](https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-
execution/#what-if)  
5.2
[Looping](https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-
execution/#looping)  
5.3 [Conditional
Loops](https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-
execution/#conditional-loops)  
5.4 [Incremental
Loops](https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-
execution/#incremental-loops)

### 6\. [Tuples, Lists, and
Dictionaries](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/)

6.1
[Tuples](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#tuples)  
6.2
[Lists](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#lists)  
6.2.1 [List
Comprehensions](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#list-comprehension)  
6.3
[Dictionaries](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#dictionaries)  
6.4 [Points and
Vectors](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#points-and-vectors)  
6.5 [An AddVector()
Example](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#an-addvector-example)  
6.6 [Nested
Lists](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/#nested-lists)

### 7\.
[Classes](https://developer.rhino3d.com/guides/rhinopython/primer-101/7-classes/)

7.1 [Class
Syntax](https://developer.rhino3d.com/guides/rhinopython/primer-101/7-classes/#class-
syntax)

### 8\.
[Geometry](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/)

8.1 [The openNURBS™
Kernel](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#the-
opennurbs-kernel)  
8.2 [Objects in
Rhino](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#obects-
in-rhino)  
8.3 [Points and
Pointclouds](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#points-
andpointclouds)  
8.4 [Lines and
Polylines](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#lines-
and-polylines)  
8.5
[Planes](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#planes)  
8.6 [Circles, Ellipses, and
Arcs](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#circles-
ellipses-and-arcs)  
8.6.1
[Ellipses](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#ellipses)  
8.6.2
[Arcs](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#arcs)  
8.7 [NURBS
Curves](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#nurbs-
curves)  
8.7.1 [Control-Point
Curves](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#control-
point-curves)  
8.7.2 [Interpolated
Curves](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#interpolate-
curves)  
8.7.3 [Geometric Curve
Properties](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#geometric-
curve-properties)  
8.8
[Meshes](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#meshes)  
8.8.1 [Geometry vs.
Topology](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#geometry-
vs-topology)  
8.8.1 [Shape vs.
Image](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#shape-
vs-image)  
8.9
[Surfaces](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#surfaces)  
8.9.1 [NURBS
Surfaces](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#nurbs-
surfaces)  
8.9.2 [Surface
Curvature](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#surface-
curvature)  
8.9.3 [Vector And Tensor
Spaces](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/#vector-
and-tensor-spaces)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/primer-101/_index.md)
[
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/primer-101/_index.md)
[ Admin](https://developer.rhino3d.com/admin)

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

