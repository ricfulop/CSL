---
url: https://developer.rhino3d.com/samples/rhinoscript/render-named-views/
scraped_at: 2025-09-08T15:49:48.156089
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

Render Named Views

__

Windows only

Demonstrates how to render named views using RhinoScript.

VBScript

    
    
    Option Explicit
    
    ' Renders one or more named views to a user-defined folder
    Sub RenderNamedViews
    
      ' Let the user pick the named view to render
      Dim render_views
      render_views = GetRenderViews
      If Not IsArray(render_views) Then Exit Sub
    
      ' Let the user pick the folder to save the renderings  
      Dim folder  
      folder = Rhino.BrowseForFolder(Rhino.DocumentPath, "Browse for folder", "Batch Render")
      If IsNull(folder) Then Exit Sub
    
      ' Save the active view
      Dim saved_view_name
      saved_view_name = Rhino.CurrentView
      Rhino.Command "_-NamedView _Save $$_save_$$ _Enter", 0
    
      ' Process each named view
      Dim view
      For Each view In render_views
        If IsStandardView(view) Then
          ' If the named view is a standard view
          Rhino.Command "_-SetView _World _" & view, 0
        Else
          ' If the named view is not a standard view
          Rhino.Command "_-NamedView _Restore " & view & " _Enter", 0
        End If
        ' Render the scene with the current render engine
        Rhino.Command "_-Render"
        ' Save the render to a jpg file
        Rhino.Command "_-SaveRenderWindowAs " & GetRenderFileName(folder, view, "jpg")
        ' Close the render window
        Rhino.Command "_-CloseRenderWindow"    
      Next
    
      ' Restore the active view
      Rhino.Command "_-NamedView _Restore $$_save_$$ _Enter", 0
      Rhino.RenameView Rhino.CurrentView, saved_view_name
    
      ' Delete the temporary named view
      Rhino.Command "_-NamedView _Delete $$_save_$$ _Enter", 0
    
    End Sub
    
    ' Returns an array of view names to render
    Function GetRenderViews()
      GetRenderViews = vbNull  
      Dim all_views, selected_views
      all_views = GetAllViews
      selected_views = Rhino.MultiListBox(all_views, "Select views to render.", "Batch Render")
      If IsArray(selected_views) Then
        GetRenderViews = selected_views
      End If
    End Function
    
    ' Returns a render-formatted file name
    Function GetRenderFileName(folder, view, ext)
      Dim doc, file, temp
      doc = Rhino.DocumentName
      temp = "_" & view & "." & ext
      file = LCase(Replace(doc, ".3dm", temp, 1, -1, 1))
      GetRenderFileName = Chr(34) & folder & file & Chr(34)
    End Function
    
    ' Returns an array of both standard and named view names
    Function GetAllViews()
      Dim all_views, std_views, named_views
      std_views = GetStandardViews
      named_views = Rhino.NamedViews
      If IsArray(named_views) Then
        all_views = Rhino.JoinArrays(std_views, named_views)
        all_views = Rhino.CullDuplicateStrings(all_views)
        GetAllViews = Rhino.SortStrings(all_views)
      Else
        GetAllViews = std_views
      End If
    End Function
    
    ' Returns an array of standard view names
    Function GetStandardViews()
      GetStandardViews = Array("Back", "Bottom", "Front", "Left", "Perspective", "Right", "Top")
    End Function
    
    ' Verifies a string is a standard view name
    Function IsStandardView(str)
      IsStandardView = vbFalse
      Dim std_views, i
      std_views = GetStandardViews
      For i = 0 To UBound(std_views)
        If StrComp(std_views(i), str, 1) = 0 Then
          IsStandardView = vbTrue
          Exit For
        End If
      Next
    End Function
    

  

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

