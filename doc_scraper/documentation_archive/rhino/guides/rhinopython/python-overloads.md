---
url: https://developer.rhino3d.com/guides/rhinopython/python-overloads/
scraped_at: 2025-09-08T15:37:56.152482
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

[Calling Overloaded Methods from
Python](https://developer.rhino3d.com/guides/rhinopython/python-overloads/)

  * Problem
  * More Information
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Calling Overloaded Methods from Python

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
April 12, 2019)

## Problem

When you run a script that calls a RhinoCommon method that has
[overloads](https://docs.microsoft.com/en-us/dotnet/standard/design-
guidelines/member-overloading) , you might see the following error:

    
    
    Message: Multiple targets could match
    

## More Information

.NET supports [overloading methods](https://docs.microsoft.com/en-
us/dotnet/standard/design-guidelines/member-overloading) by both number of
arguments and type of arguments.

When [IronPython](https://ironpython.net/) code calls an overloaded method, it
tries to select one of the overloads at runtime based on the number and type
of arguments passed to the method, and also names of any keyword arguments.

In most cases, the expected overload gets selected. However,
[IronPython](https://ironpython.net/) will raise a `TypeError` if there are
conversions to more than one of the overloads:

To control the exact overload that gets called, use the **Overloads** method
on _method_ objects:

## Example

For a practical example, let’s look at RhinoCommon’s
[Brep.Split](https://developer.rhino3d.com/api/RhinoCommon/html/Overload_Rhino_Geometry_Brep_Split.htm)
method, which has five overloads:

    
    
    // Splits a Brep into pieces using a Brep as a cutter.
    public Brep[] Split(Brep splitter, double intersectionTolerance)
    
    // Splits a Brep into pieces using Breps as cutters.
    public Brep[] Split(IEnumerable<Brep> cutters, double intersectionTolerance)
    
    // Splits a Brep into pieces using curves, at least partially on the Brep, as cutters.
    public Brep[] Split(IEnumerable<Curve> cutters, double intersectionTolerance)
    
    // Splits a Brep into pieces using a Brep as a cutter.
    public Brep[] Split(Brep splitter, double intersectionTolerance, out bool toleranceWasRaised)
    
    // Splits a Brep into pieces using a combination of curves, to be extruded, and Breps as cutters.
    public Brep[] Split(IEnumerable<GeometryBase> cutters, Vector3d normal, bool planView, double intersectionTolerance)
    

If you run the following example code, which should split a `Brep` with one or
more cutting `Breps`:

    
    
    import Rhino
    import scriptcontext as sc
    import rhinoscriptsyntax as rs
    
    id = rs.GetObject("Select Brep to split", filter = 8+16, preselect = True)
    brep = rs.coercebrep(id)
    
    ids = rs.GetObjects("Select cutting Breps", filter = 8+16,)
    cutters = [rs.coercebrep(item) for item in ids]
    
    tol = sc.doc.ModelAbsoluteTolerance
    out_breps = brep.Split(cutters, tol)
    new_ids = [sc.doc.Objects.AddBrep(brep) for brep in out_breps]
    

You will receive the following error:

    
    
    Message: Multiple targets could match: Split(IEnumerable[Curve], float), Split(IEnumerable[Brep], float)
    

To use the second overload, use the **Overloads** method in this manner:

    
    
    out_breps = brep.Split.Overloads[IEnumerable[Rhino.Geometry.Brep], System.Double](cutters, tol)
    

Here is the full working sample:

    
    
    import System
    import System.Collections.Generic.IEnumerable as IEnumerable
    import Rhino
    import rhinoscriptsyntax as rs
    import scriptcontext as sc
    
    id = rs.GetObject("Select Brep to split", filter = 8+16, preselect = True)
    brep = rs.coercebrep(id)
    
    ids = rs.GetObjects("Select cutting Breps", filter = 8+16,)
    cutters = [rs.coercebrep(item) for item in ids]
        
    tol = sc.doc.ModelAbsoluteTolerance
    out_breps = brep.Split.Overloads[IEnumerable[Rhino.Geometry.Brep], System.Double](cutters, tol)
    new_ids = [sc.doc.Objects.AddBrep(brep) for brep in out_breps]
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
overloads/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
overloads/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

