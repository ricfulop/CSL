---
url: https://developer.rhino3d.com/guides/cpp/canceling-long-processes-with-esc/
scraped_at: 2025-09-08T15:39:35.572614
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

[Canceling Long Processes with
ESC](https://developer.rhino3d.com/guides/cpp/canceling-long-processes-with-
esc/)

  * Overview
  * Example 1
  * Example 2
  * Usage

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Canceling Long Processes with ESC

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

When writing commands that contain long, time-consuming tasks, you might want
to allow the user to cancel the process or command. Here are a couple examples
of ways this can be achieved…

## Example 1

The following example demonstrates how to periodically test to see if the user
pressed the `ESC` key by “peeking” in Rhino’s message queue…

    
    
    //  -1 = Quit Rhino
    //   1 = Escape key pressed
    //   0 = Okay to proceed
    int EscapeKeyPressed()
    {
      AFX_MANAGE_STATE( RhinoApp().RhinoModuleState() );
    
      MSG msg;
      memset( &msg, 0, sizeof(MSG) );
      while( ::PeekMessage(&msg, 0, 0, 0, PM_NOREMOVE) )
      {
        if( msg.message == WM_KEYDOWN && msg.wParam == VK_ESCAPE )
          return 1;
    
        if( !RhinoApp().PumpMessage() )
          return -1;
      }
    
      return 0;
    }
    

Using this function is quite simple: in the middle of your loop, call the
above function. If the function returns something other than 0, break out of
your loop.

## Example 2

The following sample class demonstrates how to hook the Windows keyboard from
a Rhino plugin and check for the `ESC` key.

    
    
    //
    // rhinoEscapeKey.h
    //
    
    class CRhinoEscapeKey
    {
    public:
      CRhinoEscapeKey( bool bHookNow = false );
      ~CRhinoEscapeKey();
      bool Start();
      void Stop();
      bool EscapeKeyPressed() const;
      void ClearEscapeKeyPressedFlag();
    protected:
      static LRESULT CALLBACK HookProc( int code, WPARAM wParam, LPARAM lParam );
      static HHOOK m_KeyboardHookProc;
      static bool m_escape_pressed;
    };
    
    //
    // rhinoEscapeKey.cpp
    //
    
    bool CRhinoEscapeKey::m_escape_pressed = false;
    HHOOK CRhinoEscapeKey::m_KeyboardHookProc = NULL;
    
    CRhinoEscapeKey::CRhinoEscapeKey( bool bStartNow )
    {
      if( bStartNow )
        Start();
    }
    
    CRhinoEscapeKey::~CRhinoEscapeKey()
    {
      Stop();
    }
    
    bool CRhinoEscapeKey::Start()
    {
      if( NULL == m_KeyboardHookProc )
        m_KeyboardHookProc = ::SetWindowsHookEx(
                                  WH_KEYBOARD,
                                  CRhinoEscapeKey::HookProc,
                                  RhinoApp().RhinoInstanceHandle(),
                                  ::AfxGetThread()->m_nThreadID
                                  );
      ClearEscapeKeyPressedFlag();
      return( NULL != m_KeyboardHookProc );
    }
    
    void CRhinoEscapeKey::Stop()
    {
      if( m_KeyboardHookProc )
        UnhookWindowsHookEx( m_KeyboardHookProc );
      m_KeyboardHookProc = NULL;
    }
    
    bool CRhinoEscapeKey::EscapeKeyPressed() const
    {
      RhinoApp().Wait(0);
      return m_escape_pressed;
    }
    
    void CRhinoEscapeKey::ClearEscapeKeyPressedFlag()
    {
      m_escape_pressed = false;
    }
    
    LRESULT CALLBACK CRhinoEscapeKey::HookProc( int code, WPARAM wParam, LPARAM lParam )
    {
      // On escape key down....
      if( code == HC_ACTION && wParam == VK_ESCAPE && !(lParam & 0x80000000) )
      {
        m_escape_pressed = true;
        UnhookWindowsHookEx( m_KeyboardHookProc );
        m_KeyboardHookProc = NULL;
        return 0; // Eat the escape key
      }
      // call next hook proc including standard windows proc.
      return CallNextHookEx( m_KeyboardHookProc, code, wParam, lParam );
    }
    

## Usage

The following sample code demonstrates using the `CRhinoEscapeKey` class
within a Rhino command…

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      CRhinoEscapeKey escape;
      escape.Start();
    
      int i = 0;
      while( true )
      {
        if( escape.EscapeKeyPressed() )
        {
          escape.Stop();
          RhinoApp().Print( L"Command canceled.\n" );
          break;
        }
        RhinoApp().Print( L"Count = %d.\n", ++i );
      }
    
      return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/canceling-
long-processes-with-esc/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/canceling-
long-processes-with-esc/index.md) [
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

