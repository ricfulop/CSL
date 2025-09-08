---
url: https://developer.rhino3d.com/samples/rhinocommon/overlay-text-display-conduit/
scraped_at: 2025-09-08T15:45:29.491584
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

Overlay Text Display Conduit

Demonstrates how to use a display conduit to draw overlay text.

C# VB.NET Python

    
    
    class CustomConduit : Rhino.Display.DisplayConduit
    {
      protected override void DrawForeground(Rhino.Display.DrawEventArgs e)
      {
        var bounds = e.Viewport.Bounds;
        var pt = new Rhino.Geometry.Point2d(bounds.Right - 100, bounds.Bottom - 30);
        e.Display.Draw2dText("Hello", System.Drawing.Color.Red, pt, false);
      }
    }
    
    partial class Examples
    {
      readonly static CustomConduit m_customconduit = new CustomConduit();
      public static Rhino.Commands.Result DrawOverlay(RhinoDoc doc)
      {
        // toggle conduit on/off
        m_customconduit.Enabled = !m_conduit.Enabled;
    
        RhinoApp.WriteLine("Custom conduit enabled = {0}", m_customconduit.Enabled);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Private ReadOnly Shared m_customconduit As New CustomConduit()
      Public Shared Function DrawOverlay(ByVal doc As RhinoDoc) As Rhino.Commands.Result
    	' toggle conduit on/off
    	m_customconduit.Enabled = Not m_conduit.Enabled
    
    	RhinoApp.WriteLine("Custom conduit enabled = {0}", m_customconduit.Enabled)
    	doc.Views.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import System.Drawing
    import scriptcontext
    import rhinoscriptsyntax as rs
    
    # DisplayConduit subclass that overrides the DrawForeground function
    # e is an instance of Rhino.Display.DrawEventArgs
    class CustomConduit(Rhino.Display.DisplayConduit):
        def DrawForeground(self, e):
            color = System.Drawing.Color.Red
            bounds = e.Viewport.Bounds
            pt = Rhino.Geometry.Point2d(bounds.Right - 100, bounds.Bottom - 30)
            e.Display.Draw2dText("Hello", color, pt, False)
    
    
    def showafterscript():
        # Create a custom conduit that can continue to draw after the
        # script has completed. The conduit is kept in the sticky
        # dictionary so we can get at it and turn it off in the future
        #
        # check to see if the conduit has been created and is in sticky
        conduit = None
        if scriptcontext.sticky.has_key("myconduit"):
            conduit = scriptcontext.sticky["myconduit"]
        else:
            # create a conduit and place it in sticky
            conduit = CustomConduit()
            scriptcontext.sticky["myconduit"] = conduit
    
        # Toggle enabled state for conduit. Every time this script is
        # run, it will turn the conduit on and off
        conduit.Enabled = not conduit.Enabled
        if conduit.Enabled: print "conduit enabled"
        else: print "conduit disabled"
        scriptcontext.doc.Views.Redraw()
    
    
    def showinscript():
        # create a custom conduit that only displays during the execution
        # of this script. Once the script has completed, the conduit is turned
        # off and display goes back to normal
        conduit = CustomConduit()
        conduit.Enabled = True
        scriptcontext.doc.Views.Redraw()
        rs.GetString("Pausing for user input")
        conduit.Enabled = False
        scriptcontext.doc.Views.Redraw()
    
    if __name__=="__main__":
        showinscript()
        #showafterscript()
    

  

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

