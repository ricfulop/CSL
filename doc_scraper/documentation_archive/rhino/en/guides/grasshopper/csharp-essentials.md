---
url: https://developer.rhino3d.com/en/guides/grasshopper/csharp-essentials/
scraped_at: 2025-09-08T16:08:00.736113
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

Essential C# Scripting for Grasshopper

A full course on RhinoComon in Grasshopper using C#

This is an essential scripting guide

![https://developer.rhino3d.com/images/math-logo.svg](cover_csharp.png)

This manual is intended for designers who are experienced in [Grasshopper®
(GH)](https://www.grasshopper3d.com) visual scripting, and would like to take
their skills to the next level to create their own custom scripts using C#
programming language. This guide does not assume nor require any background in
programming. The document is divided into four parts.

  1. [C# Component in Grasshopper](https://developer.rhino3d.com/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/) explains the general interface of the C# scripting component in Grasshopper.
  2. [C# Programming Basics](https://developer.rhino3d.com/guides/grasshopper/csharp-essentials/2-csharp-basics/) reviews the basics of the C# DotNet programming language.
  3. [RhinoCommon Geometry](https://developer.rhino3d.com/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/) covers the main geometry types and functions in the RhinoCommon SDK.
  4. [Design Algorithms](https://developer.rhino3d.com/guides/grasshopper/csharp-essentials/4-design-algorithms/) includes examples of a number of design algorithms.

The guide includes many examples that are also available as a Grasshopper file
available with the download of this guide. Note that all examples are written
in version 8 of [Rhinoceros® (Rhino)](https://www.rhino3d.com) and
Grasshopper.

I would like to acknowledge the excellent technical review by Mr. Steve Baer
of Robert McNeel and Associates. I would also like to acknowledge Ms. Sandy
McNeel for reviewing the writing and formatting of this document.

_**[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)**_

Robert McNeel & Associates

### Table of Contents

### 1\. [C# Component in
Grasshopper](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/)

1.1 [Introduction](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#11-introduction)  
1.2 [C# component
interface](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#12-c-component-interface)  
1.3 [The input
parameters](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#13-the-input-parameters)  
1.4 [The output
parameters](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#14-the-output-parameters)  
1.5 [The out string](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#15-the-out-string)  
1.6 [Main menu](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#16-main-menu)  
1.7 [Code editor](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#17-code-editor)  
1.7.1 [Imports](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#171-imports)  
1.7.2 [Utility members and
functions](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#172-utility-members--functions)  
1.7.3 [The RunScript](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#173-the-runscript)  
1.8 [Data access](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#18-data-access)  
1.8.1 [Item access](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#181-item-access)  
1.8.2 [Lists access](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#182-list-access)  
1.8.3 [Tree access](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/1-grasshopper-csharp-component/#183-tree-access)

### 2\. [C# Programming
Basics](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/)

2.1 [Introduction](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#21-introduction)  
2.2 [Comments](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#22-comments)  
2.3 [Variables](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#23-variables)  
2.4 [Operators](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#24-operators)  
2.5 [Namespaces](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#25-namespaces)  
2.6 [Data](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#26-data)  
2.6.1 [Primitive data
types](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#261-primitive-data-types)  
2.6.2 [Collections](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#262-collections)  
2.7 [Flow control](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#27-flow-control)  
2.7.1 [Conditional
statements](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#271-conditional-statements)  
2.7.2 [Loops](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#272-loops)  
2.8 [Methods](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#28-methods)  
2.8.1 [Overview](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#281-overview)  
2.8.2 [Method
parameters](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#282-method-parameters)  
2.9 [User-defined data
types](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#29-user-defined-data-types)  
2.9.1 [Enumerations](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#291-enumerations)  
2.9.2 [Structures](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#292-structures)  
2.9.3 [Classes](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#293-classes)  
2.9.4 [Value vs reference
types](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#294-value-vs-reference-types)  
2.9.5 [Interface](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#295-interface)  
2.10 [Read and write text
files](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#210--read--write-text-files)  
2.11 [Recursive
functions](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/2-csharp-basics/#211-recursive-functions)

### 3\. [RhinoCommon
Geometry](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/)

3.1 [Overview](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#31-overview)  
3.2 [Geometry
structures](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#32-geometry-structures)  
3.2.1 [The Point3d
structure](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#321-the-point3d-structure)  
3.2.2 [Points and
vectors](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#322-points--vectors)  
3.2.3 [Lightweight
curves](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#323-lightweight-curves)  
3.2.4 [Lightweight
surfaces](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#324-lightweight-surfaces)  
3.2.5 [Lightweight
surfaces](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#325-other-geometry-structures)  
3.3 [Geometry
classes](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#33-geometry-classes)  
3.3.1 [Curves](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#331-curves)  
3.3.2 [Surfaces](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#332-surfaces)  
3.3.3 [Meshes](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#333-meshes)  
3.3.4 [Boundary representation
(Brep)](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#334-boundary-representation-brep)  
3.3.5 [Other geometry
classes](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#335-other-geometry-classes)  
3.4 [Geometry
transformations](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/3-rhinocommon-geometry/#34-geometry-transformations)

### 4\. [Design
Algorithms](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/)

4.1 [Introduction](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#41-introduction)  
4.2 [Geometry
algorithms](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#42-geometry-algorithms)  
4.2.1 [Sine curves and
surface](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#421-sine-curves-and-surface)  
4.2.2 [De Casteljau algorithm to interpolate a Bezier
curve](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#421-sine-curves-and-surface)  
4.2.3 [Simple subdivision
mesh](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#422-de-casteljau-algorithm-to-interpolate-a-
bezier-curve)  
4.3 [Generative
algorithms](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#43-generative-algorithms)  
4.3.1 [Dragon curve](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#431-dragon-curve)  
4.3.2 [Fractal tree](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#432-fractal-tree)  
4.3.3 [Penrose
tiling](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#433-penrose-tiling)  
4.3.4 [Conway Game of
Life](https://developer.rhino3d.com/guides/grasshopper/csharp-
essentials/4-design-algorithms/#434-conway-game-of-life)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/csharp-
essentials/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/csharp-
essentials/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

