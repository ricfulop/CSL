---
url: https://developer.rhino3d.com/guides/rhinoscript/comparing-arrays/
scraped_at: 2025-09-08T15:42:13.263743
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

[Comparing Arrays](https://developer.rhino3d.com/guides/rhinoscript/comparing-
arrays/)

  * Slow Comparison
  * Fast Comparison
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Comparing Arrays

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Slow Comparison

Imagine you have two collections of items and you want to determine how many
of those items have the same name. In short, you want to compare the contents
of two arrays. Consider this straightforward method of comparison:

    
    
    intSame = 0
    For Each strFirst In arrFirst
      For Each strSecond In arrSecond
        If StrComp(strFirst, strSecond, vbTextCompare) = 0 Then
          intSame = intSame + 1
          Exit For
        End If
      Next
    Next
    

This method, although simple, is extremely slow. Let’s say there are 5000
items in `arrFirst`, 3000 items in `arrSecond`, and 1500 of them have the same
value. Every one of the 3500 unsuccessful searches checks all 3000 `arrSecond`
items, and the 1500 successful searches on average check 1500 `arrSecond`
items each. Each time through, the inner loop does one loop iteration and one
string comparison. Add all those up and you get millions of function calls to
determine this count. Now, each individual function call is only taking a few
microseconds, but all of these calls add up!

There is another way…

## Fast Comparison

Try building a faster lookup table rather than doing a full search through the
collection every time.

    
    
    Set objLookup = CreateObject("Scripting.Dictionary")
    For Each strFirst In arrFirst
      Call objLookup.Add(strFirst, 0) ' 0 = some useless value
    Next
    For Each strSecond In arrSecond
      If objLookup.Exists(strSecond) Then intSame = intSame + 1
    Next
    

This is only a couple of thousand function calls. So we believe that this will
be much, much faster.

## Related Topics

  * [Array Bounds](https://developer.rhino3d.com/guides/rhinoscript/array-bounds/)
  * [Array Utilities](https://developer.rhino3d.com/guides/rhinoscript/array-utilities/)
  * [VBScript Dictionaries](https://developer.rhino3d.com/guides/rhinoscript/vbscript-dictionaries/)
  * [VBScript Looping](https://developer.rhino3d.com/guides/rhinoscript/vbscript-looping/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/comparing-
arrays/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/comparing-
arrays/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

