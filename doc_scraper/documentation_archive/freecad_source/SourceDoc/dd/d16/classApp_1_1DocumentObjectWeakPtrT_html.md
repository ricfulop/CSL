---
url: https://freecad.github.io/SourceDoc/dd/d16/classApp_1_1DocumentObjectWeakPtrT.html
scraped_at: 2025-09-08T14:54:24.407719
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html)

[List of all members](../../d5/d77/classApp_1_1DocumentObjectWeakPtrT-members.html) | Classes | Public Member Functions

App::DocumentObjectWeakPtrT Class Reference

The
[DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html
"The DocumentObjectWeakPtrT class.") class.
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#details)

`#include <DocumentObserver.h>`

##  Classes  
  
---  
class | [Private](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html)  
  
##  Public Member Functions  
  
---  
|
[DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a91507654ff286854fbd0be6806fda9c5)
([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
[bool](../../d9/db9/classbool.html) | [expired](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#ae267ebbec6f21864c14135117b65a3ec) () const noexcept  
| expired
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#ae267ebbec6f21864c14135117b65a3ec)  
  
template<typename T >  
T * | [get](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a02ba45b1ec8aef8ae386f0a096c04f54) () const noexcept  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a8da427d3e24f123b981bc0ad036107a0) (const [DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html) &p) const noexcept  
| operator !=
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a8da427d3e24f123b981bc0ad036107a0)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [operator*](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a476fab2e41476b926d63b5ebba9bc95d) () const noexcept  
| operator *
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a476fab2e41476b926d63b5ebba9bc95d)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [operator->](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a62782ca4385560ae6540bb39149ecaae) () const noexcept  
| operator ->
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a62782ca4385560ae6540bb39149ecaae)  
  
[DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html) & | [operator=](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#acc85782ea9bc8bf07931752eef1610a5) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *p)  
| operator = Assignment operator
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#acc85782ea9bc8bf07931752eef1610a5)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a9d637f93ddcdb24903cb75cc24baec7b) (const [DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html) &p) const noexcept  
| operator ==
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a9d637f93ddcdb24903cb75cc24baec7b)  
  
void | [reset](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a0b452bf8e1c30c8b8e8c9794ce2ec911) ()  
| reset Releases the reference to the managed object. After the call *this
manages no object.
[More...](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#a0b452bf8e1c30c8b8e8c9794ce2ec911)  
  
|
[~DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html#af9fae55c209c8c50cba04ef01895fcc1)
()  
  
## Detailed Description

The
[DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html
"The DocumentObjectWeakPtrT class.") class.

## Constructor & Destructor Documentation

## ◆ DocumentObjectWeakPtrT()

DocumentObjectWeakPtrT::DocumentObjectWeakPtrT  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
## ◆ ~DocumentObjectWeakPtrT()

DocumentObjectWeakPtrT::~DocumentObjectWeakPtrT  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ expired()

| [bool](../../d9/db9/classbool.html) DocumentObjectWeakPtrT::expired  | ( | | ) |  const  
---|---|---|---|---  
noexcept  
  
expired

Returns

    true if the managed object has already been deleted, false otherwise. 

Referenced by
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[PartGui::DlgPrimitives::accept()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a1db668afa4bde5626f25c5e34f596b82),
[PartGui::DlgPrimitives::reject()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a934c3b40a9db52e7a9cc8f2daffc3dba),
[PartDesignGui::TaskDlgFeatureParameters::reject()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#ab22141db4eb33119ad64ed387063f830),
and
[PartDesignGui::TaskDlgSketchBasedParameters::reject()](../../da/def/classPartDesignGui_1_1TaskDlgSketchBasedParameters.html#af410e02c04329e37c65f34452f4ce972).

## ◆ get()

template<typename T >

| T * App::DocumentObjectWeakPtrT::get  | ( | | ) |  const  
---|---|---|---|---  
noexcept  
  
Get a pointer to the object or 0 if it doesn't exist any more or the type
doesn't match.

Referenced by
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[FemGui::TaskPostBox::getTypedObject()](../../dc/d51/classFemGui_1_1TaskPostBox.html#ab2add9aef09b20ac0e793e4aaf057324),
and
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ operator!=()

| [bool](../../d9/db9/classbool.html) DocumentObjectWeakPtrT::operator!=  | ( | const [DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html) & | _p_| ) |  const  
---|---|---|---|---|---  
noexcept  
  
operator !=

Returns

    true if both objects are inequal, false otherwise 

## ◆ operator*()

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * DocumentObjectWeakPtrT::operator*  | ( | | ) |  const  
---|---|---|---|---  
noexcept  
  
operator *

Returns

    pointer to the document object 

## ◆ operator->()

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * DocumentObjectWeakPtrT::operator-> | ( | | ) |  const  
---|---|---|---|---  
noexcept  
  
operator ->

Returns

    pointer to the document object 

## ◆ operator=()

[DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html) & DocumentObjectWeakPtrT::operator=  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _p_| ) |   
---|---|---|---|---|---  
  
operator = Assignment operator

## ◆ operator==()

| [bool](../../d9/db9/classbool.html) DocumentObjectWeakPtrT::operator==  | ( | const [DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html) & | _p_| ) |  const  
---|---|---|---|---|---  
noexcept  
  
operator ==

Returns

    true if both objects are equal, false otherwise 

## ◆ reset()

void DocumentObjectWeakPtrT::reset  | ( | | ) |   
---|---|---|---|---  
  
reset Releases the reference to the managed object. After the call *this
manages no object.

Referenced by
[draftguitools.gui_trackers.gridTracker::set()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a1499cdcfd43fe110d46cd9c72c52b356).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObserver.h
  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

