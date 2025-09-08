---
url: https://developer.rhino3d.com/guides/rhinoscript/disconnected-recordset-sorting/
scraped_at: 2025-09-08T15:42:41.370322
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

[Disconnected Recordset
Sorting](https://developer.rhino3d.com/guides/rhinoscript/disconnected-
recordset-sorting/)

  * Overview
  * Example
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Disconnected Recordset Sorting

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

If you are dealing with data which requires more than just key-value pairs and
fits best in 2-D array, and you wanted to perform sorting and filtering on it,
then Disconnected Recordsets will be an excellent option.

A disconnected recordset is essentially a database that exists only in memory;
it is not tied to a physical database. You create the recordset, add records
to it, and then manipulate the data, just like any other recordset. The only
difference is that the moment the script terminates, the recordset, which is
stored only in memory, disappears as well.

To use a disconnected recordset to sort data, you must first create the
recordset, adding any fields needed to store the data. After you have created
the fields, you then use the `AddNew` method to add new records to the
recordset, using the same process used to add new records to a physical
database. After the recordset has been populated, a single line of code can
then `Sort` the data on the specified field or fields.

## Example

The following example demonstrates how to sort an array of 3D points in
ascending x, y, z order. The code can be quickly modified to sort the point in
any order by simply modifying the `Sort` statement…

    
    
    Sub SortPoints
    
      ' Local constants
      Const adDouble = 5
    
      ' Local variables
      Dim arrPoints, arrPoint, x, y, z
      Dim objRecordSet
    
      ' Get the coordinates of selected point objects
      arrPoints = Rhino.GetPointCoordinates
      If IsNull(arrPoints) Then Exit Sub
    
      ' Create a disconnected recordset object
      Set objRecordSet = CreateObject("ADODB.Recordset")
    
      ' Define the fields of the recordset
      Call objRecordSet.Fields.Append("X", adDouble)
      Call objRecordSet.Fields.Append("Y", adDouble)
      Call objRecordSet.Fields.Append("Z", adDouble)
    
      ' Open the recordset
      objRecordSet.Open
    
      ' Add the curve data to the recordset
      For Each arrPoint In arrPoints
        objRecordSet.AddNew
        objRecordSet("X").Value = arrPoint(0)
        objRecordSet("Y").Value = arrPoint(1)
        objRecordSet("Z").Value = arrPoint(2)
        objRecordSet.Update
      Next
    
      ' Sort the recordset by x,y,z in ascending order
      objRecordSet.Sort = "X ASC, Y ASC, Z ASC"
    
      ' Iterate through the sorted recordset and print each record's values
      objRecordSet.MoveFirst
      Do Until objRecordSet.EOF
        x = objRecordSet("X").Value
        y = objRecordSet("Y").Value
        z = objRecordSet("Z").Value
        Call Rhino.Print(Rhino.Pt2Str(Array(x, y, z)))
        objRecordSet.MoveNext
      Loop
    
      objRecordSet.Close
    
    End Sub
    

## Related Topics

  * [Recordset Object (ADO) on MSDN](http://msdn.microsoft.com/en-us/library/windows/desktop/ms681510%28v=vs.85%29.aspx)
  * [Use a disconnected recordset to sort large data sets in VBScript on Microsoft Technet](http://technet.microsoft.com/en-us/magazine/2008.09.heyscriptingguy.aspx?pr=PuzzleAnswer)
  * [How Can I Delete a Record From a Disconnected Recordset? on Microsoft Technet](http://blogs.technet.com/b/heyscriptingguy/archive/2006/10/11/how-can-i-delete-a-record-from-a-disconnected-recordset.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/disconnected-
recordset-sorting/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/disconnected-
recordset-sorting/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

