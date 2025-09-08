---
url: https://developer.rhino3d.com/samples/rhinocommon/advanced-display-settings/
scraped_at: 2025-09-08T15:45:40.677574
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

Advanced Display Settings

Demonstrates how to change advanced display settings in Rhino where the mesh
wireframe thickness (in pixels) is modified.

C# VB.NET Python

    
    
    partial class Examples
    {
      // The following example code demonstrates how to modify advanced display settings using
      // the Rhino SDK. In this example, a display mode's mesh wireframe thickness (in pixels)
      // will be modified.
      public static Rhino.Commands.Result AdvancedDisplay(Rhino.RhinoDoc doc)
      {
        // Use the display attributes manager to build a list of display modes.
        // Note, these are copies of the originals...
        DisplayModeDescription[] display_modes = DisplayModeDescription.GetDisplayModes();
        if( display_modes==null || display_modes.Length<1 )
          return Rhino.Commands.Result.Failure;
    
        // Construct an options picker so the user can pick which
        // display mode they want modified
        Rhino.Input.Custom.GetOption go = new Rhino.Input.Custom.GetOption();
        go.SetCommandPrompt("Display mode to modify mesh thickness");
        List<int> opt_list = new List<int>();
    
        for( int i=0; i<display_modes.Length; i++ )
        {
          string english_name = display_modes[i].EnglishName;
          english_name = english_name.Replace("_", "");
          english_name = english_name.Replace(" ", "");
          english_name = english_name.Replace("-", "");
          english_name = english_name.Replace(",", "");
          english_name = english_name.Replace(".", "");
          int index = go.AddOption(english_name);
          opt_list.Add(index);
        }
    
        // Get the command option
        go.Get();
        if( go.CommandResult() != Rhino.Commands.Result.Success )
          return go.CommandResult();
    
        int selected_index = go.Option().Index;
        DisplayModeDescription selected_description = null;
        for( int i=0; i<opt_list.Count; i++ )
        {
          if( opt_list[i]==selected_index )
          {
            selected_description = display_modes[i];
            break;
          }
        }
    
        // Validate...
        if( selected_description==null )
          return Rhino.Commands.Result.Failure;
    
        // Modify the desired display mode. In this case, we
        // will just set the mesh wireframe thickness to zero.
        selected_description.DisplayAttributes.MeshSpecificAttributes.MeshWireThickness = 0;
        // Use the display attributes manager to update the display mode.
        DisplayModeDescription.UpdateDisplayMode(selected_description);
    
        // Force the document to regenerate.
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      ' The following example code demonstrates how to modify advanced display settings using
      ' the Rhino SDK. In this example, a display mode's mesh wireframe thickness (in pixels)
      ' will be modified.
      Public Shared Function AdvancedDisplay(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Use the display attributes manager to build a list of display modes.
    	' Note, these are copies of the originals...
    	Dim display_modes() As DisplayModeDescription = DisplayModeDescription.GetDisplayModes()
    	If display_modes Is Nothing OrElse display_modes.Length<1 Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	' Construct an options picker so the user can pick which
    	' display mode they want modified
    	Dim go As New Rhino.Input.Custom.GetOption()
    	go.SetCommandPrompt("Display mode to modify mesh thickness")
    	Dim opt_list As New List(Of Integer)()
    
    	For i As Integer = 0 To display_modes.Length - 1
    	  Dim english_name As String = display_modes(i).EnglishName
    	  english_name = english_name.Replace("_", "")
    	  english_name = english_name.Replace(" ", "")
    	  english_name = english_name.Replace("-", "")
    	  english_name = english_name.Replace(",", "")
    	  english_name = english_name.Replace(".", "")
    	  Dim index As Integer = go.AddOption(english_name)
    	  opt_list.Add(index)
    	Next i
    
    	' Get the command option
    	go.Get()
    	If go.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go.CommandResult()
    	End If
    
    	Dim selected_index As Integer = go.Option().Index
    	Dim selected_description As DisplayModeDescription = Nothing
    	For i As Integer = 0 To opt_list.Count - 1
    	  If opt_list(i)=selected_index Then
    		selected_description = display_modes(i)
    		Exit For
    	  End If
    	Next i
    
    	' Validate...
    	If selected_description Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	' Modify the desired display mode. In this case, we
    	' will just set the mesh wireframe thickness to zero.
    	selected_description.DisplayAttributes.MeshSpecificAttributes.MeshWireThickness = 0
    	' Use the display attributes manager to update the display mode.
    	DisplayModeDescription.UpdateDisplayMode(selected_description)
    
    	' Force the document to regenerate.
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    # The following example demonstrates how to modify advanced display settings
    # using RhinoCommon. In this example, a display mode's mesh wireframe thickness
    # (in pixels) will be modified.
    def AdvancedDisplay():
        # Use the display attributes manager to build a list of display modes.
        # Note, these are copies of the originals...
        display_modes = Rhino.Display.DisplayModeDescription.GetDisplayModes()
        if not display_modes: return Rhino.Commands.Result.Failure
    
        # Construct an options picker so the user can pick which
        # display mode they want modified
        go = Rhino.Input.Custom.GetOption()
        go.SetCommandPrompt("Display mode to modify mesh thickness")
        opt_list = []
        for i, mode in enumerate(display_modes):
            english_name = mode.EnglishName
            english_name = english_name.translate(None, "_ -,.")
            opt_list.append( go.AddOption(english_name) )
    
        # Get the command option
        go.Get()
        if go.CommandResult()!=Rhino.Commands.Result.Success:
            return go.CommandResult();
    
        selected_index = go.Option().Index
        selected_description = None
        for i,option in enumerate(opt_list):
            if option==selected_index:
                selected_description = display_modes[i]
                break
        # Validate...
        if not selected_description: return Rhino.Commands.Result.Failure
    
        # Modify the desired display mode. In this case, we
        # will just set the mesh wireframe thickness to zero.
        selected_description.DisplayAttributes.MeshSpecificAttributes.MeshWireThickness = 0
        # Use the display attributes manager to update the display mode.
        Rhino.Display.DisplayModeDescription.UpdateDisplayMode(selected_description)
        # Force the document to regenerate.
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        AdvancedDisplay()
    

  

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

