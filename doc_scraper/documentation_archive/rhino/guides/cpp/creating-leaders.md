---
url: https://developer.rhino3d.com/guides/cpp/creating-leaders/
scraped_at: 2025-09-08T15:38:51.632131
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

[Creating Leaders](https://developer.rhino3d.com/guides/cpp/creating-leaders/)

  * How To

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating Leaders

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## How To

Leaders in Rhino are defined by the `ON_Leader2` class. To construct a leader,
you must provide:

  1. A plane, or an `ON_Plane` object, which defines the plane in which the leader will be located.
  2. Two or more 2D points that line in the plane that you specified above.

In the following sample code, we will construct a simple leader object. The
leader will reside in the world x-y plane and will have four points…

    
    
    CRhinoCommand::result CCommandLeader::RunCommand( const CRhinoCommandContext& context )
    {
      // Some set of points that define the leader
      ON_3dPointArray points;
      points.Append( ON_3dPoint(1.0, 1.0, 0.0) );
      points.Append( ON_3dPoint(5.0, 1.0, 0.0) );
      points.Append( ON_3dPoint(5.0, 5.0, 0.0) );
      points.Append( ON_3dPoint(9.0, 5.0, 0.0) );
    
      // The plane in which the leader resides
      ON_Plane plane = ON_xy_plane;
    
      // Create the leader
      ON_Leader2 leader;
      leader.SetPlane( plane );
    
      // Add the points to the leader
      int i;
      for( i = 0; i < points.Count(); i++ )
      {
        // Make sure the points are on the plane
        ON_2dPoint p2;
        if( leader.m_plane.ClosestPointTo(points[i], &p2.x, &p2.y) )
        {
          if( leader.m_points.Count() < 1 | p2.DistanceTo(*leader.m_points.Last()) > ON_SQRT_EPSILON )
            leader.m_points.Append( p2 );
        }
      }
    
      // Create the leader object
      CRhinoAnnotationLeader* leader_object = new CRhinoAnnotationLeader();
      // Add our leader to the object
      leader_object->SetAnnotation( leader );
    
      if( context.m_doc.AddObject(leader_object) )
        context.m_doc.Redraw();
      else
        delete leader_object; // error
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
leaders/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
leaders/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

