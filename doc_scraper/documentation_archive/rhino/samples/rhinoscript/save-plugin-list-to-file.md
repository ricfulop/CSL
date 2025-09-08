---
url: https://developer.rhino3d.com/samples/rhinoscript/save-plugin-list-to-file/
scraped_at: 2025-09-08T15:50:30.305333
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

Save Plugin List to File

__

Windows only

Demonstrates how to save the names of loaded and unloaded plugins to a text
file using RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' SavePlugInInfo.rvb -- April 2008
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    
    Option Explicit
    
    Sub SavePlugInInfo()
    
      Dim objShell, objNetwork, objFSO, objFolder, objStream
      Dim arrPlugIns, arrSorted, strPlugIn, strDesktop, strFile, strName, strMsg
    
      Set objShell = CreateObject("WScript.Shell")
      Set objNetwork = CreateObject("WScript.Network")
      Set objFSO = CreateObject("Scripting.FileSystemObject")
    
      strName = "RhinoPlugInInfo.txt"
      strDesktop = objShell.SpecialFolders("Desktop")
      strFile = strDeskTop & "\" & strName
    
      'On Error Resume Next
      Set objStream = objFSO.CreateTextFile(strFile, True)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If
    
      objStream.WriteLine "**************************"
      objStream.WriteLine "Rhino Plug-in Info"
      objStream.WriteLine
      objStream.WriteLine "Computer Name = " & objNetwork.ComputerName
      objStream.WriteLine "Date and Time = " & CStr(Now)
      objStream.WriteLine "Rhino Build Date = " & CStr(Rhino.BuildDate)
      objStream.WriteLine "Rhino SDK Version = " & CStr(Rhino.SdkVersion)
      objStream.WriteLine "**************************"
      objStream.WriteLine
    
      objStream.WriteLine "**************************"
      objStream.WriteLine "Loaded Plug-ins"
      objStream.WriteLine "**************************"
      objStream.WriteLine
    
      arrPlugIns = Rhino.PlugIns(0, 1)
      If IsArray(arrPlugIns) Then
        arrSorted = Rhino.SortStrings(arrPlugIns)
        For Each strPlugIn In arrSorted
          objStream.WriteLine strPlugIn
        Next
      End If
    
      objStream.WriteLine
      objStream.WriteLine "**************************"
      objStream.WriteLine "Unloaded Plug-ins"
      objStream.WriteLine "**************************"
      objStream.WriteLine
    
      arrPlugIns = Rhino.PlugIns(0, 2)
      If IsArray(arrPlugIns) Then
        arrSorted = Rhino.SortStrings(arrPlugIns)
        For Each strPlugIn In arrSorted
          objStream.WriteLine strPlugIn
        Next
      End If
    
      objStream.Close
    
      strMsg = "A file named " & Chr(34) & strName & Chr(34) & VbCrLf
      strMsg = strMsg & "has been saved to your desktop." & VbCrLf & VbCrLf
      strMsg = strMsg & "If you are experiencing problems with Rhino," & VbCrLf
      strMsg = strMsg & "email this file to " & Chr(34) & "tech@mcneel.com" & Chr(34) & VbCrLf
      strMsg = strMsg & "along with a detailed description" & VbCrLf
      strMsg = strMsg & "of your problem."
      MsgBox strMsg, 64, "Rhinoceros"
    
    End Sub
    
    ' Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
    ' Rhino.AddAlias "SavePlugInInfo", "_-RunScript (SavePlugInInfo)"
    
    ' Run it!
    Call SavePlugInInfo
    

  

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

