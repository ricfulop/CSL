---
url: https://freecad.github.io/SourceDoc/d8/de6/classDocumentObjectWeakPtrT_1_1Private.html
scraped_at: 2025-09-08T14:54:25.395296
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObjectWeakPtrT](../../dd/d16/classApp_1_1DocumentObjectWeakPtrT.html)
  * [Private](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html)

[List of all members](../../d3/d3d/classDocumentObjectWeakPtrT_1_1Private-members.html) | Public Types | Public Member Functions | Public Attributes

App::DocumentObjectWeakPtrT::Private Class Reference

##  Public Types  
  
---  
typedef boost::signals2::scoped_connection | [Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8)  
  
##  Public Member Functions  
  
---  
void | [createdObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aa1973e20c2895b62ace71624cb59508f) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &obj) noexcept  
void | [deletedDocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#adccf0a7f8715c9193d2fa2f38a5d9dbe) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
void | [deletedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a26e2acd99c19cb36d7f96e51133fa779) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &obj) noexcept  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [get](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a2acf6718d2f132500cd19c04ffd96067) () const noexcept  
|
[Private](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aa1c86bf82a66bd4f248ffa84d4914471)
([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
void | [reset](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a622159b934824212b13fd9b778bb0629) ()  
void | [set](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
  
##  Public Attributes  
  
---  
[Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8) | [connectApplicationDeletedDocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aefe322383e7a7fc216e4da7c8353cf2b)  
[Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8) | [connectDocumentCreatedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#af13f255a0b34bb9aa3f86473a23bd07e)  
[Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8) | [connectDocumentDeletedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a65139731d5c04c048e14ff08cfc790cd)  
[bool](../../d9/db9/classbool.html) | [indocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a308abf25bc0dbf860b940ee4208c23be)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [object](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#ac0344cc8819c48ef9b2b15ef6b49620c)  
  
## Member Typedef Documentation

## ◆ Connection

typedef boost::signals2::scoped_connection
[App::DocumentObjectWeakPtrT::Private::Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8)  
---  
  
## Constructor & Destructor Documentation

## ◆ Private()

App::DocumentObjectWeakPtrT::Private::Private  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
References
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## Member Function Documentation

## ◆ createdObject()

| void App::DocumentObjectWeakPtrT::Private::createdObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _obj_| ) |   
---|---|---|---|---|---  
noexcept  
  
References
[App::DocumentObjectWeakPtrT::Private::indocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a308abf25bc0dbf860b940ee4208c23be).

Referenced by
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ deletedDocument()

void App::DocumentObjectWeakPtrT::Private::deletedDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
References
[App::DocumentObjectWeakPtrT::Private::reset()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a622159b934824212b13fd9b778bb0629).

Referenced by
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ deletedObject()

| void App::DocumentObjectWeakPtrT::Private::deletedObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _obj_| ) |   
---|---|---|---|---|---  
noexcept  
  
References
[App::DocumentObjectWeakPtrT::Private::indocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a308abf25bc0dbf860b940ee4208c23be).

Referenced by
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ get()

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::DocumentObjectWeakPtrT::Private::get  | ( | | ) |  const  
---|---|---|---|---  
noexcept  
  
References
[App::DocumentObjectWeakPtrT::Private::indocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a308abf25bc0dbf860b940ee4208c23be),
and
[App::DocumentObjectWeakPtrT::Private::object](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#ac0344cc8819c48ef9b2b15ef6b49620c).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ reset()

void App::DocumentObjectWeakPtrT::Private::reset  | ( | | ) |   
---|---|---|---|---  
  
References
[App::DocumentObjectWeakPtrT::Private::connectApplicationDeletedDocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aefe322383e7a7fc216e4da7c8353cf2b),
[App::DocumentObjectWeakPtrT::Private::connectDocumentCreatedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#af13f255a0b34bb9aa3f86473a23bd07e),
[App::DocumentObjectWeakPtrT::Private::connectDocumentDeletedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a65139731d5c04c048e14ff08cfc790cd),
and
[App::DocumentObjectWeakPtrT::Private::indocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a308abf25bc0dbf860b940ee4208c23be).

Referenced by
[App::DocumentObjectWeakPtrT::Private::deletedDocument()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#adccf0a7f8715c9193d2fa2f38a5d9dbe),
and
[draftguitools.gui_trackers.gridTracker::set()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a1499cdcfd43fe110d46cd9c72c52b356).

## ◆ set()

void App::DocumentObjectWeakPtrT::Private::set  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[App::DocumentObjectWeakPtrT::Private::connectApplicationDeletedDocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aefe322383e7a7fc216e4da7c8353cf2b),
[App::DocumentObjectWeakPtrT::Private::connectDocumentCreatedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#af13f255a0b34bb9aa3f86473a23bd07e),
[App::DocumentObjectWeakPtrT::Private::connectDocumentDeletedObject](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a65139731d5c04c048e14ff08cfc790cd),
[App::DocumentObjectWeakPtrT::Private::createdObject()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aa1973e20c2895b62ace71624cb59508f),
[App::DocumentObjectWeakPtrT::Private::deletedDocument()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#adccf0a7f8715c9193d2fa2f38a5d9dbe),
[App::DocumentObjectWeakPtrT::Private::deletedObject()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a26e2acd99c19cb36d7f96e51133fa779),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::DocumentObjectWeakPtrT::Private::indocument](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a308abf25bc0dbf860b940ee4208c23be),
and
[App::Application::signalDeleteDocument](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297),
and
[App::DocumentObjectWeakPtrT::Private::Private()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aa1c86bf82a66bd4f248ffa84d4914471).

## Member Data Documentation

## ◆ connectApplicationDeletedDocument

[Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8)
App::DocumentObjectWeakPtrT::Private::connectApplicationDeletedDocument  
---  
  
Referenced by
[App::DocumentObjectWeakPtrT::Private::reset()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a622159b934824212b13fd9b778bb0629),
and
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ connectDocumentCreatedObject

[Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8)
App::DocumentObjectWeakPtrT::Private::connectDocumentCreatedObject  
---  
  
Referenced by
[App::DocumentObjectWeakPtrT::Private::reset()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a622159b934824212b13fd9b778bb0629),
and
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ connectDocumentDeletedObject

[Connection](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a11db2e5df15beae525b46f8dab67d0f8)
App::DocumentObjectWeakPtrT::Private::connectDocumentDeletedObject  
---  
  
Referenced by
[App::DocumentObjectWeakPtrT::Private::reset()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a622159b934824212b13fd9b778bb0629),
and
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ indocument

[bool](../../d9/db9/classbool.html)
App::DocumentObjectWeakPtrT::Private::indocument  
---  
  
Referenced by
[App::DocumentObjectWeakPtrT::Private::createdObject()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#aa1973e20c2895b62ace71624cb59508f),
[App::DocumentObjectWeakPtrT::Private::deletedObject()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a26e2acd99c19cb36d7f96e51133fa779),
[App::DocumentObjectWeakPtrT::Private::get()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a2acf6718d2f132500cd19c04ffd96067),
[App::DocumentObjectWeakPtrT::Private::reset()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a622159b934824212b13fd9b778bb0629),
and
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ object

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::DocumentObjectWeakPtrT::Private::object  
---  
  
Referenced by
[ArchIFCView.IfcContextUI::accept()](../../d6/d87/classArchIFCView_1_1IfcContextUI.html#ab7d354b99609992d4e72469f8a78e1a0),
[App::DocumentObjectWeakPtrT::Private::get()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a2acf6718d2f132500cd19c04ffd96067),
[ArchIFCView.IfcContextUI::prefillMapConversionForm()](../../d6/d87/classArchIFCView_1_1IfcContextUI.html#a0544c623b3745c8d7f0ec61e095e6ba4),
[importIFCHelper.ProjectImporter::setAttributes()](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#aae3c6ca3f199450ac7a0573d42741c5d),
and
[importIFCHelper.ProjectImporter::setComplexAttributes()](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#a348daed84b62f0bd0f8503772ff8bf40).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

