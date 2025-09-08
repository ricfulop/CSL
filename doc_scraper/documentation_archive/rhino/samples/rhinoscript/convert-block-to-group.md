---
url: https://developer.rhino3d.com/samples/rhinoscript/convert-block-to-group/
scraped_at: 2025-09-08T15:49:06.831172
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

Convert Block to Group

__

Windows only

Demonstrates how to explode a block and group its components using
RhinoScript.

VBScript

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' ConvertBlockToGroup.rvb -- March 2010
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Main procedure for script
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ConvertBlockToGroup()
    
      ' Local variables
      Dim arrBlocks, strBlock, arrObjects(), nBound
    
      ' Get blocks to explode
      arrBlocks = Rhino.GetObjects("Select blocks to convert", 4096, True, True)
      If IsNull(arrBlocks) Then Exit Sub
    
      ' Explode the blocks    
      For Each strBlock In arrBlocks  
        ' Reset our array of objects
        ReDim arrObjects(-1)  
        ' Explode the block
        Call BlockExplode(strBlock, arrObjects)
        ' See if any objects were added to our array
        On Error Resume Next
        nBound = UBound(arrObjects)
        If (Err.Number = 0) Then
          ' Group the objects
          Call Rhino.AddObjectsToGroup(arrObjects, Rhino.AddGroup())
        End If
      Next
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Explodes a block and all of its nested blocks
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub BlockExplode(ByVal strBlock, ByRef arrObjects)
    
     ' Local variables
     Dim arrExplodes, strExplode
    
     ' Explode the block
     If Rhino.IsBlockInstance(strBlock) Then
       arrExplodes = Rhino.ExplodeBlockInstance(strBlock)
       If IsArray(arrExplodes) Then
         For Each strExplode In arrExplodes
           ' Recusive call...
           Call BlockExplode(strExplode, arrObjects)
         Next
       End If
     Else
       ' Add the object to our array
       Call ArrayAdd(arrObjects, strBlock)   
     End If
    
    End Sub
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Adds a new element to the end of an array
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub ArrayAdd(ByRef arr, ByVal val)
      Dim ub
      If IsArray(arr) Then
       On Error Resume Next
       ub = UBound(arr)
       If Err.Number <> 0 Then ub = -1
       ReDim Preserve arr(ub + 1)
       arr(UBound(arr)) = val
      End If
    End Sub
    

  

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

