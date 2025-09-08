---
url: https://developer.rhino3d.com/guides/cpp/selecting-objects/
scraped_at: 2025-09-08T15:39:20.519859
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

[Selecting Objects](https://developer.rhino3d.com/guides/cpp/selecting-
objects/)

  * Overview
  * Samples

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Selecting Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

The Rhino C/C++ SDK provides the class `CRhinoGetObject` that will let you
interactively select objects on the screen. This is a large class with many
options. We recommend that you read through the header file,
_rhinoSdkGetObject.h_ , before using.

To use the `CRhinoGetObject` class, put one on the stack and call its
`GetObjects()` member. It is possible to derive custom classes from
`CRhinoGetObject`. But, the class is powerful enough that deriving new classes
from it is usually unnecessary.

If an instance of `CRhinoGetObject` was successful in selecting one or more
objects, then use its `Object()` member to retrieve information about the
selected object. The `Object()` member returns a `CRhinoObjRef` class which
has several member functions to help you quickly get to the information you
are looking for.

## Samples

This sample selects a single object…

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select object" );
    CRhinoGet::result res = go.GetObjects( 1, 1 );
    if( res == CRhinoGet::object )
    {
      const CRhinoObjRef& obj_ref = go.Object( 0 );
      const CRhinoObject* obj = obj_ref.Object();
      if( obj )
      {
        // TODO
      }
    }
    

This sample selects one or more objects…

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select objects" );
    CRhinoGet::result res = go.GetObjects( 1, 0 );
    if( res == CRhinoGet::object )
    {
      int i, count = go.ObjectCount();
      for( i = 0; i < count; i++ )
      {
        const CRhinoObjRef& obj_ref = go.Object( 0 );
        const CRhinoObject* obj = obj_ref.Object();
        if( obj )
        {
          // TODO
        }
      }
    }
    

This sample selects a single curve object…

    
    
    CRhinoGetObject go;
    go.SetCommandPrompt( L"Select curve" );
    go.SetGeometryFilter( CRhinoGetObject::curve_object );
    CRhinoGet::result res = go.GetObjects( 1, 1 );
    if( res == CRhinoGet::object )
    {
      const CRhinoObjRef& obj_ref = go.Object( 0 );
      const ON_Curve* crv = obj_ref.Curve();
      if( crv )
      {
        // TODO
      }
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/selecting-
objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/selecting-
objects/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

