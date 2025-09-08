---
url: https://developer.rhino3d.com/samples/rhinocommon/custom-undo/
scraped_at: 2025-09-08T15:45:54.605442
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

Custom Undo

Demonstrates how to set up a custom set of actions when the Undo command is
called.

C# VB.NET Python

    
    
    partial class Examples
    {
      static double MyFavoriteNumber = 0;
    
      public static Rhino.Commands.Result CustomUndo(RhinoDoc doc)
      {
        // Rhino automatically sets up an undo record when a command is run,
        // but... the undo record is not saved if nothing changes in the
        // document (objects added/deleted, layers changed,...)
        //
        // If we have a command that doesn't change things in the document,
        // but we want to have our own custom undo called then we need to do
        // a little extra work
    
        double d = MyFavoriteNumber;
        if (Rhino.Input.RhinoGet.GetNumber("Favorite number", true, ref d) == Rhino.Commands.Result.Success)
        {
          double current_value = MyFavoriteNumber;
          doc.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value);
          MyFavoriteNumber = d;
        }
        return Rhino.Commands.Result.Success;
      }
    
      // event handler for custom undo
      static void OnUndoFavoriteNumber(object sender, Rhino.Commands.CustomUndoEventArgs e)
      {
        // !!!!!!!!!!
        // NEVER change any setting in the Rhino document or application.  Rhino
        // handles ALL changes to the application and document and you will break
        // the Undo/Redo commands if you make any changes to the application or
        // document. This is meant only for your own private plugin data
        // !!!!!!!!!!
    
        // This function can be called either by undo or redo
        // In order to get redo to work, add another custom undo event with the
        // current value.  If you don't want redo to work, just skip adding
        // a custom undo event here
        double current_value = MyFavoriteNumber;
        e.Document.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value);
    
        double old_value = (double)e.Tag;
        RhinoApp.WriteLine("Going back to your favorite = {0}", old_value);
        MyFavoriteNumber = old_value;
      }
    }
    
    
    
    Partial Friend Class Examples
      Private Shared MyFavoriteNumber As Double = 0
    
      Public Shared Function CustomUndo(ByVal doc As RhinoDoc) As Rhino.Commands.Result
    	' Rhino automatically sets up an undo record when a command is run,
    	' but... the undo record is not saved if nothing changes in the
    	' document (objects added/deleted, layers changed,...)
    	'
    	' If we have a command that doesn't change things in the document,
    	' but we want to have our own custom undo called then we need to do
    	' a little extra work
    
    	Dim d As Double = MyFavoriteNumber
    	If Rhino.Input.RhinoGet.GetNumber("Favorite number", True, d) = Rhino.Commands.Result.Success Then
    	  Dim current_value As Double = MyFavoriteNumber
    	  doc.AddCustomUndoEvent("Favorite Number", AddressOf OnUndoFavoriteNumber, current_value)
    	  MyFavoriteNumber = d
    	End If
    	Return Rhino.Commands.Result.Success
      End Function
    
      ' event handler for custom undo
      Private Shared Sub OnUndoFavoriteNumber(ByVal sender As Object, ByVal e As Rhino.Commands.CustomUndoEventArgs)
    	' !!!!!!!!!!
    	' NEVER change any setting in the Rhino document or application.  Rhino
    	' handles ALL changes to the application and document and you will break
    	' the Undo/Redo commands if you make any changes to the application or
    	' document. This is meant only for your own private plugin data
    	' !!!!!!!!!!
    
    	' This function can be called either by undo or redo
    	' In order to get redo to work, add another custom undo event with the
    	' current value.  If you don't want redo to work, just skip adding
    	' a custom undo event here
    	Dim current_value As Double = MyFavoriteNumber
    	e.Document.AddCustomUndoEvent("Favorite Number", AddressOf OnUndoFavoriteNumber, current_value)
    
    	Dim old_value As Double = CDbl(e.Tag)
    	RhinoApp.WriteLine("Going back to your favorite = {0}", old_value)
    	MyFavoriteNumber = old_value
      End Sub
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    
    def OnUndoFavoriteNumber(sender, e):
        """!!!!!!!!!!
        NEVER change any setting in the Rhino document or application.  Rhino
        handles ALL changes to the application and document and you will break
        the Undo/Redo commands if you make any changes to the application or
        document. This is meant only for your own private plugin data
        !!!!!!!!!!
    
        This function can be called either by undo or redo
        In order to get redo to work, add another custom undo event with the
        current value.  If you don't want redo to work, just skip adding
        a custom undo event here
        """
        current_value = scriptcontext.sticky["FavoriteNumber"]
        e.Document.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value)
    
        old_value = e.Tag
        print "Going back to your favorite =", old_value
        scriptcontext.sticky["FavoriteNumber"]= old_value;
    
    
    def TestCustomUndo():
        """
        Rhino automatically sets up an undo record when a command is run,
        but... the undo record is not saved if nothing changes in the
        document (objects added/deleted, layers changed,...)
    
        If we have a command that doesn't change things in the document,
        but we want to have our own custom undo called then we need to do
        a little extra work
        """
        current_value = 0
        if scriptcontext.sticky.has_key("FavoriteNumber"):
            current_value = scriptcontext.sticky["FavoriteNumber"]
        rc, new_value = Rhino.Input.RhinoGet.GetNumber("Favorite number", True, current_value)
        if rc!=Rhino.Commands.Result.Success: return
    
        scriptcontext.doc.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value);
        scriptcontext.sticky["FavoriteNumber"] = new_value
    
    if __name__=="__main__":
        TestCustomUndo()
    

  

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

