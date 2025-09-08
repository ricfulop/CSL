---
url: https://developer.rhino3d.com/samples/rhinocommon/instance-definition-tree/
scraped_at: 2025-09-08T15:46:17.853677
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

Instance Definition Tree

Demonstrates how to list or enumerate the objects that make up a nested block
definition.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result InstanceDefinitionTree(RhinoDoc doc)
      {
        var instance_definitions = doc.InstanceDefinitions;
        var instance_definition_count = instance_definitions.Count;
    
        if (instance_definition_count == 0)
        {
          RhinoApp.WriteLine("Document contains no instance definitions.");
          return Result.Nothing;
        }
    
        var dump = new TextLog();
        dump.IndentSize = 4;
    
        for (int i = 0; i < instance_definition_count; i++)
          DumpInstanceDefinition(instance_definitions[i], ref dump, true);
    
        RhinoApp.WriteLine(dump.ToString());
    
        return Result.Success;
      }
    
      private static void DumpInstanceDefinition(InstanceDefinition instanceDefinition, ref TextLog dump, bool isRoot)
      {
        if (instanceDefinition != null && !instanceDefinition.IsDeleted)
        {
          string node = isRoot ? "─" : "└";
          dump.Print(string.Format("{0} Instance definition {1} = {2}\n", node, instanceDefinition.Index, instanceDefinition.Name));
    
          if (instanceDefinition.ObjectCount  > 0)
          {
            dump.PushIndent();
            for (int i = 0; i < instanceDefinition.ObjectCount ; i++)
            {
              var obj = instanceDefinition.Object(i);
              if (obj == null) continue;
              if (obj is InstanceObject)
                DumpInstanceDefinition((obj as InstanceObject).InstanceDefinition, ref dump, false); // Recursive...
              else
                dump.Print("\u2514 Object {0} = {1}\n", i, obj.ShortDescription(false));
            }
            dump.PopIndent();
          }
        }
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function InstanceDefinitionTree(ByVal doc As RhinoDoc) As Result
    	Dim instance_definitions = doc.InstanceDefinitions
    	Dim instance_definition_count = instance_definitions.Count
    
    	If instance_definition_count = 0 Then
    	  RhinoApp.WriteLine("Document contains no instance definitions.")
    	  Return Result.Nothing
    	End If
    
    	Dim dump = New TextLog()
    	dump.IndentSize = 4
    
    	For i As Integer = 0 To instance_definition_count - 1
    	  DumpInstanceDefinition(instance_definitions(i), dump, True)
    	Next i
    
    	RhinoApp.WriteLine(dump.ToString())
    
    	Return Result.Success
      End Function
    
      Private Shared Sub DumpInstanceDefinition(ByVal instanceDefinition As InstanceDefinition, ByRef dump As TextLog, ByVal isRoot As Boolean)
    	If instanceDefinition IsNot Nothing AndAlso Not instanceDefinition.IsDeleted Then
    	  Dim node As String = If(isRoot, "─", "└")
    	  dump.Print(String.Format("{0} Instance definition {1} = {2}" & ControlChars.Lf, node, instanceDefinition.Index, instanceDefinition.Name))
    
    	  If instanceDefinition.ObjectCount > 0 Then
    		dump.PushIndent()
    		For i As Integer = 0 To instanceDefinition.ObjectCount - 1
    		  Dim obj = instanceDefinition.Object(i)
    		  If obj Is Nothing Then
    			  Continue For
    		  End If
    		  If TypeOf obj Is InstanceObject Then
    			DumpInstanceDefinition((TryCast(obj, InstanceObject)).InstanceDefinition, dump, False) ' Recursive...
    		  Else
    			dump.Print(ChrW(&H2514).ToString() & " Object {0} = {1}" & ControlChars.Lf, i, obj.ShortDescription(False))
    		  End If
    		Next i
    		dump.PopIndent()
    	  End If
    	End If
      End Sub
    End Class
    
    
    
    from scriptcontext import doc
    import Rhino
    
    def RunCommand():
        instanceDefinitions = doc.InstanceDefinitions
        instanceDefinitionCount = instanceDefinitions.Count
    
        if instanceDefinitionCount == 0:
            print "Document contains no instance definitions."
            return
    
        dump = Rhino.FileIO.TextLog()
        dump.IndentSize = 4
    
        for i in range(0, instanceDefinitionCount):
            DumpInstanceDefinition(instanceDefinitions[i], dump, True)
    
        print dump.ToString()
    
    def DumpInstanceDefinition(instanceDefinition, dump, isRoot):
        if instanceDefinition != None and not instanceDefinition.IsDeleted:
            if isRoot:
                node = '-'
            else:
                node = '+'
            dump.Print(u"{0} Instance definition {1} = {2}\n".format(node, instanceDefinition.Index, instanceDefinition.Name))
    
            if instanceDefinition.ObjectCount  > 0:
                dump.PushIndent()
                for i in range(0, instanceDefinition.ObjectCount):
                    obj = instanceDefinition.Object(i)
                    if obj != None and type(obj) == Rhino.DocObjects.InstanceObject:
                        DumpInstanceDefinition(obj.InstanceDefinition, dump, False) # Recursive...
                    else:
                        dump.Print(u"+ Object {0} = {1}\n".format(i, obj.ShortDescription(False)))
                dump.PopIndent()
    
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

