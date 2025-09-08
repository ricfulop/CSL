---
url: https://developer.rhino3d.com/guides/cpp/brep-data-structure/
scraped_at: 2025-09-08T15:39:29.538342
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

[Brep Data Structure](https://developer.rhino3d.com/guides/cpp/brep-data-
structure/)

  * Conceptual diagram
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Brep Data Structure

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Conceptual diagram

![BRep Data Structure](https://developer.rhino3d.com/images/brep-data-
structure-01.png)

## Sample

    
    
    //Given a brep and a face index
    const ON_Brep* brep;
    const int face_index = 0;
    ON_SimpleArray<int> face_ti_list; //trims indeces list
    ON_SimpleArray<int> face_ei_list; //edges indeces list
    
    //Get the BrepFace of the given index
    const ON_BrepFace* face = brep->Face(face_index);
    if( 0 == face )
      return false;
    
    //Get the loop of the face
    for( int fli = 0; fli < face->LoopCount(); fli++ )
    {
      const ON_BrepLoop* loop = face->Loop( fli );
      if( 0 == loop )
        continue;
    
      for( int lti = 0; lti < loop->TrimCount(); lti++ )
      {
        //Find the trim
        const ON_BrepTrim* trim = loop->Trim( lti );
        if( 0 == trim )
          continue;
        face_ti_list.Append( trim->m_trim_index );
    
        //Find the edge of that trim
        //Each trim has exactly one edge attached to it
        const ON_BrepEdge* edge = trim->Edge();
        if( 0 == edge )
          continue;
        face_ei_list.Append( edge->m_edge_index );
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/brep-
data-structure/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/brep-
data-structure/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

