---
url: https://developer.rhino3d.com/guides/cpp/picking-text-dots/
scraped_at: 2025-09-08T15:39:14.498846
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

[Picking Text Dots](https://developer.rhino3d.com/guides/cpp/picking-text-
dots/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Picking Text Dots

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you would like to allow the user to interactively select text dot
objects from my plugin command. The first place you might look is the
`CRhinoGetObject` class, for a text dot geometry filter. This does not exist.
So, how to go about this?

## Solution

If `CRhinoGetObject` does not have filters to select what you want, then
simply derive a new class from `CRhinoGetObject` and override the
`CustomGeometryFilter` virtual function. From within this function, simply
return true if the object meets your selection criteria.

## Sample

The following example code demonstrates how to derive a new class from
`CRhinoGetObject` and override the `CustomGeometryFilter` virtual function in
order to allow for selection of just text dot objects. That is, those objects
whose geometry member is `ON_TextDot`…

    
    
    class CGetTextDotObject : public CRhinoGetObject
    {
      bool CustomGeometryFilter(
    const CRhinoObject* object,
    const ON_Geometry* geometry,
    ON_COMPONENT_INDEX component_index
    ) const;
    };
    
    bool CGetTextDotObject::CustomGeometryFilter(
        const CRhinoObject* object,
        const ON_Geometry* geometry,
        ON_COMPONENT_INDEX component_index
        ) const
    {
      bool rc = false;
      if( geometry )
      {
        const ON_TextDot* p = ON_TextDot::Cast( geometry );
        if( p )
          rc = true;
      }
      return rc;
    }
    

The following example code demonstrates how you can use the new class…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CGetTextDotObject go;
      go.SetCommandPrompt( L"Select text dots" );
      go.GetObjects( 1, 0 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const int object_count = go.ObjectCount();
      int i;
      for( i = 0; i < object_count; i++ )
      {
        const ON_TextDot* p = ON_TextDot::Cast( go.Object(i).Geometry() );
        if( p )
        {
          ON_wString sPoint;
          RhinoFormatPoint( p->m_point, sPoint );
          RhinoApp().Print( L"TextDot%d: point = (%s), text = \"%s\"\n",
      i, sPoint, p->m_text );
        }
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/picking-
text-dots/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/picking-
text-dots/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

