---
url: https://developer.rhino3d.com/samples/rhinocommon/delete-block-instance-definition/
scraped_at: 2025-09-08T15:45:01.498954
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

Delete Block Instance Definition

Demonstrates how to delete a block instance definition given the name of the
block.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DeleteBlock(RhinoDoc doc)
      {
        // Get the name of the instance definition to rename
        string instance_definition_name = "";
        var rc = RhinoGet.GetString("Name of block to delete", true, ref instance_definition_name);
        if (rc != Result.Success)
          return rc;
        if (string.IsNullOrWhiteSpace(instance_definition_name))
          return Result.Nothing;
    
        // Verify instance definition exists
        var instance_definition = doc.InstanceDefinitions.Find(instance_definition_name, true);
        if (instance_definition == null) {
          RhinoApp.WriteLine("Block \"{0}\" not found.", instance_definition_name);
          return Result.Nothing;
        }
    
        // Verify instance definition can be deleted
        if (instance_definition.IsReference) {
          RhinoApp.WriteLine("Unable to delete block \"{0}\".", instance_definition_name);
          return Result.Nothing;
        }
    
        // delete block and all references
        if (!doc.InstanceDefinitions.Delete(instance_definition.Index, true, true)) {
          RhinoApp.WriteLine("Could not delete {0} block", instance_definition.Name);
          return Result.Failure;
        }
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DeleteBlock(ByVal doc As RhinoDoc) As Result
    	' Get the name of the instance definition to rename
    	Dim instance_definition_name As String = ""
    	Dim rc = RhinoGet.GetString("Name of block to delete", True, instance_definition_name)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	If String.IsNullOrWhiteSpace(instance_definition_name) Then
    	  Return Result.Nothing
    	End If
    
    	' Verify instance definition exists
    	Dim instance_definition = doc.InstanceDefinitions.Find(instance_definition_name, True)
    	If instance_definition Is Nothing Then
    	  RhinoApp.WriteLine("Block ""{0}"" not found.", instance_definition_name)
    	  Return Result.Nothing
    	End If
    
    	' Verify instance definition can be deleted
    	If instance_definition.IsReference Then
    	  RhinoApp.WriteLine("Unable to delete block ""{0}"".", instance_definition_name)
    	  Return Result.Nothing
    	End If
    
    	' delete block and all references
    	If Not doc.InstanceDefinitions.Delete(instance_definition.Index, True, True) Then
    	  RhinoApp.WriteLine("Could not delete {0} block", instance_definition.Name)
    	  Return Result.Failure
    	End If
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    
    def Delete():
        blockName = rs.GetString("block to delete")
        instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
        if not instanceDefinition:
            print "{0} block does not exist".format(blockName)
            return
    
        rs.DeleteBlock(blockName)
    
    if __name__ == "__main__":
        Delete()
    

  

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

