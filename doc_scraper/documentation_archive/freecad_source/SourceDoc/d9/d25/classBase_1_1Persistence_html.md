---
url: https://freecad.github.io/SourceDoc/d9/d25/classBase_1_1Persistence.html
scraped_at: 2025-09-08T15:16:51.086059
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Persistence](../../d9/d25/classBase_1_1Persistence.html)

[List of all members](../../d7/d8c/classBase_1_1Persistence-members.html) | Public Member Functions | Static Public Member Functions

Base::Persistence Class Referenceabstract

[Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class
and root of the type system.") class and root of the type system.
[More...](../../d9/d25/classBase_1_1Persistence.html#details)

`#include <Persistence.h>`

##  Public Member Functions  
  
---  
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
  
  
##  Static Public Member Functions  
  
---  
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
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

[Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence class
and root of the type system.") class and root of the type system.

## Member Function Documentation

## ◆ create()

| void * Base::Persistence::create  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[draftguitools.gui_labels.Label::action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf).

## ◆ dumpToStream()

void Persistence::dumpToStream  | ( | std::ostream & | _stream_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _compression_  
| ) | |   
  
References
[Base::ZipWriter::putNextEntry()](../../d9/df3/classBase_1_1ZipWriter.html#abb607a9c82879c6ead67f9dee234bd24),
[Save()](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436),
[Base::ZipWriter::setLevel()](../../d9/df3/classBase_1_1ZipWriter.html#a8e1bad6d8787aa75f5d5144ef166b16f),
[Base::Writer::setMode()](../../dd/d4d/classBase_1_1Writer.html#a3a26c2bb6285dcd29c97037cdda5042e),
[Base::ZipWriter::Stream()](../../d9/df3/classBase_1_1ZipWriter.html#a37330d3d5bff097e58268aa7853abaa4),
and
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a).

## ◆ encodeAttribute()

| std::string Persistence::encodeAttribute  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
static  
  
Encodes an attribute upon saving.

Referenced by
[Path::Tool::Save()](../../dd/dfe/classPath_1_1Tool.html#af460887ae0bff6e585c176ec5fb7d090),
[Sketcher::Constraint::Save()](../../d6/def/classSketcher_1_1Constraint.html#a88eebfd4c47c91fe0325cfacbd93b5cc),
[App::PropertyFileIncluded::Save()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::PropertyPath::Save()](../../dc/d24/classApp_1_1PropertyPath.html#a45c4b988fe3e59cadd90a86d13864c30),
[App::PropertyEnumeration::Save()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[App::PropertyMap::Save()](../../db/d3f/classApp_1_1PropertyMap.html#a97872819db9f4c70a132c8995df2369a),
[App::PropertyString::Save()](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164),
[App::PropertyExpressionEngine::Save()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e),
[App::PropertyLinkSub::Save()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList::Save()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink::Save()](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[App::PropertyStringList::Save()](../../d8/d55/classApp_1_1PropertyStringList.html#ae923a954a46e42768bec37194a9c69e2),
[App::DynamicProperty::save()](../../d5/d76/classApp_1_1DynamicProperty.html#a6e38d28a7d5937858b56fdfa3a717086),
[Spreadsheet::Cell::save()](../../d5/d22/classSpreadsheet_1_1Cell.html#a0561387a5a9ded9180edba20d5497dc2),
[Gui::Document::SaveDocFile()](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b),
and
[App::Document::writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ getClassTypeId()

| [Base::Type](../../dc/dee/classBase_1_1Type.html) Base::Persistence::getClassTypeId  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[MeshPartGui::Tessellation::accept()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#a222ec7598711d0c506f4897d9a996bd1),
[PartDesignGui::TaskDlgFeatureParameters::accept()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#abfc2d8ecb714c2b558cc8feb07fa55c3),
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06),
[PartDesignGui::TaskDlgSketchBasedParameters::accept()](../../da/def/classPartDesignGui_1_1TaskDlgSketchBasedParameters.html#a781c55f79eb60cc2c7472679f26dcce7),
[PartGui::DlgPrimitives::accept()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a1db668afa4bde5626f25c5e34f596b82),
[Gui::Dialog::TransformStrategy::acceptDataTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a7eef0b122a11900cca84fcf149180e90),
[App::ObjectIdentifier::access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[SketcherCopy::activate()](../../da/dc9/classSketcherCopy.html#a859bdd8b67b8dc9856f4353ac1fe37aa),
[StdCmdExport::activated()](../../dd/d65/classStdCmdExport.html#a7ee127d8eac7ec03ab328a47bc3fc36f),
[StdCmdSelectAll::activated()](../../d7/d6b/classStdCmdSelectAll.html#a202abf9e8903ce640f488dee93886a8e),
[StdCmdPlacement::activated()](../../d5/d61/classStdCmdPlacement.html#aa4b496fefdba5569fdd808ae245a45b0),
[StdCmdTransformManip::activated()](../../d5/d00/classStdCmdTransformManip.html#abe5d881a1abc655601756111df2fbc54),
[StdCmdAlignment::activated()](../../df/d17/classStdCmdAlignment.html#a44409be4abd266d5d5e34dacb5484101),
[StdCmdMeasurementSimple::activated()](../../d5/d90/classStdCmdMeasurementSimple.html#ac53945e4ee05a762e0719af8b9a28982),
[StdCmdToggleSelectability::activated()](../../d6/d27/classStdCmdToggleSelectability.html#a0ce2e8138a2c546adb161b8804521a28),
[StdCmdSelectVisibleObjects::activated()](../../dc/dac/classStdCmdSelectVisibleObjects.html#a604e385a346a11b7eedebdaf65809abc),
[StdCmdToggleObjects::activated()](../../d5/d4f/classStdCmdToggleObjects.html#a74579d96b6fd41d8ca7fd9bab34f9469),
[StdCmdShowObjects::activated()](../../da/ded/classStdCmdShowObjects.html#a814244e304bf5f31941edaadcfa5f1ed),
[StdCmdHideObjects::activated()](../../d5/d83/classStdCmdHideObjects.html#a2019d661abff8f879c16eb6e1802609f),
[StdCmdTreeSelectAllInstances::activated()](../../de/d0d/classStdCmdTreeSelectAllInstances.html#aeb1fea0671af665274acfd603756c662),
[CmdSketcherConstrainHorizontal::activated()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#adc766562bb486afb5941fc9bade87c59),
[CmdSketcherConstrainVertical::activated()](../../d7/d37/classCmdSketcherConstrainVertical.html#a0f174c055305b510bc2b3ce16eb6e80b),
[CmdSketcherConstrainLock::activated()](../../d9/dc2/classCmdSketcherConstrainLock.html#a337b578fd38e4359b3177138a91a9162),
[CmdSketcherConstrainBlock::activated()](../../d9/d19/classCmdSketcherConstrainBlock.html#a9aae799a29f3aac8783c1f99d1ebb21e),
[CmdSketcherConstrainCoincident::activated()](../../d0/d76/classCmdSketcherConstrainCoincident.html#a52a709fffac7be283b7b50f8687e8602),
[CmdSketcherConstrainDistance::activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainPointOnObject::activated()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#aa6f7ed1adb19f60b65703fafe91fdda9),
[CmdSketcherConstrainDistanceX::activated()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#a175608d3c6099fc7504de3b5641a01c0),
[CmdSketcherConstrainDistanceY::activated()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a59b776e3be604ff1686d112c0f82334b),
[CmdSketcherConstrainParallel::activated()](../../d3/df0/classCmdSketcherConstrainParallel.html#a4c2b4c186452210ed3e69fb1c5f1afe6),
[CmdSketcherConstrainPerpendicular::activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainTangent::activated()](../../d8/d80/classCmdSketcherConstrainTangent.html#a49b68ec579dfa3ac0410539e34096f90),
[CmdSketcherConstrainRadius::activated()](../../d2/d16/classCmdSketcherConstrainRadius.html#a210220527e41b3ad828269b80a359354),
[CmdSketcherConstrainDiameter::activated()](../../da/dbe/classCmdSketcherConstrainDiameter.html#af5d04e1e2fa404f140625af1b917f186),
[CmdSketcherConstrainRadiam::activated()](../../d6/d18/classCmdSketcherConstrainRadiam.html#aee6c0c85caaecf9e7bcd99dff1efd6bc),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[CmdSketcherConstrainEqual::activated()](../../de/dbe/classCmdSketcherConstrainEqual.html#ac247e0d1e55a27e0e40c204965f758be),
[CmdSketcherConstrainSymmetric::activated()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#afc33b5d3e672956b47801982de4611ef),
[SketcherGui::ActivateHandler()](../../d6/d44/namespaceSketcherGui.html#accbdefafb7d39b27d9bb9f19ad4b9fa5),
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[Sketcher::SketchObject::addGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#aa396c8e47c8be25854a016dd6330b295),
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[Mesh::Exporter::addObject()](../../d2/d5a/classMesh_1_1Exporter.html#ae49139d78513fcba38fd6ed832f9d8f4),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[Gui::SelectionSingleton::addSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab2e9be9afea962a0ed8e7f73b5214b02),
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[TechDraw::DrawPage::addView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3e23be3a1fe6b9e35a45c680e33dd8a),
[MeshGui::DlgEvaluateMeshImp::addViewProvider()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a40061f032d5f55a73a2c0eb3a699e886),
[Gui::ManualAlignment::alignObject()](../../d7/d97/classGui_1_1ManualAlignment.html#abfc74600e952621993594238eae06219),
[PartGui::ShapeSelection::allow()](../../d2/d24/classPartGui_1_1ShapeSelection.html#aedd4b5a2bf0d8035205222f679714cae),
[SketcherGui::ExtendSelection::allow()](../../d8/db8/classSketcherGui_1_1ExtendSelection.html#a071a91a94c7f8b448ea508d6b87d76ef),
[SketcherGui::FilletSelection::allow()](../../dd/d6f/classSketcherGui_1_1FilletSelection.html#a2d300c4873259393e235ef5a3845825b),
[SketcherGui::SplittingSelection::allow()](../../d6/d33/classSketcherGui_1_1SplittingSelection.html#a0adaeae8fbe5fbacaa163b208eddc691),
[SketcherGui::TrimmingSelection::allow()](../../de/d39/classSketcherGui_1_1TrimmingSelection.html#a981ac86ae1dbd466c3f25a6ffb7774f8),
[SurfaceGui::FillingPanel::ShapeSelection::allow()](../../df/d8f/classSurfaceGui_1_1FillingPanel_1_1ShapeSelection.html#a3cb549a7831215516813455581b60860),
[SurfaceGui::FillingEdgePanel::ShapeSelection::allow()](../../d7/d97/classSurfaceGui_1_1FillingEdgePanel_1_1ShapeSelection.html#a7d65698bcdefe88bc739c97a70a2e2b0),
[SurfaceGui::FillingVertexPanel::VertexSelection::allow()](../../d0/de5/classSurfaceGui_1_1FillingVertexPanel_1_1VertexSelection.html#a5d7e3b9dae02ef51b26955df36344b74),
[SurfaceGui::SectionsPanel::ShapeSelection::allow()](../../d0/d13/classSurfaceGui_1_1SectionsPanel_1_1ShapeSelection.html#aff2fc432cece76367f9e7018d511f9f9),
[PartDesignGui::ReferenceSelection::allow()](../../dd/d1c/classPartDesignGui_1_1ReferenceSelection.html#aba5a74db909e196f326ebb626e1ba150),
[SketcherGui::ExternalSelection::allow()](../../d3/dff/classSketcherGui_1_1ExternalSelection.html#a8cb2852af5a0bfc42d8844d3f5d1edde),
[SurfaceGui::GeomFillSurface::EdgeSelection::allow()](../../d7/d85/classSurfaceGui_1_1GeomFillSurface_1_1EdgeSelection.html#a9db046f5cffbdc64fc7cf1743c72b592),
[PartGui::ViewProviderPartExt::allowOverride()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#aef11ccd8d18daf6e55d2f5cb7af8431f),
[Sketcher::SketchAnalysis::analyseMissingPointOnPointCoincident()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a353f09f64b5882c26cc62b5560299383),
[MeshPartGui::CrossSections::apply()](../../d1/d27/classMeshPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[PartGui::CrossSections::apply()](../../dc/d84/classPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[Gui::QuantitySpinBox::apply()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ac3ec986d0729752d078f3c57a18f7cca),
[CmdSketcherConstrainHorizontal::applyConstraint()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#a36f07e42457531be9ed67008ba95d021),
[CmdSketcherConstrainVertical::applyConstraint()](../../d7/d37/classCmdSketcherConstrainVertical.html#adf3ea9ac8dd73b137225507c8028e880),
[CmdSketcherConstrainDistance::applyConstraint()](../../d4/de5/classCmdSketcherConstrainDistance.html#a9c0f733b397d4f7e05af5f7c70f9debb),
[CmdSketcherConstrainPointOnObject::applyConstraint()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#a70d28fda1de1503aa99cf66b055420d1),
[CmdSketcherConstrainDistanceX::applyConstraint()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#abf16c738ea7247db91721d5d14d279fc),
[CmdSketcherConstrainDistanceY::applyConstraint()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a2df22f90384fbde7d951992c9564d3ad),
[CmdSketcherConstrainParallel::applyConstraint()](../../d3/df0/classCmdSketcherConstrainParallel.html#a8be8ee71d2e5dc2f276abb4d9eba2be9),
[CmdSketcherConstrainPerpendicular::applyConstraint()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#aa62bab542b8f016bd752fdef90110778),
[CmdSketcherConstrainTangent::applyConstraint()](../../d8/d80/classCmdSketcherConstrainTangent.html#a90a8595e30112cb64ddb61088c3af96b),
[CmdSketcherConstrainRadius::applyConstraint()](../../d2/d16/classCmdSketcherConstrainRadius.html#a0529327862aefd7a8d9d0bed9a03571c),
[CmdSketcherConstrainDiameter::applyConstraint()](../../da/dbe/classCmdSketcherConstrainDiameter.html#a2cba7a76a06cffab82d09cdfcddf0065),
[CmdSketcherConstrainRadiam::applyConstraint()](../../d6/d18/classCmdSketcherConstrainRadiam.html#a08e2367864e5c690e2c6607f10af5e7d),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[CmdSketcherConstrainEqual::applyConstraint()](../../de/dbe/classCmdSketcherConstrainEqual.html#a7efdda717363d452685832c9670be199),
[CmdSketcherConstrainSymmetric::applyConstraint()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#af292ec0892fe051d1d5f06fb9440664e),
[TechDrawGui::ViewProviderDimension::attach()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a074916255bd70c0cd57d36b717586f4d),
[PartDesignGui::ViewProviderDatum::attach()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a68c38571568f0796648a34849f99d36a),
[Gui::ViewProviderLink::attach()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab31e41e9a24ec097be019cdff4fb969b),
[TechDrawGui::MDIViewPage::attachView()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#abe1a2c160e4954c76faa254383387772),
[PartDesignGui::TaskFeaturePick::buildFeatures()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a10945e14aca2a56d0f5ac9e4b0064379),
[PartDesign::ShapeBinder::buildShapeFromReferences()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a06fdaef81be7aa6eb2e83b474a6e5599),
[Gui::PropertyEditor::PropertyEditor::buildUp()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#a00d6964123d5c1c51b41538befbe5ca6),
[TechDrawGui::TaskRichAnno::calcTextStartPos()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae1abe86bd3bc257ecd36cc0212763a37),
[Part::Extrusion::calculateShapeNormal()](../../db/d6c/classPart_1_1Extrusion.html#a9068fcaf96e864a90a04b860140de9c9),
[Gui::ViewProviderLink::callDraggerProxy()](../../d6/d59/classGui_1_1ViewProviderLink.html#aed7a020d79a588a04fdf2774313fca8a),
[Gui::ViewProviderDocumentObject::canDelete()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af693d465f282457e260eed5092506cf1),
[FemGui::ViewProviderFemAnalysis::canDragObject()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a2d0a02dafcabd5a3d2217137fe2fe63c),
[PartGui::ViewProviderCompound::canDragObject()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a8a192ed62ba8fbde86da9d6c95839e14),
[PathGui::ViewProviderArea::canDragObject()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a5b23b48a685f856df048e89dfbb96595),
[PathGui::ViewProviderAreaView::canDragObject()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a7b07997b0a797986bdf725f3541027dd),
[PathGui::ViewProviderPathShape::canDragObject()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a4219b43bf6f1ab5eb62561faa97daa34),
[PartGui::ViewProviderCompound::canDropObject()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#aeed1231298a5c85b3bcde059a5c1e81e),
[PartDesignGui::ViewProviderBody::canDropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#aecc79ac8b9648a6f38d03aa375d74989),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[PartDesignGui::TaskTransformedParameters::checkVisibility()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#aace0a2937bba198ac1276c2d25185683),
[PartDesignGui::ViewProviderHelix::claimChildren()](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a27d75e659da5ae824301907d1f95fe4d),
[PartDesignGui::ViewProviderLoft::claimChildren()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#ac368f091664f727043f69262f84d3d3a),
[PartDesignGui::ViewProviderPipe::claimChildren()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a4c581523b2a518090737db2569d91dfa),
[PartDesignGui::ViewProviderSketchBased::claimChildren()](../../d3/d7d/classPartDesignGui_1_1ViewProviderSketchBased.html#a4552ed8301193054b5f18e6d1b445b89),
[TechDrawGui::ViewProviderLeader::claimChildren()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#ab90cf47c766f83da23d7f960ded3ccdd),
[TechDrawGui::ViewProviderViewPart::claimChildren()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aba1c9f4a2a6681b4ea6666ba487847c1),
[TechDrawGui::ViewProviderWeld::claimChildren()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a4e8d25b0066202499ac3da63f664db36),
[TechDrawGui::ViewProviderPage::claimChildren()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abaf1943763d885917f20c4a78a8e2ef5),
[MeshGui::ViewProviderMesh::clipMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2163df57149a01e40800e85a88d3ce20),
[PointsGui::ViewProviderPoints::clipPointsCallback()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a4245d12144abe01706409cd10565cd60),
[PartDesignGui::collectMovableDependencies()](../../dc/d12/namespacePartDesignGui.html#a134e411f38de8ca01fe259064cdcc27b),
[TechDrawGui::MDIViewPage::compareSelections()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a673364710a7482dbff101d0e4d081ff8),
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[Gui::PropertyEditor::PropertyEditor::contextMenuEvent()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#acc178ef7986ad83af1780aac8bf70e14),
[SketcherGui::EditModeInformationOverlayCoinConverter::convert()](../../d1/d32/classSketcherGui_1_1EditModeInformationOverlayCoinConverter.html#a8673e5dbebfb33a1f0ba7edee9b0bd9b),
[SketcherGui::EditModeGeometryCoinConverter::convert()](../../d7/dcb/classSketcherGui_1_1EditModeGeometryCoinConverter.html#acf8c1e7e07343e0529ad8484b8b7fa6a),
[Sketcher::SketchObject::convertToNURBS()](../../d9/dad/classSketcher_1_1SketchObject.html#a23e6660388fbe498a07b07a8c4f065fe),
[TechDraw::DrawViewCollection::countChildren()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a5474d7126e47e209e9b7c929422d4287),
[TechDraw::DrawView::countParentPages()](../../d6/d1c/classTechDraw_1_1DrawView.html#aaafae8e4da4d73fafd4212576188b326),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[SketcherGui::DrawSketchHandler::createAutoConstraints()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#aaeb21f657e7a40232d0b9e275295765c),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[Fem::createObjectByType()](../../dd/d72/namespaceFem.html#af3663ac69e66763d50fbbd579cb9024a),
[MeshGui::ViewProviderMeshCurvature::curvatureInfo()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#aa2902a6b29f9d107136899cdbf8eca28),
[MeshGui::ViewProviderMeshCurvature::curvatureInfoCallback()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd81924b9ccb33db4d9fb1fe49f1f934),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[PointsGui::ViewProviderScattered::cut()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#a6e93ecaa9bbca01c9cd9c294ba22f38c),
[SpreadsheetGui::SheetModel::data()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aff7232e483f3a56defe5f6f574ac940b),
[Sketcher::SketchObject::decreaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#ace68bb529eeba8cd3e39e3418213d044),
[Sketcher::SketchObject::deleteUnusedInternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a1a8c355b131873c4cb9d783fa5510fd9),
[Sketcher::SketchObject::delGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a40dfaae474c808c67807476529431053),
[Sketcher::SketchAnalysis::detectDegeneratedGeometries()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#abff3a14cad90b3ac1a76b96d30681f12),
[Sketcher::SketchAnalysis::detectMissingEqualityConstraints()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ae30b99d197ec3ff96bd47bf2e0d91e26),
[Sketcher::SketchAnalysis::detectMissingPointOnPointConstraints()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#aa3ccb4b59ed67acd26b695ac6c6e99b1),
[Sketcher::SketchAnalysis::detectMissingVerticalHorizontalConstraints()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ad6435b4ec776c835bdfeee9b91770583),
[PartDesignGui::DlgActiveBody::DlgActiveBody()](../../dc/dd5/classPartDesignGui_1_1DlgActiveBody.html#a286928f45731d5575f688ae3b871c67f),
[Gui::Dialog::DlgAddProperty::DlgAddProperty()](../../d3/d89/classGui_1_1Dialog_1_1DlgAddProperty.html#a54a1e5a0ea475b11a47a9a7ba164f89f),
[PartGui::DlgExtrusion::DlgExtrusion()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a7d11626ecae8d02d4421aa4fdd640dc8),
[PartGui::DlgPrimitives::DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[PartGui::DlgRevolution::DlgRevolution()](../../d1/d83/classPartGui_1_1DlgRevolution.html#ad75370b34cc9b2f2ddb1439faa282f0d),
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[TechDrawGui::QGIViewDimension::draw()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5a804977a329425219739213bc82ec70),
[TechDrawGui::QGIViewBalloon::drawBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a6d26eb06a692339e02c1b57545903f29),
[SketcherGui::EditModeConstraintCoinManager::drawConstraintIcons()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a20c4280c68dc704bd2652d6097b0383a),
[TechDrawGui::QGIViewPart::drawMatting()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a8ee1ae8bd3c4894661e9911784534607),
[TechDrawGui::QGIViewSymbol::drawSvg()](../../d1/da0/classTechDrawGui_1_1QGIViewSymbol.html#a96e6cc364d0c92688d256b192eeec557),
[PartDesignGui::ViewProviderBody::dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[Sketcher::SketchObject::evaluateSupport()](../../d9/dad/classSketcher_1_1SketchObject.html#ae2d3e03c3503536535164dfea9630169),
[Mesh::HarmonizeNormals::execute()](../../d8/d1c/classMesh_1_1HarmonizeNormals.html#a7f4d3c74b5c71fcb87e8467ae09a78f0),
[Mesh::FlipNormals::execute()](../../d3/d05/classMesh_1_1FlipNormals.html#a781c0a4c289cd3fecb312a743d04c2a6),
[Mesh::FixNonManifolds::execute()](../../d5/d33/classMesh_1_1FixNonManifolds.html#a1ee7ec392eeb5cb3a206989d21b3e3bc),
[Mesh::FixDuplicatedFaces::execute()](../../d9/d63/classMesh_1_1FixDuplicatedFaces.html#affadc4a69ba22744612248e94059ea13),
[Mesh::FixDuplicatedPoints::execute()](../../d1/d7b/classMesh_1_1FixDuplicatedPoints.html#abb108a05948e9906cefd394da59fdf77),
[Mesh::FixDegenerations::execute()](../../db/d8f/classMesh_1_1FixDegenerations.html#a3425c9ffba4deeb1c73c7fe910429687),
[Mesh::FixDeformations::execute()](../../d1/dbc/classMesh_1_1FixDeformations.html#a8c0ddd5b2e77c30a2466dc1fd08cdc7a),
[Mesh::FixIndices::execute()](../../d3/deb/classMesh_1_1FixIndices.html#a83eddf2883e3fc904c150d124d8aa01f),
[Mesh::FillHoles::execute()](../../d2/ddd/classMesh_1_1FillHoles.html#a21a0e0e99c2dcd82f9918fe67def820b),
[Mesh::RemoveComponents::execute()](../../da/d7a/classMesh_1_1RemoveComponents.html#a552facf8870d9ef3b36e1dee379fac07),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[PartDesign::FeatureBase::execute()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a7cc09059c368f65475f0fa3f05bc06f5),
[PartDesign::Loft::execute()](../../d0/deb/classPartDesign_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[PartDesign::Transformed::execute()](../../dd/de1/classPartDesign_1_1Transformed.html#aef9667071a3f6bb2ed13226f84629049),
[Path::FeatureArea::execute()](../../da/d1e/classPath_1_1FeatureArea.html#af00ad2b6bd7ffa0f8db73f7b51b94fbc),
[Path::FeatureAreaView::execute()](../../d3/db4/classPath_1_1FeatureAreaView.html#a181be122ea1283aac8cb22d51edc5686),
[Path::FeatureCompound::execute()](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[Path::FeatureShape::execute()](../../da/d9b/classPath_1_1FeatureShape.html#a62d47b3cb3d7ed9081cdfc0966c71c3e),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Robot::TrajectoryCompound::execute()](../../df/de7/classRobot_1_1TrajectoryCompound.html#a230683c181418d56d66a986fe5063a3a),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Surface::Cut::execute()](../../d4/d17/classSurface_1_1Cut.html#adade24c19d386572d09157489463f785),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[Surface::Sewing::execute()](../../d2/d52/classSurface_1_1Sewing.html#a956109125cae787085423aeb93d8e1f3),
[TechDraw::DrawTemplate::execute()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a67d8e151c886e0ef62f246cc3a4e5ff6),
[TechDraw::DrawViewClip::execute()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a31cd0c2306b266d607e29672b3825340),
[TechDraw::DrawViewSpreadsheet::execute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[PartDesign::Body::execute()](../../dd/db8/classPartDesign_1_1Body.html#a4abca6b2645adade81347d0e850a2659),
[PartDesign::Boolean::execute()](../../d2/d81/classPartDesign_1_1Boolean.html#a471715716cd89abfe18b9f50b7728567),
[Surface::Extend::execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[Surface::Sections::execute()](../../d7/d6e/classSurface_1_1Sections.html#a2c9525c3b5343d49da189cd26cd2ad4e),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[Fem::FemVTKTools::exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[Import::ExportOCAF::exportObject()](../../d2/dda/classImport_1_1ExportOCAF.html#a44829a66a0a0a1481f0b17eb8f29331b),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[Sketcher::SketchObject::exposeInternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a7d89f466b41e7479505e70c73d832428),
[Sketcher::SketchObject::extend()](../../d9/dad/classSketcher_1_1SketchObject.html#a863df4c6af57263b15a8170b377ef466),
[PartGui::ViewProviderSplineExtension::extensionUpdateData()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#ac0f6ab010c3a75a975e8ca3ad2ef60e2),
[Part::AttachExtension::extHandleChangedPropertyName()](../../dc/d47/classPart_1_1AttachExtension.html#a660e1d33e4a6e9d23e2178b45395d9fe),
[MeshGui::ViewProviderMesh::faceInfoCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae3d2f360b9f432962521c1bb1b77dd98),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a045cba23726c2d8dfe57ce28c758973c),
[MeshGui::ViewProviderMesh::fillHoleCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ad3cdb2b5549c092780ef6b1bb252cc02),
[TechDraw::DrawView::findAllParentPages()](../../d6/d1c/classTechDraw_1_1DrawView.html#a9b28f37bc7b1197a9de93065bec24190),
[Part::BodyBase::findBodyOf()](../../da/dc8/classPart_1_1BodyBase.html#aa97e09a088d42e23f853450ab5b44989),
[ImportGui::ExportOCAFGui::findColors()](../../d7/dd1/classImportGui_1_1ExportOCAFGui.html#a1c4f907241651d44fa92f9d57984d5b6),
[TechDrawGui::MDIViewPage::findMissingViews()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a008268149662b6262a0a1aa91cb12d5a),
[TechDrawGui::DrawGuiUtil::findPage()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a5e81d631634196d2c5fe0d083fd7cb9b),
[TechDraw::DrawView::findParentPage()](../../d6/d1c/classTechDraw_1_1DrawView.html#a5afa0f83d15ac28c8fd00cd47663c79e),
[PartGui::DlgFilletEdges::findShapes()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a3bd2ba2fd4b83d69ee72ad80a4cae2e4),
[Gui::FreeCADGui_subgraphFromObject()](../../d9/dad/namespaceGui.html#a1562062f6fcff8f9ec05618c80435514),
[PartDesign::DressUp::getAddSubShape()](../../df/de5/classPartDesign_1_1DressUp.html#ad0ea5289ebf6d00059754a3cd95b7981),
[TechDraw::DrawPage::getAllViews()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a5e94239ad9e3ffb6b034ec2eddd4beb2),
[Sketcher::SolverGeometryExtension::getArc()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#a6818ede87814f4640fbf8ef5484a686a),
[Sketcher::SolverGeometryExtension::getArcOfEllipse()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#a4eca56fed970dac3386c92f1c4fc4a45),
[Sketcher::SolverGeometryExtension::getArcOfHyperbola()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#afc77745b2caeba3f37434f27db81219d),
[Sketcher::SolverGeometryExtension::getArcOfParabola()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#a7e3bfa1d816aa94783f2f0e639d36ad7),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[App::Origin::getAxis()](../../d9/d8b/classApp_1_1Origin.html#a22ff56dd7f14783a94fe81dbb5ac648c),
[Sketcher::SketchObject::getAxis()](../../d9/dad/classSketcher_1_1SketchObject.html#aba78a99760f91409c6af09810daaa797),
[Sketcher::SketchObject::getAxisCount()](../../d9/dad/classSketcher_1_1SketchObject.html#afbfd6982e4fee081789564a22ef4b4f5),
[TechDraw::DrawViewPart::getBalloons()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a2af77af02e9b46ff8535f3c0e3d5cda3),
[TechDraw::DrawViewSection::getBaseDPGI()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af83079c6b71a10b1c2986ecb0b30375c),
[TechDraw::DrawViewSection::getBaseDVP()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aae6243e0a6dd3abfd5bd02e1066dcfbb),
[PartDesign::Feature::getBaseObject()](../../d7/d51/classPartDesign_1_1Feature.html#a4b32fcefa87c31a546571d96cfd41413),
[PartDesign::DressUp::getBaseObject()](../../df/de5/classPartDesign_1_1DressUp.html#ae90233bb954119d82b5afdf3593b771c),
[PartDesign::ProfileBased::getBaseObject()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a401f7d69c600f553aa66a01f8414ef5b),
[PartDesign::Transformed::getBaseObject()](../../dd/de1/classPartDesign_1_1Transformed.html#aba5db649de61d67db332e2cd71a86d09),
[PartDesign::Feature::getBaseShape()](../../d7/d51/classPartDesign_1_1Feature.html#ad6682cb08a683af75dc2b9de5bbcc13f),
[PartDesign::Feature::getBaseTopoShape()](../../d7/d51/classPartDesign_1_1Feature.html#a17c6163f5824ed676fab0cd92e9794e3),
[PartDesignGui::getBody()](../../dc/d12/namespacePartDesignGui.html#a7c1be98b8f7c9925793b53015ca52c15),
[PartDesignGui::ViewProvider::getBodyViewProvider()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aa91f903016c0d40372778ba96b43a5f9),
[Gui::AlignmentGroup::getBoundingBox()](../../dc/d5e/classGui_1_1AlignmentGroup.html#a61b723faec476204d9ef279204fce7bf),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[Sketcher::SolverGeometryExtension::getBSpline()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#afd7ed46b3ec4ce91618e7a420957bc6c),
[TechDraw::DrawViewClip::getChildViewNames()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#aec9acaae16e2f82bdcc0994a767559ef),
[Sketcher::SolverGeometryExtension::getCircle()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#a066c2c4c302948fdbfb9eb98b9c7d6ba),
[TechDraw::DrawView::getClipGroup()](../../d6/d1c/classTechDraw_1_1DrawView.html#a5d4c311b15da7ecfce93f6ee47cc5326),
[MeshGui::ViewProviderMesh::getColorProperty()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ab3eae9bc83c8bec9cc875f7f548a9f2b),
[App::LinkBaseExtension::getContainer()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a57b46869e220d668ce2184446b7d6f80),
[TechDraw::DrawViewPart::getDetailRefs()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a55c64661c530b34d53d7bd85e2e6bc54),
[TechDraw::DrawViewPart::getDimensions()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aead97bcf62218c84e4f895b710ed1ae3),
[Fem::Constraint::getDirection()](../../d0/d11/classFem_1_1Constraint.html#a74ee50a75fff721d064b164c334e9f1b),
[PointsGui::ViewProviderPoints::getDisplayModes()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a2d67beeb09773e4dc1ee1d2d00a2772d),
[App::PropertyFileIncluded::getDocTransientPath()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a5f4e5ed4004ee3084755508e6c3b071a),
[Sketcher::SolverGeometryExtension::getEllipse()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#af98e13a2bf61adde09fe840c3f53ab88),
[App::DocumentObjectExtension::getExtendedObject()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af6e17e520cf9b556992786cb5d57e911),
[Gui::ViewProviderExtension::getExtendedViewProvider()](../../d5/db8/classGui_1_1ViewProviderExtension.html#a3bc1434c0b8c077a46c3c8ead596c11e),
[PartDesign::ShapeBinder::getFilteredReferences()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a60be3190092c35ac6740f45a4b808dee),
[Spreadsheet::Cell::getFormattedQuantity()](../../d5/d22/classSpreadsheet_1_1Cell.html#a66a4fb5ffaa93232823dfbe49833ab7b),
[TechDraw::DrawViewPart::getGeomHatches()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a791ac89a7da3090c29febc0ca990c198),
[App::GeoFeatureGroupExtension::getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
[App::OriginGroupExtension::getGroupOfObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b),
[TechDraw::DrawViewPart::getHatches()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aaf6c2599b3dfdb89053d5685f33bf747),
[InspectionGui::ViewProviderInspection::getIcon()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a76d57438c1350bd9a432557f0c23dc5e),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[TechDraw::DrawView::getLeaders()](../../d6/d1c/classTechDraw_1_1DrawView.html#a06b2c3010e85ba1e320e12cad20ae5bf),
[Sketcher::SolverGeometryExtension::getLine()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#a9ce69727c9d155f453b42c063312ee9a),
[Fem::getObjectByType()](../../dd/d72/namespaceFem.html#a1d62957fae198eb1c03b3ce2c2503c3c),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
[MeshGui::MeshSelection::getObjects()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a28460ca199aa44464490e0b41eb44cbd),
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1),
[App::OriginFeature::getOrigin()](../../da/dfe/classApp_1_1OriginFeature.html#ae153618f0361a30dd55b8b0f21294cfa),
[App::OriginGroupExtension::getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[TechDraw::DrawPage::getPageHeight()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac3db535fcb4092f6a10886b734610eab),
[TechDraw::DrawPage::getPageOrientation()](../../d9/d5a/classTechDraw_1_1DrawPage.html#acfcfcccb6fbd3ebc861e8c7ffd06d301),
[TechDraw::DrawPage::getPageWidth()](../../d9/d5a/classTechDraw_1_1DrawPage.html#abe7626bfbc51068143aa7d089fecb586),
[TechDrawGui::QGIDrawingTemplate::getParametricTemplate()](../../d3/d23/classTechDrawGui_1_1QGIDrawingTemplate.html#aa35d8e88fa3a262776ef10b8caa1e603),
[TechDraw::DrawTemplate::getParentPage()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a14c9c348c4695881293c7ba14f8d0bb0),
[TechDraw::DrawProjGroupItem::getPGroup()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#adf1f84e5479b18e7dae605f8afb7825d),
[App::PropertyPlacementLink::getPlacementObject()](../../d8/db5/classApp_1_1PropertyPlacementLink.html#a99f7a47899a0bb96bbaf4321c81aed02),
[App::Origin::getPlane()](../../d9/d8b/classApp_1_1Origin.html#a9079a145e03b6fb0715db0246ace036b),
[Sketcher::SolverGeometryExtension::getPoint()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#aa504b70e1e8bf7aeb397cfc31cc4f9be),
[Sketcher::SketchObject::getPoint()](../../d9/dad/classSketcher_1_1SketchObject.html#a8c0707e1362b0b4214aea676a125332c),
[PartDesign::ProfileBased::getProfileNormal()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#af389a14c1da76e8ce4aa4dd5dc874540),
[PartDesign::ProfileBased::getProfileWires()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#ac961ce965c86590b3d865e3cf87ab019),
[PartDesignGui::getReferencedSelection()](../../dc/d12/namespacePartDesignGui.html#a3f00fb1f14bb1e8917fe623cecd8ab59),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a8437c5be88154b9cb0bd2bae5ef94db3),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[TechDraw::DrawViewPart::getSectionRefs()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a193d33664258d178df8d627db0b2dc39),
[TechDrawGui::TaskAlignViews::getSelectedEdges()](../../d8/d23/classTechDrawGui_1_1TaskAlignViews.html#a748566d07ecc0ca6df66f78ceca681a5),
[Gui::SelectionSingleton::getSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#ad876028e2a678027a0828e2a5d309ec6),
[Path::FeatureAreaView::getShapes()](../../d3/db4/classPath_1_1FeatureAreaView.html#a8bdeb47d6e84b6cfb93ce2eb43e7bbe9),
[TechDraw::ShapeExtractor::getShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#ae76c98b8a90588bf6515ac4738f5e16b),
[TechDraw::ShapeExtractor::getShapes2d()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a7b6b34e0c817f34b537bdb53b36956f1),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[PartGui::getShapesFromSelection()](../../d5/d49/namespacePartGui.html#a220faba7cb905e4e2fe20917a6bd91e2),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[PartDesign::Transformed::getSketchObject()](../../dd/de1/classPartDesign_1_1Transformed.html#a7b52a3658c0f24c04278bc8c1fcc55fd),
[SketcherGui::getSketchViewprovider()](../../d6/d44/namespaceSketcherGui.html#a4ceb5e5d4995709e3a6864825045cf30),
[PartDesign::Body::getSubObject()](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[PartDesign::ProfileBased::getSupportFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a021db5d3d85698ee0d5a4f8d8a4391a5),
[TechDrawGui::QGISVGTemplate::getSVGTemplate()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a31406f43b09ce7700a787ce3a1c42880),
[TechDraw::DrawWeldSymbol::getTiles()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#a70aed4254307b5004b56244677295366),
[PartDesignGui::TaskTransformedParameters::getTopTransformedObject()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#ac3995a277718acf03174db7534fd3461),
[PartDesign::MultiTransform::getTransformations()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a33b71497cd61478ec6fb8d660b759b6b),
[PartDesign::Scaled::getTransformations()](../../db/dce/classPartDesign_1_1Scaled.html#a114f3de4184f1d8b572ed057609c03d6),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::ProfileBased::getUpToFaceFromLinkSub()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#af91fce8a1c9f53727ca70b642dcad1c3),
[PartDesign::ProfileBased::getVerifiedFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a4172d89f228cd87e6517a0518401b11a),
[PartDesign::ProfileBased::getVerifiedObject()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#aa78f3895fcd96617d6bc5d12206b3e62),
[PartDesign::ProfileBased::getVerifiedSketch()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a7a0531e338df1efce486dca72af449f0),
[Gui::LinkInfo::getView()](../../d4/da4/classGui_1_1LinkInfo.html#a860b0cea7256187c0f3325e7359e29e2),
[MeshGui::MeshSelection::getViewProviders()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a13d49d4d64c535509228e1f548671aa3),
[Gui::ViewProviderDocumentObjectGroup::getViewProviders()](../../df/d84/classGui_1_1ViewProviderDocumentObjectGroup.html#a15b9f85e289a705b97e815a838764e6e),
[Surface::GeomFillSurface::getWire()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#acb54e9fd0d6302521906069a06003c6e),
[TechDraw::ShapeExtractor::getXShapes()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4e820635335afa9ce7506faaf4274cbd),
[Gui::GraphicsView3D::GraphicsView3D()](../../df/d0b/classGui_1_1GraphicsView3D.html#ad33d0c8f32b37ee2eff8e67494289edc),
[Fem::FemAnalysis::handleChangedPropertyName()](../../de/d36/classFem_1_1FemAnalysis.html#a77d4363b7c6734ec7754d6c4de10a481),
[Part::BodyBase::handleChangedPropertyName()](../../da/dc8/classPart_1_1BodyBase.html#a2038d6fd9d31b5033c193ca7a95d0b33),
[PartDesign::Boolean::handleChangedPropertyName()](../../d2/d81/classPartDesign_1_1Boolean.html#ad635959d9d69278a1c46fbd6cc0f78f4),
[Surface::Extend::handleChangedPropertyName()](../../d1/d22/classSurface_1_1Extend.html#aa2e1ed26c2018e7234938836df41545c),
[TechDraw::DrawViewBalloon::handleChangedPropertyName()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a8f43bff2ef5b6712e7fd0546b639e6ef),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[Gui::SelectionSingleton::hasSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a89f10df8046ce9e2382cb0c8123ce3e3),
[PartGui::hasShapesInSelection()](../../d5/d49/namespacePartGui.html#ad528565e643c4ef351810cb1cc417d30),
[TechDraw::DrawPage::hasValidTemplate()](../../d9/d5a/classTechDraw_1_1DrawPage.html#addb0ce93dfeaa39ce5808639fc3ff9fb),
[DrawingGui::ViewProviderDrawingView::hide()](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#af1f9e27cb4717b1eab17df64def3a5a3),
[DrawingGui::ViewProviderDrawingClip::hide()](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#ae328b7a7c463a0cfe21fb19adb6a8cab),
[TechDrawGui::ViewProviderViewClip::hide()](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a0dad53d8ccb241aa1ffaa1ca6cd0e85b),
[TechDrawGui::ViewProviderDrawingView::hide()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a76b2851b249a59575433a30cc5776432),
[PartDesignGui::ViewProviderShapeBinder::highlightReferences()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a88fdfde939bae5a7f7d2ed7d3865a9a8),
[PartDesignGui::ViewProviderLoft::highlightSection()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#aef670c0f855e6e36a97aa14355df92bb),
[Sketcher::SketchObject::increaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#a3daba3e80990ea7e01b8b4a9bde2217a),
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
[Gui::ViewProviderLink::initDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a1386127ddc37cfa7078215b347149a71),
[App::GeoFeatureGroupExtension::initExtension()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a74933934579b51ddd24efdd5be7bb3ba),
[App::Application::initTypes()](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
[Gui::Application::initTypes()](../../d9/da8/classGui_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
[Sketcher::SketchObject::insertBSplineKnot()](../../d9/dad/classSketcher_1_1SketchObject.html#a48c6d4c74904307c87c4e8f65a9e89af),
[PartDesign::Body::insertObject()](../../dd/db8/classPartDesign_1_1Body.html#a5cbb7aa1f902c8b111a9c9a428072c09),
[InspectionGui::ViewProviderInspection::inspectCallback()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a4e6895f19ff09d06e34c94fe7df62517),
[InspectionGui::ViewProviderInspection::inspectDistance()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac0352eb6e4af339e08975b253269b0ab),
[StdCmdPlacement::isActive()](../../d5/d61/classStdCmdPlacement.html#af4c0d10f4515a8f9ef6d6c0325a45f3c),
[StdCmdTransformManip::isActive()](../../d5/d00/classStdCmdTransformManip.html#af138c934e241646d55c75d6ae912da44),
[StdCmdAlignment::isActive()](../../df/d17/classStdCmdAlignment.html#ac21ec0c9ec9d9b138cc8101a87172c0a),
[StdCmdTreeSelectAllInstances::isActive()](../../de/d0d/classStdCmdTreeSelectAllInstances.html#acf721a5c43191645257b29af03ab52aa),
[StdCmdMeasureDistance::isActive()](../../db/dfc/classStdCmdMeasureDistance.html#ae34eeedc376782cacdd1d9b6745864ad),
[PartDesign::Body::isAllowed()](../../dd/db8/classPartDesign_1_1Body.html#a85743938d32f9f85137b6ada784c32c5),
[PartDesignGui::isAnyNonPartDesignLinksTo()](../../dc/d12/namespacePartDesignGui.html#a763622795328f1193ce61804dc4c61b6),
[SketcherGui::isBsplineKnotOrEndPoint()](../../d6/d44/namespaceSketcherGui.html#a5f794ae2b51c8a757babfa7258a84bee),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[SketcherGui::isCommandActive()](../../d6/d44/namespaceSketcherGui.html#a9bd77d0da12d76d5e6b05a52b8edd52b),
[PartDesign::Feature::isDatum()](../../d7/d51/classPartDesign_1_1Feature.html#ae76e0e61b446d25dde1053d691c87081),
[PartDesignGui::isFeatureMovable()](../../dc/d12/namespacePartDesignGui.html#a6b3f9e577dd13e884d8aca2e0ce6a6c8),
[TechDraw::DrawView::isInClip()](../../d6/d1c/classTechDraw_1_1DrawView.html#ac7c414b101516f9925ec8c992e71e54c),
[App::GeoFeatureGroupExtension::isLinkValid()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7),
[PartDesign::Body::isMemberOfMultiTransform()](../../dd/db8/classPartDesign_1_1Body.html#a9a9ab9d38f99b313ee96c4720f7bff6b),
[PartDesignGui::isPartDesignAwareObjecta()](../../dc/d12/namespacePartDesignGui.html#afdb55dba9e76e28bc607fd742f333fd2),
[TechDraw::ShapeExtractor::isPointType()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a2b92d44933b7ed3a67d4ea9f63ee4739),
[App::PropertyLinkBase::isSame()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407),
[PartDesign::Body::isSolidFeature()](../../dd/db8/classPartDesign_1_1Body.html#a794071c5f5e588b7c9e0631556bf1cd9),
[Sketcher::SketchObject::isSupportedGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a2f7ea4092440c2afc10ce26ce6cf5948),
[TechDrawGui::QGIProjGroup::itemChange()](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#aa1611210aac32505ffac13b3c321ba65),
[TechDrawGui::QGIView::itemChange()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a5a2dfe4ec1878b54977f351509389239),
[Fem::FemPostPipeline::load()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a6b8a523a3afbb19474bf90fa955f1a41),
[TechDrawGui::TaskLinkDim::loadAvailDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a3e6b427c8a0b62b4199b25d3eb07f58b),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[PartDesignGui::TaskSketchBasedParameters::make2DLabel()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#abe69c78ef76010267804b7bfb977e00d),
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[SketcherGui::makeTangentToArcOfEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#ade2d18eb05327cda22e2eb86409e4642),
[SketcherGui::makeTangentToArcOfHyperbolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a2d88b81b020ee6003474b180fad75a3b),
[SketcherGui::makeTangentToArcOfParabolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a8153db87ad16afe18f0f5e0a01bf5251),
[SketcherGui::makeTangentToEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a0221a346db6666022488335587d92562),
[MeshGui::ViewProviderMesh::markPartCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a6eb548accf81ef25b6aa376ac7fa53a8),
[Sketcher::SketchObject::migrateSketch()](../../d9/dad/classSketcher_1_1SketchObject.html#aaafb8589473a3087af97dde1bbf276fb),
[PartGui::Mirroring::Mirroring()](../../db/d41/classPartGui_1_1Mirroring.html#a37c415d13595eeeaa2f1a1fa54a5f740),
[Sketcher::SketchObject::modifyBSplineKnotMultiplicity()](../../d9/dad/classSketcher_1_1SketchObject.html#ae318b60c226c883e53725f9ebef29991),
[SketcherGui::ViewProviderSketch::mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[Gui::TreeView::mouseDoubleClickEvent()](../../d9/ddf/classGui_1_1TreeView.html#ad2e4760d9a018ee92f83e36adbadcfa7),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::ViewProviderSketch::mouseMove()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa),
[TechDrawGui::DrawGuiUtil::needPage()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a4c52b5348f0784d3c0679c33bf99804d),
[TechDrawGui::DrawGuiUtil::needView()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a6062f181af83a85f81e62e169db5402a),
[Sketcher::SolverGeometryExtension::notifyAttachment()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#acdfa7733cbaee3f792a8db0dd49aef49),
[PartGui::OffsetWidget::OffsetWidget()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ae7bb4b5d03b3c78115b8e3943bb318d1),
[Gui::Dialog::DlgMaterialPropertiesImp::on_ambientColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a49825eab8b369a08e23c6e14f3929301),
[Gui::Dialog::DlgMaterialPropertiesImp::on_diffuseColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a9ccc20c9c5d253b5e9ed7fbe4d34f13e),
[Gui::Dialog::DlgMaterialPropertiesImp::on_emissiveColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aa448adcda1877165e407fafcf0354cf3),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_filterShortcutPressed()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#ad7edd0b6dbbd073d9b6c12951a8cb71e),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemEntered()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a2e956e6abd25667f7e59514a401b0f42),
[MeshGui::DlgEvaluateMeshImp::on_meshNameButton_activated()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ae54004188b150e536ff0d1a2fec6c314),
[Gui::Dialog::DlgMaterialPropertiesImp::on_shininess_valueChanged()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#af0d5014718205e140eb9e8799167d518),
[Gui::Dialog::DlgMaterialPropertiesImp::on_specularColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a458ce64d9a0930c339444dff48ac809f),
[App::Document::onBeforeChangeProperty()](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb),
[Gui::ViewProviderAnnotationLabel::onChanged()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[Fem::FemPostClipFilter::onChanged()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostCutFilter::onChanged()](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesignGui::ViewProvider::onChanged()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[SketcherGui::ViewProviderSketch::onDelete()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a83277547707db7a956f740a550845361),
[TechDrawGui::MDIViewPage::onDeleteObject()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#aa6c1a0b76aea98fadec5b8dcde54844b),
[PartDesign::Body::onDocumentRestored()](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[App::OriginGroupExtension::onExtendedSetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb),
[Gui::ElementColors::Private::onSelectionChanged()](../../d8/dc9/classElementColors_1_1Private.html#afd57ddb2a0592ad0eef0d2bdcb9066ce),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[PartDesignGui::TaskLinearPatternParameters::onSelectionChanged()](../../da/d31/classPartDesignGui_1_1TaskLinearPatternParameters.html#a865b9046f3a77031028528e8330e7bcc),
[PartDesignGui::TaskMirroredParameters::onSelectionChanged()](../../d8/d3c/classPartDesignGui_1_1TaskMirroredParameters.html#a5b8572d198c9289b07e5223b5ab90578),
[PartDesignGui::TaskPolarPatternParameters::onSelectionChanged()](../../d7/d72/classPartDesignGui_1_1TaskPolarPatternParameters.html#a100a716e1bd223ef70db3b1961b6ed49),
[TechDrawGui::MDIViewPage::onSelectionChanged()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a41cff4fd37a6ddb55d5c40e9c044a9f0),
[SketcherGui::DrawSketchHandlerCarbonCopy::onSelectionChanged()](../../d8/dcc/classSketcherGui_1_1DrawSketchHandlerCarbonCopy.html#a0abe4b682958afcce6e53de58d3225fa),
[SketcherGui::DrawSketchHandlerExternal::onSelectionChanged()](../../d5/d95/classSketcherGui_1_1DrawSketchHandlerExternal.html#aab1764f7bd2af3f2cf49a7131a443253),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[PartGui::PropertyEnumAttacherItem::openTask()](../../dd/db5/classPartGui_1_1PropertyEnumAttacherItem.html#a232e6f966edd003419540ac9e7c9f405),
[App::DocumentObjectT::operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b),
[PartDesignGui::TaskTransformedParameters::originalSelected()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#adb918122e8572632cc17114506d98ccd),
[TechDrawGui::MDIViewPage::orphanExists()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#af53edffe3018bd0dfa04f4cdee23c85f),
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[App::PropertyPythonObject::Paste()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a086c7bb8deef61645433e76eeb2fe3b0),
[App::PropertyLink::Paste()](../../d4/d77/classApp_1_1PropertyLink.html#a31b305bd16358bc6459e33bf47e1c2b6),
[App::PropertyLinkList::Paste()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a4395718ac6e9c8f221569c4de1933ba9),
[App::PropertyLinkSub::Paste()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a5514822b7ffa4a3ebaf2c8a569d0df67),
[App::PropertyLinkSubList::Paste()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a3dfbcd135189c2b3e6e7c6136ed572a1),
[App::PropertyXLink::Paste()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27),
[App::PropertyXLinkSubList::Paste()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a4ac663947ed88fa49f3a874273098fe4),
[Sketcher::SketchObject::port_reversedExternalArcs()](../../d9/dad/classSketcher_1_1SketchObject.html#a7a63cf359bdc3559fb9911559f4d1cd7),
[PartDesign::DressUp::positionByBaseFeature()](../../df/de5/classPartDesign_1_1DressUp.html#ad0f7b71428ae5784d44e9a75f810ff3c),
[PartDesign::ProfileBased::positionByPrevious()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#acdddc3b78089a2b2dbd5c567998c9039),
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710),
[SpreadsheetGui::DlgSheetConf::prepare()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#abfbeb695362f8ae8074215c61a254de3),
[SketcherGui::DrawSketchHandlerLineSet::pressButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#aeee22456b9d6c86500b37dca09b6bca0),
[Gui::ManualAlignment::probePickedCallback()](../../d7/d97/classGui_1_1ManualAlignment.html#af255c1f31bf62293781d8a04cbecbceb),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Import::ExportOCAF::reallocateFreeShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a6c187685f014b96ecdceaa814f7eaa81),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[Sketcher::SketchObject::rebuildVertexIndex()](../../d9/dad/classSketcher_1_1SketchObject.html#a1049c1593780a788adbd203066fc562f),
[TechDraw::DrawViewCollection::rebuildViewList()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a2cddd1c4b006821c3ec11a31dedf7338),
[PartDesignGui::TaskShapeBinder::referenceSelected()](../../d0/d2a/classPartDesignGui_1_1TaskShapeBinder.html#a4821e3f83b3b3cccc89fc2da1b7cd441),
[MeshGui::DlgEvaluateMeshImp::refreshList()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a09df67f594d7ad5fa40960e816fc8f4a),
[SketcherGui::DrawSketchHandlerLineSet::registerPressedKey()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a032722eff2ff16ed091e0ff7a7b9d6ce),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerSplitting::releaseButton()](../../d1/d6f/classSketcherGui_1_1DrawSketchHandlerSplitting.html#a0766956ef48057437eca84c83e1b3521),
[SketcherGui::DrawSketchHandlerTrimming::releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[SketcherGui::ReleaseHandler()](../../d6/d44/namespaceSketcherGui.html#aa74aecd09a88397d70ef1f1ed6b72511),
[PartDesignGui::relinkToBody()](../../dc/d12/namespacePartDesignGui.html#a5bd0f34409b95d9ccc03b0b80655b0fd),
[PartDesignGui::relinkToOrigin()](../../dc/d12/namespacePartDesignGui.html#a04b9ca5c57afc44a5ab6f8bc71f9a681),
[App::OriginGroupExtension::relinkToOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49),
[PartDesign::ProfileBased::remapSupportShape()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#ad1985a2126f28aecb119562d9f47ba37),
[Sketcher::SketchAnalysis::removeDegeneratedGeometries()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a54caaa293a607376706ca5c6a9cb33ab),
[PartDesign::Body::removeObject()](../../dd/db8/classPartDesign_1_1Body.html#a207956cf2a361690d971c7e604fc8bf1),
[TechDraw::DrawPage::removeView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47c86c19ddcbaabe9a680e836c437012),
[App::PropertyLink::resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Path::PropertyPath::RestoreDocFile()](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[PartGui::DlgSettings3DViewPart::saveSettings()](../../d2/d45/classPartGui_1_1DlgSettings3DViewPart.html#ae256735cc3da90df3b8c481c60d28f72),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Part::Part2DObject::seekTrimPoints()](../../d9/d57/classPart_1_1Part2DObject.html#a7f5beeba90cfa4cdf7a72f7827bae9f1),
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
[Gui::View3DInventorViewer::selectAll()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a0421813978ac6e4b89ba676ca20acf44),
[MeshGui::ViewProviderMesh::selectGLCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2b53e6d9eccae0cd2400b98862e20979),
[PartGui::FaceColors::Private::selectionCallback()](../../d4/d4b/classFaceColors_1_1Private.html#a5ff66514ce5125d41dd193313edfdb8e),
[Gui::SelectionSingleton::selStackGet()](../../d4/dca/classGui_1_1SelectionSingleton.html#a43d032c9814131c9596e3203893e9a80),
[App::PropertyLinkList::set1Value()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a7a16fe45fc1c04feba8b79c9cd463f4d),
[PartDesign::Body::setBaseProperty()](../../dd/db8/classPartDesign_1_1Body.html#abbb8bb2a283a57b6d6f2230dcacd7be3),
[PointsGui::ViewProviderPoints::setDisplayMode()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a6fba67f9c755f7ae29cdfe1eb581b6b1),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
[Gui::Document::setEdit()](../../de/d4e/classGui_1_1Document.html#a2064c6eb4172240d40a7f409febc81a9),
[Gui::ViewProviderDragger::setEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[Gui::Document::setHide()](../../de/d4e/classGui_1_1Document.html#a210ce66ce252fecbfb7107f60c37429c),
[Gui::Dialog::DlgInspector::setNodeNames()](../../de/d72/classGui_1_1Dialog_1_1DlgInspector.html#a76de55354260496b98e1f50d29598a19),
[Gui::View3DInventorViewer::setOverrideMode()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a9b1899603aa3f23dd39acbc8bead4b4f),
[TechDrawGui::QGSPage::setPageTemplate()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a8a78c463d8d428192f1e952b7a24413a),
[App::LinkBaseExtension::setProperty()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a77ef5fd8bc8c57b9e1bb729ece7cb770),
[Gui::PropertyEditor::PropertyItem::setPropertyValue()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a9e936f305d42674e1ef1f93d5ed8c539),
[Spreadsheet::Sheet::setQuantityProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1200f02d91cc685af952ac5c7d369010),
[Gui::AlignmentGroup::setRandomColor()](../../dc/d5e/classGui_1_1AlignmentGroup.html#ab3d8e3e17690fe5a440e809ea552ec84),
[Gui::Document::setShow()](../../de/d4e/classGui_1_1Document.html#ab3f9186bfa28a712509d5fcc077754ef),
[SketcherGui::SketchSelection::setUp()](../../dc/d2d/structSketcherGui_1_1SketchSelection.html#a984c246a92a7277cf097f37bd61e542c),
[MeshGui::Workbench::setupContextMenu()](../../db/d83/classMeshGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e),
[PartDesignGui::Workbench::setupContextMenu()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e),
[Gui::StdWorkbench::setupContextMenu()](../../db/d0a/classGui_1_1StdWorkbench.html#a9fc2ca1a33fe4dde2a8a5e6dfc89c57d),
[App::Origin::setupObject()](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[PartDesignGui::TaskSketchBasedParameters::setUpToFace()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#acd1f7bc55f973a0923ef8c31bf3e2ee5),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[PartDesignGui::ViewProviderBody::setVisualBodyMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a50b3de515b84c2e3e19b840ef5fc8187),
[Gui::SelectionSingleton::sGetSelectionEx()](../../d4/dca/classGui_1_1SelectionSingleton.html#acecbfdd83660c2974890d4a57fda9a6f),
[Gui::RecoveryWriter::shouldWrite()](../../d9/d25/classGui_1_1RecoveryWriter.html#aec0a593c8a632c1e1700c4b8e851372f),
[MeshGui::Annotation::show()](../../dd/d2d/classMeshGui_1_1Annotation.html#a8e675bcb0e642864e58f2d9f3b482ca8),
[DrawingGui::ViewProviderDrawingView::show()](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a41516072b7f56cf582e8c638c6dcdf05),
[DrawingGui::ViewProviderDrawingClip::show()](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#a8f9447ce75000777ba104a171d6f85f5),
[TechDrawGui::ViewProviderViewClip::show()](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#abd596bd2eafad6eb412c38723c2fb972),
[TechDrawGui::ViewProviderDrawingView::show()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#aae97a088f034e7f01fb29c28bd2b812a),
[PartGui::ViewProviderSplineExtension::showControlPoints()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a47ebeaa5788d9341eaa389b79acdf55d),
[Gui::Document::slotActivatedObject()](../../de/d4e/classGui_1_1Document.html#af83f915830c8075a246b5424caaa4d2c),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
[PartDesignGui::ViewProviderBody::slotChangedObjectApp()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac2b54ba3e85e13c4e5a63fe12dcc17bf),
[Gui::ViewProviderOriginGroupExtension::slotChangedObjectGui()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a302efc5ec7a5b6a38ba690fbb2ba18af),
[PartDesignGui::ViewProviderBody::slotChangedObjectGui()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ad65bd2facfeba3ad583f89bcbbb4fdb4),
[Gui::Document::slotDeletedObject()](../../de/d4e/classGui_1_1Document.html#a02acfc1218f2666ad7e6b80c804abc99),
[Gui::ManualAlignment::slotDeletedObject()](../../d7/d97/classGui_1_1ManualAlignment.html#a175a5f2e149be360e8a143456cd48ae1),
[Gui::Document::slotFinishRestoreDocument()](../../de/d4e/classGui_1_1Document.html#a63ad8aad31e89cca0651086cf3fd93d2),
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb),
[Gui::Document::slotRelabelObject()](../../de/d4e/classGui_1_1Document.html#af01aad30e324bdccd072f0550b2b9628),
[Gui::Document::slotTransactionAppend()](../../de/d4e/classGui_1_1Document.html#a8f4d208373fe26556f80553a8aa062f1),
[Sketcher::SketchObject::split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68),
[PartDesignGui::ViewProviderTransformed::startEditing()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#aca65c3594f90b54775e4c73ededd1ffc),
[App::PropertyXLink::supportXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a3eec738eb9480c2a52fc5791de8a6d80),
[PartDesignGui::TaskFeaturePick::TaskFeaturePick()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a6a91644eabfe77025b57d629f74ebbba),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[TechDrawGui::TaskLeaderLine::TaskLeaderLine()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a873d04472b6a0de7f250ac13eef14913),
[DrawingGui::TaskOrthoViews::TaskOrthoViews()](../../d4/dd1/classDrawingGui_1_1TaskOrthoViews.html#ae82943a42dfe2bfe1a72ace25e2ddb96),
[FemGui::TaskPostClip::TaskPostClip()](../../da/d40/classFemGui_1_1TaskPostClip.html#a67ad899057f54d4b5f33fa10c3a339e2),
[FemGui::TaskPostCut::TaskPostCut()](../../d5/d1e/classFemGui_1_1TaskPostCut.html#a5a904b79d411b84288d0f838e688c7f0),
[FemGui::TaskPostDataAlongLine::TaskPostDataAlongLine()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#a63d24585168c09609383c5025fc02c61),
[FemGui::TaskPostDataAtPoint::TaskPostDataAtPoint()](../../d9/da7/classFemGui_1_1TaskPostDataAtPoint.html#a442bb680fc74fbe236c0415717eb94a4),
[FemGui::TaskPostFunction::TaskPostFunction()](../../da/d93/classFemGui_1_1TaskPostFunction.html#ae6d7fad41673d6df8797509e030cdcf3),
[FemGui::TaskPostScalarClip::TaskPostScalarClip()](../../df/d2a/classFemGui_1_1TaskPostScalarClip.html#ab3c128515f1c8b3ab10aef3edd773832),
[FemGui::TaskPostWarpVector::TaskPostWarpVector()](../../d9/dc4/classFemGui_1_1TaskPostWarpVector.html#a63fe1a9b92a9a794810bc9d8a020df54),
[PartDesignGui::TaskRevolutionParameters::TaskRevolutionParameters()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#a5509b04d5cfc1da7d5314c4a038a01e2),
[TechDrawGui::TaskRichAnno::TaskRichAnno()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#acfd26140dce1c41560c4391c78b2fb06),
[Gui::TaskView::TaskSelectLinkProperty::TaskSelectLinkProperty()](../../d3/d1b/classGui_1_1TaskView_1_1TaskSelectLinkProperty.html#a6ec8c7b8e4d45bde4f8ce5968bdd91b4),
[MeshGui::TaskSmoothing::TaskSmoothing()](../../da/d50/classMeshGui_1_1TaskSmoothing.html#ab51dce40b8a4bd1bc653af4b18f6fda9),
[TechDrawGui::TaskWeldingSymbol::TaskWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aaf7cb244a051a9f8977d8ca2e0f00a17),
[Sketcher::SketchObject::toggleDriving()](../../d9/dad/classSketcher_1_1SketchObject.html#a5127694bcd6a2f20e35545e6d374c026),
[Gui::PropertyEditor::PropertyMatrixItem::toolTip()](../../d6/d20/classGui_1_1PropertyEditor_1_1PropertyMatrixItem.html#a0d3887efda4155ea320aba09ee6af779),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyMaterialItem::toolTip()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#a493166d2591c115bc095c5866bd5e4a0),
[Gui::PropertyEditor::PropertyMaterialListItem::toolTip()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a420082fd5b1643a150fb0650377990cc),
[SketcherGui::CurveConverter::toVector2D()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#a1c983e1d8c4e502bb95bf515b85c5067),
[Sketcher::SketchObject::transferFilletConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a618d3720b583b93238a18fec74007377),
[Sketcher::SketchObject::trim()](../../d9/dad/classSketcher_1_1SketchObject.html#a55c244742ef90c7bc339e6c0285e2027),
[MeshGui::ViewProviderMesh::trimMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a99db0ab49ba22437ef202c633d752b52),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
[Gui::ViewProviderAnnotation::updateData()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#acaee4ade8605ecc0ce997f273a931986),
[Gui::ViewProviderAnnotationLabel::updateData()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#aa2e79cd63adfc0a43501b66ffa4438dd),
[Gui::ViewProviderGeometryObject::updateData()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a4818bdc22e4b19444d703d72bec9d7ca),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[DrawingGui::ViewProviderDrawingPage::updateData()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
[FemGui::ViewProviderFemMesh::updateData()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2b42be80762272d7f6be0b30e7d6a3f5),
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[MeshGui::ViewProviderMesh::updateData()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#acfabc68fbd4cb6188071e498739066d8),
[MeshGui::ViewProviderIndexedFaceSet::updateData()](../../d8/d12/classMeshGui_1_1ViewProviderIndexedFaceSet.html#a18d4f21152ed2f96bfcec096aa0e639c),
[MeshGui::ViewProviderMeshObject::updateData()](../../db/d49/classMeshGui_1_1ViewProviderMeshObject.html#ab567af502db9d5a8e0beba2181fb39b3),
[MeshGui::ViewProviderMeshCurvature::updateData()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033),
[MeshGui::ViewProviderMeshFaceSet::updateData()](../../df/de9/classMeshGui_1_1ViewProviderMeshFaceSet.html#a1a79e8c47f1e048e3027f7908856d85f),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderMultiFuse::updateData()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a2dd30d90dd627899aae55dd7f6082bfd),
[PartGui::ViewProviderMultiCommon::updateData()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#afd2565caa649c9122a8da1bad7217b88),
[PartGui::ViewProviderCompound::updateData()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a864f55403bd4a3b5a81834205fe9561d),
[PartGui::ViewProviderCurveNet::updateData()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#ac10fc8ddaf0e0f8b4fed8ed9f957073a),
[PartGui::ViewProviderFillet::updateData()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a681e5f4afcfbf90240da46de01068325),
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
[PartGui::ViewProviderCustom::updateData()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[PartGui::ViewProviderRuledSurface::updateData()](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#af8ea975ad249bc60db35caf151b9908b),
[PathGui::ViewProviderArea::updateData()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a33f43f1d72596152fa4d6944b59360b0),
[PathGui::ViewProviderAreaView::updateData()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a5681f9ff35ad2a07e43b5847ebe09f15),
[PathGui::ViewProviderPathShape::updateData()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ac696ef550f0e27b0665de391ca5891a9),
[PointsGui::ViewProviderScattered::updateData()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab2bc3db5bc92357f983d5c88d287df35),
[PointsGui::ViewProviderStructured::updateData()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#afdfd3564ae817f52b13b4ba6f6e093e8),
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[SketcherGui::ViewProviderCustom::updateData()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[Gui::ViewProviderDragger::updateData()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a6d433c9fe9d47fa7ab9be6d7e01d6509),
[PartDesignGui::ViewProvider::updateData()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae230b789ddc5d513656f4e87964bd01e),
[TechDrawGui::ViewProviderTemplate::updateData()](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#af08c8e552302f0c07734e06211b6fb17),
[PartDesignGui::ViewProviderBody::updateData()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a2a541fb893a7130314f3c7161c33477e),
[FemGui::ViewProviderFemPostPipeline::updateFunctionSize()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#a015e75189dd7b4b8719fce0c264388f5),
[SketcherGui::EditModeGeometryCoinManager::updateGeometryColor()](../../d2/d97/classSketcherGui_1_1EditModeGeometryCoinManager.html#a4b2ba186bb93e2b535c65ba180ab0682),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e),
[FemGui::ViewProviderFemPostFunctionProvider::updateSize()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#ad783f019da5429b4ca0669a14d606d72),
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461),
[SketcherGui::DrawSketchHandlerLineSet::updateTransitionData()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a87c661c6611a6c685accb1c089fdeba8),
[App::PropertyLinkSubList::upgrade()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac14ef2a9047eefe8d8090b75da12841b),
[App::PropertyXLink::upgrade()](../../d2/de2/classApp_1_1PropertyXLink.html#ab593a78066f09572d98eac5046d8accf),
[App::PropertyXLinkSubList::upgrade()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a66df091fa4c2e1c15d7823fe5b3d77a2),
[App::PropertyXLinkSub::upgrade()](../../d4/da0/classApp_1_1PropertyXLinkSub.html#a0f3a85600e83e0f36d654f72939d9add),
[Sketcher::SketchObject::validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9),
[Gui::PropertyEditor::PropertyStringItem::value()](../../dd/d22/classGui_1_1PropertyEditor_1_1PropertyStringItem.html#af7d6ebf7226ead072d520b62051d77ed),
[Gui::PropertyEditor::PropertyFontItem::value()](../../de/df5/classGui_1_1PropertyEditor_1_1PropertyFontItem.html#ad4b2d0d05eea1344b23cf64e5af0bf85),
[Gui::PropertyEditor::PropertyIntegerItem::value()](../../de/d3b/classGui_1_1PropertyEditor_1_1PropertyIntegerItem.html#af8403087a42310e8e396c69ba89b31dc),
[Gui::PropertyEditor::PropertyIntegerConstraintItem::value()](../../d6/d39/classGui_1_1PropertyEditor_1_1PropertyIntegerConstraintItem.html#a2b469055bba9c4ee087df3e587dcf857),
[Gui::PropertyEditor::PropertyFloatItem::value()](../../db/df4/classGui_1_1PropertyEditor_1_1PropertyFloatItem.html#a3504141c979ff4cb5f9ea5cf54a05be9),
[Gui::PropertyEditor::PropertyUnitItem::value()](../../d7/d5d/classGui_1_1PropertyEditor_1_1PropertyUnitItem.html#a77537bbfa6f70779bae14ec0c8af8ce7),
[Gui::PropertyEditor::PropertyFloatConstraintItem::value()](../../d2/d0a/classGui_1_1PropertyEditor_1_1PropertyFloatConstraintItem.html#acbaae4a3b13384b2e824bc1162c4c668),
[Gui::PropertyEditor::PropertyBoolItem::value()](../../d4/dc0/classGui_1_1PropertyEditor_1_1PropertyBoolItem.html#a656033aba09820501b40c49cfd240a45),
[Gui::PropertyEditor::PropertyVectorItem::value()](../../dc/d86/classGui_1_1PropertyEditor_1_1PropertyVectorItem.html#a5856c2d9815846f5c63baf8785c77e0e),
[Gui::PropertyEditor::PropertyVectorListItem::value()](../../dc/d19/classGui_1_1PropertyEditor_1_1PropertyVectorListItem.html#a8043a12f10c28a8bf2ef6ba93a7812cb),
[Gui::PropertyEditor::PropertyVectorDistanceItem::value()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#a022f31e7063dd604bec6e771a36d0c96),
[Gui::PropertyEditor::PropertyMatrixItem::value()](../../d6/d20/classGui_1_1PropertyEditor_1_1PropertyMatrixItem.html#afcae29df2122fd2d492f14d7bfc3f781),
[Gui::PropertyEditor::PropertyRotationItem::value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem::value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
[Gui::PropertyEditor::PropertyEnumItem::value()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a94427cf59c1c81076fda89e8f9f0dd7f),
[Gui::PropertyEditor::PropertyStringListItem::value()](../../d7/d2f/classGui_1_1PropertyEditor_1_1PropertyStringListItem.html#ac7e887e41792012af96be518db34a533),
[Gui::PropertyEditor::PropertyFloatListItem::value()](../../de/d74/classGui_1_1PropertyEditor_1_1PropertyFloatListItem.html#a36c1a4829509db372d7f393525345529),
[Gui::PropertyEditor::PropertyIntegerListItem::value()](../../d4/d5f/classGui_1_1PropertyEditor_1_1PropertyIntegerListItem.html#a579b1460c152751041d4d9bdede76c69),
[Gui::PropertyEditor::PropertyColorItem::value()](../../d9/d81/classGui_1_1PropertyEditor_1_1PropertyColorItem.html#acf049af57cd349ad168116b0e0ab7e26),
[Gui::PropertyEditor::PropertyMaterialItem::value()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#acdc82f103ed6664a083e9fa11532c4cc),
[Gui::PropertyEditor::PropertyMaterialListItem::value()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a7440116fc91a842840573c86ddbee0ab),
[Gui::PropertyEditor::PropertyFileItem::value()](../../d3/d1f/classGui_1_1PropertyEditor_1_1PropertyFileItem.html#a803bcb00934c3d895af5520cfea041f1),
[Gui::PropertyEditor::PropertyPathItem::value()](../../de/d04/classGui_1_1PropertyEditor_1_1PropertyPathItem.html#a78946d13ccf37898411e45d4d9730537),
[Gui::PropertyEditor::PropertyTransientFileItem::value()](../../de/d80/classGui_1_1PropertyEditor_1_1PropertyTransientFileItem.html#a7ec4af498f59a81de2414fdaced5669f),
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1),
[MeshPartGui::CurveOnMeshHandler::Private::vertexCallback()](../../d2/d9f/classCurveOnMeshHandler_1_1Private.html#a373137b450a6003db4057cc546930264),
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c),
[App::PropertyLinkList::~PropertyLinkList()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aef7be25314c8c5441d9baa207ddd51c1),
[App::PropertyLinkSub::~PropertyLinkSub()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac2366078790473115b614fdc02345a4a),
[App::PropertyLinkSubList::~PropertyLinkSubList()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17189b0ae71b797884f1ca041cfe263f),
[PartDesignGui::TaskDatumParameters::~TaskDatumParameters()](../../d1/d52/classPartDesignGui_1_1TaskDatumParameters.html#a5a7f379ad21fc1a6ffa05fbd0ae2ac7a),
and
[App::Transaction::~Transaction()](../../de/dbf/classApp_1_1Transaction.html#a362b0d2524d0c799165190517192dca9).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) Persistence::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
pure virtual  
  
This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?

Implemented in
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#acf0627e62bf073aac01348d2781a5048),
[Mesh::MeshObject](../../d8/dcc/classMesh_1_1MeshObject.html#abb896051b37caefa717049dac0cd3b48),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#a4c9fe5dbd7d6842a0080cb8ea1d29260),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a9bb3a257e38b56ffd6395771c9f49539),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a5fb0c1063d6c1f8ee74d5bb12c114f03),
[Points::PointKernel](../../dc/de1/classPoints_1_1PointKernel.html#a643e566cb51da18f96aa90dea9e6e924),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a3ee505b7da59d00f2abf78020a502ede),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a4c9fe5dbd7d6842a0080cb8ea1d29260),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a1ddc9de25c76ec9ade4d29a77e8b0664),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a75847bb599e4c1d12fb874c6a9775c48),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#ac815825f1926b909f5138223e5f4a2ec),
[App::MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#af48ade47d965eec0fc69a895b163d761),
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a3cb1a922e29e35137aec11c7d91614ff),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#ac0947f60bbe89d193b47e229636004c1),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#af3dc5d89e0377b785478fbfb2f0f1064),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a070c6c11a8fd1ecf96644985c9b8700f),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a8de3ce227ab32597ae3c903fedcac66d),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a0a92013a1e026a536da4b4b8a5e74086),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a8c29971099b9581c77eef99b42218ad7),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a1dacdc31bef9c42aa5da1b0cc1c628bc),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#ae0cbcb1161e090b5ff249c4fc5a70f03),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#aa07a81452563bf739d36dcaec51429a3),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#acfb47acb28b9927f07d24bcb1248c317),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a04fa2896f24ea0bd06223699ef813421),
[App::Transaction](../../de/dbf/classApp_1_1Transaction.html#ae95719b55aff8b6a974ee4dbbc263ea2),
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#a3a43e98f7d1bf137d920be96bc8a4587),
[Gui::Document](../../de/d4e/classGui_1_1Document.html#a04bb8a0b26b9a73280523abe24444263),
[Gui::MergeDocuments](../../d5/d20/classGui_1_1MergeDocuments.html#af48ade47d965eec0fc69a895b163d761),
[Gui::Thumbnail](../../d3/d4d/classGui_1_1Thumbnail.html#a0210151fc417c8b9d4fa81aba4799722),
[Fem::FemMesh](../../d3/d2e/classFem_1_1FemMesh.html#a3d722571a0dff3f2a52f4fb4651c35b4),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a342c2d3d8b671357fa6654db21f352a3),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ae81b5620b77d2cc1831ad44910df1301),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ab30094bbea0f04d4ccc0c7f85488815e),
[Part::Geometry](../../dc/df0/classPart_1_1Geometry.html#ab50e1bf7e2261d8df7d95d2992608c4a),
[Part::GeomPoint](../../d2/dfb/classPart_1_1GeomPoint.html#abc5c9e51aea0190b042e39e084db59b0),
[Part::GeomBezierCurve](../../d5/d40/classPart_1_1GeomBezierCurve.html#aae57050f278adc40572c3eccb785ee71),
[Part::GeomBSplineCurve](../../df/dfe/classPart_1_1GeomBSplineCurve.html#afc463eaf55761075722005ec10a27311),
[Part::GeomTrimmedCurve](../../df/d24/classPart_1_1GeomTrimmedCurve.html#a6e8d660bbbd70d9093d4d83b89c5cea2),
[Part::GeomCircle](../../d0/dde/classPart_1_1GeomCircle.html#af94b90bd3d8c2f3d565e82260f325c9e),
[Part::GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html#a20954b6074b2aa0ac19c5bc0c23164b7),
[Part::GeomEllipse](../../db/d52/classPart_1_1GeomEllipse.html#a6ec7386aee684ae5740cadcc8c5e7333),
[Part::GeomArcOfEllipse](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a0d565827bfb4bdc7cbd1bcf473e9c2c6),
[Part::GeomHyperbola](../../d7/d9e/classPart_1_1GeomHyperbola.html#a51f341bd51fdece7104a55542589a441),
[Part::GeomArcOfHyperbola](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a829226c0c25519ee39ecd7e040f8e713),
[Part::GeomParabola](../../d9/ddf/classPart_1_1GeomParabola.html#a3d22357ca7b599b71df7ea85ead4cf65),
[Part::GeomArcOfParabola](../../db/ddc/classPart_1_1GeomArcOfParabola.html#a1cf0e3946735c4f66d33b421da95b87f),
[Part::GeomLine](../../d5/d30/classPart_1_1GeomLine.html#a84f1e49cba6801b9ae3985402bc65287),
[Part::GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html#aae89ab9986dac82fda456c6efe2ff1bb),
[Part::GeomOffsetCurve](../../d0/d36/classPart_1_1GeomOffsetCurve.html#aec3c9cdd6ab95c78d5753e4543d080f2),
[Part::GeomBezierSurface](../../df/dab/classPart_1_1GeomBezierSurface.html#a83720e70a9468afdf627bc2a117bafbb),
[Part::GeomBSplineSurface](../../d1/d27/classPart_1_1GeomBSplineSurface.html#ae0216932ffa84f0af171df14fb0c92ae),
[Part::GeomCylinder](../../de/dc7/classPart_1_1GeomCylinder.html#a653ee1f2201ef2b6146734d5abbcb2da),
[Part::GeomCone](../../d0/d7c/classPart_1_1GeomCone.html#acbdc85e79cf7f082245c525ace5424ad),
[Part::GeomSphere](../../dc/da5/classPart_1_1GeomSphere.html#a4e5a59f38babe453921f36ffca358046),
[Part::GeomToroid](../../da/d8f/classPart_1_1GeomToroid.html#ab5fa2f107669f91fa7bd984356acb2d7),
[Part::GeomPlane](../../d2/d0e/classPart_1_1GeomPlane.html#a0440f2dc4afe1a6a9397b1dadd03e37d),
[Part::GeomOffsetSurface](../../dc/d14/classPart_1_1GeomOffsetSurface.html#a4d302ee132e9cd3ce365a1fc29805bc5),
[Part::GeomPlateSurface](../../d7/db9/classPart_1_1GeomPlateSurface.html#ae4cc89a4804d8d3f5784833d504b8a86),
[Part::GeomTrimmedSurface](../../de/dd0/classPart_1_1GeomTrimmedSurface.html#ae32d5cf43aa0ce71c53bd61d5e0786d1),
[Part::GeomSurfaceOfRevolution](../../df/dc7/classPart_1_1GeomSurfaceOfRevolution.html#ace16824cde62d59a2765e4e986270732),
[Part::GeomSurfaceOfExtrusion](../../de/dd5/classPart_1_1GeomSurfaceOfExtrusion.html#a5c0aa9d6788510ea5b50acbbaa5021b4),
[Part::Geometry2d](../../d1/dad/classPart_1_1Geometry2d.html#aa889888c9a352e10e5b73f3bd82ecc65),
[Part::Geom2dPoint](../../d8/da9/classPart_1_1Geom2dPoint.html#a58bfdb28f79acfb452be1d69250a57c3),
[Part::Geom2dBezierCurve](../../d6/d50/classPart_1_1Geom2dBezierCurve.html#adeef4af2c297cfb769295bb6e41a952f),
[Part::Geom2dBSplineCurve](../../dd/d59/classPart_1_1Geom2dBSplineCurve.html#ad5d0c82228624a74854d5c044a92e85f),
[Part::Geom2dCircle](../../d7/d4e/classPart_1_1Geom2dCircle.html#a86683674eddeeb7af34a5ed485f61141),
[Part::Geom2dArcOfCircle](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a98f96a157051a39abd65f5931655d5fb),
[Part::Geom2dEllipse](../../db/db9/classPart_1_1Geom2dEllipse.html#ab7e5ce753558a28054279a8874d95f10),
[Part::Geom2dArcOfEllipse](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a36f1dfa147b05d3e55a877a4668b484c),
[Part::Geom2dHyperbola](../../d2/d95/classPart_1_1Geom2dHyperbola.html#aa054849da14c6e37c8b0403697ac70ba),
[Part::Geom2dArcOfHyperbola](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#a1e1430efc47afe51e82d1f83fc53ce56),
[Part::Geom2dParabola](../../d9/dff/classPart_1_1Geom2dParabola.html#a8d9a90d87d4fde94678c17f49d6cb399),
[Part::Geom2dArcOfParabola](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a4a209578594c7334a8f33433473d37d4),
[Part::Geom2dLine](../../d2/d27/classPart_1_1Geom2dLine.html#aaed57b931e60d411db746e286c0331ce),
[Part::Geom2dLineSegment](../../df/ded/classPart_1_1Geom2dLineSegment.html#ae5457982ff9430af6c89774f58979ac2),
[Part::Geom2dOffsetCurve](../../d5/de5/classPart_1_1Geom2dOffsetCurve.html#a8412323e747ac749ce38c40570fafdfd),
[Part::Geom2dTrimmedCurve](../../d8/da3/classPart_1_1Geom2dTrimmedCurve.html#a7b71bc296dbca0c7efcf39d2262d3056),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#a63c36bfe30bbdfccb175cfd21659c3e4),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a206503fb4c63200740b8d39c1c48f87e),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ad190366d173d7c806c9072700cbc2cae),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a7d0e216876cfa009eeacb77bffaf9924),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#ac655ec10e179df8d8b1e92b7e0ed7852),
[Path::Command](../../d7/d2e/classPath_1_1Command.html#a86a23f4a609042ef134ff3f865a6b421),
[Path::Toolpath](../../d6/d0c/classPath_1_1Toolpath.html#ad41fc0368a4d3c4a7cbe151db38efbc4),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#a070c6c11a8fd1ecf96644985c9b8700f),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#adf84af3865b017b4e342e1cd8dbc6fbf),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#a0b7a308849d743524e7da5bae7979a24),
[Path::Tool](../../dd/dfe/classPath_1_1Tool.html#a96b287708e771d15ba84d28a14c71271),
[Path::Tooltable](../../df/dca/classPath_1_1Tooltable.html#ada66c6f807c40878f51cb08dc73c2907),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a1bf4c5d61a30a4a92473dda0faffac51),
[Robot::Robot6Axis](../../dc/d5f/classRobot_1_1Robot6Axis.html#a1608a3a59fe137c8d4168a708c7b9d41),
[Robot::Trajectory](../../d7/d14/classRobot_1_1Trajectory.html#ae61d1d5f0804b581c2e7e948aa8be348),
[Robot::Waypoint](../../d1/dc7/classRobot_1_1Waypoint.html#a892239e4c5677505c84d339d804d1e58),
[Sketcher::Sketch](../../d9/d9b/classSketcher_1_1Sketch.html#a905fed374d53d0c7d296d050fcfbb823),
[TechDraw::CosmeticVertex](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a494a5e07ce741f855c97310ac87df778),
[TechDraw::CosmeticEdge](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a122887bd9cace75bf424115d15b86cf9),
[TechDraw::CenterLine](../../d5/dd5/classTechDraw_1_1CenterLine.html#a96b2054b98aeaff0857d5b1e0bbc4da9),
[TechDraw::GeomFormat](../../d7/d64/classTechDraw_1_1GeomFormat.html#ab78ebce050df603f16108dea47cf8558),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a20ecb322cb917b1296743d6ee09498e4),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a3922fe662498c7af4bcba1534cc8a3ee),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a8061d4341f265a7eecd653cbbeffc563),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2a7bd2bbdbd92e080d7d599a0e8148b6),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a10f0edf85c1bd933f329ccc3ca9d14a8),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a8e52149fbd49677ea09a15d3d5e09d6b),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ac1dde1b7bc7de9e0ad57bc40f3e3a23a),
[Part::GeomConic](../../d1/d86/classPart_1_1GeomConic.html#a48f4355ef14d76732eb1ddb3bf70f7ce),
[Part::GeomArcOfConic](../../db/d48/classPart_1_1GeomArcOfConic.html#aeb921a9a1897e7867370a447620e45f9),
[Part::Geom2dConic](../../d8/d0d/classPart_1_1Geom2dConic.html#a8e0d68cc1f9bd32625cb7fe81d959e00),
[Part::Geom2dArcOfConic](../../dc/d1b/classPart_1_1Geom2dArcOfConic.html#a543aff4c6145555eb97cd83fa0071c37),
[App::Document](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043),
[App::Property](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9c2ed33cbd8061fca8fb90a67aadf4cb),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a125d7701b320054ba27f96a1ce07eeb5),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#aff4590ccda7a04bc8f92c30b4a3495e6),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a33e86ed95a033c93066f10d03b35fb17),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a45392f70e5990f85fd629a2c2add51b7),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a7467d6db2f6e7842e417ecc0d0f85bb7),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#ab78285bd88df778df0e28d4a849ab2a6),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a984b975e8df1de6523aa9588ad1a4751),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a05d3ff3e3e2e736467523e3fbc715df0),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a19431f105396ee0ea39fb438e0f72fef),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7b812edb54403de064bed5a2dc2ea33d),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a412587d903efffdb3abcaad4f4c73250),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a9ff58b5b4cdbe716aa81a3b025f782ab),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#aac54de337807ec4a440a3452a42f6810),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a84c1f4f40247c1cbce90a85d082206c9),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a1c04e166a0692a748058db4772118c22),
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a8487b7c73af09eed5681c133040fb417),
[Gui::DocumentItem](../../df/d15/classGui_1_1DocumentItem.html#a8ac1482ce35e5cc7d79424e2a10da057),
[Sketcher::Constraint](../../d6/def/classSketcher_1_1Constraint.html#a404e5a242fefd7137bd044aee6e88113),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#ac720a742459c231434f2c5ee0595abaf),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a904bc155ca037a1eb404b3778b8cd603),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adcb04008a5202a2f3eeacc2f10554e88).

## ◆ getTypeId()

| [Base::Type](../../dc/dee/classBase_1_1Type.html) Base::Persistence::getTypeId  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566).

Referenced by
[PartDesignGui::TaskDlgFeatureParameters::accept()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#abfc2d8ecb714c2b558cc8feb07fa55c3),
[PartDesignGui::TaskDlgSketchBasedParameters::accept()](../../da/def/classPartDesignGui_1_1TaskDlgSketchBasedParameters.html#a781c55f79eb60cc2c7472679f26dcce7),
[PartGui::DlgPrimitives::accept()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a1db668afa4bde5626f25c5e34f596b82),
[Sketcher::PropertyConstraintList::acceptGeometry()](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#acb51bc9feaf1b68d216e0935eb9713b0),
[SketcherCopy::activate()](../../da/dc9/classSketcherCopy.html#a859bdd8b67b8dc9856f4353ac1fe37aa),
[StdCmdPlacement::activated()](../../d5/d61/classStdCmdPlacement.html#aa4b496fefdba5569fdd808ae245a45b0),
[StdCmdGroup::activated()](../../d0/de4/classStdCmdGroup.html#a44a9faa66df180f400cd830bb538771d),
[CmdSketcherConstrainHorizontal::activated()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#adc766562bb486afb5941fc9bade87c59),
[CmdSketcherConstrainVertical::activated()](../../d7/d37/classCmdSketcherConstrainVertical.html#a0f174c055305b510bc2b3ce16eb6e80b),
[CmdSketcherConstrainDistance::activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainPointOnObject::activated()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#aa6f7ed1adb19f60b65703fafe91fdda9),
[CmdSketcherConstrainDistanceX::activated()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#a175608d3c6099fc7504de3b5641a01c0),
[CmdSketcherConstrainDistanceY::activated()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a59b776e3be604ff1686d112c0f82334b),
[CmdSketcherConstrainParallel::activated()](../../d3/df0/classCmdSketcherConstrainParallel.html#a4c2b4c186452210ed3e69fb1c5f1afe6),
[CmdSketcherConstrainPerpendicular::activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainTangent::activated()](../../d8/d80/classCmdSketcherConstrainTangent.html#a49b68ec579dfa3ac0410539e34096f90),
[CmdSketcherConstrainRadius::activated()](../../d2/d16/classCmdSketcherConstrainRadius.html#a210220527e41b3ad828269b80a359354),
[CmdSketcherConstrainDiameter::activated()](../../da/dbe/classCmdSketcherConstrainDiameter.html#af5d04e1e2fa404f140625af1b917f186),
[CmdSketcherConstrainRadiam::activated()](../../d6/d18/classCmdSketcherConstrainRadiam.html#aee6c0c85caaecf9e7bcd99dff1efd6bc),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[CmdSketcherConstrainEqual::activated()](../../de/dbe/classCmdSketcherConstrainEqual.html#ac247e0d1e55a27e0e40c204965f758be),
[CmdSketcherConstrainSymmetric::activated()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#afc33b5d3e672956b47801982de4611ef),
[Sketcher::SketchObject::addCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#a2ae92a618d60a264ed20d7a359b89f98),
[Sketcher::SketchObject::addGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#ad1b1d3067af464e9d4f245b9ef145096),
[Sketcher::Sketch::addGeometry()](../../d9/d9b/classSketcher_1_1Sketch.html#a76c2ea9371fa62f03aeba26a5f10160b),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a77502422ab7bde4fb01ab4474fd930af),
[App::Transaction::addObjectChange()](../../de/dbf/classApp_1_1Transaction.html#a49570b3477b90ad3f35dae121668ea87),
[App::Transaction::addObjectDel()](../../de/dbf/classApp_1_1Transaction.html#aaa52509516281edac9af07edc57bb707),
[App::Transaction::addObjectNew()](../../de/dbf/classApp_1_1Transaction.html#a33d72374a75b0138c6a5c9d71c858cff),
[App::TransactionObject::addOrRemoveProperty()](../../d9/d02/classApp_1_1TransactionObject.html#a1a9c63db207f7e24ed6918877c134764),
[App::Transaction::addOrRemoveProperty()](../../de/dbf/classApp_1_1Transaction.html#a13b0dfb6149502294662f69042e250d8),
[Sketcher::SketchObject::addSymmetric()](../../d9/dad/classSketcher_1_1SketchObject.html#afcbb1d6f5a99e52a70fdf6d9d3c9d361),
[MeshGui::DlgEvaluateMeshImp::addViewProvider()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a40061f032d5f55a73a2c0eb3a699e886),
[SketcherGui::ExtendSelection::allow()](../../d8/db8/classSketcherGui_1_1ExtendSelection.html#a071a91a94c7f8b448ea508d6b87d76ef),
[SketcherGui::FilletSelection::allow()](../../dd/d6f/classSketcherGui_1_1FilletSelection.html#a2d300c4873259393e235ef5a3845825b),
[SketcherGui::SplittingSelection::allow()](../../d6/d33/classSketcherGui_1_1SplittingSelection.html#a0adaeae8fbe5fbacaa163b208eddc691),
[SketcherGui::TrimmingSelection::allow()](../../de/d39/classSketcherGui_1_1TrimmingSelection.html#a981ac86ae1dbd466c3f25a6ffb7774f8),
[PartDesignGui::ReferenceSelection::allow()](../../dd/d1c/classPartDesignGui_1_1ReferenceSelection.html#aba5a74db909e196f326ebb626e1ba150),
[SketcherGui::ExternalSelection::allow()](../../d3/dff/classSketcherGui_1_1ExternalSelection.html#a8cb2852af5a0bfc42d8844d3f5d1edde),
[PartGui::ViewProviderPartExt::allowOverride()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#aef11ccd8d18daf6e55d2f5cb7af8431f),
[Gui::QuantitySpinBox::apply()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#ac3ec986d0729752d078f3c57a18f7cca),
[CmdSketcherConstrainHorizontal::applyConstraint()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#a36f07e42457531be9ed67008ba95d021),
[CmdSketcherConstrainVertical::applyConstraint()](../../d7/d37/classCmdSketcherConstrainVertical.html#adf3ea9ac8dd73b137225507c8028e880),
[CmdSketcherConstrainDistance::applyConstraint()](../../d4/de5/classCmdSketcherConstrainDistance.html#a9c0f733b397d4f7e05af5f7c70f9debb),
[CmdSketcherConstrainPointOnObject::applyConstraint()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#a70d28fda1de1503aa99cf66b055420d1),
[CmdSketcherConstrainDistanceX::applyConstraint()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#abf16c738ea7247db91721d5d14d279fc),
[CmdSketcherConstrainDistanceY::applyConstraint()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a2df22f90384fbde7d951992c9564d3ad),
[CmdSketcherConstrainPerpendicular::applyConstraint()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#aa62bab542b8f016bd752fdef90110778),
[CmdSketcherConstrainTangent::applyConstraint()](../../d8/d80/classCmdSketcherConstrainTangent.html#a90a8595e30112cb64ddb61088c3af96b),
[CmdSketcherConstrainRadius::applyConstraint()](../../d2/d16/classCmdSketcherConstrainRadius.html#a0529327862aefd7a8d9d0bed9a03571c),
[CmdSketcherConstrainDiameter::applyConstraint()](../../da/dbe/classCmdSketcherConstrainDiameter.html#a2cba7a76a06cffab82d09cdfcddf0065),
[CmdSketcherConstrainRadiam::applyConstraint()](../../d6/d18/classCmdSketcherConstrainRadiam.html#a08e2367864e5c690e2c6607f10af5e7d),
[CmdSketcherConstrainAngle::applyConstraint()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a5602881a59f6c0a0a83a30641560aeb7),
[CmdSketcherConstrainEqual::applyConstraint()](../../de/dbe/classCmdSketcherConstrainEqual.html#a7efdda717363d452685832c9670be199),
[CmdSketcherConstrainSymmetric::applyConstraint()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#af292ec0892fe051d1d5f06fb9440664e),
[Part::Geometry::assignTag()](../../dc/df0/classPart_1_1Geometry.html#a86a437b296be54098f3470b861036550),
[TechDraw::CenterLine::assignTag()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a2abd56f5bd1a5c2fb394be0a05ef782a),
[TechDraw::CosmeticEdge::assignTag()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a4c1356c06ac8f05c144c8c6775a4b5b6),
[TechDraw::CosmeticVertex::assignTag()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a6316eae88b6910cb7e2aebde7050cd30),
[TechDraw::GeomFormat::assignTag()](../../d7/d64/classTechDraw_1_1GeomFormat.html#a3c4f657b6cca5fe253d19904801dcf3a),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[App::LinkBaseExtension::checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[PartDesign::SubShapeBinder::checkCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3698bc706a89765ff35db75048a08698),
[PartDesignGui::collectMovableDependencies()](../../dc/d12/namespacePartDesignGui.html#a134e411f38de8ca01fe259064cdcc27b),
[Sketcher::SketchObject::convertToNURBS()](../../d9/dad/classSketcher_1_1SketchObject.html#a23e6660388fbe498a07b07a8c4f065fe),
[SketcherGui::DrawSketchHandler::createAutoConstraints()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#aaeb21f657e7a40232d0b9e275295765c),
[MeshGui::ViewProviderMeshCurvature::curvatureInfo()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#aa2902a6b29f9d107136899cdbf8eca28),
[MeshGui::ViewProviderMeshCurvature::curvatureInfoCallback()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd81924b9ccb33db4d9fb1fe49f1f934),
[Sketcher::SketchObject::decreaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#ace68bb529eeba8cd3e39e3418213d044),
[Sketcher::SketchObject::deleteUnusedInternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a1a8c355b131873c4cb9d783fa5510fd9),
[Sketcher::SketchObject::delGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a40dfaae474c808c67807476529431053),
[Gui::DocumentObjectItem::displayStatusInfo()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a235f26b8fbf37e4e4efccdae9cbbada0),
[PartGui::DlgPrimitives::DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[SketcherGui::EditModeConstraintCoinManager::drawConstraintIcons()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a20c4280c68dc704bd2652d6097b0383a),
[Sketcher::SketchObject::evaluateSupport()](../../d9/dad/classSketcher_1_1SketchObject.html#ae2d3e03c3503536535164dfea9630169),
[Gui::ViewProvider::eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99),
[Mesh::HarmonizeNormals::execute()](../../d8/d1c/classMesh_1_1HarmonizeNormals.html#a7f4d3c74b5c71fcb87e8467ae09a78f0),
[Mesh::FlipNormals::execute()](../../d3/d05/classMesh_1_1FlipNormals.html#a781c0a4c289cd3fecb312a743d04c2a6),
[Mesh::FixNonManifolds::execute()](../../d5/d33/classMesh_1_1FixNonManifolds.html#a1ee7ec392eeb5cb3a206989d21b3e3bc),
[Mesh::FixDuplicatedFaces::execute()](../../d9/d63/classMesh_1_1FixDuplicatedFaces.html#affadc4a69ba22744612248e94059ea13),
[Mesh::FixDuplicatedPoints::execute()](../../d1/d7b/classMesh_1_1FixDuplicatedPoints.html#abb108a05948e9906cefd394da59fdf77),
[Mesh::FixDegenerations::execute()](../../db/d8f/classMesh_1_1FixDegenerations.html#a3425c9ffba4deeb1c73c7fe910429687),
[Mesh::FixDeformations::execute()](../../d1/dbc/classMesh_1_1FixDeformations.html#a8c0ddd5b2e77c30a2466dc1fd08cdc7a),
[Mesh::FixIndices::execute()](../../d3/deb/classMesh_1_1FixIndices.html#a83eddf2883e3fc904c150d124d8aa01f),
[Mesh::FillHoles::execute()](../../d2/ddd/classMesh_1_1FillHoles.html#a21a0e0e99c2dcd82f9918fe67def820b),
[Mesh::RemoveComponents::execute()](../../da/d7a/classMesh_1_1RemoveComponents.html#a552facf8870d9ef3b36e1dee379fac07),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Surface::Cut::execute()](../../d4/d17/classSurface_1_1Cut.html#adade24c19d386572d09157489463f785),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[TechDraw::DrawViewSpreadsheet::execute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[PartDesign::Body::execute()](../../dd/db8/classPartDesign_1_1Body.html#a4abca6b2645adade81347d0e850a2659),
[Surface::Extend::execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[Sketcher::SketchObject::exposeInternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a7d89f466b41e7479505e70c73d832428),
[Sketcher::SketchObject::extend()](../../d9/dad/classSketcher_1_1SketchObject.html#a863df4c6af57263b15a8170b377ef466),
[PartGui::ViewProviderSplineExtension::extensionUpdateData()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#ac0f6ab010c3a75a975e8ca3ad2ef60e2),
[MeshGui::ViewProviderMesh::faceInfoCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae3d2f360b9f432962521c1bb1b77dd98),
[Sketcher::SketchObject::fillet()](../../d9/dad/classSketcher_1_1SketchObject.html#a045cba23726c2d8dfe57ce28c758973c),
[MeshGui::ViewProviderMesh::fillHoleCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ad3cdb2b5549c092780ef6b1bb252cc02),
[Gui::FreeCADGui_subgraphFromObject()](../../d9/dad/namespaceGui.html#a1562062f6fcff8f9ec05618c80435514),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[PartDesign::Feature::getBaseObject()](../../d7/d51/classPartDesign_1_1Feature.html#a4b32fcefa87c31a546571d96cfd41413),
[InspectionGui::ViewProviderInspection::getIcon()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a76d57438c1350bd9a432557f0c23dc5e),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[App::OriginGroupExtension::getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[Sketcher::SketchObject::getPoint()](../../d9/dad/classSketcher_1_1SketchObject.html#a8c0707e1362b0b4214aea676a125332c),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[PartDesign::Transformed::getSketchObject()](../../dd/de1/classPartDesign_1_1Transformed.html#a7b52a3658c0f24c04278bc8c1fcc55fd),
[PartDesign::ProfileBased::getSupportFace()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a021db5d3d85698ee0d5a4f8d8a4391a5),
[PartDesign::MultiTransform::getTransformations()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a33b71497cd61478ec6fb8d660b759b6b),
[PartDesign::Scaled::getTransformations()](../../db/dce/classPartDesign_1_1Scaled.html#a114f3de4184f1d8b572ed057609c03d6),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[Gui::DAG::FilterOrigin::goFilter()](../../d5/dff/classGui_1_1DAG_1_1FilterOrigin.html#a52a1c4f0ed387fbd9ed995e99f71818e),
[Gui::DAG::FilterTyped::goFilter()](../../dd/d76/classGui_1_1DAG_1_1FilterTyped.html#a6014b0c63b3c4341c7a94965dbcf39a5),
[Part::Circle::handleChangedPropertyName()](../../de/de4/classPart_1_1Circle.html#aac14a5128cb8850c0cd7f37ffc71e22a),
[Part::Ellipse::handleChangedPropertyName()](../../d6/d22/classPart_1_1Ellipse.html#a7448b87a31bf68edc8d6a6909613615b),
[PartGui::ViewProvider2DObjectGrid::handleChangedPropertyType()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a4c2d97cecf5419da9ce703e47f8c1e6a),
[PartDesign::Fillet::handleChangedPropertyType()](../../d0/d50/classPartDesign_1_1Fillet.html#a4dec9f6780093c637468b21782cc0347),
[PartDesign::Transformed::handleChangedPropertyType()](../../dd/de1/classPartDesign_1_1Transformed.html#a9e4288037e29095bf566a11f3f13fe12),
[Part::Part2DObject::handleChangedPropertyType()](../../d9/d57/classPart_1_1Part2DObject.html#a3b4551d03504c25446ede14dcf2309e3),
[Part::Primitive::handleChangedPropertyType()](../../d2/d31/classPart_1_1Primitive.html#a1e49f13eafbcb2ce0de44916a8407cf7),
[PartDesign::Chamfer::handleChangedPropertyType()](../../da/d6f/classPartDesign_1_1Chamfer.html#a8efe172f26b587a447f0bb5b183ae67b),
[TechDraw::DrawPage::handleChangedPropertyType()](../../d9/d5a/classTechDraw_1_1DrawPage.html#adde1799122996153278b2c68d4fa9b80),
[TechDraw::DrawView::handleChangedPropertyType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a6b6592fb3ddfe6e21aa80f02fb40911e),
[Sketcher::SketchObject::increaseBSplineDegree()](../../d9/dad/classSketcher_1_1SketchObject.html#a3daba3e80990ea7e01b8b4a9bde2217a),
[Sketcher::SketchObject::insertBSplineKnot()](../../d9/dad/classSketcher_1_1SketchObject.html#a48c6d4c74904307c87c4e8f65a9e89af),
[InspectionGui::ViewProviderInspection::inspectCallback()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a4e6895f19ff09d06e34c94fe7df62517),
[InspectionGui::ViewProviderInspection::inspectDistance()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac0352eb6e4af339e08975b253269b0ab),
[SketcherGui::isBsplineKnotOrEndPoint()](../../d6/d44/namespaceSketcherGui.html#a5f794ae2b51c8a757babfa7258a84bee),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[PartDesign::Feature::isDatum()](../../d7/d51/classPartDesign_1_1Feature.html#ae76e0e61b446d25dde1053d691c87081),
[PartDesignGui::isFeatureMovable()](../../dc/d12/namespacePartDesignGui.html#a6b3f9e577dd13e884d8aca2e0ce6a6c8),
[App::Property::isSame()](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d),
[App::PropertyFileIncluded::isSame()](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a048b1c82d308cbef3911301fd596c4ef),
[App::PropertyMatrix::isSame()](../../d8/d77/classApp_1_1PropertyMatrix.html#a28697d5a9c116da22f000f008905c571),
[App::PropertyInteger::isSame()](../../dd/d85/classApp_1_1PropertyInteger.html#a70d2499769026e10fba6bc7a711aebb2),
[App::PropertyPath::isSame()](../../dc/d24/classApp_1_1PropertyPath.html#adcdd24fcfaaf72e0bd6f8b57305186e4),
[App::PropertyEnumeration::isSame()](../../d4/df2/classApp_1_1PropertyEnumeration.html#a516c0ea146e0da67db130812b58f5e49),
[App::PropertyIntegerSet::isSame()](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a5b3dcc5a39a3b54c0450229e4d9f3099),
[App::PropertyMap::isSame()](../../db/d3f/classApp_1_1PropertyMap.html#a232940d7c85e4ebbced00b78426032f4),
[App::PropertyFloat::isSame()](../../d3/dbe/classApp_1_1PropertyFloat.html#a386b26cdbb4e26dfd8e6340d3bb9ca5e),
[App::PropertyString::isSame()](../../dd/df8/classApp_1_1PropertyString.html#a33f0ebb36205838e6f94328870e60ac6),
[App::PropertyUUID::isSame()](../../d2/d6c/classApp_1_1PropertyUUID.html#aa8a6948ef082a962c3c4d1dac7e93dee),
[App::PropertyFont::isSame()](../../df/d8c/classApp_1_1PropertyFont.html#a9bf6ebb41630ff61cecf13cf6436afca),
[App::PropertyBool::isSame()](../../dc/d81/classApp_1_1PropertyBool.html#abd96cbaefa1ebf8b44b844bfc4a60989),
[App::PropertyColor::isSame()](../../d9/d0b/classApp_1_1PropertyColor.html#adeb2113cc4d951709b1cb609cbadc977),
[App::PropertyMaterial::isSame()](../../d0/df5/classApp_1_1PropertyMaterial.html#a363ae57fcaef5cc5de4ead589c5744da),
[App::PropertyQuantity::isSame()](../../d4/d65/classApp_1_1PropertyQuantity.html#a223868a557555d8f3ea7e1eb647af452),
[App::PropertyListsT< T, ListT, ParentT
>::isSame()](../../d1/d0e/classApp_1_1PropertyListsT.html#ab982d594ffdc3d4adb9ea11ec7ba7109),
[App::PropertyVector::isSame()](../../d5/d2b/classApp_1_1PropertyVector.html#a6e4d497b46c90c57f0a6c4f95be4237e),
[App::PropertyPlacement::isSame()](../../da/d51/classApp_1_1PropertyPlacement.html#a3645ce165f801b3aef3bfdda4ada6c83),
[Sketcher::SketchObject::isSupportedGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a2f7ea4092440c2afc10ce26ce6cf5948),
[TechDrawGui::QGIProjGroup::itemChange()](../../db/d20/classTechDrawGui_1_1QGIProjGroup.html#aa1611210aac32505ffac13b3c321ba65),
[SketcherGui::makeTangentToArcOfEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#ade2d18eb05327cda22e2eb86409e4642),
[SketcherGui::makeTangentToArcOfHyperbolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a2d88b81b020ee6003474b180fad75a3b),
[SketcherGui::makeTangentToArcOfParabolaviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a8153db87ad16afe18f0f5e0a01bf5251),
[SketcherGui::makeTangentToEllipseviaNewPoint()](../../d6/d44/namespaceSketcherGui.html#a0221a346db6666022488335587d92562),
[MeshGui::ViewProviderMesh::markPartCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a6eb548accf81ef25b6aa376ac7fa53a8),
[Sketcher::SketchObject::modifyBSplineKnotMultiplicity()](../../d9/dad/classSketcher_1_1SketchObject.html#ae318b60c226c883e53725f9ebef29991),
[SketcherGui::ViewProviderSketch::mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[SketcherGui::DrawSketchHandlerExtend::mouseMove()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#aa7a93c3f3980309d65e4b1ecc9a559d0),
[SketcherGui::ViewProviderSketch::mouseMove()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa),
[Sketcher::SolverGeometryExtension::notifyAttachment()](../../da/db8/classSketcher_1_1SolverGeometryExtension.html#acdfa7733cbaee3f792a8db0dd49aef49),
[Gui::Dialog::DlgMaterialPropertiesImp::on_ambientColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a49825eab8b369a08e23c6e14f3929301),
[Gui::Dialog::DlgMaterialPropertiesImp::on_diffuseColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a9ccc20c9c5d253b5e9ed7fbe4d34f13e),
[Gui::Dialog::DlgMaterialPropertiesImp::on_emissiveColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aa448adcda1877165e407fafcf0354cf3),
[Gui::Dialog::DlgMaterialPropertiesImp::on_shininess_valueChanged()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#af0d5014718205e140eb9e8799167d518),
[Gui::Dialog::DlgMaterialPropertiesImp::on_specularColor_changed()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#a458ce64d9a0930c339444dff48ac809f),
[FemGui::ViewProviderFemPostObject::onChanged()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5d27aeff234b60ec0214c939556b26c5),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[SketcherGui::ViewProviderSketch::onDelete()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a83277547707db7a956f740a550845361),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[App::PropertyPythonObject::Paste()](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a086c7bb8deef61645433e76eeb2fe3b0),
[SketcherGui::DrawSketchHandlerLineSet::pressButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#aeee22456b9d6c86500b37dca09b6bca0),
[Gui::ManualAlignment::probePickedCallback()](../../d7/d97/classGui_1_1ManualAlignment.html#af255c1f31bf62293781d8a04cbecbceb),
[SketcherGui::EditModeConstraintCoinManager::processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[SketcherGui::DrawSketchHandlerLineSet::registerPressedKey()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a032722eff2ff16ed091e0ff7a7b9d6ce),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[SketcherGui::DrawSketchHandlerSplitting::releaseButton()](../../d1/d6f/classSketcherGui_1_1DrawSketchHandlerSplitting.html#a0766956ef48057437eca84c83e1b3521),
[SketcherGui::DrawSketchHandlerTrimming::releaseButton()](../../db/df9/classSketcherGui_1_1DrawSketchHandlerTrimming.html#a19ae638451e1d23b50c23409a6eeded1),
[PartDesignGui::relinkToOrigin()](../../dc/d12/namespacePartDesignGui.html#a04b9ca5c57afc44a5ab6f8bc71f9a681),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[SketcherGui::DrawSketchHandler::seekAutoConstraint()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a618d10641535f24db3b94a9624dd18ce),
[Part::Part2DObject::seekTrimPoints()](../../d9/d57/classPart_1_1Part2DObject.html#a7f5beeba90cfa4cdf7a72f7827bae9f1),
[PartGui::FaceColors::Private::selectionCallback()](../../d4/d4b/classFaceColors_1_1Private.html#a5ff66514ce5125d41dd193313edfdb8e),
[Sandbox::DocumentObjectProtectorPy::setattr()](../../d3/d95/classSandbox_1_1DocumentObjectProtectorPy.html#ac8490e2b3e2c078a8bb27eb6bb608f56),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
[Spreadsheet::Sheet::setFloatProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a082ddc211d51376d6d8c3c77aa4a9bb2),
[Gui::Document::setHide()](../../de/d4e/classGui_1_1Document.html#a210ce66ce252fecbfb7107f60c37429c),
[Spreadsheet::Sheet::setIntegerProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a396a15ce1feb26825369fc32d38c028e),
[App::TransactionObject::setProperty()](../../d9/d02/classApp_1_1TransactionObject.html#ad234dbb98feea5e3fb448aa2b0825207),
[Spreadsheet::Sheet::setQuantityProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1200f02d91cc685af952ac5c7d369010),
[Gui::Document::setShow()](../../de/d4e/classGui_1_1Document.html#ab3f9186bfa28a712509d5fcc077754ef),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[PartGui::ViewProviderSplineExtension::showControlPoints()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a47ebeaa5788d9341eaa389b79acdf55d),
[Gui::Document::slotDeletedObject()](../../de/d4e/classGui_1_1Document.html#a02acfc1218f2666ad7e6b80c804abc99),
[Gui::ManualAlignment::slotDeletedObject()](../../d7/d97/classGui_1_1ManualAlignment.html#a175a5f2e149be360e8a143456cd48ae1),
[Sketcher::SketchObject::split()](../../d9/dad/classSketcher_1_1SketchObject.html#ab73e7a53a704168c004b9aa6c9ad7a68),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[Gui::TaskView::TaskSelectLinkProperty::TaskSelectLinkProperty()](../../d3/d1b/classGui_1_1TaskView_1_1TaskSelectLinkProperty.html#a6ec8c7b8e4d45bde4f8ce5968bdd91b4),
[Gui::SelectionFilter::test()](../../d3/de7/classGui_1_1SelectionFilter.html#a5e11b2a1c8e404cf6236ee475fe5e0dc),
[Gui::PropertyEditor::PropertyMatrixItem::toolTip()](../../d6/d20/classGui_1_1PropertyEditor_1_1PropertyMatrixItem.html#a0d3887efda4155ea320aba09ee6af779),
[Gui::PropertyEditor::PropertyRotationItem::toolTip()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#abbb3c671e82d0c8d54f1f6f2b95abe5d),
[Gui::PropertyEditor::PropertyPlacementItem::toolTip()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#add11217c79e909fa0d6a5fa97d739d2f),
[Gui::PropertyEditor::PropertyMaterialItem::toolTip()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#a493166d2591c115bc095c5866bd5e4a0),
[Gui::PropertyEditor::PropertyMaterialListItem::toolTip()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a420082fd5b1643a150fb0650377990cc),
[Sketcher::SketchObject::transferFilletConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#a618d3720b583b93238a18fec74007377),
[Sketcher::SketchObject::trim()](../../d9/dad/classSketcher_1_1SketchObject.html#a55c244742ef90c7bc339e6c0285e2027),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[Gui::ViewProviderAnnotation::updateData()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#acaee4ade8605ecc0ce997f273a931986),
[Gui::ViewProviderAnnotationLabel::updateData()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#aa2e79cd63adfc0a43501b66ffa4438dd),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[DrawingGui::ViewProviderDrawingPage::updateData()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[MeshGui::ViewProviderMesh::updateData()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#acfabc68fbd4cb6188071e498739066d8),
[MeshGui::ViewProviderIndexedFaceSet::updateData()](../../d8/d12/classMeshGui_1_1ViewProviderIndexedFaceSet.html#a18d4f21152ed2f96bfcec096aa0e639c),
[MeshGui::ViewProviderMeshObject::updateData()](../../db/d49/classMeshGui_1_1ViewProviderMeshObject.html#ab567af502db9d5a8e0beba2181fb39b3),
[MeshGui::ViewProviderMeshCurvature::updateData()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033),
[MeshGui::ViewProviderMeshFaceSet::updateData()](../../df/de9/classMeshGui_1_1ViewProviderMeshFaceSet.html#a1a79e8c47f1e048e3027f7908856d85f),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
[PartGui::ViewProviderBoolean::updateData()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderMultiFuse::updateData()](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a2dd30d90dd627899aae55dd7f6082bfd),
[PartGui::ViewProviderMultiCommon::updateData()](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#afd2565caa649c9122a8da1bad7217b88),
[PartGui::ViewProviderCompound::updateData()](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a864f55403bd4a3b5a81834205fe9561d),
[PartGui::ViewProviderCurveNet::updateData()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#ac10fc8ddaf0e0f8b4fed8ed9f957073a),
[PartGui::ViewProviderFillet::updateData()](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a681e5f4afcfbf90240da46de01068325),
[PartGui::ViewProviderChamfer::updateData()](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
[PartGui::ViewProviderCustom::updateData()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[PartGui::ViewProviderRuledSurface::updateData()](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#af8ea975ad249bc60db35caf151b9908b),
[PathGui::ViewProviderArea::updateData()](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a33f43f1d72596152fa4d6944b59360b0),
[PathGui::ViewProviderAreaView::updateData()](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a5681f9ff35ad2a07e43b5847ebe09f15),
[PathGui::ViewProviderPathShape::updateData()](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ac696ef550f0e27b0665de391ca5891a9),
[PointsGui::ViewProviderScattered::updateData()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab2bc3db5bc92357f983d5c88d287df35),
[PointsGui::ViewProviderStructured::updateData()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#afdfd3564ae817f52b13b4ba6f6e093e8),
[SketcherGui::ViewProviderCustom::updateData()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[PartDesignGui::ViewProvider::updateData()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae230b789ddc5d513656f4e87964bd01e),
[SketcherGui::DrawSketchHandlerLineSet::updateTransitionData()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a87c661c6611a6c685accb1c089fdeba8),
[Sketcher::SketchObject::validateExternalLinks()](../../d9/dad/classSketcher_1_1SketchObject.html#aeb60483adfd2364036d7264a10392ee9),
[Gui::PropertyEditor::PropertyStringItem::value()](../../dd/d22/classGui_1_1PropertyEditor_1_1PropertyStringItem.html#af7d6ebf7226ead072d520b62051d77ed),
[Gui::PropertyEditor::PropertyFontItem::value()](../../de/df5/classGui_1_1PropertyEditor_1_1PropertyFontItem.html#ad4b2d0d05eea1344b23cf64e5af0bf85),
[Gui::PropertyEditor::PropertyIntegerItem::value()](../../de/d3b/classGui_1_1PropertyEditor_1_1PropertyIntegerItem.html#af8403087a42310e8e396c69ba89b31dc),
[Gui::PropertyEditor::PropertyIntegerConstraintItem::value()](../../d6/d39/classGui_1_1PropertyEditor_1_1PropertyIntegerConstraintItem.html#a2b469055bba9c4ee087df3e587dcf857),
[Gui::PropertyEditor::PropertyFloatItem::value()](../../db/df4/classGui_1_1PropertyEditor_1_1PropertyFloatItem.html#a3504141c979ff4cb5f9ea5cf54a05be9),
[Gui::PropertyEditor::PropertyUnitItem::value()](../../d7/d5d/classGui_1_1PropertyEditor_1_1PropertyUnitItem.html#a77537bbfa6f70779bae14ec0c8af8ce7),
[Gui::PropertyEditor::PropertyFloatConstraintItem::value()](../../d2/d0a/classGui_1_1PropertyEditor_1_1PropertyFloatConstraintItem.html#acbaae4a3b13384b2e824bc1162c4c668),
[Gui::PropertyEditor::PropertyBoolItem::value()](../../d4/dc0/classGui_1_1PropertyEditor_1_1PropertyBoolItem.html#a656033aba09820501b40c49cfd240a45),
[Gui::PropertyEditor::PropertyVectorItem::value()](../../dc/d86/classGui_1_1PropertyEditor_1_1PropertyVectorItem.html#a5856c2d9815846f5c63baf8785c77e0e),
[Gui::PropertyEditor::PropertyVectorListItem::value()](../../dc/d19/classGui_1_1PropertyEditor_1_1PropertyVectorListItem.html#a8043a12f10c28a8bf2ef6ba93a7812cb),
[Gui::PropertyEditor::PropertyVectorDistanceItem::value()](../../db/dd4/classGui_1_1PropertyEditor_1_1PropertyVectorDistanceItem.html#a022f31e7063dd604bec6e771a36d0c96),
[Gui::PropertyEditor::PropertyMatrixItem::value()](../../d6/d20/classGui_1_1PropertyEditor_1_1PropertyMatrixItem.html#afcae29df2122fd2d492f14d7bfc3f781),
[Gui::PropertyEditor::PropertyRotationItem::value()](../../dc/d4b/classGui_1_1PropertyEditor_1_1PropertyRotationItem.html#a863981824fc5e2a970540f4e707913d1),
[Gui::PropertyEditor::PropertyPlacementItem::value()](../../d2/dbb/classGui_1_1PropertyEditor_1_1PropertyPlacementItem.html#a02b71a4429874d510e780c4a2375a1be),
[Gui::PropertyEditor::PropertyEnumItem::value()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a94427cf59c1c81076fda89e8f9f0dd7f),
[Gui::PropertyEditor::PropertyStringListItem::value()](../../d7/d2f/classGui_1_1PropertyEditor_1_1PropertyStringListItem.html#ac7e887e41792012af96be518db34a533),
[Gui::PropertyEditor::PropertyFloatListItem::value()](../../de/d74/classGui_1_1PropertyEditor_1_1PropertyFloatListItem.html#a36c1a4829509db372d7f393525345529),
[Gui::PropertyEditor::PropertyIntegerListItem::value()](../../d4/d5f/classGui_1_1PropertyEditor_1_1PropertyIntegerListItem.html#a579b1460c152751041d4d9bdede76c69),
[Gui::PropertyEditor::PropertyColorItem::value()](../../d9/d81/classGui_1_1PropertyEditor_1_1PropertyColorItem.html#acf049af57cd349ad168116b0e0ab7e26),
[Gui::PropertyEditor::PropertyMaterialItem::value()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#acdc82f103ed6664a083e9fa11532c4cc),
[Gui::PropertyEditor::PropertyMaterialListItem::value()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a7440116fc91a842840573c86ddbee0ab),
[Gui::PropertyEditor::PropertyFileItem::value()](../../d3/d1f/classGui_1_1PropertyEditor_1_1PropertyFileItem.html#a803bcb00934c3d895af5520cfea041f1),
[Gui::PropertyEditor::PropertyPathItem::value()](../../de/d04/classGui_1_1PropertyEditor_1_1PropertyPathItem.html#a78946d13ccf37898411e45d4d9730537),
[Gui::PropertyEditor::PropertyTransientFileItem::value()](../../de/d80/classGui_1_1PropertyEditor_1_1PropertyTransientFileItem.html#a7ec4af498f59a81de2414fdaced5669f),
[SketcherGui::PropertyConstraintListItem::value()](../../dd/d04/classSketcherGui_1_1PropertyConstraintListItem.html#afbd28ea5bf2d11eedc5c916575b9a5a1),
and
[MeshPartGui::CurveOnMeshHandler::Private::vertexCallback()](../../d2/d9f/classCurveOnMeshHandler_1_1Private.html#a373137b450a6003db4057cc546930264).

## ◆ init()

| void Base::Persistence::init  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::Application::initTypes()](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
[Gui::Application::initTypes()](../../d9/da8/classGui_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1),
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
and
[MeshGui::ViewProviderMeshCurvature::updateData()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033).

## ◆ Restore()

| void Persistence::Restore  | ( | [XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
pure virtual  
  
This method is used to restore properties from an XML document.

It uses the [XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The XML
reader class This is an important helper class for the store and retrieval
system of objects ...") class, which bases on SAX, to read the in
[Save()](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436
"This method is used to save properties to an XML document.") written
information. Again the Vector as an example:

void
PropertyVector::Restore([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html
"The XML reader class This is an important helper class for the store and
retrieval system of objects ...") &reader)

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

Implemented in
[Fem::FemMesh](../../d3/d2e/classFem_1_1FemMesh.html#a814209824262c9cd4f14ddf22b9cf4cf),
[Part::Geometry](../../dc/df0/classPart_1_1Geometry.html#a1aae6b35e6fba2cbf794c5391847c77b),
[Part::GeomPoint](../../d2/dfb/classPart_1_1GeomPoint.html#aff8fe01b1e05f053db6ac2f10a2744ef),
[Part::GeomBezierCurve](../../d5/d40/classPart_1_1GeomBezierCurve.html#a8bcb644e2aedde67cdb66f7aaa3776e1),
[Part::GeomBSplineCurve](../../df/dfe/classPart_1_1GeomBSplineCurve.html#a4729db2206213978ad19f3f242179483),
[Part::GeomTrimmedCurve](../../df/d24/classPart_1_1GeomTrimmedCurve.html#aef28e629afa1786d54777197cad172b8),
[Part::GeomCircle](../../d0/dde/classPart_1_1GeomCircle.html#af4b7a3f5d7dbd10ae63207445d2774dc),
[Part::GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html#ac4ac7f8e5d9ce8abf685102ea1414d33),
[Part::GeomEllipse](../../db/d52/classPart_1_1GeomEllipse.html#a6c8493d4d7ea506331d9908e3e5e3258),
[Part::GeomArcOfEllipse](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a2e373a4343b69f760be7dbe82d1bc3ff),
[Part::GeomHyperbola](../../d7/d9e/classPart_1_1GeomHyperbola.html#ad47231b8c5d06074ff90da802cd3a913),
[Part::GeomArcOfHyperbola](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#a821f3cf6340c7b5ea26587b92f3ace14),
[Part::GeomParabola](../../d9/ddf/classPart_1_1GeomParabola.html#a4576d65d095cc16b53b327ff0d547b32),
[Part::GeomArcOfParabola](../../db/ddc/classPart_1_1GeomArcOfParabola.html#ad3651d13c1cfc433252921965b8cbb6c),
[Part::GeomLine](../../d5/d30/classPart_1_1GeomLine.html#a5a0b0e4fafe02652e8199e1ea0404fc1),
[Part::GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html#aa9c977ad83ada922a774ef226d9b092d),
[Part::GeomOffsetCurve](../../d0/d36/classPart_1_1GeomOffsetCurve.html#a3e930cfd1c7662dbc19af305ce607603),
[Part::GeomBezierSurface](../../df/dab/classPart_1_1GeomBezierSurface.html#aefca76e368cf44a3f23a6477c7e7922f),
[Part::GeomBSplineSurface](../../d1/d27/classPart_1_1GeomBSplineSurface.html#a045c4377631fa43df87fa9a2185b7adc),
[Part::GeomCylinder](../../de/dc7/classPart_1_1GeomCylinder.html#a4d2bfef3240f16fcbeec4686d4d73c56),
[Part::GeomCone](../../d0/d7c/classPart_1_1GeomCone.html#a42d22469133879127a94bb187bddae99),
[Part::GeomSphere](../../dc/da5/classPart_1_1GeomSphere.html#a6bdb88e79bac011c843140d00870f42d),
[Part::GeomToroid](../../da/d8f/classPart_1_1GeomToroid.html#a6b0245eac6051d70633c59cbc6a0eeb3),
[Part::GeomPlane](../../d2/d0e/classPart_1_1GeomPlane.html#a524ce5530903654c34cce65009b04173),
[Part::GeomOffsetSurface](../../dc/d14/classPart_1_1GeomOffsetSurface.html#a67925ea7598463c174e7726b8ca2194a),
[Part::GeomPlateSurface](../../d7/db9/classPart_1_1GeomPlateSurface.html#af2f8fc282d1187b1196fd49f335e9eef),
[Part::GeomTrimmedSurface](../../de/dd0/classPart_1_1GeomTrimmedSurface.html#a3074600c5e404407785574ddfb223bbc),
[Part::GeomSurfaceOfRevolution](../../df/dc7/classPart_1_1GeomSurfaceOfRevolution.html#a3e60856cb926f2303123fd039692cc0f),
[Part::GeomSurfaceOfExtrusion](../../de/dd5/classPart_1_1GeomSurfaceOfExtrusion.html#a2b319c7e564b1d4489feabaab5ee1bfe),
[Part::Geometry2d](../../d1/dad/classPart_1_1Geometry2d.html#a2c9e74c3b9941fd5b21e6f63c40ac98b),
[Part::Geom2dPoint](../../d8/da9/classPart_1_1Geom2dPoint.html#ae3ae1851f3f8caa3f5ce8739a0a2072e),
[Part::Geom2dBezierCurve](../../d6/d50/classPart_1_1Geom2dBezierCurve.html#aac1effe93178163f5ad0b051dfd053bd),
[Part::Geom2dBSplineCurve](../../dd/d59/classPart_1_1Geom2dBSplineCurve.html#a1dd4f45099d0d956c285a48f49b92453),
[Part::Geom2dCircle](../../d7/d4e/classPart_1_1Geom2dCircle.html#a935cf4d824a7bbb8fc7c4bab51fc0a47),
[Part::Geom2dArcOfCircle](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a2c6839555697c101a94c6600064478a9),
[Part::Geom2dEllipse](../../db/db9/classPart_1_1Geom2dEllipse.html#a69dd5ee48eef1e3d07a3cde17b5213d2),
[Part::Geom2dArcOfEllipse](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a3cca7e273f244ed9299a47c70afa019c),
[Part::Geom2dHyperbola](../../d2/d95/classPart_1_1Geom2dHyperbola.html#a9aa82ebdcae679d490e28f69d8e8b15d),
[Part::Geom2dArcOfHyperbola](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#ae257d16f6106902cd4be1ded2afb12d3),
[Part::Geom2dParabola](../../d9/dff/classPart_1_1Geom2dParabola.html#ac27ce7869ff49efc95f21fb60024f621),
[Part::Geom2dArcOfParabola](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a54034881b3b953385eb987068c7878ac),
[Part::Geom2dLine](../../d2/d27/classPart_1_1Geom2dLine.html#a988cde451fc932b650e4dd3d5cc4591a),
[Part::Geom2dLineSegment](../../df/ded/classPart_1_1Geom2dLineSegment.html#a7d8d4ba2ddea88d8135befdb47b28289),
[Part::Geom2dOffsetCurve](../../d5/de5/classPart_1_1Geom2dOffsetCurve.html#aa26e9c3c981edee0c02ee9387be49d37),
[Part::Geom2dTrimmedCurve](../../d8/da3/classPart_1_1Geom2dTrimmedCurve.html#a46a3b7b759d3a660b3de3dead5f86031),
[Path::Command](../../d7/d2e/classPath_1_1Command.html#a6ff90cf3809d3bdb0390e8ca33cbbef3),
[Path::Toolpath](../../d6/d0c/classPath_1_1Toolpath.html#a5ffa4b9600118d7689e0d485b63d4afa),
[Path::Tool](../../dd/dfe/classPath_1_1Tool.html#afe9d6f36b22e02eaf7f99b584c455b39),
[Path::Tooltable](../../df/dca/classPath_1_1Tooltable.html#aa6832676e89f0215973ccbe0a6cd6ffb),
[Robot::Robot6Axis](../../dc/d5f/classRobot_1_1Robot6Axis.html#a6e0075555eff89970979c568369365af),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[Robot::Trajectory](../../d7/d14/classRobot_1_1Trajectory.html#a0294c37886cce33476159b3e9bd3102e),
[Robot::Waypoint](../../d1/dc7/classRobot_1_1Waypoint.html#a922b6bfba5cd598e35388754d587bb10),
[Sketcher::Sketch](../../d9/d9b/classSketcher_1_1Sketch.html#a290e7e1205108cd218025cca17561860),
[TechDraw::CosmeticVertex](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a11aa1f69e9211c240d61949a237056a1),
[TechDraw::CosmeticEdge](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
[TechDraw::GeomFormat](../../d7/d64/classTechDraw_1_1GeomFormat.html#ac64bf6edf61062cc6acaf193cdba1864),
[Gui::DocumentItem](../../df/d15/classGui_1_1DocumentItem.html#a0b9ab7578bf8cee38467ad7a45983367),
[Sketcher::Constraint](../../d6/def/classSketcher_1_1Constraint.html#a030951705bba6aa6323885f998e5c8b7),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a2e81a7dc633df4672dac82d4e8e1792a),
[App::MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#a42b6e5f8e2e91b8be37bb5c1e89a331f),
[Gui::MergeDocuments](../../d5/d20/classGui_1_1MergeDocuments.html#a42b6e5f8e2e91b8be37bb5c1e89a331f),
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a476ae4b35c3a21c78336ed0877de0ebd),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#ac341d4242623336eafaf73bd16dfe8ad),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a7c4c1053b780d2f149cc99c86d3e39ff),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a172043a2979b6d97bc1f79cf82fdfb02),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a85f27002715e3073a38a20a8f5c2859c),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#a2326110666959447c4218d46d2d30dd7),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a9362c746cddf00578f7c2772133b2419),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#aa6d8ab192c6855fe5506b10e458460cf),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#abc5f8aca58c0b128522e490fa4f87ce1),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#afec516dbf82dbaa0fbc6ad5c96a0708f),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a198b7cda570cfdad094c8886cd995778),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#a4e375cae7bed77bacf0a6dd30794212e),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a9f1511c5fd99820c649307361c6c8880),
[App::Transaction](../../de/dbf/classApp_1_1Transaction.html#aa36b93a360af29f8d5d225cc0fc13422),
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#abfde1f093dc2aed8ca598fecdedb6a7c),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[Gui::Document](../../de/d4e/classGui_1_1Document.html#a2dd4824fb42f9df790ad9f2ea345e5ab),
[Gui::Thumbnail](../../d3/d4d/classGui_1_1Thumbnail.html#a79fc87f3a5a812a9184e83f2a27557f1),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#a4e6bcf20d9aa065b34edc83e9619ba51),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a92213066095ff3edf5189f0038d3dde7),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#ab855a7ff4e993051613fb38b4f5e5e11),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a3499fd97bd4023a5b3628a13742fd138),
[Mesh::MeshObject](../../d8/dcc/classMesh_1_1MeshObject.html#aaba1c40b1d156a541a3f119d0908a235),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#ae5fd1c096fb6b3a70935261847e70115),
[Part::Box](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#a31f09d03f0ee6b6f7a9e98b20b7223d4),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#a90f7d460c9b3b2d2cf7b07282ad83efd),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#a360fb6f1427d3281758a96fc1d88426d),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a3e01a3548f94138d0aad884954e85dad),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a9cf7e3f42e8bfb7058df567bf34a42fb),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#ab0f152b8576922a623c621bac56010a5),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#a55ed2a5aeabe64ead44560c8be45ccbd),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#af020d668456d6c40964757726bb9d1aa),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#a0daddf322de5233314e8ec1e5d73f658),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#ab91b894b378df78eb983a34f62c5cc46),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#ada1c34ac1dc39bd284a23e440d663312),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a911a7f2f77e2adb2277a344a4ffb33f2),
[PartDesign::Transformed](../../dd/de1/classPartDesign_1_1Transformed.html#a4e823053076cbcb1c6a8add13d191405),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#a1d537921c7d5b1a621646b5d8d90e385),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#afbf260ea9285a4c64d5eacca685ebf2b),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#ab2656f675dd437d7057ca54436e67524),
[Points::PointKernel](../../dc/de1/classPoints_1_1PointKernel.html#af4c6a89cb77c9799928d858ddcaad09c),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#af3c51f0c54d5a9ec82ef35950ce21d83),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a32a4eaf9dacfd7e3054863b81b4f3e04),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a2a9a94fc9ab5fb708987621f32d5e02d),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a2dac7950d3d008d99f0f51f58afed622),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a4e72a35a1ea913ffee981734df7e500f),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#a69d288c2ccef5cb0448c33cb4c5290a0),
[Spreadsheet::PropertyColumnWidths](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a3e5f54a360a79e8a1ada41e549fdb51f),
[Spreadsheet::PropertyRowHeights](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a63938d46c9385cca14d404ffa9ccbb74),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a8daf05e49d6c90ebd1bd43a1706cccc2),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a58e90efb8e812efcc17e545683479bce),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a57e55e349c6e686b5cda7b0b94e16cf0),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9a07c6baffee23cf54bfb8d74db35807),
[App::Document](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a64ee9a1ab4beeb4a98fd0c80227703ea),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#a585fd1033be79f3fd3ebd0ae6fe8f734),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a92707872de5970bad0cce842e8644fd8),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#af641d12c42fa3ed2076e9d3f234ef31c),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a1a047c1c95612cfc2e4ca4a91491d995),
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#aae0652a9de7572ada2cdb818c54e29ef),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a602bb1a4bae4daee9223f26201d96795),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#a63237fa5b3eaf0a6fc3a051d5a6e9bcf),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#ab04174271d33c19c037c99c930e25a7e),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#af8af562580107a8bcd34a2e88b650a73),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a8ea57c6a941944daa32ea5ab471b8877),
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#a13c0f90fcb93033f1114904553aaee4c),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#a24712341d8edfa206b25b21bdda998a2),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ad739d09a91f363ecaac5bce84d2271f7),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#aa7e36b44d9a038c47691655463d2eaf4),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#aa6e11dd2fcd1f2307c14e3df94e4fbe7),
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5682de0cd8471dd97ec68393abec332a),
and
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#afb1057b5d67039082147ba14225f1c82).

Referenced by
[restoreFromStream()](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd).

## ◆ RestoreDocFile()

| void Persistence::RestoreDocFile  | ( | [Reader](../../d1/d1f/classBase_1_1Reader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45
"This method is used to save large amounts of data to a binary file.") saved
data.

Again you have to apply for the call of this method in the
[Restore()](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc
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
[RestoreDocFile()](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b
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

Reimplemented in
[App::MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967),
[Gui::MergeDocuments](../../d5/d20/classGui_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967),
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#abaa879168b2300ffb4fdb20d3fdd4ef0),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#af97b03d68515ca8bde89d895a1a6b08b),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[Gui::Document](../../de/d4e/classGui_1_1Document.html#ac4b89a171b3259b15facb5b1b85b0d09),
[Gui::Thumbnail](../../d3/d4d/classGui_1_1Thumbnail.html#a4c4513ac7061eae5f00b6614511d173a),
[Fem::FemMesh](../../d3/d2e/classFem_1_1FemMesh.html#a0d087a665305a95b22c0b16b751cd5b1),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a57a423cdaccbe74d791cc980d9a9fd1a),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ac8dce4be630e3453f9953f28263d24f9),
[Mesh::MeshObject](../../d8/dcc/classMesh_1_1MeshObject.html#a7661a4eb1fc996dff4e502590bcc3e5f),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#ae3bf5a98c6bb9d9b6ac38e10d0cfabef),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a32396a81795cdda13c5a888412e9596b),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a5150b28419d76cabc4f473f5daa59313),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a4863dc4e56fd41546d7cae6422435f4f),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a134325fd0d6732f54d661cbc5ef522ea),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a1f915d5dd125eaf19b5e2ba8797da61d),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#a20c3d7db61029d4aa70d41c583574668),
[Path::Toolpath](../../d6/d0c/classPath_1_1Toolpath.html#a9c989ff33ab1fd65262864cc8810731c),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[Points::PointKernel](../../dc/de1/classPoints_1_1PointKernel.html#a2ed163fabbc9fd9699f4abf1963703da),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a3ed357100287e25fe4c86f40c6bbec71),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a64df9235b7a4f3806641bcc16fcfd9ee),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#ae3bf5a98c6bb9d9b6ac38e10d0cfabef),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a32396a81795cdda13c5a888412e9596b),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a52466ad6689e8d30234bf5ec71b35646),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a889f6a81c93feae64c452de8cca4e4f9),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a22b5814f0d97c838f30c9abd1c8db26d),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a3ec9c1ade28cff79be19ad914c63c9aa),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a48a1edd98f727583fd23c99bb503f0ec),
and
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a040633d87f14e88c9deea536d4168e5e).

## ◆ restoreFromStream()

void Persistence::restoreFromStream  | ( | std::istream & | _stream_| ) |   
---|---|---|---|---|---  
  
References
[Base::XMLReader::isValid()](../../dc/d95/classBase_1_1XMLReader.html#a8104be87d837faa87cfc73aeaa6fe7ed),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readFiles()](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16),
and
[Restore()](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc).

## ◆ Save()

| void Persistence::Save  | ( | [Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
pure virtual  
  
This method is used to save properties to an XML document.

A good example you'll find in PropertyStandard.cpp, e.g. the vector:

void PropertyVector::Save ([Writer](../../dd/d4d/classBase_1_1Writer.html "The
Writer class This is an important helper class for the store and retrieval
system of persistent o...") &writer) const

{

writer <<
writer.[ind](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368
"get the current indentation")() << "<PropertyVector valueX=\"" << _cVec.x <<

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

Implemented in
[Fem::FemMesh](../../d3/d2e/classFem_1_1FemMesh.html#ad8e9b3ebd3dec1f3c6716e7e5db4f9ef),
[Part::Geometry](../../dc/df0/classPart_1_1Geometry.html#afdca307efd3460ac12d9d11212e1019e),
[Part::GeomPoint](../../d2/dfb/classPart_1_1GeomPoint.html#a7e8b345036cf110981470940974c9421),
[Part::GeomBezierCurve](../../d5/d40/classPart_1_1GeomBezierCurve.html#ae78b8695ccfc86ed379f8b5b7381054a),
[Part::GeomBSplineCurve](../../df/dfe/classPart_1_1GeomBSplineCurve.html#aca65bd3ef743a053f69ca6a17b750a1d),
[Part::GeomTrimmedCurve](../../df/d24/classPart_1_1GeomTrimmedCurve.html#a75414ee8aab1c3b44afad9b1305ba9d3),
[Part::GeomCircle](../../d0/dde/classPart_1_1GeomCircle.html#a2f7a8a988205a3502995c750c42a1aaf),
[Part::GeomArcOfCircle](../../de/d1f/classPart_1_1GeomArcOfCircle.html#abb7da9e20b87676c9557910696b97349),
[Part::GeomEllipse](../../db/d52/classPart_1_1GeomEllipse.html#ab0790cef5529063209a951021f1f994d),
[Part::GeomArcOfEllipse](../../df/d3f/classPart_1_1GeomArcOfEllipse.html#a72706ed4fdf3b0243d4d72b2db42db85),
[Part::GeomHyperbola](../../d7/d9e/classPart_1_1GeomHyperbola.html#a1d363e31ed931e93b4c0c62b8ae8018e),
[Part::GeomArcOfHyperbola](../../dc/d04/classPart_1_1GeomArcOfHyperbola.html#aab8732d0bd4af614691d908a63c31429),
[Part::GeomParabola](../../d9/ddf/classPart_1_1GeomParabola.html#a70eb5699782809d25fc97d63e9621b82),
[Part::GeomArcOfParabola](../../db/ddc/classPart_1_1GeomArcOfParabola.html#a2cac7fa995e020b7c51049929c5eae65),
[Part::GeomLine](../../d5/d30/classPart_1_1GeomLine.html#a88fd00890c6c4e7729b05c279a64656d),
[Part::GeomLineSegment](../../d9/d6f/classPart_1_1GeomLineSegment.html#acc377c70086de1bfbfd88e523b663529),
[Part::GeomOffsetCurve](../../d0/d36/classPart_1_1GeomOffsetCurve.html#aa88e84dd7acecae6b210810caba02159),
[Part::GeomBezierSurface](../../df/dab/classPart_1_1GeomBezierSurface.html#aafe509808bccee30e632e9b496740140),
[Part::GeomBSplineSurface](../../d1/d27/classPart_1_1GeomBSplineSurface.html#a30b1d429b534cdfea9b0f89282ffb148),
[Part::GeomCylinder](../../de/dc7/classPart_1_1GeomCylinder.html#af9020de92cb4009696c518d155cf3e53),
[Part::GeomCone](../../d0/d7c/classPart_1_1GeomCone.html#abf367fc98e1ed73fb2fa7c39f6b21000),
[Part::GeomSphere](../../dc/da5/classPart_1_1GeomSphere.html#af876587cdb4b901b0484f14a3d3a39fa),
[Part::GeomToroid](../../da/d8f/classPart_1_1GeomToroid.html#ab4d38e060addd1b934f5d868c2ba2f6a),
[Part::GeomPlane](../../d2/d0e/classPart_1_1GeomPlane.html#aa7be424fde22117c13b283885d564a8c),
[Part::GeomOffsetSurface](../../dc/d14/classPart_1_1GeomOffsetSurface.html#a38a3520a1aabe596f88f0acb29ef8ab2),
[Part::GeomPlateSurface](../../d7/db9/classPart_1_1GeomPlateSurface.html#acff008d5d51aea29cb3f94aa1651b2cb),
[Part::GeomTrimmedSurface](../../de/dd0/classPart_1_1GeomTrimmedSurface.html#a1354b4755c5ed741858b33c22dc58870),
[Part::GeomSurfaceOfRevolution](../../df/dc7/classPart_1_1GeomSurfaceOfRevolution.html#ad3912f99d4873bf66b33d58a2db74cf8),
[Part::GeomSurfaceOfExtrusion](../../de/dd5/classPart_1_1GeomSurfaceOfExtrusion.html#a92c66d7905b48a0e973b8f0b92966689),
[Part::Geometry2d](../../d1/dad/classPart_1_1Geometry2d.html#a3f9a78fac18712772f14066719402ae6),
[Part::Geom2dPoint](../../d8/da9/classPart_1_1Geom2dPoint.html#a6cb271d4c4de1c17c078eed91bc53a52),
[Part::Geom2dBezierCurve](../../d6/d50/classPart_1_1Geom2dBezierCurve.html#ae105fa147ec0c7016f5beb26c767a15e),
[Part::Geom2dBSplineCurve](../../dd/d59/classPart_1_1Geom2dBSplineCurve.html#a36be00b4dd65ecc9bb0351bbee1582ff),
[Part::Geom2dCircle](../../d7/d4e/classPart_1_1Geom2dCircle.html#a7c7cdaca3789102fbfdd9ab3aa8fe408),
[Part::Geom2dArcOfCircle](../../de/d96/classPart_1_1Geom2dArcOfCircle.html#a7a2a3066d0fb89137073b6700ab613ce),
[Part::Geom2dEllipse](../../db/db9/classPart_1_1Geom2dEllipse.html#ae7f027bb3905600426bfd2427f766bd9),
[Part::Geom2dArcOfEllipse](../../db/dbd/classPart_1_1Geom2dArcOfEllipse.html#a5b11e14c488d2aa4cf7beed42745f196),
[Part::Geom2dHyperbola](../../d2/d95/classPart_1_1Geom2dHyperbola.html#af5ea41c1bb958c6654b71ddd5d1f9b46),
[Part::Geom2dArcOfHyperbola](../../dc/db7/classPart_1_1Geom2dArcOfHyperbola.html#adedc32e2aed23cac9140c5d9007d1796),
[Part::Geom2dParabola](../../d9/dff/classPart_1_1Geom2dParabola.html#afe579248a312b0b96cdc9df68c84208b),
[Part::Geom2dArcOfParabola](../../d3/d95/classPart_1_1Geom2dArcOfParabola.html#a647166ea11f48f42548738541a21c92f),
[Part::Geom2dLine](../../d2/d27/classPart_1_1Geom2dLine.html#aa897040dd0e644bedf461b572cf3dba0),
[Part::Geom2dLineSegment](../../df/ded/classPart_1_1Geom2dLineSegment.html#af2f3e338722ce52e89ce1624e57e4d31),
[Part::Geom2dOffsetCurve](../../d5/de5/classPart_1_1Geom2dOffsetCurve.html#a24bcf846099f2796ac0f5cb3870e10c1),
[Part::Geom2dTrimmedCurve](../../d8/da3/classPart_1_1Geom2dTrimmedCurve.html#aacb05ea48b705fe55af43c1caa16971d),
[Path::Command](../../d7/d2e/classPath_1_1Command.html#aa1b581f8eaf7d8d238ae8f9cdff9d485),
[Path::Toolpath](../../d6/d0c/classPath_1_1Toolpath.html#a33b041eee4faec233434f7449d2b7cc3),
[Path::Tool](../../dd/dfe/classPath_1_1Tool.html#af460887ae0bff6e585c176ec5fb7d090),
[Path::Tooltable](../../df/dca/classPath_1_1Tooltable.html#a4d341fe1c98f1ebe4c6b06b46f8aa54e),
[Robot::Robot6Axis](../../dc/d5f/classRobot_1_1Robot6Axis.html#a7cf092c9dc75bf16fe3b6a01d9fa03d4),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#ab1443831f8c6492a77f0f9483688c5b6),
[Robot::Trajectory](../../d7/d14/classRobot_1_1Trajectory.html#a4b7ed465fb7575ec163f78c8e3485a3d),
[Robot::Waypoint](../../d1/dc7/classRobot_1_1Waypoint.html#a2d0f51a0e8e89f1148887af8e2eb0537),
[Sketcher::Sketch](../../d9/d9b/classSketcher_1_1Sketch.html#ab9aae747b5e136965661ae51d2f0b949),
[TechDraw::CosmeticVertex](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#aee8e2101aa119ae2dc4750442745264c),
[TechDraw::CosmeticEdge](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a31c75a92b51476f8968d584e6be31d6c),
[TechDraw::CenterLine](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::GeomFormat](../../d7/d64/classTechDraw_1_1GeomFormat.html#a6f418ed280615fd0ad22d9bea8d19070),
[Gui::DocumentItem](../../df/d15/classGui_1_1DocumentItem.html#a39b445578a0bb04a1e70f68910a69472),
[Sketcher::Constraint](../../d6/def/classSketcher_1_1Constraint.html#a88eebfd4c47c91fe0325cfacbd93b5cc),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a914f9773505d35bfd655e97abffb6d7b),
[App::MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c),
[Gui::MergeDocuments](../../d5/d20/classGui_1_1MergeDocuments.html#ac6da80279e7624f6b7c3e7c29772594c),
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#a91d153116cb6f83444cc0a3cac3673a8),
[App::PropertyMatrix](../../d8/d77/classApp_1_1PropertyMatrix.html#a3880b86eb64ba6104ad5fd9ec0d2514f),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a6ef3c19e6ce7cb04aeb9f9c577551e7e),
[App::PropertyInteger](../../dd/d85/classApp_1_1PropertyInteger.html#a0c826cdd034a3b4bda67fb25b37cad70),
[App::PropertyPath](../../dc/d24/classApp_1_1PropertyPath.html#a45c4b988fe3e59cadd90a86d13864c30),
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html#a4cf9cdfd4e14e6901973762b7b47a663),
[App::PropertyIntegerSet](../../d0/df3/classApp_1_1PropertyIntegerSet.html#aac6c3e40141af20243f925cfe96ee552),
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html#a97872819db9f4c70a132c8995df2369a),
[App::PropertyFloat](../../d3/dbe/classApp_1_1PropertyFloat.html#a4d58561153acf13b6eda8b115deb33a7),
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html#a22cfc259b6c352cd5f14b3a400704164),
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html#a10ff7273e6db8ef0a7199d32212cf6a5),
[App::PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html#a8c59652996dcffd9f4a2d503afaccd29),
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html#a0b4dc7c8284cd7511308f8bb55dc56d0),
[App::PropertyMaterial](../../d0/df5/classApp_1_1PropertyMaterial.html#a286a132daf0dd131911a0b20a6a64db5),
[App::Transaction](../../de/dbf/classApp_1_1Transaction.html#aeb77b2f00b307e4ae1f5d64b86172749),
[App::TransactionObject](../../d9/d02/classApp_1_1TransactionObject.html#abc2454a0ce4e5fa73563fc8f0b9ac3fa),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3),
[Gui::Document](../../de/d4e/classGui_1_1Document.html#a17dba40a2ef0e606900ad09fadca20f5),
[Gui::Thumbnail](../../d3/d4d/classGui_1_1Thumbnail.html#afd06c326111670d8cf2d296e094ab0f6),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#a84f115c98f2080496e7f7ef7ad39485f),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a95feddffb556cb077d779dabafe7232b),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a2f3aea08bb628f6a4c47cb757e79afec),
[Mesh::MeshObject](../../d8/dcc/classMesh_1_1MeshObject.html#af2b4b66eb5dce74ae888d7d1203fc831),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#a4a43a02937b4bee415437e54cba3ad5a),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#aaab5a1c8943cf5a2ec331fc97dc14938),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#ab90c789bcc0e243359d66b110d7e5517),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#ad0c70d9cc93f2eadb42130129156664f),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a0e7532f6fa496fb602617495364aed71),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#ad08e3143d01da16a01393a63241c70fd),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#a45c4b988fe3e59cadd90a86d13864c30),
[Path::PropertyTool](../../d4/d51/classPath_1_1PropertyTool.html#a5227af687ffcea7df5c35a65a4750e97),
[Path::PropertyTooltable](../../d4/d86/classPath_1_1PropertyTooltable.html#a8bbf9ba5ac3749f5386c894b6cf5f7e0),
[Points::PointKernel](../../dc/de1/classPoints_1_1PointKernel.html#a2b6a9c3ce6a26f1b0756db4fe67daa91),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a44c4930cc7950e12f25b7d14d5fa906a),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#af4b0a562cf7811bc7979e8de0908c0a4),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ad96fb0d1fea8fd39d2a1867fa3e2e440),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a9526997cfb42eaef5e8a7436da16b558),
[Robot::PropertyTrajectory](../../d9/d1b/classRobot_1_1PropertyTrajectory.html#ace0e75a249101045b5eaf8347bd33a9f),
[Spreadsheet::PropertyColumnWidths](../../da/ddd/classSpreadsheet_1_1PropertyColumnWidths.html#a976f43505863b7470c1eb93726de2d5e),
[Spreadsheet::PropertyRowHeights](../../d4/d0d/classSpreadsheet_1_1PropertyRowHeights.html#a7dbc1225885f9daac0294390384589d6),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a2ca2a9291bf7a7d3a3e4445b27d1e0b0),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#a278a66fea5146613150022462cd5866b),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a76a4d9006162906f7df1bc9544c03f42),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#ab0cfb70b4099f758b0969d3b76176ef5),
[App::Document](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#aceb2a532b12d3ad6806562eb64bfcf06),
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5),
[App::PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e),
[App::PropertyVector](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a5f00ee26daf66ffaa7bc7a6974c71467),
[App::PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html#ae1314101350bc9e76b9d692693c8e9e1),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7e1537af27ac4c78360e5f75699b3a8e),
[App::PropertyRotation](../../df/d76/classApp_1_1PropertyRotation.html#ad9e882ab49bd192e84f62de9a64c62ce),
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html#a89ed9d7172c31abd43b9ce7e99424ed8),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a5615ef760136231d57a938213dd9bd36),
[App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html#a828dfbbf362ee9875da57453517b3358),
[App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a2258fd848ddcac25ab59fba4b2fb6a2e),
[App::PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html#ad3de7956ba5a12cc37891a34c7f187e8),
[App::PropertyXLinkSubList](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a456f78573d34d76300c400382a36960d),
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
[App::PropertyIntegerList](../../d7/daa/classApp_1_1PropertyIntegerList.html#a7205d3bff255da22b44e7737b4f90529),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#ab02594a5872688e133cc4eb300952ed6),
[App::PropertyStringList](../../d8/d55/classApp_1_1PropertyStringList.html#ae923a954a46e42768bec37194a9c69e2),
[App::PropertyBoolList](../../d1/dcf/classApp_1_1PropertyBoolList.html#add6fd55ff90b5b181391621f6fadae36),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a83eefd2fbd347e44e2c0d5e63b1bc2e1),
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a83f1b747fe9b8b41254e244294809f4a),
[App::PropertyPersistentObject](../../d3/d97/classApp_1_1PropertyPersistentObject.html#aaab9b1d794bd67a605f6aef13f00e9f7),
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a0bb1d243847dd000f61a4b326df0b184),
and
[Spreadsheet::PropertySheet](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ac590ae825fd968155d7efb7801ddeb74).

Referenced by
[dumpToStream()](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7),
and
[App::Property::isSame()](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d).

## ◆ SaveDocFile()

| void Persistence::SaveDocFile  | ( | [Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
This method is used to save large amounts of data to a binary file.

Sometimes it makes no sense to write property data as XML. In case the amount
of data is too big or the data type has a more effective way to save itself.
In this cases it is possible to write the data in a separate file inside the
document archive. In case you want do so you have to re-implement
[SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45
"This method is used to save large amounts of data to a binary file."). First,
you have to inform the framework in
[Save()](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436
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
[RestoreDocFile()](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b
"This method is used to restore large amounts of data from a file In this
method you simply stream in ...") method to identify and read the file again.
Later your
[SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45
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

Reimplemented in
[App::MergeDocuments](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b),
[Gui::MergeDocuments](../../d5/d20/classGui_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b),
[App::PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html#aa23e081d9346621336c5c258f40c4a82),
[App::PropertyPythonObject](../../d7/d1d/classApp_1_1PropertyPythonObject.html#a8de29b7c3f897d0fbfb67f705ce18b3a),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[Gui::Document](../../de/d4e/classGui_1_1Document.html#a5ef0b1ad79ca519de9539c9765e8004b),
[Gui::Thumbnail](../../d3/d4d/classGui_1_1Thumbnail.html#a2c08e4f59778bc033417224a3b83028c),
[Fem::FemMesh](../../d3/d2e/classFem_1_1FemMesh.html#a879fc2d7f331b9cb54e05424ecf62d87),
[Fem::PropertyFemMesh](../../db/da7/classFem_1_1PropertyFemMesh.html#ae628234deb8a30a1f543a8f547f37bdb),
[Fem::PropertyPostDataObject](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ac9622ce80183b9e88f97945047eddd5f),
[Mesh::MeshObject](../../d8/dcc/classMesh_1_1MeshObject.html#a78494e86aa3f8ea36c41c7e47f8a7f4d),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#a89d6adfc66489e9ade2a3b4d7e1fb24d),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#a600f4dbb1c74ae80d9404b5d0c1732ff),
[Mesh::PropertyMeshKernel](../../d8/ddb/classMesh_1_1PropertyMeshKernel.html#aa194e6f59eb0c358a42e219ba575f0bd),
[Part::PropertyPartShape](../../d7/d28/classPart_1_1PropertyPartShape.html#a0a5d9ad2a3ed87aa769ab8e36f51d2f2),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#af051dec83cc5d4fed5dfbab5b36a6a39),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#a41c525ac72a07069e44f42c6592e1648),
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html#a8c81378436a7dc1d04e02923f00b9820),
[Path::Toolpath](../../d6/d0c/classPath_1_1Toolpath.html#a453ab7efa508ad9e45653d8a9f681930),
[Path::PropertyPath](../../da/d75/classPath_1_1PropertyPath.html#afd9e66c92e598417c819096bf0a5abb2),
[Points::PointKernel](../../dc/de1/classPoints_1_1PointKernel.html#ac39f327070b864fa326baa75ee453d58),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a6b36b085a220e2645377dc6a60ebd237),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#a89d6adfc66489e9ade2a3b4d7e1fb24d),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#a600f4dbb1c74ae80d9404b5d0c1732ff),
[Points::PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#a9505267c2de28943446e4029cb956e56),
[App::PropertyVectorList](../../d5/d13/classApp_1_1PropertyVectorList.html#a36ef88c4cd85ee0fc26f8f49a8342e12),
[App::PropertyPlacementList](../../d1/d76/classApp_1_1PropertyPlacementList.html#a7a5c65d0ae1925916f9bc4af21bf7172),
[App::PropertyFloatList](../../dc/d40/classApp_1_1PropertyFloatList.html#a824104f367e47aa1dba79edfe6372d57),
[App::PropertyColorList](../../d0/dc7/classApp_1_1PropertyColorList.html#a7e0b4a92693212f1c9f9217e081b5843),
and
[App::PropertyMaterialList](../../d7/dfc/classApp_1_1PropertyMaterialList.html#a5b8b284a9a23e827623d949fcf5c720e).

Referenced by
[Gui::RecoveryRunnable::run()](../../d9/dc2/classGui_1_1RecoveryRunnable.html#a208e97d67c3514ace646442df3a0f30b),
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a),
[Base::FileWriter::writeFiles()](../../df/de4/classBase_1_1FileWriter.html#a617e36a2afd38f0317aa3b6789d48805),
[Gui::RecoveryWriter::writeFiles()](../../d9/d25/classGui_1_1RecoveryWriter.html#a943a1fe17a358266e1e6566c69c91e4c),
and
[Cloud::CloudWriter::writeFiles()](../../d0/d23/classCloud_1_1CloudWriter.html#ae10b7fa9f42a7c2b6cd73c6c9fb33b38).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Persistence.h
  * FreeCAD/src/Base/Persistence.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

