---
url: https://developer.rhino3d.com/guides/rhinoscript/running-scripts-from-macros/
scraped_at: 2025-09-08T15:58:43.951816
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

[Running Scripts from
Macros](https://developer.rhino3d.com/guides/rhinoscript/running-scripts-from-
macros/)

  * How To
    * Creating button or alias for your macro or script
    * Use the macro editor to work out new macros
    * Paste your macro or script into the button or alias
    * Linking to external scripts

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Running Scripts from Macros

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## How To

### Creating button or alias for your macro or script

The simplest way to save and run your macro is from a toolbar button or alias.
If you don’t know how to make a new toolbar button or alias, look in the Help
file. There’s a good explanation. Once you have your new button (or have
chosen to edit an existing one), open the editor by `shift`+right-clicking on
the button. For an alias, you will do the same thing, but instead of creating
a new button, go into _Options_ > _Aliases_ and use the _New_ button to create
a new alias.

### Use the macro editor to work out new macros

The _MacroEditor_ command opens a text editing window in which you can type
macros and try them out without the need to edit a button every time. The run
button on the lower edge of the editor runs the macro. If there is selected
text, it runs the selected text. When it all runs to your satisfaction, copy
and paste the macro to a toolbar button.

![Macro Editor](https://developer.rhino3d.com/images/running-scripts-from-
macros-01.png)

### Paste your macro or script into the button or alias

Now, there are two ways to approach associating the macro or script to your
button or alias. First and simplest is to just copy/paste the whole thing into
the left or right button box (or in the alias box). The advantage of the
button method is that it is portable. That is, if you copy or export the
button to another installation the macro goes with it. Once the test is pasted
in, click _OK_ to exit the button editor, and you’re ready to go!

The paste-in-button (or alias) method is fine for macros of Rhino commands and
shorter, smaller scripts, but it gets a bit unwieldy to edit if there is a
great deal of text. For larger scripts, some people like to place them
externally in a folder with a link so that Rhino can find them. Both toolbar
buttons and aliases can link to external scripts. One advantage of this system
is that all scripts are located in one spot so you can easily find and update
them. The problem here is that if you copy your button or workspace for use
somewhere else, you have to remember to bring the script with it.

### Linking to external scripts

To set up an external scripts folder: Find a logical place to create your
folder. _Take care in choosing this folder. Make sure that the user has
permissions to access it._ Open the _Options_ dialog, and navigate to the
_Files_ tab. In the file search paths box, click the new button and then the
little _…_ button and browse to the location of the scripts folder. Then click
_OK_. Exit the options dialog. Rhino will now go looking for scripts in this
folder.

Currently Python does not read this section, so if you use Python scripts you
will also need to do a similar operation inside the Python script editor: Open
the editor with _EditPythonScript_ and go to _Tools_ > _Options_ and enter the
path to your folder in _Module Search Paths_.

To link your button or alias to an external script: The syntax used will
depend on the type of script. If it is a simple text file with normal Rhino
commands (like a long macro), you will need to use the command
_ReadCommandFile Filename.txt_ Substitute the name of your text file for
_Filename.txt_. Paste that string into the left or right button box and you’re
good to go. To run a _RhinoScript .rvb_ file use the command _LoadScript
Filename.rvb_ instead. In general, that’s all you need to do, but some scripts
are written to run immediately on load. Others are not, so some script
tweaking may be necessary.

![Edit Toolbar Button Dialog](https://developer.rhino3d.com/images/running-
scripts-from-macros-02.png)

You can also paste an entire RhinoScript into a button. For that, start with
the command _-_RunScript_ (not _-_LoadScript_) followed by a space and an open
parentheses. At the end of the script you need a close parentheses. For python
scripts, you want to use _-_RunPythonScript_ instead of just _-_RunScript_.

Don’t forget the dash in front of the command, otherwise it will stop and
prompt you for what script you want to run. The underbar insures that the __-
Runscript_ command will run in languages other than English, but it will not
insure the actual script will do the same. It has to be written correctly as
well.

    
    
    ! _NoEcho -_Runscript (
    
    Paste in
    your entire
    script here
    
    )
    

The button editor showing pasted in complete RhinoScript should look something
like this…

![Edit Toolbar Button Done](https://developer.rhino3d.com/images/running-
scripts-from-macros-03.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/running-
scripts-from-macros/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/running-
scripts-from-macros/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

