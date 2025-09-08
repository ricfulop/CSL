---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm
scraped_at: 2025-09-08T16:19:36.141611
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm
"Grasshopper.Kernel.Expressions")

[GH_ExpressionSyntaxWriter
Class](../html/T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm
"GH_ExpressionSyntaxWriter Class")

[GH_ExpressionSyntaxWriter
Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm
"GH_ExpressionSyntaxWriter Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ExpressionSyntaxWriter Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.ExpressionsGH_ExpressionSyntaxWriter  

**Namespace:**
[Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_ExpressionSyntaxWriter
    
    
    Public NotInheritable Class GH_ExpressionSyntaxWriter

The GH_ExpressionSyntaxWriter type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RewriteAll](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteAll.htm)|
Apply all syntax rulesets to the expression.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RewriteForEvaluator(GH_CodeString)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator.htm)|
Rewrite the expression so that all temporary keywords and symbols are replaced
by evaluator-specific chars. The expression will become less readable, do not
let the user see the result of this function. You need to rewrite the
expression with this function if you intend to feed it into the Evaluator.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RewriteForEvaluator(String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator_1.htm)|
Rewrite the expression so that all temporary keywords and symbols are replaced
by evaluator-specific chars. The expression will become less readable, do not
let the user see the result of this function. You need to rewrite the
expression with this function if you intend to feed it into the Evaluator.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RewriteForGraphicInterface(GH_CodeString)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForGraphicInterface.htm)|
Rewrite the expression so that tags are replaced by the complex characters
that make up the esoteric operators, functions and constants. The expression
should become more readable for humans.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RewriteForGraphicInterface(String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForGraphicInterface_1.htm)|
Rewrite the expression so that tags are replaced by the complex characters
that make up the esoteric operators, functions and constants. The expression
should become more readable  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Expressions
Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

