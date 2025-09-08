---
url: https://developer.rhino3d.com/guides/cpp/getting-units-of-active-document/
scraped_at: 2025-09-08T15:39:02.503990
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

[Getting the Units of the Active
Document](https://developer.rhino3d.com/guides/cpp/getting-units-of-active-
document/)

  * Overview
  * More information

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Getting the Units of the Active Document

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Tuesday,
March 12, 2019)

## Overview

There are two unit systems associated with a document, model and page units.
The `ON_UnitSystem` class makes it easy to work with custom units. The Rhino
document class contains two functions to return these unit systems:

  1. `const ON_UnitSystem& CRhinoDoc::ModelUnits() const;`
  2. `const ON_UnitSystem& CRhinoDoc::PageUnits() const;`

## More information

The unit system of the active document is stored on an
`ON_3dmUnitsAndTolerances` class that is located on the `CRhinoDoc` object.

If you inside of a `CRhinoCommand`-derived object’s `RunCommand()` member, you
can get the current units system as follows:

    
    
    const CRhinoDocProperties& doc_props = context.m_doc.Properties();
    const ON_3dmUnitsAndTolerances& units_tolerances = doc_props.ModelUnitsAndTolerances();
    ON::LengthUnitSystem units_system = units_tolerances.m_unit_system;
    

As a shortcut, you can do the following:

    
    
    ON::LengthUnitSystem units_system = context.m_doc.UnitSystem();
    

If you outside of a `CRhinoCommand`-derived object’s `RunCommand()` member,
you can get the current units system as follows:

    
    
    CRhinoDoc* doc = RhinoApp().ActiveDoc();
    if (nullptr != doc)
    {
      ON::LengthUnitSystem units_system = doc->UnitSystem();
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/getting-
units-of-active-document/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/getting-
units-of-active-document/index.md) [
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

