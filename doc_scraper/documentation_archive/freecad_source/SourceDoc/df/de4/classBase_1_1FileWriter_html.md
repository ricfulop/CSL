---
url: https://freecad.github.io/SourceDoc/df/de4/classBase_1_1FileWriter.html
scraped_at: 2025-09-08T15:16:12.837331
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [FileWriter](../../df/de4/classBase_1_1FileWriter.html)

[List of all members](../../d6/d7d/classBase_1_1FileWriter-members.html) | Public Member Functions | Protected Attributes

Base::FileWriter Class Reference

`#include <Writer.h>`

##  Public Member Functions  
  
---  
void | [close](../../df/de4/classBase_1_1FileWriter.html#ae49581ca5845fa0d28f0f521ad73bc12) ()  
|
[FileWriter](../../df/de4/classBase_1_1FileWriter.html#a6c1055699e5846399268df23f3db88f6)
(const char
*[DirName](../../df/de4/classBase_1_1FileWriter.html#a4ba024aead8bac97a4f6796f90529f27))  
void | [putNextEntry](../../df/de4/classBase_1_1FileWriter.html#ae374b579a39c038fafa0818b209634dd) (const char *file)  
virtual [bool](../../d9/db9/classbool.html) | [shouldWrite](../../df/de4/classBase_1_1FileWriter.html#aba8ec7f70ad58e41a57e7dc9ad48d242) (const std::string &name, const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *Object) const  
virtual std::ostream & | [Stream](../../df/de4/classBase_1_1FileWriter.html#a8afbc7f269c0994675f1a2751dde9cdc) ()  
virtual void | [writeFiles](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805) ()  
| process the requested file storing
[More...](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805)  
  
virtual | [~FileWriter](../../df/de4/classBase_1_1FileWriter.html#ae5490307dcaf9237f4c1b8b8df433e03) ()  
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
  
  
##  Protected Attributes  
  
---  
std::string | [DirName](../../df/de4/classBase_1_1FileWriter.html#a4ba024aead8bac97a4f6796f90529f27)  
std::ofstream | [FileStream](../../df/de4/classBase_1_1FileWriter.html#a103dc279243dd09f9725f5c645e1a2ba)  
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
![-](../../closed.png) Public Attributes inherited from
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html)  
std::string | [ObjectName](../../dd/d4d/classBase_1_1Writer.html#a33392412488d03635dfb4527e3df677d)  
| name for underlying file saves
[More...](../../dd/d4d/classBase_1_1Writer.html#a33392412488d03635dfb4527e3df677d)  
  
![-](../../closed.png) Protected Member Functions inherited from
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html)  
std::string | [getUniqueFileName](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc) (const char *Name)  
  
## Detailed Description

The [FileWriter](../../df/de4/classBase_1_1FileWriter.html) class This class
writes out the data into files into a given directory name.

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ FileWriter()

FileWriter::FileWriter  | ( | const char *  | _DirName_| ) |   
---|---|---|---|---|---  
  
## ◆ ~FileWriter()

| FileWriter::~FileWriter  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ close()

void Base::FileWriter::close  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[femexamples.examplesgui.FemExamples::reject()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ade2cd979d737a9fa26b1e5f5ff8ebfcf),
and
[Gui::RecoveryRunnable::run()](../../d9/dc2/classGui_1_1RecoveryRunnable.html#a208e97d67c3514ace646442df3a0f30b).

## ◆ putNextEntry()

void FileWriter::putNextEntry  | ( | const char *  | _file_| ) |   
---|---|---|---|---|---  
  
References
[DirName](../../df/de4/classBase_1_1FileWriter.html#a4ba024aead8bac97a4f6796f90529f27),
and
[FileStream](../../df/de4/classBase_1_1FileWriter.html#a103dc279243dd09f9725f5c645e1a2ba).

Referenced by
[Gui::RecoveryRunnable::RecoveryRunnable()](../../d9/dc2/classGui_1_1RecoveryRunnable.html#aa1a456691d55fb28fb664f5fbc60bdfc),
and
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059).

## ◆ shouldWrite()

| [bool](../../d9/db9/classbool.html) FileWriter::shouldWrite  | ( | const std::string & | _name_ ,   
---|---|---|---  
|  | const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *  | _Object_  
| ) | |  const  
virtual  
  
This method can be re-implemented in sub-classes to avoid to write out certain
objects. The default implementation always returns true.

Reimplemented in
[Gui::RecoveryWriter](../../d9/d25/classGui_1_1RecoveryWriter.html#aec0a593c8a632c1e1700c4b8e851372f).

Referenced by
[writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805).

## ◆ Stream()

| virtual std::ostream & Base::FileWriter::Stream  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Implements
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ writeFiles()

| void FileWriter::writeFiles  | ( | | ) |   
---|---|---|---|---  
virtual  
  
process the requested file storing

Implements
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html#a4ac216f6afc4c088950ae53dc75a9e2d).

Reimplemented in
[Gui::RecoveryWriter](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c).

References
[Base::FileInfo::createDirectory()](../../dd/d34/classBase_1_1FileInfo.html#aa6f05ba743ce834588f77fdc15a1e7c4),
[DirName](../../df/de4/classBase_1_1FileWriter.html#a4ba024aead8bac97a4f6796f90529f27),
[Base::Writer::FileList](../../dd/d4d/classBase_1_1Writer.html#a364da33cc8f9237793691c1ed545b866),
[Base::Writer::FileEntry::FileName](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#abd6c12817010758a25f9af39c2c3a70c),
[FileStream](../../df/de4/classBase_1_1FileWriter.html#a103dc279243dd09f9725f5c645e1a2ba),
[Base::Writer::FileEntry::Object](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#a15a35046c9bd5dad11dd5d97c18d675f),
[Base::Persistence::SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45),
and
[shouldWrite()](../../df/de4/classBase_1_1FileWriter.html#aba8ec7f70ad58e41a57e7dc9ad48d242).

## Member Data Documentation

## ◆ DirName

| std::string Base::FileWriter::DirName  
---  
protected  
  
Referenced by
[putNextEntry()](../../df/de4/classBase_1_1FileWriter.html#ae374b579a39c038fafa0818b209634dd),
[writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
and
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c).

## ◆ FileStream

| std::ofstream Base::FileWriter::FileStream  
---  
protected  
  
Referenced by
[putNextEntry()](../../df/de4/classBase_1_1FileWriter.html#ae374b579a39c038fafa0818b209634dd),
[writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
and
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Writer.h
  * FreeCAD/src/Base/Writer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

