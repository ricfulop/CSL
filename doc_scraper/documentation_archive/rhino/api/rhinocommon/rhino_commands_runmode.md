---
url: https://developer.rhino3d.com/api/rhinocommon/rhino.commands.runmode
scraped_at: 2025-09-08T16:05:17.493561
title: Untitled
---

[ _home_](/api/rhinocommon/)

/

[Rhino.Commands](/api/rhinocommon/rhino.commands)

/

RunMode

# RunMode enum

Provides enumerated constants for a command running mode. This is currently
interactive or scripted.

  
_Derived Classes:_

_Namespace:[Rhino.Commands](/api/rhinocommon/rhino.commands)_  
 _RunMode:[references](/api/rhinocommon/references/rhino.commands.runmode)_

 _keyboard_arrow_down_

Values (2)

[**Interactive = 0** Can use dialogs for input. Must use message boxes to
report serious error conditions.](/api/rhinocommon/undefined#)

* * *

[**Scripted = 1** All input must come from command line, GetPoint, GetObject,
GetString, etc. Must use message boxes to report serious error conditions.
Script mode gets used when a command is run with a hyphen (-)
prefix.](/api/rhinocommon/undefined#)

* * *

