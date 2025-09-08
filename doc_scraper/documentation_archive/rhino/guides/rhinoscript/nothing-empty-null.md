---
url: https://developer.rhino3d.com/guides/rhinoscript/nothing-empty-null/
scraped_at: 2025-09-08T15:42:24.297113
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

[Nothing vs Empty vs
Null](https://developer.rhino3d.com/guides/rhinoscript/nothing-empty-null/)

  * Overview
  * Empty
  * Nothing
  * Null

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Nothing vs Empty vs Null

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

There has always been confusion about the semantics of data that are not even
there. Usually they’ve written code something like:

    
    
    If varValue = Nothing Then
    

or

    
    
    If varValue = Empty Then
    

or

    
    
    If varValue = Null Then
    

Why does VBScript have `Null`, `Nothing` and `Empty`, and what are the
differences between them?

## Empty

When you declare a variable in VBScript, the variable’s value before the first
assignment is undefined, or `Empty`.

    
    
    Dim varValue ' Empty value
    

So basically, `Empty` says “I am an uninitialized variant.” If you need to
detect whether a variable actually is an empty variant and not a string or a
number, you can use `IsEmpty`. Alternatively, you could use `TypeName` or
`VarType`, but `IsEmpty` is best.

## Nothing

`Nothing` is similar to `Empty` but subtly different. If `Empty` says “I am an
uninitialized variant,” `Nothing` says “I am an object reference that refers
to no object.” Objects are assigned to variables using the `Set` statement.
Since the equality operator on objects checks for equality on the default
property of an object, any attempt to say:

    
    
    If varValue = Nothing Then
    

is doomed to failure; `Nothing` does not have a default property, so this will
produce a run-time error. To check to see if an object reference is invalid,
use:

    
    
    If varValue Is Nothing Then
    

## Null

`Null` is more obscure. The semantics of `Null` are very poorly understood,
particularly amongst people who have little experience with programming. Empty
says “I’m an uninitialized variant,” `Nothing` says “I’m an invalid object”
and `Null` says “I represent a value which is not known.” Null is not _True_ ,
not _False_ , but `Null`! The correct way to check for `Null` is much as you’d
do for `Empty`: use `IsNull` (or `TypeName` or `VarType`.)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/nothing-
empty-null/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/nothing-
empty-null/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

