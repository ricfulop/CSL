---
url: https://developer.rhino3d.com/guides/scripting/advanced-scripteditor-macros/#script-search-paths
scraped_at: 2025-09-08T16:05:30.305113
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

[ScriptEditor Command in
Macros](https://developer.rhino3d.com/guides/scripting/advanced-scripteditor-
macros/)

  * ScriptEditor Command Options
  * Script Search Paths

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

ScriptEditor Command in Macros

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Monday, October 7, 2024)

## ScriptEditor Command Options

_ScriptEditor_ command has a few options that could be used in macros. Run
`_-ScriptEditor` command in Rhino prompt to see these options (`-` is for non-
interactive mode, and `_` ensures command works in all Rhino UI languages.
[See Command Macros & Scripting](https://docs.mcneel.com/rhino/8/help/en-
us/information/rhinoscripting.htm) for more):

  * **Edit (E):** This is the default option when running ScriptEditor command in Rhino. It opens the standalone Script Editor and initialized all languages.

  * **Run (R):** Runs given script using the new scripting infrastructure in Rhino 8. It can run scripts or script files of any supported language.

    * **Browse (B):** Using this suboption, allows to browse and select a script file
    * Run a script file in a macro this way 👉 `_-ScriptEditor _R "C:\path\to\script.py"`
    * Run a script in a macro this way 👇. Note that the language specifier (`#! python 3`, `#! python 2`, or `// #! csharp`) is necessary so the command can determine which language to run the script with:

    
    
    _-ScriptEditor _R (
        #! python 3
        print("Hello Rhino")
    )
    

  * **Open (O):** : Opens given script file in ScriptEditor 
    * **Browse (B):** Using this suboption, allows to browse and open a script file
    * Open a script file to edit this way 👉 `_-ScriptEditor _O "C:\path\to\script.py"`

## Script Search Paths

Normally you have specify the full script path in a macro like `_-ScriptEditor
_R "C:\path\to\HelloWorld.py"` to run the script. However, you can place your
most common scripts under a directory, and add the path of that directory to
[Rhino File Search Paths](https://docs.mcneel.com/rhino/8/help/en-
us/options/files_search_paths.htm). When search paths are set up, you can run
`_-ScriptEditor _R "HelloWorld.py"` and the command can find the script under
specified search paths.

Please note that [Python Module Search
Paths](https://developer.rhino3d.com/guides/scripting/editor-configs/#python-
paths) are not searched for scripts. They are purely to search and find python
modules.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/advanced-
scripteditor-macros/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/advanced-
scripteditor-macros/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

