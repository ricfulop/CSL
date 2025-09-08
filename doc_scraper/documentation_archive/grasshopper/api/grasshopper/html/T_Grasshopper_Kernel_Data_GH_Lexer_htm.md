---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_Lexer.htm
scraped_at: 2025-09-08T16:19:03.982136
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_Lexer Class](../html/T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer
Class")

[GH_Lexer Constructor
](../html/Overload_Grasshopper_Kernel_Data_GH_Lexer__ctor.htm "GH_Lexer
Constructor ")

[GH_Lexer
Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Lexer.htm
"GH_Lexer Properties")

[GH_Lexer Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Lexer.htm
"GH_Lexer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Lexer Class  
  
---  
  
Represents a lexical mask for path operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_Lexer  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Lexer
    
    
    Public Class GH_Lexer

The GH_Lexer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_Lexer](M_Grasshopper_Kernel_Data_GH_Lexer__ctor.htm)|  Blank constructor.  
![Public method](../icons/pubmethod.gif)|
[GH_Lexer(String)](M_Grasshopper_Kernel_Data_GH_Lexer__ctor_1.htm)|  Create a
new mask from a textual string.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsItem](P_Grasshopper_Kernel_Data_GH_Lexer_IsItem.htm)|  Gets a value
indicating whether or not the item portion of the lexer has been set.  
![Public property](../icons/pubproperty.gif)|
[IsPath](P_Grasshopper_Kernel_Data_GH_Lexer_IsPath.htm)|  Gets a value
indicating whether or not the path portion of the lexer has been set.  
![Public property](../icons/pubproperty.gif)|
[Item](P_Grasshopper_Kernel_Data_GH_Lexer_Item.htm)|  Gets the item string
that was extracted from the mask. The default is "append"  
![Public property](../icons/pubproperty.gif)|
[Mask](P_Grasshopper_Kernel_Data_GH_Lexer_Mask.htm)|  Gets the original string
that represents the user input for this lexer.  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Kernel_Data_GH_Lexer_Path.htm)|  Gets the list of path
strings that was extracted from the mask. If the mask hasn't been parsed yet,
it will be parsed now. If the returned list is still nothing, parsing failed.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[EvaluatePath](M_Grasshopper_Kernel_Data_GH_Lexer_EvaluatePath.htm)|  Evaluate
the variables in this mask with the provided expression solver.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[PerformLexicalReplaceT(GH_Lexer, GH_Lexer, DataTreeT,
DataTreeT)](M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1.htm)|
Lexical Find..Replace operations.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[PerformLexicalReplaceT(GH_Lexer, GH_Lexer, IGH_Structure,
GH_StructureT)](M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1_1.htm)|
Lexical Find..Replace operations.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

