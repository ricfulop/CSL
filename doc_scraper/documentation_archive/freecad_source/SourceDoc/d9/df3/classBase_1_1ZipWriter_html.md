---
url: https://freecad.github.io/SourceDoc/d9/df3/classBase_1_1ZipWriter.html
scraped_at: 2025-09-08T15:18:22.376164
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html)

[List of all members](../../d7/d19/classBase_1_1ZipWriter-members.html) | Public Member Functions

Base::ZipWriter Class Reference

The [ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html "The ZipWriter class
This is an important helper class implementation for the store and retrieval
syst...") class This is an important helper class implementation for the store
and retrieval system of persistent objects in FreeCAD.
[More...](../../d9/df3/classBase_1_1ZipWriter.html#details)

`#include <Writer.h>`

##  Public Member Functions  
  
---  
void | [putNextEntry](../../d9/df3/classBase_1_1ZipWriter.html#abb607a9c82879c6ead67f9dee234bd24) (const char *[str](../../d9/d36/classstr.html))  
void | [setComment](../../d9/df3/classBase_1_1ZipWriter.html#a15c873494ac59c3bc50b0875eb34a1fd) (const char *[str](../../d9/d36/classstr.html))  
void | [setLevel](../../d9/df3/classBase_1_1ZipWriter.html#a8e1bad6d8787aa75f5d5144ef166b16f) ([int](../../d1/da0/classint.html) [level](../../d1/da0/classint.html))  
virtual std::ostream & | [Stream](../../d9/df3/classBase_1_1ZipWriter.html#a37330d3d5bff097e58268aa7853abaa4) ()  
virtual void | [writeFiles](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a) ()  
| process the requested file storing
[More...](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a)  
  
|
[ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html#a1816eb9ed9d10289bd43d19beb0747bd)
(const char *FileName)  
|
[ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html#abdb23125137719a0bcc53b7e7a09ac15)
(std::ostream &)  
virtual | [~ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html#ac6cf71151a9ef11cf031e814126207d3) ()  
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
  
## Detailed Description

The [ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html "The ZipWriter class
This is an important helper class implementation for the store and retrieval
syst...") class This is an important helper class implementation for the store
and retrieval system of persistent objects in FreeCAD.

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Author

    Juergen Riegel 

## Constructor & Destructor Documentation

## ◆ ZipWriter() [1/2]

ZipWriter::ZipWriter  | ( | const char *  | _FileName_| ) |   
---|---|---|---|---|---  
  
## ◆ ZipWriter() [2/2]

ZipWriter::ZipWriter  | ( | std::ostream & | _os_| ) |   
---|---|---|---|---|---  
  
## ◆ ~ZipWriter()

| ZipWriter::~ZipWriter  | ( | | ) |   
---|---|---|---|---  
virtual  
  
References
[zipios::ZipOutputStream::close()](../../d3/d51/classzipios_1_1ZipOutputStream.html#a1e7ef30f3d6512c984698795b830b544).

## Member Function Documentation

## ◆ putNextEntry()

void Base::ZipWriter::putNextEntry  | ( | const char *  | _str_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Base::Persistence::dumpToStream()](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7),
[App::Document::exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
and
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ setComment()

void Base::ZipWriter::setComment  | ( | const char *  | _str_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
and
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ setLevel()

void Base::ZipWriter::setLevel  | ( | [int](../../d1/da0/classint.html) | _level_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Base::Persistence::dumpToStream()](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
and
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ Stream()

| virtual std::ostream & Base::ZipWriter::Stream  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Implements
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[Base::Persistence::dumpToStream()](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7),
[App::Document::exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
and
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ writeFiles()

| void ZipWriter::writeFiles  | ( | | ) |   
---|---|---|---|---  
virtual  
  
process the requested file storing

Implements
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html#a4ac216f6afc4c088950ae53dc75a9e2d).

References
[Base::Writer::FileList](../../dd/d4d/classBase_1_1Writer.html#a364da33cc8f9237793691c1ed545b866),
[Base::Writer::FileEntry::FileName](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#abd6c12817010758a25f9af39c2c3a70c),
[Base::Writer::FileEntry::Object](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#a15a35046c9bd5dad11dd5d97c18d675f),
[zipios::ZipOutputStream::putNextEntry()](../../d3/d51/classzipios_1_1ZipOutputStream.html#a59f847b10b7715934f9dc2ef74165df1),
and
[Base::Persistence::SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45).

Referenced by
[Base::Persistence::dumpToStream()](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7),
[App::Document::exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
and
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Writer.h
  * FreeCAD/src/Base/Writer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

