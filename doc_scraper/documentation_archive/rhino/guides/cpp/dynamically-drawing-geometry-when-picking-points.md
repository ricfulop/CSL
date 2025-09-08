---
url: https://developer.rhino3d.com/guides/cpp/dynamically-drawing-geometry-when-picking-points/
scraped_at: 2025-09-08T15:39:47.676943
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

[Dynamically Drawing Geometry when Picking
Points](https://developer.rhino3d.com/guides/cpp/dynamically-drawing-geometry-
when-picking-points/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Dynamically Drawing Geometry when Picking Points

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

When using Rhino, you have probably noticed that many of the object creation
commands, such as _Line_ and _Circle_ , and transformation commands, such as
_Move_ and _Copy_ , dynamically draw objects as they are being created or
transformed. This operation is performed by deriving a new class from Rhino’s
point pick class, `CRhinoGetPoint`, and overriding two member functions:
`OnMouseMove()` and `DynamicDraw()`.

`OnMouseMove()` is called every time the mouse moves. This is a great place to
perform calculations, such as transformations.

`DynamicDraw()` is called as the mouse moves, as well. Every time the mouse
moves, `DynamicDraw()` will be called once per viewport.

**NOTE** : Rhino calls `DynamicDraw()` happen after the call to
`OnMouseMove()`.

## Sample

The following sample demonstrates how to derive a new class from
`CRhinoGetPoint` and override `OnMouseMove()` and `DynamicDraw()` to
dynamically draw geometry. In this sample, we are going to dynamically draw a
circle while the user is specifying its radius.

    
    
    class CGetCircleRadiusPoint : public CRhinoGetPoint
    {
    public:
      CGetCircleRadiusPoint();
      void SetCenterPoint( const ON_3dPoint center_point );
      bool CalculateCircle( CRhinoViewport& vp, const ON_3dPoint& pt );
    
      void OnMouseMove( CRhinoViewport& vp,
                        UINT flags,
                        const ON_3dPoint& pt,
                        const CPoint* pt2d );
    
      void DynamicDraw( HDC hDC, CRhinoViewport& vp, const ON_3dPoint& pt );
      const ON_Circle& Circle() const;
    private:
      ON_Circle m_circle;
      ON_3dPoint m_center_point;
      bool m_draw_circle;
    };
    
    CGetCircleRadiusPoint::CGetCircleRadiusPoint()
    {
      m_draw_circle = false;
    }
    
    void CGetCircleRadiusPoint::SetCenterPoint( const ON_3dPoint center_point )
    {
      m_center_point = center_point;
    }
    
    bool CGetCircleRadiusPoint::CalculateCircle( CRhinoViewport& vp, const ON_3dPoint& pt )
    {
      double radius = m_center_point.DistanceTo( pt );
      if( radius < ON_SQRT_EPSILON )
        return false;
    
      ON_Plane plane = vp.ConstructionPlane().m_plane;
      plane.SetOrigin( m_center_point );
      m_circle.Create( plane, radius );
      return m_circle.IsValid() ? true : false;
    }
    
    void CGetCircleRadiusPoint::OnMouseMove( CRhinoViewport& vp,
                                             UINT flags,
                                             const ON_3dPoint& pt,
                                             const CPoint* pt2d )
    {
      m_draw_circle = CalculateCircle( vp, pt );
      CRhinoGetPoint::OnMouseMove( vp, flags, pt, pt2d );
    }
    
    void CGetCircleRadiusPoint::DynamicDraw( HDC hDC,
                                             CRhinoViewport& vp,
                                             const ON_3dPoint& pt )
    {
      if( m_draw_circle )
      {
        ON_Color color = RhinoApp().AppSettings().TrackingColor();
        ON_Color saved_color = vp.SetDrawColor( color );
        vp.DrawCircle( m_circle );
        vp.SetDrawColor( saved_color );
      }
      CRhinoGetPoint::DynamicDraw( hDC, vp, pt );
    }
    const ON_Circle& CGetCircleRadiusPoint::Circle() const
    {
      return m_circle;
    }
    

Finally, here is our `CRhinoGetPoint` derived class in action:

    
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Center point" );
      gp.ConstrainToConstructionPlane( FALSE );
      gp.GetPoint();
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      ON_3dPoint center_point = gp.Point();
    
      CGetCircleRadiusPoint gc;
      gc.SetCommandPrompt( L"Radius" );
      gc.ConstrainToConstructionPlane( FALSE );
      gc.SetBasePoint( center_point );
      gc.DrawLineFromPoint( center_point, TRUE );
      gc.SetCenterPoint( center_point );
      gc.GetPoint();
      if( gc.CommandResult() != CRhinoCommand::success )
        return gc.CommandResult();
    
      if( gc.CalculateCircle( gc.View()->Viewport(), gc.Point() ))
      {
        ON_Circle circle = gc.Circle();
        context.m_doc.AddCurveObject( circle );
        context.m_doc.Redraw();
      }
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/dynamically-
drawing-geometry-when-picking-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/dynamically-
drawing-geometry-when-picking-points/index.md) [
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

