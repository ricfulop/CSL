---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-datatypes/
scraped_at: 2025-09-08T15:41:58.171176
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

[VBScript Data
Types](https://developer.rhino3d.com/guides/rhinoscript/vbscript-datatypes/)

  * Overview
  * Variant Subtypes
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Data Types

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

VBScript has only one data type called a Variant. A Variant is a special kind
of data type that can contain different kinds of information, depending on how
it is used. Because Variant is the only data type in VBScript, it is also the
data type returned by all functions in VBScript.

At its simplest, a Variant can contain either numeric or string information. A
Variant behaves as a number when you use it in a numeric context and as a
string when you use it in a string context. That is, if you are working with
data that looks like numbers, VBScript assumes that it is numbers and does
what is most appropriate for numbers. Similarly, if you’re working with data
that can only be string data, VBScript treats it as string data. You can
always make numbers behave as strings by enclosing them in quotation marks (`"
"`).

## Variant Subtypes

Beyond the simple numeric or string classifications, a Variant can make
further distinctions about the specific nature of numeric information. For
example, you can have numeric information that represents a date or a time.
When used with other date or time data, the result is always expressed as a
date or a time. You can also have a rich variety of numeric information
ranging in size from Boolean values to huge floating-point numbers. These
different categories of information that can be contained in a Variant are
called subtypes. Most of the time, you can just put the kind of data you want
in a Variant, and the Variant behaves in a way that is most appropriate for
the data it contains.

The following table shows subtypes of data that a Variant can contain:

Subtype |  |  |  | Description  
---|---|---|---|---  
Empty |  |  |  | Variant is uninitialized. Value is 0 for numeric variables or a zero-length string () for string variables.  
Null |  |  |  | Variant intentionally contains no valid data.  
Boolean |  |  |  | Contains either True or False.  
Byte |  |  |  | Contains integer in the range 0 to 255.  
Integer |  |  |  | Contains integer in the range -32,768 to 32,767.  
Currency |  |  |  | -922,337,203,685,477.5808 to 922,337,203,685,477.5807.  
Long |  |  |  | Contains integer in the range -2,147,483,648 to 2,147,483,647.  
Single |  |  |  | Contains a single-precision, floating-point number in the range -3.402823E38 to -1.401298E-45 for negative values; 1.401298E-45 to 3.402823E38 for positive values.  
Double |  |  |  | Contains a double-precision, floating-point number in the range -1.79769313486232E308 to -4.94065645841247E-324 for negative values; 4.94065645841247E-324 to 1.79769313486232E308 for positive values.  
Date (Time) |  |  |  | Contains a number that represents a date between January 1, 100 to December 31, 9999.  
String |  |  |  | Contains a variable-length string that can be up to approximately 2 billion characters in length.  
Object |  |  |  | Contains an object.  
Error |  |  |  | Contains an error number.  
  
You can use VBScript conversion functions to convert data from one subtype to
another. In addition, the `VarType` function returns information about how
your data is stored within a Variant.

## Related topics

  * [What are VBScript and RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-vbscript-rhinoscript/)
  * [VBScript Variables](https://developer.rhino3d.com/guides/rhinoscript/vbscript-variables/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
datatypes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
datatypes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

