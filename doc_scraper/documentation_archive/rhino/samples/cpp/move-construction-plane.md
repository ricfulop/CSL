---
url: https://developer.rhino3d.com/samples/cpp/move-construction-plane/
scraped_at: 2025-09-08T15:48:37.884387
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

Move a Construction Plane

__

Windows only

Demonstrates how to move the origin of a construction plane.

C/C++

    
    
    class CTestMoveCPlanePoint : public CRhinoGetPoint
    {
    public:
      CTestMoveCPlanePoint( const ON_3dmConstructionPlane& cplane );
      ~CTestMoveCPlanePoint() {}
      void SetConstructionPlane(const ON_3dmConstructionPlane& cplane);
      void OnMouseMove( CRhinoViewport& vp,
                        UINT flags,
                        const ON_3dPoint& pt,
                        const CPoint* pt2d );
      void DynamicDraw( HDC hdc,
                        CRhinoViewport& vp,
                        const ON_3dPoint& pt );
    private:
      ON_3dmConstructionPlane m_cplane;
    };
    
    CTestMoveCPlanePoint::CTestMoveCPlanePoint(const ON_3dmConstructionPlane& cplane)
    : m_cplane(cplane)
    {
    }
    
    void CTestMoveCPlanePoint::OnMouseMove( CRhinoViewport& vp, UINT flags,
                                            const ON_3dPoint& pt, const CPoint* pt2d )
    {
      m_cplane.m_plane.CreateFromFrame( pt, m_cplane.m_plane.xaxis, m_cplane.m_plane.yaxis );
      CRhinoGetPoint::OnMouseMove( vp, flags, pt, pt2d );
    }
    
    void CTestMoveCPlanePoint::DynamicDraw(HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt)
    {
      vp.DrawConstructionPlane( m_cplane, FALSE, TRUE );
      CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
    }
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      CRhinoView* view = ::RhinoApp().ActiveView();
      if( !view )
        return CRhinoCommand::failure;
    
      ON_3dmConstructionPlane cplane = view->Viewport().ConstructionPlane();
      ON_3dPoint origin = cplane.m_plane.origin;
    
      CTestMoveCPlanePoint gp( cplane );
      gp.SetCommandPrompt( L"CPlane origin" );
      gp.SetBasePoint( origin );
      gp.DrawLineFromPoint( origin, TRUE );
      gp.GetPoint();
    
      if( gp.CommandResult() != CRhinoCommand::success )
        return gp.CommandResult();
    
      ON_3dPoint pt = gp.Point();
      ON_3dVector v = origin - pt;
      if( v.IsTiny() )
        return CRhinoCommand::nothing;
    
      cplane.m_plane.CreateFromFrame( pt, cplane.m_plane.xaxis,
                                      cplane.m_plane.yaxis );
      view->Viewport().SetConstructionPlane( cplane );
      view->Redraw();
      return CRhinoCommand::success;
    }
    

  

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

