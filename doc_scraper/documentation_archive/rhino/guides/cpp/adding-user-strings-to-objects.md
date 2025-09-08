---
url: https://developer.rhino3d.com/guides/cpp/adding-user-strings-to-objects/
scraped_at: 2025-09-08T15:38:41.340231
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

[Adding User Strings to
Objects](https://developer.rhino3d.com/guides/cpp/adding-user-strings-to-
objects/)

  * Overview
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding User Strings to Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

User Data is a powerful set of APIs that allow plugin developers to attach
custom data of any kind to any object derived from `ON_Object`. In order to
take advantage of User Data, you are required to implement your own user data
object by deriving a class from `ON_UserData` and overriding the required
virtual functions.

In Rhino, the SDK adds a new standardized approach for adding User Data to
objects called User Strings. The Rhino C/C++ SDK allows you to quickly
attaches User Data in the form of a key-value string pair to any object
derived from `ON_Object`. This feature is exposed to the C/C++ SDK as member
functions on `ON_Object`:

  * `ON_Object::SetUserString`: attaches a user string to an object. This information will persist through copy construction, operator=, and file IO.
  * `ON_Object::GetUserString`: gets a user string from an object.
  * `ON_Object::GetUserStringKeys`: retrieves a list of all user string keys on an object.
  * `ON_Object::GetUserStrings`: retrieves a list of all user strings on an object.

There are a number of advantages to User Strings:

  * The mechanism is very simple - you do not have to derive any new classes.
  * Rhino is responsible for all of the file IO.
  * User Strings can hold text of any length and format, including XML.
  * Since the mechanism is standard, user strings can shared between Rhino and other plugins. For example, you can use Rhino’s _GetUserText_ and _SetUserText_ commands to get and set user strings.

## Example

The following example demonstrates how to add User Strings to a selected
object…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      bool bAttribute = true;
    
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select object to attach user text" );
      go.AddCommandOptionToggle(
            RHCMDOPTNAME(L"Location"),
            RHCMDOPTVALUE(L"Object"),
            RHCMDOPTVALUE(L"Attribute"),
            bAttribute,
            &bAttribute
            );
    
      for(;;)
      {
        CRhinoGet::result res = go.GetObjects( 1, 1 );
        if( res == CRhinoGet::option )
          continue;
        if( res != CRhinoGet::object )
          return cancel;
        break;
      }
    
      const CRhinoObjRef& ref = go.Object(0);
      const CRhinoObject* obj = ref.Object();
      if( !obj )
        return failure;
    
      ON_wString key = L"test";
      ON_wString text = L"sample text";
    
      if( bAttribute )
      {
        // Attach user string to object's attributes
        CRhinoObjectAttributes attribs = obj->Attributes();
        attribs.SetUserString( key, text );
        context.m_doc.ModifyObjectAttributes( ref, attribs );
      }
      else
      {
        // Attach user string to object's geometry
        CRhinoObject* dupe = obj->DuplicateRhinoObject();
        if( dupe )
        {
          ON_Geometry* geom = const_cast<ON_Geometry*>( dupe->Geometry() );
          if( geom )
          {
            geom->SetUserString( key, text );
            context.m_doc.ReplaceObject( ref, dupe );
          }
        }
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
user-strings-to-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
user-strings-to-objects/index.md) [
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

