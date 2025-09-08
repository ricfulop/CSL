---
url: https://freecad.github.io/SourceDoc/d6/d0c/classApp_1_1MergeDocuments.html
scraped_at: 2025-09-08T14:55:06.602050
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html)

[List of all members](../../d7/d4c/classApp_1_1MergeDocuments-members.html) | Public Member Functions

App::MergeDocuments Class Reference

`#include <MergeDocuments.h>`

##  Public Member Functions  
  
---  
void | [exportObject](../../d6/d0c/classApp_1_1MergeDocuments.html#a76cbe05edd195053458a8fe80ac661ec) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &o, [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &w)  
unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d6/d0c/classApp_1_1MergeDocuments.html#af48ade47d965eec0fc69a895b163d761) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d6/d0c/classApp_1_1MergeDocuments.html#af48ade47d965eec0fc69a895b163d761)  
  
const std::map< std::string, std::string > & | [getNameMap](../../d6/d0c/classApp_1_1MergeDocuments.html#aaeb37ec63dcd5d3d2fedaaf4e9774a57) () const  
void | [importObject](../../d6/d0c/classApp_1_1MergeDocuments.html#aabdb85b2cd55e6354b1a706a8bf912b4) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &o, [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &r)  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [importObjects](../../d6/d0c/classApp_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6) (std::istream &)  
[bool](../../d9/db9/classbool.html) | [isVerbose](../../d6/d0c/classApp_1_1MergeDocuments.html#a52d742af95850049554a42a8883508a8) () const  
|
[MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#aabfd8fec3eb7938a5af2e14c18e50a76)
([App::Document](../../d8/d3e/classApp_1_1Document.html) *doc)  
void | [Restore](../../d6/d0c/classApp_1_1MergeDocuments.html#a42b6e5f8e2e91b8be37bb5c1e89a331f) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &r)  
| This method is used to restore properties from an XML document.
[More...](../../d6/d0c/classApp_1_1MergeDocuments.html#a42b6e5f8e2e91b8be37bb5c1e89a331f)  
  
void | [RestoreDocFile](../../d6/d0c/classApp_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967) ([Base::Reader](../../d1/d1f/classBase_1_1Reader.html) &r)  
| This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b
"This method is used to save large amounts of data to a binary file.") saved
data.
[More...](../../d6/d0c/classApp_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967)  
  
void | [Save](../../d6/d0c/classApp_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &w) const  
| This method is used to save properties to an XML document.
[More...](../../d6/d0c/classApp_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c)  
  
void | [SaveDocFile](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &w) const  
| This method is used to save large amounts of data to a binary file.
[More...](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b)  
  
void | [setVerbose](../../d6/d0c/classApp_1_1MergeDocuments.html#aed8da7ec5b0b0acbc0ad0d0a7b029f62) ([bool](../../d9/db9/classbool.html) on)  
|
[~MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#a616572ec9445a6dc476c2745edf51cb3)
()  
![-](../../closed.png) Public Member Functions inherited from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)  
void | [dumpToStream](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7) (std::ostream &stream, [int](../../d1/da0/classint.html) compression)  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9) () const =0  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9)  
  
virtual [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596) (void) const  
virtual void | [Restore](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc) ([XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)=0  
| This method is used to restore properties from an XML document.
[More...](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc)  
  
virtual void | [RestoreDocFile](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b) ([Reader](../../d1/d1f/classBase_1_1Reader.html) &)  
| This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45
"This method is used to save large amounts of data to a binary file.") saved
data.
[More...](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b)  
  
void | [restoreFromStream](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd) (std::istream &stream)  
virtual void | [Save](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436) ([Writer](../../dd/d4d/classBase_1_1Writer.html) &) const =0  
| This method is used to save properties to an XML document.
[More...](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436)  
  
virtual void | [SaveDocFile](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45) ([Writer](../../dd/d4d/classBase_1_1Writer.html) &) const  
| This method is used to save large amounts of data to a binary file.
[More...](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45)  
  
![-](../../closed.png) Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)
()  
| Construction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)  
  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#ae41bc09a1498fbd4e952e7a7dd9de791)
(const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514)  
  
virtual [Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566) () const  
[bool](../../d9/db9/classbool.html) | [isDerivedFrom](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | [operator=](../../df/d4d/classBase_1_1BaseClass.html#ad334dfcaf7aa8b86993eaefac41207c2) (const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual void | [setPyObject](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual | [~BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49) ()  
| Destruction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)  
static void * | [create](../../d9/d25/classBase_1_1Persistence.html#a8cecc55259bc79661a33a2d8df9764b7) (void)  
static std::string | [encodeAttribute](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec) (const std::string &)  
| Encodes an attribute upon saving.
[More...](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec)  
  
static [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56) (void)  
static void | [init](../../d9/d25/classBase_1_1Persistence.html#a4e9f73ac099dd794f6c87946f61cee0e) (void)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Constructor & Destructor Documentation

## ◆ MergeDocuments()

MergeDocuments::MergeDocuments  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
  
References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[exportObject()](../../d6/d0c/classApp_1_1MergeDocuments.html#a76cbe05edd195053458a8fe80ac661ec),
and
[importObject()](../../d6/d0c/classApp_1_1MergeDocuments.html#aabdb85b2cd55e6354b1a706a8bf912b4).

## ◆ ~MergeDocuments()

MergeDocuments::~MergeDocuments  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ exportObject()

void MergeDocuments::exportObject  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _o_ ,   
---|---|---|---  
|  | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | _w_  
| ) | |   
  
References
[Save()](../../d6/d0c/classApp_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c).

Referenced by
[MergeDocuments()](../../d6/d0c/classApp_1_1MergeDocuments.html#aabfd8fec3eb7938a5af2e14c18e50a76).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) MergeDocuments::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9).

## ◆ getNameMap()

const std::map< std::string, std::string > & App::MergeDocuments::getNameMap  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::Document::importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778).

## ◆ importObject()

void MergeDocuments::importObject  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _o_ ,   
---|---|---|---  
|  | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _r_  
| ) | |   
  
References
[Restore()](../../d6/d0c/classApp_1_1MergeDocuments.html#a42b6e5f8e2e91b8be37bb5c1e89a331f).

Referenced by
[MergeDocuments()](../../d6/d0c/classApp_1_1MergeDocuments.html#aabfd8fec3eb7938a5af2e14c18e50a76).

## ◆ importObjects()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > MergeDocuments::importObjects  | ( | std::istream & | _input_| ) |   
---|---|---|---|---|---  
  
References
[App::Document::importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
[isVerbose()](../../d6/d0c/classApp_1_1MergeDocuments.html#a52d742af95850049554a42a8883508a8),
and
[Base::XMLReader::setVerbose()](../../dc/d95/classBase_1_1XMLReader.html#aaea2a3e84a2f7c2dc22bf4d66bf2c6f4).

Referenced by
[App::Document::copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
and
[App::Document::importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778).

## ◆ isVerbose()

[bool](../../d9/db9/classbool.html) App::MergeDocuments::isVerbose  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[importObjects()](../../d6/d0c/classApp_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6).

## ◆ Restore()

| void MergeDocuments::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d6/d0c/classApp_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c
"This method is used to save properties to an XML document.") written
information. Again the Vector as an example:

void
[PropertyVector::Restore](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c
"This method is used to restore properties from an XML
document.")([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The
XML reader class This is an important helper class for the store and retrieval
system of objects ...") &reader)

{

// read my Element

reader.[readElement](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e
"read until a start element is found \(<name>\) or start-end element
\(<name/>\) \(with special name if giv...")("PropertyVector");

// get the value of my Attribute

_cVec.x =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueX");

_cVec.y =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueY");

_cVec.z =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueZ");

}

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc).

Referenced by
[importObject()](../../d6/d0c/classApp_1_1MergeDocuments.html#aabdb85b2cd55e6354b1a706a8bf912b4).

## ◆ RestoreDocFile()

| void MergeDocuments::RestoreDocFile  | ( | [Base::Reader](../../d1/d1f/classBase_1_1Reader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b
"This method is used to save large amounts of data to a binary file.") saved
data.

Again you have to apply for the call of this method in the
[Restore()](../../d6/d0c/classApp_1_1MergeDocuments.html#a42b6e5f8e2e91b8be37bb5c1e89a331f
"This method is used to restore properties from an XML document.") call:

void
PropertyMeshKernel::Restore([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html
"The XML reader class This is an important helper class for the store and
retrieval system of objects ...") &reader)

{

reader.[readElement](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e
"read until a start element is found \(<name>\) or start-end element
\(<name/>\) \(with special name if giv...")("Mesh");

std::string file
(reader.[getAttribute](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788
"return the named attribute as a double floating point \(does type
checking\)")("file") );

if(file == "")

{

// read XML

MeshCore::MeshDocXML restorer(*_pcMesh);

restorer.Restore(reader);

}else{

// initiate a file read

reader.[addFile](../../dc/d95/classBase_1_1XMLReader.html#adf371fa6365af1b80097055bebf87dfe
"add a read request of a persistent object")(file.c_str(),this);

}

}

After you issued the reader.addFile() your
[RestoreDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967
"This method is used to restore large amounts of data from a file In this
method you simply stream in ...") is called:

void
PropertyMeshKernel::RestoreDocFile([Base::Reader](../../d1/d1f/classBase_1_1Reader.html)
&reader)

{

_pcMesh->Read( reader );

}

See also

    [Base::Reader](../../d1/d1f/classBase_1_1Reader.html),[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The XML reader class This is an important helper class for the store and retrieval system of objects ...")

Reimplemented from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b).

References
[App::Document::signalImportViewObjects](../../d8/d3e/classApp_1_1Document.html#a38702e1f0098ffae1da77091590d429e).

## ◆ Save()

| void MergeDocuments::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to save properties to an XML document.

A good example you'll find in PropertyStandard.cpp, e.g. the vector:

void
[PropertyVector::Save](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10
"This method is used to save properties to an XML document.") (Writer &writer)
const

{

writer << writer.ind() << "<PropertyVector valueX=\"" << _cVec.x <<

"\" valueY=\"" << _cVec.y <<

"\" valueZ=\"" << _cVec.z <<"\"/>" << endl;

}

The writer.ind() expression writes the indentation, just for pretty printing
of the XML. As you see, the writing of the XML document is not done with a DOM
implementation because of performance reasons. Therefore the programmer has to
take care that a valid XML document is written. This means closing tags and
writing UTF-8.

See also

    [Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This is an important helper class for the store and retrieval system of persistent o...")

Implements
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436).

Referenced by
[exportObject()](../../d6/d0c/classApp_1_1MergeDocuments.html#a76cbe05edd195053458a8fe80ac661ec).

## ◆ SaveDocFile()

| void MergeDocuments::SaveDocFile  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to save large amounts of data to a binary file.

Sometimes it makes no sense to write property data as XML. In case the amount
of data is too big or the data type has a more effective way to save itself.
In this cases it is possible to write the data in a separate file inside the
document archive. In case you want do so you have to re-implement
[SaveDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b
"This method is used to save large amounts of data to a binary file."). First,
you have to inform the framework in
[Save()](../../d6/d0c/classApp_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c
"This method is used to save properties to an XML document.") that you want do
so. Here an example from the [Mesh](../../dc/d48/namespaceMesh.html "The
namespace of the Mesh Application layer library.") module which can save a
(pontetionaly big) triangle mesh:

void PropertyMeshKernel::Save
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This
is an important helper class for the store and retrieval system of persistent
o...") &writer) const

{

if
(writer.[isForceXML](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6
"check on state")())

{

writer <<
writer.[ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368
"get the current indentation")() << "<Mesh>" << std::endl;

MeshCore::MeshDocXML saver(*_pcMesh);

saver.Save(writer);

}else{

writer <<
writer.[ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368
"get the current indentation")() << "<Mesh file=\"" <<
writer.[addFile](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55
"add a write request of a persistent object")("MeshKernel.bms", this) <<
"\"/>" << std::endl;

}

The writer.isForceXML() is an indication to force you to write XML. Regardless
of size and effectiveness. The second part informs the Base::writer through
writer.addFile("MeshKernel.bms", this) that this object wants to write a file
with the given name. The method addFile() returns a unique name that then is
written in the XML stream. This allows your
[RestoreDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967
"This method is used to restore large amounts of data from a file In this
method you simply stream in ...") method to identify and read the file again.
Later your
[SaveDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b
"This method is used to save large amounts of data to a binary file.") method
is called as many times as you issued the addFile() call:

void PropertyMeshKernel::SaveDocFile
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This
is an important helper class for the store and retrieval system of persistent
o...") &writer) const

{

_pcMesh->Write( writer );

}

In this method you can simply stream your content to the file
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This
is an important helper class for the store and retrieval system of persistent
o...") inheriting from ostream).

Reimplemented from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45).

References
[App::Document::signalExportViewObjects](../../d8/d3e/classApp_1_1Document.html#ae6faa5b2cfe5d182e156e1cc1f937981).

## ◆ setVerbose()

void App::MergeDocuments::setVerbose  | ( | [bool](../../d9/db9/classbool.html) | _on_| ) |   
---|---|---|---|---|---  
  
Referenced by
[App::Document::copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/MergeDocuments.h
  * FreeCAD/src/App/MergeDocuments.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

