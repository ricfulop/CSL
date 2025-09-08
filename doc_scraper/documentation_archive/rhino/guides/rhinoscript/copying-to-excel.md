---
url: https://developer.rhino3d.com/guides/rhinoscript/copying-to-excel/
scraped_at: 2025-09-08T15:42:39.261789
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

[Copying to Excel](https://developer.rhino3d.com/guides/rhinoscript/copying-
to-excel/)

  * Overview
  * Details
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Copying to Excel

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

You can copy information from Rhino and then paste it into Excel. The real
question is “what do you want to copy and paste?”

Copying information from Rhino and pasting it into Excel is fairly easy using
RhinoScript. All you have to do is use the `ClipboardText` method to copy a
text string into the Windows Clipboard. Then from Excel, just select the cell
and paste.

## Details

If you want to copy the string “Hello from Rhino!” into Excel, your script
could be as simple as this:

    
    
    Call Rhino.ClipboardText("Hello from Rhino!")
    

Easy enough. But, what if you want to copy some delimited data so each “token”
appears in a different column in Excel when pasted. Then, simply separate each
token with a tab, or `vbTab`, character. For example:

    
    
    Call Rhino.ClipboardText("A" & vbTab & "B" & vbTab & "C" & vbTab & "1" & vbTab & "2" & vbTab & "3")
    

Likewise, if you want to copy some delimited data so each “token” appears in a
different row in Excel when pasted, then separate each token with a line-feed,
or `vbLf`, character. For example:

    
    
    Call Rhino.ClipboardText("A" & vbLf & "B" & vbLf & "C" & vbLf & "1" & vbLf & "2" & vbLf & "3")
    

You can get more elaborate by creating a formatted string that contains both
tab and line-feed characters. In this example, we will copy something useful -
curve lengths in this example…

    
    
    Sub CopyClipCrvLength()
      Dim curves, crv, length, str
      curves = Rhino.GetObjects("Select curves to copy length", 4, True, True)
      If IsArray(curves) Then
        str = str & "Id" & vbTab & "Length" & vbLf
        For Each crv In curves
          length = Rhino.CurveLength(crv)
          str = str & crv & vbTab & CStr(length) & vbLf
        Next
        Call Rhino.ClipboardText(str)
      End If    
    End Sub
    

Now that you have the basic idea, you should be able to write your own scripts
that copy any type of data you want from Rhino into Excel.

## Related Topics

  * [Reading Excel Files](https://developer.rhino3d.com/guides/rhinoscript/reading-excel-files/)
  * Automating Excel From RhinoScript (Sample)
  * Automating Curve Properties to Excel From RhinoScript (Sample)
  * Exporting Point Coordinates to Excel (Sample)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/copying-
to-excel/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/copying-
to-excel/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

