---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-logic/
scraped_at: 2025-09-08T15:42:00.181673
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

[VBScript Logic](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
logic/)

  * Logic?
  * What Logic?
  * Details
  * Best Practices

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Logic

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Logic?

Consider the following statements:

    
    
    If blnResult = True Then Print "True!" Else Print "False!"
    

and

    
    
    If blnResult Then Print "True!" Else Print "False!"
    

Is there a difference?

## What Logic?

Yes, there is a big difference. If `blnResult` is True or False, then both
statements do what you would expect – the same thing. But, the first statement
is asking “Is `blnResult` equal to True?” whereas the second question is
asking “Is `blnResult` not equal to False?”

In a strictly Boolean world, those are equal statements. But the VBScript type
system is richer than just Booleans.

## Details

For example, what if - in the above example - `blnResult` is the string True?
The string True is not equal to the Boolean True, so the first statement is
false. But the string is also not equal to False, so the second statement is
true, and the statements have different semantics.

The same goes for numbers. When converted to a number, True converts to -1
(for reasons which will become clear in a moment) and False converts to 0. So,
if `blnResult` is 1, again the first statement is false because 1 <> -1, and
the second statement is true because 1 <> 0.

What’s going on is that VBScript is not logical. VBScript is bitwise. All the
so-called logical operators work on numbers, not on Boolean values. `Not`,
`And`, `Or`, `XOr`, `Eqv` and `Imp` all convert their arguments to four-byte
integers, do the logical operation on each pair of bits in the integers, and
return the result. If True is -1 and False is 0 then everything works out,
because -1 has all its bits turned on and 0 has all its bits turned off. But
if other numbers get in there, all bets are off.

This can lead to some strange situations if you’re not careful. In VBScript,
it is certainly possible for…

    
    
    If blnResult Then
    

and

    
    
    If blnAnswer Then
    

to be both true, but

    
    
    If Blah And Foo Then
    

to be false, if `blnResult` is 1 and `blnAnswer` is 2, for example.

## Best Practices

Conditional statements should always take Booleans. Or, in other words, use
Booleans as Booleans. Use nothing else as Booleans.

Suppose you’ve got a method that returns a number and you want to do something
if it doesn’t return zero. Don’t do this, even though it does exactly what you
want:

    
    
    If intResult Then
    

it’s clearer to call it out and make the conditional take a Boolean:

    
    
    If intResult <> 0 Then
    

Conversely, if a value is a Boolean and you know that, there’s no need to
compare it. When you see:

    
    
    If blnResult = True Then
    

If blnResult can only contain True or False, then you can just say

    
    
    If Blah Then
    

Use the same practice with logical operators. Do not mix-and-match. Either
every argument should explicitly be a number and you’re doing bitwise
comparisons, or every argument is a Boolean. Mixing the two makes the code
harder to read and more bug-prone.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
logic/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
logic/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

