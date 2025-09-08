---
url: https://developer.rhino3d.com/samples/rhinocommon/instance-archive-file-status/
scraped_at: 2025-09-08T15:46:15.825629
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

Instance Archive File Status

Demonstrates how to find the status of a file that contains an instance
(block) definition.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result InstanceArchiveFileStatus(Rhino.RhinoDoc doc)
      {
        for (int i = 0; i < doc.InstanceDefinitions.Count; i++)
        {
          Rhino.DocObjects.InstanceDefinition iDef = doc.InstanceDefinitions[i];
          Rhino.DocObjects.InstanceDefinitionArchiveFileStatus iDefStatus = iDef.ArchiveFileStatus;
    
          string status = "Unknown";
          switch (iDefStatus)
          {
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.NotALinkedInstanceDefinition:
              status = "not a linked instance definition.";
              break;
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotReadable:
              status = "archive file is not readable.";
              break;
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotFound:
              status = "archive file cannot be found.";
              break;
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsUpToDate:
              status = "archive file is up-to-date.";
              break;
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsNewer:
              status = "archive file is newer.";
              break;
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsOlder:
              status = "archive file is older.";
              break;
            case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsDifferent:
              status = "archive file is different.";
              break;
          }
    
          Rhino.RhinoApp.WriteLine("{0} - {1}", iDef.Name, status);
        }
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function InstanceArchiveFileStatus(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	For i As Integer = 0 To doc.InstanceDefinitions.Count - 1
    	  Dim iDef As Rhino.DocObjects.InstanceDefinition = doc.InstanceDefinitions(i)
    	  Dim iDefStatus As Rhino.DocObjects.InstanceDefinitionArchiveFileStatus = iDef.ArchiveFileStatus
    
    	  Dim status As String = "Unknown"
    	  Select Case iDefStatus
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.NotALinkedInstanceDefinition
    		  status = "not a linked instance definition."
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotReadable
    		  status = "archive file is not readable."
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotFound
    		  status = "archive file cannot be found."
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsUpToDate
    		  status = "archive file is up-to-date."
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsNewer
    		  status = "archive file is newer."
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsOlder
    		  status = "archive file is older."
    		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsDifferent
    		  status = "archive file is different."
    	  End Select
    
    	  Rhino.RhinoApp.WriteLine("{0} - {1}", iDef.Name, status)
    	Next i
    
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    # No Python sample available
    

  

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

