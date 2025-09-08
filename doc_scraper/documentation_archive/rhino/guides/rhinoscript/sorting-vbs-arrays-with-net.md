---
url: https://developer.rhino3d.com/guides/rhinoscript/sorting-vbs-arrays-with-net/
scraped_at: 2025-09-08T15:43:04.337638
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

[Sorting VBS Arrays with
.NET](https://developer.rhino3d.com/guides/rhinoscript/sorting-vbs-arrays-
with-net/)

  * Overview
  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Sorting VBS Arrays with .NET

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

One of the big limitations in VBScript is that there is no easy way to sort a
list of items. To put a list in alphabetical order requires you to either use
the pre-canned RhinoScript methods, such as `SortNumbers`, `SortPoints` or
`SortStrings`, or write a sorting function of your own, like the following
bubble sort code:

    
    
    For i = (UBound(arrNames) - 1) to 0 Step -1
      For j= 0 to i
        If UCase(arrNames(j)) >
          UCase(arrNames(j+1)) Then
            strHolder = arrNames(j+1)
            arrNames(j+1) = arrNames(j)
            arrNames(j) = strHolder
        End If
      Next
    Next
    

## Discussion

There is another option and that is to use the .NET Framework to help. The
majority of .NET Framework classes are unusable in VBScript. However, there
are a large number of .NET classes that have COM-callable wrappers. T his
means these classes include a COM interface enabling them to be accessed from
VBScript.

For example, consider the following script:

    
    
    Set DataList = CreateObject("System.Collections.ArrayList")
    DataList.Add "B"
    DataList.Add "C"
    DataList.Add "E"
    DataList.Add "D"
    DataList.Add "A"
    DataList.Sort()
    For Each strItem in DataList
      Rhino.Print strItem
    Next
    

Notice that we have created an instance of the .NET Framework class
`System.Collections.ArrayList`. We then use the `Add` method to add five items
to the list. To sort the list, all we need to do is call the `ArrayList`’s
`Sort` method.

Now, what if you really wanted those values in descending order? In this case,
just call `ArrayList`’s `Sort` method after calling the `Sort` method.

    
    
    Set DataList = CreateObject("System.Collections.ArrayList")
    DataList.Add "B"
    DataList.Add "C"
    DataList.Add "E"
    DataList.Add "D"
    DataList.Add "A"
    DataList.Sort()
    DataList.Reverse()
    For Each strItem in DataList
      Rhino.Print strItem
    Next
    

Also, have you ever tried to remove an item from a VBScript array? It is not
easy. But, with the .NET Framework’s `ArrayList`, you just need to call the
`Remove` method. The following script, an `ArrayList`, sorts it, and then
removes the entry for `D`…

    
    
    Set DataList = CreateObject("System.Collections.ArrayList")
    DataList.Add "B"
    DataList.Add "C"
    DataList.Add "E"
    DataList.Add "D"
    DataList.Add "A"
    DataList.Sort()
    DataList.Remove("D")
    For Each strItem in DataList
      Rhino.Print strItem
    Next
    

Copying items VBScript arrays and an `ArrayList` is just as easy. In the
following script, an `ArrayList` is used to sort a list of layer names…

    
    
    LayerNames = Rhino.LayerNames
    Set DataList = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(LayerNames)
      DataList.Add LayerNames(i)
    Next
    DataList.Sort()
    For i = 0 To UBound(LayerNames)
      LayerNames(i) = DataList(i)
    Next
    Layer = Rhino.ListBox(LayerNames, "Layer to set current")
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/sorting-
vbs-arrays-with-net/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/sorting-
vbs-arrays-with-net/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

