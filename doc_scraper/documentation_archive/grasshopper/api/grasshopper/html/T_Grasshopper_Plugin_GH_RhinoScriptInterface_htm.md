---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Plugin_GH_RhinoScriptInterface.htm
scraped_at: 2025-09-08T16:22:28.843848
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Plugin](../html/N_Grasshopper_Plugin.htm "Grasshopper.Plugin")

[GH_RhinoScriptInterface
Class](../html/T_Grasshopper_Plugin_GH_RhinoScriptInterface.htm
"GH_RhinoScriptInterface Class")

[GH_RhinoScriptInterface Constructor
](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface__ctor.htm
"GH_RhinoScriptInterface Constructor ")

[GH_RhinoScriptInterface
Methods](../html/Methods_T_Grasshopper_Plugin_GH_RhinoScriptInterface.htm
"GH_RhinoScriptInterface Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RhinoScriptInterface Class  
  
---  
  
Plugin Interface object that is exposed via the RhinoScript layer.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.PluginGH_RhinoScriptInterface  

**Namespace:** [Grasshopper.Plugin](N_Grasshopper_Plugin.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RhinoScriptInterface
    
    
    Public Class GH_RhinoScriptInterface

The GH_RhinoScriptInterface type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_RhinoScriptInterface](M_Grasshopper_Plugin_GH_RhinoScriptInterface__ctor.htm)|
Initializes a new instance of the GH_RhinoScriptInterface class  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AssignDataToParameter](M_Grasshopper_Plugin_GH_RhinoScriptInterface_AssignDataToParameter.htm)|
Find a parameter and assign some persistent data.  
![Public method](../icons/pubmethod.gif)|
[BakeDataInObject](M_Grasshopper_Plugin_GH_RhinoScriptInterface_BakeDataInObject.htm)|
Find an object and bake all geometry inside of it.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[CloseAllDocuments](M_Grasshopper_Plugin_GH_RhinoScriptInterface_CloseAllDocuments.htm)|
Close all Grasshopper documents.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[CloseDocument](M_Grasshopper_Plugin_GH_RhinoScriptInterface_CloseDocument.htm)|
Close the currently active Grasshopper document. If there is not active
document, nothing will happen.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[DisableBanner](M_Grasshopper_Plugin_GH_RhinoScriptInterface_DisableBanner.htm)|
Disables the display of the Grasshopper banner during Component loading. The
banner is typically only shown once during a Grasshopper session, namely when
the Editor is first loaded.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[DisableSolver](M_Grasshopper_Plugin_GH_RhinoScriptInterface_DisableSolver.htm)|
Disables the Grasshopper Solver. If the Solver is disabled, expired components
and parameter will not be recomputed, though any existing solution will remain
intact.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[EnableBanner](M_Grasshopper_Plugin_GH_RhinoScriptInterface_EnableBanner.htm)|
Enables the display of the Grasshopper banner during Component loading. The
banner is typically only shown once during a Grasshopper session, namely when
the Editor is first loaded.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[EnableSolver](M_Grasshopper_Plugin_GH_RhinoScriptInterface_EnableSolver.htm)|
Enables the Grasshopper Solver. If the Solver is enabled, expired components
and parameter will be recomputed.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[HideEditor](M_Grasshopper_Plugin_GH_RhinoScriptInterface_HideEditor.htm)|
Hide the main Grasshopper Editor. If the editor hasn't been loaded or if the
Editor is already hidden, nothing will happen.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[IsEditorLoaded](M_Grasshopper_Plugin_GH_RhinoScriptInterface_IsEditorLoaded.htm)|
Returns the loaded state of the Grasshopper Main window.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[IsEditorVisible](M_Grasshopper_Plugin_GH_RhinoScriptInterface_IsEditorVisible.htm)|
Returns the visible state of the Grasshopper Main window.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[IsSolverEnabled](M_Grasshopper_Plugin_GH_RhinoScriptInterface_IsSolverEnabled.htm)|
Returns the state of the Grasshopper Solver.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[LoadEditor](M_Grasshopper_Plugin_GH_RhinoScriptInterface_LoadEditor.htm)|
Load the main Grasshopper Editor. If the editor has already been loaded
nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[LoadedPluginGuids](M_Grasshopper_Plugin_GH_RhinoScriptInterface_LoadedPluginGuids.htm)|
Gets an array of the IDs of all loaded plugins.  
![Public method](../icons/pubmethod.gif)|
[LoadedPluginNames](M_Grasshopper_Plugin_GH_RhinoScriptInterface_LoadedPluginNames.htm)|
Gets an array of the names and versions (if known) of all loaded plugins.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[OpenDocument](M_Grasshopper_Plugin_GH_RhinoScriptInterface_OpenDocument.htm)|
Open a Grasshopper document. The editor will be loaded if necessary, but it
will not be automatically shown.  
![Public method](../icons/pubmethod.gif)|
[RunAsCommand](M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunAsCommand.htm)|
**Obsolete.**  
![Public method](../icons/pubmethod.gif)|
[RunHeadless](M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunHeadless.htm)|  
![Public method](../icons/pubmethod.gif)|
[RunInCommandContext](M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunInCommandContext.htm)|  
![Public method](../icons/pubmethod.gif)|
[RunSolver](M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunSolver.htm)|  Runs
the solver once, even if the global solver lock is on.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[SaveDocument](M_Grasshopper_Plugin_GH_RhinoScriptInterface_SaveDocument.htm)|
Save the currently active Grasshopper document. If the active document has
never been saved, a Save... dialog will be shown. If there is no active
document, nothing will happen.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[SaveDocumentAs](M_Grasshopper_Plugin_GH_RhinoScriptInterface_SaveDocumentAs.htm)|
Save the currently active Grasshopper document in a specific location. If
there is no active document, nothing will happen.  
![Public method](../icons/pubmethod.gif)|
[SetSliderRangeAndValue](M_Grasshopper_Plugin_GH_RhinoScriptInterface_SetSliderRangeAndValue.htm)|
Find a slider and assign a new value.  
![Public method](../icons/pubmethod.gif)|
[SetSliderValue](M_Grasshopper_Plugin_GH_RhinoScriptInterface_SetSliderValue.htm)|
Find a slider and assign a new value.  
![Public method](../icons/pubmethod.gif)![Code
example](../icons/CodeExample.png)|
[ShowEditor](M_Grasshopper_Plugin_GH_RhinoScriptInterface_ShowEditor.htm)|
Show the main Grasshopper Editor. The editor will be loaded first if needed.
If the Editor is already on screen, nothing will happen.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Plugin Namespace](N_Grasshopper_Plugin.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

