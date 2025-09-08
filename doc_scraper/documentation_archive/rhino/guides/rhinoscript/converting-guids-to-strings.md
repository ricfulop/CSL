---
url: https://developer.rhino3d.com/guides/rhinoscript/converting-guids-to-strings/
scraped_at: 2025-09-08T15:42:14.246311
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

[Converting GUIDs to
Strings](https://developer.rhino3d.com/guides/rhinoscript/converting-guids-to-
strings/)

  * Problem
  * Solution
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Converting GUIDs to Strings

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

If you have written a RhinoScript function which calls a method on a COM
object that return an array of bytes with a GUID, you will likely want to
convert this GUID into a string. Converting GUIDs to strings is possible, but
it takes a little work.

## Solution

The logical format of a GUID in memory is not in the same order as the bytes
are in the string. A GUID stored in binary format in memory is a sixteen byte
structure in the following format:

`DWORD-WORD-WORD-BYTE BYTE-BYTE BYTE BYTE BYTE BYTE BYTE`

Where a WORD consists of two bytes and a DWORD consists of four bytes. They
are stored in memory in order from the least to the most significant, or
“little endian”, on Intel-based systems. So, you need to make sure you decode
the array in the correct order

The following example RhinoScript code demonstrates how to convert an array of
bytes containing a GUID to a string.

    
    
    ' Returns single digit bytes, like 0, as "00", not "0"
    Function HexByte(b)
      HexByte = Right("0" & Hex(b), 2)
    End Function
    
    ' Converts a GUID to a string
    Function GuidToString(ByteArray)
      Dim Binary, S
      Binary = CStr(ByteArray)
      ' Uncomment if you want opening paren
      ' S = "{"
      S = S & HexByte(AscB(MidB(Binary, 4, 1)))
      S = S & HexByte(AscB(MidB(Binary, 3, 1)))
      S = S & HexByte(AscB(MidB(Binary, 2, 1)))
      S = S & HexByte(AscB(MidB(Binary, 1, 1)))
      S = S & "-"  
      S = S & HexByte(AscB(MidB(Binary, 6, 1)))
      S = S & HexByte(AscB(MidB(Binary, 5, 1)))
      S = S & "-"  
      S = S & HexByte(AscB(MidB(Binary, 8, 1)))
      S = S & HexByte(AscB(MidB(Binary, 7, 1)))
      S = S & "-"  
      S = S & HexByte(AscB(MidB(Binary, 9, 1)))
      S = S & HexByte(AscB(MidB(Binary, 10, 1)))
      S = S & "-"  
      S = S & HexByte(AscB(MidB(Binary, 11, 1)))
      S = S & HexByte(AscB(MidB(Binary, 12, 1)))
      S = S & HexByte(AscB(MidB(Binary, 13, 1)))
      S = S & HexByte(AscB(MidB(Binary, 14, 1)))
      S = S & HexByte(AscB(MidB(Binary, 15, 1)))
      S = S & HexByte(AscB(MidB(Binary, 16, 1)))
      ' Uncomment if you want closing paren
      ' S = S & "}"
      GuidToString = S
    End Function
    

## Related Topics

  * [Creating GUIDs](https://developer.rhino3d.com/guides/rhinoscript/creating-guids/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/converting-
guids-to-strings/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/converting-
guids-to-strings/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

