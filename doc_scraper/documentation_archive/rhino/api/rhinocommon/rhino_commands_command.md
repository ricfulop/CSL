---
url: https://developer.rhino3d.com/api/rhinocommon/rhino.commands.command
scraped_at: 2025-09-08T16:05:15.500757
title: Untitled
---

[_home_](/api/rhinocommon/)

/

[Rhino.Commands](/api/rhinocommon/rhino.commands)

/

Command

# Command class

Defines a base class for all commands. This class is abstract.

  
_Derived Classes:__[SelCommand](/api/rhinocommon/rhino.commands.selcommand)
_,___[TransformCommand](/api/rhinocommon/rhino.commands.transformcommand)_

 _Namespace:[Rhino.Commands](/api/rhinocommon/rhino.commands)_  
 _Command:[references](/api/rhinocommon/references/rhino.commands.command)_

 _keyboard_arrow_down_

Constructors (1)

[**Command**() Default protected constructor. It only allows instantiation
through sub-classing.](/api/rhinocommon/rhino.commands.command/command#\(\))

* * *

_keyboard_arrow_down_

Properties (8)

[**CommandContextHelpUrl** Gets the URL of the command contextual help. This
is usually a location of a local CHM file.  
The default implementation return an empty
string.](/api/rhinocommon/rhino.commands.command/commandcontexthelpurl#)

* * *

[**EnglishName** Gets the name of the command. This method is
abstract.](/api/rhinocommon/rhino.commands.command/englishname#)

* * *

[**Id** Gets the unique ID of this command. It is best to use a Guid attribute
for each custom derived command class since this will keep the id consistent
between sessions of Rhino
<b>System.Runtime.InteropServices.GuidAttribute</b>](/api/rhinocommon/rhino.commands.command/id#)

* * *

[**LastCommandId** Gets the ID of the last
commands.](/api/rhinocommon/rhino.commands.command/lastcommandid#)

* * *

[**LastCommandResult** Gets the result code of the last
command.](/api/rhinocommon/rhino.commands.command/lastcommandresult#)

* * *

[**LocalName** Gets the local name of the
command.](/api/rhinocommon/rhino.commands.command/localname#)

* * *

[**PlugIn** Gets the plug-in where this commands is
placed.](/api/rhinocommon/rhino.commands.command/plugin#)

* * *

[**Settings** Gets the settings of the
command.](/api/rhinocommon/rhino.commands.command/settings#)

* * *

_keyboard_arrow_down_

Methods (15)

[**DisplayHelp**(Guid commandId) Displays help for a
command.](/api/rhinocommon/rhino.commands.command/displayhelp#\(guid\))

* * *

[**GetCommandContextHelpUrl**(Guid commandId) Returns a command's context help
url.](/api/rhinocommon/rhino.commands.command/getcommandcontexthelpurl#\(guid\))

* * *

[**GetCommandNames**(Boolean english,Boolean loaded) Gets list of command
names in Rhino. This list does not include Test, Alpha, or System
commands.](/api/rhinocommon/rhino.commands.command/getcommandnames#\(boolean,boolean\))

* * *

[**GetCommandStack**() Determines if Rhino is currently running a command.
Because Rhino allow for transparent commands (commands that can be run from
inside of other commands), this method returns the total ids of active
commands.](/api/rhinocommon/rhino.commands.command/getcommandstack#\(\))

* * *

[**GetMostRecentCommands**() Gets an array of most recent command
descriptions.](/api/rhinocommon/rhino.commands.command/getmostrecentcommands#\(\))

* * *

[**InCommand**() Determines if Rhino is currently running a
command.](/api/rhinocommon/rhino.commands.command/incommand#\(\))

* * *

[**InScriptRunnerCommand**() This is a low level tool to determine if Rhino is
currently running a script running command like "ReadCommandFile" or the
RhinoScript plug-in's
"RunScript".](/api/rhinocommon/rhino.commands.command/inscriptrunnercommand#\(\))

* * *

[**IsCommand**(String name) Determines is a string is a
command.](/api/rhinocommon/rhino.commands.command/iscommand#\(string\))

* * *

[**IsValidCommandName**(String name) Determines if a string is a valid command
name.](/api/rhinocommon/rhino.commands.command/isvalidcommandname#\(string\))

* * *

[**LookupCommandId**(String name,Boolean searchForEnglishName) Returns the ID
of a
command.](/api/rhinocommon/rhino.commands.command/lookupcommandid#\(string,boolean\))

* * *

[**LookupCommandName**(Guid commandId,Boolean englishName) Returns the command
name given a command
ID.](/api/rhinocommon/rhino.commands.command/lookupcommandname#\(guid,boolean\))

* * *

[**OnHelp**() ____ Is called when the user needs assistance with this
command.](/api/rhinocommon/rhino.commands.command/onhelp#\(\))

* * *

[**ReplayHistory**(ReplayHistoryData replayData) ____ Repeats an operation of
a command.  
In order to make this function work, you will likely need to grab the Result
property that gives the list of input objects. Then, you will be able to
replace these inputs by using one of the UpdateToX() methods of the
ReplayHistoryResult.  
You should NOT use any document AddX() or ReplaceX() functions, as they will
break
history.](/api/rhinocommon/rhino.commands.command/replayhistory#\(replayhistorydata\))

* * *

[**RunCommand**(RhinoDoc doc, RunMode mode) __ Executes the
command.](/api/rhinocommon/rhino.commands.command/runcommand#\(rhinodoc,runmode\))

* * *

[**RunProxyCommand**(RunCommandDelegate commandCallback, RhinoDoc doc,Object
data) Execute some code as if it were running in a
command](/api/rhinocommon/rhino.commands.command/runproxycommand#\(runcommanddelegate,rhinodoc,object\))

* * *

 _keyboard_arrow_down_

Events (3)

[**BeginCommand** Called just before
command.RunCommand().](/api/rhinocommon/rhino.commands.command/begincommand#)

* * *

[**EndCommand** Called immediately after
command.RunCommand().](/api/rhinocommon/rhino.commands.command/endcommand#)

* * *

[**UndoRedo** Used to monitor Rhino's built in undo/redo
support.](/api/rhinocommon/rhino.commands.command/undoredo#)

* * *

