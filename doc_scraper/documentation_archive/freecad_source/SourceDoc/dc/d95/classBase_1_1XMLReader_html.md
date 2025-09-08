---
url: https://freecad.github.io/SourceDoc/dc/d95/classBase_1_1XMLReader.html
scraped_at: 2025-09-08T15:18:19.454931
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [XMLReader](../../dc/d95/classBase_1_1XMLReader.html)

[List of all members](../../d0/dbf/classBase_1_1XMLReader-members.html) | Classes | Public Types | Public Member Functions

Base::XMLReader Class Reference

The XML reader class This is an important helper class for the store and
retrieval system of objects in FreeCAD.
[More...](../../dc/d95/classBase_1_1XMLReader.html#details)

`#include <Reader.h>`

##  Classes  
  
---  
struct | [FileEntry](../../d4/d0e/structBase_1_1XMLReader_1_1FileEntry.html)  
  
##  Public Types  
  
---  
enum | [ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50) { [PartialRestore](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50aee244f56623eb5670c7219096835a52c) = 0 , [PartialRestoreInDocumentObject](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50a22ec7d4e78b150adbed3f2546a405e1e) = 1 , [PartialRestoreInProperty](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50a5d210453139b949521d6bc19d20732f9) = 2 , [PartialRestoreInObject](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50a18fabdd961603a12048f1bfdb670c7ef) = 3 }  
  
##  Public Member Functions  
  
---  
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
Parser handling  
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
  
Attribute handling  
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
  
  
##  Protected Member Functions  
  
---  
Content handler  
virtual void | [startDocument](../../dc/d95/classBase_1_1XMLReader.html#a81c1cb0a200a4249e973fe6b01a1a736) ()  
virtual void | [endDocument](../../dc/d95/classBase_1_1XMLReader.html#a1a330b1a0744588a97aadbd274048148) ()  
virtual void | [startElement](../../dc/d95/classBase_1_1XMLReader.html#aa99360f6d38f98f1c6f60d22ff055738) (const XMLCh *const uri, const XMLCh *const localname, const XMLCh *const qname, const XERCES_CPP_NAMESPACE_QUALIFIER Attributes &attrs)  
virtual void | [endElement](../../dc/d95/classBase_1_1XMLReader.html#aca0fa7593b57b5929f3d431b1d25ece9) (const XMLCh *const uri, const XMLCh *const localname, const XMLCh *const qname)  
virtual void | [characters](../../dc/d95/classBase_1_1XMLReader.html#a1f20264114d4c9f143831b7479417cbc) (const XMLCh *const chars, const XMLSize_t length)  
virtual void | [ignorableWhitespace](../../dc/d95/classBase_1_1XMLReader.html#aae2669227d3d5e1b70d0866e18dadd7c) (const XMLCh *const chars, const XMLSize_t length)  
Lexical handler  
virtual void | [startCDATA](../../dc/d95/classBase_1_1XMLReader.html#a058a241dc9cc900d24f7f1a7a83cf8a0) ()  
virtual void | [endCDATA](../../dc/d95/classBase_1_1XMLReader.html#aa6600b5e27fd64db2d8709d7116d6454) ()  
Document handler  
virtual void | [resetDocument](../../dc/d95/classBase_1_1XMLReader.html#a40996ed04a1bcccb7d61e4fe0d473304) ()  
  
## Error handler  
  
---  
typedef std::map< std::string, std::string > | [AttrMapType](../../dc/d95/classBase_1_1XMLReader.html#a287bd21096c2d7f40616931b90be0c67)  
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
void | [warning](../../dc/d95/classBase_1_1XMLReader.html#a8d030ff8ef85ae16aaefbf5635897c30) (const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException &exc)  
void | [error](../../dc/d95/classBase_1_1XMLReader.html#af7f902f8c2c83c9f7ca5286a213260d6) (const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException &exc)  
void | [fatalError](../../dc/d95/classBase_1_1XMLReader.html#a0f2f8688a7a6db9c41eac713496483f1) (const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException &exc)  
void | [resetErrors](../../dc/d95/classBase_1_1XMLReader.html#a4d701e3c554d9203142df4ea41be99dd) ()  
  
## additional file reading  
  
---  
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
virtual void | [addName](../../dc/d95/classBase_1_1XMLReader.html#a96a6be27f027068b5260c1df328faea4) (const char *, const char *)  
virtual const char * | [getName](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8) (const char *) const  
virtual [bool](../../d9/db9/classbool.html) | [doNameMapping](../../dc/d95/classBase_1_1XMLReader.html#a1d431382d6f452a2a87cb9c7462d6e72) () const  
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
  
[bool](../../d9/db9/classbool.html) | [read](../../dc/d95/classBase_1_1XMLReader.html#af5fba875db7b1494423dc339fbeb425e) ()  
| read the next element
[More...](../../dc/d95/classBase_1_1XMLReader.html#af5fba875db7b1494423dc339fbeb425e)  
  
  
## Detailed Description

The XML reader class This is an important helper class for the store and
retrieval system of objects in FreeCAD.

These classes mainly inherit the App::Persitance base class and implement the
Restore() method.

    The reader gets mainly initialized by the [App::Document](../../d8/d3e/classApp_1_1Document.html "The document class.") on retrieving a document out of a file. From there subsequently the Restore() method will by called on all object stored. 

    A simple example is the Restore of [App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html "String properties This is the father of all properties handling Strings."): 

void PropertyString::Save (short indent,std::ostream
&[str](../../d9/d36/classstr.html))

{

[str](../../d9/d36/classstr.html) << "<String value=\"" << _cValue.c_str()
<<"\"/>" ;

}

void
PropertyString::Restore([Base::Reader](../../d1/d1f/classBase_1_1Reader.html)
&reader)

{

// read my Element

reader.readElement("String");

// get the value of my Attribute

_cValue = reader.getAttribute("value");

}

    An more complicated example is the retrieval of the [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base class of all classes with properties."): 

void PropertyContainer::Save (short indent,std::ostream
&[str](../../d9/d36/classstr.html))

{

std::map<std::string,Property*> Map;

getPropertyMap(Map);

[str](../../d9/d36/classstr.html) << ind(indent) << "<Properties Count=\"" <<
Map.size() << "\">" << endl;

std::map<std::string,Property*>::iterator it;

for(it = Map.begin(); it != Map.end(); ++it)

{

[str](../../d9/d36/classstr.html) << ind(indent+1) << "<Property name=\"" <<
it->first << "\" type=\"" << it->second->getTypeId().getName() << "\">" ;

it->second->Save(indent+2,[str](../../d9/d36/classstr.html));

[str](../../d9/d36/classstr.html) << "</Property>" << endl;

}

[str](../../d9/d36/classstr.html) << ind(indent) << "</Properties>" << endl;

}

void
PropertyContainer::Restore([Base::Reader](../../d1/d1f/classBase_1_1Reader.html)
&reader)

{

reader.readElement("Properties");

int Cnt = reader.getAttributeAsInteger("Count");

for(int i=0 ;i<Cnt ;i++)

{

reader.readElement("Property");

string PropName = reader.getAttribute("name");

Property* prop = getPropertyByName(PropName.c_str());

if(prop)

prop->Restore(reader);

reader.readEndElement("Property");

}

reader.readEndElement("Properties");

}

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Author

    Juergen Riegel 

## Member Typedef Documentation

## ◆ AttrMapType

| typedef std::map<std::string,std::string>
[Base::XMLReader::AttrMapType](../../dc/d95/classBase_1_1XMLReader.html#a287bd21096c2d7f40616931b90be0c67)  
---  
protected  
  
## Member Enumeration Documentation

## ◆ anonymous enum

| anonymous enum  
---  
protected  
  
Enumerator  
---  
Chars |   
StartDocument |   
EndDocument |   
StartElement |   
StartEndElement |   
EndElement |   
StartCDATA |   
EndCDATA |   
  
## ◆ ReaderStatus

enum
[Base::XMLReader::ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50)  
---  
  
Enumerator  
---  
PartialRestore |   
PartialRestoreInDocumentObject |   
PartialRestoreInProperty |   
PartialRestoreInObject |   
  
## Constructor & Destructor Documentation

## ◆ XMLReader()

Base::XMLReader::XMLReader  | ( | const char *  | _FileName_ ,   
---|---|---|---  
|  | std::istream & | _str_  
| ) | |   
  
open the file and read the first element

References
[parser](../../dc/d95/classBase_1_1XMLReader.html#ab0dd486704a3c691df1085cbd4da93af),
and
[token](../../dc/d95/classBase_1_1XMLReader.html#a51f866977ae5d5bd7450fca671de0072).

## ◆ ~XMLReader()

Base::XMLReader::~XMLReader  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ addFile()

const char * Base::XMLReader::addFile  | ( | const char *  | _Name_ ,   
---|---|---|---  
|  | [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *  | _Object_  
| ) | |   
  
add a read request of a persistent object

References
[Base::XMLReader::FileEntry::FileName](../../d4/d0e/structBase_1_1XMLReader_1_1FileEntry.html#a2c981449d3a5ad92ffe17c69a5253b29),
and
[Base::XMLReader::FileEntry::Object](../../d4/d0e/structBase_1_1XMLReader_1_1FileEntry.html#a810a31633177de69f84d2b9749940dc9).

Referenced by
[Fem::FemMesh::Restore()](../../d3/d2e/classFem_1_1FemMesh.html#a814209824262c9cd4f14ddf22b9cf4cf),
[Path::Toolpath::Restore()](../../d6/d0c/classPath_1_1Toolpath.html#a5ffa4b9600118d7689e0d485b63d4afa),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::VRMLObject::Restore()](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[Gui::Document::Restore()](../../de/d4e/classGui_1_1Document.html#a2dd4824fb42f9df790ad9f2ea345e5ab),
[Fem::PropertyPostDataObject::Restore()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ab855a7ff4e993051613fb38b4f5e5e11),
[Inspection::PropertyDistanceList::Restore()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a3499fd97bd4023a5b3628a13742fd138),
[Mesh::PropertyNormalList::Restore()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Mesh::PropertyCurvatureList::Restore()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Mesh::PropertyMeshKernel::Restore()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ae5fd1c096fb6b3a70935261847e70115),
[Part::PropertyPartShape::Restore()](../../d7/d28/classPart_1_1PropertyPartShape.html#a3e01a3548f94138d0aad884954e85dad),
[Part::PropertyFilletEdges::Restore()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#ab0f152b8576922a623c621bac56010a5),
[Path::PropertyPath::Restore()](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[Points::PointKernel::Restore()](../../dc/de1/classPoints_1_1PointKernel.html#af4c6a89cb77c9799928d858ddcaad09c),
[Points::PropertyGreyValueList::Restore()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a32a4eaf9dacfd7e3054863b81b4f3e04),
[Points::PropertyNormalList::Restore()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Points::PropertyCurvatureList::Restore()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
[App::PropertyVectorList::Restore()](../../d5/d13/classApp_1_1PropertyVectorList.html#a64ee9a1ab4beeb4a98fd0c80227703ea),
[App::PropertyPlacementList::Restore()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a92707872de5970bad0cce842e8644fd8),
[App::PropertyFloatList::Restore()](../../dc/d40/classApp_1_1PropertyFloatList.html#a602bb1a4bae4daee9223f26201d96795),
[App::PropertyColorList::Restore()](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73),
and
[App::PropertyMaterialList::Restore()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a8ea57c6a941944daa32ea5ab471b8877).

## ◆ addName()

| void Base::XMLReader::addName  | ( | const char *  | ,   
---|---|---|---  
|  | const char *  |   
| ) | |   
virtual  
  
Reimplemented in
[App::XMLMergeReader](../../d5/d76/classApp_1_1XMLMergeReader.html#aaa60a28ad48675faa89dc03e8858b204),
and
[Gui::XMLMergeReader](../../d4/d19/classGui_1_1XMLMergeReader.html#a70930dd1b1ef3783a67ab5c554a431fd).

Referenced by
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d).

## ◆ characters()

| void Base::XMLReader::characters  | ( | const XMLCh *const  | _chars_ ,   
---|---|---|---  
|  | const XMLSize_t  | _length_  
| ) | |   
protectedvirtual  
  
References
[StrX::c_str()](../../d2/d3f/classStrX.html#ac350b620adc70fb4cdcb4f5bfdd0f07e).

## ◆ clearPartialRestoreDocumentObject()

void Base::XMLReader::clearPartialRestoreDocumentObject  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d).

## ◆ clearPartialRestoreObject()

void Base::XMLReader::clearPartialRestoreObject  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
and
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807).

## ◆ clearPartialRestoreProperty()

void Base::XMLReader::clearPartialRestoreProperty  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

## ◆ doNameMapping()

| [bool](../../d9/db9/classbool.html) Base::XMLReader::doNameMapping  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::XMLMergeReader](../../d5/d76/classApp_1_1XMLMergeReader.html#a2248ef49970d1203f48c6c04e2893a84),
and
[Gui::XMLMergeReader](../../d4/d19/classGui_1_1XMLMergeReader.html#ad742476c5e7d88455b060295cbf6a5cc).

Referenced by
[App::PropertyLinkBase::importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e),
and
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d).

## ◆ endCDATA()

| void Base::XMLReader::endCDATA  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
## ◆ endDocument()

| void Base::XMLReader::endDocument  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
## ◆ endElement()

| void Base::XMLReader::endElement  | ( | const XMLCh *const  | _uri_ ,   
---|---|---|---  
|  | const XMLCh *const  | _localname_ ,   
|  | const XMLCh *const  | _qname_  
| ) | |   
protectedvirtual  
  
References
[StrX::c_str()](../../d2/d3f/classStrX.html#ac350b620adc70fb4cdcb4f5bfdd0f07e).

## ◆ error()

| void Base::XMLReader::error  | ( | const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException & | _exc_| ) |   
---|---|---|---|---|---  
protected  
  
Referenced by
[femmesh.gmshtools.GmshTools::read_and_set_new_mesh()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a5ef3ad4b8ff477c0c3b13c11b9a9062e),
[FreeCADInit.FCADLogger::report()](../../d2/d1e/classFreeCADInit_1_1FCADLogger.html#a53ca47c23bb6061489b47ab9c2e19512),
and
[femmesh.gmshtools.GmshTools::run_gmsh_with_geo()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a37e8a08f6afd2d35a718d51070fd4f35).

## ◆ fatalError()

| void Base::XMLReader::fatalError  | ( | const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException & | _exc_| ) |   
---|---|---|---|---|---  
protected  
  
## ◆ getAttribute()

const char * Base::XMLReader::getAttribute  | ( | const char *  | _AttrName_| ) |  const  
---|---|---|---|---|---  
  
return the named attribute as a double floating point (does type checking)

Referenced by
[PartDesign::ProfileBased::handleChangedPropertyName()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Fem::FemMesh::Restore()](../../d3/d2e/classFem_1_1FemMesh.html#a814209824262c9cd4f14ddf22b9cf4cf),
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Path::Command::Restore()](../../d7/d2e/classPath_1_1Command.html#a6ff90cf3809d3bdb0390e8ca33cbbef3),
[Path::Toolpath::Restore()](../../d6/d0c/classPath_1_1Toolpath.html#a5ffa4b9600118d7689e0d485b63d4afa),
[Path::Tool::Restore()](../../dd/dfe/classPath_1_1Tool.html#afe9d6f36b22e02eaf7f99b584c455b39),
[Robot::Waypoint::Restore()](../../d1/dc7/classRobot_1_1Waypoint.html#a922b6bfba5cd598e35388754d587bb10),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CosmeticEdge::Restore()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::GeomFormat::Restore()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ac64bf6edf61062cc6acaf193cdba1864),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[Sketcher::Constraint::Restore()](../../d6/def/classSketcher_1_1Constraint.html#a030951705bba6aa6323885f998e5c8b7),
[TechDraw::BaseGeom::Restore()](../../db/d3c/classTechDraw_1_1BaseGeom.html#afae6206ff96624f44308697f53c868d3),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyPath::Restore()](../../dc/d24/classApp_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyMap::Restore()](../../db/d3f/classApp_1_1PropertyMap.html#a9362c746cddf00578f7c2772133b2419),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyUUID::Restore()](../../d2/d6c/classApp_1_1PropertyUUID.html#afec516dbf82dbaa0fbc6ad5c96a0708f),
[App::PropertyBool::Restore()](../../dc/d81/classApp_1_1PropertyBool.html#a198b7cda570cfdad094c8886cd995778),
[Gui::DocumentItem::ExpandInfo::restore()](../../dc/dd6/classDocumentItem_1_1ExpandInfo.html#ad851dd90613261db134bdfeef8d1ff58),
[Fem::PropertyPostDataObject::Restore()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ab855a7ff4e993051613fb38b4f5e5e11),
[Inspection::PropertyDistanceList::Restore()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a3499fd97bd4023a5b3628a13742fd138),
[Mesh::PropertyNormalList::Restore()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Mesh::PropertyCurvatureList::Restore()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Mesh::PropertyMeshKernel::Restore()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ae5fd1c096fb6b3a70935261847e70115),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[Part::PropertyPartShape::Restore()](../../d7/d28/classPart_1_1PropertyPartShape.html#a3e01a3548f94138d0aad884954e85dad),
[Part::PropertyFilletEdges::Restore()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#ab0f152b8576922a623c621bac56010a5),
[Path::PropertyPath::Restore()](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[Points::PointKernel::Restore()](../../dc/de1/classPoints_1_1PointKernel.html#af4c6a89cb77c9799928d858ddcaad09c),
[Points::PropertyGreyValueList::Restore()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a32a4eaf9dacfd7e3054863b81b4f3e04),
[Points::PropertyNormalList::Restore()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Points::PropertyCurvatureList::Restore()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
[Spreadsheet::PropertyColumnWidths::Restore()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a3e5f54a360a79e8a1ada41e549fdb51f),
[Spreadsheet::PropertyRowHeights::Restore()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a63938d46c9385cca14d404ffa9ccbb74),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::PropertyExpressionEngine::Restore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyVectorList::Restore()](../../d5/d13/classApp_1_1PropertyVectorList.html#a64ee9a1ab4beeb4a98fd0c80227703ea),
[App::PropertyPlacementList::Restore()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a92707872de5970bad0cce842e8644fd8),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkContainer::Restore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4),
[App::PropertyFloatList::Restore()](../../dc/d40/classApp_1_1PropertyFloatList.html#a602bb1a4bae4daee9223f26201d96795),
[App::PropertyStringList::Restore()](../../d8/d55/classApp_1_1PropertyStringList.html#a63237fa5b3eaf0a6fc3a051d5a6e9bcf),
[App::PropertyBoolList::Restore()](../../d1/dcf/classApp_1_1PropertyBoolList.html#ab04174271d33c19c037c99c930e25a7e),
[App::PropertyColorList::Restore()](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73),
[App::PropertyMaterialList::Restore()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a8ea57c6a941944daa32ea5ab471b8877),
[Spreadsheet::PropertySheet::Restore()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5682de0cd8471dd97ec68393abec332a),
[Spreadsheet::Cell::restore()](../../d5/d22/classSpreadsheet_1_1Cell.html#a3a19ec5a32c6ebedd936aa7475943735),
[App::DynamicProperty::restore()](../../d5/d76/classApp_1_1DynamicProperty.html#aabd3c2d0b261a6a0bb4aa55500ea09ca),
[Part::GeometryDefaultExtension< T
>::restoreAttributes()](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a4c828a085b814d724f75da3d3d86ec8a),
[Sketcher::ExternalGeometryExtension::restoreAttributes()](../../d5/dea/classSketcher_1_1ExternalGeometryExtension.html#a2f138a338ceeb9fac06582c7923362e3),
[Sketcher::SketchGeometryExtension::restoreAttributes()](../../d7/db4/classSketcher_1_1SketchGeometryExtension.html#a707950a7e8fbc8861c29f8d6aa94687f),
and
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab).

## ◆ getAttributeAsFloat()

double Base::XMLReader::getAttributeAsFloat  | ( | const char *  | _AttrName_| ) |  const  
---|---|---|---|---|---  
  
return the named attribute as a double floating point (does type checking)

Referenced by
[MeshCore::MeshInput::LoadXML()](../../d9/d08/classMeshCore_1_1MeshInput.html#a86550f4aa655451367800cbc22aa1afb),
[Fem::FemMesh::Restore()](../../d3/d2e/classFem_1_1FemMesh.html#a814209824262c9cd4f14ddf22b9cf4cf),
[Part::GeomPoint::Restore()](../../d2/dfb/classPart_1_1GeomPoint.html#aff8fe01b1e05f053db6ac2f10a2744ef),
[Part::GeomBSplineCurve::Restore()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#a4729db2206213978ad19f3f242179483),
[Part::GeomCircle::Restore()](../../d0/dde/classPart_1_1GeomCircle.html#af4b7a3f5d7dbd10ae63207445d2774dc),
[Part::GeomArcOfCircle::Restore()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#ac4ac7f8e5d9ce8abf685102ea1414d33),
[Part::GeomEllipse::Restore()](../../db/d52/classPart_1_1GeomEllipse.html#a6c8493d4d7ea506331d9908e3e5e3258),
[Part::GeomArcOfEllipse::Restore()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a2e373a4343b69f760be7dbe82d1bc3ff),
[Part::GeomHyperbola::Restore()](../../d7/d9e/classPart_1_1GeomHyperbola.html#ad47231b8c5d06074ff90da802cd3a913),
[Part::GeomArcOfHyperbola::Restore()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a821f3cf6340c7b5ea26587b92f3ace14),
[Part::GeomParabola::Restore()](../../d9/ddf/classPart_1_1GeomParabola.html#a4576d65d095cc16b53b327ff0d547b32),
[Part::GeomArcOfParabola::Restore()](../../db/ddc/classPart_1_1GeomArcOfParabola.html#ad3651d13c1cfc433252921965b8cbb6c),
[Part::GeomLine::Restore()](../../d5/d30/classPart_1_1GeomLine.html#a5a0b0e4fafe02652e8199e1ea0404fc1),
[Part::GeomLineSegment::Restore()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aa9c977ad83ada922a774ef226d9b092d),
[Part::Geom2dPoint::Restore()](../../d8/da9/classPart_1_1Geom2dPoint.html#ae3ae1851f3f8caa3f5ce8739a0a2072e),
[Part::Geom2dCircle::Restore()](../../d7/d4e/classPart_1_1Geom2dCircle.html#a935cf4d824a7bbb8fc7c4bab51fc0a47),
[Part::Geom2dArcOfCircle::Restore()](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a2c6839555697c101a94c6600064478a9),
[Part::Geom2dEllipse::Restore()](../../db/db9/classPart_1_1Geom2dEllipse.html#a69dd5ee48eef1e3d07a3cde17b5213d2),
[Part::Geom2dArcOfEllipse::Restore()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a3cca7e273f244ed9299a47c70afa019c),
[Part::Geom2dHyperbola::Restore()](../../d2/d95/classPart_1_1Geom2dHyperbola.html#a9aa82ebdcae679d490e28f69d8e8b15d),
[Part::Geom2dArcOfHyperbola::Restore()](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#ae257d16f6106902cd4be1ded2afb12d3),
[Part::Geom2dParabola::Restore()](../../d9/dff/classPart_1_1Geom2dParabola.html#ac27ce7869ff49efc95f21fb60024f621),
[Part::Geom2dArcOfParabola::Restore()](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a54034881b3b953385eb987068c7878ac),
[Part::Geom2dLineSegment::Restore()](../../df/ded/classPart_1_1Geom2dLineSegment.html#a7d8d4ba2ddea88d8135befdb47b28289),
[Path::Tool::Restore()](../../dd/dfe/classPath_1_1Tool.html#afe9d6f36b22e02eaf7f99b584c455b39),
[Robot::Robot6Axis::Restore()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a6e0075555eff89970979c568369365af),
[Robot::Waypoint::Restore()](../../d1/dc7/classRobot_1_1Waypoint.html#a922b6bfba5cd598e35388754d587bb10),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CosmeticEdge::Restore()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::GeomFormat::Restore()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ac64bf6edf61062cc6acaf193cdba1864),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[Sketcher::Constraint::Restore()](../../d6/def/classSketcher_1_1Constraint.html#a030951705bba6aa6323885f998e5c8b7),
[TechDraw::Circle::Restore()](../../d3/d63/classTechDraw_1_1Circle.html#a0c95eda08d536f7de7c3a3abb3007e76),
[TechDraw::AOC::Restore()](../../d0/d5c/classTechDraw_1_1AOC.html#a6adb7fceabe6a5089727723cff4b2760),
[TechDraw::Generic::Restore()](../../dd/d23/classTechDraw_1_1Generic.html#a8850e5eb8a34c47b152b62fafe77905d),
[App::PropertyMatrix::Restore()](../../d8/d77/classApp_1_1PropertyMatrix.html#ac341d4242623336eafaf73bd16dfe8ad),
[App::PropertyFloat::Restore()](../../d3/dbe/classApp_1_1PropertyFloat.html#aa6d8ab192c6855fe5506b10e458460cf),
[App::PropertyMaterial::Restore()](../../d0/df5/classApp_1_1PropertyMaterial.html#a9f1511c5fd99820c649307361c6c8880),
[Path::PropertyPath::Restore()](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[App::PropertyExpressionEngine::Restore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyVector::Restore()](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c),
[App::PropertyPlacement::Restore()](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734),
[App::PropertyRotation::Restore()](../../df/d76/classApp_1_1PropertyRotation.html#af641d12c42fa3ed2076e9d3f234ef31c),
[Part::GeometryDefaultExtension< T
>::restoreAttributes()](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a0d3a1575cbb11fdc5abe03cfc83c701c),
[Part::Geom2dConic::RestoreAxis()](../../d8/d0d/classPart_1_1Geom2dConic.html#a9c3240c5ed7c23ef9e23b43c732ab793),
and
[Part::Geom2dArcOfConic::RestoreAxis()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#af57fff92db125fddb52fc7b14acf9823).

## ◆ getAttributeAsInteger()

long Base::XMLReader::getAttributeAsInteger  | ( | const char *  | _AttrName_| ) |  const  
---|---|---|---|---|---  
  
return the named attribute as an interer (does type checking)

Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[MeshCore::MeshInput::LoadXML()](../../d9/d08/classMeshCore_1_1MeshInput.html#a86550f4aa655451367800cbc22aa1afb),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Part::GeomBSplineCurve::Restore()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#a4729db2206213978ad19f3f242179483),
[Path::Tooltable::Restore()](../../df/dca/classPath_1_1Tooltable.html#aa6832676e89f0215973ccbe0a6cd6ffb),
[Robot::Trajectory::Restore()](../../d7/d14/classRobot_1_1Trajectory.html#a0294c37886cce33476159b3e9bd3102e),
[Robot::Waypoint::Restore()](../../d1/dc7/classRobot_1_1Waypoint.html#a922b6bfba5cd598e35388754d587bb10),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CosmeticEdge::Restore()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::GeomFormat::Restore()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ac64bf6edf61062cc6acaf193cdba1864),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[Sketcher::Constraint::Restore()](../../d6/def/classSketcher_1_1Constraint.html#a030951705bba6aa6323885f998e5c8b7),
[TechDraw::BaseGeom::Restore()](../../db/d3c/classTechDraw_1_1BaseGeom.html#afae6206ff96624f44308697f53c868d3),
[TechDraw::AOC::Restore()](../../d0/d5c/classTechDraw_1_1AOC.html#a6adb7fceabe6a5089727723cff4b2760),
[TechDraw::Generic::Restore()](../../dd/d23/classTechDraw_1_1Generic.html#a8850e5eb8a34c47b152b62fafe77905d),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyInteger::Restore()](../../dd/d85/classApp_1_1PropertyInteger.html#a172043a2979b6d97bc1f79cf82fdfb02),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyIntegerSet::Restore()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a2326110666959447c4218d46d2d30dd7),
[App::PropertyMap::Restore()](../../db/d3f/classApp_1_1PropertyMap.html#a9362c746cddf00578f7c2772133b2419),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[Gui::DocumentItem::ExpandInfo::restore()](../../dc/dd6/classDocumentItem_1_1ExpandInfo.html#ad851dd90613261db134bdfeef8d1ff58),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[Path::PropertyPath::Restore()](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[Spreadsheet::PropertyColumnWidths::Restore()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a3e5f54a360a79e8a1ada41e549fdb51f),
[Spreadsheet::PropertyRowHeights::Restore()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a63938d46c9385cca14d404ffa9ccbb74),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::PropertyExpressionEngine::Restore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkSubList::Restore()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995),
[App::PropertyIntegerList::Restore()](../../d7/daa/classApp_1_1PropertyIntegerList.html#aae0652a9de7572ada2cdb818c54e29ef),
[App::PropertyStringList::Restore()](../../d8/d55/classApp_1_1PropertyStringList.html#a63237fa5b3eaf0a6fc3a051d5a6e9bcf),
[Sketcher::PropertyConstraintList::Restore()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#aa6e11dd2fcd1f2307c14e3df94e4fbe7),
[Spreadsheet::PropertySheet::Restore()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5682de0cd8471dd97ec68393abec332a),
[Part::GeometryDefaultExtension< T
>::restoreAttributes()](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a04c4da712d5c0d75ebdc29d4cbe08717),
[Sketcher::SketchGeometryExtension::restoreAttributes()](../../d7/db4/classSketcher_1_1SketchGeometryExtension.html#a707950a7e8fbc8861c29f8d6aa94687f),
and
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab).

## ◆ getAttributeAsUnsigned()

unsigned long Base::XMLReader::getAttributeAsUnsigned  | ( | const char *  | _AttrName_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyColor::Restore()](../../d9/d0b/classApp_1_1PropertyColor.html#a4e375cae7bed77bacf0a6dd30794212e),
[App::PropertyMaterial::Restore()](../../d0/df5/classApp_1_1PropertyMaterial.html#a9f1511c5fd99820c649307361c6c8880),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
and
[App::PropertyXLinkContainer::Restore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4).

## ◆ getAttributeCount()

unsigned [int](../../d1/da0/classint.html) Base::XMLReader::getAttributeCount  | ( | | ) |  const  
---|---|---|---|---  
  
get the number of attributes of the current element

## ◆ getFilenames()

const std::vector< std::string > & Base::XMLReader::getFilenames  | ( | | ) |  const  
---|---|---|---|---  
  
get all registered file names

## ◆ getName()

| const char * Base::XMLReader::getName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[App::XMLMergeReader](../../d5/d76/classApp_1_1XMLMergeReader.html#ab6451493700a993be1f241b745709b64),
and
[Gui::XMLMergeReader](../../d4/d19/classGui_1_1XMLMergeReader.html#a527deae08d79856029c7a593a1d5a99d).

Referenced by
[App::PropertyLinkBase::importSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
and
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c).

## ◆ hasAttribute()

[bool](../../d9/db9/classbool.html) Base::XMLReader::hasAttribute  | ( | const char *  | _AttrName_| ) |  const  
---|---|---|---|---|---  
  
check if the read element has a special attribute

Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Fem::FemMesh::Restore()](../../d3/d2e/classFem_1_1FemMesh.html#a814209824262c9cd4f14ddf22b9cf4cf),
[Part::GeomCircle::Restore()](../../d0/dde/classPart_1_1GeomCircle.html#af4b7a3f5d7dbd10ae63207445d2774dc),
[Part::GeomArcOfCircle::Restore()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#ac4ac7f8e5d9ce8abf685102ea1414d33),
[Part::GeomEllipse::Restore()](../../db/d52/classPart_1_1GeomEllipse.html#a6c8493d4d7ea506331d9908e3e5e3258),
[Path::Tool::Restore()](../../dd/dfe/classPath_1_1Tool.html#afe9d6f36b22e02eaf7f99b584c455b39),
[Robot::Robot6Axis::Restore()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a6e0075555eff89970979c568369365af),
[Gui::DocumentItem::Restore()](../../df/d15/classGui_1_1DocumentItem.html#a0b9ab7578bf8cee38467ad7a45983367),
[Sketcher::Constraint::Restore()](../../d6/def/classSketcher_1_1Constraint.html#a030951705bba6aa6323885f998e5c8b7),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[Gui::DocumentItem::ExpandInfo::restore()](../../dc/dd6/classDocumentItem_1_1ExpandInfo.html#ad851dd90613261db134bdfeef8d1ff58),
[Fem::PropertyPostDataObject::Restore()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ab855a7ff4e993051613fb38b4f5e5e11),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Path::PropertyPath::Restore()](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[Spreadsheet::PropertyColumnWidths::Restore()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a3e5f54a360a79e8a1ada41e549fdb51f),
[Spreadsheet::PropertyRowHeights::Restore()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a63938d46c9385cca14d404ffa9ccbb74),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::PropertyExpressionEngine::Restore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyPlacement::Restore()](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkSubList::Restore()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995),
[App::PropertyXLinkContainer::Restore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4),
[App::PropertyColorList::Restore()](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73),
[App::PropertyMaterialList::Restore()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a8ea57c6a941944daa32ea5ab471b8877),
[Spreadsheet::PropertySheet::Restore()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5682de0cd8471dd97ec68393abec332a),
[Spreadsheet::Cell::restore()](../../d5/d22/classSpreadsheet_1_1Cell.html#a3a19ec5a32c6ebedd936aa7475943735),
[App::DynamicProperty::restore()](../../d5/d76/classApp_1_1DynamicProperty.html#aabd3c2d0b261a6a0bb4aa55500ea09ca),
[Sketcher::SketchGeometryExtension::restoreAttributes()](../../d7/db4/classSketcher_1_1SketchGeometryExtension.html#a707950a7e8fbc8861c29f8d6aa94687f),
and
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab).

## ◆ ignorableWhitespace()

| void Base::XMLReader::ignorableWhitespace  | ( | const XMLCh *const  | _chars_ ,   
---|---|---|---  
|  | const XMLSize_t  | _length_  
| ) | |   
protectedvirtual  
  
## ◆ isRegistered()

[bool](../../d9/db9/classbool.html) Base::XMLReader::isRegistered  | ( | [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *  | _Object_| ) |  const  
---|---|---|---|---|---  
  
## ◆ isValid()

[bool](../../d9/db9/classbool.html) Base::XMLReader::isValid  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Cloud::Module::cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[Base::Persistence::restoreFromStream()](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd).

## ◆ isVerbose()

[bool](../../d9/db9/classbool.html) Base::XMLReader::isVerbose  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
and
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c).

## ◆ level()

[int](../../d1/da0/classint.html) Base::XMLReader::level  | ( | | ) |  const  
---|---|---|---|---  
  
get the current element level

Referenced by
[Gui::DocumentItem::ExpandInfo::restore()](../../dc/dd6/classDocumentItem_1_1ExpandInfo.html#ad851dd90613261db134bdfeef8d1ff58).

## ◆ localName()

const char * Base::XMLReader::localName  | ( | | ) |  const  
---|---|---|---|---  
  
get the local name of the current Element

Referenced by
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
and
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807).

## ◆ read()

| [bool](../../d9/db9/classbool.html) Base::XMLReader::read  | ( | | ) |   
---|---|---|---|---  
protected  
  
read the next element

Referenced by
[gzip_utf8.GzipFile::readline()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a17112c17fb6431a0d56b0108931c73e0),
and
[gzip_utf8.GzipFile::seek()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ac5b53848e16b6ba800ed9ac8d3f737c3).

## ◆ readBinFile()

void Base::XMLReader::readBinFile  | ( | const char *  | _filename_| ) |   
---|---|---|---|---|---  
  
read binary file

References
[Base::base64_decode()](../../db/d07/namespaceBase.html#a80246c7918e80c2610af4c94378565df).

Referenced by
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd).

## ◆ readCharacters()

void Base::XMLReader::readCharacters  | ( | | ) |   
---|---|---|---|---  
  
read until characters are found

## ◆ readElement()

void Base::XMLReader::readElement  | ( | const char *  | _ElementName_ = `nullptr`| ) |   
---|---|---|---|---|---  
  
read until a start element is found (<name>) or start-end element (<name/>)
(with special name if given)

Referenced by
[PartDesign::ProfileBased::handleChangedPropertyName()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[MeshCore::MeshInput::LoadXML()](../../d9/d08/classMeshCore_1_1MeshInput.html#a86550f4aa655451367800cbc22aa1afb),
[Spreadsheet::PropertySheet::pasteCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aad0cff130f9da4be76ddc9a92a2236a0),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Fem::FemMesh::Restore()](../../d3/d2e/classFem_1_1FemMesh.html#a814209824262c9cd4f14ddf22b9cf4cf),
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Part::GeomPoint::Restore()](../../d2/dfb/classPart_1_1GeomPoint.html#aff8fe01b1e05f053db6ac2f10a2744ef),
[Part::GeomBSplineCurve::Restore()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#a4729db2206213978ad19f3f242179483),
[Part::GeomCircle::Restore()](../../d0/dde/classPart_1_1GeomCircle.html#af4b7a3f5d7dbd10ae63207445d2774dc),
[Part::GeomArcOfCircle::Restore()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#ac4ac7f8e5d9ce8abf685102ea1414d33),
[Part::GeomEllipse::Restore()](../../db/d52/classPart_1_1GeomEllipse.html#a6c8493d4d7ea506331d9908e3e5e3258),
[Part::GeomArcOfEllipse::Restore()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a2e373a4343b69f760be7dbe82d1bc3ff),
[Part::GeomHyperbola::Restore()](../../d7/d9e/classPart_1_1GeomHyperbola.html#ad47231b8c5d06074ff90da802cd3a913),
[Part::GeomArcOfHyperbola::Restore()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a821f3cf6340c7b5ea26587b92f3ace14),
[Part::GeomParabola::Restore()](../../d9/ddf/classPart_1_1GeomParabola.html#a4576d65d095cc16b53b327ff0d547b32),
[Part::GeomArcOfParabola::Restore()](../../db/ddc/classPart_1_1GeomArcOfParabola.html#ad3651d13c1cfc433252921965b8cbb6c),
[Part::GeomLine::Restore()](../../d5/d30/classPart_1_1GeomLine.html#a5a0b0e4fafe02652e8199e1ea0404fc1),
[Part::GeomLineSegment::Restore()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aa9c977ad83ada922a774ef226d9b092d),
[Part::Geom2dPoint::Restore()](../../d8/da9/classPart_1_1Geom2dPoint.html#ae3ae1851f3f8caa3f5ce8739a0a2072e),
[Part::Geom2dCircle::Restore()](../../d7/d4e/classPart_1_1Geom2dCircle.html#a935cf4d824a7bbb8fc7c4bab51fc0a47),
[Part::Geom2dArcOfCircle::Restore()](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a2c6839555697c101a94c6600064478a9),
[Part::Geom2dEllipse::Restore()](../../db/db9/classPart_1_1Geom2dEllipse.html#a69dd5ee48eef1e3d07a3cde17b5213d2),
[Part::Geom2dArcOfEllipse::Restore()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a3cca7e273f244ed9299a47c70afa019c),
[Part::Geom2dHyperbola::Restore()](../../d2/d95/classPart_1_1Geom2dHyperbola.html#a9aa82ebdcae679d490e28f69d8e8b15d),
[Part::Geom2dArcOfHyperbola::Restore()](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#ae257d16f6106902cd4be1ded2afb12d3),
[Part::Geom2dParabola::Restore()](../../d9/dff/classPart_1_1Geom2dParabola.html#ac27ce7869ff49efc95f21fb60024f621),
[Part::Geom2dArcOfParabola::Restore()](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a54034881b3b953385eb987068c7878ac),
[Part::Geom2dLineSegment::Restore()](../../df/ded/classPart_1_1Geom2dLineSegment.html#a7d8d4ba2ddea88d8135befdb47b28289),
[Path::Command::Restore()](../../d7/d2e/classPath_1_1Command.html#a6ff90cf3809d3bdb0390e8ca33cbbef3),
[Path::Toolpath::Restore()](../../d6/d0c/classPath_1_1Toolpath.html#a5ffa4b9600118d7689e0d485b63d4afa),
[Path::Tool::Restore()](../../dd/dfe/classPath_1_1Tool.html#afe9d6f36b22e02eaf7f99b584c455b39),
[Path::Tooltable::Restore()](../../df/dca/classPath_1_1Tooltable.html#aa6832676e89f0215973ccbe0a6cd6ffb),
[Robot::Robot6Axis::Restore()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a6e0075555eff89970979c568369365af),
[Robot::Trajectory::Restore()](../../d7/d14/classRobot_1_1Trajectory.html#a0294c37886cce33476159b3e9bd3102e),
[Robot::Waypoint::Restore()](../../d1/dc7/classRobot_1_1Waypoint.html#a922b6bfba5cd598e35388754d587bb10),
[TechDraw::CosmeticVertex::Restore()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CosmeticEdge::Restore()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::GeomFormat::Restore()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ac64bf6edf61062cc6acaf193cdba1864),
[TechDraw::Vertex::Restore()](../../dd/db1/classTechDraw_1_1Vertex.html#a8db190000b0c2b933006ee8c4d94f511),
[Gui::DocumentItem::Restore()](../../df/d15/classGui_1_1DocumentItem.html#a0b9ab7578bf8cee38467ad7a45983367),
[Sketcher::Constraint::Restore()](../../d6/def/classSketcher_1_1Constraint.html#a030951705bba6aa6323885f998e5c8b7),
[TechDraw::BaseGeom::Restore()](../../db/d3c/classTechDraw_1_1BaseGeom.html#afae6206ff96624f44308697f53c868d3),
[TechDraw::Circle::Restore()](../../d3/d63/classTechDraw_1_1Circle.html#a0c95eda08d536f7de7c3a3abb3007e76),
[TechDraw::AOC::Restore()](../../d0/d5c/classTechDraw_1_1AOC.html#a6adb7fceabe6a5089727723cff4b2760),
[TechDraw::Generic::Restore()](../../dd/d23/classTechDraw_1_1Generic.html#a8850e5eb8a34c47b152b62fafe77905d),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyMatrix::Restore()](../../d8/d77/classApp_1_1PropertyMatrix.html#ac341d4242623336eafaf73bd16dfe8ad),
[App::PropertyPythonObject::Restore()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyInteger::Restore()](../../dd/d85/classApp_1_1PropertyInteger.html#a172043a2979b6d97bc1f79cf82fdfb02),
[App::PropertyPath::Restore()](../../dc/d24/classApp_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyIntegerSet::Restore()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a2326110666959447c4218d46d2d30dd7),
[App::PropertyMap::Restore()](../../db/d3f/classApp_1_1PropertyMap.html#a9362c746cddf00578f7c2772133b2419),
[App::PropertyFloat::Restore()](../../d3/dbe/classApp_1_1PropertyFloat.html#aa6d8ab192c6855fe5506b10e458460cf),
[App::PropertyString::Restore()](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyUUID::Restore()](../../d2/d6c/classApp_1_1PropertyUUID.html#afec516dbf82dbaa0fbc6ad5c96a0708f),
[App::PropertyBool::Restore()](../../dc/d81/classApp_1_1PropertyBool.html#a198b7cda570cfdad094c8886cd995778),
[App::PropertyColor::Restore()](../../d9/d0b/classApp_1_1PropertyColor.html#a4e375cae7bed77bacf0a6dd30794212e),
[App::PropertyMaterial::Restore()](../../d0/df5/classApp_1_1PropertyMaterial.html#a9f1511c5fd99820c649307361c6c8880),
[Gui::DocumentItem::ExpandInfo::restore()](../../dc/dd6/classDocumentItem_1_1ExpandInfo.html#ad851dd90613261db134bdfeef8d1ff58),
[Fem::PropertyPostDataObject::Restore()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ab855a7ff4e993051613fb38b4f5e5e11),
[Inspection::PropertyDistanceList::Restore()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a3499fd97bd4023a5b3628a13742fd138),
[Mesh::PropertyNormalList::Restore()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Mesh::PropertyCurvatureList::Restore()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Mesh::PropertyMeshKernel::Restore()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ae5fd1c096fb6b3a70935261847e70115),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[Part::PropertyPartShape::Restore()](../../d7/d28/classPart_1_1PropertyPartShape.html#a3e01a3548f94138d0aad884954e85dad),
[Part::PropertyFilletEdges::Restore()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#ab0f152b8576922a623c621bac56010a5),
[Path::PropertyPath::Restore()](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[Points::PointKernel::Restore()](../../dc/de1/classPoints_1_1PointKernel.html#af4c6a89cb77c9799928d858ddcaad09c),
[Points::PropertyGreyValueList::Restore()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a32a4eaf9dacfd7e3054863b81b4f3e04),
[Points::PropertyNormalList::Restore()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Points::PropertyCurvatureList::Restore()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
[Spreadsheet::PropertyColumnWidths::Restore()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a3e5f54a360a79e8a1ada41e549fdb51f),
[Spreadsheet::PropertyRowHeights::Restore()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a63938d46c9385cca14d404ffa9ccbb74),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::PropertyExpressionEngine::Restore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyVector::Restore()](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c),
[App::PropertyVectorList::Restore()](../../d5/d13/classApp_1_1PropertyVectorList.html#a64ee9a1ab4beeb4a98fd0c80227703ea),
[App::PropertyPlacement::Restore()](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734),
[App::PropertyPlacementList::Restore()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a92707872de5970bad0cce842e8644fd8),
[App::PropertyRotation::Restore()](../../df/d76/classApp_1_1PropertyRotation.html#af641d12c42fa3ed2076e9d3f234ef31c),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkSubList::Restore()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995),
[App::PropertyXLinkContainer::Restore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4),
[App::PropertyIntegerList::Restore()](../../d7/daa/classApp_1_1PropertyIntegerList.html#aae0652a9de7572ada2cdb818c54e29ef),
[App::PropertyFloatList::Restore()](../../dc/d40/classApp_1_1PropertyFloatList.html#a602bb1a4bae4daee9223f26201d96795),
[App::PropertyStringList::Restore()](../../d8/d55/classApp_1_1PropertyStringList.html#a63237fa5b3eaf0a6fc3a051d5a6e9bcf),
[App::PropertyBoolList::Restore()](../../d1/dcf/classApp_1_1PropertyBoolList.html#ab04174271d33c19c037c99c930e25a7e),
[App::PropertyColorList::Restore()](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73),
[App::PropertyMaterialList::Restore()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a8ea57c6a941944daa32ea5ab471b8877),
[App::PropertyPersistentObject::Restore()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a13c0f90fcb93033f1114904553aaee4c),
[Sketcher::PropertyConstraintList::Restore()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#aa6e11dd2fcd1f2307c14e3df94e4fbe7),
[Spreadsheet::PropertySheet::Restore()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5682de0cd8471dd97ec68393abec332a),
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab),
and
[Base::Persistence::restoreFromStream()](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd).

## ◆ readEndElement()

void Base::XMLReader::readEndElement  | ( | const char *  | _ElementName_ = `nullptr`,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _level_ = `-1`  
| ) | |   
  
read until an end element is found

Parameters

     ElementName| optional end element name to look for. If given, then the parser will read until this name is found.  
---|---  
level| optional level to look for. If given, then the parser will read until
this level. Note that the parse only increase the level when finding a start
element, not start-end element, and decrease the level after finding an end
element. So, if you obtain the parser level after calling
[readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e
"read until a start element is found \(<name>\) or start-end element
\(<name/>\) \(with special name if giv..."), you should specify a level minus
one when calling this function. This `level` parameter is only useful if you
know the child element may have the same name as its parent, otherwise, using
`ElementName` is enough.  
  
Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[MeshCore::MeshInput::LoadXML()](../../d9/d08/classMeshCore_1_1MeshInput.html#a86550f4aa655451367800cbc22aa1afb),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Part::Geometry::Restore()](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Part::GeomBSplineCurve::Restore()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#a4729db2206213978ad19f3f242179483),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::Generic::Restore()](../../dd/d23/classTechDraw_1_1Generic.html#a8850e5eb8a34c47b152b62fafe77905d),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyEnumeration::Restore()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyIntegerSet::Restore()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a2326110666959447c4218d46d2d30dd7),
[App::PropertyMap::Restore()](../../db/d3f/classApp_1_1PropertyMap.html#a9362c746cddf00578f7c2772133b2419),
[Gui::DocumentItem::ExpandInfo::restore()](../../dc/dd6/classDocumentItem_1_1ExpandInfo.html#ad851dd90613261db134bdfeef8d1ff58),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[Spreadsheet::PropertyColumnWidths::Restore()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a3e5f54a360a79e8a1ada41e549fdb51f),
[Spreadsheet::PropertyRowHeights::Restore()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a63938d46c9385cca14d404ffa9ccbb74),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::PropertyExpressionEngine::Restore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkSubList::Restore()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995),
[App::PropertyXLinkContainer::Restore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4),
[App::PropertyIntegerList::Restore()](../../d7/daa/classApp_1_1PropertyIntegerList.html#aae0652a9de7572ada2cdb818c54e29ef),
[App::PropertyStringList::Restore()](../../d8/d55/classApp_1_1PropertyStringList.html#a63237fa5b3eaf0a6fc3a051d5a6e9bcf),
[App::PropertyPersistentObject::Restore()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a13c0f90fcb93033f1114904553aaee4c),
[Sketcher::PropertyConstraintList::Restore()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#aa6e11dd2fcd1f2307c14e3df94e4fbe7),
[Spreadsheet::PropertySheet::Restore()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5682de0cd8471dd97ec68393abec332a),
and
[App::ExtensionContainer::restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab).

## ◆ readFiles()

void Base::XMLReader::readFiles  | ( | [zipios::ZipInputStream](../../d0/d1f/classzipios_1_1ZipInputStream.html) & | _zipstream_| ) |  const  
---|---|---|---|---|---  
  
process the requested file writes

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::Reader::getLocalReader()](../../d1/d1f/classBase_1_1Reader.html#a6769c159644cf3be618ebfb69338cb6c),
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
[zipios::ZipInputStream::getNextEntry()](../../d0/d1f/classzipios_1_1ZipInputStream.html#aac1f1733bc10d3c21a1a7d5de7abc7b1),
and
[Base::SequencerLauncher::next()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a).

Referenced by
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[Base::Persistence::restoreFromStream()](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd).

## ◆ resetDocument()

| void Base::XMLReader::resetDocument  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
## ◆ resetErrors()

| void Base::XMLReader::resetErrors  | ( | | ) |   
---|---|---|---|---  
protected  
  
## ◆ setPartialRestore()

void Base::XMLReader::setPartialRestore  | ( | [bool](../../d9/db9/classbool.html) | _on_| ) |   
---|---|---|---|---|---  
  
sets simultaneously the global and local PartialRestore bits

Referenced by
[Part::GeomLineSegment::Restore()](../../d9/d6f/classPart_1_1GeomLineSegment.html#aa9c977ad83ada922a774ef226d9b092d),
and
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

## ◆ setStatus()

void Base::XMLReader::setStatus  | ( | [ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50) | _pos_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _on_  
| ) | |   
  
set the status bits

## ◆ setVerbose()

void Base::XMLReader::setVerbose  | ( | [bool](../../d9/db9/classbool.html) | _on_| ) |   
---|---|---|---|---|---  
  
Referenced by
[App::MergeDocuments::importObjects()](../../d6/d0c/classApp_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6).

## ◆ startCDATA()

| void Base::XMLReader::startCDATA  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
## ◆ startDocument()

| void Base::XMLReader::startDocument  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
## ◆ startElement()

| void Base::XMLReader::startElement  | ( | const XMLCh *const  | _uri_ ,   
---|---|---|---  
|  | const XMLCh *const  | _localname_ ,   
|  | const XMLCh *const  | _qname_ ,   
|  | const XERCES_CPP_NAMESPACE_QUALIFIER Attributes & | _attrs_  
| ) | |   
protectedvirtual  
  
References
[StrX::c_str()](../../d2/d3f/classStrX.html#ac350b620adc70fb4cdcb4f5bfdd0f07e),
and
[StrXUTF8::c_str()](../../d7/d9a/classStrXUTF8.html#a218aa95a70fba7010872cb66eb83ac3c).

## ◆ testStatus()

[bool](../../d9/db9/classbool.html) Base::XMLReader::testStatus  | ( | [ReaderStatus](../../dc/d95/classBase_1_1XMLReader.html#a738ab4c9a417f97633ca0d15797dea50) | _pos_| ) |  const  
---|---|---|---|---|---  
  
return the status bits

Referenced by
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[Part::PropertyGeometryList::Restore()](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[TechDraw::PropertyCenterLineList::Restore()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList::Restore()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList::Restore()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList::Restore()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ warning()

| void Base::XMLReader::warning  | ( | const XERCES_CPP_NAMESPACE_QUALIFIER SAXParseException & | _exc_| ) |   
---|---|---|---|---|---  
protected  
  
## Member Data Documentation

## ◆ AttrMap

| std::map<std::string,std::string> Base::XMLReader::AttrMap  
---  
protected  
  
## ◆ CharacterCount

| unsigned [int](../../d1/da0/classint.html) Base::XMLReader::CharacterCount  
---  
protected  
  
## ◆ Characters

| std::string Base::XMLReader::Characters  
---  
protected  
  
## ◆ DocumentSchema

[int](../../d1/da0/classint.html) Base::XMLReader::DocumentSchema  
---  
  
Schema Version of the document.

Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[Points::PointKernel::Restore()](../../dc/de1/classPoints_1_1PointKernel.html#af4c6a89cb77c9799928d858ddcaad09c),
[Points::PropertyPointKernel::Restore()](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
and
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82).

## ◆ FileList

std::vector<[FileEntry](../../d4/d0e/structBase_1_1XMLReader_1_1FileEntry.html)>
Base::XMLReader::FileList  
---  
  
## ◆ FileNames

| std::vector<std::string> Base::XMLReader::FileNames  
---  
protected  
  
## ◆ FileVersion

[int](../../d1/da0/classint.html) Base::XMLReader::FileVersion  
---  
  
Version of the file format.

Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
and
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82).

## ◆ Level

| [int](../../d1/da0/classint.html) Base::XMLReader::Level  
---  
protected  
  
## ◆ LocalName

| std::string Base::XMLReader::LocalName  
---  
protected  
  
## ◆ parser

| XERCES_CPP_NAMESPACE_QUALIFIER SAX2XMLReader* Base::XMLReader::parser  
---  
protected  
  
Referenced by
[XMLReader()](../../dc/d95/classBase_1_1XMLReader.html#a99f834c210330c8cb20eaf5e2e74f8d7).

## ◆ ProgramVersion

std::string Base::XMLReader::ProgramVersion  
---  
  
Version of FreeCAD that wrote this document.

Referenced by
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆

enum { ... } Base::XMLReader::ReadType  
---  
  
## ◆ StatusBits

| std::bitset<32> Base::XMLReader::StatusBits  
---  
protected  
  
## ◆ token

| XERCES_CPP_NAMESPACE_QUALIFIER XMLPScanToken Base::XMLReader::token  
---  
protected  
  
Referenced by
[XMLReader()](../../dc/d95/classBase_1_1XMLReader.html#a99f834c210330c8cb20eaf5e2e74f8d7).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Reader.h
  * FreeCAD/src/Base/Reader.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

