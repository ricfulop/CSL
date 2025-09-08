---
url: https://developer.rhino3d.com/samples/cpp/add-linear-dimension/
scraped_at: 2025-09-08T15:47:11.019608
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

Add a Linear Dimension

__

Windows only

Demonstrates how to add a linear dimension object.

C/C++

    
    
    // The following is a demonstration of how to interactively add a linear dimension object to Rhino.
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoLinearDimension* pDim = 0;
    
      CArgsRhinoDimLinear args;
      args.SetFirstPointPrompt( L"First dimension point" );
      args.SetSecondPointPrompt( L"Second dimension point" );
      args.SetDragPointPrompt( L"Dimension location" );
      args.SetIsInteractive( context.IsInteractive() ? true : false );
    
      CRhinoCommand::result rc = RhinoGetDimLinear( args, pDim, 0 );
    
      if( rc == success && pDim )
      {
        context.m_doc.AddObject( pDim, FALSE);
        context.m_doc.Redraw();
      }
    
      return rc;
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

