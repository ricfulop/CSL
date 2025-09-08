---
url: https://freecad.github.io/SourceDoc/d5/d07/classApp_1_1DocumentObjectT.html
scraped_at: 2025-09-08T14:54:23.465436
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html)

[List of all members](../../d5/d51/classApp_1_1DocumentObjectT-members.html) | Public Member Functions

App::DocumentObjectT Class Reference

The [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html "The
DocumentObjectT class is a helper class to store the names of a document
object and its document.") class is a helper class to store the names of a
document object and its document.
[More...](../../d5/d07/classApp_1_1DocumentObjectT.html#details)

`#include <DocumentObserver.h>`

##  Public Member Functions  
  
---  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#a468d5d841ba45cba78a3527cc01e04d2)
()  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#a074600b90f83edc336212d7e02a1ab32)
(const char *docName, const char *objName)  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#a6507767f3e4fdbe93a7dc3468e353ab7)
(const [Document](../../d8/d3e/classApp_1_1Document.html) *, const std::string
&objName)  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#a33c59e6e1c75215ef3bad4646c35418f)
(const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#ac9e6f240db7e8367eb74ca1bbd941f19)
(const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &)  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#a9a16b7c1b1452c9d742044e5bda6e616)
(const [Property](../../d0/da9/classApp_1_1Property.html) *)  
|
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6afcac6fac9a081c8db420dbb01a877)
([DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &&)  
[Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../d5/d07/classApp_1_1DocumentObjectT.html#acadd08abfd3a0d947b8047ab70d4eb31) () const  
const std::string & | [getDocumentName](../../d5/d07/classApp_1_1DocumentObjectT.html#ac83a9c2caeb3bdeaff17c36cea7fbadc) () const  
std::string | [getDocumentPython](../../d5/d07/classApp_1_1DocumentObjectT.html#afa6813cdce35b36f1a28d4c11076f904) () const  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getObject](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b) () const  
template<typename T >  
T * | [getObjectAs](../../d5/d07/classApp_1_1DocumentObjectT.html#a46aea9b385359f08a6fba6ce75271ab2) () const  
const std::string & | [getObjectLabel](../../d5/d07/classApp_1_1DocumentObjectT.html#a2a011c1051aa0b846062711a8f7f142c) () const  
const std::string & | [getObjectName](../../d5/d07/classApp_1_1DocumentObjectT.html#a9c1f9b8511580a7ce10345531963d6b1) () const  
std::string | [getObjectPython](../../d5/d07/classApp_1_1DocumentObjectT.html#a763d2972bd0e3618d65bd52a17aeb90a) () const  
[Property](../../d0/da9/classApp_1_1Property.html) * | [getProperty](../../d5/d07/classApp_1_1DocumentObjectT.html#acc26a36e5ea30cddb7c648355310af33) () const  
template<typename T >  
T * | [getPropertyAs](../../d5/d07/classApp_1_1DocumentObjectT.html#af4777517ffbe6d04724b1e42bedf5dfa) () const  
const std::string & | [getPropertyName](../../d5/d07/classApp_1_1DocumentObjectT.html#a114f4f9fa39a507c3b3ad793c0c8b346) () const  
std::string | [getPropertyPython](../../d5/d07/classApp_1_1DocumentObjectT.html#a55a57c49dfe3c44f190eac7a382cf383) () const  
void | [operator=](../../d5/d07/classApp_1_1DocumentObjectT.html#a47562177ef9ee1f7c0277966364a064f) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | [operator=](../../d5/d07/classApp_1_1DocumentObjectT.html#ac9d1b8ac237975caa91a1262a30d3f5e) (const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &)  
void | [operator=](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | [operator=](../../d5/d07/classApp_1_1DocumentObjectT.html#a43092ac909db57e859c9a45bcc323ea3) ([DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &&)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d5/d07/classApp_1_1DocumentObjectT.html#ae3678e71addb2d8e9e65805dde558c38) (const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &) const  
|
[~DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html#aa958730299eb76af1ca3b55c6e336971)
()  
  
## Detailed Description

The [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html "The
DocumentObjectT class is a helper class to store the names of a document
object and its document.") class is a helper class to store the names of a
document object and its document.

This can be useful when you cannot rely on that the document or the object
still exists when you have to access it.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ DocumentObjectT() [1/7]

DocumentObjectT::DocumentObjectT  | ( | | ) |   
---|---|---|---|---  
  
Constructor

## ◆ DocumentObjectT() [2/7]

DocumentObjectT::DocumentObjectT  | ( | const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | _other_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ DocumentObjectT() [3/7]

DocumentObjectT::DocumentObjectT  | ( | [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) && | _other_| ) |   
---|---|---|---|---|---  
  
Constructor

References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ DocumentObjectT() [4/7]

DocumentObjectT::DocumentObjectT  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ DocumentObjectT() [5/7]

DocumentObjectT::DocumentObjectT  | ( | const [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ ,   
---|---|---|---  
|  | const std::string & | _objName_  
| ) | |   
  
Constructor

## ◆ DocumentObjectT() [6/7]

DocumentObjectT::DocumentObjectT  | ( | const char *  | _docName_ ,   
---|---|---|---  
|  | const char *  | _objName_  
| ) | |   
  
Constructor

## ◆ DocumentObjectT() [7/7]

DocumentObjectT::DocumentObjectT  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ ~DocumentObjectT()

DocumentObjectT::~DocumentObjectT  | ( | | ) |   
---|---|---|---|---  
  
Destructor

## Member Function Documentation

## ◆ getDocument()

[Document](../../d8/d3e/classApp_1_1Document.html) * DocumentObjectT::getDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get a pointer to the document or 0 if it doesn't exist any more.

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
and
[App::Application::getDocument()](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d).

Referenced by
[getObject()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b),
[App::SubObjectT::getObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f),
[App::SubObjectT::getSubObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f),
and
[Gui::PropertyEditor::PropertyLinkItem::toString()](../../d7/d66/classGui_1_1PropertyEditor_1_1PropertyLinkItem.html#a4172d8d52560f288bdea837ecd7bfecb).

## ◆ getDocumentName()

const std::string & DocumentObjectT::getDocumentName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the name of the document.

Referenced by
[App::SubObjectT::getObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f),
[App::SubObjectT::getSubObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f),
[App::SubObjectT::operator<()](../../dd/d78/classApp_1_1SubObjectT.html#a9e5227eb83787cebacdd673eac2662af),
and
[Gui::PropertyEditor::LinkSelection::select()](../../d9/d3f/classGui_1_1PropertyEditor_1_1LinkSelection.html#a38e017ceb21ec3a0dcbda17270b43135).

## ◆ getDocumentPython()

std::string DocumentObjectT::getDocumentPython  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document as Python command.

Referenced by
[ReenGui::FitBSplineSurfaceWidget::accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
and
[ReenGui::PoissonWidget::accept()](../../d7/dae/classReenGui_1_1PoissonWidget.html#a947b3b6b4d87c7a8ca5429c9bef3de2e).

## ◆ getObject()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * DocumentObjectT::getObject  | ( | | ) |  const  
---|---|---|---|---  
  
Get a pointer to the document object or 0 if it doesn't exist any more.

References
[getDocument()](../../d5/d07/classApp_1_1DocumentObjectT.html#acadd08abfd3a0d947b8047ab70d4eb31).

Referenced by
[Gui::TaskCSysDragger::accept()](../../d2/dff/classGui_1_1TaskCSysDragger.html#ad513cbcf32b69dc11ee35b96cc6a2a64),
[Gui::Dialog::DlgPropertyLink::formatObject()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#ad29b80daf8e70d7794b2fd852c9c8c6c),
[App::SubObjectT::getNewElementName()](../../dd/d78/classApp_1_1SubObjectT.html#a3f4df581957c8dbc1ffaee6d315ea452),
[App::SubObjectT::getOldElementName()](../../dd/d78/classApp_1_1SubObjectT.html#a91100833ef50109008ae5deff6cd2441),
[getProperty()](../../d5/d07/classApp_1_1DocumentObjectT.html#acc26a36e5ea30cddb7c648355310af33),
[App::SubObjectT::getSubObject()](../../dd/d78/classApp_1_1SubObjectT.html#a7d6d7046e2ca49c3858cb0659bbcaa00),
[App::SubObjectT::getSubObjectList()](../../dd/d78/classApp_1_1SubObjectT.html#af22223aa847f2b41aa9fa72916bff3d9),
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
[Gui::PropertyEditor::LinkLabel::updatePropertyLink()](../../d5/d5f/classGui_1_1PropertyEditor_1_1LinkLabel.html#a444c666ddd0929725b1cea41510868a2),
and
[MeshPartGui::Mesh2ShapeGmsh::writeProject()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a3931d67654b40d307417d697e6291ab3).

## ◆ getObjectAs()

template<typename T >

T * App::DocumentObjectT::getObjectAs  | ( | | ) |  const  
---|---|---|---|---  
  
Get a pointer to the document or 0 if it doesn't exist any more or the type
doesn't match.

## ◆ getObjectLabel()

const std::string & DocumentObjectT::getObjectLabel  | ( | | ) |  const  
---|---|---|---|---  
  
Get the label of the document object.

Referenced by
[App::SubObjectT::getObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f).

## ◆ getObjectName()

const std::string & DocumentObjectT::getObjectName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the name of the document object.

Referenced by
[App::SubObjectT::getObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f),
[App::SubObjectT::getSubObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f),
[Gui::SelectionSingleton::hasPreselection()](../../d4/dca/classGui_1_1SelectionSingleton.html#aac3d528f216f4534f5962e2723de7971),
[App::SubObjectT::operator<()](../../dd/d78/classApp_1_1SubObjectT.html#a9e5227eb83787cebacdd673eac2662af),
[Gui::PropertyEditor::LinkSelection::select()](../../d9/d3f/classGui_1_1PropertyEditor_1_1LinkSelection.html#a38e017ceb21ec3a0dcbda17270b43135),
and
[Gui::SelectionSingleton::setPreselectCoord()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab221ec4315e6968c08b10785fc03b85a).

## ◆ getObjectPython()

std::string DocumentObjectT::getObjectPython  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document object as Python command.

Referenced by
[ReenGui::FitBSplineSurfaceWidget::accept()](../../d9/d48/classReenGui_1_1FitBSplineSurfaceWidget.html#af94ddfaebc20a805f34a94face578ce6),
[ReenGui::PoissonWidget::accept()](../../d7/dae/classReenGui_1_1PoissonWidget.html#a947b3b6b4d87c7a8ca5429c9bef3de2e),
[getPropertyPython()](../../d5/d07/classApp_1_1DocumentObjectT.html#a55a57c49dfe3c44f190eac7a382cf383),
[App::SubObjectT::getSubObjectPython()](../../dd/d78/classApp_1_1SubObjectT.html#afc63dfe396a3a3cbd15a0b421df53662),
and
[App::PropertyLinkT::PropertyLinkT()](../../db/d5d/classApp_1_1PropertyLinkT.html#a1e66edc5b32ff238cc1f7b99e15c85f8).

## ◆ getProperty()

[Property](../../d0/da9/classApp_1_1Property.html) * DocumentObjectT::getProperty  | ( | | ) |  const  
---|---|---|---|---  
  
Get a pointer to the property or 0 if it doesn't exist any more.

References
[getObject()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b).

Referenced by
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
and
[Gui::PropertyEditor::LinkLabel::updatePropertyLink()](../../d5/d5f/classGui_1_1PropertyEditor_1_1LinkLabel.html#a444c666ddd0929725b1cea41510868a2).

## ◆ getPropertyAs()

template<typename T >

T * App::DocumentObjectT::getPropertyAs  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getPropertyName()

const std::string & DocumentObjectT::getPropertyName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the name of the property.

Referenced by
[App::SubObjectT::operator<()](../../dd/d78/classApp_1_1SubObjectT.html#a9e5227eb83787cebacdd673eac2662af).

## ◆ getPropertyPython()

std::string DocumentObjectT::getPropertyPython  | ( | | ) |  const  
---|---|---|---|---  
  
Get the property as Python command.

References
[getObjectPython()](../../d5/d07/classApp_1_1DocumentObjectT.html#a763d2972bd0e3618d65bd52a17aeb90a).

## ◆ operator=() [1/4]

void DocumentObjectT::operator=  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [2/4]

[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & DocumentObjectT::operator=  | ( | const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | _obj_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [3/4]

void DocumentObjectT::operator=  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
  
Assignment operator

References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::Property::hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

## ◆ operator=() [4/4]

[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & DocumentObjectT::operator=  | ( | [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) && | _obj_| ) |   
---|---|---|---|---|---  
  
Assignment operator

References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) DocumentObjectT::operator==  | ( | const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Equality operator

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObserver.h
  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

