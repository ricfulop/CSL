---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm
scraped_at: 2025-09-08T16:19:34.136208
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm
"Grasshopper.Kernel.Expressions")

[GH_ExpressionParser
Class](../html/T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm
"GH_ExpressionParser Class")

[GH_ExpressionParser Constructor
](../html/Overload_Grasshopper_Kernel_Expressions_GH_ExpressionParser__ctor.htm
"GH_ExpressionParser Constructor ")

[GH_ExpressionParser
Properties](../html/Properties_T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm
"GH_ExpressionParser Properties")

[GH_ExpressionParser
Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm
"GH_ExpressionParser Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ExpressionParser Class  
  
---  
  
Provides a run-time evaluator for Grasshopper expressions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.ExpressionsGH_ExpressionParser  

**Namespace:**
[Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ExpressionParser
    
    
    Public Class GH_ExpressionParser

The GH_ExpressionParser type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ExpressionParser](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser__ctor.htm)|
Initializes a new instance of the GH_ExpressionParser class  
![Public method](../icons/pubmethod.gif)|
[GH_ExpressionParser(Boolean)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser__ctor_1.htm)|
Initializes a new instance of the GH_ExpressionParser class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ThrowExceptions](P_Grasshopper_Kernel_Expressions_GH_ExpressionParser_ThrowExceptions.htm)|  
![Public property](../icons/pubproperty.gif)|
[Variables](P_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Variables.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Complex)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Plane)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_1.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Point3d)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_2.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Vector3d)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_3.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Boolean)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_4.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Double)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_5.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
Int32)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_6.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariable(String,
String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_7.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariableEx(String,
GH_Variant)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariableEx.htm)|  
![Public method](../icons/pubmethod.gif)| [AddVariableEx(String,
IGH_Goo)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariableEx_1.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[BalancedCharTest](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_BalancedCharTest.htm)|
Test a string for balanced open and close chars. You can use this function to
see if brackets or parenthesis have been properly used.  
![Public method](../icons/pubmethod.gif)|
[CachedSymbols](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_CachedSymbols.htm)|
Retrieve a copy of the Queue of cached symbols. You can use the cached symbols
as an uber-optimization to speed up successive calls to Evaluate() with an
identical expression string  
![Public method](../icons/pubmethod.gif)|
[CacheSymbols](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_CacheSymbols.htm)|
Create a Symbols array from the expression. Use this method if you intend to
evaluate the same expression multiple times. At this point, the expression has
to be in correct syntax format. Use the GH_ExpressionSyntaxWriter.RewriteAll()
method to make sure.  
![Public method](../icons/pubmethod.gif)|
[ClearSymbols](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_ClearSymbols.htm)|
Destroy the Symbols cache.  
![Public method](../icons/pubmethod.gif)|
[ClearVariables](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_ClearVariables.htm)|
Destroy the variable cache.  
![Public method](../icons/pubmethod.gif)|
[DisplayFunctionList](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_DisplayFunctionList.htm)|  
![Public method](../icons/pubmethod.gif)|
[Evaluate](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate.htm)|
Evaluate the expression currently loaded in the Symbols cache using the
currently loaded variables.  
![Public method](../icons/pubmethod.gif)|
[Evaluate(QueueGH_ParserSymbol)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_1.htm)|
Evaluate the expression queue without overriding any local caches. You can
obtain an expression queue by calling CachedSymbols()  
![Public method](../icons/pubmethod.gif)|
[Evaluate(String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_2.htm)|
Store a new expression in the Symbols cache and evaluate it using the current
variables  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsValidVariableName](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_IsValidVariableName.htm)|
Tests whether a string is a valid variable name for expressions. Valid names
must contain at least one character, must start with an alphabetic character,
and only contain alphanumeric chars and underscores.  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryAddition](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAddition.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryAmpersand](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAmpersand.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryAND](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAND.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryAngle](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAngle.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryCircumflex](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryCircumflex.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryCrossProduct](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryCrossProduct.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryDistance](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryDistance.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryDivision](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryDivision.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryEquality](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryEquality.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryIntegerDivision](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryIntegerDivision.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryLargerThan](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryLargerThan.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryLargerThanOrEqual](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryLargerThanOrEqual.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryModulus](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryModulus.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryMultiplication](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryMultiplication.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryNearEquality](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryNearEquality.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryOR](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryOR.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryPull](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryPull.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryPush](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryPush.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinarySmallerThan](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinarySmallerThan.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinarySmallerThanOrEqual](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinarySmallerThanOrEqual.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinarySubtraction](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinarySubtraction.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_BinaryXOR](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryXOR.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryBang](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryBang.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryCube](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryCube.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryDeg2Rad](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryDeg2Rad.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryImaginary](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryImaginary.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryMinus](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryMinus.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryNOT](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryNOT.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryOComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryOComponent.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryPlus](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryPlus.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnarySquare](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnarySquare.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryXComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryXComponent.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryYComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryYComponent.htm)|  
![Protected method](../icons/protmethod.gif)|
[Op_UnaryZComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryZComponent.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Expressions
Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

