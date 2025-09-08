---
url: https://freecad.github.io/SourceDoc/d9/d80/classCloud_1_1Module.html
scraped_at: 2025-09-08T15:19:28.628170
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Cloud](../../d9/dea/namespaceCloud.html)
  * [Module](../../d9/d80/classCloud_1_1Module.html)

[List of all members](../../d3/d8c/classCloud_1_1Module-members.html) | Public Member Functions | Public Attributes

Cloud::Module Class Reference

`#include <AppCloud.h>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [cloudRestore](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4) (const char *BucketName)  
[bool](../../d9/db9/classbool.html) | [cloudSave](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71) (const char *BucketName)  
void | [LinkXSetValue](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af) (std::string filename)  
|
[Module](../../d9/d80/classCloud_1_1Module.html#a7e05b936f9e0e41c5ffb7eae9ea97ba5)
()  
virtual | [~Module](../../d9/d80/classCloud_1_1Module.html#a82aeb7231e48f4234293a5e850ccafe7) ()  
  
##  Public Attributes  
  
---  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [ProtocolVersion](../../d9/d80/classCloud_1_1Module.html#a25a3e33a1e02775dc026cbc8fbeaa0e8)  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Region](../../d9/d80/classCloud_1_1Module.html#a7f868299473e85d66a0a610436c08339)  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [TCPPort](../../d9/d80/classCloud_1_1Module.html#ab67383f22e29b00f894b107f1378f18a)  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [TokenAuth](../../d9/d80/classCloud_1_1Module.html#a5faf81bfd40a1bfc5101849bb521fd89)  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [TokenSecret](../../d9/d80/classCloud_1_1Module.html#ac7c282ff79caaacab8fd77a479dab318)  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [URL](../../d9/d80/classCloud_1_1Module.html#a2972f0fa9d04de45f011d678efdaa67d)  
  
## Constructor & Destructor Documentation

## ◆ Module()

Cloud::Module::Module  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~Module()

| virtual Cloud::Module::~Module  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ cloudRestore()

[bool](../../d9/db9/classbool.html) Cloud::Module::cloudRestore  | ( | const char *  | _BucketName_| ) |   
---|---|---|---|---|---  
  
References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Cloud::CloudReader::FileEntry::FileStream](../../df/d62/structCloud_1_1CloudReader_1_1FileEntry.html#ac85e8a4839a51dfab009594b596fba07),
[App::Application::getActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0be953356bea8c16bd958433e3769dd9),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[Cloud::CloudReader::GetEntry()](../../d2/de7/classCloud_1_1CloudReader.html#aee8ab3acc0f9cdc7f5360b733cd650a7),
[Base::XMLReader::isValid()](../../dc/d95/classBase_1_1XMLReader.html#a8104be87d837faa87cfc73aeaa6fe7ed),
[LinkXSetValue()](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af),
[App::Application::signalFinishRestoreDocument](../../da/dbf/classApp_1_1Application.html#ac7b262994ef3ae8766bd3c7590185046),
and
[App::Application::signalStartRestoreDocument](../../da/dbf/classApp_1_1Application.html#a79b377bd369df1b15b2ae2b9181f7f75).

## ◆ cloudSave()

[bool](../../d9/db9/classbool.html) Cloud::Module::cloudSave  | ( | const char *  | _BucketName_| ) |   
---|---|---|---|---|---  
  
References
[Base::TimeInfo::currentDateTimeString()](../../df/d75/classBase_1_1TimeInfo.html#a395c874b184fdb4fc9ffc90fb4714371),
[App::Application::getActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0be953356bea8c16bd958433e3769dd9),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetASCII()](../../d4/d97/classParameterGrp.html#a5c579b580966bb5ddb8d07df2da9bc9c),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[Cloud::CloudWriter::putNextEntry()](../../d0/d23/classCloud_1_1CloudWriter.html#a717c543549341700a14e070ba4d9e4c0),
[Base::Writer::setMode()](../../dd/d4d/classBase_1_1Writer.html#a3a26c2bb6285dcd29c97037cdda5042e),
[Cloud::CloudWriter::Stream()](../../d0/d23/classCloud_1_1CloudWriter.html#ac6dec3675fe3bead371f8d345b707dc6),
and
[Cloud::CloudWriter::writeFiles()](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38).

## ◆ LinkXSetValue()

void Cloud::Module::LinkXSetValue  | ( | std::string  | _filename_| ) |   
---|---|---|---|---|---  
  
References
[App::Application::getActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0be953356bea8c16bd958433e3769dd9),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Application::getDocuments()](../../da/dbf/classApp_1_1Application.html#a955aad8188b482bb46f74a46b1946e3a),
[App::Application::getUniqueDocumentName()](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030),
[App::Application::newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b),
and
[App::Application::setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94).

Referenced by
[cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4).

## Member Data Documentation

## ◆ ProtocolVersion

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
Cloud::Module::ProtocolVersion  
---  
  
## ◆ Region

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
Cloud::Module::Region  
---  
  
## ◆ TCPPort

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
Cloud::Module::TCPPort  
---  
  
## ◆ TokenAuth

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
Cloud::Module::TokenAuth  
---  
  
## ◆ TokenSecret

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
Cloud::Module::TokenSecret  
---  
  
## ◆ URL

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
Cloud::Module::URL  
---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Cloud/App/AppCloud.h
  * FreeCAD/src/Mod/Cloud/App/AppCloud.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

