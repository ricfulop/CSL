---
url: https://developer.rhino3d.com/guides/rhinoscript/trimming-curves/
scraped_at: 2025-09-08T15:43:06.470539
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

[Trimming Curves](https://developer.rhino3d.com/guides/rhinoscript/trimming-
curves/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Trimming Curves

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you need to trim a lot of lines where they intersect. How is this
done? What is a “domain?”

## Solution

If you can remember back to your pre-calculus days, a domain is most often
defined as the set of values for which a function is defined. As curves in
Rhino have starting and ending points, they also have starting (minimum) and
ending (maximum) domain values (parameters). You can obtain a curve’s minimum
and maximum domain values using the `CurveDomain` function.

To trim a curve using TrimCurve, you must provide an interval, or sub-domain,
of the curve that you want to keep. For example, if you have a curve with a
minimum domain value of 0 and a maximum domain value of 5 and you wanted
everything from t=2 to the end of the curve trimmed away, then you’d do
something like this:

    
    
    domain = Rhino.CurveDomain(curve)
    Call Rhino.TrimCurve(curve, Array(domain(0), 2), True)
    

Remember, the interval argument defines what you want to keep, not what you
want to trim.

If two curves intersect, `CurveCurveIntersection` will return the parameter on
the curve where the intersection event took place. Using this parameter, you
can begin to build an interval to pass to `TrimCurve`.

The following example script demonstrates how to interactively trim a curve
using what was discussed above…

    
    
    Sub TestTrimCurve
    
      Const rhCurve = 4
    
      ' Pick the cutting curve
      Dim cutter : cutter = Rhino.GetObject("Select cutting curve", rhCurve)
      If IsNull(cutter) Then Exit Sub
    
      ' Pick the curve to trim    
      Dim curve : curve = Rhino.GetCurveObject("Select curve to trim")
      If IsNull(curve) Then Exit Sub
    
      ' Calculate the intersection of the two curves      
      Dim ccx : ccx = Rhino.CurveCurveIntersection(curve(0), cutter)
      If IsNull(ccx) Then
        Rhino.Print "Curves do not intersect."
        Exit Sub
      End If
    
      Dim trim_t : trim_t = ccx(0, 5)             ' intersection parameter
      Dim pick_t : pick_t = curve(4)              ' pick parameter
      Dim domain : domain = CurveDomain(curve(0)) ' curve domain
    
      ' TrimCurve's interval argument defines what to keep.
      ' So, figure out what side of the curve to keep.
      Dim interval
      If (trim_t < pick_t) Then
        interval = Array(domain(0), trim_t)
      Else
        interval = Array(trim_t, domain(1))
      End If
    
      ' Trim the curve
      Rhino.TrimCurve curve(0), interval
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/trimming-
curves/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/trimming-
curves/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

