---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm
scraped_at: 2025-09-08T16:19:02.986517
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_IndexRuleSet Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm
"GH_IndexRuleSet Class")

[GH_IndexRuleSet Constructor
](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet__ctor.htm "GH_IndexRuleSet
Constructor ")

[GH_IndexRuleSet
Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm
"GH_IndexRuleSet Properties")

[GH_IndexRuleSet
Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm
"GH_IndexRuleSet Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_IndexRuleSet Class  
  
---  
  
A collection of index rules.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.DataGH_IndexRuleSet  

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_IndexRuleSet
    
    
    Public Class GH_IndexRuleSet

The GH_IndexRuleSet type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_IndexRuleSet](M_Grasshopper_Kernel_Data_GH_IndexRuleSet__ctor.htm)|  Blank
constructor. Creates an empty collection of rules.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Count](P_Grasshopper_Kernel_Data_GH_IndexRuleSet_Count.htm)|  Gets the number
of rules defined in this collection.  
![Public property](../icons/pubproperty.gif)|
[Rule](P_Grasshopper_Kernel_Data_GH_IndexRuleSet_Rule.htm)|  Gets the rule at
the specified index.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddAnyDigitRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddAnyDigitRule.htm)|
Append a rule for any single digit.  
![Public method](../icons/pubmethod.gif)|
[AddAnyDigitsRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddAnyDigitsRule.htm)|
Append a rule for any amount of digits.  
![Public method](../icons/pubmethod.gif)|
[AddDigitPatternRule(Int32)](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_2.htm)|
Append a rule for filtering digit patterns.  
![Public method](../icons/pubmethod.gif)| [AddDigitPatternRule(Int32,
Int32)](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule.htm)|
Append a rule for filtering digit patterns. This pattern does not have an
upper bound.  
![Public method](../icons/pubmethod.gif)| [AddDigitPatternRule(Int32, Int32,
Int32)](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_1.htm)|
Append a rule for filtering digit patterns.  
![Public method](../icons/pubmethod.gif)|
[AddDigitRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitRule.htm)|
Append a single digit rule.  
![Public method](../icons/pubmethod.gif)|
[AddRangePatternRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangePatternRule.htm)|
Append a rule for filtering range patterns.  
![Public method](../icons/pubmethod.gif)|
[AddRangeRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangeRule.htm)|
Append a single range rule.  
![Public method](../icons/pubmethod.gif)|
[Evaluate](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_Evaluate.htm)|  Evaluate
the index given the local rules.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

