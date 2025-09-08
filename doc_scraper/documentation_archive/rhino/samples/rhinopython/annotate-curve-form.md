---
url: https://developer.rhino3d.com/samples/rhinopython/annotate-curve-form/
scraped_at: 2025-09-08T15:47:02.877242
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

Annotate Curve Form

__

Windows only

The following sample shows how to create a custom Windows form.

Python

    
    
    """
    NOTE:
    
    - Reference to RhinoCommmon.dll is added by default
    
    - You can specify your script requirements like:
    
        # r: <package-specifier> [, <package-specifier>]
        # requirements: <package-specifier> [, <package-specifier>]
    
        For example this line will ask the runtime to install
        the listed packages before running the script:
    
        # requirements: pytoml, keras
    
        You can install specific versions of a package
        using pip-like package specifiers:
    
        # r: pytoml==0.10.2, keras>=2.6.0
    
    - Use env directive to add an environment path to sys.path automatically
        # env: /path/to/your/site-packages/
    """
    #! python3
    
    # Imports
    import Rhino
    import rhinoscriptsyntax as rs
    import scriptcontext
    import System
    import Rhino.UI
    import Eto.Drawing as drawing
    import Eto.Forms as forms
     
    # SampleEtoRoomNumber dialog class
    class SampleEtoCurveAnnotateDialog(forms.Dialog[bool]):
     
        # Dialog box Class initializer
        def __init__(self, curveid):
            super().__init__()
            # Initialize dialog box
            self.Title = 'Sample Eto: Curve Annotation'
            self.Padding = drawing.Padding(10)
            self.Resizable = False
     
            # Create controls for the dialog
            self.m_label = forms.Label()
            self.m_label.Text = 'Curve ID:'
            self.m_idlabel = forms.Label()
            self.m_idlabel.Text = curveid
            self.m_tlabel = forms.Label()
            self.m_tlabel.Text = 'Curve Label:'
            self.m_textbox = forms.TextBox()
            self.m_textbox.Text = 'Start'
    
    
    
            # Create the default button
            self.DefaultButton = forms.Button()
            self.DefaultButton.Text ='OK'
            self.DefaultButton.Click += self.OnOKButtonClick
     
            # Create the abort button
            self.AbortButton = forms.Button()
            self.AbortButton.Text ='Cancel'
            self.AbortButton.Click += self.OnCloseButtonClick
     
            # Create a table layout and add all the controls
            layout = forms.DynamicLayout()
            layout.Spacing = drawing.Size(5, 5)
            layout.AddRow(self.m_label, self.m_idlabel)
            layout.AddRow(None) # spacer
            layout.AddRow(self.m_tlabel, self.m_textbox)
            layout.AddRow(None) # spacer
            layout.AddRow(self.DefaultButton, self.AbortButton)
     
            # Set the dialog content
            self.Content = layout
     
        # Start of the class functions
     
        # Get the value of the textbox
        def GetText(self):
            return self.m_idlabel.Text
     
        # Close button click handler
        def OnCloseButtonClick(self, sender, e):
            self.m_idlabel.Text = ""
            self.Close(False)
     
        # OK button click handler
        def OnOKButtonClick(self, sender, e):
            if self.m_idlabel.Text == "":
                self.Close(False)
            else:
                self.Close(True)
     
        ## End of Dialog Class ##
     
    # The script that will be using the dialog.
    def AnnotateCurve():
        curveId = rs.GetCurveObject("Select Curve");
        if curveId is None:
            print("no curve selected")
        else:
            location = rs.CurveStartPoint(curveId[0])
            if location is not None:
                dialog = SampleEtoCurveAnnotateDialog(str(curveId[0]));
                rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
                if (rc):
                    text = dialog.m_textbox.Text
                    if len(text) > 0:
                        # create a new text dot at the start of the curve
                        rs.AddTextDot(text, location)
     
    #########################################################################
    # Check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if __name__ == "__main__":
        AnnotateCurve()
    

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

