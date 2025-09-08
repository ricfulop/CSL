---
url: https://developer.rhino3d.com/guides/rhinopython/python-reference/
scraped_at: 2025-09-08T15:37:58.175835
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

[Providing Arguments for By-Reference
Parameters](https://developer.rhino3d.com/guides/rhinopython/python-
reference/)

  * Overview
  * More Information
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Providing Arguments for By-Reference Parameters

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
September 9, 2019)

## Overview

Python functions can return multiple objects as a _tuple_.

On the other hand, .NET methods, like those provided by RhinoCommon, can only
return one object as the result of a call. In order to return more than one
object, by-reference, or _by-ref_ , parameters are needed. These parameters
are decorated with the `ref` and `out` keywords in C#.

## More Information

A example of a method that requires a by-ref parameter is
[Dictionary.TryGetValue](https://docs.microsoft.com/en-
us/dotnet/api/system.collections.generic.dictionary-2.trygetvalue), which has
a `value` [output parameter](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/keywords/out-parameter-modifier). The
method returns `true` if the dictionary contains an element with the specified
key (the element value itself is returned to the parameter “value”), otherwise
it returns `false`.

When making calls to such methods in IronPython, we may not pass in arguments
for the output parameters. Instead, the result of such .NET method call in
IronPython will likely be a tuple (unless the .NET method’s return type is
`void` and the method has only one by-ref parameter), which contains the value
of the output parameter (see the example below).

    
    
    import System
    d = System.Collections.Generic.Dictionary[int, str]()
    d[1], d[2] = 'One', 'Two'
     
    print d.TryGetValue(1)         # (True, 'One')
    print d.TryGetValue(2)[1]      # Two 
    print d.TryGetValue(3)         # (False, None)
    

We may also pass a **clr.Reference** object for the output parameter. The
**clr.Reference** object has only one member “Value”, which will carry the
output parameter value after the call. When encountering this type of
argument, the IronPython code generation and runtime does something special to
update the “Value”.

    
    
    x = clr.Reference[str]()
    print d.TryGetValue(1, x), x.Value   # True One
    print d.TryGetValue(3, x), x.Value   # False None
    

For [reference parameters](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/keywords/ref), we are required to pass in
something. If the argument is not a **clr.Reference** object, such reference
argument value will also be part of the returned tuple; otherwise, the by-ref
change is tracked inside **clr.Reference**.

Note, if the .NET method contains more than one by-ref parameter, Python
expects the user to provide proper **clr.Reference** objects for either all or
none of them. A mix of **clr.Reference** objects and normal argument/omission
(for out parameter) will cause an error.

## Example

For a practical example, let’s look at RhinoCommon’s
[NurbsSurfacePointList.GetPoint](https://developer.rhino3d.com/api/RhinoCommon/html/Overload_Rhino_Geometry_Collections_NurbsSurfacePointList_GetPoint.htm)
method, which has two overloads:

    
    
    // Gets a world 3-D, or Euclidean, control point at the given u,v index. 
    // The 4-D representation is (x, y, z, 1.0).
    public bool GetPoint(int u, int v, out Point3d point)
    
    // Gets a homogeneous control point at the given (u, v) index, 
    // where the 4-D representation is (x, y, z, w). 
    // The world 3-D, or Euclidean, representation is (x/w, y/w, z/w).
    public bool GetPoint(int u, int v, out Point4d point)
    

The following sample code calls each overloaded method. Notice how using
**clr.Reference** eliminates the need for using the **Overloads** method, in
this case.

    
    
    import clr
    import Rhino
    import rhinoscriptsyntax as rs
    
    srf_id = rs.GetObject("Select surface", rs.filter.surface)
    srf = rs.coercesurface(srf_id)
    ns = srf.ToNurbsSurface()
    
    pt3d = clr.Reference[Rhino.Geometry.Point3d]()
    for u in range(0, ns.Points.CountU):
        for v in range(0, ns.Points.CountV):
            if ns.Points.GetPoint(u, v, pt3d):
                print pt3d
    
    pt4d = clr.Reference[Rhino.Geometry.Point4d]()
    for u in range(0, ns.Points.CountU):
        for v in range(0, ns.Points.CountV):
            if ns.Points.GetPoint(u, v, pt4d):
                print pt4d
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
reference/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
reference/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

