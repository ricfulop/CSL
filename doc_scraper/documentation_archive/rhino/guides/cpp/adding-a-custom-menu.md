---
url: https://developer.rhino3d.com/guides/cpp/adding-a-custom-menu/
scraped_at: 2025-09-08T15:38:36.355484
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

[Adding a Custom Menu](https://developer.rhino3d.com/guides/cpp/adding-a-
custom-menu/)

  * Problem
  * Solution
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding a Custom Menu

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you would like to add a submenu to Rhino’s File menu. You might start
fiddling around with the `Insert­Plug­In­Menu­To­Rhino­Menu()` and
­`Insert­Plug­In­Item­To­Rhino­Menu()` functions but not seem to be getting
anywhere. `Insert­Plug­In­Menu­To­Rhino­Menu()` adds a menu into the Rhino’s
main menu bar. `Insert­Plug­In­Item­To­RhinoMenu()` adds a menu item anywhere
in the Rhino menu. To solve this problem, you want a little of both…

## Solution

To insert a menu item, or a submenu, into Rhino’s menu, do the following:

  1. Use `CRhinoApp::FindMenuItem` to search through Rhino’s menu structure for an existing menu item that’s where you want to insert your menu item.
  2. Use `CRhinoPlugIn::InsertPlugInItemToRhinoMenu` to insert your menu into Rhino’s menu.

## Sample

The following example command demonstrates how to add and remove a custom menu
from Rhino’s menu:

    
    
    ////////////////////////////////////////////////////////////////
    // cmdMyMenu.cpp
    
    #include "StdAfx.h"
    #include "MyTestPlugIn.h"
    #include "Resource.h"
    
    ////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////
    //
    // BEGIN MyMenu command
    //
    
    class CCommandMyMenu : public CRhinoCommand
    {
    public:
      CCommandMyMenu() {}
      ~CCommandMyMenu() {}
      UUID CommandUUID()
      {
        static const GUID MyMenuCommand_UUID =
        { <TODO: add your command uuid here> };
        return MyMenuCommand_UUID;
      }
      const wchar_t* EnglishCommandName() { return L"MyMenu"; }
      const wchar_t* LocalCommandName() { return L"MyMenu"; }
      CRhinoCommand::result RunCommand( const CRhinoCommandContext& );
    
      BOOL LoadMyMenu();
      BOOL UnloadMyMenu();
    
    private:
      CMenu m_menu;
    };
    
    // The one and only CCommandMyMenu object
    static class CCommandMyMenu theMyMenuCommand;
    
    CRhinoCommand::result CCommandMyMenu::RunCommand( const CRhinoCommandContext& context )
    {
      bool bVisible = ( m_menu.GetSafeHmenu() ) ? true : false;
    
      ON_wString prompt;
      prompt.Format( L"%s is %s. New value",
        EnglishCommandName(),
        bVisible ? L"visible" : L"hidden"
        );
    
      CRhinoGetOption go;
      go.SetCommandPrompt( prompt );
      int s_opt = go.AddCommandOption( RHCMDOPTNAME(L"Show") );
      int h_opt = go.AddCommandOption( RHCMDOPTNAME(L"Hide") );
      int t_opt = go.AddCommandOption( RHCMDOPTNAME(L"Toggle") );
      go.GetOption();
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoCommandOption* opt = go.Option();
      if( 0 == opt )
        return failure;
    
      if( opt->m_option_index == s_opt )
      {
        if( false == bVisible )
          LoadMyMenu();
      }
      else if( opt->m_option_index == h_opt )
      {
        if( true == bVisible )
          UnloadMyMenu();
      }
      else
      {
        if( true == bVisible )
          UnloadMyMenu();
        else
          LoadMyMenu();
      }
    
      return success;
    }
    
    BOOL CCommandMyMenu::LoadMyMenu()
    {
      // Switch the module state so resources are read
      // from our plugin (DLL), not Rhino.
      AFX_MANAGE_STATE( AfxGetStaticModuleState() );
    
      // Try to load our menu resource from our plugin.
      // Note, m_my_menu is a CMenu member variable.
      if( 0 == m_menu.GetSafeHmenu() )
      {
        if( !m_menu.LoadMenu(IDR_MY_MENU) )
          return FALSE;
      }
    
      // Find a location in Rhino's menu to insert our
      // menu item. For this example, we will insert our
      // menu on the "Tools" menu just below the "Commands"
      // item.
      HMENU hParent = 0;
      int index = 0;
      //if( !RhinoApp().FindRhinoMenuItem(L"&File::&Print...Ctrl+P", hParent, index) )
      if( !RhinoApp().FindRhinoMenuItem(L"Too&ls::&Commands", hParent, index) )
      {
        m_menu.DestroyMenu();
        return FALSE;
      }
    
      // Create and initialize a MENUITEMINFO struct.
      MENUITEMINFO mi;
      memset( &mi, 0, sizeof(mi) );
      mi.cbSize = sizeof(mi);
    
      // Fill in our menu info
      mi.fMask = MIIM_ID | MIIM_TYPE | MIIM_STATE | MIIM_SUBMENU;
      mi.wID = MF_POPUP;
      mi.fType = MFT_STRING;
    
      ON_wString wstr = L"MyMenu";
      mi.dwTypeData = wstr.Array();
    
      mi.fState = MFS_ENABLED;
      mi.hSubMenu = m_menu.GetSafeHmenu();
      mi.hSubMenu = ::GetSubMenu( mi.hSubMenu, 0 );
      mi.wID = IDR_MY_MENU;
    
      // Add our menu to Rhino's menu
      BOOL rc = MyTestPlugIn().InsertPlugInItemToRhinoMenu( hParent, index + 1, &mi );
      if( !rc )
        m_menu.DestroyMenu();
    
      return rc;
    }
    
    BOOL CCommandMyMenu::UnloadMyMenu()
    {
      BOOL rc = FALSE;
    
      // Find our menu item in Rhino's menu.
      HMENU hParent = 0;
      int index = 0;
      if( RhinoApp().FindRhinoMenuItem(L"Too&ls::MyMenu", hParent, index) )
      {
        // Remove our menu item.
        if( ::RemoveMenu(hParent, index, MF_BYPOSITION) )
        {
          // Redraw Rhino's menu bar.
          DrawMenuBar( RhinoApp().MainWnd() );
          m_menu.DestroyMenu();
          rc = TRUE;
        }
      }
    
      return rc;
    }
    
    //
    // END MyMenu command
    //
    ////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
a-custom-menu/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
a-custom-menu/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

