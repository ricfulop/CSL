---
url: https://developer.rhino3d.com/guides/cpp/creating-custom-color-picker/
scraped_at: 2025-09-08T15:39:38.600429
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

[Creating a Custom Color
Picker](https://developer.rhino3d.com/guides/cpp/creating-custom-color-
picker/)

  * How To

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Creating a Custom Color Picker

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## How To

To replace Rhino’s color picking dialog, derive a new class from
`CRhinoReplaceColorDialog` and override the `ColorDialog()` virtual function.
Note, if more that one `CRhinoReplaceColorDialog`-derived classes exist, then
the last `CRhinoReplaceColorDialog`-derived object created will be displayed.

The following sample code demonstrates how to replace Rhino’s color picking
dialog. In this example, we will simply replace it with the Windows standard
color picking dialog…

    
    
    class CMyColorDialog : public CRhinoReplaceColorDialog
    {
    public:
      CMyColorDialog() : CRhinoReplaceColorDialog(::AfxGetStaticModuleState()) {};
      virtual ~CMyColorDialog() {};
      bool CMyColorDialog::ColorDialog( HWND hWndParent,
                                        ON_Color& color,
                                        bool bIncludeButtonColors,
                                        const wchar_t* lpsDialogTitle )
      {
        CColorDialog dlg( color, CC_ANYCOLOR|CC_FULLOPEN, CWnd::FromHandle(hWndParent) );
        if( IDOK != dlg.DoModal() )
          return false;
        color = dlg.GetColor();
        return true;
      }
    };
    

Now, create a new Rhino command and add a pointer to the above class as a
public data member. Do not forget to initialize it’s value to `NULL` in the
command classes constructor. For example:

    
    
    CMyColorDialog* m_pMyColorDialog;
    // ...
    CTestCommand::CTestCommand() : pMyColorDialog(NULL) {}
    

Finally, in your new command classes `RunCommand()` member, install the new
color picker. For example:

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      if( m_pMyColorDialog )
      {
        delete m_pMyColorDialog;
        m_pMyColorDialog = NULL;
        RhinoApp().Print( L"Rhino color dialog restored.\n" );
      }
      else
      {
        m_pMyColorDialog = new CMyColorDialog;
        if( m_pMyColorDialog )
          RhinoApp().Print( L"Rhino color dialog replaced.\n" );
        else
          RhinoApp().Print( L"Error replacing Rhino color dialog.\n" );
      }
      return CRhinoCommand::success;
    }
    

For more information on the `CRhinoReplaceColorDialog` class, see it’s
declaration in _rhinoSdkUtilities.h_.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/creating-
custom-color-picker/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/creating-
custom-color-picker/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

