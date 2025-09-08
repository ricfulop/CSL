---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_StructurePath.htm
scraped_at: 2025-09-08T16:21:30.621908
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_StructurePath
Class](../html/T_Grasshopper_Kernel_Types_GH_StructurePath.htm
"GH_StructurePath Class")

[GH_StructurePath Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_StructurePath__ctor.htm
"GH_StructurePath Constructor ")

[GH_StructurePath
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_StructurePath.htm
"GH_StructurePath Properties")

[GH_StructurePath
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_StructurePath.htm
"GH_StructurePath Methods")

[GH_StructurePath
Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_StructurePath.htm
"GH_StructurePath Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_StructurePath Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)[GH_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
Grasshopper.Kernel.TypesGH_StructurePath  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_StructurePath : GH_Goo<GH_Path>
    
    
    Public Class GH_StructurePath
    	Inherits GH_Goo(Of GH_Path)

The GH_StructurePath type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_StructurePath](M_Grasshopper_Kernel_Types_GH_StructurePath__ctor.htm)|
Blank constructor  
![Public method](../icons/pubmethod.gif)|
[GH_StructurePath(GH_Path)](M_Grasshopper_Kernel_Types_GH_StructurePath__ctor_1.htm)|
Initializes a new instance of the GH_StructurePath class  
![Public method](../icons/pubmethod.gif)|
[GH_StructurePath(GH_StructurePath)](M_Grasshopper_Kernel_Types_GH_StructurePath__ctor_2.htm)|
Initializes a new instance of the GH_StructurePath class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_StructurePath_IsValid.htm)|  Gets the
validity of this instance. Integers are always valid  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_StructurePath_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_StructurePath_TypeName.htm)|
(Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_StructurePath_Value.htm)|  (Overrides
[GH_GooTValue](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_StructurePath_CastFrom.htm)|
(Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_StructurePath_CastTo__1.htm)|
(Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_StructurePath_Duplicate.htm)|
(Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicatePath](M_Grasshopper_Kernel_Types_GH_StructurePath_DuplicatePath.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_StructurePath_EmitProxy.htm)|
(Overrides
[GH_GooTEmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_StructurePath_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_StructurePath_ScriptVariable.htm)|
(Overrides
[GH_GooTScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_StructurePath_ToString.htm)|
(Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_StructurePath_Write.htm)|  (Overrides
[GH_GooTWrite(GH_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm)|  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

