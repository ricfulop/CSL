---
url: https://developer.rhino3d.com/guides/cpp/creating-points-from-text-objects/
scraped_at: 2025-09-08T15:39:40.589716
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

[Creating Points from Text
Objects](https://developer.rhino3d.com/guides/cpp/creating-points-from-text-
objects/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating Points from Text Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you have many text elements that display numeric values that identify
elevation and you would like to convert these elements to points objects using
the C/C++. The text elements denote the elevations of the locations and you
would like create the 2D point by the location of the text and then use the
number of the text as the z-coordinate.

## Solution

To make picking text entities easier for the user, we will use a custom object
picker that just filters `CRhinoAnnotationText` objects…

    
    
    class CRhGetTextObject : public CRhinoGetObject
    {
    public:
      bool CustomGeometryFilter(
            const CRhinoObject* object,
            const ON_Geometry* geometry,
            ON_COMPONENT_INDEX component_index
            ) const
      {
        if( object && CRhinoAnnotationText::Cast(object) )
          return true;
        return false;
      }
    };
    

Here is the portion of the command that creates points from the text entities…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhGetTextObject go;
      go.SetCommandPrompt( L"Select text" );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
      {
        const CRhinoAnnotationText* text_obj = CRhinoAnnotationText::Cast( go.Object(i).Object() );
        if( 0 == text_obj )
          continue;
    
        ON_wString text_str( text_obj->String() );
        text_str.TrimLeftAndRight();
    
        double z = 0.0;
        if( RhinoParseNumber(text_str, &z) )
        {
          ON_3dPoint text_pt = text_obj->m_text_block.Plane().Origin();
          text_pt.z = z;
          context.m_doc.AddPointObject( text_pt );
        }
      }
    
      context.m_doc.Redraw();
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
points-from-text-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
points-from-text-objects/index.md) [
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

