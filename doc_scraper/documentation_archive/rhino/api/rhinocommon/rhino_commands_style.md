---
url: https://developer.rhino3d.com/api/rhinocommon/rhino.commands.style
scraped_at: 2025-09-08T16:05:19.449974
title: Untitled
---

[_home_](/api/rhinocommon/)

/

[Rhino.Commands](/api/rhinocommon/rhino.commands)

/

Style

# Style enum

Defines bitwise mask flags for different styles of commands, such as
**Style.Hidden** or **Style.DoNotRepeat** .

  
_Derived Classes:_

_Namespace:[Rhino.Commands](/api/rhinocommon/rhino.commands)_  
 _Style:[references](/api/rhinocommon/references/rhino.commands.style)_

 _keyboard_arrow_down_

Values (6)

[**None = 0** No flag is defined.](/api/rhinocommon/undefined#)

* * *

[**Hidden = 1** Also known as a "test" command. The command name does not
auto-complete when typed on the command line an is therefore not discoverable.
Useful for writing commands that users don't normally have access
to.](/api/rhinocommon/undefined#)

* * *

[**ScriptRunner = 2** For commands that want to run scripts as if they were
typed at the command line (like RhinoScript's RunScript
command)](/api/rhinocommon/undefined#)

* * *

[**Transparent = 4** Transparent commands can be run inside of other commands.
The command does not modify the contents of the model's geometry in any way.
Examples of transparent commands include commands that change views and toggle
snap states. Any command that adds or deletes, a view cannot be
transparent.](/api/rhinocommon/undefined#)

* * *

[**DoNotRepeat = 8** The command should not be repeated by pressing "ENTER"
immediately after the command finishes.](/api/rhinocommon/undefined#)

* * *

[**NotUndoable = 16** By default, all commands are undo-
able.](/api/rhinocommon/undefined#)

* * *

