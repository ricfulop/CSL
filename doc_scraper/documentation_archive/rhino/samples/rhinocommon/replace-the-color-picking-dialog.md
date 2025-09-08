---
url: https://developer.rhino3d.com/samples/rhinocommon/replace-the-color-picking-dialog/
scraped_at: 2025-09-08T15:45:33.613297
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

Replace the Color Picking Dialog

Demonstrates how to replace Rhino's color picking dialog.

C# VB.NET Python

    
    
    partial class Examples
    {
      private static ColorDialog m_dlg = null;
    
      public static Result ReplaceColorDialog(RhinoDoc doc)
      {
        Dialogs.SetCustomColorDialog(OnSetCustomColorDialog);
        return Result.Success;
      }
    
      static void OnSetCustomColorDialog(object sender, GetColorEventArgs e)
      {
        m_dlg = new ColorDialog();
        if (m_dlg.ShowDialog(null) == DialogResult.Ok)
        {
          var c = m_dlg.Color;
          e.SelectedColor = System.Drawing.Color.FromArgb (c.Ab, c.Rb, c.Gb, c.Bb);
        }
      }
    }
    
    
    
    Partial Friend Class Examples
      Private Shared m_dlg As ColorDialog = Nothing
    
      Public Shared Function ReplaceColorDialog(ByVal doc As RhinoDoc) As Result
    	Dialogs.SetCustomColorDialog(AddressOf OnSetCustomColorDialog)
    	Return Result.Success
      End Function
    
      Private Shared Sub OnSetCustomColorDialog(ByVal sender As Object, ByVal e As GetColorEventArgs)
    	m_dlg = New ColorDialog()
    	If m_dlg.ShowDialog(Nothing) = DialogResult.Ok Then
    	  Dim c = m_dlg.Color
    	  e.SelectedColor = System.Drawing.Color.FromArgb(c.Ab, c.Rb, c.Gb, c.Bb)
    	End If
      End Sub
    End Class
    
    
    
    # No Python sample available
    

  

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

