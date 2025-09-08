---
url: https://developer.rhino3d.com/guides/rhinoscript/offsetting-meshes/
scraped_at: 2025-09-08T15:42:51.502145
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

[Offsetting
Meshes](https://developer.rhino3d.com/guides/rhinoscript/offsetting-meshes/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Offsetting Meshes

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

RhinoScript can generate a closed mesh as a result of a base mesh and an
offset. Rhino’s _OffsetMesh_ command does this task very well if you use the
solidify option, but RhinoScript’s `MeshOffset` function does not have this
option. Let’s take a look at creating a solid mesh with RhinoScript…

## Solution

RhinoScript’s `MeshOffset` function does not have a solidify option, but you
can accomplish what you want by simply scripting Rhino’s _OffsetMesh_ command,
instead of calling RhinoScript’s `MeshOffset` function.

The following example function will offset a mesh by scripting Rhino’s
OffsetMesh command…

    
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Offset and solidify a mesh object
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function OffsetMeshSolidify(strMesh, dblDistance)
    
      ' Declare local variables
      Dim arrSaved, strCommand
    
      ' Save any selected objects
      arrSaved = Rhino.SelectedObjects
    
      ' Unselect all objects
      Rhino.UnSelectAllObjects
    
      ' Select the mesh
      Call Rhino.SelectObject(strMesh)
    
      ' Script the OffsetMesh command
      strCommand = "_-OffsetMesh _CapMeshes=_Yes " & CStr(dblDistance) & " _Enter"
      Call Rhino.Command(strCommand, 0)
    
      ' Get the results of the command
      If Rhino.LastCommandResult = 0 Then
        OffsetMeshSolidify = Rhino.LastCreatedObjects()(0)
      Else
        OffsetMeshSolidify = Null
      End If
    
      ' Unselect all objects
      Rhino.UnSelectAllObjects
    
      ' If any objects were selected before calling
      ' this function, re-select them
      If IsArray(arrSaved) Then Rhino.SelectObjects(arrSaved)
    
    End Function
    

You can test the above function with the following code…

    
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' This procedure tests the OffsetMeshSolidify function
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub TestOffsetMeshSolidify()
    
      ' Declare local constants and variables
      Const rhMesh = 32
      Dim strMesh, dblDistance, strOffset
    
      ' Select a mesh to offset
      strMesh = Rhino.GetObject("Select mesh to offset", rhMesh, True)
      If IsNull(strMesh) Then Exit Sub
    
      ' Get the offset distance
      dblDistance = Rhino.GetReal("Offset distance", 1.0)
      If IsNull(dblDistance) Then Exit Sub
      If (dblDistance = 0.0) Then Exit Sub
    
      ' Call our mesh offsetting function...
      strOffset = OffsetMeshSolidify(strMesh, dblDistance)
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/offsetting-
meshes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/offsetting-
meshes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

