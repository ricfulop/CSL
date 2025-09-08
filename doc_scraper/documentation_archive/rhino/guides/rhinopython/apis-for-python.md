---
url: https://developer.rhino3d.com/guides/rhinopython/apis-for-python/
scraped_at: 2025-09-08T15:37:53.184323
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

[APIs Available to
Python](https://developer.rhino3d.com/guides/rhinopython/apis-for-python/)

  * Overview
  * RhinoScriptSyntax
  * RhinoCommon
  * Common Python Modules
  * Python Package Index (PyPI)
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

APIs Available to Python

by [Alain Cormier](https://discourse.mcneel.com/u/Alain/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Python is an extensible programming language with hundreds of additional
modules. This allows Python to be used in many situations both inside Rhino
and outside Rhino. There are some specific additional models that are
specifically of interest related to Rhino and Grasshopper.

These new modules can be accessed in a Python script by including the `import`
method at the top of each Python script:

    
    
    import rhinoscriptsyntax as rs
    import math
    

## RhinoScriptSyntax

The RhinoScriptSyntax methods library contains hundreds of easy-to-use
functions that perform a variety of operations on Rhino. The library allows
Python to be aware of the Rhino’s:

  * Geometry
  * Commands
  * Document objects
  * Application methods

To make these methods easy-to-use, all RhinoScriptSyntax methods return simple
Python variables or Python List-based data structures. Thus, once you are
familiar with Python, you will be able to use any and all functions in the
RhinoScriptSyntax methods library. RhinoScriptSyntax is divided into
[modules](https://developer.rhino3d.com/api/RhinoScriptSyntax/win) that mirror
standard Rhino commands.

A good set of tutorials on using RhinoScript methods can be found in the
[Python in Rhino
tutorials](https://developer.rhino3d.com/guides/rhinopython/#python-in-rhino)

For those that are familiar with the RhinoScript language in Rhino for
Windows. RhinoScriptSyntax is meant to duplicate the functionality provided by
the RhinoScript language. If you are familiar with RhinoScript in Rhino for
Windows the transition to Python in Rhino should be natural.

## RhinoCommon

RhinoCommon is an extensive, low level .NET library of the Rhino SDK. It is
meant for more experienced programmers that would like to most extensive
access to Rhino and its classes.

An important detail that will become important as you are learning to script
Rhino with Python is that the implementation of Python that is embedded in
Rhino is called IronPython: a Python implementation in C# that runs on the
.Net/mono platform which means that in addition to the Python language
features and the [rhinoscriptsyntax
package](https://developer.rhino3d.com/api/RhinoScriptSyntax/win), you also
have access to all the libraries in .Net/mono and
[RhinoCommon](../../rhinocommon/what-is-rhinocommon/).

The rhinoscriptsyntax package is implemented on top of RhinoCommon so reading
the source code is a great way to learn how to use RhinoCommon from Python.
The source code files are included in the Rhino distribution on your computer
and the default location is:

    
    
    /Users/<YOUR_HOME_DIRECTORY>/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/ironpython/settings/lib/rhinoscript
    

## Common Python Modules

There are many modules other modules for Python. Here are a list of the most
useful to modules for Rhino.Python are:

  * Date and Time 
    * datetime — Basic date and time types
    * time — Time access and conversions
  * Numeric and Mathematical Modules 
    * math — Mathematical functions
    * fractions — Rational numbers
    * random — Generate pseudo-random numbers
  * File and Directory Access 
    * System.IO — Common pathname manipulations
    * tempfile — Generate temporary files and directories
    * csv — CSV File Reading and Writing
  * String Services 
    * string — Common string operations
    * StringIO — Read and write strings as files
    * fpformat — Floating point conversions

A complete list of predefined modules in Python, see the [Python Standard
Library modules](https://docs.python.org/3/library/)

## Python Package Index (PyPI)

PyPI is a repository of software for the Python programming language with over
500,000 packages. Popular PiPy cpackage are:

  * Pandas - data analysis toolkit
  * Numpy - popular scientific computing with Python
  * Scipy - modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing
  * pyyaml - human-readable YAML-serialized data
  * Pillow - Python Imaging Library
  * openpyxl - library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

The [PyPI website](https://pypi.org/) can be searched for the many packages
that are availble.

## Related Topics

  * [What are Python and RhinoScriptSyntax?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python Basic Syntax](https://developer.rhino3d.com/guides/rhinopython/python-statements/)
  * [Python Procedures](https://developer.rhino3d.com/guides/rhinopython/python-procedures/)
  * [Rhinoscript Syntax in Python](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
  * [Rhino.Python Home Page](https://developer.rhino3d.com/guides/rhinopython/)
  * [Python (homepage)](https://www.python.org/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/apis-
for-python/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/apis-
for-python/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

