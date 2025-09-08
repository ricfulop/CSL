---
url: https://developer.rhino3d.com/samples/rhinoscript/exporting-meshes-to-geomview/
scraped_at: 2025-09-08T15:50:15.235098
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

Exporting Meshes to Geomview

__

Windows only

Demonstrates how to export a mesh object to Geomview's OFF file format using
RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ExportOff.rvb -- February 2009
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Exports a mesh object to a Geomview .OFF file
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ExportOff
    
      ' Local variables
      Dim strMesh, strFilter, strFileName
      Dim objFSO, objStream, i
      Dim v_count, v_list, v
      Dim f_count, f_list, f
    
      ' Pick a mesh object
      strMesh = Rhino.GetObject("Select mesh", 32)
      If IsNull(strMesh) Then Exit Sub
    
      ' Prompt the user to specify a file name    
      strFilter = "Geomview OFF (*.off)|*.off|"
      strFileName = Rhino.SaveFileName("Save As", strFilter)
      If IsNull(strFileName) Then Exit Sub
    
      ' Get the file system object
      Set objFSO = CreateObject("Scripting.FileSystemObject")
    
      ' Open a text file to write to
      On Error Resume Next
      Set objStream = objFSO.CreateTextFile(strFileName, True)
      If Err Then
        MsgBox Err.Description
        Exit Sub
      End If
    
      ' Write the header
      objStream.WriteLine("OFF")
      objStream.WriteLine("#")
      objStream.WriteLine("# " & strFileName)
      objStream.WriteLine("#")
    
      ' Write the vertex, face, and edge counts
      v_count = Rhino.MeshVertexCount(strMesh)
      f_count = Rhino.MeshFaceCount(strMesh)
      objStream.WriteLine(CStr(v_count) & " " & CStr(f_count) & " " & CStr(v_count*f_count))
    
      ' Write the vertices
      v_list = Rhino.MeshVertices(strMesh)
      For Each v In v_list
        objStream.WriteLine(CStr(v(0)) & " " & CStr(v(1)) & " " & CStr(v(2)))
      Next
    
      ' Write the faces
      f_list = Rhino.MeshFaceVertices(strMesh)
      For Each f In f_list
        If f(2) = f(3) Then
          objStream.WriteLine(CStr(3) & " " & CStr(f(0)) & " " & CStr(f(1)) & " " & CStr(f(2)))
        Else
          objStream.WriteLine(CStr(4) & " " & CStr(f(0)) & " " & CStr(f(1)) & " " & CStr(f(2)) & " " & CStr(f(3)))
        End If
      Next
    
      ' Close the file
      objStream.Close
    
      End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Rhino.AddStartupScript Rhino.LastLoadedScriptFile
    Rhino.AddAlias "ExportOff", "_NoEcho _-RunScript (ExportOff)"
    

  

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

