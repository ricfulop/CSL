---
url: https://developer.rhino3d.com/guides/rhinoscript/disposing-of-variables/
scraped_at: 2025-09-08T15:42:16.145289
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

[Disposing of
Variables](https://developer.rhino3d.com/guides/rhinoscript/disposing-of-
variables/)

  * Overview
  * Example
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Disposing of Variables

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

VBScript’s garbage collector runs at the end of every statement and procedure,
and does not do a search of all memory. Rather, it keeps track of everything
allocated in the statement or procedure; if anything has gone out of scope, it
frees it immediately.

Global variables, ones declared outside of a procedure, do not go out of scope
until VBScript is reset or destroyed. Thus, for memory efficiency, it is best
not use global variables.

With this said, one can conclude that it is more memory efficient to write
scripts that contain a number of small, efficient procedures, so variables
that are no longer needed are garbage collected, than it is to write a single,
massive procedure.

But, sometimes is neither possible nor convenient to write a script in a
granular fashion. In such cases, it is possible to manually clean up unused
objects and variables along the way to keep your single, massive procedure
memory efficient.

## Example

The following example demonstrates how to create a single procedure that is
capable of cleaning up a number of different variable types. The idea is that
when a variable is no longer needed, you can call a single procedure to clean
it up, thus making your scripts use less memory.

For example, lets say your script used an array variable to store a massive
amount of data. When you were finished with the variable, you could dispose of
the array, and recover its memory, like this:

    
    
    Call Dispose(arr)
    

This examples cleans up dictionary objects, arrays, and simple variables. But,
it could be extended to include other types of objects, such as file streams,
database recordsets, or user-defined class objects.

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Dispose.rvb -- April 2010
    ' If this code works, it was written by Dale Fugier.
    ' If not, I don't know who wrote it.
    ' Works with Rhino 4.0.
    
    Option Explicit
    
    ' Disposes of dictionaries, arrays, and variables
    Sub Dispose(ByRef obj)
      If IsObject(obj) Then
        If LCase(TypeName(obj)) = "dictionary" Then
         obj.RemoveAll ' Remove all key, item pairs
        End If
        Set Obj = Nothing ' Disassociate
      ElseIf IsArray(obj) Then
        Erase obj ' Clear the array
      End If
      obj = Empty ' Uninitialize
    End Sub
    

## Related Topics

  * [VBScript Variables](https://developer.rhino3d.com/guides/rhinoscript/vbscript-variables/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/disposing-
of-variables/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/disposing-
of-variables/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

