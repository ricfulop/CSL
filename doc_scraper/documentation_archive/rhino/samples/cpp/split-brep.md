---
url: https://developer.rhino3d.com/samples/cpp/split-brep/
scraped_at: 2025-09-08T15:48:43.877803
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

Split Brep

__

Windows only

Demonstrates how to split a brep with another brep using the RhinoSplitBrep
function.

C/C++

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Pick the brep to split
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select surface or polysuface to split" );
      go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoObjRef& split_ref = go.Object(0);
    
      const CRhinoObject* split_object = split_ref.Object();
      if( !split_object )
        return failure;
    
      const ON_Brep* split = split_ref.Brep();
      if( !split )
        return failure;
    
      // Pick the cutting brep
      go.SetCommandPrompt( L"Select cutting surface or polysuface" );
      go.EnablePreSelect( FALSE );
      go.EnableDeselectAllBeforePostSelect( FALSE );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const ON_Brep* cutter = go.Object(0).Brep();
      if( !cutter )
        return failure;
    
      ON_SimpleArray<ON_Brep*> pieces;
      double tol = context.m_doc.AbsoluteTolerance();
    
      // Try splitting the brep
      if( !RhinoBrepSplit(*split, *cutter, tol, pieces) )
        RhinoApp().Print( L"Unable to split brep.\n" );
    
      int i, count = pieces.Count();
      if( count == 0 | count == 1 )
      {
        if( count == 1 )
          delete pieces[0];
        return nothing;
      }
    
      CRhinoObjectAttributes attrib = split_object->Attributes();
      attrib.m_uuid = ON_nil_uuid;
    
      const CRhinoObjectVisualAnalysisMode* vam_list = split_object->m_analysis_mode_list;
    
      for( i = 0; i < count; i++ )
      {
        CRhinoBrepObject* brep_object = new CRhinoBrepObject( attrib );
        if( brep_object )
        {
          brep_object->SetBrep( pieces[i] );
          if( context.m_doc.AddObject(brep_object) )
            RhinoCopyAnalysisModes( vam_list, brep_object );
          else
            delete brep_object;
        }
      }
    
      context.m_doc.DeleteObject( split_ref );
      context.m_doc.Redraw();
    
      return success;
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

