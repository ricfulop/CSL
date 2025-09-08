---
url: https://developer.rhino3d.com/guides/scripting/scripting-command/#help
scraped_at: 2025-09-08T16:02:03.550747
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

[ScriptEditor
Command](https://developer.rhino3d.com/guides/scripting/scripting-command/)

  * Opening Script Editor
  * First Script
  * Edit Script
  * Running Scripts
  * Debugging Scripts
  * Using Packages
    * Python Packages
    * Python Libraries (Modules)
    * NuGet Packages
  * Editor Features
    * Explorer
    * Search
    * Help

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

ScriptEditor Command

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Thursday, August 15, 2024)

## Opening Script Editor

To access the unified script editor in Rhino, type `ScriptEditor` in the
command prompt and select enter to run the command:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/01.png)

If this is the first time you are using the scripting features in Rhino, the
editor will immediately start initializing the languages. Setting up the
Python 3 ([CPython](https://www.python.org)) environment is the most important
and normally the longest task here. The editor will display a progress bar
showing each initialization task. All editor features are disabled at this
point so you should wait for the initialization process to complete.

![](https://developer.rhino3d.com/guides/scripting/scripting-command/02.png)

Once the initialization is complete, the editor will load all the previously
open scripts (if any), and will enable the buttons and menus:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/03.png)

## First Script

Let’s create our first script. We will use IronPython for this example. From
the Dashboard (row of buttons at the top of the editor window), click on the
**New** button and choose “Iron Python” to create the first script:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/04.png)

The default script contains a good amount of information under the `NOTES:`
multiline comment (or _docstring_). We can skip that for now, as we will
discuss these more advanced topics later in this guide. Let’s remove those
comments.

![](https://developer.rhino3d.com/guides/scripting/scripting-command/05.png)

Click on the **Save** button on the Dashboard to save the script:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/06.png)

## Edit Script

Let’s type a new line at the bottom of the script. The editor will help
autocomplete the names:

    
    
    print(Rhino.RhinoApp.Version)
    

![](https://developer.rhino3d.com/guides/scripting/scripting-command/07.png)

![](https://developer.rhino3d.com/guides/scripting/scripting-command/08.png)

In this example, the script tab showing the script’s name (`FirstScript.py`)
now shows a dark circle by the name denoting that the script has been modified
but not saved.

![](https://developer.rhino3d.com/guides/scripting/scripting-command/09.png)

## Running Scripts

Click the green **Run** button on the Dashboard (or hit **F5**) to run the
script. The only line in our script that produces a result is the `print`
statement. This will print the version of Rhino we are using in the terminal.
Click on the **Terminal** tab at the bottom of the screen to open up the
terminal tray and see the printed results.

![](https://developer.rhino3d.com/guides/scripting/scripting-command/10.png)

The Terminal tray has a series of buttons on the top-right side to **Copy**
and **Clear Contents** of terminal. Most panels and trays in the editor follow
the same design, with buttons for the most-used actions in the top-right
corner.

![](https://developer.rhino3d.com/guides/scripting/scripting-command/11.png)

## Debugging Scripts

The script editor can debug scripts of any supported language. During debug,
we can execute the script line by line or pause the execution at certain lines
called **Breakpoints** and inspect the values of global and local variables.

Let’s add these lines to our script:

    
    
    total = 0
    for i in range(5):
        total += i
    

![](https://developer.rhino3d.com/guides/scripting/scripting-command/12.png)

Move your mouse cursor to the left side of the line number column on line 12
and click. This should add a red dot and mark that line as a **Breakpoint**.
Let’s do the same for line number 14:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/13.png)

The **Breakpoints** tray at the bottom will show all the active breakpoints,
and will provide buttons to Clear or Toggle either all of them or individual
breakpoints:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/14.png)

When you add breakpoints, the editor makes a few UI changes and provides a few
more utilities for debugging:

  * The **Run** button will change to **Debug**
  * **Variables** , **Watch** , and **Call Stack** trays will be added to the bottom tray bar

Now click on the green **Debug** button on the Dashboard. The editor will run
the script and will:

  * Stop at the first breakpoint on line 12
  * Highlight the breakpoint line in orange and show an arrow on the left side of the line
  * Highlight the Status Bar in orange to show we are debugging a script
  * Activate the debug control buttons on the Dashboard
  * Open the **Variables** tray at the bottom to show global and local variables

![](https://developer.rhino3d.com/guides/scripting/scripting-command/15.png)

We can control the execution of script using the debug control buttons on the
Dashboard:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/16.png)

From left to right, they are:

  * **Continue:** continues running the script until it stops on another breakpoint
  * **Step Over:** executes current line and moves on the next line
  * **Step In:** if the current line includes a function call, this will step into the lines defining the function code
  * **Step Out:** if previously stepped into a function code, this will continue executing the function code until control is returned from the function to the calling code and will stop there
  * **Stop:** stops debugging the script and does not continue executing the rest

Click on **Step Over** to see the execution move to the next line:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/17.png)

Click on **Step Over** one more time and script should stop on line 14. At
this point the **Variables** tray will be showing the current values (and
their data types) for `i` and `total` variables:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/18.png)

Progressively clicking on **Step Over** , will continue executing the script
and modifying the variables. At each stop, **Variables** tray highlights the
modified value by a red dot to left of the variable name:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/19.png)

![](https://developer.rhino3d.com/guides/scripting/scripting-command/20.png)

![](https://developer.rhino3d.com/guides/scripting/scripting-command/21.png)

Once the script ends, the editor UI changes back to normal, and the
**Variables** tray will show the last state of the variables. The tray will
keep these data until the script is closed or another session of debugging is
started:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/22.png)

At any point in time, you can use the **Toggle** button in the **Breakpoints**
panel to activate or deactivate the breakpoints. Deactivated breakpoints will
show up as gray dots in the editor:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/23.png)

## Using Packages

### Python Packages

You can specify the packages required for your scripts inside the script
source. This creates self-contained scripts that carry all their requirements
with them.

  * Python 3 will use **pip** to install packages from [PyPI.org](https://pypi.org)
    * **pip** does not support Python 2 anymore so we are limited to the packages used in IronPython
  * C# will use **NuGet** to install packages from [NuGet.org](https://www.nuget.org)

The default script for each language has a NOTE section at the top that
describes how to specify the requirements in your scripts. Looking at Python 3
default script, we can specify required packages using this syntax:

    
    
    # r: numpy
    

or

    
    
    # requirements: numpy
    

Let’s create a new Python 3 script and add `numpy` as a package and use that
in our script:

    
    
    # requirements: numpy
    
    import numpy
    
    print(f"using numpy: {numpy.version.full_version}\n")
    
    for i in numpy.random.rand(10):
        print(i)
    

![](https://developer.rhino3d.com/guides/scripting/scripting-command/24.png)

Click Run, and the script editor will attempt to install the required packages
before running the script. This process might take some time and the editor is
going to be disabled. Once the packages are installed, editor will continue to
execute the script:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/25.png)

### Python Libraries (Modules)

Another method of adding local packages to Python scripts is by adding their
path to the `sys.path`. You can simplify this step by using the `# env:`
specifier in your scripts to automatically add a path to the `sys.path` before
running your script:

    
    
    # env: C:/Path/To/Where/My/Library/Is/Located/
    
    import mylibrary
    
    mylibrary.do_something()
    

### NuGet Packages

The same convention applies to C# scripts. They use a different syntax to
specify packages that match the format provided on the NuGet.org page for the
package you want to use:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/26.png)

Here is an example script that uses the
[RestSharp](https://www.nuget.org/packages/RestSharp/110.2.0) NuGet package to
grab some data from a website. Note the first line of the script specifies the
**RestSharp** package version `110.2.0`

    
    
    #r "nuget: RestSharp, 110.2.0"
     
    using System;
    using System.Collections.Generic;
    using Rhino;
     
    using RestSharp;
    using RestSharp.Authenticators;
     
    var client = new RestClient("https://httpbin.org");
    var request = new RestRequest("get");
    var response = client.Get(request);
     
    Console.WriteLine(response.Content);
    

![](https://developer.rhino3d.com/guides/scripting/scripting-command/27.png)

## Editor Features

Script Editor has other noteworthy features. Here we highlight a few that are
used more often:

### Explorer

Use the **Explorer** panel to the left of the editor window to browse and edit
your local scripts. Click the **Explorer** tab to open the panel, and click on
the folder icon on the top-right corner of the panel to browser to a folder:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/28.png)

Once a folder is set, Explorer will show the scripts in that folder and all
subfolders and will activate a new set of buttons to manage the scripts:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/29.png)

### Search

Click on the **Search** tab to open the Search panel. Searching for a keyword
will show all the matches for all the open scripts in the panel. You can click
on any matched item to navigate to the script and line:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/30.png)

### Help

Click on the **Help** tab to open the Help panel. This panel provides a simple
method to get help on Rhino and Grasshopper APIs and provides Python modules:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/31.png)

Use the search field to search for class or method names. The info panel at
the bottom provides some info about the method and its parameters:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/32.png)

If the selected member has online documentation, a preview tab opens in the
editor showing the contents:

![](https://developer.rhino3d.com/guides/scripting/scripting-command/33.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/scripting-
command/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/scripting-
command/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

