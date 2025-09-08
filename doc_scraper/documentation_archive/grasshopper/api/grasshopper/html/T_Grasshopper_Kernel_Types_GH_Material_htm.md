---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Material.htm
scraped_at: 2025-09-08T16:21:01.483294
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Material Class](../html/T_Grasshopper_Kernel_Types_GH_Material.htm
"GH_Material Class")

[GH_Material Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Material__ctor.htm "GH_Material
Constructor ")

[GH_Material
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Material.htm
"GH_Material Properties")

[GH_Material
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Material.htm
"GH_Material Methods")

[GH_Material Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Material.htm
"GH_Material Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Material Class  
  
---  
  
Represents a implementation of the Rhino material

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)DisplayMaterial  
Grasshopper.Kernel.TypesGH_Material  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Material : GH_Goo<DisplayMaterial>
    
    
    Public Class GH_Material
    	Inherits GH_Goo(Of DisplayMaterial)

The GH_Material type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Material](M_Grasshopper_Kernel_Types_GH_Material__ctor.htm)| Initializes a
new instance of the GH_Material class  
![Public method](../icons/pubmethod.gif)|
[GH_Material(Color)](M_Grasshopper_Kernel_Types_GH_Material__ctor_4.htm)|
Create a new material based on a colour. The colour is used to control
Diffuse, Emission and Transparency. Ambient, Specular and Shine are always
default.  
![Public method](../icons/pubmethod.gif)|
[GH_Material(DisplayMaterial)](M_Grasshopper_Kernel_Types_GH_Material__ctor_2.htm)|
Create a new Material.  
![Public method](../icons/pubmethod.gif)|
[GH_Material(GH_Material)](M_Grasshopper_Kernel_Types_GH_Material__ctor_1.htm)|
Copy another GH_Material instance.  
![Public method](../icons/pubmethod.gif)|
[GH_Material(Guid)](M_Grasshopper_Kernel_Types_GH_Material__ctor_5.htm)|
Create a new Material from an RDK material ID.  
![Public method](../icons/pubmethod.gif)|
[GH_Material(RenderMaterial)](M_Grasshopper_Kernel_Types_GH_Material__ctor_3.htm)|
Create a new Material.  
![Public method](../icons/pubmethod.gif)|
[GH_Material(String)](M_Grasshopper_Kernel_Types_GH_Material__ctor_6.htm)|
Create a new Material from an RDK xml string.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Material_IsValid.htm)|  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Material_IsValidWhyNot.htm)|
Gets a string describing the state of "invalidness". If the instance _is_
valid, then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[RdkMaterialId](P_Grasshopper_Kernel_Types_GH_Material_RdkMaterialId.htm)|
Gets or sets the RDK material ID this material is associated with.  
![Public property](../icons/pubproperty.gif)|
[RdkMaterialRmtl](P_Grasshopper_Kernel_Types_GH_Material_RdkMaterialRmtl.htm)|
Gets or sets the RDK material RMTL file path.  
![Public property](../icons/pubproperty.gif)|
[RdkMaterialXml](P_Grasshopper_Kernel_Types_GH_Material_RdkMaterialXml.htm)|
Gets or sets the RDK material Xml string.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_Types_GH_Material_Type.htm)|  Gets the implied
type based on what fields have been assigned.  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Material_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Material_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Material_CastFrom.htm)|  (Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_Material_CastTo__1.htm)|
(Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateRhinoMaterial](M_Grasshopper_Kernel_Types_GH_Material_CreateRhinoMaterial.htm)|
Creates a standard Rhino material from a colour.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateStandardMaterial](M_Grasshopper_Kernel_Types_GH_Material_CreateStandardMaterial.htm)|
Creates a standard Grasshopper material from a colour.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Material_Duplicate.htm)|  Duplicate
this material.  (Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateMaterial](M_Grasshopper_Kernel_Types_GH_Material_DuplicateMaterial.htm)|
Duplicate this material.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Material_EmitProxy.htm)|  (Overrides
[GH_GooTEmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[MaterialBestGuess](M_Grasshopper_Kernel_Types_GH_Material_MaterialBestGuess.htm)|
Gets the best guess RenderMaterial for this shader.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Material_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Material_ScriptVariable.htm)|
(Overrides
[GH_GooTScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Material_ToString.htm)|  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Material_Write.htm)|  (Overrides
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

