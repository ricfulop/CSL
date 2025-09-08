---
url: https://freecad.github.io/SourceDoc/d7/d23/classApp_1_1DocInfo.html
scraped_at: 2025-09-08T14:54:15.374135
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocInfo](../../d7/d23/classApp_1_1DocInfo.html)

[List of all members](../../dd/d78/classApp_1_1DocInfo-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes

App::DocInfo Class Reference

##  Public Types  
  
---  
typedef boost::signals2::scoped_connection | [Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)  
  
##  Public Member Functions  
  
---  
void | [attach](../../d7/d23/classApp_1_1DocInfo.html#abfdf47204bf7a84f4d19f3a04c5a4199) ([Document](../../d8/d3e/classApp_1_1Document.html) *doc)  
void | [deinit](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef) ()  
|
[DocInfo](../../d7/d23/classApp_1_1DocInfo.html#afd71298265437d060955fbbba855b13f)
()  
const char * | [filePath](../../d7/d23/classApp_1_1DocInfo.html#a734562de80859a471b972373316295a7) () const  
QString | [getFullPath](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7) () const  
[bool](../../d9/db9/classbool.html) | [hasXLink](../../d7/d23/classApp_1_1DocInfo.html#a8f86a3a1a64a037d53f9b66c7f01e3c4) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc) const  
void | [init](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca) (DocInfoMap::iterator pos, const char *objName, [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) *l)  
void | [remove](../../d7/d23/classApp_1_1DocInfo.html#af2d96170c638014561077c6f58af9f98) ([PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) *l)  
void | [slotDeleteDocument](../../d7/d23/classApp_1_1DocInfo.html#ac304ec8dca7b41f324f00c05df2702f0) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
void | [slotFinishRestoreDocument](../../d7/d23/classApp_1_1DocInfo.html#a267d94a9a178b9aff702ce8588a617f8) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
void | [slotSaveDocument](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
|
[~DocInfo](../../d7/d23/classApp_1_1DocInfo.html#a0c588447aad073afb6b018e037f170fe)
()  
  
##  Static Public Member Functions  
  
---  
static void | [breakLinks](../../d7/d23/classApp_1_1DocInfo.html#a9eeca81cb964af7cf2d763d2ae31e199) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear)  
static [DocInfoPtr](../../dd/dc2/namespaceApp.html#a1752a0f247a3d9b40c49fb0d930114d5) | [get](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a) (const char *filename, [App::Document](../../d8/d3e/classApp_1_1Document.html) *pDoc, [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) *l, const char *objName)  
static std::string | [getDocPath](../../d7/d23/classApp_1_1DocInfo.html#a9a066a626c84cb4c5ce152b9449b64f3) (const char *filename, [App::Document](../../d8/d3e/classApp_1_1Document.html) *pDoc, [bool](../../d9/db9/classbool.html) relative, QString *fullPath=nullptr)  
static QString | [getFullPath](../../d7/d23/classApp_1_1DocInfo.html#a50717ea39ed31d00a5ea06f82d69e714) (const char *p)  
static void | [restoreDocument](../../d7/d23/classApp_1_1DocInfo.html#adbe834c3373cedf88409bac61bb0302e) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)  
  
##  Public Attributes  
  
---  
[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60) | [connDeletedObject](../../d7/d23/classApp_1_1DocInfo.html#ad16fa9818f8eac85b73a2ad11dd9a3f4)  
[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60) | [connDeleteDocument](../../d7/d23/classApp_1_1DocInfo.html#a5affea3e5e1af4c72fff43ad7d7d066f)  
[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60) | [connFinishRestoreDocument](../../d7/d23/classApp_1_1DocInfo.html#aa3cf9a04d67a6c00ff073fb94872e975)  
[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60) | [connPendingReloadDocument](../../d7/d23/classApp_1_1DocInfo.html#a67666267a55890c8ecc3e2e71951bedd)  
[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60) | [connSaveDocument](../../d7/d23/classApp_1_1DocInfo.html#a7a7e1279c2afd7c33a3c002ae10d6390)  
std::set< [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) * > | [links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777)  
std::string | [myPath](../../d7/d23/classApp_1_1DocInfo.html#a07503c453981a0de2a8e9a4331618b73)  
DocInfoMap::iterator | [myPos](../../d7/d23/classApp_1_1DocInfo.html#a70fe9f14dcfa154b6ff85d8b90d87e2f)  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [pcDoc](../../d7/d23/classApp_1_1DocInfo.html#a4bee0e66d2dc16f678619500f28fd723)  
  
## Member Typedef Documentation

## ◆ Connection

typedef boost::signals2::scoped_connection
[App::DocInfo::Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)  
---  
  
## Constructor & Destructor Documentation

## ◆ DocInfo()

App::DocInfo::DocInfo  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~DocInfo()

App::DocInfo::~DocInfo  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ attach()

void App::DocInfo::attach  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
  
References
[App::Application::addPendingDocument()](../../da/dbf/classApp_1_1Application.html#a19eb6e22125db0a37cd540e4076b8b41),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::PropertyLinkBase::LinkRestoring](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa1de51bd54c0f62a03f8a15c70ed4a365),
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777),
[App::Document::PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
and
[pcDoc](../../d7/d23/classApp_1_1DocInfo.html#a4bee0e66d2dc16f678619500f28fd723).

Referenced by
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca),
and
[slotFinishRestoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#a267d94a9a178b9aff702ce8588a617f8).

## ◆ breakLinks()

| static void App::DocInfo::breakLinks  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clear_  
| ) | |   
static  
  
References
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777).

Referenced by
[App::PropertyLinkBase::breakLinks()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44).

## ◆ deinit()

void App::DocInfo::deinit  | ( | | ) |   
---|---|---|---|---  
  
References
[connDeletedObject](../../d7/d23/classApp_1_1DocInfo.html#ad16fa9818f8eac85b73a2ad11dd9a3f4),
[connDeleteDocument](../../d7/d23/classApp_1_1DocInfo.html#a5affea3e5e1af4c72fff43ad7d7d066f),
[connFinishRestoreDocument](../../d7/d23/classApp_1_1DocInfo.html#aa3cf9a04d67a6c00ff073fb94872e975),
[connPendingReloadDocument](../../d7/d23/classApp_1_1DocInfo.html#a67666267a55890c8ecc3e2e71951bedd),
[connSaveDocument](../../d7/d23/classApp_1_1DocInfo.html#a7a7e1279c2afd7c33a3c002ae10d6390),
[filePath()](../../d7/d23/classApp_1_1DocInfo.html#a734562de80859a471b972373316295a7),
[App::Document::getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777),
[myPath](../../d7/d23/classApp_1_1DocInfo.html#a07503c453981a0de2a8e9a4331618b73),
[myPos](../../d7/d23/classApp_1_1DocInfo.html#a70fe9f14dcfa154b6ff85d8b90d87e2f),
and
[pcDoc](../../d7/d23/classApp_1_1DocInfo.html#a4bee0e66d2dc16f678619500f28fd723).

Referenced by
[remove()](../../d7/d23/classApp_1_1DocInfo.html#af2d96170c638014561077c6f58af9f98),
and
[slotDeleteDocument()](../../d7/d23/classApp_1_1DocInfo.html#ac304ec8dca7b41f324f00c05df2702f0).

## ◆ filePath()

const char * App::DocInfo::filePath  | ( | | ) |  const  
---|---|---|---|---  
  
References
[myPath](../../d7/d23/classApp_1_1DocInfo.html#a07503c453981a0de2a8e9a4331618b73).

Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
and
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## ◆ get()

| static [DocInfoPtr](../../dd/dc2/namespaceApp.html#a1752a0f247a3d9b40c49fb0d930114d5) App::DocInfo::get  | ( | const char *  | _filename_ ,   
---|---|---|---  
|  | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _pDoc_ ,   
|  | [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) *  | _l_ ,   
|  | const char *  | _objName_  
| ) | |   
static  
  
References
[App::Application::addPendingDocument()](../../da/dbf/classApp_1_1Application.html#a19eb6e22125db0a37cd540e4076b8b41),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[getDocPath()](../../d7/d23/classApp_1_1DocInfo.html#a9a066a626c84cb4c5ce152b9449b64f3),
[getFullPath()](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7),
and
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297),
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

## ◆ getDocPath()

| static std::string App::DocInfo::getDocPath  | ( | const char *  | _filename_ ,   
---|---|---|---  
|  | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _pDoc_ ,   
|  | [bool](../../d9/db9/classbool.html) | _relative_ ,   
|  | QString *  | _fullPath_ = `nullptr`  
| ) | |   
static  
  
References
[App::Document::getFileName()](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d).

Referenced by
[get()](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a),
and
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8).

## ◆ getFullPath() [1/2]

QString App::DocInfo::getFullPath  | ( | | ) |  const  
---|---|---|---|---  
  
References
[myPos](../../d7/d23/classApp_1_1DocInfo.html#a70fe9f14dcfa154b6ff85d8b90d87e2f).

Referenced by
[get()](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a),
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca),
[restoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#adbe834c3373cedf88409bac61bb0302e),
[slotFinishRestoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#a267d94a9a178b9aff702ce8588a617f8),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

## ◆ getFullPath() [2/2]

| static QString App::DocInfo::getFullPath  | ( | const char *  | _p_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ hasXLink()

[bool](../../d9/db9/classbool.html) App::DocInfo::hasXLink  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |  const  
---|---|---|---|---|---  
  
References
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777).

## ◆ init()

void App::DocInfo::init  | ( | DocInfoMap::iterator  | _pos_ ,   
---|---|---|---  
|  | const char *  | _objName_ ,   
|  | [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) *  | _l_  
| ) | |   
  
References
[attach()](../../d7/d23/classApp_1_1DocInfo.html#abfdf47204bf7a84f4d19f3a04c5a4199),
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[connDeleteDocument](../../d7/d23/classApp_1_1DocInfo.html#a5affea3e5e1af4c72fff43ad7d7d066f),
[connFinishRestoreDocument](../../d7/d23/classApp_1_1DocInfo.html#aa3cf9a04d67a6c00ff073fb94872e975),
[connPendingReloadDocument](../../d7/d23/classApp_1_1DocInfo.html#a67666267a55890c8ecc3e2e71951bedd),
[connSaveDocument](../../d7/d23/classApp_1_1DocInfo.html#a7a7e1279c2afd7c33a3c002ae10d6390),
[filePath()](../../d7/d23/classApp_1_1DocInfo.html#a734562de80859a471b972373316295a7),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[getFullPath()](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7),
[App::PropertyLinkBase::LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45),
[myPath](../../d7/d23/classApp_1_1DocInfo.html#a07503c453981a0de2a8e9a4331618b73),
[myPos](../../d7/d23/classApp_1_1DocInfo.html#a70fe9f14dcfa154b6ff85d8b90d87e2f),
[App::Document::PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[slotDeleteDocument()](../../d7/d23/classApp_1_1DocInfo.html#ac304ec8dca7b41f324f00c05df2702f0),
[slotFinishRestoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#a267d94a9a178b9aff702ce8588a617f8),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

Referenced by
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ remove()

void App::DocInfo::remove  | ( | [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) *  | _l_| ) |   
---|---|---|---|---|---  
  
References
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
and
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777).

## ◆ restoreDocument()

| static void App::DocInfo::restoreDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
static  
  
References
[getFullPath()](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7).

Referenced by
[App::PropertyXLink::restoreDocument()](../../d2/de2/classApp_1_1PropertyXLink.html#a5ef57584d28afeba3785b8d5dada73b5).

## ◆ slotDeleteDocument()

void App::DocInfo::slotDeleteDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
References
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
[App::PropertyLinkBase::LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da),
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777),
and
[pcDoc](../../d7/d23/classApp_1_1DocInfo.html#a4bee0e66d2dc16f678619500f28fd723).

Referenced by
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

## ◆ slotFinishRestoreDocument()

void App::DocInfo::slotFinishRestoreDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
References
[attach()](../../d7/d23/classApp_1_1DocInfo.html#abfdf47204bf7a84f4d19f3a04c5a4199),
[getFullPath()](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7),
and
[pcDoc](../../d7/d23/classApp_1_1DocInfo.html#a4bee0e66d2dc16f678619500f28fd723).

Referenced by
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

## ◆ slotSaveDocument()

void App::DocInfo::slotSaveDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
References
[get()](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a),
[App::DocumentObject::getFullName()](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
[getFullPath()](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7),
[links](../../d7/d23/classApp_1_1DocInfo.html#a414d056dd4df8a82893750a9b1bba777),
[myPos](../../d7/d23/classApp_1_1DocInfo.html#a70fe9f14dcfa154b6ff85d8b90d87e2f),
[pcDoc](../../d7/d23/classApp_1_1DocInfo.html#a4bee0e66d2dc16f678619500f28fd723),
[slotDeleteDocument()](../../d7/d23/classApp_1_1DocInfo.html#ac304ec8dca7b41f324f00c05df2702f0),
and
[slotFinishRestoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#a267d94a9a178b9aff702ce8588a617f8).

Referenced by
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## Member Data Documentation

## ◆ connDeletedObject

[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)
App::DocInfo::connDeletedObject  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef).

## ◆ connDeleteDocument

[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)
App::DocInfo::connDeleteDocument  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
and
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## ◆ connFinishRestoreDocument

[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)
App::DocInfo::connFinishRestoreDocument  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
and
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## ◆ connPendingReloadDocument

[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)
App::DocInfo::connPendingReloadDocument  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
and
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## ◆ connSaveDocument

[Connection](../../d7/d23/classApp_1_1DocInfo.html#a44c7db086a7dce7f6057c1ccd272bc60)
App::DocInfo::connSaveDocument  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
and
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## ◆ links

std::set<[PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html)*>
App::DocInfo::links  
---  
  
Referenced by
[attach()](../../d7/d23/classApp_1_1DocInfo.html#abfdf47204bf7a84f4d19f3a04c5a4199),
[breakLinks()](../../d7/d23/classApp_1_1DocInfo.html#a9eeca81cb964af7cf2d763d2ae31e199),
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
[hasXLink()](../../d7/d23/classApp_1_1DocInfo.html#a8f86a3a1a64a037d53f9b66c7f01e3c4),
[remove()](../../d7/d23/classApp_1_1DocInfo.html#af2d96170c638014561077c6f58af9f98),
[slotDeleteDocument()](../../d7/d23/classApp_1_1DocInfo.html#ac304ec8dca7b41f324f00c05df2702f0),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

## ◆ myPath

std::string App::DocInfo::myPath  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
[filePath()](../../d7/d23/classApp_1_1DocInfo.html#a734562de80859a471b972373316295a7),
and
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca).

## ◆ myPos

DocInfoMap::iterator App::DocInfo::myPos  
---  
  
Referenced by
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
[getFullPath()](../../d7/d23/classApp_1_1DocInfo.html#a926217bf2eed05ad4c00ada228d14eb7),
[init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

## ◆ pcDoc

[App::Document](../../d8/d3e/classApp_1_1Document.html)* App::DocInfo::pcDoc  
---  
  
Referenced by
[attach()](../../d7/d23/classApp_1_1DocInfo.html#abfdf47204bf7a84f4d19f3a04c5a4199),
[deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
[slotDeleteDocument()](../../d7/d23/classApp_1_1DocInfo.html#ac304ec8dca7b41f324f00c05df2702f0),
[slotFinishRestoreDocument()](../../d7/d23/classApp_1_1DocInfo.html#a267d94a9a178b9aff702ce8588a617f8),
and
[slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/PropertyLinks.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

