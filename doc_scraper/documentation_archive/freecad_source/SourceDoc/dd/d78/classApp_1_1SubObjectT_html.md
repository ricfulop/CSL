---
url: https://freecad.github.io/SourceDoc/dd/d78/classApp_1_1SubObjectT.html
scraped_at: 2025-09-08T14:57:07.100961
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html)

[List of all members](../../d7/dee/classApp_1_1SubObjectT-members.html) | Public Member Functions

App::SubObjectT Class Reference

`#include <DocumentObserver.h>`

##  Public Member Functions  
  
---  
const char * | [getElementName](../../dd/d78/classApp_1_1SubObjectT.html#a54662cbfb806ba3b9b20223d97561d14) () const  
| Return the sub-element ([Face](../../d3/db7/classFace.html), Edge, etc) of
the subname path.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a54662cbfb806ba3b9b20223d97561d14)  
  
std::string | [getNewElementName](../../dd/d78/classApp_1_1SubObjectT.html#a3f4df581957c8dbc1ffaee6d315ea452) () const  
| Return the new style sub-element name.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a3f4df581957c8dbc1ffaee6d315ea452)  
  
std::string | [getObjectFullName](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f) (const char *docName=nullptr) const  
| Return docname::objname (label)
[More...](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f)  
  
std::string | [getOldElementName](../../dd/d78/classApp_1_1SubObjectT.html#a91100833ef50109008ae5deff6cd2441) ([int](../../d1/da0/classint.html) *index=nullptr) const  
| Return the old style sub-element name.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a91100833ef50109008ae5deff6cd2441)  
  
const std::string & | [getSubName](../../dd/d78/classApp_1_1SubObjectT.html#af7ab54a6c3930aefce99af00675eef73) () const  
| Return the subname path.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#af7ab54a6c3930aefce99af00675eef73)  
  
std::string | [getSubNameNoElement](../../dd/d78/classApp_1_1SubObjectT.html#a8a78b0a5a01228944e273735f9535073) () const  
| Return the subname path without sub-element.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a8a78b0a5a01228944e273735f9535073)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getSubObject](../../dd/d78/classApp_1_1SubObjectT.html#a7d6d7046e2ca49c3858cb0659bbcaa00) () const  
| Return the sub-object.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a7d6d7046e2ca49c3858cb0659bbcaa00)  
  
std::string | [getSubObjectFullName](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f) (const char *docName=nullptr) const  
| Return docname::objname.subname (label)
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getSubObjectList](../../dd/d78/classApp_1_1SubObjectT.html#af22223aa847f2b41aa9fa72916bff3d9) () const  
| Return all objects along the subname path.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#af22223aa847f2b41aa9fa72916bff3d9)  
  
std::string | [getSubObjectPython](../../dd/d78/classApp_1_1SubObjectT.html#afc63dfe396a3a3cbd15a0b421df53662) ([bool](../../d9/db9/classbool.html) force=true) const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dd/d78/classApp_1_1SubObjectT.html#a9e5227eb83787cebacdd673eac2662af) (const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) &other) const  
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | [operator=](../../dd/d78/classApp_1_1SubObjectT.html#a06177251efc4972bba1d9af6af40c1c8) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | [operator=](../../dd/d78/classApp_1_1SubObjectT.html#a3f765fdd3d3345d1ce739a429e4af11f) (const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &)  
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | [operator=](../../dd/d78/classApp_1_1SubObjectT.html#a62b09c25e6b691b816b926ac419fa993) (const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) &)  
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | [operator=](../../dd/d78/classApp_1_1SubObjectT.html#a783148f9c5cd3c7d9019c933c63ca212) ([SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) &&)  
[bool](../../d9/db9/classbool.html) | [operator==](../../dd/d78/classApp_1_1SubObjectT.html#a792fc0923b616ec694e1eeb3903e5e62) (const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) &) const  
void | [setSubName](../../dd/d78/classApp_1_1SubObjectT.html#aa221cb881d4cb67c566ed2266e3ccd40) (const char *subname)  
| Set the subname path to the sub-object.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#aa221cb881d4cb67c566ed2266e3ccd40)  
  
void | [setSubName](../../dd/d78/classApp_1_1SubObjectT.html#a8928134e23495cd69e078a18f22c8280) (const std::string &subname)  
| Set the subname path to the sub-object.
[More...](../../dd/d78/classApp_1_1SubObjectT.html#a8928134e23495cd69e078a18f22c8280)  
  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#accbf91de44a3f6cbea5c43748ce04f08)
()  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#a8fa58fed13019ca5e05c0f4b24aceb6a)
(const char *docName, const char *objName, const char *subname)  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#a591ccc7a2fc5016e7e631475850237c4)
(const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#a56d955bfdee86aa2a713e22b0618accd)
(const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const
char *subname)  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#a705f49dded97e954f2f162953d652368)
(const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) &obj,
const char *subname)  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#a3b36871f51f05a9159c779441fd8e8f7)
(const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) &)  
|
[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html#aec8485634284bca285120afc96b64d55)
([SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) &&)  
![-](../../closed.png) Public Member Functions inherited from
[App::DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html)  
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
  
## Constructor & Destructor Documentation

## ◆ SubObjectT() [1/7]

SubObjectT::SubObjectT  | ( | | ) |   
---|---|---|---|---  
  
Constructor

## ◆ SubObjectT() [2/7]

SubObjectT::SubObjectT  | ( | const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | _other_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ SubObjectT() [3/7]

SubObjectT::SubObjectT  | ( | [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) && | _other_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ SubObjectT() [4/7]

SubObjectT::SubObjectT  | ( | const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | _obj_ ,   
---|---|---|---  
|  | const char *  | _subname_  
| ) | |   
  
Constructor

## ◆ SubObjectT() [5/7]

SubObjectT::SubObjectT  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const char *  | _subname_  
| ) | |   
  
Constructor

## ◆ SubObjectT() [6/7]

SubObjectT::SubObjectT  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ SubObjectT() [7/7]

SubObjectT::SubObjectT  | ( | const char *  | _docName_ ,   
---|---|---|---  
|  | const char *  | _objName_ ,   
|  | const char *  | _subname_  
| ) | |   
  
Constructor

## Member Function Documentation

## ◆ getElementName()

const char * SubObjectT::getElementName  | ( | | ) |  const  
---|---|---|---|---  
  
Return the sub-element ([Face](../../d3/db7/classFace.html), Edge, etc) of the
subname path.

References
[Data::ComplexGeoData::findElementName()](../../d8/daf/classData_1_1ComplexGeoData.html#a7a2ff773f05abdf81ee7194a81788085).

## ◆ getNewElementName()

std::string SubObjectT::getNewElementName  | ( | | ) |  const  
---|---|---|---|---  
  
Return the new style sub-element name.

References
[App::DocumentObjectT::getObject()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[App::GeoFeature::resolveElement()](../../d7/d75/classApp_1_1GeoFeature.html#aef8b2a9f75e796e56f7921d93b2f2a8a).

## ◆ getObjectFullName()

std::string SubObjectT::getObjectFullName  | ( | const char *  | _docName_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
Return docname::objname (label)

Parameters

     docName| optional document name. The document prefix will only be printed if it is different then the given 'doc'.   
---|---  
  
References
[App::DocumentObjectT::getDocument()](../../d5/d07/classApp_1_1DocumentObjectT.html#acadd08abfd3a0d947b8047ab70d4eb31),
[App::DocumentObjectT::getDocumentName()](../../d5/d07/classApp_1_1DocumentObjectT.html#ac83a9c2caeb3bdeaff17c36cea7fbadc),
[App::DocumentObjectT::getObjectLabel()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2a011c1051aa0b846062711a8f7f142c),
and
[App::DocumentObjectT::getObjectName()](../../d5/d07/classApp_1_1DocumentObjectT.html#a9c1f9b8511580a7ce10345531963d6b1).

Referenced by
[getSubObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f).

## ◆ getOldElementName()

std::string SubObjectT::getOldElementName  | ( | [int](../../d1/da0/classint.html) *  | _index_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
Return the old style sub-element name.

Parameters

     index| if given, then return the element type, and extract the index   
---|---  
  
References
[App::DocumentObjectT::getObject()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[App::GeoFeature::resolveElement()](../../d7/d75/classApp_1_1GeoFeature.html#aef8b2a9f75e796e56f7921d93b2f2a8a).

## ◆ getSubName()

const std::string & SubObjectT::getSubName  | ( | | ) |  const  
---|---|---|---|---  
  
Return the subname path.

Referenced by
[Gui::Dialog::DlgPropertyLink::formatObject()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#ad29b80daf8e70d7794b2fd852c9c8c6c),
[operator<()](../../dd/d78/classApp_1_1SubObjectT.html#a9e5227eb83787cebacdd673eac2662af),
[Gui::PropertyEditor::LinkSelection::select()](../../d9/d3f/classGui_1_1PropertyEditor_1_1LinkSelection.html#a38e017ceb21ec3a0dcbda17270b43135),
[Gui::SelectionSingleton::slotSelectionChanged()](../../d4/dca/classGui_1_1SelectionSingleton.html#ae0bb1709723ef769a331ac020f67d7b0),
and
[MeshPartGui::Mesh2ShapeGmsh::writeProject()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a3931d67654b40d307417d697e6291ab3).

## ◆ getSubNameNoElement()

std::string SubObjectT::getSubNameNoElement  | ( | | ) |  const  
---|---|---|---|---  
  
Return the subname path without sub-element.

References
[Data::ComplexGeoData::noElementName()](../../d8/daf/classData_1_1ComplexGeoData.html#ac39f368821b707f9d7140a6eea7f830f).

## ◆ getSubObject()

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * SubObjectT::getSubObject  | ( | | ) |  const  
---|---|---|---|---  
  
Return the sub-object.

References
[App::DocumentObjectT::getObject()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b).

Referenced by
[getSubObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#a1fb35960eb3388e452f8a8445008569f),
and
[Gui::PropertyEditor::LinkSelection::select()](../../d9/d3f/classGui_1_1PropertyEditor_1_1LinkSelection.html#a38e017ceb21ec3a0dcbda17270b43135).

## ◆ getSubObjectFullName()

std::string SubObjectT::getSubObjectFullName  | ( | const char *  | _docName_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
Return docname::objname.subname (label)

Parameters

     doc| optional document name. The document prefix will only be printed if it is different then the given 'doc'.   
---|---  
  
References
[App::DocumentObjectT::getDocument()](../../d5/d07/classApp_1_1DocumentObjectT.html#acadd08abfd3a0d947b8047ab70d4eb31),
[App::DocumentObjectT::getDocumentName()](../../d5/d07/classApp_1_1DocumentObjectT.html#ac83a9c2caeb3bdeaff17c36cea7fbadc),
[getObjectFullName()](../../dd/d78/classApp_1_1SubObjectT.html#ac857b0185124c8489310a5e6c22b9e4f),
[App::DocumentObjectT::getObjectName()](../../d5/d07/classApp_1_1DocumentObjectT.html#a9c1f9b8511580a7ce10345531963d6b1),
and
[getSubObject()](../../dd/d78/classApp_1_1SubObjectT.html#a7d6d7046e2ca49c3858cb0659bbcaa00).

## ◆ getSubObjectList()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > SubObjectT::getSubObjectList  | ( | | ) |  const  
---|---|---|---|---  
  
Return all objects along the subname path.

References
[App::DocumentObjectT::getObject()](../../d5/d07/classApp_1_1DocumentObjectT.html#a2e783029b254d6a99d500987e3d5b28b).

## ◆ getSubObjectPython()

std::string SubObjectT::getSubObjectPython  | ( | [bool](../../d9/db9/classbool.html) | _force_ = `true`| ) |  const  
---|---|---|---|---|---  
  
References
[Base::Tools::escapedUnicodeFromUtf8()](../../d6/dda/structBase_1_1Tools.html#a2cfe13d9b5c340ec5dc8a7b34fff8645),
and
[App::DocumentObjectT::getObjectPython()](../../d5/d07/classApp_1_1DocumentObjectT.html#a763d2972bd0e3618d65bd52a17aeb90a).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) SubObjectT::operator< | ( | const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
References
[App::DocumentObjectT::getDocumentName()](../../d5/d07/classApp_1_1DocumentObjectT.html#ac83a9c2caeb3bdeaff17c36cea7fbadc),
[App::DocumentObjectT::getObjectName()](../../d5/d07/classApp_1_1DocumentObjectT.html#a9c1f9b8511580a7ce10345531963d6b1),
[App::DocumentObjectT::getPropertyName()](../../d5/d07/classApp_1_1DocumentObjectT.html#a114f4f9fa39a507c3b3ad793c0c8b346),
and
[getSubName()](../../dd/d78/classApp_1_1SubObjectT.html#af7ab54a6c3930aefce99af00675eef73).

## ◆ operator=() [1/4]

[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & SubObjectT::operator=  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _other_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [2/4]

[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & SubObjectT::operator=  | ( | const [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) & | _other_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [3/4]

[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & SubObjectT::operator=  | ( | const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | _other_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [4/4]

[SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & SubObjectT::operator=  | ( | [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) && | _other_| ) |   
---|---|---|---|---|---  
  
Assignment operator

References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) SubObjectT::operator==  | ( | const [SubObjectT](../../dd/d78/classApp_1_1SubObjectT.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Equality operator

## ◆ setSubName() [1/2]

void SubObjectT::setSubName  | ( | const char *  | _subname_| ) |   
---|---|---|---|---|---  
  
Set the subname path to the sub-object.

Referenced by
[Gui::SelectionSingleton::slotSelectionChanged()](../../d4/dca/classGui_1_1SelectionSingleton.html#ae0bb1709723ef769a331ac020f67d7b0).

## ◆ setSubName() [2/2]

void App::SubObjectT::setSubName  | ( | const std::string & | _subname_| ) |   
---|---|---|---|---|---  
  
Set the subname path to the sub-object.

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObserver.h
  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

