---
url: https://developer.rhino3d.com/samples/rhinocommon/mesh-volume/
scraped_at: 2025-09-08T15:46:23.723516
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

Mesh Volume

Demonstrates how to calculate the volume of a user-specified closed mesh.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result MeshVolume(RhinoDoc doc)
      {
        var gm = new GetObject();
        gm.SetCommandPrompt("Select solid meshes for volume calculation");
        gm.GeometryFilter = ObjectType.Mesh;
        gm.GeometryAttributeFilter = GeometryAttributeFilter.ClosedMesh;
        gm.SubObjectSelect = false;
        gm.GroupSelect = true;
        gm.GetMultiple(1, 0);
        if (gm.CommandResult() != Result.Success)
          return gm.CommandResult();
    
        double volume = 0.0;
        double volume_error = 0.0;
        foreach (var obj_ref in gm.Objects())
        {
          if (obj_ref.Mesh() != null)
          {
            var mass_properties = VolumeMassProperties.Compute(obj_ref.Mesh());
            if (mass_properties != null)
            {
              volume += mass_properties.Volume;
              volume_error += mass_properties.VolumeError;
            }
          }
        }
    
        RhinoApp.WriteLine("Total volume = {0:f} (+/- {1:f})", volume, volume_error);
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function MeshVolume(ByVal doc As RhinoDoc) As Result
    	Dim gm = New GetObject()
    	gm.SetCommandPrompt("Select solid meshes for volume calculation")
    	gm.GeometryFilter = ObjectType.Mesh
    	gm.GeometryAttributeFilter = GeometryAttributeFilter.ClosedMesh
    	gm.SubObjectSelect = False
    	gm.GroupSelect = True
    	gm.GetMultiple(1, 0)
    	If gm.CommandResult() <> Result.Success Then
    	  Return gm.CommandResult()
    	End If
    
    	Dim volume As Double = 0.0
    	Dim volume_error As Double = 0.0
    	For Each obj_ref In gm.Objects()
    	  If obj_ref.Mesh() IsNot Nothing Then
    		Dim mass_properties = VolumeMassProperties.Compute(obj_ref.Mesh())
    		If mass_properties IsNot Nothing Then
    		  volume += mass_properties.Volume
    		  volume_error += mass_properties.VolumeError
    		End If
    	  End If
    	Next obj_ref
    
    	RhinoApp.WriteLine("Total volume = {0:f} (+/- {1:f})", volume, volume_error)
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino.Input.Custom import *
    from Rhino.DocObjects import ObjectType
    from Rhino.Geometry import *
    from Rhino.Commands import Result
    
    def RunCommand():
        gm = GetObject()
        gm.SetCommandPrompt("Select solid meshes for volume calculation")
        gm.GeometryFilter = ObjectType.Mesh
        gm.GeometryAttributeFilter = GeometryAttributeFilter.ClosedMesh
        gm.SubObjectSelect = False
        gm.GroupSelect = True
        gm.GetMultiple(1, 0)
        if gm.CommandResult() != Result.Success:
            return gm.CommandResult()
    
        volume = 0.0
        volume_error = 0.0
        for obj_ref in gm.Objects():
            if obj_ref.Mesh() != None:
                mass_properties = VolumeMassProperties.Compute(obj_ref.Mesh())
                if mass_properties != None:
                    volume += mass_properties.Volume
                    volume_error += mass_properties.VolumeError
    
        print "Total volume = {0:f} (+/- {1:f})".format(volume, volume_error)
        return Result.Success
    
    if __name__ == "__main__":
        RunCommand()
    

  

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

