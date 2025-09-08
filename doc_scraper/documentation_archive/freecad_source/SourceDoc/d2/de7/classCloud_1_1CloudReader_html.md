---
url: https://freecad.github.io/SourceDoc/d2/de7/classCloud_1_1CloudReader.html
scraped_at: 2025-09-08T15:19:25.630814
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Cloud](../../d9/dea/namespaceCloud.html)
  * [CloudReader](../../d2/de7/classCloud_1_1CloudReader.html)

[List of all members](../../d9/d1a/classCloud_1_1CloudReader-members.html) | Classes | Public Member Functions | Public Attributes | Protected Attributes

Cloud::CloudReader Class Reference

`#include <AppCloud.h>`

##  Classes  
  
---  
struct | [FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html)  
  
##  Public Member Functions  
  
---  
void | [addFile](../../d2/de7/classCloud_1_1CloudReader.html#aa6721854d1f8ec03ab568f99133be83f) (struct [Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) *new_entry)  
void | [checkElement](../../d2/de7/classCloud_1_1CloudReader.html#ac4fca482a13cae371783da1d83caf09e) (XERCES_CPP_NAMESPACE_QUALIFIER DOMElement *element)  
void | [checkText](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a) (XERCES_CPP_NAMESPACE_QUALIFIER DOMText *text)  
void | [checkXML](../../d2/de7/classCloud_1_1CloudReader.html#aa2e1606fd194b8292a5c03c08c0744d2) (XERCES_CPP_NAMESPACE_QUALIFIER DOMNode *node)  
|
[CloudReader](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94)
(const char
*[URL](../../d2/de7/classCloud_1_1CloudReader.html#af79b9b35acb9f6f1ac37f54c841809cb),
const char *AccessKey, const char *SecretKey, const char
*[TCPPort](../../d2/de7/classCloud_1_1CloudReader.html#a194190d077c1d0bde8df18f82c9ccebc),
const char
*[Bucket](../../d2/de7/classCloud_1_1CloudReader.html#a05a70891b71c34026072bf23c4ea27e5),
std::string
[ProtocolVersion](../../d2/de7/classCloud_1_1CloudReader.html#ad4a1f9d531a335661e7f8e0d675a6b45),
std::string
[Region](../../d2/de7/classCloud_1_1CloudReader.html#ae341fa730cc0024ff94b26a6db825563))  
void | [DownloadFile](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085) ([Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) *entry)  
struct [FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) * | [GetEntry](../../d2/de7/classCloud_1_1CloudReader.html#aee8ab3acc0f9cdc7f5360b733cd650a7) (std::string FileName)  
[int](../../d1/da0/classint.html) | [isTouched](../../d2/de7/classCloud_1_1CloudReader.html#a3fc9227c497bad007ec41b54ce52fcfa) (std::string FileName)  
virtual | [~CloudReader](../../d2/de7/classCloud_1_1CloudReader.html#a0be0d94b2cae2af327c063e16c65c47b) ()  
  
##  Public Attributes  
  
---  
[int](../../d1/da0/classint.html) | [continuation](../../d2/de7/classCloud_1_1CloudReader.html#af0c8984dc5abdc2df71fab69bf89f432) =0  
[int](../../d1/da0/classint.html) | [file](../../d2/de7/classCloud_1_1CloudReader.html#a39c8cc4ce055ec185a0535d0920ca2ae) =0  
[int](../../d1/da0/classint.html) | [truncated](../../d2/de7/classCloud_1_1CloudReader.html#abfafda130c0545b486499108c8465d4a) =0  
  
##  Protected Attributes  
  
---  
const char * | [Bucket](../../d2/de7/classCloud_1_1CloudReader.html#a05a70891b71c34026072bf23c4ea27e5)  
std::list< [Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) * > | [FileList](../../d2/de7/classCloud_1_1CloudReader.html#aaf53637ede63872bf94a3a25b6807a64)  
char * | [NextFileName](../../d2/de7/classCloud_1_1CloudReader.html#a1928d7e58da4762f12a03a70e43e0499)  
std::string | [ProtocolVersion](../../d2/de7/classCloud_1_1CloudReader.html#ad4a1f9d531a335661e7f8e0d675a6b45)  
std::string | [Region](../../d2/de7/classCloud_1_1CloudReader.html#ae341fa730cc0024ff94b26a6db825563)  
const char * | [TCPPort](../../d2/de7/classCloud_1_1CloudReader.html#a194190d077c1d0bde8df18f82c9ccebc)  
const char * | [TokenAuth](../../d2/de7/classCloud_1_1CloudReader.html#ab38831e1fe1373d9fd7ba05d797868d7)  
const char * | [TokenSecret](../../d2/de7/classCloud_1_1CloudReader.html#a96b85945d33ef03617666f2c6e8735b0)  
const char * | [URL](../../d2/de7/classCloud_1_1CloudReader.html#af79b9b35acb9f6f1ac37f54c841809cb)  
  
## Constructor & Destructor Documentation

## ◆ CloudReader()

Cloud::CloudReader::CloudReader  | ( | const char *  | _URL_ ,   
---|---|---|---  
|  | const char *  | _AccessKey_ ,   
|  | const char *  | _SecretKey_ ,   
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
[NextFileName](../../d2/de7/classCloud_1_1CloudReader.html#a1928d7e58da4762f12a03a70e43e0499).

## ◆ ~CloudReader()

| Cloud::CloudReader::~CloudReader  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addFile()

void Cloud::CloudReader::addFile  | ( | struct [Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) *  | _new_entry_| ) |   
---|---|---|---|---|---  
  
References
[FileList](../../d2/de7/classCloud_1_1CloudReader.html#aaf53637ede63872bf94a3a25b6807a64).

## ◆ checkElement()

void Cloud::CloudReader::checkElement  | ( | XERCES_CPP_NAMESPACE_QUALIFIER DOMElement *  | _element_| ) |   
---|---|---|---|---|---  
  
Referenced by
[checkXML()](../../d2/de7/classCloud_1_1CloudReader.html#aa2e1606fd194b8292a5c03c08c0744d2).

## ◆ checkText()

void Cloud::CloudReader::checkText  | ( | XERCES_CPP_NAMESPACE_QUALIFIER DOMText *  | _text_| ) |   
---|---|---|---|---|---  
  
References
[continuation](../../d2/de7/classCloud_1_1CloudReader.html#af0c8984dc5abdc2df71fab69bf89f432),
[file](../../d2/de7/classCloud_1_1CloudReader.html#a39c8cc4ce055ec185a0535d0920ca2ae),
[FileList](../../d2/de7/classCloud_1_1CloudReader.html#aaf53637ede63872bf94a3a25b6807a64),
[Cloud::CloudReader::FileEntry::FileName](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#aaacf4f1a4c7b1beaa85fca81ac51ba85),
[NextFileName](../../d2/de7/classCloud_1_1CloudReader.html#a1928d7e58da4762f12a03a70e43e0499),
and
[truncated](../../d2/de7/classCloud_1_1CloudReader.html#abfafda130c0545b486499108c8465d4a).

Referenced by
[checkXML()](../../d2/de7/classCloud_1_1CloudReader.html#aa2e1606fd194b8292a5c03c08c0744d2).

## ◆ checkXML()

void Cloud::CloudReader::checkXML  | ( | XERCES_CPP_NAMESPACE_QUALIFIER DOMNode *  | _node_| ) |   
---|---|---|---|---|---  
  
References
[checkElement()](../../d2/de7/classCloud_1_1CloudReader.html#ac4fca482a13cae371783da1d83caf09e),
[checkText()](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a),
and
[checkXML()](../../d2/de7/classCloud_1_1CloudReader.html#aa2e1606fd194b8292a5c03c08c0744d2).

Referenced by
[checkXML()](../../d2/de7/classCloud_1_1CloudReader.html#aa2e1606fd194b8292a5c03c08c0744d2).

## ◆ DownloadFile()

void Cloud::CloudReader::DownloadFile  | ( | [Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) *  | _entry_| ) |   
---|---|---|---|---|---  
  
References
[Cloud::BuildHeaderAmzS3v2()](../../d9/dea/namespaceCloud.html#a2537fd6ec769988ae3664f50a776fbbf),
[Cloud::BuildHeaderAmzS3v4()](../../d9/dea/namespaceCloud.html#a068954d887c1095aacd27be7c5bb35ed),
[Cloud::ComputeDigestAmzS3v2()](../../d9/dea/namespaceCloud.html#a7553aac877d630c37c9dc682752fca09),
[Cloud::ComputeDigestAmzS3v4()](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb),
[Cloud::CurlWrite_CallbackFunc_StdString()](../../d9/dea/namespaceCloud.html#a0706f2042a82b5e6a6375577359be029),
[Cloud::eraseSubStr()](../../d9/dea/namespaceCloud.html#a200581597cdfe01a88dfcc0b5d3f8529),
[Cloud::CloudReader::FileEntry::FileName](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#aaacf4f1a4c7b1beaa85fca81ac51ba85),
and
[Cloud::CloudReader::FileEntry::FileStream](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#ac85e8a4839a51dfab009594b596fba07).

Referenced by
[GetEntry()](../../d2/de7/classCloud_1_1CloudReader.html#aee8ab3acc0f9cdc7f5360b733cd650a7).

## ◆ GetEntry()

struct [Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html) * Cloud::CloudReader::GetEntry  | ( | std::string  | _FileName_| ) |   
---|---|---|---|---|---  
  
References
[DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085),
[FileList](../../d2/de7/classCloud_1_1CloudReader.html#aaf53637ede63872bf94a3a25b6807a64),
[Cloud::CloudReader::FileEntry::FileName](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#aaacf4f1a4c7b1beaa85fca81ac51ba85),
and
[Cloud::CloudReader::FileEntry::touch](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#a7f85c33c5c2e2d9603b83620c2788977).

Referenced by
[Cloud::Module::cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4).

## ◆ isTouched()

[int](../../d1/da0/classint.html) Cloud::CloudReader::isTouched  | ( | std::string  | _FileName_| ) |   
---|---|---|---|---|---  
  
References
[FileList](../../d2/de7/classCloud_1_1CloudReader.html#aaf53637ede63872bf94a3a25b6807a64),
and
[Cloud::CloudReader::FileEntry::FileName](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#aaacf4f1a4c7b1beaa85fca81ac51ba85).

## Member Data Documentation

## ◆ Bucket

| const char* Cloud::CloudReader::Bucket  
---  
protected  
  
## ◆ continuation

[int](../../d1/da0/classint.html) Cloud::CloudReader::continuation =0  
---  
  
Referenced by
[checkText()](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a).

## ◆ file

[int](../../d1/da0/classint.html) Cloud::CloudReader::file =0  
---  
  
Referenced by
[checkText()](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a),
[exportIFCHelper.ContextCreator::createAutomaticProject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a148406623b830e96b625e4cc9ac25bd2),
[exportIFCHelper.ContextCreator::createCustomProject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a34f97033698a98007b430b629d694626),
[exportIFCHelper.ContextCreator::createGeometricRepresentationContext()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a6a54d0b2f20650b6a7ce05d57d2ae8e3),
[exportIFCHelper.ContextCreator::createGeometricRepresentationSubContext()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a706ac46037632ab6fb9ea483bf3e4095),
[exportIFCHelper.ContextCreator::createMapConversion()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#aac779e6f884db286129eb07b8622645b),
[exportIFCHelper.ContextCreator::createTargetCRS()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#ab3bc2c1c6282b286bd93af440fda7afc),
[exportIFCHelper.ContextCreator::createTrueNorth()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a8491dc7a339dce3412310dd42a65fd01),
[Cloud::CloudWriter::putNextEntry()](../../d0/d23/classCloud_1_1CloudWriter.html#a717c543549341700a14e070ba4d9e4c0),
and
[importIFClegacy.IfcFile::read()](../../d1/daa/classimportIFClegacy_1_1IfcFile.html#a9ad8d00537a61e0be429282c1c56fbdf).

## ◆ FileList

|
std::list<[Cloud::CloudReader::FileEntry](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html)*>
Cloud::CloudReader::FileList  
---  
protected  
  
Referenced by
[addFile()](../../d2/de7/classCloud_1_1CloudReader.html#aa6721854d1f8ec03ab568f99133be83f),
[checkText()](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a),
[GetEntry()](../../d2/de7/classCloud_1_1CloudReader.html#aee8ab3acc0f9cdc7f5360b733cd650a7),
and
[isTouched()](../../d2/de7/classCloud_1_1CloudReader.html#a3fc9227c497bad007ec41b54ce52fcfa).

## ◆ NextFileName

| char* Cloud::CloudReader::NextFileName  
---  
protected  
  
Referenced by
[checkText()](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a),
and
[CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94).

## ◆ ProtocolVersion

| std::string Cloud::CloudReader::ProtocolVersion  
---  
protected  
  
## ◆ Region

| std::string Cloud::CloudReader::Region  
---  
protected  
  
## ◆ TCPPort

| const char* Cloud::CloudReader::TCPPort  
---  
protected  
  
## ◆ TokenAuth

| const char* Cloud::CloudReader::TokenAuth  
---  
protected  
  
## ◆ TokenSecret

| const char* Cloud::CloudReader::TokenSecret  
---  
protected  
  
## ◆ truncated

[int](../../d1/da0/classint.html) Cloud::CloudReader::truncated =0  
---  
  
Referenced by
[checkText()](../../d2/de7/classCloud_1_1CloudReader.html#a9741498f64fe9f792fd9df0139c6869a).

## ◆ URL

| const char* Cloud::CloudReader::URL  
---  
protected  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Cloud/App/AppCloud.h
  * FreeCAD/src/Mod/Cloud/App/AppCloud.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

