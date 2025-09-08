---
url: https://developer.rhino3d.com/guides/rhinoscript/replacing-points-with-blocks/
scraped_at: 2025-09-08T15:42:58.428888
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

[Replacing Points with
Blocks](https://developer.rhino3d.com/guides/rhinoscript/replacing-points-
with-blocks/)

  * Problem
  * Solution
  * Inverse

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Replacing Points with Blocks

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Imagine you have a number of point objects in your model and you would like to
replace them with a block so they appear as markers. How can this be done
without running the Insert command a bunch of times?

## Solution

The following sample code demonstrates how to replace point objects with block
objects using RhinoScript…

    
    
    ' Replaces points with blocks
    Sub ReplacePointsWithBlocks
    
      ' Select points to replace with a block
      Dim arrObjects
      arrObjects = Rhino.GetObjects("Select points to replace with a block", 1, True, True)
      If Not IsArray(arrObjects) Then Exit Sub
    
      ' Get the names of all block definitions in the document    
      Dim arrBlocks
      arrBlocks = Rhino.BlockNames(True)
      If Not IsArray(arrBlocks) Then
        Rhino.Print "No block definitions found in the document."
        Exit Sub
      End If
    
      ' Select a block name from a list
      Dim strBlock
      strBlock = Rhino.ListBox(arrBlocks, "Select block", "Replace Points")
      If IsNull(strBlock) Then Exit Sub
    
      ' Turn off redrawing (faster)
      Rhino.EnableRedraw True      
    
      ' Process each selected point object
      Dim strObject, arrPoint
      For Each strObject In arrObjects
        ' Get the point object's coordinates
        arrPoint = Rhino.PointCoordinates(strObject)
        ' Insert the block at that location
        Rhino.InsertBlock strBlock, arrPoint
      Next
    
      ' Delete all of the point objects
      Rhino.DeleteObjects arrObjects   
    
      ' Turn redrawing back on     
      Rhino.EnableRedraw True      
    
    End Sub
    

## Inverse

The following script will do just the opposite - it will replace block objects
with point objects…

    
    
    ' Replaces blocks with points
    Sub ReplaceBlocksWithPoints
    
      ' Select blocks to replace with points
      Dim arrObjects
      arrObjects = Rhino.GetObjects("Select blocks to replace with points", 4096, True, True)
      If Not IsArray(arrObjects) Then Exit Sub
    
      ' Turn off redrawing (faster)
      Rhino.EnableRedraw True      
    
      ' Process each selected block object
      Dim strObject, arrPoint
      For Each strObject In arrObjects
        ' Get the block's insertion point
        arrPoint = Rhino.BlockInstanceInsertPoint(strObject)
        ' Add a point object at that location
        Rhino.AddPoint arrPoint
      Next
    
      ' Delete all of the block objects
      Rhino.DeleteObjects arrObjects   
    
      ' Turn redrawing back on     
      Rhino.EnableRedraw True      
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/replacing-
points-with-blocks/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/replacing-
points-with-blocks/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

