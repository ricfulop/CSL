---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_RuleKind.htm
scraped_at: 2025-09-08T16:19:13.034249
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm
"Grasshopper.Kernel.Data")

[GH_BracketMismatchException
Class](../html/T_Grasshopper_Kernel_Data_GH_BracketMismatchException.htm
"GH_BracketMismatchException Class")

[GH_ExpandMode
Enumeration](../html/T_Grasshopper_Kernel_Data_GH_ExpandMode.htm
"GH_ExpandMode Enumeration")

[GH_GraftMode Enumeration](../html/T_Grasshopper_Kernel_Data_GH_GraftMode.htm
"GH_GraftMode Enumeration")

[GH_IndexRange Structure](../html/T_Grasshopper_Kernel_Data_GH_IndexRange.htm
"GH_IndexRange Structure")

[GH_IndexRanges Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRanges.htm
"GH_IndexRanges Class")

[GH_IndexRuleSet Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm
"GH_IndexRuleSet Class")

[GH_Lexer Class](../html/T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer
Class")

[GH_LexerCombo Class](../html/T_Grasshopper_Kernel_Data_GH_LexerCombo.htm
"GH_LexerCombo Class")

[GH_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH_Path.PathLengthComparer
Class](../html/T_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer.htm
"GH_Path.PathLengthComparer Class")

[GH_PathOffset Class](../html/T_Grasshopper_Kernel_Data_GH_PathOffset.htm
"GH_PathOffset Class")

[GH_RuleAnyNumber
Class](../html/T_Grasshopper_Kernel_Data_GH_RuleAnyNumber.htm
"GH_RuleAnyNumber Class")

[GH_RuleAnyNumbers
Class](../html/T_Grasshopper_Kernel_Data_GH_RuleAnyNumbers.htm
"GH_RuleAnyNumbers Class")

[GH_RuleComplex Class](../html/T_Grasshopper_Kernel_Data_GH_RuleComplex.htm
"GH_RuleComplex Class")

[GH_RuleGroup Class](../html/T_Grasshopper_Kernel_Data_GH_RuleGroup.htm
"GH_RuleGroup Class")

[GH_RuleKind Enumeration](../html/T_Grasshopper_Kernel_Data_GH_RuleKind.htm
"GH_RuleKind Enumeration")

[GH_RuleNumber Class](../html/T_Grasshopper_Kernel_Data_GH_RuleNumber.htm
"GH_RuleNumber Class")

[GH_RuleOperator
Enumeration](../html/T_Grasshopper_Kernel_Data_GH_RuleOperator.htm
"GH_RuleOperator Enumeration")

[GH_RuleRange Class](../html/T_Grasshopper_Kernel_Data_GH_RuleRange.htm
"GH_RuleRange Class")

[GH_RuleResult
Enumeration](../html/T_Grasshopper_Kernel_Data_GH_RuleResult.htm
"GH_RuleResult Enumeration")

[GH_RuleSequence Class](../html/T_Grasshopper_Kernel_Data_GH_RuleSequence.htm
"GH_RuleSequence Class")

[GH_SimplificationMode
Enumeration](../html/T_Grasshopper_Kernel_Data_GH_SimplificationMode.htm
"GH_SimplificationMode Enumeration")

[GH_StringMismatchException
Class](../html/T_Grasshopper_Kernel_Data_GH_StringMismatchException.htm
"GH_StringMismatchException Class")

[GH_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm
"GH_Structure\(T\) Class")

[GH_Structure(T).ConversionDelegate(Tfrom, Tto)
Delegate](../html/T_Grasshopper_Kernel_Data_GH_Structure_1_ConversionDelegate_2.htm
"GH_Structure\(T\).ConversionDelegate\(Tfrom, Tto\) Delegate")

[GH_TreeFilter Class](../html/T_Grasshopper_Kernel_Data_GH_TreeFilter.htm
"GH_TreeFilter Class")

[GH_TreeIndex Structure](../html/T_Grasshopper_Kernel_Data_GH_TreeIndex.htm
"GH_TreeIndex Structure")

[GH_TreeRules Class](../html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm
"GH_TreeRules Class")

[IGH_DataTree Interface](../html/T_Grasshopper_Kernel_Data_IGH_DataTree.htm
"IGH_DataTree Interface")

[IGH_IndexRule Interface](../html/T_Grasshopper_Kernel_Data_IGH_IndexRule.htm
"IGH_IndexRule Interface")

[IGH_Rule Interface](../html/T_Grasshopper_Kernel_Data_IGH_Rule.htm "IGH_Rule
Interface")

[IGH_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm
"IGH_Structure Interface")

[IGH_StructureEnumerator
Interface](../html/T_Grasshopper_Kernel_Data_IGH_StructureEnumerator.htm
"IGH_StructureEnumerator Interface")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RuleKind Enumeration  
  
---  
  
Represents all possible element types in a Path Pattern.

**Namespace:** [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public enum GH_RuleKind
    
    
    Public Enumeration GH_RuleKind

![](../icons/SectionExpanded.png)Members

| Member name| Value| Description  
---|---|---|---  
| None| 0|  Represents an invalid, default value.  
| AnyNumber| 1|  Any single number  
| AnyNumbers| 2|  Any (or no) collection of numbers  
| Number| 3|  Single number  
| Group| 4|  A collection of non-related integers.  
| Range| 5|  A range of digits delimited by two extremes.  
| Sequence| 6|  A collection of increasing non-related integers which repeat
either indefinitely or up to a limit  
| Complex| 7|  Represents a complex of multiple pattern types.  
  
![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

