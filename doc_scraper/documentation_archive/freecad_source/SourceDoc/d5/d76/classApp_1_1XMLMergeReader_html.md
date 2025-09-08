---
url: https://freecad.github.io/SourceDoc/d5/d76/classApp_1_1XMLMergeReader.html
scraped_at: 2025-09-08T14:57:22.190213
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [XMLMergeReader](../../d5/d76/classApp_1_1XMLMergeReader.html)

[List of all members](../../d7/d0d/classApp_1_1XMLMergeReader-members.html) | Public Member Functions

App::XMLMergeReader Class Reference

##  Public Member Functions  
  
---  
void | [addName](../../d5/d76/classApp_1_1XMLMergeReader.html#aaa60a28ad48675faa89dc03e8858b204) (const char *s1, const char *s2)  
[bool](../../d9/db9/classbool.html) | [doNameMapping](../../d5/d76/classApp_1_1XMLMergeReader.html#a2248ef49970d1203f48c6c04e2893a84) () const  
const char * | [getName](../../d5/d76/classApp_1_1XMLMergeReader.html#ab6451493700a993be1f241b745709b64) (const char *name) const  
|
[XMLMergeReader](../../d5/d76/classApp_1_1XMLMergeReader.html#a2329942baaff929440403ab77c803135)
(std::map< std::string, std::string > &name, const char *FileName,
std::istream &[str](../../d9/d36/classstr.html))  
![-](../../closed.png) Public Member Functions inherited from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)  
[bool](../../d9/db9/classbool.html) | [isValid](../../dc/d95/classBase_1_1XMLReader.html#a8104be87d837faa87cfc73aeaa6fe7ed) () const  
[bool](../../d9/db9/classbool.html) | [isVerbose](../../dc/d95/classBase_1_1XMLReader.html#a89fa30d380593281c1e22864653a8b0a) () const  
void | [setVerbose](../../dc/d95/classBase_1_1XMLReader.html#aaea2a3e84a2f7c2dc22bf4d66bf2c6f4) ([bool](../../d9/db9/classbool.html) on)  
|
[XMLReader](../../dc/d95/classBase_1_1XMLReader.html#a99f834c210330c8cb20eaf5e2e74f8d7)
(const char *FileName, std::istream &)  
| open the file and read the first element
[More...](../../dc/d95/classBase_1_1XMLReader.html#a99f834c210330c8cb20eaf5e2e74f8d7)  
  
|
[~XMLReader](../../dc/d95/classBase_1_1XMLReader.html#a22df0cabc0d0237cd5d65e84cc2b0307)
()  
const char * | [localName](../../dc/d95/classBase_1_1XMLReader.html#a03caf199f35d2c0cc744743c2dc0f8ae) () const  
| get the local name of the current Element
[More...](../../dc/d95/classBase_1_1XMLReader.html#a03caf199f35d2c0cc744743c2dc0f8ae)  
  
[int](../../d1/da0/classint.html) | [level](../../dc/d95/classBase_1_1XMLReader.html#a9ec34bbba5e4b1f8e747bf502fa643e3) () const  
| get the current element level
[More...](../../dc/d95/classBase_1_1XMLReader.html#a9ec34bbba5e4b1f8e747bf502fa643e3)  
  
void | [readElement](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e) (const char *ElementName=nullptr)  
| read until a start element is found (<name>) or start-end element (<name/>)
(with special name if given)
[More...](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e)  
  
void | [readEndElement](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3) (const char *ElementName=nullptr, [int](../../d1/da0/classint.html) [level](../../d1/da0/classint.html)=-1)  
| read until an end element is found
[More...](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3)  
  
void | [readCharacters](../../dc/d95/classBase_1_1XMLReader.html#ac1ec77dd8039d43f47934fd784301753) ()  
| read until characters are found
[More...](../../dc/d95/classBase_1_1XMLReader.html#ac1ec77dd8039d43f47934fd784301753)  
  
void | [readBinFile](../../dc/d95/classBase_1_1XMLReader.html#a9c7fc15570f69a6db6e1961770928912) (const char *)  
| read binary file
[More...](../../dc/d95/classBase_1_1XMLReader.html#a9c7fc15570f69a6db6e1961770928912)  
  
unsigned [int](../../d1/da0/classint.html) | [getAttributeCount](../../dc/d95/classBase_1_1XMLReader.html#a7e1e8be82f67c2dcc0bdb8e8145a4163) () const  
| get the number of attributes of the current element
[More...](../../dc/d95/classBase_1_1XMLReader.html#a7e1e8be82f67c2dcc0bdb8e8145a4163)  
  
[bool](../../d9/db9/classbool.html) | [hasAttribute](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910) (const char *AttrName) const  
| check if the read element has a special attribute
[More...](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910)  
  
long | [getAttributeAsInteger](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c) (const char *AttrName) const  
| return the named attribute as an interer (does type checking)
[More...](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c)  
  
unsigned long | [getAttributeAsUnsigned](../../dc/d95/classBase_1_1XMLReader.html#ac384789d0b975c7caee3762a236d951c) (const char *AttrName) const  
double | [getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820) (const char *AttrName) const  
| return the named attribute as a double floating point (does type checking)
[More...](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820)  
  
const char * | [getAttribute](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788) (const char *AttrName) const  
| return the named attribute as a double floating point (does type checking)
[More...](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788)  
  
const char * | [addFile](../../dc/d95/classBase_1_1XMLReader.html#adf371fa6365af1b80097055bebf87dfe) (const char *Name, [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *Object)  
| add a read request of a persistent object
[More...](../../dc/d95/classBase_1_1XMLReader.html#adf371fa6365af1b80097055bebf87dfe)  
  
void | [readFiles](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16) ([zipios::ZipInputStream](../../d0/d1f/classzipios_1_1ZipInputStream.html) &zipstream) const  
| process the requested file writes
[More...](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16)  
  
const std::vector< std::string > & | [getFilenames](../../dc/d95/classBase_1_1XMLReader.html#a87e7f17434d9bc50694df12d10ee3510) () const  
| get all registered file names
[More...](../../dc/d95/classBase_1_1XMLReader.html#a87e7f17434d9bc50694df12d10ee3510)  
  
[bool](../../d9/db9/classbool.html) | [isRegistered](../../dc/d95/classBase_1_1XMLReader.html#a549e35a938c26907745f6cb8bc5c95f1) ([Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *Object) const  
void | [setPartialRestore](../../dc/d95/classBase_1_1XMLReader.html#adaf7e17e8787a7f2bc25ba0c62bbd389) ([bool](../../d9/db9/classbool.html) on)  
| sets simultaneously the global and local PartialRestore bits
[More...](../../dc/d95/classBase_1_1XMLReader.html#adaf7e17e8787a7f2bc25ba0c62bbd389)  
  
void | [clearPartialRestoreDocumentObject](../../dc/d95/classBase_1_1XMLReader.html#a050bbb542ef0f85cca44204fc1d961a2) ()  
void | [clearPartialRestoreProperty](../../dc/d95/classBase_1_1XMLReader.html#a3c89a7778a60cc6bc5709aa7e93d7bd4) ()  
void | [clearPartialRestoreObject](../../dc/d95/classBase_1_1XMLReader.html#a64cdb40adef67632889905988ce34e42) ()  
[bool](../../d9/db9/classbool.html) | [testStatus](../../dc/d95/classBase_1_1XMLReader.html#a1f076d2b8f0c7ff3257cfa6fc595c06c) ([ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50) pos) const  
| return the status bits
[More...](../../dc/d95/classBase_1_1XMLReader.html#a1f076d2b8f0c7ff3257cfa6fc595c06c)  
  
void | [setStatus](../../dc/d95/classBase_1_1XMLReader.html#aa424bc7428542103bf5324d28574bae4) ([ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50) pos, [bool](../../d9/db9/classbool.html) on)  
| set the status bits
[More...](../../dc/d95/classBase_1_1XMLReader.html#aa424bc7428542103bf5324d28574bae4)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)  
enum | [ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50) { [PartialRestore](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50aee244f56623eb5670c7219096835a52c) = 0 , [PartialRestoreInDocumentObject](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50a22ec7d4e78b150adbed3f2546a405e1e) = 1 , [PartialRestoreInProperty](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50a5d210453139b949521d6bc19d20732f9) = 2 , [PartialRestoreInObject](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50a18fabdd961603a12048f1bfdb670c7ef) = 3 }  
![-](../../closed.png) Public Attributes inherited from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)  
[int](../../d1/da0/classint.html) | [DocumentSchema](../../dc/d95/classBase_1_1XMLReader.html#a74af603513fa80d2be16b626f023223a)  
| Schema Version of the document.
[More...](../../dc/d95/classBase_1_1XMLReader.html#a74af603513fa80d2be16b626f023223a)  
  
std::string | [ProgramVersion](../../dc/d95/classBase_1_1XMLReader.html#a8de5cc0038e7b748554f9d82757e3c22)  
| Version of FreeCAD that wrote this document.
[More...](../../dc/d95/classBase_1_1XMLReader.html#a8de5cc0038e7b748554f9d82757e3c22)  
  
[int](../../d1/da0/classint.html) | [FileVersion](../../dc/d95/classBase_1_1XMLReader.html#aa1e0b79c86e73f829e400840f52eaadf)  
| Version of the file format.
[More...](../../dc/d95/classBase_1_1XMLReader.html#aa1e0b79c86e73f829e400840f52eaadf)  
  
std::vector< [FileEntry](../../d4/d0e/structBase_1_1XMLReader_1_1FileEntry.html) > | [FileList](../../dc/d95/classBase_1_1XMLReader.html#a633630eb9759529b190e5ea552d1d3f9)  
![-](../../closed.png) Protected Types inherited from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)  
enum | {   
}  
typedef std::map< std::string, std::string > | [AttrMapType](../../dc/d95/classBase_1_1XMLReader.html#a287bd21096c2d7f40616931b90be0c67)  
![-](../../closed.png) Protected Member Functions inherited from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)  
virtual void | [startDocument](../../dc/d95/classBase_1_1XMLReader.html#a81c1cb0a200a4249e973fe6b01a1a736) ()  
virtual void | [endDocument](../../dc/d95/classBase_1_1XMLReader.html#a1a330b1a0744588a97aadbd274048148) ()  
virtual void | [startElement](../../dc/d95/classBase_1_1XMLReader.html#aa99360f6d38f98f1c6f60d22ff055738) (const XMLCh *const uri, const XMLCh *const localname, const XMLCh *const qname, const XERCES_CPP_NAMESPACE_QUALIFIER Attributes &attrs)  
virtual void | [endElement](../../dc/d95/classBase_1_1XMLReader.html#aca0fa7593b57b5929f3d431b1d25ece9) (const XMLCh *const uri, const XMLCh *const localname, const XMLCh *const qname)  
virtual void | [characters](../../dc/d95/classBase_1_1XMLReader.html#a1f20264114d4c9f143831b7479417cbc) (const XMLCh *const chars, const XMLSize_t length)  
virtual void | [ignorableWhitespace](../../dc/d95/classBase_1_1XMLReader.html#aae2669227d3d5e1b70d0866e18dadd7c) (const XMLCh *const chars, const XMLSize_t length)  
virtual void | [startCDATA](../../dc/d95/classBase_1_1XMLReader.html#a058a241dc9cc900d24f7f1a7a83cf8a0) ()  
virtual void | [endCDATA](../../dc/d95/classBase_1_1XMLReader.html#aa6600b5e27fd64db2d8709d7116d6454) ()  
virtual void | [resetDocument](../../dc/d95/classBase_1_1XMLReader.html#a40996ed04a1bcccb7d61e4fe0d473304) ()  
void | [warning](../../dc/d95/classBase_1_1XMLReader.html#a8d030ff8ef85ae16aaefbf5635897c30) (const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException &exc)  
void | [error](../../dc/d95/classBase_1_1XMLReader.html#af7f902f8c2c83c9f7ca5286a213260d6) (const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException &exc)  
void | [fatalError](../../dc/d95/classBase_1_1XMLReader.html#a0f2f8688a7a6db9c41eac713496483f1) (const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException &exc)  
void | [resetErrors](../../dc/d95/classBase_1_1XMLReader.html#a4d701e3c554d9203142df4ea41be99dd) ()  
[bool](../../d9/db9/classbool.html) | [read](../../dc/d95/classBase_1_1XMLReader.html#af5fba875db7b1494423dc339fbeb425e) ()  
| read the next element
[More...](../../dc/d95/classBase_1_1XMLReader.html#af5fba875db7b1494423dc339fbeb425e)  
  
![-](../../closed.png) Protected Attributes inherited from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)  
[int](../../d1/da0/classint.html) | [Level](../../dc/d95/classBase_1_1XMLReader.html#a61492c7e83a48d2d741ece3a206247aa)  
std::string | [LocalName](../../dc/d95/classBase_1_1XMLReader.html#a3770f141f44ff81e21dacfe5820ad8ba)  
std::string | [Characters](../../dc/d95/classBase_1_1XMLReader.html#a6ea7476fa5d4b3080c2c2380844ae291)  
unsigned [int](../../d1/da0/classint.html) | [CharacterCount](../../dc/d95/classBase_1_1XMLReader.html#a75dde7a646291100f3ef6e93bb229af4)  
std::map< std::string, std::string > | [AttrMap](../../dc/d95/classBase_1_1XMLReader.html#addd22e3d3b22576bbb557015e138ffb4)  
enum Base::XMLReader:: { ... } | [ReadType](../../dc/d95/classBase_1_1XMLReader.html#afbe9c0aca18c1e73bea9b9109466286f)  
XERCES_CPP_NAMESPACE_QUALIFIER SAX2XMLReader * | [parser](../../dc/d95/classBase_1_1XMLReader.html#ab0dd486704a3c691df1085cbd4da93af)  
XERCES_CPP_NAMESPACE_QUALIFIER XMLPScanToken | [token](../../dc/d95/classBase_1_1XMLReader.html#a51f866977ae5d5bd7450fca671de0072)  
std::vector< std::string > | [FileNames](../../dc/d95/classBase_1_1XMLReader.html#a02b9352cc15b50721388c62348c29c34)  
std::bitset< 32 > | [StatusBits](../../dc/d95/classBase_1_1XMLReader.html#acf6975b0f5b21866b5eb6edab7ba38ac)  
  
## Constructor & Destructor Documentation

## ◆ XMLMergeReader()

App::XMLMergeReader::XMLMergeReader  | ( | std::map< std::string, std::string > & | _name_ ,   
---|---|---|---  
|  | const char *  | _FileName_ ,   
|  | std::istream & | _str_  
| ) | |   
  
## Member Function Documentation

## ◆ addName()

| void App::XMLMergeReader::addName  | ( | const char *  | _s1_ ,   
---|---|---|---  
|  | const char *  | _s2_  
| ) | |   
virtual  
  
Reimplemented from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html#a96a6be27f027068b5260c1df328faea4).

## ◆ doNameMapping()

| [bool](../../d9/db9/classbool.html) App::XMLMergeReader::doNameMapping  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html#a1d431382d6f452a2a87cb9c7462d6e72).

## ◆ getName()

| const char * App::XMLMergeReader::getName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/MergeDocuments.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

