---
url: https://developer.rhino3d.com/guides/cpp/changing-display-precision/
scraped_at: 2025-09-08T15:39:36.580302
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

[Changing Display
Precision](https://developer.rhino3d.com/guides/cpp/changing-display-
precision/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Changing Display Precision

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Rhino has a document display precision - the “display precision” option found
in the _Units_ page in the _Options_ dialog. Imagine you want to modify this
using C/C++ from your plugin.

## Solution

A document’s display precision, the number of decimal places used for the
distance display, is maintained on an `ON_3dmUnitsAndTolerances` object, which
in turn is stored on a `CRhinoDocProperties` object which is a member of the
current `CRhinoDoc` object. To modify this variable, you will need to:

  1. Make a copy of the document’s `ON_3dmUnitsAndTolerances` object.
  2. Modify the object’s `m_distance_display_precision` member variable.
  3. Replace the current `ON_3dmUnitsAndTolerances` with the newly modified one.

## Sample

The following sample code demonstrates how to change the unit’s display
precision of the current document using the Rhino C/C++ SDK…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Make a copy of the current model units and tolerances
      ON_3dmUnitsAndTolerances units = context.m_doc.Properties().ModelUnitsAndTolerances();
    
      // Prompt the user to enter a new display precision value
      CRhinoGetInteger gi;
      gi.SetCommandPrompt( L"New display precision" );
      gi.SetDefaultInteger( units.m_distance_display_precision );
      gi.SetLowerLimit( 0 );
      gi.SetUpperLimit( 6 );
      gi.GetInteger();
      if( gi.CommandResult() == CRhinoCommand::success )
      {
        // The the user's input
        int distance_display_precision = gi.Number();
        if( distance_display_precision != units.m_distance_display_precision )
        {
          units.m_distance_display_precision = distance_display_precision;
          // Replace the current setting with our updated value
          context.m_doc.Properties().SetModelUnitsAndTolerances( units, false );
        }
      }
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/changing-
display-precision/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/changing-
display-precision/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

