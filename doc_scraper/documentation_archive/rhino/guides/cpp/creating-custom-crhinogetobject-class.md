---
url: https://developer.rhino3d.com/guides/cpp/creating-custom-crhinogetobject-class/
scraped_at: 2025-09-08T15:39:39.608900
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

[Creating a Custom CRhinoGetObject
Class](https://developer.rhino3d.com/guides/cpp/creating-custom-
crhinogetobject-class/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating a Custom CRhinoGetObject Class

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The `CRhinoGetObject` class that is used for interactively picking one or more
objects is a large, full-featured class (see _rhinoSdkGetObject.h_ for
details). But, on occasion, the class does not offer enough options. For
example, `CRhinoGetObject` is capable of picking curve objects. But, it is not
capable of picking polyline curve objects that are closed. When the required
object filtering exceeds the capabilities of the base class, it’s time to
derive your own.

`CRhinoGetObject` has a virtual function named `CustomGeometryFilter()` that
is called after all obvious geometry filter checks have been performed. Thus,
if you derive a new class from `CRhinoGetObject` and override this virtual
member, you can filter for most any geometric object or property.

## Sample

The following example code demonstrates deriving from `CRhinoGetObject`. In
this example, we want to allow the user to only select closed polylines…

    
    
    class CRhGetClosedPolylineObject : public CRhinoGetObject
    {
    public:
      bool CustomGeometryFilter(
            const CRhinoObject* obj,
            const ON_Geometry* geom,
            RHINO_COMPONENT_INDEX idx
            ) const;
    };
    
    bool CRhGetClosedPolylineObject::CustomGeometryFilter(
            const CRhinoObject* obj,
            const ON_Geometry* geom,
            RHINO_COMPONENT_INDEX idx
            ) const
    {
      if( geom )
      {
        // is it a polyline?
        if( const ON_PolylineCurve* p = ON_PolylineCurve::Cast(geom) )
        {
          if( p->IsClosed() && p->IsPolyline() > 3 )
            return true;
        }
        // is is a polycurve that looks like a polyline?
        if( const ON_PolyCurve* p = ON_PolyCurve::Cast(geom) )
        {
          if( p->IsClosed() && p->IsPolyline() > 3 )
            return true;
        }
        // is it a [[rhino:nurbs|NURBs]] curve that looks like a polyline?
        if( const ON_Curve* p = ON_Curve::Cast(geom) )
        {
          ON_NurbsCurve n;
          if( p->GetNurbForm(n) )
          {
            if( n.IsClosed() && n.IsPolyline() > 3 )
              return true;
          }
        }
      }
      return false;
    }
    

We can use the above class as follows:

    
    
    CRhGetClosedPolylineObject go;
    go.SetCommandPrompt( L"Select closed polyline" );
    go.SetGeometryFilter( CRhinoGetObject::curve_object );
    go.GetObjects( 1, 1 );
    if( go.CommandResult() == CRhinoCommand::success )
    {
      // TODO...
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
custom-crhinogetobject-class/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
custom-crhinogetobject-class/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

