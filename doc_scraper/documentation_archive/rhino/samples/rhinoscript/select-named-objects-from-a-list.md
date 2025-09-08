---
url: https://developer.rhino3d.com/samples/rhinoscript/select-named-objects-from-a-list/
scraped_at: 2025-09-08T15:49:35.961389
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

Select Named Objects from a List

__

Windows only

Demonstrates how to use a dialog box to select named objects using
RhinoScript.

VBScript

    
    
    Option Explicit
    
    Sub SelNamedObjects
    
      ' Get all the objects in the document
      Dim arrAll
      arrAll = Rhino.AllObjects
      If Not IsArray(arrAll) Then
        Rhino.Print "No objects added to selection."
        Exit Sub
      End If
    
      ' Find all of the object names    
      Dim arrNames(), strName, nBound, i
      nBound = 0
      For i = 0 To UBound(arrAll)
        strName = Rhino.ObjectName(arrAll(i))
        If Not IsNull(strName) Then
          ReDim Preserve arrNames(nBound)
          arrNames(nBound) = strName
          nBound = nBound + 1
        End If
      Next
    
      ' Exit if no names found
      If nBound = 0 Then
        Rhino.Print "No objects added to selection."
        Exit Sub
      End If
    
      ' Cull the duplicate names    
      Dim arrCulled
      arrCulled = Rhino.CullDuplicateStrings(arrNames)  
    
      ' Sort the list alphabetically  
      Dim arrSorted
      arrSorted = Rhino.Sort(arrCulled) 'Error =>SortStrings
    
      ' Select one or more objects names from a list    
      Dim arrSelected
      arrSelected = Rhino.MultiListBox(arrSorted, "Object names to select", "Select Named Objects")
      If Not IsArray(arrSelected) Then Exit Sub
    
      ' Select, and count, the objects
      Dim arrObjs, nCount
      nCount = 0
      For i = 0 To UBound(arrSelected)    
        arrObjs = Rhino.ObjectsByName(arrSelected(i), True)
        If IsArray(arrObjs) Then
          nCount = nCount + UBound(arrObjs) + 1
        End If
      Next
    
      'Print report to commandline
      If nCount = 0 Then
        Rhino.Print "No objects added to selection."
      ElseIf nCount = 1 Then
        Rhino.Print "1 object added to selection."
      Else
        Rhino.Print CStr(nCount) & " objects added to selection."
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

