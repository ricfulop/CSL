---
url: https://developer.rhino3d.com/samples/rhinocommon/determine-language-setting/
scraped_at: 2025-09-08T15:45:55.596008
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

Determine Language Setting

Demonstrates how to determine Rhino's language setting.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DetermineCurrentLanguage(RhinoDoc doc)
      {
        var language_id = Rhino.ApplicationSettings.AppearanceSettings.LanguageIdentifier;
        var culture = new System.Globalization.CultureInfo(language_id);
        RhinoApp.WriteLine("The current language is {0}", culture.EnglishName);
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DetermineCurrentLanguage(ByVal doc As RhinoDoc) As Result
    	Dim language_id = Rhino.ApplicationSettings.AppearanceSettings.LanguageIdentifier
    	Dim culture = New System.Globalization.CultureInfo(language_id)
    	RhinoApp.WriteLine("The current language is {0}", culture.EnglishName)
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    import System
    
    locale_id = rs.LocaleID()
    culture = System.Globalization.CultureInfo(locale_id)
    print culture.EnglishName
    

  

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

