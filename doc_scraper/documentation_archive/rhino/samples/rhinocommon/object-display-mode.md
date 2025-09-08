---
url: https://developer.rhino3d.com/samples/rhinocommon/object-display-mode/
scraped_at: 2025-09-08T15:44:51.456617
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

Object Display Mode

Demonstrates how to set the object display mode of a user-specified mesh or
surface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ObjectDisplayMode(Rhino.RhinoDoc doc)
      {
        const ObjectType filter = ObjectType.Mesh | ObjectType.Brep;
        ObjRef objref;
        Result rc = Rhino.Input.RhinoGet.GetOneObject("Select mesh or surface", true, filter, out objref);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
        Guid viewportId = doc.Views.ActiveView.ActiveViewportID;
    
        ObjectAttributes attr = objref.Object().Attributes;
        if (attr.HasDisplayModeOverride(viewportId))
        {
          RhinoApp.WriteLine("Removing display mode override from object");
          attr.RemoveDisplayModeOverride(viewportId);
        }
        else
        {
          Rhino.Display.DisplayModeDescription[] modes = Rhino.Display.DisplayModeDescription.GetDisplayModes();
          Rhino.Display.DisplayModeDescription mode = null;
          if (modes.Length == 1)
            mode = modes[0];
          else
          {
            Rhino.Input.Custom.GetOption go = new Rhino.Input.Custom.GetOption();
            go.SetCommandPrompt("Select display mode");
            string[] str_modes = new string[modes.Length];
            for (int i = 0; i < modes.Length; i++)
              str_modes[i] = modes[i].EnglishName.Replace(" ", "").Replace("-", "");
            go.AddOptionList("DisplayMode", str_modes, 0);
            if (go.Get() == Rhino.Input.GetResult.Option)
              mode = modes[go.Option().CurrentListOptionIndex];
          }
          if (mode == null)
            return Rhino.Commands.Result.Cancel;
          attr.SetDisplayModeOverride(mode, viewportId);
        }
        doc.Objects.ModifyAttributes(objref, attr, false);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ObjectDisplayMode(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const filter As ObjectType = ObjectType.Mesh Or ObjectType.Brep
    	Dim objref As ObjRef = Nothing
    	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select mesh or surface", True, filter, objref)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    	Dim viewportId As Guid = doc.Views.ActiveView.ActiveViewportID
    
    	Dim attr As ObjectAttributes = objref.Object().Attributes
    	If attr.HasDisplayModeOverride(viewportId) Then
    	  RhinoApp.WriteLine("Removing display mode override from object")
    	  attr.RemoveDisplayModeOverride(viewportId)
    	Else
    	  Dim modes() As Rhino.Display.DisplayModeDescription = Rhino.Display.DisplayModeDescription.GetDisplayModes()
    	  Dim mode As Rhino.Display.DisplayModeDescription = Nothing
    	  If modes.Length = 1 Then
    		mode = modes(0)
    	  Else
    		Dim go As New Rhino.Input.Custom.GetOption()
    		go.SetCommandPrompt("Select display mode")
    		Dim str_modes(modes.Length - 1) As String
    		For i As Integer = 0 To modes.Length - 1
    		  str_modes(i) = modes(i).EnglishName.Replace(" ", "").Replace("-", "")
    		Next i
    		go.AddOptionList("DisplayMode", str_modes, 0)
    		If go.Get() = Rhino.Input.GetResult.Option Then
    		  mode = modes(go.Option().CurrentListOptionIndex)
    		End If
    	  End If
    	  If mode Is Nothing Then
    		Return Rhino.Commands.Result.Cancel
    	  End If
    	  attr.SetDisplayModeOverride(mode, viewportId)
    	End If
    	doc.Objects.ModifyAttributes(objref, attr, False)
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def ObjectDisplayMode():
        filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Mesh
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select mesh or surface", True, filter)
        if rc != Rhino.Commands.Result.Success: return rc;
        viewportId = scriptcontext.doc.Views.ActiveView.ActiveViewportID
    
        attr = objref.Object().Attributes
        if attr.HasDisplayModeOverride(viewportId):
            print "Removing display mode override from object"
            attr.RemoveDisplayModeOverride(viewportId)
        else:
            modes = Rhino.Display.DisplayModeDescription.GetDisplayModes()
            mode = None
            if len(modes) == 1:
                mode = modes[0]
            else:
                go = Rhino.Input.Custom.GetOption()
                go.SetCommandPrompt("Select display mode")
                str_modes = []
                for m in modes:
                    s = m.EnglishName.replace(" ","").replace("-","")
                    str_modes.append(s)
                go.AddOptionList("DisplayMode", str_modes, 0)
                if go.Get()==Rhino.Input.GetResult.Option:
                    mode = modes[go.Option().CurrentListOptionIndex]
            if not mode: return Rhino.Commands.Result.Cancel
            attr.SetDisplayModeOverride(mode, viewportId)
        scriptcontext.doc.Objects.ModifyAttributes(objref, attr, False)
        scriptcontext.doc.Views.Redraw()
    
    
    if __name__=="__main__":
        ObjectDisplayMode()
    

  

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

