---
url: https://developer.rhino3d.com/guides/rhinopython/your-first-python-script-in-rhino-windows/
scraped_at: 2025-09-08T15:37:04.833600
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

[Your First Python Script in
Rhino](https://developer.rhino3d.com/guides/rhinopython/your-first-python-
script-in-rhino-windows/)

  * The Complete Script
  * The HelloWorld Function
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Your First Python Script in Rhino

[New in 8](https://developer.rhino3d.com/8/new)

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

You will learn how to display a message box in Rhino that says “Hello World.”
It covers the most basic concepts for editing, loading, and running scripts.

## The Complete Script

    
    
    import rhinoscriptsyntax as rs
    
    rs.MessageBox ("Hello World")
    

To test the Script:

  * Start Rhino
  * At the command prompt, type Scripteditor and press Enter.
  * The Script editor dialog box appears.
  * In the script Code window, type the code sample above.
  * Click the “Run the script” button.
  * The editor dialog box disappears, and the message below appears:

## The HelloWorld Function

If you were writing a more complex script, and wanted to display “Hello World”
at strategic points throughout the script, you could write this code every
time you wanted the message to appear.

But if you changed your mind and wanted it to say “Howdy World” instead, you’d
have to search for all the places “Hello World” was used, and replace them.

An easier way to solve this problem is to write a Function (`def` is used to
define the function). At several places throughout your script, you call the
function. The function handles displaying the message, so you only have to
change the message in one place.

Here’s what the function definition looks like:

    
    
    import rhinoscriptsyntax as rs
    
    def HelloWorld():
        rs.MessageBox ("Hello World")
    

If you click the run button at this time nothing will happen. Nothing
happened? That’s because the RhinoScript defined the Subroutine but did not
actually call it. To call the subroutine, either add this line of code and
click Run.

To call this function, simply add this to the bottom of the script:

    
    
    HelloWorld()
    

In Python the functions definitions need to come before being called in the
code.

#### Testing HelloWorld

  * At the command prompt, type ScriptEditor and press Enter.
  * The Scripteditor dialog box appears.
  * In the script Code window, type

    
    
    import rhinoscriptsyntax as rs
    
    def HelloWorld():
        rs.MessageBox ("Hello World")
    
    HelloWorld()
    

  * Click the Run button.

When you do more than write a couple lines of script, it becomes necessary to
save the script to a file so that you can run the script without typing it
every time.

#### To save your script:

In the Edit Script dialog box, Click the Save button. Save the file as
“HelloWorld.py”.

#### Running HelloWorld.py

  * At the Command prompt, type RunPythonScript and press Enter.
  * In the Run python script dialog box, select “HelloWorld.py” and click Open.

Your script will run, and display the familiar “Hello World” dialog box.

## Related Topics

  * [What is RhinoPython?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Running Scripts](https://developer.rhino3d.com/guides/rhinopython/python-running-scripts/)
  * [Canceling Scripts](https://developer.rhino3d.com/guides/rhinopython/python-canceling-scripts/)
  * [Editing Scripts](https://developer.rhino3d.com/guides/rhinopython/python-editing-scripts)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/your-
first-python-script-in-rhino-windows/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/your-
first-python-script-in-rhino-windows/index.md) [
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

