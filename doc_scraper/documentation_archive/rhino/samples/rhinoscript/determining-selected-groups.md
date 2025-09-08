---
url: https://developer.rhino3d.com/samples/rhinoscript/determining-selected-groups/
scraped_at: 2025-09-08T15:49:33.070560
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

Determining Selected Groups

__

Windows only

Demonstrates how to determine what object groups are selected using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Description
    '   Returns an array of objects group names
    '   from selected objects.
    ' Parameters
    '   none
    ' Returns
    '   An array of object group names or vbNull if none
    '   of the selected objects belongs to a group.
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function SelectedGroups()
    
      ' Declare locals
      Dim arrObjects, arrGroups(), strGroup
      Dim i, nCount, bAppend
    
      SelectedGroups = Null ' Default
      nCount = -1
    
      ' Get the selected objects  
      arrObjects = Rhino.SelectedObjects
      If Not IsArray(arrObjects) Then Exit Function
    
      ' Process each object. If the object belongs to an
      ' object group and that group name is not already
      ' in arrGroups, then append it to the end.    
      For i = 0 To UBound(arrObjects)
        bAppend = False
        strGroup = Rhino.ObjectTopGroup(arrObjects(i))
        If Not IsNull(strGroup) Then
          If (nCount = -1) Then
            bAppend = True
          ElseIf (FindGroup(strGroup, arrGroups) = -1) Then
            bAppend = True
          End If
          If bAppend = True Then
            nCount = nCount + 1
            ReDim Preserve arrGroups(nCount)
            arrGroups(nCount) = strGroup
          End If
        End If
      Next
    
      ' Return the array of group names    
      If (nCount > -1) Then SelectedGroups = arrGroups
    
    End Function
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Description
    '   Searches an array of strings
    ' Parameters
    '   strGroup - the name to look for
    '   arrGroups - the array to search
    ' Returns
    '   >= 0 if strGroup is found in arrGroups
    '   -1 otherwise      
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function FindGroup(strGroup, arrGroups)
      Dim i
      FindGroup = -1 ' Default
      For i = 0 To UBound(arrGroups)
        If (StrComp(strGroup, arrGroups(i), 1) = 0) Then
          FindGroup = i
          Exit Function
        End If
      Next
    End Function
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Test our SelectedGroups function
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub TestSelectedGroups
      Dim i, arrGroups
      arrGroups = SelectedGroups
      If IsArray(arrGroups) Then
        For i = 0 To UBound(arrGroups)
          Rhino.Print( arrGroups(i) )
        Next
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

