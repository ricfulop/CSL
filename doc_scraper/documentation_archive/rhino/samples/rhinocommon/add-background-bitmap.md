---
url: https://developer.rhino3d.com/samples/rhinocommon/add-background-bitmap/
scraped_at: 2025-09-08T15:44:14.460268
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

Add Background Bitmap

Demonstrates how to add a background bitmap to a Rhino model at a user-
specified location.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddBackgroundBitmap(Rhino.RhinoDoc doc)
      {
        Rhino.RhinoApp.WriteLine ("hey");
        // Allow the user to select a bitmap file
        Rhino.UI.OpenFileDialog fd = new Rhino.UI.OpenFileDialog();
        fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg";
        if (!fd.ShowDialog())
          return Rhino.Commands.Result.Cancel;
    
        // Verify the file that was selected
        System.Drawing.Image image;
        try
        {
          image = System.Drawing.Image.FromFile(fd.FileName);
        }
        catch (Exception)
        {
          return Rhino.Commands.Result.Failure;
        }
    
        // Allow the user to pick the bitmap origin
        Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
        gp.SetCommandPrompt("Bitmap Origin");
        gp.ConstrainToConstructionPlane(true);
        gp.Get();
        if (gp.CommandResult() != Rhino.Commands.Result.Success)
          return gp.CommandResult();
    
        // Get the view that the point was picked in.
        // This will be the view that the bitmap appears in.
        Rhino.Display.RhinoView view = gp.View();
        if (view == null)
        {
          view = doc.Views.ActiveView;
          if (view == null)
            return Rhino.Commands.Result.Failure;
        }
    
        // Allow the user to specify the bitmap with in model units
        Rhino.Input.Custom.GetNumber gn = new Rhino.Input.Custom.GetNumber();
        gn.SetCommandPrompt("Bitmap width");
        gn.SetLowerLimit(1.0, false);
        gn.Get();
        if (gn.CommandResult() != Rhino.Commands.Result.Success)
          return gn.CommandResult();
    
        // Cook up some scale factors
        double w = gn.Number();
        double image_width = image.Width;
        double image_height = image.Height;
        double h = w * (image_height / image_width);
    
        Rhino.Geometry.Plane plane = view.ActiveViewport.ConstructionPlane();
        plane.Origin = gp.Point();
        view.ActiveViewport.SetTraceImage(fd.FileName, plane, w, h, false, false);
        view.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddBackgroundBitmap(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Rhino.RhinoApp.WriteLine("hey")
    	' Allow the user to select a bitmap file
    	Dim fd As New Rhino.UI.OpenFileDialog()
    	fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
    	If Not fd.ShowDialog() Then
    	  Return Rhino.Commands.Result.Cancel
    	End If
    
    	' Verify the file that was selected
    	Dim image As System.Drawing.Image
    	Try
    	  image = System.Drawing.Image.FromFile(fd.FileName)
    	Catch e1 As Exception
    	  Return Rhino.Commands.Result.Failure
    	End Try
    
    	' Allow the user to pick the bitmap origin
    	Dim gp As New Rhino.Input.Custom.GetPoint()
    	gp.SetCommandPrompt("Bitmap Origin")
    	gp.ConstrainToConstructionPlane(True)
    	gp.Get()
    	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gp.CommandResult()
    	End If
    
    	' Get the view that the point was picked in.
    	' This will be the view that the bitmap appears in.
    	Dim view As Rhino.Display.RhinoView = gp.View()
    	If view Is Nothing Then
    	  view = doc.Views.ActiveView
    	  If view Is Nothing Then
    		Return Rhino.Commands.Result.Failure
    	  End If
    	End If
    
    	' Allow the user to specify the bitmap with in model units
    	Dim gn As New Rhino.Input.Custom.GetNumber()
    	gn.SetCommandPrompt("Bitmap width")
    	gn.SetLowerLimit(1.0, False)
    	gn.Get()
    	If gn.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gn.CommandResult()
    	End If
    
    	' Cook up some scale factors
    	Dim w As Double = gn.Number()
    	Dim image_width As Double = image.Width
    	Dim image_height As Double = image.Height
    	Dim h As Double = w * (image_height / image_width)
    
    	Dim plane As Rhino.Geometry.Plane = view.ActiveViewport.ConstructionPlane()
    	plane.Origin = gp.Point()
    	view.ActiveViewport.SetTraceImage(fd.FileName, plane, w, h, False, False)
    	view.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Windows.Forms.DialogResult
    import System.Drawing.Image
    
    def AddBackgroundBitmap():
        # Allow the user to select a bitmap file
        fd = Rhino.UI.OpenFileDialog()
        fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
        if not fd.ShowDialog():
            return Rhino.Commands.Result.Cancel
    
        # Verify the file that was selected
        image = None
        try:
            image = System.Drawing.Image.FromFile(fd.FileName)
        except:
            return Rhino.Commands.Result.Failure
    
        # Allow the user to pick the bitmap origin
        gp = Rhino.Input.Custom.GetPoint()
        gp.SetCommandPrompt("Bitmap Origin")
        gp.ConstrainToConstructionPlane(True)
        gp.Get()
        if gp.CommandResult()!=Rhino.Commands.Result.Success:
            return gp.CommandResult()
    
        # Get the view that the point was picked in.
        # This will be the view that the bitmap appears in.
        view = gp.View()
        if view is None:
            view = scriptcontext.doc.Views.ActiveView
            if view is None: return Rhino.Commands.Result.Failure
    
        # Allow the user to specify the bitmap with in model units
        gn = Rhino.Input.Custom.GetNumber()
        gn.SetCommandPrompt("Bitmap width")
        gn.SetLowerLimit(1.0, False)
        gn.Get()
        if gn.CommandResult()!=Rhino.Commands.Result.Success:
            return gn.CommandResult()
    
        # Cook up some scale factors
        w = gn.Number()
        h = w * (image.Width / image.Height)
    
        plane = view.ActiveViewport.ConstructionPlane()
        plane.Origin = gp.Point()
        view.ActiveViewport.SetTraceImage(fd.FileName, plane, w, h, False, False)
        view.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        AddBackgroundBitmap()
    

  

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

