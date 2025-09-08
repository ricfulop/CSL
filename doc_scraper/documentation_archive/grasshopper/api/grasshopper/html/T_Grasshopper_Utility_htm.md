---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Utility.htm
scraped_at: 2025-09-08T16:11:50.096117
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Utility Class](../html/T_Grasshopper_Utility.htm "Utility Class")

[Utility Methods](../html/Methods_T_Grasshopper_Utility.htm "Utility Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Utility Class  
  
---  
  
Class with useful static methods.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GrasshopperUtility  

**Namespace:** [Grasshopper](N_Grasshopper.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Utility
    
    
    Public NotInheritable Class Utility

The Utility type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DocumentAngleTolerance](M_Grasshopper_Utility_DocumentAngleTolerance.htm)|
Returns the Angle Tolerance in degrees for the model document  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DocumentTolerance](M_Grasshopper_Utility_DocumentTolerance.htm)|  Returns the
Absolute Tolerance of the model document  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DocumentUnits](M_Grasshopper_Utility_DocumentUnits.htm)|  Returns the unit
system for the model document  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FixNewlines(String)](M_Grasshopper_Utility_FixNewlines.htm)|  Make sure all
newlines in a string adhere to the current platform standard.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FixNewlines(String, String)](M_Grasshopper_Utility_FixNewlines_1.htm)|  Make
sure all newlines in a string have a specific pattern.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeDownloader](M_Grasshopper_Utility_InvokeDownloader.htm)|  Start an
asynchronous download operation. The download runs in a separate appdomain.
After triggering that process this method returns immediately.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeGetter](M_Grasshopper_Utility_InvokeGetter.htm)|  Call a getter
property via its name.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeGetterSafe](M_Grasshopper_Utility_InvokeGetterSafe.htm)|  Call a getter
property via its name. No exceptions are thrown.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeMethod(Object, String)](M_Grasshopper_Utility_InvokeMethod.htm)|  Call
a method via its name.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeMethod(Object, String,
Object)](M_Grasshopper_Utility_InvokeMethod_1.htm)|  Call a method via its
name.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeMethodSafe(Object,
String)](M_Grasshopper_Utility_InvokeMethodSafe.htm)|  Call a method via its
name. No exceptions are thrown.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeMethodSafe(Object, String,
Object)](M_Grasshopper_Utility_InvokeMethodSafe_1.htm)|  Call a method via its
name. No exceptions are thrown.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeSetter](M_Grasshopper_Utility_InvokeSetter.htm)|  Call a setter
property via its name.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[InvokeSetterSafe](M_Grasshopper_Utility_InvokeSetterSafe.htm)|  Call a setter
property via its name. No exceptions are thrown.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[LikeOperator](M_Grasshopper_Utility_LikeOperator.htm)|  Exposes the VB.NET
Like operator as a static method.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SetDefaultTolerances](M_Grasshopper_Utility_SetDefaultTolerances.htm)|
Utility function to set absolute and angle tolerance fields.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[SetDefaultUnits](M_Grasshopper_Utility_SetDefaultUnits.htm)|  Utility
function to set model unit fields  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[TernaryIfT](M_Grasshopper_Utility_TernaryIf__1.htm)|  **Obsolete.** Type safe
implementation of the IIf conditional statement.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

