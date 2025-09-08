---
url: https://developer.rhino3d.com/guides/rhinoscript/using-net-classes-in-vbs/
scraped_at: 2025-09-08T15:42:30.318776
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

[Using .NET Classes](https://developer.rhino3d.com/guides/rhinoscript/using-
net-classes-in-vbs/)

  * Overview
  * ArrayList
  * SortedList
  * Stack
  * Queue
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Using .NET Classes

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Unlike other programming languages, VBScript lacks support of complex data
structures. Sometimes this makes life a bit difficult. We need to code our own
algorithms to achieve simple tasks like sorting or reversing an array. .NET
has support for complex data structures which come with built-in functions for
these simple tasks. So if we can use .NET data structure then we can eliminate
the reinvention of the wheel for some of these tasks. Well, the good news is
that some .NET libraries are exposed to COM and can be used in VBScript. Let’s
take a look at the most useful of these…

## ArrayList

An [ArrayList](http://msdn.microsoft.com/en-
us/library/system.collections.arraylist%28v=vs.100%29.aspx) is an array whose
size is dynamically increased when needed. Here is an example of its use:

    
    
    Set objArrayList = CreateObject("System.Collections.ArrayList")
    
    objArrayList.Add 6
    objArrayList.Add 8
    objArrayList.Add 2
    objArrayList.Add 4
    objArrayList.Add 1
    objArrayList.Add 5
    objArrayList.Add 3
    objArrayList.Add 3
    objArrayList.Add 7
    
    'Convert to VBScript Array
    Rhino.Print Join(objArrayList.ToArray, ",")
    
    'Return the element at a given index
    Rhino.Print objArrayList(0)
    
    'Return the number of elements
    Rhino.Print objArrayList.Count
    
    'Verifies an element exists or not.
    Rhino.Print objArrayList.Contains(5)
    
    'Sort the elements
    objArrayList.Sort
    Rhino.Print Join(objArrayList.ToArray, ",")
    
    'Reverse the order of all elements
    objArrayList.Reverse
    Rhino.Print Join(objArrayList.ToArray, ",")
    
    'Remove a specific element
    objArrayList.Remove 8
    
    'Remove element by index
    objArrayList.RemoveAt 6
    
    'Remove all elements
    objArrayList.Clear  
    

For VBScript `Dictionary` objects we don’t need to redim while appending or
removing elements. Also, an element can be directly searched without iterating
through each of them. Both of these features are available with `ArrayList` as
well but one of the most important dictionary object features, Key-Value pair,
is not in `ArrayList`. `SortedList` is an alternative if you want the power of
both `ArrayList` and `Dictionary`.

## SortedList

A [SortedList](http://msdn.microsoft.com/en-
us/library/system.collections.sortedlist.aspx) a is sorted Dictionary. Every
time we add or remove a key value pair in the dictionary, it automatically
gets sorted by Key. You can also access elements based on its index (just like
arrays) which makes this even more powerful. Here is an example:

    
    
    Set objSortedList = CreateObject("System.Collections.SortedList")
    
    objSortedList.Add "Point", 1
    objSortedList.Add "Point Cloud", 2
    objSortedList.Add "Curve", 4
    objSortedList.Add "Surface", 8
    objSortedList.Add "Polysurface", 16
    objSortedList.Add "Mesh", 32
    
    'Return the number of elements
    Rhino.Print objSortedList.Count
    
    'Return a value by its key
    Rhino.Print objSortedList("Surface")
    
    'Access all elements by index
    For i = 0 To objSortedList.Count - 1
      Rhino.Print CStr(objSortedList.GetByIndex(i))
    Next
    
    'Verify a key exists
    Rhino.Print objSortedList.ContainsKey("Polysurface")
    
    'Verify a value exists
    Rhino.Print objSortedList.ContainsValue(16)
    
    'Return the index by key (zero based index)
    Rhino.Print objSortedList.IndexOfKey("Polysurface")
    
    'Return the index by value
    Rhino.Print objSortedList.IndexOfValue(16)
    
    'Remove an element by key
    objSortedList.Remove "Polysurface"
    
    'Remove an element by index
    objSortedList.RemoveAt 0
    
    'Remove all elements
    objSortedList.Clear
    

## Stack

A [Stack](http://msdn.microsoft.com/en-
us/library/system.collections.stack.aspx) is a simple last-in, first-out
(LIFO) non-generic collection of objects or data. By last-in, first-out, what
we mean is if a set of objects is put into a stack, the last object that was
put in will be the first object to be taken out. For example, in a restaurants
with an automatic plate dispenser, the stack of plates are added to from the
top. As each person takes a plate, the next plate in the stack becomes
available. Here is an example of using `Stack`:

    
    
    Set objStack = CreateObject("System.Collections.Stack")
    
    'Add elements to stack
    objStack.Push "Item_1"
    objStack.Push "Item_2"
    objStack.Push "Item_3"
    objStack.Push "Item_4"
    
    'Iterate through each element
    For Each Item In objStack
     Rhino.Print Item
    Next
    
    'Convert to VBScript array
    Rhino.Print Join(objStack.ToArray, ",")
    
    'Return the number of elements
    Rhino.Print objStack.Count
    
    'Verify an element exists
    Rhino.Print objStack.Contains("Item_2")
    
    'Pop the last element
    Rhino.Print objStack.Pop
    
    'Return the last in element without popping
    Rhino.Print objStack.Peek
    Rhino.Print objStack.Pop
    Rhino.Print objStack.Pop
    
    'Remove all elements
    objStack.Clear
    

## Queue

Unlike a `Stack`, a [Queue](http://msdn.microsoft.com/en-
us/library/system.collections.queue%28v=vs.100%29.aspx) represents a first-in,
first-out collection of objects or data. Here is an example:

    
    
    Set objQueue = CreateObject("System.Collections.Queue")
    
    'Add elements to queue
    objQueue.Enqueue "Item_1"
    objQueue.Enqueue "Item_2"
    objQueue.Enqueue "Item_3"
    objQueue.Enqueue "Item_4"
    
    'Iterate through each element
    For Each Item In objQueue
      Rhino.Print Item
    Next
    
    'Convert to VBScript array
    Rhino.Print Join(objQueue.ToArray, ",")
    
    'Return the number of elements
    Rhino.Print objQueue.Count
    
    'Verify an element exists
    Rhino.Print objQueue.Contains("Item_2")
    
    'Return the first element
    Rhino.Print objQueue.Dequeue
    
    'Return the first element without removing it
    Rhino.Print objQueue.Peek
    Rhino.Print objQueue.Dequeue
    Rhino.Print objQueue.Dequeue
    
    'Removes all elements
    objQueue.Clear
    

## Related Topics

  * [ArrayList on MSDN](http://msdn.microsoft.com/en-us/library/system.collections.arraylist%28v=vs.100%29.aspx)
  * [SortedList on MSDN](http://msdn.microsoft.com/en-us/library/system.collections.sortedlist.aspx)
  * [Stack on MSDN](http://msdn.microsoft.com/en-us/library/system.collections.stack.aspx)
  * [Queue on MSDN](http://msdn.microsoft.com/en-us/library/system.collections.queue%28v=vs.100%29.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/using-
net-classes-in-vbs/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/using-
net-classes-in-vbs/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

