---
url: https://freecad.github.io/SourceDoc/d3/d3a/classApp_1_1Color.html
scraped_at: 2025-09-08T14:53:50.264356
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Color](../../d3/d3a/classApp_1_1Color.html)

[List of all members](../../dc/d60/classApp_1_1Color-members.html) | Public Member Functions | Public Attributes

App::Color Class Reference

[Color](../../d3/d3a/classApp_1_1Color.html "Color class.") class.
[More...](../../d3/d3a/classApp_1_1Color.html#details)

`#include <Material.h>`

##  Public Member Functions  
  
---  
std::string | [asCSSString](../../d3/d3a/classApp_1_1Color.html#a98a00ec5ac514a5741c8462778974070) () const  
std::string | [asHexString](../../d3/d3a/classApp_1_1Color.html#a92d52884341fa9598e385801aeed4376) () const  
| returns color as hex color "#RRGGBB"
[More...](../../d3/d3a/classApp_1_1Color.html#a92d52884341fa9598e385801aeed4376)  
  
template<typename T >  
T | [asValue](../../d3/d3a/classApp_1_1Color.html#ad3262d2482b64370063e865951605594) () const  
| returns a template type e.g.
[More...](../../d3/d3a/classApp_1_1Color.html#ad3262d2482b64370063e865951605594)  
  
|
[Color](../../d3/d3a/classApp_1_1Color.html#ac556a97a9b9bc269748dc42f768c9cb6)
(const [Color](../../d3/d3a/classApp_1_1Color.html) &c)  
| Copy constructor.
[More...](../../d3/d3a/classApp_1_1Color.html#ac556a97a9b9bc269748dc42f768c9cb6)  
  
|
[Color](../../d3/d3a/classApp_1_1Color.html#a1b731d7b9acc684df25b29231f0dcc02)
(float R=0.0, float G=0.0, float B=0.0, float A=0.0)  
| Defines the color as (R,G,B,A) whereas all values are in the range [0,1].
[More...](../../d3/d3a/classApp_1_1Color.html#a1b731d7b9acc684df25b29231f0dcc02)  
  
|
[Color](../../d3/d3a/classApp_1_1Color.html#a7a9b982976264ac5e2bebb36bdc2b067)
(uint32_t rgba)  
| Does basically the same as the constructor above unless that (R,G,B,A) is
encoded as an unsigned int.
[More...](../../d3/d3a/classApp_1_1Color.html#a7a9b982976264ac5e2bebb36bdc2b067)  
  
[bool](../../d9/db9/classbool.html) | [fromHexString](../../d3/d3a/classApp_1_1Color.html#a43ee9379f150aa78144e01a9c19aedd8) (const std::string &hex)  
| gets color from hex color "#RRGGBB"
[More...](../../d3/d3a/classApp_1_1Color.html#a43ee9379f150aa78144e01a9c19aedd8)  
  
uint32_t | [getPackedValue](../../d3/d3a/classApp_1_1Color.html#a38a46423f244f19f0adece1b69a9fd70) () const  
| Returns color as a 32 bit packed unsigned int in the form 0xRRGGBBAA.
[More...](../../d3/d3a/classApp_1_1Color.html#a38a46423f244f19f0adece1b69a9fd70)  
  
[bool](../../d9/db9/classbool.html) | [operator!=](../../d3/d3a/classApp_1_1Color.html#a6af575f17c8962d6387f4cefffb37958) (const [Color](../../d3/d3a/classApp_1_1Color.html) &c) const  
[Color](../../d3/d3a/classApp_1_1Color.html) & | [operator=](../../d3/d3a/classApp_1_1Color.html#a24e0af47c249605022ce109f59e04fff) (const [Color](../../d3/d3a/classApp_1_1Color.html) &c)  
[bool](../../d9/db9/classbool.html) | [operator==](../../d3/d3a/classApp_1_1Color.html#abfcee78108ef38439d75795394e9de44) (const [Color](../../d3/d3a/classApp_1_1Color.html) &c) const  
| Returns true if both colors are equal.
[More...](../../d3/d3a/classApp_1_1Color.html#abfcee78108ef38439d75795394e9de44)  
  
void | [set](../../d3/d3a/classApp_1_1Color.html#a4dc979ff8824e18cdeea9b33c52f9610) (float R, float G, float B, float A=0.0)  
| Defines the color as (R,G,B,A) whereas all values are in the range [0,1].
[More...](../../d3/d3a/classApp_1_1Color.html#a4dc979ff8824e18cdeea9b33c52f9610)  
  
[Color](../../d3/d3a/classApp_1_1Color.html) & | [setPackedValue](../../d3/d3a/classApp_1_1Color.html#a967e60ab823022f2867963ea17f5ac1a) (uint32_t rgba)  
| Sets the color value as a 32 bit combined red/green/blue/alpha value.
[More...](../../d3/d3a/classApp_1_1Color.html#a967e60ab823022f2867963ea17f5ac1a)  
  
template<typename T >  
void | [setValue](../../d3/d3a/classApp_1_1Color.html#a1fb7f896c9a53af564453aa23433be41) (const T &q)  
| creates FC [Color](../../d3/d3a/classApp_1_1Color.html "Color class.") from
template type, e.g.
[More...](../../d3/d3a/classApp_1_1Color.html#a1fb7f896c9a53af564453aa23433be41)  
  
  
##  Public Attributes  
  
---  
float | [a](../../d3/d3a/classApp_1_1Color.html#a6fee1c51422d3526256e50cfacfea28f)  
float | [b](../../d3/d3a/classApp_1_1Color.html#a80db35212156aad08612f92a82d60340)  
float | [g](../../d3/d3a/classApp_1_1Color.html#a95e979ab4c74614e16a24752023b3910)  
float | [r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4)  
| color values, public accessible
[More...](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4)  
  
  
## Detailed Description

[Color](../../d3/d3a/classApp_1_1Color.html "Color class.") class.

## Constructor & Destructor Documentation

## ◆ Color() [1/3]

| App::Color::Color  | ( | float  | _R_ = `0.0`,   
---|---|---|---  
|  | float  | _G_ = `0.0`,   
|  | float  | _B_ = `0.0`,   
|  | float  | _A_ = `0.0`  
| ) | |   
explicit  
  
Defines the color as (R,G,B,A) whereas all values are in the range [0,1].

_A_ defines the transparency.

## ◆ Color() [2/3]

App::Color::Color  | ( | uint32_t  | _rgba_| ) |   
---|---|---|---|---|---  
  
Does basically the same as the constructor above unless that (R,G,B,A) is
encoded as an unsigned int.

## ◆ Color() [3/3]

App::Color::Color  | ( | const [Color](../../d3/d3a/classApp_1_1Color.html) & | _c_| ) |   
---|---|---|---|---|---  
  
Copy constructor.

## Member Function Documentation

## ◆ asCSSString()

std::string App::Color::asCSSString  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[TechDrawGui::QGIViewAnnotation::drawAnnotation()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#a1da6a03b5c446d2593b9dea4492b07b6),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
and
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b).

## ◆ asHexString()

std::string App::Color::asHexString  | ( | | ) |  const  
---|---|---|---|---  
  
returns color as hex color "#RRGGBB"

Referenced by
[PartGui::addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[MeshPart::BrepMesh::create()](../../de/d62/classMeshPart_1_1BrepMesh.html#ad32eda06dc21d116690d1cf98568ade1),
[TechDraw::CosmeticEdge::Save()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a31c75a92b51476f8968d584e6be31d6c),
[TechDraw::CenterLine::Save()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a839727d2157056f5002672e34ab35b3b),
[TechDraw::GeomFormat::Save()](../../d7/d64/classTechDraw_1_1GeomFormat.html#a6f418ed280615fd0ad22d9bea8d19070),
and
[TechDraw::LineFormat::toString()](../../d6/d5f/classTechDraw_1_1LineFormat.html#a9b824059d59a728f047e72cf89f86eac).

## ◆ asValue()

template<typename T >

T App::Color::asValue  | ( | | ) |  const  
---|---|---|---|---  
  
returns a template type e.g.

Qt color equivalent to FC color

Referenced by
[TechDrawGui::PreferencesGui::centerQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a1b2f842f6ea5b16e468f8ba97700a3b9),
[TechDrawGui::PreferencesGui::dimQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a2bf7e4b574b3969e671400c9b5f41711),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[TechDrawGui::QGIViewPart::formatGeomFromCenterLine()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#adbd4867d23f7a088cd0d56869dec896a),
[TechDrawGui::QGIViewPart::formatGeomFromCosmetic()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a50d74c4e077a6b4cddb0cd98f0f1f114),
[TechDrawGui::QGSPage::getBackgroundColor()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a0d838100a744b8e5d9cb709a7d876d5e),
[TechDrawGui::QGVPage::getBackgroundColor()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#ac122949057daa3c4f5ecaea257efc67d),
[TechDrawGui::QGICMark::getCMarkColor()](../../d0/de9/classTechDrawGui_1_1QGICMark.html#a12656505be177e459609f8501cdeef0f),
[TechDrawGui::QGIEdge::getHiddenColor()](../../dd/d6c/classTechDrawGui_1_1QGIEdge.html#ab102e238463840921d3f6e2f73fc815c),
[TechDrawGui::QGIFace::getParameters()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#a554cfb77c3958f6e6a16abb211d731fb),
[TechDrawGui::QGITile::getTileColor()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#afe064c54983e107c72dfb37cb7b0aaf6),
[TechDrawGui::QGTracker::getTrackerColor()](../../da/d66/classTechDrawGui_1_1QGTracker.html#af07805427c57fbf5b0e24e96d04110f2),
[TechDrawGui::PreferencesGui::gridQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a5cb975824e50f811ed55d82636a702e2),
[TechDrawGui::TaskGeomHatch::initUi()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#acfee83bfb4690c933dc1f4149fd4c054),
[TechDrawGui::TaskLineDecor::initUi()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#a58ab677c87cd4089a322fc2bc523b570),
[TechDrawGui::PreferencesGui::leaderQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ad7461c938a2e7be49a922aea7ced4567),
[TechDrawGui::PreferencesGui::normalQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ab5aca62faa3f8c8a3dd7c5403ed45e6e),
[TechDrawGui::QGIViewDimension::prefNormalColor()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a5c66d03c084c654168e059c57e052a19),
[TechDrawGui::PreferencesGui::preselectQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#aaf59d05244650265643b11ff737107d4),
[TechDrawGui::QGIRichAnno::rectPen()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#ae7fb6471633bf71c75461d319aac210f),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[TechDrawGui::PreferencesGui::sectionLineQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ac1139312e983abb9116932ca31a9473e),
[TechDrawGui::PreferencesGui::selectQColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a44c0c8b83c1514f44677274ab13919a1),
[TechDrawGui::TaskHatch::setUiEdit()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#aae6e162e74354c8d160865c07d91d1c5),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskBalloon::TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[TechDrawGui::TaskDimension::TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
and
[Gui::PropertyEditor::PropertyMaterialListItem::toolTip()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a420082fd5b1643a150fb0650377990cc).

## ◆ fromHexString()

[bool](../../d9/db9/classbool.html) App::Color::fromHexString  | ( | const std::string & | _hex_| ) |   
---|---|---|---|---|---  
  
gets color from hex color "#RRGGBB"

Referenced by
[PartGui::addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[MeshGui::ViewProviderMesh::highlightSegments()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aa17a124626e50184e9d881c8fc6a1d40),
[TechDraw::CosmeticEdge::Restore()](../../de/d2d/classTechDraw_1_1CosmeticEdge.html#a393b837a069a0baa76e15088e1fe49a0),
[TechDraw::CenterLine::Restore()](../../d5/dd5/classTechDraw_1_1CenterLine.html#ad12921606b8baba7068f1aba18283455),
and
[TechDraw::GeomFormat::Restore()](../../d7/d64/classTechDraw_1_1GeomFormat.html#ac64bf6edf61062cc6acaf193cdba1864).

## ◆ getPackedValue()

uint32_t App::Color::getPackedValue  | ( | | ) |  const  
---|---|---|---|---  
  
Returns color as a 32 bit packed unsigned int in the form 0xRRGGBBAA.

See also

    [setPackedValue()](../../d3/d3a/classApp_1_1Color.html#a967e60ab823022f2867963ea17f5ac1a "Sets the color value as a 32 bit combined red/green/blue/alpha value."). 

Referenced by
[App::ColorLegend::getPackedColor()](../../d1/d74/classApp_1_1ColorLegend.html#a84e3c65fa2c3e3eeb6be4eae90391524),
[MeshGui::ViewProviderMesh::ViewProviderMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af37ac6ef652848ebec00a71902819d4f),
and
[MeshGui::ViewProviderMeshNode::ViewProviderMeshNode()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a5ad69ea9a0dc1d1d97d616b4e42ce5dd).

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) App::Color::operator!=  | ( | const [Color](../../d3/d3a/classApp_1_1Color.html) & | _c_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=()

[Color](../../d3/d3a/classApp_1_1Color.html) & App::Color::operator=  | ( | const [Color](../../d3/d3a/classApp_1_1Color.html) & | _c_| ) |   
---|---|---|---|---|---  
  
References
[r](../../d3/d3a/classApp_1_1Color.html#ac6aecf7a9aabad5c63b67ef031ec6df4).

## ◆ operator==()

[bool](../../d9/db9/classbool.html) App::Color::operator==  | ( | const [Color](../../d3/d3a/classApp_1_1Color.html) & | _c_| ) |  const  
---|---|---|---|---|---  
  
Returns true if both colors are equal.

Therefore all components must be equal.

## ◆ set()

void App::Color::set  | ( | float  | _R_ ,   
---|---|---|---  
|  | float  | _G_ ,   
|  | float  | _B_ ,   
|  | float  | _A_ = `0.0`  
| ) | |   
  
Defines the color as (R,G,B,A) whereas all values are in the range [0,1].

_A_ defines the transparency, 0 means complete opaque and 1 invisible.

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
and
[PartGui::ViewProviderPartReference::ViewProviderPartReference()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#af78fff593f8cef1f9cc78450928722cd).

## ◆ setPackedValue()

[Color](../../d3/d3a/classApp_1_1Color.html) & App::Color::setPackedValue  | ( | uint32_t  | _rgba_| ) |   
---|---|---|---|---|---  
  
Sets the color value as a 32 bit combined red/green/blue/alpha value.

Each component is 8 bit wide (i.e. from 0x00 to 0xff), and the red value
should be stored leftmost, like this: 0xRRGGBBAA.

See also

    [getPackedValue()](../../d3/d3a/classApp_1_1Color.html#a38a46423f244f19f0adece1b69a9fd70 "Returns color as a 32 bit packed unsigned int in the form 0xRRGGBBAA."). 

Referenced by
[MeshPart::BrepMesh::create()](../../de/d62/classMeshPart_1_1BrepMesh.html#ad32eda06dc21d116690d1cf98568ade1),
[TechDrawGui::PreferencesGui::dimColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a95a094ff75737586e1173090a1a4c8ea),
[Import::ExportOCAF2::ExportOCAF2()](../../d1/d6e/classImport_1_1ExportOCAF2.html#a3b2589d3096f2857273bd28d202bc8c5),
[TechDrawGui::QGSPage::getBackgroundColor()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a0d838100a744b8e5d9cb709a7d876d5e),
[TechDrawGui::QGVPage::getBackgroundColor()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#ac122949057daa3c4f5ecaea257efc67d),
[TechDrawGui::PreferencesGui::gridColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a22bf50d673de79886edae8313ebef8a4),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
[TechDrawGui::PreferencesGui::leaderColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a317d02efc5f1a2fa44ba56ba821e0a8a),
[MeshCore::MeshInput::LoadOBJ()](../../d9/d08/classMeshCore_1_1MeshInput.html#a7799edf1fa4b6fb4e05d8f374e3d8c4d),
[TechDraw::Preferences::normalColor()](../../d6/dde/classTechDraw_1_1Preferences.html#adb6c09529cd68c3282cf99c8a301020e),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[TechDraw::DrawGeomHatch::prefGeomHatchColor()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a40d7be42405ae1d1cd4709fea43e3d2e),
[TechDrawGui::ViewProviderViewPart::prefHighlightColor()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aace0358ec81505b5e3bda84919495805),
[TechDraw::DrawHatch::prefSvgHatchColor()](../../d0/d97/classTechDraw_1_1DrawHatch.html#aeca1a29638d429cb325d49d144c58662),
[TechDraw::Preferences::preselectColor()](../../d6/dde/classTechDraw_1_1Preferences.html#a51bfd9c397346caf1de29c09e62cb902),
[TechDrawGui::PreferencesGui::sectionLineColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#aa8528664be8ce3842047229819c6ab3b),
[TechDraw::Preferences::selectColor()](../../d6/dde/classTechDraw_1_1Preferences.html#a4aa75b1352c633d046ec12ab0929df6a),
[App::PropertyColor::setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
[TechDraw::Preferences::vertexColor()](../../d6/dde/classTechDraw_1_1Preferences.html#acb17c87d06ccdb555bf7a1dc1a0a4372),
[Gui::ViewProviderLink::ViewProviderLink()](../../d6/d59/classGui_1_1ViewProviderLink.html#ac80b32ec9821edd74f1e39d58951773d),
and
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963).

## ◆ setValue()

template<typename T >

void App::Color::setValue  | ( | const T & | _q_| ) |   
---|---|---|---|---|---  
  
creates FC [Color](../../d3/d3a/classApp_1_1Color.html "Color class.") from
template type, e.g.

Qt QColor

Referenced by
[MeshGui::ViewProviderFace::attach()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#ad7b2603bd549bbf7120aa424fc0adf77),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::TaskCenterLine::createCenterLine()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a9fb5dd30626ee43ec4671c9ea2ce150b),
[TechDrawGui::TaskHatch::createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[TechDrawGui::TaskHatch::onColorChanged()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#aa7333435518474c0cc32cfa8cd6d57dc),
[TechDrawGui::TaskLineDecor::onColorChanged()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#a12467cb149db38a08862d2dbf9852e87),
[Gui::PropertyEditor::PropertyColorItem::setValue()](../../d9/d81/classGui_1_1PropertyEditor_1_1PropertyColorItem.html#a67fe14e02fc503ac083076de54148dac),
[Gui::PropertyEditor::PropertyMaterialItem::setValue()](../../da/d17/classGui_1_1PropertyEditor_1_1PropertyMaterialItem.html#ab7ef99ef914ed6d0d59db213d4455808),
[Gui::PropertyEditor::PropertyMaterialListItem::setValue()](../../d9/d3e/classGui_1_1PropertyEditor_1_1PropertyMaterialListItem.html#a02fc8aac174b508719a5630edbf1ba47),
[MeshGui::ViewProviderMeshCurvature::setVertexCurvatureMode()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a5f3a5eba7e4ce16c86b37579a2bc4bc4),
[TechDrawGui::TaskRichAnno::updateAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#adc9c72650392178995bfd8adf6344831),
[TechDrawGui::TaskHatch::updateHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a885b8fcb16ca312a825e37d5f4ee11b4),
[TechDrawGui::TaskLeaderLine::updateLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0797a29d0a4ef849d5643c1ed982acb2),
and
[TechDrawGui::TaskGeomHatch::updateValues()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a12acdd2beb497c2bfd197b8d8234f389).

## Member Data Documentation

## ◆ a

float App::Color::a  
---  
  
Referenced by
[SpreadsheetGui::PropertiesDialog::apply()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a5aa7098c11c9d893cb9b30cd6541939d),
[Import::ExportOCAF2::ExportOCAF2()](../../d1/d6e/classImport_1_1ExportOCAF2.html#a3b2589d3096f2857273bd28d202bc8c5),
[PartGui::ViewProviderPartExt::getElementColors()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a15bdce85211acfec231620d1fea14805),
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartGui::FaceColors::onSelectionChanged()](../../db/d9e/classPartGui_1_1FaceColors.html#a6280483113ee1508b29134ccad6d35b1),
[SpreadsheetGui::PropertiesDialog::PropertiesDialog()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a1a48a3dff37267c81257bf75efc33fdf),
[Gui::ViewProviderLink::setElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3),
[Gui::LinkView::setMaterial()](../../da/d11/classGui_1_1LinkView.html#a3881060944b7eec683ed8898dc53fce0),
[App::PropertyColor::setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
and
[PartDesignGui::ViewProviderDatum::ViewProviderDatum()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#adf0685fe5a17533d5150eee8e625d03a).

## ◆ b

float App::Color::b  
---  
  
Referenced by
[PartGui::addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[App::ColorLegend::addMax()](../../d1/d74/classApp_1_1ColorLegend.html#af001cb74d8bbe5e56f36118a967b77c8),
[App::ColorLegend::addMin()](../../d1/d74/classApp_1_1ColorLegend.html#a94c8640f299f9f38e58c909456d172e2),
[SpreadsheetGui::PropertiesDialog::apply()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a5aa7098c11c9d893cb9b30cd6541939d),
[MeshGui::ViewProviderFace::attach()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#ad7b2603bd549bbf7120aa424fc0adf77),
[App::ColorField::getColor()](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9),
[App::ColorField::interpolate()](../../d8/da6/classApp_1_1ColorField.html#a290f75780235047fb37c172ca5d6304f),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartGui::FaceColors::onSelectionChanged()](../../db/d9e/classPartGui_1_1FaceColors.html#a6280483113ee1508b29134ccad6d35b1),
[SpreadsheetGui::PropertiesDialog::PropertiesDialog()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a1a48a3dff37267c81257bf75efc33fdf),
[Gui::SoFCColorGradient::rebuildGradient()](../../d0/de7/classGui_1_1SoFCColorGradient.html#ac5bcadd79ec610d11c2ad38883e951dd),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[Gui::SoFCColorLegend::setColorLegend()](../../dd/dd5/classGui_1_1SoFCColorLegend.html#a681c3e9072651d653c452b4978a50320),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
[App::PropertyColor::setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643),
[Mod.Test.Menu.MenuCreateCases::tearDown()](../../d7/db4/classMod_1_1Test_1_1Menu_1_1MenuCreateCases.html#a4aea5b6bf92e9b717a904424a3da573c),
and
[Mod.Test.Menu.MenuDeleteCases::tearDown()](../../d2/daa/classMod_1_1Test_1_1Menu_1_1MenuDeleteCases.html#a2f23a05b3cd9e225f1e65327c2bffc1a).

## ◆ g

float App::Color::g  
---  
  
Referenced by
[PartGui::addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[App::ColorLegend::addMax()](../../d1/d74/classApp_1_1ColorLegend.html#af001cb74d8bbe5e56f36118a967b77c8),
[App::ColorLegend::addMin()](../../d1/d74/classApp_1_1ColorLegend.html#a94c8640f299f9f38e58c909456d172e2),
[SpreadsheetGui::PropertiesDialog::apply()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a5aa7098c11c9d893cb9b30cd6541939d),
[MeshGui::ViewProviderFace::attach()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#ad7b2603bd549bbf7120aa424fc0adf77),
[App::ColorField::getColor()](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9),
[App::ColorField::interpolate()](../../d8/da6/classApp_1_1ColorField.html#a290f75780235047fb37c172ca5d6304f),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartGui::FaceColors::onSelectionChanged()](../../db/d9e/classPartGui_1_1FaceColors.html#a6280483113ee1508b29134ccad6d35b1),
[SpreadsheetGui::PropertiesDialog::PropertiesDialog()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a1a48a3dff37267c81257bf75efc33fdf),
[Gui::SoFCColorGradient::rebuildGradient()](../../d0/de7/classGui_1_1SoFCColorGradient.html#ac5bcadd79ec610d11c2ad38883e951dd),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[Gui::SoFCColorLegend::setColorLegend()](../../dd/dd5/classGui_1_1SoFCColorLegend.html#a681c3e9072651d653c452b4978a50320),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
[App::PropertyColor::setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
and
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643).

## ◆ r

float App::Color::r  
---  
  
color values, public accessible

Referenced by
[PartGui::addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[App::ColorLegend::addMax()](../../d1/d74/classApp_1_1ColorLegend.html#af001cb74d8bbe5e56f36118a967b77c8),
[App::ColorLegend::addMin()](../../d1/d74/classApp_1_1ColorLegend.html#a94c8640f299f9f38e58c909456d172e2),
[SpreadsheetGui::PropertiesDialog::apply()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a5aa7098c11c9d893cb9b30cd6541939d),
[MeshGui::ViewProviderFace::attach()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#ad7b2603bd549bbf7120aa424fc0adf77),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[App::ColorField::getColor()](../../d8/da6/classApp_1_1ColorField.html#a61694c18f7bc4929a2dd57baf03da7b9),
[App::ColorField::interpolate()](../../d8/da6/classApp_1_1ColorField.html#a290f75780235047fb37c172ca5d6304f),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[MeshGui::ViewProviderMeshCurvature::onChanged()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[PartGui::ViewProviderPartExt::onChanged()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartGui::FaceColors::onSelectionChanged()](../../db/d9e/classPartGui_1_1FaceColors.html#a6280483113ee1508b29134ccad6d35b1),
[operator=()](../../d3/d3a/classApp_1_1Color.html#a24e0af47c249605022ce109f59e04fff),
[SpreadsheetGui::PropertiesDialog::PropertiesDialog()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a1a48a3dff37267c81257bf75efc33fdf),
[Points::E57Reader::read()](../../d2/dfb/classPoints_1_1E57Reader.html#a7af6bb0bc50ff56c203f0cb0aa04d458),
[Gui::SoFCColorGradient::rebuildGradient()](../../d0/de7/classGui_1_1SoFCColorGradient.html#ac5bcadd79ec610d11c2ad38883e951dd),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveVRML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8fc229d0641d58846478dbcaa077e8db),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[Gui::SoFCColorLegend::setColorLegend()](../../dd/dd5/classGui_1_1SoFCColorLegend.html#a681c3e9072651d653c452b4978a50320),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
[App::PropertyColor::setPyObject()](../../d9/d0b/classApp_1_1PropertyColor.html#a6e633e7e63cde42f29ea066464910433),
and
[Gui::Dialog::DlgMaterialPropertiesImp::setViewProviders()](../../db/d39/classGui_1_1Dialog_1_1DlgMaterialPropertiesImp.html#aee7cb0bd3911e5488fa0868e14e3f643).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/Material.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

