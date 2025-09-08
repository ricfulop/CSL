---
url: https://developer.rhino3d.com/guides/cpp/calculating-angle-between-two-points/
scraped_at: 2025-09-08T15:38:47.400447
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

[Calculating the Angle Between Two
Points](https://developer.rhino3d.com/guides/cpp/calculating-angle-between-
two-points/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Calculating the Angle Between Two Points

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

For two sets of 3D vectors, you can use the method demonstrated in [Calculate
the Angle Between Two Vectors
](https://developer.rhino3d.com/samples/cpp/calculate-the-angle-between-two-
vectors/) to calculate the angle between them. The results for both are always
the same - 45 degree in this case. For example:

![Angle between vectors](https://developer.rhino3d.com/images/calculating-
angle-between-two-points-01.png)

But what if you need a result in which one is 45 degrees the other is 315
degrees?

## Solution

The following example code demonstrates how to calculate the angle between two
3D points, given a common base point.

    
    
    /*
    Description:
      Calculates the angle between two points that lie on a
      given plane.
    Parameters:
      plane   - [in]  The plane on which the points lie
      basept  - [in]  The base point
      refpt1  - [in]  The first reference point
      refpt2  - [in]  The second reference point
      radians - [out] The angle in radians
    Returns:
      TRUE if successful, FALSE otherwise.
    */
    static bool CalculatePlaneAngle(
            const ON_Plane& plane,
            const ON_3dPoint& basept,
            const ON_3dPoint& refpt1,
            const ON_3dPoint& refpt2,
            double& radians
            )
    {
      // Make sure the points are on the plane
      double tolerance = 0.000001;
      double dist = 0.0;
    
      dist = plane.plane_equation.ValueAt( basept );  
      if( fabs(dist) > tolerance )
        return false;
    
      dist = plane.plane_equation.ValueAt( refpt1 );
      if( fabs(dist) > tolerance )
        return false;
    
      dist = plane.plane_equation.ValueAt( refpt2 );
      if( fabs(dist) > tolerance )
        return false;
    
      // Make sure base and reference points are not equal
    
      if( basept == refpt1 | basept == refpt2 )
        return false;
    
      // Calculate angle between vectors
    
      ON_3dVector v = refpt2 - basept;
      v.Unitize();
    
      ON_3dVector zerov = refpt1 - basept;
      zerov.Unitize();  
    
      double dot = ON_DotProduct( zerov, v );
      dot = RHINO_CLAMP( dot, -1.0, 1.0 );
      double angle = acos( dot );
    
      // Calculate a new y-axis based on the plane's
      // zaxis and our zero vector
      v = ON_CrossProduct( plane.zaxis, zerov );
      v.Unitize();
    
      // Create a plane using our y-axis a the normal
      ON_Plane yplane;
      yplane.CreateFromNormal( basept, v );
    
      // Figure out which side of this plane that refpt2 is on
      dist = yplane.plane_equation.ValueAt( refpt2 );
      if( dist < 0.0 )
        angle = (ON_PI * 2.0) - angle;
    
      radians = angle;
    
      return true;
    }
    

You can use the above function as follows…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoView* view = RhinoApp().ActiveView();
      if( 0 == view )
        return failure;
    
      ON_Plane plane = view->ActiveViewport().ConstructionPlane().m_plane;
      ON_3dPoint basept, refpt1, refpt2;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Base point" );
      gp.Constrain( plane );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      basept = gp.Point();
    
      gp.SetCommandPrompt( L"First angle point" );
      gp.SetBasePoint( basept );
      gp.DrawLineFromPoint( basept, TRUE );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      refpt1 = gp.Point();
    
      gp.SetCommandPrompt( L"Second angle point" );
      gp.SetBasePoint( basept );
      gp.DrawLineFromPoint( basept, TRUE );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      refpt2 = gp.Point();
    
      double angle = 0.0;
      if( CalculatePlaneAngle(plane, basept, refpt1, refpt2, angle) )
        RhinoApp().Print( L"Angle = %.3f degrees.\n", angle * (180.0 / ON_PI) );
    
      return success;
    }
    

## Related Topics

  * [Calculate the Angle Between Two Vectors (Sample)](https://developer.rhino3d.com/samples/cpp/calculate-the-angle-between-two-vectors/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/calculating-
angle-between-two-points/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/calculating-
angle-between-two-points/index.md) [
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

