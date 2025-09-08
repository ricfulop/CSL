---
url: https://developer.rhino3d.com/samples/cpp/add-text/
scraped_at: 2025-09-08T15:47:20.051525
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

Add Text

__

Windows only

Demonstrates how to use ON_TextEntity2 to add text to Rhino.

C/C++

    
    
    bool AddAnnotationText(
          CRhinoDoc& doc,       // reference to active document
          const ON_3dPoint& pt, // location of anotation text
          const wchar_t* text,  // the text
          double height,        // height of text item
          const wchar_t* font,  // font or face name
          int style             // style 0=normal, 1=bold,
          )                     //       2=italic, 3=bold and italic
    {
      bool rc = false;
    
      ON_wString wText( text );
      if( wText.IsEmpty() )
        return rc;
    
      if( height <= 0 )
        height = 1.0;
    
      ON_wString wFont( font );
      if( wFont.IsEmpty() )
        wFont = L"Arial";
    
      if( style < 0 | style > 3 )
        style = 0;
    
      ON_Plane plane = RhinoActiveCPlane();
      plane.SetOrigin( pt );
    
      ON_TextEntity2* text_entity = new ON_TextEntity2;
      CRhinoAnnotationText* text_object = new CRhinoAnnotationText;
      text_object->SetAnnotation( text_entity );
      text_object->SetTextHeight( height );
      text_object->SetString( wText );
      text_object->SetPlane( plane );
      int idx = doc.m_font_table.FindOrCreateFont( wFont, style & 1, style & 2 );
      text_object->SetFontIndex( idx );
    
      if( doc.AddObject(text_object) )
      {
        rc = true;
        doc.Redraw();
      }
      else
      {
        delete text_object;
        text_object = 0;
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

