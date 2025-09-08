---
url: https://developer.rhino3d.com/guides/cpp/archiving-curves-to-a-file/
scraped_at: 2025-09-08T15:38:45.361866
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

[Archiving Curves to a
File](https://developer.rhino3d.com/guides/cpp/archiving-curves-to-a-file/)

  * Problem
  * Solution
    * Write
    * Read
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Archiving Curves to a File

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Writing curves to a file has some special considerations. Curves come in many
variations: the curve could be a circle, simple curve, or a polycurve. You
cannot know in advance what the user will be selecting. As such, the class
containing my data declares it as an `ON_Curve`.

Writing the data is not an issue. You simply call `ON_Curve::Write`. However,
things don’t go so well when you try to read the data. You need a way to
simply read curve data without going to a non-abstract class. What is needed
is a way to read/write curve data that represents any kind of curve possible.

## Solution

It is probably best not to call `ON_Curve::Write` for this very reason. When
serializing anything derived from `ON_Object`, just use
`ON_BinaryArchive::WriteObject` and `ON_BinaryArchive::ReadObject`…

### Write

    
    
    static bool WriteCurveFile(FILE* fp, const ON_Curve* curve)
    {
      if (nullptr == fp || nullptr == curve)
        return false;
    
      ON_BinaryFile archive(ON::archive_mode::write3dm, fp);
    
      int major_version = 1;
      int minor_version = 0;
      bool rc = archive.BeginWrite3dmChunk(TCODE_ANONYMOUS_CHUNK, major_version, minor_version);
      if (!rc)
        return false;
    
      for (;;)
      {
        // version 1.0 fields
        rc = (archive.WriteObject(curve) ? true : false);
        if (!rc) break;
    
        // todo...
    
        break;
      }
    
      if (!archive.EndWrite3dmChunk())
        rc = false;
    
      return rc;
    }
    

### Read

    
    
    static bool ReadCurveFile(FILE* fp, ON_Curve*& curve)
    {
      if (nullptr == fp)
        return false;
    
      ON_BinaryFile archive(ON::archive_mode::read3dm, fp);
    
      int major_version = 0;
      int minor_version = 0;
      bool rc = archive.BeginRead3dmChunk(TCODE_ANONYMOUS_CHUNK, &major_version, &minor_version);
      if (!rc)
        return false;
    
      for (;;)
      {
        rc = (1 == major_version);
        if (!rc) break;
    
        // version 1.0 fields
        ON_Object* object = 0;
        rc = (archive.ReadObject(&object) ? true : false);
        if (!rc) break;
    
        curve = ON_Curve::Cast(object);
    
        // todo...
    
        break;
      }
    
      if (!archive.EndRead3dmChunk())
        rc = false;
    
      return (rc && curve);
    }
    

## Sample

To use the above functions, you could do the following:

    
    
    bool rc = false;
    
    FILE* fp = ON::OpenFile(filename, L"wb");
    if (fp)
    {
      rc = WriteCurveFile(fp, curve);
      ON::CloseFile(fp);
    }
    
    if (rc)
      RhinoApp().Print(L"Successfully wrote %s.\n", filename);
    else
      RhinoApp().Print(L"Errors while writing %s.\n", filename);
    

and

    
    
    bool rc = false;
    ON_Curve* curve = nullptr;
    
    FILE* fp = ON::OpenFile(filename, L"rb");
    if (fp)
    {
      rc = ReadCurveFile(fp, curve);
      ON::CloseFile(fp);
    }
    
    if (rc)
    {
      CRhinoCurveObject* curve_object = new CRhinoCurveObject();
      curve_object->SetCurve(curve);
      context.m_doc.AddObject(curve_object);
      context.m_doc.Redraw();
    }
    else
    {
      RhinoApp().Print(L"Errors while reading %s.\n", filename);
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/archiving-
curves-to-a-file/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/archiving-
curves-to-a-file/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

