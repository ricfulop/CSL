---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_DataAccess.htm
scraped_at: 2025-09-08T16:18:21.800206
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm
"IGH_DataAccess Interface")

[IGH_DataAccess
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_DataAccess.htm
"IGH_DataAccess Properties")

[IGH_DataAccess
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm
"IGH_DataAccess Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_DataAccess Interface  
  
---  
  
Provides access to component parameters, in order to retrieve and assign data
during solutions.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_DataAccess
    
    
    Public Interface IGH_DataAccess

The IGH_DataAccess type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Iteration](P_Grasshopper_Kernel_IGH_DataAccess_Iteration.htm)|  Gets the
current iteration count. The first time the SolveInstance() function is called
on a component during a solution the Iteration counter will be zero. It will
be incremented by one for every subsequent call.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AbortComponentSolution](M_Grasshopper_Kernel_IGH_DataAccess_AbortComponentSolution.htm)|
Call this method if you wish to stop solving this component.  
![Public method](../icons/pubmethod.gif)|
[BlitDataQ](M_Grasshopper_Kernel_IGH_DataAccess_BlitData__1.htm)|  Creates a
direct copy of an existing data structure. The existing generic instance must
of the exact same type as the target parameter.  
![Public method](../icons/pubmethod.gif)|
[DisableGapLogic](M_Grasshopper_Kernel_IGH_DataAccess_DisableGapLogic.htm)|
Call this function if you want to disable the gap null logic for the current
iteration.  
![Public method](../icons/pubmethod.gif)|
[DisableGapLogic(Int32)](M_Grasshopper_Kernel_IGH_DataAccess_DisableGapLogic_1.htm)|
Call this function if you want to disable the gap null logic for a specific
output parameter.  
![Public method](../icons/pubmethod.gif)| [GetDataT(Int32,
T)](M_Grasshopper_Kernel_IGH_DataAccess_GetData__1.htm)|  Retrieve data from
an input parameter during GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [GetDataT(String,
T)](M_Grasshopper_Kernel_IGH_DataAccess_GetData__1_1.htm)|  Retrieve data from
an input parameter during GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [GetDataListT(Int32,
ListT)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1.htm)|  Retrieve an
entire list of data from an input parameter during
GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [GetDataListT(String,
ListT)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1_1.htm)|  Retrieve
an entire list of data from an input parameter during
GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [GetDataTreeT(Int32,
GH_StructureT)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1.htm)|
Retrieve an entire data tree from an input parameter during
GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [GetDataTreeT(String,
GH_StructureT)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1_1.htm)|
Retrieve an entire data tree from an input parameter during
GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)|
[IncrementIteration](M_Grasshopper_Kernel_IGH_DataAccess_IncrementIteration.htm)|
Increments the iteration count by 1.  
![Public method](../icons/pubmethod.gif)|
[ParameterTargetIndex](M_Grasshopper_Kernel_IGH_DataAccess_ParameterTargetIndex.htm)|
Get the target index for the specified output parameter.  
![Public method](../icons/pubmethod.gif)|
[ParameterTargetPath](M_Grasshopper_Kernel_IGH_DataAccess_ParameterTargetPath.htm)|
Get the target path for the specified output parameter.  
![Public method](../icons/pubmethod.gif)| [SetData(Int32,
Object)](M_Grasshopper_Kernel_IGH_DataAccess_SetData.htm)|  Stores data in an
output parameter during GH_Component.SolveInstance(). Use this function only
for setting individual data items. If you want to set lists of data, you
*must* call SetDataList() instead.  
![Public method](../icons/pubmethod.gif)| [SetData(String,
Object)](M_Grasshopper_Kernel_IGH_DataAccess_SetData_2.htm)|  Stores data in
an output parameter during GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [SetData(Int32, Object,
Int32)](M_Grasshopper_Kernel_IGH_DataAccess_SetData_1.htm)|  Expert user
function. Stores data in an output parameter during
GH_Component.SolveInstance(). Use this function only for setting individual
data items. If you want to set lists of data, you *must* call SetDataList()
instead.  
![Public method](../icons/pubmethod.gif)| [SetDataList(Int32,
IEnumerable)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataList.htm)|  Stores a
list of data in an output parameter during GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [SetDataList(String,
IEnumerable)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_2.htm)|  Stores
data in an output parameter during GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [SetDataList(Int32, IEnumerable,
Int32)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_1.htm)|  Expert user
function. Stores a list of data in an output parameter during
GH_Component.SolveInstance().  
![Public method](../icons/pubmethod.gif)| [SetDataTree(Int32,
IGH_DataTree)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataTree.htm)|  Folds a
utility tree representation into this tree.  
![Public method](../icons/pubmethod.gif)| [SetDataTree(Int32,
IGH_Structure)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataTree_1.htm)|  Folds
a utility tree representation into this tree.  
![Public method](../icons/pubmethod.gif)|
[Util_CountNonNullRefsT](M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNonNullRefs__1.htm)|
Count all object references in L  
![Public method](../icons/pubmethod.gif)|
[Util_CountNullRefsT](M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNullRefs__1.htm)|
Count all null references in L  
![Public method](../icons/pubmethod.gif)|
[Util_EnsureNonNullCountT](M_Grasshopper_Kernel_IGH_DataAccess_Util_EnsureNonNullCount__1.htm)|
Tests a list to see if it contains sufficient non-null references.  
![Public method](../icons/pubmethod.gif)|
[Util_FirstNonNullItemT](M_Grasshopper_Kernel_IGH_DataAccess_Util_FirstNonNullItem__1.htm)|
Returns the index of the first non-null item in a list.  
![Public method](../icons/pubmethod.gif)|
[Util_RemoveNullRefsT](M_Grasshopper_Kernel_IGH_DataAccess_Util_RemoveNullRefs__1.htm)|
Remove all null references from a list of items.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

