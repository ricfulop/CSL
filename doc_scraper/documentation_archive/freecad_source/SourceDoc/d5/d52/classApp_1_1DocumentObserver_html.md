---
url: https://freecad.github.io/SourceDoc/d5/d52/classApp_1_1DocumentObserver.html
scraped_at: 2025-09-08T14:54:26.400888
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html)

[List of all members](../../de/de4/classApp_1_1DocumentObserver-members.html) | Public Member Functions | Protected Member Functions

App::DocumentObserver Class Reference

The [DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html "The
DocumentObserver class simplfies the step to write classes that listen to what
happens inside a d...") class simplfies the step to write classes that listen
to what happens inside a document.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#details)

`#include <DocumentObserver.h>`

##  Public Member Functions  
  
---  
void | [attachDocument](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1) ([Document](../../d8/d3e/classApp_1_1Document.html) *)  
| Attaches to another document, the old document is not longer observed then.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1)  
  
void | [detachDocument](../../d5/d52/classApp_1_1DocumentObserver.html#a47fa57aec4571b9e8e844bcc56962546) ()  
| Detaches from the current document, the document is not longer observed
then.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#a47fa57aec4571b9e8e844bcc56962546)  
  
|
[DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71)
()  
| Constructor.
[More...](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71)  
  
|
[DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html#aede80a503f96172d392f86ab3047a4da)
([Document](../../d8/d3e/classApp_1_1Document.html) *)  
virtual | [~DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html#ae777e9e5f17925e2740c3d126336c6ff) ()  
  
##  Protected Member Functions  
  
---  
[Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../d5/d52/classApp_1_1DocumentObserver.html#adda884e1c97f6d107ce0723a4ad6316c) () const  
  
## Detailed Description

The [DocumentObserver](../../d5/d52/classApp_1_1DocumentObserver.html "The
DocumentObserver class simplfies the step to write classes that listen to what
happens inside a d...") class simplfies the step to write classes that listen
to what happens inside a document.

This is very useful for classes that needs to be notified when an observed
object has changed.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ DocumentObserver() [1/2]

DocumentObserver::DocumentObserver  | ( | | ) |   
---|---|---|---|---  
  
Constructor.

References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Application::signalActiveDocument](../../da/dbf/classApp_1_1Application.html#ad9cf4f57c0d4fda56d79ec91936efa39),
[App::Application::signalDeleteDocument](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47),
and
[App::Application::signalNewDocument](../../da/dbf/classApp_1_1Application.html#a49425118433ce84229402407d5631ea4).

## ◆ DocumentObserver() [2/2]

DocumentObserver::DocumentObserver  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
  
References
[attachDocument()](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1).

## ◆ ~DocumentObserver()

| DocumentObserver::~DocumentObserver  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[detachDocument()](../../d5/d52/classApp_1_1DocumentObserver.html#a47fa57aec4571b9e8e844bcc56962546).

## Member Function Documentation

## ◆ attachDocument()

void DocumentObserver::attachDocument  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
  
Attaches to another document, the old document is not longer observed then.

References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
and
[detachDocument()](../../d5/d52/classApp_1_1DocumentObserver.html#a47fa57aec4571b9e8e844bcc56962546).

Referenced by
[MeshGui::ViewProviderMeshCurvature::attach()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad36ed9ef7edb7c4ec98d622ec6acf48c),
[PartGui::DlgProjectionOnSurface::DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a280d8ac8bf690484a268f54625c2c7e2),
[DocumentObserver()](../../d5/d52/classApp_1_1DocumentObserver.html#aede80a503f96172d392f86ab3047a4da),
[MeshGui::DlgEvaluateMeshImp::on_refreshButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a605469a13d795eb6e023070fd85ade67),
[FemGui::ActiveAnalysisObserver::setActiveObject()](../../dd/df6/classFemGui_1_1ActiveAnalysisObserver.html#a668eeab67692a4bf570ccdf236264d19),
and
[MeshGui::DlgEvaluateMeshImp::setMesh()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a7f2b91d48902ffdad8f55ddc9ef1fce2).

## ◆ detachDocument()

void DocumentObserver::detachDocument  | ( | | ) |   
---|---|---|---|---  
  
Detaches from the current document, the document is not longer observed then.

Referenced by
[attachDocument()](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1),
and
[~DocumentObserver()](../../d5/d52/classApp_1_1DocumentObserver.html#ae777e9e5f17925e2740c3d126336c6ff).

## ◆ getDocument()

| [Document](../../d8/d3e/classApp_1_1Document.html) * DocumentObserver::getDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
protected  
  
Referenced by
[Sandbox::DocumentProtector::addObject()](../../d0/d8d/classSandbox_1_1DocumentProtector.html#ab3e2eccd0614aea0d2988a03c2e59f55),
[Spreadsheet::SheetObserver::getDocument()](../../db/d2b/classSpreadsheet_1_1SheetObserver.html#adcbcf41923104aefe294ef59d94d8e00),
[MeshGui::DlgEvaluateMeshImp::on_meshNameButton_activated()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ae54004188b150e536ff0d1a2fec6c314),
[MeshGui::DlgEvaluateMeshImp::on_refreshButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a605469a13d795eb6e023070fd85ade67),
[Sandbox::DocumentProtector::recompute()](../../d0/d8d/classSandbox_1_1DocumentProtector.html#a7bfc865c9997d286b937bf58e109ff82),
[MeshGui::DlgEvaluateMeshImp::refreshList()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a09df67f594d7ad5fa40960e816fc8f4a),
[Sandbox::DocumentProtector::removeObject()](../../d0/d8d/classSandbox_1_1DocumentProtector.html#aa2c7a64fd80eccc6af9e4f9810e766c0),
and
[MeshGui::DlgEvaluateMeshImp::setMesh()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a7f2b91d48902ffdad8f55ddc9ef1fce2).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObserver.h
  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

