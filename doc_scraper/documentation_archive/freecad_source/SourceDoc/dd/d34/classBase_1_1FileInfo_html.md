---
url: https://freecad.github.io/SourceDoc/dd/d34/classBase_1_1FileInfo.html
scraped_at: 2025-09-08T15:16:10.892737
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [FileInfo](../../dd/d34/classBase_1_1FileInfo.html)

[List of all members](../../d9/dcd/classBase_1_1FileInfo-members.html) | Public Types | Public Member Functions

Base::FileInfo Class Reference

File name unification This class handles everything related to file names the
file names are internal generally UTF-8 encoded on all platforms.
[More...](../../dd/d34/classBase_1_1FileInfo.html#details)

`#include <FileInfo.h>`

##  Public Types  
  
---  
enum | [Permissions](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738) { [WriteOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738ac642426fce847ed13f5cb06a233fc5bb) = 0x01 , [ReadOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a2a81c484ad2171f79da987b019813a9c) = 0x02 , [ReadWrite](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a4c66903b9ac6c5788840b9e36d1b5911) = 0x03 }  
  
##  Public Member Functions  
  
---  
|
[FileInfo](../../dd/d34/classBase_1_1FileInfo.html#ae586b7919e8716c8782a7e0ba44e76e0)
(const char *_FileName="")  
| Construction.
[More...](../../dd/d34/classBase_1_1FileInfo.html#ae586b7919e8716c8782a7e0ba44e76e0)  
  
|
[FileInfo](../../dd/d34/classBase_1_1FileInfo.html#aa74985c96c7f2a10375d6a04f3cfebfb)
(const std::string &_FileName)  
void | [setFile](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616) (const char *name)  
| Set a new file name.
[More...](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616)  
  
void | [setFile](../../dd/d34/classBase_1_1FileInfo.html#a8295101575413cfa1be9c4a5fe13684c) (const std::string &name)  
| Set a new file name.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a8295101575413cfa1be9c4a5fe13684c)  
  
extraction of information  
std::string | [filePath](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987) () const  
| Returns the file name, including the path (which may be absolute or
relative).
[More...](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987)  
  
std::string | [dirPath](../../dd/d34/classBase_1_1FileInfo.html#a931384d1da89e1295bb158617f3f5712) () const  
| Returns the dir path name (which may be absolute or relative).
[More...](../../dd/d34/classBase_1_1FileInfo.html#a931384d1da89e1295bb158617f3f5712)  
  
std::string | [fileName](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a) () const  
| Returns the name of the file, excluding the path, including the extension.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a)  
  
std::string | [fileNamePure](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894) () const  
| Returns the name of the file, excluding the path and the extension.
[More...](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894)  
  
std::wstring | [toStdWString](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304) () const  
| Convert the path name into a UTF-16 encoded wide string format.
[More...](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304)  
  
std::string | [extension](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5) () const  
| Returns the extension of the file.
[More...](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5)  
  
std::string | [completeExtension](../../dd/d34/classBase_1_1FileInfo.html#a6d041427fe955c1db09a9731503a728e) () const  
| Returns the complete extension of the file.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a6d041427fe955c1db09a9731503a728e)  
  
[bool](../../d9/db9/classbool.html) | [hasExtension](../../dd/d34/classBase_1_1FileInfo.html#a267092c449aa51848b11fb9226c0be4d) (const char *Ext) const  
| Checks for a special extension, NOT case sensitive.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a267092c449aa51848b11fb9226c0be4d)  
  
methods to test the status of the file or dir  
[bool](../../d9/db9/classbool.html) | [exists](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f) () const  
| Does the file exist?
[More...](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f)  
  
[bool](../../d9/db9/classbool.html) | [isReadable](../../dd/d34/classBase_1_1FileInfo.html#aa7bd4cf0e93293d4c3bf057b53f02063) () const  
| Checks if the file exist and is readable.
[More...](../../dd/d34/classBase_1_1FileInfo.html#aa7bd4cf0e93293d4c3bf057b53f02063)  
  
[bool](../../d9/db9/classbool.html) | [isWritable](../../dd/d34/classBase_1_1FileInfo.html#a550b75d516c531e941faffbd70054862) () const  
| Checks if the file exist and is writable.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a550b75d516c531e941faffbd70054862)  
  
[bool](../../d9/db9/classbool.html) | [setPermissions](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23) ([Permissions](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738))  
| Tries to set the file permission.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23)  
  
[bool](../../d9/db9/classbool.html) | [isFile](../../dd/d34/classBase_1_1FileInfo.html#ab7840bb4fca4b3d9938c1b3f0e1352ef) () const  
| Checks if it is a file (not a directory)
[More...](../../dd/d34/classBase_1_1FileInfo.html#ab7840bb4fca4b3d9938c1b3f0e1352ef)  
  
[bool](../../d9/db9/classbool.html) | [isDir](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f) () const  
| Checks if it is a directory (not a file)
[More...](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f)  
  
unsigned [int](../../d1/da0/classint.html) | [size](../../dd/d34/classBase_1_1FileInfo.html#a10ee386bf1fa66edb6dc01298c257d65) () const  
| The size of the file.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a10ee386bf1fa66edb6dc01298c257d65)  
  
[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) | [lastModified](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8) () const  
| Returns the time when the file was last modified.
[More...](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8)  
  
[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) | [lastRead](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0) () const  
| Returns the time when the file was last read (accessed).
[More...](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0)  
  
Directory management  
[bool](../../d9/db9/classbool.html) | [createDirectory](../../dd/d34/classBase_1_1FileInfo.html#aa6f05ba743ce834588f77fdc15a1e7c4) () const  
| Creates a directory. Returns true if successful; otherwise returns false.
[More...](../../dd/d34/classBase_1_1FileInfo.html#aa6f05ba743ce834588f77fdc15a1e7c4)  
  
[bool](../../d9/db9/classbool.html) | [createDirectories](../../dd/d34/classBase_1_1FileInfo.html#ae2b639e68c2acc94843eced585d3fb08) () const  
| Creates a directory and all its parent directories. Returns true if
successful; otherwise returns false.
[More...](../../dd/d34/classBase_1_1FileInfo.html#ae2b639e68c2acc94843eced585d3fb08)  
  
std::vector< [Base::FileInfo](../../dd/d34/classBase_1_1FileInfo.html) > | [getDirectoryContent](../../dd/d34/classBase_1_1FileInfo.html#a9b33b65881316baad94257470aa77c07) () const  
| Get a list of the directory content.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a9b33b65881316baad94257470aa77c07)  
  
[bool](../../d9/db9/classbool.html) | [deleteDirectory](../../dd/d34/classBase_1_1FileInfo.html#a90076a5e4c647966ce0b79e58381f30e) () const  
| Delete an empty directory.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a90076a5e4c647966ce0b79e58381f30e)  
  
[bool](../../d9/db9/classbool.html) | [deleteDirectoryRecursive](../../dd/d34/classBase_1_1FileInfo.html#a9b042f228fbabe4c34c357669189cca8) () const  
| Delete a directory and all its content.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a9b042f228fbabe4c34c357669189cca8)  
  
[bool](../../d9/db9/classbool.html) | [deleteFile](../../dd/d34/classBase_1_1FileInfo.html#aafd7a8df3d22c3e48523afe865115b9c) () const  
| Delete the file.
[More...](../../dd/d34/classBase_1_1FileInfo.html#aafd7a8df3d22c3e48523afe865115b9c)  
  
[bool](../../d9/db9/classbool.html) | [renameFile](../../dd/d34/classBase_1_1FileInfo.html#ac5067c657858a93f81d2fbfdd4fdf8eb) (const char *NewName)  
| Rename the file.
[More...](../../dd/d34/classBase_1_1FileInfo.html#ac5067c657858a93f81d2fbfdd4fdf8eb)  
  
[bool](../../d9/db9/classbool.html) | [copyTo](../../dd/d34/classBase_1_1FileInfo.html#a47907e1927f6ff3b767f83ac846ef8e1) (const char *NewName) const  
| Rename the file.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a47907e1927f6ff3b767f83ac846ef8e1)  
  
  
## Tools  
  
---  
std::string | [FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c)  
static std::string | [getTempFileName](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74) (const char *[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c)=nullptr, const char *path=nullptr)  
| Get a unique File Name in the given or (if 0) in the temp path.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74)  
  
static const std::string & | [getTempPath](../../dd/d34/classBase_1_1FileInfo.html#a8cb1ad2d421e1c95d208b92e7f964658) ()  
| Get the path to the dir which is considered to temp files.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a8cb1ad2d421e1c95d208b92e7f964658)  
  
static std::string | [pathToString](../../dd/d34/classBase_1_1FileInfo.html#a9950171f00c8c79e983b8be1326c7f55) (const boost::filesystem::path &p)  
| Convert from filesystem path to string.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a9950171f00c8c79e983b8be1326c7f55)  
  
static boost::filesystem::path | [stringToPath](../../dd/d34/classBase_1_1FileInfo.html#a7ecabc034f3fff6e5d15aa1b3e7c99c7) (const std::string &[str](../../d9/d36/classstr.html))  
| Convert from string to filesystem path.
[More...](../../dd/d34/classBase_1_1FileInfo.html#a7ecabc034f3fff6e5d15aa1b3e7c99c7)  
  
  
## Detailed Description

File name unification This class handles everything related to file names the
file names are internal generally UTF-8 encoded on all platforms.

## Member Enumeration Documentation

## ◆ Permissions

enum
[Base::FileInfo::Permissions](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738)  
---  
  
Enumerator  
---  
WriteOnly |   
ReadOnly |   
ReadWrite |   
  
## Constructor & Destructor Documentation

## ◆ FileInfo() [1/2]

FileInfo::FileInfo  | ( | const char *  | __FileName_ = `""`| ) |   
---|---|---|---|---|---  
  
Construction.

References
[setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616).

Referenced by
[getDirectoryContent()](../../dd/d34/classBase_1_1FileInfo.html#a9b33b65881316baad94257470aa77c07).

## ◆ FileInfo() [2/2]

FileInfo::FileInfo  | ( | const std::string & | __FileName_| ) |   
---|---|---|---|---|---  
  
References
[setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616).

## Member Function Documentation

## ◆ completeExtension()

std::string FileInfo::completeExtension  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the complete extension of the file.

The complete extension consists of all characters in the file after (but not
including) the first '.' character.

[FileInfo](../../dd/d34/classBase_1_1FileInfo.html "File name unification This
class handles everything related to file names the file names are
internal...") fi( "/tmp/archive.tar.gz" );

ext = fi.completeExtension(); // ext = "tar.gz"

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

## ◆ copyTo()

[bool](../../d9/db9/classbool.html) FileInfo::copyTo  | ( | const char *  | _NewName_| ) |  const  
---|---|---|---|---|---  
  
Rename the file.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[TechDraw::DrawUtil::copyFile()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae9807e29f390c2fe10bad030edb01a37),
and
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e).

## ◆ createDirectories()

[bool](../../d9/db9/classbool.html) FileInfo::createDirectories  | ( | | ) |  const  
---|---|---|---|---  
  
Creates a directory and all its parent directories. Returns true if
successful; otherwise returns false.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[stringToPath()](../../dd/d34/classBase_1_1FileInfo.html#a7ecabc034f3fff6e5d15aa1b3e7c99c7).

Referenced by
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a).

## ◆ createDirectory()

[bool](../../d9/db9/classbool.html) FileInfo::createDirectory  | ( | | ) |  const  
---|---|---|---|---  
  
Creates a directory. Returns true if successful; otherwise returns false.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[App::VRMLObject::makeDirectories()](../../df/df6/classApp_1_1VRMLObject.html#ad582e14e97992ca59b4f028042c13fc1),
[Gui::AutoSaver::slotCreateDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#ac494a904b86d92d32163dab8049b0d80),
[Base::FileWriter::writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
and
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c).

## ◆ deleteDirectory()

[bool](../../d9/db9/classbool.html) FileInfo::deleteDirectory  | ( | | ) |  const  
---|---|---|---|---  
  
Delete an empty directory.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
[isDir()](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[deleteDirectoryRecursive()](../../dd/d34/classBase_1_1FileInfo.html#a9b042f228fbabe4c34c357669189cca8).

## ◆ deleteDirectoryRecursive()

[bool](../../d9/db9/classbool.html) FileInfo::deleteDirectoryRecursive  | ( | | ) |  const  
---|---|---|---|---  
  
Delete a directory and all its content.

References
[deleteDirectory()](../../dd/d34/classBase_1_1FileInfo.html#a90076a5e4c647966ce0b79e58381f30e),
[getDirectoryContent()](../../dd/d34/classBase_1_1FileInfo.html#a9b33b65881316baad94257470aa77c07),
[isDir()](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f),
and
[ReadWrite](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a4c66903b9ac6c5788840b9e36d1b5911).

Referenced by
[App::Document::~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ deleteFile()

[bool](../../d9/db9/classbool.html) FileInfo::deleteFile  | ( | | ) |  const  
---|---|---|---|---  
  
Delete the file.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[StdCmdDuplicateSelection::activated()](../../d4/d75/classStdCmdDuplicateSelection.html#a1ffe671eebc9f7e4c99740df06eaf0a9),
[Gui::MainWindow::closeEvent()](../../d5/d2f/classGui_1_1MainWindow.html#a8a5bf36f9544ed3ec3a9eea9b7154564),
[App::Document::importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778),
[MeshGui::RemeshGmsh::loadOutput()](../../dd/d1b/classMeshGui_1_1RemeshGmsh.html#ae2d3d4b0bb6bf0fecd761bf42cd6fb42),
[MeshPartGui::Mesh2ShapeGmsh::loadOutput()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a44307c501da72ba058c29e10998ef358),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[Fem::FemMesh::RestoreDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a0d087a665305a95b22c0b16b751cd5b1),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Fem::FemMesh::SaveDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a879fc2d7f331b9cb54e05424ecf62d87),
and
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b).

## ◆ dirPath()

std::string FileInfo::dirPath  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the dir path name (which may be absolute or relative).

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

Referenced by
[Mesh::AmfExporter::AmfExporter()](../../d1/d2e/classMesh_1_1AmfExporter.html#a5f4547096bcae5b12934fb6addb7858a),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
[Mesh::MeshObject::load()](../../d8/dcc/classMesh_1_1MeshObject.html#a18e2e8170174a57463675c300bb8a584),
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[Mesh::MeshObject::save()](../../d8/dcc/classMesh_1_1MeshObject.html#a4a20379185dd31620a2df5c047c695bc),
[Import::ImportOCAF2::setMode()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a865601fce708b9141eb0bbf40b3e96f8),
and
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa).

## ◆ exists()

[bool](../../d9/db9/classbool.html) FileInfo::exists  | ( | | ) |  const  
---|---|---|---|---  
  
Does the file exist?

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[Gui::ViewProviderVRMLObject::addResource()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a90119133e310080de7e7ba113e5c4ea8),
[Mesh::AmfExporter::AmfExporter()](../../d1/d2e/classMesh_1_1AmfExporter.html#a5f4547096bcae5b12934fb6addb7858a),
[Gui::MainWindow::closeEvent()](../../d5/d2f/classGui_1_1MainWindow.html#a8a5bf36f9544ed3ec3a9eea9b7154564),
[App::PropertyFileIncluded::getUniqueFileName()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006),
[Part::ImportStepParts()](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619),
[isDir()](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f),
[isFile()](../../dd/d34/classBase_1_1FileInfo.html#ab7840bb4fca4b3d9938c1b3f0e1352ef),
[lastModified()](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8),
[lastRead()](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0),
[MeshCore::MeshInput::LoadAny()](../../d9/d08/classMeshCore_1_1MeshInput.html#a6abd637db3c98170463307577f165a06),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[Import::StepShape::read()](../../d8/da2/classImport_1_1StepShape.html#af6a61185f0012ef83203f3a101a3f0db),
[App::PropertyFileIncluded::RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[MeshCore::MeshOutput::SaveAny()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8dbc378f95be29a5479206b0239a4977),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa),
and
[Gui::Application::sLoadFile()](../../d9/da8/classGui_1_1Application.html#ac274116543bbd50d4cd21c20f69799ec).

## ◆ extension()

std::string FileInfo::extension  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the extension of the file.

The extension consists of all characters in the file after (but not including)
the last '.' character.

[FileInfo](../../dd/d34/classBase_1_1FileInfo.html "File name unification This
class handles everything related to file names the file names are
internal...") fi( "/tmp/archive.tar.gz" );

ext = fi.extension(); // ext = "gz"

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

Referenced by
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[Base::Writer::getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc),
[hasExtension()](../../dd/d34/classBase_1_1FileInfo.html#a267092c449aa51848b11fb9226c0be4d),
[Gui::Application::importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[TechDraw::DrawHatch::isBitmapHatch()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a6cd818ffc795a57c95dff46e117be1dc),
[TechDraw::DrawHatch::isSvgHatch()](../../d0/d97/classTechDraw_1_1DrawHatch.html#ab74a45f89d5d30095178c7b1621bd5fe),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa),
and
[Gui::Application::sLoadFile()](../../d9/da8/classGui_1_1Application.html#ac274116543bbd50d4cd21c20f69799ec).

## ◆ fileName()

std::string FileInfo::fileName  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the name of the file, excluding the path, including the extension.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

Referenced by
[Mesh::AmfExporter::AmfExporter()](../../d1/d2e/classMesh_1_1AmfExporter.html#a5f4547096bcae5b12934fb6addb7858a),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[Drawing::FeaturePage::getEditableTextsFromTemplate()](../../db/d0f/classDrawing_1_1FeaturePage.html#af1b06dab1d22245e410d1a251f5eda96),
[Base::FileException::getFileName()](../../d1/dc2/classBase_1_1FileException.html#a85d7bd985f2af2646f9faa62c6228bf3),
[Base::FileException::getPyObject()](../../d1/dc2/classBase_1_1FileException.html#af518f2b1282226fb40c4367c3aca0ae6),
[App::VRMLObject::getRelativePath()](../../df/df6/classApp_1_1VRMLObject.html#acc45a77504394dfd80e2be65376ef14a),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[TechDrawGui::QGSPage::postProcessXml()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#ac4055009ba04a7f89f6c9a935e4ce0a5),
and
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa).

## ◆ fileNamePure()

std::string FileInfo::fileNamePure  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the name of the file, excluding the path and the extension.

References
[fileName()](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a).

Referenced by
[Base::Writer::getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc),
[Part::ImportIgesParts()](../../d2/db9/namespacePart.html#a10322b892abc3b1779054dacf1a49e53),
[Part::ImportStepParts()](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[Fem::FemMesh::read()](../../d3/d2e/classFem_1_1FemMesh.html#a249060b25e0be4ceea12945cd6b2c932),
[Gui::Application::sAddCommand()](../../d9/da8/classGui_1_1Application.html#a37041ecaa7a54653737c0c7664881f5d),
[Mesh::MeshObject::save()](../../d8/dcc/classMesh_1_1MeshObject.html#a4a20379185dd31620a2df5c047c695bc),
[App::Document::saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa),
and
[Fem::FemMesh::write()](../../d3/d2e/classFem_1_1FemMesh.html#aae76fd7da094c3497f08daafa044afc0).

## ◆ filePath()

std::string FileInfo::filePath  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the file name, including the path (which may be absolute or relative).

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

Referenced by
[Mesh::AmfExporter::AmfExporter()](../../d1/d2e/classMesh_1_1AmfExporter.html#a5f4547096bcae5b12934fb6addb7858a),
[App::Application::closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244),
[App::PropertyFileIncluded::Copy()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99),
[Gui::MainWindow::createMimeDataFromSelection()](../../d5/d2f/classGui_1_1MainWindow.html#a1471665356b86fc81addf133db22c977),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[WebGui::FcCookieJar::FcCookieJar()](../../da/d30/classWebGui_1_1FcCookieJar.html#a574284936a1d4a14e15688ef32e36583),
[Base::FileException::FileException()](../../d1/dc2/classBase_1_1FileException.html#aed8ff529f974ce63883db2fc6a1317c9),
[App::Application::getDocumentByPath()](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[Drawing::FeaturePage::getEditableTextsFromTemplate()](../../db/d0f/classDrawing_1_1FeaturePage.html#af1b06dab1d22245e410d1a251f5eda96),
[CDxfWrite::getPlateFile()](../../d6/d47/classCDxfWrite.html#a1a6d27cd40ddcd75bad06f9fb94b195d),
[App::PropertyFileIncluded::getUniqueFileName()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006),
[Gui::Application::importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[Gui::SoSVGVectorOutput::openFile()](../../df/d57/classGui_1_1SoSVGVectorOutput.html#aa9fb309773930c52402b2511a075d338),
[Gui::SoU3DVectorOutput::openFile()](../../d7/dd7/classGui_1_1SoU3DVectorOutput.html#a046dd9fdaf6dee941a8d14ab622b3d62),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[Fem::FemPostPipeline::read()](../../d5/d4b/classFem_1_1FemPostPipeline.html#af5ecfae978f1f5a922fd53da8acc84df),
[Fem::FemMesh::read()](../../d3/d2e/classFem_1_1FemMesh.html#a249060b25e0be4ceea12945cd6b2c932),
[Part::TopoShape::read()](../../d8/ded/classPart_1_1TopoShape.html#a9ef603cedae4d957ffc1962a73c67f6f),
[Fem::FemMesh::RestoreDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a0d087a665305a95b22c0b16b751cd5b1),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Gui::Application::sAddCommand()](../../d9/da8/classGui_1_1Application.html#a37041ecaa7a54653737c0c7664881f5d),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[Fem::FemMesh::SaveDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a879fc2d7f331b9cb54e05424ecf62d87),
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa),
[Fem::FemMesh::write()](../../d3/d2e/classFem_1_1FemMesh.html#aae76fd7da094c3497f08daafa044afc0),
[Part::TopoShape::write()](../../d8/ded/classPart_1_1TopoShape.html#a24d5d1cb382a291ca38462ea74981f38),
and
[MeshGui::RemeshGmsh::writeProject()](../../dd/d1b/classMeshGui_1_1RemeshGmsh.html#ad872d9d576cad94fdc7de3d1992c10ff).

## ◆ getDirectoryContent()

std::vector< [Base::FileInfo](../../dd/d34/classBase_1_1FileInfo.html) > FileInfo::getDirectoryContent  | ( | | ) |  const  
---|---|---|---|---  
  
Get a list of the directory content.

References
[FileInfo()](../../dd/d34/classBase_1_1FileInfo.html#ae586b7919e8716c8782a7e0ba44e76e0),
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[deleteDirectoryRecursive()](../../dd/d34/classBase_1_1FileInfo.html#a9b042f228fbabe4c34c357669189cca8).

## ◆ getTempFileName()

| std::string FileInfo::getTempFileName  | ( | const char *  | _FileName_ = `nullptr`,   
---|---|---|---  
|  | const char *  | _path_ = `nullptr`  
| ) | |   
static  
  
Get a unique File Name in the given or (if 0) in the temp path.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
[getTempPath()](../../dd/d34/classBase_1_1FileInfo.html#a8cb1ad2d421e1c95d208b92e7f964658),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[App::PropertyFileIncluded::getExchangeTempFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a73f7c9a5c1633254cda5d292da6b10a5),
and
[App::Application::getTempFileName()](../../da/dbf/classApp_1_1Application.html#a6550097c7ee9c3857f8190954acfbf48).

## ◆ getTempPath()

| const std::string & FileInfo::getTempPath  | ( | | ) |   
---|---|---|---|---  
static  
  
Get the path to the dir which is considered to temp files.

References
[isDir()](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f).

Referenced by
[getTempFileName()](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74).

## ◆ hasExtension()

[bool](../../d9/db9/classbool.html) FileInfo::hasExtension  | ( | const char *  | _Ext_| ) |  const  
---|---|---|---|---|---  
  
Checks for a special extension, NOT case sensitive.

References
[extension()](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5).

Referenced by
[Fem::FemPostPipeline::canRead()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a97b84aa47a07dbcec87c4cd3251ebc7a),
[Gui::View3DInventorViewer::dumpToFile()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a5e9a2d9d7220d13bacafd6aca3634c2f),
[MeshCore::MeshInput::getFormat()](../../d9/d08/classMeshCore_1_1MeshInput.html#a956b3249ab5d391aacf65f8472b1f42a),
[Gui::Application::importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[Points::PointsAlgos::Load()](../../d8/d62/classPoints_1_1PointsAlgos.html#aa554d9d886e81083f2557a4fa6346f1b),
[MeshCore::MeshInput::LoadAny()](../../d9/d08/classMeshCore_1_1MeshInput.html#a6abd637db3c98170463307577f165a06),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[Fem::FemPostPipeline::read()](../../d5/d4b/classFem_1_1FemPostPipeline.html#af5ecfae978f1f5a922fd53da8acc84df),
[Fem::FemMesh::read()](../../d3/d2e/classFem_1_1FemMesh.html#a249060b25e0be4ceea12945cd6b2c932),
[Part::TopoShape::read()](../../d8/ded/classPart_1_1TopoShape.html#a9ef603cedae4d957ffc1962a73c67f6f),
[Part::PropertyPartShape::RestoreDocFile()](../../d7/d28/classPart_1_1PropertyPartShape.html#a4863dc4e56fd41546d7cae6422435f4f),
[Gui::View3DInventorPy::saveVectorGraphic()](../../d3/df7/classGui_1_1View3DInventorPy.html#ace7d4a5d96b3ca762380981c5e205b2e),
[Fem::FemMesh::write()](../../d3/d2e/classFem_1_1FemMesh.html#aae76fd7da094c3497f08daafa044afc0),
[Part::TopoShape::write()](../../d8/ded/classPart_1_1TopoShape.html#a24d5d1cb382a291ca38462ea74981f38),
and
[Gui::SoFCDB::writeToFile()](../../d3/d6d/classGui_1_1SoFCDB.html#aa0d07e0d5eb75c999b19cd2ca8382b4a).

## ◆ isDir()

[bool](../../d9/db9/classbool.html) FileInfo::isDir  | ( | | ) |  const  
---|---|---|---|---  
  
Checks if it is a directory (not a file)

References
[exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[deleteDirectory()](../../dd/d34/classBase_1_1FileInfo.html#a90076a5e4c647966ce0b79e58381f30e),
[deleteDirectoryRecursive()](../../dd/d34/classBase_1_1FileInfo.html#a9b042f228fbabe4c34c357669189cca8),
and
[getTempPath()](../../dd/d34/classBase_1_1FileInfo.html#a8cb1ad2d421e1c95d208b92e7f964658).

## ◆ isFile()

[bool](../../d9/db9/classbool.html) FileInfo::isFile  | ( | | ) |  const  
---|---|---|---|---  
  
Checks if it is a file (not a directory)

References
[exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[MeshCore::MeshInput::LoadAny()](../../d9/d08/classMeshCore_1_1MeshInput.html#a6abd637db3c98170463307577f165a06),
and
[Gui::Application::sLoadFile()](../../d9/da8/classGui_1_1Application.html#ac274116543bbd50d4cd21c20f69799ec).

## ◆ isReadable()

[bool](../../d9/db9/classbool.html) FileInfo::isReadable  | ( | | ) |  const  
---|---|---|---|---  
  
Checks if the file exist and is readable.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[TechDraw::Preferences::bitmapFill()](../../d6/dde/classTechDraw_1_1Preferences.html#aaa59c01070e04cb1f547cc0d0fca41b8),
[TechDraw::DrawUtil::copyFile()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae9807e29f390c2fe10bad030edb01a37),
[TechDraw::Preferences::defaultTemplate()](../../d6/dde/classTechDraw_1_1Preferences.html#aa2ba4e5c813143e90316673e9073e586),
[TechDraw::Preferences::defaultTemplateDir()](../../d6/dde/classTechDraw_1_1Preferences.html#abe38defbf2f6314b882b30707b5bde06),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Part::CurveNet::execute()](../../d9/d41/classPart_1_1CurveNet.html#ab3d3703fdaab33d94b764c62d6739ce6),
[Part::ImportBrep::execute()](../../d8/d3e/classPart_1_1ImportBrep.html#a3fbd619fb350dff418fffd6b6f185ca7),
[Part::ImportIges::execute()](../../d2/d1d/classPart_1_1ImportIges.html#a1d947e212fdeb8ed2b8bb8ef3fae1041),
[Part::ImportStep::execute()](../../d4/de2/classPart_1_1ImportStep.html#a3c81f94deddd927756144ef4e8040678),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[TechDraw::DrawParametricTemplate::execute()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#acc1380e0737504ec1d64b2bbca2380e6),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawGeomHatch::getDecodedSpecsFromFile()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a554ea0b075dd29378c7a20bc4a76bb54),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[Drawing::FeaturePage::getEditableTextsFromTemplate()](../../db/d0f/classDrawing_1_1FeaturePage.html#af1b06dab1d22245e410d1a251f5eda96),
[CDxfWrite::getPlateFile()](../../d6/d47/classCDxfWrite.html#a1a6d27cd40ddcd75bad06f9fb94b195d),
[TechDraw::Preferences::lineGroupFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a9c538c5e2ad7c65962a5dd44dd26b17c),
[Points::PointsAlgos::Load()](../../d8/d62/classPoints_1_1PointsAlgos.html#aa554d9d886e81083f2557a4fa6346f1b),
[MeshCore::MeshInput::LoadAny()](../../d9/d08/classMeshCore_1_1MeshInput.html#a6abd637db3c98170463307577f165a06),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[TechDraw::DrawTileWeld::onChanged()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawTileWeld::onDocumentRestored()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a7a4b1b5d8aac6cdb9a3a16997934c000),
[TechDraw::DrawGeomHatch::onDocumentRestored()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a236c7efbf2e991277bd53a914eb247bb),
[TechDraw::DrawHatch::onDocumentRestored()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a3437412caff103d7c68842db2e694a7b),
[TechDraw::DrawViewSection::onDocumentRestored()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a639636de121b31e8f97a010b214fb71e),
[TechDraw::Preferences::patFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a603db0a17ac567dd7dc8b20fbe51c609),
[Fem::FemPostPipeline::read()](../../d5/d4b/classFem_1_1FemPostPipeline.html#af5ecfae978f1f5a922fd53da8acc84df),
[Fem::FemMesh::read()](../../d3/d2e/classFem_1_1FemMesh.html#a249060b25e0be4ceea12945cd6b2c932),
[Part::TopoShape::read()](../../d8/ded/classPart_1_1TopoShape.html#a9ef603cedae4d957ffc1962a73c67f6f),
[TechDraw::DrawViewImage::setupImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a70665b6da416755ac2cdb36d9c9ecf6d),
[TechDraw::Preferences::svgFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a7948f1f445732b3f5720eaa35de03d8d),
and
[TechDrawGui::PreferencesGui::weldingDirectory()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ae8f758711778daab1558370f25fa519f).

## ◆ isWritable()

[bool](../../d9/db9/classbool.html) FileInfo::isWritable  | ( | | ) |  const  
---|---|---|---|---  
  
Checks if the file exist and is writable.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[Mesh::AmfExporter::AmfExporter()](../../d1/d2e/classMesh_1_1AmfExporter.html#a5f4547096bcae5b12934fb6addb7858a),
[App::PropertyFileIncluded::RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0),
and
[MeshCore::MeshOutput::SaveAny()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8dbc378f95be29a5479206b0239a4977).

## ◆ lastModified()

[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) FileInfo::lastModified  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the time when the file was last modified.

References
[exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
[Base::TimeInfo::null()](../../df/d75/classBase_1_1TimeInfo.html#a1f75ecad31f55a21884ea6a36af41a67),
[Base::TimeInfo::setTime_t()](../../df/d75/classBase_1_1TimeInfo.html#ae874a0ed3ec680b6f1aefba28ec6974c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

## ◆ lastRead()

[TimeInfo](../../df/d75/classBase_1_1TimeInfo.html) FileInfo::lastRead  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the time when the file was last read (accessed).

References
[exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
[Base::TimeInfo::null()](../../df/d75/classBase_1_1TimeInfo.html#a1f75ecad31f55a21884ea6a36af41a67),
[Base::TimeInfo::setTime_t()](../../df/d75/classBase_1_1TimeInfo.html#ae874a0ed3ec680b6f1aefba28ec6974c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

## ◆ pathToString()

| std::string FileInfo::pathToString  | ( | const boost::filesystem::path & | _p_| ) |   
---|---|---|---|---|---  
static  
  
Convert from filesystem path to string.

## ◆ renameFile()

[bool](../../d9/db9/classbool.html) FileInfo::renameFile  | ( | const char *  | _NewName_| ) |   
---|---|---|---|---|---  
  
Rename the file.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
and
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e).

## ◆ setFile() [1/2]

void FileInfo::setFile  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
  
Set a new file name.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

Referenced by
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[FileInfo()](../../dd/d34/classBase_1_1FileInfo.html#ae586b7919e8716c8782a7e0ba44e76e0),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[Drawing::FeaturePage::getEditableTextsFromTemplate()](../../db/d0f/classDrawing_1_1FeaturePage.html#af1b06dab1d22245e410d1a251f5eda96),
[Base::Writer::getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc),
[App::PropertyFileIncluded::getUniqueFileName()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#ac6b94c77254825a17621686c38efd006),
[Mesh::MeshObject::load()](../../d8/dcc/classMesh_1_1MeshObject.html#a18e2e8170174a57463675c300bb8a584),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[Mesh::MeshObject::save()](../../d8/dcc/classMesh_1_1MeshObject.html#a4a20379185dd31620a2df5c047c695bc),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[Base::FileException::setFileName()](../../d1/dc2/classBase_1_1FileException.html#a0412edf20db63572bee4728e4209fe97),
and
[App::PropertyFileIncluded::setValue()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa9362fd089d933299e27a32607d771aa).

## ◆ setFile() [2/2]

void Base::FileInfo::setFile  | ( | const std::string & | _name_| ) |   
---|---|---|---|---|---  
  
Set a new file name.

References
[setFile()](../../dd/d34/classBase_1_1FileInfo.html#a8295101575413cfa1be9c4a5fe13684c).

Referenced by
[setFile()](../../dd/d34/classBase_1_1FileInfo.html#a8295101575413cfa1be9c4a5fe13684c).

## ◆ setPermissions()

[bool](../../d9/db9/classbool.html) FileInfo::setPermissions  | ( | [Permissions](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738) | _perms_| ) |   
---|---|---|---|---|---  
  
Tries to set the file permission.

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c),
[ReadOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738a2a81c484ad2171f79da987b019813a9c),
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304),
and
[WriteOnly](../../dd/d34/classBase_1_1FileInfo.html#a747c8b5c53639e0d55a2dbd32973a738ac642426fce847ed13f5cb06a233fc5bb).

Referenced by
[App::PropertyFileIncluded::Copy()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a8357945cf4e3e84abd535ef6d53d4f99),
[App::PropertyFileIncluded::Paste()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5598d54beecd9857ffe43b17aa0e8a4e),
[App::PropertyFileIncluded::Restore()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
and
[App::PropertyFileIncluded::RestoreDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0).

## ◆ size()

unsigned [int](../../d1/da0/classint.html) FileInfo::size  | ( | | ) |  const  
---|---|---|---|---  
  
The size of the file.

Referenced by
[gzip_utf8.GzipFile::close()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a5c40910b0ce0286256128c6dae8a2c9b),
[PathScripts.PostUtils.GCodeEditorDialog::done()](../../d2/da8/classPathScripts_1_1PostUtils_1_1GCodeEditorDialog.html#a248bce41aba9c00f132e290610d68fae),
and
[gzip_utf8.GzipFile::write()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a3148c5b71cccbdfce05d52d31114810e).

## ◆ stringToPath()

| boost::filesystem::path FileInfo::stringToPath  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
static  
  
Convert from string to filesystem path.

Referenced by
[createDirectories()](../../dd/d34/classBase_1_1FileInfo.html#ae2b639e68c2acc94843eced585d3fb08).

## ◆ toStdWString()

std::wstring FileInfo::toStdWString  | ( | | ) |  const  
---|---|---|---|---  
  
Convert the path name into a UTF-16 encoded wide string format.

Note

    : Use this function on Windows only. 

References
[FileName](../../dd/d34/classBase_1_1FileInfo.html#a13de85f9dcaaa4d283b1bd3f7c4a284c).

Referenced by
[copyTo()](../../dd/d34/classBase_1_1FileInfo.html#a47907e1927f6ff3b767f83ac846ef8e1),
[createDirectory()](../../dd/d34/classBase_1_1FileInfo.html#aa6f05ba743ce834588f77fdc15a1e7c4),
[deleteDirectory()](../../dd/d34/classBase_1_1FileInfo.html#a90076a5e4c647966ce0b79e58381f30e),
[deleteFile()](../../dd/d34/classBase_1_1FileInfo.html#aafd7a8df3d22c3e48523afe865115b9c),
[exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[getDirectoryContent()](../../dd/d34/classBase_1_1FileInfo.html#a9b33b65881316baad94257470aa77c07),
[isDir()](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f),
[isFile()](../../dd/d34/classBase_1_1FileInfo.html#ab7840bb4fca4b3d9938c1b3f0e1352ef),
[isReadable()](../../dd/d34/classBase_1_1FileInfo.html#aa7bd4cf0e93293d4c3bf057b53f02063),
[isWritable()](../../dd/d34/classBase_1_1FileInfo.html#a550b75d516c531e941faffbd70054862),
[lastModified()](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8),
[lastRead()](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0),
[Gui::SoSVGVectorOutput::openFile()](../../df/d57/classGui_1_1SoSVGVectorOutput.html#aa9fb309773930c52402b2511a075d338),
[Gui::SoU3DVectorOutput::openFile()](../../d7/dd7/classGui_1_1SoU3DVectorOutput.html#a046dd9fdaf6dee941a8d14ab622b3d62),
[renameFile()](../../dd/d34/classBase_1_1FileInfo.html#ac5067c657858a93f81d2fbfdd4fdf8eb),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Base::InterpreterSingleton::runFile()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae05d01943aa268be77244fa1e98e88f0),
[Gui::PythonDebugger::runFile()](../../d6/d11/classGui_1_1PythonDebugger.html#abc87bde9333762be5102ca6d99b14be6),
[setPermissions()](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23),
[zipios::ZipFile::ZipFile()](../../d7/da4/classzipios_1_1ZipFile.html#ac9bd79d4830c21157a4547c1c114ac53),
and
[zipios::ZipInputStream::ZipInputStream()](../../d0/d1f/classzipios_1_1ZipInputStream.html#a1a888477ad89e681f6959f056c1640d7).

## Member Data Documentation

## ◆ FileName

| std::string Base::FileInfo::FileName  
---  
protected  
  
Referenced by
[completeExtension()](../../dd/d34/classBase_1_1FileInfo.html#a6d041427fe955c1db09a9731503a728e),
[copyTo()](../../dd/d34/classBase_1_1FileInfo.html#a47907e1927f6ff3b767f83ac846ef8e1),
[createDirectories()](../../dd/d34/classBase_1_1FileInfo.html#ae2b639e68c2acc94843eced585d3fb08),
[createDirectory()](../../dd/d34/classBase_1_1FileInfo.html#aa6f05ba743ce834588f77fdc15a1e7c4),
[deleteDirectory()](../../dd/d34/classBase_1_1FileInfo.html#a90076a5e4c647966ce0b79e58381f30e),
[deleteFile()](../../dd/d34/classBase_1_1FileInfo.html#aafd7a8df3d22c3e48523afe865115b9c),
[dirPath()](../../dd/d34/classBase_1_1FileInfo.html#a931384d1da89e1295bb158617f3f5712),
[exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[extension()](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5),
[fileName()](../../dd/d34/classBase_1_1FileInfo.html#a8ae2069796787d27306bb49bd70e3e3a),
[filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[getDirectoryContent()](../../dd/d34/classBase_1_1FileInfo.html#a9b33b65881316baad94257470aa77c07),
[getTempFileName()](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74),
[isDir()](../../dd/d34/classBase_1_1FileInfo.html#aa941e087c82c28ff498d9d3dec551b1f),
[isFile()](../../dd/d34/classBase_1_1FileInfo.html#ab7840bb4fca4b3d9938c1b3f0e1352ef),
[isReadable()](../../dd/d34/classBase_1_1FileInfo.html#aa7bd4cf0e93293d4c3bf057b53f02063),
[isWritable()](../../dd/d34/classBase_1_1FileInfo.html#a550b75d516c531e941faffbd70054862),
[lastModified()](../../dd/d34/classBase_1_1FileInfo.html#aa87adf0f1e8c32d54ff01bbcf64dfff8),
[lastRead()](../../dd/d34/classBase_1_1FileInfo.html#a8d2e7762c1ce1c3ca606d2d3bda0bff0),
[renameFile()](../../dd/d34/classBase_1_1FileInfo.html#ac5067c657858a93f81d2fbfdd4fdf8eb),
[setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616),
[setPermissions()](../../dd/d34/classBase_1_1FileInfo.html#a5e5820903b5f70e76899d9962c0c6f23),
and
[toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/FileInfo.h
  * FreeCAD/src/Base/FileInfo.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

