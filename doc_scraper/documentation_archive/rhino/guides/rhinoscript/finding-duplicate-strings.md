---
url: https://developer.rhino3d.com/guides/rhinoscript/finding-duplicate-strings/
scraped_at: 2025-09-08T15:42:17.155753
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

[Finding Duplicate
Strings](https://developer.rhino3d.com/guides/rhinoscript/finding-duplicate-
strings/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Finding Duplicate Strings

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you have an array of strings which contains duplicates. RhinoScript
has a method to cull the duplicate strings. But rather than cull them, one
would like to find them with a routine that will return the indices of the
duplicate items.

Better yet, a routine that would return sets of indices, with each set
containing the indices of a particular string would solve the problem. For
example, if an array contained “Curve”, “Surface”, “curve”, “surface”, we
would like to have an array containing [0,2] and [1,3] returned.

## Solution

VBScript’s `Dictionary` is a useful tool for storing associative data, or data
in the form of (key, item) pairs. In the problem outlined above, you could use
a Dictionary to track each string and the indices where is appears in the
array. In other words, use a Dictionary to store (string, indices) pairs.

To store the indices, you are going to need an array. But creating and
resizing VBScript arrays is always a challenge. So, you might consider using a
.NET’s `ArrayList` object. A .NET `ArrayList` is a COM-enabled object, which
means it can be used in VBScript.

The following sample function demonstrates how you can use a `Dictionary` of
strings and .NET `ArrayList` objects to find the indices of duplicate string
items in an array.

    
    
    Function FindDuplicateStrings(arrStrings, blnCase)
    
      ' Local variables
      Dim objDict, strKey, objItem, arrItems
      Dim i, j, nCount
      Dim arrResults()
    
      ' Default return value
      FindDuplicateStrings = Null
    
      ' Create a dictionary object and set it's compare mode
      Set objDict = CreateObject("Scripting.Dictionary")
      If (blnCase = True) Then
        objDict.CompareMode = vbBinaryCompare
      Else
        objDict.CompareMode = vbTextCompare
      End If
    
      ' Process input strings. If the string is not in the dictionary,
      ' then add it and add it's index to the ArrayList. Otherwise,
      ' just add it's index to the dictionary item's existing ArrayList.
      For i = 0 To UBound(arrStrings)
        strKey = arrStrings(i)
        If Not objDict.Exists(strKey) Then
          objDict.Add strKey, CreateObject("System.Collections.ArrayList")
        End If      
        objDict(strKey).Add(i)
      Next
    
      ' Find all of the dictionary items that have more than one index.
      ' Add those arrays to our result array
      nCount = 0
      arrItems = objDict.Items
      For Each objItem In arrItems
        If (objItem.Count > 1) Then
          ReDim Preserve arrResults(nCount)    
          arrResults(nCount) = objItem.ToArray()
          nCount = nCount + 1
        End If
      Next
    
      ' Done!
      FindDuplicateStrings = arrResults
    
    End Function
    

Here is an example of how to use the above function:

    
    
    Sub TestFindDuplicateStrings
    
      Dim arrStrings, arrResults, arrItem, nItem, i
    
      arrStrings = Array("Curve" ,  _
                         "Surface", _
                         "Mesh",    _
                         "Point",   _
                         "Surface", _
                         "Curve",   _
                         "Curve")
    
      arrResults = FindDuplicateStrings(arrStrings, False)
      If IsArray(arrResults) Then
        Call Rhino.Print("Duplicate Sets = " & CStr(UBound(arrResults) + 1))
        For i = 0 To UBound(arrResults)
          Call Rhino.Print("Set = " & CStr(i + 1))
          arrItem = arrResults(i)
          For Each nItem In arrItem
            Call Rhino.Print("Item " & CStr(nItem) & " = " & arrStrings(nItem))
          Next
        Next
      End If
    
    End Sub
    

## Related Topics

  * [Array Utilities](https://developer.rhino3d.com/guides/rhinoscript/array-utilities/)
  * [Sorting VBScript Arrays with .NET](https://developer.rhino3d.com/guides/rhinoscript/sorting-vbs-arrays-with-net/)
  * [VBScript Dictionaries](https://developer.rhino3d.com/guides/rhinoscript/vbscript-dictionaries/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/finding-
duplicate-strings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/finding-
duplicate-strings/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

