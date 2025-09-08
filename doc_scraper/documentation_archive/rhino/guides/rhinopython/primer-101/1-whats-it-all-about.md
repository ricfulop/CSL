---
url: https://developer.rhino3d.com/guides/rhinopython/primer-101/1-whats-it-all-about/
scraped_at: 2025-09-08T15:37:39.078414
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

[1 What's it all
about?](https://developer.rhino3d.com/guides/rhinopython/primer-101/1-whats-
it-all-about/)

  * 1.1 Macros
  * 1.2 Scripts
  * 1.3 Running Scripts
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) / [Rhino.Python
101](https://developer.rhino3d.com/en/guides/rhinopython/primer-101/) /

1 What's it all about?

[New in 8](https://developer.rhino3d.com/8/new)

by [Skylar Tibbits](https://discourse.mcneel.com/u//), [Arthur van der
Harten](https://discourse.mcneel.com/u/aharten/), and [Steve
Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated: Wednesday,
December 5, 2018)

## 1.1 Macros

Rhinoceros is based on a command-line interface. This means you can control it
by using only the keyboard. You type in the commands and the program will
execute them. Ever since the advent of the mouse, a user interface which is
purely command-line based is considered to be primitive, and rightly so.
Instead of typing:

    
    
    Line 0,0,0 10,0,0
    

you can also click on the Line button and then twice in the viewport to define
the starting and ending points of a line-curve. Because of this second
(graphical) interface some people have done away with the command-line
entirely. Emotions run high on the subject; some users are command-line
fanatics, others use only toolbars and menus. Programmers have no emotions in
this respect, they are all wedded to the command-line. It’s no use programming
the mouse to go to a certain coordinate and then simulate a mouse click, that
is just plain silly. Programmers pump text into Rhino and they expect to get
text in return.

The lowest form of programming in Rhino is using macros. I do not wish to
offend those of you who write macros for a living, but it cannot be denied
that it is a very primitive way to automate processes. I shall only briefly
pause at the subject of macros, partly so we know which is which and partly
because we might at some point simulate macros using RhinoScriptSyntax in
Python.

A macro is a prerecorded list of orders for Rhino to execute. The __Line_
command at the top of this page is an example of a very simple macro. If your
job is to open Rhino files, add a line from 0,0,0 to 10,0,0 to each one and
save the file again, you would probably get very tired very quickly from
typing `_Line w0,0,0 w10,0,0` six times a minute. Enter macros. Macros allow
you to automate tasks you would normally do by hand but not by brain. Macros
cannot be made smart, nor do they react to the things they help create.
They’re a bit like traffic wardens in that respect. An example of a more
sophisticated macro would be:

    
    
    _SelNone
    _Polygon _NumSides=6 w0,0,0 w10,0,0
    _SelLast
    -_Properties _Object _Name RailPolygon _Enter _Enter
    _SelNone
    _Polygon _NumSides=6 w10,0,0 w12,0,0
    _SelLast
    _Rotate3D w0,0,0 w10,0,0 90
    -_Properties _Object _Name ProfilePolygon _Enter _Enter
    _SelNone
    -_Sweep1 -_SelName RailPolygon -_SelName ProfilePolygon _Enter _Enter Closed=Yes _Enter 
    

![https://developer.rhino3d.com/images/hexagonaltorus.svg](https://developer.rhino3d.com/images/hexagonaltorus.svg)

The above code will create the same hexagonal torus over and over again. It
might be useful, but it’s not flexible. You can type the above text into the
command-line by hand, or you can put it into a button. You can even copy-paste
the text directly into Rhino.

Incidentally, the underscores before all the command names are due to Rhino
localization. Using underscores will force Rhino to use English command names
instead of -say- Italian or Japanese or whatever the custom setting is. You
should always force English command names since that is the only guarantee
that your code will work on all copies of Rhino worldwide.

The hyphen in front of the __Properties_ and __Sweep1_ command is used to
suppress dialog boxes. If you take the hyphens out you will no longer be able
to change the way a command works through the command -line.

There’s no limit to how complex a macro can become, you can keep adding
commands without restrictions, but you’ll never be able to get around the
limitations that lie at the heart of macros.

## 1.2 Scripts

The limitations of macros have led to the development of scripting languages.
Scripts are something halfway between macros and true (compiled) programs and
plug-ins. Unlike macros they can perform mathematical operations, evaluate
variable conditions, respond to their environment and communicate with the
user. Unlike programs they do not need to be compiled prior to running.
Rhinoceros implements the standard ‘Microsoft® Visual Basic® Scripting
Edition’ language, as well as the Python Programming language. This primer
will introduce the Python Programming Language and how to utilize its
functionality within Rhinoceros.

Scripts, then, are text files which are interpreted one line at a time. But
here’s the interesting part; unlike macros, scripts have control over which
line is executed next. This flow control enables the script to skip certain
instructions or to repeat others. Flow control is achieved by what is called
“conditional evaluation” and we must familiarize ourselves with the language
rules of Python before we can take advantage of flow control.

The language rules are usually referred to as the syntax and they indicate
what is and isn’t valid:

  1. “There is no apple cake here.” » valid 
     1. “There is here no apple cake”» invalid
  2. “Here, there is no apple cake."» valid
  3. “There is no Apfelstrudel here."» invalid

The above list is a validity check for English syntax rules. The first and
third lines are proper English and the others are not. However, there are
certain degrees of wrong. Nobody will misunderstand the second line just
because the word order is wrong. The forth line is already a bit harder since
it features a word from a different language.

Although most of us are smart enough to understand all four lines, a computer
is not.

Python is a wonderful language for beginners or advanced programmers. It
offers a simple and efficient syntax as well as powerful programming
functions, object-oriented capabilities and a large fan-base with user-built
libraries. Also, since Rhino Python is available on both Windows and Mac, the
exact same python scripts will run on both versions of Rhino! Don’t get too
excited yet - will get more of the details in the following sections!

## 1.3 Running Scripts

There are several ways to run scripts in Rhino, each has its own
(dis)advantages. You could store scripts as external text files and have Rhino
load them for you whenever you want to run them. You could also use Rhino’s
in-build script editor which means you can run the Scripts directly from the
editor. The last option is to embed scripts in toolbar buttons, which makes it
very hard to edit them, but much easier to distribute them.

Throughout this book, I will use the in-build editor method. I find this to be
the best way to work on simple scripts. In order to run a script via the in-
build editor, use the __ScriptEditor_ command to activate it, then type in
your script and press the Run button:

![script_editor.png](script_editor.png)

All the example code in this primer can be copy-pasted directly into the
__ScriptEditor_ dialog.

## Next Steps

Now that you know what a scripting language is, check out the [Python
Essentials](https://developer.rhino3d.com/guides/rhinopython/primer-101/2-python-
essentials/) guide to learn more about the Python language.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/primer-101/1-whats-
it-all-about/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/primer-101/1-whats-
it-all-about/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

