---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ComponentServer.htm
scraped_at: 2025-09-08T16:15:51.140023
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm
"GH_ComponentServer Class")

[GH_ComponentServer Constructor
](../html/M_Grasshopper_Kernel_GH_ComponentServer__ctor.htm
"GH_ComponentServer Constructor ")

[GH_ComponentServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ComponentServer.htm
"GH_ComponentServer Properties")

[GH_ComponentServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm
"GH_ComponentServer Methods")

[GH_ComponentServer
Events](../html/Events_T_Grasshopper_Kernel_GH_ComponentServer.htm
"GH_ComponentServer Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ComponentServer Class  
  
---  
  
Maintains proxies for all components, parameters and other object types as
defined in all grasshopper assemblies.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_ComponentServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_ComponentServer
    
    
    Public NotInheritable Class GH_ComponentServer

The GH_ComponentServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ComponentServer](M_Grasshopper_Kernel_GH_ComponentServer__ctor.htm)|
Initializes a new instance of the GH_ComponentServer class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Aliases](P_Grasshopper_Kernel_GH_ComponentServer_Aliases.htm)|  Gets a list
of all the defined aliases.  
![Public property](../icons/pubproperty.gif)|
[CompleteRibbonLayout](P_Grasshopper_Kernel_GH_ComponentServer_CompleteRibbonLayout.htm)|
Gets the default component layout featuring all non-hidden components and
parameters.  
![Public property](../icons/pubproperty.gif)|
[DiscardedProxies](P_Grasshopper_Kernel_GH_ComponentServer_DiscardedProxies.htm)|
Returns the total number of IGH_DocumentObjects that were discarded during
assembly parsing. This includes both skipped and replaced proxies.  
![Public property](../icons/pubproperty.gif)|
[GraphProxies](P_Grasshopper_Kernel_GH_ComponentServer_GraphProxies.htm)|
Returns a list of all cached GH_GraphProxy instances.  
![Public property](../icons/pubproperty.gif)|
[Libraries](P_Grasshopper_Kernel_GH_ComponentServer_Libraries.htm)|  Returns a
list of Assembly Info objects describing all loaded assemblies.  
![Public property](../icons/pubproperty.gif)|
[LoadingExceptions](P_Grasshopper_Kernel_GH_ComponentServer_LoadingExceptions.htm)|
Gets a list of all the exceptions that were recorded during the most recent
loading sequence.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[NoLoadExtension](P_Grasshopper_Kernel_GH_ComponentServer_NoLoadExtension.htm)|  
![Public property](../icons/pubproperty.gif)|
[ObjectProxies](P_Grasshopper_Kernel_GH_ComponentServer_ObjectProxies.htm)|
Returns a list of all cached GH_ObjectProxy instances.  
![Public property](../icons/pubproperty.gif)|
[ObjectProxyNames](P_Grasshopper_Kernel_GH_ComponentServer_ObjectProxyNames.htm)|
Returns a specialized string collection of all component names.  
![Public property](../icons/pubproperty.gif)|
[TypeHints](P_Grasshopper_Kernel_GH_ComponentServer_TypeHints.htm)|  Gets a
list of all IGH_TypeHint types in all loaded assemblies.  
![Public property](../icons/pubproperty.gif)|
[Upgraders](P_Grasshopper_Kernel_GH_ComponentServer_Upgraders.htm)|  Gets a
list of all the upgraders that have been cached.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddAlias](M_Grasshopper_Kernel_GH_ComponentServer_AddAlias.htm)|  Add an
alias to a target.  
![Public method](../icons/pubmethod.gif)|
[AddCategoryIcon](M_Grasshopper_Kernel_GH_ComponentServer_AddCategoryIcon.htm)|
Add an icon for a tab category. 16x16 images are required.  
![Public method](../icons/pubmethod.gif)|
[AddCategoryShortName](M_Grasshopper_Kernel_GH_ComponentServer_AddCategoryShortName.htm)|
Add an abbreviation for a tab category. 2~4 letter abbreviations are best.  
![Public method](../icons/pubmethod.gif)|
[AddCategorySymbolName](M_Grasshopper_Kernel_GH_ComponentServer_AddCategorySymbolName.htm)|
Add a single char category description.  
![Public method](../icons/pubmethod.gif)|
[AliasTargets](M_Grasshopper_Kernel_GH_ComponentServer_AliasTargets.htm)|  Get
all the target Component IDs for a given alias.  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_Kernel_GH_ComponentServer_Clear.htm)|  Clear all caches.  
![Public method](../icons/pubmethod.gif)|
[ClearStaleUserObjects](M_Grasshopper_Kernel_GH_ComponentServer_ClearStaleUserObjects.htm)|
Remove all user objects that no longer point to existing files.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CompareProxies](M_Grasshopper_Kernel_GH_ComponentServer_CompareProxies.htm)|
Compare two object proxies. Names and exposures are taken into account.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CopyFileToAppropriateFolder](M_Grasshopper_Kernel_GH_ComponentServer_CopyFileToAppropriateFolder.htm)|
Copy a GHA or GHUSER file into the appropriate Roaming Application Data
folder. Of the file is already in the top-level roaming folder it will not be
copied.  
![Public method](../icons/pubmethod.gif)|
[CreateComponentPalette](M_Grasshopper_Kernel_GH_ComponentServer_CreateComponentPalette.htm)|  
![Public method](../icons/pubmethod.gif)|
[DestroyLoadingUI](M_Grasshopper_Kernel_GH_ComponentServer_DestroyLoadingUI.htm)|
Destroy the loading UI (the banner and the progress bar).  
![Public method](../icons/pubmethod.gif)|
[EmitGraph](M_Grasshopper_Kernel_GH_ComponentServer_EmitGraph.htm)|  Create a
new instance of the IGH_Graph that matches the id. If no proxy can be matched
to the id, a null reference will be returned.  
![Public method](../icons/pubmethod.gif)|
[EmitObject](M_Grasshopper_Kernel_GH_ComponentServer_EmitObject.htm)|  Create
a new instance of the IGH_DocumentObject that matches the id. If no proxy can
be matched to the id, a null reference will be returned.  
![Public method](../icons/pubmethod.gif)|
[EmitObjectIcon](M_Grasshopper_Kernel_GH_ComponentServer_EmitObjectIcon.htm)|
Get the icon that is associated with the given Object ID.  
![Public method](../icons/pubmethod.gif)|
[EmitObjectProxy](M_Grasshopper_Kernel_GH_ComponentServer_EmitObjectProxy.htm)|
Get the proxy that is associated with the given Object ID.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ExternalFiles](M_Grasshopper_Kernel_GH_ComponentServer_ExternalFiles.htm)|
Get lists of all the external files (GHA, GHUSER and GHCLUSTER) that will be
loaded by Grasshopper. Note: this does not equal the files that may already
have been loaded, just the files that we'll attempt to load if we were asked
to load all plugins now. The list contains no duplicate file paths, but it may
contain identical files which won't be filtered until actual loading.  
![Public method](../icons/pubmethod.gif)|
[FindAssembly](M_Grasshopper_Kernel_GH_ComponentServer_FindAssembly.htm)|
Gets the assembly that corresponds to the given library ID.  
![Public method](../icons/pubmethod.gif)|
[FindAssemblyByObject(Guid)](M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject_1.htm)|
Gets the assembly that corresponds to the given library ID.  
![Public method](../icons/pubmethod.gif)|
[FindAssemblyByObject(IGH_DocumentObject)](M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject.htm)|
Gets the assembly that corresponds to the given library ID.  
![Public method](../icons/pubmethod.gif)|
[FindObjectByName](M_Grasshopper_Kernel_GH_ComponentServer_FindObjectByName.htm)|
Find an object by name. Obsolete and hidden objects are ignored. Only exact
matches are included.  
![Public method](../icons/pubmethod.gif)|
[FindObjects(Guid)](M_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm)|
Find all the objects that are part of a certain library.  
![Public method](../icons/pubmethod.gif)| [FindObjects(String, Int32,
IGH_ObjectProxy,
Double)](M_Grasshopper_Kernel_GH_ComponentServer_FindObjects_1.htm)|  Searches
the list of cached object proxies for objects that might be implied by a
search term.  
![Public method](../icons/pubmethod.gif)|
[FindUpgrader](M_Grasshopper_Kernel_GH_ComponentServer_FindUpgrader.htm)|
Find the upgrader that can convert from the given target.  
![Public method](../icons/pubmethod.gif)|
[GetAlias](M_Grasshopper_Kernel_GH_ComponentServer_GetAlias.htm)|  Gets the
alias display string for a given object.  
![Public method](../icons/pubmethod.gif)|
[GetCategoryIcon](M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryIcon.htm)|
Get the icon for a specific category. If the icon hasn't been defined, this
method will return the default icon.  
![Public method](../icons/pubmethod.gif)|
[GetCategoryShortName](M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryShortName.htm)|
Get the abbreviation (short name) for a specific category. If the short name
hasn't been defined, this method will return the full name instead.  
![Public method](../icons/pubmethod.gif)|
[GetCategorySymbolName](M_Grasshopper_Kernel_GH_ComponentServer_GetCategorySymbolName.htm)|
Get the single char representation for a specific category. If the char hasn't
been defined, this method will return the first char of the full name instead.  
![Public method](../icons/pubmethod.gif)|
[IsGraphCached](M_Grasshopper_Kernel_GH_ComponentServer_IsGraphCached.htm)|
Tests the graph cache for an existing graph type ID.  
![Public method](../icons/pubmethod.gif)|
[IsObjectCached](M_Grasshopper_Kernel_GH_ComponentServer_IsObjectCached.htm)|
Tests the caches for an existing object type ID.  
![Public method](../icons/pubmethod.gif)|
[IsUpgrader](M_Grasshopper_Kernel_GH_ComponentServer_IsUpgrader.htm)|  Checks
to see if at least one upgrader is defined for a collection of objects.  
![Public method](../icons/pubmethod.gif)|
[LoadAliases](M_Grasshopper_Kernel_GH_ComponentServer_LoadAliases.htm)|  Load
the Alias table from the settings directory. Only use this function if you
suspect the alias table settings file has changed due to some external
process.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewUserObject](M_Grasshopper_Kernel_GH_ComponentServer_NewUserObject.htm)|
Create a new UserObject and write it to the Grasshopper User Object folder.  
![Public method](../icons/pubmethod.gif)|
[RemoveCachedGraph](M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedGraph.htm)|
Remove a cache entry from the graph cache. This cannot be undone.  
![Public method](../icons/pubmethod.gif)|
[RemoveCachedObject(Guid)](M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm)|
Remove a cache entry from the object cache. This cannot be undone.  
![Public method](../icons/pubmethod.gif)|
[RemoveCachedObject(String)](M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject_1.htm)|
Remove the user object (if any) that loads itself from a specified *.ghuser
file.  
![Public method](../icons/pubmethod.gif)|
[SaveAliases](M_Grasshopper_Kernel_GH_ComponentServer_SaveAliases.htm)|  Save
the alias table to the settings directory. Use this function if you change the
alias table while ignoring usual channels.  
![Public method](../icons/pubmethod.gif)|
[SetAlias](M_Grasshopper_Kernel_GH_ComponentServer_SetAlias.htm)|  Sets the
aliases for a given target.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[UpdateRibbonUI](M_Grasshopper_Kernel_GH_ComponentServer_UpdateRibbonUI.htm)|
Forces an update of the Ribbon control on the Grasshopper main form.  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)|
[GHAFileLoaded](E_Grasshopper_Kernel_GH_ComponentServer_GHAFileLoaded.htm)|
Raised whenever a GHA file has been successfully loaded.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

