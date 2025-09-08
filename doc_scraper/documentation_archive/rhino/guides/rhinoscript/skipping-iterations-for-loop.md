---
url: https://developer.rhino3d.com/guides/rhinoscript/skipping-iterations-for-loop/
scraped_at: 2025-09-08T15:43:03.451484
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

[Skipping current iteration in a For
loop](https://developer.rhino3d.com/guides/rhinoscript/skipping-iterations-
for-loop/)

  * Problem
  * Solution

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Skipping current iteration in a For loop

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

Both the C++ and C# programming languages have a `continue` statement that,
when used with a `For` loop, skips the remaining statements of that iteration
and moves on to next iteration. Does VBScript have anything like this?

## Solution

There is no `continue` or continue-like statement in VBScript. But using a `Do
While loop` inside of a `For Each` statement, you can achieve the same
functionality. For example:

    
    
    For i = 0 To 10
      Do
        If i = 4 Then Exit Do
        Rhino.Print i
      Loop While False
    Next
    

Here is another example:

    
    
    Sub TestContinue
     
      Dim arrTests, arrTest
     
      arrTests = Array( _
            Array(1) _
          , Array(1,2,3 ) _
          , Array(1,2) _
          , Array(1) _
          , Array(1,2,3) _
          )
     
      For Each arrTest In arrTests
         Call Rhino.Print("Process: {" & Join(arrTest, ", ") & "}")
         Do While True ' Continue trick
           Call Rhino.Print(" Process: " & arrTest(0))
           If 0 = UBound(arrTest) Then Exit Do ' Continue
           Call Rhino.Print(" Process: " & arrTest(1))
           If 1 = UBound(arrTest) Then Exit Do ' Continue
           Call Rhino.Print(" Process: " & arrTest(2))
           Exit Do
         Loop
      Next
     
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/skipping-
iterations-for-loop/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/skipping-
iterations-for-loop/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

