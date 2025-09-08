---
url: https://developer.rhino3d.com/guides/rhinoscript/finding-perfect-squares/
scraped_at: 2025-09-08T15:42:18.287779
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

[Finding Perfect
Squares](https://developer.rhino3d.com/guides/rhinoscript/finding-perfect-
squares/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Finding Perfect Squares

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

In mathematics, a perfect square is an integer that is the square of an
integer; in other words, it is the product of some integer with itself. For
example, 9 is a perfect square, since it can be written as 3 × 3. How can one
determine whether or not an integer is a perfect square in RhinoScript?

## Solution

Here is an example of a function that determines whether or not a number is a
perfect square:

    
    
    Function IsPerfectSquare(n)
    
      Dim h, t
    
      IsPerfectSquare = False ' default return value
    
      h = n And &HF ' last hexadecimal "digit"
      If (h > 9) Then Exit Function ' return immediately in 6 cases out of 16
    
      If (h <> 2 And h <> 3 And h <> 5 And h <> 6 And h <> 7 And h <> 8) Then
        t = Int(Rhino.Floor(Sqr(n)+0.5))
        If (t*t = n) Then IsPerfectSquare = True
      End If
    
    End Function
    

You can test the above function as follows:

    
    
    For i = 0 To 60^2
      If IsPerfectSquare(i) Then
        Call Rhino.Print(CStr(i) & "^2 = " & CStr(i^2))
      End If
    Next
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/finding-
perfect-squares/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/finding-
perfect-squares/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

