---
url: https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/#related-topics
scraped_at: 2025-09-08T15:57:50.190722
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

[Developer Prerequisites](https://developer.rhino3d.com/guides/general/rhino-
developer-prerequisites/)

  * Hardware
  * Software
  * Programming Knowledge
    * Learning C# .NET
    * Learning C/C++
    * Learning Python
    * Learning RhinoScript
    * Learning More
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [General
Guides](https://developer.rhino3d.com/en/guides/general/) /

Developer Prerequisites

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) and [Callum
Sykes](https://discourse.mcneel.com/u/Callumsykes/) (Last updated: Monday,
March 17, 2025)

There are a number of prerequisites required to do Rhino development. Broadly
speaking, these can be divided into three categories, ranked in ascending
order of difficulty:

  1. [Hardware prerequisites](https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/#hardware)
  2. [Software prerequisites](https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/#software)
  3. [Programming Knowledge](https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/#programming-knowledge)

## Hardware

If you are reading this guide, you likely already have a computer that can run
Rhino. (If not, Rhino has some minimum [System
Requirements](http://www.rhino3d.com/system_requirements/) that you should
review before acquiring any hardware). Generally speaking, any computer that
can run Rhino _ought_ to be able to run the developer tools outlined in the
[Software](https://developer.rhino3d.com/guides/general/rhino-developer-
prerequisites/#software) section.

If you are a Windows user and wish to develop plugins for Rhino for Mac, you
will need an Apple Mac computer. Conversely, if you are an macOS user and you
wish to develop for Rhino for Windows, you will need a computer that can run
Rhino for Windows (however, virtual machines running Windows under macOS can
potentially work just fine).

## Software

Depending on what you want to do, the software prerequisites vary. However, in
general, you will need:

  * [Rhinoceros](http://www.rhino3d.com/download)
  * A code editor. There are many options…here are a few: 
    * [Visual Studio for Windows](https://www.visualstudio.com): Microsoft’s flagship Integrated Development Environment (IDE) for Windows.
    * [Visual Studio Code](https://code.visualstudio.com/): The best free cross-platform editor

See the [SDK-specific guides](https://developer.rhino3d.com/guides/) for the
software prerequisites…normally found in the _“Installing Tools”_ guides.

## Programming Knowledge

Acquiring programming knowledge is the most labor intensive prerequisite.
However, learning to program - even trying out a new language - is fun and
enriching. Learning to program using Rhino is a great way to begin…

### Learning C# .NET

If you wish to write plugins with RhinoCommon, you will need to understand a
.NET compatible programming language like C# (or VB). We recommend
[C#](https://en.wikipedia.org/wiki/C_Sharp_%28programming_language%29) (C
Sharp) because it is modern, safe, and easy to learn - and you can develop in
C# on both Windows and macOS.

_Watch_ …

  * [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) By Eric Lippert - Published by O’Reilly Media
  * [C# Fundamentals for Absolute Beginners](https://learn.microsoft.com/en-us/shows/csharp-fundamentals-for-absolute-beginners/) on Microsoft’s Virtual Academy
  * [C# and .NET Essential Training](https://www.linkedin.com/learning/c-sharp-and-dot-net-essential-training) on LinkedIn Learning

_Read_ …

  * [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) By Ian Griffiths - Published by O’Reilly Media
  * [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) By Joseph Albahari, Ben Albahari - Published by O’Reilly Media

_Do_ …

  * [Check out samples](https://developer.rhino3d.com/samples/#rhinocommon) on this site
  * [Ask for help on Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Learning C/C++

To write plugins for Rhino using the C/C++ SDK, you first need to learn the
[C++ programing language](https://en.wikipedia.org/wiki/C%2B%2B) itself. C/C++
is sometimes considered an “advanced” programming language.

_Watch_ …

  * [C++: A General Purpose Language](https://learn.microsoft.com/en-us/shows/cplusplus-language-library/) on Microsoft Virtual Academy
  * [C++ Essential Training](https://www.linkedin.com/learning/c-plus-plus-essential-training-15106801) with Bill Weinmann on LinkedIn Learning

_Read_ …

  * [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) by Ian Kernighan and Dennis Ritchie
  * [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) by Steve Oualline - Published by O’Reilly Media
  * [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) by Stephen Prata

_Do_ …

  * [Check out samples](https://developer.rhino3d.com/samples/#cc) on this site
  * [Ask for help on Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Learning Python

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) is a
fantastic first language and an amazingly flexible additional language to add
to your toolkit.

_Watch_ …

  * [Google’s Python Class](https://developers.google.com/edu/python/) by Google for Education
  * [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) with Joe Marini on Lynda.com

_Read_ …

  * [The Python Tutorial](https://docs.python.org/2/tutorial/index.html)
  * [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) by Skylar Tibbits, Arthur van der Harten, Steve Baer, and David Rutten
  * [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) by the Python Software Foundation
  * [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) by Zed A. Shaw - despite the title, this is a beginner’s book
  * [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) by Al Sweigart

_Do_ …

  * [Check out samples](https://developer.rhino3d.com/samples/#rhinopython) on this site
  * [Ask for help on Discourse](http://discourse.mcneel.com/c/scripting)

### Learning RhinoScript

RhinoScript is a scripting tool based on Microsoft’s VBScript language.
RhinoScript runs in Rhino for Windows.

_Read_ …

  * [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) by David Rutten
  * [Microsoft VBScript User’s Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6%28VS.85%29.aspx)

_Do_ …

  * [Check out samples](https://developer.rhino3d.com/samples/#rhinoscript) on this site
  * [Ask for help on Discourse](http://discourse.mcneel.com/c/scripting)

### Learning More

  * [Crafting Interpreters](https://craftinginterpreters.com/) by Robert Nystrom
  * [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) by Robert C. Martin

## Related topics

  * [What is a Rhino Plugin?](https://developer.rhino3d.com/guides/general/what-is-a-rhino-plugin/)
  * [C Sharp on Wikipedia](https://en.wikipedia.org/wiki/C_Sharp_\(programming_language)
  * [C++ on Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
  * [Python on Wikipedia](https://en.wikipedia.org/wiki/Python_%28programming_language%29)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/general/rhino-
developer-prerequisites/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/general/rhino-
developer-prerequisites/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

