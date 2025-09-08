---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_VersionNumber_Branch.htm
scraped_at: 2025-09-08T16:10:35.815163
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO](../html/N_GH_IO.htm "GH_IO")

[GH_ISerializable Interface](../html/T_GH_IO_GH_ISerializable.htm
"GH_ISerializable Interface")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber
Structure")

[VersionNumber.Branch Enumeration](../html/T_GH_IO_VersionNumber_Branch.htm
"VersionNumber.Branch Enumeration")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# VersionNumberBranch Enumeration  
  
---  
  
Build branch, set by the build process.

**Namespace:** [GH_IO](N_GH_IO.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public enum Branch
    
    
    Public Enumeration Branch

![](../icons/SectionExpanded.png)Members

| Member name| Value| Description  
---|---|---|---  
| Unset| 0|  Uninitialized value.  
| Developer| 1|  Private developer build; should never be released to the
public.  
| Trunk| 2|  Mainline trunk build. May be released to the public.  
| ReleaseCandidate| 3|  Release candidate build. Will be released to the
public.  
| Release| 4|  Final Release build. Will be released to the public.  
  
![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

