---
url: https://freecad.github.io/SourceDoc/dd/d4d/classBase_1_1Writer.html
scraped_at: 2025-09-08T15:18:14.433251
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Writer](../../dd/d4d/classBase_1_1Writer.html)

[List of all members](../../dc/db4/classBase_1_1Writer-members.html) | Classes | Public Member Functions

Base::Writer Class Referenceabstract

The [Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This is
an important helper class for the store and retrieval system of persistent
o...") class This is an important helper class for the store and retrieval
system of persistent objects in FreeCAD.
[More...](../../dd/d4d/classBase_1_1Writer.html#details)

`#include <Writer.h>`

##  Classes  
  
---  
struct | [FileEntry](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html)  
  
##  Public Member Functions  
  
---  
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
additional file writing  
std::string | [addFile](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55) (const char *Name, const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *Object)  
| add a write request of a persistent object
[More...](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55)  
  
virtual void | [writeFiles](../../dd/d4d/classBase_1_1Writer.html#a4ac216f6afc4c088950ae53dc75a9e2d) ()=0  
| process the requested file storing
[More...](../../dd/d4d/classBase_1_1Writer.html#a4ac216f6afc4c088950ae53dc75a9e2d)  
  
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
  
Error handling  
void | [addError](../../dd/d4d/classBase_1_1Writer.html#a060e45ed91863b5535fa9c9721dde11f) (const std::string &)  
[bool](../../d9/db9/classbool.html) | [hasErrors](../../dd/d4d/classBase_1_1Writer.html#a63b47ea7f6739149a2df8c4bf6344f3a) () const  
void | [clearErrors](../../dd/d4d/classBase_1_1Writer.html#af772e74bbf7a1dd181af9fb5dfc94ccc) ()  
std::vector< std::string > | [getErrors](../../dd/d4d/classBase_1_1Writer.html#a0a8724e4f558be340dce98381cfc6097) () const  
  
## pretty formatting for XML  
  
---  
std::string | [ObjectName](../../dd/d4d/classBase_1_1Writer.html#a33392412488d03635dfb4527e3df677d)  
| name for underlying file saves
[More...](../../dd/d4d/classBase_1_1Writer.html#a33392412488d03635dfb4527e3df677d)  
  
std::vector< [FileEntry](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html) > | [FileList](../../dd/d4d/classBase_1_1Writer.html#a364da33cc8f9237793691c1ed545b866)  
std::vector< std::string > | [FileNames](../../dd/d4d/classBase_1_1Writer.html#afaea6adc505c9a950ce2b6385a7fec2c)  
std::vector< std::string > | [Errors](../../dd/d4d/classBase_1_1Writer.html#a20d9a8919ae090e2910a0b8068e7ff62)  
std::set< std::string > | [Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd)  
short | [indent](../../dd/d4d/classBase_1_1Writer.html#a51f1a622cb20d7dceb19ec58b1a111c5)  
char | [indBuf](../../dd/d4d/classBase_1_1Writer.html#acb8178b1adf60b3f6b58db2324456062) [1024]  
[bool](../../d9/db9/classbool.html) | [forceXML](../../dd/d4d/classBase_1_1Writer.html#aac5ceb3ba47d3598d2e357fe9c2afab1)  
[int](../../d1/da0/classint.html) | [fileVersion](../../dd/d4d/classBase_1_1Writer.html#ade28c77127289e039bc9eeccfe40ff61)  
const char * | [ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368) () const  
| get the current indentation
[More...](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368)  
  
void | [incInd](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5) ()  
| increase indentation by one tab
[More...](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5)  
  
void | [decInd](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92) ()  
| decrease indentation by one tab
[More...](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92)  
  
virtual std::ostream & | [Stream](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205) ()=0  
std::string | [getUniqueFileName](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc) (const char *Name)  
  
## Detailed Description

The [Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This is
an important helper class for the store and retrieval system of persistent
o...") class This is an important helper class for the store and retrieval
system of persistent objects in FreeCAD.

See also

    [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class and root of the type system.")

Author

    Juergen Riegel 

## Constructor & Destructor Documentation

## ◆ Writer()

Writer::Writer  | ( | | ) |   
---|---|---|---|---  
  
References
[indBuf](../../dd/d4d/classBase_1_1Writer.html#acb8178b1adf60b3f6b58db2324456062).

## ◆ ~Writer()

| Writer::~Writer  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addError()

void Writer::addError  | ( | const std::string & | _msg_| ) |   
---|---|---|---|---|---  
  
References
[Errors](../../dd/d4d/classBase_1_1Writer.html#a20d9a8919ae090e2910a0b8068e7ff62).

Referenced by
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b).

## ◆ addFile()

std::string Writer::addFile  | ( | const char *  | _Name_ ,   
---|---|---|---  
|  | const [Base::Persistence](../../d9/d25/classBase_1_1Persistence.html) *  | _Object_  
| ) | |   
  
add a write request of a persistent object

References
[FileList](../../dd/d4d/classBase_1_1Writer.html#a364da33cc8f9237793691c1ed545b866),
[Base::Writer::FileEntry::FileName](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#abd6c12817010758a25f9af39c2c3a70c),
[FileNames](../../dd/d4d/classBase_1_1Writer.html#afaea6adc505c9a950ce2b6385a7fec2c),
[getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc),
[isForceXML()](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6),
and
[Base::Writer::FileEntry::Object](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html#a15a35046c9bd5dad11dd5d97c18d675f).

Referenced by
[Fem::FemMesh::Save()](../../d3/d2e/classFem_1_1FemMesh.html#ad8e9b3ebd3dec1f3c6716e7e5db4f9ef),
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::VRMLObject::Save()](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3),
[Gui::Document::Save()](../../de/d4e/classGui_1_1Document.html#a17dba40a2ef0e606900ad09fadca20f5),
[Gui::Thumbnail::Save()](../../d3/d4d/classGui_1_1Thumbnail.html#afd06c326111670d8cf2d296e094ab0f6),
[Fem::PropertyPostDataObject::Save()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a95feddffb556cb077d779dabafe7232b),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Mesh::PropertyNormalList::Save()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Mesh::PropertyCurvatureList::Save()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Mesh::PropertyMeshKernel::Save()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a4a43a02937b4bee415437e54cba3ad5a),
[Part::PropertyPartShape::Save()](../../d7/d28/classPart_1_1PropertyPartShape.html#ab90c789bcc0e243359d66b110d7e5517),
[Part::PropertyFilletEdges::Save()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a0e7532f6fa496fb602617495364aed71),
[Points::PointKernel::Save()](../../dc/de1/classPoints_1_1PointKernel.html#a2b6a9c3ce6a26f1b0756db4fe67daa91),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Points::PropertyNormalList::Save()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Points::PropertyCurvatureList::Save()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[App::PropertyVectorList::Save()](../../d5/d13/classApp_1_1PropertyVectorList.html#a5f00ee26daf66ffaa7bc7a6974c71467),
[App::PropertyPlacementList::Save()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7e1537af27ac4c78360e5f75699b3a8e),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyColorList::Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1),
and
[App::PropertyMaterialList::Save()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a83f1b747fe9b8b41254e244294809f4a).

## ◆ clearErrors()

void Writer::clearErrors  | ( | | ) |   
---|---|---|---|---  
  
References
[Errors](../../dd/d4d/classBase_1_1Writer.html#a20d9a8919ae090e2910a0b8068e7ff62).

## ◆ clearMode()

void Writer::clearMode  | ( | const std::string & | _mode_| ) |   
---|---|---|---|---|---  
  
Clear mode.

References
[Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd).

## ◆ clearModes()

void Writer::clearModes  | ( | | ) |   
---|---|---|---|---  
  
Clear modes.

References
[Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd).

## ◆ decInd()

void Writer::decInd  | ( | | ) |   
---|---|---|---|---  
  
decrease indentation by one tab

References
[indBuf](../../dd/d4d/classBase_1_1Writer.html#acb8178b1adf60b3f6b58db2324456062),
and
[indent](../../dd/d4d/classBase_1_1Writer.html#a51f1a622cb20d7dceb19ec58b1a111c5).

Referenced by
[Spreadsheet::PropertySheet::copyCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad4547b9f9b5dc69f0541e8c307fc98df),
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
[Part::Geometry::Save()](../../dc/df0/classPart_1_1Geometry.html#afdca307efd3460ac12d9d11212e1019e),
[Part::GeomBSplineCurve::Save()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#aca65bd3ef743a053f69ca6a17b750a1d),
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[Path::Tooltable::Save()](../../df/dca/classPath_1_1Tooltable.html#a4d341fe1c98f1ebe4c6b06b46f8aa54e),
[Robot::Trajectory::Save()](../../d7/d14/classRobot_1_1Trajectory.html#a4b7ed465fb7575ec163f78c8e3485a3d),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::Generic::Save()](../../dd/d23/classTechDraw_1_1Generic.html#a40f63eb0caff9ecc530a2355ba704ef7),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::PropertyEnumeration::Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[App::PropertyIntegerSet::Save()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#aac6c3e40141af20243f925cfe96ee552),
[App::PropertyMap::Save()](../../db/d3f/classApp_1_1PropertyMap.html#a97872819db9f4c70a132c8995df2369a),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Part::PropertyGeometryList::Save()](../../db/dca/classPart_1_1PropertyGeometryList.html#aaab5a1c8943cf5a2ec331fc97dc14938),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Spreadsheet::PropertyColumnWidths::Save()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a976f43505863b7470c1eb93726de2d5e),
[Spreadsheet::PropertyRowHeights::Save()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a7dbc1225885f9daac0294390384589d6),
[TechDraw::PropertyCenterLineList::Save()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2ca2a9291bf7a7d3a3e4445b27d1e0b0),
[TechDraw::PropertyCosmeticEdgeList::Save()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a278a66fea5146613150022462cd5866b),
[TechDraw::PropertyCosmeticVertexList::Save()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a76a4d9006162906f7df1bc9544c03f42),
[TechDraw::PropertyGeomFormatList::Save()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ab0cfb70b4099f758b0969d3b76176ef5),
[App::PropertyExpressionEngine::Save()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e),
[App::PropertyLinkList::Save()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a5615ef760136231d57a938213dd9bd36),
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkSubList::Save()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[App::PropertyIntegerList::Save()](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7205d3bff255da22b44e7737b4f90529),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyStringList::Save()](../../d8/d55/classApp_1_1PropertyStringList.html#ae923a954a46e42768bec37194a9c69e2),
[App::PropertyPersistentObject::Save()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7),
[Sketcher::PropertyConstraintList::Save()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a0bb1d243847dd000f61a4b326df0b184),
[Spreadsheet::PropertySheet::Save()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac590ae825fd968155d7efb7801ddeb74),
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b),
[App::ExtensionContainer::saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
and
[App::Document::writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ getErrors()

std::vector< std::string > Writer::getErrors  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Errors](../../dd/d4d/classBase_1_1Writer.html#a20d9a8919ae090e2910a0b8068e7ff62).

## ◆ getFilenames()

const std::vector< std::string > & Writer::getFilenames  | ( | | ) |  const  
---|---|---|---|---  
  
get all registered file names

References
[FileNames](../../dd/d4d/classBase_1_1Writer.html#afaea6adc505c9a950ce2b6385a7fec2c).

## ◆ getFileVersion()

[int](../../d1/da0/classint.html) Writer::getFileVersion  | ( | | ) |  const  
---|---|---|---|---  
  
References
[fileVersion](../../dd/d4d/classBase_1_1Writer.html#ade28c77127289e039bc9eeccfe40ff61).

Referenced by
[App::Document::Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0).

## ◆ getMode()

[bool](../../d9/db9/classbool.html) Writer::getMode  | ( | const std::string & | _mode_| ) |  const  
---|---|---|---|---|---  
  
Get mode.

References
[Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd).

Referenced by
[Part::PropertyPartShape::Save()](../../d7/d28/classPart_1_1PropertyPartShape.html#ab90c789bcc0e243359d66b110d7e5517),
and
[Part::PropertyPartShape::SaveDocFile()](../../d7/d28/classPart_1_1PropertyPartShape.html#a0a5d9ad2a3ed87aa769ab8e36f51d2f2).

## ◆ getModes()

std::set< std::string > Writer::getModes  | ( | | ) |  const  
---|---|---|---|---  
  
Get modes.

References
[Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd).

Referenced by
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c).

## ◆ getUniqueFileName()

| std::string Writer::getUniqueFileName  | ( | const char *  | _Name_| ) |   
---|---|---|---|---|---  
protected  
  
References
[Base::FileInfo::extension()](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5),
[Base::FileInfo::fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[FileNames](../../dd/d4d/classBase_1_1Writer.html#afaea6adc505c9a950ce2b6385a7fec2c),
[DraftVecUtils::find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b),
and
[Base::FileInfo::setFile()](../../dd/d34/classBase_1_1FileInfo.html#ad254d88b127a0e93086c58f9c0487616).

Referenced by
[addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55).

## ◆ hasErrors()

[bool](../../d9/db9/classbool.html) Writer::hasErrors  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Errors](../../dd/d4d/classBase_1_1Writer.html#a20d9a8919ae090e2910a0b8068e7ff62).

Referenced by
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ incInd()

void Writer::incInd  | ( | | ) |   
---|---|---|---|---  
  
increase indentation by one tab

References
[indBuf](../../dd/d4d/classBase_1_1Writer.html#acb8178b1adf60b3f6b58db2324456062),
and
[indent](../../dd/d4d/classBase_1_1Writer.html#a51f1a622cb20d7dceb19ec58b1a111c5).

Referenced by
[Spreadsheet::PropertySheet::copyCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad4547b9f9b5dc69f0541e8c307fc98df),
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
[Part::Geometry::Save()](../../dc/df0/classPart_1_1Geometry.html#afdca307efd3460ac12d9d11212e1019e),
[Part::GeomBSplineCurve::Save()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#aca65bd3ef743a053f69ca6a17b750a1d),
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[Path::Tooltable::Save()](../../df/dca/classPath_1_1Tooltable.html#a4d341fe1c98f1ebe4c6b06b46f8aa54e),
[Robot::Trajectory::Save()](../../d7/d14/classRobot_1_1Trajectory.html#a4b7ed465fb7575ec163f78c8e3485a3d),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::Generic::Save()](../../dd/d23/classTechDraw_1_1Generic.html#a40f63eb0caff9ecc530a2355ba704ef7),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::PropertyEnumeration::Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[App::PropertyIntegerSet::Save()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#aac6c3e40141af20243f925cfe96ee552),
[App::PropertyMap::Save()](../../db/d3f/classApp_1_1PropertyMap.html#a97872819db9f4c70a132c8995df2369a),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Part::PropertyGeometryList::Save()](../../db/dca/classPart_1_1PropertyGeometryList.html#aaab5a1c8943cf5a2ec331fc97dc14938),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Spreadsheet::PropertyColumnWidths::Save()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a976f43505863b7470c1eb93726de2d5e),
[Spreadsheet::PropertyRowHeights::Save()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a7dbc1225885f9daac0294390384589d6),
[TechDraw::PropertyCenterLineList::Save()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2ca2a9291bf7a7d3a3e4445b27d1e0b0),
[TechDraw::PropertyCosmeticEdgeList::Save()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a278a66fea5146613150022462cd5866b),
[TechDraw::PropertyCosmeticVertexList::Save()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a76a4d9006162906f7df1bc9544c03f42),
[TechDraw::PropertyGeomFormatList::Save()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ab0cfb70b4099f758b0969d3b76176ef5),
[App::PropertyExpressionEngine::Save()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e),
[App::PropertyLinkList::Save()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a5615ef760136231d57a938213dd9bd36),
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkSubList::Save()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[App::PropertyIntegerList::Save()](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7205d3bff255da22b44e7737b4f90529),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyStringList::Save()](../../d8/d55/classApp_1_1PropertyStringList.html#ae923a954a46e42768bec37194a9c69e2),
[App::PropertyPersistentObject::Save()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7),
[Sketcher::PropertyConstraintList::Save()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a0bb1d243847dd000f61a4b326df0b184),
[Spreadsheet::PropertySheet::Save()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac590ae825fd968155d7efb7801ddeb74),
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b),
[App::ExtensionContainer::saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
and
[App::Document::writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ ind()

const char * Base::Writer::ind  | ( | | ) |  const  
---|---|---|---|---  
  
get the current indentation

Referenced by
[Spreadsheet::PropertySheet::copyCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad4547b9f9b5dc69f0541e8c307fc98df),
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
[Fem::FemMesh::Save()](../../d3/d2e/classFem_1_1FemMesh.html#ad8e9b3ebd3dec1f3c6716e7e5db4f9ef),
[Part::Geometry::Save()](../../dc/df0/classPart_1_1Geometry.html#afdca307efd3460ac12d9d11212e1019e),
[Part::GeomPoint::Save()](../../d2/dfb/classPart_1_1GeomPoint.html#a7e8b345036cf110981470940974c9421),
[Part::GeomBSplineCurve::Save()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#aca65bd3ef743a053f69ca6a17b750a1d),
[Part::GeomCircle::Save()](../../d0/dde/classPart_1_1GeomCircle.html#a2f7a8a988205a3502995c750c42a1aaf),
[Part::GeomArcOfCircle::Save()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#abb7da9e20b87676c9557910696b97349),
[Part::GeomEllipse::Save()](../../db/d52/classPart_1_1GeomEllipse.html#ab0790cef5529063209a951021f1f994d),
[Part::GeomArcOfEllipse::Save()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a72706ed4fdf3b0243d4d72b2db42db85),
[Part::GeomHyperbola::Save()](../../d7/d9e/classPart_1_1GeomHyperbola.html#a1d363e31ed931e93b4c0c62b8ae8018e),
[Part::GeomArcOfHyperbola::Save()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#aab8732d0bd4af614691d908a63c31429),
[Part::GeomParabola::Save()](../../d9/ddf/classPart_1_1GeomParabola.html#a70eb5699782809d25fc97d63e9621b82),
[Part::GeomArcOfParabola::Save()](../../db/ddc/classPart_1_1GeomArcOfParabola.html#a2cac7fa995e020b7c51049929c5eae65),
[Part::GeomLine::Save()](../../d5/d30/classPart_1_1GeomLine.html#a88fd00890c6c4e7729b05c279a64656d),
[Part::GeomLineSegment::Save()](../../d9/d6f/classPart_1_1GeomLineSegment.html#acc377c70086de1bfbfd88e523b663529),
[Part::Geom2dPoint::Save()](../../d8/da9/classPart_1_1Geom2dPoint.html#a6cb271d4c4de1c17c078eed91bc53a52),
[Part::Geom2dCircle::Save()](../../d7/d4e/classPart_1_1Geom2dCircle.html#a7c7cdaca3789102fbfdd9ab3aa8fe408),
[Part::Geom2dArcOfCircle::Save()](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a7a2a3066d0fb89137073b6700ab613ce),
[Part::Geom2dEllipse::Save()](../../db/db9/classPart_1_1Geom2dEllipse.html#ae7f027bb3905600426bfd2427f766bd9),
[Part::Geom2dArcOfEllipse::Save()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a5b11e14c488d2aa4cf7beed42745f196),
[Part::Geom2dHyperbola::Save()](../../d2/d95/classPart_1_1Geom2dHyperbola.html#af5ea41c1bb958c6654b71ddd5d1f9b46),
[Part::Geom2dArcOfHyperbola::Save()](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#adedc32e2aed23cac9140c5d9007d1796),
[Part::Geom2dParabola::Save()](../../d9/dff/classPart_1_1Geom2dParabola.html#afe579248a312b0b96cdc9df68c84208b),
[Part::Geom2dArcOfParabola::Save()](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a647166ea11f48f42548738541a21c92f),
[Part::Geom2dLineSegment::Save()](../../df/ded/classPart_1_1Geom2dLineSegment.html#af2f3e338722ce52e89ce1624e57e4d31),
[Part::GeometryPersistenceExtension::Save()](../../de/db6/classPart_1_1GeometryPersistenceExtension.html#af4b4cb8e926350eb9cf1f7c78ce2a7c8),
[Path::Command::Save()](../../d7/d2e/classPath_1_1Command.html#aa1b581f8eaf7d8d238ae8f9cdff9d485),
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[Path::Tool::Save()](../../dd/dfe/classPath_1_1Tool.html#af460887ae0bff6e585c176ec5fb7d090),
[Path::Tooltable::Save()](../../df/dca/classPath_1_1Tooltable.html#a4d341fe1c98f1ebe4c6b06b46f8aa54e),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Trajectory::Save()](../../d7/d14/classRobot_1_1Trajectory.html#a4b7ed465fb7575ec163f78c8e3485a3d),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[TechDraw::CosmeticVertex::Save()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#aee8e2101aa119ae2dc4750442745264c),
[TechDraw::CosmeticEdge::Save()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a31c75a92b51476f8968d584e6be31d6c),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::GeomFormat::Save()](../../d7/d64/classTechDraw_1_1GeomFormat.html#a6f418ed280615fd0ad22d9bea8d19070),
[TechDraw::Vertex::Save()](../../dd/db1/classTechDraw_1_1Vertex.html#aed3011b8fc0de22659800304c3f1b0af),
[Gui::DocumentItem::Save()](../../df/d15/classGui_1_1DocumentItem.html#a39b445578a0bb04a1e70f68910a69472),
[Sketcher::Constraint::Save()](../../d6/def/classSketcher_1_1Constraint.html#a88eebfd4c47c91fe0325cfacbd93b5cc),
[TechDraw::BaseGeom::Save()](../../db/d3c/classTechDraw_1_1BaseGeom.html#abad15f5dfecd726e438d459eab1e00dd),
[TechDraw::Circle::Save()](../../d3/d63/classTechDraw_1_1Circle.html#ab3a64b9c96ec1f8dc658f0432955bfa5),
[TechDraw::AOC::Save()](../../d0/d5c/classTechDraw_1_1AOC.html#a4627154c0a8d5886ee4ee54231107de2),
[TechDraw::Generic::Save()](../../dd/d23/classTechDraw_1_1Generic.html#a40f63eb0caff9ecc530a2355ba704ef7),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::PropertyMatrix::Save()](../../d8/d77/classApp_1_1PropertyMatrix.html#a3880b86eb64ba6104ad5fd9ec0d2514f),
[App::PropertyPythonObject::Save()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a6ef3c19e6ce7cb04aeb9f9c577551e7e),
[App::PropertyInteger::Save()](../../dd/d85/classApp_1_1PropertyInteger.html#a0c826cdd034a3b4bda67fb25b37cad70),
[App::PropertyPath::Save()](../../dc/d24/classApp_1_1PropertyPath.html#a45c4b988fe3e59cadd90a86d13864c30),
[App::PropertyEnumeration::Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[App::PropertyIntegerSet::Save()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#aac6c3e40141af20243f925cfe96ee552),
[App::PropertyMap::Save()](../../db/d3f/classApp_1_1PropertyMap.html#a97872819db9f4c70a132c8995df2369a),
[App::PropertyFloat::Save()](../../d3/dbe/classApp_1_1PropertyFloat.html#a4d58561153acf13b6eda8b115deb33a7),
[App::PropertyString::Save()](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164),
[App::PropertyUUID::Save()](../../d2/d6c/classApp_1_1PropertyUUID.html#a10ff7273e6db8ef0a7199d32212cf6a5),
[App::PropertyBool::Save()](../../dc/d81/classApp_1_1PropertyBool.html#a8c59652996dcffd9f4a2d503afaccd29),
[App::PropertyColor::Save()](../../d9/d0b/classApp_1_1PropertyColor.html#a0b4dc7c8284cd7511308f8bb55dc56d0),
[App::PropertyMaterial::Save()](../../d0/df5/classApp_1_1PropertyMaterial.html#a286a132daf0dd131911a0b20a6a64db5),
[Fem::PropertyPostDataObject::Save()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a95feddffb556cb077d779dabafe7232b),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Mesh::PropertyNormalList::Save()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Mesh::PropertyCurvatureList::Save()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Mesh::PropertyMeshKernel::Save()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a4a43a02937b4bee415437e54cba3ad5a),
[Part::PropertyGeometryList::Save()](../../db/dca/classPart_1_1PropertyGeometryList.html#aaab5a1c8943cf5a2ec331fc97dc14938),
[Part::PropertyPartShape::Save()](../../d7/d28/classPart_1_1PropertyPartShape.html#ab90c789bcc0e243359d66b110d7e5517),
[Part::PropertyFilletEdges::Save()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a0e7532f6fa496fb602617495364aed71),
[Points::PointKernel::Save()](../../dc/de1/classPoints_1_1PointKernel.html#a2b6a9c3ce6a26f1b0756db4fe67daa91),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Points::PropertyNormalList::Save()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Points::PropertyCurvatureList::Save()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Spreadsheet::Cell::save()](../../d5/d22/classSpreadsheet_1_1Cell.html#a6a34f1ee9208af26c12c858780b24874),
[Spreadsheet::PropertyColumnWidths::Save()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a976f43505863b7470c1eb93726de2d5e),
[Spreadsheet::PropertyRowHeights::Save()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a7dbc1225885f9daac0294390384589d6),
[TechDraw::PropertyCenterLineList::Save()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2ca2a9291bf7a7d3a3e4445b27d1e0b0),
[TechDraw::PropertyCosmeticEdgeList::Save()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a278a66fea5146613150022462cd5866b),
[TechDraw::PropertyCosmeticVertexList::Save()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a76a4d9006162906f7df1bc9544c03f42),
[TechDraw::PropertyGeomFormatList::Save()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ab0cfb70b4099f758b0969d3b76176ef5),
[App::PropertyExpressionEngine::Save()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e),
[App::PropertyVector::Save()](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10),
[App::PropertyVectorList::Save()](../../d5/d13/classApp_1_1PropertyVectorList.html#a5f00ee26daf66ffaa7bc7a6974c71467),
[App::PropertyPlacement::Save()](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1),
[App::PropertyPlacementList::Save()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7e1537af27ac4c78360e5f75699b3a8e),
[App::PropertyRotation::Save()](../../df/d76/classApp_1_1PropertyRotation.html#ad9e882ab49bd192e84f62de9a64c62ce),
[App::PropertyLink::Save()](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8),
[App::PropertyLinkList::Save()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a5615ef760136231d57a938213dd9bd36),
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkSubList::Save()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[App::PropertyIntegerList::Save()](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7205d3bff255da22b44e7737b4f90529),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyStringList::Save()](../../d8/d55/classApp_1_1PropertyStringList.html#ae923a954a46e42768bec37194a9c69e2),
[App::PropertyBoolList::Save()](../../d1/dcf/classApp_1_1PropertyBoolList.html#add6fd55ff90b5b181391621f6fadae36),
[App::PropertyColorList::Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1),
[App::PropertyMaterialList::Save()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a83f1b747fe9b8b41254e244294809f4a),
[App::PropertyPersistentObject::Save()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7),
[Sketcher::PropertyConstraintList::Save()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a0bb1d243847dd000f61a4b326df0b184),
[Spreadsheet::PropertySheet::Save()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac590ae825fd968155d7efb7801ddeb74),
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b),
[App::ExtensionContainer::saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
and
[App::Document::writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ insertAsciiFile()

void Writer::insertAsciiFile  | ( | const char *  | _FileName_| ) |   
---|---|---|---|---|---  
  
insert a file as CDATA section in the XML file

References
[Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ insertBinFile()

void Writer::insertBinFile  | ( | const char *  | _FileName_| ) |   
---|---|---|---|---|---  
  
insert a binary file BASE64 coded as CDATA section in the XML file

References
[Base::base64_encode()](../../db/d07/namespaceBase.html#a3a68598115d554cfc1fd43f196e98adb),
and
[Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8).

## ◆ isForceXML()

[bool](../../d9/db9/classbool.html) Writer::isForceXML  | ( | | ) |   
---|---|---|---|---  
  
check on state

References
[forceXML](../../dd/d4d/classBase_1_1Writer.html#aac5ceb3ba47d3598d2e357fe9c2afab1).

Referenced by
[addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
[Fem::FemMesh::Save()](../../d3/d2e/classFem_1_1FemMesh.html#ad8e9b3ebd3dec1f3c6716e7e5db4f9ef),
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[Gui::Document::Save()](../../de/d4e/classGui_1_1Document.html#a17dba40a2ef0e606900ad09fadca20f5),
[Gui::Thumbnail::Save()](../../d3/d4d/classGui_1_1Thumbnail.html#afd06c326111670d8cf2d296e094ab0f6),
[Fem::PropertyPostDataObject::Save()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a95feddffb556cb077d779dabafe7232b),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Mesh::PropertyNormalList::Save()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Mesh::PropertyCurvatureList::Save()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Mesh::PropertyMeshKernel::Save()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a4a43a02937b4bee415437e54cba3ad5a),
[Part::PropertyPartShape::Save()](../../d7/d28/classPart_1_1PropertyPartShape.html#ab90c789bcc0e243359d66b110d7e5517),
[Part::PropertyFilletEdges::Save()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a0e7532f6fa496fb602617495364aed71),
[Points::PointKernel::Save()](../../dc/de1/classPoints_1_1PointKernel.html#a2b6a9c3ce6a26f1b0756db4fe67daa91),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Points::PropertyNormalList::Save()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Points::PropertyCurvatureList::Save()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[App::PropertyVectorList::Save()](../../d5/d13/classApp_1_1PropertyVectorList.html#a5f00ee26daf66ffaa7bc7a6974c71467),
[App::PropertyPlacementList::Save()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7e1537af27ac4c78360e5f75699b3a8e),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyColorList::Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1),
[App::PropertyMaterialList::Save()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a83f1b747fe9b8b41254e244294809f4a),
and
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b).

## ◆ setFileVersion()

void Writer::setFileVersion  | ( | [int](../../d1/da0/classint.html) | _v_| ) |   
---|---|---|---|---|---  
  
References
[fileVersion](../../dd/d4d/classBase_1_1Writer.html#ade28c77127289e039bc9eeccfe40ff61).

## ◆ setForceXML()

void Writer::setForceXML  | ( | [bool](../../d9/db9/classbool.html) | _on_| ) |   
---|---|---|---|---|---  
  
switch the writer in XML only mode (no files allowed)

References
[forceXML](../../dd/d4d/classBase_1_1Writer.html#aac5ceb3ba47d3598d2e357fe9c2afab1).

Referenced by
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
and
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b).

## ◆ setMode()

void Writer::setMode  | ( | const std::string & | _mode_| ) |   
---|---|---|---|---|---  
  
Set mode.

References
[Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd).

Referenced by
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71),
[Base::Persistence::dumpToStream()](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
and
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ setModes()

void Writer::setModes  | ( | const std::set< std::string > & | _modes_| ) |   
---|---|---|---|---|---  
  
Set modes.

References
[Modes](../../dd/d4d/classBase_1_1Writer.html#ac621e7c0f597b9220dd9bdab6acab4dd).

Referenced by
[Gui::RecoveryRunnable::RecoveryRunnable()](../../d9/dc2/classGui_1_1RecoveryRunnable.html#aa1a456691d55fb28fb664f5fbc60bdfc).

## ◆ Stream()

| virtual std::ostream & Base::Writer::Stream  | ( | | ) |   
---|---|---|---|---  
pure virtual  
  
Implemented in
[Base::ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html#a37330d3d5bff097e58268aa7853abaa4),
[Base::StringWriter](../../dd/ddf/classBase_1_1StringWriter.html#ada958264e1957ee52bb714dd02a6c61e),
[Base::FileWriter](../../df/de4/classBase_1_1FileWriter.html#a8afbc7f269c0994675f1a2751dde9cdc),
and
[Cloud::CloudWriter](../../d0/d23/classCloud_1_1CloudWriter.html#ac6dec3675fe3bead371f8d345b707dc6).

Referenced by
[Spreadsheet::PropertySheet::copyCells()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad4547b9f9b5dc69f0541e8c307fc98df),
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
[insertAsciiFile()](../../dd/d4d/classBase_1_1Writer.html#ac188706203bae688ddec31a05e57425d),
[insertBinFile()](../../dd/d4d/classBase_1_1Writer.html#aafe5f2af569301dbae674de29e757de4),
[Fem::FemMesh::Save()](../../d3/d2e/classFem_1_1FemMesh.html#ad8e9b3ebd3dec1f3c6716e7e5db4f9ef),
[Part::Geometry::Save()](../../dc/df0/classPart_1_1Geometry.html#afdca307efd3460ac12d9d11212e1019e),
[Part::GeomPoint::Save()](../../d2/dfb/classPart_1_1GeomPoint.html#a7e8b345036cf110981470940974c9421),
[Part::GeomBSplineCurve::Save()](../../df/dfe/classPart_1_1GeomBSplineCurve.html#aca65bd3ef743a053f69ca6a17b750a1d),
[Part::GeomCircle::Save()](../../d0/dde/classPart_1_1GeomCircle.html#a2f7a8a988205a3502995c750c42a1aaf),
[Part::GeomArcOfCircle::Save()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#abb7da9e20b87676c9557910696b97349),
[Part::GeomEllipse::Save()](../../db/d52/classPart_1_1GeomEllipse.html#ab0790cef5529063209a951021f1f994d),
[Part::GeomArcOfEllipse::Save()](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a72706ed4fdf3b0243d4d72b2db42db85),
[Part::GeomHyperbola::Save()](../../d7/d9e/classPart_1_1GeomHyperbola.html#a1d363e31ed931e93b4c0c62b8ae8018e),
[Part::GeomArcOfHyperbola::Save()](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#aab8732d0bd4af614691d908a63c31429),
[Part::GeomParabola::Save()](../../d9/ddf/classPart_1_1GeomParabola.html#a70eb5699782809d25fc97d63e9621b82),
[Part::GeomArcOfParabola::Save()](../../db/ddc/classPart_1_1GeomArcOfParabola.html#a2cac7fa995e020b7c51049929c5eae65),
[Part::GeomLine::Save()](../../d5/d30/classPart_1_1GeomLine.html#a88fd00890c6c4e7729b05c279a64656d),
[Part::GeomLineSegment::Save()](../../d9/d6f/classPart_1_1GeomLineSegment.html#acc377c70086de1bfbfd88e523b663529),
[Part::Geom2dPoint::Save()](../../d8/da9/classPart_1_1Geom2dPoint.html#a6cb271d4c4de1c17c078eed91bc53a52),
[Part::Geom2dCircle::Save()](../../d7/d4e/classPart_1_1Geom2dCircle.html#a7c7cdaca3789102fbfdd9ab3aa8fe408),
[Part::Geom2dArcOfCircle::Save()](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a7a2a3066d0fb89137073b6700ab613ce),
[Part::Geom2dEllipse::Save()](../../db/db9/classPart_1_1Geom2dEllipse.html#ae7f027bb3905600426bfd2427f766bd9),
[Part::Geom2dArcOfEllipse::Save()](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a5b11e14c488d2aa4cf7beed42745f196),
[Part::Geom2dHyperbola::Save()](../../d2/d95/classPart_1_1Geom2dHyperbola.html#af5ea41c1bb958c6654b71ddd5d1f9b46),
[Part::Geom2dArcOfHyperbola::Save()](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#adedc32e2aed23cac9140c5d9007d1796),
[Part::Geom2dParabola::Save()](../../d9/dff/classPart_1_1Geom2dParabola.html#afe579248a312b0b96cdc9df68c84208b),
[Part::Geom2dArcOfParabola::Save()](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a647166ea11f48f42548738541a21c92f),
[Part::Geom2dLineSegment::Save()](../../df/ded/classPart_1_1Geom2dLineSegment.html#af2f3e338722ce52e89ce1624e57e4d31),
[Part::GeometryPersistenceExtension::Save()](../../de/db6/classPart_1_1GeometryPersistenceExtension.html#af4b4cb8e926350eb9cf1f7c78ce2a7c8),
[Path::Command::Save()](../../d7/d2e/classPath_1_1Command.html#aa1b581f8eaf7d8d238ae8f9cdff9d485),
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[Path::Tool::Save()](../../dd/dfe/classPath_1_1Tool.html#af460887ae0bff6e585c176ec5fb7d090),
[Path::Tooltable::Save()](../../df/dca/classPath_1_1Tooltable.html#a4d341fe1c98f1ebe4c6b06b46f8aa54e),
[Robot::Robot6Axis::Save()](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::Trajectory::Save()](../../d7/d14/classRobot_1_1Trajectory.html#a4b7ed465fb7575ec163f78c8e3485a3d),
[Robot::Waypoint::Save()](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[TechDraw::CosmeticVertex::Save()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#aee8e2101aa119ae2dc4750442745264c),
[TechDraw::CosmeticEdge::Save()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a31c75a92b51476f8968d584e6be31d6c),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::GeomFormat::Save()](../../d7/d64/classTechDraw_1_1GeomFormat.html#a6f418ed280615fd0ad22d9bea8d19070),
[TechDraw::Vertex::Save()](../../dd/db1/classTechDraw_1_1Vertex.html#aed3011b8fc0de22659800304c3f1b0af),
[Gui::DocumentItem::Save()](../../df/d15/classGui_1_1DocumentItem.html#a39b445578a0bb04a1e70f68910a69472),
[Sketcher::Constraint::Save()](../../d6/def/classSketcher_1_1Constraint.html#a88eebfd4c47c91fe0325cfacbd93b5cc),
[TechDraw::BaseGeom::Save()](../../db/d3c/classTechDraw_1_1BaseGeom.html#abad15f5dfecd726e438d459eab1e00dd),
[TechDraw::Circle::Save()](../../d3/d63/classTechDraw_1_1Circle.html#ab3a64b9c96ec1f8dc658f0432955bfa5),
[TechDraw::AOC::Save()](../../d0/d5c/classTechDraw_1_1AOC.html#a4627154c0a8d5886ee4ee54231107de2),
[TechDraw::Generic::Save()](../../dd/d23/classTechDraw_1_1Generic.html#a40f63eb0caff9ecc530a2355ba704ef7),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::PropertyMatrix::Save()](../../d8/d77/classApp_1_1PropertyMatrix.html#a3880b86eb64ba6104ad5fd9ec0d2514f),
[App::PropertyPythonObject::Save()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a6ef3c19e6ce7cb04aeb9f9c577551e7e),
[App::PropertyInteger::Save()](../../dd/d85/classApp_1_1PropertyInteger.html#a0c826cdd034a3b4bda67fb25b37cad70),
[App::PropertyPath::Save()](../../dc/d24/classApp_1_1PropertyPath.html#a45c4b988fe3e59cadd90a86d13864c30),
[App::PropertyEnumeration::Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[App::PropertyIntegerSet::Save()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#aac6c3e40141af20243f925cfe96ee552),
[App::PropertyMap::Save()](../../db/d3f/classApp_1_1PropertyMap.html#a97872819db9f4c70a132c8995df2369a),
[App::PropertyFloat::Save()](../../d3/dbe/classApp_1_1PropertyFloat.html#a4d58561153acf13b6eda8b115deb33a7),
[App::PropertyString::Save()](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164),
[App::PropertyUUID::Save()](../../d2/d6c/classApp_1_1PropertyUUID.html#a10ff7273e6db8ef0a7199d32212cf6a5),
[App::PropertyBool::Save()](../../dc/d81/classApp_1_1PropertyBool.html#a8c59652996dcffd9f4a2d503afaccd29),
[App::PropertyColor::Save()](../../d9/d0b/classApp_1_1PropertyColor.html#a0b4dc7c8284cd7511308f8bb55dc56d0),
[App::PropertyMaterial::Save()](../../d0/df5/classApp_1_1PropertyMaterial.html#a286a132daf0dd131911a0b20a6a64db5),
[Fem::PropertyPostDataObject::Save()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a95feddffb556cb077d779dabafe7232b),
[Inspection::PropertyDistanceList::Save()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Mesh::PropertyNormalList::Save()](../../df/dcd/classMesh_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Mesh::PropertyCurvatureList::Save()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Mesh::PropertyMeshKernel::Save()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a4a43a02937b4bee415437e54cba3ad5a),
[Part::PropertyGeometryList::Save()](../../db/dca/classPart_1_1PropertyGeometryList.html#aaab5a1c8943cf5a2ec331fc97dc14938),
[Part::PropertyPartShape::Save()](../../d7/d28/classPart_1_1PropertyPartShape.html#ab90c789bcc0e243359d66b110d7e5517),
[Part::PropertyFilletEdges::Save()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a0e7532f6fa496fb602617495364aed71),
[Points::PointKernel::Save()](../../dc/de1/classPoints_1_1PointKernel.html#a2b6a9c3ce6a26f1b0756db4fe67daa91),
[Points::PropertyGreyValueList::Save()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Points::PropertyNormalList::Save()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Points::PropertyCurvatureList::Save()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Spreadsheet::Cell::save()](../../d5/d22/classSpreadsheet_1_1Cell.html#a6a34f1ee9208af26c12c858780b24874),
[Spreadsheet::PropertyColumnWidths::Save()](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a976f43505863b7470c1eb93726de2d5e),
[Spreadsheet::PropertyRowHeights::Save()](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a7dbc1225885f9daac0294390384589d6),
[TechDraw::PropertyCenterLineList::Save()](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2ca2a9291bf7a7d3a3e4445b27d1e0b0),
[TechDraw::PropertyCosmeticEdgeList::Save()](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a278a66fea5146613150022462cd5866b),
[TechDraw::PropertyCosmeticVertexList::Save()](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a76a4d9006162906f7df1bc9544c03f42),
[TechDraw::PropertyGeomFormatList::Save()](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ab0cfb70b4099f758b0969d3b76176ef5),
[App::Document::Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
[App::PropertyExpressionEngine::Save()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e),
[App::PropertyVector::Save()](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10),
[App::PropertyVectorList::Save()](../../d5/d13/classApp_1_1PropertyVectorList.html#a5f00ee26daf66ffaa7bc7a6974c71467),
[App::PropertyPlacement::Save()](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1),
[App::PropertyPlacementList::Save()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7e1537af27ac4c78360e5f75699b3a8e),
[App::PropertyRotation::Save()](../../df/d76/classApp_1_1PropertyRotation.html#ad9e882ab49bd192e84f62de9a64c62ce),
[App::PropertyLink::Save()](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8),
[App::PropertyLinkList::Save()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a5615ef760136231d57a938213dd9bd36),
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkSubList::Save()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[App::PropertyIntegerList::Save()](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7205d3bff255da22b44e7737b4f90529),
[App::PropertyFloatList::Save()](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyStringList::Save()](../../d8/d55/classApp_1_1PropertyStringList.html#ae923a954a46e42768bec37194a9c69e2),
[App::PropertyBoolList::Save()](../../d1/dcf/classApp_1_1PropertyBoolList.html#add6fd55ff90b5b181391621f6fadae36),
[App::PropertyColorList::Save()](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1),
[App::PropertyMaterialList::Save()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a83f1b747fe9b8b41254e244294809f4a),
[App::PropertyPersistentObject::Save()](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7),
[Sketcher::PropertyConstraintList::Save()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a0bb1d243847dd000f61a4b326df0b184),
[Spreadsheet::PropertySheet::Save()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac590ae825fd968155d7efb7801ddeb74),
[App::DynamicProperty::save()](../../d5/d76/classApp_1_1DynamicProperty.html#a6e38d28a7d5937858b56fdfa3a717086),
[Part::GeometryPersistenceExtension::saveAttributes()](../../de/db6/classPart_1_1GeometryPersistenceExtension.html#ae510926cf9df7b1046d5d9bb0e03b189),
[Part::GeometryDefaultExtension< T
>::saveAttributes()](../../d6/d66/classPart_1_1GeometryDefaultExtension.html#a8120c33b94771ab9dbdd7ee410e1517b),
[Sketcher::ExternalGeometryExtension::saveAttributes()](../../d5/dea/classSketcher_1_1ExternalGeometryExtension.html#a8dfd1b3a66123c38c752f93afa688204),
[Sketcher::SketchGeometryExtension::saveAttributes()](../../d7/db4/classSketcher_1_1SketchGeometryExtension.html#acf0c635d68cb5daf8c3e4c6785594b48),
[Part::Geom2dConic::SaveAxis()](../../d8/d0d/classPart_1_1Geom2dConic.html#a7be1f34bda169a2101d4339f2b2480dd),
[Part::Geom2dArcOfConic::SaveAxis()](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#a266ca3edcbc945deb212a2a66b5a2917),
[App::PropertyFileIncluded::SaveDocFile()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82),
[App::PropertyPythonObject::SaveDocFile()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a8de29b7c3f897d0fbfb67f705ce18b3a),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b),
[Gui::Thumbnail::SaveDocFile()](../../d3/d4d/classGui_1_1Thumbnail.html#a2c08e4f59778bc033417224a3b83028c),
[Fem::FemMesh::SaveDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a879fc2d7f331b9cb54e05424ecf62d87),
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[Inspection::PropertyDistanceList::SaveDocFile()](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ac9622ce80183b9e88f97945047eddd5f),
[Mesh::MeshObject::SaveDocFile()](../../d8/dcc/classMesh_1_1MeshObject.html#a78494e86aa3f8ea36c41c7e47f8a7f4d),
[Mesh::PropertyNormalList::SaveDocFile()](../../df/dcd/classMesh_1_1PropertyNormalList.html#a89d6adfc66489e9ade2a3b4d7e1fb24d),
[Mesh::PropertyCurvatureList::SaveDocFile()](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a600f4dbb1c74ae80d9404b5d0c1732ff),
[Mesh::PropertyMeshKernel::SaveDocFile()](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aa194e6f59eb0c358a42e219ba575f0bd),
[Part::PropertyPartShape::SaveDocFile()](../../d7/d28/classPart_1_1PropertyPartShape.html#a0a5d9ad2a3ed87aa769ab8e36f51d2f2),
[Part::PropertyFilletEdges::SaveDocFile()](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a41c525ac72a07069e44f42c6592e1648),
[Path::Toolpath::SaveDocFile()](../../d6/d0c/classPath_1_1Toolpath.html#a453ab7efa508ad9e45653d8a9f681930),
[Points::PointKernel::SaveDocFile()](../../dc/de1/classPoints_1_1PointKernel.html#ac39f327070b864fa326baa75ee453d58),
[Points::PropertyGreyValueList::SaveDocFile()](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a6b36b085a220e2645377dc6a60ebd237),
[Points::PropertyNormalList::SaveDocFile()](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a89d6adfc66489e9ade2a3b4d7e1fb24d),
[Points::PropertyCurvatureList::SaveDocFile()](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a600f4dbb1c74ae80d9404b5d0c1732ff),
[App::PropertyVectorList::SaveDocFile()](../../d5/d13/classApp_1_1PropertyVectorList.html#a36ef88c4cd85ee0fc26f8f49a8342e12),
[App::PropertyPlacementList::SaveDocFile()](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7a5c65d0ae1925916f9bc4af21bf7172),
[App::PropertyFloatList::SaveDocFile()](../../dc/d40/classApp_1_1PropertyFloatList.html#a824104f367e47aa1dba79edfe6372d57),
[App::PropertyColorList::SaveDocFile()](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843),
[App::PropertyMaterialList::SaveDocFile()](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a5b8b284a9a23e827623d949fcf5c720e),
[App::ExtensionContainer::saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0),
[MeshCore::MeshOutput::SaveXML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8a89241b7984ceab819293e9b7385c20),
and
[App::Document::writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ writeFiles()

| virtual void Base::Writer::writeFiles  | ( | | ) |   
---|---|---|---|---  
pure virtual  
  
process the requested file storing

Implemented in
[Base::ZipWriter](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a),
[Base::StringWriter](../../dd/ddf/classBase_1_1StringWriter.html#ab4177ca37ded0ca8aec93245e596de6d),
[Base::FileWriter](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
[Gui::RecoveryWriter](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c),
and
[Cloud::CloudWriter](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38).

## Member Data Documentation

## ◆ Errors

| std::vector<std::string> Base::Writer::Errors  
---  
protected  
  
Referenced by
[addError()](../../dd/d4d/classBase_1_1Writer.html#a060e45ed91863b5535fa9c9721dde11f),
[clearErrors()](../../dd/d4d/classBase_1_1Writer.html#af772e74bbf7a1dd181af9fb5dfc94ccc),
[getErrors()](../../dd/d4d/classBase_1_1Writer.html#a0a8724e4f558be340dce98381cfc6097),
and
[hasErrors()](../../dd/d4d/classBase_1_1Writer.html#a63b47ea7f6739149a2df8c4bf6344f3a).

## ◆ FileList

|
std::vector<[FileEntry](../../d5/de8/structBase_1_1Writer_1_1FileEntry.html)>
Base::Writer::FileList  
---  
protected  
  
Referenced by
[addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a),
[Base::FileWriter::writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
and
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c).

## ◆ FileNames

| std::vector<std::string> Base::Writer::FileNames  
---  
protected  
  
Referenced by
[addFile()](../../dd/d4d/classBase_1_1Writer.html#a253afcb774015eed79da264548ef4b55),
[getFilenames()](../../dd/d4d/classBase_1_1Writer.html#a6cc1724ce9808ed9d010057a45c0fd6b),
and
[getUniqueFileName()](../../dd/d4d/classBase_1_1Writer.html#a5f42876fd6d991fd34f2de3ca657f9cc).

## ◆ fileVersion

| [int](../../d1/da0/classint.html) Base::Writer::fileVersion  
---  
protected  
  
Referenced by
[getFileVersion()](../../dd/d4d/classBase_1_1Writer.html#aaf8877bfc94b43f802bbe6b41fadf7ed),
and
[setFileVersion()](../../dd/d4d/classBase_1_1Writer.html#a2fed004ddd6bc5ba1793d9344db63291).

## ◆ forceXML

| [bool](../../d9/db9/classbool.html) Base::Writer::forceXML  
---  
protected  
  
Referenced by
[isForceXML()](../../dd/d4d/classBase_1_1Writer.html#a2312714b18983912a3b4b01121bab5d6),
and
[setForceXML()](../../dd/d4d/classBase_1_1Writer.html#af7c44d252aa9e28e3fcdce658bcb6e58).

## ◆ indBuf

| char Base::Writer::indBuf[1024]  
---  
protected  
  
Referenced by
[decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
and
[Writer()](../../dd/d4d/classBase_1_1Writer.html#aedc04cd5fb7b4b99d3ad906fef2116ce).

## ◆ indent

| short Base::Writer::indent  
---  
protected  
  
Referenced by
[decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
and
[incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5).

## ◆ Modes

| std::set<std::string> Base::Writer::Modes  
---  
protected  
  
Referenced by
[clearMode()](../../dd/d4d/classBase_1_1Writer.html#a4c81edd99ae05bebdeec57cc65f371e1),
[clearModes()](../../dd/d4d/classBase_1_1Writer.html#aaa6ac018d7d3fc0f8215e785b9d2918d),
[getMode()](../../dd/d4d/classBase_1_1Writer.html#a67a2c785c2554167b104bad578ae5c83),
[getModes()](../../dd/d4d/classBase_1_1Writer.html#a86e86c861b4596a5470e64b06749154f),
[setMode()](../../dd/d4d/classBase_1_1Writer.html#a3a26c2bb6285dcd29c97037cdda5042e),
and
[setModes()](../../dd/d4d/classBase_1_1Writer.html#ada4367ab704c07fc4347bb6055c88f1c).

## ◆ ObjectName

std::string Base::Writer::ObjectName  
---  
  
name for underlying file saves

Referenced by
[Path::Toolpath::Save()](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
and
[Points::PointKernel::Save()](../../dc/de1/classPoints_1_1PointKernel.html#a2b6a9c3ce6a26f1b0756db4fe67daa91).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Writer.h
  * FreeCAD/src/Base/Writer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

