---
url: https://developer.rhino3d.com/guides/cpp/showing-objects-transforming-dynamically/
scraped_at: 2025-09-08T15:40:13.765014
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

[Showing Objects Transforming
Dynamically](https://developer.rhino3d.com/guides/cpp/showing-objects-
transforming-dynamically/)

  * Overview
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Showing Objects Transforming Dynamically

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The `CRhinoViewport` class has two member functions, `GetModelXform()` and
`SetModelXform()`, that either retrieve or modify the model transformation
matrix that is applied to objects before they are drawn. The model
transformation matrix is intended to be used for dynamic drawing of objects.
Note, the default model transformation matrix is the identity.

Some of the Rhino command that use this technique to dynamically draw
transforming objects include the _Move_ , _Copy_ , _Scale_ , and _Rotate_
commands. These commands derive new `CRhinoGetPoint` classes and override the
virtual `DynamicDraw()` member function to draw objects dynamically as the
mouse moves during a point picking operation.

## Sample

The following is an sample `CRhinoGetPoint`-derived class that demonstrates
how to dynamically draw transforming objects during a point picking operation.
In this sample, the transformation is a simple translation, like used in the
_Move_ command.

First, the class declaration…

    
    
    ////////////////////////////////////////////////////////////////////
    // CRhinoGetTranslationPoint declaration
    
    class CRhinoGetTranslationPoint : public CRhinoGetPoint
    {
    public:
    
      CRhinoGetTranslationPoint();
      ~CRhinoGetTranslationPoint() {}
    
      // CRhinoGetPoint overrides  
      void SetBasePoint( ON_3dPoint base_point, BOOL bShowDistanceInStatusBar = false );
      void OnMouseMove( CRhinoViewport& vp, UINT flags, const ON_3dPoint& pt, const CPoint* p );
      void DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt );
    
      // Additional helpers
      void AddObject( const CRhinoObject* object );
      void CalculateTranslation( const ON_3dPoint& pt, ON_Xform& xform );
    
    private:
      ON_3dPoint m_start_point; // starting point of translation
      ON_Xform m_xform; // transformation matrix
      ON_SimpleArray<const CRhinoObject*> m_objects; //objects to transform
    };
    
    ////////////////////////////////////////////////////////////////////
    // CRhinoGetTranslationPoint definition
    
    CRhinoGetTranslationPoint::CRhinoGetTranslationPoint()
    {
      m_xform.Identity();
    }
    
    void CRhinoGetTranslationPoint::AddObject( const CRhinoObject* object )
    {
      m_objects.Append( object );
    }
    
    void CRhinoGetTranslationPoint::SetBasePoint(
          ON_3dPoint base_point,
          BOOL bShowDistanceInStatusBar
          )
    {
      m_start_point = base_point;
      CRhinoGetPoint::SetBasePoint( base_point, bShowDistanceInStatusBar );
    }
    
    void CRhinoGetTranslationPoint::CalculateTranslation(
          const ON_3dPoint& pt,
          ON_Xform& xform
          )
    {
      ON_3dVector v = pt - m_start_point;
      if( v.IsTiny() )
        xform.Identity();
      else
        xform.Translation( v );
    }
    
    void CRhinoGetTranslationPoint::OnMouseMove(
         CRhinoViewport& vp,
         UINT flags,
         const ON_3dPoint& pt,
         const CPoint* p
         )
    {
      // Everytime the mouse moves, calculate the translation
      CalculateTranslation( pt, m_xform );
      CRhinoGetPoint::OnMouseMove( vp, flags, pt, p );
    }
    
    void CRhinoGetTranslationPoint::DynamicDraw(
         HDC hdc,
         CRhinoViewport& vp,
         const ON_3dPoint& pt
         )
    {
      // Time to draw our objects dynamically
      int i, count = m_objects.Count();
      if( m_xform.IsIdentity() == false && count > 0 )
      {
        ON_Color saved_color = vp.DrawColor();
        ON_Xform saved_model_xform;
        // Save the current model transformation, we will
        // need to restore it later
        vp.GetModelXform( saved_model_xform );
        // Set the model transformation to ours
        vp.SetModelXform( m_xform );
        // Draw all of the objects in our array
        for( i = 0; i < m_objects.Count(); i++ )
        {
          const CRhinoObject* object = m_objects[i];
          if( object == 0 )
            continue;
          vp.SetDrawColor( object->ObjectDrawColor(TRUE) );
          object->Draw( vp );
          if( vp.InterruptDrawing() )
            break;
        }
        // Reset modified viewport members
        vp.SetModelXform( saved_model_xform );
        vp.SetDrawColor( saved_color );
      }
    
      // Let the base class do its drawing too
      CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/showing-
objects-transforming-dynamically/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/showing-
objects-transforming-dynamically/index.md) [
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

