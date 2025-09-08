---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_FileWatcher.htm
scraped_at: 2025-09-08T16:16:44.360502
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_FileWatcher Class](../html/T_Grasshopper_Kernel_GH_FileWatcher.htm
"GH_FileWatcher Class")

[GH_FileWatcher
Properties](../html/Properties_T_Grasshopper_Kernel_GH_FileWatcher.htm
"GH_FileWatcher Properties")

[GH_FileWatcher
Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileWatcher.htm
"GH_FileWatcher Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_FileWatcher Class  
  
---  
  
Provides easy mechanisms to monitor changes to the local File System.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_FileWatcher  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_FileWatcher : IDisposable
    
    
    Public Class GH_FileWatcher
    	Implements IDisposable

The GH_FileWatcher type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Active](P_Grasshopper_Kernel_GH_FileWatcher_Active.htm)|  Gets or sets the
active flag on this watcher.  
![Public property](../icons/pubproperty.gif)|
[Buffer](P_Grasshopper_Kernel_GH_FileWatcher_Buffer.htm)|  Gets or sets the
time during which events are buffered. If multiple events for the same file
occur within the buffered timespan, they will be merged into one event.  
![Public property](../icons/pubproperty.gif)|
[InvokeOnDefaultThread](P_Grasshopper_Kernel_GH_FileWatcher_InvokeOnDefaultThread.htm)|
Gets or sets invoke behaviour for events. If true, then the event delegate is
called via the Grasshopper main UI thread. This is almost always what you
need.  
![Public property](../icons/pubproperty.gif)|
[IsDisposed](P_Grasshopper_Kernel_GH_FileWatcher_IsDisposed.htm)|  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Kernel_GH_FileWatcher_Path.htm)|  Gets the file or folder
path currently being watched.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateDirectoryWatcher(String, String, GH_FileWatcherEvents,
GH_FileWatcherFileChanged)](M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher.htm)|
Create a new FileSystem Watcher object aimed at a specific file.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateDirectoryWatcher(String, String, GH_FileWatcherEvents,
GH_FileWatcherFileChangedSimple)](M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher_1.htm)|
Create a new FileSystem Watcher object aimed at a specific file.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateFileWatcher(String, GH_FileWatcherEvents,
GH_FileWatcherFileChanged)](M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher.htm)|
Create a new FileSystem Watcher object aimed at a specific file.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateFileWatcher(String, GH_FileWatcherEvents,
GH_FileWatcherFileChangedSimple)](M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher_1.htm)|
Create a new FileSystem Watcher object aimed at a specific file.  
![Public method](../icons/pubmethod.gif)|
[Dispose](M_Grasshopper_Kernel_GH_FileWatcher_Dispose.htm)| Releases all
resources used by the GH_FileWatcher  
![Protected method](../icons/protmethod.gif)|
[Dispose(Boolean)](M_Grasshopper_Kernel_GH_FileWatcher_Dispose_1.htm)|
Releases the unmanaged resources used by the GH_FileWatcher and optionally
releases the managed resources  
![Public method](../icons/pubmethod.gif)|
[SetCustomUIThread(Control)](M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread.htm)|
If you want to override the default Invoke behaviour, you must set
InvokeOnDefaultThread to False and supply either a custom Control or a Form.  
![Public method](../icons/pubmethod.gif)|
[SetCustomUIThread(Form)](M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread_1.htm)|
If you want to override the default Invoke behaviour, you must set
InvokeOnDefaultThread to False and supply either a custom Control or a Form.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

