---
url: https://developer.rhino3d.com/api/RhinoScriptSyntax
scraped_at: 2025-09-08T15:50:39.889273
title: Untitled
---

[RhinoDeveloper](/)

[design, model, present, analyze, realize...](/)

[![](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account ![user
avatar](https://www.rhino3d.com/user/avatar/) ](https://www.rhino3d.com/my-
account/ "Manage your account, licenses, and teams") [sign
in](https://www.rhino3d.com/my-account/ "Sign in to manage your account,
licenses, and teams")

[RhinoScriptSyntax](https://developer.rhino3d.com/api/RhinoScriptSyntax/)

  * application
  * block
  * curve
  * dimension
  * document
  * geometry
  * grips
  * group
  * hatch
  * layer
  * light
  * line
  * linetype
  * material
  * mesh
  * object
  * plane
  * pointvector
  * selection
  * surface
  * toolbar
  * transformation
  * userdata
  * userinterface
  * utility
  * view

[API References](https://developer.rhino3d.com/en/api/) /

RhinoScriptSyntax

## application

AddAlias

    
    
    AddAlias(alias, macro)

Add new command alias to Rhino. Command aliases can be added manually by using
Rhino's Options command and modifying the contents of the Aliases tab.

##### Parameters:

    
    
    alias (str): Name of new command alias. Cannot match command names or existing
            aliases.
    macro (str): The macro to run when the alias is executed.

##### Returns:

    
    
    bool: True or False indicating success or failure.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    rs.AddAlias("OriginLine",  "!_Line 0,0,0")

##### See Also:

  * AliasCount
  * AliasMacro
  * AliasNames
  * DeleteAlias
  * IsAlias

  

AddSearchPath

    
    
    AddSearchPath(folder, index=-1)

Add new path to Rhino's search path list. Search paths can be added by using
Rhino's Options command and modifying the contents of the files tab.

##### Parameters:

    
    
    folder (str): A valid folder, or path, to add.
    index (number, optional): Zero-based position in the search path list to insert.
                           If omitted, path will be appended to the end of the
                           search path list.

##### Returns:

    
    
    number: The index where the item was inserted if success.
         -1 on failure.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddSearchPath("C:\\My Python Scripts")

##### See Also:

  * DeleteSearchPath
  * SearchPathCount
  * SearchPathList

  

AliasCount

    
    
    AliasCount()

Returns number of command aliases in Rhino.

##### Returns:

    
    
    number: the number of command aliases in Rhino.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("alias count = {}".format(rs.AliasCount()))

##### See Also:

  * AddAlias
  * AliasMacro
  * AliasNames
  * DeleteAlias
  * IsAlias

  

AliasMacro

    
    
    AliasMacro(alias, macro=None)

Returns or modifies the macro of a command alias.

##### Parameters:

    
    
    alias (str): The name of an existing command alias.
    macro (str, optional): The new macro to run when the alias is executed. If omitted, the current alias macro is returned.

##### Returns:

    
    
    str:  If a new macro is not specified, the existing macro if successful.
    str:  If a new macro is specified, the previous macro if successful.
    null:  None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    aliases = rs.AliasNames()
    for alias in aliases:
        print("{} -> {}".format(alias, rs.AliasMacro(alias)))

##### See Also:

  * AddAlias
  * AliasCount
  * AliasNames
  * DeleteAlias
  * IsAlias

  

AliasNames

    
    
    AliasNames()

Returns a list of command alias names.

##### Returns:

    
    
    str: a list of command alias names.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    aliases = rs.AliasNames()
    for alias in aliases: print(alias)

##### See Also:

  * AddAlias
  * AliasCount
  * AliasMacro
  * DeleteAlias
  * IsAlias

  

AppearanceColor

    
    
    AppearanceColor(item, color=None)

Returns or modifies an application interface item's color.

##### Parameters:

    
    
    item (number): Item number to either query or modify
           0  = View background
           1  = Major grid line
           2  = Minor grid line
           3  = X-Axis line
           4  = Y-Axis line
           5  = Selected Objects
           6  = Locked Objects
           7  = New layers
           8  = Feedback
           9  = Tracking
           10 = Crosshair
           11 = Text
           12 = Text Background
           13 = Text hover
    color ([r255,g255,b255], optional): The new color value in (r255,g255,b255). If omitted, the current item color is returned.

##### Returns:

    
    
    tuple (r255,g255,b255): if color is not specified, the current item color.
    tuple (r255,g255,b255): if color is specified, the previous item color.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    oldColor = rs.AppearanceColor(0)
    newColor = rs.GetColor(oldColor)
    if newColor is not None:
        rs.AppearanceColor(0, newColor)
        rs.Redraw()

##### See Also:

  * GetColor

  

AutosaveFile

    
    
    AutosaveFile(filename=None)

Returns or changes the file name used by Rhino's automatic file saving

##### Parameters:

    
    
    filename (str, optional): Name of the new autosave file

##### Returns:

    
    
    str: if filename is not specified, the name of the current autosave file
    str: if filename is specified, the name of the previous autosave file

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = rs.AutosaveFile()
    print("The current autosave file is {}".format(file))

##### See Also:

  * AutosaveInterval
  * EnableAutosave

  

AutosaveInterval

    
    
    AutosaveInterval(minutes=None)

Returns or changes how often the document will be saved when Rhino's automatic
file saving mechanism is enabled

##### Parameters:

    
    
    minutes (number, optional): The number of minutes between saves

##### Returns:

    
    
    number: if minutes is not specified, the current interval in minutes
    number: if minutes is specified, the previous interval in minutes

##### Example:

    
    
    import rhinoscriptsyntax as rs
    minutes = rs.AutosaveInterval()
    if minutes>20: rs.AutosaveInterval(20)

##### See Also:

  * AutosaveFile
  * EnableAutosave

  

BuildDate

    
    
    BuildDate()

Returns the build date of Rhino

##### Returns:

    
    
    Datetime.date: the build date of Rhino. Will be converted to a string by most functions.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    build = rs.BuildDate()
    print("Rhino Build:{}".format(build)

  

ClearCommandHistory

    
    
    ClearCommandHistory()

Clears contents of Rhino's command history window. You can view the command
history window by using the CommandHistory command in Rhino.

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.ClearCommandHistory()

##### See Also:

  * CommandHistory

  

Command

    
    
    Command(commandString, echo=True)

Runs a Rhino command script. All Rhino commands can be used in command
scripts. The command can be a built-in Rhino command or one provided by a 3rd
party plug-in.

##### Parameters:

    
    
    commandString (str): A Rhino command including any arguments
    echo (bool, optional): The command echo mode True will display the commands on the commandline. If omitted, command prompts are echoed (True)

##### Returns:

    
    
    bool: True or False indicating success or failure
    
    Write command scripts just as you would type the command sequence at the
    command line. A space or a new line acts like pressing <Enter> at the
    command line. For more information, see "Scripting" in Rhino help.
    
    Note, this function is designed to run one command and one command only.
    Do not combine multiple Rhino commands into a single call to this method.
      WRONG:
        rs.Command("_Line _SelLast _Invert")
      CORRECT:
        rs.Command("_Line")
        rs.Command("_SelLast")
        rs.Command("_Invert")
    
    Also, the exclamation point and space character ( ! ) combination used by
    button macros and batch-driven scripts to cancel the previous command is
    not valid.
      WRONG:
        rs.Command("! _Line _Pause _Pause")
      CORRECT:
        rs.Command("_Line _Pause _Pause")
    After the command script has run, you can obtain the identifiers of most
    recently created or changed object by calling LastCreatedObjects.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Command("_Line 0,0,0 2,2,2")
    rs.Command("_Line _Pause _Pause")

##### See Also:

  * IsCommand
  * LastCommandName
  * LastCommandResult
  * LastCreatedObjects
  * Prompt

  

CommandHistory

    
    
    CommandHistory()

Returns the contents of Rhino's command history window

##### Returns:

    
    
    str: the contents of Rhino's command history window

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.CommandHistory())

##### See Also:

  * ClearCommandHistory

  

DefaultRenderer

    
    
    DefaultRenderer(renderer=None)

Returns or changes the default render plug-in

##### Parameters:

    
    
    renderer (str, optional): The name of the renderer to set as default renderer.  If omitted the Guid of the current renderer is returned.

##### Returns:

    
    
    guid: Unique identifier of default renderer

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.DefaultRenderer("MyRenderPlugIn")

##### See Also:

  * PlugIns

  

DeleteAlias

    
    
    DeleteAlias(alias)

Delete an existing alias from Rhino.

##### Parameters:

    
    
    alias (str): The name of an existing alias.

##### Returns:

    
    
    bool: True or False indicating success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.DeleteAlias("Hello"))

##### See Also:

  * AddAlias
  * AliasCount
  * AliasMacro
  * AliasNames
  * IsAlias

  

DeleteSearchPath

    
    
    DeleteSearchPath(folder)

Removes existing path from Rhino's search path list. Search path items can be
removed manually by using Rhino's options command and modifying the contents
of the files tab

##### Parameters:

    
    
    folder (str): A folder to remove

##### Returns:

    
    
    bool: True or False indicating success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.DeleteSearchPath("C:\\My RhinoScripts")

##### See Also:

  * AddSearchPath
  * SearchPathCount
  * SearchPathList

  

DisplayOleAlerts

    
    
    DisplayOleAlerts(enable)

Enables/disables OLE Server Busy/Not Responding dialog boxes

##### Parameters:

    
    
    enable (bool): Whether alerts should be visible (True or False)

##### Returns:

    
    
    none

##### Example:

    
    
    import System
    import rhinoscriptsyntax as rs
    rs.DisplayOleAlerts( False )
    t = System.Type.GetTypeFromProgID("Excel.Application")
    objExcel = System.Activator.CreateObject(t)
    ...

  

EdgeAnalysisColor

    
    
    EdgeAnalysisColor(color=None)

Returns or modifies edge analysis color displayed by the ShowEdges command

##### Parameters:

    
    
    color (tuple (r255,g255,b255), optional): The new color for the analysis.

##### Returns:

    
    
    tuple (r255,g255,b255): if color is not specified, the current edge analysis color
    tuple (r255,g255,b255): if color is specified, the previous edge analysis color

##### Example:

    
    
    import rhinoscriptsyntax as rs
    oldcolor = rs.EdgeAnalysisColor()
    newcolor = rs.GetColor(oldcolor)
    if newcolor is not None:
        rs.EdgeAnalysisColor(newcolor)

##### See Also:

  * EdgeAnalysisMode

  

EdgeAnalysisMode

    
    
    EdgeAnalysisMode(mode=None)

Returns or modifies edge analysis mode displayed by the ShowEdges command

##### Parameters:

    
    
    mode (number, optional): The new display mode. The available modes are
                 0 - display all edges
                 1 - display naked edges

##### Returns:

    
    
    number: if mode is not specified, the current edge analysis mode
    number: if mode is specified, the previous edge analysis mode

##### Example:

    
    
    import rhinoscriptsyntax as rs
    previous_mode = rs.EdgeAnalysisMode(1)

##### See Also:

  * EdgeAnalysisColor

  

EnableAutosave

    
    
    EnableAutosave(enable=True)

Enables or disables Rhino's automatic file saving mechanism

##### Parameters:

    
    
    enable (bool, optional): The autosave state. If omitted automatic saving is enabled (True)

##### Returns:

    
    
    bool: the previous autosave state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    prevstate = rs.EnableAutosave()

##### See Also:

  * AutosaveFile
  * AutosaveInterval

  

EnablePlugIn

    
    
    EnablePlugIn(plugin, enable=None)

Enables or disables a Rhino plug-in

##### Parameters:

    
    
    plugin (guid): The unique Guid id of the plugin.
    enable (bool, optional): Load silently if True. If omitted Load silently is False.

##### Returns:

    
    
    bool: True if set to load silently otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.EnablePlugIn("RhinoCrasher", False))

##### See Also:

  * IsPlugIn
  * PlugInId
  * PlugIns

  

ExeFolder

    
    
    ExeFolder()

Returns the full path to Rhino's executable folder.

##### Returns:

    
    
    str: the full path to Rhino's executable folder.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    folder = rs.ExeFolder()
    print(folder)

##### See Also:

  * InstallFolder

  

ExePlatform

    
    
    ExePlatform()

Returns the platform of the Rhino executable

##### Returns:

    
    
    str: the platform of the Rhino executable

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if rs.ExePlatform() == 1:
        print("You are using a 64-bit version of Rhino.")
    else:
        print("You are using a 32-bit version of Rhino.")

##### See Also:

  * BuildDate
  * ExeVersion
  * SdkVersion

  

ExeServiceRelease

    
    
    ExeServiceRelease()

Returns the service release number of the Rhino executable

##### Returns:

    
    
    str: the service release number of the Rhino executable

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("Build date:{}".format(rs.BuildDate())
    print("SDK Version:{}".format(rs.SdkVersion())
    print("SDK Service Release:{}".format(rs.SdkServiceRelease())
    print("Executable Version:{}".format(rs.ExeVersion())
    print("Executable Service Release:{}".format(rs.ExeServiceRelease())
    print("Serial Number:{}".format(rs.SerialNumber())
    print("Node Type:{}".format(rs.NodeType())
    print("Install Type:{}".format(rs.InstallType())

##### See Also:

  * BuildDate
  * ExeVersion
  * SdkVersion

  

ExeVersion

    
    
    ExeVersion()

Returns the major version number of the Rhino executable

##### Returns:

    
    
    str: the major version number of the Rhino executable

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("Build date:{}".format(rs.BuildDate()))
    print("SDK Version:{}".format(rs.SdkVersion()))
    print("SDK Service Release:{}".format(rs.SdkServiceRelease()))
    print("Executable Version:{}".format(rs.ExeVersion()))
    print("Executable Service Release:{}".format(rs.ExeServiceRelease()))
    print("Serial Number:{}".format(rs.SerialNumber()))
    print("Node Type:{}".format(rs.NodeType()))
    print("Install Type:{}".format(rs.InstallType()))

##### See Also:

  * BuildDate
  * ExeServiceRelease
  * SdkVersion

  

Exit

    
    
    Exit()

Closes the rhino application

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Exit()

  

FindFile

    
    
    FindFile(filename)

Searches for a file using Rhino's search path. Rhino will look for a file in
the following locations: 1\. The current document's folder. 2\. Folder's
specified in Options dialog, File tab. 3\. Rhino's System folders

##### Parameters:

    
    
    filename (str): A short file name to search for

##### Returns:

    
    
    str: full path on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    path = rs.FindFile("Rhino.exe")
    print(path)

  

GetPlugInObject

    
    
    GetPlugInObject(plug_in)

Returns a scriptable object from a specified plug-in. Not all plug-ins contain
scriptable objects. Check with the manufacturer of your plug-in to see if they
support this capability.

##### Parameters:

    
    
    plug_in (str or guid): The name or Id of a registered plug-in that supports scripting.
                           If the plug-in is registered but not loaded, it will be loaded

##### Returns:

    
    
    guid: scriptable object if successful
    null: None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objPlugIn = rs.GetPlugInObject("SomePlugIn")
    if objPlugIn is not None:
        print(objPlugIn.About())

  

InCommand

    
    
    InCommand(ignore_runners=True)

Determines if Rhino is currently running a command. Because Rhino allows for
transparent commands (commands run from inside of other commands), this method
returns the total number of active commands.

##### Parameters:

    
    
    ignore_runners (bool, optional): If True, script running commands, such as
                                     LoadScript, RunScript, and ReadCommandFile will not counted.
                                     If omitted the default is not to count script running command (True).

##### Returns:

    
    
    number: the number of active commands

##### Example:

    
    
    import rhinoscriptsyntax as rs
    commands = rs.InCommand()
    if commands > 0:
        print("Rhino is running", commands, "command(s).")
    else:
        print("Rhino is not running any command(s).")

##### See Also:

  * Command
  * IsCommand

  

InstallFolder

    
    
    InstallFolder()

The full path to Rhino's installation folder

##### Returns:

    
    
    str: the full path to Rhino's installation folder

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.InstallFolder())

##### See Also:

  * ExeFolder

  

IsAlias

    
    
    IsAlias(alias)

Verifies that a command alias exists in Rhino

##### Parameters:

    
    
    alias (str): The name of an existing command alias

##### Returns:

    
    
    bool: True if exists or False if the alias does not exist.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.IsAlias("Hello"))

##### See Also:

  * AddAlias
  * AliasCount
  * AliasMacro
  * AliasNames
  * DeleteAlias

  

IsCommand

    
    
    IsCommand(command_name)

Verifies that a command exists in Rhino. Useful when scripting commands found
in 3rd party plug-ins.

##### Parameters:

    
    
    command_name (str): The command name to test

##### Returns:

    
    
    bool: True if the string is a command or False if it is not a command.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cmdname = rs.GetString("Command name to test")
    if cmdname is not None:
        iscmd = rs.IsCommand(cmdname)
        if iscmd:
            print("The", cmdname, "command exists.")
        else:
            print("The", cmdname, "command does not exist.")

##### See Also:

  * Command
  * InCommand

  

IsPlugIn

    
    
    IsPlugIn(plugin)

Verifies that a plug-in is registered

##### Parameters:

    
    
    plugin (guid): The unique id of the plug-in

##### Returns:

    
    
    bool: True if the Guid is registered or False if it is not.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plugin = rs.GetString("Plug-in name")
    if rs.IsPlugIn(plugin): print("The  plug-in is registered.")
    else: print("The  plug-in is not registered.")

##### See Also:

  * EnablePlugIn
  * PlugInId
  * PlugIns

  

IsRunningOnWindows

    
    
    IsRunningOnWindows()

Returns True if this script is being executed on a Windows platform

##### Returns:

    
    
    bool: True if currently running on the Widows platform. False if it is not Windows.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if rs.IsRunngingOnWindows():
        print("Running on Windows")
    else:
        print("Running on Mac")

  

LastCommandName

    
    
    LastCommandName()

Returns the name of the last executed command

##### Returns:

    
    
    str: the name of the last executed command

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Command( "Line" )
    print("The last command was the {} {}".format(rs.LastCommandName(), "command."))

##### See Also:

  * Command
  * IsCommand
  * LastCommandResult

  

LastCommandResult

    
    
    LastCommandResult()

Returns the result code for the last executed command

##### Returns:

    
    
    number: the result code for the last executed command.
              0 = success (command successfully completed)
              1 = cancel (command was cancelled by the user)
              2 = nothing (command did nothing, but was not cancelled)
              3 = failure (command failed due to bad input, computational problem...)
              4 = unknown command (the command was not found)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Command( "Line" )
    result = rs.LastCommandResult()
    if result==0:
        print("The command completed.")
    else:
        print("The command did not complete.")

##### See Also:

  * Command
  * IsCommand
  * LastCommandName

  

LocaleID

    
    
    LocaleID()

Returns the current language used for the Rhino interface. The current
language is returned as a locale ID, or LCID, value.

##### Returns:

    
    
    number: the current language used for the Rhino interface as a locale ID, or LCID.
              1029  Czech
              1031  German-Germany
              1033  English-United States
              1034  Spanish-Spain
              1036  French-France
              1040  Italian-Italy
              1041  Japanese
              1042  Korean
              1045  Polish

##### Example:

    
    
    import rhinoscriptsyntax as rs
    lcid = rs.LocaleID()
    if lcid==1029:
        print("message in Czech")
    elif lcid==1031:
        print("message in German")
    elif lcid==1033:
        print("message in English")
    elif lcid==1034:
        print("message in Spanish")
    elif lcid==1036:
        print("message in Italian")
    elif lcid==1040:
        print("message in Japanese")
    elif lcid==1042:
        print("message in Korean")
    elif lcid==1045:
        print("message in Polish")

  

Ortho

    
    
    Ortho(enable=None)

Enables or disables Rhino's ortho modeling aid.

##### Parameters:

    
    
    enable (bool, optional): The new enabled status (True or False). If omitted the current state is returned.

##### Returns:

    
    
    bool: if enable is not specified, then the current ortho status
    bool: if enable is specified, then the previous ortho status

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if not rs.Ortho(): rs.Ortho(True)

##### See Also:

  * Osnap
  * Planar
  * Snap

  

Osnap

    
    
    Osnap(enable=None)

Enables or disables Rhino's object snap modeling aid. Object snaps are tools
for specifying points on existing objects.

##### Parameters:

    
    
    enable (bool, optional): The new enabled status.

##### Returns:

    
    
    bool: if enable is not specified, then the current osnap status
    bool: if enable is specified, then the previous osnap status

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if not rs.Osnap(): rs.Osnap(True)

##### See Also:

  * Ortho
  * OsnapMode
  * Planar
  * Snap

  

OsnapDialog

    
    
    OsnapDialog(visible=None)

Shows or hides Rhino's dockable object snap bar

##### Parameters:

    
    
    visible (bool, optional): The new visibility state. If omitted then the current state is returned.

##### Returns:

    
    
    bool: if visible is not specified, then the current visible state
    bool: if visible is specified, then the previous visible state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if not rs.OsnapDialog(): rs.OsnapDialog(True)

##### See Also:

  * Osnap
  * OsnapMode
  * ProjectOsnaps

  

OsnapMode

    
    
    OsnapMode(mode=None)

Returns or sets the object snap mode. Object snaps are tools for specifying
points on existing objects

##### Parameters:

    
    
    mode (number, optional): The object snap mode or modes to set. Object snap modes
                   can be added together to set multiple modes
                   0          None
                   2          Near
                   8          Focus
                   32         Center
                   64         Vertex
                   128        Knot
                   512        Quadrant
                   2048       Midpoint
                   8192       Intersection
                   131072     End
                   524288     Perpendicular
                   2097152    Tangent
                   134217728  Point

##### Returns:

    
    
    number: if mode is not specified, then the current object snap mode(s)
    number: if mode is specified, then the previous object snap mode(s)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rhOsnapModeEnd = 131072
    #add 'End' mode while keeping the ones that are already set
    mode = rs.OsnapMode()
    rs.OsnapMode(mode + rhOsnapModeEnd)
    #add 'End' mode while clearing the others
    rs.OsnapMode(rhOsnapModeEnd)

##### See Also:

  * Osnap
  * OsnapDialog
  * ProjectOsnaps

  

Planar

    
    
    Planar(enable=None)

Enables or disables Rhino's planar modeling aid

##### Parameters:

    
    
    enable (bool, optional): The new enable status.  If omitted the current state is returned.

##### Returns:

    
    
    bool: if enable is not specified, then the current planar status
    bool: if enable is secified, then the previous planar status

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if not rs.Planar(): rs.Planar(True)

##### See Also:

  * Ortho
  * Osnap
  * Snap

  

PlugInId

    
    
    PlugInId(plugin)

Returns the identifier of a plug-in given the plug-in name

##### Parameters:

    
    
    plugin (guid): Unique id of the plug-in

##### Returns:

    
    
    guid: the id of the plug-in
    None: None if the plug-in isn't valid

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plugins = rs.PlugIns(0, 1)
    if plugins:
        for plugin in plugins: print(rs.PlugInId(plugin))

##### See Also:

  * EnablePlugIn
  * IsPlugIn
  * PlugIns

  

PlugIns

    
    
    PlugIns(types=0, status=0)

Returns a list of registered Rhino plug-ins

##### Parameters:

    
    
    types (number, optional): The type of plug-ins to return.
                              0=all
                              1=render
                              2=file export
                              4=file import
                              8=digitizer
                              16=utility.
                              If omitted, all are returned.
    status (number, optional): 0=both loaded and unloaded, 1=loaded, 2=unloaded.  If omitted both status is returned.

##### Returns:

    
    
    list of str: list of registered Rhino plug-ins

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plugins = rs.PlugIns(0, 1)
    for plugin in plugins: print(plugin)

  

ProjectOsnaps

    
    
    ProjectOsnaps(enable=None)

Enables or disables object snap projection

##### Parameters:

    
    
    enable (bool, optional): The new enabled status.  If omitted the current status is returned.

##### Returns:

    
    
    bool: the current object snap projection status

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if not rs.ProjectOsnaps(): rs.ProjectOsnaps(True)

##### See Also:

  * Osnap
  * OsnapDialog
  * OsnapMode

  

Prompt

    
    
    Prompt(message=None)

Change Rhino's command window prompt

##### Parameters:

    
    
    message (str, optional): The new prompt on the commandline.  If omitted the prompt will be blank.

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Prompt("Hello Rhino!")

##### See Also:

  * Command

  

ScreenSize

    
    
    ScreenSize()

Returns current width and height, of the screen of the primary monitor.

##### Returns:

    
    
    tuple (width, height): containing two numbers identifying the width and height in pixels

##### Example:

    
    
    import rhinoscriptsyntax as rs
    size = rs.ScreenSize()
    print("Screen Width: {} pixels".format(size[0]))
    print("Screen Height: {} pixels".format(size[1]))

  

SdkVersion

    
    
    SdkVersion()

Returns version of the Rhino SDK supported by the executing Rhino.

##### Returns:

    
    
    str: the version of the Rhino SDK supported by the executing Rhino. Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("Required SDK Version: {}".format(rs.SdkVersion()))

  

SearchPathCount

    
    
    SearchPathCount()

Returns the number of path items in Rhino's search path list. See "Options
Files settings" in the Rhino help file for more details.

##### Returns:

    
    
    number: the number of path items in Rhino's search path list

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.SearchPathCount()
    if count>0:
        paths = rs.SearchPathList()
        for path in paths: print(path)

##### See Also:

  * AddSearchPath
  * DeleteSearchPath
  * SearchPathList

  

SearchPathList

    
    
    SearchPathList()

Returns all of the path items in Rhino's search path list. See "Options Files
settings" in the Rhino help file for more details.

##### Returns:

    
    
    list of str: list of search paths

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.SearchPathCount()
    if count>0:
        paths = rs.SearchPathList()
        for path in paths: print(path)

##### See Also:

  * AddSearchPath
  * DeleteSearchPath
  * SearchPathCount

  

SendKeystrokes

    
    
    SendKeystrokes(keys=None, add_return=True)

Sends a string of printable characters to Rhino's command line

##### Parameters:

    
    
    keys (str, optional): A string of characters to send to the command line.
    add_return (bool, optional): Append a return character to the end of the string. If omitted an return character will be added (True)

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.SendKeystroke( "Hello Rhino!" )
    rs.SendKeystrokes( 25/4 )

##### See Also:

  * Command

  

Snap

    
    
    Snap(enable=None)

Enables or disables Rhino's grid snap modeling aid

##### Parameters:

    
    
    enable (bool, optional): The new enabled status. If omitted the current status is returned.

##### Returns:

    
    
    bool: the current grid snap status

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if not rs.Snap(): rs.Snap(True)

##### See Also:

  * Ortho
  * Osnap
  * Planar

  

StatusBarDistance

    
    
    StatusBarDistance(distance=0)

Sets Rhino's status bar distance pane

##### Parameters:

    
    
    distance (number, optional): The distance to set the status bar.  If omitted the distance will be set to 0.

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.StatusBarDistance(3.14159)

##### See Also:

  * StatusBarMessage
  * StatusBarPoint

  

StatusBarMessage

    
    
    StatusBarMessage(message=None)

Sets Rhino's status bar message pane

##### Parameters:

    
    
    message (str, optional): The message to display.

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.StatusBarMessage("Hello Rhino!")

##### See Also:

  * StatusBarDistance
  * StatusBarPoint

  

StatusBarPoint

    
    
    StatusBarPoint(point=None)

Sets Rhino's status bar point coordinate pane

##### Parameters:

    
    
    point (point3d, optional): The 3d coordinates of the status bar.  If omitted the current poition is set to (0,0,0).

##### Returns:

    
    
    none

##### Example:

    
    
    import rhinoscriptsyntax as rs
    pt = (1.1, 2.2, 3.3)
    rs.StatusBarPoint(pt)

##### See Also:

  * StatusBarDistance
  * StatusBarMessage

  

StatusBarProgressMeterShow

    
    
    StatusBarProgressMeterShow(label, lower, upper, embed_label=True, show_percent=True)

Start the Rhino status bar progress meter

##### Parameters:

    
    
    label (str): Short description of the progesss
    lower (str): Lower limit of the progress meter's range
    upper (str): Upper limit of the progress meter's range
    embed_label (bool, optional): If True, the label will show inside the meter.
                                  If false, the label will show to the left of the meter.
                                  If omitted the label will show inside the meter (True)
    show_percent (bool): Show the percent complete if True. If omitted the percnetage will be shown (True)

##### Returns:

    
    
    bool: True or False indicating success or failure

  

StatusBarProgressMeterUpdate

    
    
    StatusBarProgressMeterUpdate(position, absolute=True)

Set the current position of the progress meter

##### Parameters:

    
    
    position (number): The new position in the progress meter
    absolute (bool, optional): The position is set absolute (True) or relative (False) to its current position. If omitted the absolute (True) is used.

##### Returns:

    
    
    number: previous position setting.

  

StatusBarProgressMeterHide

    
    
    StatusBarProgressMeterHide()

Hide the progress meter

##### Returns:

    
    
    none

  

TemplateFile

    
    
    TemplateFile(filename=None)

Returns or sets Rhino's default template file. This is the file used when
Rhino starts.

##### Parameters:

    
    
    filename (str, optional): The name of the new default template file. If omitted the current default template name is returned.

##### Returns:

    
    
    str: if filename is not specified, then the current default template file
    str: if filename is specified, then the previous default template file

##### Example:

    
    
    import rhinoscriptsyntax as rs
    folder = rs.TemplateFolder()
    filename = folder + "\\Millimeters.3dm"
    rs.TemplateFile(filename)

##### See Also:

  * TemplateFolder

  

TemplateFolder

    
    
    TemplateFolder(folder=None)

Returns or sets the location of Rhino's template folder

##### Parameters:

    
    
    folder (str, optional): The location of Rhino's template files. Note, the location must exist.

##### Returns:

    
    
    str: if folder is not specified, then the current template file folder
    str: if folder is specified, then the previous template file folder

##### Example:

    
    
    import rhinoscriptsyntax as rs
    folder = rs.TemplateFolder()
    filename = folder + "\\Millimeters.3dm"
    rs.TemplateFile(filename)

##### See Also:

  * TemplateFile

  

WindowHandle

    
    
    WindowHandle()

Returns the windows handle of Rhino's main window

##### Returns:

    
    
    IntPt: the Window's handle of Rhino's main window. IntPtr is a platform-specific type that is used to represent a pointer or a handle.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    handle = rs.WindowHandle()
    print(handle)

  

WorkingFolder

    
    
    WorkingFolder(folder=None)

Returns or sets Rhino's working folder (directory). The working folder is the
default folder for all file operations.

##### Parameters:

    
    
    folder (str, optional): The new working folder for the current Rhino session.

##### Returns:

    
    
    str: if folder is not specified, then the current working folder
    str: if folder is specified, then the previous working folder

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    folder = rs.WorkingFolder()
    folder = rs.BrowseForFolder(folder,  "Directory", "Select Directory")
    if folder is not None:
        rs.WorkingFolder(folder)

##### See Also:

  * BrowseForFolder

  

## block

AddBlock

    
    
    AddBlock(object_ids, base_point, name=None, delete_input=False)

Adds a new block definition to the document

##### Parameters:

    
    
    object_ids ([guid, ....]) objects that will be included in the block
    base_point (point): 3D base point for the block definition
    name (str, optional): name of the block definition. If omitted a name will be
      automatically generated
    delete_input (bool): if True, the object_ids will be deleted

##### Returns:

    
    
    str: name of new block definition on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to define block")
    if objs:
        point = rs.GetPoint("Block base point")
        if point:
            block = rs.AddBlock(objs, point, None, True)
            rs.InsertBlock(block, point)

##### See Also:

  * InsertBlock

  

BlockContainerCount

    
    
    BlockContainerCount(block_name)

Returns number of block definitions that contain a specified block definition

##### Parameters:

    
    
    block_name (str): the name of an existing block definition

##### Returns:

    
    
    number: the number of block definitions that contain a specified block definition

##### Example:

    
    
    import rhinoscriptscriptsyntax as rs
    block = rs.GetString("Block name to query")
    if rs.IsBlock(block):
        count = rs.BlockContainerCount(block)
        print("This block is nested in {} block(s).".format(count))

##### See Also:

  * BlockContainers
  * IsBlock

  

BlockContainers

    
    
    BlockContainers(block_name)

Returns names of the block definitions that contain a specified block
definition.

##### Parameters:

    
    
    block_name (str): the name of an existing block definition

##### Returns:

    
    
    list(str, ...): A list of block definition names

##### Example:

    
    
    import rhinoscriptsyntax as rs
    blockname = rs.GetString("Block name to query")
    if rs.IsBlock(blockname):
        blocks = rs.BlockContainers(blockname)
        for block in blocks: print(block)

##### See Also:

  * BlockContainerCount
  * IsBlock

  

BlockCount

    
    
    BlockCount()

Returns the number of block definitions in the document

##### Returns:

    
    
    number: the number of block definitions in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.BlockCount()
    print("There are {} blocks".format(count)

##### See Also:

  * BlockNames
  * IsBlock

  

BlockDescription

    
    
    BlockDescription(block_name, description=None)

Returns or sets the description of a block definition

##### Parameters:

    
    
    block_name (str): the name of an existing block definition
    description (str, optional): The new description.

##### Returns:

    
    
    str: if description is not specified, the current description
    str: if description is specified, the previous description

##### Example:

    
    
    import rhinoscriptsyntax as rs
    blockname = rs.GetString("Block name to list description")
    if rs.IsBlock(blockname):
        desc = rs.BlockDescription(blockname)
        if desc is None: print("No description")
        else: print(desc)

##### See Also:

  * IsBlock

  

BlockInstanceCount

    
    
    BlockInstanceCount(block_name,where_to_look=0)

Counts number of instances of the block in the document. Nested instances are
not included in the count.

##### Parameters:

    
    
    block_name (str): the name of an existing block definition
    where_to_look (number, optional):
      0 = get top level references in active document.
      1 = get top level and nested references in active document.
      2 = check for references from other instance definitions

##### Returns:

    
    
    number: the number of instances of the block in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    blockname = rs.GetString("Block to count")
    if rs.IsBlock(blockname):
        count = rs.BlockInstanceCount(blockname)
        print("{} block(s) found.".format(count))

##### See Also:

  * BlockInstanceInsertPoint
  * BlockInstances
  * BlockInstanceXform
  * IsBlockInstance

  

BlockInstanceInsertPoint

    
    
    BlockInstanceInsertPoint(object_id)

Returns the insertion point of a block instance.

##### Parameters:

    
    
    object_id (guid): The identifier of an existing block insertion object

##### Returns:

    
    
    point: The insertion 3D point if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strObject = rs.GetObject("Select block")
    if rs.IsBlockInstance(strObject):
        rs.AddPoint( rs.BlockInstanceInsertPoint(strObject) )

##### See Also:

  * BlockInstanceCount
  * BlockInstances
  * BlockInstanceXform
  * IsBlockInstance

  

BlockInstanceName

    
    
    BlockInstanceName(object_id)

Returns the block name of a block instance

##### Parameters:

    
    
    object_id (guid): The identifier of an existing block insertion object

##### Returns:

    
    
    str: the block name of a block instance

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strObject = rs.GetObject("Select block")
    if rs.IsBlockInstance(strObject):
        print(rs.BlockInstanceName(strObject))

##### See Also:

  * BlockInstanceCount
  * BlockInstances
  * BlockInstanceXform
  * IsBlockInstance

  

BlockInstances

    
    
    BlockInstances(block_name,where_to_look=0)

Returns the identifiers of the inserted instances of a block.

##### Parameters:

    
    
    block_name (str): the name of an existing block definition
    where_to_look (number, optional):
      0 = get top level references in active document.
      1 = get top level and nested references in active document.
      2 = check for references from other instance definitions

##### Returns:

    
    
    list(guid, ...): Ids identifying the instances of a block in the model.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block to select")
    if rs.IsBlock(strBlock):
        arrObjects = rs.BlockInstances(strBlock)
        if arrobjects:
            rs.SelectObjects(arrObjects)

##### See Also:

  * BlockInstanceCount
  * BlockInstanceInsertPoint
  * BlockInstanceXform
  * IsBlockInstance

  

BlockInstanceXform

    
    
    BlockInstanceXform(object_id)

Returns the location of a block instance relative to the world coordinate
system origin (0,0,0). The position is returned as a 4x4 transformation matrix

##### Parameters:

    
    
    object_id (guid): The identifier of an existing block insertion object

##### Returns:

    
    
    transform: the location, as a transform matrix, of a block instance relative to the world coordinate
    system origin

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select block to query")
    if rs.IsBlockInstance(obj):
        arrMatrix = rs.BlockInstanceXform(obj)
        if arrMatrix is not None:
            pointId = rs.AddPoint([0,0,0])
            rs.TransformObject( pointId, arrMatrix)

##### See Also:

  * BlockInstanceCount
  * BlockInstanceInsertPoint
  * BlockInstances
  * IsBlockInstance

  

BlockNames

    
    
    BlockNames( sort=False )

Returns the names of all block definitions in the document

##### Parameters:

    
    
    sort (bool): True to return a sorted list

##### Returns:

    
    
    list(str, ...): the names of all block definitions in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.BlockNames(True)
    if names:
        for name in names: print(name)

##### See Also:

  * BlockCount
  * IsBlock

  

BlockObjectCount

    
    
    BlockObjectCount(block_name)

Returns number of objects that make up a block definition

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    number: the number of objects that make up a block definition

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.BlockObjectCount()
    print("There are {} blocks".format(count))

##### See Also:

  * BlockNames
  * BlockObjects
  * IsBlock

  

BlockObjects

    
    
    BlockObjects(block_name)

Returns identifiers of the objects that make up a block definition

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    list(guid, ...): list of identifiers on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name to list identifiers")
    if rs.IsBlock(strBlock):
        objects = rs.BlockObjects(strBlock)
        if objects:
            for item in objects: print(item)

##### See Also:

  * BlockNames
  * BlockObjectCount
  * IsBlock

  

BlockPath

    
    
    BlockPath(block_name)

Returns path to the source of a linked or embedded block definition. A linked
or embedded block definition is a block definition that was inserted from an
external file.

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    str: path to the linked block on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name to list path")
    if rs.IsBlockEmbedded(strBlock):
        print(rs.BlockPath(strBlock))

##### See Also:

  * IsBlock
  * IsBlockEmbedded

  

BlockStatus

    
    
    BlockStatus(block_name)

Returns the status of a linked block

##### Parameters:

    
    
    block_name (str): Name of an existing block

##### Returns:

    
    
    number: the status of a linked block
      Value Description
      -3    Not a linked block definition.
      -2    The linked block definition's file could not be opened or could not be read.
      -1    The linked block definition's file could not be found.
       0    The linked block definition is up-to-date.
       1    The linked block definition's file is newer than definition.
       2    The linked block definition's file is older than definition.
       3    The linked block definition's file is different than definition.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    block = rs.GetString("Block name to list description")
    if rs.IsBlock(block):
        status = rs.BlockStatus(block)
        print("block status for {} is {}".format(block, status))

##### See Also:

  * IsBlock

  

DeleteBlock

    
    
    DeleteBlock(block_name)

Deletes a block definition and all of it's inserted instances.

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name to delete")
    if rs.IsBlock(strBlock):
        rs.DeleteBlock(strBlock)

##### See Also:

  * BlockNames
  * ExplodeBlockInstance
  * IsBlock

  

ExplodeBlockInstance

    
    
    ExplodeBlockInstance(object_id, explode_nested_instances=False)

Explodes a block instance into it's geometric components. The exploded objects
are added to the document

##### Parameters:

    
    
    object_id (guid): The identifier of an existing block insertion object
    explode_nested_instances (bool, optional): By default nested blocks are not exploded.

##### Returns:

    
    
    list(guid, ...): identifiers for the newly exploded objects on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strObject = rs.GetObject("Select block instance to explode")
    if rs.IsBlockInstance(strObject):
        rs.ExplodeBlockInstance(strObject)

##### See Also:

  * DeleteBlock
  * IsBlockInstance

  

InsertBlock

    
    
    InsertBlock( block_name, insertion_point, scale=(1,1,1), angle_degrees=0, rotation_normal=(0,0,1) )

Inserts a block whose definition already exists in the document

##### Parameters:

    
    
    block_name (str): name of an existing block definition
    insertion_point (point): insertion point for the block
    scale ({number, number, number]): x,y,z scale factors
    angle_degrees (number, optional): rotation angle in degrees
    rotation_normal (vector, optional): the axis of rotation.

##### Returns:

    
    
    guid: id for the block that was added to the doc

  

InsertBlock2

    
    
    InsertBlock2(block_name, xform)

Inserts a block whose definition already exists in the document

##### Parameters:

    
    
    block_name (str): name of an existing block definition
    xform (transform): 4x4 transformation matrix to apply

##### Returns:

    
    
    guid: id for the block that was added to the doc on success

  

IsBlock

    
    
    IsBlock(block_name)

Verifies the existence of a block definition in the document.

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name")
    if rs.IsBlock(strBlock):
        print("The block definition exists.")
    else:
        print("The block definition does not exist.")

##### See Also:

  * IsBlockEmbedded
  * IsBlockInstance
  * IsBlockInUse
  * IsBlockReference

  

IsBlockEmbedded

    
    
    IsBlockEmbedded(block_name)

Verifies a block definition is embedded, or linked, from an external file.

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name")
    if rs.IsBlock(strBlock):
        if rs.IsBlockEmbedded(strBlock):
            print("The block definition is embedded.")
        else:
            print("The block definition is not embedded.")
    else:
        print("The block definition does not exist.")

##### See Also:

  * IsBlock
  * IsBlockInstance
  * IsBlockInUse
  * IsBlockReference

  

IsBlockInstance

    
    
    IsBlockInstance(object_id)

Verifies an object is a block instance

##### Parameters:

    
    
    object_id (guid): The identifier of an existing block insertion object

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select block instance")
    if rs.IsBlockInstance(obj):
        print("The object is a block instance.")
    else:
        print("The object is not a block instance.")

##### See Also:

  * IsBlock
  * IsBlockEmbedded
  * IsBlockInUse
  * IsBlockReference

  

IsBlockInUse

    
    
    IsBlockInUse(block_name, where_to_look=0)

Verifies that a block definition is being used by an inserted instance

##### Parameters:

    
    
    block_name (str): name of an existing block definition
    where_to_look (number, optional): One of the following values
         0 = Check for top level references in active document
         1 = Check for top level and nested references in active document
         2 = Check for references in other instance definitions

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name")
    if rs.IsBlock(strBlock):
        if rs.IsBlockInUse(strBlock):
            print("The block definition is in use.")
        else:
            print("The block definition is not in use.")
    else:
        print("The block definition does not exist.")

##### See Also:

  * IsBlock
  * IsBlockInstance
  * IsBlockEmbedded
  * IsBlockReference

  

IsBlockReference

    
    
    IsBlockReference(block_name)

Verifies that a block definition is from a reference file.

##### Parameters:

    
    
    block_name (str): name of an existing block definition

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strBlock = rs.GetString("Block name")
    if rs.IsBlock(strBlock):
        if rs.IsBlockReference(strBlock):
            print("The block definition is a reference definition.")
        else:
            print("The block definition is not a reference definition.")
    else:
        print("The block definition does not exist.")

##### See Also:

  * IsBlock
  * IsBlockEmbedded
  * IsBlockInUse
  * IsBlockInstance

  

RenameBlock

    
    
    RenameBlock( block_name, new_name )

Renames an existing block definition

##### Parameters:

    
    
    block_name (str): name of an existing block definition
    new_name (str): name to change to

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strOldBlock = rs.GetString("Old block name")
    if strOldBlock:
        strNewBlock = rs.GetString("New block name")
        if strNewBlock:
            rs.RenameBlock (strOldBlock, strNewBlock)

##### See Also:

  * BlockNames
  * IsBlock

  

## curve

AddArc

    
    
    AddArc(plane, radius, angle_degrees)

Adds an arc curve to the document

##### Parameters:

    
    
    plane (str): plane on which the arc will lie. The origin of the plane will be
      the center point of the arc. x-axis of the plane defines the 0 angle
      direction.
    radius(number): radius of the arc
    angle_degrees (number): interval of arc in degrees

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    plane = rs.WorldXYPlane()
    plane = rs.RotatePlane(plane,  45.0, [0,0,1])
    rs.AddArc( plane, 5.0, 45.0  )

##### See Also:

  * AddArc3Pt
  * ArcAngle
  * ArcCenterPoint
  * ArcMidPoint
  * ArcRadius
  * IsArc

  

AddArc3Pt

    
    
    AddArc3Pt(start, end, point_on_arc)

Adds a 3-point arc curve to the document

##### Parameters:

    
    
    start, end (point|guid): endpoints of the arc
    point_on_arc (point|guid): a point on the arc

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    start = rs.GetPoint("Start of arc")
    if start is not None:
        end = rs.GetPoint("End of arc")
        if end is not None:
            pton = rs.GetPoint("Point on arc")
            if pton is not None:
                rs.AddArc3Pt(start, end, pton)

##### See Also:

  * AddArc
  * ArcAngle
  * ArcCenterPoint
  * ArcMidPoint
  * ArcRadius
  * IsArc

  

AddArcPtTanPt

    
    
    AddArcPtTanPt(start, direction, end)

Adds an arc curve, created from a start point, a start direction, and an end
point, to the document

##### Parameters:

    
    
    start (point): the starting point of the arc
    direction (vector): the arc direction at start
    end (point): the ending point of the arc

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    pick = rs.GetCurveObject("Select curve to extend")
    point = rs.GetPoint("End of extension")
    domain = rs.CurveDomain(pick[0])
    if abs(pick[4]-domain[0]) < abs(pick[4]-domain[1]):
        origin = rs.CurveStartPoint(pick[0])
        tangent = rs.VectorReverse(rs.CurveTangent(pick[0], domain[0]))
    else:
        origin = rs.CurveEndPoint(pick[0])
        tangent = rs.CurveTangent(pick[0], domain[1])
    rs.AddArcPtTanPt(origin, tangent, point)

##### See Also:

  * AddArc
  * AddArc3Pt
  * IsArc

  

AddBlendCurve

    
    
    AddBlendCurve(curves, parameters, reverses, continuities)

Makes a curve blend between two curves

##### Parameters:

    
    
    curves ([guid|curve, guid|curve]): list of two curves
    parameters ([number, number]): list of two curve parameters defining the blend end points
    reverses ([bool, bool]): list of two boolean values specifying to use the natural or opposite direction of the curve
    continuities ([number, number]): list of two numbers specifying continuity at end points
                                          0 = position
                                          1 = tangency
                                          2 = curvature

##### Returns:

    
    
    guid: identifier of new curve on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve0 = rs.AddLine((0,0,0), (0,9,0))
    curve1 = rs.AddLine((1,10,0), (10,10,0))
    curves = curve0, curve1
    domain_crv0 = rs.CurveDomain(curve0)
    domain_crv1 = rs.CurveDomain(curve1)
    params = domain_crv0[1], domain_crv1[0]
    revs = False, True
    cont = 2,2
    rs.AddBlendCurve( curves, params, revs, cont )

##### See Also:

  * AddFilletCurve

  

AddCircle

    
    
    AddCircle(plane_or_center, radius)

Adds a circle curve to the document

##### Parameters:

    
    
    plane_or_center (point|plane): plane on which the circle will lie. If a point is
      passed, this will be the center of the circle on the active
      construction plane
    radius (number): the radius of the circle

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.WorldXYPlane()
    rs.AddCircle( plane, 5.0 )

##### See Also:

  * AddCircle3Pt
  * CircleCenterPoint
  * CircleCircumference
  * CircleRadius
  * IsCircle

  

AddCircle3Pt

    
    
    AddCircle3Pt(first, second, third)

Adds a 3-point circle curve to the document

##### Parameters:

    
    
    first, second, third (point|guid): points on the circle

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = rs.GetPoint("First point on circle")
    if point1:
        point2 = rs.GetPoint("Second point on circle")
        if point2:
            point3 = rs.GetPoint("Third point on circle")
            if point3:
                rs.AddCircle3Pt(point1, point2, point3)

##### See Also:

  * AddCircle
  * CircleCenterPoint
  * CircleCircumference
  * CircleRadius
  * IsCircle

  

AddCurve

    
    
    AddCurve(points, degree=3)

Adds a control points curve object to the document

##### Parameters:

    
    
    points ([point|guid, ...]) a list of points
    degree (number): degree of the curve

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(True, message1="Pick curve point")
    if points: rs.AddCurve(points)

##### See Also:

  * AddInterpCurve
  * IsCurve

  

AddEllipse

    
    
    AddEllipse(plane, radiusX, radiusY)

Adds an elliptical curve to the document

##### Parameters:

    
    
    plane (plane) the plane on which the ellipse will lie. The origin of
            the plane will be the center of the ellipse
    radiusX, radiusY (number): radius in the X and Y axis directions

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.WorldXYPlane()
    rs.AddEllipse( plane, 5.0, 10.0 )

##### See Also:

  * AddEllipse3Pt
  * IsEllipse
  * EllipseCenterPoint
  * EllipseQuadPoints

  

AddEllipse3Pt

    
    
    AddEllipse3Pt(center, second, third)

Adds a 3-point elliptical curve to the document

##### Parameters:

    
    
    center (point|guid): center point of the ellipse
    second (point|guid): end point of the x axis
    third  (point|guid): end point of the y axis

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    center = (0,0,0)
    second = (5,0,0)
    third = (0,10,0)
    rs.AddEllipse3Pt( center, second, third )

##### See Also:

  * AddEllipse
  * IsEllipse
  * EllipseCenterPoint
  * EllipseQuadPoints

  

AddFilletCurve

    
    
    AddFilletCurve(curve0id, curve1id, radius=1.0, base_point0=None, base_point1=None)

Adds a fillet curve between two curve objects

##### Parameters:

    
    
    curve0id (guid): identifier of the first curve object
    curve1id (guid): identifier of the second curve object
    radius (number, optional): fillet radius
    base_point0 (point|guid, optional): base point of the first curve. If omitted,
                        starting point of the curve is used
    base_point1 (point|guid, optional): base point of the second curve. If omitted,
                        starting point of the curve is used

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve0 = rs.AddLine([0,0,0], [5,1,0])
    curve1 = rs.AddLine([0,0,0], [1,5,0])
    rs.AddFilletCurve( curve0, curve1 )

##### See Also:

  * CurveFilletPoints

  

AddInterpCrvOnSrf

    
    
    AddInterpCrvOnSrf(surface_id, points)

Adds an interpolated curve object that lies on a specified surface. Note, this
function will not create periodic curves, but it will create closed curves.

##### Parameters:

    
    
    surface_id (guid): identifier of the surface to create the curve on
    points ([point|guid, point|guid, ...])list of 3D points that lie on the specified surface.
             The list must contain at least 2 points

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface_id = rs.GetObject("Select surface to draw curve on", rs.filter.surface)
    if surface_id:
        point1 = rs.GetPointOnSurface( surface_id, "First point on surface")
        if point1:
            point2 = rs.GetPointOnSurface( surface_id, "Second point on surface")
            if point2:
                rs.AddInterpCrvOnSrf( surface_id, [point1, point2])

##### See Also:

  * AddCurve
  * AddInterpCurve
  * AddInterpCrvOnSrfUV

  

AddInterpCrvOnSrfUV

    
    
    AddInterpCrvOnSrfUV(surface_id, points)

Adds an interpolated curve object based on surface parameters, that lies on a
specified surface. Note, this function will not create periodic curves, but it
will create closed curves.

##### Parameters:

    
    
    surface_id (guid): identifier of the surface to create the curve on
    points ([[number, number}, [number,number], ...]): a list of 2D surface parameters. The list must contain
                                                       at least 2 sets of parameters

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface_id = rs.GetObject("Select surface to draw curve on", rs.filter.surface)
    if surface_id:
        domainU = rs.SurfaceDomain( surface_id, 0)
        u0 = domainU[0]/2
        u1 = domainU[1]/2
        domainV = rs.SurfaceDomain( surface_id, 1)
        v0 = domainV[0]/2
        v1 = domainV[1]/2
        rs.AddInterpCrvOnSrfUV( surface_id, [[u0,v0],[u1,v1]])

##### See Also:

  * AddCurve
  * AddInterpCurve
  * AddInterpCrvOnSrf

  

AddInterpCurve

    
    
    AddInterpCurve(points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None)

Adds an interpolated curve object to the document. Options exist to make a
periodic curve or to specify the tangent at the endpoints. The resulting curve
is a non-rational NURBS curve of the specified degree.

##### Parameters:

    
    
    points (point|guid, point|guid, ...]): a list containing 3D points to interpolate. For periodic curves,
        if the final point is a duplicate of the initial point, it is
        ignored. The number of control points must be >= (degree+1).
    degree (number, optional): The degree of the curve (must be >=1).
        Periodic curves must have a degree >= 2. For knotstyle = 1 or 2,
        the degree must be 3. For knotstyle = 4 or 5, the degree must be odd
    knotstyle(opt):
        0 Uniform knots.  Parameter spacing between consecutive knots is 1.0.
        1 Chord length spacing.  Requires degree = 3 with arrCV1 and arrCVn1 specified.
        2 Sqrt (chord length).  Requires degree = 3 with arrCV1 and arrCVn1 specified.
        3 Periodic with uniform spacing.
        4 Periodic with chord length spacing.  Requires an odd degree value.
        5 Periodic with sqrt (chord length) spacing.  Requires an odd degree value.
    start_tangent (vector, optional): a vector that specifies a tangency condition at the
        beginning of the curve. If the curve is periodic, this argument must be omitted.
    end_tangent (vector, optional): 3d vector that specifies a tangency condition at the
        end of the curve. If the curve is periodic, this argument must be omitted.

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = (0,0,0), (1,1,0), (2,0,0), (3,1,0), (4,0,0), (5,1,0)
    rs.AddInterpCurve(points)

##### See Also:

  * AddCurve
  * CurvePointCount
  * IsCurve

  

AddLine

    
    
    AddLine(start, end)

Adds a line curve to the current model.

##### Parameters:

    
    
    start, end (point|guid) end points of the line

##### Returns:

    
    
    guid: id of the new curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    start = rs.GetPoint("Start of line")
    if start:
        end = rs.GetPoint("End of line")
        if end: rs.AddLine(start, end)

##### See Also:

  * CurveEndPoint
  * CurveStartPoint
  * IsLine

  

AddNurbsCurve

    
    
    AddNurbsCurve(points, knots, degree, weights=None)

Adds a NURBS curve object to the document

##### Parameters:

    
    
    points ([guid|point, guid|point, ...]): a list containing 3D control points
    knots ([number, number, ...]): Knot values for the curve. The number of elements in knots must
        equal the number of elements in points plus degree minus 1
    degree (number): degree of the curve. must be greater than of equal to 1
    weights([number, number, ...], optional) weight values for the curve. Number of elements should
        equal the number of elements in points. Values must be greater than 0

##### Returns:

    
    
    guid: the identifier of the new object if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve_id = rs.GetObject("Pick a curve", rs.filter.curve)
    if curve_id:
        points = rs.CurvePoints(curve_id)
        knots = rs.CurveKnots(curve_id)
        degree = rs.CurveDegree(curve_id)
        newcurve = rs.AddNurbsCurve( points, knots, degree)
        if newcurve: rs.SelectObject(newcurve)

##### See Also:

  * CurveDegree
  * CurveKnots
  * CurvePoints

  

AddPolyline

    
    
    AddPolyline(points, replace_id=None)

Adds a polyline curve to the current model

##### Parameters:

    
    
    points ([guid|point, guid|point, ...]): list of 3D points. Duplicate, consecutive points will be
             removed. The list must contain at least two points. If the
             list contains less than four points, then the first point and
             last point must be different.
    replace_id (guid, optional): If set to the id of an existing object, the object
             will be replaced by this polyline

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(True)
    if points: rs.AddPolyline(points)

##### See Also:

  * IsPolyline

  

AddRectangle

    
    
    AddRectangle(plane, width, height)

Add a rectangular curve to the document

##### Parameters:

    
    
    plane (plane) plane on which the rectangle will lie
    width, height (number): width and height of rectangle as measured along the plane's
      x and y axes

##### Returns:

    
    
    guid: id of new rectangle

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.WorldXYPlane()
    plane = rs.RotatePlane(plane, 45.0, [0,0,1])
    rs.AddRectangle( plane, 5.0, 15.0 )

  

AddSpiral

    
    
    AddSpiral(point0, point1, pitch, turns, radius0, radius1=None)

Adds a spiral or helical curve to the document

##### Parameters:

    
    
    point0 (point|guid): helix axis start point or center of spiral
    point1 (point|guid): helix axis end point or point normal on spiral plane
    pitch (number): distance between turns. If 0, then a spiral. If > 0 then the
            distance between helix "threads"
    turns (number): number of turns
    radius0 (number): starting radius of spiral
    radius1 (number, optional): ending radius of spiral. If omitted, the starting radius is used for the complete spiral.

##### Returns:

    
    
    guid: id of new curve on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point0 = (0,0,0)
    point1 = (0,0,10)
    pitch = 1
    turns = 10
    radius0 = 5.0
    radius1 = 8.0
    rs.AddSpiral(point0, point1, pitch, turns, radius0, radius1)

  

AddSubCrv

    
    
    AddSubCrv(curve_id, param0, param1)

Add a curve object based on a portion, or interval of an existing curve
object. Similar in operation to Rhino's SubCrv command

##### Parameters:

    
    
    curve_id (guid): identifier of a closed planar curve object
    param0, param1 (number): first and second parameters on the source curve

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    getresult = rs.GetCurveObject()
    if getresult:
        curve_id = getresult[0]
        point0 = rs.GetPointOnCurve( curve_id )
        if point0:
            point1 = rs.GetPointOnCurve( curve_id )
            if point1:
                t0 = rs.CurveClosestPoint( curve_id, point0)
                t1 = rs.CurveClosestPoint( curve_id, point1)
                rs.AddSubCrv( curve_id, t0, t1 )

##### See Also:

  * CurveClosestPoint
  * GetCurveObject
  * GetPointOnCurve

  

ArcAngle

    
    
    ArcAngle(curve_id, segment_index=-1)

Returns the angle of an arc curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): identifies the curve segment if
    curve_id (guid): identifies a polycurve

##### Returns:

    
    
    number: The angle in degrees if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select arc")
    if rs.IsArc(id):
        angle = rs.ArcAngle(id)
        print("Arc angle: {}".format(angle))

##### See Also:

  * AddArc3Pt
  * ArcCenterPoint
  * ArcMidPoint
  * ArcRadius
  * IsArc

  

ArcCenterPoint

    
    
    ArcCenterPoint(curve_id, segment_index=-1)

Returns the center point of an arc curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    point: The 3D center point of the arc if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select arc")
    if rs.IsArc(id):
    point = rs.ArcCenterPoint(id)
    rs.AddPoint(point)

##### See Also:

  * AddArc3Pt
  * ArcAngle
  * ArcMidPoint
  * ArcRadius
  * IsArc

  

ArcMidPoint

    
    
    ArcMidPoint(curve_id, segment_index=-1)

Returns the mid point of an arc curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    point: The 3D mid point of the arc if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select arc")
    if rs.IsArc(id):
        point = rs.ArcMidPoint(id)
        rs.AddPoint(point)

##### See Also:

  * AddArc3Pt
  * ArcAngle
  * ArcCenterPoint
  * ArcRadius
  * IsArc

  

ArcRadius

    
    
    ArcRadius(curve_id, segment_index=-1)

Returns the radius of an arc curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    number: The radius of the arc if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select arc")
    if rs.IsArc(id):
        radius = rs.ArcRadius(id)
        print("Arc radius: {}".format(radius))

##### See Also:

  * AddArc3Pt
  * ArcAngle
  * ArcCenterPoint
  * ArcMidPoint
  * IsArc

  

CircleCenterPoint

    
    
    CircleCenterPoint(curve_id, segment_index=-1, return_plane=False)

Returns the center point of a circle curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve
    return_plane (bool, optional): if True, the circle's plane is returned. If omitted the plane is not returned.

##### Returns:

    
    
    point: The 3D center point of the circle if successful.
    plane: The plane of the circle if return_plane is True

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select circle")
    if rs.IsCircle(id):
        point = rs.CircleCenterPoint(id)
        rs.AddPoint( point )

##### See Also:

  * AddCircle
  * AddCircle3Pt
  * CircleCircumference
  * CircleRadius
  * IsCircle

  

CircleCircumference

    
    
    CircleCircumference(curve_id, segment_index=-1)

Returns the circumference of a circle curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    number: The circumference of the circle if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select circle")
    if rs.IsCircle(id):
        circumference = rs.CircleCircumference(id)
        print("Circle circumference: {}".format(circumference))

##### See Also:

  * AddCircle
  * AddCircle3Pt
  * CircleCenterPoint
  * CircleRadius
  * IsCircle

  

CircleRadius

    
    
    CircleRadius(curve_id, segment_index=-1)

Returns the radius of a circle curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    number: The radius of the circle if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select circle")
    if rs.IsCircle(id):
        radius = rs.CircleRadius(id)
        print("Circle radius: {}".format(radius))

##### See Also:

  * AddCircle
  * AddCircle3Pt
  * CircleCenterPoint
  * CircleCircumference
  * IsCircle

  

CloseCurve

    
    
    CloseCurve(curve_id, tolerance=-1.0)

Closes an open curve object by making adjustments to the end points so they
meet at a point

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    tolerance (number, optional): maximum allowable distance between start and end
                                  point. If omitted, the current absolute tolerance is used

##### Returns:

    
    
    guid: id of the new curve object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    if not rs.IsCurveClosed(obj) and rs.IsCurveClosable(obj):
        rs.CloseCurve( obj )

##### See Also:

  * IsCurveClosable
  * IsCurveClosed

  

ClosedCurveOrientation

    
    
    ClosedCurveOrientation(curve_id, direction=(0,0,1))

Determine the orientation (counter-clockwise or clockwise) of a closed, planar
curve

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    direction (vector, optional): 3d vector that identifies up, or Z axs, direction of
                                  the plane to test against

##### Returns:

    
    
    number: 1 if the curve's orientation is clockwise
           -1 if the curve's orientation is counter-clockwise
            0 if unable to compute the curve's orientation

  

ConvertCurveToPolyline

    
    
    ConvertCurveToPolyline(curve_id, angle_tolerance=5.0, tolerance=0.01, delete_input=False, min_edge_length=0, max_edge_length=0)

Convert curve to a polyline curve

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    angle_tolerance (number, optional): The maximum angle between curve tangents at line endpoints.
                                        If omitted, the angle tolerance is set to 5.0.
    tolerance(number, optional): The distance tolerance at segment midpoints. If omitted, the tolerance is set to 0.01.
    delete_input(bool, optional): Delete the curve object specified by curve_id. If omitted, curve_id will not be deleted.
    min_edge_length (number, optional): Minimum segment length
    max_edge_length (number, optonal): Maximum segment length

##### Returns:

    
    
    guid: The new curve if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        polyline = rs.ConvertCurveToPolyline(obj)
        if polyline: rs.SelectObject(polyline)

##### See Also:

  * IsCurve

  

CurveArcLengthPoint

    
    
    CurveArcLengthPoint(curve_id, length, from_start=True)

Returns the point on the curve that is a specified arc length from the start
of the curve.

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    length (number): The arc length from the start of the curve to evaluate.
    from_start (bool, optional): If not specified or True, then the arc length point is
        calculated from the start of the curve. If False, the arc length
        point is calculated from the end of the curve.

##### Returns:

    
    
    point: on curve if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        length = rs.CurveLength(obj)
        point = rs.CurveArcLengthPoint(obj, length/3.0)
        rs.AddPoint( point )

##### See Also:

  * CurveEndPoint
  * CurveMidPoint
  * CurveStartPoint

  

CurveArea

    
    
    CurveArea(curve_id)

Returns area of closed planar curves. The results are based on the current
drawing units.

##### Parameters:

    
    
    curve_id (guid): The identifier of a closed, planar curve object.

##### Returns:

    
    
    list[number, number]: List of area information. The list will contain the following information:
      Element  Description
      [0]      The area. If more than one curve was specified, the
                 value will be the cumulative area.
      [1]      The absolute (+/-) error bound for the area.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a curve", rs.filter.curve)
    if id:
        props = rs.CurveArea(id)
        if props:
            print("The curve area is: {}".format(props[0]))

##### See Also:

  * IsCurve
  * IsCurveClosed
  * IsCurvePlanar

  

CurveAreaCentroid

    
    
    CurveAreaCentroid(curve_id)

Returns area centroid of closed, planar curves. The results are based on the
current drawing units.

##### Parameters:

    
    
    curve_id (guid)The identifier of a closed, planar curve object.

##### Returns:

    
    
    tuple(point, vector): of area centroid information containing the following information:
      Element  Description
      [0]        The 3d centroid point. If more than one curve was specified,
               the value will be the cumulative area.
      [1]        A 3d vector with the absolute (+/-) error bound for the area
               centroid.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a curve", rs.filter.curve)
    if id:
        props = rs.CurveAreaCentroid(id)
        if props:
            print("The curve area centroid is: {}".format(props[0]))

##### See Also:

  * IsCurve
  * IsCurveClosed
  * IsCurvePlanar

  

CurveArrows

    
    
    CurveArrows(curve_id, arrow_style=None)

Enables or disables a curve object's annotation arrows

##### Parameters:

    
    
    curve_id (guid): identifier of a curve
    arrow_style (number, optional): the style of annotation arrow to be displayed. If omitted the current type is returned.
      0 = no arrows
      1 = display arrow at start of curve
      2 = display arrow at end of curve
      3 = display arrow at both start and end of curve

##### Returns:

    
    
    number: if arrow_style is not specified, the current annotation arrow style
    number: if arrow_style is specified, the previous arrow style

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve", rs.filter.curve)
    if rs.CurveArrows(obj)!=3: rs.CurveArrows(obj, 3)

##### See Also:

  * IsCurve

  

CurveBooleanDifference

    
    
    CurveBooleanDifference(curve_id_0, curve_id_1, tolerance=None)

Calculates the difference between two closed, planar curves and adds the
results to the document. Note, curves must be coplanar.

##### Parameters:

    
    
    curve_id_0 (guid): identifier of the first curve object.
    curve_id_1 (guid): identifier of the second curve object.
    tolerance (float, optional): a positive tolerance value, or None for the doc default.

##### Returns:

    
    
    list(guid, ...): The identifiers of the new objects if successful, None on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curveA = rs.GetObject("Select first curve", rs.filter.curve)
    curveB = rs.GetObject("Select second curve", rs.filter.curve)
    arrResult = rs.CurveBooleanDifference(curveA, curveB)
    if arrResult:
        rs.DeleteObject( curveA )
        rs.DeleteObject( curveB )

##### See Also:

  * CurveBooleanIntersection
  * CurveBooleanUnion

  

CurveBooleanIntersection

    
    
    CurveBooleanIntersection(curve_id_0, curve_id_1, tolerance=None)

Calculates the intersection of two closed, planar curves and adds the results
to the document. Note, curves must be coplanar.

##### Parameters:

    
    
    curve_id_0 (guid): identifier of the first curve object.
    curve_id_1 (guid): identifier of the second curve object.
    tolerance (float, optional): a positive tolerance value, or None for the doc default.

##### Returns:

    
    
    list(guid, ...): The identifiers of the new objects.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curveA = rs.GetObject("Select first curve", rs.filter.curve)
    curveB = rs.GetObject("Select second curve", rs.filter.curve)
    result = rs.CurveBooleanIntersection(curveA, curveB)
    if result:
        rs.DeleteObject( curveA )
        rs.DeleteObject( curveB )

##### See Also:

  * CurveBooleanDifference
  * CurveBooleanUnion

  

CurveBooleanUnion

    
    
    CurveBooleanUnion(curve_id, tolerance=None)

Calculate the union of two or more closed, planar curves and add the results
to the document. Note, curves must be coplanar.

##### Parameters:

    
    
    curve_id ([guid, guid, ...])list of two or more close planar curves identifiers
    tolerance (float, optional): a positive tolerance value, or None for the doc default.

##### Returns:

    
    
    list(guid, ...): The identifiers of the new objects.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve_ids = rs.GetObjects("Select curves to union", rs.filter.curve)
    if curve_ids and len(curve_ids)>1:
        result = rs.CurveBooleanUnion(curve_ids)
        if result: rs.DeleteObjects(curve_ids)

##### See Also:

  * CurveBooleanDifference
  * CurveBooleanIntersection

  

CurveBrepIntersect

    
    
    CurveBrepIntersect(curve_id, brep_id, tolerance=None)

Intersects a curve object with a brep object. Note, unlike the
CurveSurfaceIntersection function, this function works on trimmed surfaces.

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    brep_id (guid): identifier of a brep object
    tolerance (number, optional): distance tolerance at segment midpoints.
                      If omitted, the current absolute tolerance is used.

##### Returns:

    
    
    list(guid, ...): identifiers for the newly created intersection objects if successful.
    None: on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve", rs.filter.curve)
    if curve:
        brep = rs.GetObject("Select a brep", rs.filter.surface + rs.filter.polysurface)
        if brep: rs.CurveBrepIntersect( curve, brep )

##### See Also:

  * CurveSurfaceIntersection

  

CurveClosestObject

    
    
    CurveClosestObject(curve_id, object_ids)

Returns the 3D point locations on two objects where they are closest to each
other. Note, this function provides similar functionality to that of Rhino's
ClosestPt command.

##### Parameters:

    
    
    curve_id (guid):identifier of the curve object to test
    object_ids ([guid, ...]) list of identifiers of point cloud, curve, surface, or
      polysurface to test against

##### Returns:

    
    
    tuple[guid, point, point]: containing the results of the closest point calculation.
    The elements are as follows:
      [0]    The identifier of the closest object.
      [1]    The 3-D point that is closest to the closest object.
      [2]    The 3-D point that is closest to the test curve.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filter = rs.filter.curve | rs.filter.pointcloud | rs.filter.surface | rs.filter.polysurface
    objects = rs.GetObjects("Select target objects for closest point", filter)
    if objects:
        curve = rs.GetObject("Select curve")
        if curve:
            results = rs.CurveClosestObject(curve, objects)
            if results:
                print("Curve id: {}".format(results[0]))
                rs.AddPoint( results[1] )
                rs.AddPoint( results[2] )

##### See Also:

  * CurveClosestPoint
  * EvaluateCurve
  * IsCurve

  

CurveClosestPoint

    
    
    CurveClosestPoint(curve_id, test_point, segment_index=-1 )

Returns parameter of the point on a curve that is closest to a test point.

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    point (point): sampling point
    segment_index (number, optional): curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    number: The parameter of the closest point on the curve

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a curve")
    if id:
        point = rs.GetPointOnCurve(id, "Pick a test point")
        if point:
            param = rs.CurveClosestPoint(id, point)
            print("Curve parameter: {}".format(param))

##### See Also:

  * EvaluateCurve
  * IsCurve

  

CurveContourPoints

    
    
    CurveContourPoints(curve_id, start_point, end_point, interval=None)

Returns the 3D point locations calculated by contouring a curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object.
    start_point (point): 3D starting point of a center line.
    end_point (point): 3D ending point of a center line.
    interval (number, optional): The distance between contour curves. If omitted,
    the interval will be equal to the diagonal distance of the object's
    bounding box divided by 50.

##### Returns:

    
    
    list(point, ....): A list of 3D points, one for each contour

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    start_point = rs.GetPoint("Base point of center line")
    end_point = rs.GetPoint("Endpoint of center line", start_point)
    contour = rs.CurveContourPoints(obj, start_point, end_point)
    if contour: rs.AddPoints(contour)

##### See Also:

  * AddSrfContourCrvs

  

CurveCurvature

    
    
    CurveCurvature(curve_id, parameter)

Returns the curvature of a curve at a parameter. See the Rhino help for
details on curve curvature

##### Parameters:

    
    
    curve_id (guid): identifier of the curve
    parameter (number): parameter to evaluate

##### Returns:

    
    
    tuple[point, vector, point, number, vector]: of curvature information on success
      [0] = point at specified parameter
      [1] = tangent vector
      [2] = center of radius of curvature
      [3] = radius of curvature
      [4] = curvature vector
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        point = rs.GetPointOnCurve(obj, "Pick a test point")
        if point:
            param = rs.CurveClosestPoint(obj, point)
            if param:
                data = rs.CurveCurvature(obj, param)
                if data:
                    print("Curve curvature evaluation at parameter {}".format(param, ":"))
                    print(" 3-D Point: {}".format(data[0]))
                    print(" 3-D Tangent: {}".format(data[1]))
                    print(" Center of radius of curvature: {}".format(data[2]))
                    print(" Radius of curvature: {}".format(data[3]))
                    print(" 3-D Curvature: {}".format(data[4]))

##### See Also:

  * SurfaceCurvature

  

CurveCurveIntersection

    
    
    CurveCurveIntersection(curveA, curveB=None, tolerance=-1)

Calculates intersection of two curve objects.

##### Parameters:

    
    
    curveA (guid): identifier of the first curve object.
    curveB  (guid, optional): identifier of the second curve object. If omitted, then a
             self-intersection test will be performed on curveA.
    tolerance (number, optional): absolute tolerance in drawing units. If omitted,
                      the document's current absolute tolerance is used.

##### Returns:

    
    
    list of tuples: containing intersection information if successful.
    The list will contain one or more of the following elements:
      Element Type     Description
      [n][0]  Number   The intersection event type, either Point (1) or Overlap (2).
      [n][1]  Point3d  If the event type is Point (1), then the intersection point 
                       on the first curve. If the event type is Overlap (2), then
                       intersection start point on the first curve.
      [n][2]  Point3d  If the event type is Point (1), then the intersection point
                       on the first curve. If the event type is Overlap (2), then
                       intersection end point on the first curve.
      [n][3]  Point3d  If the event type is Point (1), then the intersection point 
                       on the second curve. If the event type is Overlap (2), then
                       intersection start point on the second curve.
      [n][4]  Point3d  If the event type is Point (1), then the intersection point
                       on the second curve. If the event type is Overlap (2), then
                       intersection end point on the second curve.
      [n][5]  Number   If the event type is Point (1), then the first curve parameter.
                       If the event type is Overlap (2), then the start value of the
                       first curve parameter range.
      [n][6]  Number   If the event type is Point (1), then the first curve parameter.
                       If the event type is Overlap (2), then the end value of the
                       first curve parameter range.
      [n][7]  Number   If the event type is Point (1), then the second curve parameter.
                       If the event type is Overlap (2), then the start value of the
                       second curve parameter range.
      [n][8]  Number   If the event type is Point (1), then the second curve parameter.
                       If the event type is Overlap (2), then the end value of the 
                       second curve parameter range.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def ccx():
        curve1 = rs.GetObject("Select first curve", rs.filter.curve)
        if curve1 is None: return
        curve2 = rs.GetObject("Select second curve", rs.filter.curve)
        if curve2 is None: return
        intersection_list = rs.CurveCurveIntersection(curve1, curve2)
        if intersection_list is None:
            print("Selected curves do not intersect.")
            return
        for intersection in intersection_list:
            if intersection[0] == 1:
                print("Point")
                print("Intersection point on first curve:  {}".format(intersection[1]))
                print("Intersection point on second curve:  {}".format(intersection[3]))
                print("First curve parameter:  {}".format(intersection[5]))
                print("Second curve parameter:  {}".format(intersection[7]))
            else:
                print("Overlap")
                print("Intersection start point on first curve: {}".format(intersection[1]))
                print("Intersection end point on first curve: {}".format(intersection[2]))
                print("Intersection start point on second curve: {}".format(intersection[3]))
                print("Intersection end point on second curve: {}".format(intersection[4]))
                print("First curve parameter range: {} to {}".format(intersection[5], intersection[6]))
                print("Second curve parameter range: {} to {}".format(intersection[7], intersection[8]))
    ccx()

##### See Also:

  * CurveSurfaceIntersection

  

CurveDegree

    
    
    CurveDegree(curve_id, segment_index=-1)

Returns the degree of a curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object.
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve.

##### Returns:

    
    
    number: The degree of the curve if successful.
    None: on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        degree = rs.CurveDegree(obj)
        print("Curve degree:{}".format(degree))

##### See Also:

  * CurveDomain
  * IsCurve

  

CurveDeviation

    
    
    CurveDeviation(curve_a, curve_b)

Returns the minimum and maximum deviation between two curve objects

##### Parameters:

    
    
    curve_a, curve_b (guid): identifiers of two curves

##### Returns:

    
    
    tuple[number, number, number, number, number, number]: of deviation information on success
      [0] = curve_a parameter at maximum overlap distance point
      [1] = curve_b parameter at maximum overlap distance point
      [2] = maximum overlap distance
      [3] = curve_a parameter at minimum overlap distance point
      [4] = curve_b parameter at minimum overlap distance point
      [5] = minimum distance between curves
    None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curveA = rs.GetObject("Select first curve to test", rs.filter.curve)
    curveB = rs.GetObject("Select second curve to test", rs.filter.curve)
    deviation = rs.CurveDeviation(curveA, curveB)
    if deviation:
        print("Minimum deviation = {}".format(deviation[5]))
        print("Maximum deviation = {}".format(deviation[2]))

##### See Also:

  * CurveArea
  * CurveAreaCentroid

  

CurveDim

    
    
    CurveDim(curve_id, segment_index=-1)

Returns the dimension of a curve object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object.
    segment_index (number, optional): the curve segment if `curve_id` identifies a polycurve.

##### Returns:

    
    
    number: The dimension of the curve if successful. None on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve")
    if rs.IsCurve(curve):
        print("Curve dimension = {}".format(rs.CurveDim(curve)))

##### See Also:

  * CurveDegree
  * CurveDomain

  

CurveDirectionsMatch

    
    
    CurveDirectionsMatch(curve_id_0, curve_id_1)

Tests if two curve objects are generally in the same direction or if they
would be more in the same direction if one of them were flipped. When testing
curve directions, both curves must be either open or closed - you cannot test
one open curve and one closed curve.

##### Parameters:

    
    
    curve_id_0 (guid): identifier of first curve object
    curve_id_1 (guid): identifier of second curve object

##### Returns:

    
    
    bool: True if the curve directions match, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve1 = rs.GetObject("Select first curve to compare", rs.filter.curve)
    curve2 = rs.GetObject("Select second curve to compare", rs.filter.curve)
    if rs.CurveDirectionsMatch(curve1, curve2):
        print("Curves are in the same direction")
    else:
        print("Curve are not in the same direction")

##### See Also:

  * ReverseCurve

  

CurveDiscontinuity

    
    
    CurveDiscontinuity(curve_id, style)

Search for a derivatitive, tangent, or curvature discontinuity in a curve
object.

##### Parameters:

    
    
    curve_id (guid): identifier of curve object
    style (number): The type of continuity to test for. The types of
        continuity are as follows:
        Value    Description
        1        C0 - Continuous function
        2        C1 - Continuous first derivative
        3        C2 - Continuous first and second derivative
        4        G1 - Continuous unit tangent
        5        G2 - Continuous unit tangent and curvature

##### Returns:

    
    
    list(point, ...): 3D points where the curve is discontinuous

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve", rs.filter.curve)
    if rs.IsCurve(curve):
        points = rs.CurveDiscontinuity(curve, 2)
        if points: rs.AddPoints( points )

##### See Also:

  * IsCurve

  

CurveDomain

    
    
    CurveDomain(curve_id, segment_index=-1)

Returns the domain of a curve object as an indexable object with two elements.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve.

##### Returns:

    
    
    list(number, number): the domain of the curve if successful.
       [0] Domain minimum
       [1] Domain maximum
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        domain = rs.CurveDomain(obj)
        print("Curve domain: {} to {}".format(domain[0], domain[1]))

##### See Also:

  * CurveDegree
  * IsCurve

  

CurveEditPoints

    
    
    CurveEditPoints(curve_id, return_parameters=False, segment_index=-1)

Returns the edit, or Greville, points of a curve object. For each curve
control point, there is a corresponding edit point.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    return_parameters (bool, optional): if True, return as a list of curve parameters.
                                        If False, return as a list of 3d points
    segment_index (number, optional): the curve segment index is `curve_id` identifies a polycurve

##### Returns:

    
    
    list(point, ....): curve edit points on success
    None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        points = rs.CurveEditPoints(obj)
        if points: rs.AddPointCloud( points )

##### See Also:

  * IsCurve
  * CurvePointCount
  * CurvePoints

  

CurveEndPoint

    
    
    CurveEndPoint(curve_id, segment_index=-1)

Returns the end point of a curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    point: The 3d endpoint of the curve if successful.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a curve")
    if rs.IsCurve(object):
        point = rs.CurveEndPoint(object)
        rs.AddPoint(point)

##### See Also:

  * CurveMidPoint
  * CurveStartPoint
  * IsCurve

  

CurveFilletPoints

    
    
    CurveFilletPoints(curve_id_0, curve_id_1, radius=1.0, base_point_0=None, base_point_1=None, return_points=True)

Find points at which to cut a pair of curves so that a fillet of a specified
radius fits. A fillet point is a pair of points (point0, point1) such that
there is a circle of radius tangent to curve curve0 at point0 and tangent to
curve curve1 at point1. Of all possible fillet points, this function returns
the one which is the closest to the base point base_point_0, base_point_1.
Distance from the base point is measured by the sum of arc lengths along the
two curves.

##### Parameters:

    
    
    curve_id_0 (guid): identifier of the first curve object.
    curve_id_1 (guid): identifier of the second curve object.
    radius (number, optional): The fillet radius. If omitted, a radius
                   of 1.0 is specified.
    base_point_0 (point, optional): The base point on the first curve.
                   If omitted, the starting point of the curve is used.
    base_point_1 (point, optional): The base point on the second curve. If omitted,
                   the starting point of the curve is used.
    return_points (bool, optional): If True (Default), then fillet points are
                   returned. Otherwise, a fillet curve is created and
                   it's identifier is returned.

##### Returns:

    
    
    list(point, point, point, vector, vector, vector): If return_points is True, then a list of point and vector values
    if successful. The list elements are as follows:
        [0]    A point on the first curve at which to cut (point).
        [1]    A point on the second curve at which to cut (point).
        [2]    The fillet plane's origin (point). This point is also
                 the center point of the fillet
        [3]    The fillet plane's X axis (vector).
        [4]    The fillet plane's Y axis (vector).
        [5]    The fillet plane's Z axis (vector).
          
    guid: If return_points is False, then the identifier of the fillet curve
          if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve0 = rs.AddLine([0,0,0], [5,1,0])
    curve1 = rs.AddLine([0,0,0], [1,5,0])
    fillet = rs.CurveFilletPoints(curve0, curve1)
    if fillet:
        rs.AddPoint( fillet[0] )
        rs.AddPoint( fillet[1] )
        rs.AddPoint( fillet[2] )

##### See Also:

  * AddFilletCurve

  

CurveFrame

    
    
    CurveFrame(curve_id, parameter, segment_index=-1)

Returns the plane at a parameter of a curve. The plane is based on the tangent
and curvature vectors at a parameter.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object.
    parameter (number): parameter to evaluate.
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    plane: The plane at the specified parameter if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetCurveObject("Select a curve")
    if curve:
        plane = rs.CurveFrame(curve[0], curve[4])
        rs.AddPlaneSurface(plane, 5.0, 3.0)

##### See Also:

  * CurvePerpFrame

  

CurveKnotCount

    
    
    CurveKnotCount(curve_id, segment_index=-1)

Returns the knot count of a curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object.
    segment_index (number, optional): the curve segment if `curve_id` identifies a polycurve.

##### Returns:

    
    
    number: The number of knots if successful.
    None: if not successful or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        count = rs.CurveKnotCount(obj)
        print("Curve knot count:{}".format(count))

##### See Also:

  * DivideCurve
  * IsCurve

  

CurveKnots

    
    
    CurveKnots(curve_id, segment_index=-1)

Returns the knots, or knot vector, of a curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object.
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve.

##### Returns:

    
    
    list(number, ....): knot values if successful.
    None: if not successful or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        knots = rs.CurveKnots(obj)
        if knots:
            for knot in knots: print("Curve knot value:{}".format(knot))

##### See Also:

  * CurveKnotCount
  * IsCurve

  

CurveLength

    
    
    CurveLength(curve_id, segment_index=-1, sub_domain=None)

Returns the length of a curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve
    sub_domain ([number, number], optional): list of two numbers identifying the sub-domain of the
        curve on which the calculation will be performed. The two parameters
        (sub-domain) must be non-decreasing. If omitted, the length of the
        entire curve is returned.

##### Returns:

    
    
    number: The length of the curve if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a curve")
    if rs.IsCurve(object):
        length = rs.CurveLength(object)
        print("Curve length:{}".format(length))

##### See Also:

  * CurveDomain
  * IsCurve

  

CurveMidPoint

    
    
    CurveMidPoint(curve_id, segment_index=-1)

Returns the mid point of a curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    point: The 3D midpoint of the curve if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a curve")
    if rs.IsCurve(object):
        point = rs.CurveMidPoint(pbject)
        rs.AddPoint( point )

##### See Also:

  * CurveEndPoint
  * CurveStartPoint
  * IsCurve

  

CurveNormal

    
    
    CurveNormal(curve_id, segment_index=-1)

Returns the normal direction of the plane in which a planar curve object lies.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment if curve_id identifies a polycurve

##### Returns:

    
    
    vector: The 3D normal vector if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a planar curve")
    if rs.IsCurve(object) and rs.IsCurvePlanar(object):
        normal = rs.CurveNormal(object)
        if normal: print("Curve Normal:{}".format(normal))

##### See Also:

  * IsCurve
  * IsCurvePlanar

  

CurveNormalizedParameter

    
    
    CurveNormalizedParameter(curve_id, parameter)

Converts a curve parameter to a normalized curve parameter; one that ranges
between 0-1

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    parameter (number): the curve parameter to convert

##### Returns:

    
    
    number: normalized curve parameter

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve")
    if rs.IsCurve(obj):
        domain = rs.CurveDomain(obj)
        parameter = (domain[0]+domain[1])/2.0
        print("Curve parameter:{}".format(parameter))
        normalized = rs.CurveNormalizedParameter(obj, parameter)
        print("Normalized parameter:{}".format(normalized))

##### See Also:

  * CurveDomain
  * CurveParameter

  

CurveParameter

    
    
    CurveParameter(curve_id, parameter)

Converts a normalized curve parameter to a curve parameter; one within the
curve's domain

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    parameter (number): the normalized curve parameter to convert

##### Returns:

    
    
    number: curve parameter

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve")
    if rs.IsCurve(obj):
        normalized = 0.5
        print("Normalized parameter:{}".format(normalized))
        parameter = rs.CurveParameter(obj, normalized)
        print("Curve parameter:{}".format(parameter))

##### See Also:

  * CurveDomain
  * CurveNormalizedParameter

  

CurvePerpFrame

    
    
    CurvePerpFrame(curve_id, parameter)

Returns the perpendicular plane at a parameter of a curve. The result is
relatively parallel (zero-twisting) plane

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    parameter (number): parameter to evaluate

##### Returns:

    
    
    plane: Plane on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    crv = rs.GetCurveObject("Select a curve")
    if crv:
        plane = rs.CurvePerpFrame(crv[0], crv[4])
        rs.AddPlaneSurface( plane, 1, 1 )

##### See Also:

  * CurveFrame

  

CurvePlane

    
    
    CurvePlane(curve_id, segment_index=-1)

Returns the plane in which a planar curve lies. Note, this function works only
on planar curves.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    plane: The plane in which the curve lies if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve", rs.filter.curve)
    if rs.IsCurvePlanar(curve):
        plane = rs.CurvePlane(curve)
        rs.ViewCPlane(None, plane)

##### See Also:

  * IsCurve
  * IsCurvePlanar

  

CurvePointCount

    
    
    CurvePointCount(curve_id, segment_index=-1)

Returns the control points count of a curve object.

##### Parameters:

    
    
    curve_id (guid) identifier of the curve object
    segment_index (number, optional): the curve segment if `curve_id` identifies a polycurve

##### Returns:

    
    
    number: Number of control points if successful.
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        count = rs.CurvePointCount(obj)
        print("Curve point count:{}".format(count))

##### See Also:

  * DivideCurve
  * IsCurve

  

CurvePoints

    
    
    CurvePoints(curve_id, segment_index=-1)

Returns the control points, or control vertices, of a curve object. If the
curve is a rational NURBS curve, the euclidean control vertices are returned.

##### Parameters:

    
    
    curve_id (guid): the object's identifier
    segment_index (number, optional): the curve segment if `curve_id` identifies a polycurve

##### Returns:

    
    
    list(point, ...): the control points, or control vertices, of a curve object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        points = rs.CurvePoints(obj)
        if points: [rs.AddPoint(pt) for pt in points]

##### See Also:

  * CurvePointCount
  * IsCurve

  

CurveRadius

    
    
    CurveRadius(curve_id, test_point, segment_index=-1)

Returns the radius of curvature at a point on a curve.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    test_point (point): sampling point
    segment_index (number, optional): the curve segment if curve_id identifies a polycurve

##### Returns:

    
    
    number: The radius of curvature at the point on the curve if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        point = rs.GetPointOnCurve(obj, "Pick a test point")
        if point:
            radius = rs.CurveRadius(obj, point)
            print("Radius of curvature:{}".format(radius))

##### See Also:

  * IsCurve

  

CurveSeam

    
    
    CurveSeam(curve_id, parameter)

Adjusts the seam, or start/end, point of a closed curve.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    parameter (number): The parameter of the new start/end point.
                Note, if successful, the resulting curve's
                domain will start at `parameter`.

##### Returns:

    
    
    bool: True or False indicating success or failure.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select closed curve", rs.filter.curve)
    if rs.IsCurveClosed(obj):
        domain = rs.CurveDomain(obj)
        parameter = (domain[0] + domain[1])/2.0
        rs.CurveSeam( obj, parameter )

##### See Also:

  * IsCurve
  * IsCurveClosed

  

CurveStartPoint

    
    
    CurveStartPoint(curve_id, segment_index=-1, point=None)

Returns the start point of a curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve
    point (point, optional): new start point

##### Returns:

    
    
    point: The 3D starting point of the curve if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a curve")
    if rs.IsCurve(object):
        point = rs.CurveStartPoint(object)
        rs.AddPoint(point)

##### See Also:

  * CurveEndPoint
  * CurveMidPoint
  * IsCurve

  

CurveSurfaceIntersection

    
    
    CurveSurfaceIntersection(curve_id, surface_id, tolerance=-1, angle_tolerance=-1)

Calculates intersection of a curve object with a surface object. Note, this
function works on the untrimmed portion of the surface.

##### Parameters:

    
    
    curve_id (guid): The identifier of the first curve object.
    surface_id (guid): The identifier of the second curve object. If omitted,
        the a self-intersection test will be performed on curve.
    tolerance (number, optional): The absolute tolerance in drawing units. If omitted,
        the document's current absolute tolerance is used.
    angle_tolerance (number, optional) angle tolerance in degrees. The angle
        tolerance is used to determine when the curve is tangent to the
        surface. If omitted, the document's current angle tolerance is used.

##### Returns:

    
    
    list(list(point, point, point, point, number, number, number, number, number, number), ...): of intersection information if successful.
    The list will contain one or more of the following elements:
      Element Type     Description
      [n][0]  Number   The intersection event type, either Point(1) or Overlap(2).
      [n][1]  Point3d  If the event type is Point(1), then the intersection point
                       on the first curve. If the event type is Overlap(2), then
                       intersection start point on the first curve.
      [n][2]  Point3d  If the event type is Point(1), then the intersection point
                       on the first curve. If the event type is Overlap(2), then
                       intersection end point on the first curve.
      [n][3]  Point3d  If the event type is Point(1), then the intersection point
                       on the second curve. If the event type is Overlap(2), then
                       intersection start point on the surface.
      [n][4]  Point3d  If the event type is Point(1), then the intersection point
                       on the second curve. If the event type is Overlap(2), then
                       intersection end point on the surface.
      [n][5]  Number   If the event type is Point(1), then the first curve parameter.
                       If the event type is Overlap(2), then the start value of the
                       first curve parameter range.
      [n][6]  Number   If the event type is Point(1), then the first curve parameter.
                       If the event type is Overlap(2), then the end value of the
                       curve parameter range.
      [n][7]  Number   If the event type is Point(1), then the U surface parameter.
                       If the event type is Overlap(2), then the U surface parameter
                       for curve at (n, 5).
      [n][8]  Number   If the event type is Point(1), then the V surface parameter.
                       If the event type is Overlap(2), then the V surface parameter
                       for curve at (n, 5).
      [n][9]  Number   If the event type is Point(1), then the U surface parameter.
                       If the event type is Overlap(2), then the U surface parameter
                       for curve at (n, 6).
      [n][10] Number   If the event type is Point(1), then the V surface parameter.
                       If the event type is Overlap(2), then the V surface parameter
                       for curve at (n, 6).

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def csx():
        curve = rs.GetObject("Select curve", rs.filter.curve)
        if curve is None: return
        surface = rs.GetObject("Select surface", rs.filter.surface)
        if surface is None: return
        intersection_list = rs.CurveSurfaceIntersection(curve, surface)
        if intersection_list is None:
            print("Curve and surface do not intersect.")
            return
        for intersection in intersection_list:
            if intersection[0]==1:
                print("Point")
                print("Intersection point on curve:{}".format(intersection[1]))
                print("Intersection point on surface:{}".format(intersection[3]))
                print("Curve parameter:{}".format(intersection[5]))
                print("Surface parameter: {}, {}".format(intersection[7], intersection[8]))
            else:
                print("Overlap")
                print("Intersection start point on curve:{}".format(intersection[1]))
                print("Intersection end point on curve:{}".format(intersection[2]))
                print("Intersection start point on surface:{}".format(intersection[3]))
                print("Intersection end point on surface:{}".format(intersection[4]))
                print("Curve parameter range: {} to {}".format(intersection[5], intersection[6]))
                print("Surface parameter range: {}, {} to {}, {}".format(intersection[7] intersection[8], intersection[9], intersection[10]))
    csx()

##### See Also:

  * CurveCurveIntersection
  * CurveBrepIntersect

  

CurveTangent

    
    
    CurveTangent(curve_id, parameter, segment_index=-1)

Returns a 3D vector that is the tangent to a curve at a parameter.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    parameter (number) parameter to evaluate
    segment_index (number, optional) the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    vector: A 3D vector if successful.
    None: on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve", rs.filter.curve)
    if obj:
        point = rs.GetPointOnCurve(obj)
        if point:
            param = rs.CurveClosestPoint(obj, point)
            normal = rs.CurveTangent(obj, param)
            print(normal)

##### See Also:

  * CurveClosestPoint
  * CurveDomain

  

CurveWeights

    
    
    CurveWeights(curve_id, segment_index=-1)

Returns list of weights that are assigned to the control points of a curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    number: The weight values of the curve if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        weights = rs.CurveWeights(obj)
        if weights:
            for weight in weights:
                print("Curve control point weight value:{}".format(weight))

##### See Also:

  * CurveKnots
  * IsCurve

  

DivideCurve

    
    
    DivideCurve(curve_id, segments, create_points=False, return_points=True)

Divides a curve object into a specified number of segments.

##### Parameters:

    
    
    curve_id (guid):identifier of the curve object
    segments (number): The number of segments.
    create_points (bool, optional): Create the division points. If omitted or False,
        points are not created.
    return_points (bool, optional): If omitted or True, points are returned.
        If False, then a list of curve parameters are returned.

##### Returns:

    
    
    list(point|number, ...): If `return_points` is not specified or True, then a list containing 3D division points.
    list(point|number, ...): If `return_points` is False, then an array containing division curve parameters.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if obj:
        points = rs.DivideCurve(obj, 4)
        for point in points: rs.AddPoint(point)

##### See Also:

  * DivideCurveEquidistant
  * DivideCurveLength

  

DivideCurveEquidistant

    
    
    DivideCurveEquidistant(curve_id, distance, create_points=False, return_points=True)

Divides a curve such that the linear distance between the points is equal.

##### Parameters:

    
    
    curve_id (guid): the object's identifier
    distance (number): linear distance between division points
    create_points (bool, optional): create the division points if True.
    return_points (bool, optional): If True, return a list of points.
                                    If False, return a list of curve parameters

##### Returns:

    
    
    list(point|number, ...): points or curve parameters based on the value of return_points
    none on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve", rs.filter.curve)
    if obj:
        points = rs.DivideCurveEquidistant(obj, 4, True)

##### See Also:

  * DivideCurve
  * DivideCurveLength

  

DivideCurveLength

    
    
    DivideCurveLength(curve_id, length, create_points=False, return_points=True)

Divides a curve object into segments of a specified length.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    length (number): The length of each segment.
    create_points (bool, optional): Create the division points. If omitted or False,
        points are not created.
    return_points (bool, optional): If omitted or True, points are returned.
        If False, then a list of curve parameters are returned.

##### Returns:

    
    
    list(point, ...): If return_points is not specified or True, then a list containing division points.
    list(number, ...): If return_points is False, then an array containing division curve parameters.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        length = rs.CurveLength(obj) / 4
        points = rs.DivideCurveLength(obj, length)
        for point in points: rs.AddPoint(point)

##### See Also:

  * DivideCurve
  * DivideCurveEquidistant

  

EllipseCenterPoint

    
    
    EllipseCenterPoint(curve_id)

Returns the center point of an elliptical-shaped curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object.

##### Returns:

    
    
    point: The 3D center point of the ellipse if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select ellipse")
    if rs.IsEllipse(obj):
        point = rs.EllipseCenterPoint(obj)
        rs.AddPoint( point )

##### See Also:

  * IsEllipse
  * EllipseQuadPoints

  

EllipseQuadPoints

    
    
    EllipseQuadPoints(curve_id)

Returns the quadrant points of an elliptical-shaped curve object.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object.

##### Returns:

    
    
    list(point, point, point, point): Four points identifying the quadrants of the ellipse

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select ellipse")
    if rs.IsEllipse(obj):
        rs.AddPoints( rs.EllipseQuadPoints(obj) )

##### See Also:

  * IsEllipse
  * EllipseCenterPoint

  

EvaluateCurve

    
    
    EvaluateCurve(curve_id, t, segment_index=-1)

Evaluates a curve at a parameter and returns a 3D point

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    t (number): the parameter to evaluate
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    point: a 3-D point if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        domain = rs.CurveDomain(obj)
        t = domain[1]/2.0
        point = rs.EvaluateCurve(obj, t)
        rs.AddPoint( point )

##### See Also:

  * CurveClosestPoint
  * IsCurve

  

ExplodeCurves

    
    
    ExplodeCurves(curve_ids, delete_input=False)

Explodes, or un-joins, one curves. Polycurves will be exploded into curve
segments. Polylines will be exploded into line segments. ExplodeCurves will
return the curves in topological order.

##### Parameters:

    
    
    curve_ids (guid): the curve object(s) to explode.
    delete_input (bool, optional): Delete input objects after exploding if True.

##### Returns:

    
    
    list(guid, ...): identifying the newly created curve objects

##### Example:

    
    
    import rhinoscriptsyntax as rs
    crv = rs.GetObject("Select curve to explode", rs.filter.curve)
    if rs.IsCurve(crv): rs.ExplodeCurves(crv)

##### See Also:

  * IsCurve
  * IsPolyCurve
  * IsPolyline
  * JoinCurves

  

ExtendCurve

    
    
    ExtendCurve(curve_id, extension_type, side, boundary_object_ids)

Extends a non-closed curve object by a line, arc, or smooth extension until it
intersects a collection of objects.

##### Parameters:

    
    
    curve_id (guid): identifier of curve to extend
    extension_type (number):
      0 = line
      1 = arc
      2 = smooth
    side (number):
      0=extend from the start of the curve
      1=extend from the end of the curve
      2=extend from both the start and the end of the curve
    boundary_object_ids (guid): curve, surface, and polysurface objects to extend to

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filter = rs.filter.curve | rs.filter.surface | rs.filter.polysurface
    objects = rs.GetObjects("Select boundary objects", filter)
    if objects:
        curve = rs.GetObject("Select curve to extend", rs.filter.curve)
        if curve: rs.ExtendCurve( curve, 2, 1, objects )

##### See Also:

  * ExtendCurveLength
  * ExtendCurvePoint

  

ExtendCurveLength

    
    
    ExtendCurveLength(curve_id, extension_type, side, length)

Extends a non-closed curve by a line, arc, or smooth extension for a specified
distance

##### Parameters:

    
    
    curve_id (guid): curve to extend
    extension_type (number):
      0 = line
      1 = arc
      2 = smooth
    side (number):
      0=extend from start of the curve
      1=extend from end of the curve
      2=Extend from both ends
    length (number): distance to extend

##### Returns:

    
    
    guid: The identifier of the new object
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve to extend", rs.filter.curve)
    if curve:
        length = rs.GetReal("Length to extend", 3.0)
        if length: rs.ExtendCurveLength( curve, 2, 2, length )

##### See Also:

  * ExtendCurve
  * ExtendCurvePoint

  

ExtendCurvePoint

    
    
    ExtendCurvePoint(curve_id, side, point, extension_type=2)

Extends a non-closed curve by smooth extension to a point

##### Parameters:

    
    
    curve_id (guid): curve to extend
    side (number):
      0=extend from start of the curve
      1=extend from end of the curve
    point (guid|point): point to extend to
    extension_type (number, optional): type of extension
      0 = Line
      1 = Arc
      2 = Smooth

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve to extend", rs.filter.curve)
    if curve:
        point = rs.GetPoint("Point to extend to")
        if point: rs.ExtendCurvePoint(curve, 1, point)

##### See Also:

  * ExtendCurve
  * ExtendCurveLength

  

FairCurve

    
    
    FairCurve(curve_id, tolerance=1.0)

Fairs a curve. Fair works best on degree 3 (cubic) curves. Fair attempts to
remove large curvature variations while limiting the geometry changes to be no
more than the specified tolerance. Sometimes several applications of this
method are necessary to remove nasty curvature problems.

##### Parameters:

    
    
    curve_id (guid): curve to fair
    tolerance (number, optional): fairing tolerance

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curves = rs.GetObjects("Select curves to fair", rs.filter.curve)
    if curves:
        [rs.FairCurve(curve) for curve in curves]

  

FitCurve

    
    
    FitCurve(curve_id, degree=3, distance_tolerance=-1, angle_tolerance=-1)

Reduces number of curve control points while maintaining the curve's same
general shape. Use this function for replacing curves with many control
points. For more information, see the Rhino help for the FitCrv command.

##### Parameters:

    
    
    curve_id (guid): Identifier of the curve object
    degree (number, optional): The curve degree, which must be greater than 1.
                   The default is 3.
    distance_tolerance (number, optional): The fitting tolerance. If distance_tolerance
        is not specified or <= 0.0, the document absolute tolerance is used.
    angle_tolerance (number, optional): The kink smoothing tolerance in degrees. If
        angle_tolerance is 0.0, all kinks are smoothed. If angle_tolerance
        is > 0.0, kinks smaller than angle_tolerance are smoothed. If
        angle_tolerance is not specified or < 0.0, the document angle
        tolerance is used for the kink smoothing.

##### Returns:

    
    
    guid: The identifier of the new object
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    oldCurve = rs.GetObject("Select curve to fit", rs.filter.curve)
    if oldCurve:
        newCurve = rs.FitCurve(oldCurve)
        if newCurve: rs.DeleteObject(oldCurve)

  

InsertCurveKnot

    
    
    InsertCurveKnot(curve_id, parameter, symmetrical=False )

Inserts a knot into a curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    parameter (number): parameter on the curve
    symmetrical (bool, optional): if True, then knots are added on both sides of
        the center of the curve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve for knot insertion", rs.filter.curve)
    if obj:
        point = rs.GetPointOnCurve(obj, "Point on curve to add knot")
        if point:
            parameter = rs.CurveClosestPoint(obj, point)
            rs.InsertCurveKnot( obj, parameter )

##### See Also:

  * CurveKnotCount
  * CurveKnots

  

IsArc

    
    
    IsArc(curve_id, segment_index=-1)

Verifies an object is an open arc curve

##### Parameters:

    
    
    curve_id (guid): Identifier of the curve object
    segment_index (number): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select an arc")
    if rs.IsArc(obj):
        print("The object is an arc.")
    else:
        print("The object is not an arc.")

##### See Also:

  * AddArc3Pt
  * ArcAngle
  * ArcCenterPoint
  * ArcMidPoint
  * ArcRadius

  

IsCircle

    
    
    IsCircle(curve_id, tolerance=None)

Verifies an object is a circle curve

##### Parameters:

    
    
    curve_id (guid): Identifier of the curve object
    tolerance (number, optional) If the curve is not a circle, then the tolerance used
      to determine whether or not the NURBS form of the curve has the
      properties of a circle. If omitted, Rhino's internal zero tolerance is used

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a circle")
    if rs.IsCircle(obj):
        print("The object is a circle.")
    else:
        print("The object is not a circle.")

##### See Also:

  * AddCircle
  * AddCircle3Pt
  * CircleCenterPoint
  * CircleCircumference
  * CircleRadius

  

IsCurve

    
    
    IsCurve(object_id)

Verifies an object is a curve

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a curve")
    if rs.IsCurve(object):
        print("The object is a curve.")
    else:
        print("The object is not a curve.")

##### See Also:

  * IsCurveClosed
  * IsCurveLinear
  * IsCurvePeriodic
  * IsCurvePlanar

  

IsCurveClosable

    
    
    IsCurveClosable(curve_id, tolerance=None)

Decide if it makes sense to close off the curve by moving the end point to the
start point based on start-end gap size and length of curve as approximated by
chord defined by 6 points

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    tolerance[opt] = maximum allowable distance between start point and end
      point. If omitted, the document's current absolute tolerance is used

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    crv = rs.GetObject("Select curve", rs.filter.curve)
    if not rs.IsCurveClosed(crv) and rs.IsCurveClosable(crv):
        rs.CloseCurve( crv, 0.1 )

##### See Also:

  * CloseCurve
  * IsCurveClosed

  

IsCurveClosed

    
    
    IsCurveClosed(object_id)

Verifies an object is a closed curve object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if successful otherwise False.  None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a curve")
    if rs.IsCurve(object):
        if rs.IsCurveClosed(oObject):
            print("The object is a closed curve.")
        else:
            print("The object is not a closed curve.")
    else:
        print("The object is not a curve.")

##### See Also:

  * IsCurve
  * IsCurveLinear
  * IsCurvePeriodic
  * IsCurvePlanar

  

IsCurveInPlane

    
    
    IsCurveInPlane(object_id, plane=None)

Test a curve to see if it lies in a specific plane

##### Parameters:

    
    
    object_id (guid): the object's identifier
    plane (plane, optional): plane to test. If omitted, the active construction plane is used

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj) and rs.IsCurvePlanar(obj):
        if rs.IsCurveInPlane(obj):
            print("The curve lies in the current cplane.")
        else:
            print("The curve does not lie in the current cplane.")
    else:
        print("The object is not a planar curve.")

##### See Also:

  * IsCurve
  * IsCurvePlanar

  

IsCurveLinear

    
    
    IsCurveLinear(object_id, segment_index=-1)

Verifies an object is a linear curve

##### Parameters:

    
    
    curve_id (guid):identifier of the curve object
    segment_index (number): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a curve")
    if rs.IsCurve(id):
        if rs.IsCurveLinear(id):
            print("The object is a linear curve.")
        else:
            print("The object is not a linear curve.")
    else:
        print("The object is not a curve.")

##### See Also:

  * IsCurve
  * IsCurveClosed
  * IsCurvePeriodic
  * IsCurvePlanar

  

IsCurvePeriodic

    
    
    IsCurvePeriodic(curve_id, segment_index=-1)

Verifies an object is a periodic curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        if rs.IsCurvePeriodic(obj):
            print("The object is a periodic curve.")
        else:
            print("The object is not a periodic curve.")
    else:
        print("The object is not a curve.")

##### See Also:

  * IsCurve
  * IsCurveClosed
  * IsCurveLinear
  * IsCurvePlanar

  

IsCurvePlanar

    
    
    IsCurvePlanar(curve_id, segment_index=-1)

Verifies an object is a planar curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        if rs.IsCurvePlanar(obj):
            print("The object is a planar curve.")
        else:
            print("The object is not a planar curve.")
    else:
        print("The object is not a curve.")

##### See Also:

  * IsCurve
  * IsCurveClosed
  * IsCurveLinear
  * IsCurvePeriodic

  

IsCurveRational

    
    
    IsCurveRational(curve_id, segment_index=-1)

Verifies an object is a rational NURBS curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        if rs.IsCurveRational(obj):
            print("The object is a rational NURBS curve.")
        else:
            print("The object is not a rational NURBS curve.")
    else:
        print("The object is not a curve.")

##### See Also:

  * IsCurve
  * IsCurveClosed
  * IsCurveLinear
  * IsCurvePeriodic

  

IsEllipse

    
    
    IsEllipse(object_id, segment_index=-1)

Verifies an object is an elliptical-shaped curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select an ellipse")
    if rs.IsEllipse(obj):
        print("The object is an ellipse.")
    else:
        print("The object is not an ellipse.")

##### See Also:

  * EllipseCenterPoint
  * EllipseQuadPoints

  

IsLine

    
    
    IsLine(object_id, segment_index=-1)

Verifies an object is a line curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a line")
    if rs.IsLine(obj):
        print("The object is a line.")
    else:
        print("The object is not a line.")

##### See Also:

  * AddLine

  

IsPointOnCurve

    
    
    IsPointOnCurve(object_id, point, segment_index=-1)

Verifies that a point is on a curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    point (point): the test point
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve")
    if rs.IsCurve(obj):
        point = rs.GetPoint("Pick a test point")
        if point:
            if rs.IsPointOnCurve(obj, point):
                print("The point is on the curve")
            else:
                print("The point is not on the curve")

##### See Also:

  * IsCurve

  

IsPolyCurve

    
    
    IsPolyCurve(object_id, segment_index=-1)

Verifies an object is a PolyCurve curve

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional) the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polycurve")
    if rs.IsPolyCurve(obj):
        print("The object is a polycurve.")
    else:
        print("The object is not a polycurve.")

##### See Also:

  * PolyCurveCount

  

IsPolyline

    
    
    IsPolyline( object_id, segment_index=-1 )

Verifies an object is a Polyline curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    segment_index (number, optional): the curve segment index if `curve_id` identifies a polycurve

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polyline")
    if rs.IsPolyline(obj):
        print("The object is a polyline.")
    else:
        print("The object is not a polyline.")

##### See Also:

  * IsPolyline
  * PolylineVertices

  

JoinCurves

    
    
    JoinCurves(object_ids, delete_input=False, tolerance=None)

Joins multiple curves together to form one or more curves or polycurves

##### Parameters:

    
    
    object_ids (guid): list of multiple curves
    delete_input (bool, optional): delete input objects after joining
    tolerance (number, optional): join tolerance. If omitted, 2.1 * document absolute
        tolerance is used

##### Returns:

    
    
    list(guid, ...): Object id representing the new curves

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select curves to join", rs.filter.curve)
    if objs: rs.JoinCurves(objs)

##### See Also:

  * ExplodeCurves
  * IsCurve
  * IsCurveClosed

  

LineFitFromPoints

    
    
    LineFitFromPoints(points)

Returns a line that was fit through an array of 3D points

##### Parameters:

    
    
    points ([point, point, ...]): a list of at least two 3D points

##### Returns:

    
    
    line: line on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints()
    if points and len(points)>1:
        line=rs.LineFitFromPoints(points)
        if line: rs.AddLine(line.From, line.To)

##### See Also:

  * AddLine
  * CurveEndPoint
  * CurveStartPoint

  

MakeCurveNonPeriodic

    
    
    MakeCurveNonPeriodic(curve_id, delete_input=False)

Makes a periodic curve non-periodic. Non-periodic curves can develop kinks
when deformed

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    delete_input (bool): delete the input curve. If omitted, the input curve will not be deleted.

##### Returns:

    
    
    guid: id of the new or modified curve if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve", rs.filter.curve)
    if rs.IsCurvePeriodic(curve): rs.MakeCurveNonPeriodic( curve )

##### See Also:

  * IsCurvePeriodic

  

MeanCurve

    
    
    MeanCurve(curve0, curve1, tolerance=None)

Creates an average curve from two curves

##### Parameters:

    
    
    curve0, curve1 (guid): identifiers of two curves
    tolerance (number, optional): angle tolerance used to match kinks between curves

##### Returns:

    
    
    guid: id of the new or modified curve if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve0 = rs.GetObject("Select the first curve", rs.filter.curve)
    curve1 = rs.GetObject("Select the second curve", rs.filter.curve)
    rs.MeanCurve( curve0, curve1 )

##### See Also:

  * UnitAngleTolerance

  

MeshPolyline

    
    
    MeshPolyline(polyline_id)

Creates a polygon mesh object based on a closed polyline curve object. The
created mesh object is added to the document

##### Parameters:

    
    
    polyline_id (guid): identifier of the polyline curve object

##### Returns:

    
    
    guid: identifier of the new mesh object
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    polyline = rs.GetObject("Select a polyline", rs.filter.curve)
    if polyline:
        if rs.IsPolyline(polyline) and rs.IsCurveClosed(polyline):
            rs.MeshPolyline( polyline )

##### See Also:

  * IsCurveClosed
  * IsPolyline

  

OffsetCurve

    
    
    OffsetCurve(object_id, direction, distance, normal=None, style=1)

Offsets a curve by a distance. The offset curve will be added to Rhino

##### Parameters:

    
    
    object_id (guid): identifier of a curve object
    direction (point): point describing direction of the offset
    distance (number): distance of the offset
    normal (vector, optional): normal of the plane in which the offset will occur.
        If omitted, the normal of the active construction plane will be used
    style (number, optional): the corner style. If omitted, the style is sharp.
                              0 = None
                              1 = Sharp
                              2 = Round
                              3 = Smooth
                              4 = Chamfer

##### Returns:

    
    
    list(guid, ...): list of ids for the new curves on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a curve", rs.filter.curve)
    if rs.IsCurve(obj):
        rs.OffsetCurve( obj, [0,0,0], 1.0 )

##### See Also:

  * OffsetCurveOnSurface
  * OffsetSurface

  

OffsetCurveOnSurface

    
    
    OffsetCurveOnSurface(curve_id, surface_id, distance_or_parameter)

Offset a curve on a surface. The source curve must lie on the surface. The
offset curve or curves will be added to Rhino

##### Parameters:

    
    
    curve_id, surface_id (guid): curve and surface identifiers
    distance_or_parameter (number|tuple(number, number)): If a single number is passed, then this is the
      distance of the offset. Based on the curve's direction, a positive value
      will offset to the left and a negative value will offset to the right.
      If a tuple of two values is passed, this is interpreted as the surface
      U,V parameter that the curve will be offset through

##### Returns:

    
    
    list(guid, ...): identifiers of the new curves if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def TestOffset():
        curve = rs.GetObject("Select curve on a surface", rs.filter.curve)
        if curve is None: return False
        surface = rs.GetObject("Select base surface", rs.filter.surface)
        if surface is None: return False
        point = rs.GetPointOnSurface( surface, "Through point" )
        if point is None: return False
        parameter = rs.SurfaceClosestPoint(surface, point)
        rc = rs.OffsetCurveOnSurface( curve, surface, parameter )
        return rc is not None
           
    TestOffset()

##### See Also:

  * OffsetCurve
  * OffsetSurface

  

PlanarClosedCurveContainment

    
    
    PlanarClosedCurveContainment(curve_a, curve_b, plane=None, tolerance=None)

Determines the relationship between the regions bounded by two coplanar simple
closed curves

##### Parameters:

    
    
    curve_a, curve_b (guid): identifiers of two planar, closed curves
    plane (plane, optional): test plane. If omitted, the currently active construction
      plane is used
    tolerance (number, optional): if omitted, the document absolute tolerance is used

##### Returns:

    
    
    number: a number identifying the relationship if successful
      0 = the regions bounded by the curves are disjoint
      1 = the two curves intersect
      2 = the region bounded by curve_a is inside of curve_b
      3 = the region bounded by curve_b is inside of curve_a
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve1 = rs.GetObject("Select first curve", rs.filter.curve )
    curve2 = rs.GetObject("Select second curve", rs.filter.curve )
    if rs.IsCurvePlanar(curve1) and rs.IsCurvePlanar(curve2):
        if rs.IsCurveClosed(curve1) and rs.IsCurveClosed(curve2):
            if rs.IsCurveInPlane(curve1) and rs.IsCurveInPlane(curve2):
                result = rs.PlanarClosedCurveContainment(curve1, curve2)
                if result==0: print("The regions bounded by the curves are disjoint.")
                elif result==1: print("The two curves intersect..")
                elif result==2: print("The region bounded by Curve1 is inside of Curve2.")
                else: print("The region bounded by Curve2 is inside of Curve1.")

##### See Also:

  * PlanarCurveCollision
  * PointInPlanarClosedCurve

  

PlanarCurveCollision

    
    
    PlanarCurveCollision(curve_a, curve_b, plane=None, tolerance=None)

Determines if two coplanar curves intersect

##### Parameters:

    
    
    curve_a, curve_b (guid): identifiers of two planar curves
    plane (plane, optional): test plane. If omitted, the currently active construction
      plane is used
    tolerance (number, optional): if omitted, the document absolute tolerance is used

##### Returns:

    
    
    bool: True if the curves intersect; otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve1 = rs.GetObject("Select first curve")
    curve2 = rs.GetObject("Select second curve")
    if( rs.IsCurvePlanar(curve1) and rs.IsCurvePlanar(curve2) and rs.IsCurveInPlane(curve1) and rs.IsCurveInPlane(curve2) ):
        if rs.PlanarCurveCollision(curve1, curve2):
            print("The coplanar curves intersect.")
        else:
            print("The coplanar curves do not intersect.")

##### See Also:

  * CurveCurveIntersection
  * PlanarClosedCurveContainment
  * PointInPlanarClosedCurve

  

PointInPlanarClosedCurve

    
    
    PointInPlanarClosedCurve(point, curve, plane=None, tolerance=None)

Determines if a point is inside of a closed curve, on a closed curve, or
outside of a closed curve

##### Parameters:

    
    
    point (point|guid): text point
    curve (guid): identifier of a curve object
    plane (plane, optional): plane containing the closed curve and point. If omitted,
        the currently active construction plane is used
    tolerance (number, optional) it omitted, the document abosulte tolerance is used

##### Returns:

    
    
    number: number identifying the result if successful
            0 = point is outside of the curve
            1 = point is inside of the curve
            2 = point in on the curve

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a planar, closed curve", rs.filter.curve)
    if rs.IsCurveClosed(curve) and rs.IsCurvePlanar(curve):
        point = rs.GetPoint("Pick a point")
        if point:
            result = rs.PointInPlanarClosedCurve(point, curve)
            if result==0: print("The point is outside of the closed curve.")
            elif result==1: print("The point is inside of the closed curve.")
            else: print("The point is on the closed curve.")

##### See Also:

  * PlanarClosedCurveContainment
  * PlanarCurveCollision

  

PolyCurveCount

    
    
    PolyCurveCount(curve_id, segment_index=-1)

Returns the number of curve segments that make up a polycurve

##### Parameters:

    
    
    curve_id (guid): the object's identifier
    segment_index (number, optional): if `curve_id` identifies a polycurve object, then `segment_index` identifies the curve segment of the polycurve to query.

##### Returns:

    
    
    number: the number of curve segments in a polycurve if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polycurve")
    if rs.IsPolyCurve(obj):
        count = rs.PolyCurveCount(obj)
        if count: print("The polycurve contains {} curves".format(count))

##### See Also:

  * IsPolyCurve

  

PolylineVertices

    
    
    PolylineVertices(curve_id, segment_index=-1)

Returns the vertices of a polyline curve on success

##### Parameters:

    
    
    curve_id (guid): the object's identifier
    segment_index (number, optional): if curve_id identifies a polycurve object, then segment_index identifies the curve segment of the polycurve to query.

##### Returns:

    
    
    list(point, ...): an list of Point3d vertex points if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polyline")
    if rs.IsPolyline(obj):
        points = rs.PolylineVertices(obj)
        if points:
            for point in points: rs.AddPoint(point)

##### See Also:

  * AddPolyline
  * IsPolyline

  

ProjectCurveToMesh

    
    
    ProjectCurveToMesh(curve_ids, mesh_ids, direction)

Projects one or more curves onto one or more surfaces or meshes

##### Parameters:

    
    
    curve_ids ([guid, ...]): identifiers of curves to project
    mesh_ids ([guid, ...]): identifiers of meshes to project onto
    direction (vector): projection direction

##### Returns:

    
    
    list(guid, ...): list of identifiers for the resulting curves.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Select mesh to project onto", rs.filter.mesh)
    curve= rs.GetObject("Select curve to project", rs.filter.curve)
    #Project down...
    results = rs.ProjectCurveToMesh(curve, mesh, (0,0,-1))

##### See Also:

  * ProjectCurveToSurface
  * ProjectPointToMesh
  * ProjectPointToSurface

  

ProjectCurveToSurface

    
    
    ProjectCurveToSurface(curve_ids, surface_ids, direction)

Projects one or more curves onto one or more surfaces or polysurfaces

##### Parameters:

    
    
    curve_ids ([guid, ...]): identifiers of curves to project
    surface_ids ([guid, ...]): identifiers of surfaces to project onto
    direction (vector): projection direction

##### Returns:

    
    
    list(guid, ...): list of identifiers

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface to project onto", rs.filter.surface)
    curve = rs.GetObject("Select curve to project", rs.filter.curve)
    # Project down...
    results = rs.ProjectCurveToSurface(curve, surface, (0,0,-1))

##### See Also:

  * ProjectCurveToMesh
  * ProjectPointToMesh
  * ProjectPointToSurface

  

RebuildCurve

    
    
    RebuildCurve(curve_id, degree=3, point_count=10)

Rebuilds a curve to a given degree and control point count. For more
information, see the Rhino help for the Rebuild command.

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object
    degree (number, optional): new degree (must be greater than 0)
    point_count (number, optional) new point count, which must be bigger than degree.

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve to rebuild", rs.filter.curve)
    if curve: rs.RebuildCurve(curve, 3, 10)

##### See Also:

  * RebuildSurface

  

RemoveCurveKnot

    
    
    RemoveCurveKnot(curve, parameter)

Deletes a knot from a curve object.

##### Parameters:

    
    
    curve (guid): The reference of the source object
    parameter (number): The parameter on the curve. Note, if the parameter is not equal to one
                    of the existing knots, then the knot closest to the specified parameter
                    will be removed.

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    
    crv_info = rs.GetCurveObject("Select curve near knot to be removed")
    if crv_info:
        crv_id = crv_info[0]
        crv_param = crv_info[4]
        rs.RemoveCurveKnot(crv_id, crv_param)

##### See Also:

  * RemoveSurfaceKnot

  

ReverseCurve

    
    
    ReverseCurve(curve_id)

Reverses the direction of a curve object. Same as Rhino's Dir command

##### Parameters:

    
    
    curve_id (guid): identifier of the curve object

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve to reverse")
    if rs.IsCurve(curve): rs.ReverseCurve(curve)

##### See Also:

  * CurveDirectionsMatch

  

SimplifyCurve

    
    
    SimplifyCurve(curve_id, flags=0)

Replace a curve with a geometrically equivalent polycurve. The polycurve will
have the following properties: \- All the polycurve segments are lines,
polylines, arcs, or NURBS curves. \- The NURBS curves segments do not have
fully multiple interior knots. \- Rational NURBS curves do not have constant
weights. \- Any segment for which IsCurveLinear or IsArc is True is a line,
polyline segment, or an arc. \- Adjacent co-linear or co-circular segments are
combined. \- Segments that meet with G1-continuity have there ends tuned up so
that they meet with G1-continuity to within machine precision. \- If the
polycurve is a polyline, a polyline will be created

##### Parameters:

    
    
    curve_id (guid): the object's identifier
    flags (number, optional): the simplification methods to use. By default, all methods are used (flags = 0)
      Value Description
      0     Use all methods.
      1     Do not split NURBS curves at fully multiple knots.
      2     Do not replace segments with IsCurveLinear = True with line curves.
      4     Do not replace segments with IsArc = True with arc curves.
      8     Do not replace rational NURBS curves with constant denominator with an equivalent non-rational NURBS curve.
      16    Do not adjust curves at G1-joins.
      32    Do not merge adjacent co-linear lines or co-circular arcs or combine consecutive line segments into a polyline.

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve to simplify", rs.filter.curve)
    if curve: rs.SimplifyCurve(curve)

##### See Also:

  * IsArc
  * IsCurveLinear

  

SplitCurve

    
    
    SplitCurve(curve_id, parameter, delete_input=True)

Splits, or divides, a curve at a specified parameter. The parameter must be in
the interior of the curve's domain

##### Parameters:

    
    
    curve_id (guid): the curve to split
    parameter ({number, ...]) one or more parameters to split the curve at
    delete_input (bool, optional): delete the input curve

##### Returns:

    
    
    list(guid, ....): list of new curves on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve to split", rs.filter.curve)
    if rs.IsCurve(curve):
        domain = rs.CurveDomain(curve)
        parameter = domain[1] / 2.0
        rs.SplitCurve( curve, parameter )

##### See Also:

  * TrimCurve

  

TrimCurve

    
    
    TrimCurve(curve_id, interval, delete_input=True)

Trims a curve by removing portions of the curve outside a specified interval

##### Parameters:

    
    
    curve_id (guid):the curve to trim
    interval ([number, number]): two numbers identifying the interval to keep. Portions of
      the curve before domain[0] and after domain[1] will be removed. If the
      input curve is open, the interval must be increasing. If the input
      curve is closed and the interval is decreasing, then the portion of
      the curve across the start and end of the curve is returned
    delete_input (bool): delete the input curve. If omitted the input curve is deleted.

##### Returns:

    
    
    list(guid, ...): identifier of the new curve on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve to trim", rs.filter.curve)
    if rs.IsCurve(curve):
        domain = rs.CurveDomain(curve)
        domain[1] /= 2.0
        rs.TrimCurve( curve, domain )

##### See Also:

  * SplitCurve

  

ChangeCurveDegree

    
    
    ChangeCurveDegree(object_id, degree)

Changes the degree of a curve object. For more information see the Rhino help
file for the ChangeDegree command.

##### Parameters:

    
    
    object_id (guid): the object's identifier.
    degree (number): the new degree.

##### Returns:

    
    
    bool: True of False indicating success or failure.
    None: on failure

##### See Also:

  * IsCurve
  * CurveDegree

  

AddTweenCurves

    
    
    AddTweenCurves(from_curve_id, to_curve_id, number_of_curves = 1, method = 0, sample_number = 10)

Creates curves between two open or closed input curves.

##### Parameters:

    
    
    from_curve_id (guid): identifier of the first curve object.
    to_curve_id (guid): identifier of the second curve object.
    number_of_curves (number): The number of curves to create. The default is 1.
    method (number): The method for refining the output curves, where:
      0: (Default) Uses the control points of the curves for matching. So the first control point of first curve is matched to first control point of the second curve.
      1: Refits the output curves like using the FitCurve method.  Both the input curve and the output curve will have the same structure. The resulting curves are usually more complex than input unless input curves are compatible.
      2: Input curves are divided to the specified number of points on the curve, corresponding points define new points that output curves go through. If you are making one tween curve, the method essentially does the following: divides the two curves into an equal number of points, finds the midpoint between the corresponding points on the curves, and interpolates the tween curve through those points.
    sample_number (number): The number of samples points to use if method is 2. The default is 10.

##### Returns:

    
    
    list(guid, ...): The identifiers of the new tween objects if successful, None on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curveA = rs.GetObject("Select first curve", rs.filter.curve)
    curveB = rs.GetObject("Select second curve", rs.filter.curve)
    arrResult = rs.AddTweenCurves(curveA, curveB, 6, 2, 30)

  

## dimension

AddAlignedDimension

    
    
    AddAlignedDimension(start_point, end_point, point_on_dimension_line, style=None)

Adds an aligned dimension object to the document. An aligned dimension is a
linear dimension lined up with two points

##### Parameters:

    
    
    start_point (point): first point of dimension
    end_point (point): second point of dimension
    point_on_dimension_line (point): location point of dimension line
    style (str, optional): name of dimension style

##### Returns:

    
    
    guid: identifier of new dimension on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    origin = 1, 1, 0
    offset = 11, 5, 0
    point = 1, 3, 0
    rs.AddAlignedDimension( origin, offset, point )

##### See Also:

  * IsAlignedDimension

  

AddDimStyle

    
    
    AddDimStyle(dimstyle_name=None)

Adds a new dimension style to the document. The new dimension style will be
initialized with the current default dimension style properties.

##### Parameters:

    
    
    dimstyle_name (str, optional): name of the new dimension style. If omitted, Rhino automatically generates the dimension style name

##### Returns:

    
    
    str: name of the new dimension style on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("New dimension style: {}".format(rs.AddDimStyle()))
    print("New dimension style: {}".format(rs.AddDimStyle("MyDimStyle")))

##### See Also:

  * CurrentDimStyle
  * DeleteDimStyle
  * IsDimStyle
  * RenameDimStyle

  

AddLeader

    
    
    AddLeader(points, view_or_plane=None, text=None)

Adds a leader to the document. Leader objects are planar. The 3D points passed
to this function should be co-planar

##### Parameters:

    
    
    points ([point, point, ....])list of (at least 2) 3D points
    view_or_plane (str, optional): If a view name is specified, points will be constrained
      to the view's construction plane. If a view is not specified, points
      will be constrained to a plane fit through the list of points
    text (str, optional): leader's text string

##### Returns:

    
    
    guid: identifier of the new leader on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(True, False, "Select leader points")
    if points: rs.AddLeader( points )

##### See Also:

  * IsLeader
  * LeaderText

  

AddLinearDimension

    
    
    AddLinearDimension(plane, start_point, end_point, point_on_dimension_line)

Adds a linear dimension to the document

##### Parameters:

    
    
    plane (plane): The plane on which the dimension will lie.
    start_point (point): The origin, or first point of the dimension.
    end_point (point): The offset, or second point of the dimension.
    point_on_dimension_line (point): A point that lies on the dimension line.

##### Returns:

    
    
    guid: identifier of the new object on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    points = rs.GetPoints(True,  False, "Select 3 dimension points")
    if points and len(points)>2:
        rs.AddLinearDimension(rs.WorldXYPlane(),  points[0], points[1], points[2] )

##### See Also:

  * IsLeader
  * LeaderText

  

CurrentDimStyle

    
    
    CurrentDimStyle(dimstyle_name=None)

Returns or changes the current default dimension style

##### Parameters:

    
    
    dimstyle_name (str, optional): name of an existing dimension style to make current

##### Returns:

    
    
    str: if dimstyle_name is not specified, name of the current dimension style
    str: if dimstyle_name is specified, name of the previous dimension style
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddDimStyle("MyDimStyle")
    rs.CurrentDimStyle("MyDimStyle")

##### See Also:

  * AddDimStyle
  * DeleteDimStyle
  * IsDimStyle
  * RenameDimStyle

  

DeleteDimStyle

    
    
    DeleteDimStyle(dimstyle_name)

Removes an existing dimension style from the document. The dimension style to
be removed cannot be referenced by any dimension objects.

##### Parameters:

    
    
    dimstyle_name (str): the name of an unreferenced dimension style

##### Returns:

    
    
    str: The name of the deleted dimension style if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.GetString("Dimension style to remove")
    if dimstyle: rs.DeleteDimStyle(dimstyle)

##### See Also:

  * AddDimStyle
  * CurrentDimStyle
  * IsDimStyle
  * RenameDimStyle

  

DimensionStyle

    
    
    DimensionStyle(object_id, dimstyle_name=None)

Returns or modifies the dimension style of a dimension object

##### Parameters:

    
    
    object_id (guid): identifier of the object
    dimstyle_name (str, optional): the name of an existing dimension style

##### Returns:

    
    
    str: if dimstyle_name is not specified, the object's current dimension style name
    str: if dimstyle_name is specified, the object's previous dimension style name
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsDimension(obj): rs.DimensionStyle(obj, "Default")

##### See Also:

  * DimStyleNames
  * IsDimStyle

  

DimensionText

    
    
    DimensionText(object_id)

Returns the text displayed by a dimension object

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    str: the text displayed by a dimension object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsDimension(obj):
        print(rs.DimensionText(obj))

##### See Also:

  * DimensionUserText
  * DimensionValue
  * IsDimension

  

DimensionUserText

    
    
    DimensionUserText(object_id, usertext=None)

Returns of modifies the user text string of a dimension object. The user text
is the string that gets printed when the dimension is defined

##### Parameters:

    
    
    object_id (guid): identifier of the object
    usertext (str, optional): the new user text string value

##### Returns:

    
    
    str: if usertext is not specified, the current usertext string
    str: if usertext is specified, the previous usertext string

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsDimension(obj):
        usertext = "!= " + chr(177) + str(rs.UnitAbsoluteTolerance())
        rs.DimensionUserText( obj, usertext )

##### See Also:

  * DimensionText
  * DimensionValue
  * IsDimension

  

DimensionValue

    
    
    DimensionValue(object_id)

Returns the value of a dimension object

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    number: numeric value of the dimension if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsDimension(obj):
        print(rs.DimensionValue(obj))

##### See Also:

  * DimensionText
  * DimensionUserText
  * IsDimension

  

DimStyleAnglePrecision

    
    
    DimStyleAnglePrecision(dimstyle, precision=None)

Returns or changes the angle display precision of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    precision (number, optional): the new angle precision value. If omitted, the current angle
      precision is returned

##### Returns:

    
    
    number: If a precision is not specified, the current angle precision
    number: If a precision is specified, the previous angle precision

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    precision = rs.DimStyleAnglePrecision(dimstyle)
    if precision>2:
        rs.DimStyleAnglePrecision( dimstyle, 2 )

##### See Also:

  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleArrowSize

    
    
    DimStyleArrowSize(dimstyle, size=None)

Returns or changes the arrow size of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    size (number, optional): the new arrow size. If omitted, the current arrow size is returned

##### Returns:

    
    
    number: If size is not specified, the current arrow size
    number: If size is specified, the previous arrow size
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    size = rs.DimStyleArrowSize(dimstyle)
    if size>1.0: rs.DimStyleArrowSize( dimstyle, 1.0 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleCount

    
    
    DimStyleCount()

Returns the number of dimension styles in the document

##### Returns:

    
    
    number: the number of dimension styles in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.DimStyleCount()
    print("There are", count, "dimension styles.")

##### See Also:

  * DimStyleNames
  * IsDimStyle

  

DimStyleExtension

    
    
    DimStyleExtension(dimstyle, extension=None)

Returns or changes the extension line extension of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    extension (number, optional): the new extension line extension

##### Returns:

    
    
    number: if extension is not specified, the current extension line extension
    number: if extension is specified, the previous extension line extension
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    extension = rs.DimStyleExtension(dimstyle)
    if extension>0.5: rs.DimStyleExtension( dimstyle, 0.5 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleFont

    
    
    DimStyleFont(dimstyle, font=None)

Returns or changes the font used by a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    font (str, optional): the new font face name

##### Returns:

    
    
    str: if font is not specified, the current font if successful
    str: if font is specified, the previous font if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    font = rs.DimStyleFont(dimstyle)
    if font!="Arial": rs.DimStyleFont( dimstyle, "Arial" )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleLeaderArrowSize

    
    
    DimStyleLeaderArrowSize(dimstyle, size=None)

Returns or changes the leader arrow size of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    size (number, optional) the new leader arrow size

##### Returns:

    
    
    number: if size is not specified, the current leader arrow size
    number: if size is specified, the previous leader arrow size
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    size = rs.DimStyleLeaderArrowSize(dimstyle)
    if size>1.0: rs.DimStyleLeaderArrowSize( dimstyle, 1.0 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleLengthFactor

    
    
    DimStyleLengthFactor(dimstyle, factor=None)

Returns or changes the length factor of a dimension style. Length factor is
the conversion between Rhino units and dimension units

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    factor (number, optional): the new length factor

##### Returns:

    
    
    number: if factor is not defined, the current length factor
    number: if factor is defined, the previous length factor
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    factor = rs.DimStyleLengthFactor(dimstyle)
    if factor>1.0: rs.DimStyleLengthFactor( dimstyle, 1.0 )

##### See Also:

  * DimStylePrefix
  * DimStyleSuffix

  

DimStyleLinearPrecision

    
    
    DimStyleLinearPrecision(dimstyle, precision=None)

Returns or changes the linear display precision of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    precision (number, optional): the new linear precision value

##### Returns:

    
    
    number: if precision is not specified, the current linear precision value
    number: if precision is specified, the previous linear precision value
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    precision = rs.DimStyleLinearPrecision(dimstyle)
    if precision>2: rs.DimStyleLinearPrecision( dimstyle, 2 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleNames

    
    
    DimStyleNames(sort=False)

Returns the names of all dimension styles in the document

##### Parameters:

    
    
    sort (bool): sort the list if True, not sorting is the default (False)

##### Returns:

    
    
    list(str, ...): the names of all dimension styles in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyles = rs.DimStyleNames()
    if dimstyles:
        for dimstyle in dimstyles: print(dimstyle)

##### See Also:

  * DimStyleCount
  * IsDimStyle

  

DimStyleNumberFormat

    
    
    DimStyleNumberFormat(dimstyle, format=None)

Returns or changes the number display format of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    format (number, optional) the new number format
       0 = Decimal
       1 = Fractional
       2 = Feet and inches

##### Returns:

    
    
    number: if format is not specified, the current display format
    number: if format is specified, the previous display format
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    format = rs.DimStyleNumberFormat(dimstyle)
    if format>0: rs.DimStyleNumberFormat( dimstyle, 0 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleOffset

    
    
    DimStyleOffset(dimstyle, offset=None)

Returns or changes the extension line offset of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    offset (number, optional): the new extension line offset

##### Returns:

    
    
    number: if offset is not specified, the current extension line offset
    number: if offset is specified, the previous extension line offset
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    offset = rs.DimStyleOffset(dimstyle)
    if offset>0.5: rs.DimStyleOffset( dimstyle, 0.5 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStylePrefix

    
    
    DimStylePrefix(dimstyle, prefix=None)

Returns or changes the prefix of a dimension style - the text to prefix to the
dimension text.

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimstyle
    prefix (str, optional): the new prefix

##### Returns:

    
    
    str: if prefix is not specified, the current prefix
    str: if prefix is specified, the previous prefix
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    rs.DimStylePrefix( dimstyle, "[" )

##### See Also:

  * DimStyleLengthFactor
  * DimStyleSuffix

  

DimStyleScale

    
    
    DimStyleScale(dimstyle, scale=None)

Returns or modifies the scale of a dimension style.

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimstyle
    scale (number, optional): the new scale value

##### Returns:

    
    
    number: if scale is not specified, the current scale
    number: if scale is specified, the previous scale
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    dimstyle = doc.DimStyles.Current
    scale = rs.DimStyleScale(dimstyle)
    rs.DimStyleScale(dimstyle, scale*2.0)

##### See Also:

  * DimStyleTextHeight
  * DimStyleOffset

  

DimStyleSuffix

    
    
    DimStyleSuffix(dimstyle, suffix=None)

Returns or changes the suffix of a dimension style - the text to append to the
dimension text.

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimstyle
    suffix (str, optional): the new suffix

##### Returns:

    
    
    str: if suffix is not specified, the current suffix
    str: if suffix is specified, the previous suffix
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    rs.DimStyleSuffix( dimstyle, "}" )

##### See Also:

  * DimStyleLengthFactor
  * DimStylePrefix

  

DimStyleTextAlignment

    
    
    DimStyleTextAlignment(dimstyle, alignment=None)

Returns or changes the text alignment mode of a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    alignment (number, optional): the new text alignment
        0 = Normal (same as 2)
        1 = Horizontal to view
        2 = Above the dimension line
        3 = In the dimension line

##### Returns:

    
    
    number: if alignment is not specified, the current text alignment
    number: if alignment is specified, the previous text alignment
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    alignment = rs.DimStyleTextAlignment(dimstyle)
    if alignment!=2: rs.DimStyleTextAlignment( dimstyle, 2 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextHeight

  

DimStyleTextGap

    
    
    DimStyleTextGap(dimstyle, gap=None)

Returns or changes the text gap used by a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    gap (number, optional): the new text gap

##### Returns:

    
    
    number: if gap is not specified, the current text gap
    number: if gap is specified, the previous text gap
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    gap = rs.DimStyleTextGap(dimstyle)
    if gap>0.25: rs.DimStyleTextGap( dimstyle, 0.25 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment
  * DimStyleTextHeight

  

DimStyleTextHeight

    
    
    DimStyleTextHeight(dimstyle, height=None)

Returns or changes the text height used by a dimension style

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style
    height (number, optional): the new text height

##### Returns:

    
    
    number: if height is not specified, the current text height
    number: if height is specified, the previous text height
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.CurrentDimStyle()
    height = rs.DimStyleTextHeight(dimstyle)
    if offset>1.0: rs.DimStyleTextHeight( dimstyle, 1.0 )

##### See Also:

  * DimStyleAnglePrecision
  * DimStyleArrowSize
  * DimStyleExtension
  * DimStyleFont
  * DimStyleLinearPrecision
  * DimStyleNumberFormat
  * DimStyleOffset
  * DimStyleTextAlignment

  

IsAlignedDimension

    
    
    IsAlignedDimension(object_id)

Verifies an object is an aligned dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.  None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsAlignedDimension(obj):
        print("The object is an aligned dimension.")
    else:
        print("The object is not an aligned dimension.")

##### See Also:

  * IsAngularDimension
  * IsDiameterDimension
  * IsDimension
  * IsLinearDimension
  * IsOrdinateDimension
  * IsRadialDimension

  

IsAngularDimension

    
    
    IsAngularDimension(object_id)

Verifies an object is an angular dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsAngularDimension(obj):
        print("The object is an angular dimension.")
    else:
        print("The object is not an angular dimension.")

##### See Also:

  * IsAlignedDimension
  * IsDiameterDimension
  * IsDimension
  * IsLinearDimension
  * IsOrdinateDimension
  * IsRadialDimension

  

IsDiameterDimension

    
    
    IsDiameterDimension(object_id)

Verifies an object is a diameter dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsDiameterDimension(obj):
        print("The object is a diameter dimension.")
    else:
        print("The object is not a diameter dimension.")

##### See Also:

  * IsAlignedDimension
  * IsAngularDimension
  * IsDimension
  * IsLinearDimension
  * IsOrdinateDimension
  * IsRadialDimension

  

IsDimension

    
    
    IsDimension(object_id)

Verifies an object is a dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsDimension(obj):
        print("The object is a dimension.")
    else:
        print("The object is not a dimension.")

##### See Also:

  * IsAlignedDimension
  * IsAngularDimension
  * IsDiameterDimension
  * IsLinearDimension
  * IsOrdinateDimension
  * IsRadialDimension

  

IsDimStyle

    
    
    IsDimStyle(dimstyle)

Verifies the existance of a dimension style in the document

##### Parameters:

    
    
    dimstyle (str): the name of a dimstyle to test for

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.GetString("Dimension style to test")
    if rs.IsDimStyle(dimstyle):
        if rs.IsDimStyleReference(dimstyle):
            print("The dimension style is from a reference file.")
        else:
            print("The dimension style is not from a reference file.")
    else:
        print("The dimension style does not exist.")

##### See Also:

  * IsDimStyleReference

  

IsDimStyleReference

    
    
    IsDimStyleReference(dimstyle)

Verifies that an existing dimension style is from a reference file

##### Parameters:

    
    
    dimstyle (str): the name of an existing dimension style

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    dimstyle = rs.GetString("Dimension style to test")
    if rs.IsDimStyle(dimstyle):
        if rs.IsDimStyleReference(dimstyle):
            print("The dimension style is from a reference file.")
        else:
            print("The dimension style is not from a reference file.")
    else:
        print("The dimension style does not exist.")

##### See Also:

  * IsDimStyle

  

IsLeader

    
    
    IsLeader(object_id)

Verifies an object is a dimension leader object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a leader")
    if rs.IsLeader(obj):
        print("The object is a leader.")
    else:
        print("The object is not a leader.")

##### See Also:

  * AddLeader
  * LeaderText

  

IsLinearDimension

    
    
    IsLinearDimension(object_id)

Verifies an object is a linear dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsLinearDimension(obj):
        print("The object is a linear dimension.")
    else:
        print("The object is not a linear dimension.")

##### See Also:

  * IsAlignedDimension
  * IsAngularDimension
  * IsDiameterDimension
  * IsDimension
  * IsOrdinateDimension
  * IsRadialDimension

  

IsOrdinateDimension

    
    
    IsOrdinateDimension(object_id)

Verifies an object is an ordinate dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsOrdinateDimension(obj):
        print("The object is an ordinate dimension.")
    else:
        print("The object is not an ordinate dimension.")

##### See Also:

  * IsAlignedDimension
  * IsAngularDimension
  * IsDiameterDimension
  * IsDimension
  * IsLinearDimension
  * IsRadialDimension

  

IsRadialDimension

    
    
    IsRadialDimension(object_id)

Verifies an object is a radial dimension object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True or False.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a dimension")
    if rs.IsRadialDimension(obj):
        print("The object is a radial dimension.")
    else:
        print("The object is not a radial dimension.")

##### See Also:

  * IsAlignedDimension
  * IsAngularDimension
  * IsDiameterDimension
  * IsDimension
  * IsLinearDimension
  * IsOrdinateDimension

  

LeaderText

    
    
    LeaderText(object_id, text=None)

Returns or modifies the text string of a dimension leader object

##### Parameters:

    
    
    object_id (guid): the object's identifier
    text (string, optional): the new text string

##### Returns:

    
    
    str: if text is not specified, the current text string
    str: if text is specified, the previous text string
    None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a leader")
    if rs.IsLeader(obj): print(rs.LeaderText(obj))

##### See Also:

  * AddLeader
  * IsLeader

  

RenameDimStyle

    
    
    RenameDimStyle(oldstyle, newstyle)

Renames an existing dimension style

##### Parameters:

    
    
    oldstyle (str): the name of an existing dimension style
    newstyle (str): the new dimension style name

##### Returns:

    
    
    str: the new dimension style name if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    oldstyle = rs.GetString("Old dimension style name")
    if oldstyle:
        newstyle = rs.GetString("New dimension style name")
        if newstyle: rs.RenameDimStyle( oldstyle, newstyle )

##### See Also:

  * AddDimStyle
  * CurrentDimStyle
  * DeleteDimStyle
  * IsDimStyle

  

## document

CreatePreviewImage

    
    
    CreatePreviewImage(filename, view=None, size=None, flags=0, wireframe=False)

Create a bitmap preview image of the current model

##### Parameters:

    
    
    filename (str): name of the bitmap file to create
    view (str, optional): title of the view. If omitted, the active view is used
    size (number, optional): two integers that specify width and height of the bitmap
    flags (number, optional): Bitmap creation flags. Can be the combination of:
        1 = honor object highlighting
        2 = draw construction plane
        4 = use ghosted shading
    wireframe (bool, optional): If True then a wireframe preview image. If False,
        a rendered image will be created

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    result = rs.CreatePreviewImage("test.jpg")
    if result:
        print( "test.jpg created successfully.")
    else:
        print( "Unable to create preview image.")

##### See Also:

  * ExtractPreviewImage

  

DocumentModified

    
    
    DocumentModified(modified=None)

Returns or sets the document's modified flag. This flag indicates whether or
not any changes to the current document have been made. NOTE: setting the
document modified flag to False will prevent the "Do you want to save this
file..." from displaying when you close Rhino.

##### Parameters:

    
    
    modified (bool): the modified state, either True or False

##### Returns:

    
    
    bool: if no modified state is specified, the current modified state
    bool: if a modified state is specified, the previous modified state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    modified = rs.IsDocumentModified()
    if not modified: rs.DocumentModified(True)

##### See Also:

  * IsDocumentModified

  

DocumentName

    
    
    DocumentName()

Returns the name of the currently loaded Rhino document (3DM file)

##### Returns:

    
    
    str: the name of the currently loaded Rhino document (3DM file)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = rs.DocumentName()
    print(name)

##### See Also:

  * DocumentPath

  

DocumentPath

    
    
    DocumentPath()

Returns path of the currently loaded Rhino document (3DM file)

##### Returns:

    
    
    str: the path of the currently loaded Rhino document (3DM file)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    path = rs.DocumentPath()
    print(path)

##### See Also:

  * DocumentName

  

EnableRedraw

    
    
    EnableRedraw(enable=True)

Enables or disables screen redrawing

##### Parameters:

    
    
    enable (bool, optional): True to enable, False to disable

##### Returns:

    
    
    bool: previous screen redrawing state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    redraw = rs.EnableRedraw(True)

##### See Also:

  * Redraw

  

ExtractPreviewImage

    
    
    ExtractPreviewImage(filename, modelname=None)

Extracts the bitmap preview image from the specified model (.3dm)

##### Parameters:

    
    
    filename (str): name of the bitmap file to create. The extension of
       the filename controls the format of the bitmap file created.
       (.bmp, .tga, .jpg, .jpeg, .pcx, .png, .tif, .tiff)
    modelname (str, optional): The model (.3dm) from which to extract the
       preview image. If omitted, the currently loaded model is used.

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    result = rs.ExtractPreviewImage("test.jpg")
    if result:
        print("Test.jpg created successfully.")
    else:
        print("Unable to extract preview image.")

##### See Also:

  * CreatePreviewImage

  

IsDocumentModified

    
    
    IsDocumentModified()

Verifies that the current document has been modified in some way

##### Returns:

    
    
    bool: True or False. None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    modified = rs.IsDocumentModified()
    if not modified: rs.DocumentModified(True)

##### See Also:

  * DocumentModified

  

Notes

    
    
    Notes(newnotes=None)

Returns or sets the document's notes. Notes are generally created using
Rhino's Notes command

##### Parameters:

    
    
    newnotes (str): new notes to set

##### Returns:

    
    
    str: if `newnotes` is omitted, the current notes if successful
    str: if `newnotes` is specified, the previous notes if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    notes = rs.Notes()
    if notes: rs.MessageBox(notes)

  

ReadFileVersion

    
    
    ReadFileVersion()

Returns the file version of the current document. Use this function to
determine which version of Rhino last saved the document. Note, this function
will not return values from referenced or merged files.

##### Returns:

    
    
    str: the file version of the current document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("ReadFileVersion = {}".format(rs.ReadFileVersion()))

##### See Also:

  * DocumentName
  * DocumentPath

  

Redraw

    
    
    Redraw()

Redraws all views

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Redraw()

##### See Also:

  * EnableRedraw

  

RenderAntialias

    
    
    RenderAntialias(style=None)

Returns or sets render antialiasing style

##### Parameters:

    
    
    style (number, optional): level of antialiasing (0=none, 1=normal, 2=best)

##### Returns:

    
    
    number: if style is not specified, the current antialiasing style
    number: if style is specified, the previous antialiasing style

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.RenderAntialias(1)

##### See Also:

  * RenderColor
  * RenderResolution
  * RenderSettings

  

RenderColor

    
    
    RenderColor(item, color=None)

Returns or sets the render ambient light or background color

##### Parameters:

    
    
    item (number): 0=ambient light color, 1=background color
    color (color, optional): the new color value. If omitted, the current item color is returned

##### Returns:

    
    
    color: if color is not specified, the current item color
    color: if color is specified, the previous item color

##### Example:

    
    
    import rhinoscriptsyntax as rs
    render_background_color = 1
    rs.RenderColor( render_background_color, (0,0,255) )

##### See Also:

  * RenderAntialias
  * RenderResolution
  * RenderSettings

  

RenderResolution

    
    
    RenderResolution(resolution=None)

Returns or sets the render resolution

##### Parameters:

    
    
    resolution ([number, number], optional): width and height of render

##### Returns:

    
    
    tuple(number, number): if resolution is not specified, the current resolution width,height
    tuple(number, number): if resolution is specified, the previous resolution width, height

##### Example:

    
    
    import rhinoscriptsyntax as rs
    sizex, sizey = rs.Viewsize()
    resolution = sizex/2 , sizey/2
    rs.RenderResolution( resolution )

##### See Also:

  * RenderAntialias
  * RenderColor
  * RenderSettings

  

RenderMeshDensity

    
    
    RenderMeshDensity(density=None)

Returns or sets the render mesh density property of the active document. For
more information on render meshes, see the Document Properties: Mesh topic in
the Rhino help file.

##### Parameters:

    
    
    density (number, optional): the new render mesh density, which is a number between 0.0 and 1.0.

##### Returns:

    
    
    number: if density is not specified, the current render mesh density if successful.
    number: if density is specified, the previous render mesh density if successful.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshMaxAngle

    
    
    RenderMeshMaxAngle(angle_degrees=None)

Returns or sets the render mesh maximum angle property of the active document.
For more information on render meshes, see the Document Properties: Mesh topic
in the Rhino help file.

##### Parameters:

    
    
    angle_degrees (number, optional): the new maximum angle, which is a positive number in degrees.

##### Returns:

    
    
    number: if angle_degrees is not specified, the current maximum angle if successful.
    number: if angle_degrees is specified, the previous maximum angle if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshMaxAspectRatio

    
    
    RenderMeshMaxAspectRatio(ratio=None)

Returns or sets the render mesh maximum aspect ratio property of the active
document. For more information on render meshes, see the Document Properties:
Mesh topic in the Rhino help file.

##### Parameters:

    
    
    ratio (number, optional): the render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.

##### Returns:

    
    
    number: if ratio is not specified, the current render mesh maximum aspect ratio if successful.
    number: if ratio is specified, the previous render mesh maximum aspect ratio if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshMaxDistEdgeToSrf

    
    
    RenderMeshMaxDistEdgeToSrf(distance=None)

Returns or sets the render mesh maximum distance, edge to surface parameter of
the active document. For more information on render meshes, see the Document
Properties: Mesh topic in the Rhino help file.

##### Parameters:

    
    
    distance (number, optional): the render mesh maximum distance, edge to surface.

##### Returns:

    
    
    number: if distance is not specified, the current render mesh maximum distance, edge to surface if successful.
    number: if distance is specified, the previous render mesh maximum distance, edge to surface if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshMaxEdgeLength

    
    
    RenderMeshMaxEdgeLength(distance=None)

Returns or sets the render mesh maximum edge length parameter of the active
document. For more information on render meshes, see the Document Properties:
Mesh topic in the Rhino help file.

##### Parameters:

    
    
    distance (number, optional): the render mesh maximum edge length.

##### Returns:

    
    
    number: if distance is not specified, the current render mesh maximum edge length if successful.
    number: if distance is specified, the previous render mesh maximum edge length if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshMinEdgeLength

    
    
    RenderMeshMinEdgeLength(distance=None)

Returns or sets the render mesh minimum edge length parameter of the active
document. For more information on render meshes, see the Document Properties:
Mesh topic in the Rhino help file.

##### Parameters:

    
    
    distance (number, optional): the render mesh minimum edge length.

##### Returns:

    
    
    number: if distance is not specified, the current render mesh minimum edge length if successful.
    number: if distance is specified, the previous render mesh minimum edge length if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshMinInitialGridQuads

    
    
    RenderMeshMinInitialGridQuads(quads=None)

Returns or sets the render mesh minimum initial grid quads parameter of the
active document. For more information on render meshes, see the Document
Properties: Mesh topic in the Rhino help file.

##### Parameters:

    
    
    quads (number, optional): the render mesh minimum initial grid quads. The suggested range is from 0 to 10000.

##### Returns:

    
    
    number: if quads is not specified, the current render mesh minimum initial grid quads if successful.
    number: if quads is specified, the previous render mesh minimum initial grid quads if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshQuality

    
    
    RenderMeshQuality(quality=None)

Returns or sets the render mesh quality of the active document. For more
information on render meshes, see the Document Properties: Mesh topic in the
Rhino help file.

##### Parameters:

    
    
    quality (number, optional): the render mesh quality, either:
      0: Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
      1: Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
      2: Custom.

##### Returns:

    
    
    number: if quality is not specified, the current render mesh quality if successful.
    number: if quality is specified, the previous render mesh quality if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderMeshSettings

    
    
    RenderMeshSettings(settings=None)

Returns or sets the render mesh settings of the active document. For more
information on render meshes, see the Document Properties: Mesh topic in the
Rhino help file.

##### Parameters:

    
    
    settings (number, optional): the render mesh settings, which is a bit-coded number that allows or disallows certain features.
    The bits can be added together in any combination to form a value between 0 and 7.  The bit values are as follows:
      0: No settings enabled.
      1: Refine mesh enabled.
      2: Jagged seams enabled.
      4: Simple planes enabled.
      8: Texture is packed, scaled and normalized; otherwise unpacked, unscaled and normalized.

##### Returns:

    
    
    number: if settings is not specified, the current render mesh settings if successful.
    number: if settings is specified, the previous render mesh settings if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print("Quality: %s" % rs.RenderMeshQuality())
    print("Mesh density: %s" % rs.RenderMeshDensity())
    print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
    print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
    print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
    print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
    print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
    print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
    print("Other settings: %s" % rs.RenderMeshSettings())

##### See Also:

  * RenderMeshDensity
  * RenderMeshMaxAngle
  * RenderMeshMaxAspectRatio
  * RenderMeshMaxDistEdgeToSrf
  * RenderMeshMaxEdgeLength
  * RenderMeshMinEdgeLength
  * RenderMeshMinInitialGridQuads
  * RenderMeshQuality
  * RenderMeshSettings

  

RenderSettings

    
    
    RenderSettings(settings=None)

Returns or sets render settings

##### Parameters:

    
    
    settings (number, optional): bit-coded flags of render settings to modify.
      0=none,
      1=create shadows,
      2=use lights on layers that are off,
      4=render curves and isocurves,
      8=render dimensions and text

##### Returns:

    
    
    number: if settings are not specified, the current render settings in bit-coded flags
    number: if settings are specified, the previous render settings in bit-coded flags

##### Example:

    
    
    import rhinoscriptsyntax as rs
    render_annotations = 8
    settings = rs.RenderSettings()
    if settings & render_annotations:
        settings = settings - render_annotations
        rs.RenderSettings( settings )

##### See Also:

  * RenderAntialias
  * RenderColor
  * RenderResolution

  

UnitAbsoluteTolerance

    
    
    UnitAbsoluteTolerance(tolerance=None, in_model_units=True)

Resturns or sets the document's absolute tolerance. Absolute tolerance is
measured in drawing units. See Rhino's document properties command (Units and
Page Units Window) for details

##### Parameters:

    
    
    tolerance (number, optional): the absolute tolerance to set
    in_model_units (bool, optional): Return or modify the document's model units (True)
                          or the document's page units (False)

##### Returns:

    
    
    number: if tolerance is not specified, the current absolute tolerance
    number: if tolerance is specified, the previous absolute tolerance

##### Example:

    
    
    import rhinoscriptsyntax as rs
    tol = rs.UnitAbsoluteTolerance()
    if tol<0.01:
        rs.UnitAbsoluteTolerance( 0.01 )

##### See Also:

  * UnitAngleTolerance
  * UnitDistanceDisplayPrecision
  * UnitRelativeTolerance
  * UnitSystem

  

UnitAngleTolerance

    
    
    UnitAngleTolerance(angle_tolerance_degrees=None, in_model_units=True)

Return or set the document's angle tolerance. Angle tolerance is measured in
degrees. See Rhino's DocumentProperties command (Units and Page Units Window)
for details

##### Parameters:

    
    
    angle_tolerance_degrees (number, optional): the angle tolerance to set
    in_model_units (number, optional): Return or modify the document's model units (True)
                           or the document's page units (False)

##### Returns:

    
    
    number: if angle_tolerance_degrees is not specified, the current angle tolerance
    number: if angle_tolerance_degrees is specified, the previous angle tolerance

##### Example:

    
    
    import rhinoscriptsyntax as rs
    tol = rs.UnitAngleTolerance()
    if tol<3.0:
        rs.UnitAngleTolerance(3.0)

##### See Also:

  * UnitAbsoluteTolerance
  * UnitDistanceDisplayPrecision
  * UnitRelativeTolerance
  * UnitSystem

  

UnitDistanceDisplayPrecision

    
    
    UnitDistanceDisplayPrecision(precision=None, model_units=True)

Return or set the document's distance display precision

##### Parameters:

    
    
    precision (number, optional): The distance display precision.  If the current distance display mode is Decimal, then precision is the number of decimal places.
                                  If the current distance display mode is Fractional (including Feet and Inches), then the denominator = (1/2)^precision.
                                  Use UnitDistanceDisplayMode to get the current distance display mode.
    model_units (bool, optional): Return or modify the document's model units (True) or the document's page units (False). The default is True.

##### Returns:

    
    
    number: If precision is not specified, the current distance display precision if successful. If precision is specified, the previous distance display precision if successful. If not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    precision = 3
    rs.UnitDistanceDisplayPrecision( precision )

##### See Also:

  * UnitAbsoluteTolerance
  * UnitAngleTolerance
  * UnitRelativeTolerance
  * UnitSystem

  

UnitRelativeTolerance

    
    
    UnitRelativeTolerance(relative_tolerance=None, in_model_units=True)

Return or set the document's relative tolerance. Relative tolerance is
measured in percent. See Rhino's DocumentProperties command (Units and Page
Units Window) for details

##### Parameters:

    
    
    relative_tolerance (number, optional) the relative tolerance in percent
    in_model_units (bool, optional): Return or modify the document's model units (True)
                           or the document's page units (False)

##### Returns:

    
    
    number: if relative_tolerance is not specified, the current tolerance in percent
    number: if relative_tolerance is specified, the previous tolerance in percent

##### Example:

    
    
    import rhinoscriptsyntax as rs
    tol = rs.UnitRelativeTolerance()
    if tol<1.0:
        rs.UnitRelativeTolerance(1.0)

##### See Also:

  * UnitAbsoluteTolerance
  * UnitAngleTolerance
  * UnitDistanceDisplayPrecision
  * UnitSystem

  

UnitScale

    
    
    UnitScale(to_system, from_system=None)

Return the scale factor for changing between unit systems.

##### Parameters:

    
    
    to_system (number): The unit system to convert to. The unit systems are are:
       0 - No unit system
       1 - Microns (1.0e-6 meters)
       2 - Millimeters (1.0e-3 meters)
       3 - Centimeters (1.0e-2 meters)
       4 - Meters
       5 - Kilometers (1.0e+3 meters)
       6 - Microinches (2.54e-8 meters, 1.0e-6 inches)
       7 - Mils (2.54e-5 meters, 0.001 inches)
       8 - Inches (0.0254 meters)
       9 - Feet (0.3408 meters, 12 inches)
      10 - Miles (1609.344 meters, 5280 feet)
      11 - *Reserved for custom Unit System*
      12 - Angstroms (1.0e-10 meters)
      13 - Nanometers (1.0e-9 meters)
      14 - Decimeters (1.0e-1 meters)
      15 - Dekameters (1.0e+1 meters)
      16 - Hectometers (1.0e+2 meters)
      17 - Megameters (1.0e+6 meters)
      18 - Gigameters (1.0e+9 meters)
      19 - Yards (0.9144  meters, 36 inches)
      20 - Printer point (1/72 inches, computer points)
      21 - Printer pica (1/6 inches, (computer picas)
      22 - Nautical mile (1852 meters)
      23 - Astronomical (1.4959787e+11)
      24 - Lightyears (9.46073e+15 meters)
      25 - Parsecs (3.08567758e+16)
    from_system (number, optional): the unit system to convert from (see above). If omitted,
        the document's current unit system is used

##### Returns:

    
    
    number: scale factor for changing between unit systems

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.UnitScale(3, 4)) # 100.0
    print(rs.UnitScale(3, 8)) # 2.54
    print(rs.UnitScale(8, 9)) # 12.0

##### See Also:

  * UnitSystem
  * UnitSystemName

  

UnitSystem

    
    
    UnitSystem(unit_system=None, scale=False, in_model_units=True)

Return or set the document's unit system. See Rhino's DocumentProperties
command (Units and Page Units Window) for details

##### Parameters:

    
    
    unit_system (number, optional): The unit system to set the document to. The unit systems are:
       0 - No unit system
       1 - Microns (1.0e-6 meters)
       2 - Millimeters (1.0e-3 meters)
       3 - Centimeters (1.0e-2 meters)
       4 - Meters
       5 - Kilometers (1.0e+3 meters)
       6 - Microinches (2.54e-8 meters, 1.0e-6 inches)
       7 - Mils (2.54e-5 meters, 0.001 inches)
       8 - Inches (0.0254 meters)
       9 - Feet (0.3048 meters, 12 inches)
      10 - Miles (1609.344 meters, 5280 feet)
      11 - *Reserved for custom Unit System*
      12 - Angstroms (1.0e-10 meters)
      13 - Nanometers (1.0e-9 meters)
      14 - Decimeters (1.0e-1 meters)
      15 - Dekameters (1.0e+1 meters)
      16 - Hectometers (1.0e+2 meters)
      17 - Megameters (1.0e+6 meters)
      18 - Gigameters (1.0e+9 meters)
      19 - Yards (0.9144  meters, 36 inches)
      20 - Printer point (1/72 inches, computer points)
      21 - Printer pica (1/6 inches, (computer picas)
      22 - Nautical mile (1852 meters)
      23 - Astronomical (1.4959787e+11)
      24 - Lightyears (9.46073e+15 meters)
      25 - Parsecs (3.08567758e+16)
    scale (bool, optional): Scale existing geometry based on the new unit system.
        If not specified, any existing geometry is not scaled (False)
    in_model_units (number, optional): Return or modify the document's model units (True)
        or the document's page units (False). The default is True.

##### Returns:

    
    
    number: if unit_system is not specified, the current unit system
    number: if unit_system is specified, the previous unit system
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rhUnitMillimeters = 2
    rhUnitInches = 8
    current_system = rs.UnitSystem()
    if current_system==rhUnitMillimeters:
        rs.UnitSystem(rhUnitInches, True)

##### See Also:

  * UnitAbsoluteTolerance
  * UnitAngleTolerance
  * UnitDistanceDisplayPrecision
  * UnitRelativeTolerance

  

UnitSystemName

    
    
    UnitSystemName(capitalize=False, singular=True, abbreviate=False, model_units=True)

Returns the name of the current unit system

##### Parameters:

    
    
    capitalize (bool, optional): Capitalize the first character of the units system name (e.g. return "Millimeter" instead of "millimeter"). The default is not to capitalize the first character (false).
    singular (bool, optional): Return the singular form of the units system name (e.g. "millimeter" instead of "millimeters"). The default is to return the singular form of the name (true).
    abbreviate (bool, optional): Abbreviate the name of the units system (e.g. return "mm" instead of "millimeter"). The default is not to abbreviate the name (false).
    model_units (bool, optional): Return the document's model units (True) or the document's page units (False). The default is True.

##### Returns:

    
    
    str: The name of the current units system if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    system = rs.UnitSystemName(False, False, False)
    print("The units system is set to{}".format(system))

##### See Also:

  * UnitSystem

  

## geometry

AddClippingPlane

    
    
    AddClippingPlane(plane, u_magnitude, v_magnitude, views=None)

Create a clipping plane for visibly clipping away geometry in a specific view.
Note, clipping planes are infinite

##### Parameters:

    
    
    plane (plane): the plane
    u_magnitude, v_magnitude (number): size of the plane
    views ([str|guid, ...]): Titles or ids the the view(s) to clip. If omitted, the active
      view is used.

##### Returns:

    
    
    guid: object identifier on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddClippingPlane( rs.WorldXYPlane(), 5.0, 3.0 )

##### See Also:

  * IsClippingPlane

  

AddPictureFrame

    
    
    AddPictureFrame(plane, filename, width=0.0, height=0.0, self_illumination=True, embed=False, use_alpha=False, make_mesh=False)

Creates a picture frame and adds it to the document.

##### Parameters:

    
    
    plane (plane): The plane in which the PictureFrame will be created.  The bottom-left corner of picture will be at plane's origin. The width will be in the plane's X axis direction, and the height will be in the plane's Y axis direction.
    filename (str): The path to a bitmap or image file.
    width (number, optional): If both dblWidth and dblHeight = 0, then the width and height of the PictureFrame will be the width and height of the image. If dblWidth = 0 and dblHeight is > 0, or if dblWidth > 0 and dblHeight = 0, then the non-zero value is assumed to be an aspect ratio of the image's width or height, which ever one is = 0. If both dblWidth and dblHeight are > 0, then these are assumed to be the width and height of in the current unit system.
    height (number, optional):  If both dblWidth and dblHeight = 0, then the width and height of the PictureFrame will be the width and height of the image. If dblWidth = 0 and dblHeight is > 0, or if dblWidth > 0 and dblHeight = 0, then the non-zero value is assumed to be an aspect ratio of the image's width or height, which ever one is = 0. If both dblWidth and dblHeight are > 0, then these are assumed to be the width and height of in the current unit system.
    self_illumination (bool, optional): If True, then the image mapped to the picture frame plane always displays at full intensity and is not affected by light or shadow.
    embed (bool, optional): If True, then the function adds the image to Rhino's internal bitmap table, thus making the document self-contained.
    use_alpha (bool, optional): If False, the picture frame is created without any transparency texture.  If True, a transparency texture is created with a "mask texture" set to alpha, and an instance of the diffuse texture in the source texture slot.
    make_mesh (bool, optional): If True, the function will make a PictureFrame object from a mesh rather than a plane surface.

##### Returns:

    
    
    guid: object identifier on success
    None: on failure

  

AddPoint

    
    
    AddPoint(point, y=None, z=None)

Adds point object to the document.

##### Parameters:

    
    
    point (point): a point3d or list(x,y,z) location of point to add

##### Returns:

    
    
    guid: identifier for the object that was added to the doc

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddPoint( (1,2,3) )

##### See Also:

  * IsPoint
  * PointCoordinates

  

AddPointCloud

    
    
    AddPointCloud(points, colors=None)

Adds point cloud object to the document

##### Parameters:

    
    
    points ([point, ....]): list of values where every multiple of three represents a point
    colors ([color, ...]): list of colors to apply to each point

##### Returns:

    
    
    guid: identifier of point cloud on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = (0,0,0), (1,1,1), (2,2,2), (3,3,3)
    rs.AddPointCloud(points)

##### See Also:

  * IsPointCloud
  * PointCloudCount
  * PointCloudPoints

  

AddPoints

    
    
    AddPoints(points)

Adds one or more point objects to the document

##### Parameters:

    
    
    points ([point, ...]): list of points

##### Returns:

    
    
    list(guid, ...): identifiers of the new objects on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(True, True, "Select points")
    if points: rs.AddPoints(points)

##### See Also:

  * AddPoint
  * AddPointCloud

  

AddText

    
    
    AddText(text, point_or_plane, height=1.0, font=None, font_style=0, justification=None)

Adds a text string to the document

##### Parameters:

    
    
    text (str): the text to display
    point_or_plane (point|plane): a 3-D point or the plane on which the text will lie.
        The origin of the plane will be the origin point of the text
    height (number, optional): the text height
    font (str, optional): the text font
    font_style (number, optional): any of the following flags
       0 = normal
       1 = bold
       2 = italic
       3 = bold and italic
    justification (number, optional): text justification. Values may be added to create combinations.
       1 = Left
       2 = Center (horizontal)
       4 = Right
       65536 = Bottom
       131072 = Middle (vertical)
       262144 = Top

##### Returns:

    
    
    guid: identifier for the object that was added to the doc on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.GetPoint("Pick point")
    if point: rs.AddText("Hello Rhino!", point)

##### See Also:

  * IsText

  

AddTextDot

    
    
    AddTextDot(text, point)

Add a text dot to the document.

##### Parameters:

    
    
    text (str): string in dot
    point (point): A 3D point identifying the origin point.

##### Returns:

    
    
    guid: The identifier of the new object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddTextDot("howdy",(1,2,3))

##### See Also:

  * IsTextDot

  

Area

    
    
    Area(object_id)

Compute the area of a closed curve, hatch, surface, polysurface, or mesh

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    number: area if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    a = rs.Area('a9e34aa8-226c-4e17-9e11-b74bf2cf581b')

##### See Also:

  * IsPoint
  * PointCoordinates

  

BoundingBox

    
    
    BoundingBox(objects, view_or_plane=None, in_world_coords=True)

Returns either world axis-aligned or a construction plane axis-aligned
bounding box of an object or of several objects

##### Parameters:

    
    
    objects ([guid, ...]): The identifiers of the objects
    view_or_plane (str|guid): Title or id of the view that contains the
        construction plane to which the bounding box should be aligned -or-
        user defined plane. If omitted, a world axis-aligned bounding box
        will be calculated
    in_world_coords (bool, optional): return the bounding box as world coordinates or
        construction plane coordinates. Note, this option does not apply to
        world axis-aligned bounding boxes.

##### Returns:

    
    
    list(point, point, point, point, point, point, point, point): Eight 3D points that define the bounding box.
         Points returned in counter-clockwise order starting with the bottom rectangle of the box.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select object")
    if object:
        box = rs.BoundingBox(object)
        if box:
            for i, point in enumerate(box):
                rs.AddTextDot( i, point )

  

CompareGeometry

    
    
    CompareGeometry(first, second)

Compares two objects to determine if they are geometrically identical.

##### Parameters:

    
    
    first (guid|geometry): The identifier of the first object to compare.
    second (guid|geometry): The identifier of the second object to compare.

##### Returns:

    
    
    True if the objects are geometrically identical, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object1 = rs.GetObject("Select first object")
    object2 = rs.GetObject("Select second object")
    if object:
    print("Objects are identical" if rs.CompareGeometry(object1, object2) else "Objects differ")

  

ExplodeText

    
    
    ExplodeText(text_id, delete=False)

Creates outline curves for a given text entity

##### Parameters:

    
    
    text_id (guid): identifier of Text object to explode
    delete (bool, optional): delete the text object after the curves have been created

##### Returns:

    
    
    list(guid): of outline curves

##### Example:

    
    
    import rhinoscriptsyntax as rs
    text = rs.AddText("abcd", rs.WorldXYPlane())
    rs.ExplodeText(text, True)

##### See Also:

  * IsHatch
  * HatchPattern
  * HatchRotation
  * HatchScale

  

IsClippingPlane

    
    
    IsClippingPlane(object_id)

Verifies that an object is a clipping plane object

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if the object with a given id is a clipping plane

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a clipping plane")
    if rs.IsClippingPlane(id):
        print("The object is a clipping plane.")
    else:
        print("The object is not a clipping plane.")

##### See Also:

  * AddClippingPlane

  

IsPoint

    
    
    IsPoint(object_id)

Verifies an object is a point object.

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if the object with a given id is a point

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a point")
    if rs.IsPoint(id):
        print("The object is a point.")
    else:
        print("The object is not a point.")

##### See Also:

  * AddPoint
  * PointCoordinates

  

IsPointCloud

    
    
    IsPointCloud(object_id)

Verifies an object is a point cloud object.

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if the object with a given id is a point cloud

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a point cloud")
    if rs.IsPointCloud(id):
        print("The object is a point cloud.")
    else:
        print("The object is not a point cloud.")

##### See Also:

  * AddPointCloud
  * PointCloudCount
  * PointCloudPoints

  

IsText

    
    
    IsText(object_id)

Verifies an object is a text object.

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if the object with a given id is a text object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a text object")
    if rs.IsText(id):
        print("The object is a text object.")
    else:
        print("The object is not a text object.")

##### See Also:

  * AddText

  

IsTextDot

    
    
    IsTextDot(object_id)

Verifies an object is a text dot object.

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if the object with a given id is a text dot object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a text dot object")
    if rs.IsTextDot(id):
        print("The object is a text dot object.")
    else:
        print("The object is not a text dot object.")

##### See Also:

  * AddTextDot

  

PointCloudCount

    
    
    PointCloudCount(object_id)

Returns the point count of a point cloud object

##### Parameters:

    
    
    object_id (guid): the point cloud object's identifier

##### Returns:

    
    
    number: number of points if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    print("Point count:{}".format(rs.PointCloudCount(id)))

##### See Also:

  * AddPointCloud
  * IsPointCloud
  * PointCloudPoints

  

PointCloudHasHiddenPoints

    
    
    PointCloudHasHiddenPoints(object_id)

Verifies that a point cloud has hidden points

##### Parameters:

    
    
    object_id (guid): the point cloud object's identifier

##### Returns:

    
    
    bool: True if cloud has hidden points, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a point cloud", rs.filter.pointcloud)
    if rs.PointCloudHasHiddenPoints(obj):
        print("The point cloud has hidden points.")
    else:
        print("The point cloud has no hidden points.")

##### See Also:

  * PointCloudHasPointColors
  * PointCloudHidePoints
  * PointCloudPointColors

  

PointCloudHasPointColors

    
    
    PointCloudHasPointColors(object_id)

Verifies that a point cloud has point colors

##### Parameters:

    
    
    object_id (guid): the point cloud object's identifier

##### Returns:

    
    
    bool: True if cloud has point colors, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a point cloud", rs.filter.pointcloud)
    if rs.PointCloudHasPointColors(obj):
        print("The point cloud has point colors.")
    else:
        print("The point cloud has no point colors.")

##### See Also:

  * PointCloudHasPointColors
  * PointCloudHidePoints
  * PointCloudPointColors

  

PointCloudHidePoints

    
    
    PointCloudHidePoints(object_id, hidden=[])

Returns or modifies the hidden points of a point cloud object

##### Parameters:

    
    
    object_id (guid): the point cloud object's identifier
    hidden ([bool, ....]): list of booleans matched to the index of points to be hidden

##### Returns:

    
    
    list(bool, ....): List of point cloud hidden states

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    if obj:
        hidden = [True] * rs.PointCloudCount(obj)
        for i in range(len(hidden)):
            hidden[i] = (i%2==0)
        rs.PointCloudHidePoints(obj, hidden)

##### See Also:

  * PointCloudHasPointColors
  * PointCloudPointColors

  

PointCloudPointColors

    
    
    PointCloudPointColors(object_id, colors=[])

Returns or modifies the point colors of a point cloud object

##### Parameters:

    
    
    object_id (guid): the point cloud object's identifier
    colors ([color, ...]) list of color values if you want to adjust colors

##### Returns:

    
    
    list(color, ...): List of point cloud colors

##### Example:

    
    
    import rhinoscriptsyntax as rs
    import random
           
    def RandomColor():
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return rs.coercecolor((red,green,blue))
           
    obj = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    if obj:
        colors = [RandomColor() for i in range(rs.PointCloudCount(obj))]
        rs.PointCloudColors(obj, colors)

##### See Also:

  * PointCloudHasHiddenPoints
  * PointCloudHasPointColors
  * PointCloudHidePoints

  

PointCloudPoints

    
    
    PointCloudPoints(object_id)

Returns the points of a point cloud object

##### Parameters:

    
    
    object_id (guid): the point cloud object's identifier

##### Returns:

    
    
    list(guid, ...): list of points if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    points = rs.PointCloudPoints(id)
    if points: for point in points: print(point)

##### See Also:

  * AddPointCloud
  * IsPointCloud
  * PointCloudCount

  

PointCloudKNeighbors

    
    
    PointCloudKNeighbors(pt_cloud, needle_points, amount=1)

Returns amount indices of points in a point cloud that are near needle_points.

##### Parameters:

    
    
    pt_cloud (guid|[point, ...]): the point cloud to be searched, or the "hay stack". This can also be a list of points.
    needle_points (guid|[point, ...]): a list of points to search in the point_cloud. This can also be specified as a point cloud.
    amount (int, optional): the amount of required closest points. Defaults to 1.

##### Returns:

    
    
    [int, int,...]: a list of indices of the found points, if amount equals 1.
    [[int, ...], ...]: nested lists with amount items within a list, with the indices of the found points.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    if id:
        result = rs.PointCloudKNeighbors(id, [(0,0,0)])
        if result:
            print("The closest point to origin has index : %s." % result[0])

##### See Also:

  * AddPointCloud
  * IsPointCloud
  * PointCloudPoints

  

PointCloudClosestPoints

    
    
    PointCloudClosestPoints(pt_cloud, needle_points, distance)

Returns a list of lists of point indices in a point cloud that are closest to
needle_points. Each inner list references all points within or on the surface
of a sphere of distance radius.

##### Parameters:

    
    
    pt_cloud (guid|[point, ...]): the point cloud to be searched, or the "hay stack". This can also be a list of points.
    needle_points (guid|[point, ...]): a list of points to search in the point_cloud. This can also be specified as a point cloud.
    distance (float): the included limit for listing points.

##### Returns:

    
    
    [[int, ...], ...]: a list of lists with the indices of the found points.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
    if id:
        result = rs.PointCloudClosestPoints(id, [[0,0,0]], 1.0)
        if result and result[0]:
            print("The first point next to origin within a 1.0 unit radius is: %s." % result[0][0])
        else:
            print("There is no point in the point cloud within a 1.0 unit radius sphere from origin.")

##### See Also:

  * AddPointCloud
  * IsPointCloud
  * PointCloudPoints

  

PointCoordinates

    
    
    PointCoordinates(object_id, point=None)

Returns or modifies the X, Y, and Z coordinates of a point object

##### Parameters:

    
    
    object_id (guid): The identifier of a point object
    point (point, optional): A new 3D point location.

##### Returns:

    
    
    point: If point is not specified, the current 3-D point location
    point: If point is specified, the previous 3-D point location

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select point", rs.filter.point)
    point = rs.PointCoordinates(id)
    if point: print(point)

##### See Also:

  * AddPoint
  * IsPoint

  

TextDotFont

    
    
    TextDotFont(object_id, fontface=None)

Returns or modified the font of a text dot

##### Parameters:

    
    
    object_id (guid): identifier of a text dot object
    fontface (str, optional): new font face name

##### Returns:

    
    
    str: If font is not specified, the current text dot font
    str: If font is specified, the previous text dot font
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text dot")
    if rs.IsTextDot(obj): rs.TextDotFont( obj, "Arial" )

##### See Also:

  * AddTextDot
  * IsTextDot
  * TextDotHeight
  * TextDotPoint
  * TextDotText

  

TextDotHeight

    
    
    TextDotHeight(object_id, height=None)

Returns or modified the font height of a text dot

##### Parameters:

    
    
    object_id (guid): identifier of a text dot object
    height (number, optional) new font height

##### Returns:

    
    
    number: If height is not specified, the current text dot height
    number: If height is specified, the previous text dot height
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text dot")
    if rs.IsTextDot(obj): rs.TextDotHeight(obj, 10.0)

##### See Also:

  * AddTextDot
  * IsTextDot
  * TextDotFont
  * TextDotPoint
  * TextDotText

  

TextDotPoint

    
    
    TextDotPoint(object_id, point=None)

Returns or modifies the location, or insertion point, on a text dot object

##### Parameters:

    
    
    object_id (guid): identifier of a text dot object
    point (point, optional): A new 3D point location.

##### Returns:

    
    
    point: If point is not specified, the current 3-D text dot location
    point: If point is specified, the previous 3-D text dot location
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select text dot")
    if rs.IsTextDot(id):
        point = rs.TestDotPoint(id)
        rs.AddPoint( point )
        rs.TextDotPoint(id, [0,0,0])

##### See Also:

  * AddTextDot
  * IsTextDot
  * TextDotText

  

TextDotText

    
    
    TextDotText(object_id, text=None)

Returns or modifies the text on a text dot object

##### Parameters:

    
    
    object_id (guid): The identifier of a text dot object
    text (str, optional): a new string for the dot

##### Returns:

    
    
    str: If text is not specified, the current text dot text
    str: If text is specified, the previous text dot text
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select text dot")
    if rs.IsTextDot(id):
        rs.TextDotText( id, "Rhino")

##### See Also:

  * AddTextDot
  * IsTextDot
  * TextDotPoint

  

TextObjectFont

    
    
    TextObjectFont(object_id, font=None)

Returns of modifies the font used by a text object

##### Parameters:

    
    
    object_id (guid): the identifier of a text object
    font (str): the new font face name

##### Returns:

    
    
    str: if a font is not specified, the current font face name
    str: if a font is specified, the previous font face name
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text")
    if rs.IsText(obj): rs.TextObjectFont(obj, "Arial")

##### See Also:

  * AddText
  * IsText
  * TextObjectHeight
  * TextObjectPlane
  * TextObjectPoint
  * TextObjectStyle
  * TextObjectText

  

TextObjectHeight

    
    
    TextObjectHeight(object_id, height=None)

Returns or modifies the height of a text object

##### Parameters:

    
    
    object_id (guid): the identifier of a text object
    height (number, optional): the new text height.

##### Returns:

    
    
    number: if height is not specified, the current text height
    number: if height is specified, the previous text height
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text")
    if rs.IsText(obj):
        rs.TextObjectHeight( obj, 1.0 )

##### See Also:

  * AddText
  * IsText
  * TextObjectFont
  * TextObjectPlane
  * TextObjectPoint
  * TextObjectStyle
  * TextObjectText

  

TextObjectPlane

    
    
    TextObjectPlane(object_id, plane=None)

Returns or modifies the plane used by a text object

##### Parameters:

    
    
    object_id (guid): the identifier of a text object
    plane (plane): the new text object plane

##### Returns:

    
    
    plane: if a plane is not specified, the current plane if successful
    plane: if a plane is specified, the previous plane if successful
    None: if not successful, or on Error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text")
    if rs.IsText(obj):
        plane = rs.ViewCPlane("Top")
        rs.TextObjectPlane( obj, plane )

##### See Also:

  * AddText
  * IsText
  * TextObjectFont
  * TextObjectHeight
  * TextObjectPoint
  * TextObjectStyle
  * TextObjectText

  

TextObjectPoint

    
    
    TextObjectPoint(object_id, point=None)

Returns or modifies the location of a text object

##### Parameters:

    
    
    object_id (guid): the identifier of a text object
    point (point, optional) the new text object location

##### Returns:

    
    
    point: if point is not specified, the 3D point identifying the current location
    point: if point is specified, the 3D point identifying the previous location
    None: if not successful, or on Error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text")
    if rs.IsText(obj):
        rs.TextObjectPoint( obj, [0,0,0] )

##### See Also:

  * AddText
  * IsText
  * TextObjectFont
  * TextObjectHeight
  * TextObjectPlane
  * TextObjectStyle
  * TextObjectText

  

TextObjectStyle

    
    
    TextObjectStyle(object_id, style=None)

Returns or modifies the font style of a text object

##### Parameters:

    
    
    object_id (guid) the identifier of a text object
    style (number, optional) the font style. Can be any of the following flags
       0 = Normal
       1 = Bold
       2 = Italic

##### Returns:

    
    
    number: if style is not specified, the current font style
    number: if style is specified, the previous font style
    None: if not successful, or on Error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text")
    if rs.IsText(obj):
        rs.TextObjectStyle( obj, 3 )

##### See Also:

  * AddText
  * IsText
  * TextObjectFont
  * TextObjectHeight
  * TextObjectPlane
  * TextObjectPoint
  * TextObjectText

  

TextObjectText

    
    
    TextObjectText(object_id, text=None)

Returns or modifies the text string of a text object.

##### Parameters:

    
    
    object_id (guid): the identifier of a text object
    text (str, optional): a new text string

##### Returns:

    
    
    str: if text is not specified, the current string value if successful
    str: if text is specified, the previous string value if successful
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select text")
    if rs.IsText(obj): rs.TextObjectText(obj, "Rhino")

##### See Also:

  * AddText
  * IsText
  * TextObjectFont
  * TextObjectHeight
  * TextObjectPlane
  * TextObjectPoint
  * TextObjectStyle

  

## grips

EnableObjectGrips

    
    
    EnableObjectGrips(object_id, enable=True)

Enables or disables an object's grips. For curves and surfaces, these are also
called control points.

##### Parameters:

    
    
    object_id (guid): identifier of the object
    enable (bool, optional): if True, the specified object's grips will be turned on.
      Otherwise, they will be turned off

##### Returns:

    
    
    bool: True on success, False on failure

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    objects = rs.GetObjects("Select  objects")
    if objects: [rs.EnableObjectGrips(obj)  for obj in objs]

##### See Also:

  * ObjectGripCount
  * ObjectGripsOn
  * ObjectGripsSelected
  * SelectObjectGrips
  * UnselectObjectGrips

  

GetObjectGrip

    
    
    GetObjectGrip(message=None, preselect=False, select=False)

Prompts the user to pick a single object grip

##### Parameters:

    
    
    message (str, optional): prompt for picking
    preselect (bool, optional): allow for selection of pre-selected object grip.
    select (bool, optional): select the picked object grip.

##### Returns:

    
    
    tuple(guid, number, point): defining a grip record.
       [0] = identifier of the object that owns the grip
       [1] = index value of the grip
       [2] = location of the grip
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select a curve", rs.filter.curve)
    if curve:
        rs.EnableObjectGrips( curve )
        grip = rs.GetObjectGrip("Select a curve grip")
        if grip: print(grip[2])

##### See Also:

  * GetObjectGrips

  

GetObjectGrips

    
    
    GetObjectGrips(message=None, preselect=False, select=False)

Prompts user to pick one or more object grips from one or more objects.

##### Parameters:

    
    
    message (str, optional): prompt for picking
    preselect (bool, optional): allow for selection of pre-selected object grips
    select (bool, optional) select the picked object grips

##### Returns:

    
    
    list((guid, number, point), ...): containing one or more grip records. Each grip record is a tuple
      [n][0] = identifier of the object that owns the grip
      [n][1] = index value of the grip
      [n][2] = location of the grip
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curves = rs.GetObjects("Select curves", rs.filter.curves)
    if curves:
        for curve in curves: rs.EnableObjectGrips(curve)
        grips = rs.GetObjectGrips("Select curve grips")
        if grips: for grip in grips: print(grip[0])

##### See Also:

  * GetObjectGrip

  

NextObjectGrip

    
    
    NextObjectGrip(object_id, index, direction=0, enable=True)

Returns the next grip index from a specified grip index of an object

##### Parameters:

    
    
    object_id (guid): identifier of the object
    index (number): zero based grip index from which to get the next grip index
    direction ([number, number], optional): direction to get the next grip index (0=U, 1=V)
    enable (bool, optional): if True, the next grip index found will be selected

##### Returns:

    
    
    number: index of the next grip on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object_id = rs.GetObject("Select curve", rs.filter.curve)
    if object_id:
        rs.EnableObjectGrips( object_id )
        count = rs.ObjectGripCount( object_id )
        for i in range(0,count,2):
            rs.NextObjectGrip(object_id, i, 0, True)

##### See Also:

  * EnableObjectGrips
  * PrevObjectGrip

  

ObjectGripCount

    
    
    ObjectGripCount(object_id)

Returns number of grips owned by an object

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    number: number of grips if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.ObjectGripsOn(obj):
        print("Grip count ={}".format(rs.ObjectGripCount(obj)))

##### See Also:

  * EnableObjectGrips
  * ObjectGripsOn
  * ObjectGripsSelected
  * SelectObjectGrips
  * UnselectObjectGrips

  

ObjectGripLocation

    
    
    ObjectGripLocation(object_id, index, point=None)

Returns or modifies the location of an object's grip

##### Parameters:

    
    
    object_id (guid) identifier of the object
    index (number): index of the grip to either query or modify
    point (point, optional): 3D point defining new location of the grip

##### Returns:

    
    
    point: if point is not specified, the current location of the grip referenced by index
    point: if point is specified, the previous location of the grip referenced by index
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    if obj:
        rs.EnableObjectGrips(obj)
        point = rs.ObjectGripLocation(obj, 0)
        point[0] = point[0] + 1.0
        point[1] = point[1] + 1.0
        point[2] = point[2] + 1.0
        rs.ObjectGripLocation(obj, 0, point)
        rs.EnableObjectGrips(obj, False)

##### See Also:

  * EnableObjectGrips
  * ObjectGripLocations

  

ObjectGripLocations

    
    
    ObjectGripLocations(object_id, points=None)

Returns or modifies the location of all grips owned by an object. The
locations of the grips are returned in a list of Point3d with each position in
the list corresponding to that grip's index. To modify the locations of the
grips, you must provide a list of points that contain the same number of
points at grips

##### Parameters:

    
    
    object_id (guid): identifier of the object
    points ([point, ...], optional) list of 3D points identifying the new grip locations

##### Returns:

    
    
    list(point, ...): if points is not specified, the current location of all grips
    list(point, ...): if points is specified, the previous location of all grips
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    if obj:
        rs.EnableObjectGrips( obj )
        points = rs.ObjectGripLocations(obj)
        for point in points:  print(point)

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * ObjectGripLocation

  

ObjectGripsOn

    
    
    ObjectGripsOn(object_id)

Verifies that an object's grips are turned on

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    bool: True or False indicating Grips state
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.ObjectGripsOn(obj):
        print("Grip count = {}".format(rs.ObjectGripCount(obj)))

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * ObjectGripsSelected
  * SelectObjectGrips
  * UnselectObjectGrips

  

ObjectGripsSelected

    
    
    ObjectGripsSelected(object_id)

Verifies that an object's grips are turned on and at least one grip is
selected

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.ObjectGripsSelected(obj):
        rs.UnselectObjectGrips( obj )

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * ObjectGripsOn
  * SelectObjectGrips
  * UnselectObjectGrips

  

PrevObjectGrip

    
    
    PrevObjectGrip(object_id, index, direction=0, enable=True)

Returns the previous grip index from a specified grip index of an object

##### Parameters:

    
    
    object_id (guid): identifier of the object
    index (number): zero based grip index from which to get the previous grip index
    direction ([number, number], optional): direction to get the next grip index (0=U, 1=V)
    enable (bool, optional): if True, the next grip index found will be selected

##### Returns:

    
    
    number: index of the next grip on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object_id = rs.GetObject("Select curve", rs.filter.curve)
    if object_id:
        rs.EnableObjectGrips(object_id)
        count = rs.ObjectGripCount(object_id)
        for i in range(count-1, 0, -2):
            rs.PrevObjectGrip(object_id, i, 0, True)

##### See Also:

  * EnableObjectGrips
  * NextObjectGrip

  

SelectedObjectGrips

    
    
    SelectedObjectGrips(object_id)

Returns a list of grip indices indentifying an object's selected grips

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    list(number): list of indices on success
    None: on failure or if no grips are selected

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    if obj:
        rs.EnableObjectGrips( obj )
        count = rs.ObjectGripCount( obj )
        for i in range(0,count,2):
            rs.SelectObjectGrip( obj, i )
        grips = rs.SelectedObjectGrips(obj)
        if grips: print(len(grips{}).format("grips selected"))

##### See Also:

  * EnableObjectGrips
  * SelectObjectGrip
  * SelectObjectGrips

  

SelectObjectGrip

    
    
    SelectObjectGrip(object_id, index)

Selects a single grip owned by an object. If the object's grips are not turned
on, the grips will not be selected

##### Parameters:

    
    
    object_id (guid) identifier of the object
    index (number): index of the grip to select

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    if obj:
        rs.EnableObjectGrips( obj )
        count = rs.ObjectGripCount( obj )
        for i in range(0,count,2): rs.SelectObjectGrip(obj,i)

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * SelectObjectGrips

  

SelectObjectGrips

    
    
    SelectObjectGrips(object_id)

Selects an object's grips. If the object's grips are not turned on, they will
not be selected

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    number: Number of grips selected on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.ObjectGripsSelected(obj)==False:
        rs.SelectObjectGrips( obj )

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * SelectObjectGrip

  

UnselectObjectGrip

    
    
    UnselectObjectGrip(object_id, index)

Unselects a single grip owned by an object. If the object's grips are not
turned on, the grips will not be unselected

##### Parameters:

    
    
    object_id (guid): identifier of the object
    index (number): index of the grip to unselect

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select curve", rs.filter.curve)
    if obj:
        rs.EnableObjectGrips( obj )
        count = rs.ObjectGripCount(obj)
        for i in range(0,count,2):
            rs.UnselectObjectGrip( obj, i )

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * UnselectObjectGrips

  

UnselectObjectGrips

    
    
    UnselectObjectGrips(object_id)

Unselects an object's grips. Note, the grips will not be turned off.

##### Parameters:

    
    
    object_id (guid): identifier of the object

##### Returns:

    
    
    number: Number of grips unselected on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.ObjectGripsSelected(obj): rs.UnselectObjectGrips(obj)

##### See Also:

  * EnableObjectGrips
  * ObjectGripCount
  * UnselectObjectGrip

  

## group

AddGroup

    
    
    AddGroup(group_name=None)

Adds a new empty group to the document

##### Parameters:

    
    
    group_name (str, optional): name of the new group. If omitted, rhino automatically
        generates the group name

##### Returns:

    
    
    str: name of the new group if successful
    None: is not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = rs.AddGroup("NewGroup")

##### See Also:

  * DeleteGroup
  * GroupCount
  * GroupNames
  * IsGroup
  * RenameGroup

  

AddObjectsToGroup

    
    
    AddObjectsToGroup(object_ids, group_name)

Adds one or more objects to an existing group.

##### Parameters:

    
    
    object_ids ([guid, ...]) list of Strings or Guids representing the object identifiers
    group_name (str): the name of an existing group

##### Returns:

    
    
    number: number of objects added to the group

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = "NewGroup"
    object_ids = rs.GetObjects("Select objects to add to group")
    if object_ids: rs.AddObjectsToGroup(object_ids, name)

##### See Also:

  * AddObjectToGroup
  * IsGroupEmpty
  * ObjectGroups
  * ObjectsByGroup

  

AddObjectToGroup

    
    
    AddObjectToGroup(object_id, group_name)

Adds a single object to an existing group.

##### Parameters:

    
    
    object_id (guid): String or Guid representing the object identifier
    group_name (str): the name of an existing group

##### Returns:

    
    
    True or False representing success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = "NewGroup"
    id = rs.GetObject("Select object to add to group")
    if id: rs.AddObjectToGroup(id,name)

##### See Also:

  * AddObjectsToGroup
  * IsGroupEmpty
  * ObjectGroups
  * ObjectsByGroup

  

DeleteGroup

    
    
    DeleteGroup(group_name)

Removes an existing group from the document. Reference groups cannot be
removed. Deleting a group does not delete the member objects

##### Parameters:

    
    
    group_name (str): the name of an existing group

##### Returns:

    
    
    bool: True or False representing success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    groups = rs.GroupNames()
    if groups:
        for group in groups: rs.DeleteGroup(group)

##### See Also:

  * AddGroup
  * GroupCount
  * GroupNames
  * IsGroup
  * RenameGroup

  

GroupCount

    
    
    GroupCount()

Returns the number of groups in the document

##### Returns:

    
    
    number: the number of groups in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    numgroups = rs.GroupCount()
    print("Group count:{}".format(numgroups))

##### See Also:

  * AddGroup
  * DeleteGroup
  * GroupNames
  * IsGroup
  * RenameGroup

  

GroupNames

    
    
    GroupNames()

Returns the names of all the groups in the document None if no names exist in
the document

##### Returns:

    
    
    list(str, ...): the names of all the groups in the document.  None if no names exist in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    groups = rs.GroupNames()
    if groups:
        for group in groups: print(group)

##### See Also:

  * AddGroup
  * DeleteGroup
  * GroupCount
  * IsGroup
  * RenameGroup

  

HideGroup

    
    
    HideGroup(group_name)

Hides a group of objects. Hidden objects are not visible, cannot be snapped
to, and cannot be selected

##### Parameters:

    
    
    group_name (str): the name of an existing group

##### Returns:

    
    
    number: The number of objects that were hidden

##### Example:

    
    
    import rhinoscriptsyntax as rs
    groups = rs.GroupNames()
    if groups:
        for group in groups: rs.HideGroup(group)

##### See Also:

  * LockGroup
  * ShowGroup
  * UnlockGroup

  

IsGroup

    
    
    IsGroup(group_name)

Verifies the existance of a group

##### Parameters:

    
    
    group_name (str): the name of the group to check for

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    group = rs.GetString("Group name to verify")
    if rs.IsGroup(group):
        print("The group exists.")
    else:
        print("The group does not exist.")

##### See Also:

  * AddGroup
  * DeleteGroup
  * GroupCount
  * GroupNames
  * RenameGroup

  

IsGroupEmpty

    
    
    IsGroupEmpty(group_name)

Verifies that an existing group is empty, or contains no object members

##### Parameters:

    
    
    group_name (str): the name of an existing group

##### Returns:

    
    
    bool: True or False if group_name exists
    None: if group_name does not exist

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.GroupNames()
    if names:
        for name in names:
            if rs.IsGroupEmpty(name): rs.DeleteGroup(name)

##### See Also:

  * AddObjectsToGroup
  * AddObjectToGroup
  * RemoveObjectFromAllGroups
  * RemoveObjectFromGroup
  * RemoveObjectsFromGroup

  

LockGroup

    
    
    LockGroup(group_name)

Locks a group of objects. Locked objects are visible and they can be snapped
to. But, they cannot be selected

##### Parameters:

    
    
    group_name (str): the name of an existing group

##### Returns:

    
    
    number: Number of objects that were locked if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.GroupNames()
    if names:
        for name in names: rs.LockGroup(name)

##### See Also:

  * HideGroup
  * ShowGroup
  * UnlockGroup

  

RemoveObjectFromAllGroups

    
    
    RemoveObjectFromAllGroups(object_id)

Removes a single object from any and all groups that it is a member. Neither
the object nor the group can be reference objects

##### Parameters:

    
    
    object_id (guid): the object identifier

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select object")
    if object: rs.RemoveObjectFromAllGroups(object)

##### See Also:

  * IsGroupEmpty
  * ObjectGroups
  * ObjectsByGroup
  * RemoveObjectFromGroup
  * RemoveObjectsFromGroup

  

RemoveObjectFromGroup

    
    
    RemoveObjectFromGroup(object_id, group_name)

Remove a single object from an existing group

##### Parameters:

    
    
    object_id (guid): the object identifier
    group_name (str): the name of an existing group

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = "NewGroup"
    id = rs.GetObject("Select object")
    if name: rs.RemoveObjectFromGroup(id,name)

##### See Also:

  * IsGroupEmpty
  * ObjectGroups
  * ObjectsByGroup
  * RemoveObjectFromAllGroups
  * RemoveObjectsFromGroup

  

RemoveObjectsFromGroup

    
    
    RemoveObjectsFromGroup(object_ids, group_name)

Removes one or more objects from an existing group

##### Parameters:

    
    
    object_ids ([guid, ...]): a list of object identifiers
    group_name (str): the name of an existing group

##### Returns:

    
    
    number: The number of objects removed from the group is successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    group = "NewGroup"
    ids = rs.GetObjects("Select objects")
    if ids: rs.RemoveObjectsFromGroup(ids,group)

##### See Also:

  * IsGroupEmpty
  * ObjectGroups
  * ObjectsByGroup
  * RemoveObjectFromAllGroups
  * RemoveObjectFromGroup

  

RenameGroup

    
    
    RenameGroup(old_name, new_name)

Renames an existing group

##### Parameters:

    
    
    old_name (str): the name of an existing group
    new_name (str): the new group name

##### Returns:

    
    
    str: the new group name if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    strOldGroup = rs.GetString("Old group name")
    if strOldGroup:
        strNewGroup = rs.GetString("New group name")
        if strNewName: rs.RenameGroup(strOldGroup, strNewGroup)

##### See Also:

  * AddGroup
  * DeleteGroup
  * GroupCount
  * GroupNames
  * IsGroup

  

ShowGroup

    
    
    ShowGroup(group_name)

Shows a group of previously hidden objects. Hidden objects are not visible,
cannot be snapped to, and cannot be selected

##### Parameters:

    
    
    group_name (str): the name of an existing group

##### Returns:

    
    
    number: The number of objects that were shown if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    groups = rs.GroupNames()
    if groups:
        for group in groups: rs.ShowGroup(group)

##### See Also:

  * HideGroup
  * LockGroup
  * UnlockGroup

  

UnlockGroup

    
    
    UnlockGroup(group_name)

Unlocks a group of previously locked objects. Lockes objects are visible, can
be snapped to, but cannot be selected

##### Parameters:

    
    
    group_name (str): the name of an existing group

##### Returns:

    
    
    number: The number of objects that were unlocked if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    groups = rs.GroupNames()
    if groups:
        for group in groups: rs.UnlockGroup(group)

##### See Also:

  * HideGroup
  * LockGroup
  * ShowGroup

  

ObjectTopGroup

    
    
    ObjectTopGroup(object_id)

Returns the top most group name that an object is assigned. This function
primarily applies to objects that are members of nested groups

##### Parameters:

    
    
    object_id (guid): String or Guid representing the object identifier

##### Returns:

    
    
    str: the top group's name if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object to add to group")
    groupName = rs.ObjectTopGroup(id)

##### See Also:

  * ObjectGroups

  

## hatch

AddHatch

    
    
    AddHatch(curve_id, hatch_pattern=None, scale=1.0, rotation=0.0)

Creates a new hatch object from a closed planar curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the closed planar curve that defines the
        boundary of the hatch object
    hatch_pattern (str, optional): name of the hatch pattern to be used by the hatch
        object. If omitted, the current hatch pattern will be used
    scale (number, optional): hatch pattern scale factor
    rotation (number, optional): hatch pattern rotation angle in degrees.

##### Returns:

    
    
    guid:identifier of the newly created hatch on success
    None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    circle = rs.AddCircle(rs.WorldXYPlane(), 10.0)
    if rs.IsHatchPattern("Grid"):
        rs.AddHatch( circle, "Grid" )
    else:
        rs.AddHatch( circle, rs.CurrentHatchPattern() )

##### See Also:

  * AddHatches
  * CurrentHatchPattern
  * HatchPatternNames

  

AddHatches

    
    
    AddHatches(curve_ids, hatch_pattern=None, scale=1.0, rotation=0.0, tolerance=None)

Creates one or more new hatch objects a list of closed planar curves

##### Parameters:

    
    
    curve_ids ([guid, ...]): identifiers of the closed planar curves that defines the
        boundary of the hatch objects
    hatch_pattern (str, optional):  name of the hatch pattern to be used by the hatch
        object. If omitted, the current hatch pattern will be used
    scale (number, optional): hatch pattern scale factor
    rotation (number, optional): hatch pattern rotation angle in degrees.
    tolerance (number, optional): tolerance for hatch fills.

##### Returns:

    
    
    list(guid, ...): identifiers of the newly created hatch on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curves = rs.GetObjects("Select closed planar curves", rs.filter.curve)
    if curves:
        if rs.IsHatchPattern("Grid"):
            rs.AddHatches( curves, "Grid" )
        else:
            rs.AddHatches( curves, rs.CurrentHatchPattern() )

##### See Also:

  * AddHatch
  * CurrentHatchPattern
  * HatchPatternNames

  

AddHatchPatterns

    
    
    AddHatchPatterns(filename, replace=False)

Adds hatch patterns to the document by importing hatch pattern definitions
from a pattern file.

##### Parameters:

    
    
    filename (str): name of the hatch pattern file
    replace (bool, optional): If hatch pattern names already in the document match hatch
        pattern names in the pattern definition file, then the existing hatch
        patterns will be redefined

##### Returns:

    
    
    list(str, ...): Names of the newly added hatch patterns if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filename = rs.OpenFileName("Import", "Pattern Files (*.pat)|*.pat||")
    if filename:
        patterns = rs.AddHatchPatterns(filename)
        if patterns:
            for pattern in patterns: print(pattern)

##### See Also:

  * HatchPatternCount
  * HatchPatternNames

  

CurrentHatchPattern

    
    
    CurrentHatchPattern(hatch_pattern=None)

Returns or sets the current hatch pattern file

##### Parameters:

    
    
    hatch_pattern(str, optional):  name of an existing hatch pattern to make current

##### Returns:

    
    
    str: if hatch_pattern is not specified, the current hatch pattern
    str: if hatch_pattern is specified, the previous hatch pattern
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if rs.IsHatchPattern("Hatch2"): rs.CurrentHatchPattern("Hatch2")

##### See Also:

  * HatchPatternCount
  * HatchPatternNames

  

ExplodeHatch

    
    
    ExplodeHatch(hatch_id, delete=False)

Explodes a hatch object into its component objects. The exploded objects will
be added to the document. If the hatch object uses a solid pattern, then
planar face Brep objects will be created. Otherwise, line curve objects will
be created

##### Parameters:

    
    
    hatch_id (guid): identifier of a hatch object
    delete (bool, optional): delete the hatch object

##### Returns:

    
    
    list(guid, ...): list of identifiers for the newly created objects
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if rs.IsHatch(id): rs.ExplodeHatch(id, True)

##### See Also:

  * IsHatch
  * HatchPattern
  * HatchRotation
  * HatchScale

  

HatchPattern

    
    
    HatchPattern(hatch_id, hatch_pattern=None)

Returns or changes a hatch object's hatch pattern

##### Parameters:

    
    
    hatch_id (guid): identifier of a hatch object
    hatch_pattern (str, optional): name of an existing hatch pattern to replace the
        current hatch pattern

##### Returns:

    
    
    str: if hatch_pattern is not specified, the current hatch pattern
    str: if hatch_pattern is specified, the previous hatch pattern
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.AllObjects()
    if objects is not None:
        for obj in objects:
            if rs.IsHatch(obj) and rs.HatchPattern(obj)=="Solid":
                rs.SelectObject(obj)

##### See Also:

  * AddHatch
  * AddHatches
  * HatchRotation
  * HatchScale
  * IsHatch

  

HatchPatternCount

    
    
    HatchPatternCount()

Returns the number of hatch patterns in the document

##### Returns:

    
    
    number: the number of hatch patterns in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("There are {} hatch patterns.".format(rs.HatchPatternCount()))

##### See Also:

  * HatchPatternNames

  

HatchPatternDescription

    
    
    HatchPatternDescription(hatch_pattern)

Returns the description of a hatch pattern. Note, not all hatch patterns have
descriptions

##### Parameters:

    
    
    hatch_pattern (str): name of an existing hatch pattern

##### Returns:

    
    
    str: description of the hatch pattern on success otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    patterns = rs.HatchPatternNames()
    for pattern in patterns:
        description = rs.HatchPatternDescription(pattern)
        if description: print("{} - {}".format(pattern, description))
        else: print(pattern)

##### See Also:

  * HatchPatternCount
  * HatchPatternNames

  

HatchPatternFillType

    
    
    HatchPatternFillType(hatch_pattern)

Returns the fill type of a hatch pattern.

##### Parameters:

    
    
    hatch_pattern (str): name of an existing hatch pattern

##### Returns:

    
    
    number: hatch pattern's fill type if successful
            0 = solid, uses object color
            1 = lines, uses pattern file definition
            2 = gradient, uses fill color definition
    None: if unsuccessful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    patterns = rs.HatchPatternNames()
    for pattern in patterns:
        fill = rs.HatchPatternFillType(pattern)
        print("{} - {}".format(pattern, fill))

##### See Also:

  * HatchPatternCount
  * HatchPatternNames

  

HatchPatternNames

    
    
    HatchPatternNames()

Returns the names of all of the hatch patterns in the document

##### Returns:

    
    
    list(str, ...): the names of all of the hatch patterns in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    patterns = rs.HatchPatternNames()
    for pattern in patterns:
        description = rs.HatchPatternDescription(pattern)
        if description: print("{} - {}".format(pattern, description))
        else: print(pattern)

##### See Also:

  * HatchPatternCount

  

HatchRotation

    
    
    HatchRotation(hatch_id, rotation=None)

Returns or modifies the rotation applied to the hatch pattern when it is
mapped to the hatch's plane

##### Parameters:

    
    
    hatch_id (guid): identifier of a hatch object
    rotation (number, optional): rotation angle in degrees

##### Returns:

    
    
    number: if rotation is not defined, the current rotation angle
    number: if rotation is specified, the previous rotation angle
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.AllObjects()
    if objects:
        for obj in objects:
            if rs.IsHatch(obj) and rs.HatchRotation(obj)>0:
                rs.HatchRotation(obj,0)

##### See Also:

  * AddHatch
  * AddHatches
  * HatchPattern
  * HatchScale
  * IsHatch

  

HatchScale

    
    
    HatchScale(hatch_id, scale=None)

Returns or modifies the scale applied to the hatch pattern when it is mapped
to the hatch's plane

##### Parameters:

    
    
    hatch_id (guid): identifier of a hatch object
    scale (number, optional):  scale factor

##### Returns:

    
    
    number: if scale is not defined, the current scale factor
    number: if scale is defined, the previous scale factor
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.NormalObjects()
    if objects:
        for obj in objects:
            if rs.IsHatch(obj) and rs.HatchScale(obj)>1.0:
                rs.HatchScale(obj, 1.0)

##### See Also:

  * HatchPattern
  * HatchRotation
  * IsHatch

  

IsHatch

    
    
    IsHatch(object_id)

Verifies the existence of a hatch object in the document

##### Parameters:

    
    
    object_id (guid): identifier of an object

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.IsHatch(obj): print("Object is a hatch")
    else: print("Object is not a hatch")

##### See Also:

  * HatchPattern
  * HatchRotation
  * HatchScale

  

IsHatchPattern

    
    
    IsHatchPattern(name)

Verifies the existence of a hatch pattern in the document

##### Parameters:

    
    
    name (str): the name of a hatch pattern

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    hatch = rs.GetString("Hatch pattern name")
    if rs.IsHatchPattern(hatch): print("The hatch pattern exists.")
    else: print("The hatch pattern does not exist.")

##### See Also:

  * IsHatchPatternCurrent
  * IsHatchPatternReference

  

IsHatchPatternCurrent

    
    
    IsHatchPatternCurrent(hatch_pattern)

Verifies that a hatch pattern is the current hatch pattern

##### Parameters:

    
    
    hatch_pattern (str): name of an existing hatch pattern

##### Returns:

    
    
    bool: True or False
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    hatch = rs.GetString("Hatch pattern name")
    if rs.IsHatchPattern(hatch):
        if rs.IsHatchPatternCurrent(hatch):
            print("The hatch pattern is current.")
        else:
            print("The hatch pattern is not current.")
    else: print("The hatch pattern does not exist.")

##### See Also:

  * IsHatchPattern
  * IsHatchPatternReference

  

IsHatchPatternReference

    
    
    IsHatchPatternReference(hatch_pattern)

Verifies that a hatch pattern is from a reference file

##### Parameters:

    
    
    hatch_pattern (str): name of an existing hatch pattern

##### Returns:

    
    
    bool: True or False
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    hatch = rs.GetString("Hatch pattern name")
    if rs.IsHatchPattern(hatch):
        if rs.IsHatchPatternReference(hatch):
            print("The hatch pattern is reference.")
        else:
            print("The hatch pattern is not reference.")
    else:
        print("The hatch pattern does not exist.")

##### See Also:

  * IsHatchPattern
  * IsHatchPatternCurrent

  

## layer

AddLayer

    
    
    AddLayer(name=None, color=None, visible=True, locked=False, parent=None)

Add a new layer to the document

##### Parameters:

    
    
    name (str, optional): The name of the new layer. If omitted, Rhino automatically
        generates the layer name.
    color (color): A Red-Green-Blue color value. If omitted, the color Black is assigned.
    visible (bool optional): layer's visibility
    locked (bool, optional): layer's locked state
    parent (str, optional): name of the new layer's parent layer. If omitted, the new
        layer will not have a parent layer.

##### Returns:

    
    
    str: The full name of the new layer if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    from System.Drawing import Color
    print("New layer:{}".format(rs.AddLayer()))
    print("New layer:{}".format(rs.AddLayer("MyLayer1")))
    print("New layer:{}".format(rs.AddLayer("MyLayer2", Color.DarkSeaGreen)))
    print("New layer:{}".format(rs.AddLayer("MyLayer3", Color.Cornsilk)))
    print("New layer:{}".format(rs.AddLayer("MyLayer4",parent="MyLayer3")))

##### See Also:

  * CurrentLayer
  * DeleteLayer
  * RenameLayer

  

CurrentLayer

    
    
    CurrentLayer(layer=None)

Returns or changes the current layer

##### Parameters:

    
    
    layer (guid): the name or Guid of an existing layer to make current

##### Returns:

    
    
    str: If a layer name is not specified, the full name of the current layer
    str: If a layer name is specified, the full name of the previous current layer

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddLayer("MyLayer")
    rs.CurrentLayer("MyLayer")

##### See Also:

  * AddLayer
  * DeleteLayer
  * RenameLayer

  

DeleteLayer

    
    
    DeleteLayer(layer)

Removes an existing layer from the document. The layer to be removed cannot be
the current layer. Unlike the PurgeLayer method, the layer must be empty, or
contain no objects, before it can be removed. Any layers that are children of
the specified layer will also be removed if they are also empty.

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing empty layer

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer to remove")
    if layer: rs.DeleteLayer(layer)

##### See Also:

  * AddLayer
  * CurrentLayer
  * PurgeLayer
  * RenameLayer

  

ExpandLayer

    
    
    ExpandLayer( layer, expand )

Expands a layer. Expanded layers can be viewed in Rhino's layer dialog

##### Parameters:

    
    
    layer (str): name of the layer to expand
    expand (bool): True to expand, False to collapse

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if rs.IsLayerExpanded("Default"):
        rs.ExpandLayer( "Default", False )

##### See Also:

  * IsLayerExpanded

  

IsLayer

    
    
    IsLayer(layer)

Verifies the existance of a layer in the document

##### Parameters:

    
    
    layer (str|guid): the name or id of a layer to search for

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        print("The layer exists.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayerChangeable
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerOn
  * IsLayerReference
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerChangeable

    
    
    IsLayerChangeable(layer)

Verifies that the objects on a layer can be changed (normal)

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerChangeable(layer): print("The layer is changeable.")
        else: print("The layer is not changeable.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerOn
  * IsLayerReference
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerChildOf

    
    
    IsLayerChildOf(layer, test)

Verifies that a layer is a child of another layer

##### Parameters:

    
    
    layer (str|guid): the name or id of the layer to test against
    test (str|guid): the name or id to the layer to test

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddLayer("MyLayer1")
    rs.AddLayer("MyLayer2", parent="MyLayer1")
    rs.AddLayer("MyLayer3", parent="MyLayer2")
    rs.MessageBox( rs.IsLayerChildOf("MyLayer1", "MyLayer3") )

##### See Also:

  * IsLayerParentOf

  

IsLayerCurrent

    
    
    IsLayerCurrent(layer)

Verifies that a layer is the current layer

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerCurrent(layer): print("The layer is current.")
        else: print("The layer is not current.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerOn
  * IsLayerReference
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerEmpty

    
    
    IsLayerEmpty(layer)

Verifies that an existing layer is empty, or contains no objects

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerEmpty(layer): print("The layer is empty.")
        else: print("The layer is not empty.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayerChangeable
  * IsLayerLocked
  * IsLayerOn
  * IsLayerReference
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerExpanded

    
    
    IsLayerExpanded(layer)

Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's
layer dialog

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    if rs.IsLayerExpanded("Default"):
        rs.ExpandLayer( "Default", False )

##### See Also:

  * ExpandLayer

  

IsLayerLocked

    
    
    IsLayerLocked(layer)

Verifies that a layer is locked.

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    cool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerLocked(layer): print("The layer is locked.")
        else: print("The layer is not locked.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerChangeable
  * IsLayerEmpty
  * IsLayerOn
  * IsLayerReference
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerOn

    
    
    IsLayerOn(layer)

Verifies that a layer is on.

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerOn(layer): print("The layer is on.")
        else: print("The layer is not on.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerChangeable
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerReference
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerSelectable

    
    
    IsLayerSelectable(layer)

Verifies that an existing layer is selectable (normal and reference)

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerSelectable(layer): print("The layer is selectable.")
        else: print("The layer is not selectable.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerChangeable
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerOn
  * IsLayerReference
  * IsLayerVisible

  

IsLayerParentOf

    
    
    IsLayerParentOf(layer, test)

Verifies that a layer is a parent of another layer

##### Parameters:

    
    
    layer (str|guid): the name or id of the layer to test against
    test (str|guid): the name or id to the layer to test

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddLayer("MyLayer1")
    rs.AddLayer("MyLayer2", parent="MyLayer1")
    rs.AddLayer("MyLayer3", parent="MyLayer2")
    rs.MessageBox( rs.IsLayerParentOf("MyLayer3", "MyLayer1") )

##### See Also:

  * IsLayerChildOf

  

IsLayerReference

    
    
    IsLayerReference(layer)

Verifies that a layer is from a reference file.

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerReference(layer): print("The layer is a reference layer.")
        else: print("The layer is not a reference layer.")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerChangeable
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerOn
  * IsLayerSelectable
  * IsLayerVisible

  

IsLayerVisible

    
    
    IsLayerVisible(layer)

Verifies that a layer is visible (normal, locked, and reference)

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    bool: True on success otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer name")
    if rs.IsLayer(layer):
        if rs.IsLayerVisible(layer): print("The layer is visible")
        else: print("The layer is not visible")
    else:
        print("The layer does not exist.")

##### See Also:

  * IsLayer
  * IsLayerChangeable
  * IsLayerEmpty
  * IsLayerLocked
  * IsLayerOn
  * IsLayerReference
  * IsLayerSelectable

  

LayerChildCount

    
    
    LayerChildCount(layer)

Returns the number of immediate child layers of a layer

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    number: the number of immediate child layers if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    children = rs.LayerChildCount("Default")
    if children: rs.ExpandLayer("Default", True)

##### See Also:

  * LayerChildren

  

LayerChildren

    
    
    LayerChildren(layer)

Returns the immediate child layers of a layer

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing layer

##### Returns:

    
    
    list(str, ...): List of children layer names

##### Example:

    
    
    import rhinoscriptsyntax as rs
    children = rs.LayerChildren("Default")
    if children:
        for child in children: print(child)

##### See Also:

  * LayerChildCount
  * ParentLayer

  

LayerColor

    
    
    LayerColor(layer, color=None)

Returns or changes the color of a layer.

##### Parameters:

    
    
    layer (str|guid): name or id of an existing layer
    color (color): the new color value. If omitted, the current layer color is returned.

##### Returns:

    
    
    color: If a color value is not specified, the current color value on success
    color: If a color value is specified, the previous color value on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    import random
    from System.Drawing import Color
           
    def randomcolor():
        red = int(255*random.random())
        green = int(255*random.random())
        blue = int(255*random.random())
        return Color.FromArgb(red,green,blue)
           
    layerNames = rs.LayerNames()
    if layerNames:
        for name in layerNames: rs.LayerColor(name, randomcolor())

  

LayerCount

    
    
    LayerCount()

Returns the number of layers in the document

##### Returns:

    
    
    number: the number of layers in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.LayerCount()
    print("There are {} layers".format(count))

##### See Also:

  * LayerNames

  

LayerIds

    
    
    LayerIds()

Return identifiers of all layers in the document

##### Returns:

    
    
    list(guid, ...): the identifiers of all layers in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerIds()
    for layer in layers: print(layer)

##### See Also:

  * LayerCount
  * LayerNames

  

LayerLinetype

    
    
    LayerLinetype(layer, linetype=None)

Returns or changes the linetype of a layer

##### Parameters:

    
    
    layer (str): name of an existing layer
    linetype (str, optional): name of a linetype

##### Returns:

    
    
    str: If linetype is not specified, name of the current linetype
    str: If linetype is specified, name of the previous linetype

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        for layer in layers:
            if rs.LayerLinetype(layer)!="Continuous":
                rs.LayerLinetype(layer,"Continuous")

##### See Also:

  * LayerPrintColor
  * LayerPrintWidth

  

LayerLocked

    
    
    LayerLocked(layer, locked=None)

Returns or changes the locked mode of a layer

##### Parameters:

    
    
    layer (str): name of an existing layer
    locked (bool, optional): new layer locked mode

##### Returns:

    
    
    bool: If locked is not specified, the current layer locked mode
    bool: If locked is specified, the previous layer locked mode

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        for layer in layers:
            if rs.LayerLocked(layer): rs.LayerLocked(layer, False)

##### See Also:

  * LayerVisible

  

LayerMaterialIndex

    
    
    LayerMaterialIndex(layer,index=None)

Returns or changes the material index of a layer. A material index of -1
indicates that no material has been assigned to the layer. Thus, the layer
will use Rhino's default layer material

##### Parameters:

    
    
    layer (str):  name of existing layer
    index (number, optional): the new material index

##### Returns:

    
    
    number: a zero-based material index if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    index = rs.LayerMaterialIndex("Default")
    if index is not None:
        if index==-1:
            print("The default layer does not have a material assigned.")
        else:
            print("The default layer has a material assigned.")

  

LayerId

    
    
    LayerId(layer)

Returns the identifier of a layer given the layer's name.

##### Parameters:

    
    
    layer (str): name of existing layer

##### Returns:

    
    
    guid (str): The layer's identifier if successful.
    None: If not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    id = rs.LayerId('Layer 01')

##### See Also:

  * LayerName

  

LayerName

    
    
    LayerName(layer_id, fullpath=True)

Return the name of a layer given it's identifier

##### Parameters:

    
    
    layer_id (guid): layer identifier
    fullpath (bool, optional): return the full path name `True` or short name `False`

##### Returns:

    
    
    str: the layer's name if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerIds()
    if layers:
        for layer in layers: print(rs.LayerName(layer))

##### See Also:

  * LayerId

  

LayerNames

    
    
    LayerNames(sort=False)

Returns the names of all layers in the document.

##### Parameters:

    
    
    sort (bool, optional): return a sorted list of the layer names

##### Returns:

    
    
    list(str, ...): list of layer names

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        for layer in layers: print(layer)

##### See Also:

  * LayerCount

  

LayerOrder

    
    
    LayerOrder(layer)

Returns the current display order index of a layer as displayed in Rhino's
layer dialog box. A display order index of -1 indicates that the current layer
dialog filter does not allow the layer to appear in the layer list

##### Parameters:

    
    
    layer (str): name of existing layer

##### Returns:

    
    
    number: 0 based index of layer

##### Example:

    
    
    import rhinoscriptsyntax as rs
    index = rs.LayerOrder("Default")
    if index is not None:
        if index==-1: print("The layer does not display in the Layer dialog.")
        else: print("The layer does display in the Layer dialog.")

  

LayerPrintColor

    
    
    LayerPrintColor(layer, color=None)

Returns or changes the print color of a layer. Layer print colors are
represented as RGB colors.

##### Parameters:

    
    
    layer (str): name of existing layer
    color (color): new print color

##### Returns:

    
    
    color: if color is not specified, the current layer print color
    color: if color is specified, the previous layer print color
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        for layer in layers:
            black = rs.CreateColor((0,0,0))
            if rs.LayerPrintColor(layer)!=black:
                rs.LayerPrintColor(layer, black)

##### See Also:

  * LayerLinetype
  * LayerPrintWidth

  

LayerPrintWidth

    
    
    LayerPrintWidth(layer, width=None)

Returns or changes the print width of a layer. Print width is specified in
millimeters. A print width of 0.0 denotes the "default" print width.

##### Parameters:

    
    
    layer (str): name of existing layer
    width (number, optional): new print width

##### Returns:

    
    
    number: if width is not specified, the current layer print width
    number: if width is specified, the previous layer print width

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        for layer in layers:
            if rs.LayerPrintWidth(layer)!=0:
                rs.LayerPrintWidth(layer, 0)

##### See Also:

  * LayerLinetype
  * LayerPrintColor

  

LayerVisible

    
    
    LayerVisible(layer, visible=None, forcevisible_or_donotpersist=False)

Returns or changes the visible property of a layer.

##### Parameters:

    
    
    layer (str): name of existing layer
    visible (bool, optional): new visible state
    forcevisible_or_donotpersist (bool, optional): if visible is True then turn parent layers on if True.  If visible is False then do not persist if True

##### Returns:

    
    
    bool: if visible is not specified, the current layer visibility
    bool: if visible is specified, the previous layer visibility

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        for layer in layers:
            if rs.LayerVisible(layer)==False:
                rs.LayerVisible(layer,True)

##### See Also:

  * LayerLocked

  

ParentLayer

    
    
    ParentLayer(layer, parent=None)

Return or modify the parent layer of a layer

##### Parameters:

    
    
    layer (str): name of an existing layer
    parent (str, optional):  name of new parent layer. To remove the parent layer,
      thus making a root-level layer, specify an empty string

##### Returns:

    
    
    str: If parent is not specified, the name of the current parent layer
    str: If parent is specified, the name of the previous parent layer
    None: if the layer does not have a parent

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    for layer in layers:
        parent = rs.ParentLayer(layer)
        print("Layer: {}, Parent: {}".format(layer, parent))

##### See Also:

  * LayerChildren

  

PurgeLayer

    
    
    PurgeLayer(layer)

Removes an existing layer from the document. The layer will be removed even if
it contains geometry objects. The layer to be removed cannot be the current
layer empty.

##### Parameters:

    
    
    layer (str|guid): the name or id of an existing empty layer

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.GetString("Layer to purge")
    if layer: rs.PurgeLayer(layer)

##### See Also:

  * AddLayer
  * CurrentLayer
  * DeleteLayer
  * RenameLayer

  

RenameLayer

    
    
    RenameLayer(oldname, newname)

Renames an existing layer

##### Parameters:

    
    
    oldname (str): original layer name
    newname (str): new layer name

##### Returns:

    
    
    str: The new layer name if successful otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    oldname = rs.GetString("Old layer name")
    if oldname:
        newname = rs.GetString("New layer name")
        if newname: rs.RenameLayer(oldname, newname)

##### See Also:

  * AddLayer
  * CurrentLayer
  * DeleteLayer

  

## light

AddDirectionalLight

    
    
    AddDirectionalLight(start_point, end_point)

Adds a new directional light object to the document

##### Parameters:

    
    
    start_point(point): starting point of the light
    end_point (point): ending point and direction of the light

##### Returns:

    
    
    (guid): identifier of the new object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    end = rs.GetPoint("End of light vector direction")
    if end:
        start = rs.GetPoint("Start of light vector direction", end)
        if start: rs.AddDirectionalLight( start, end )

##### See Also:

  * IsDirectionalLight

  

AddLinearLight

    
    
    AddLinearLight(start_point, end_point, width=None)

Adds a new linear light object to the document

##### Parameters:

    
    
    start_point (point): starting point of the light
    end_point (point): ending point and direction of the light
    width (number): width of the light

##### Returns:

    
    
    guid: identifier of the new object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    start = rs.GetPoint("Light origin")
    if start:
        end = rs.GetPoint("Light length and direction", start)
        if end: rs.AddLinearLight(start, end)

##### See Also:

  * IsLinearLight

  

AddPointLight

    
    
    AddPointLight(point)

Adds a new point light object to the document

##### Parameters:

    
    
    point (point): the 3d location of the point

##### Returns:

    
    
    guid: identifier of the new object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.GetPoint("Point light location")
    if point: rs.AddPointLight(point)

##### See Also:

  * IsPointLight

  

AddRectangularLight

    
    
    AddRectangularLight(origin, width_point, height_point)

Adds a new rectangular light object to the document

##### Parameters:

    
    
    origin (point): 3d origin point of the light
    width_point (point): 3d width and direction point of the light
    height_point (point): 3d height and direction point of the light

##### Returns:

    
    
    guid: identifier of the new object if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rect = rs.GetRectangle(2)
    if rect: rs.AddRectangularLight( rect[0], rect[1], rect[3] )

##### See Also:

  * IsRectangularLight

  

AddSpotLight

    
    
    AddSpotLight(origin, radius, apex_point)

Adds a new spot light object to the document

##### Parameters:

    
    
    origin (point): 3d origin point of the light
    radius (number):  radius of the cone
    apex_point (point): 3d apex point of the light

##### Returns:

    
    
    guid: identifier of the new object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = 5.0
    origin = rs.GetPoint("Base of cone")
    if origin:
        apex = rs.GetPoint("End of cone", origin)
        if apex: rs.AddSpotLight(origin, radius, apex)

##### See Also:

  * IsSpotLight
  * SpotLightHardness
  * SpotLightShadowIntensity

  

EnableLight

    
    
    EnableLight(object_id, enable=None)

Enables or disables a light object

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    enable (bool, optional): the light's enabled status

##### Returns:

    
    
    bool: if enable is not specified, the current enabled status
    bool: if enable is specified, the previous enabled status
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select light", rs.filter.light)
    if id: rs.EnableLight( id, False )

##### See Also:

  * IsLight
  * IsLightEnabled
  * LightColor
  * LightCount
  * LightName
  * LightObjects

  

IsDirectionalLight

    
    
    IsDirectionalLight(object_id)

Verifies a light object is a directional light

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsDirectionalLight(id):
        print("The object is a directional light.")
    else:
        print("The object is not a directional light.")

##### See Also:

  * AddDirectionalLight

  

IsLight

    
    
    IsLight(object_id)

Verifies an object is a light object

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light")
    if rs.IsLight(id):
        print("The object is a light.")
    else:
        print("The object is not a light.")

##### See Also:

  * EnableLight
  * IsLightEnabled
  * LightColor
  * LightCount
  * LightName
  * LightObjects

  

IsLightEnabled

    
    
    IsLightEnabled(object_id)

Verifies a light object is enabled

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsLightEnabled(id):
        print("The light is enabled (on).")
    else:
        print("The light is disabled (off).")

##### See Also:

  * EnableLight
  * IsLight
  * LightColor
  * LightCount
  * LightName
  * LightObjects

  

IsLightReference

    
    
    IsLightReference(object_id)

Verifies a light object is referenced from another file

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsLightReference(id):
        print("The light is a reference object.")
    else:
        print("The light is not a reference object.")

##### See Also:

  * IsObjectReference

  

IsLinearLight

    
    
    IsLinearLight(object_id)

Verifies a light object is a linear light

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsLinearLight(id):
        print("The object is a linear light.")
    else:
        print("The object is not a linear light.")

##### See Also:

  * AddLinearLight

  

IsPointLight

    
    
    IsPointLight(object_id)

Verifies a light object is a point light

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsPointLight(id):
        print("The object is a point light.")
    else:
        print("The object is not a point light.")

##### See Also:

  * AddPointLight

  

IsRectangularLight

    
    
    IsRectangularLight(object_id)

Verifies a light object is a rectangular light

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsRectangularLight(id):
        print("The object is a rectangular light.")
    else:
        print("The object is not a rectangular light.")

##### See Also:

  * AddRectangularLight

  

IsSpotLight

    
    
    IsSpotLight(object_id)

Verifies a light object is a spot light

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if rs.IsSpotLight(id):
        print("The object is a spot light.")
    else:
        print("The object is not a spot light.")

##### See Also:

  * AddSpotLight
  * SpotLightHardness
  * SpotLightShadowIntensity

  

LightColor

    
    
    LightColor(object_id, color=None)

Returns or changes the color of a light

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    color (color, optional): the light's new color

##### Returns:

    
    
    color: if color is not specified, the current color
    color: if color is specified, the previous color

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id: rs.LightColor( id, (0,255,255) )

##### See Also:

  * EnableLight
  * IsLight
  * IsLightEnabled
  * LightCount
  * LightName
  * LightObjects

  

LightCount

    
    
    LightCount()

Returns the number of light objects in the document

##### Returns:

    
    
    number: the number of light objects in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("There are {} lights".format(rs.LightCount()))

##### See Also:

  * EnableLight
  * IsLight
  * IsLightEnabled
  * LightColor
  * LightName
  * LightObjects

  

LightDirection

    
    
    LightDirection(object_id, direction=None)

Returns or changes the direction of a light object

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    direction (vector, optional): the light's new direction

##### Returns:

    
    
    vector: if direction is not specified, the current direction
    vector: if direction is specified, the previous direction

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id: print( rs.LightDirection(id) )

##### See Also:

  * IsLight
  * LightLocation

  

LightLocation

    
    
    LightLocation(object_id, location=None)

Returns or changes the location of a light object

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    location (point, optional): the light's new location

##### Returns:

    
    
    point: if location is not specified, the current location
    point: if location is specified, the previous location

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id: rs.AddPoint( rs.LightLocation(id) )

##### See Also:

  * IsLight
  * LightDirection

  

LightName

    
    
    LightName(object_id, name=None)

Returns or changes the name of a light object

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    name (str, optional): the light's new name

##### Returns:

    
    
    str: if name is not specified, the current name
    str: if name is specified, the previous name

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id:
        name = rs.GetString("New light name")
        if name: rs.LightName(id, name)

##### See Also:

  * EnableLight
  * IsLight
  * IsLightEnabled
  * LightColor
  * LightCount
  * LightObjects

  

LightObjects

    
    
    LightObjects()

Returns list of identifiers of light objects in the document

##### Returns:

    
    
    list(guid, ...): the list of identifiers of light objects in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    lights = rs.LightObjects()
    if lights:
        rs.AddLayer( "Lights" )
        for light in lights: rs.ObjectLayer( light, "Lights" )

##### See Also:

  * EnableLight
  * IsLight
  * IsLightEnabled
  * LightColor
  * LightCount
  * LightName

  

RectangularLightPlane

    
    
    RectangularLightPlane(object_id)

Returns the plane of a rectangular light object

##### Parameters:

    
    
    object_id (guid): the light object's identifier

##### Returns:

    
    
    plane: the plane if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a rectangular light", rs.filter.light)
    if id:
        rc = rs.RectangularLightPlane(id)
        if rc:
            plane, extents = rc
            rs.AddPlaneSurface( plane, extents[0], extents[1] )

##### See Also:

  * IsRectangularLight

  

SpotLightHardness

    
    
    SpotLightHardness(object_id, hardness=None)

Returns or changes the hardness of a spot light. Spotlight hardness controls
the fully illuminated region.

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    hardness (number, optional): the light's new hardness

##### Returns:

    
    
    number: if hardness is not specified, the current hardness
    number: if hardness is specified, the previous hardness

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id: rs.SpotLightHardness(id, 0.75)

##### See Also:

  * AddSpotLight
  * IsSpotLight
  * SpotLightRadius
  * SpotLightShadowIntensity

  

SpotLightRadius

    
    
    SpotLightRadius(object_id, radius=None)

Returns or changes the radius of a spot light.

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    radius (number, optional): the light's new radius

##### Returns:

    
    
    number: if radius is not specified, the current radius
    number: if radius is specified, the previous radius

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id: rs.SpotLightRadius(id, 5.0)

##### See Also:

  * AddSpotLight
  * IsSpotLight
  * SpotLightHardness
  * SpotLightShadowIntensity

  

SpotLightShadowIntensity

    
    
    SpotLightShadowIntensity(object_id, intensity=None)

Returns or changes the shadow intensity of a spot light.

##### Parameters:

    
    
    object_id (guid): the light object's identifier
    intensity (number, optional): the light's new intensity

##### Returns:

    
    
    number: if intensity is not specified, the current intensity
    number: if intensity is specified, the previous intensity

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select a light", rs.filter.light)
    if id: rs.SpotLightShadowIntensity(id, 0.75)

##### See Also:

  * AddSpotLight
  * IsSpotLight
  * SpotLightHardness
  * SpotLightRadius

  

## line

LineClosestPoint

    
    
    LineClosestPoint(line, testpoint)

Finds the point on an infinite line that is closest to a test point

##### Parameters:

    
    
    line ([point, point]): List of 6 numbers or 2 Point3d.  Two 3-D points identifying the starting and ending points of the line.
    testpoint (point): List of 3 numbers or Point3d.  The test point.

##### Returns:

    
    
    point: the point on the line that is closest to the test point if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    line = (0,0,0), (5,5,0)
    point = (15, 10, 0)
    result = rs.LineClosestPoint( line, point)
    if result: rs.AddPoint(result)

##### See Also:

  * LineIsFartherThan
  * LineMaxDistanceTo
  * LineMinDistanceTo
  * LinePlane
  * LineTransform

  

LineCylinderIntersection

    
    
    LineCylinderIntersection(line, cylinder_plane, cylinder_height, cylinder_radius)

Calculates the intersection of a line and a cylinder

##### Parameters:

    
    
    line (guid|line): the line to intersect
    cylinder_plane (plane): base plane of the cylinder
    cylinder_height (number): height of the cylinder
    cylinder_radius (number): radius of the cylinder

##### Returns:

    
    
    list(point, ...): list of intersection points (0, 1, or 2 points)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.WorldXYPlane()
    line = (-10,0,0), (10,0,10)
    points = rs.LineCylinderIntersection(line, plane, cylinder_height=10, cylinder_radius=5)
    if points:
        for point in points: rs.AddPoint(point)

##### See Also:

  * LineLineIntersection
  * LinePlaneIntersection
  * LineSphereIntersection

  

LineIsFartherThan

    
    
    LineIsFartherThan(line, distance, point_or_line)

Determines if the shortest distance from a line to a point or another line is
greater than a specified distance

##### Parameters:

    
    
    line (line | [point, point]): List of 6 numbers, 2 Point3d, or Line.
    distance (number): the distance
    point_or_line (point|line) the test point or the test line

##### Returns:

    
    
    bool: True if the shortest distance from the line to the other project is
          greater than distance, False otherwise
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    line = (0,0,0), (10,10,0)
    testPoint = (10,5,0)
    print(rs.LineIsFartherThan(line, 3, testPoint))

##### See Also:

  * LineClosestPoint
  * LineMaxDistanceTo
  * LineMinDistanceTo
  * LinePlane
  * LineTransform

  

LineLineIntersection

    
    
    LineLineIntersection(lineA, lineB)

Calculates the intersection of two non-parallel lines. Note, the two lines do
not have to intersect for an intersection to be found. (see help)

##### Parameters:

    
    
    lineA, lineB (line): lines to intersect

##### Returns:

    
    
    tuple(point, point): containing a point on the first line and a point on the second line if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    lineA = (1,1,0), (5,0,0)
    lineB = (1,3,0), (5,5,0)
    point = rs.LineLineIntersection(lineA, lineB)
    if point:
        rs.AddPoint(point[0])
        rs.AddPoint(point[1])

##### See Also:

  * IntersectPlanes
  * LinePlaneIntersection
  * PlanePlaneIntersection

  

LineMaxDistanceTo

    
    
    LineMaxDistanceTo(line, point_or_line)

Finds the longest distance between a line as a finite chord, and a point or
another line

##### Parameters:

    
    
    line (line | [point, point]): List of 6 numbers, two Point3d, or Line.
    point_or_line (point|line): the test point or test line.

##### Returns:

    
    
    number: A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P).
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    line = (0,0,0), (10,10,0)
    print(rs.LineMaxDistanceTo( line, (10,5,0) ))

##### See Also:

  * LineClosestPoint
  * LineIsFartherThan
  * LineMinDistanceTo
  * LinePlane
  * LineTransform

  

LineMinDistanceTo

    
    
    LineMinDistanceTo(line, point_or_line)

Finds the shortest distance between a line as a finite chord, and a point or
another line

##### Parameters:

    
    
    line (line | [point, point]): List of 6 numbers, two Point3d, or Line.
    point_or_line (point|line): the test point or test line.

##### Returns:

    
    
    number: A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P).
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    line = (0,0,0), (10,10,0)
    print(rs.LineMinDistanceTo(line, (10,5,0)))

##### See Also:

  * LineClosestPoint
  * LineIsFartherThan
  * LineMaxDistanceTo
  * LinePlane
  * LineTransform

  

LinePlane

    
    
    LinePlane(line)

Returns a plane that contains the line. The origin of the plane is at the
start of the line. If possible, a plane parallel to the world XY, YZ, or ZX
plane is returned

##### Parameters:

    
    
    line (line | [point, point]):  List of 6 numbers, two Point3d, or Line.

##### Returns:

    
    
    plane: the plane if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    lineFrom = (0,0,0)
    lineTo = (10,10,0)
    distance = rs.Distance(lineFrom, lineTo)
    plane = rs.LinePlane([lineFrom, lineTo])
    rs.AddPlaneSurface( plane, distance, distance )

##### See Also:

  * LineClosestPoint
  * LineIsFartherThan
  * LineMaxDistanceTo
  * LineMinDistanceTo
  * LineTransform

  

LinePlaneIntersection

    
    
    LinePlaneIntersection(line, plane)

Calculates the intersection of a line and a plane.

##### Parameters:

    
    
    line ([point, point]): Two 3D points identifying the starting and ending points of the line to intersect.
    plane (plane): The plane to intersect.

##### Returns:

    
    
    point: The 3D point of intersection is successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.WorldXYPlane()
    line = (2, 11, 13), (20, 4, -10)
    point = rs.LinePlaneIntersection(line, plane)
    if( point!=None ): rs.AddPoint(point)

##### See Also:

  * LineLineIntersection
  * PlanePlaneIntersection

  

LineSphereIntersection

    
    
    LineSphereIntersection(line, sphere_center, sphere_radius)

Calculates the intersection of a line and a sphere

##### Parameters:

    
    
    line (line | [point, point]): the line
    sphere_center (point): the center point of the sphere
    sphere_radius (number): the radius of the sphere

##### Returns:

    
    
    list(point, ...): list of intersection points if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = 10
    line = (-10,0,0), (10,0,10)
    points = rs.LineSphereIntersection(line, (0,0,0), radius)
    if points:
        for point in points: rs.AddPoint(point)

##### See Also:

  * LineCylinderIntersection
  * LineLineIntersection
  * LinePlaneIntersection

  

LineTransform

    
    
    LineTransform(line, xform)

Transforms a line

##### Parameters:

    
    
    line (guid): the line to transform
    xform (transform): the transformation to apply

##### Returns:

    
    
    guid: transformed line

##### Example:

    
    
    import rhinoscriptsyntax as rs
    line = (0,0,0), (10,10,0)
    rs.AddLine( line[0], line[1] )
    plane = rs.WorldXYPlane()
    xform = rs.XformRotation(30, plane.Zaxis, plane.Origin)
    line = rs.LineTransform(line, xform)
    rs.AddLine( line.From, line.To )

##### See Also:

  * LineClosestPoint
  * LineIsFartherThan
  * LineMaxDistanceTo
  * LineMinDistanceTo
  * LinePlane

  

## linetype

IsLinetype

    
    
    IsLinetype(name_or_id)

Verifies the existance of a linetype in the document

##### Parameters:

    
    
    name_or_id (guid|str): The name or identifier of an existing linetype.

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = rs.GetString("Linetype name")
    if rs.IsLinetype(name): print("The linetype exists.")
    else: print("The linetype does not exist")

##### See Also:

  * IsLinetypeReference

  

IsLinetypeReference

    
    
    IsLinetypeReference(name_or_id)

Verifies that an existing linetype is from a reference file

##### Parameters:

    
    
    name_or_id (guid|str): The name or identifier of an existing linetype.

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = rs.GetString("Linetype name")
    if rs.IsLinetype(name):
        if rs.IsLinetypeReference(name):
            print("The linetype is a reference linetype.")
        else:
            print("The linetype is not a reference linetype.")
    else:
        print("The linetype does not exist.")

##### See Also:

  * IsLinetype

  

LinetypeCount

    
    
    LinetypeCount()

Returns number of linetypes in the document

##### Returns:

    
    
    number: the number of linetypes in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.LinetypeCount()
    print("There are {} linetypes".format(count))

##### See Also:

  * LinetypeNames

  

LinetypeNames

    
    
    LinetypeNames(sort=False)

Returns names of all linetypes in the document

##### Parameters:

    
    
    sort (bool, optional): return a sorted list of the linetype names

##### Returns:

    
    
    list(str, ...): list of linetype names if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.LinetypeNames()
    if names:
        for name in names: print(name)

##### See Also:

  * LinetypeCount

  

## material

AddMaterialToLayer

    
    
    AddMaterialToLayer(layer)

Add material to a layer and returns the new material's index. If the layer
already has a material, then the layer's current material index is returned

##### Parameters:

    
    
    layer (str): name of an existing layer.

##### Returns:

    
    
    number: Material index of the layer if successful
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.CurrentLayer()
    index = rs.LayerMaterialIndex(layer)
    if index==-1: index = rs.AddMaterialToLayer(layer)

##### See Also:

  * LayerMaterialIndex
  * IsMaterialDefault

  

AddMaterialToObject

    
    
    AddMaterialToObject(object_id)

Adds material to an object and returns the new material's index. If the object
already has a material, the the object's current material index is returned.

##### Parameters:

    
    
    object_id (guid): identifier of an object

##### Returns:

    
    
    number: material index of the object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject()
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index==-1: index = rs.AddMaterialToObject(obj)

##### See Also:

  * IsMaterialDefault
  * ObjectMaterialIndex
  * ObjectMaterialSource

  

CopyMaterial

    
    
    CopyMaterial(source_index, destination_index)

Copies definition of a source material to a destination material

##### Parameters:

    
    
    source_index, destination_index (number): indices of materials to copy

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    src = rs.LayerMaterialIndex("Default")
    dest = rs.LayerMaterialIndex(rs.CurrentLayer())
    if src>=0 and dest>=0 and src!=dest:
        rs.CopyMaterial( src, dest )

##### See Also:

  * LayerMaterialIndex
  * ObjectMaterialIndex

  

IsMaterialDefault

    
    
    IsMaterialDefault(material_index)

Verifies a material is a copy of Rhino's built-in "default" material. The
default material is used by objects and layers that have not been assigned a
material.

##### Parameters:

    
    
    material_index (number): the zero-based material index

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject()
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if rs.IsMaterialDefault(index):
            print("Object is assigned default material.")
        else:
            print("Object is not assigned default material.")

##### See Also:

  * LayerMaterialIndex
  * ObjectMaterialIndex

  

IsMaterialReference

    
    
    IsMaterialReference(material_index)

Verifies a material is referenced from another file

##### Parameters:

    
    
    material_index (number): the zero-based material index

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject()
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if rs.IsMaterialReference(index):
            print("The material is referenced from another file.")
        else:
            print("The material is not referenced from another file.")

##### See Also:

  * IsLayerReference
  * IsLightReference
  * IsObjectReference

  

MatchMaterial

    
    
    MatchMaterial(source, destination)

Copies the material definition from one material to one or more objects

##### Parameters:

    
    
    source (number|guid): source material index -or- identifier of the source object.
      The object must have a material assigned
    destination ([guid, ...]) identifiers(s) of the destination object(s)

##### Returns:

    
    
    number: number of objects that were modified if successful
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select source object")
    if obj and rs.ObjectMaterialIndex(obj)>-1:
        objects = rs.GetObjects("Select destination objects")
        if objects: rs.MatchMaterial( obj, objects )

##### See Also:

  * CopyMaterial
  * LayerMaterialIndex
  * ObjectMaterialIndex

  

MaterialBump

    
    
    MaterialBump(material_index, filename=None)

Returns or modifies a material's bump bitmap filename

##### Parameters:

    
    
    material_index (number): zero based material index
    filename (str, optional): the bump bitmap filename

##### Returns:

    
    
    str: if filename is not specified, the current bump bitmap filename
    str: if filename is specified, the previous bump bitmap filename
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialBump( index, "C:\\Users\\Steve\\Desktop\\bumpimage.png" )

##### See Also:

  * MaterialColor
  * MaterialName
  * MaterialReflectiveColor
  * MaterialShine
  * MaterialTexture
  * MaterialTransparency

  

MaterialColor

    
    
    MaterialColor(material_index, color=None)

Returns or modifies a material's diffuse color.

##### Parameters:

    
    
    material_index (number): zero based material index
    color (color, optional): the new color value

##### Returns:

    
    
    color: if color is not specified, the current material color
    color: if color is specified, the previous material color
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialColor( index, (127, 255, 191) )

##### See Also:

  * MaterialBump
  * MaterialName
  * MaterialReflectiveColor
  * MaterialShine
  * MaterialTexture
  * MaterialTransparency

  

MaterialEnvironmentMap

    
    
    MaterialEnvironmentMap(material_index, filename=None)

Returns or modifies a material's environment bitmap filename.

##### Parameters:

    
    
    material_index (number): zero based material index
    filename (str, optional): the environment bitmap filename

##### Returns:

    
    
    str: if filename is not specified, the current environment bitmap filename
    str: if filename is specified, the previous environment bitmap filename
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialEnvironmentMap( index, "C:\\Users\\Steve\\Desktop\\emapimage.png" )

##### See Also:

  * MaterialBump
  * MaterialTexture
  * MaterialTransparencyMap

  

MaterialName

    
    
    MaterialName(material_index, name=None)

Returns or modifies a material's user defined name

##### Parameters:

    
    
    material_index (number): zero based material index
    name (str, optional): the new name

##### Returns:

    
    
    str: if name is not specified, the current material name
    str: if name is specified, the previous material name
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialName( index, "Fancy_Material" )

##### See Also:

  * MaterialBump
  * MaterialColor
  * MaterialReflectiveColor
  * MaterialShine
  * MaterialTexture
  * MaterialTransparency

  

MaterialReflectiveColor

    
    
    MaterialReflectiveColor(material_index, color=None)

Returns or modifies a material's reflective color.

##### Parameters:

    
    
    material_index (number): zero based material index
    color (color, optional): the new color value

##### Returns:

    
    
    color: if color is not specified, the current material reflective color
    color: if color is specified, the previous material reflective color
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialReflectiveColor( index, (191, 191, 255) )

##### See Also:

  * MaterialBump
  * MaterialColor
  * MaterialName
  * MaterialShine
  * MaterialTexture
  * MaterialTransparency

  

MaterialShine

    
    
    MaterialShine(material_index, shine=None)

Returns or modifies a material's shine value

##### Parameters:

    
    
    material_index (number): zero based material index
    shine (number, optional): the new shine value. A material's shine value ranges from 0.0 to 255.0, with
      0.0 being matte and 255.0 being glossy

##### Returns:

    
    
    number: if shine is not specified, the current material shine value
    number: if shine is specified, the previous material shine value
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    MAX_SHINE = 255.0
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialShine( index, MAX_SHINE/2 )

##### See Also:

  * MaterialBump
  * MaterialColor
  * MaterialName
  * MaterialReflectiveColor
  * MaterialTexture
  * MaterialTransparency

  

MaterialTexture

    
    
    MaterialTexture(material_index, filename=None)

Returns or modifies a material's texture bitmap filename

##### Parameters:

    
    
    material_index (number): zero based material index
    filename (str, optional): the texture bitmap filename

##### Returns:

    
    
    str: if filename is not specified, the current texture bitmap filename
    str: if filename is specified, the previous texture bitmap filename
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialTexture( index, "C:\\Users\\Steve\\Desktop\\textureimage.png" )

##### See Also:

  * MaterialBump
  * MaterialColor
  * MaterialName
  * MaterialReflectiveColor
  * MaterialShine
  * MaterialTransparency

  

MaterialTransparency

    
    
    MaterialTransparency(material_index, transparency=None)

Returns or modifies a material's transparency value

##### Parameters:

    
    
    material_index (number): zero based material index
    transparency (number, optional): the new transparency value. A material's transparency value ranges from 0.0 to 1.0, with
      0.0 being opaque and 1.0 being transparent

##### Returns:

    
    
    number: if transparency is not specified, the current material transparency value
    number: if transparency is specified, the previous material transparency value
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialTransparency( index, 0.50 )

##### See Also:

  * MaterialBump
  * MaterialColor
  * MaterialName
  * MaterialReflectiveColor
  * MaterialShine
  * MaterialTexture

  

MaterialTransparencyMap

    
    
    MaterialTransparencyMap(material_index, filename=None)

Returns or modifies a material's transparency bitmap filename

##### Parameters:

    
    
    material_index (number): zero based material index
    filename (str, optional): the transparency bitmap filename

##### Returns:

    
    
    str: if filename is not specified, the current transparency bitmap filename
    str: if filename is specified, the previous transparency bitmap filename
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1:
            rs.MaterialTransparencyMap( index, "C:\\Users\\Steve\\Desktop\\texture.png" )

##### See Also:

  * MaterialBump
  * MaterialEnvironmentMap
  * MaterialTexture

  

ResetMaterial

    
    
    ResetMaterial(material_index)

Resets a material to Rhino's default material

##### Parameters:

    
    
    material_index (number) zero based material index

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        index = rs.ObjectMaterialIndex(obj)
        if index>-1: rs.ResetMaterial(index)

##### See Also:

  * LayerMaterialIndex
  * ObjectMaterialIndex

  

## mesh

AddMesh

    
    
    AddMesh(vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None)

Add a mesh object to the document

##### Parameters:

    
    
    vertices ([point, ...]) list of 3D points defining the vertices of the mesh
    face_vertices ([[number, number, number], [number, number, number, number], ...]) list containing lists of 3 or 4 numbers that define the
                  vertex indices for each face of the mesh. If the third a fourth vertex
                   indices of a face are identical, a triangular face will be created.
    vertex_normals ([vector, ...], optional) list of 3D vectors defining the vertex normals of
      the mesh. Note, for every vertex, there must be a corresponding vertex
      normal
    texture_coordinates ([[number, number], [number, number], [number, number]], ...], optional): list of 2D texture coordinates. For every
      vertex, there must be a corresponding texture coordinate
    vertex_colors ([color, ...]) a list of color values. For every vertex,
      there must be a corresponding vertex color

##### Returns:

    
    
    guid: Identifier of the new object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vertices = []
    vertices.append((0.0,0.0,0.0))
    vertices.append((5.0, 0.0, 0.0))
    vertices.append((10.0, 0.0, 0.0))
    vertices.append((0.0, 5.0, 0.0))
    vertices.append((5.0, 5.0, 0.0))
    vertices.append((10.0, 5.0, 0.0))
    vertices.append((0.0, 10.0, 0.0))
    vertices.append((5.0, 10.0, 0.0))
    vertices.append((10.0, 10.0, 0.0))
    faceVertices = []
    faceVertices.append((0,1,4,4))
    faceVertices.append((2,4,1,1))
    faceVertices.append((0,4,3,3))
    faceVertices.append((2,5,4,4))
    faceVertices.append((3,4,6,6))
    faceVertices.append((5,8,4,4))
    faceVertices.append((6,4,7,7))
    faceVertices.append((8,7,4,4))
    rs.AddMesh( vertices, faceVertices )

##### See Also:

  * MeshFaces
  * MeshFaceVertices
  * MeshVertexNormals
  * MeshVertices

  

AddPlanarMesh

    
    
    AddPlanarMesh(object_id, delete_input=False)

Creates a planar mesh from a closed, planar curve

##### Parameters:

    
    
    object_id (guid): identifier of a closed, planar curve
    delete_input (bool, optional) if True, delete the input curve defined by object_id

##### Returns:

    
    
    guid: id of the new mesh on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select planar curves to build mesh", rs.filter.curve)
    if obj: rs.AddPlanarMesh(obj)

##### See Also:

  * IsCurveClosed
  * IsCurvePlanar

  

CurveMeshIntersection

    
    
    CurveMeshIntersection(curve_id, mesh_id, return_faces=False)

Calculates the intersection of a curve object and a mesh object

##### Parameters:

    
    
    curve_id (guid): identifier of a curve object
    mesh_id (guid): identifier or a mesh object
    return_faces (bool, optional): return both intersection points and face indices.
      If False, then just the intersection points are returned

##### Returns:

    
    
    list(point, ...): if return_false is omitted or False, then a list of intersection points
    list([point, number], ...): if return_false is True, the a one-dimensional list containing information
      about each intersection. Each element contains the following two elements
        [0] = point of intersection
        [1] = mesh face index where intersection lies
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve to intersect", rs.filter.curve)
    if curve:
        mesh = rs.GetObject("Select mesh to intersect", rs.filter.mesh)
        if mesh:
            cmx = rs.CurveMeshIntersection(curve, mesh, True)
            if cmx:
                for element in cmx:
                    print("{}, Face index = {}".format(element[0], element[1]))
                    rs.AddPoint(element[0])

##### See Also:

  * MeshClosestPoint
  * MeshMeshIntersection

  

DisjointMeshCount

    
    
    DisjointMeshCount(object_id)

Returns number of meshes that could be created by calling SplitDisjointMesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    number: The number of meshes that could be created

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    if rs.DisjointMeshCount(obj)>1: rs.SplitDisjointMesh(obj)

##### See Also:

  * IsMesh
  * SplitDisjointMesh

  

DuplicateMeshBorder

    
    
    DuplicateMeshBorder(mesh_id)

Creates curves that duplicates a mesh border

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object

##### Returns:

    
    
    list(guid, ...): list of curve ids on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    if obj: rs.DuplicateMeshBorder(obj)

##### See Also:

  * DuplicateEdgeCurves
  * DuplicateSurfaceBorder

  

ExplodeMeshes

    
    
    ExplodeMeshes(mesh_ids, delete=False)

Explodes a mesh object, or mesh objects int submeshes. A submesh is a
collection of mesh faces that are contained within a closed loop of unwelded
mesh edges. Unwelded mesh edges are where the mesh faces that share the edge
have unique mesh vertices (not mesh topology vertices) at both ends of the
edge

##### Parameters:

    
    
    mesh_ids ([guid, ...]): list of mesh identifiers
    delete (bool, optional): delete the input meshes

##### Returns:

    
    
    list(guid, ...): List of resulting objects after explode.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh to explode", rs.filter.mesh)
    if rs.IsMesh(obj): rs.ExplodeMeshes(obj)

##### See Also:

  * IsMesh

  

IsMesh

    
    
    IsMesh(object_id)

Verifies if an object is a mesh

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh")
    if rs.IsMesh(obj):
        print("The object is a mesh.")
    else:
        print("The object is not a mesh.")

##### See Also:

  * IsMeshClosed
  * MeshFaceCount
  * MeshFaces
  * MeshVertexCount
  * MeshVertices

  

IsMeshClosed

    
    
    IsMeshClosed(object_id)

Verifies a mesh object is closed

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh", rs.filter.mesh)
    if rs.IsMeshClosed(obj):
        print("The mesh is closed.")
    else:
        print("The mesh is not closed.")

##### See Also:

  * IsMesh

  

IsMeshManifold

    
    
    IsMeshManifold(object_id)

Verifies a mesh object is manifold. A mesh for which every edge is shared by
at most two faces is called manifold. If a mesh has at least one edge that is
shared by more than two faces, then that mesh is called non-manifold

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh", rs.filter.mesh)
    if rs.IsMeshClosed(obj):
        print("The mesh is manifold.")
    else:
        print("The mesh is non-manifold.")

##### See Also:

  * IsMesh
  * IsMeshClosed

  

IsPointOnMesh

    
    
    IsPointOnMesh(object_id, point)

Verifies a point is on a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object
    point (point): test point

##### Returns:

    
    
    bool: True if successful, otherwise False.
    None: on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh")
    if rs.IsMesh(obj):
        point = rs.GetPointOnMesh(strObject, "Pick a test point")
        if point:
            if rs.IsPointOnMesh(obj, point):
                print("The point is on the mesh")
            else:
                print("The point is not on the mesh")

##### See Also:

  * IsMesh
  * MeshClosestPoint

  

JoinMeshes

    
    
    JoinMeshes(object_ids, delete_input=False)

Joins two or or more mesh objects together

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of two or more mesh objects
    delete_input (bool, optional): delete input after joining

##### Returns:

    
    
    guid: identifier of newly created mesh on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select meshes to join", rs.filter.mesh)
    if objs and len(objs)>1: rs.JoinMeshes(objs, True)

##### See Also:

  * JoinCurves
  * JoinSurfaces

  

MeshArea

    
    
    MeshArea(object_ids)

Returns approximate area of one or more mesh objects

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of one or more mesh objects

##### Returns:

    
    
    list(number, number, number): if successful where
      [0] = number of meshes used in calculation
      [1] = total area of all meshes
      [2] = the error estimate
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    if obj:
        area_rc = rs.MeshArea(obj)
        if area_rc: print("Mesh area:{}".format(area_rc[1]))

##### See Also:

  * MeshVolume

  

MeshAreaCentroid

    
    
    MeshAreaCentroid(object_id)

Calculates the area centroid of a mesh object

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    point: representing the area centroid if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    rs.AddPoint( rs.MeshAreaCentroid(obj) )

##### See Also:

  * IsMesh
  * MeshArea
  * MeshVolume
  * MeshVolumeCentroid

  

MeshBooleanDifference

    
    
    MeshBooleanDifference(input0, input1, delete_input=True, tolerance=None)

Performs boolean difference operation on two sets of input meshes

##### Parameters:

    
    
    input0, input1 (guid): identifiers of meshes
    delete_input (bool, optional): delete the input meshes
    tolerance (float, optional): this value is ignored. 
        The parameter is only there to keep the function signature the same, 
        The build in tolerenace always is used.

##### Returns:

    
    
    list(guid, ...): identifiers of newly created meshes

##### Example:

    
    
    import rhinoscriptsyntax as rs
    input0 = rs.GetObjects("Select first set of meshes", rs.filter.mesh)
    if input0:
        input1 = rs.GetObjects("Select second set of meshes", rs.filter.mesh)
        if input1: rs.MeshBooleanDifference(input0, input1)

##### See Also:

  * MeshBooleanIntersection
  * MeshBooleanSplit
  * MeshBooleanUnion

  

MeshBooleanIntersection

    
    
    MeshBooleanIntersection(input0, input1, delete_input=True)

Performs boolean intersection operation on two sets of input meshes

##### Parameters:

    
    
    input0, input1 (guid): identifiers of meshes
    delete_input (bool, optional): delete the input meshes

##### Returns:

    
    
    list(guid, ...): identifiers of new meshes on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    input0 = rs.GetObjects("Select first set of meshes", rs.filter.mesh)
    if input0:
        input1 = rs.GetObjects("Select second set of meshes", rs.filter.mesh)
        if input1: rs.MeshBooleanIntersection(input0, input1)

##### See Also:

  * MeshBooleanDifference
  * MeshBooleanSplit
  * MeshBooleanUnion

  

MeshBooleanSplit

    
    
    MeshBooleanSplit(input0, input1, delete_input=True)

Performs boolean split operation on two sets of input meshes

##### Parameters:

    
    
    input0, input1 (guid): identifiers of meshes
    delete_input (bool, optional): delete the input meshes

##### Returns:

    
    
    list(guid, ...): identifiers of new meshes on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    input0 = rs.GetObjects("Select first set of meshes", rs.filter.mesh)
    if input0:
        input1 = rs.GetObjects("Select second set of meshes", rs.filter.mesh)
        if input1: rs.MeshBooleanSplit(input0, input1)

##### See Also:

  * MeshBooleanDifference
  * MeshBooleanIntersection
  * MeshBooleanUnion

  

MeshBooleanUnion

    
    
    MeshBooleanUnion(mesh_ids, delete_input=True)

Performs boolean union operation on a set of input meshes

##### Parameters:

    
    
    mesh_ids ([guid, ...]): identifiers of meshes
    delete_input (bool, optional): delete the input meshes

##### Returns:

    
    
    list(guid, ...): identifiers of new meshes

##### Example:

    
    
    import rhinoscriptsyntax as rs
    input = rs.GetObjects("Select meshes to union", rs.filter.mesh)
    if input: rs.MeshBooleanUnion(input)

##### See Also:

  * MeshBooleanDifference
  * MeshBooleanIntersection
  * MeshBooleanSplit

  

MeshClosestPoint

    
    
    MeshClosestPoint(object_id, point, maximum_distance=None)

Returns the point on a mesh that is closest to a test point

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object
    point (point): point to test
    maximum_distance (number, optional): upper bound used for closest point calculation.
      If you are only interested in finding a point Q on the mesh when
      point.DistanceTo(Q) < maximum_distance, then set maximum_distance to
      that value

##### Returns:

    
    
    tuple(point, number): containing the results of the calculation where
                          [0] = the 3-D point on the mesh
                          [1] = the index of the mesh face on which the 3-D point lies
    None: on error

##### Example:

    
    
    import rhinocriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    point = rs.GetPoint("Pick test point")
    intersect = rs.MeshClosestPoint(obj, point)
    if intersect: rs.AddPoint(intersect)

##### See Also:

  * MeshFaceCount
  * MeshFaces

  

MeshFaceCenters

    
    
    MeshFaceCenters(mesh_id)

Returns the center of each face of the mesh object

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object

##### Returns:

    
    
    list(point, ...): points defining the center of each face

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    centers = rs.MeshFaceCenters(obj)
    if centers:
        for point in centers: rs.AddPoint(point)

##### See Also:

  * IsMesh
  * MeshFaceCount
  * MeshFaces

  

MeshFaceCount

    
    
    MeshFaceCount(object_id)

Returns total face count of a mesh object

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    number: the number of mesh faces if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    print("Quad faces:{}".format(rs.MeshQuadCount(obj)))
    print("Triangle faces:{}".format(rs.MeshTriangleCount(obj)))
    print("Total faces:{}".format(rs.MeshFaceCount(obj)))

##### See Also:

  * IsMesh
  * MeshFaces
  * MeshVertexCount
  * MeshVertices

  

MeshFaceNormals

    
    
    MeshFaceNormals(mesh_id)

Returns the face unit normal for each face of a mesh object

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object

##### Returns:

    
    
    list(vector, ...): 3D vectors that define the face unit normals of the mesh
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    normals = rs.MeshFaceNormals(obj)
    if normals:
        for vector in normals: print(vector)

##### See Also:

  * MeshHasFaceNormals
  * MeshFaceCount
  * MeshFaces

  

MeshFaces

    
    
    MeshFaces(object_id, face_type=True)

Returns face vertices of a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object
    face_type (bool, optional): The face type to be returned. True = both triangles
      and quads. False = only triangles

##### Returns:

    
    
    list([point, point, point, point], ...): 3D points that define the face vertices of the mesh. If
    face_type is True, then faces are returned as both quads and triangles
    (4 3D points). For triangles, the third and fourth vertex will be
    identical. If face_type is False, then faces are returned as only
    triangles(3 3D points). Quads will be converted to triangles.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    faces = rs.MeshFaces(obj, False)
    if faces:
        rs.EnableRedraw(False)
        i = 0
        while( i<=len(faces) ):
            face = faces[i], faces[i+1], faces[i+2], faces[i]
            rs.AddPolyline( face )
            i += 3
    rs.EnableRedraw(True)

##### See Also:

  * IsMesh
  * MeshFaceCount
  * MeshVertexCount
  * MeshVertices

  

MeshFaceVertices

    
    
    MeshFaceVertices(object_id)

Returns the vertex indices of all faces of a mesh object

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    list((number, number, number, number), ...): containing tuples of 4 numbers that define the vertex indices for
    each face of the mesh. Both quad and triangle faces are returned. If the
    third and fourth vertex indices are identical, the face is a triangle.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    faceVerts = rs.MeshFaceVertices( obj )
    if faceVerts:
        for count, face in enumerate(faceVerts):
            print("face({}) = ({}, {}, {}, {})".format(count, face[0], face[1], face[2], face[3]))

##### See Also:

  * IsMesh
  * MeshFaceCount
  * MeshFaces

  

MeshHasFaceNormals

    
    
    MeshHasFaceNormals(object_id)

Verifies a mesh object has face normals

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh", rs.filter.mesh)
    if rs.MeshHasFaceNormals(obj):
        print("The mesh has face normal.")
    else:
        print("The mesh does not have face normals.")

##### See Also:

  * MeshFaceNormals

  

MeshHasTextureCoordinates

    
    
    MeshHasTextureCoordinates(object_id)

Verifies a mesh object has texture coordinates

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh", rs.filter.mesh)
    if rs.MeshHasTextureCoordinates(obj):
        print("The mesh has texture coordinates.")
    else:
        print("The mesh does not have texture coordinates.")

  

MeshHasVertexColors

    
    
    MeshHasVertexColors(object_id)

Verifies a mesh object has vertex colors

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh", rs.filter.mesh)
    if rs.mesh.MeshHasVertexColors(obj):
        print("The mesh has vertex colors.")
    else:
        print("The mesh does not have vertex colors.")

##### See Also:

  * MeshVertexColors

  

MeshHasVertexNormals

    
    
    MeshHasVertexNormals(object_id)

Verifies a mesh object has vertex normals

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a mesh", rs.filter.mesh)
    if rs.MeshHasVertexNormals(obj):
        print("The mesh has vertex normals.")
    else:
        print("The mesh does not have vertex normals.")

##### See Also:

  * MeshVertexNormals

  

MeshMeshIntersection

    
    
    MeshMeshIntersection(mesh1, mesh2, tolerance=None)

Calculates the intersections of a mesh object with another mesh object

##### Parameters:

    
    
    mesh1, mesh2 (guid): identifiers of meshes
    tolerance (number, optional): the intersection tolerance. Defaults to ModelAbsoluteTolerance * MeshIntersectionsTolerancesCoefficient

##### Returns:

    
    
    list(point, ...): of points that define the vertices of the intersection curves

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh1 = rs.GetObject("Select first mesh to intersect", rs.filter.mesh)
    mesh2 = rs.GetObject("Select second mesh to intersect", rs.filter.mesh)
    results = rs.MeshMeshIntersection(mesh1, mesh2)
    if results:
        for points in results: rs.AddPolyline(points)

##### See Also:

  * CurveMeshIntersection
  * MeshClosestPoint

  

MeshNakedEdgePoints

    
    
    MeshNakedEdgePoints(object_id)

Identifies the naked edge points of a mesh object. This function shows where
mesh vertices are not completely surrounded by faces. Joined meshes, such as
are made by MeshBox, have naked mesh edge points where the sub-meshes are
joined

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    list(bool, ...): of boolean values that represent whether or not a mesh vertex is
    naked or not. The number of elements in the list will be equal to
    the value returned by MeshVertexCount. In which case, the list will
    identify the naked status for each vertex returned by MeshVertices
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    vertices = rs.MeshVertices( obj )
    naked = rs.MeshNakedEdgePoints( obj )
    for i, vertex in enumerate(vertices):
        if naked[i]: rs.AddPoint(vertex)

##### See Also:

  * IsMesh
  * MeshVertexCount
  * MeshVertices

  

MeshOffset

    
    
    MeshOffset(mesh_id, distance)

Makes a new mesh with vertices offset at a distance in the opposite direction
of the existing vertex normals

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object
    distance (number, optional): the distance to offset

##### Returns:

    
    
    guid: identifier of the new mesh object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Select mesh to offset", rs.filter.mesh)
    rs.MeshOffset( mesh, 10.0 )

##### See Also:

  * IsMesh

  

MeshOutline

    
    
    MeshOutline(object_ids, view=None)

Creates polyline curve outlines of mesh objects

##### Parameters:

    
    
    objects_ids ([guid, ...]): identifiers of meshes to outline
    view (str, optional): view to use for outline direction

##### Returns:

    
    
    list(guid, ...): polyline curve identifiers on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select mesh objects to outline", rs.filter.mesh)
    if objs: rs.MeshOutline(objs)

##### See Also:

  * IsMesh

  

MeshQuadCount

    
    
    MeshQuadCount(object_id)

Returns the number of quad faces of a mesh object

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    number: the number of quad mesh faces if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    print("Quad faces:{}".format(rs.MeshQuadCount(obj)))
    print("Triangle faces:{}".format(rs.MeshTriangleCount(obj)))
    print("Total faces:{}".format(rs.MeshFaceCount(obj)))

##### See Also:

  * MeshQuadCount

  

MeshQuadsToTriangles

    
    
    MeshQuadsToTriangles(object_id)

Converts a mesh object's quad faces to triangles

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    if rs.MeshQuadCount(obj)>0:
        rs.MeshQuadsToTriangles(obj)

  

MeshToNurb

    
    
    MeshToNurb(object_id, trimmed_triangles=True, delete_input=False)

Duplicates each polygon in a mesh with a NURBS surface. The resulting surfaces
are then joined into a polysurface and added to the document

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object
    trimmed_triangles (bool, optional): if True, triangles in the mesh will be
      represented by a trimmed plane
    delete_input (bool, optional): delete input object

##### Returns:

    
    
    list(guid, ...): identifiers for the new breps on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    if obj: rs.MeshToNurb(obj)

##### See Also:

  * IsMesh
  * MeshFaces
  * MeshVertices

  

MeshTriangleCount

    
    
    MeshTriangleCount(object_id)

Returns number of triangular faces of a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    number: The number of triangular mesh faces if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    print("Quad faces:{}".format(rs.MeshQuadCount(obj)))
    print("Triangle faces:{}".format(rs.MeshTriangleCount(obj)))
    print("Total faces:{}".format(rs.MeshFaceCount(obj)))

##### See Also:

  * IsMesh

  

MeshVertexColors

    
    
    MeshVertexColors(mesh_id, colors=0)

Returns of modifies vertex colors of a mesh

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object
    colors 9{color, ...], optional) A list of color values. Note, for each vertex, there must
      be a corresponding vertex color. If the value is None, then any
      existing vertex colors will be removed from the mesh

##### Returns:

    
    
    color: if colors is not specified, the current vertex colors
    color: if colors is specified, the previous vertex colors

##### Example:

    
    
    import rhinoscriptsyntax as rs
    import random
           
    def randomcolor():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return r,g,b
           
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    if obj:
        colors = []
        for i in range(rs.MeshVertexCount(obj)): colors.append( randomcolor() )
        rs.MeshVertexColors( obj, colors )

##### See Also:

  * MeshHasVertexColors
  * MeshVertexCount
  * MeshVertices

  

MeshVertexCount

    
    
    MeshVertexCount(object_id)

Returns the vertex count of a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    number: The number of mesh vertices if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    print("Vertex count: {}".format(rs.MeshVertexCount(obj)))

##### See Also:

  * IsMesh
  * MeshFaceCount
  * MeshFaces
  * MeshVertices

  

MeshVertexFaces

    
    
    MeshVertexFaces(mesh_id, vertex_index)

Returns the mesh faces that share a specified mesh vertex

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object
    vertex_index (number): index of the mesh vertex to find faces for

##### Returns:

    
    
    list(number, ...): face indices on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    import random
    def TestMeshVertexFaces():
        mesh = rs.GetObject("Select mesh", rs.filter.mesh)
        vertices = rs.MeshVertices(mesh)
        meshfaces = rs.MeshFaceVertices(mesh)
        vertex = random.randint(0, len(vertices)-1) #some random vertex
        vertex_faces = rs.MeshVertexFaces(mesh, vertex )
        if vertex_faces:
            rs.AddPoint( vertices[vertex] )
            for face_index in vertex_faces:
                face = meshfaces[face_index]
                polyline = []
                polyline.append( vertices[face[0]] )
                polyline.append( vertices[face[1]] )
                polyline.append( vertices[face[2]] )
                if face[2]!=face[3]:
                    polyline.append( vertices[face[3]] )
                polyline.append( polyline[0] )
                rs.AddPolyline(polyline)
           
    TestMeshVertexFaces()

##### See Also:

  * MeshFaces
  * MeshFaceVertices
  * MeshVertices

  

MeshVertexNormals

    
    
    MeshVertexNormals(mesh_id)

Returns the vertex unit normal for each vertex of a mesh

##### Parameters:

    
    
    mesh_id (guid): identifier of a mesh object

##### Returns:

    
    
    list(vector, ...): of vertex normals, (empty list if no normals exist)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    normals = rs.MeshVertexNormals(obj)
    if normals:
        for normal in normals: print(normal)

##### See Also:

  * MeshHasVertexNormals
  * MeshVertexCount
  * MeshVertices

  

MeshVertices

    
    
    MeshVertices(object_id)

Returns the vertices of a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    list(point, ...): vertex points in the mesh

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    vertices = rs.MeshVertices(obj)
    if vertices: rs.AddPointCloud(vertices)

##### See Also:

  * IsMesh
  * MeshFaceCount
  * MeshFaces
  * MeshVertexCount

  

MeshVolume

    
    
    MeshVolume(object_ids)

Returns the approximate volume of one or more closed meshes

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of one or more mesh objects

##### Returns:

    
    
    tuple(number, number, number): containing 3 velues if successful where
         [0] = number of meshes used in volume calculation
         [1] = total volume of all meshes
         [2] = the error estimate
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    if obj and rs.IsMeshClosed(obj):
        volume = rs.MeshVolume(obj)
        if volume: print("Mesh volume:{}".format(volume[1]))

##### See Also:

  * IsMeshClosed
  * MeshArea

  

MeshVolumeCentroid

    
    
    MeshVolumeCentroid(object_id)

Calculates the volume centroid of a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    point: Point3d representing the volume centroid
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    centroid = rs.MeshVolumeCentroid(obj)
    rs.AddPoint( centroid )

##### See Also:

  * IsMesh
  * MeshArea
  * MeshAreaCentroid
  * MeshVolume

  

PullCurveToMesh

    
    
    PullCurveToMesh(mesh_id, curve_id)

Pulls a curve to a mesh. The function makes a polyline approximation of the
input curve and gets the closest point on the mesh for each point on the
polyline. Then it "connects the points" to create a polyline on the mesh

##### Parameters:

    
    
    mesh_id (guid): identifier of mesh that pulls
    curve_id (guid): identifier of curve to pull

##### Returns:

    
    
    guid: identifier new curve on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Select mesh that pulls", rs.filter.mesh)
    curve = rs.GetObject("Select curve to pull", rs.filter.curve)
    rs.PullCurveToMesh( mesh, curve )

##### See Also:

  * IsMesh

  

SplitDisjointMesh

    
    
    SplitDisjointMesh(object_id, delete_input=False)

Splits up a mesh into its unconnected pieces

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object
    delete_input (bool, optional): delete the input object

##### Returns:

    
    
    list(guid, ...): identifiers for the new meshes

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    if rs.DisjointMeshCount(obj)>0: rs.SplitDisjointMesh(obj)

##### See Also:

  * IsMesh
  * DisjointMeshCount

  

UnifyMeshNormals

    
    
    UnifyMeshNormals(object_id)

Fixes inconsistencies in the directions of faces of a mesh

##### Parameters:

    
    
    object_id (guid): identifier of a mesh object

##### Returns:

    
    
    number: the number of faces that were modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select mesh", rs.filter.mesh)
    if rs.IsMesh(obj): rs.UnifyMeshNormals(obj)

##### See Also:

  * IsMesh

  

## object

CopyObject

    
    
    CopyObject(object_id, translation=None)

Copies object from one location to another, or in-place.

##### Parameters:

    
    
    object_id (guid): object to copy
    translation (vector, optional): translation vector to apply

##### Returns:

    
    
    guid: id for the copy if successful
    None: if not able to copy

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object to copy")
    if id:
        start = rs.GetPoint("Point to copy from")
        if start:
            end = rs.GetPoint("Point to copy to", start)
            if end:
                translation = end-start
                rs.CopyObject( id, translation )

##### See Also:

  * CopyObjects

  

CopyObjects

    
    
    CopyObjects(object_ids, translation=None)

Copies one or more objects from one location to another, or in-place.

##### Parameters:

    
    
    object_ids ([guid, ...])list of objects to copy
    translation (vector, optional): list of three numbers or Vector3d representing
                       translation vector to apply to copied set

##### Returns:

    
    
    list(guid, ...): identifiers for the copies if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objectIds = rs.GetObjects("Select objects to copy")
    if objectIds:
        start = rs.GetPoint("Point to copy from")
        if start:
            end = rs.GetPoint("Point to copy to", start)
            if end:
                translation = end-start
                rs.CopyObjects( objectIds, translation )

##### See Also:

  * CopyObject

  

DeleteObject

    
    
    DeleteObject(object_id)

Deletes a single object from the document

##### Parameters:

    
    
    object_id (guid): identifier of object to delete

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object to delete")
    if id: rs.DeleteObject(id)

##### See Also:

  * DeleteObjects

  

DeleteObjects

    
    
    DeleteObjects(object_ids)

Deletes one or more objects from the document

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of objects to delete

##### Returns:

    
    
    number: Number of objects deleted

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object_ids = rs.GetObjects("Select objects to delete")
    if object_ids: rs.DeleteObjects(object_ids)

##### See Also:

  * DeleteObject

  

FlashObject

    
    
    FlashObject(object_ids, style=True)

Causes the selection state of one or more objects to change momentarily so the
object appears to flash on the screen

##### Parameters:

    
    
    object_ids ([guid, ...]) identifiers of objects to flash
    style (bool, optional): If True, flash between object color and selection color.
      If False, flash between visible and invisible

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.ObjectsByLayer("Default")
    if objs: rs.FlashObject(objs)

##### See Also:

  * HideObjects
  * SelectObjects
  * ShowObjects
  * UnselectObjects

  

HideObject

    
    
    HideObject(object_id)

Hides a single object

##### Parameters:

    
    
    object_id (guid): id of object to hide

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object to hide")
    if id: rs.HideObject(id)

##### See Also:

  * HideObjects
  * IsObjectHidden
  * ShowObject
  * ShowObjects

  

HideObjects

    
    
    HideObjects(object_ids)

Hides one or more objects

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of objects to hide

##### Returns:

    
    
    number: Number of objects hidden

##### Example:

    
    
    import rhinoscriptsyntax as rs
    ids = rs.GetObjects("Select objects to hide")
    if ids: rs.HideObjects(ids)

##### See Also:

  * HideObjects
  * IsObjectHidden
  * ShowObject
  * ShowObjects

  

IsLayoutObject

    
    
    IsLayoutObject(object_id)

Verifies that an object is in either page layout space or model space

##### Parameters:

    
    
    object_id (guid): id of an object to test

##### Returns:

    
    
    bool: True if the object is in page layout space
    bool: False if the object is in model space

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if id:
        if rs.IsLayoutObject(id):
            print("The object is in page layout space.")
        else:
            print("The object is in model space.")

##### See Also:

  * IsObject
  * IsObjectReference

  

IsObject

    
    
    IsObject(object_id)

Verifies the existence of an object

##### Parameters:

    
    
    object_id (guid): an object to test

##### Returns:

    
    
    bool: True if the object exists
    bool: False if the object does not exist

##### Example:

    
    
    import rhinoscriptsyntax as rs
    #Do something here...
    if rs.IsObject(id):
        print("The object exists.")
    else:
        print("The object does not exist.")

##### See Also:

  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectHidden

    
    
    IsObjectHidden(object_id)

Verifies that an object is hidden. Hidden objects are not visible, cannot be
snapped to, and cannot be selected

##### Parameters:

    
    
    object_id (guid): The identifier of an object to test

##### Returns:

    
    
    bool: True if the object is hidden
    bool: False if the object is not hidden

##### Example:

    
    
    import rhinoscriptsyntax as rs
    # Do something here...
    if rs.IsObjectHidden(id):
        print("The object is hidden.")
    else:
        print("The object is not hidden.")

##### See Also:

  * IsObject
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectInBox

    
    
    IsObjectInBox(object_id, box, test_mode=True)

Verifies an object's bounding box is inside of another bounding box

##### Parameters:

    
    
    object_id (guid): identifier of an object to be tested
    box ([point, point, point, point, point, point, point, point]): bounding box to test for containment
    test_mode (bool, optional): If True, the object's bounding box must be contained by box
      If False, the object's bounding box must be contained by or intersect box

##### Returns:

    
    
    bool: True if object is inside box
    bool: False is object is not inside box

##### Example:

    
    
    import rhinoscriptsyntax as rs
    box = rs.GetBox()
    if box:
        rs.EnableRedraw(False)
        object_list = rs.AllObjects()
        for obj in object_list:
            if rs.IsObjectInBox(obj, box, False):
                rs.SelectObject( obj )
        rs.EnableRedraw( True )

##### See Also:

  * BoundingBox
  * GetBox

  

IsObjectInGroup

    
    
    IsObjectInGroup(object_id, group_name=None)

Verifies that an object is a member of a group

##### Parameters:

    
    
    object_id (guid): The identifier of an object
    group_name (str, optional): The name of a group. If omitted, the function
      verifies that the object is a member of any group

##### Returns:

    
    
    bool: True if the object is a member of the specified group. If a group_name
      was not specified, the object is a member of some group.
    bool: False if the object is not a member of the specified group. If a
      group_name was not specified, the object is not a member of any group

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if id:
        name = rs.GetString("Group name")
        if name:
            result = rs.IsObjectInGroup(id, name)
            if result:
                print("The object belongs to the group.")
            else:
                print("The object does not belong to the group.")

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectLocked

    
    
    IsObjectLocked(object_id)

Verifies that an object is locked. Locked objects are visible, and can be
snapped to, but cannot be selected

##### Parameters:

    
    
    object_id (guid): The identifier of an object to be tested

##### Returns:

    
    
    bool: True if the object is locked
    bool: False if the object is not locked

##### Example:

    
    
    import rhinoscriptsyntax as rs
    # Do something here...
    if rs.IsObjectLocked(object):
        print("The object is locked.")
    else:
        print("The object is not locked.")

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectNormal

    
    
    IsObjectNormal(object_id)

Verifies that an object is normal. Normal objects are visible, can be snapped
to, and can be selected

##### Parameters:

    
    
    object_id (guid): The identifier of an object to be tested

##### Returns:

    
    
    bool: True if the object is normal
    bool: False if the object is not normal

##### Example:

    
    
    import rhinoscriptsyntax as rs
    #Do something here...
    if rs.IsObjectNormal(object):
        print("The object is normal.")
    else:
        print("The object is not normal.")

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectReference

    
    
    IsObjectReference(object_id)

Verifies that an object is a reference object. Reference objects are objects
that are not part of the current document

##### Parameters:

    
    
    object_id (guid): The identifier of an object to test

##### Returns:

    
    
    bool: True if the object is a reference object
    bool: False if the object is not a reference object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if rs.IsObjectReference(id):
        print("The object is a reference object.")
    else:
        print("The object is not a reference object.")

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectSelectable
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectSelectable

    
    
    IsObjectSelectable(object_id)

Verifies that an object can be selected

##### Parameters:

    
    
    object_id (guid): The identifier of an object to test

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    # Do something here...
    if rs.IsObjectSelectable(object):
    rs.SelectObject( object )

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelected
  * IsObjectSolid

  

IsObjectSelected

    
    
    IsObjectSelected(object_id)

Verifies that an object is currently selected.

##### Parameters:

    
    
    object_id (guid): The identifier of an object to test

##### Returns:

    
    
    int: 0, the object is not selected
    int: 1, the object is selected
    int: 2, the object is entirely persistently selected
    int: 3, one or more proper sub-objects are selected

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject()
    if rs.IsObjectSelected(object):
        print("The object is selected.")
    else:
        print("The object is not selected.")

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSolid

  

IsObjectSolid

    
    
    IsObjectSolid(object_id)

Determines if an object is closed, solid

##### Parameters:

    
    
    object_id (guid): The identifier of an object to test

##### Returns:

    
    
    bool: True if the object is solid, or a mesh is closed.
    bool: False otherwise.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if rs.IsObjectSolid(id):
        print("The object is solid.")
    else:
        print("The object is not solid.")

##### See Also:

  * IsObject
  * IsObjectHidden
  * IsObjectInGroup
  * IsObjectLocked
  * IsObjectNormal
  * IsObjectReference
  * IsObjectSelectable
  * IsObjectSelected

  

IsObjectValid

    
    
    IsObjectValid(object_id)

Verifies an object's geometry is valid and without error

##### Parameters:

    
    
    object_id (guid): The identifier of an object to test

##### Returns:

    
    
    bool: True if the object is valid

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if rs.IsObjectValid(id):
        print("The object is valid.")
    else:
        print("The object is not valid.")

##### See Also:

  * IsObject

  

IsVisibleInView

    
    
    IsVisibleInView(object_id, view=None)

Verifies an object is visible in a view

##### Parameters:

    
    
    object_id (guid): the identifier of an object to test
    view (str, optional): he title of the view.  If omitted, the current active view is used.

##### Returns:

    
    
    bool: True if the object is visible in the specified view, otherwise False.  None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if rs.IsObject(obj):
        view = rs.CurrentView()
        if rs.IsVisibleInView(obj, view):
            print("The object is visible in {}.".format(view))
        else:
            print("The object is not visible in {}.".format(view))

##### See Also:

  * IsObject
  * IsView

  

LockObject

    
    
    LockObject(object_id)

Locks a single object. Locked objects are visible, and they can be snapped to.
But, they cannot be selected.

##### Parameters:

    
    
    object_id (guid): The identifier of an object

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object to lock")
    if id: rs.LockObject(id)

##### See Also:

  * IsObjectLocked
  * LockObjects
  * UnlockObject
  * UnlockObjects

  

LockObjects

    
    
    LockObjects(object_ids)

Locks one or more objects. Locked objects are visible, and they can be snapped
to. But, they cannot be selected.

##### Parameters:

    
    
    object_ids ([guid, ...]): list of Strings or Guids. The identifiers of objects

##### Returns:

    
    
    number: number of objects locked

##### Example:

    
    
    import rhinoscriptsyntax as rs
    ids = rs.GetObjects("Select objects to lock")
    if ids: rs.LockObjects(ids)

##### See Also:

  * IsObjectLocked
  * LockObject
  * UnlockObject
  * UnlockObjects

  

MatchObjectAttributes

    
    
    MatchObjectAttributes(target_ids, source_id=None)

Matches, or copies the attributes of a source object to a target object

##### Parameters:

    
    
    target_ids ([guid, ...]): identifiers of objects to copy attributes to
    source_id (guid, optional): identifier of object to copy attributes from. If None,
      then the default attributes are copied to the target_ids

##### Returns:

    
    
    number: number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    targets = rs.GetObjects("Select objects")
    if targets:
        source = rs.GetObject("Select object to match")
        if source: rs.MatchObjectAttributes( targets, source )

##### See Also:

  * GetObject
  * GetObjects

  

MirrorObject

    
    
    MirrorObject(object_id, start_point, end_point, copy=False)

Mirrors a single object

##### Parameters:

    
    
    object_id (guid): The identifier of an object to mirror
    start_point (point): start of the mirror plane
    end_point (point): end of the mirror plane
    copy (bool, optional): copy the object

##### Returns:

    
    
    guid: Identifier of the mirrored object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to mirror")
    if obj:
        start = rs.GetPoint("Start of mirror plane")
        end = rs.GetPoint("End of mirror plane")
        if start and end:
            rs.MirrorObject( obj, start, end, True )

##### See Also:

  * MirrorObjects

  

MirrorObjects

    
    
    MirrorObjects(object_ids, start_point, end_point, copy=False)

Mirrors a list of objects

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of objects to mirror
    start_point (point): start of the mirror plane
    end_point (point): end of the mirror plane
    copy (bool, optional): copy the objects

##### Returns:

    
    
    list(guid, ...): List of identifiers of the mirrored objects if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to mirror")
    if objs:
        start = rs.GetPoint("Start of mirror plane")
        end = rs.GetPoint("End of mirror plane")
        if start and end:
            rs.MirrorObjects( objs, start, end, True )

##### See Also:

  * MirrorObject

  

MoveObject

    
    
    MoveObject(object_id, translation)

Moves a single object

##### Parameters:

    
    
    object_id (guid): The identifier of an object to move
    translation (vector): list of 3 numbers or Vector3d

##### Returns:

    
    
    guid: Identifier of the moved object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object to move")
    if id:
        start = rs.GetPoint("Point to move from")
        if start:
            end = rs.GetPoint("Point to move to")
            if end:
                translation = end-start
                rs.MoveObject(id, translation)

##### See Also:

  * MoveObjects

  

MoveObjects

    
    
    MoveObjects(object_ids, translation)

Moves one or more objects

##### Parameters:

    
    
    object_ids ([guid, ...]): The identifiers objects to move
    translation (vector): list of 3 numbers or Vector3d

##### Returns:

    
    
    list(guid, ...): identifiers of the moved objects if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    ids = rs.GetObjects("Select objects to move")
    if ids:
        start = rs.GetPoint("Point to move from")
        if start:
            end = rs.GetPoint("Point to move to")
            if end:
                translation = end-start
                rs.MoveObjects( ids, translation )

##### See Also:

  * MoveObject

  

ObjectColor

    
    
    ObjectColor(object_ids, color=None)

Returns of modifies the color of an object. Object colors are represented as
RGB colors. An RGB color specifies the relative intensity of red, green, and
blue to cause a specific color to be displayed

##### Parameters:

    
    
    object_ids ([guid, ...]): id or ids of object(s)
    color (color, optional): the new color value. If omitted, then current object
        color is returned. If object_ids is a list, color is required

##### Returns:

    
    
    color: If color value is not specified, the current color value
    color: If color value is specified, the previous color value
    number: If object_ids is a list, then the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to change color")
    if objs:
        color = rs.GetColor(0)
        if color:
            for obj in objs: rs.ObjectColor( obj, color )

##### See Also:

  * ObjectColorSource
  * ObjectsByColor

  

ObjectColorSource

    
    
    ObjectColorSource(object_ids, source=None)

Returns of modifies the color source of an object.

##### Parameters:

    
    
    object_ids ([guid, ...]): single identifier of list of identifiers
    source (number, optional) = new color source
        0 = color from layer
        1 = color from object
        2 = color from material
        3 = color from parent

##### Returns:

    
    
    if color source is not specified, the current color source
    is color source is specified, the previous color source
    if color_ids is a list, then the number of objects modifief

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to reset color source")
    if objs:
        for obj In objs: rs.ObjectColorSource(obj, 0)

##### See Also:

  * ObjectColor

  

ObjectDescription

    
    
    ObjectDescription(object_id)

Returns a short text description of an object

##### Parameters:

    
    
    object_id = identifier of an object

##### Returns:

    
    
    A short text description of the object if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        description = rs.ObjectDescription(obj)
        print("Object description:"{} .format(description))

##### See Also:

  * ObjectType

  

ObjectGroups

    
    
    ObjectGroups(object_id)

Returns all of the group names that an object is assigned to

##### Parameters:

    
    
    object_id ([guid, ...]): identifier of an object(s)

##### Returns:

    
    
    list(str, ...): list of group names on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        groups = rs.ObjectGroups(obj)
        if groups:
            for group in groups: print("Object group: {}".format(group))
        else:
            print("No groups.")

##### See Also:

  * ObjectsByGroup

  

ObjectLayer

    
    
    ObjectLayer(object_id, layer=None)

Returns or modifies the layer of an object

##### Parameters:

    
    
    object_id ([guid, ...]) the identifier of the object(s)
    layer (str, optional):  name of an existing layer

##### Returns:

    
    
    str: If a layer is not specified, the object's current layer
    str: If a layer is specified, the object's previous layer
    number: If object_id is a list or tuple, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    id = rs.GetObject("Select object")
    if id: rs.ObjectLayer(id, "Default")

##### See Also:

  * ObjectsByLayer

  

ObjectLayout

    
    
    ObjectLayout(object_id, layout=None, return_name=True)

Returns or changes the layout or model space of an object

##### Parameters:

    
    
    object_id (guid): identifier of the object
    layout (str|guid, optional): to change, or move, an object from model space to page
      layout space, or from one page layout to another, then specify the
      title or identifier of an existing page layout view. To move an object
      from page layout space to model space, just specify None
    return_name[opt] = If True, the name, or title, of the page layout view
      is returned. If False, the identifier of the page layout view is returned

##### Returns:

    
    
    str: if layout is not specified, the object's current page layout view
    str: if layout is specified, the object's previous page layout view
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj: rs.ObjectLayout(obj, "Page 1")

##### See Also:

  * IsLayoutObject
  * IsLayout
  * ViewNames

  

ObjectLinetype

    
    
    ObjectLinetype(object_ids, linetype=None)

Returns of modifies the linetype of an object

##### Parameters:

    
    
    object_ids ({guid, ...]): identifiers of object(s)
    linetype (str, optional): name of an existing linetype. If omitted, the current
      linetype is returned. If object_ids is a list of identifiers, this parameter
      is required

##### Returns:

    
    
    str: If a linetype is not specified, the object's current linetype
    str: If linetype is specified, the object's previous linetype
    number: If object_ids is a list, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj: rs.ObjectLinetype(obj, "Continuous")

##### See Also:

  * ObjectLinetypeSource

  

ObjectLinetypeSource

    
    
    ObjectLinetypeSource(object_ids, source=None)

Returns of modifies the linetype source of an object

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of object(s)
    source (number, optional): new linetype source. If omitted, the current source is returned.
      If object_ids is a list of identifiers, this parameter is required
        0 = By Layer
        1 = By Object
        3 = By Parent

##### Returns:

    
    
    number: If a source is not specified, the object's current linetype source
    number: If source is specified, the object's previous linetype source
    number: If object_ids is a list, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to reset linetype source")
    if objects:
        for obj in objects: rs.ObjectLinetypeSource( obj, 0 )

##### See Also:

  * ObjectLinetype

  

ObjectMaterialIndex

    
    
    ObjectMaterialIndex(object_id, material_index=None)

Returns or changes the material index of an object. Rendering materials are
stored in Rhino's rendering material table. The table is conceptually an
array. Render materials associated with objects and layers are specified by
zero based indices into this array.

##### Parameters:

    
    
    object_id (guid): identifier of an object
    index (number, optional): the new material index

##### Returns:

    
    
    number: If the return value of ObjectMaterialSource is "material by object", then
        the return value of this function is the index of the object's rendering
        material. A material index of -1 indicates no material has been assigned,
        and that Rhino's internal default material has been assigned to the object.
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        source = rs.ObjectMaterialSource(obj)
        if source==0:
            print("The material source is by layer")
        else:
            print("The material source is by object")
            index = rs.ObjectMaterialIndex(obj)
            if index==-1: print("The material is default.")
            else: print("The material is custom.")

##### See Also:

  * ObjectMaterialSource

  

ObjectMaterialSource

    
    
    ObjectMaterialSource(object_ids, source=None)

Returns or modifies the rendering material source of an object.

##### Parameters:

    
    
    object_ids ([guid, ...]): one or more object identifiers
    source (number, optional): The new rendering material source. If omitted and a single
      object is provided in object_ids, then the current material source is
      returned. This parameter is required if multiple objects are passed in
      object_ids
      0 = Material from layer
      1 = Material from object
      3 = Material from parent

##### Returns:

    
    
    number: If source is not specified, the current rendering material source
    number: If source is specified, the previous rendering material source
    number: If object_ids refers to multiple objects, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to reset rendering material source")
    if objects:
        [rs.ObjectMaterialSource(obj, 0) for obj in objects]

##### See Also:

  * ObjectMaterialIndex

  

ObjectName

    
    
    ObjectName(object_id, name=None)

Returns or modifies the name of an object

##### Parameters:

    
    
    object_id ([guid, ...]): id or ids of object(s)
    name (str, optional): the new object name. If omitted, the current name is returned

##### Returns:

    
    
    str: If name is not specified, the current object name
    str: If name is specified, the previous object name
    number: If object_id is a list, the number of objects changed

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(message1="Pick some points")
    if points:
        count = 0
        for point in points:
            obj = rs.AddPoint(point)
            if obj:
                rs.ObjectName( obj, "Point"+str(count) )
                count += 1

##### See Also:

  * ObjectsByName

  

ObjectPrintColor

    
    
    ObjectPrintColor(object_ids, color=None)

Returns or modifies the print color of an object

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of object(s)
    color (color, optional): new print color. If omitted, the current color is returned.

##### Returns:

    
    
    color: If color is not specified, the object's current print color
    color: If color is specified, the object's previous print color
    number: If object_ids is a list or tuple, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to change print color")
    if objects:
        color = rs.GetColor()
        if color:
            for object in objects: rs.ObjectPrintColor(object, color)

##### See Also:

  * ObjectPrintColorSource

  

ObjectPrintColorSource

    
    
    ObjectPrintColorSource(object_ids, source=None)

Returns or modifies the print color source of an object

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of object(s)
    source (number, optional): new print color source
      0 = print color by layer
      1 = print color by object
      3 = print color by parent

##### Returns:

    
    
    number: If source is not specified, the object's current print color source
    number: If source is specified, the object's previous print color source
    number: If object_ids is a list or tuple, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to reset print color source")
    if objects:
        for object in objects: rs.ObjectPrintColorSource(object, 0)

##### See Also:

  * ObjectPrintColor

  

ObjectPrintWidth

    
    
    ObjectPrintWidth(object_ids, width=None)

Returns or modifies the print width of an object

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of object(s)
    width (number, optional): new print width value in millimeters, where width=0 means use
      the default width, and width<0 means do not print (visible for screen display,
      but does not show on print). If omitted, the current width is returned.

##### Returns:

    
    
    number: If width is not specified, the object's current print width
    number: If width is specified, the object's previous print width
    number: If object_ids is a list or tuple, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to change print width")
    if objs:
        for obj in objs: rs.ObjectPrintWidth(obj,0.5)

##### See Also:

  * ObjectPrintWidthSource

  

ObjectPrintWidthSource

    
    
    ObjectPrintWidthSource(object_ids, source=None)

Returns or modifies the print width source of an object

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of object(s)
    source (number, optional): new print width source
      0 = print width by layer
      1 = print width by object
      3 = print width by parent

##### Returns:

    
    
    number: If source is not specified, the object's current print width source
    number: If source is specified, the object's previous print width source
    number: If object_ids is a list or tuple, the number of objects modified

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to reset print width source")
    if objects:
        for obj in objects: rs.ObjectPrintWidthSource(obj,0)

##### See Also:

  * ObjectPrintColor

  

ObjectType

    
    
    ObjectType(object_id)

Returns the object type

##### Parameters:

    
    
    object_id (guid): identifier of an object

##### Returns:

    
    
    number: The object type if successful.
      The valid object types are as follows:
      Value   Description
        0           Unknown object
        1           Point
        2           Point cloud
        4           Curve
        8           Surface or single-face brep
        16          Polysurface or multiple-face
        32          Mesh
        256         Light
        512         Annotation
        4096        Instance or block reference
        8192        Text dot object
        16384       Grip object
        32768       Detail
        65536       Hatch
        131072      Morph control
        134217728   Cage
        268435456   Phantom
        536870912   Clipping plane
        1073741824  Extrusion

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        objtype = rs.ObjectType(obj)
        print("Object type:{}".format(objtype))

##### See Also:

  * ObjectsByType

  

OrientObject

    
    
    OrientObject(object_id, reference, target, flags=0)

Orients a single object based on input points. If two 3-D points are
specified, then this method will function similar to Rhino's Orient command.
If more than two 3-D points are specified, then the function will orient
similar to Rhino's Orient3Pt command. The orient flags values can be added
together to specify multiple options. Value Description 1 Copy object. The
default is not to copy the object. 2 Scale object. The default is not to scale
the object. Note, the scale option only applies if both reference and target
contain only two 3-D points.

##### Parameters:

    
    
    object_id (guid): The identifier of an object
    reference ([point, point, ...]): list of 3-D reference points.
    target  ([point, point, ...]): list of 3-D target points
    flags (number):  1 = copy object
                     2 = scale object
                     3 = copy and scale

##### Returns:

    
    
    guid: The identifier of the oriented object if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to orient")
    if obj:
        reference = rs.GetPoints(message1="First reference point")
        if reference and len(reference)>0:
            target = rs.GetPoints(message1="First target point")
            if target and len(target)>0:
                rs.OrientObject( obj, reference, target )

  

RotateObject

    
    
    RotateObject(object_id, center_point, rotation_angle, axis=None, copy=False)

Rotates a single object

##### Parameters:

    
    
    object_id (guid): The identifier of an object to rotate
    center_point (point): the center of rotation
    rotation_angle (number): in degrees
    axis (plane, optional): axis of rotation, If omitted, the Z axis of the active
      construction plane is used as the rotation axis
    copy (bool, optional): copy the object

##### Returns:

    
    
    guid: Identifier of the rotated object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to rotate")
    if obj:
        point = rs.GetPoint("Center point of rotation")
        if point: rs.RotateObject(obj, point, 45.0, None, copy=True)

##### See Also:

  * RotateObjects

  

RotateObjects

    
    
    RotateObjects( object_ids, center_point, rotation_angle, axis=None, copy=False)

Rotates multiple objects

##### Parameters:

    
    
    object_ids ([guid, ...]): Identifiers of objects to rotate
    center_point (point): the center of rotation
    rotation_angle (number): in degrees
    axis (plane, optional): axis of rotation, If omitted, the Z axis of the active
      construction plane is used as the rotation axis
    copy (bool, optional): copy the object

##### Returns:

    
    
    list(guid, ...): identifiers of the rotated objects if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to rotate")
    if objs:
        point = rs.GetPoint("Center point of rotation")
        if point:
            rs.RotateObjects( objs, point, 45.0, None, True )

##### See Also:

  * RotateObject

  

ScaleObject

    
    
    ScaleObject(object_id, origin, scale, copy=False)

Scales a single object. Can be used to perform a uniform or non-uniform scale
transformation. Scaling is based on the active construction plane.

##### Parameters:

    
    
    object_id (guid): The identifier of an object
    origin (point): the origin of the scale transformation
    scale ([number, number, number]): three numbers that identify the X, Y, and Z axis scale factors to apply
    copy (bool, optional): copy the object

##### Returns:

    
    
    guid: Identifier of the scaled object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to scale")
    if obj:
        origin = rs.GetPoint("Origin point")
        if origin:
            rs.ScaleObject( obj, origin, (1,2,3), True )

##### See Also:

  * ScaleObjects

  

ScaleObjects

    
    
    ScaleObjects(object_ids, origin, scale, copy=False)

Scales one or more objects. Can be used to perform a uniform or non- uniform
scale transformation. Scaling is based on the active construction plane.

##### Parameters:

    
    
    object_ids ([guid, ...]): Identifiers of objects to scale
    origin (point): the origin of the scale transformation
    scale ([number, number, number]): three numbers that identify the X, Y, and Z axis scale factors to apply
    copy (bool, optional): copy the objects

##### Returns:

    
    
    list(guid, ...): identifiers of the scaled objects if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to scale")
    if objs:
        origin = rs.GetPoint("Origin point")
        if origin:
            rs.ScaleObjects( objs, origin, (2,2,2), True )

##### See Also:

  * ScaleObject

  

SelectObject

    
    
    SelectObject(object_id, redraw=True)

Selects a single object

##### Parameters:

    
    
    object_id (guid): the identifier of the object to select

##### Returns:

    
    
    bool: True on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Command( "Line 0,0,0 5,5,0" )
    id = rs.FirstObject()
    if id: rs.SelectObject(id)
    # Do something here...
    rs.UnselectObject(id)

##### See Also:

  * IsObjectSelectable
  * IsObjectSelected
  * SelectObjects
  * UnselectObject
  * UnselectObjects

  

SelectObjects

    
    
    SelectObjects( object_ids)

Selects one or more objects

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of the objects to select

##### Returns:

    
    
    number: number of selected objects

##### Example:

    
    
    import rhinoscriptsyntax as rs
    ids = rs.GetObjects("Select object to copy in-place")
    if ids:
        rs.UnselectObjects(ids)
        copies = rs.CopyObjects(ids)
        if copies: rs.SelectObjects(copies)

##### See Also:

  * IsObjectSelectable
  * IsObjectSelected
  * SelectObject
  * UnselectObject
  * UnselectObjects

  

ShearObject

    
    
    ShearObject(object_id, origin, reference_point, angle_degrees, copy=False)

Perform a shear transformation on a single object

##### Parameters:

    
    
    object_id (guid, ...): The identifier of an object
    origin, reference_point (point) origin/reference point of the shear transformation
    copy (bool, optional): copy the objects

##### Returns:

    
    
    guid: Identifier of the sheared object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to shear")
    if obj:
        origin = rs.GetPoint("Origin point")
        refpt = rs.GetPoint("Reference point")
        if origin and refpt:
            rs.ShearObject(obj, origin, refpt, 45.0, True)

##### See Also:

  * ShearObjects

  

ShearObjects

    
    
    ShearObjects(object_ids, origin, reference_point, angle_degrees, copy=False)

Shears one or more objects

##### Parameters:

    
    
    object_ids ([guid, ...]): The identifiers objects to shear
    origin, reference_point (point): origin/reference point of the shear transformation
    copy (bool, optional): copy the objects

##### Returns:

    
    
    list(guid, ...]): identifiers of the sheared objects if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object_ids = rs.GetObjects("Select objects to shear")
    if object_ids:
        origin = rs.GetPoint("Origin point")
        refpt = rs.GetPoint("Reference point")
        if origin and refpt:
            rs.ShearObjects( object_ids, origin, refpt, 45.0, True )

##### See Also:

  * ShearObject

  

ShowObject

    
    
    ShowObject(object_id)

Shows a previously hidden object. Hidden objects are not visible, cannot be
snapped to and cannot be selected

##### Parameters:

    
    
    object_id (guid): representing id of object to show

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to hide")
    if obj: rs.HideObject(obj)
    # Do something here...
    rs.ShowObject( obj )

##### See Also:

  * HideObject
  * HideObjects
  * IsObjectHidden
  * ShowObjects

  

ShowObjects

    
    
    ShowObjects(object_ids)

Shows one or more objects. Hidden objects are not visible, cannot be snapped
to and cannot be selected

##### Parameters:

    
    
    object_ids ([guid, ...]): ids of objects to show

##### Returns:

    
    
    number: Number of objects shown

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to hide")
    if objs: rs.HideObjects(objs)
    #Do something here...
    rs.ShowObjects( objs )

##### See Also:

  * HideObject
  * HideObjects
  * IsObjectHidden
  * ShowObject

  

TransformObject

    
    
    TransformObject(object_id, matrix, copy=False)

Moves, scales, or rotates an object given a 4x4 transformation matrix. The
matrix acts on the left.

##### Parameters:

    
    
    object (guid): The identifier of the object.
    matrix (transform): The transformation matrix (4x4 array of numbers).
    copy (bool, optional): Copy the object.

##### Returns:

    
    
    (guid): The identifier of the transformed object
    None: if not successful, or on error

##### Example:

    
    
    # Rotate an object by theta degrees about the world Z axis
    import math
    import rhinoscriptsyntax as rs
    degrees = 90.0 # Some angle
    radians = math.radians(degrees)
    c = math.cos(radians)
    s = math.sin(radians)
    matrix = []
    matrix.append( [c,-s, 0, 0] )
    matrix.append( [s, c, 0, 0] )
    matrix.append( [0, 0, 1, 0] )
    matrix.append( [0, 0, 0, 1] )
    obj = rs.GetObject("Select object to rotate")
    if obj: rs.TransformObject( obj, matrix )

##### See Also:

  * TransformObjects

  

TransformObjects

    
    
    TransformObjects(object_ids, matrix, copy=False)

Moves, scales, or rotates a list of objects given a 4x4 transformation matrix.
The matrix acts on the left.

##### Parameters:

    
    
    object_ids [(guid, ...}): List of object identifiers.
    matrix (transform): The transformation matrix (4x4 array of numbers).
    copy (bool, optional): Copy the objects

##### Returns:

    
    
    list(guid, ...): ids identifying the newly transformed objects

##### Example:

    
    
    import rhinoscriptsyntax as rs
    # Translate (move) objects by (10,10,0)
    xform = rs.XformTranslation([10,10,0])
    objs = rs.GetObjects("Select objects to translate")
    if objs: rs.TransformObjects(objs, xform)

##### See Also:

  * TransformObject

  

UnlockObject

    
    
    UnlockObject(object_id)

Unlocks an object. Locked objects are visible, and can be snapped to, but they
cannot be selected.

##### Parameters:

    
    
    object_id (guid): The identifier of an object

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object to lock")
    if obj: rs.LockObject(obj)
    #Do something here...
    rs.UnlockObject( obj )

##### See Also:

  * IsObjectLocked
  * LockObject
  * LockObjects
  * UnlockObjects

  

UnlockObjects

    
    
    UnlockObjects(object_ids)

Unlocks one or more objects. Locked objects are visible, and can be snapped
to, but they cannot be selected.

##### Parameters:

    
    
    object_ids ([guid, ...]): The identifiers of objects

##### Returns:

    
    
    number: number of objects unlocked

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to lock")
    if objs: rs.LockObjects(objs)
    #Do something here...
    rs.UnlockObjects( objs )

##### See Also:

  * IsObjectLocked
  * LockObject
  * LockObjects
  * UnlockObject

  

UnselectObject

    
    
    UnselectObject(object_id)

Unselects a single selected object

##### Parameters:

    
    
    object_id: (guid): id of object to unselect

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Command("Line 0,0,0 5,5,0")
    obj = rs.FirstObject()
    if obj: rs.SelectObject(obj)
    #Do something here...
    rs.UnselectObject( obj )

##### See Also:

  * IsObjectSelected
  * SelectObject
  * SelectObjects
  * UnselectObjects

  

UnselectObjects

    
    
    UnselectObjects(object_ids)

Unselects one or more selected objects.

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of the objects to unselect.

##### Returns:

    
    
    number: The number of objects unselected

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select object to copy in-place")
    if objects:
        rs.UnselectObjects(objects)
        copies= rs.CopyObjects(objects)
        if copies: rs.SelectObjects(copies)

##### See Also:

  * IsObjectSelected
  * SelectObject
  * SelectObjects
  * UnselectObject

  

## plane

DistanceToPlane

    
    
    DistanceToPlane(plane, point)

Returns the distance from a 3D point to a plane

##### Parameters:

    
    
    plane (plane): the plane
    point (point): List of 3 numbers or Point3d

##### Returns:

    
    
    number: The distance if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.GetPoint("Point to test")
    if point:
        plane = rs.ViewCPlane()
        if plane:
            distance = rs.DistanceToPlane(plane, point)
            if distance is not None:
                print("Distance to plane: {}".format(distance))

##### See Also:

  * Distance
  * PlaneClosestPoint

  

EvaluatePlane

    
    
    EvaluatePlane(plane, parameter)

Evaluates a plane at a U,V parameter

##### Parameters:

    
    
    plane (plane): the plane to evaluate
    parameter ([number, number]): list of two numbers defining the U,V parameter to evaluate

##### Returns:

    
    
    point: Point3d on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    plane = rs.ViewCPlane(view)
    point = rs.EvaluatePlane(plane, (5,5))
    rs.AddPoint( point )

##### See Also:

  * PlaneClosestPoint

  

IntersectPlanes

    
    
    IntersectPlanes(plane1, plane2, plane3)

Calculates the intersection of three planes

##### Parameters:

    
    
    plane1 (plane): the 1st plane to intersect
    plane2 (plane): the 2nd plane to intersect
    plane3 (plane): the 3rd plane to intersect

##### Returns:

    
    
    point: the intersection point between the 3 planes on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane1 = rs.WorldXYPlane()
    plane2 = rs.WorldYZPlane()
    plane3 = rs.WorldZXPlane()
    point = rs.IntersectPlanes(plane1, plane2, plane3)
    if point: rs.AddPoint(point)

##### See Also:

  * LineLineIntersection
  * LinePlaneIntersection
  * PlanePlaneIntersection

  

MovePlane

    
    
    MovePlane(plane, origin)

Moves the origin of a plane

##### Parameters:

    
    
    plane (plane): Plane or ConstructionPlane
    origin (point): Point3d or list of three numbers

##### Returns:

    
    
    plane: moved plane

##### Example:

    
    
    import rhinoscriptsyntax as rs
    origin = rs.GetPoint("CPlane origin")
    if origin:
        plane = rs.ViewCPlane()
        plane = rs.MovePlane(plane,origin)
        rs.ViewCplane(plane)

##### See Also:

  * PlaneFromFrame
  * PlaneFromNormal
  * RotatePlane

  

PlaneClosestPoint

    
    
    PlaneClosestPoint(plane, point, return_point=True)

Returns the point on a plane that is closest to a test point.

##### Parameters:

    
    
    plane (plane): The plane
    point (point): The 3-D point to test.
    return_point (bool, optional): If omitted or True, then the point on the plane
       that is closest to the test point is returned. If False, then the
       parameter of the point on the plane that is closest to the test
       point is returned.

##### Returns:

    
    
    point: If return_point is omitted or True, then the 3-D point
    point: If return_point is False, then an array containing the U,V parameters
    of the point
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.GetPoint("Point to test")
    if point:
        plane = rs.ViewCPlane()
        if plane:
            print(rs.PlaneClosestPoint(plane, point))

##### See Also:

  * DistanceToPlane
  * EvaluatePlane

  

PlaneCurveIntersection

    
    
    PlaneCurveIntersection(plane, curve, tolerance=None)

Intersect an infinite plane and a curve object

##### Parameters:

    
    
    plane (plane): The plane to intersect.
    curve (guid): The identifier of the curve object
    torerance (number, optional): The intersection tolerance. If omitted, the document's absolute tolerance is used.

##### Returns:

    
    
    A list of intersection information tuple if successful.  The list will contain one or more of the following tuple:
    
      Element Type        Description
    
      [0]       Number      The intersection event type, either Point (1) or Overlap (2).
    
      [1]       Point3d     If the event type is Point (1), then the intersection point on the curve.
                          If the event type is Overlap (2), then intersection start point on the curve.
    
      [2]       Point3d     If the event type is Point (1), then the intersection point on the curve.
                          If the event type is Overlap (2), then intersection end point on the curve.
    
      [3]       Point3d     If the event type is Point (1), then the intersection point on the plane.
                          If the event type is Overlap (2), then intersection start point on the plane.
    
      [4]       Point3d     If the event type is Point (1), then the intersection point on the plane.
    
                          If the event type is Overlap (2), then intersection end point on the plane.
    
      [5]       Number      If the event type is Point (1), then the curve parameter.
                          If the event type is Overlap (2), then the start value of the curve parameter range.
                                
      [6]       Number      If the event type is Point (1), then the curve parameter.
                          If the event type is Overlap (2),  then the end value of the curve parameter range.
    
      [7]       Number      If the event type is Point (1), then the U plane parameter.
                          If the event type is Overlap (2), then the U plane parameter for curve at (n, 5).
    
      [8]       Number      If the event type is Point (1), then the V plane parameter.
                          If the event type is Overlap (2), then the V plane parameter for curve at (n, 5).
    
      [9]       Number      If the event type is Point (1), then the U plane parameter.
                          If the event type is Overlap (2), then the U plane parameter for curve at (n, 6).
                                
      [10]      Number      If the event type is Point (1), then the V plane parameter.
                          If the event type is Overlap (2), then the V plane parameter for curve at (n, 6).
    
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve", rs.filter.curve)
    if curve:
        plane = rs.WorldXYPlane()
        intersections = rs.PlaneCurveIntersection(plane, curve)
        if intersections:
            for intersection in intersections:
                rs.AddPoint(intersection[1])

##### See Also:

  * IntersectPlanes
  * PlanePlaneIntersection
  * PlaneSphereIntersection

  

PlaneEquation

    
    
    PlaneEquation(plane)

Returns the equation of a plane as a tuple of four numbers. The standard
equation of a plane with a non-zero vector is Ax+By+Cz+D=0

##### Parameters:

    
    
    plane (plane): the plane to deconstruct

##### Returns:

    
    
    tuple(number, number, number, number): containing four numbers that represent the coefficients of the equation  (A, B, C, D) if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.ViewCPlane()
    equation = rs.PlaneEquation(plane)
    print("A = {}".format(equation[0]))
    print("B = {}".format(equation[1]))
    print("C = {}".format(equation[2]))
    print("D = {}".format(equation[3]))

##### See Also:

  * PlaneFromFrame
  * PlaneFromNormal
  * PlaneFromPoints

  

PlaneFitFromPoints

    
    
    PlaneFitFromPoints(points)

Returns a plane that was fit through an array of 3D points.

##### Parameters:

    
    
    points (point): An array of 3D points.

##### Returns:

    
    
    plane: The plane if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints()
    if points:
        plane = rs.PlaneFitFromPoints(points)
        if plane:
            magX = plane.XAxis.Length
            magY = plane.YAxis.Length
            rs.AddPlaneSurface( plane, magX, magY )

##### See Also:

  * PlaneFromFrame
  * PlaneFromNormal
  * PlaneFromPoints

  

PlaneFromFrame

    
    
    PlaneFromFrame(origin, x_axis, y_axis)

Construct a plane from a point, and two vectors in the plane.

##### Parameters:

    
    
    origin (point): A 3D point identifying the origin of the plane.
    x_axis (vector): A non-zero 3D vector in the plane that determines the X axis
             direction.
    y_axis (vector): A non-zero 3D vector not parallel to x_axis that is used
             to determine the Y axis direction. Note, y_axis does not
             have to be perpendicular to x_axis.

##### Returns:

    
    
    plane: The plane if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    origin = rs.GetPoint("CPlane origin")
    if origin:
        xaxis = (1,0,0)
        yaxis = (0,0,1)
        plane = rs.PlaneFromFrame( origin, xaxis, yaxis )
        rs.ViewCPlane(None, plane)

##### See Also:

  * MovePlane
  * PlaneFromNormal
  * PlaneFromPoints
  * RotatePlane

  

PlaneFromNormal

    
    
    PlaneFromNormal(origin, normal, xaxis=None)

Creates a plane from an origin point and a normal direction vector.

##### Parameters:

    
    
    origin (point): A 3D point identifying the origin of the plane.
    normal (vector): A 3D vector identifying the normal direction of the plane.
    xaxis (vector, optional): optional vector defining the plane's x-axis

##### Returns:

    
    
    plane: The plane if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    origin = rs.GetPoint("CPlane origin")
    if origin:
        direction = rs.GetPoint("CPlane direction")
        if direction:
            normal = direction - origin
            normal = rs.VectorUnitize(normal)
            rs.ViewCPlane( None, rs.PlaneFromNormal(origin, normal) )

##### See Also:

  * MovePlane
  * PlaneFromFrame
  * PlaneFromPoints
  * RotatePlane

  

PlaneFromPoints

    
    
    PlaneFromPoints(origin, x, y)

Creates a plane from three non-colinear points

##### Parameters:

    
    
    origin (point): origin point of the plane
    x, y (point): points on the plane's x and y axes

##### Returns:

    
    
    plane: The plane if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    corners = rs.GetRectangle()
    if corners:
        rs.ViewCPlane( rs.PlaneFromPoints(corners[0], corners[1], corners[3]))

##### See Also:

  * PlaneFromFrame
  * PlaneFromNormal

  

PlanePlaneIntersection

    
    
    PlanePlaneIntersection(plane1, plane2)

Calculates the intersection of two planes

##### Parameters:

    
    
    plane1 (plane): the 1st plane to intersect
    plane2 (plane): the 2nd plane to intersect

##### Returns:

    
    
    line:  a line with two 3d points identifying the starting/ending points of the intersection
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane1 = rs.WorldXYPlane()
    plane2 = rs.WorldYZPlane()
    line = rs.PlanePlaneIntersection(plane1, plane2)
    if line: rs.AddLine(line[0], line[1])

##### See Also:

  * IntersectPlanes
  * LineLineIntersection
  * LinePlaneIntersection

  

PlaneSphereIntersection

    
    
    PlaneSphereIntersection(plane, sphere_plane, sphere_radius)

Calculates the intersection of a plane and a sphere

##### Parameters:

    
    
    plane (plane): the plane to intersect
    sphere_plane (plane): equatorial plane of the sphere. origin of the plane is
      the center of the sphere
    sphere_radius (number): radius of the sphere

##### Returns:

    
    
    list(number, point|plane, number): of intersection results
        Element    Type      Description
        [0]       number     The type of intersection, where 0 = point and 1 = circle.
        [1]   point or plane If a point intersection, the a Point3d identifying the 3-D intersection location.
                             If a circle intersection, then the circle's plane. The origin of the plane will be the center point of the circle
        [2]       number     If a circle intersection, then the radius of the circle.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.WorldXYPlane()
    radius = 10
    results = rs.PlaneSphereIntersection(plane, plane, radius)
    if results:
        if results[0]==0:
            rs.AddPoint(results[1])
        else:
            rs.AddCircle(results[1], results[2])

##### See Also:

  * IntersectPlanes
  * LinePlaneIntersection
  * PlanePlaneIntersection

  

PlaneTransform

    
    
    PlaneTransform(plane, xform)

Transforms a plane

##### Parameters:

    
    
    plane (plane): Plane to transform
    xform (transform): Transformation to apply

##### Returns:

    
    
    plane:the resulting plane if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.ViewCPlane()
    xform = rs.XformRotation(45.0, plane.Zaxis, plane.Origin)
    plane = rs.PlaneTransform(plane, xform)
    rs.ViewCPlane(None, plane)

##### See Also:

  * PlaneFromFrame
  * PlaneFromNormal
  * PlaneFromPoints

  

RotatePlane

    
    
    RotatePlane(plane, angle_degrees, axis)

Rotates a plane

##### Parameters:

    
    
    plane (plane): Plane to rotate
    angle_degrees (number): rotation angle in degrees
    axis (vector): Axis of rotation or list of three numbers

##### Returns:

    
    
    plane: rotated plane on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.ViewCPlane()
    rotated = rs.RotatePlane(plane, 45.0, plane.XAxis)
    rs.ViewCPlane( None, rotated )

##### See Also:

  * MovePlane
  * PlaneFromFrame
  * PlaneFromNormal

  

WorldXYPlane

    
    
    WorldXYPlane()

Returns Rhino's world XY plane

##### Returns:

    
    
    plane: Rhino's world XY plane

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    rs.ViewCPlane( view, rs.WorldXYPlane() )

##### See Also:

  * WorldYZPlane
  * WorldZXPlane

  

WorldYZPlane

    
    
    WorldYZPlane()

Returns Rhino's world YZ plane

##### Returns:

    
    
    plane: Rhino's world YZ plane

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    rs.ViewCPlane( view, rs.WorldYZPlane() )

##### See Also:

  * WorldXYPlane
  * WorldZXPlane

  

WorldZXPlane

    
    
    WorldZXPlane()

Returns Rhino's world ZX plane

##### Returns:

    
    
    plane: Rhino's world ZX plane

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    rs.ViewCPlane( view, rs.WorldZXPlane() )

##### See Also:

  * WorldXYPlane
  * WorldYZPlane

  

## pointvector

IsVectorParallelTo

    
    
    IsVectorParallelTo(vector1, vector2)

Compares two vectors to see if they are parallel

##### Parameters:

    
    
    vector1, vector2 (vector): the vectors to compare

##### Returns:

    
    
    number: the value represents
            -1 = the vectors are anti-parallel
             0 = the vectors are not parallel
             1 = the vectors are parallel

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = (1,0,0)
    vector2 = (0,1,0)
    print(rs.IsVectorParallelTo( vector1, vector2 ))

##### See Also:

  * IsVectorPerpendicularTo
  * IsVectorTiny
  * IsVectorZero

  

IsVectorPerpendicularTo

    
    
    IsVectorPerpendicularTo(vector1, vector2)

Compares two vectors to see if they are perpendicular

##### Parameters:

    
    
    vector1, vector2 (vector): the vectors to compare

##### Returns:

    
    
    bool: True if vectors are perpendicular, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = (1,0,0)
    vector2 = (0,1,0)
    print(rs.IsVectorPerpendicularTo( vector1, vector2 ))

##### See Also:

  * IsVectorParallelTo
  * IsVectorTiny
  * IsVectorZero

  

IsVectorTiny

    
    
    IsVectorTiny(vector)

Verifies that a vector is very short. The X,Y,Z elements are <= 1.0e-12

##### Parameters:

    
    
    vector (vector): the vector to check

##### Returns:

    
    
    bool: True if the vector is tiny, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    pt1 = rs.GetPoint("First point")
    pt2 = rs.GetPoint("Next point")
    vector = pt2 - pt1
    if rs.IsVectorTiny(vector):
        print("The vector is tiny.")
    else:
        print("The vector is not tiny.")

##### See Also:

  * IsVectorZero
  * VectorCreate

  

IsVectorZero

    
    
    IsVectorZero(vector)

Verifies that a vector is zero, or tiny. The X,Y,Z elements are equal to 0.0

##### Parameters:

    
    
    vector (vector): the vector to check

##### Returns:

    
    
    bool: True if the vector is zero, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    pt1 = rs.GetPoint("First point")
    pt2 = rs.GetPoint("Next point")
    vector = pt2 - pt1
    if rs.IsVectorZero(vector):
        print("The vector is zero.")
    else:
        print("The vector is not zero.")

##### See Also:

  * IsVectorTiny
  * VectorCreate

  

PointAdd

    
    
    PointAdd(point1, point2)

Adds a 3D point or a 3D vector to a 3D point

##### Parameters:

    
    
    point1, point2 (point): the points to add

##### Returns:

    
    
    point: the resulting 3D point if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = (1,1,1)
    point2 = (2,2,2)
    point = rs.PointAdd(point1, point2)
    print(point)

##### See Also:

  * PointCompare
  * PointDivide
  * PointScale
  * PointSubtract
  * PointTransform

  

PointArrayClosestPoint

    
    
    PointArrayClosestPoint(points, test_point)

Finds the point in a list of 3D points that is closest to a test point

##### Parameters:

    
    
    points ([point, ...]): list of points
    test_point (point): the point to compare against

##### Returns:

    
    
    number: index of the element in the point list that is closest to the test point

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cloud = rs.GetObject("Select point cloud")
    if cloud:
        point = rs.GetPoint("Point to test")
        if point:
            cloud = rs.PointCloudPoints(cloud)
            index = rs.PointArrayClosestPoint(cloud, point)
            if index is not None:
                point_id = rs.AddPoint(cloud[index])
                rs.SelectObject( point_id )

##### See Also:

  * CurveClosestPoint
  * SurfaceClosestPoint

  

PointArrayTransform

    
    
    PointArrayTransform(points, xform)

Transforms a list of 3D points

##### Parameters:

    
    
    points ([point, ...]): list of 3D points
    xform (transform): transformation to apply

##### Returns:

    
    
    list(point, ...): transformed points on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    points = rs.BoundingBox(obj)
    xform = rs.XformRotation2(45.0, (0,0,1), (0,0,0))
    points = rs.PointArrayTransform(points, xform)
    rs.AddPoints(points)

##### See Also:

  * PointArrayClosestPoint

  

PointClosestObject

    
    
    PointClosestObject(point, object_ids)

Finds the object that is closest to a test point

##### Parameters:

    
    
    point (point): point to test
    object_id ([guid, ...]): identifiers of one or more objects

##### Returns:

    
    
    list(guid, point): closest [0] object_id and [1] point on object on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select target objects for closest point", 63)
    if objs:
        point = rs.GetPoint("Test point")
        if point:
            results = rs.PointClosestObject(point, objs)
            if results:
                print("Object id:{}".format(results[0]))
                rs.AddPoint( results[1] )

##### See Also:

  * CurveClosestObject

  

PointCompare

    
    
    PointCompare(point1, point2, tolerance=None)

Compares two 3D points

##### Parameters:

    
    
    point1, point2 (point): the points to compare
    tolerance (number, optional): tolerance to use for comparison. If omitted,
                                  Rhino's internal zero tolerance is used

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = (1,1,1)
    point2 = (2,2,2)
    print(rs.PointCompare(point1, point2))

##### See Also:

  * PointAdd
  * PointDivide
  * PointScale
  * PointSubtract
  * PointTransform

  

PointDivide

    
    
    PointDivide(point, divide)

Divides a 3D point by a value

##### Parameters:

    
    
    point (point): the point to divide
    divide (number): a non-zero value to divide

##### Returns:

    
    
    point: resulting point

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.PointDivide([5,5,0], 5)
    print(point)

##### See Also:

  * PointAdd
  * PointCompare
  * PointScale
  * PointSubtract
  * PointTransform

  

PointsAreCoplanar

    
    
    PointsAreCoplanar(points, tolerance=1.0e-12)

Verifies that a list of 3D points are coplanar

##### Parameters:

    
    
    points ([point, ...]): 3D points to test
    tolerance (number, optional): tolerance to use when verifying

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def SurfacesAreCoplanar(srf1, srf2):
        if( not rs.IsSurface(srf1) or not rs.IsSurface(srf2) ): return False
        if( not rs.IsSurfacePlanar(srf1) or not rs.IsSurfacePlanar(srf2) ): return False
        pts1 = rs.SurfacePoints(srf1)
        pts2 = rs.SurfacePoints(srf2)
        if( pts1==None or pts2==None ): return False
        pts1.extend(pts2)
        return rs.PointsAreCoplanar(pts1)
           
    x = rs.GetObject( "First surface to test", rs.filter.surface)
    y = rs.GetObject( "Second surface to test", rs.filter.surface)
    print(SurfacesAreCoplanar(x, y))

##### See Also:

  * IsPoint
  * IsPointCloud
  * PointCoordinates

  

PointScale

    
    
    PointScale(point, scale)

Scales a 3D point by a value

##### Parameters:

    
    
    point (point): the point to divide
    scale (number): scale factor to apply

##### Returns:

    
    
    point: resulting point on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.PointScale([1,0,0], 5)
    print(point)

##### See Also:

  * PointAdd
  * PointCompare
  * PointDivide
  * PointSubtract
  * PointTransform

  

PointSubtract

    
    
    PointSubtract(point1, point2)

Subtracts a 3D point or a 3D vector from a 3D point

##### Parameters:

    
    
    point1, point2 (point): the points to subtract

##### Returns:

    
    
    point: the resulting 3D point if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = (1,1,1)
    point2 = (2,2,2)
    point = rs.PointSubtract(point1, point2)
    print(point)

##### See Also:

  * PointAdd
  * PointCompare
  * PointDivide
  * PointScale
  * PointTransform

  

PointTransform

    
    
    PointTransform(point, xform)

Transforms a 3D point

##### Parameters:

    
    
    point (point): the point to transform
    xform (transform): a valid 4x4 transformation matrix

##### Returns:

    
    
    vector: transformed vector on success

##### Example:

    
    
    # Translate (move) objects by (10,10,0)
    import rhinoscriptsyntax as rs
    point = 5,5,0
    matrix = rs.XformTranslation((10,10,0))
    result = rs.PointTransform(point, matrix)
    print(result)

##### See Also:

  * PointAdd
  * PointCompare
  * PointDivide
  * PointScale
  * PointSubtract

  

ProjectPointToMesh

    
    
    ProjectPointToMesh(points, mesh_ids, direction)

Projects one or more points onto one or more meshes

##### Parameters:

    
    
    points ([point, ...]): one or more 3D points
    mesh_ids ([guid, ...]): identifiers of one or more meshes
    direction (vector): direction vector to project the points

##### Returns:

    
    
    list(point, ...): projected points on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Select mesh to project onto", rs.filter.mesh)
    objects = rs.GetObjects("Select points to project", rs.filter.point)
    points = [rs.PointCoordinates(obj) for obj in objects]
    # project down...
    results = rs.ProjectPointToMesh(points, mesh, (0,0,-1))
    rs.AddPoints( results )

##### See Also:

  * ProjectCurveToMesh
  * ProjectCurveToSurface
  * ProjectPointToSurface

  

ProjectPointToSurface

    
    
    ProjectPointToSurface(points, surface_ids, direction)

Projects one or more points onto one or more surfaces or polysurfaces

##### Parameters:

    
    
    points ([point, ...]): one or more 3D points
    surface_ids ([guid, ...]): identifiers of one or more surfaces/polysurfaces
    direction (vector): direction vector to project the points

##### Returns:

    
    
    list(point, ...): projected points on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface to project onto", rs.filter.surface)
    objects = rs.GetObjects("Select points to project", rs.filter.point)
    points = [rs.PointCoordinates(obj) for obj in objects]
    # Project down...
    results = rs.ProjectPointToSurface(points, surface, (0,0,-1))
    rs.AddPoints(results)

##### See Also:

  * ProjectCurveToMesh
  * ProjectCurveToSurface
  * ProjectPointToMesh

  

PullPoints

    
    
    PullPoints(object_id, points)

Pulls an array of points to a surface or mesh object. For more information,
see the Rhino help file Pull command

##### Parameters:

    
    
    object_id (guid): the identifier of the surface or mesh object that pulls
    points ([point, ...]): list of 3D points

##### Returns:

    
    
    list(point, ...): 3D points pulled onto surface or mesh

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface that pulls", rs.filter.surface)
    objects = rs.GetObjects("Select points to pull", rs.filter.point)
    points = [rs.PointCoordinates(obj) for obj in objects]
    results = rs.PullPoints( surface, points )
    rs.AddPoints( results )

##### See Also:

  * PullCurve

  

VectorAdd

    
    
    VectorAdd(vector1, vector2)

Adds two 3D vectors

##### Parameters:

    
    
    vector1, vector2 (vector): the vectors to add

##### Returns:

    
    
    vector: the resulting 3D vector if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = (1,0,0)
    vector2 = (0,1,0)
    vector = rs.VectorAdd(vector1, vector2)
    print(vector)

##### See Also:

  * VectorCreate
  * VectorScale
  * VectorSubtract

  

VectorAngle

    
    
    VectorAngle(vector1, vector2)

Returns the angle, in degrees, between two 3-D vectors

##### Parameters:

    
    
    vector1 (vector): The first 3-D vector.
    vector2 (vector): The second 3-D vector.

##### Returns:

    
    
    number: The angle in degrees if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    s0 = rs.GetObject("Surface 0", rs.filter.surface)
    s1 = rs.GetObject("Surface 1", rs.filter.surface)
    du0 = rs.SurfaceDomain(s0, 0)
    dv0 = rs.SurfaceDomain(s0, 1)
    du1 = rs.SurfaceDomain(s1, 0)
    dv1 = rs.SurfaceDomain(s1, 1)
    n0 = rs.SurfaceNormal(s0, (du0[0], dv0[0]))
    n1 = rs.SurfaceNormal(s1, (du1[0], dv1[0]))
    print(rs.VectorAngle(n0, n1))
    print(rs.VectorAngle(n0, rs.VectorReverse(n1)))

##### See Also:

  * Angle
  * Angle2

  

VectorCompare

    
    
    VectorCompare(vector1, vector2)

Compares two 3D vectors

##### Parameters:

    
    
    vector1, vector2 (vector): the two vectors to compare

##### Returns:

    
    
    number: result of comparing the vectors.
            -1 if vector1 is less than vector2
            0 if vector1 is equal to vector2
            1 if vector1 is greater than vector2

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = (1,0,0)
    vector2 = (0,1,0)
    rc = rs.VectorCompare(vector1 , vector2)
    print(rc)

##### See Also:

  * IsVectorTiny
  * IsVectorZero
  * VectorCreate

  

VectorCreate

    
    
    VectorCreate(to_point, from_point)

Creates a vector from two 3D points

##### Parameters:

    
    
    to_point, from_point (point): the points defining the vector

##### Returns:

    
    
    vector: the resulting vector if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = rs.GetPoint("First point")
    point2 = rs.GetPoint("Next point")
    vector = rs.VectorCreate(point2, point1)
    print(vector)

##### See Also:

  * IsVectorTiny
  * IsVectorZero
  * VectorCompare
  * VectorUnitize

  

VectorCrossProduct

    
    
    VectorCrossProduct(vector1, vector2)

Calculates the cross product of two 3D vectors

##### Parameters:

    
    
    vector1, vector2 (vector): the vectors to perform cross product on

##### Returns:

    
    
    vector: the resulting cross product direction if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = (1,0,0)
    vector2 = (0,1,0)
    vector = rs.VectorCrossProduct(vector1, vector2)
    print(vector)

##### See Also:

  * VectorDotProduct
  * VectorUnitize

  

VectorDivide

    
    
    VectorDivide(vector, divide)

Divides a 3D vector by a value

##### Parameters:

    
    
    vector (vector): the vector to divide
    divide (number): a non-zero value to divide

##### Returns:

    
    
    vector: resulting vector on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector = rs.VectorDivide((5,5,0), 5)
    print(vector)

##### See Also:

  * VectorAdd
  * VectorCreate
  * VectorSubtract

  

VectorDotProduct

    
    
    VectorDotProduct(vector1, vector2)

Calculates the dot product of two 3D vectors

##### Parameters:

    
    
    vector1, vector2 (vector): the vectors to perform the dot product on

##### Returns:

    
    
    vector: the resulting dot product if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = [1,0,0]
    vector2 = [0,1,0]
    dblDotProduct = rs.VectorDotProduct(vector1, vector2)
    print(dblDotProduct)

##### See Also:

  * VectorCrossProduct
  * VectorUnitize

  

VectorLength

    
    
    VectorLength(vector)

Returns the length of a 3D vector

##### Parameters:

    
    
    vector (vector):  The 3-D vector.

##### Returns:

    
    
    number: The length of the vector if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = rs.GetPoint("First point")
    point2 = rs.GetPoint("Next point")
    vector = rs.VectorCreate(point1, point2)
    print(rs.VectorLength(vector))

##### See Also:

  * VectorAdd
  * VectorCreate
  * VectorSubtract
  * VectorUnitize

  

VectorMultiply

    
    
    VectorMultiply(vector1, vector2)

Multiplies two 3D vectors

##### Parameters:

    
    
    vector1, vector2 (vector): the vectors to multiply

##### Returns:

    
    
    vector: the resulting inner (dot) product if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    product = rs.VectorMultiply( [2,2,2], [3,3,3] )
    print(product)

##### See Also:

  * VectorAdd
  * VectorCreate
  * VectorSubtract

  

VectorReverse

    
    
    VectorReverse(vector)

Reverses the direction of a 3D vector

##### Parameters:

    
    
    vector (vector): the vector to reverse

##### Returns:

    
    
    vector: reversed vector on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector = rs.VectorReverse([1,0,0])
    print(vector)

##### See Also:

  * VectorCreate
  * VectorUnitize

  

VectorRotate

    
    
    VectorRotate(vector, angle_degrees, axis)

Rotates a 3D vector

##### Parameters:

    
    
    vector (vector): the vector to rotate
    angle_degrees (number): rotation angle
    axis (vector): axis of rotation

##### Returns:

    
    
    vector: rotated vector on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector = rs.VectorRotate([1,0,0], 90.0, [0,0,1])
    print(vector)

##### See Also:

  * VectorCreate
  * VectorScale

  

VectorScale

    
    
    VectorScale(vector, scale)

Scales a 3-D vector

##### Parameters:

    
    
    vector (vector): the vector to scale
    scale (number): scale factor to apply

##### Returns:

    
    
    vector: resulting vector on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector = rs.VectorScale([1,0,0], 5)
    print(vector)

##### See Also:

  * VectorAdd
  * VectorCreate
  * VectorSubtract

  

VectorSubtract

    
    
    VectorSubtract(vector1, vector2)

Subtracts two 3D vectors

##### Parameters:

    
    
    vector1 (vector): the vector to subtract from
    vector2 (vector): the vector to subtract

##### Returns:

    
    
    vector: the resulting 3D vector

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector1 = [1,0,0]
    vector2 = [0,1,0]
    vector = rs.VectorSubtract(vector1, vector2)
    print(vector)

##### See Also:

  * VectorAdd
  * VectorCreate
  * VectorScale

  

VectorTransform

    
    
    VectorTransform(vector, xform)

Transforms a 3D vector

##### Parameters:

    
    
    vector (vector): the vector to transform
    xform (transform): a valid 4x4 transformation matrix

##### Returns:

    
    
    vector: transformed vector on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector = (1,0,0) #world x-axis
    xform = rs.XformRotation2(90.0, (0,0,1), (0,0,0))
    vector = rs.VectorTransform(vector, xform)
    print(vector)

##### See Also:

  * IsVectorZero
  * VectorCreate
  * VectorUnitize

  

VectorUnitize

    
    
    VectorUnitize(vector)

Unitizes, or normalizes a 3D vector. Note, zero vectors cannot be unitized

##### Parameters:

    
    
    vector (vector): the vector to unitize

##### Returns:

    
    
    vector: unitized vector on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    vector = rs.VectorUnitize( [1.5,-4.1,3.6] )
    print(vector)

##### See Also:

  * IsVectorZero
  * VectorCreate

  

PointArrayBoundingBox

    
    
    PointArrayBoundingBox(points, view_or_plane=None, in_world_coords=True)

Returns either a world axis-aligned or a construction plane axis-aligned
bounding box of an array of 3-D point locations.

##### Parameters:

    
    
    points ([point, ...]): A list of 3-D points
    view_or_plane (str|plane, optional): Title or id of the view that contains the
        construction plane to which the bounding box should be aligned -or-
        user defined plane. If omitted, a world axis-aligned bounding box
        will be calculated
    in_world_coords (bool, optional): return the bounding box as world coordinates or
        construction plane coordinates. Note, this option does not apply to
        world axis-aligned bounding boxes.

##### Returns:

    
    
    list(point, ....): Eight points that define the bounding box. Points returned in counter-
    clockwise order starting with the bottom rectangle of the box.
    None: on error

##### See Also:

  * BoundingBox

  

## selection

AllObjects

    
    
    AllObjects(select=False, include_lights=False, include_grips=False, include_references=False)

Returns identifiers of all objects in the document.

##### Parameters:

    
    
    select(bool, optional): Select the objects
    include_lights (bool, optional): Include light objects
    include_grips (bool, optional): Include grips objects

##### Returns:

    
    
    list(guid, ...): identifiers for all the objects in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.AllObjects()
    for obj in objs: print("Object identifier: {}".format(obj))

##### See Also:

  * HiddenObjects
  * LockedObjects
  * NormalObjects

  

FirstObject

    
    
    FirstObject(select=False, include_lights=False, include_grips=False)

Returns identifier of the first object in the document. The first object is
the last object created by the user.

##### Parameters:

    
    
    select (bool, optional): Select the object.  If omitted (False), the object is not selected.
    include_lights (bool, optional): Include light objects.  If omitted (False), light objects are not returned.
    include_grips (bool, optional): Include grips objects.  If omitted (False), grips objects are not returned.

##### Returns:

    
    
    guid: The identifier of the object if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddLine( (0,0,0), (5,5,0) )
    rs.AddLine( (0,0,0), (5,0,0) )
    rs.AddLine( (0,0,0), (0,5,0) )
    objectId = rs.FirstObject()
    print("Object identifier: {}".format(objectId))
    rs.SelectObject(objectId)

##### See Also:

  * LastObject
  * NextObject

  

GetCurveObject

    
    
    GetCurveObject(message=None, preselect=False, select=False)

Prompts user to pick or select a single curve object

##### Parameters:

    
    
    message (str, optional): a prompt or message.
    preselect (bool,, optional): Allow for the selection of pre-selected objects.
    select (bool, optional): Select the picked objects. If False, objects that
      are picked are not selected.

##### Returns:

    
    
    Tuple containing the following information
      [0]  guid     identifier of the curve object
      [1]  bool     True if the curve was preselected, otherwise False
      [2]  number   selection method
                       0 = selected by non-mouse method (SelAll, etc.).
                       1 = selected by mouse click on the object.
                       2 = selected by being inside of a mouse window.
                       3 = selected by intersecting a mouse crossing window.
      [3]  point    selection point
      [4]  number   the curve parameter of the selection point
      [5]  str      name of the view selection was made
    None: if no object picked

##### Example:

    
    
    import rhinoscriptsyntax as rs
    select_result = rs.GetCurveObject("Select curve")
    if select_result:
        print("Curve identifier: {}".format(select_result[0]))

##### See Also:

  * GetObject
  * GetObjects
  * GetSurfaceObject

  

GetObject

    
    
    GetObject(message=None, filter=0, preselect=False, select=False, custom_filter=None, subobjects=False)

Prompts user to pick, or select, a single object.

##### Parameters:

    
    
    message(str, optional): a prompt or message.
    filter (number, optional): The type(s) of geometry (points, curves, surfaces, meshes,...)
        that can be selected. Object types can be added together to filter
        several different kinds of geometry. use the filter class to get values
    preselect (bool, optional): Allow for the selection of pre-selected objects.
    select (bool, optional): Select the picked objects.  If False, the objects that are
        picked are not selected.
    subobjects (bool, optional): If True, subobjects can be selected. When this is the
        case, an ObjRef is returned instead of a Guid to allow for tracking
        of the subobject when passed into other functions

##### Returns:

    
    
    guid: Identifier of the picked object
    None: if user did not pick an object

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objectId = rs.GetObject("Pick any object")
    if objectId:
        print("Object identifier: {}".format(objectId))
    objectId = rs.GetObject("Pick a curve or surface", rs.filter.curve | rs.filter.surface)
    if objectId:
        print("Object identifier: {}".format(objectId))

##### See Also:

  * GetCurveObject
  * GetObjectEx
  * GetObjects
  * GetSurfaceObject

  

GetObjectEx

    
    
    GetObjectEx(message=None, filter=0, preselect=False, select=False, objects=None)

Prompts user to pick, or select a single object

##### Parameters:

    
    
    message (str, optional): a prompt or message.
    filter (number, optional): The type(s) of geometry (points, curves, surfaces, meshes,...)
        that can be selected. Object types can be added together to filter
        several different kinds of geometry. use the filter class to get values
    preselect (bool, optional):  Allow for the selection of pre-selected objects.
    select (bool, optional): Select the picked objects.  If False, the objects that are
        picked are not selected.
    objects ([guid, ...]): list of object identifiers specifying objects that are
        allowed to be selected

##### Returns:

    
    
    tuple(guid, bool, number, point, str): containing the following information
        [0] identifier of the object
        [1] True if the object was preselected, otherwise False
        [2] selection method (see help)
        [3] selection point
        [4] name of the view selection was made
    None: if no object selected

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObjectEx("Select object", 0, True)
    if obj:
        print("Object id = {}".format(obj[0]))
        print("Object was preselected = {}".format(obj[1]))
        if obj[2]==0:
            print("Selection method = 0 (non-mouse)")
        elif obj[2]==1:
            print("Selection method = 1 (mouse)")
            print("Pick point = {}".format(obj[3]))
        elif obj[2]==2:
            print("Selection method = 2 (window)")
        elif obj[2]==3:
            print("Selection method = 3 (crossing)")
        print("Active view = {}".format(obj[4]))

##### See Also:

  * GetCurveObject
  * GetObject
  * GetObjects
  * GetObjectsEx
  * GetSurfaceObject

  

GetObjects

    
    
    GetObjects(message=None, filter=0, group=True, preselect=False, select=False, objects=None, minimum_count=1, maximum_count=0, custom_filter=None)

Prompts user to pick or select one or more objects.

##### Parameters:

    
    
    message (str, optional): a prompt or message.
    filter (number, optional): The type(s) of geometry (points, curves, surfaces, meshes,...)
        that can be selected. Object types can be added together to filter
        several different kinds of geometry. use the filter class to get values
            Value         Description
            0             All objects (default)
            1             Point
            2             Point cloud
            4             Curve
            8             Surface or single-face brep
            16            Polysurface or multiple-face
            32            Mesh
            256           Light
            512           Annotation
            4096          Instance or block reference
            8192          Text dot object
            16384         Grip object
            32768         Detail
            65536         Hatch
            131072        Morph control
            262144        SubD
            134217728     Cage
            268435456     Phantom
            536870912     Clipping plane
            1073741824    Extrusion
    group (bool, optional): Honor object grouping.  If omitted and the user picks a group,
        the entire group will be picked (True). Note, if filter is set to a
        value other than 0 (All objects), then group selection will be disabled.
    preselect (bool, optional):  Allow for the selection of pre-selected objects.
    select (bool, optional): Select the picked objects.  If False, the objects that are
        picked are not selected.
    objects ([guid, ...]): list of objects that are allowed to be selected
    minimum_count, maximum_count(number): limits on number of objects allowed to be selected
    custom_filter (str, optional): Calls a custom function in the script and passes the Rhino Object, Geometry, and component index and returns true or false indicating if the object can be selected

##### Returns:

    
    
    list(guid, ...): identifiers of the picked objects

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objectIds = rs.GetObjects("Pick some curves", rs.filter.curve)
    for id in objectIds: print("Object identifier:{}".format(id))

##### See Also:

  * GetCurveObject
  * GetObject
  * GetSurfaceObject

  

GetObjectsEx

    
    
    GetObjectsEx(message=None, filter=0, group=True, preselect=False, select=False, objects=None)

Prompts user to pick, or select one or more objects

##### Parameters:

    
    
    message (str, optional):  a prompt or message.
    filter (number, optional): The type(s) of geometry (points, curves, surfaces, meshes,...)
        that can be selected. Object types can be added together to filter
        several different kinds of geometry. use the filter class to get values
    group (bool, optional): Honor object grouping.  If omitted and the user picks a group,
        the entire group will be picked (True). Note, if filter is set to a
        value other than 0 (All objects), then group selection will be disabled.
    preselect (bool, optional):  Allow for the selection of pre-selected objects.
    select (bool, optional): Select the picked objects. If False, the objects that are
        picked are not selected.
    objects ([guid, ...]): list of object identifiers specifying objects that are
        allowed to be selected

##### Returns:

    
    
    list(tuple(guid, bool, number, point, str), ...): containing the following information
      [n][0]  identifier of the object
      [n][1]  True if the object was preselected, otherwise False
      [n][2]  selection method (see help)
      [n][3]  selection point
      [n][4]  name of the view selection was made

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjectsEx("Select objects", 0, True)
    for obj in objects:
        print("Object id = {}".format(obj[0]))
        print("Object was preselected = {}".format(obj[1]))
        if obj[2]==0:
            print("Selection method = 0 (non-mouse)")
        elif obj[2]==1:
            print("Selection method = 1 (mouse)")
            print("Pick point = {}".format(obj[3]))
        elif obj[2]==2:
            print("Selection method = 2 (window)")
        elif obj[2]==3:
            print("Selection method = 3 (crossing)")
        print("Active view = {}".format(obj[4]))

##### See Also:

  * GetCurveObject
  * GetObject
  * GetObjectEx
  * GetObjects
  * GetSurfaceObject

  

GetPointCoordinates

    
    
    GetPointCoordinates(message="Select points", preselect=False)

Prompts the user to select one or more point objects.

##### Parameters:

    
    
    message (str, optional): a prompt message.
    preselect (bool, optional): Allow for the selection of pre-selected objects.  If omitted (False), pre-selected objects are not accepted.

##### Returns:

    
    
    list(point, ...): 3d coordinates of point objects on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPointCoordinates()
    for point in points: print(point)

##### See Also:

  * GetObject
  * GetObjects
  * GetPoint
  * GetPoints
  * PointCoordinates

  

GetSurfaceObject

    
    
    GetSurfaceObject(message="Select surface", preselect=False, select=False)

Prompts the user to select a single surface

##### Parameters:

    
    
    message(str, optional): prompt displayed
    preselect (bool, optional): allow for preselected objects
    select (bool, optional):  select the picked object

##### Returns:

    
    
    tuple(guid, bool, number, point, (number, number), str): of information on success
      [0]  identifier of the surface
      [1]  True if the surface was preselected, otherwise False
      [2]  selection method ( see help )
      [3]  selection point
      [4]  u,v surface parameter of the selection point
      [5]  name of the view in which the selection was made
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    select = rs.GetSurfaceObject("Select surface")
    if select:
        print("Surface identifier: {}".format(select[0]))

##### See Also:

  * GetCurveObject
  * GetObject
  * GetObjects

  

LockedObjects

    
    
    LockedObjects(include_lights=False, include_grips=False, include_references=False)

Returns identifiers of all locked objects in the document. Locked objects
cannot be snapped to, and cannot be selected

##### Parameters:

    
    
    include_lights (bool, optional): include light objects
    include_grips (bool, optional): include grip objects

##### Returns:

    
    
    list(guid, ...): identifiers the locked objects if successful.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    objs = rs.LockedObjects()
    for obj in objs: print("Object  identifier:{}".format(obj))

##### See Also:

  * AllObjects
  * HiddenObjects
  * NormalObjects

  

HiddenObjects

    
    
    HiddenObjects(include_lights=False, include_grips=False, include_references=False)

Returns identifiers of all hidden objects in the document. Hidden objects are
not visible, cannot be snapped to, and cannot be selected

##### Parameters:

    
    
    include_lights (bool, optional): include light objects
    include_grips (bool, optional): include grip objects

##### Returns:

    
    
    list(guid, ...): identifiers of the hidden objects if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    hidden = rs.HiddenObjects()
    for obj in hidden: print("Object identifier{}".format(obj))

##### See Also:

  * AllObjects
  * LockedObjects
  * NormalObjects

  

InvertSelectedObjects

    
    
    InvertSelectedObjects(include_lights=False, include_grips=False, include_references=False)

Inverts the current object selection. The identifiers of the newly selected
objects are returned

##### Parameters:

    
    
    include_lights (bool, optional): Include light objects.  If omitted (False), light objects are not returned.
    include_grips (bool, optional): Include grips objects.  If omitted (False), grips objects are not returned.
    include_references (bool, optional): Include reference objects.  If omitted (False), reference objects are not returned.

##### Returns:

    
    
    list(guid, ...): identifiers of the newly selected objects if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.GetObjects("Select some objects", select=True)
    objs = rs.InvertSelectedObjects()
    for id in objs: print("Object identifier:{}".format(id))

##### See Also:

  * SelectedObjects
  * UnselectAllObjects

  

LastCreatedObjects

    
    
    LastCreatedObjects(select=False)

Returns identifiers of the objects that were most recently created or changed
by scripting a Rhino command using the Command function. It is important to
call this function immediately after calling the Command function as only the
most recently created or changed object identifiers will be returned

##### Parameters:

    
    
    select (bool, optional): Select the object.  If omitted (False), the object is not selected.

##### Returns:

    
    
    list(guid, ...): identifiers of the most recently created or changed objects if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.Command( "_-Circle 0,0,0 10" )
    rs.Command( "_-Circle 10,0,0 10" )
    rs.Command( "_-Circle 20,0,0 10" )
    objs = rs.LastCreatedObjects()
    if objs:
        # Only the last circle will be selected
        rs.SelectObjects( objs )

##### See Also:

  * Command

  

LastObject

    
    
    LastObject(select=False, include_lights=False, include_grips=False)

Returns the identifier of the last object in the document. The last object in
the document is the first object created by the user

##### Parameters:

    
    
    select (bool, optional): select the object
    include_lights (bool, optional): include lights in the potential set
    include_grips (bool, optional): include grips in the potential set

##### Returns:

    
    
    guid: identifier of the object on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddLine((0,0,0), (5,5,0))
    rs.AddCircle((0,0,0), 5)
    print("Object identifier: {}".format(rs.LastObject()))

##### See Also:

  * FirstObject
  * NextObject

  

NextObject

    
    
    NextObject(object_id, select=False, include_lights=False, include_grips=False)

Returns the identifier of the next object in the document

##### Parameters:

    
    
    object_id (guid): the identifier of the object from which to get the next object
    select (bool, optional): select the object
    include_lights (bool, optional): include lights in the potential set
    include_grips (bool, optional): include grips in the potential set

##### Returns:

    
    
    guid: identifier of the object on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.FirstObject()
    while obj:
        print("Object identifier:{}".format(obj))
        obj = rs.NextObject(obj)

##### See Also:

  * FirstObject
  * LastObject

  

NormalObjects

    
    
    NormalObjects(include_lights=False, include_grips=False)

Returns identifiers of all normal objects in the document. Normal objects are
visible, can be snapped to, and are independent of selection state

##### Parameters:

    
    
    include_lights (bool, optional): Include light objects.  If omitted (False), light objects are not returned.
    include_gripts (bool, optional): Include grips objects.  If omitted (False), grips objects are not returned.

##### Returns:

    
    
    list(guid, ...): identifier of normal objects if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.NormalObjects()
    for obj in objs: print("Object identifier:{}".format(obj))

##### See Also:

  * AllObjects
  * HiddenObjects
  * LockedObjects

  

ObjectsByColor

    
    
    ObjectsByColor(color, select=False, include_lights=False)

Returns identifiers of all objects based on color

##### Parameters:

    
    
    color (color): color to get objects by
    select (bool, optional): select the objects
    include_lights (bool, optional): include lights in the set

##### Returns:

    
    
    list(guid, ...): identifiers of objects of the selected color.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Pick any object")
    if obj:
        color = rs.ObjectColor(obj)
        rs.ObjectsByColor(color, True)

  

ObjectsByGroup

    
    
    ObjectsByGroup(group_name, select=False)

Returns identifiers of all objects based on the objects' group name

##### Parameters:

    
    
    group_name (str): name of the group
    select (bool, optional): select the objects

##### Returns:

    
    
    list(guid, ...):identifiers for objects in the group on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    group = rs.GetString("Group to select")
    if group: rs.ObjectsByGroup( group, True )

  

ObjectsByLayer

    
    
    ObjectsByLayer(layer_name, select=False)

Returns identifiers of all objects based on the objects' layer name

##### Parameters:

    
    
    layer_name (str): name of the layer
    select (bool, optional): select the objects

##### Returns:

    
    
    list(guid, ...): identifiers for objects in the specified layer

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Pick any object")
    if obj:
        layer = rs.ObjectLayer(obj)
        rs.ObjectsByLayer(layer, True)

  

ObjectsByName

    
    
    ObjectsByName(name, select=False, include_lights=False, include_references=False)

Returns identifiers of all objects based on user-assigned name

##### Parameters:

    
    
    name (str): name of the object or objects
    select (bool, optional): select the objects
    include_lights (bool, optional): include light objects

##### Returns:

    
    
    list(guid, ...): identifiers for objects with the specified name.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = rs.GetString("Name to select")
    if name: rs.ObjectsByName(name,True)

  

ObjectsByType

    
    
    ObjectsByType(geometry_type, select=False, state=0)

Returns identifiers of all objects based on the objects' geometry type.

##### Parameters:

    
    
    geometry_type (number): The type(s) of geometry objects (points, curves, surfaces,
           meshes, etc.) that can be selected. Object types can be
           added together as bit-coded flags to filter several different kinds of geometry.
            Value        Description
             0           All objects
             1           Point
             2           Point cloud
             4           Curve
             8           Surface or single-face brep
             16          Polysurface or multiple-face
             32          Mesh
             256         Light
             512         Annotation
             4096        Instance or block reference
             8192        Text dot object
             16384       Grip object
             32768       Detail
             65536       Hatch
             131072      Morph control
             262144      SubD
             134217728   Cage
             268435456   Phantom
             536870912   Clipping plane
             1073741824  Extrusion
    select (bool, optional): Select the objects
    state (bool, optional): The object state (normal, locked, and hidden). Object states can be 
      added together to filter several different states of geometry.
            Value     Description
            0         All objects
            1         Normal objects
            2         Locked objects
            4         Hidden objects

##### Returns:

    
    
    list(guid, ...): identifiers of object that fit the specified type(s).

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.ObjectsByType(4 | 8, True)

  

SelectedObjects

    
    
    SelectedObjects(include_lights=False, include_grips=False)

Returns the identifiers of all objects that are currently selected

##### Parameters:

    
    
    include_lights (bool, optional): include light objects
    include_grips (bool, optional): include grip objects

##### Returns:

    
    
    list(guid, ...) identifiers of selected objects

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.SelectedObjects()
    for obj in objects: print("Object identifier: {}".format(obj))

##### See Also:

  * InvertSelectedObjects
  * UnselectAllObjects

  

UnselectAllObjects

    
    
    UnselectAllObjects()

Unselects all objects in the document

##### Returns:

    
    
    number: the number of objects that were unselected

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.UnselectAllObjects()
    print("{} objects were unselected".format(count))

##### See Also:

  * InvertSelectedObjects
  * SelectedObjects

  

VisibleObjects

    
    
    VisibleObjects(view=None, select=False, include_lights=False, include_grips=False)

Return identifiers of all objects that are visible in a specified view

##### Parameters:

    
    
    view (bool, optional): the view to use. If omitted, the current active view is used
    select (bool, optional): Select the objects
    include_lights (bool, optional): include light objects
    include_grips (bool, optional): include grip objects

##### Returns:

    
    
    list(guid, ...): identifiers of the visible objects

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object_ids = rs.VisibleObjects("Top")
    if object_ids:
        for id in object_ids: print("Object identifier:{}".format(id))

##### See Also:

  * IsView
  * IsVisibleInView

  

WindowPick

    
    
    WindowPick(corner1, corner2, view=None, select=False, in_window=True)

Picks objects using either a window or crossing selection

##### Parameters:

    
    
    corner1, corner2 (point): corners of selection window
    view (bool, optional): view to perform the selection in
    select (bool, optional): select picked objects
    in_window (bool, optional): if False, then a crossing window selection is performed

##### Returns:

    
    
    list(guid, ...): identifiers of selected objects on success

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    rs.WindowPick((0,0,0), (0,0,0),  None, True)

  

## surface

AddBox

    
    
    AddBox(corners)

Adds a box shaped polysurface to the document

##### Parameters:

    
    
    corners ([point, point, point ,point, point, point ,point,point]) 8 points that define the corners of the box. Points need to
      be in counter-clockwise order starting with the bottom rectangle of the box

##### Returns:

    
    
    guid: identifier of the new object on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    box = rs.GetBox()
    if box: rs.AddBox(box)

##### See Also:

  * AddCone
  * AddCylinder
  * AddSphere
  * AddTorus

  

AddCone

    
    
    AddCone(base, height, radius, cap=True)

Adds a cone shaped polysurface to the document

##### Parameters:

    
    
    base (point|plane): 3D origin point of the cone or a plane with an apex at the origin
        and normal along the plane's z-axis
    height (point|number): 3D height point of the cone if base is a 3D point. The height
        point defines the height and direction of the cone. If base is a
        plane, height is a numeric value
    radius (number): the radius at the base of the cone
    cap (bool, optional): cap base of the cone

##### Returns:

    
    
    guid: identifier of the new object on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = 5.0
    base = rs.GetPoint("Base of cone")
    if base:
        height = rs.GetPoint("Height of cone", base)
        if height: rs.AddCone(base, height, radius)

##### See Also:

  * AddBox
  * AddCylinder
  * AddSphere
  * AddTorus

  

AddCutPlane

    
    
    AddCutPlane(object_ids, start_point, end_point, normal=None)

Adds a planar surface through objects at a designated location. For more
information, see the Rhino help file for the CutPlane command

##### Parameters:

    
    
    objects_ids ([guid, ...]): identifiers of objects that the cutting plane will
        pass through
    start_point, end_point (line): line that defines the cutting plane
    normal (vector, optional): vector that will be contained in the returned planar
        surface. In the case of Rhino's CutPlane command, this is the
        normal to, or Z axis of, the active view's construction plane.
        If omitted, the world Z axis is used

##### Returns:

    
    
    guid: identifier of new object on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects for cut plane")
    if objs:
        point0 = rs.GetPoint("Start of cut plane")
        if point0:
            point1 = rs.GetPoint("End of cut plane", point0)
            if point1: rs.AddCutPlane( objs, point0, point1 )

##### See Also:

  * AddPlaneSurface

  

AddCylinder

    
    
    AddCylinder(base, height, radius, cap=True)

Adds a cylinder-shaped polysurface to the document

##### Parameters:

    
    
    base (point|plane): The 3D base point of the cylinder or the base plane of the cylinder
    height (point|number): if base is a point, then height is a 3D height point of the
      cylinder. The height point defines the height and direction of the
      cylinder. If base is a plane, then height is the numeric height value
      of the cylinder
    radius (number): radius of the cylinder
    cap (bool, optional): cap the cylinder

##### Returns:

    
    
    guid: identifier of new object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = 5.0
    base = rs.GetPoint("Base of cylinder")
    if base:
        height = rs.GetPoint("Height of cylinder", base)
        if height: rs.AddCylinder( base, height, radius )

##### See Also:

  * AddBox
  * AddCone
  * AddSphere
  * AddTorus

  

AddEdgeSrf

    
    
    AddEdgeSrf(curve_ids)

Creates a surface from 2, 3, or 4 edge curves

##### Parameters:

    
    
    curve_ids ([guid, ...]): list or tuple of curves

##### Returns:

    
    
    guid: identifier of new object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curves = rs.GetObjects("Select 2, 3, or 4 curves", rs.filter.curve)
    if curves and len(curves)>1 ): rs.AddEdgeSrf(curves)

##### See Also:

  * AddPlanarSrf
  * AddSrfControlPtGrid
  * AddSrfPt
  * AddSrfPtGrid

  

AddNetworkSrf

    
    
    AddNetworkSrf(curves, continuity=1, edge_tolerance=0, interior_tolerance=0, angle_tolerance=0)

Creates a surface from a network of crossing curves

##### Parameters:

    
    
    curves ([guid, ...]): curves from which to create the surface
    continuity (number, optional): how the edges match the input geometry
               0 = loose
               1 = position
               2 = tangency
               3 = curvature

##### Returns:

    
    
    guid: identifier of new object if successful

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    curve_ids = rs.GetObjects("Select  curves in network", 4, True, True)
    if len(curve_ids) > 0:
        rs.AddNetworkSrf(curve_ids)

  

AddNurbsSurface

    
    
    AddNurbsSurface(point_count, points, knots_u, knots_v, degree, weights=None)

Adds a NURBS surface object to the document

##### Parameters:

    
    
    point_count ([number, number]) number of control points in the u and v direction
    points ({point, ...]): list of 3D points
    knots_u ([number, ...]): knot values for the surface in the u direction.
              Must contain point_count[0]+degree[0]-1 elements
    knots_v ([number, ...]): knot values for the surface in the v direction.
              Must contain point_count[1]+degree[1]-1 elements
    degree ([number, number]): degree of the surface in the u and v directions.
    weights [(number, ...]): weight values for the surface. The number of elements in
      weights must equal the number of elements in points. Values must be
      greater than zero.

##### Returns:

    
    
    guid: identifier of new object if successful
    None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Pick a surface", rs.filter.surface)
    if obj:
        point_count = rs.SurfacePointCount(obj)
        points = rs.SurfacePoints(obj)
        knots = rs.SurfaceKnots(obj)
        degree = rs.SurfaceDegree(obj)
        if rs.IsSurfaceRational(obj):
            weights = rs.SurfaceWeights(obj)
            obj = rs.AddNurbsSurface(point_count, points, knots[0], knots[1], degree, weights)
        else:
            obj = rs.AddNurbsSurface(point_count, points, knots[0], knots[1], degree)
        if obj: rs.SelectObject(obj)

##### See Also:

  * IsSurfaceRational
  * SurfaceDegree
  * SurfaceKnotCount
  * SurfaceKnots
  * SurfacePointCount
  * SurfacePoints
  * SurfaceWeights

  

AddPatch

    
    
    AddPatch(object_ids, uv_spans_tuple_OR_surface_object_id, tolerance=None, trim=True, point_spacing=0.1, flexibility=1.0, surface_pull=1.0, fix_edges=False)

Fits a surface through curve, point, point cloud, and mesh objects.

##### Parameters:

    
    
    object_ids ({guid, ...]): a list of object identifiers that indicate the objects to use for the patch fitting.
        Acceptable object types include curves, points, point clouds, and meshes.
    uv_spans_tuple_OR_surface_object_id ([number, number]|guid):  the U and V direction span counts for the automatically generated surface OR
        The identifier of the starting surface.  It is best if you create a starting surface that is similar in shape 
        to the surface you are trying to create.
    tolerance (number, optional): The tolerance used by input analysis functions. If omitted, Rhino's document absolute tolerance is used.
    trim (bool, optional): Try to find an outside curve and trims the surface to it.  The default value is True.
    point_spacing (number, optional): The basic distance between points sampled from input curves.  The default value is 0.1.
    flexibility (number, optional): Determines the behavior of the surface in areas where its not otherwise controlled by the input.
        Lower numbers make the surface behave more like a stiff material, higher, more like a flexible material.  
        That is, each span is made to more closely match the spans adjacent to it if there is no input geometry 
        mapping to that area of the surface when the flexibility value is low.  The scale is logarithmic.  
        For example, numbers around 0.001 or 0.1 make the patch pretty stiff and numbers around 10 or 100 
        make the surface flexible.  The default value is 1.0.
    surface_pull (number, optional): Similar to stiffness, but applies to the starting surface. The bigger the pull, the closer
        the resulting surface shape will be to the starting surface.  The default value is 1.0.
    fix_edges (bool, optional): Clamps the edges of the starting surface in place. This option is useful if you are using a
        curve or points for deforming an existing surface, and you do not want the edges of the starting surface 
        to move.  The default if False.

##### Returns:

    
    
    guid: Identifier of the new surface object if successful.
    None: on error.

  

AddPipe

    
    
    AddPipe(curve_id, parameters, radii, blend_type=0, cap=0, fit=False)

Creates a single walled surface with a circular profile around a curve

##### Parameters:

    
    
    curve_id (guid): identifier of rail curve
    parameters, radii ([number, ...]): list of radius values at normalized curve parameters
    blend_type (number, optional): 0(local) or 1(global)
    cap (number, optional): 0(none), 1(flat), 2(round)
    fit (bool, optional): attempt to fit a single surface

##### Returns:

    
    
    list(guid, ...): identifiers of new objects created

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve to create pipe around", rs.filter.curve, True)
    if curve:
        domain = rs.CurveDomain(curve)
        rs.AddPipe(curve, 0, 4)

  

AddPlanarSrf

    
    
    AddPlanarSrf(object_ids)

Creates one or more surfaces from planar curves

##### Parameters:

    
    
    object_ids ({guid, ...]): curves to use for creating planar surfaces

##### Returns:

    
    
    list(guid, ...): identifiers of surfaces created on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select planar curves to build surface", rs.filter.curve)
    if objs: rs.AddPlanarSrf(objs)

##### See Also:

  * AddEdgeSrf
  * AddSrfControlPtGrid
  * AddSrfPt
  * AddSrfPtGrid

  

AddPlaneSurface

    
    
    AddPlaneSurface(plane, u_dir, v_dir)

Create a plane surface and add it to the document.

##### Parameters:

    
    
    plane (plane): The plane.
    u_dir (number): The magnitude in the U direction.
    v_dir (number): The magnitude in the V direction.

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddPlaneSurface( rs.WorldXYPlane(), 5.0, 3.0 )

##### See Also:

  * AddCutPlane
  * AddEdgeSrf
  * AddSrfControlPtGrid
  * AddSrfPt
  * AddSrfPtGrid
  * IsPlaneSurface

  

AddLoftSrf

    
    
    AddLoftSrf(object_ids, start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False)

Adds a surface created by lofting curves to the document. \- no curve sorting
performed. pass in curves in the order you want them sorted \- directions of
open curves not adjusted. Use CurveDirectionsMatch and ReverseCurve to adjust
the directions of open curves \- seams of closed curves are not adjusted. Use
CurveSeam to adjust the seam of closed curves

##### Parameters:

    
    
    object_ids ({guid, guid, ...]): ordered list of the curves to loft through
    start (point, optional): starting point of the loft
    end (point, optional): ending point of the loft
    loft_type (number, optional): type of loft. Possible options are:
      0 = Normal. Uses chord-length parameterization in the loft direction
      1 = Loose. The surface is allowed to move away from the original curves
          to make a smoother surface. The surface control points are created
          at the same locations as the control points of the loft input curves.
      2 = Straight. The sections between the curves are straight. This is
          also known as a ruled surface.
      3 = Tight. The surface sticks closely to the original curves. Uses square
          root of chord-length parameterization in the loft direction
      4 = Developable. Creates a separate developable surface or polysurface
          from each pair of curves.
    simplify_method (number, optional): Possible options are:
      0 = None. Does not simplify.
      1 = Rebuild. Rebuilds the shape curves before lofting. modified by `value` below
      2 = Refit. Refits the shape curves to a specified tolerance. modified by `value` below
    value (number, optional): Additional value based on the specified `simplify_method`:
      Simplify  -   Description
      Rebuild(1) - then value is the number of control point used to rebuild
      Rebuild(1) - is specified and this argument is omitted, then curves will be
                   rebuilt using 10 control points.
      Refit(2) - then value is the tolerance used to rebuild.
      Refit(2) - is specified and this argument is omitted, then the document's
                   absolute tolerance us used for refitting.
    closed (bool, optional): close the loft back to the first curve

##### Returns:

    
    
    list(guid, ...):Array containing the identifiers of the new surface objects if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Pick curves to loft", rs.filter.curve)
    if objs: rs.AddLoftSrf(objs)

##### See Also:

  * CurveDirectionsMatch
  * CurveSeam
  * ReverseCurve

  

AddRevSrf

    
    
    AddRevSrf(curve_id, axis, start_angle=0.0, end_angle=360.0)

Create a surface by revolving a curve around an axis

##### Parameters:

    
    
    curve_id (guid): identifier of profile curve
    axis (line): line for the rail revolve axis
    start_angle, end_angle (number, optional): start and end angles of revolve

##### Returns:

    
    
    guid: identifier of new object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.AddLine((5,0,0), (10,0,10))
    rs.AddRevSrf( curve, ((0,0,0), (0,0,1)) )

  

AddSphere

    
    
    AddSphere(center_or_plane, radius)

Add a spherical surface to the document

##### Parameters:

    
    
    center_or_plane (point|plane): center point of the sphere. If a plane is input,
      the origin of the plane will be the center of the sphere
    radius (number): radius of the sphere in the current model units

##### Returns:

    
    
    guid: identifier of the new object on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = 2
    center = rs.GetPoint("Center of sphere")
    if center: rs.AddSphere(center, radius)

##### See Also:

  * AddBox
  * AddCone
  * AddCylinder
  * AddTorus

  

AddSrfContourCrvs

    
    
    AddSrfContourCrvs(object_id, points_or_plane, interval=None)

Adds a spaced series of planar curves resulting from the intersection of
defined cutting planes through a surface or polysurface. For more information,
see Rhino help for details on the Contour command

##### Parameters:

    
    
    object_id (guid): object identifier to contour
    points_or_plane ([point,point]|plane): either a list/tuple of two points or a plane
      if two points, they define the start and end points of a center line
      if a plane, the plane defines the cutting plane
    interval (number, optional): distance between contour curves.

##### Returns:

    
    
    guid: ids of new contour curves on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object", rs.filter.surface + rs.filter.polysurface)
    startpoint = rs.GetPoint("Base point of center line")
    endpoint = rs.GetPoint("Endpoint of center line", startpoint)
    rs.AddSrfContourCrvs( obj, (startpoint, endpoint) )

##### See Also:

  * CurveContourPoints

  

AddSrfControlPtGrid

    
    
    AddSrfControlPtGrid(count, points, degree=(3,3))

Creates a surface from a grid of points

##### Parameters:

    
    
    count ([number, number])tuple of two numbers defining number of points in the u,v directions
    points ([point, ...]): list of 3D points
    degree ([number, number]): two numbers defining degree of the surface in the u,v directions

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful, or on error.

  

AddSrfPt

    
    
    AddSrfPt(points)

Creates a new surface from either 3 or 4 corner points.

##### Parameters:

    
    
    points ([point, point, point, point]): list of either 3 or 4 corner points

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(True, message1="Pick 3 or 4 corner points")
    if points: rs.AddSrfPt(points)

##### See Also:

  * AddEdgeSrf
  * AddSrfControlPtGrid
  * AddSrfPtGrid

  

AddSrfPtGrid

    
    
    AddSrfPtGrid(count, points, degree=(3,3), closed=(False,False))

Creates a surface from a grid of points

##### Parameters:

    
    
    count ([number, number}): tuple of two numbers defining number of points in the u,v directions
    points ([point, ...]): list of 3D points
    degree ([number, number], optional): two numbers defining degree of the surface in the u,v directions
    closed ([bool, bool], optional): two booleans defining if the surface is closed in the u,v directions

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful, or on error.

  

AddSweep1

    
    
    AddSweep1(rail, shapes, closed=False)

Adds a surface created through profile curves that define the surface shape
and one curve that defines a surface edge.

##### Parameters:

    
    
    rail (guid): identifier of the rail curve
    shapes ([guid, ...]): one or more cross section shape curves
    closed (bool, optional): If True, then create a closed surface

##### Returns:

    
    
    list(guid, ...): of new surface objects if successful
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rail = rs.GetObject("Select rail curve", rs.filter.curve)
    if rail:
        shapes = rs.GetObjects("Select cross-section curves", rs.filter.curve)
        if shapes: rs.AddSweep1( rail, shapes )

##### See Also:

  * AddSweep2
  * CurveDirectionsMatch
  * ReverseCurve

  

AddSweep2

    
    
    AddSweep2(rails, shapes, closed=False)

Adds a surface created through profile curves that define the surface shape
and two curves that defines a surface edge.

##### Parameters:

    
    
    rails ([guid, guid]): identifiers of the two rail curve
    shapes ([guid, ...]): one or more cross section shape curves
    closed (bool, optional): If True, then create a closed surface

##### Returns:

    
    
    list(guid, ...): of new surface objects if successful
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rails = rs.GetObjects("Select two rail curve", rs.filter.curve)
    if rails and len(rails)==2:
        shapes = rs.GetObjects("Select cross-section curves", rs.filter.curve)
        if shapes: rs.AddSweep2(rails, shapes)

##### See Also:

  * AddSweep1
  * CurveDirectionsMatch
  * ReverseCurve

  

AddRailRevSrf

    
    
    AddRailRevSrf(profile, rail, axis, scale_height=False)

Adds a surface created through profile curves that define the surface shape
and two curves that defines a surface edge.

##### Parameters:

    
    
    profile (guid): identifier of the profile curve
    rail (guid): identifier of the rail curve
    axis ([point, point]): A list of two 3-D points identifying the start point and end point of the rail revolve axis, or a Line
    scale_height (bool, optional): If True, surface will be locally scaled. Defaults to False

##### Returns:

    
    
    guid: identifier of the new object if successful
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    profile = rs.GetObject("Select a profile", rs.filter.curve)
    if profile:
        rail = rs.GetObject("Select a rail", rs.filter.curve)
        if rail:
            rs.AddRailRevSrf(profile, rail, ((0,0,0),(0,0,1)))

##### See Also:

  * AddSweep1
  * CurveDirectionsMatch
  * ReverseCurve

  

AddTorus

    
    
    AddTorus(base, major_radius, minor_radius, direction=None)

Adds a torus shaped revolved surface to the document

##### Parameters:

    
    
    base (point): 3D origin point of the torus or the base plane of the torus
    major_radius, minor_radius (number): the two radii of the torus
    directions (point):  A point that defines the direction of the torus when base is a point.
      If omitted, a torus that is parallel to the world XY plane is created

##### Returns:

    
    
    guid: The identifier of the new object if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    major_radius = 5.0
    minor_radius = major_radius - 2.0
    base = rs.GetPoint("Base of torus")
    if base:
        direction = rs.GetPoint("Direction of torus", base)
        if direction:
            rs.AddTorus( base, major_radius, minor_radius, direction )

##### See Also:

  * AddBox
  * AddCone
  * AddCylinder
  * AddSphere

  

BooleanDifference

    
    
    BooleanDifference(input0, input1, delete_input=True)

Performs a boolean difference operation on two sets of input surfaces and
polysurfaces. For more details, see the BooleanDifference command in the Rhino
help file

##### Parameters:

    
    
    input0 ([guid, ...]): list of surfaces to subtract from
    input1 ([guid, ...]): list of surfaces to be subtracted
    delete_input (bool, optional): delete all input objects

##### Returns:

    
    
    list(guid, ...): of identifiers of newly created objects on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filter = rs.filter.surface | rs.filter.polysurface
    input0 = rs.GetObjects("Select first set of surfaces or polysurfaces", filter)
    if input0:
        input1 = rs.GetObjects("Select second set of surfaces or polysurfaces", filter)
        if input1: rs.BooleanDifference(input0, input1)

##### See Also:

  * BooleanIntersection
  * BooleanUnion

  

BooleanIntersection

    
    
    BooleanIntersection(input0, input1, delete_input=True)

Performs a boolean intersection operation on two sets of input surfaces and
polysurfaces. For more details, see the BooleanIntersection command in the
Rhino help file

##### Parameters:

    
    
    input0 ([guid, ...]): list of surfaces
    input1 ([guid, ...]): list of surfaces
    delete_input (bool, optional): delete all input objects

##### Returns:

    
    
    list(guid, ...): of identifiers of newly created objects on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    input0 = rs.GetObjects("Select first set of surfaces or polysurfaces", rs.filter.surface | rs.filter.polysurface)
    if input0:
        input1 = rs.GetObjects("Select second set of surfaces or polysurfaces", rs.filter.surface | rs.filter.polysurface)
        if input1: rs.BooleanIntersection( input0, input1 )

##### See Also:

  * BooleanDifference
  * BooleanUnion

  

BooleanUnion

    
    
    BooleanUnion(input, delete_input=True)

Performs a boolean union operation on a set of input surfaces and
polysurfaces. For more details, see the BooleanUnion command in the Rhino help
file

##### Parameters:

    
    
    input ([guid, ...]): list of surfaces to union
    delete_input (bool, optional):  delete all input objects

##### Returns:

    
    
    list(guid, ...): of identifiers of newly created objects on success
    None on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    input = rs.GetObjects("Select surfaces or polysurfaces to union", rs.filter.surface | rs.filter.polysurface)
    if input and len(input)>1: rs.BooleanUnion(input)

##### See Also:

  * BooleanDifference
  * BooleanUnion

  

BrepClosestPoint

    
    
    BrepClosestPoint(object_id, point)

Returns the point on a surface or polysurface that is closest to a test point.
This function works on both untrimmed and trimmed surfaces.

##### Parameters:

    
    
    object_id (guid): The object's identifier.
    point (point): The test, or sampling point.

##### Returns:

    
    
    tuple(point, [number, number], [number, number], vector): of closest point information if successful. The list will
    contain the following information:
    Element     Type             Description
       0        Point3d          The 3-D point at the parameter value of the 
                                 closest point.
       1        (U, V)           Parameter values of closest point. Note, V 
                                 is 0 if the component index type is brep_edge
                                 or brep_vertex. 
       2        (type, index)    The type and index of the brep component that
                                 contains the closest point. Possible types are
                                 brep_face, brep_edge or brep_vertex.
       3        Vector3d         The normal to the brep_face, or the tangent
                                 to the brep_edge.  
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if obj:
        point = rs.GetPoint("Pick a test point")
        if point:
            arrCP = rs.BrepClosestPoint(obj, point)
            if arrCP:
                rs.AddPoint(point)
                rs.AddPoint( arrCP[0] )

##### See Also:

  * EvaluateSurface
  * IsSurface
  * SurfaceClosestPoint

  

CapPlanarHoles

    
    
    CapPlanarHoles(surface_id)

Caps planar holes in a surface or polysurface

##### Parameters:

    
    
    surface_id (guid): The identifier of the surface or polysurface to cap.

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface or polysurface to cap", rs.filter.surface | rs.filter.polysurface)
    if surface: rs.CapPlanarHoles( surface )

##### See Also:

  * ExtrudeCurve
  * ExtrudeCurvePoint
  * ExtrudeCurveStraight
  * ExtrudeSurface

  

DuplicateEdgeCurves

    
    
    DuplicateEdgeCurves(object_id, select=False)

Duplicates the edge curves of a surface or polysurface. For more information,
see the Rhino help file for information on the DupEdge command.

##### Parameters:

    
    
    object_id (guid): The identifier of the surface or polysurface object.
    select (bool, optional):  Select the duplicated edge curves. The default is not
    to select (False).

##### Returns:

    
    
    list(guid, ..): identifying the newly created curve objects if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select surface or polysurface", rs.filter.surface | rs.filter.polysurface)
    if obj:
        rs.DuplicateEdgeCurves( obj, True )
        rs.DeleteObject( obj )

##### See Also:

  * IsPolysurface
  * IsSurface

  

DuplicateSurfaceBorder

    
    
    DuplicateSurfaceBorder(surface_id, type=0)

Create curves that duplicate a surface or polysurface border

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    type (number, optional): the border curves to return
       0=both exterior and interior,
       1=exterior
       2=interior

##### Returns:

    
    
    list(guid, ...): list of curve ids on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface or polysurface", rs.filter.surface | rs.filter.polysurface)
    if surface: rs.DuplicateSurfaceBorder( surface )

##### See Also:

  * DuplicateEdgeCurves
  * DuplicateMeshBorder

  

EvaluateSurface

    
    
    EvaluateSurface(surface_id, u, v)

Evaluates a surface at a U,V parameter

##### Parameters:

    
    
    surface_id (guid): the object's identifier.
    u, v ({number, number]): u, v parameters to evaluate.

##### Returns:

    
    
    point: a 3-D point if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objectId = rs.GetObject("Select a surface")
    if rs.IsSurface(objectId):
        domainU = rs.SurfaceDomain(objectId, 0)
        domainV = rs.SurfaceDomain(objectId, 1)
        u = domainU[1]/2.0
        v = domainV[1]/2.0
        point = rs.EvaluateSurface(objectId, u, v)
        rs.AddPoint( point )

##### See Also:

  * IsSurface
  * SurfaceClosestPoint

  

ExtendSurface

    
    
    ExtendSurface(surface_id, parameter, length, smooth=True)

Lengthens an untrimmed surface object

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    parameter ([number, number}): tuple of two values definfing the U,V parameter to evaluate.
      The surface edge closest to the U,V parameter will be the edge that is
      extended
    length (number): amount to extend to surface
    smooth (bool, optional): If True, the surface is extended smoothly curving from the
      edge. If False, the surface is extended in a straight line from the edge

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    pick = rs.GetObjectEx("Select surface to extend", rs.filter.surface)
    if pick:
        parameter = rs.SurfaceClosestPoint(pick[0], pick[3])
        rs.ExtendSurface(pick[0], parameter, 5.0)

##### See Also:

  * IsSurface

  

ExplodePolysurfaces

    
    
    ExplodePolysurfaces(object_ids, delete_input=False)

Explodes, or unjoins, one or more polysurface objects. Polysurfaces will be
exploded into separate surfaces

##### Parameters:

    
    
    object_ids ([guid, ...]): identifiers of polysurfaces to explode
    delete_input 9bool, optional): delete input objects after exploding

##### Returns:

    
    
    list(guid, ...): of identifiers of exploded pieces on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select polysurface to explode", rs.filter.polysurface)
    if rs.IsPolysurface(obj):
        rs.ExplodePolysurfaces( obj )

##### See Also:

  * IsPolysurface
  * IsSurface

  

ExtractIsoCurve

    
    
    ExtractIsoCurve(surface_id, parameter, direction)

Extracts isoparametric curves from a surface

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    parameter ([number, number]): u,v parameter of the surface to evaluate
    direction (number): Direction to evaluate
      0 = u
      1 = v
      2 = both

##### Returns:

    
    
    list(guid, ...): of curve ids on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select surface for isocurve extraction", rs.filter.surface)
    point = rs.GetPointOnSurface(obj, "Select location for extraction")
    parameter = rs.SurfaceClosestPoint(obj, point)
    rs.ExtractIsoCurve( obj, parameter, 2 )

##### See Also:

  * IsSurface

  

ExtractSurface

    
    
    ExtractSurface(object_id, face_indices, copy=False)

Separates or copies a surface or a copy of a surface from a polysurface

##### Parameters:

    
    
    object_id (guid): polysurface identifier
    face_indices (number, ...): one or more numbers representing faces
    copy (bool, optional): If True the faces are copied. If False, the faces are extracted

##### Returns:

    
    
    list(guid, ...): identifiers of extracted surface objects on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select polysurface", rs.filter.polysurface, True)
    if obj: rs.ExtractSurface(obj, 0)

##### See Also:

  * BrepClosestPoint
  * IsSurface
  * IsPolysurface

  

ExtrudeCurve

    
    
    ExtrudeCurve(curve_id, path_id)

Creates a surface by extruding a curve along a path

##### Parameters:

    
    
    curve_id (guid): identifier of the curve to extrude
    path_id (guid): identifier of the path curve

##### Returns:

    
    
    guid: identifier of new surface on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.AddCircle(rs.WorldXYPlane(), 5)
    path = rs.AddLine([5,0,0], [10,0,10])
    rs.ExtrudeCurve( curve, path )

##### See Also:

  * ExtrudeCurvePoint
  * ExtrudeCurveStraight
  * ExtrudeSurface

  

ExtrudeCurvePoint

    
    
    ExtrudeCurvePoint(curve_id, point)

Creates a surface by extruding a curve to a point

##### Parameters:

    
    
    curve_id (guid): identifier of the curve to extrude
    point (point): 3D point

##### Returns:

    
    
    guid: identifier of new surface on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.AddCircle(rs.WorldXYPlane(), 5)
    point = (0,0,10)
    rs.ExtrudeCurvePoint( curve, point )

##### See Also:

  * ExtrudeCurve
  * ExtrudeCurveStraight
  * ExtrudeSurface

  

ExtrudeCurveStraight

    
    
    ExtrudeCurveStraight(curve_id, start_point, end_point)

Create surface by extruding a curve along two points that define a line

##### Parameters:

    
    
    curve_id (guid): identifier of the curve to extrude
    start_point, end_point (point): 3D points that specify distance and direction

##### Returns:

    
    
    guid: identifier of new surface on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.AddCircle(rs.WorldXYPlane(), 5)
    rs.ExtrudeCurveStraight( curve, (0,0,0), (0, 10, 10) )

##### See Also:

  * ExtrudeCurve
  * ExtrudeCurvePoint
  * ExtrudeSurface

  

ExtrudeSurface

    
    
    ExtrudeSurface(surface, curve, cap=True)

Create surface by extruding along a path curve

##### Parameters:

    
    
    surface (guid): identifier of the surface to extrude
    curve (guid): identifier of the path curve
    cap (bool, optional): extrusion is capped at both ends

##### Returns:

    
    
    guid: identifier of new surface on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.AddSrfPt([(0,0,0), (5,0,0), (5,5,0), (0,5,0)])
    curve = rs.AddLine((5,0,0), (10,0,10))
    rs.ExtrudeSurface(surface, curve)

##### See Also:

  * ExtrudeCurve
  * ExtrudeCurvePoint
  * ExtrudeCurveStraight

  

FilletSurfaces

    
    
    FilletSurfaces(surface0, surface1, radius, uvparam0=None, uvparam1=None)

Create constant radius rolling ball fillets between two surfaces. Note, this
function does not trim the original surfaces of the fillets

##### Parameters:

    
    
    surface0, surface1 (guid): identifiers of first and second surface
    radius (number): a positive fillet radius
    uvparam0 ([number, number], optional): a u,v surface parameter of surface0 near where the fillet
      is expected to hit the surface
    uvparam1([number, number], optional): same as uvparam0, but for surface1

##### Returns:

    
    
    guid: ids of surfaces created on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface0 = rs.GetObject("First surface", rs.filter.surface)
    surface1 = rs.GetObject("Second surface", rs.filter.surface)
    rs.FilletSurfaces(surface0, surface1, 2.0)

##### See Also:

  * IsSurface

  

FlipSurface

    
    
    FlipSurface(surface_id, flip=None)

Returns or changes the normal direction of a surface. This feature can also be
found in Rhino's Dir command

##### Parameters:

    
    
    surface_id (guid): identifier of a surface object
    flip (bool, optional) new normal orientation, either flipped(True) or not flipped (False).

##### Returns:

    
    
    vector: if flipped is not specified, the current normal orientation
    vector: if flipped is specified, the previous normal orientation
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surf = rs.GetObject("Select object", rs.filter.surface)
    if surf:
        flip = rs.FlipSurface(surf)
        if flip: rs.FlipSurface(surf, False)

##### See Also:

  * IsSurface

  

IntersectBreps

    
    
    IntersectBreps(brep1, brep2, tolerance=None)

Intersects a brep object with another brep object. Note, unlike the
SurfaceSurfaceIntersection function this function works on trimmed surfaces.

##### Parameters:

    
    
    brep1 (guid): identifier of first brep object
    brep2 (guid): identifier of second brep object
    tolerance (number): Distance tolerance at segment midpoints. If omitted,
                the current absolute tolerance is used.

##### Returns:

    
    
    list(guid, ...): identifying the newly created intersection curve and point objects if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    brep1 = rs.GetObject("Select the first brep", rs.filter.surface | rs.filter.polysurface)
    if brep1:
        brep2 = rs.GetObject("Select the second", rs.filter.surface | rs.filter.polysurface)
        if brep2: rs.IntersectBreps( brep1, brep2)

  

IntersectSpheres

    
    
    IntersectSpheres(sphere_plane0, sphere_radius0, sphere_plane1, sphere_radius1)

Calculates intersections of two spheres

##### Parameters:

    
    
    sphere_plane0 (plane): an equatorial plane of the first sphere. The origin of the
      plane will be the center point of the sphere
    sphere_radius0 (number): radius of the first sphere
    sphere_plane1 (plane): plane for second sphere
    sphere_radius1 (number): radius for second sphere

##### Returns:

    
    
    list(number, point, number): of intersection results
      [0] = type of intersection (0=point, 1=circle, 2=spheres are identical)
      [1] = Point of intersection or plane of circle intersection
      [2] = radius of circle if circle intersection
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane0 = rs.WorldXYPlane()
    plane1 = rs.MovePlane(plane0, (10,0,0))
    radius = 10
    results = rs.IntersectSpheres(plane0, radius, plane1, radius)
    if results:
        if results[0] == 0: rs.AddPoint(results[1])
        else: rs.AddCircle( results[1], results[2])

##### See Also:

  * IntersectBreps
  * IntersectPlanes

  

IsBrep

    
    
    IsBrep(object_id)

Verifies an object is a Brep, or a boundary representation model, object.

##### Parameters:

    
    
    object_id (guid): The object's identifier.

##### Returns:

    
    
    bool: True if successful, otherwise False.
    None: on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a Brep")
    if rs.IsBrep(obj):
        print("The object is a Brep.")
    else:
        print("The object is not a Brep.")

##### See Also:

  * IsPolysurface
  * IsPolysurfaceClosed
  * IsSurface

  

IsCone

    
    
    IsCone(object_id)

Determines if a surface is a portion of a cone

##### Parameters:

    
    
    object_id (guid): the surface object's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    if surface:
        if rs.IsCone(surface):
            print("The surface is a portion of a cone.")
        else:
            print("The surface is not a portion of a cone.")

##### See Also:

  * IsCylinder
  * IsSphere
  * IsSurface
  * IsTorus

  

IsCylinder

    
    
    IsCylinder(object_id)

Determines if a surface is a portion of a cone

##### Parameters:

    
    
    object_id (guid): the cylinder object's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    if surface:
        if rs.IsCylinder(surface):
            print("The surface is a portion of a cylinder.")
        else:
            print("The surface is not a portion of a cylinder.")

##### See Also:

  * IsCone
  * IsSphere
  * IsSurface
  * IsTorus

  

IsPlaneSurface

    
    
    IsPlaneSurface(object_id)

Verifies an object is a plane surface. Plane surfaces can be created by the
Plane command. Note, a plane surface is not a planar NURBS surface

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface to trim", rs.filter.surface)
    if surface and rs.IsPlaneSurface(surface):
        print("got a plane surface")
    else:
        print("not a plane surface")

##### See Also:

  * IsBrep
  * IsPolysurface
  * IsSurface

  

IsPointInSurface

    
    
    IsPointInSurface(object_id, point, strictly_in=False, tolerance=None)

Verifies that a point is inside a closed surface or polysurface

##### Parameters:

    
    
    object_id (guid): the object's identifier
    point (point): The test, or sampling point
    strictly_in (bool, optional): If true, the test point must be inside by at least tolerance
    tolerance (number, optional): distance tolerance used for intersection and determining
      strict inclusion. If omitted, Rhino's internal tolerance is used

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polysurface", rs.filter.polysurface)
    if rs.IsPolysurfaceClosed(obj):
        point = rs.GetPoint("Pick a test point")
        if point:
            if rs.IsPointInSurface(obj, point):
                print("The point is inside the polysurface.")
            else:
                print("The point is not inside the polysurface.")

##### See Also:

  * IsPointOnSurface

  

IsPointOnSurface

    
    
    IsPointOnSurface(object_id, point)

Verifies that a point lies on a surface

##### Parameters:

    
    
    object_id (guid): the object's identifier
    point (point): The test, or sampling point

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surf = rs.GetObject("Select a surface")
    if rs.IsSurface(surf):
        point = rs.GetPoint("Pick a test point")
        if point:
            if rs.IsPointOnSurface(surf, point):
                print("The point is on the surface.")
            else:
                print("The point is not on the surface.")

##### See Also:

  * IsPointInSurface

  

IsPolysurface

    
    
    IsPolysurface(object_id)

Verifies an object is a polysurface. Polysurfaces consist of two or more
surfaces joined together. If the polysurface fully encloses a volume, it is
considered a solid.

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True is successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polysurface")
    if rs.IsPolysurface(obj):
        print("The object is a polysurface.")
    else:
        print("The object is not a polysurface.")

##### See Also:

  * IsBrep
  * IsPolysurfaceClosed

  

IsPolysurfaceClosed

    
    
    IsPolysurfaceClosed(object_id)

Verifies a polysurface object is closed. If the polysurface fully encloses a
volume, it is considered a solid.

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True is successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a polysurface", rs.filter.polysurface)
    if rs.IsPolysurfaceClosed(obj):
        print("The polysurface is closed.")
    else:
        print("The polysurface is not closed.")

##### See Also:

  * IsBrep
  * IsPolysurface

  

IsSphere

    
    
    IsSphere(object_id)

Determines if a surface is a portion of a sphere

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    if surface:
        if rs.IsSphere(surface):
            print("The surface is a portion of a sphere.")
        else:
            print("The surface is not a portion of a sphere.")

##### See Also:

  * IsCone
  * IsCylinder
  * IsSurface
  * IsTorus

  

IsSurface

    
    
    IsSurface(object_id)

Verifies an object is a surface. Brep objects with only one face are also
considered surfaces.

##### Parameters:

    
    
    object_id (guid): the object's identifier.

##### Returns:

    
    
    bool: True if successful, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objectId = rs.GetObject("Select a surface")
    if rs.IsSurface(objectId):
        print("The object is a surface.")
    else:
        print("The object is not a surface.")

##### See Also:

  * IsPointOnSurface
  * IsSurfaceClosed
  * IsSurfacePlanar
  * IsSurfaceSingular
  * IsSurfaceTrimmed

  

IsSurfaceClosed

    
    
    IsSurfaceClosed( surface_id, direction )

Verifies a surface object is closed in the specified direction. If the surface
fully encloses a volume, it is considered a solid

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    direction (number): 0=U direction check, 1=V direction check

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurfaceClosed(obj, 0):
        print("The surface is closed in the U direction.")
    else:
        print("The surface is not closed in the U direction.")

##### See Also:

  * IsSurface
  * IsSurfacePlanar
  * IsSurfaceSingular
  * IsSurfaceTrimmed

  

IsSurfacePeriodic

    
    
    IsSurfacePeriodic(surface_id, direction)

Verifies a surface object is periodic in the specified direction.

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    direction (number): 0=U direction check, 1=V direction check

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurfacePeriodic(obj, 0):
        print("The surface is periodic in the U direction.")
    else:
        print("The surface is not periodic in the U direction.")

##### See Also:

  * IsSurface
  * IsSurfaceClosed
  * IsSurfacePlanar
  * IsSurfaceSingular
  * IsSurfaceTrimmed

  

IsSurfacePlanar

    
    
    IsSurfacePlanar(surface_id, tolerance=None)

Verifies a surface object is planar

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    tolerance (number): tolerance used when checked. If omitted, the current absolute
      tolerance is used

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurfacePlanar(obj):
        print("The surface is planar.")
    else:
        print("The surface is not planar.")

##### See Also:

  * IsSurface
  * IsSurfaceClosed
  * IsSurfaceSingular
  * IsSurfaceTrimmed

  

IsSurfaceRational

    
    
    IsSurfaceRational(surface_id)

Verifies a surface object is rational

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurfaceRational(obj):
        print("The surface is rational.")
    else:
        print("The surface is not rational.")

##### See Also:

  * IsSurface
  * IsSurfaceClosed
  * IsSurfacePlanar
  * IsSurfaceTrimmed

  

IsSurfaceSingular

    
    
    IsSurfaceSingular(surface_id, direction)

Verifies a surface object is singular in the specified direction. Surfaces are
considered singular if a side collapses to a point.

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    direction (number):
      0=south
      1=east
      2=north
      3=west

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurfaceSingular(obj, 0):
        print("The surface is singular.")
    else:
        print("The surface is not singular.")

##### See Also:

  * IsSurface
  * IsSurfaceClosed
  * IsSurfacePlanar
  * IsSurfaceTrimmed

  

IsSurfaceTrimmed

    
    
    IsSurfaceTrimmed(surface_id)

Verifies a surface object has been trimmed

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurfaceTrimmed(obj):
        print("The surface is trimmed.")
    else:
        print("The surface is not trimmed.")

##### See Also:

  * IsSurface
  * IsSurfaceClosed
  * IsSurfacePlanar
  * IsSurfaceSingular

  

IsTorus

    
    
    IsTorus(surface_id)

Determines if a surface is a portion of a torus

##### Parameters:

    
    
    surface_id (guid): the surface object's identifier

##### Returns:

    
    
    bool: True if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    if surface:
        if rs.IsTorus(surface):
            print("The surface is a portion of a torus.")
        else:
            print("The surface is not a portion of a torus.")

##### See Also:

  * IsCone
  * IsCylinder
  * IsSphere
  * IsSurface

  

SurfaceSphere

    
    
    SurfaceSphere(surface_id)

Gets the sphere definition from a surface, if possible.

##### Parameters:

    
    
    surface_id (guid): the identifier of the surface object

##### Returns:

    
    
    (plane, number): The equatorial plane of the sphere, and its radius.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    if surface:
        result = rs.SurfaceSphere(surface)
        if result:
            print("The sphere radius is: " + str(result[1]))

##### See Also:

  * SurfaceCylinder

  

JoinSurfaces

    
    
    JoinSurfaces(object_ids, delete_input=False, return_all=False)

Joins two or more surface or polysurface objects together to form one
polysurface object

##### Parameters:

    
    
    object_ids ([guid, ...]) list of object identifiers
    delete_input (bool, optional): Delete the original surfaces
    return_all (bool, optional): Return all surfaces in result

##### Returns:

    
    
    guid or guid list: identifier, or list of identifiers if return_all == True, of newly created object(s) on success
    None: on failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select surfaces in order", rs.filter.surface)
    if objs and len(objs)>1: rs.JoinSurfaces(objs)

##### See Also:

  * ExplodePolysurfaces
  * IsPolysurface
  * IsPolysurfaceClosed
  * IsSurface
  * IsSurfaceClosed

  

MakeSurfacePeriodic

    
    
    MakeSurfacePeriodic(surface_id, direction, delete_input=False)

Makes an existing surface a periodic NURBS surface

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    direction (number): The direction to make periodic, either 0=U or 1=V
    delete_input (bool, optional): delete the input surface

##### Returns:

    
    
    guid: if delete_input is False, identifier of the new surface
    guid: if delete_input is True, identifier of the modifier surface
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    obj = rs.GetObject("Select  a surface", rs.filter.surface)
    if not rs.IsSurfacePeriodic(obj,  0):
        rs.MakeSurfacePeriodic(obj,  0)

##### See Also:

  * IsSurfacePeriodic

  

OffsetSurface

    
    
    OffsetSurface(surface_id, distance, tolerance=None, both_sides=False, create_solid=False)

Offsets a trimmed or untrimmed surface by a distance. The offset surface will
be added to Rhino.

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    distance (number): the distance to offset
    tolerance (number, optional): The offset tolerance. Use 0.0 to make a loose offset. Otherwise, the
      document's absolute tolerance is usually sufficient.
    both_sides (bool, optional): Offset to both sides of the input surface
    create_solid (bool, optional): Make a solid object

##### Returns:

    
    
    guid: identifier of the new object if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurface(surface):
        rs.OffsetSurface( surface, 10.0 )

##### See Also:

  * OffsetCurve

  

PullCurve

    
    
    PullCurve(surface, curve, delete_input=False)

Pulls a curve object to a surface object

##### Parameters:

    
    
    surface (guid): the surface's identifier
    curve (guid): the curve's identifier
    delete_input (bool, optional) should the input items be deleted

##### Returns:

    
    
    list(guid, ...): of new curves if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    curve = rs.GetObject("Select curve to pull", rs.filter.curve )
    surface = rs.GetObject("Select surface that pulls", rs.filter.surface )
    rs.PullCurve(surface, curve)

##### See Also:

  * IsSurface

  

RebuildSurface

    
    
    RebuildSurface(object_id, degree=(3,3), pointcount=(10,10))

Rebuilds a surface to a given degree and control point count. For more
information see the Rhino help file for the Rebuild command

##### Parameters:

    
    
    object_id (guid): the surface's identifier
    degree ([number, number], optional): two numbers that identify surface degree in both U and V directions
    pointcount ([number, number], optional): two numbers that identify the surface point count in both the U and V directions

##### Returns:

    
    
    bool: True of False indicating success or failure

  

RemoveSurfaceKnot

    
    
    RemoveSurfaceKnot(surface, uv_parameter, v_direction)

Deletes a knot from a surface object.

##### Parameters:

    
    
    surface (guid): The reference of the surface object
    uv_parameter (list(number, number)): An indexable item containing a U,V parameter on the surface. List, tuples and UVIntervals will work.
      Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
    v_direction (bool): if True, or 1, the V direction will be addressed. If False, or 0, the U direction.

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    
    srf_info = rs.GetSurfaceObject()
    if srf_info:
        srf_id = srf_info[0]
        srf_param = srf_info[4]
        rs.RemoveSurfaceKnot(srf_id, srf_param, 1)

##### See Also:

  * RemoveSurfaceKnot

  

ReverseSurface

    
    
    ReverseSurface(surface_id, direction)

Reverses U or V directions of a surface, or swaps (transposes) U and V
directions.

##### Parameters:

    
    
    surface_id (guid): identifier of a surface object
    direction (number): as a bit coded flag to swap
          1 = reverse U
          2 = reverse V
          4 = transpose U and V (values can be combined)

##### Returns:

    
    
    bool: indicating success or failure
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface to reverse")
    if rs.IsSurface(obj):
        rs.ReverseSurface( obj, 1 )

##### See Also:

  * FlipSurface
  * IsSurface

  

ShootRay

    
    
    ShootRay(surface_ids, start_point, direction, reflections=10)

Shoots a ray at a collection of surfaces

##### Parameters:

    
    
    surface_ids ([guid, ...]): one of more surface identifiers
    start_point (point): starting point of the ray
    direction (vector):  vector identifying the direction of the ray
    reflections (number, optional): the maximum number of times the ray will be reflected

##### Returns:

    
    
    list(point, ...): of reflection points on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def TestRayShooter():
        corners = []
        corners.append((0,0,0))
        corners.append((10,0,0))
        corners.append((10,10,0))
        corners.append((0,10,0))
        corners.append((0,0,10))
        corners.append((10,0,10))
        corners.append((10,10,10))
        corners.append((0,10,10))
        box = rs.AddBox(corners)
        dir = 10,7.5,7
        reflections = rs.ShootRay(box, (0,0,0), dir)
        rs.AddPolyline( reflections )
        rs.AddPoints( reflections )
    TestRayShooter()

##### See Also:

  * IsPolysurface
  * IsSurface

  

ShortPath

    
    
    ShortPath(surface_id, start_point, end_point)

Creates the shortest possible curve(geodesic) between two points on a surface.
For more details, see the ShortPath command in Rhino help

##### Parameters:

    
    
    surface_id (guid): identifier of a surface
    start_point, end_point (point): start/end points of the short curve

##### Returns:

    
    
    guid: identifier of the new surface on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface for short path", rs.filter.surface + rs.filter.surface)
    if surface:
        start = rs.GetPointOnSurface(surface, "First point")
        end = rs.GetPointOnSurface(surface, "Second point")
        rs.ShortPath(surface, start, end)

##### See Also:

  * EvaluateSurface
  * SurfaceClosestPoint

  

ShrinkTrimmedSurface

    
    
    ShrinkTrimmedSurface(object_id, create_copy=False)

Shrinks the underlying untrimmed surfaces near to the trimming boundaries. See
the ShrinkTrimmedSrf command in the Rhino help.

##### Parameters:

    
    
    object_id (guid): the surface's identifier
    create_copy (bool, optional): If True, the original surface is not deleted

##### Returns:

    
    
    bool: If create_copy is False, True or False indicating success or failure
    bool: If create_copy is True, the identifier of the new surface
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filter = rs.filter.surface | rs.filter.polysurface
    surface = rs.GetObject("Select surface or polysurface to shrink", filter )
    if surface: rs.ShrinkTrimmedSurface( surface )

##### See Also:

  * IsSurfaceTrimmed

  

SplitBrep

    
    
    SplitBrep(brep_id, cutter_id, delete_input=False)

Splits a brep

##### Parameters:

    
    
    brep (guid): identifier of the brep to split
    cutter (guid): identifier of the brep to split with

##### Returns:

    
    
    list(guid, ...): identifiers of split pieces on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filter = rs.filter.surface + rs.filter.polysurface
    brep = rs.GetObject("Select brep to split", filter)
    cutter = rs.GetObject("Select cutting brep", filter)
    rs.SplitBrep ( brep, cutter )

##### See Also:

  * IsBrep

  

SurfaceArea

    
    
    SurfaceArea(object_id)

Calculate the area of a surface or polysurface object. The results are based
on the current drawing units

##### Parameters:

    
    
    object_id (guid): the surface's identifier

##### Returns:

    
    
    list(number, number): of area information on success (area, absolute error bound)
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if obj:
        massprop = rs.SurfaceArea( obj )
        if massprop:
            print("The surface area is: {}".format(massprop[0]))

##### See Also:

  * SurfaceAreaCentroid
  * SurfaceAreaMoments

  

SurfaceAreaCentroid

    
    
    SurfaceAreaCentroid(object_id)

Calculates the area centroid of a surface or polysurface

##### Parameters:

    
    
    object_id (guid): the surface's identifier

##### Returns:

    
    
    list(point, tuple(number, number, number)): Area centroid information (Area Centroid, Error bound in X, Y, Z)
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if obj:
        massprop = rs.SurfaceAreaCentroid(obj)
        if massprop: rs.AddPoint( massprop[0] )

##### See Also:

  * SurfaceArea
  * SurfaceAreaMoments

  

SurfaceAreaMoments

    
    
    SurfaceAreaMoments(surface_id)

Calculates area moments of inertia of a surface or polysurface object. See the
Rhino help for "Mass Properties calculation details"

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    list(tuple(number, number,number), ...): of moments and error bounds in tuple(X, Y, Z) - see help topic
      Index   Description
      [0]     First Moments.
      [1]     The absolute (+/-) error bound for the First Moments.
      [2]     Second Moments.
      [3]     The absolute (+/-) error bound for the Second Moments.
      [4]     Product Moments.
      [5]     The absolute (+/-) error bound for the Product Moments.
      [6]     Area Moments of Inertia about the World Coordinate Axes.
      [7]     The absolute (+/-) error bound for the Area Moments of Inertia about World Coordinate Axes.
      [8]     Area Radii of Gyration about the World Coordinate Axes.
      [9]     The absolute (+/-) error bound for the Area Radii of Gyration about World Coordinate Axes.
      [10]    Area Moments of Inertia about the Centroid Coordinate Axes.
      [11]    The absolute (+/-) error bound for the Area Moments of Inertia about the Centroid Coordinate Axes.
      [12]    Area Radii of Gyration about the Centroid Coordinate Axes.
      [13]    The absolute (+/-) error bound for the Area Radii of Gyration about the Centroid Coordinate Axes.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if obj:
        massprop= rs.SurfaceAreaMoments(obj)
        if massprop:
            print("Area Moments of Inertia about the World Coordinate Axes: {}".format(massprop[6]))

##### See Also:

  * SurfaceArea
  * SurfaceAreaCentroid

  

SurfaceClosestPoint

    
    
    SurfaceClosestPoint(surface_id, test_point)

Returns U,V parameters of point on a surface that is closest to a test point

##### Parameters:

    
    
    surface_id (guid): identifier of a surface object
    test_point (point): sampling point

##### Returns:

    
    
    list(number, number): The U,V parameters of the closest point on the surface if successful.
    None: on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurface(obj):
        point = rs.GetPointOnSurface(obj, "Pick a test point")
        if point:
            param = rs.SurfaceClosestPoint(obj, point)
            if param:
                print("Surface U parameter: {}".format(str(param[0])))
                print("Surface V parameter: {}".format(str(param[1])))

##### See Also:

  * BrepClosestPoint
  * EvaluateSurface
  * IsSurface

  

SurfaceCone

    
    
    SurfaceCone(surface_id)

Returns the definition of a surface cone

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    tuple(plane, number, number): containing the definition of the cone if successful
      [0]   the plane of the cone. The apex of the cone is at the
            plane's origin and the axis of the cone is the plane's z-axis
      [1]   the height of the cone
      [2]   the radius of the cone
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cone = rs.AddCone(rs.WorldXYPlane(), 6, 2, False)
    if rs.IsCone(cone):
        cone_def = rs.SurfaceCone(cone)
        rs.AddCone( cone_def[0], cone_def[1], cone_def[2], False )

  

SurfaceCurvature

    
    
    SurfaceCurvature(surface_id, parameter)

Returns the curvature of a surface at a U,V parameter. See Rhino help for
details of surface curvature

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    parameter (number, number): u,v parameter

##### Returns:

    
    
    tuple(point, vector, number, number, number, number, number): of curvature information
      [0]   point at specified U,V parameter
      [1]   normal direction
      [2]   maximum principal curvature
      [3]   maximum principal curvature direction
      [4]   minimum principal curvature
      [5]   minimum principal curvature direction
      [6]   gaussian curvature
      [7]   mean curvature
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    srf = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurface(srf):
        point = rs.GetPointOnSurface(srf, "Pick a test point")
        if point:
            param = rs.SurfaceClosestPoint(srf, point)
            if param:
                data = rs.SurfaceCurvature(srf, param)
                if data:
                    print("Surface curvature evaluation at parameter {}:".format(param))
                    print(" 3-D Point:{}".format(data[0]))
                    print(" 3-D Normal:{}".format(data[1]))
                    print(" Maximum principal curvature: {} {}".format(data[2], data[3]))
                    print(" Minimum principal curvature: {} {}".format(data[4], data[5]))
                    print(" Gaussian curvature:{}".format(data[6]))
                    print(" Mean curvature:{}".format(data[7]))

##### See Also:

  * CurveCurvature

  

SurfaceCylinder

    
    
    SurfaceCylinder(surface_id)

Returns the definition of a cylinder surface

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    tuple(plane, number, number): of the cylinder plane, height, radius on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cylinder = rs.AddCylinder(rs.WorldXYPlane(), 6, 2, False)
    if rs.IsCylinder(cylinder):
        plane, height, radius = rs.SurfaceCylinder(cylinder)
        rs.AddCylinder(plane, height, radius, False)

##### See Also:

  * SurfaceSphere

  

SurfaceDegree

    
    
    SurfaceDegree(surface_id, direction=2)

Returns the degree of a surface object in the specified direction

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    direction (number, optional): The degree U, V direction
              0 = U
              1 = V
              2 = both

##### Returns:

    
    
    number: Single number if `direction` = 0 or 1
    tuple(number, number): of two values if `direction` = 2
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurface(obj):
        print("Degree in U direction: {}".format(rs.SurfaceDegree(obj, 0)))
        print("Degree in V direction: {}".format(rs.SurfaceDegree(obj, 1)))

##### See Also:

  * IsSurface
  * SurfaceDomain

  

SurfaceDomain

    
    
    SurfaceDomain(surface_id, direction)

Returns the domain of a surface object in the specified direction.

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    direction (number): domain direction 0 = U, or 1 = V

##### Returns:

    
    
    list(number, number): containing the domain interval in the specified direction
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    object = rs.GetObject("Select a surface", rs.filter.surface)
    if rs.IsSurface(object):
        domainU = rs.SurfaceDomain(object, 0)
        domainV = rs.SurfaceDomain(object, 1)
        print("Domain in U direction: {}".format(domainU))
        print("Domain in V direction: {}".format(domainV))

##### See Also:

  * IsSurface
  * SurfaceDegree

  

SurfaceEditPoints

    
    
    SurfaceEditPoints(surface_id, return_parameters=False, return_all=True)

Returns the edit, or Greville points of a surface object. For each surface
control point, there is a corresponding edit point

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    return_parameters (bool, optional): If False, edit points are returned as a list of
      3D points. If True, edit points are returned as a list of U,V surface
      parameters
    return_all (bool, options): If True, all surface edit points are returned. If False,
      the function will return surface edit points based on whether or not the
      surface is closed or periodic

##### Returns:

    
    
    list(point, ...): if return_parameters is False, a list of 3D points
    list((number, number), ...): if return_parameters is True, a list of U,V parameters
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface")
    if rs.IsSurface(obj):
        points = rs.SurfaceEditPoints(obj)
        if points: rs.AddPointCloud(points)

##### See Also:

  * IsSurface
  * SurfacePointCount
  * SurfacePoints

  

SurfaceEvaluate

    
    
    SurfaceEvaluate(surface_id, parameter, derivative)

A general purpose surface evaluator

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    parameter ([number, number]): u,v parameter to evaluate
    derivative (number): number of derivatives to evaluate

##### Returns:

    
    
    list((point, vector, ...), ...): list length (derivative+1)*(derivative+2)/2 if successful.  The elements are as follows:
      Element  Description
      [0]      The 3-D point.
      [1]      The first derivative.
      [2]      The first derivative.
      [3]      The second derivative.
      [4]      The second derivative.
      [5]      The second derivative.
      [6]      etc...
    None: If not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def TestSurfaceEvaluate():
        srf = rs.GetObject("Select surface to evaluate", rs.filter.surface, True)
        if srf is None: return
        point = rs.GetPointOnSurface(srf, "Point to evaluate")
        if point is None: return
        der = rs.GetInteger("Number of derivatives to evaluate", 1, 1)
        if der is None: return
        uv = rs.SurfaceClosestPoint(srf, point)
        res = rs.SurfaceEvaluate(srf, uv, der)
        if res is None:
            print("Failed to evaluate surface.")
            return
        for i,r in enumerate(res):
            print("{} = {}".format(i, r))
    TestSurfaceEvaluate()

##### See Also:

  * EvaluateSurface

  

SurfaceFrame

    
    
    SurfaceFrame(surface_id, uv_parameter)

Returns a plane based on the normal, u, and v directions at a surface U,V
parameter

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    uv_parameter ([number, number]): u,v parameter to evaluate

##### Returns:

    
    
    plane: plane on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetSurfaceObject("Select a surface")
    if surface:
        plane = rs.SurfaceFrame(surface[0], surface[4])
        rs.ViewCPlane(None, plane)

##### See Also:

  * EvaluateSurface
  * SurfaceClosestPoint
  * SurfaceNormal

  

SurfaceIsocurveDensity

    
    
    SurfaceIsocurveDensity(surface_id, density=None)

Returns or sets the isocurve density of a surface or polysurface object. An
isoparametric curve is a curve of constant U or V value on a surface. Rhino
uses isocurves and surface edge curves to visualize the shape of a NURBS
surface

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    density (number, optional): the isocurve wireframe density. The possible values are
        -1: Hides the surface isocurves
         0: Display boundary and knot wires
         1: Display boundary and knot wires and one interior wire if there
            are no interior knots
       >=2: Display boundary and knot wires and (N+1) interior wires

##### Returns:

    
    
    number: If density is not specified, then the current isocurve density if successful
    number: If density is specified, the the previous isocurve density if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface | rs.filter.polysurface)
    if obj: rs.SurfaceIsocurveDensity( obj, 8 )

##### See Also:

  * IsPolysurface
  * IsSurface

  

SurfaceKnotCount

    
    
    SurfaceKnotCount(surface_id)

Returns the control point count of a surface surface_id = the surface's
identifier

##### Parameters:

    
    
    surface_id (guid): the surface object's identifier

##### Returns:

    
    
    list(number, number): a list containing (U count, V count) on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface")
    if rs.IsSurface(obj):
        count = rs.SurfaceKnotCount(obj)
        print("Knot count in U direction: {}".format(count[0]))
        print("Knot count in V direction: {}".format(count[1]))

##### See Also:

  * IsSurface
  * SurfaceKnots

  

SurfaceKnots

    
    
    SurfaceKnots(surface_id)

Returns the knots, or knot vector, of a surface object.

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    list(number, number): knot values of the surface if successful. The list will
     contain the following information:
     Element   Description
       [0]     Knot vector in U direction
       [1]     Knot vector in V direction
     None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface")
    if rs.IsSurface(obj):
        knots = rs.SurfaceKnots(obj)
        if knots:
            vector = knots[0]
            print("Knot vector in U direction")
            for item in vector: print("Surface knot value: {}".format(item))
            vector = knots[1]
            print("Knot vector in V direction")
            for item in vector: print("Surface knot value: {}".format(item))

##### See Also:

  * IsSurface
  * SurfaceKnotCount

  

SurfaceNormal

    
    
    SurfaceNormal(surface_id, uv_parameter)

Returns 3D vector that is the normal to a surface at a parameter

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    uv_parameter  ([number, number]): the uv parameter to evaluate

##### Returns:

    
    
    vector: Normal vector on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.surface)
    if obj:
        point = rs.GetPointOnSurface(obj)
        if point:
            param = rs.SurfaceClosestPoint(obj, point)
            normal = rs.SurfaceNormal(obj, param)
            rs.AddPoints( [point, point + normal] )

##### See Also:

  * SurfaceClosestPoint
  * SurfaceDomain

  

SurfaceNormalizedParameter

    
    
    SurfaceNormalizedParameter(surface_id, parameter)

Converts surface parameter to a normalized surface parameter; one that ranges
between 0.0 and 1.0 in both the U and V directions

##### Parameters:

    
    
    surface_id (guid) the surface's identifier
    parameter ([number, number]): the surface parameter to convert

##### Returns:

    
    
    list(number, number): normalized surface parameter if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select surface")
    if rs.IsSurface(obj):
        domain_u = rs.SurfaceDomain(obj, 0)
        domain_v = rs.SurfaceDomain(obj, 1)
        parameter = (domain_u[1] + domain_u[0]) / 2.0, (domain_v[1] + domain_v[0]) / 2.0
        print("Surface parameter: {}".format(parameter))
        normalized = rs.SurfaceNormalizedParameter(obj, parameter)
        print("Normalized parameter: {}".format(normalized))

##### See Also:

  * SurfaceDomain
  * SurfaceParameter

  

SurfaceParameter

    
    
    SurfaceParameter(surface_id, parameter)

Converts normalized surface parameter to a surface parameter; or within the
surface's domain

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    parameter ([number, number]): the normalized parameter to convert

##### Returns:

    
    
    tuple(number, number): surface parameter on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select surface")
    if obj:
        normalized = (0.5, 0.5)
        print("Normalized parameter: {}".format(normalized))
        parameter = rs.SurfaceParameter(obj, normalized)
        print("Surface parameter: {}".format(parameter))

##### See Also:

  * SurfaceDomain
  * SurfaceNormalizedParameter

  

SurfacePointCount

    
    
    SurfacePointCount(surface_id)

Returns the control point count of a surface surface_id = the surface's
identifier

##### Parameters:

    
    
    surface_id (guid): the surface object's identifier

##### Returns:

    
    
    list(number, number): THe number of control points in UV direction. (U count, V count)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface")
    if rs.IsSurface(obj):
        count = rs.SurfacePointCount(obj)
        print("Point count in U direction: {}".format(count[0]))
        print("Point count in V direction: {}".format(count[1]))

##### See Also:

  * IsSurface
  * SurfacePoints

  

SurfacePoints

    
    
    SurfacePoints(surface_id, return_all=True)

Returns the control points, or control vertices, of a surface object

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    return_all (bool, optional): If True all surface edit points are returned. If False,
      the function will return surface edit points based on whether or not
      the surface is closed or periodic

##### Returns:

    
    
    list(point, ...): the control points if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def PrintControlPoints():
        surface = rs.GetObject("Select surface", rs.filter.surface)
        points = rs.SurfacePoints(surface)
        if points is None: return
        count = rs.SurfacePointCount(surface)
        i = 0
        for u in range(count[0]):
            for v in range(count[1]):
                print("CV[{}".format(u, ",", v, "] = ", points[i]))
                i += 1
    PrintControlPoints()

##### See Also:

  * IsSurface
  * SurfacePointCount

  

SurfaceTorus

    
    
    SurfaceTorus(surface_id)

Returns the definition of a surface torus

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    tuple(plane, number, number): containing the definition of the torus if successful
      [0]   the base plane of the torus
      [1]   the major radius of the torus
      [2]   the minor radius of the torus
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    torus = rs.AddTorus(rs.WorldXYPlane(), 6, 2)
    if rs.IsTorus(torus):
        torus_def = rs.SurfaceTorus(torus)
        rs.AddTorus( torus_def[0], torus_def[1], torus_def[2] )

  

SurfaceVolume

    
    
    SurfaceVolume(object_id)

Calculates volume of a closed surface or polysurface

##### Parameters:

    
    
    object_id (guid): the surface's identifier

##### Returns:

    
    
    list(number, tuple(X, Y, Z): volume data returned (Volume, Error bound) on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.polysurface)
    if rs.IsPolysurfaceClosed(obj):
        massprop = rs.SurfaceVolume(obj)
        if massprop:
            print("The polysurface volume is: {}".format(massprop[0]))

##### See Also:

  * SurfaceVolume
  * SurfaceVolumeCentroid
  * SurfaceVolumeMoments

  

SurfaceVolumeCentroid

    
    
    SurfaceVolumeCentroid(object_id)

Calculates volume centroid of a closed surface or polysurface

##### Parameters:

    
    
    object_id (guid): the surface's identifier

##### Returns:

    
    
    list(point, tuple(X, Y, Z): volume data returned (Volume Centriod, Error bound) on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.polysurface)
    if rs.IsPolysurfaceClosed(obj):
        massprop= rs.SurfaceVolumeCentroid(obj)
        if massprop: rs.AddPoint( massprop[0] )

##### See Also:

  * SurfaceVolume
  * SurfaceVolumeMoments

  

SurfaceVolumeMoments

    
    
    SurfaceVolumeMoments(surface_id)

Calculates volume moments of inertia of a surface or polysurface object. For
more information, see Rhino help for "Mass Properties calculation details"

##### Parameters:

    
    
    surface_id (guid): the surface's identifier

##### Returns:

    
    
    list(tuple(number, number,number), ...): of moments and error bounds in tuple(X, Y, Z) - see help topic
      Index   Description
      [0]     First Moments.
      [1]     The absolute (+/-) error bound for the First Moments.
      [2]     Second Moments.
      [3]     The absolute (+/-) error bound for the Second Moments.
      [4]     Product Moments.
      [5]     The absolute (+/-) error bound for the Product Moments.
      [6]     Area Moments of Inertia about the World Coordinate Axes.
      [7]     The absolute (+/-) error bound for the Area Moments of Inertia about World Coordinate Axes.
      [8]     Area Radii of Gyration about the World Coordinate Axes.
      [9]     The absolute (+/-) error bound for the Area Radii of Gyration about World Coordinate Axes.
      [10]    Area Moments of Inertia about the Centroid Coordinate Axes.
      [11]    The absolute (+/-) error bound for the Area Moments of Inertia about the Centroid Coordinate Axes.
      [12]    Area Radii of Gyration about the Centroid Coordinate Axes.
      [13]    The absolute (+/-) error bound for the Area Radii of Gyration about the Centroid Coordinate Axes.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select a surface", rs.filter.polysurface)
    if rs.IsPolysurfaceClosed(obj):
        massprop = rs.SurfaceVolumeMoments(obj)
        if massprop:
            print("Volume Moments of Inertia about the World Coordinate Axes: {}".format(massprop[6]))

##### See Also:

  * SurfaceVolume
  * SurfaceVolumeCentroid

  

SurfaceWeights

    
    
    SurfaceWeights(object_id)

Returns list of weight values assigned to the control points of a surface. The
number of weights returned will be equal to the number of control points in
the U and V directions.

##### Parameters:

    
    
    object_id (guid): the surface's identifier

##### Returns:

    
    
    list(number, ...): point weights.
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surf = rs.GetObject("Select a surface")
    if rs.IsSurface(surf):
        weights = rs.SurfaceWeights(surf)
        if weights:
            for w in weights:
                print("Surface control point weight value:{}".format(w))

##### See Also:

  * IsSurface
  * SurfacePointCount
  * SurfacePoints

  

TrimBrep

    
    
    TrimBrep(object_id, cutter, tolerance=None)

Trims a surface using an oriented cutter

##### Parameters:

    
    
    object_id (guid): surface or polysurface identifier
    cutter (guid|plane): surface, polysurface, or plane performing the trim
    tolerance (number, optional): trimming tolerance. If omitted, the document's absolute
      tolerance is used

##### Returns:

    
    
    list(guid, ...): identifiers of retained components on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filter = rs.filter.surface + rs.filter.polysurface
    obj = rs.GetObject("Select surface or polysurface to trim", filter)
    if obj:
        cutter = rs.GetObject("Select cutting surface or polysurface", filter)
        if cutter:
            rs.TrimBrep(obj,cutter)

##### See Also:

  * TrimSurface

  

TrimSurface

    
    
    TrimSurface( surface_id, direction, interval, delete_input=False)

Remove portions of the surface outside of the specified interval

##### Parameters:

    
    
    surface_id (guid): surface identifier
    direction (number, optional): 0(U), 1(V), or 2(U and V)
    interval (interval): sub section of the surface to keep.
      If both U and V then a list or tuple of 2 intervals
    delete_input (bool, optional): should the input surface be deleted

##### Returns:

    
    
    guid: new surface identifier on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface to split", rs.filter.surface)
    if surface:
        domain_u = rs.SurfaceDomain(surface, 0)
        domain_u[0] = (domain_u[1] - domain_u[0]) * 0.25
        rs.TrimSurface( surface, 0, domain_u, True )

  

UnrollSurface

    
    
    UnrollSurface(surface_id, explode=False, following_geometry=None, absolute_tolerance=None, relative_tolerance=None)

Flattens a developable surface or polysurface

##### Parameters:

    
    
    surface_id (guid): the surface's identifier
    explode (bool, optional): If True, the resulting surfaces ar not joined
    following_geometry ({guid, ...]): List of curves, dots, and points which
      should be unrolled with the surface

##### Returns:

    
    
    list(guid, ...): of unrolled surface ids
    tuple((guid, ...),(guid, ...)): if following_geometry is not None, a tuple
      [1] is the list of unrolled surface ids
      [2] is the list of unrolled following geometry

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Select surface or polysurface to unroll", rs.filter.surface + rs.filter.polysurface)
    if surface: rs.UnrollSurface(surface)

  

ChangeSurfaceDegree

    
    
    ChangeSurfaceDegree(object_id, degree)

Changes the degree of a surface object. For more information see the Rhino
help file for the ChangeDegree command.

##### Parameters:

    
    
    object_id (guid): the object's identifier.
    degree ([number, number]) two integers, specifying the degrees for the U  V directions

##### Returns:

    
    
    bool: True of False indicating success or failure.
    None: on failure.

##### See Also:

  * IsSurface

  

## toolbar

CloseToolbarCollection

    
    
    CloseToolbarCollection(name, prompt=False)

Closes a currently open toolbar collection

##### Parameters:

    
    
    name (str): name of a currently open toolbar collection
    prompt  (bool, optional): if True, user will be prompted to save the collection file
      if it has been modified prior to closing

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.ToolbarCollectionNames()
    if names:
        for name in names: rs.CloseToolbarCollection( name, True )

##### See Also:

  * IsToolbarCollection
  * OpenToolbarCollection
  * ToolbarCollectionCount
  * ToolbarCollectionNames
  * ToolbarCollectionPath

  

HideToolbar

    
    
    HideToolbar(name, toolbar_group)

Hides a previously visible toolbar group in an open toolbar collection

##### Parameters:

    
    
    name (str): name of a currently open toolbar file
    toolbar_group (str): name of a toolbar group to hide

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
    name = rs.IsToolbarCollection(file)
    if names: rs.HideToolbar(name, "Layer")

##### See Also:

  * IsToolbar
  * IsToolbarVisible
  * ShowToolbar
  * ToolbarCount
  * ToolbarNames

  

IsToolbar

    
    
    IsToolbar(name, toolbar, group=False)

Verifies a toolbar (or toolbar group) exists in an open collection file

##### Parameters:

    
    
    name (str): name of a currently open toolbar file
    toolbar (str): name of a toolbar group
    group (bool, optional): if toolbar parameter is referring to a toolbar group

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
    name = rs.IsToolbarCollection(file)
    if name:
        if rs.IsToolbar(name, "Layer"):
            print("The collection contains the Layer toolbar.")
        else:
            print("The collection does not contain the Layer toolbar.")

##### See Also:

  * HideToolbar
  * IsToolbarVisible
  * ShowToolbar
  * ToolbarCount
  * ToolbarNames

  

IsToolbarCollection

    
    
    IsToolbarCollection(file)

Verifies that a toolbar collection is open

##### Parameters:

    
    
    file (str): full path to a toolbar collection file

##### Returns:

    
    
    str: Rhino-assigned name of the toolbar collection if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
    name = rs.IsToolbarCollection(file)
    if name: print("The default toolbar collection is loaded.")
    else: print("The default toolbar collection is not loaded.")

##### See Also:

  * CloseToolbarCollection
  * OpenToolbarCollection
  * ToolbarCollectionCount
  * ToolbarCollectionNames
  * ToolbarCollectionPath

  

IsToolbarDocked

    
    
    IsToolbarDocked(name, toolbar_group)

Verifies that a toolbar group in an open toolbar collection is visible

##### Parameters:

    
    
    name (str): name of a currently open toolbar file
    toolbar_group (str): name of a toolbar group

##### Returns:

    
    
    boolean: True or False indicating success or failure
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rc = rs.IsToolbarDocked("Default", "Main1")
    if rc==True:
        print("The Main1 toolbar is docked.")
    elif rc==False:
        print("The Main1 toolbar is not docked.")
    else:
        print("The Main1 toolbar is not visible.")

##### See Also:

  * IsToolbar
  * IsToolbarVisible

  

IsToolbarVisible

    
    
    IsToolbarVisible(name, toolbar_group)

Verifies that a toolbar group in an open toolbar collection is visible

##### Parameters:

    
    
    name (str): name of a currently open toolbar file
    toolbar_group (str): name of a toolbar group

##### Returns:

    
    
    bool:True or False indicating success or failure
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
    name = rs.IsToolbarCollection(file)
    if name:
        if rs.IsToolbarVisible(name, "Layer"): print("The Layer toolbar is visible.")
        else: print("The Layer toolbar is not visible.")

##### See Also:

  * HideToolbar
  * IsToolbar
  * ShowToolbar
  * ToolbarCount
  * ToolbarNames

  

OpenToolbarCollection

    
    
    OpenToolbarCollection(file)

Opens a toolbar collection file

##### Parameters:

    
    
    file (str): full path to the collection file

##### Returns:

    
    
    str: Rhino-assigned name of the toolbar collection if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
    name = rs.IsToolbarCollection(file)
    if name is None: rs.OpenToolbarCollection(file)

##### See Also:

  * CloseToolbarCollection
  * IsToolbarCollection
  * ToolbarCollectionCount
  * ToolbarCollectionNames
  * ToolbarCollectionPath

  

SaveToolbarCollection

    
    
    SaveToolbarCollection(name)

Saves an open toolbar collection to disk

##### Parameters:

    
    
    name (str): name of a currently open toolbar file

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = "Default"
    rs.SaveToolbarCollection(name)

##### See Also:

  * SaveToolbarCollectionAs

  

SaveToolbarCollectionAs

    
    
    SaveToolbarCollectionAs(name, file)

Saves an open toolbar collection to a different disk file

##### Parameters:

    
    
    name (str): name of a currently open toolbar file
    file (str): full path to file name to save to

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    name = "Default"
    file = "D:\\NewDefault.rui"
    rs.SaveToolbarCollectionAs(name,file)

##### See Also:

  * SaveToolbarCollection

  

ShowToolbar

    
    
    ShowToolbar(name, toolbar_group)

Shows a previously hidden toolbar group in an open toolbar collection

##### Parameters:

    
    
    name (str): name of a currently open toolbar file
    toolbar_group (str): name of a toolbar group to show

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
    name = rs.IsToolbarCollection(file)
    if name: rs.ShowToolbar(name, "Layer")

##### See Also:

  * HideToolbar
  * IsToolbar
  * IsToolbarVisible
  * ToolbarCount
  * ToolbarNames

  

ToolbarCollectionCount

    
    
    ToolbarCollectionCount()

Returns number of currently open toolbar collections

##### Returns:

    
    
    number: the number of currently open toolbar collections

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.ToolbarCollectionCount()
    print("There are {} toolbar(s) collections loaded".format(count))

##### See Also:

  * CloseToolbarCollection
  * IsToolbarCollection
  * OpenToolbarCollection
  * ToolbarCollectionNames
  * ToolbarCollectionPath

  

ToolbarCollectionNames

    
    
    ToolbarCollectionNames()

Returns names of all currently open toolbar collections

##### Returns:

    
    
    list(str, ...): the names of all currently open toolbar collections

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.ToolbarCollectionNames()
    if names:
        for name in names: print(name)

##### See Also:

  * CloseToolbarCollection
  * IsToolbarCollection
  * OpenToolbarCollection
  * ToolbarCollectionCount
  * ToolbarCollectionPath

  

ToolbarCollectionPath

    
    
    ToolbarCollectionPath(name)

Returns full path to a currently open toolbar collection file

##### Parameters:

    
    
    name (str): name of currently open toolbar collection

##### Returns:

    
    
    str: full path on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.ToolbarCollectionNames()
    if names:
        for name in names: print(rs.ToolbarCollectionPath(name))

##### See Also:

  * CloseToolbarCollection
  * IsToolbarCollection
  * OpenToolbarCollection
  * ToolbarCollectionCount
  * ToolbarCollectionNames

  

ToolbarCount

    
    
    ToolbarCount(name, groups=False)

Returns the number of toolbars or groups in a currently open toolbar file

##### Parameters:

    
    
    name (str): name of currently open toolbar collection
    groups (bool, optional): If true, return the number of toolbar groups in the file

##### Returns:

    
    
    number: number of toolbars on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.ToolbarCollectionNames()
    if names:
        count = rs.ToolbarCount(names[0])
        print("The {} collection contains {} toolbars.".format(names[0], count))

##### See Also:

  * HideToolbar
  * IsToolbar
  * IsToolbarVisible
  * ShowToolbar
  * ToolbarNames

  

ToolbarNames

    
    
    ToolbarNames(name, groups=False)

Returns the names of all toolbars (or toolbar groups) found in a currently
open toolbar file

##### Parameters:

    
    
    name (str): name of currently open toolbar collection
    groups (bool, optional): If true, return the names of toolbar groups in the file

##### Returns:

    
    
    list(str, ...): names of all toolbars (or toolbar groups) on success
    None: on error

##### Example:

    
    
    import rhinoscriptsytax as rs
    names = rs.ToolbarCollectionNames()
    if names:
        toolbars = rs.ToolbarNames(names[0])
        if toolbars:
            for toolbar in toolbars: print(toolbar)

##### See Also:

  * HideToolbar
  * IsToolbar
  * IsToolbarVisible
  * ShowToolbar
  * ToolbarCount

  

## transformation

IsXformIdentity

    
    
    IsXformIdentity(xform)

Verifies a matrix is the identity matrix

##### Parameters:

    
    
    xform (transform): List or Rhino.Geometry.Transform.  A 4x4 transformation matrix.

##### Returns:

    
    
    bool: True or False indicating success or failure.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    xform = rs.XformIdentity()
    print(rs.IsXformIdentity(xform))

##### See Also:

  * IsXformSimilarity
  * IsXformZero
  * XformIdentity

  

IsXformSimilarity

    
    
    IsXformSimilarity(xform)

Verifies a matrix is a similarity transformation. A similarity transformation
can be broken into a sequence of dialations, translations, rotations, and
reflections

##### Parameters:

    
    
    xform (transform): List or Rhino.Geometry.Transform.  A 4x4 transformation matrix.

##### Returns:

    
    
    bool: True if this transformation is an orientation preserving similarity, otherwise False.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    xform = rs.BlockInstanceXform(block)
    print(rs.IsXformSimilarity(xform))

##### See Also:

  * IsXformIdentity
  * IsXformZero

  

IsXformZero

    
    
    IsXformZero(xform)

verifies that a matrix is a zero transformation matrix

##### Parameters:

    
    
    xform (transform): List or Rhino.Geometry.Transform.  A 4x4 transformation matrix.

##### Returns:

    
    
    bool: True or False indicating success or failure.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    xform = rs.XformZero()
    print(rs.IsXformZero(xform))

##### See Also:

  * IsXformIdentity
  * IsXformSimilarity
  * XformZero

  

XformChangeBasis

    
    
    XformChangeBasis(initial_plane, final_plane)

Returns a change of basis transformation matrix or None on error

##### Parameters:

    
    
    initial_plane (plane): the initial plane
    final_plane (plane): the final plane

##### Returns:

    
    
    transform: The 4x4 transformation matrix if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    import math
    objs = rs.GetObjects("Select objects to shear")
    if objs:
        cplane = rs.ViewCPlane()
        cob = rs.XformChangeBasis(rs.WorldXYPlane(), cplane)
        shear2d = rs.XformIdentity()
        shear2d[0,2] = math.tan(math.radians(45.0))
        cob_inverse = rs.XformChangeBasis(cplane, rs.WorldXYPlane())
        temp = rs.XformMultiply(shear2d, cob)
        xform = rs.XformMultiply(cob_inverse, temp)
        rs.TransformObjects( objs, xform, True )

##### See Also:

  * XformCPlaneToWorld
  * XformWorldToCPlane

  

XformChangeBasis2

    
    
    XformChangeBasis2(x0,y0,z0,x1,y1,z1)

Returns a change of basis transformation matrix of None on error

##### Parameters:

    
    
    x0,y0,z0 (vector): initial basis
    x1,y1,z1 (vector): final basis

##### Returns:

    
    
    transform: The 4x4 transformation matrix if successful
    None: if not successful

  

XformCompare

    
    
    XformCompare(xform1, xform2)

Compares two transformation matrices

##### Parameters:

    
    
    xform1, xform2 = matrices to compare

##### Returns:

    
    
    number:
    -1 if xform1<xform2
     1 if xform1>xform2
     0 if xform1=xform2

##### Example:

    
    
    import rhinoscriptsyntax as rs
    xform0 = rs.XformZero()
    xform1 = rs.XformIdentity()
    print(rs.XformCompare(xform0, xform1))

##### See Also:

  * IsXformIdentity
  * IsXformSimilarity
  * IsXformZero

  

XformCPlaneToWorld

    
    
    XformCPlaneToWorld(point, plane)

Transform point from construction plane coordinates to world coordinates

##### Parameters:

    
    
    point (point): A 3D point in construction plane coordinates.
    plane (plane): The construction plane

##### Returns:

    
    
    point: A 3D point in world coordinates

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.ViewCPlane()
    point = rs.XFormCPlaneToWorld([0,0,0], plane)
    if point: print("World point: {}".format(point))

##### See Also:

  * XformWorldToCPlane

  

XformDeterminant

    
    
    XformDeterminant(xform)

Returns the determinant of a transformation matrix. If the determinant of a
transformation matrix is 0, the matrix is said to be singular. Singular
matrices do not have inverses.

##### Parameters:

    
    
    xform (transform): List or Rhino.Geometry.Transform.  A 4x4 transformation matrix.

##### Returns:

    
    
    number: The determinant if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    xform = rs.BlockInstanceXform(obj)
    if xform: print(rs.XformDeterminant(xform))

##### See Also:

  * XformInverse

  

XformDiagonal

    
    
    XformDiagonal(diagonal_value)

Returns a diagonal transformation matrix. Diagonal matrices are 3x3 with the
bottom row [0,0,0,1]

##### Parameters:

    
    
    diagonal_value (number): the diagonal value

##### Returns:

    
    
    transform: The 4x4 transformation matrix if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def printmatrix(xform):
        for i in range(4):
            print("[{}, {}, {}, {}]".format(xform[i,0], xform[i,1], xform[i,2], xform[i,3]))
    printmatrix(rs.XformDiagonal(3))

##### See Also:

  * XformIdentity
  * XformZero

  

XformIdentity

    
    
    XformIdentity()

returns the identity transformation matrix

##### Returns:

    
    
    transform: The 4x4 transformation matrix

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def printmatrix(xform):
        for i in range(4):
            print("[{}, {}, {}, {}]".format(xform[i,0], xform[i,1], xform[i,2], xform[i,3]))
    printmatrix(rs.XformIdentity())

##### See Also:

  * XformDiagonal
  * XformZero

  

XformInverse

    
    
    XformInverse(xform)

Returns the inverse of a non-singular transformation matrix

##### Parameters:

    
    
    xform (transform): List or Rhino.Geometry.Transform.  A 4x4 transformation matrix.

##### Returns:

    
    
    transform: The inverted 4x4 transformation matrix if successful.
    None: if matrix is non-singular or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    xform = rs.BlockInstanceXform(obj)
    if xform:
        rs.TransformObject( obj, rs.XformInverse(xform) )

##### See Also:

  * XformDeterminant

  

XformMirror

    
    
    XformMirror(mirror_plane_point, mirror_plane_normal)

Creates a mirror transformation matrix

##### Parameters:

    
    
    mirror_plane_point (point): point on the mirror plane
    mirror_plane_normal (vector): a 3D vector that is normal to the mirror plane

##### Returns:

    
    
    transform: mirror Transform matrix

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to mirror")
    if objs:
        plane = rs.ViewCPlane()
        xform = rs.XformMirror(plane.Origin, plane.Normal)
        rs.TransformObjects( objs, xform, True )

##### See Also:

  * XformPlanarProjection
  * XformRotation1
  * XformRotation2
  * XformRotation3
  * XformRotation4
  * XformScale
  * XformShear
  * XformTranslation

  

XformMultiply

    
    
    XformMultiply(xform1, xform2)

Multiplies two transformation matrices, where result = xform1 * xform2

##### Parameters:

    
    
    xform1 (transform): List or Rhino.Geometry.Transform.  The first 4x4 transformation matrix to multiply.
    xform2 (transform): List or Rhino.Geometry.Transform.  The second 4x4 transformation matrix to multiply.

##### Returns:

    
    
    transform: result transformation on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    import math
    objs = rs.GetObjects("Select objects to shear")
    if objs:
        cplane = rs.ViewCPlane()
        cob = rs.XformChangeBasis(rs.WorldXYPlane(), cplane)
        shear2d = rs.XformIdentity()
        shear2d[0,2] = math.tan(math.radians(45.0))
        cob_inv = rs.XformChangeBasis(cplane, rs.WorldXYPlane())
        temp = rs.XformMultiply(shear2d, cob)
        xform = rs.XformMultiply(cob_inv, temp)
        rs.TransformObjects( objs, xform, True )

##### See Also:

  * XformPlanarProjection
  * XformRotation1
  * XformRotation2
  * XformRotation3
  * XformRotation4
  * XformScale
  * XformShear
  * XformTranslation

  

XformPlanarProjection

    
    
    XformPlanarProjection(plane)

Returns a transformation matrix that projects to a plane.

##### Parameters:

    
    
    plane (plane): The plane to project to.

##### Returns:

    
    
    transform: The 4x4 transformation matrix.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to project")
    if objects:
        cplane = rs.ViewCPlane()
        xform = rs.XformPlanarProjection(cplane)
        rs.TransformObjects( objects, xform, True )

##### See Also:

  * XformMirror
  * XformRotation1
  * XformRotation2
  * XformRotation3
  * XformRotation4
  * XformScale
  * XformShear
  * XformTranslation

  

XformRotation1

    
    
    XformRotation1(initial_plane, final_plane)

Returns a rotation transformation that maps initial_plane to final_plane. The
planes should be right hand orthonormal planes.

##### Parameters:

    
    
    initial_plane (plane): plane to rotate from
    final_plane (plane): plane to rotate to

##### Returns:

    
    
    transform: The 4x4 transformation matrix.
    None: on error.

  

XformRotation2

    
    
    XformRotation2(angle_degrees, rotation_axis, center_point)

Returns a rotation transformation around an axis

##### Parameters:

    
    
    angle_degrees (number): rotation angle in degrees
    rotation_axis (vector): rotation axis
    center_point (point): rotation center

##### Returns:

    
    
    transform: The 4x4 transformation matrix.
    None: on error.

  

XformRotation3

    
    
    XformRotation3( start_direction, end_direction, center_point )

Calculate the minimal transformation that rotates start_direction to
end_direction while fixing center_point

##### Parameters:

    
    
    start_direction, end_direction (vector): 3d vectors
    center_point (point): the rotation center

##### Returns:

    
    
    transform: The 4x4 transformation matrix.
    None: on error.

  

XformRotation4

    
    
    XformRotation4(x0, y0, z0, x1, y1, z1)

Returns a rotation transformation.

##### Parameters:

    
    
    x0,y0,z0 (vector): Vectors defining the initial orthonormal frame
    x1,y1,z1 (vector): Vectors defining the final orthonormal frame

##### Returns:

    
    
    transform: The 4x4 transformation matrix.
    None: on error.

  

XformScale

    
    
    XformScale(scale, point=None)

Creates a scale transformation

##### Parameters:

    
    
    scale (number|point|vector|[number, number, number]): single number, list of 3 numbers, Point3d, or Vector3d
    point (point, optional): center of scale. If omitted, world origin is used

##### Returns:

    
    
    transform: The 4x4 transformation matrix on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to scale")
    if objs:
        xform = rs.XformScale( (3.0,1.0,1.0) )
        rs.TransformObjects( objs, xform, True)

##### See Also:

  * XformMirror
  * XformPlanarProjection
  * XformRotation1
  * XformRotation2
  * XformRotation3
  * XformRotation4
  * XformShear
  * XformTranslation

  

XformScreenToWorld

    
    
    XformScreenToWorld(point, view=None, screen_coordinates=False)

Transforms a point from either client-area coordinates of the specified view
or screen coordinates to world coordinates. The resulting coordinates are
represented as a 3-D point

##### Parameters:

    
    
    point (point): 2D point
    view (str, optional): title or identifier of a view. If omitted, the active view is used
    screen_coordinates (bool, optional): if False, point is in client-area coordinates. If True,
    point is in screen-area coordinates

##### Returns:

    
    
    point: on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point2d = 200,100
    view = rs.CurrentView()
    point = rs.XformScreenToWorld(point2d, view)
    print(point)

##### See Also:

  * XformWorldToScreen

  

XformShear

    
    
    XformShear(plane, x, y, z)

Returns a shear transformation matrix

##### Parameters:

    
    
    plane (plane): plane[0] is the fixed point
    x,y,z (number): each axis scale factor

##### Returns:

    
    
    transform: The 4x4 transformation matrix on success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objects = rs.GetObjects("Select objects to shear")
    if objects:
        cplane = rs.ViewCPlane()
        xform = rs.XformShear(cplane, (1,1,0), (-1,1,0), (0,0,1))
        rs.TransformObjects(objects, xform, True)

##### See Also:

  * XformMirror
  * XformPlanarProjection
  * XformRotation1
  * XformRotation2
  * XformRotation3
  * XformRotation4
  * XformScale
  * XformTranslation

  

XformTranslation

    
    
    XformTranslation(vector)

Creates a translation transformation matrix

##### Parameters:

    
    
    vector (vector): List of 3 numbers, Point3d, or Vector3d.  A 3-D translation vector.

##### Returns:

    
    
    transform: The 4x4 transformation matrix is successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select objects to copy")
    if objs:
        xform = rs.XformTranslation([1,0,0])
        rs.TransformObjects( objs, xform, True )

##### See Also:

  * XformMirror
  * XformPlanarProjection
  * XformRotation1
  * XformRotation2
  * XformRotation3
  * XformRotation4
  * XformScale
  * XformShear

  

XformWorldToCPlane

    
    
    XformWorldToCPlane(point, plane)

Transforms a point from world coordinates to construction plane coordinates.

##### Parameters:

    
    
    point (point): A 3D point in world coordinates.
    plane (plane): The construction plane

##### Returns:

    
    
    (point): 3D point in construction plane coordinates

##### Example:

    
    
    import rhinoscriptsyntax as rs
    plane = rs.ViewCPlane()
    point = rs.XformWorldToCPlane([0,0,0], plane)
    if point: print("CPlane point:{}".format(point))

##### See Also:

  * XformCPlaneToWorld

  

XformWorldToScreen

    
    
    XformWorldToScreen(point, view=None, screen_coordinates=False)

Transforms a point from world coordinates to either client-area coordinates of
the specified view or screen coordinates. The resulting coordinates are
represented as a 2D point

##### Parameters:

    
    
    point (point): 3D point in world coordinates
    view (str, optional): title or identifier of a view. If omitted, the active view is used
    screen_coordinates (bool, optional): if False, the function returns the results as
      client-area coordinates. If True, the result is in screen-area coordinates

##### Returns:

    
    
    (point): 2D point on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = (0.0, 0.0, 0.0)
    view = rs.CurrentView()
    point2d = rs.XformWorldToScreen(point, view)
    print(point2d)

##### See Also:

  * XformScreenToWorld

  

XformZero

    
    
    XformZero()

Returns a zero transformation matrix

##### Returns:

    
    
    transform: a zero transformation matrix

##### Example:

    
    
    import rhinoscriptsyntax as rs
    def printmatrix(xform):
        for i in range(4):
            print("[{}, {}, {}, {}]".format(xform[i,0], xform[i,1], xform[i,2], xform[i,3]))
    printmatrix( rs.XformZero() )

##### See Also:

  * XformDiagonal
  * XformIdentity

  

## userdata

DeleteDocumentData

    
    
    DeleteDocumentData(section=None, entry=None)

Removes user data strings from the current document

##### Parameters:

    
    
    section (str, optional): section name. If omitted, all sections and their corresponding
      entries are removed
    entry (str, optional): entry name. If omitted, all entries for section are removed

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.DeleteDocumentData( "MySection1", "MyEntry1" )
    rs.DeleteDocumentData( "MySection1", "MyEntry2" )
    rs.DeleteDocumentData( "MySection2", "MyEntry1" )

##### See Also:

  * DocumentDataCount
  * GetDocumentData
  * IsDocumentData
  * SetDocumentData

  

DocumentDataCount

    
    
    DocumentDataCount()

Returns the number of user data strings in the current document

##### Returns:

    
    
    number: the number of user data strings in the current document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    count = rs.DocumentDataCount()
    print("RhinoScript document user data count: {}".format(count))

##### See Also:

  * DeleteDocumentData
  * GetDocumentData
  * IsDocumentData
  * SetDocumentData

  

DocumentUserTextCount

    
    
    DocumentUserTextCount()

Returns the number of user text strings in the current document

##### Returns:

    
    
    number: the number of user text strings in the current document

##### See Also:

  * GetDocumentUserText
  * IsDocumentUserText
  * SetDocumentUserText

  

GetDocumentData

    
    
    GetDocumentData(section=None, entry=None)

Returns a user data item from the current document

##### Parameters:

    
    
    section (str, optional): section name. If omitted, all section names are returned
    entry (str, optional): entry name. If omitted, all entry names for section are returned

##### Returns:

    
    
    list(str, ...): of all section names if section name is omitted
    list(str, ...) of all entry names for a section if entry is omitted
    str: value of the entry if both section and entry are specified
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    value = rs.GetDocumentData("MySection1", "MyEntry1")
    print(value)
    value = rs.GetDocumentData("MySection1", "MyEntry2")
    print(value)
    value = rs.GetDocumentData("MySection2", "MyEntry1")
    print(value)

##### See Also:

  * DeleteDocumentData
  * DocumentDataCount
  * IsDocumentData
  * SetDocumentData

  

GetDocumentUserText

    
    
    GetDocumentUserText(key=None)

Returns user text stored in the document

##### Parameters:

    
    
    key (str, optional): key to use for retrieving user text. If empty, all keys are returned

##### Returns:

    
    
    str: If key is specified, then the associated value if successful.
    list(str, ...):If key is not specified, then a list of key names if successful.
    None: If not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print(rs.GetDocumentUserText("Designer"))
    print(rs.GetDocumentUserText("Notes"))

##### See Also:

  * SetDocumentUserText

  

GetUserText

    
    
    GetUserText(object_id, key=None, attached_to_geometry=False)

Returns user text stored on an object.

##### Parameters:

    
    
    object_id (guid): the object's identifies
    key (str, optional): the key name. If omitted all key names for an object are returned
    attached_to_geometry (bool, optional): location on the object to retrieve the user text

##### Returns:

    
    
    str: if key is specified, the associated value if successful
    list(str, ...): if key is not specified, a list of key names if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        print(rs.GetUserText(obj, "PartNo"))
        print(rs.GetUserText(obj, "Price"))

##### See Also:

  * IsUserText
  * SetUserText

  

IsDocumentData

    
    
    IsDocumentData()

Verifies the current document contains user data

##### Returns:

    
    
    bool: True or False indicating the presence of Script user data

##### Example:

    
    
    import rhinoscriptsyntax as rs
    result = rs.IsDocumentData()
    if result:
        print("This document contains Script document user data")
    else:
        print("This document contains no Script document user data")

##### See Also:

  * DeleteDocumentData
  * DocumentDataCount
  * GetDocumentData
  * SetDocumentData

  

IsDocumentUserText

    
    
    IsDocumentUserText()

Verifies the current document contains user text

##### Returns:

    
    
    bool: True or False indicating the presence of Script user text

##### See Also:

  * GetDocumentUserText
  * SetDocumentUserText

  

IsUserText

    
    
    IsUserText(object_id)

Verifies that an object contains user text

##### Parameters:

    
    
    object_id (guid): the object's identifier

##### Returns:

    
    
    number: result of test:
      0 = no user text
      1 = attribute user text
      2 = geometry user text
      3 = both attribute and geometry user text

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")  
    if obj:
        usertext_type = rs.IsUserText(obj)
        if usertext_type==0: print("Object has no user text")
        elif usertext_type==1: print("Object has attribute user text")
        elif usertext_type==2: print("Object has geometry user text")
        elif usertext_type==3: print("Object has attribute and geometry user text")
        else: print("Object does not exist")

##### See Also:

  * GetUserText
  * SetUserText

  

SetDocumentData

    
    
    SetDocumentData(section, entry, value)

Adds or sets a user data string to the current document

##### Parameters:

    
    
    section (str): the section name
    entry (str): the entry name
    value (str): the string value

##### Returns:

    
    
    str: The previous value

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.SetDocumentData( "MySection1", "MyEntry1", "MyValue1" )
    rs.SetDocumentData( "MySection1", "MyEntry2", "MyValue2" )
    rs.SetDocumentData( "MySection2", "MyEntry1", "MyValue1" )

##### See Also:

  * DeleteDocumentData
  * DocumentDataCount
  * GetDocumentData
  * IsDocumentData

  

SetDocumentUserText

    
    
    SetDocumentUserText(key, value=None)

Sets or removes user text stored in the document

##### Parameters:

    
    
    key (str): key name to set
    value (str): The string value to set. If omitted the key/value pair
      specified by key will be deleted

##### Returns:

    
    
    bool: True or False indicating success

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.SetDocumentUserText("Designer", "Steve Baer")
    rs.SetDocumentUserText("Notes", "Added some layer and updated some geometry")

##### See Also:

  * GetDocumentUserText

  

SetUserText

    
    
    SetUserText(object_id, key, value=None, attach_to_geometry=False)

Sets or removes user text stored on an object.

##### Parameters:

    
    
    object_id (str): the object's identifier
    key (str): the key name to set
    value (str, optional) the string value to set. If omitted, the key/value pair
        specified by key will be deleted
    attach_to_geometry (bool, optional): location on the object to store the user text

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        rs.SetUserText( obj, "PartNo", "KM40-4960" )
        rs.SetUserText( obj, "Price", "1.25" )

##### See Also:

  * GetUserText
  * IsUserText

  

## userinterface

BrowseForFolder

    
    
    BrowseForFolder(folder=None, message=None, title=None)

Display browse-for-folder dialog allowing the user to select a folder

##### Parameters:

    
    
    folder (str, optional): a default folder
    message (str, optional): a prompt or message
    title (str, optional): a dialog box title

##### Returns:

    
    
    str: selected folder
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    folder = rs.BrowseForFolder("C:\\Program Files\\" )
    if folder: print(folder)

##### See Also:

  * OpenFileName
  * SaveFileName

  

CheckListBox

    
    
    CheckListBox(items, message=None, title=None)

Displays a list of items in a checkable-style list dialog box

##### Parameters:

    
    
    items ([[str, bool], ...]): a list of tuples containing a string and a boolean check state
    message (str, optional):  a prompt or message
    title (str, optional):  a dialog box title

##### Returns:

    
    
    list((str, bool), ...): of tuples containing the input string in items along with their new boolean check value
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    layers = rs.LayerNames()
    if layers:
        items  = [(layer, rs.IsLayerOn(layer)) for layer in layers]
        results  = rs.CheckListBox(items, "Turn layers on/off", "Layers")
        if results:
            for  layer, state in results: rs.LayerVisible(layer, state)

##### See Also:

  * ComboListBox
  * ListBox
  * MultiListBox
  * PropertyListBox

  

ComboListBox

    
    
    ComboListBox(items, message=None, title=None)

Displays a list of items in a combo-style list box dialog.

##### Parameters:

    
    
    items ([str, ...]): a list of string
    message (str, optional):  a prompt of message
    title (str, optional):  a dialog box title

##### Returns:

    
    
    str: The selected item if successful
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        layer = rs.ComboListBox(layers, "Select current layer")
        if layer: rs.CurrentLayer(layer)

##### See Also:

  * CheckListBox
  * ListBox
  * MultiListBox
  * PropertyListBox

  

EditBox

    
    
    EditBox(default_string=None, message=None, title=None)

Display dialog prompting the user to enter a string. The string value may span
multiple lines

##### Parameters:

    
    
    default_string  (str, optional):  a default string value.
    message (str, optional): a prompt message.
    title (str, optional): a dialog box title.

##### Returns:

    
    
    str: Multiple lines that are separated by carriage return-linefeed combinations if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    text = rs.EditBox(message="Enter some text")
    print(text)

##### See Also:

  * GetString
  * StringBox

  

GetAngle

    
    
    GetAngle(point=None, reference_point=None, default_angle_degrees=0, message=None)

Pause for user input of an angle

##### Parameters:

    
    
    point (point): starting, or base point
    reference_point (point, optional): if specified, the reference angle is calculated
      from it and the base point
    default_angle_degrees (number, optional): a default angle value specified
    message (str, optional): a prompt to display

##### Returns:

    
    
    number: angle in degree if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.GetPoint("Base point")
    if point:
        reference = rs.GetPoint("Reference point", point)
        if reference:
            angle = rs.GetAngle(point, reference)
            if angle!=None: print("Angle:{}".format(angle))

##### See Also:

  * GetDistance

  

GetBoolean

    
    
    GetBoolean(message, items, defaults)

Pauses for user input of one or more boolean values. Boolean values are
displayed as click-able command line option toggles

##### Parameters:

    
    
    message (str): a prompt
    items ([str, str, str], ...): list or tuple of options. Each option is a tuple of three strings
      [n][1]    description of the boolean value. Must only consist of letters
                and numbers. (no characters like space, period, or dash
      [n][2]    string identifying the false value
      [n][3]    string identifying the true value
    defaults ([bool, ...]): list of boolean values used as default or starting values

##### Returns:

    
    
    list(bool, ...): a list of values that represent the boolean values if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    items = ("Lights", "Off", "On"), ("Cameras", "Disabled", "Enabled"), ("Action", "False", "True")
    results = rs.GetBoolean("Boolean options", items, (True, True, True) )
    if results:
        for val in results: print(val)

##### See Also:

  * GetString

  

GetBox

    
    
    GetBox(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None)

Pauses for user input of a box

##### Parameters:

    
    
    mode (number): The box selection mode.
       0 = All modes
       1 = Corner. The base rectangle is created by picking two corner points
       2 = 3-Point. The base rectangle is created by picking three points
       3 = Vertical. The base vertical rectangle is created by picking three points.
       4 = Center. The base rectangle is created by picking a center point and a corner point
    base_point (point, optional): optional 3D base point
    prompt1, prompt2, prompt3 (str, optional): optional prompts to set

##### Returns:

    
    
    list(point, ...): list of eight Point3d that define the corners of the box on success
    None: is not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    box = rs.GetBox()
    if box:
        for i, pt in enumerate(box): rs.AddTextDot( i, pt )

##### See Also:

  * GetRectangle

  

GetColor

    
    
    GetColor(color=[0,0,0])

Display the Rhino color picker dialog allowing the user to select an RGB color

##### Parameters:

    
    
    color (color, optional): default RGB value. If omitted, the default color is black

##### Returns:

    
    
    color: RGB tuple of three numbers on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    color = rs.LayerColor("Default")
    rgb = rs.GetColor(color)
    if rgb: rs.LayerColor("Default", rgb)

  

GetCursorPos

    
    
    GetCursorPos()

Retrieves the cursor's position

##### Returns:

    
    
    tuple(point, point, guid, point) containing the following information
      [0]  cursor position in world coordinates
      [1]  cursor position in screen coordinates
      [2]  id of the active viewport
      [3]  cursor position in client coordinates

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    world, screen, view, client  = rs.GetCursorPos()

##### See Also:

  * XformScreenToWorld
  * XformWorldToScreen

  

GetDistance

    
    
    GetDistance(first_pt=None, distance=None, first_pt_msg='First distance point', second_pt_msg='Second distance point')

Pauses for user input of a distance.

##### Parameters:

    
    
    first_pt (point, optional): First distance point
    distance (number, optional): Default distance
    first_pt_msg (str, optional): Prompt for the first distance point
    second_pt_msg (str, optional): Prompt for the second distance point

##### Returns:

    
    
    number: The distance between the two points if successful.
    None: if not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    dist = rs.GetDistance()
    if dist:
        print( dist)

##### See Also:

  * GetAngle

  

GetEdgeCurves

    
    
    GetEdgeCurves(message=None, min_count=1, max_count=0, select=False)

Prompt the user to pick one or more surface or polysurface edge curves

##### Parameters:

    
    
    message  (str, optional):  A prompt or message.
    min_count (number, optional): minimum number of edges to select.
    max_count (number, optional): maximum number of edges to select.
    select (bool, optional): Select the duplicated edge curves.

##### Returns:

    
    
    list(tuple[guid, point, point], ...): of selection prompts (curve id, parent id, selection point)
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    edges = rs.GetEdgeCurves()
    if edges:
        for edgeinfo in edges:
            print("Curve Id ={}".format(edgeinfo[0]))
            print("Parent Id ={}".format(edgeinfo[1]))
            print("Pick point ={}".format(edgeinfo[2]))

##### See Also:

  * DuplicateEdgeCurves

  

GetInteger

    
    
    GetInteger(message=None, number=None, minimum=None, maximum=None)

Pauses for user input of a whole number.

##### Parameters:

    
    
    message (str, optional): A prompt or message.
    number (number, optional): A default whole number value.
    minimum (number, optional): A minimum allowable value.
    maximum (number, optional): A maximum allowable value.

##### Returns:

    
    
    number: The whole number input by the user if successful.
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    color = rs.LayerColor("Default")
    color = rs.GetInteger("Enter an RGB color value", color.ToArgb(), 0)
    if color: rs.LayerColor("Default", color)

  

GetLayer

    
    
    GetLayer(title="Select Layer", layer=None, show_new_button=False, show_set_current=False)

Displays dialog box prompting the user to select a layer

##### Parameters:

    
    
    title (str, optional): dialog box title
    layer (str, optional): name of a layer to preselect. If omitted, the current layer will be preselected
    show_new_button, show_set_current (bool, optional): Optional buttons to show on the dialog

##### Returns:

    
    
    str: name of selected layer if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Select object")
    if obj:
        layer = rs.GetLayer("Select Layer", rs.ObjectLayer(obj), True, True)
        if layer: rs.ObjectLayer( obj, layer )

  

GetLayers

    
    
    GetLayers(title="Select Layers", show_new_button=False)

Displays a dialog box prompting the user to select one or more layers

##### Parameters:

    
    
    title (str, optional):  dialog box title
    show_new_button (bool, optional): Optional button to show on the dialog

##### Returns:

    
    
    str: The names of selected layers if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.GetLayers("Select Layers")
    if layers:
        for layer in layers: print(layer)

##### See Also:

  * GetLayer

  

GetLine

    
    
    GetLine(mode=0, point=None, message1=None, message2=None, message3=None)

Prompts the user to pick points that define a line

##### Parameters:

    
    
    mode (number, optional): line definition mode.
      0  Default - Show all modes, start in two-point mode
      1  Two-point - Defines a line from two points.
      2  Normal - Defines a line normal to a location on a surface.
      3  Angled - Defines a line at a specified angle from a reference line.
      4  Vertical - Defines a line vertical to the construction plane.
      5  Four-point - Defines a line using two points to establish direction and two points to establish length.
      6  Bisector - Defines a line that bisects a specified angle.
      7  Perpendicular - Defines a line perpendicular to or from a curve
      8  Tangent - Defines a line tangent from a curve.
      9  Extension - Defines a line that extends from a curve.
    point (point, optional): optional starting point
    message1, message2, message3 (str, optional): optional prompts

##### Returns:

    
    
    line: Tuple of two points on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    line = rs.GetLine()
    if line: rs.AddLine( line[0],  line[1] )

##### See Also:

  * GetBox
  * GetPoint
  * GetPolyline
  * GetRectangle

  

GetLinetype

    
    
    GetLinetype(default_linetype=None, show_by_layer=False)

Displays a dialog box prompting the user to select one linetype

##### Parameters:

    
    
    default_linetype (str, optional):  Optional. The name of the linetype to select. If omitted, the current linetype will be selected.
    show_by_layer (bool, optional): If True, the "by Layer" linetype will show. Defaults to False.

##### Returns:

    
    
    str: The names of selected linetype if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    linetype = rs.GetLinetype()
    if linetype: print(linetype)

##### See Also:

  * GetLayer

  

GetMeshFaces

    
    
    GetMeshFaces(object_id, message="", min_count=1, max_count=0)

Prompts the user to pick one or more mesh faces

##### Parameters:

    
    
    object_id (guid): the mesh object's identifier
    message (str, optional): a prompt of message
    min_count (number, optional): the minimum number of faces to select
    max_count (number, optional): the maximum number of faces to select.
      If 0, the user must press enter to finish selection.
      If -1, selection stops as soon as there are at least min_count faces selected.

##### Returns:

    
    
    list(number, ...): of mesh face indices on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Select mesh", rs.filter.mesh)
    if mesh:
        indices = rs.GetMeshFaces(mesh)
        if indices:
            for index in indices: print(index)

##### See Also:

  * GetMeshVertices
  * MeshFaces
  * MeshFaceVertices
  * MeshVertices

  

GetMeshVertices

    
    
    GetMeshVertices(object_id, message="", min_count=1, max_count=0)

Prompts the user to pick one or more mesh vertices

##### Parameters:

    
    
    object_id (guid): the mesh object's identifier
    message (str, optional): a prompt of message
    min_count (number, optional): the minimum number of vertices to select
    max_count (number, optional): the maximum number of vertices to select. If 0, the user must
      press enter to finish selection. If -1, selection stops as soon as there
      are at least min_count vertices selected.

##### Returns:

    
    
    list(number, ...): of mesh vertex indices on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Select mesh", rs.filter.mesh)
    if mesh:
        indices = rs.GetMeshVertices(mesh)
        if indices:
            for index in indices: print(index)

##### See Also:

  * GetMeshFaces
  * MeshFaces
  * MeshFaceVertices
  * MeshVertices

  

GetPoint

    
    
    GetPoint(message=None, base_point=None, distance=None, in_plane=False)

Pauses for user input of a point.

##### Parameters:

    
    
    message (str, optional): A prompt or message.
    base_point (point, optional): list of 3 numbers or Point3d identifying a starting, or base point
    distance  (number, optional): constraining distance. If distance is specified, basePoint must also be specified.
    in_plane (bool, optional): constrains the point selections to the active construction plane.

##### Returns:

    
    
    point: point on success
    None: if no point picked or user canceled

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = rs.GetPoint("Pick first point")
    if point1:
        rs.AddPoint(point1)
        point2 = rs.GetPoint("Pick second point", point1)
        if point2:
            rs.AddPoint(point2)
            distance = (point1-point2).Length
            point3 = rs.GetPoint("Pick third point", point2, distance)
            if point3: rs.AddPoint(point3)

##### See Also:

  * GetPointOnCurve
  * GetPointOnSurface
  * GetPoints
  * GetRectangle

  

GetPointOnCurve

    
    
    GetPointOnCurve(curve_id, message=None)

Pauses for user input of a point constrainted to a curve object

##### Parameters:

    
    
    curve_id (guid): identifier of the curve to get a point on
    message (str, optional): a prompt of message

##### Returns:

    
    
    point: 3d point if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject("Pick a curve")
    if rs.IsCurve(obj):
        point = rs.GetPointOnCurve(obj, "Point on curve")
        if point: rs.AddPoint(point)

##### See Also:

  * GetPoint
  * GetPointOnMesh
  * GetPointOnSurface
  * GetPoints

  

GetPointOnMesh

    
    
    GetPointOnMesh(mesh_id, message=None)

Pauses for user input of a point constrained to a mesh object

##### Parameters:

    
    
    mesh_id (guid): identifier of the mesh to get a point on
    message (str, optional): a prompt or message

##### Returns:

    
    
    point: 3d point if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    mesh = rs.GetObject("Pick a mesh", rs.filter.mesh)
    if mesh:
        point = rs.GetPointOnMesh(mesh, "Point on mesh")
        if point: rs.AddPoint( point )

##### See Also:

  * GetPoint
  * GetPointOnCurve
  * GetPointOnSurface
  * GetPoints

  

GetPointOnSurface

    
    
    GetPointOnSurface(surface_id, message=None)

Pauses for user input of a point constrained to a surface or polysurface
object

##### Parameters:

    
    
    surface_id (guid): identifier of the surface to get a point on
    message (str, optional): a prompt or message

##### Returns:

    
    
    point: 3d point if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    surface = rs.GetObject("Pick a surface")
    if surface:
        point = rs.GetPointOnSurface(surface, "Point on surface")
        if point: rs.AddPoint(point)

##### See Also:

  * GetPoint
  * GetPointOnCurve
  * GetPointOnMesh
  * GetPoints

  

GetPoints

    
    
    GetPoints(draw_lines=False, in_plane=False, message1=None, message2=None, max_points=None, base_point=None)

Pauses for user input of one or more points

##### Parameters:

    
    
    draw_lines (bool, optional): Draw lines between points
    in_plane (bool, optional): Constrain point selection to the active construction plane
    message1 (str, optional): A prompt or message for the first point
    message2 (str, optional): A prompt or message for the next points
    max_points (number, optional): maximum number of points to pick. If not specified, an
                      unlimited number of points can be picked.
    base_point (point, optional): a starting or base point

##### Returns:

    
    
    list(point, ...): of 3d points if successful
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(True)
    if points: rs.AddPointCloud(points)

##### See Also:

  * GetPoint
  * GetPointOnCurve
  * GetPointOnSurface
  * GetRectangle

  

GetPolyline

    
    
    GetPolyline(flags=3, message1=None, message2=None, message3=None, message4=None, min=2, max=0)

Prompts the user to pick points that define a polyline.

##### Parameters:

    
    
    flags (number, optional) The options are bit coded flags. Values can be added together to specify more than one option. The default is 3.
      value description
      1     Permit close option. If specified, then after 3 points have been picked, the user can type "Close" and a closed polyline will be returned.
      2     Permit close snap. If specified, then after 3 points have been picked, the user can pick near the start point and a closed polyline will be returned.
      4     Force close. If specified, then the returned polyline is always closed. If specified, then intMax must be 0 or >= 4.
      Note: the default is 3, or "Permit close option = True", "Permit close snap = True", and "Force close = False".
    message1 (str, optional): A prompt or message for the first point.
    message2 (str, optional): A prompt or message for the second point.
    message3 (str, optional): A prompt or message for the third point.
    message4 (str, optional): A prompt or message for the 'next' point.
    min (number, optional): The minimum number of points to require. The default is 2.
    max (number, optional): The maximum number of points to require; 0 for no limit.  The default is 0.

##### Returns:

    
    
    list(point, ...): A list of 3-D points that define the polyline if successful.
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    arr = rs.GetPolyline()
    if arr is not None:
        doc.AddPolyline(arr)

##### See Also:

  * GetBox
  * GetLine
  * GetRectangle

  

GetReal

    
    
    GetReal(message="Number", number=None, minimum=None, maximum=None)

Pauses for user input of a number.

##### Parameters:

    
    
    message (str, optional): A prompt or message.
    number (number, optional): A default number value.
    minimum (number, optional): A minimum allowable value.
    maximum (number, optional): A maximum allowable value.

##### Returns:

    
    
    number: The number input by the user if successful.
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = rs.GetReal("Radius of new circle", 3.14, 1.0)
    if radius: rs.AddCircle( (0,0,0), radius )

##### See Also:

  * RealBox

  

GetRectangle

    
    
    GetRectangle(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None)

Pauses for user input of a rectangle

##### Parameters:

    
    
    mode (number, optional): The rectangle selection mode. The modes are as follows
        0 = All modes
        1 = Corner - a rectangle is created by picking two corner points
        2 = 3Point - a rectangle is created by picking three points
        3 = Vertical - a vertical rectangle is created by picking three points
        4 = Center - a rectangle is created by picking a center point and a corner point
    base_point (point, optional): a 3d base point
    prompt1, prompt2, prompt3 (str, optional): optional prompts

##### Returns:

    
    
    tuple(point, point, point, point): four 3d points that define the corners of the rectangle
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rect = rs.GetRectangle()
    if rect:
        for i, corner in enumerate(rect):
            rs.AddTextDot( i, corner )

##### See Also:

  * GetPoint
  * GetPoints

  

GetString

    
    
    GetString(message=None, defaultString=None, strings=None)

Pauses for user input of a string value

##### Parameters:

    
    
    message (str, optional): a prompt or message
    defaultString (str, optional): a default value
    strings ([str, ...], optional): list of strings to be displayed as a click-able command options.
                                    Note, strings cannot begin with a numeric character

##### Returns:

    
    
    str: The string either input or selected by the user if successful.
         If the user presses the Enter key without typing in a string, an empty string "" is returned.
    None: if not successful, on error, or if the user pressed cancel.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.CurrentLayer()
    layer = rs.GetString("Layer to set current", layer)
    if layer: rs.CurrentLayer(layer)

##### See Also:

  * GetBoolean
  * StringBox

  

ListBox

    
    
    ListBox(items, message=None, title=None, default=None)

Display a list of items in a list box dialog.

##### Parameters:

    
    
    items ([str, ...]): a list of values to select
    message (str, optional): a prompt of message
    title (str, optional): a dialog box title
    default (str, optional): selected item in the list

##### Returns:

    
    
    str: he selected item if successful
    None: if not successful or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layers = rs.LayerNames()
    if layers:
        result = rs.ListBox(layers, "Layer to set current")
        if result: rs.CurrentLayer( result )

##### See Also:

  * CheckListBox
  * ComboListBox
  * MultiListBox
  * PropertyListBox

  

MessageBox

    
    
    MessageBox(message, buttons=0, title="")

Displays a message box. A message box contains a message and title, plus any
combination of predefined icons and push buttons.

##### Parameters:

    
    
    message (str): A prompt or message.
    buttons (number, optional): buttons and icon to display as a bit coded flag. Can be a combination of the
      following flags. If omitted, an OK button and no icon is displayed
      0      Display OK button only.
      1      Display OK and Cancel buttons.
      2      Display Abort, Retry, and Ignore buttons.
      3      Display Yes, No, and Cancel buttons.
      4      Display Yes and No buttons.
      5      Display Retry and Cancel buttons.
      16     Display Critical Message icon.
      32     Display Warning Query icon.
      48     Display Warning Message icon.
      64     Display Information Message icon.
      0      First button is the default.
      256    Second button is the default.
      512    Third button is the default.
      768    Fourth button is the default.
      0      Application modal. The user must respond to the message box
             before continuing work in the current application.
      4096   System modal. The user must respond to the message box
             before continuing work in any application.
    title(str, optional): the dialog box title

##### Returns:

    
    
    number: indicating which button was clicked:
      1      OK button was clicked.
      2      Cancel button was clicked.
      3      Abort button was clicked.
      4      Retry button was clicked.
      5      Ignore button was clicked.
      6      Yes button was clicked.
      7      No button was clicked.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.MessageBox("Hello Rhino!")
    rs.MessageBox("Hello Rhino!", 4 | 32)
    rs.MessageBox("Hello Rhino!", 2 | 48)

  

PropertyListBox

    
    
    PropertyListBox(items, values, message=None, title=None)

Displays list of items and their values in a property-style list box dialog

##### Parameters:

    
    
    items, values ([str, ...]): list of string items and their corresponding values
    message (str, optional): a prompt or message
    title (str, optional): a dialog box title

##### Returns:

    
    
    list(str, ..): of new values on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    objs = rs.GetObjects("Select Objects")
    if objs:
        names = []
        for obj in objs:
            name = rs.ObjectName(obj)
            if name is None: name=""
            names.append(name)
        results = rs.PropertyListBox(objs, names, "Modify object name(s)")
        if results:
            for i in compat.RANGE(len(objs)):
                rs.ObjectName( objs[i], results[i] )

##### See Also:

  * CheckListBox
  * ComboListBox
  * ListBox
  * MultiListBox

  

MultiListBox

    
    
    MultiListBox(items, message=None, title=None, defaults=None)

Displays a list of items in a multiple-selection list box dialog

##### Parameters:

    
    
    items ([str, ...]) a zero-based list of string items
    message (str, optional): a prompt or message
    title (str, optional): a dialog box title
    defaults (str|[str,...], optional): either a string representing the pre-selected item in the list
                                        or a list if multiple items are pre-selected

##### Returns:

    
    
    list(str, ...): containing the selected items if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    layers = rs.LayerNames()
    if layers:
        layers  = rs.MultiListBox(layers, "Layers to lock")
    if layers:
        for  layer in layers:
            rs.LayerLocked(layer,  True)

##### See Also:

  * CheckListBox
  * ComboListBox
  * ListBox
  * PropertyListBox

  

OpenFileName

    
    
    OpenFileName(title=None, filter=None, folder=None, filename=None, extension=None)

Displays file open dialog box allowing the user to enter a file name. Note,
this function does not open the file.

##### Parameters:

    
    
    title (str, optional): A dialog box title.
    filter (str, optional): A filter string. The filter must be in the following form:
      "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.
      If omitted, the filter (*.*) is used.
    folder (str, optional): A default folder.
    filename (str, optional): a default file name
    extension (str, optional): a default file extension

##### Returns:

    
    
    str: file name is successful
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filename = rs.OpenFileName()
    if filename: rs.MessageBox(filename)
    filename = rs.OpenFileName("Open", "Text Files (*.txt)|*.txt||")
    if filename: rs.MessageBox(filename)
    filename = rs.OpenFileName("Open", "Text Files (*.txt)|*.txt|All Files (*.*)|*.*||")
    if filename: rs.MessageBox(filename)

##### See Also:

  * BrowseForFolder
  * OpenFileNames
  * SaveFileName

  

OpenFileNames

    
    
    OpenFileNames(title=None, filter=None, folder=None, filename=None, extension=None)

Displays file open dialog box allowing the user to select one or more file
names. Note, this function does not open the file.

##### Parameters:

    
    
    title (str, optional): A dialog box title.
    filter (str, optional): A filter string. The filter must be in the following form:
      "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.
      If omitted, the filter (*.*) is used.
    folder (str, optional): A default folder.
    filename (str, optional): a default file name
    extension (str, optional): a default file extension

##### Returns:

    
    
    list(str, ...): of selected file names

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filenames = rs.OpenFileNames("Open", "Text Files (*.txt)|*.txt|All Files (*.*)|*.*||")
    for filename in filenames: print(filename)

##### See Also:

  * BrowseForFolder
  * OpenFileName
  * SaveFileName

  

PopupMenu

    
    
    PopupMenu(items, modes=None, point=None, view=None)

Display a context-style popup menu. The popup menu can appear almost anywhere,
and can be dismissed by clicking the left or right mouse buttons

##### Parameters:

    
    
    items ([str, ...]): list of strings representing the menu items. An empty string or None
      will create a separator
    modes ([number, ...]): List of numbers identifying the display modes. If omitted, all
      modes are enabled.
        0 = menu item is enabled
        1 = menu item is disabled
        2 = menu item is checked
        3 = menu item is disabled and checked
    point (point, optional): a 3D point where the menu item will appear. If omitted, the menu
      will appear at the current cursor position
    view (str, optional): if point is specified, the view in which the point is computed.
      If omitted, the active view is used

##### Returns:

    
    
    number: index of the menu item picked or -1 if no menu item was picked

##### Example:

    
    
    import rhinoscriptsyntax as rs
    items = "Line", "", "Circle", "Arc"
    modes = 2,0,0,0
    result = rs.PopupMenu(items, modes)
    if result>=0: rs.MessageBox(items[result])

  

RealBox

    
    
    RealBox(message="", default_number=None, title="", minimum=None, maximum=None)

Display a dialog box prompting the user to enter a number

##### Parameters:

    
    
    message (str, optional): a prompt message.
    default_number (number, optional):  a default number.
    title (str, optional):  a dialog box title.
    minimum (number, optional):  a minimum allowable value.
    maximum (number, optional):  a maximum allowable value.

##### Returns:

    
    
    number: The newly entered number on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    radius = rs.RealBox("Enter a radius value", 5.0 )
    if radius:
        point = (0,0,0)
        rs.AddCircle( point, radius )

##### See Also:

  * GetReal

  

SaveFileName

    
    
    SaveFileName(title=None, filter=None, folder=None, filename=None, extension=None)

Display a save dialog box allowing the user to enter a file name. Note, this
function does not save the file.

##### Parameters:

    
    
    title (str, optional): A dialog box title.
    filter(str, optional): A filter string. The filter must be in the following form:
      "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.
      If omitted, the filter (*.*) is used.
    folder (str, optional): A default folder.
    filename (str, optional): a default file name
    extension (str, optional):  a default file extension

##### Returns:

    
    
    str: the file name is successful
    None: if not successful, or on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filename = rs.SaveFileName()
    if filename: rs.MessageBox(filename)
    filename = rs.SaveFileName ("Save", "Text Files (*.txt)|*.txt||")
    if filename: rs.MessageBox(filename)
    filename = rrshui.SaveFileName ("Save", "Text Files (*.txt)|*.txt|All Files (*.*)|*.*||")
    if filename: rs.MessageBox(filename)

##### See Also:

  * BrowseForFolder
  * OpenFileName

  

StringBox

    
    
    StringBox(message=None, default_value=None, title=None)

Display a dialog box prompting the user to enter a string value.

##### Parameters:

    
    
    message (str, optional): a prompt message
    default_value (str, optional): a default string value
    title (str, optional): a dialog box title

##### Returns:

    
    
    str: the newly entered string value if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layer = rs.StringBox("New layer name" )
    if layer: rs.AddLayer( layer )

##### See Also:

  * GetString

  

TextOut

    
    
    TextOut(message=None, title=None)

Display a text dialog box similar to the one used by the _What command.

##### Parameters:

    
    
    message (str): a message
    title (str, optional): the message title

##### Returns:

    
    
    None: in any case

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.TextOut("This is a long string..." )

##### See Also:

  * MessagBox

  

## utility

ContextIsRhino

    
    
    ContextIsRhino()

Return True if the script is being executed in the context of Rhino

##### Returns:

    
    
    bool: True if the script is being executed in the context of Rhino

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print(rs.ContextIsRhino())

##### See Also:

  * ContextIsGrasshopper

  

ContextIsGrasshopper

    
    
    ContextIsGrasshopper()

Return True if the script is being executed in a grasshopper component

##### Returns:

    
    
    bool: True if the script is being executed in a grasshopper component

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    print(rs.ContextIsGrasshopper())

##### See Also:

  * ContextIsRhino

  

Angle

    
    
    Angle(point1, point2, plane=True)

Measures the angle between two points

##### Parameters:

    
    
    point1, point2 (point): the input points
    plane (bool, optional): Boolean or Plane
      If True, angle calculation is based on the world coordinate system.
      If False, angle calculation is based on the active construction plane
      If a plane is provided, angle calculation is with respect to this plane

##### Returns:

    
    
    tuple(tuple(number, number), number, number, number, number): containing the following elements if successful
      element 0 = the X,Y angle in degrees
      element 1 = the elevation
      element 2 = delta in the X direction
      element 3 = delta in the Y direction
      element 4 = delta in the Z direction
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as  rs
    point1 = rs.GetPoint("First  point")
    if point1:
        point2  = rs.GetPoint("Second point")
        if point2:
            angle  = rs.Angle(point1, point2)
            if  angle: print("Angle: {}".format(angle[0]))

##### See Also:

  * Angle2
  * Distance

  

Angle2

    
    
    Angle2(line1, line2)

Measures the angle between two lines

##### Parameters:

    
    
    line1 (line): List of 6 numbers or 2 Point3d.
    line2 (line): List of 6 numbers or 2 Point3d.

##### Returns:

    
    
    tuple(number, number): containing the following elements if successful.
      0 The angle in degrees.
      1 The reflex angle in degrees.
    None: If not successful, or on error.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = rs.GetPoint("Start of first line")
    point2 = rs.GetPoint("End of first line", point1)
    point3 = rs.GetPoint("Start of second line")
    point4 = rs.GetPoint("End of second line", point3)
    angle = rs.Angle2( (point1, point2), (point3, point4))
    if angle: print("Angle: {}".format(angle))

##### See Also:

  * Angle
  * Distance

  

ClipboardText

    
    
    ClipboardText(text=None)

Returns or sets a text string to the Windows clipboard

##### Parameters:

    
    
    text (str, optional): text to set

##### Returns:

    
    
    str: if text is not specified, the current text in the clipboard
    str: if text is specified, the previous text in the clipboard
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    txt = rs.ClipboardText("Hello Rhino!")
    if txt: rs.MessageBox(txt, 0, "Clipboard Text")

  

ColorAdjustLuma

    
    
    ColorAdjustLuma(rgb, luma, scale=False)

Changes the luminance of a red-green-blue value. Hue and saturation are not
affected

##### Parameters:

    
    
    rgb (color): initial rgb value
    luma (number): The luminance in units of 0.1 percent of the total range. A
        value of luma = 50 corresponds to 5 percent of the maximum luminance
    scale (bool, optional): if True, luma specifies how much to increment or decrement the
        current luminance. If False, luma specified the absolute luminance.

##### Returns:

    
    
    color: modified rgb value if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rgb = rs.ColorAdjustLuma((128, 128, 128), 50)
    print("Red = {}".format(rs.ColorRedValue(rgb)))
    print("Green = {}".format(rs.ColorGreenValue(rgb)))
    print("Blue = {}".format(rs.ColorBlueValue(rgb)))

##### See Also:

  * ColorHLSToRGB
  * ColorRGBToHLS

  

ColorBlueValue

    
    
    ColorBlueValue(rgb)

Retrieves intensity value for the blue component of an RGB color

##### Parameters:

    
    
    rgb (color): the RGB color value

##### Returns:

    
    
    number: The blue component if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rgb = rs.LayerColor("Default")
    print("Red = {}".format(rs.ColorRedValue(rgb)))
    print("Green = {}".format(rs.ColorGreenValue(rgb)))
    print("Blue = {}".format(rs.ColorBlueValue(rgb)))

##### See Also:

  * ColorGreenValue
  * ColorRedValue

  

ColorGreenValue

    
    
    ColorGreenValue(rgb)

Retrieves intensity value for the green component of an RGB color

##### Parameters:

    
    
    rgb (color): the RGB color value

##### Returns:

    
    
    number: The green component if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rgb = rs.LayerColor("Default")
    print("Red = {}".format(rs.ColorRedValue(rgb)))
    print("Green = {}".format(rs.ColorGreenValue(rgb)))
    print("Blue = {}".format(rs.ColorBlueValue(rgb)))

##### See Also:

  * ColorBlueValue
  * ColorRedValue

  

ColorHLSToRGB

    
    
    ColorHLSToRGB(hls)

Converts colors from hue-lumanence-saturation to RGB

##### Parameters:

    
    
    hls (color): the HLS color value

##### Returns:

    
    
    color: The RGB color value if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rgb = rs.ColorHLSToRGB( (160, 120, 0) )
    print("Red = {}".format(rs.ColorRedValue(rgb)))
    print("Green = {}".format(rs.ColorGreenValue(rgb)))
    print("Blue = {}".format(rs.ColorBlueValue(rgb)))

##### See Also:

  * ColorAdjustLuma
  * ColorRGBToHLS

  

ColorRedValue

    
    
    ColorRedValue(rgb)

Retrieves intensity value for the red component of an RGB color

##### Parameters:

    
    
    hls (color): the HLS color value

##### Returns:

    
    
    color: The red color value if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rgb = rs.LayerColor("Default")
    print("Red = {}".format(rs.ColorRedValue(rgb)))
    print("Green = {}".format(rs.ColorGreenValue(rgb)))
    print("Blue = {}".format(rs.ColorBlueValue(rgb)))

##### See Also:

  * ColorBlueValue
  * ColorGreenValue

  

ColorRGBToHLS

    
    
    ColorRGBToHLS(rgb)

Convert colors from RGB to HLS

##### Parameters:

    
    
    rgb (color): the RGB color value

##### Returns:

    
    
    color: The HLS color value if successful, otherwise False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    hls = rs.ColorRGBToHLS((128, 128, 128))
    print("Hue = {}".format(hls[0]))
    print("Luminance = {}".format(hls[1]))
    print("Saturation = {}".format(hls[2]))

##### See Also:

  * ColorAdjustLuma
  * ColorHLSToRGB

  

CullDuplicateNumbers

    
    
    CullDuplicateNumbers(numbers, tolerance=None)

Removes duplicates from an array of numbers.

##### Parameters:

    
    
    numbers ([number, ...]): list or tuple
    tolerance (number, optional): The minimum distance between numbers.  Numbers that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.

##### Returns:

    
    
    list(number, ...): numbers with duplicates removed if successful.

##### Example:

    
    
    import rhinoscriptsyntax as rs
    arr = [1,1,2,2,3,3,4,4,5,5]
    arr = rs.CullDuplicateNumbers(arr)
    for n in arr: print(n)

##### See Also:

  * CullDuplicatePoints

  

CullDuplicatePoints

    
    
    CullDuplicatePoints(points, tolerance=-1)

Removes duplicates from a list of 3D points.

##### Parameters:

    
    
    points ([point, ...]): A list of 3D points.
    tolerance (number): Minimum distance between points. Points within this
      tolerance will be discarded. If omitted, Rhino's internal zero tolerance
      is used.

##### Returns:

    
    
    list(point, ...): of 3D points with duplicates removed if successful.
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints(,,"First point", "Next point")
    if points:
        points= rs.CullDuplicatePoints(points)
        for p in points: print(p)

##### See Also:

  * CullDuplicateNumbers

  

Distance

    
    
    Distance(point1, point2)

Measures distance between two 3D points, or between a 3D point and an array of
3D points.

##### Parameters:

    
    
    point1 (point): The first 3D point.
    point2 (point): The second 3D point or list of 3-D points.

##### Returns:

    
    
    point: If point2 is a 3D point then the distance if successful.
    point: If point2 is a list of points, then an list of distances if successful.
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point1 = rs.GetPoint("First point")
    if point1:
        point2 = rs.GetPoint("Second point")
        if point2:
            print("Distance: {}".format(rs.Distance(point1, point2)))

##### See Also:

  * Angle
  * Angle2

  

GetSettings

    
    
    GetSettings(filename, section=None, entry=None)

Returns string from a specified section in a initialization file.

##### Parameters:

    
    
    filename (str): name of the initialization file
    section (str, optional): section containing the entry
    entry (str, optional): entry whose associated string is to be returned

##### Returns:

    
    
    list(str, ...): If section is not specified, a list containing all section names
    list:(str, ...): If entry is not specified, a list containing all entry names for a given section
    str: If section and entry are specified, a value for entry
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    filename = rs.OpenFileName("Open", "Initialization Files (*.ini)|*.ini||")
    if filename:
        sections = rs.GetSettings(filename)
        if sections:
            section = rs.ListBox(sections, "Select a section", filename)
            if section:
                entries = rs.GetSettings(filename, section)
                if entries:
                    entry = rs.ListBox(entries, "Select an entry", section)
                    if entry:
                        value = rs.GetSettings(filename, section, entry)
                        if value: rs.MessageBox( value, 0, entry )

  

Polar

    
    
    Polar(point, angle_degrees, distance, plane=None)

Returns 3D point that is a specified angle and distance from a 3D point

##### Parameters:

    
    
    point (point): the point to transform
    plane (plane, optional): plane to base the transformation. If omitted, the world
      x-y plane is used

##### Returns:

    
    
    point: resulting point is successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = (1.0, 1.0, 0.0)
    result = rs.Polar(point, 45.0, 1.414214)
    print(result)

##### See Also:

  * PointAdd
  * PointCompare
  * PointDivide
  * PointScale
  * PointSubtract

  

SimplifyArray

    
    
    SimplifyArray(points)

Flattens an array of 3-D points into a one-dimensional list of real numbers.
For example, if you had an array containing three 3-D points, this method
would return a one-dimensional array containing nine real numbers.

##### Parameters:

    
    
    points ([point, ...]): Points to flatten

##### Returns:

    
    
    list(number, ...): A one-dimensional list containing real numbers, if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints()
    if points:
        numbers = rs.SimplifyArray(points)
        for n in numbers: print(n)

  

Sleep

    
    
    Sleep(milliseconds)

Suspends execution of a running script for the specified interval

##### Parameters:

    
    
    milliseconds (number): thousands of a second

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    print("This")
    rs.Sleep(2000)
    print("is")
    rs.Sleep(2000)
    print("a")
    rs.Sleep(2000)
    print("slow")
    rs.Sleep(2000)
    print("message!")

  

SortPointList

    
    
    SortPointList(points, tolerance=None)

Sorts list of points so they will be connected in a "reasonable" polyline
order

##### Parameters:

    
    
    points ({point, ...])the points to sort
    tolerance (number, optional): minimum distance between points. Points that fall within this tolerance
      will be discarded. If omitted, Rhino's internal zero tolerance is used.

##### Returns:

    
    
    list(point, ...): of sorted 3D points if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPointCoordinates()
    if points:
        sorted = rs.SortPointList(points)
        rs.AddPolyline(sorted)

##### See Also:

  * SortPoints

  

SortPoints

    
    
    SortPoints(points, ascending=True, order=0)

Sorts the components of an array of 3D points

##### Parameters:

    
    
    points ([point, ...]): points to sort
    ascending (bool, optional: ascending if omitted (True) or True, descending if False.
    order (number, optional): the component sort order
      Value       Component Sort Order
      0 (default) X, Y, Z
      1           X, Z, Y
      2           Y, X, Z
      3           Y, Z, X
      4           Z, X, Y
      5           Z, Y, X

##### Returns:

    
    
    list(point, ...): sorted 3-D points if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    points = rs.GetPoints()
    if points:
        points = rs.SortPoints(points)
        for p in points: print(p)

  

Str2Pt

    
    
    Str2Pt(point)

convert a formatted string value into a 3D point value

##### Parameters:

    
    
    point (str): A string that contains a delimited point like "1,2,3".

##### Returns:

    
    
    point: Point structure from the input string.
    None: error on invalid format

##### Example:

    
    
    import rhinoscriptsyntax as rs
    point = rs.Str2Pt("1,2,3")
    if point: rs.AddPoint( point )

  

CreatePoint

    
    
    CreatePoint(point, y=None, z=None)

Converts 'point' into a Rhino.Geometry.Point3d if possible. If the provided
object is already a point, it value is copied. In case the conversion fails,
an error is raised. Alternatively, you can also pass two coordinates
singularly for a point on the XY plane, or three for a 3D point.

##### Parameters:

    
    
    point (Point3d|Vector3d|Point3f|Vector3f|str|guid|[number, number, number])

##### Returns:

    
    
    point: a Rhino.Geometry.Point3d. This can be seen as an object with three indices:
      [0]  X coordinate
      [1]  Y coordinate
      [2]  Z coordinate.

  

CreateVector

    
    
    CreateVector(vector, y=None, z=None)

Converts 'vector' into a Rhino.Geometry.Vector3d if possible. If the provided
object is already a vector, it value is copied. If the conversion fails, an
error is raised. Alternatively, you can also pass two coordinates singularly
for a vector on the XY plane, or three for a 3D vector.

##### Parameters:

    
    
    vector (Vector3d|Point3d|Point3f|Vector3f\str|guid|[number, number, number])
    raise_on_error (bool, optionals): True or False

##### Returns:

    
    
    a Rhino.Geometry.Vector3d. This can be seen as an object with three indices:
    result[0]: X component, result[1]: Y component, and result[2] Z component.

  

CreatePlane

    
    
    CreatePlane(plane_or_origin, x_axis=None, y_axis=None, ignored=None)

Converts input into a Rhino.Geometry.Plane object if possible. If the provided
object is already a plane, its value is copied. The returned data is
accessible by indexing[origin, X axis, Y axis, Z axis], and that is the
suggested method to interact with the type. The Z axis is in any case computed
from the X and Y axes, so providing it is possible but not required. If the
conversion fails, an error is raised.

##### Parameters:

    
    
    plane (plane|point|point, vector, vector|[point, vector, vector])

##### Returns:

    
    
    plane: A Rhino.Geometry.plane.

  

CreateXform

    
    
    CreateXform(xform)

Converts input into a Rhino.Geometry.Transform object if possible. If the
provided object is already a transform, its value is copied. The returned data
is accessible by indexing[row, column], and that is the suggested method to
interact with the type. If the conversion fails, an error is raised.

##### Parameters:

    
    
    xform (list): the transform. This can be seen as a 4x4 matrix, given as nested lists or tuples.

##### Returns:

    
    
    transform: A Rhino.Geometry.Transform. result[0,3] gives access to the first row, last column.

  

CreateColor

    
    
    CreateColor(color, g=None, b=None, a=None)

Converts 'color' into a native color object if possible. The returned data is
accessible by indexing, and that is the suggested method to interact with the
type. Red index is [0], Green index is [1], Blue index is [2] and Alpha index
is [3]. If the provided object is already a color, its value is copied.
Alternatively, you can also pass three coordinates singularly for an RGB
color, or four for an RGBA color point.

##### Parameters:

    
    
    color ([number, number, number]): list or 3 or 4 items. Also, a single int can be passed and it will be bitwise-parsed.

##### Returns:

    
    
    color: An object that can be indexed for red, green, blu, alpha. Item[0] is red.

  

CreateInterval

    
    
    CreateInterval(interval, y=None)

Converts 'interval' into a Rhino.Geometry.Interval. If the provided object is
already an interval, its value is copied. In case the conversion fails, an
error is raised. In case a single number is provided, it will be translated to
an increasing interval that includes the provided input and 0. If two values
are provided, they will be used instead.

##### Parameters:

    
    
    interval ([number, number]): or any item that can be accessed at index 0 and 1; an Interval

##### Returns:

    
    
    interval: a Rhino.Geometry.Interval. This can be seen as an object made of two items:
      [0] start of interval
      [1] end of interval

  

## view

AddDetail

    
    
    AddDetail(layout_id, corner1, corner2, title=None, projection=1)

Add new detail view to an existing layout view

##### Parameters:

    
    
    layout_id (guid): identifier of an existing layout
    corner1, corner2 (point): 2d corners of the detail in the layout's unit system
    title (str, optional): title of the new detail
    projection (number, optional): type of initial view projection for the detail
        1 = parallel top view
        2 = parallel bottom view
        3 = parallel left view
        4 = parallel right view
        5 = parallel front view
        6 = parallel back view
        7 = perspective view

##### Returns:

    
    
    guid: identifier of the newly created detail on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layout = rs.AddLayout("Portrait", (8.5,11))
    if layout:
        rs.AddDetail(layout, (0.5,0.5), (8,10.5), None, 7)

##### See Also:

  * DeleteNamedView
  * NamedViews
  * RestoreNamedView

  

AddLayout

    
    
    AddLayout(title=None, size=None)

Adds a new page layout view

##### Parameters:

    
    
    title (str, optional): title of new layout
    size ([number, number], optional): width and height of paper for the new layout

##### Returns:

    
    
    guid: id of new layout

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.AddLayout("Portrait")

##### See Also:

  * DeleteNamedView
  * NamedViews
  * RestoreNamedView

  

AddNamedCPlane

    
    
    AddNamedCPlane(cplane_name, view=None)

Adds new named construction plane to the document

##### Parameters:

    
    
    cplane_name (str): the name of the new named construction plane
    view (guid|str): Title or identifier of the view from which to save
             the construction plane. If omitted, the current active view is used.

##### Returns:

    
    
    atr: name of the newly created construction plane if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.ViewNames()
    if views:
        for view in views:
            name = view + "_cplane"
            rs.AddNamedCPlane( name, view )

##### See Also:

  * DeleteNamedCPlane
  * NamedCPlane
  * NamedCPlanes
  * RestoreNamedCPlane

  

AddNamedView

    
    
    AddNamedView(name, view=None)

Adds a new named view to the document

##### Parameters:

    
    
    name (str): the name of the new named view
    view: (guid|str): the title or identifier of the view to save. If omitted, the current
          active view is saved

##### Returns:

    
    
    str: name fo the newly created named view if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.ViewNames()
    if views:
        for view in views:
            name = view + "_view"
            rs.AddNamedView( name, view )

##### See Also:

  * DeleteNamedView
  * NamedViews
  * RestoreNamedView

  

CurrentDetail

    
    
    CurrentDetail(layout, detail=None, return_name=True)

Returns or changes the current detail view in a page layout view

##### Parameters:

    
    
    layout (str|guid): title or identifier of an existing page layout view
    detail (str|guid, optional): title or identifier the the detail view to set
    return_name (bool, optional): return title if True, else return identifier

##### Returns:

    
    
    str: if detail is not specified, the title or id of the current detail view
    str: if detail is specified, the title or id of the previous detail view
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    layout = rs.CurrentView(return_name=False)
    if rs.IsLayout(layout):
        rs.CurrentDetail( layout, layout )

##### See Also:

  * IsDetail
  * IsLayout

  

CurrentView

    
    
    CurrentView(view=None, return_name=True)

Returns or sets the currently active view

##### Parameters:

    
    
    view (str|guid): Title or id of the view to set current.
      If omitted, only the title or identifier of the current view is returned
    return_name (bool, optional): If True, then the name, or title, of the view is returned.
      If False, then the identifier of the view is returned

##### Returns:

    
    
    str: if the title is not specified, the title or id of the current view
    str: if the title is specified, the title or id of the previous current view
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    previous = rs.CurrentView("Perspective")
    print("The previous current view was {}".format(previous))
    viewId = rs.CurrentView( return_name=False )
    print("The identifier of the current view is {}".format(viewId))

##### See Also:

  * IsViewCurrent
  * ViewNames

  

DeleteNamedCPlane

    
    
    DeleteNamedCPlane(name)

Removes a named construction plane from the document

##### Parameters:

    
    
    name (str): name of the construction plane to remove

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cplanes = rs.NamedCplanes()
    if cplanes:
        for cplane in cplanes: rs.DeleteNamedCPlane(cplane)

##### See Also:

  * AddNamedCPlane
  * NamedCPlane
  * NamedCPlanes
  * RestoreNamedCPlane

  

DeleteNamedView

    
    
    DeleteNamedView(name)

Removes a named view from the document

##### Parameters:

    
    
    name (str): name of the named view to remove

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.NamedViews()
    if views:
        for view in views: rs.DeleteNamedView(view)

##### See Also:

  * AddNamedView
  * NamedViews
  * RestoreNamedView

  

DetailLock

    
    
    DetailLock(detail_id, lock=None)

Returns or modifies the projection locked state of a detail

##### Parameters:

    
    
    detail_id (guid): identifier of a detail object
    lock (bool, optional) the new lock state

##### Returns:

    
    
    bool: if lock==None, the current detail projection locked state
    bool: if lock is True or False, the previous detail projection locked state
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    detail = rs.GetObject("select a detail", rs.filter.detail)
    if detail: rs.DetailLock(detail,True)

##### See Also:

  * IsDetail
  * IsLayout

  

DetailScale

    
    
    DetailScale(detail_id, model_length=None, page_length=None)

Returns or modifies the scale of a detail object

##### Parameters:

    
    
    detail_id (guid): identifier of a detail object
    model_length (number, optional): a length in the current model units
    page_length (number, optional): a length in the current page units

##### Returns:

    
    
    number: current page to model scale ratio if model_length and page_length are both None
    number: previous page to model scale ratio if model_length and page_length are values
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    detail = rs.GetObject("select a detail", rs.filter.detail)
    if detail: rs.DetailScale(detail,1,1)

##### See Also:

  * IsDetail
  * IsLayout

  

IsDetail

    
    
    IsDetail(layout, detail)

Verifies that a detail view exists on a page layout view

##### Parameters:

    
    
    layout (str|guid): title or identifier of an existing page layout
    detail (str|guid): title or identifier of an existing detail view

##### Returns:

    
    
    bool: True if detail is a detail view
    bool: False if detail is not a detail view
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.IsLayout(view):
        isdetail = rs.IsDetail(view, "Top")
        if isdetail:
            print("Top is a detail view.")
        else:
            print("Top is not a detail view.")

##### See Also:

  * IsLayout
  * CurrentDetail

  

IsLayout

    
    
    IsLayout(layout)

Verifies that a view is a page layout view

##### Parameters:

    
    
    layout (guid|str): title or identifier of an existing page layout view

##### Returns:

    
    
    bool: True if layout is a page layout view
    bool: False is layout is a standard, model view
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.IsLayout(view):
        print("The current view is a page layout view.")
    else:
        print("The current view is standard, model view.")

##### See Also:

  * IsLayout
  * CurrentDetail

  

IsView

    
    
    IsView(view)

Verifies that the specified view exists

##### Parameters:

    
    
    view (str|guid): title or identifier of the view

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    title = "Perspective"
    result = rs.IsView(title)
    if result:
        print("The {} view exists.".format(title))
    else:
        print("The {} view does not exist.".format(title))

##### See Also:

  * ViewNames

  

IsViewCurrent

    
    
    IsViewCurrent(view)

Verifies that the specified view is the current, or active view

##### Parameters:

    
    
    view (str|guid): title or identifier of the view

##### Returns:

    
    
    bool: True of False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    title = "Perspective"
    result = rs.IsViewCurrent(title)
    if result:
        print("The {} view is current".format(title))
    else:
        print("The {} view is not current".format(title))

##### See Also:

  * CurrentView

  

IsViewMaximized

    
    
    IsViewMaximized(view=None)

Verifies that the specified view is maximized (enlarged so as to fill the
entire Rhino window)

##### Parameters:

    
    
    view: (str|guid): title or identifier of the view. If omitted, the current
          view is used

##### Returns:

    
    
    bool: True of False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    title = rs.CurrentView()
    result = rs.IsViewMaximized(title)
    if result:
        print("The {} view is maximized".format(title))
    else:
        print("The {} view is not maximized".format(title))

##### See Also:

  * MaximizeRestoreView

  

IsViewPerspective

    
    
    IsViewPerspective(view)

Verifies that the specified view's projection is set to perspective

##### Parameters:

    
    
    view (str|guid): title or identifier of the view

##### Returns:

    
    
    bool: True of False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    title = rs.CurrentView()
    result = rs.IsViewPerspective(title)
    if result:
        print("The {} view is set to perspective projection".format(title))
    else:
        print("The {} view is set to parallel projection".format(title))

##### See Also:

  * ViewProjection

  

IsViewTitleVisible

    
    
    IsViewTitleVisible(view=None)

Verifies that the specified view's title window is visible

##### Parameters:

    
    
    view: (str|guid, optional): The title or identifier of the view. If omitted, the current
          active view is used

##### Returns:

    
    
    bool: True of False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    title = rs.CurrentView()
    vis = rs.IsViewTitleVisible(title)
    if vis:
        print("The {} view's title is visible".format(title))
    else:
        print("The {} view's title is not visible".format(title))

##### See Also:

  * ShowViewTitle

  

IsWallpaper

    
    
    IsWallpaper(view)

Verifies that the specified view contains a wallpaper image

##### Parameters:

    
    
    view (str|guid): view to verify

##### Returns:

    
    
    bool: True or False

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    filename = rs.OpenFileName()
    if filename and not rs.IsWallpaper(view):
        rs.Wallpaper(view, filename)

##### See Also:

  * Wallpaper

  

MaximizeRestoreView

    
    
    MaximizeRestoreView(view=None)

Toggles a view's maximized/restore window state of the specified view

##### Parameters:

    
    
    view: (str|guid, optional): the title or identifier of the view. If omitted, the current
          active view is used

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    title = rs.CurrentView()
    if rs.IsViewMaximized(title):
        rs.MaximizeRestoreView( title )

##### See Also:

  * IsViewMaximized

  

NamedCPlane

    
    
    NamedCPlane(name)

Returns the plane geometry of the specified named construction plane

##### Parameters:

    
    
    name (str): the name of the construction plane

##### Returns:

    
    
    plane: a plane on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    names = rs.NamedCPlanes()
    if names:
        for name in names:
            plane = rs.NamedCPlane(name)
            print("CPlane name:" + name)
            print("CPlane origin:" + plane.Origin)
            print("CPlane x-axis:" + plane.Xaxis)
            print("CPlane y-axis:" + plane.Yaxis)
            print("CPlane z-axis:" + plane.Zaxis)

##### See Also:

  * AddNamedCPlane
  * DeleteNamedCPlane
  * NamedCPlanes
  * RestoreNamedCPlane

  

NamedCPlanes

    
    
    NamedCPlanes()

Returns the names of all named construction planes in the document

##### Returns:

    
    
    list(str, ...): the names of all named construction planes in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cplanes = rs.NamedCPlanes()
    if cplanes:
        for cplane in cplanes: print(cplane)

##### See Also:

  * AddNamedCPlane
  * DeleteNamedCPlane
  * NamedCPlane
  * RestoreNamedCPlane

  

NamedViews

    
    
    NamedViews()

Returns the names of all named views in the document

##### Returns:

    
    
    list(str, ...): the names of all named views in the document

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.NamedViews()
    if views:
        for view in views: print(view)

##### See Also:

  * AddNamedView
  * DeleteNamedView
  * RestoreNamedView

  

RenameView

    
    
    RenameView(old_title, new_title)

Changes the title of the specified view

##### Parameters:

    
    
    old_title (str|guid): the title or identifier of the view to rename
    new_title (str): the new title of the view

##### Returns:

    
    
    str: the view's previous title if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    oldtitle = rs.CurrentView()
    rs.renameview( oldtitle, "Current" )

##### See Also:

  * ViewNames

  

RestoreNamedCPlane

    
    
    RestoreNamedCPlane(cplane_name, view=None)

Restores a named construction plane to the specified view.

##### Parameters:

    
    
    cplane_name (str): name of the construction plane to restore
    view: (str|guid, optional): the title or identifier of the view. If omitted, the current
          active view is used

##### Returns:

    
    
    str: name of the restored named construction plane if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    cplanes = rs.NamedCplanes()
    if cplanes: rs.RestoreNamedCPlane( cplanes[0] )

##### See Also:

  * AddNamedCPlane
  * DeleteNamedCPlane
  * NamedCPlane
  * NamedCPlanes

  

RestoreNamedView

    
    
    RestoreNamedView(named_view, view=None, restore_bitmap=False)

Restores a named view to the specified view

##### Parameters:

    
    
    named_view (str): name of the named view to restore
    view (str|guid, optional):  title or id of the view to restore the named view.
         If omitted, the current active view is used
    restore_bitmap: (bool, optional): restore the named view's background bitmap

##### Returns:

    
    
    str: name of the restored view if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.NamedViews()
    if views: rs.RestoreNamedView(views[0])

##### See Also:

  * AddNamedView
  * DeleteNamedView
  * NamedViews

  

RotateCamera

    
    
    RotateCamera(view=None, direction=0, angle=None)

Rotates a perspective-projection view's camera. See the RotateCamera command
in the Rhino help file for more details

##### Parameters:

    
    
    view (str|guid, optional):  title or id of the view. If omitted, current active view is used
    direction(number, optional): the direction to rotate the camera where
      0=right
      1=left
      2=down
      3=up
    angle: (number, optional): the angle to rotate. If omitted, the angle of rotation
          is specified by the "Increment in divisions of a circle" parameter
          specified in Options command's View tab

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.RotateCamera( angle=15 )

##### See Also:

  * RotateView
  * TiltView

  

RotateView

    
    
    RotateView(view=None, direction=0, angle=None)

Rotates a view. See RotateView command in Rhino help for more information

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    direction (number, optional): the direction to rotate the view where
          0=right
          1=left
          2=down
          3=up
    angle (number): angle to rotate. If omitted, the angle of rotation is specified
          by the "Increment in divisions of a circle" parameter specified in
          Options command's View tab

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.RotateView( angle=90.0 )

##### See Also:

  * RotateCamera
  * TiltView

  

ShowGrid

    
    
    ShowGrid(view=None, show=None)

Shows or hides a view's construction plane grid

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    show (bool, optional): The grid state to set. If omitted, the current grid display state is returned

##### Returns:

    
    
    bool: If show is not specified, then the grid display state if successful
    bool: If show is specified, then the previous grid display state if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.ShowGrid(view)==False:
        rs.ShowGrid( view, True )

##### See Also:

  * ShowGridAxes
  * ShowWorldAxes

  

ShowGridAxes

    
    
    ShowGridAxes(view=None, show=None)

Shows or hides a view's construction plane grid axes.

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    show (bool, optional): The state to set. If omitted, the current grid axes display state is returned

##### Returns:

    
    
    bool: If show is not specified, then the grid axes display state
    bool: If show is specified, then the previous grid axes display state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.ShowGridAxes(view)==False:
        rs.ShowGridAxes( view, True )

##### See Also:

  * ShowGrid
  * ShowWorldAxes

  

ShowViewTitle

    
    
    ShowViewTitle(view=None, show=True)

Shows or hides the title window of a view

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    show (bool, optional): The state to set.

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.IsViewTitleVisible(view)==False:
        rs.ShowViewTitle( view, True )

##### See Also:

  * IsViewTitleVisible

  

ShowWorldAxes

    
    
    ShowWorldAxes(view=None, show=None)

Shows or hides a view's world axis icon

##### Parameters:

    
    
    view (str|guid, optional):  title or id of the view. If omitted, the current active view is used
    show: (bool, optional): The state to set.

##### Returns:

    
    
    bool: If show is not specified, then the world axes display state
    bool: If show is specified, then the previous world axes display state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.ShowWorldAxes(view)==False:
        rs.ShowWorldAxes( view, True )

##### See Also:

  * ShowGrid
  * ShowGridAxes

  

TiltView

    
    
    TiltView(view=None, direction=0, angle=None)

Tilts a view by rotating the camera up vector. See the TiltView command in the
Rhino help file for more details.

##### Parameters:

    
    
    view (str|guid, optional):  title or id of the view. If omitted, the current active view is used
    direction (number, optional): the direction to rotate the view where
      0=right
      1=left
    angle (number, optional): the angle to rotate. If omitted, the angle of rotation is
      specified by the "Increment in divisions of a circle" parameter specified
      in Options command's View tab

##### Returns:

    
    
    bool: True or False indicating success or failure

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.TiltView( angle=15 )

##### See Also:

  * RotateCamera

  

ViewCamera

    
    
    ViewCamera(view=None, camera_location=None)

Returns or sets the camera location of the specified view

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    camera_location (point, optional): a 3D point identifying the new camera location.
      If omitted, the current camera location is returned

##### Returns:

    
    
    point: If camera_location is not specified, the current camera location
    point: If camera_location is specified, the previous camera location
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    camera = rs.GetPoint("Select new camera location")
    if camera: rs.ViewCamera(view,camera)

##### See Also:

  * ViewCameraTarget
  * ViewTarget

  

ViewCameraLens

    
    
    ViewCameraLens(view=None, length=None)

Returns or sets the 35mm camera lens length of the specified perspective
projection view.

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    length (number, optional): the new 35mm camera lens length. If omitted, the previous
      35mm camera lens length is returned

##### Returns:

    
    
    number: If lens length is not specified, the current lens length
    number: If lens length is specified, the previous lens length

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.IsViewPerspective(view):
        length = rs.ViewCameraLens(view, 100)

##### See Also:

  * ViewCameraTarget
  * ViewCPlane
  * ViewDisplayModes
  * ViewProjection
  * ViewSize

  

ViewCameraPlane

    
    
    ViewCameraPlane(view=None)

Returns the orientation of a view's camera.

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used

##### Returns:

    
    
    plane: the view's camera plane if successful
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    target = rs.ViewTarget(view)
    camplane = rs.ViewCameraPlane(view)
    plane = rs.MovePlane(camplane, target)
    rs.ViewCPlane( view, plane )

##### See Also:

  * ViewCamera
  * ViewTarget

  

ViewCameraTarget

    
    
    ViewCameraTarget(view=None, camera=None, target=None)

Returns or sets the camera and target positions of the specified view

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, current active view is used
    camera (point): 3d point identifying the new camera location. If camera and
       target are not specified, current camera and target locations are returned
    target (point): 3d point identifying the new target location. If camera and
       target are not specified, current camera and target locations are returned

##### Returns:

    
    
    list(point, point): if both camera and target are not specified, then the 3d points containing
      the current camera and target locations is returned
    point: if either camera or target are specified, then the 3d points containing the
      previous camera and target locations is returned

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    camera = rs.GetPoint("Select new camera location")
    target = rs.GetPoint("Select new target location")
    if camera and target:
        rs.ViewCameraTarget( view, camera, target )

##### See Also:

  * ViewCamera
  * ViewTarget

  

ViewCameraUp

    
    
    ViewCameraUp(view=None, up_vector=None)

Returns or sets the camera up direction of a specified

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, the current active view is used
    up_vector (vector): 3D vector identifying the new camera up direction

##### Returns:

    
    
    vector: if up_vector is not specified, then the current camera up direction
    vector: if up_vector is specified, then the previous camera up direction

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    upVector = rs.ViewCameraUp(view)
    print(up_vector)

##### See Also:

  * ViewCamera
  * ViewTarget

  

ViewCPlane

    
    
    ViewCPlane(view=None, plane=None)

Return or set a view's construction plane

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, current active view is used.
    plane (plane): the new construction plane if setting

##### Returns:

    
    
    plane: If a construction plane is not specified, the current construction plane
    plane: If a construction plane is specified, the previous construction plane

##### Example:

    
    
    import rhinoscriptsyntax as rs
    origin = rs.GetPoint("CPlane origin")
    if origin:
        plane = rs.ViewCPlane()
        plane = rs.MovePlane(plane,origin)
        rs.ViewCPlane(None, plane)

##### See Also:

  * ViewCameraLens
  * ViewCameraTarget
  * ViewDisplayModes
  * ViewProjection
  * ViewSize

  

ViewDisplayMode

    
    
    ViewDisplayMode(view=None, mode=None, return_name=True)

Return or set a view display mode

##### Parameters:

    
    
    view (str|guid, optional): Title or id of a view. If omitted, active view is used
    mode (str|guid, optional): Name or id of a display mode
    return_name (bool, optional): If true, return display mode name. If False, display mode id

##### Returns:

    
    
    str: If mode is specified, the previous mode
    str: If mode is not specified, the current mode

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.ViewNames()
    for view in views:
        rs.ViewDisplayMode(view, 'Ghosted')

##### See Also:

  * CurrentView
  * ViewNames

  

ViewDisplayModeId

    
    
    ViewDisplayModeId(name)

Return id of a display mode given it's name

##### Parameters:

    
    
    name (str): name of the display mode

##### Returns:

    
    
    guid: The id of the display mode if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    modes = rs.ViewDisplayModes(True)
    for mode in modes: print("{} = {}".format(mode, rs.ViewDisplayModeId(mode)))

##### See Also:

  * ViewDisplayMode
  * ViewDisplayModes

  

ViewDisplayModeName

    
    
    ViewDisplayModeName(mode_id)

Return name of a display mode given it's id

##### Parameters:

    
    
    mode_id (guid): The identifier of the display mode obtained from the ViewDisplayModes method.

##### Returns:

    
    
    str: The name of the display mode if successful, otherwise None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    modes = rs.ViewDisplayModes(False)
    for mode in modes: print("{} = {}".format(mode, rs.ViewDisplayModeName(mode)))

##### See Also:

  * ViewDisplayMode
  * ViewDisplayModes

  

ViewDisplayModes

    
    
    ViewDisplayModes(return_names=True)

Return list of display modes

##### Parameters:

    
    
    return_name (bool, otpional): If True, return mode names. If False, return ids

##### Returns:

    
    
    list(str|guid, ...): strings identifying the display mode names or identifiers if successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    modes = rs.ViewDisplayModes(False)
    for mode in modes: print("{} = {}".format(mode, rs.ViewDisplayModeName(mode)))

##### See Also:

  * ViewDisplayMode
  * ViewDisplayModeName

  

ViewNames

    
    
    ViewNames(return_names=True, view_type=0)

Return the names, titles, or identifiers of all views in the document

##### Parameters:

    
    
    return_names (bool, optional): if True then the names of the views are returned.
      If False, then the identifiers of the views are returned
    view_type: (number, optional): the type of view to return
                     0 = standard model views
                     1 = page layout views
                     2 = both standard and page layout views

##### Returns:

    
    
    list(str|guid, ...): of the view names or identifiers on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    # Print view names
    views = rs.ViewNames()
    if views:
        for view in views: print(view)
    # Print view identifiers
    view_ids = rs.ViewNames(False)
    if view_ids:
        for id in view_ids:
            print("{} = {}".format(id, rs.ViewTitle(id)))

##### See Also:

  * IsView
  * ViewTitle

  

ViewNearCorners

    
    
    ViewNearCorners(view=None)

Return 3d corners of a view's near clipping plane rectangle. Useful in
determining the "real world" size of a parallel-projected view

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, current active view is used

##### Returns:

    
    
    list(point, point, point, point): Four Point3d that define the corners of the rectangle (counter-clockwise order)

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rect = rs.ViewNearCorners()
    if rect:
        for i in range(4): rs.AddTextDot( i, rect[i] )

##### See Also:

  * CurrentView

  

ViewProjection

    
    
    ViewProjection(view=None, mode=None)

Return or set a view's projection mode.

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, current active view is used
    mode (number, optional): the projection mode
      1 = parallel
      2 = perspective
      3 = two point perspective

##### Returns:

    
    
    number: if mode is not specified, the current projection mode for the specified view
    number: if mode is specified, the previous projection mode for the specified view

##### Example:

    
    
    import rhinoscriptsyntax as rs
    views = rs.ViewNames()
    if views:
        for view in views: rs.ViewProjection(view,1)

##### See Also:

  * IsViewPerspective

  

ViewRadius

    
    
    ViewRadius(view=None, radius=None, mode=False)

Returns or sets the radius of a parallel-projected view. Useful when you need
an absolute zoom factor for a parallel-projected view

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, current active view is used
    radius (number): the view radius
    mode (bool, optional): perform a "dolly" magnification by moving the camera
      towards/away from the target so that the amount of the screen 
      subtended by an object changes.  true = perform a "zoom" 
      magnification by adjusting the "lens" angle

##### Returns:

    
    
    number: if radius is not specified, the current view radius for the specified view
    number: if radius is specified, the previous view radius for the specified view

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rhParallelView = 1
    views = rs.ViewNames()
    if views:
        for view in views:
            if rs.ViewProjection(view)==rhParallelView:
                rs.ViewRadius(view, 10.0)

##### See Also:

  * IsViewPerspective
  * ViewProjection

  

ViewSize

    
    
    ViewSize(view=None)

Returns the width and height in pixels of the specified view

##### Parameters:

    
    
    view (str|guid): title or id of the view. If omitted, current active view is used

##### Returns:

    
    
    tuple(number, number): of two numbers identifying width and height

##### Example:

    
    
    import rhinoscriptsyntax as rs
    size = rs.ViewSize()
    if size:
        print("Width: {} pixels".format(size[0]))
        print("Height: {} pixels".format(size[1]))

##### See Also:

  * ViewCameraLens
  * ViewCameraTarget
  * ViewCPlane
  * ViewDisplayModes
  * ViewProjection

  

ViewSpeedTest

    
    
    ViewSpeedTest(view=None, frames=100, freeze=True, direction=0, angle_degrees=5)

Test's Rhino's display performance

##### Parameters:

    
    
    view (str|guid, optional): The title or identifier of the view.  If omitted, the current active view is used
    frames (number, optional): The number of frames, or times to regenerate the view. If omitted, the view will be regenerated 100 times.
    freeze (bool, optional): If True (Default), then Rhino's display list will not be updated with every frame redraw. If False, then Rhino's display list will be updated with every frame redraw.
    direction (number, optional): The direction to rotate the view. The default direction is Right (0). Modes:
      0 = Right
      1 = Left
      2 = Down
      3 = Up.
    angle_degrees (number, optional): The angle to rotate. If omitted, the rotation angle of 5.0 degrees will be used.

##### Returns:

    
    
    number: The number of seconds it took to regenerate the view frames number of times, if successful
    None: if not successful

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = "Perspective"
    seconds = rs.ViewSpeedTest(view, 100)
    if seconds:
        print("Time to regen viewport 100 times = {} secords".format(seconds))

  

ViewTarget

    
    
    ViewTarget(view=None, target=None)

Returns or sets the target location of the specified view

##### Parameters:

    
    
    view (str|guid, optional): title or id of the view. If omitted, current active view is used
    target (point, optional): 3d point identifying the new target location. If omitted,
      the current target location is returned

##### Returns:

    
    
    point: is target is not specified, then the current target location
    point: is target is specified, then the previous target location
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    target = rs.GetPoint("Select new target location")
    if target: rs.ViewTarget( view, target )

##### See Also:

  * ViewCamera
  * ViewCameraTarget

  

ViewTitle

    
    
    ViewTitle(view_id)

Returns the name, or title, of a given view's identifier

##### Parameters:

    
    
    view_id (str|guid): The identifier of the view

##### Returns:

    
    
    str: name or title of the view on success
    None: on error

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view_ids = rs.ViewNames(False)
    for id in view_ids:
        print(id + " = " + rs.ViewTitle(id))

##### See Also:

  * CurrentView
  * ViewNames

  

Wallpaper

    
    
    Wallpaper(view=None, filename=None)

Returns or sets the wallpaper bitmap of the specified view. To remove a
wallpaper bitmap, pass an empty string ""

##### Parameters:

    
    
    view (str|guid, optional): The identifier of the view. If omitted, the
      active view is used
    filename (str): Name of the bitmap file to set as wallpaper

##### Returns:

    
    
    str: If filename is not specified, the current wallpaper bitmap filename
    str: If filename is specified, the previous wallpaper bitmap filename

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    filename = rs.OpenFileName()
    if filename and not rs.IsWallpaper(view):
        rs.Wallpaper(view, filename)

##### See Also:

  * IsWallpaper
  * WallpaperGrayScale
  * WallpaperHidden

  

WallpaperGrayScale

    
    
    WallpaperGrayScale(view=None, grayscale=None)

Returns or sets the grayscale display option of the wallpaper bitmap in a
specified view

##### Parameters:

    
    
    view (str|guid, optional):  The identifier of the view. If omitted, the
      active view is used
    grayscale (bool, optional): Display the wallpaper in gray(True) or color (False)

##### Returns:

    
    
    bool: If grayscale is not specified, the current grayscale display option
    bool: If grayscale is specified, the previous grayscale display option

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.WallpaperGrayScale(view)==False: rs.WallpaperGrayScale(view, True)

##### See Also:

  * Wallpaper
  * WallpaperHidden

  

WallpaperHidden

    
    
    WallpaperHidden(view=None, hidden=None)

Returns or sets the visibility of the wallpaper bitmap in a specified view

##### Parameters:

    
    
    view (str|guid, optional): The identifier of the view. If omitted, the
      active view is used
    hidden (bool, optional): Show or hide the wallpaper

##### Returns:

    
    
    bool: If hidden is not specified, the current hidden state
    bool: If hidden is specified, the previous hidden state

##### Example:

    
    
    import rhinoscriptsyntax as rs
    view = rs.CurrentView()
    if rs.WallpaperHidden(view) == False: rs.WallpaperHidden(view, True)

##### See Also:

  * Wallpaper
  * WallpaperGrayScale

  

ZoomBoundingBox

    
    
    ZoomBoundingBox(bounding_box, view=None, all=False)

Zooms to the extents of a specified bounding box in the specified view

##### Parameters:

    
    
    bounding_box ([point, point, point ,point, point, point, point, point]): eight points that define the corners
      of a bounding box or a BoundingBox class instance
    view  (str|guid, optional): title or id of the view. If omitted, current active view is used
    all (bool, optional): zoom extents in all views

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    obj = rs.GetObject()
    if obj:
        bbox = rs.BoundingBox(obj)
        rs.ZoomBoundingBox( bbox )

##### See Also:

  * ZoomExtents
  * ZoomSelected

  

ZoomExtents

    
    
    ZoomExtents(view=None, all=False)

Zooms to extents of visible objects in the specified view

##### Parameters:

    
    
    view  (str|guid, optional): title or id of the view. If omitted, current active view is used
    all (bool, optional): zoom extents in all views

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinoscriptsyntax as rs
    rs.ZoomExtents()

##### See Also:

  * ZoomBoundingBox
  * ZoomSelected

  

ZoomSelected

    
    
    ZoomSelected(view=None, all=False)

Zoom to extents of selected objects in a view

##### Parameters:

    
    
    view  (str|guid, optional): title or id of the view. If omitted, active view is used
    all (bool, optional): zoom extents in all views

##### Returns:

    
    
    None

##### Example:

    
    
    import rhinocriptsyntax as rs
    obj = rs.GetObject("Select object", select=True)
    if obj: rs.ZoomSelected()

##### See Also:

  * ZoomBoundingBox
  * ZoomExtents

  

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/api/RhinoScriptSyntax/index.md)
[
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/api/RhinoScriptSyntax/index.md)
[ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2024 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/channel/UCFk2HeZDZprti9Sm5LWeMPA)
[](https://vimeo.com/rhino) [![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

