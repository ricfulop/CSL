---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm
scraped_at: 2025-09-08T16:19:24.085400
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_TreeRules Class](../html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm
"GH_TreeRules Class")

[GH_TreeRules Constructor
](../html/M_Grasshopper_Kernel_Data_GH_TreeRules__ctor.htm "GH_TreeRules
Constructor ")

[GH_TreeRules
Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_TreeRules.htm
"GH_TreeRules Properties")

[GH_TreeRules
Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeRules.htm
"GH_TreeRules Methods")

[GH_TreeRules
Fields](../html/Fields_T_Grasshopper_Kernel_Data_GH_TreeRules.htm
"GH_TreeRules Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_TreeRules Class  
  
---  
  
Represents an entire data tree rule set.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_TreeRules  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_TreeRules
    
    
    Public NotInheritable Class GH_TreeRules

The GH_TreeRules type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_TreeRules](M_Grasshopper_Kernel_Data_GH_TreeRules__ctor.htm)|  Constructs
a new rule set for testing data trees. Unless you know exactly what you are
doing, use the FromString() static method instead.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[HasItemRule](P_Grasshopper_Kernel_Data_GH_TreeRules_HasItemRule.htm)|  Gets
whether this rule set has a defined index rule.  
![Public property](../icons/pubproperty.gif)|
[HasPathRules](P_Grasshopper_Kernel_Data_GH_TreeRules_HasPathRules.htm)|  Gets
whether this rule set has any path rules.  
![Public property](../icons/pubproperty.gif)|
[PathRuleCount](P_Grasshopper_Kernel_Data_GH_TreeRules_PathRuleCount.htm)|
Gets the number of defined path rules.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Apply(GH_Path)](M_Grasshopper_Kernel_Data_GH_TreeRules_Apply.htm)|  Apply all
the local rules to a path.  
![Public method](../icons/pubmethod.gif)| [Apply(GH_Path,
Int32)](M_Grasshopper_Kernel_Data_GH_TreeRules_Apply_1.htm)|  Apply all the
local rules to a path+index combination.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FromString](M_Grasshopper_Kernel_Data_GH_TreeRules_FromString.htm)|  Attempt
to parse a Pattern string.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Data_GH_TreeRules_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[AllowedChars](F_Grasshopper_Kernel_Data_GH_TreeRules_AllowedChars.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[AndOperator](F_Grasshopper_Kernel_Data_GH_TreeRules_AndOperator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[AnyNumbersSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_AnyNumbersSymbol.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[AnyNumberSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_AnyNumberSymbol.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ItemBrackets](F_Grasshopper_Kernel_Data_GH_TreeRules_ItemBrackets.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ItemCloseBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_ItemCloseBracket.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[ItemOpenBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_ItemOpenBracket.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[NotOperator](F_Grasshopper_Kernel_Data_GH_TreeRules_NotOperator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[OrOperator](F_Grasshopper_Kernel_Data_GH_TreeRules_OrOperator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathBrackets](F_Grasshopper_Kernel_Data_GH_TreeRules_PathBrackets.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathCloseBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_PathCloseBracket.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathOpenBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_PathOpenBracket.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[PathSeparator](F_Grasshopper_Kernel_Data_GH_TreeRules_PathSeparator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[RangeSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_RangeSymbol.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[RuleBrackets](F_Grasshopper_Kernel_Data_GH_TreeRules_RuleBrackets.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[RuleCloseBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_RuleCloseBracket.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[RuleOpenBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_RuleOpenBracket.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[Separator](F_Grasshopper_Kernel_Data_GH_TreeRules_Separator.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[SequenceCode](F_Grasshopper_Kernel_Data_GH_TreeRules_SequenceCode.htm)|  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[SequenceSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_SequenceSymbol.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

