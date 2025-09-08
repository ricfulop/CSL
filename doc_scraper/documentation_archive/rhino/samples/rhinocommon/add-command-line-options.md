---
url: https://developer.rhino3d.com/samples/rhinocommon/add-command-line-options/
scraped_at: 2025-09-08T15:44:19.314801
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

Add Command Line Options

Demonstrates how to add command-line options as inputs to your command.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result CommandLineOptions(Rhino.RhinoDoc doc)
      {
        // For this example we will use a GetPoint class, but all of the custom
        // "Get" classes support command line options.
        Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
        gp.SetCommandPrompt("GetPoint with options");
    
        // set up the options
        Rhino.Input.Custom.OptionInteger intOption = new Rhino.Input.Custom.OptionInteger(1, 1, 99);
        Rhino.Input.Custom.OptionDouble dblOption = new Rhino.Input.Custom.OptionDouble(2.2, 0, 99.9);
        Rhino.Input.Custom.OptionToggle boolOption = new Rhino.Input.Custom.OptionToggle(true, "Off", "On");
        string[] listValues = new string[] { "Item0", "Item1", "Item2", "Item3", "Item4" };
    
        gp.AddOptionInteger("Integer", ref intOption);
        gp.AddOptionDouble("Double", ref dblOption);
        gp.AddOptionToggle("Boolean", ref boolOption);
        int listIndex = 3;
        int opList = gp.AddOptionList("List", listValues, listIndex);
    
        while (true)
        {
          // perform the get operation. This will prompt the user to input a point, but also
          // allow for command line options defined above
          Rhino.Input.GetResult get_rc = gp.Get();
          if (gp.CommandResult() != Rhino.Commands.Result.Success)
            return gp.CommandResult();
    
          if (get_rc == Rhino.Input.GetResult.Point)
          {
            doc.Objects.AddPoint(gp.Point());
            doc.Views.Redraw();
            Rhino.RhinoApp.WriteLine("Command line option values are");
            Rhino.RhinoApp.WriteLine(" Integer = {0}", intOption.CurrentValue);
            Rhino.RhinoApp.WriteLine(" Double = {0}", dblOption.CurrentValue);
            Rhino.RhinoApp.WriteLine(" Boolean = {0}", boolOption.CurrentValue);
            Rhino.RhinoApp.WriteLine(" List = {0}", listValues[listIndex]);
          }
          else if (get_rc == Rhino.Input.GetResult.Option)
          {
            if (gp.OptionIndex() == opList)
              listIndex = gp.Option().CurrentListOptionIndex;
            continue;
          }
          break;
        }
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function CommandLineOptions(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' For this example we will use a GetPoint class, but all of the custom
    	' "Get" classes support command line options.
    	Dim gp As New Rhino.Input.Custom.GetPoint()
    	gp.SetCommandPrompt("GetPoint with options")
    
    	' set up the options
    	Dim intOption As New Rhino.Input.Custom.OptionInteger(1, 1, 99)
    	Dim dblOption As New Rhino.Input.Custom.OptionDouble(2.2, 0, 99.9)
    	Dim boolOption As New Rhino.Input.Custom.OptionToggle(True, "Off", "On")
    	Dim listValues() As String = { "Item0", "Item1", "Item2", "Item3", "Item4" }
    
    	gp.AddOptionInteger("Integer", intOption)
    	gp.AddOptionDouble("Double", dblOption)
    	gp.AddOptionToggle("Boolean", boolOption)
    	Dim listIndex As Integer = 3
    	Dim opList As Integer = gp.AddOptionList("List", listValues, listIndex)
    
    	Do
    	  ' perform the get operation. This will prompt the user to input a point, but also
    	  ' allow for command line options defined above
    	  Dim get_rc As Rhino.Input.GetResult = gp.Get()
    	  If gp.CommandResult() <> Rhino.Commands.Result.Success Then
    		Return gp.CommandResult()
    	  End If
    
    	  If get_rc Is Rhino.Input.GetResult.Point Then
    		doc.Objects.AddPoint(gp.Point())
    		doc.Views.Redraw()
    		Rhino.RhinoApp.WriteLine("Command line option values are")
    		Rhino.RhinoApp.WriteLine(" Integer = {0}", intOption.CurrentValue)
    		Rhino.RhinoApp.WriteLine(" Double = {0}", dblOption.CurrentValue)
    		Rhino.RhinoApp.WriteLine(" Boolean = {0}", boolOption.CurrentValue)
    		Rhino.RhinoApp.WriteLine(" List = {0}", listValues(listIndex))
    	  ElseIf get_rc Is Rhino.Input.GetResult.Option Then
    		If gp.OptionIndex() = opList Then
    		  listIndex = gp.Option().CurrentListOptionIndex
    		End If
    		Continue Do
    	  End If
    	  Exit Do
    	Loop
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def CommandLineOptions():
        # For this example we will use a GetPoint class, but all of the custom
        # "Get" classes support command line options.
        gp = Rhino.Input.Custom.GetPoint()
        gp.SetCommandPrompt("GetPoint with options")
    
        # set up the options
        intOption = Rhino.Input.Custom.OptionInteger(1, 1, 99)
        dblOption = Rhino.Input.Custom.OptionDouble(2.2, 0, 99.9)
        boolOption = Rhino.Input.Custom.OptionToggle(True, "Off", "On")
        listValues = "Item0", "Item1", "Item2", "Item3", "Item4"
    
        gp.AddOptionInteger("Integer", intOption)
        gp.AddOptionDouble("Double", dblOption)
        gp.AddOptionToggle("Boolean", boolOption)
        listIndex = 3
        opList = gp.AddOptionList("List", listValues, listIndex)
        while True:
            # perform the get operation. This will prompt the user to
            # input a point, but also allow for command line options
            # defined above
            get_rc = gp.Get()
            if gp.CommandResult()!=Rhino.Commands.Result.Success:
                return gp.CommandResult()
            if get_rc==Rhino.Input.GetResult.Point:
                point = gp.Point()
                scriptcontext.doc.Objects.AddPoint(point)
                scriptcontext.doc.Views.Redraw()
                print "Command line option values are"
                print " Integer =", intOption.CurrentValue
                print " Double =", dblOption.CurrentValue
                print " Boolean =", boolOption.CurrentValue
                print " List =", listValues[listIndex]
            elif get_rc==Rhino.Input.GetResult.Option:
                if gp.OptionIndex()==opList:
                    listIndex = gp.Option().CurrentListOptionIndex
                continue
            break
        return Rhino.Commands.Result.Success
    
    
    if __name__ == "__main__":
        CommandLineOptions()
    

  

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

