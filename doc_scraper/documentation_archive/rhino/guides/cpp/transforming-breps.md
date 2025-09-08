---
url: https://developer.rhino3d.com/guides/cpp/transforming-breps/
scraped_at: 2025-09-08T15:39:22.549977
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

[Transforming Breps](https://developer.rhino3d.com/guides/cpp/transforming-
breps/)

  * Samples
    * The Short Way
    * The Long Way

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Transforming Breps

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Samples

### The Short Way

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select brep" );
      go.SetGeometryFilter( ON::brep_object );
      go.GetObjects(1,1);
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      CRhinoObjRef ref = go.Object(0);
    
      // Simple translation transformation
      ON_Xform xform;
      xform.Translation( ON_3dVector(18,-18,-25) );
    
      context.m_doc.TransformObject( ref, xform );
      context.m_doc.Redraw();
    
      return success;
    }
    

### The Long Way

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select brep" );
      go.SetGeometryFilter( ON::brep_object );
      go.GetObjects(1,1);
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoObjRef& ref = go.Object(0);
      const CRhinoObject* obj = ref.Object();
      if( !obj )
        return failure;
      const ON_Brep* brep = ref.Brep();
      if( !brep )
        return failure;
      ON_Brep* dupe = brep->Duplicate();
      if( !dupe )
        return failure;
    
      // Simple translation transformation
      ON_Xform xform;
      xform.Translation( ON_3dVector(18,-18,-25) );
    
      if( !dupe->Transform( xform ) )
      {
        RhinoApp().Print( L"Unable to transform object.\n" );
        delete dupe;
        return failure;
      }
    
      ON_3dmObjectAttributes attribs = obj->Attributes();
      context.m_doc.AddBrepObject( *dupe, &attribs );
    
      // Since CRhinoDoc::AddBrepObject() make a copy of the input
      // brep, we are responsible for deleting the original. Otherwise
      // we will leak memory;
      delete dupe;
      // Delete the selected object
      context.m_doc.DeleteObject( ref );
      context.m_doc.Redraw();
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/transforming-
breps/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/transforming-
breps/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

