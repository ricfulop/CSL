---
url: https://developer.rhino3d.com/guides/rhinopython/grasshopper-datatrees-and-python/
scraped_at: 2025-09-08T15:37:14.884543
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

[Grasshopper data trees and
Python](https://developer.rhino3d.com/guides/rhinopython/grasshopper-
datatrees-and-python/)

  * Data trees, technically
  * Coding against the DataTree class
  * A simpler way, coding against lists of lists
  * Complete sample
  * Source & Q&A

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Grasshopper data trees and Python

by [Giulio Piacentino](https://discourse.mcneel.com/u/piac/) and [Scott
Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated: Wednesday,
June 2, 2021)

## Data trees, technically

The data tree data structure is a complex data structure that is best kept in
Grasshopper realms. It is a .Net class that is part of the Grasshopper SDK
and, as such, all its members can be found on the [DataTree
class](http://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm)
Grasshopper SDK documentation site.

On the implementation side, in Python it can be thought as an object with
behavior similar to a `dict` \- really,
[System.Collections.Generic.SortedList](https://msdn.microsoft.com/en-
us/library/system.collections.sortedlist%28v=vs.110%29.aspx) \- of `GH_Path`s,
or
[Grasshopper.Kernel.Data.GH_Path](http://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_Path.htm).
For each one of the paths-keys inside, there is an associated [.Net
list](https://msdn.microsoft.com/en-
us/library/6sh2ey19%28v=vs.110%29.aspx)-value, that is a branch. Items are
stored in each list. There is no null-path, but paths can be sparse. Items
cannot be sparse, but there can be null-items.

Other data structures would also be able to accommodate similar data. In
Python, a similar object with better language support would be a list of
lists.

    
    
    nested_list = [[0, 1], [2, 3]]
    

However, a list of lists cannot always represent the merging of two datatrees
with different dimensional depth in data (example: a datatree with an item at
{0;1}[0] and an item at {0}[1]). If the data tree is constructed by normal and
integral Grasshopper logic, it will have constant dimensional depth, and
therefore this problem can be avoided. Alternatively, the data tree with
inferior dimension can be ‘grafted’ to a branch of an upper dimension, and
also this way the problem is avoided.

## Coding against the DataTree class

This example shows how to iterate through any data tree and explain the
content of it.

    
    
    a = []
    
    for i in range(x.BranchCount):
        branchList = x.Branch(i)
        branchPath = x.Path(i)
        
        for j in range(branchList.Count):
            s = str(branchPath) + "[" + str(j) + "] "
            s += type(branchList[j]).__name__ + ": "
            s += str(branchList[j])
            
            a.append(s)
    

On the opposite side, this example shows how to create a data tree from
scratch:

    
    
    import ghpythonlib.treehelpers as th
    import Rhino
    
    layerTree = [list() for _ in layernames]
    
    for i in range(len(layernames)):
        objs = Rhino.RhinoDoc.ActiveDoc.Objects.FindByLayer(layernames[i])
        
        if objs:
            geoms = [obj.Geometry for obj in objs]
            layerTree[i].extend(geoms)
    
    layerTree = th.list_to_tree(layerTree, source=[0,0])
    a = layerTree
    

## A simpler way, coding against lists of lists

As mentioned under the first heading, when possible, it is easier to code
against nested lists (lists of lists) in Python, to leverage this more
ubiquitous programing paradigm. The `ghpythonlib.treehelpers` module contains
functions that transform trees to nested lists, and vice versa.

The first two examples can be translated to

    
    
    import ghpythonlib.treehelpers as th
    
    x = th.tree_to_list(x)
    
    a = []
    
    for i,branch in enumerate(x):
        
        for j,item in enumerate(branch):
            s = str(i) + "[" + str(j) + "] "
            s += type(item).__name__ + ": "
            s += str(item)
            
            a.append(s)
    
    
    
    import ghpythonlib.treehelpers as th
    import Rhino
    
    layerTree = []
    
    for i in range(len(layernames)):
        objs = Rhino.RhinoDoc.ActiveDoc.Objects.FindByLayer(layernames[i])
        
        if objs:
            geoms = [obj.Geometry for obj in objs]
            layerTree.append(geoms)
    
    layerTree = th.list_to_tree(layerTree, source=[0,0])
    a = layerTree
    

## Complete sample

  * [datatree_examples.gh](https://developer.rhino3d.com/files/datatree_examples.gh)

## Source & Q&A

A copy of the source is posted as
[Gist](https://gist.github.com/piac/ef91ac83cb5ee92a1294) and there is also
some Q&A on particular usages, such as [with simplified
trees](https://gist.github.com/piac/ef91ac83cb5ee92a1294#gistcomment-3763417).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/grasshopper-
datatrees-and-python/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/grasshopper-
datatrees-and-python/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

