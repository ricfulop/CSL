---
url: https://developer.rhino3d.com/api/grasshopper/html/T_GH_IO_Types_GH_Version.htm
scraped_at: 2025-09-08T16:11:01.915086
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[GH_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH_Version Structure](../html/T_GH_IO_Types_GH_Version.htm "GH_Version
Structure")

[GH_Version Constructor ](../html/Overload_GH_IO_Types_GH_Version__ctor.htm
"GH_Version Constructor ")

[GH_Version Methods](../html/Methods_T_GH_IO_Types_GH_Version.htm "GH_Version
Methods")

[GH_Version Operators](../html/Operators_T_GH_IO_Types_GH_Version.htm
"GH_Version Operators")

[GH_Version Fields](../html/Fields_T_GH_IO_Types_GH_Version.htm "GH_Version
Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Version Structure  
  
---  
  
Basic version type. Contains Major, Minor and Revision fields.

**Namespace:** [GH_IO.Types](N_GH_IO_Types.htm)  
**Assembly:** GH_IO (in GH_IO.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public struct GH_Version
    
    
    Public Structure GH_Version

The GH_Version type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Version(GH_Version)](M_GH_IO_Types_GH_Version__ctor.htm)|  Copy
constructor. Duplicate an existing version structure.  
![Public method](../icons/pubmethod.gif)| [GH_Version(Int32, Int32,
Int32)](M_GH_IO_Types_GH_Version__ctor_1.htm)|  Default constructor. Create a
new version from specified fields.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Equals](M_GH_IO_Types_GH_Version_Equals.htm)|  Performs value equality
comparison.  (Overrides
[ValueTypeEquals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_GH_IO_Types_GH_Version_GetHashCode.htm)|  Returns the hash
code for this instance.  (Overrides
[ValueTypeGetHashCode](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_GH_IO_Types_GH_Version_ToString.htm)|  Default formatter for
Version data: M.m.RRRR Revision section is padded with zeroes until it is at
least 4 digits long.  (Overrides
[ValueTypeToString](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Equality](M_GH_IO_Types_GH_Version_op_Equality.htm)|  Compares two version
structures for equality.  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[GreaterThan](M_GH_IO_Types_GH_Version_op_GreaterThan.htm)|  Compares versions
for larger than relationships.  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[GreaterThanOrEqual](M_GH_IO_Types_GH_Version_op_GreaterThanOrEqual.htm)|
Compares versions for larger than or equal to relationships.  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[Inequality](M_GH_IO_Types_GH_Version_op_Inequality.htm)|  Compares two
version structures for inequality.  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[LessThan](M_GH_IO_Types_GH_Version_op_LessThan.htm)|  Compares versions for
smaller than relationships.  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)|
[LessThanOrEqual](M_GH_IO_Types_GH_Version_op_LessThanOrEqual.htm)|  Compares
versions for smaller than or equal to relationships.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)|
[major](F_GH_IO_Types_GH_Version_major.htm)|  Major component of version
structure.  
![Public field](../icons/pubfield.gif)|
[minor](F_GH_IO_Types_GH_Version_minor.htm)|  Minor component of version
structure.  
![Public field](../icons/pubfield.gif)|
[revision](F_GH_IO_Types_GH_Version_revision.htm)|  Revision component of
version structure.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

