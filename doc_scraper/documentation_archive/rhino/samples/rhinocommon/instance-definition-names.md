---
url: https://developer.rhino3d.com/samples/rhinocommon/instance-definition-names/
scraped_at: 2025-09-08T15:46:16.814308
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

Instance Definition Names

Demonstrates how to print the instance definition names.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result InstanceDefinitionNames(RhinoDoc doc)
      {
        var instance-definition-names = (from instance_definition in doc.InstanceDefinitions
                                         where instance_definition != null && !instance_definition.IsDeleted
                                         select instance_definition.Name);
    
        foreach (var n in instance-definition-names)
          RhinoApp.WriteLine("Instance definition = {0}", n);
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function InstanceDefinitionNames(ByVal doc As RhinoDoc) As Result
    	Dim instance-definition-names = (
    	    From instance_definition In doc.InstanceDefinitions
    	    Where instance_definition IsNot Nothing AndAlso Not instance_definition.IsDeleted
    	    Select instance_definition.Name)
    
    	For Each n In instance-definition-names
    	  RhinoApp.WriteLine("Instance definition = {0}", n)
    	Next n
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    from scriptcontext import doc
    
    def RunCommand():
        instanceDefinitionNames = [instanceDefinition.Name for instanceDefinition in doc.InstanceDefinitions if instanceDefinition != None and not instanceDefinition.IsDeleted]
    
        for n in instanceDefinitionNames:
            print "instance definition = {0}".format(n)
    
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

