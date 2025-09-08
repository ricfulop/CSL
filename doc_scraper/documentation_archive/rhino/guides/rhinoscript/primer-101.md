---
url: https://developer.rhino3d.com/guides/rhinoscript/primer-101/
scraped_at: 2025-09-08T15:41:45.137388
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

RhinoScript 101

__

Windows only

A full course on RhinoScript

![https://developer.rhino3d.com/images/primer-
normals.svg](https://developer.rhino3d.com/images/primer-normals.svg)

You’ve just opened the third edition of the RhinoScript primer. This booklet
was originally written as a workshop handout for the students at the
Architecture faculty of the Universität für Angewandte Kunst in Vienna. The
aim of the workshop was to teach them how to program Rhino in no more than
four days and, counter all my expectations, they did. Most of them had never
programmed before so I had to make sure the text was suitable for absolute
beginners. I did not expect at the time that this proved to be the most
successful aspect of the primer. After the workshop, a slightly reworked
version was made available to the public and it has helped many non-
programmers getting rid of the “non” since. Incidentally, if you do not
succeed in learning RhinoScript within a time-span of four days, do not feel
bad about yourself. Remember that those students received additional lectures
and intensive support from someone who took two months to reach the same
level.

This new edition essentially caters for two major demands; the release of
Rhinoceros 4.0 and the superficiality of the old edition. RhinoScript has
existed for many years, but has recently taken a big leap forward with the
development of Rhino4. Scripters of course want to take advantage of all the
new functionality offered by this release and new programmers don’t want to
start learning an outdated language. I have tried to combine the original aims
of the primer with the requests for more in-depth articles, but it is always
hard to judge the clarity of a text when one is highly familiar with its
subject matter to begin with. You will have to be the judge. But always
remember that learning programming -though fun- is no laughing matter so to
speak. The ancient Greeks already understood that hubris is a party spoiler
and the best way to prevent this learning experience turning into a classic
tragedy, is to take it slow. Do not continue reading if you’re uncomfortable
with past paragraphs. Re-read when in doubt. Ask questions if necessary.
Programming is not difficult, but it requires a certain frame of mind which
some beginners find hard to acquire. I know I did.

![https://developer.rhino3d.com/images/primer-
branchpropagation2.svg](https://developer.rhino3d.com/images/primer-
branchpropagation2.svg)

The one advantage I enjoy over authors of other programming books, is that I
shall be teaching you to program Rhino. Writing scripts for Rhino means you
have an exceptionally powerful geometry kernel at your disposal which enables
you to achieve the most outrageous results with a minimum of code. Instead of
boring you with days-of-the-week and employee-salary-classes examples, I get
to bore you with freeform surfaces, evolving curves and inflating meshes.

Hopefully, this third edition of the RhinoScript primer will help existing
scripters get the most out of Rhino4, while teaching regular human beings how
to become scripters in the first place.

Good luck!

![https://developer.rhino3d.com/images/primer-
autograph.svg](https://developer.rhino3d.com/images/primer-autograph.svg)

David Rutten _Robert McNeel & Associates_

[__](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) [Download the
RhinoScript 101 Primer as a single PDF
](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Table of Contents

### 1\. [What’s it all
about?](https://developer.rhino3d.com/guides/rhinoscript/primer-101/1-whats-
it-all-about/)

1.1
[Macros](https://developer.rhino3d.com/guides/rhinoscript/primer-101/1-whats-
it-all-about/#11-macros)  
1.2
[Scripts](https://developer.rhino3d.com/guides/rhinoscript/primer-101/1-whats-
it-all-about/#12-scripts)  
1.3 [Running
Scripts](https://developer.rhino3d.com/guides/rhinoscript/primer-101/1-whats-
it-all-about/#13-scripts)

### 2\. [VBscript
Essentials](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/)

2.1 [Language
Origin](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#21-language-origin)  
2.2 [Flow
Control](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#f22-low-control)  
2.3 [Variable
Data](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#23-variable-data)  
2.3.1 [Integers and
Doubles](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#231-integers-and-doubles)  
2.3.2
[Booleans](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#232-booleans)  
2.3.3
[Strings](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#233-strings)  
2.3.4 [None
Variable](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#234-none-variable)  
2.3.5 [Using
Variables](https://developer.rhino3d.com/guides/rhinoscript/primer-101/2-vbscript-
essentials/#235-using-variables)

### 3\. [Script
Anatomy](https://developer.rhino3d.com/guides/rhinoscript/primer-101/3-script-
anatomy/)

3.1 [Programming in
Rhino](https://developer.rhino3d.com/guides/rhinoscript/primer-101/3-script-
anatomy/#31-programming-in-rhino)  
3.2 [The
Bones](https://developer.rhino3d.com/guides/rhinoscript/primer-101/3-script-
anatomy/#32-the-bones)  
3.3 [The
Guts](https://developer.rhino3d.com/guides/rhinoscript/primer-101/3-script-
anatomy/#33-the-guts)  
3.4 [The
Skin](https://developer.rhino3d.com/guides/rhinoscript/primer-101/3-script-
anatomy/#34-the-skin)

### 4\. [Operators and
Functions](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/)

4.1 [What on Earth are they and why should I
care?](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/#41-what-on-earth-are-they-and-why-should-i-care)  
4.2
[Careful…](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/#42-careful)  
4.3 [Logical
Operators](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/#43-logical-operators)  
4.4 [Functions and
Procedures](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/#44-functions-and-procedures)  
4.4.1 [A Simple Function
Example](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/#441-a-simple-function-example)  
4.4.2 [Advanced Function
Syntax](https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-
and-functions/#442-advanced-function-syntax)

### 5\. [Conditional
Execution](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/)

5.1 [What
if?](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/#51-what-if)  
5.2 [Select
Case](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/#52-select-case)  
5.3
[Looping](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/#53-looping)  
5.4 [Conditional
Loops](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/#54-conditional-loops)  
5.5 [Alternate
Syntax](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/#55-alternate-syntax)  
5.6 [Incremental
Loops](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/#56-incremental-loops)

### 6\.
[Arrays](https://developer.rhino3d.com/guides/rhinoscript/primer-101/6-arrays/)

6.1 [My Favorite
Things](https://developer.rhino3d.com/guides/rhinoscript/primer-101/6-arrays/#61-my-
favorite-things)  
6.2 [Points and
Vectors](https://developer.rhino3d.com/guides/rhinoscript/primer-101/6-arrays/#62-points-
and-vectors)  
6.3 [An AddVector()
Example](https://developer.rhino3d.com/guides/rhinoscript/primer-101/6-arrays/#63-an-
addvector-example)  
6.4 [Nested
Lists](https://developer.rhino3d.com/guides/rhinoscript/primer-101/6-arrays/#64-nested-
lists)

### 7\.
[Geometry](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/)

7.1 [The openNURBS™
Kernel](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#71-the-
opennurbs-kernel)  
7.2 [Objects in
Rhino](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#72-objects-
in-rhino)  
7.3 [Points and
Pointclouds](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#73-points-
and-pointclouds)  
7.4 [Lines and
Polylines](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#74-lines-
and-polylines)  
7.5
[Planes](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#75-planes)  
7.6 [Circles, Ellipses, and
Arcs](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#76-circles-
ellipses-and-arcs)  
7.6.1
[Ellipses](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#761-ellipses)  
7.6.2
[Arcs](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#762-arcs)  
7.7 [NURBS
Curves](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#77-nurbs-
curves)  
7.7.1 [Control-Point
Curves](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#771-control-
point-curves)  
7.7.2 [Interpolated
Curves](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#772-interpolate-
curves)  
7.7.3 [Geometric Curve
Properties](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#773-geometric-
curve-properties)  
7.8
[Meshes](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#78-meshes)  
7.8.1 [Geometry vs.
Topology](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#781-geometry-
vs-topology)  
7.8.1 [Shape vs.
Image](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#781-shape-
vs-image)  
7.9
[Surfaces](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#79-surfaces)  
7.9.1 [NURBS
Surfaces](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#791-nurbs-
surfaces)  
7.9.2 [Surface
Curvature](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#792-surface-
curvature)  
7.9.3 [Vector And Tensor
Spaces](https://developer.rhino3d.com/guides/rhinoscript/primer-101/7-geometry/#793-vector-
and-tensor-spaces)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/primer-101/_index.md)
[
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/primer-101/_index.md)
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

