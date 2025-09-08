---
url: https://developer.rhino3d.com/guides/cpp/picking-point-objects/
scraped_at: 2025-09-08T15:39:12.366752
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

[Picking Point Objects](https://developer.rhino3d.com/guides/cpp/picking-
point-objects/)

  * How To

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Picking Point Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## How To

If you need the user to define a 3D point location, you can use a
`CRhinoGetPoint` object. But, if the points already exist as objects in Rhino,
you will need to use a `CRhinoGetObject` object to pick them. Then, you can
determine the 3D coordinates of that point object, for example:

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select point" );
    go.SetGeometryFilter( CRhinoGetObject::point_object );
    CRhinoGet::result res = go.GetObjects( 1, 1 );
    if( res == CRhinoGet::object )
    {
      const CRhinoObjRef& objref = go.Object(0);
      const ON_Point* pt = objref.Point();
      if( pt )
        RhinoApp().Print(L"Point: %f,%f,%f", pt->point.x, pt->point.y, pt->point.z);
    }
    

If you needed access to the `CRhinoPointObject` object, you could do this:

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select point" );
    go.SetGeometryFilter( CRhinoGetObject::point_object );
    CRhinoGet::result res = go.GetObjects( 1, 1 );
    if( res == CRhinoGet::object )
    {
      const CRhinoObjRef& objref = go.Object(0);
      const CRhinoPointObject* point_object = CRhinoPointObject::Cast( objref.Object() );
      if( point_object )
      {
        const ON_Point& pt = point_object->Point();
        RhinoApp().Print(L"Point: %f,%f,%f", pt.point.x, pt.point.y, pt.point.z);
      }
    }
    

Here is how you can pick one or more point objects:

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select points" );
    go.SetGeometryFilter( CRhinoGetObject::point_object );
    CRhinoGet::result res = go.GetObjects( 1, 0 );
    if( res == CRhinoGet::object )
    {
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const CRhinoObjRef& objref = go.Object(i);
        const ON_Point* point = objref.Point();
        if( point )
          RhinoApp().Print( L"Point %d: %f,%f,%f",
                            i,
                            point->point.x,
                            point->point.y,
                            point->point.z );
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/picking-
point-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/picking-
point-objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

