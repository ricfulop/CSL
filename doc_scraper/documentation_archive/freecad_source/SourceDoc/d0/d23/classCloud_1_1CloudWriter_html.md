---
url: https://freecad.github.io/SourceDoc/d0/d23/classCloud_1_1CloudWriter.html
scraped_at: 2025-09-08T15:19:27.685119
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Cloud](../../d9/dea/namespaceCloud.html)
  * [CloudWriter](../../d0/d23/classCloud_1_1CloudWriter.html)

[List of all members](../../dc/d8d/classCloud_1_1CloudWriter-members.html) | Public Member Functions | Public Attributes | Protected Attributes

Cloud::CloudWriter Class Reference

`#include <AppCloud.h>`

##  Public Member Functions  
  
---  
void | [checkElement](../../d0/d23/classCloud_1_1CloudWriter.html#a576145190d140e4ca333b32fd5b65cad) (XERCES_CPP_NAMESPACE_QUALIFIER DOMElement *element)  
void | [checkText](../../d0/d23/classCloud_1_1CloudWriter.html#a97c7b33bafd8f974418157323462de48) (XERCES_CPP_NAMESPACE_QUALIFIER DOMText *text)  
void | [checkXML](../../d0/d23/classCloud_1_1CloudWriter.html#a3ef54778f420a5e0523232e37e1cd03c) (XERCES_CPP_NAMESPACE_QUALIFIER DOMNode *node)  
|
[CloudWriter](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f)
(const char
*[URL](../../d0/d23/classCloud_1_1CloudWriter.html#a3275777793ea5cd1f0d2b8151c769585),
const char
*[TokenAuth](../../d0/d23/classCloud_1_1CloudWriter.html#ac5729b940a1c7970bd7dadec7a8326c8),
const char
*[TokenSecret](../../d0/d23/classCloud_1_1CloudWriter.html#aba6c73c68e13e5ad871f670de388c881),
const char
*[TCPPort](../../d0/d23/classCloud_1_1CloudWriter.html#abee676c6989f239b3d380759811adee9),
const char
*[Bucket](../../d0/d23/classCloud_1_1CloudWriter.html#acc54b1caab69e1e7da66f73e3338317f),
std::string
[ProtocolVersion](../../d0/d23/classCloud_1_1CloudWriter.html#a0daec43b4fc5d4fd03cc7977717e4d11),
std::string
[Region](../../d0/d23/classCloud_1_1CloudWriter.html#a715c99a65b4be9539930810732404b94))  
void | [createBucket](../../d0/d23/classCloud_1_1CloudWriter.html#a32629112f9daf1c94c2ee29c66298b3c) ()  
void | [pushCloud](../../d0/d23/classCloud_1_1CloudWriter.html#a2cde2d5d92835fcc17d47d7215445626) (const char *[FileName](../../d0/d23/classCloud_1_1CloudWriter.html#ac0d23ec2e61c1dcc126d60bc22f49734), const char *data, long size)  
void | [putNextEntry](../../d0/d23/classCloud_1_1CloudWriter.html#a717c543549341700a14e070ba4d9e4c0) (const char *file)  
virtual [bool](../../d9/db9/classbool.html) | [shouldWrite](../../d0/d23/classCloud_1_1CloudWriter.html#a31e85dec05649a6a168ccb718035a233) (const std::string &name, const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *Object) const  
virtual std::ostream & | [Stream](../../d0/d23/classCloud_1_1CloudWriter.html#ac6dec3675fe3bead371f8d345b707dc6) (void)  
virtual void | [writeFiles](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38) (void)  
| process the requested file storing
[More...](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38)  
  
virtual | [~CloudWriter](../../d0/d23/classCloud_1_1CloudWriter.html#ad553c58159854ba17021b201e8b762b3) ()  
![-](../../closed.png) Public Member Functions inherited from
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html)  
[int](../../d1/da0/classint.html) | [getFileVersion](../../dd/d4d/classBase_1_1Writer.html#aaf8877bfc94b43f802bbe6b41fadf7ed) () const  
void | [insertAsciiFile](../../dd/d4d/classBase_1_1Writer.html#ac188706203bae688ddec31a05e57425d) (const char *FileName)  
| insert a file as CDATA section in the XML file
[More...](../../dd/d4d/classBase_1_1Writer.html#ac188706203bae688ddec31a05e57425d)  
  
void | [insertBinFile](../../dd/d4d/classBase_1_1Writer.html#aafe5f2af569301dbae674de29e757de4) (const char *FileName)  
| insert a binary file BASE64 coded as CDATA section in the XML file
[More...](../../dd/d4d/classBase_1_1Writer.html#aafe5f2af569301dbae674de29e757de4)  
  
[bool](../../d9/db9/classbool.html) | [isForceXML](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6) ()  
| check on state
[More...](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6)  
  
void | [setFileVersion](../../dd/d4d/classBase_1_1Writer.html#a2fed004ddd6bc5ba1793d9344db63291) ([int](../../d1/da0/classint.html))  
void | [setForceXML](../../dd/d4d/classBase_1_1Writer.html#af7c44d252aa9e28e3fcdce658bcb6e58) ([bool](../../d9/db9/classbool.html) on)  
| switch the writer in XML only mode (no files allowed)
[More...](../../dd/d4d/classBase_1_1Writer.html#af7c44d252aa9e28e3fcdce658bcb6e58)  
  
|
[Writer](../../dd/d4d/classBase_1_1Writer.html#aedc04cd5fb7b4b99d3ad906fef2116ce)
()  
virtual | [~Writer](../../dd/d4d/classBase_1_1Writer.html#a6f57399b94731301d267ce10a2f52ea3) ()  
std::string | [addFile](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55) (const char *Name, const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *Object)  
| add a write request of a persistent object
[More...](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55)  
  
const std::vector< std::string > & | [getFilenames](../../dd/d4d/classBase_1_1Writer.html#a6cc1724ce9808ed9d010057a45c0fd6b) () const  
| get all registered file names
[More...](../../dd/d4d/classBase_1_1Writer.html#a6cc1724ce9808ed9d010057a45c0fd6b)  
  
void | [setMode](../../dd/d4d/classBase_1_1Writer.html#a3a26c2bb6285dcd29c97037cdda5042e) (const std::string &mode)  
| Set mode.
[More...](../../dd/d4d/classBase_1_1Writer.html#a3a26c2bb6285dcd29c97037cdda5042e)  
  
void | [setModes](../../dd/d4d/classBase_1_1Writer.html#ada4367ab704c07fc4347bb6055c88f1c) (const std::set< std::string > &modes)  
| Set modes.
[More...](../../dd/d4d/classBase_1_1Writer.html#ada4367ab704c07fc4347bb6055c88f1c)  
  
[bool](../../d9/db9/classbool.html) | [getMode](../../dd/d4d/classBase_1_1Writer.html#a67a2c785c2554167b104bad578ae5c83) (const std::string &mode) const  
| Get mode.
[More...](../../dd/d4d/classBase_1_1Writer.html#a67a2c785c2554167b104bad578ae5c83)  
  
std::set< std::string > | [getModes](../../dd/d4d/classBase_1_1Writer.html#a86e86c861b4596a5470e64b06749154f) () const  
| Get modes.
[More...](../../dd/d4d/classBase_1_1Writer.html#a86e86c861b4596a5470e64b06749154f)  
  
void | [clearMode](../../dd/d4d/classBase_1_1Writer.html#a4c81edd99ae05bebdeec57cc65f371e1) (const std::string &mode)  
| Clear mode.
[More...](../../dd/d4d/classBase_1_1Writer.html#a4c81edd99ae05bebdeec57cc65f371e1)  
  
void | [clearModes](../../dd/d4d/classBase_1_1Writer.html#aaa6ac018d7d3fc0f8215e785b9d2918d) ()  
| Clear modes.
[More...](../../dd/d4d/classBase_1_1Writer.html#aaa6ac018d7d3fc0f8215e785b9d2918d)  
  
void | [addError](../../dd/d4d/classBase_1_1Writer.html#a060e45ed91863b5535fa9c9721dde11f) (const std::string &)  
[bool](../../d9/db9/classbool.html) | [hasErrors](../../dd/d4d/classBase_1_1Writer.html#a63b47ea7f6739149a2df8c4bf6344f3a) () const  
void | [clearErrors](../../dd/d4d/classBase_1_1Writer.html#af772e74bbf7a1dd181af9fb5dfc94ccc) ()  
std::vector< std::string > | [getErrors](../../dd/d4d/classBase_1_1Writer.html#a0a8724e4f558be340dce98381cfc6097) () const  
const char * | [ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368) () const  
| get the current indentation
[More...](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368)  
  
void | [incInd](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5) ()  
| increase indentation by one tab
[More...](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5)  
  
void | [decInd](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92) ()  
| decrease indentation by one tab
[More...](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92)  
  
  
##  Public Attributes  
  
---  
char | [errorCode](../../d0/d23/classCloud_1_1CloudWriter.html#a505d5df8b7208888690f74730fb5680a) [1024] =""  
[int](../../d1/da0/classint.html) | [print](../../d0/d23/classCloud_1_1CloudWriter.html#a81f0fa66497b20cd6440bf81a3c11781) =0  
![-](../../closed.png) Public Attributes inherited from
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html)  
std::string | [ObjectName](../../dd/d4d/classBase_1_1Writer.html#a33392412488d03635dfb4527e3df677d)  
| name for underlying file saves
[More...](../../dd/d4d/classBase_1_1Writer.html#a33392412488d03635dfb4527e3df677d)  
  
  
##  Protected Attributes  
  
---  
const char * | [Bucket](../../d0/d23/classCloud_1_1CloudWriter.html#acc54b1caab69e1e7da66f73e3338317f)  
std::string | [FileName](../../d0/d23/classCloud_1_1CloudWriter.html#ac0d23ec2e61c1dcc126d60bc22f49734)  
std::stringstream | [FileStream](../../d0/d23/classCloud_1_1CloudWriter.html#abbe1245bc8afdce6755eb5cc1e59fe80)  
std::string | [ProtocolVersion](../../d0/d23/classCloud_1_1CloudWriter.html#a0daec43b4fc5d4fd03cc7977717e4d11)  
std::string | [Region](../../d0/d23/classCloud_1_1CloudWriter.html#a715c99a65b4be9539930810732404b94)  
const char * | [TCPPort](../../d0/d23/classCloud_1_1CloudWriter.html#abee676c6989f239b3d380759811adee9)  
const char * | [TokenAuth](../../d0/d23/classCloud_1_1CloudWriter.html#ac5729b940a1c7970bd7dadec7a8326c8)  
const char * | [TokenSecret](../../d0/d23/classCloud_1_1CloudWriter.html#aba6c73c68e13e5ad871f670de388c881)  
const char * | [URL](../../d0/d23/classCloud_1_1CloudWriter.html#a3275777793ea5cd1f0d2b8151c769585)  
![-](../../closed.png) Protected Attributes inherited from
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html)  
std::vector< [FileEntry](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html) > | [FileList](../../dd/d4d/classBase_1_1Writer.html#a364da33cc8f9237793691c1ed545b866)  
std::vector< std::string > | [FileNames](../../dd/d4d/classBase_1_1Writer.html#afaea6adc505c9a950ce2b6385a7fec2c)  
std::vector< std::string > | [Errors](../../dd/d4d/classBase_1_1Writer.html#a20d9a8919ae090e2910a0b8068e7ff62)  
std::set< std::string > | [Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd)  
short | [indent](../../dd/d4d/classBase_1_1Writer.html#a51f1a622cb20d7dceb19ec58b1a111c5)  
char | [indBuf](../../dd/d4d/classBase_1_1Writer.html#acb8178b1adf60b3f6b58db2324456062) [1024]  
[bool](../../d9/db9/classbool.html) | [forceXML](../../dd/d4d/classBase_1_1Writer.html#aac5ceb3ba47d3598d2e357fe9c2afab1)  
[int](../../d1/da0/classint.html) | [fileVersion](../../dd/d4d/classBase_1_1Writer.html#ade28c77127289e039bc9eeccfe40ff61)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Protected Member Functions inherited from
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html)  
std::string | [getUniqueFileName](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc) (const char *Name)  
  
## Constructor & Destructor Documentation

## ◆ CloudWriter()

Cloud::CloudWriter::CloudWriter  | ( | const char *  | _URL_ ,   
---|---|---|---  
|  | const char *  | _TokenAuth_ ,   
|  | const char *  | _TokenSecret_ ,   
|  | const char *  | _TCPPort_ ,   
|  | const char *  | _Bucket_ ,   
|  | std::string  | _ProtocolVersion_ ,   
|  | std::string  | _Region_  
| ) | |   
  
References
[Cloud::BuildHeaderAmzS3v2()](../../d9/dea/namespaceCloud.html#a2537fd6ec769988ae3664f50a776fbbf),
[Cloud::BuildHeaderAmzS3v4()](../../d9/dea/namespaceCloud.html#a068954d887c1095aacd27be7c5bb35ed),
[Cloud::ComputeDigestAmzS3v2()](../../d9/dea/namespaceCloud.html#a7553aac877d630c37c9dc682752fca09),
[Cloud::ComputeDigestAmzS3v4()](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb),
[Cloud::CurlWrite_CallbackFunc_StdString()](../../d9/dea/namespaceCloud.html#a0706f2042a82b5e6a6375577359be029),
[Cloud::eraseSubStr()](../../d9/dea/namespaceCloud.html#a200581597cdfe01a88dfcc0b5d3f8529),
and
[Cloud::AmzDatav4::Region](../../d0/d4c/structCloud_1_1AmzDatav4.html#a2e3346dbf668d8bf9307b75b9c654db0).

## ◆ ~CloudWriter()

| Cloud::CloudWriter::~CloudWriter  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ checkElement()

void Cloud::CloudWriter::checkElement  | ( | XERCES_CPP_NAMESPACE_QUALIFIER DOMElement *  | _element_| ) |   
---|---|---|---|---|---  
  
## ◆ checkText()

void Cloud::CloudWriter::checkText  | ( | XERCES_CPP_NAMESPACE_QUALIFIER DOMText *  | _text_| ) |   
---|---|---|---|---|---  
  
## ◆ checkXML()

void Cloud::CloudWriter::checkXML  | ( | XERCES_CPP_NAMESPACE_QUALIFIER DOMNode *  | _node_| ) |   
---|---|---|---|---|---  
  
## ◆ createBucket()

void Cloud::CloudWriter::createBucket  | ( | | ) |   
---|---|---|---|---  
  
References
[Cloud::BuildHeaderAmzS3v2()](../../d9/dea/namespaceCloud.html#a2537fd6ec769988ae3664f50a776fbbf),
[Cloud::BuildHeaderAmzS3v4()](../../d9/dea/namespaceCloud.html#a068954d887c1095aacd27be7c5bb35ed),
[Cloud::ComputeDigestAmzS3v2()](../../d9/dea/namespaceCloud.html#a7553aac877d630c37c9dc682752fca09),
[Cloud::ComputeDigestAmzS3v4()](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb),
[Cloud::eraseSubStr()](../../d9/dea/namespaceCloud.html#a200581597cdfe01a88dfcc0b5d3f8529),
[data_buffer::ptr](../../d3/de5/structdata__buffer.html#a27a38134de532365231f8ba9955e4fc6),
and
[data_buffer::remaining_size](../../d3/de5/structdata__buffer.html#a23df2b8d541738b0ee06d796364aad49).

## ◆ pushCloud()

void Cloud::CloudWriter::pushCloud  | ( | const char *  | _FileName_ ,   
---|---|---|---  
|  | const char *  | _data_ ,   
|  | long  | _size_  
| ) | |   
  
References
[Cloud::BuildHeaderAmzS3v2()](../../d9/dea/namespaceCloud.html#a2537fd6ec769988ae3664f50a776fbbf),
[Cloud::BuildHeaderAmzS3v4()](../../d9/dea/namespaceCloud.html#a068954d887c1095aacd27be7c5bb35ed),
[Cloud::ComputeDigestAmzS3v2()](../../d9/dea/namespaceCloud.html#a7553aac877d630c37c9dc682752fca09),
[Cloud::ComputeDigestAmzS3v4()](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb),
[Cloud::eraseSubStr()](../../d9/dea/namespaceCloud.html#a200581597cdfe01a88dfcc0b5d3f8529),
[data_buffer::ptr](../../d3/de5/structdata__buffer.html#a27a38134de532365231f8ba9955e4fc6),
and
[data_buffer::remaining_size](../../d3/de5/structdata__buffer.html#a23df2b8d541738b0ee06d796364aad49).

## ◆ putNextEntry()

void Cloud::CloudWriter::putNextEntry  | ( | const char *  | _file_| ) |   
---|---|---|---|---|---  
  
References
[Cloud::CloudReader::file](../../d2/de7/classCloud_1_1CloudReader.html#a39c8cc4ce055ec185a0535d0920ca2ae),
[Cloud::CloudReader::FileEntry::FileName](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#aaacf4f1a4c7b1beaa85fca81ac51ba85),
and
[Cloud::CloudReader::FileEntry::FileStream](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#ac85e8a4839a51dfab009594b596fba07).

Referenced by
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71).

## ◆ shouldWrite()

| [bool](../../d9/db9/classbool.html) Cloud::CloudWriter::shouldWrite  | ( | const std::string & | _name_ ,   
---|---|---|---  
|  | const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *  | _Object_  
| ) | |  const  
virtual  
  
## ◆ Stream()

| virtual std::ostream & Cloud::CloudWriter::Stream  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Implements
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71).

## ◆ writeFiles()

| void Cloud::CloudWriter::writeFiles  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
process the requested file storing

Implements
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html#a4ac216f6afc4c088950ae53dc75a9e2d).

References
[Base::Writer::FileEntry::FileName](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#abd6c12817010758a25f9af39c2c3a70c),
[Base::Writer::FileEntry::Object](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#a15a35046c9bd5dad11dd5d97c18d675f),
and
[Base::Persistence::SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45).

Referenced by
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71).

## Member Data Documentation

## ◆ Bucket

| const char* Cloud::CloudWriter::Bucket  
---  
protected  
  
## ◆ errorCode

char Cloud::CloudWriter::errorCode[1024] =""  
---  
  
## ◆ FileName

| std::string Cloud::CloudWriter::FileName  
---  
protected  
  
## ◆ FileStream

| std::stringstream Cloud::CloudWriter::FileStream  
---  
protected  
  
## ◆ print

[int](../../d1/da0/classint.html) Cloud::CloudWriter::print =0  
---  
  
## ◆ ProtocolVersion

| std::string Cloud::CloudWriter::ProtocolVersion  
---  
protected  
  
## ◆ Region

| std::string Cloud::CloudWriter::Region  
---  
protected  
  
## ◆ TCPPort

| const char* Cloud::CloudWriter::TCPPort  
---  
protected  
  
## ◆ TokenAuth

| const char* Cloud::CloudWriter::TokenAuth  
---  
protected  
  
## ◆ TokenSecret

| const char* Cloud::CloudWriter::TokenSecret  
---  
protected  
  
## ◆ URL

| const char* Cloud::CloudWriter::URL  
---  
protected  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Cloud/App/AppCloud.h
  * FreeCAD/src/Mod/Cloud/App/AppCloud.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

