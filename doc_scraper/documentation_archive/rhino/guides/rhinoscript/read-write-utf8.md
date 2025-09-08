---
url: https://developer.rhino3d.com/guides/rhinoscript/read-write-utf8/
scraped_at: 2025-09-08T15:42:56.426262
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

[Read & Write UTF-8
Files](https://developer.rhino3d.com/guides/rhinoscript/read-write-utf8/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Read & Write UTF-8 Files

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

If you have a text file saved as UTF-8, sometimes - when you read the file -
it reads in weird characters and not the correct characters. This happens
often when the files contain Chinese characters. How can you make it read the
correct characters?

## Solution

The [File System Object](http://msdn.microsoft.com/en-
us/library/aa242706%28v=vs.60%29.aspx), generally used by VBScript developers
to read and write text files, can read only ASCII or Unicode text files. You
cannot use it to read or write UTF-8 encoded text files.

But, if you can use [Microsoft ActiveX Data Objects
(ADO)](http://msdn.microsoft.com/en-
us/library/windows/desktop/ms676526%28v=vs.85%29.aspx), you can read UTF-8
encoded text files like this:

    
    
    Dim objStream, strData
    Set objStream = CreateObject("ADODB.Stream")
    objStream.CharSet = "utf-8"
    objStream.Open
    objStream.LoadFromFile("C:\Users\admin\Desktop\test.txt")
    strData = objStream.ReadText()
    

If you want to write a UTF-8 encode text file, you can do so like this:

    
    
    Dim objStream
    Set objStream = CreateObject("ADODB.Stream")
    objStream.CharSet = "utf-8"
    objStream.Open
    objStream.WriteText "The data I want in utf-8"
    objStream.SaveToFile "C:\Users\admin\Desktop\test.txt", 2
    

## Related Topics

  * [File System Object on MSDN](http://msdn.microsoft.com/en-us/library/aa242706%28v=vs.60%29.aspx)
  * [Microsoft ActiveX Data Objects (ADO) on MSDN](http://msdn.microsoft.com/en-us/library/windows/desktop/ms676526%28v=vs.85%29.aspx)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/read-
write-utf8/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/read-
write-utf8/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

