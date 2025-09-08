---
url: https://developer.rhino3d.com/guides/cpp/saving-persistent-settings/
scraped_at: 2025-09-08T15:39:19.391458
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

[Saving Persistent Settings](https://developer.rhino3d.com/guides/cpp/saving-
persistent-settings/)

  * Problem
  * Solution
  * How To

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Saving Persistent Settings

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Your plugin maintains a number of settings that need to be retained between
sessions. Is there an easy way to do this? Do these setting migrate from one
Rhino service release to another?

## Solution

You can load and save persistent plugin setting from and to the Registry using
the `CRhinoPlugIn::LoadProfile` and `CRhinoPlugIn::SaveProfile` virtual
functions. For information on these virtual function, see _rhinoSdkPlugIn.h_.

## How To

Lets say we have a sample plugin class declaration that looks something like
the following:

    
    
    class CTestPlugIn : public CRhinoUtilityPlugIn
    {
    public:
      CTestPlugIn();
      ~CTestPlugIn();
    
      // Required overrides
      const wchar_t* PlugInName() const;
      const wchar_t* PlugInVersion() const;
      GUID PlugInID() const;
      BOOL OnLoadPlugIn();
      void OnUnloadPlugIn();
    
     private:
      ON_wString m_plugin_version;
    
      // Persistent data
      bool m_value0;
      int m_value1;
      double m_value2;
      ON_wString m_value3;
    };
    

Simply, overload the `CRhinoPlugIn::LoadProfile` and
`CRhinoPlugIn::SaveProfile` virtual functions by adding the the following
public declarations to our plugin class:

    
    
    void LoadProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc );
    void SaveProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc );
    

Then, provide the definition:

    
    
    void CTestPlugIn::LoadProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc )
    {
      pc.LoadProfileBool( lpszSection, L"value0", &m_value0 );
      pc.LoadProfileInt( lpszSection, L"value1", &m_value1 );
      pc.LoadProfileDouble( lpszSection, L"value2", &m_value2 );
      pc.LoadProfileString( lpszSection, L"value3", m_value3 );
    }
    
    void CTestPlugIn::SaveProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc )
    {
      pc.SaveProfileBool( lpszSection, L"value0", m_value0 );
      pc.SaveProfileInt( lpszSection, L"value1", m_value1 );
      pc.SaveProfileDouble( lpszSection, L"value2", m_value2 );
      pc.SaveProfileString( lpszSection, L"value3", m_value3 );
    }
    

That’s it! Your data is now saved at the following location in the Registry:

    
    
    HKEY_CURRENT_USER\Software\McNeel\Rhinoceros\<version>\<scheme>\Plug-ins\<plugin_id>\Settings
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/saving-
persistent-settings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/saving-
persistent-settings/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

