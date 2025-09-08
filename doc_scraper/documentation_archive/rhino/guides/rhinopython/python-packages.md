---
url: https://developer.rhino3d.com/guides/rhinopython/python-packages/
scraped_at: 2025-09-08T15:37:55.053703
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

[Using Python
Packages](https://developer.rhino3d.com/guides/rhinopython/python-packages/)

  * Built-in Modules
  * Local Modules
  * Python Package Index (PyPI)
  * Downloading Python Libraries (Modules)
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Using Python Packages

[New in 8](https://developer.rhino3d.com/8/new)

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Monday, March 17, 2025)

One of the powers of Python is its ability to use thousands of additional
modules in its scripts. There are 4 main sources of Python packages that may
be installed or loaded into Python 3.

  * [Built-in Modules](https://developer.rhino3d.com/guides/rhinopython/python-packages/#built-in-modules) \- Comes with the Rhino.Python install.
  * [Local Modules](https://developer.rhino3d.com/guides/rhinopython/python-packages/#local-modules) \- These are Libraries made from other Python files.
  * [Packages on PyPI](https://developer.rhino3d.com/guides/rhinopython/python-packages/#python-package-index-pypi) \- 500,000 Python Modules available online.
  * [Downloaded Packages](https://developer.rhino3d.com/guides/rhinopython/python-packages/#downloading-python-libraries-modules) \- For some specialized Packages, it may be necessary to download the models manually.

## Built-in Modules

Python comes with many built-in modules that add functionality. To use methods
within built-in modules they simply need to be imported first:

    
    
    import math
    

Here’s a list of most useful predefined modules within Python:

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

## Local Modules

In addition to built-in modules, you can define and import your own Python
functions from other files. This allows you to organize your code into
reusable components.

For instance in a `python_functions.py` file here are two defined functions
`print_rhino_version` and `get_python_version`

    
    
    import Rhino
    import sys
    
    
    def print_rhino_version():
        ver = str(Rhino.RhinoApp.Version)
        versp = ver.split(".")
        print("Major version: " + versp[0])
        print("Service Release: " + versp[1])
    
    
    def get_python_version():
        ver = sys.version
        print("Python version: " + ver)
    

Those functions then can be imported and called by:

    
    
    import python_functions as pf
    
    pf.print_rhino_version()
    

Additional details can be found on [Functions in
Python](https://diveintopython.org/learn/functions) and [Modules in
Python](https://docs.python.org/3/tutorial/modules.html)

## Python Package Index (PyPI)

PyPI is a repository of software for the Python programming language with over
500,000 packages.  
You can specify the packages required for your scripts inside the script
source. This creates self-contained scripts that carry all their requirements
with them. Python 3 will use pip to install packages from PyPI.org. Note: pip
does not support Python 2 any longer.

Popular PyPI packages are:

  * Pandas - data analysis toolkit
  * Numpy - popular scientific computing with Python
  * Scipy - modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing
  * pyyaml - human-readable YAML-serialized data
  * Pillow - Python Imaging Library
  * openpyxl - library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

Looking at a Python 3 default script, we can specify required packages using
this syntax:

    
    
    # r: numpy
    

or

    
    
    # requirements: numpy
    

Let’s create a new Python 3 script and add numpy as a package and use that in
our script:

    
    
    # r: numpy
    
    import numpy
    
    print(f"using numpy: {numpy.version.full_version}\n")
    
    for i in numpy.random.rand(10):
       print(i)
    

Click Run, and the script editor will attempt to install the required packages
before running the script. This process might take some time and the editor is
going to be disabled. Once the packages are installed, editor will continue to
execute the script:

Multiple packages can be install and are recommended to be listed on the same
line:

    
    
    #r: numpy, scipy
    

Additional PyPI version specifiers can also be used as referenced in [Install
PyPI Syntax
Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)

You may search the [PyPI website](https://pypi.org/) for the many available
packages.

## Downloading Python Libraries (Modules)

The last way that packages can be used is to download the packages and put
them into a library on the computer. This allows very tight control of the
packages. This is also a good way to install packages that are not available
on PyPI.

Another method of adding local packages to Python scripts is by adding their
path to the `sys.path`. You can simplify this step by using the # env:
specifier in your scripts to automatically add a path to the `sys.path` before
running your script. Note: Create a customer folder for the downloaded modules
as Rhino updates may overwrite the internal defaults folders.

    
    
    # env: C:/Path/To/Where/My/Library/Is/Located/
    
    import mylibrary
    
    mylibrary.do_something()
    

## Related Topics

  * [What are Python and RhinoScriptSyntax?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python Basic Syntax](https://developer.rhino3d.com/guides/rhinopython/python-statements/)
  * [Python Procedures](https://developer.rhino3d.com/guides/rhinopython/python-procedures/)
  * [Rhinoscript Syntax in Python](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
  * [Rhino.Python Home Page](https://developer.rhino3d.com/guides/rhinopython/)
  * [Python (homepage)](https://www.python.org/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
packages/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
packages/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

