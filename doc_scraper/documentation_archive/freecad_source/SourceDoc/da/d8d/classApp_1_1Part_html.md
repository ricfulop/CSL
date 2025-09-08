---
url: https://freecad.github.io/SourceDoc/da/d8d/classApp_1_1Part.html
scraped_at: 2025-09-08T14:55:22.811742
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Part](../../da/d8d/classApp_1_1Part.html)

[List of all members](../../d6/d55/classApp_1_1Part-members.html) | Public Attributes

App::Part Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all geometric document objects.
[More...](../../da/d8d/classApp_1_1Part.html#details)

`#include <Part.h>`

##  Public Attributes  
  
---  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Type](../../da/d8d/classApp_1_1Part.html#a0a40cb4c87c3b600ff21bbc2073a9b58)  
| type of the part
[More...](../../da/d8d/classApp_1_1Part.html#a0a40cb4c87c3b600ff21bbc2073a9b58)  
  
base properties of all Assembly Items  
These properties correspond mostly to the meta information in the
[App::Document](../../d8/d3e/classApp_1_1Document.html "The document class.")
class  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Id](../../da/d8d/classApp_1_1Part.html#a94d32e4c1a16102c84ba0aa4a639e176)  
| Id e.g. [Part](../../da/d8d/classApp_1_1Part.html "Base class of all
geometric document objects.") number.
[More...](../../da/d8d/classApp_1_1Part.html#a94d32e4c1a16102c84ba0aa4a639e176)  
  
[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html) | [Uid](../../da/d8d/classApp_1_1Part.html#a54af3be5e4810a6b9741e0d5ca557f11)  
| unique identifier of the Item
[More...](../../da/d8d/classApp_1_1Part.html#a54af3be5e4810a6b9741e0d5ca557f11)  
  
[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html) | [Material](../../da/d8d/classApp_1_1Part.html#a6cf28982e882efccb925f1f7a7c1cb06)  
| material descriptions
[More...](../../da/d8d/classApp_1_1Part.html#a6cf28982e882efccb925f1f7a7c1cb06)  
  
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html) | [Meta](../../da/d8d/classApp_1_1Part.html#a2d0ab8206ebcfbc04b50e129a81b9a99)  
| [Meta](../../d9/dcf/namespaceApp_1_1Meta.html) descriptions.
[More...](../../da/d8d/classApp_1_1Part.html#a2d0ab8206ebcfbc04b50e129a81b9a99)  
  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [License](../../da/d8d/classApp_1_1Part.html#af3556b7b0d0f76ac368b7a6de9bcc13a)  
| License string Holds the short license string for the Item, e.g.
[More...](../../da/d8d/classApp_1_1Part.html#af3556b7b0d0f76ac368b7a6de9bcc13a)  
  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [LicenseURL](../../da/d8d/classApp_1_1Part.html#ab9b8248cce4fbcb152e62651005a2513)  
| License description/contract URL.
[More...](../../da/d8d/classApp_1_1Part.html#ab9b8248cce4fbcb152e62651005a2513)  
  
![-](../../closed.png) Public Attributes inherited from
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html)  
[PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html) | [Placement](../../d7/d75/classApp_1_1GeoFeature.html#a1bb7798d3563d653aaae37376e5e4167)  
![-](../../closed.png) Public Attributes inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html) | [ExpressionEngine](../../d2/de4/classApp_1_1DocumentObject.html#a6a7c9440e119a76b45860ff899322c37)  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d)  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Label2](../../d2/de4/classApp_1_1DocumentObject.html#aadf581e717681c14919082d9929e7d04)  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalBeforeChange](../../d2/de4/classApp_1_1DocumentObject.html#aa8c236a305ce17b2c6527ab5b0be63b7)  
| signal before changing a property of this object
[More...](../../d2/de4/classApp_1_1DocumentObject.html#aa8c236a305ce17b2c6527ab5b0be63b7)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d2/de4/classApp_1_1DocumentObject.html#ac1f497bdbffacfdc82b599d8a27d223a)  
| signal on changed property of this object
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ac1f497bdbffacfdc82b599d8a27d223a)  
  
[PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html) | [Visibility](../../d2/de4/classApp_1_1DocumentObject.html#ab0cd9ce0a97b82041fffbcfbf2a62ff8)  
| Allow control visibility status in [App](../../dd/dc2/namespaceApp.html "The
FreeCAD Application layer.") name space.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ab0cd9ce0a97b82041fffbcfbf2a62ff8)  
  
![-](../../closed.png) Public Attributes inherited from
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html)  
[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html) | [Origin](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cb9a227750a0219f781a9e0c2dc4cb7)  
| [Origin](../../d9/d8b/classApp_1_1Origin.html "Base class of all geometric
document objects.") linked to the group.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cb9a227750a0219f781a9e0c2dc4cb7)  
  
![-](../../closed.png) Public Attributes inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
[PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html) | [Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
| Properties.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb)  
  
  
## Visual properties  
  
---  
[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html) | [Color](../../da/d8d/classApp_1_1Part.html#a52904254c8ea6c66fc3d3f9c9af57798)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") color of the Item If the transparency value
is 1.0 the color or the next hierarchy is used.
[More...](../../da/d8d/classApp_1_1Part.html#a52904254c8ea6c66fc3d3f9c9af57798)  
  
| [Part](../../da/d8d/classApp_1_1Part.html#a038ec889e68c1f995f33152164985ea9)
()  
| Constructor.
[More...](../../da/d8d/classApp_1_1Part.html#a038ec889e68c1f995f33152164985ea9)  
  
virtual | [~Part](../../da/d8d/classApp_1_1Part.html#ab2682c6ef15c2c670763f44501f99e9a) ()  
virtual const char * | [getViewProviderName](../../da/d8d/classApp_1_1Part.html#a11fd84ec6cafdffb21365168b44f427a) () const override  
| returns the type name of the ViewProvider
[More...](../../da/d8d/classApp_1_1Part.html#a11fd84ec6cafdffb21365168b44f427a)  
  
virtual void | [handleChangedPropertyType](../../da/d8d/classApp_1_1Part.html#a1ac1cee5e3d630cb4259859238fc9acd) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, [App::Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
|
[PropertyContainer::handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923
"PropertyContainer::handleChangedPropertyType is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of the property container.
[More...](../../da/d8d/classApp_1_1Part.html#a1ac1cee5e3d630cb4259859238fc9acd)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../da/d8d/classApp_1_1Part.html#a8efaf38ed9d96a1207ff4b6bb05955e5) () override  
| getPyObject returns the Python binding object
[More...](../../da/d8d/classApp_1_1Part.html#a8efaf38ed9d96a1207ff4b6bb05955e5)  
  
static [App::Part](../../da/d8d/classApp_1_1Part.html) * | [getPartOfObject](../../da/d8d/classApp_1_1Part.html#a8555c647df9e2ecbc01f958d2ced8224) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) recursive=true)  
| Returns the part which contains this object.
[More...](../../da/d8d/classApp_1_1Part.html#a8555c647df9e2ecbc01f958d2ced8224)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html)  
enum | [ElementNameType](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430) { [Normal](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430a97a46c8f318c64f007d9a0fc40601007) =0 , [Import](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430ace8a8cfbb41817f0c82bd8f5111a7faa) =1 , [Export](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430a718420688b05579eab7ffa9af9da983a) =2 }  
| Specify the type of element name to return when calling
[getElementName()](../../d7/d75/classApp_1_1GeoFeature.html#a13eb06dab99e7fbdd2dee9bb3db1d30d
"Return the new and old style sub-element name.")
[More...](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430)  
  
![-](../../closed.png) Public Types inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
enum | [GSReason](../../d2/de4/classApp_1_1DocumentObject.html#a64b88e0a6bb28c2c6f7a6c43e81e1fcf) { [GS_DEFAULT](../../d2/de4/classApp_1_1DocumentObject.html#a64b88e0a6bb28c2c6f7a6c43e81e1fcfabe083b32e9b2ac3a2d46b8235399f187) , [GS_SELECT](../../d2/de4/classApp_1_1DocumentObject.html#a64b88e0a6bb28c2c6f7a6c43e81e1fcfa901c4c8b27019d7fc77dc6e373f9b7bf) }  
| reason of calling
[getSubObjects()](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0
"Return name reference of all sub-objects.")
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a64b88e0a6bb28c2c6f7a6c43e81e1fcf)  
  
enum | [OutListOption](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0c) { [OutListNoExpression](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0ca783226d3cfa2eafb517b775cf854c20a) = 1 , [OutListNoHidden](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0ca631f928853757f32d5b431dc80297bd0) = 2 , [OutListNoXLinked](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0caffbf55a4a6fc04cd65fad55182961c0f) = 4 }  
| DAG handling This part of the interface deals with viewing the document as a
DAG (directed acyclic graph).
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0c)  
  
![-](../../closed.png) Public Types inherited from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)  
typedef std::map< [Base::Type](../../dc/dee/classBase_1_1Type.html), [App::Extension](../../d8/dc7/classApp_1_1Extension.html) * >::iterator | [ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f)  
![-](../../closed.png) Public Member Functions inherited from
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html)  
|
[GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html#ac8687cd76fe9b1d02e78178f5d7799eb)
(void)  
| Constructor.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#ac8687cd76fe9b1d02e78178f5d7799eb)  
  
virtual std::pair< std::string, std::string > | [getElementName](../../d7/d75/classApp_1_1GeoFeature.html#a13eb06dab99e7fbdd2dee9bb3db1d30d) (const char *name, [ElementNameType](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430) [type](../../d9/d98/classtype.html)=[Normal](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430a97a46c8f318c64f007d9a0fc40601007)) const  
| Return the new and old style sub-element name.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#a13eb06dab99e7fbdd2dee9bb3db1d30d)  
  
virtual const [PropertyComplexGeoData](../../d7/d28/classApp_1_1PropertyComplexGeoData.html) * | [getPropertyOfGeometry](../../d7/d75/classApp_1_1GeoFeature.html#a0973d8c3f2a0ca975f3b6a7eebe34e9a) () const  
| This method returns the main property of a geometric object that holds the
actual geometry.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#a0973d8c3f2a0ca975f3b6a7eebe34e9a)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d7/d75/classApp_1_1GeoFeature.html#a6837f9af91a2619c420f361033ab0da5) (void)  
| getPyObject returns the Python binding object
[More...](../../d7/d75/classApp_1_1GeoFeature.html#a6837f9af91a2619c420f361033ab0da5)  
  
[Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [globalPlacement](../../d7/d75/classApp_1_1GeoFeature.html#a0e704269769e5c10eca911b3e400d0ab) () const  
| Calculates the placement in the global reference coordinate system.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#a0e704269769e5c10eca911b3e400d0ab)  
  
virtual void | [transformPlacement](../../d7/d75/classApp_1_1GeoFeature.html#a584e8f09fca2a336406b878f0450886d) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &transform)  
| transformPlacement applies transform to placement of this shape.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#a584e8f09fca2a336406b878f0450886d)  
  
virtual | [~GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html#ab565a069f55f9e7ab4e3e512f9438325) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [addDynamicProperty](../../d2/de4/classApp_1_1DocumentObject.html#abf2aa7beac95fbed58ef392808477218) (const char *[type](../../d9/d98/classtype.html), const char *name=nullptr, const char *group=nullptr, const char *doc=nullptr, short attr=0, [bool](../../d9/db9/classbool.html) ro=false, [bool](../../d9/db9/classbool.html) hidden=false) override  
virtual [bool](../../d9/db9/classbool.html) | [adjustRelativeLinks](../../d2/de4/classApp_1_1DocumentObject.html#a8934f5cfdbb3db3c7b40f300e6945dee) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList, std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > *visited=nullptr)  
| Called to adjust link properties to avoid cyclic links.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a8934f5cfdbb3db3c7b40f300e6945dee)  
  
virtual [bool](../../d9/db9/classbool.html) | [allowDuplicateLabel](../../d2/de4/classApp_1_1DocumentObject.html#a9bd9006423ae022a34001dcf28a89ac5) () const  
virtual [bool](../../d9/db9/classbool.html) | [canLinkProperties](../../d2/de4/classApp_1_1DocumentObject.html#ad4cc5d01c15b71046b9c594cd5ac137d) () const  
virtual [int](../../d1/da0/classint.html) | [canLoadPartial](../../d2/de4/classApp_1_1DocumentObject.html#a05b6195349bdcde0d66320368db2bef4) () const  
| allow partial loading of dependent objects
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a05b6195349bdcde0d66320368db2bef4)  
  
void | [clearExpression](../../d2/de4/classApp_1_1DocumentObject.html#a43ec3e382c1f463ad26763a83e7f1df2) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path)  
void | [clearOutListCache](../../d2/de4/classApp_1_1DocumentObject.html#aad3fe1f87df22059fef61392f10e1e6d) () const  
| clear internal out list cache
[More...](../../d2/de4/classApp_1_1DocumentObject.html#aad3fe1f87df22059fef61392f10e1e6d)  
  
virtual const char * | [detachFromDocument](../../d2/de4/classApp_1_1DocumentObject.html#a18685d36a70739a43912aef660ae44fe) () override  
|
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a40a23775f8123a04dbe3176fc5c6af3b)
(void)  
| Constructor.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a40a23775f8123a04dbe3176fc5c6af3b)  
  
void | [enforceRecompute](../../d2/de4/classApp_1_1DocumentObject.html#ae0e994d2c952ec540ec284b01e294a04) ()  
| Enforce this document object to be recomputed.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ae0e994d2c952ec540ec284b01e294a04)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2) (void) const  
| gets the document in which this Object is handled
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2)  
  
std::string | [getExportName](../../d2/de4/classApp_1_1DocumentObject.html#abca24f2008297e8e2bb3a849bb3617d2) ([bool](../../d9/db9/classbool.html) forced=false) const  
| returns the name that is safe to be exported to other document
[More...](../../d2/de4/classApp_1_1DocumentObject.html#abca24f2008297e8e2bb3a849bb3617d2)  
  
virtual const [PropertyExpressionEngine::ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) | [getExpression](../../d2/de4/classApp_1_1DocumentObject.html#a971d1bc9991b264e7fab8ff56c38d60a) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
virtual std::string | [getFullName](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62) () const override  
| Return the object full name of the form DocName::ObjName.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62)  
  
[DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html) * | [getGroup](../../d2/de4/classApp_1_1DocumentObject.html#ac04631fa2c3e4e28f7382f77b2b1f4f1) () const  
| get group if object is part of a group, otherwise 0 is returned
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ac04631fa2c3e4e28f7382f77b2b1f4f1)  
  
long | [getID](../../d2/de4/classApp_1_1DocumentObject.html#ab4241c8adbabccc10b99da4118231862) () const  
| Return the object ID that is unique within its owner document.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ab4241c8adbabccc10b99da4118231862)  
  
const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | [getInList](../../d2/de4/classApp_1_1DocumentObject.html#a40180ed535a541b857baead4eece53f5) (void) const  
std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getInListEx](../../d2/de4/classApp_1_1DocumentObject.html#a6783e4a7b522a575401d965785108f3e) ([bool](../../d9/db9/classbool.html) recursive) const  
| Return a set of all objects linking to this object, including possible
external parent objects.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a6783e4a7b522a575401d965785108f3e)  
  
void | [getInListEx](../../d2/de4/classApp_1_1DocumentObject.html#ad99e8f94b3cb435ad9346dd8616a122e) (std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inSet, [bool](../../d9/db9/classbool.html) recursive, std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > *inList=nullptr) const  
| Get a set of all objects linking to this object, including possible external
parent objects.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ad99e8f94b3cb435ad9346dd8616a122e)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getInListRecursive](../../d2/de4/classApp_1_1DocumentObject.html#a8a3180e164bfb4782220b5cec85c1fe2) (void) const  
| get all objects link directly or indirectly to this object
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a8a3180e164bfb4782220b5cec85c1fe2)  
  
virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getLinkedObject](../../d2/de4/classApp_1_1DocumentObject.html#ad7c7fb6359b4d1497b06f869327154a1) ([bool](../../d9/db9/classbool.html) recurse=true, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat=nullptr, [bool](../../d9/db9/classbool.html) transform=false, [int](../../d1/da0/classint.html) depth=0) const  
| Return the linked object with optional transformation.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ad7c7fb6359b4d1497b06f869327154a1)  
  
const char * | [getNameInDocument](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1) (void) const  
| returns the name which is set in the document for this object (not the name
property!)
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1)  
  
const std::string & | [getOldLabel](../../d2/de4/classApp_1_1DocumentObject.html#a29b0a81016ac4e996f432cbea98ed59c) () const  
const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | [getOutList](../../d2/de4/classApp_1_1DocumentObject.html#ab69981229233aa7c2fd32e378d2f2087) () const  
| returns a list of objects this object is pointing to by Links
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ab69981229233aa7c2fd32e378d2f2087)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getOutList](../../d2/de4/classApp_1_1DocumentObject.html#ad793066a9596a4825fbb40abbd53c8da) ([int](../../d1/da0/classint.html) option) const  
void | [getOutList](../../d2/de4/classApp_1_1DocumentObject.html#aa1f519f82b33b4b33627b9c11cac23e5) ([int](../../d1/da0/classint.html) option, std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &res) const  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getOutListOfProperty](../../d2/de4/classApp_1_1DocumentObject.html#abe4feb31e51b7e835c1e4438b5de301d) ([App::Property](../../d0/da9/classApp_1_1Property.html) *) const  
| returns a list of objects linked by the property
[More...](../../d2/de4/classApp_1_1DocumentObject.html#abe4feb31e51b7e835c1e4438b5de301d)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getOutListRecursive](../../d2/de4/classApp_1_1DocumentObject.html#a500dc441419c37e95f70d36c93d68702) (void) const  
| returns a list of objects this object is pointing to by Links and all
further descended
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a500dc441419c37e95f70d36c93d68702)  
  
std::vector< std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::string > > | [getParents](../../d2/de4/classApp_1_1DocumentObject.html#af0ac1af888a8fae951ee28c00a3d2391) ([int](../../d1/da0/classint.html) depth=0) const  
| Obtain top parents and subnames of this object using its InList.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#af0ac1af888a8fae951ee28c00a3d2391)  
  
std::vector< std::list< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > > | [getPathsByOutList](../../d2/de4/classApp_1_1DocumentObject.html#a4492d119e30b8b186458a1187dbd214a) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *to) const  
| get all possible paths from this to another object following the OutList
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a4492d119e30b8b186458a1187dbd214a)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d2/de4/classApp_1_1DocumentObject.html#a1adfcfb2169b5c31374e07346256648f) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a1adfcfb2169b5c31374e07346256648f)  
  
unsigned long | [getStatus](../../d2/de4/classApp_1_1DocumentObject.html#a82c4fed15f5b9e99315caf4e97713f1c) () const  
| return the status bits
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a82c4fed15f5b9e99315caf4e97713f1c)  
  
const char * | [getStatusString](../../d2/de4/classApp_1_1DocumentObject.html#a45265661fa4cf3b6c914d58433901269) (void) const  
| get the status Message
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a45265661fa4cf3b6c914d58433901269)  
  
virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getSubObject](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6) (const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj=nullptr, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat=nullptr, [bool](../../d9/db9/classbool.html) transform=true, [int](../../d1/da0/classint.html) depth=0) const  
| Get the sub element/object by name.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getSubObjectList](../../d2/de4/classApp_1_1DocumentObject.html#a0fbb205b28cb6ddc9fde23eb513500a9) (const char *subname) const  
| Return a list of objects referenced by a given subname including this
object.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a0fbb205b28cb6ddc9fde23eb513500a9)  
  
virtual std::vector< std::string > | [getSubObjects](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0) ([int](../../d1/da0/classint.html) reason=0) const  
| Return name reference of all sub-objects.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0)  
  
virtual const char * | [getViewProviderName](../../d2/de4/classApp_1_1DocumentObject.html#a6a8a0335a6da079225b433b4b291653a) (void) const  
| returns the type name of the ViewProvider
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a6a8a0335a6da079225b433b4b291653a)  
  
virtual const char * | [getViewProviderNameOverride](../../d2/de4/classApp_1_1DocumentObject.html#ad4e5af68230646890aa61c051f7b9966) () const  
| This function is introduced to allow Python feature override its view
provider.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ad4e5af68230646890aa61c051f7b9966)  
  
const char * | [getViewProviderNameStored](../../d2/de4/classApp_1_1DocumentObject.html#a8cfe662473df0510292b4ffd93bd38e0) () const  
virtual [bool](../../d9/db9/classbool.html) | [hasChildElement](../../d2/de4/classApp_1_1DocumentObject.html#a54805cb13103f36e16706bbea568e98c) () const  
| return true to activate tree view group object handling and element
visibility
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a54805cb13103f36e16706bbea568e98c)  
  
virtual [bool](../../d9/db9/classbool.html) | [isAttachedToDocument](../../d2/de4/classApp_1_1DocumentObject.html#af0c800cf501791cc2d47619d6457b978) () const override  
virtual [int](../../d1/da0/classint.html) | [isElementVisible](../../d2/de4/classApp_1_1DocumentObject.html#adaba073ae0d9e6aa00dc123c3ce8e0b5) (const char *element) const  
| Get sub-element visibility.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#adaba073ae0d9e6aa00dc123c3ce8e0b5)  
  
[bool](../../d9/db9/classbool.html) | [isError](../../d2/de4/classApp_1_1DocumentObject.html#a5ccefd3f631c57d8fcd54376c5f7d6a2) (void) const  
| set this feature to error
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a5ccefd3f631c57d8fcd54376c5f7d6a2)  
  
[int](../../d1/da0/classint.html) | [isExporting](../../d2/de4/classApp_1_1DocumentObject.html#a5483904c4a9eb870a64233ac737e4dee) () const  
[bool](../../d9/db9/classbool.html) | [isInInList](../../d2/de4/classApp_1_1DocumentObject.html#a502a8a665b20d4785221354ceb72b577) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *objToTest) const  
| test if this object is directly (non recursive) in the InList
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a502a8a665b20d4785221354ceb72b577)  
  
[bool](../../d9/db9/classbool.html) | [isInInListRecursive](../../d2/de4/classApp_1_1DocumentObject.html#a41f1d53a143d9b3a401dc72d828cd8a0) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *objToTest) const  
| test if this object is in the InList and recursive further down
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a41f1d53a143d9b3a401dc72d828cd8a0)  
  
[bool](../../d9/db9/classbool.html) | [isInOutList](../../d2/de4/classApp_1_1DocumentObject.html#a6aa5c96a7383e55f26e65fc7daf63ee4) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *objToTest) const  
| test if this object is directly (non recursive) in the OutList
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a6aa5c96a7383e55f26e65fc7daf63ee4)  
  
[bool](../../d9/db9/classbool.html) | [isInOutListRecursive](../../d2/de4/classApp_1_1DocumentObject.html#a468da281654bd10226cbab32f1f43256) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *objToTest) const  
| test if the given object is in the OutList and recursive further down
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a468da281654bd10226cbab32f1f43256)  
  
[bool](../../d9/db9/classbool.html) | [isRecomputing](../../d2/de4/classApp_1_1DocumentObject.html#a44f65ddf80ee54811fb68b6407ba7b34) () const  
| returns true if this objects is currently recomputing
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a44f65ddf80ee54811fb68b6407ba7b34)  
  
[bool](../../d9/db9/classbool.html) | [isRemoving](../../d2/de4/classApp_1_1DocumentObject.html#a230a706690bd2effb512c36f81139ec2) () const  
| returns true if this objects is currently removed from the document
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a230a706690bd2effb512c36f81139ec2)  
  
[bool](../../d9/db9/classbool.html) | [isRestoring](../../d2/de4/classApp_1_1DocumentObject.html#ac2d5c9ca4c67cbb6dd7c22a71ce85da0) () const  
| returns true if this objects is currently restoring from file
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ac2d5c9ca4c67cbb6dd7c22a71ce85da0)  
  
[bool](../../d9/db9/classbool.html) | [isTouched](../../d2/de4/classApp_1_1DocumentObject.html#a6cda42dc4ffac025c03f0953cedc32c7) (void) const  
| test if this document object is touched
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a6cda42dc4ffac025c03f0953cedc32c7)  
  
[bool](../../d9/db9/classbool.html) | [isValid](../../d2/de4/classApp_1_1DocumentObject.html#ab12285411684f491cee2519c6e6e99ea) (void) const  
virtual short | [mustExecute](../../d2/de4/classApp_1_1DocumentObject.html#a60bb73bdb98747c0262b13f7c150e663) (void) const  
| mustExecute We call this method to check if the object was modified to be
invoked.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a60bb73bdb98747c0262b13f7c150e663)  
  
[bool](../../d9/db9/classbool.html) | [mustRecompute](../../d2/de4/classApp_1_1DocumentObject.html#a5b7ea3351d9bb47decb443e622fbedc9) (void) const  
| Test if this document object must be recomputed.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a5b7ea3351d9bb47decb443e622fbedc9)  
  
virtual void | [onBeforeChangeLabel](../../d2/de4/classApp_1_1DocumentObject.html#a052c5a2cafaf588780c3d5ec5211d9b3) (std::string &newLabel)  
virtual void | [onLostLinkToObject](../../d2/de4/classApp_1_1DocumentObject.html#ae793896d8cdf95d872dfb45a7a1f291d) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
| Called in case of losing a link Get called by the document when a object got
deleted a link property of this object ist pointing to.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ae793896d8cdf95d872dfb45a7a1f291d)  
  
virtual void | [onUpdateElementReference](../../d2/de4/classApp_1_1DocumentObject.html#a9c5de491fd49f9534bd828fea6d7d3b1) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
void | [purgeError](../../d2/de4/classApp_1_1DocumentObject.html#ab17719ed75dd0d0c75d045975e5b92db) (void)  
| remove the error from the object
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ab17719ed75dd0d0c75d045975e5b92db)  
  
void | [purgeTouched](../../d2/de4/classApp_1_1DocumentObject.html#a47187c23d4b5340a856b0d6eb08bcb5c) (void)  
| reset this document object touched
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a47187c23d4b5340a856b0d6eb08bcb5c)  
  
[bool](../../d9/db9/classbool.html) | [recomputeFeature](../../d2/de4/classApp_1_1DocumentObject.html#ac01c405cd91c69eb63407f3bffa82540) ([bool](../../d9/db9/classbool.html) recursive=false)  
| Recompute only this feature.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ac01c405cd91c69eb63407f3bffa82540)  
  
virtual [bool](../../d9/db9/classbool.html) | [redirectSubName](../../d2/de4/classApp_1_1DocumentObject.html#a5b47268847a70ba8520c2b6a56bd9b94) (std::ostringstream &ss, [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *topParent, [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *child) const  
| Allow object to redirect a subname path.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a5b47268847a70ba8520c2b6a56bd9b94)  
  
virtual [bool](../../d9/db9/classbool.html) | [removeDynamicProperty](../../d2/de4/classApp_1_1DocumentObject.html#a00938d679f9f65e7ee4e9ef02d399c84) (const char *prop) override  
virtual void | [renameObjectIdentifiers](../../d2/de4/classApp_1_1DocumentObject.html#a65f0f9ac48503de7eb000dc20841471a) (const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [resolve](../../d2/de4/classApp_1_1DocumentObject.html#a77d8009a94ca3045f7a4f380ca8b8e4c) (const char *subname, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) **parent=nullptr, std::string *childName=nullptr, const char **subElement=nullptr, [PyObject](../../df/d1b/classPyObject.html) **pyObj=nullptr, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat=nullptr, [bool](../../d9/db9/classbool.html) transform=true, [int](../../d1/da0/classint.html) depth=0) const  
| Resolve the last document object referenced in the subname.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a77d8009a94ca3045f7a4f380ca8b8e4c)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [resolveRelativeLink](../../d2/de4/classApp_1_1DocumentObject.html#ac8e6d9287ff1f6a10f4c3b87e51b89c0) (std::string &subname, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&link, std::string &linkSub) const  
| Resolve a link reference that is relative to this object reference.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ac8e6d9287ff1f6a10f4c3b87e51b89c0)  
  
virtual void | [Save](../../d2/de4/classApp_1_1DocumentObject.html#aceb2a532b12d3ad6806562eb64bfcf06) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#aceb2a532b12d3ad6806562eb64bfcf06)  
  
virtual [int](../../d1/da0/classint.html) | [setElementVisible](../../d2/de4/classApp_1_1DocumentObject.html#aad32b734a723878ba361804e983041a9) (const char *element, [bool](../../d9/db9/classbool.html) visible)  
| Child element handling.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#aad32b734a723878ba361804e983041a9)  
  
virtual void | [setExpression](../../d2/de4/classApp_1_1DocumentObject.html#a5b429556cb1d319a03eefce9c01087cc) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > expr)  
void | [setStatus](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815) ([ObjectStatus](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3a) pos, [bool](../../d9/db9/classbool.html) on)  
[bool](../../d9/db9/classbool.html) | [testIfLinkDAGCompatible](../../d2/de4/classApp_1_1DocumentObject.html#ad220d478c9db2963857548d8a5407cca) ([App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html) &linkTo) const  
[bool](../../d9/db9/classbool.html) | [testIfLinkDAGCompatible](../../d2/de4/classApp_1_1DocumentObject.html#aa41c5e052eaafe9e5e7f871fb4e2addd) ([App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) &linksTo) const  
[bool](../../d9/db9/classbool.html) | [testIfLinkDAGCompatible](../../d2/de4/classApp_1_1DocumentObject.html#ac8822943922cf70e9b921120b7e18dab) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &linksTo) const  
[bool](../../d9/db9/classbool.html) | [testIfLinkDAGCompatible](../../d2/de4/classApp_1_1DocumentObject.html#af6f646f713fff45d493a4d7c55d3059b) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linkTo) const  
| testIfLinkIsDAG tests a link that is about to be created for circular
references.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#af6f646f713fff45d493a4d7c55d3059b)  
  
[bool](../../d9/db9/classbool.html) | [testStatus](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120) ([ObjectStatus](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3a) pos) const  
void | [touch](../../d2/de4/classApp_1_1DocumentObject.html#a8949e65adb1315e37818719a058f4f40) ([bool](../../d9/db9/classbool.html) noRecompute=false)  
| Set the property touched -> changed, cause recomputation in Update()
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a8949e65adb1315e37818719a058f4f40)  
  
virtual | [~DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#afe99e5d61044b9657abf2e8818aa146a) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html)  
virtual const char * | [detachFromDocument](../../d8/d00/classApp_1_1TransactionalObject.html#a17f7538441e315b11eca8ebc047e11f4) ()  
virtual [bool](../../d9/db9/classbool.html) | [isAttachedToDocument](../../d8/d00/classApp_1_1TransactionalObject.html#aa76992a5607128ed5a5a7434cbd857c0) () const  
|
[TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html#af99f0a5b4acf9844a47cbe9a9d626689)
(void)  
| Constructor.
[More...](../../d8/d00/classApp_1_1TransactionalObject.html#af99f0a5b4acf9844a47cbe9a9d626689)  
  
virtual | [~TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html#a995b51d768813d09ffa5620375d304dc) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)  
[ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f) | [extensionBegin](../../d6/d76/classApp_1_1ExtensionContainer.html#ab709bb3d6a2e77fcdf71323659e26fe3) ()  
|
[ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a1576c15e0c5c9c3866a671c81b410670)
()  
[ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f) | [extensionEnd](../../d6/d76/classApp_1_1ExtensionContainer.html#ade70d6e46e548f4a8f8ff9bc2a277f83) ()  
[App::Extension](../../d8/dc7/classApp_1_1Extension.html) * | [getExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a329e85b59ccbc63a619c4d31325f23d8) ([Base::Type](../../dc/dee/classBase_1_1Type.html), [bool](../../d9/db9/classbool.html) derived=true, [bool](../../d9/db9/classbool.html) no_except=false) const  
[App::Extension](../../d8/dc7/classApp_1_1Extension.html) * | [getExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a7ccfc3ce3ac85344e07766d3d7760f50) (const std::string &name) const  
template<typename [ExtensionT](../../df/d73/classExtensionT.html) >  
[ExtensionT](../../df/d73/classExtensionT.html) * | [getExtensionByType](../../d6/d76/classApp_1_1ExtensionContainer.html#a0711e5ec3feeac1afc569569784a4994) ([bool](../../d9/db9/classbool.html) no_except=false, [bool](../../d9/db9/classbool.html) derived=true) const  
std::vector< [Extension](../../d8/dc7/classApp_1_1Extension.html) * > | [getExtensionsDerivedFrom](../../d6/d76/classApp_1_1ExtensionContainer.html#a8b1505a7cdc7d5f2c43e0d3cfaa8100c) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
template<typename [ExtensionT](../../df/d73/classExtensionT.html) >  
std::vector< [ExtensionT](../../df/d73/classExtensionT.html) * > | [getExtensionsDerivedFromType](../../d6/d76/classApp_1_1ExtensionContainer.html#a9f5f7c38f59fde6f0d7a22d242ac7aa6) () const  
[bool](../../d9/db9/classbool.html) | [hasExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#adae9aba02ce19d1611f1bb3447ee936e) ([Base::Type](../../dc/dee/classBase_1_1Type.html), [bool](../../d9/db9/classbool.html) derived=true) const  
[bool](../../d9/db9/classbool.html) | [hasExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a8e5befbc7a981a91f6912697dea587e1) (const std::string &name) const  
[bool](../../d9/db9/classbool.html) | [hasExtensions](../../d6/d76/classApp_1_1ExtensionContainer.html#a56345b1e7049b01ee7620192f06950dd) () const  
void | [registerExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a007eb07d5313eaa01d14462d7b7d960d) ([Base::Type](../../dc/dee/classBase_1_1Type.html) extension, [App::Extension](../../d8/dc7/classApp_1_1Extension.html) *ext)  
virtual | [~ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a3590d0f208eaf38fd6fdde59534c5a02) ()  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [getPropertyByName](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897) (const char *name) const override  
| find a property by its name
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897)  
  
virtual const char * | [getPropertyName](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the name of a property
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0)  
  
virtual void | [getPropertyMap](../../d6/d76/classApp_1_1ExtensionContainer.html#a12d88a996edd035623450a5b8da10d03) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const override  
| get all properties of the class (including properties of the parent)
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a12d88a996edd035623450a5b8da10d03)  
  
virtual void | [getPropertyList](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const override  
| get all properties of the class (including properties of the parent)
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6)  
  
virtual short | [getPropertyType](../../d6/d76/classApp_1_1ExtensionContainer.html#afd7697c47292ff6d6b7fce5bff86941f) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#afd7697c47292ff6d6b7fce5bff86941f)  
  
virtual short | [getPropertyType](../../d6/d76/classApp_1_1ExtensionContainer.html#afc5151a1d5fa7822d9f6fd1bb4bc4004) (const char *name) const override  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#afc5151a1d5fa7822d9f6fd1bb4bc4004)  
  
virtual const char * | [getPropertyGroup](../../d6/d76/classApp_1_1ExtensionContainer.html#a0667cf5204a8854212a23fd5d53f5b1d) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a0667cf5204a8854212a23fd5d53f5b1d)  
  
virtual const char * | [getPropertyGroup](../../d6/d76/classApp_1_1ExtensionContainer.html#a4fba6aeb529e0bbe523bb2cd62d191fc) (const char *name) const override  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a4fba6aeb529e0bbe523bb2cd62d191fc)  
  
virtual const char * | [getPropertyDocumentation](../../d6/d76/classApp_1_1ExtensionContainer.html#a4f2af686b6d232b650bf512e0bbdc223) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a4f2af686b6d232b650bf512e0bbdc223)  
  
virtual const char * | [getPropertyDocumentation](../../d6/d76/classApp_1_1ExtensionContainer.html#afd218927cb4c252f090dd1f377ced7de) (const char *name) const override  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#afd218927cb4c252f090dd1f377ced7de)  
  
virtual void | [Restore](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48)  
  
void | [saveExtensions](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
void | [restoreExtensions](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [addDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6) (const char *[type](../../d9/d98/classtype.html), const char *name=nullptr, const char *group=nullptr, const char *doc=nullptr, short attr=0, [bool](../../d9/db9/classbool.html) ro=false, [bool](../../d9/db9/classbool.html) hidden=false)  
[bool](../../d9/db9/classbool.html) | [changeDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a322267f4f7ee6ee360535cdc5dce3612) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop, const char *group, const char *doc)  
virtual void | [editProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a001e36affede2983bb0ac4852f2fc617) (const char *)  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [getDynamicPropertyByName](../../d5/d48/classApp_1_1PropertyContainer.html#aa61e4c2e94abf8310ff9d790e4b54564) (const char *name) const  
[DynamicProperty::PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html) | [getDynamicPropertyData](../../d5/d48/classApp_1_1PropertyContainer.html#aa6ac51c527bc5f13d8d6d5ddc4e51f2e) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
virtual std::vector< std::string > | [getDynamicPropertyNames](../../d5/d48/classApp_1_1PropertyContainer.html#a71fa8d125dc74b919e994a79985f601b) () const  
virtual std::string | [getFullName](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d) () const  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [getPropertyByName](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2) (const char *name) const  
| find a property by its name
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2)  
  
virtual const char * | [getPropertyDocumentation](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50) (const char *name) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50)  
  
virtual const char * | [getPropertyDocumentation](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912)  
  
virtual const char * | [getPropertyGroup](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a) (const char *name) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a)  
  
virtual const char * | [getPropertyGroup](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356)  
  
virtual void | [getPropertyList](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
| get all properties of the class (including properties of the parent)
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a)  
  
virtual void | [getPropertyMap](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
| get all properties of the class (including properties of the parent)
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8)  
  
virtual const char * | [getPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the name of a property
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981)  
  
virtual void | [getPropertyNamedList](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f) (std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > &List) const  
| get all properties with their names, may contain duplicates and aliases
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f)  
  
const char * | [getPropertyPrefix](../../d5/d48/classApp_1_1PropertyContainer.html#afd2652f19f3b1db90309c5a69713507c) () const  
virtual short | [getPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4) (const char *name) const  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4)  
  
virtual short | [getPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510)  
  
[bool](../../d9/db9/classbool.html) | [isHidden](../../d5/d48/classApp_1_1PropertyContainer.html#a1a89b20166f4e4a3feea04a84179d1ed) (const char *name) const  
| check if the named property is hidden
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a1a89b20166f4e4a3feea04a84179d1ed)  
  
[bool](../../d9/db9/classbool.html) | [isHidden](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| check if the property is hidden
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d5/d48/classApp_1_1PropertyContainer.html#a7375800ad653da01d4b5a98f5fb69799) (const char *name) const  
| check if the named property is read-only
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a7375800ad653da01d4b5a98f5fb69799)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| check if the property is read-only
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082)  
  
virtual void | [onPropertyStatusChanged](../../d5/d48/classApp_1_1PropertyContainer.html#a25dc796f1aecab39ceeed8335097b758) (const [Property](../../d0/da9/classApp_1_1Property.html) &prop, unsigned long oldStatus)  
|
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#af08e2297f31f338356f8eb8f2000ff97)
()  
| A constructor.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#af08e2297f31f338356f8eb8f2000ff97)  
  
virtual [bool](../../d9/db9/classbool.html) | [removeDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a7e5425268a06b3e8a12f45abbbcfd653) (const char *name)  
virtual void | [Restore](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944)  
  
virtual void | [Save](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482)  
  
void | [setPropertyPrefix](../../d5/d48/classApp_1_1PropertyContainer.html#aeac678dd3506bf850148f891fe368446) (const char *prefix)  
void | [setPropertyStatus](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed) (unsigned char bit, [bool](../../d9/db9/classbool.html) value)  
| set the Status bit of all properties at once
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed)  
  
virtual | [~PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#abca525c7322e6aa891390002c1b8b309) ()  
| A destructor.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#abca525c7322e6aa891390002c1b8b309)  
  
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
  
![-](../../closed.png) Public Member Functions inherited from
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObjects](../../da/d09/classApp_1_1OriginGroupExtension.html#ac875c27af27eb9f1bf001ee92aa51e5d) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj) override  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
| Get the sub object by name.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11)  
  
virtual short | [extensionMustExecute](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5) () override  
| Returns true on changing
[OriginFeature](../../da/dfe/classApp_1_1OriginFeature.html "Plane Object Used
to define planar support for all kind of operations in the document space.")
set.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5)  
  
virtual void | [extensionOnChanged](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42) (const [Property](../../d0/da9/classApp_1_1Property.html) *p) override  
[App::Origin](../../d9/d8b/classApp_1_1Origin.html) * | [getOrigin](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2) () const  
| Returns the origin link or throws an exception.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2)  
  
virtual const char * | [getViewProviderName](../../da/d09/classApp_1_1OriginGroupExtension.html#adf1af86f75a6cee95a3976bd4dac91db) () const  
| returns the type name of the ViewProvider
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#adf1af86f75a6cee95a3976bd4dac91db)  
  
virtual [bool](../../d9/db9/classbool.html) | [hasObject](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) recursive=false) const override  
| Checks whether the object _obj_ is part of this group.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#af5c6fb37f5c5c0461b41667428f62ba3)  
  
|
[OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a831ac058ccd79dedfbbe9d351fb477a5)
()  
void | [relinkToOrigin](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
virtual | [~OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#a16abb8dcc64ed4de348090f5d9ed1882) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a54bc886600443d9597349252b21a070d) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj) override  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const override  
| Get the sub object by name.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const override  
| Get name references of all sub objects.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a049b0b8b248680cbdc858bd5e44603aa)  
  
virtual void | [extensionOnChanged](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#ab40bda05c2ff03c0200d7eb2063af487) (const [Property](../../d0/da9/classApp_1_1Property.html) *p) override  
|
[GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a234c2d5269575c55406a5c8e18879772)
(void)  
| Constructor.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a234c2d5269575c55406a5c8e18879772)  
  
[Base::Placement](../../d1/d10/classBase_1_1Placement.html) | [globalGroupPlacement](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a585dae79f685156866b19a53eb93e77c) ()  
| Calculates the global placement of this group.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a585dae79f685156866b19a53eb93e77c)  
  
virtual void | [initExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a74933934579b51ddd24efdd5be7bb3ba) ([ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) *obj) override  
[PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html) & | [placement](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4cd1b76960dc22c7a5d5775c54ba76fb) ()  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [removeObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj) override  
| Removes objects from this group.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a38ac880c5d19aba50ba8726162bbe2bb)  
  
virtual void | [transformPlacement](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953) (const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) &transform)  
| transformPlacement applies transform to placement of this shape.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#af259333fef3bdbc93a30be16d92c2953)  
  
virtual | [~GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a4129a0acf45d43fa3a4f0bf7806e14db) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
|
[GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a)
(void)  
| Constructor.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#afd7849b2e26ce7e3ba33ba850054854a)  
  
virtual | [~GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html#a63e13d300db274dc5f6280a0e0c38b99) ()  
virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [addObject](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea) (const char *sType, const char *pObjectName)  
| Adds an object of _sType_ with _pObjectName_ to the document this group
belongs to and append it to this group as well.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea)  
  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObject](../../da/d3a/classApp_1_1GroupExtension.html#a583eea19b9a0e1af43bb8aa8fdf9dbad) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [setObjects](../../da/d3a/classApp_1_1GroupExtension.html#a0466cc49b83d1a3157799150b6d299af) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > obj)  
virtual [bool](../../d9/db9/classbool.html) | [allowObject](../../da/d3a/classApp_1_1GroupExtension.html#a935f7c2af21dd8b1ef7e0ae74a7b9e5f) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
virtual std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [removeObject](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Removes an object from this group.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34)  
  
virtual void | [removeObjectsFromDocument](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1) ()  
| Removes all children objects from this group and the document.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#af7405cb3abccba3302792487e514a4e1)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getObject](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961) (const char *Name) const  
| Returns the object of this group with _Name_.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961)  
  
[bool](../../d9/db9/classbool.html) | [isChildOf](../../da/d3a/classApp_1_1GroupExtension.html#ad19ccc7fc052d71da1b11e6f736ca7c3) (const [GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html) *group, [bool](../../d9/db9/classbool.html) recursive=true) const  
| Checks whether this group object is a child (or sub-child if enabled) of the
given group object.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#ad19ccc7fc052d71da1b11e6f736ca7c3)  
  
const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | [getObjects](../../da/d3a/classApp_1_1GroupExtension.html#ab7df48295e51c05fcb9eaa3ac2857938) () const  
| Returns a list of all objects this group does have.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#ab7df48295e51c05fcb9eaa3ac2857938)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getObjectsOfType](../../da/d3a/classApp_1_1GroupExtension.html#a55c23aac201dfbc053a5eeaf8bd37e5f) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId) const  
| Returns a list of all objects of _typeId_ this group does have.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a55c23aac201dfbc053a5eeaf8bd37e5f)  
  
[int](../../d1/da0/classint.html) | [countObjectsOfType](../../da/d3a/classApp_1_1GroupExtension.html#a20dc1c6c322878e94281f7a7f56b4173) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId) const  
| Returns the number of objects of _typeId_ this group does have.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a20dc1c6c322878e94281f7a7f56b4173)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../da/d3a/classApp_1_1GroupExtension.html#a860f82302ebbf404b14cca69adc9ff36) (void) override  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getAllChildren](../../da/d3a/classApp_1_1GroupExtension.html#a65e76eb95d529bdfe44189441bcf1495) () const  
void | [getAllChildren](../../da/d3a/classApp_1_1GroupExtension.html#a659c18eb455814e2dbe04a79a59947f6) (std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &) const  
![-](../../closed.png) Public Member Functions inherited from
[App::DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html)  
|
[DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a6166756be21e41923ff0cf27ca4cb13d)
()  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e) ()  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetLinkedObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab6fc58714d6b5b2ecaa09f7ff6cc005f) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, [bool](../../d9/db9/classbool.html) recursive, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const  
| Get the linked object.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab6fc58714d6b5b2ecaa09f7ff6cc005f)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ae3b4c124bec333326bb9b0f0ad9600a7) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&ret, const char *subname, [PyObject](../../df/d1b/classPyObject.html) **pyObj, [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *mat, [bool](../../d9/db9/classbool.html) transform, [int](../../d1/da0/classint.html) depth) const  
| Get the sub object by name.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ae3b4c124bec333326bb9b0f0ad9600a7)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionGetSubObjects](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2427868f8594561b0bd0b246b8938dd9) (std::vector< std::string > &ret, [int](../../d1/da0/classint.html) reason) const  
| Get name references of all sub objects.
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2427868f8594561b0bd0b246b8938dd9)  
  
virtual [bool](../../d9/db9/classbool.html) | [extensionHasChildElement](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a7ab4deac14dc40ce2e2675516baf156c) () const  
virtual [int](../../d1/da0/classint.html) | [extensionIsElementVisible](../../d4/d81/classApp_1_1DocumentObjectExtension.html#adab10ac2801e93d6efde2c3d8cbc97db) (const char *)  
virtual short | [extensionMustExecute](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af09cb831d7b6ba0300042f83af2f2ec6) ()  
virtual [int](../../d1/da0/classint.html) | [extensionSetElementVisible](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a59f60f1750805a02264f996c78967eae) (const char *, [bool](../../d9/db9/classbool.html))  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getExtendedObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a2f7cb30df26cc640a224640397938705) ()  
const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getExtendedObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af6e17e520cf9b556992786cb5d57e911) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a254f58c97024cd7e86fec56544fb77b1) () override  
virtual const char * | [getViewProviderExtensionName](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad1f73fbadf4f1160c349488b328ae128) () const  
| returns the type name of the ViewProviderExtension which is automatically
attached to the viewprovider object when it is initiated
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad1f73fbadf4f1160c349488b328ae128)  
  
virtual void | [onExtendedDocumentRestored](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af01de2fab2226a8e3e88dd1db479c3a8) ()  
| get called after a document has been fully restored
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#af01de2fab2226a8e3e88dd1db479c3a8)  
  
virtual void | [onExtendedSettingDocument](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad4ad4158178cd5cf9c7d3786d21dcf15) ()  
| get called after setting the document
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ad4ad4158178cd5cf9c7d3786d21dcf15)  
  
virtual void | [onExtendedSetupObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab86867c2b2e774c2a15819ca6ef97b89) ()  
| get called after a brand new object was created
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#ab86867c2b2e774c2a15819ca6ef97b89)  
  
virtual void | [onExtendedUnsetupObject](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133) ()  
| get called when object is going to be removed from the document
[More...](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0cf88b507c8a513d5ae2dc63a7221133)  
  
virtual | [~DocumentObjectExtension](../../d4/d81/classApp_1_1DocumentObjectExtension.html#a0157751167592aa320110ad2d85fbf66) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
|
[Extension](../../d8/dc7/classApp_1_1Extension.html#add927117e09bb09a0d83e3cd3439a15d)
()  
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) * | [getExtendedContainer](../../d8/dc7/classApp_1_1Extension.html#a178c40e2783b6e2d1f75b3c04feeabcf) ()  
const [App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) * | [getExtendedContainer](../../d8/dc7/classApp_1_1Extension.html#a565ab575fe6be7b373b0b933885268d4) () const  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getExtensionPyObject](../../d8/dc7/classApp_1_1Extension.html#a77ffed10ef0c284b3a702caf46570168) ()  
virtual void | [initExtension](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def) ([App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) *obj)  
[bool](../../d9/db9/classbool.html) | [isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#ad4a437742b2739a79a657255b2c19321) ()  
std::string | [name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016) () const  
virtual | [~Extension](../../d8/dc7/classApp_1_1Extension.html#a52c2b4e48fa3f78511b72d55fefcb48c) ()  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [extensionGetPropertyByName](../../d8/dc7/classApp_1_1Extension.html#ade0ea67a01018f91ef56838a3a557156) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| find a property by its name
[More...](../../d8/dc7/classApp_1_1Extension.html#ade0ea67a01018f91ef56838a3a557156)  
  
virtual const char * | [extensionGetPropertyName](../../d8/dc7/classApp_1_1Extension.html#a670480fa1d036c8217ef4b817f2c41a6) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the name of a property
[More...](../../d8/dc7/classApp_1_1Extension.html#a670480fa1d036c8217ef4b817f2c41a6)  
  
virtual void | [extensionGetPropertyMap](../../d8/dc7/classApp_1_1Extension.html#ab0787c477eac6d231ac91e912abc192a) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
| get all properties of the class (including properties of the parent)
[More...](../../d8/dc7/classApp_1_1Extension.html#ab0787c477eac6d231ac91e912abc192a)  
  
virtual void | [extensionGetPropertyList](../../d8/dc7/classApp_1_1Extension.html#a9cc010d4ba4318211f3f6b328116d359) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
| get all properties of the class (including properties of the parent)
[More...](../../d8/dc7/classApp_1_1Extension.html#a9cc010d4ba4318211f3f6b328116d359)  
  
virtual short | [extensionGetPropertyType](../../d8/dc7/classApp_1_1Extension.html#aea49212c18ec8617c4b43a03c73dba17) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#aea49212c18ec8617c4b43a03c73dba17)  
  
virtual short | [extensionGetPropertyType](../../d8/dc7/classApp_1_1Extension.html#ab6c4d7b5439181459122280af2c138c8) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#ab6c4d7b5439181459122280af2c138c8)  
  
virtual const char * | [extensionGetPropertyGroup](../../d8/dc7/classApp_1_1Extension.html#ab6c159292f4f6ed2a46ceb380177634d) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#ab6c159292f4f6ed2a46ceb380177634d)  
  
virtual const char * | [extensionGetPropertyGroup](../../d8/dc7/classApp_1_1Extension.html#a21e92d567142b377a337a901bb8943fc) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#a21e92d567142b377a337a901bb8943fc)  
  
virtual const char * | [extensionGetPropertyDocumentation](../../d8/dc7/classApp_1_1Extension.html#aa2d9bdeef59b8216c6bcb8f5d8ee53f3) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#aa2d9bdeef59b8216c6bcb8f5d8ee53f3)  
  
virtual const char * | [extensionGetPropertyDocumentation](../../d8/dc7/classApp_1_1Extension.html#a33043a15492e987791e91d16c0079be3) (const char *[name](../../d8/dc7/classApp_1_1Extension.html#a93870a0c0963288473c392d40a354016)) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d8/dc7/classApp_1_1Extension.html#a33043a15492e987791e91d16c0079be3)  
  
virtual void | [extensionSave](../../d8/dc7/classApp_1_1Extension.html#a94c65f4a8cf93d9a149726049885aafd) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &) const  
virtual void | [extensionRestore](../../d8/dc7/classApp_1_1Extension.html#ab1a7fb60166532ef2838ee0722c5955f) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)  
[bool](../../d9/db9/classbool.html) | [extensionIsDerivedFrom](../../d8/dc7/classApp_1_1Extension.html#ad635be48204f8f5fb9c75103cd89fb20) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
![-](../../closed.png) Static Public Member Functions inherited from
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html)  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [resolveElement](../../d7/d75/classApp_1_1GeoFeature.html#aef8b2a9f75e796e56f7921d93b2f2a8a) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *subname, std::pair< std::string, std::string > &elementName, [bool](../../d9/db9/classbool.html) append=false, [ElementNameType](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430) [type](../../d9/d98/classtype.html)=[Normal](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430a97a46c8f318c64f007d9a0fc40601007), const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *filter=nullptr, const char **element=nullptr, [GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html) **geo=nullptr)  
| Resolve both the new and old style element name.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#aef8b2a9f75e796e56f7921d93b2f2a8a)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
static const char * | [hasHiddenMarker](../../d2/de4/classApp_1_1DocumentObject.html#a613d0852b3963076e958e19a7c657c06) (const char *subname)  
| Check if the subname reference ends with hidden marker.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a613d0852b3963076e958e19a7c657c06)  
  
static const std::string & | [hiddenMarker](../../d2/de4/classApp_1_1DocumentObject.html#ad48238ffb00b5919695aeed71f5c1e37) ()  
| Special marker to mark the object as hidden.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ad48238ffb00b5919695aeed71f5c1e37)  
  
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
![-](../../closed.png) Static Public Member Functions inherited from
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html)  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the origin group which contains this object.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#aefe03f3ec93fce064aeca10ea5593d1b)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[App::GeoFeatureGroupExtension](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html)  
static [bool](../../d9/db9/classbool.html) | [areLinksValid](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a70b51273c4f85b5dd33399ccd08c7b8c) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Checks if the links of the given object comply with all GeoFeatureGroup
requirements, that means if normal links are only within the parent
GeoFeatureGroup.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a70b51273c4f85b5dd33399ccd08c7b8c)  
  
static std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getCSRelevantLinks](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Collects all links that are relevant for the coordinate system, meaning all
recursive links to obj and from obj excluding expressions and stopping the
recursion at other geofeaturegroups.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621)  
  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the geo feature group which contains this object.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13)  
  
static void | [getInvalidLinkObjects](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a391e01ee323c3d9c25c8d74aa8271ae2) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &vec)  
static [bool](../../d9/db9/classbool.html) | [isLinkValid](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7) ([App::Property](../../d0/da9/classApp_1_1Property.html) *link)  
| Checks if the given link complies with all GeoFeatureGroup requirements,
that means if normal links are only within the parent GeoFeatureGroup.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a89659fb6caa61f4cf9971b0170efcdc7)  
  
static [bool](../../d9/db9/classbool.html) | [isNonGeoGroup](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a090ae4c150d40ab2679216bf0895e3d6) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns true if the given
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") is
[DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html) but
not GeoFeatureGroup.
[More...](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a090ae4c150d40ab2679216bf0895e3d6)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)  
static [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getGroupOfObject](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Returns the object group of the document which the given object _obj_ is
part of.
[More...](../../da/d3a/classApp_1_1GroupExtension.html#a04dde88db0fd3983e66bcf8444a3e07b)  
  
![-](../../closed.png) Static Public Attributes inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
static [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [StdReturn](../../d2/de4/classApp_1_1DocumentObject.html#af53a1c6a086c5dfe228aaefeeb7316d2)  
![-](../../closed.png) Protected Member Functions inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [execute](../../d2/de4/classApp_1_1DocumentObject.html#addd0e28aebe720807dd5c1f6790fe752) (void)  
| get called by the document to recompute this feature Normally this method
get called in the processing of
[Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b
"Recompute touched features and return the number of recalculated features.").
[More...](../../d2/de4/classApp_1_1DocumentObject.html#addd0e28aebe720807dd5c1f6790fe752)  
  
[App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [executeExtensions](../../d2/de4/classApp_1_1DocumentObject.html#a035b5c3f55d521760d4839eceba0b937) ()  
| Executes the extensions of a document object.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a035b5c3f55d521760d4839eceba0b937)  
  
virtual void | [onBeforeChange](../../d2/de4/classApp_1_1DocumentObject.html#a06538b0ebeb63aad6aa62794efd626aa) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
| get called before the value is changed
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a06538b0ebeb63aad6aa62794efd626aa)  
  
virtual void | [onChanged](../../d2/de4/classApp_1_1DocumentObject.html#aa9fcfd8db6b2ffdf46274b18b45811cf) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
| get called by the container when a property was changed
[More...](../../d2/de4/classApp_1_1DocumentObject.html#aa9fcfd8db6b2ffdf46274b18b45811cf)  
  
virtual void | [onDocumentRestored](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604) ()  
| get called after a document has been fully restored
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604)  
  
virtual void | [onPropertyStatusChanged](../../d2/de4/classApp_1_1DocumentObject.html#a89e5f59efb767cc633a6837305d04479) (const [Property](../../d0/da9/classApp_1_1Property.html) &prop, unsigned long oldStatus) override  
| get called when a property status has changed
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a89e5f59efb767cc633a6837305d04479)  
  
virtual void | [onSettingDocument](../../d2/de4/classApp_1_1DocumentObject.html#a920e769c3d0e5d8bb61b021655cf9824) ()  
| get called after setting the document
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a920e769c3d0e5d8bb61b021655cf9824)  
  
virtual void | [onUndoRedoFinished](../../d2/de4/classApp_1_1DocumentObject.html#a82f797a0e731564abb8ae8fd6eee44be) ()  
| get called after an undo/redo transaction is finished
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a82f797a0e731564abb8ae8fd6eee44be)  
  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [recompute](../../d2/de4/classApp_1_1DocumentObject.html#a44b395b4b13f86a41e9f4f073898a183) (void)  
| recompute only this object
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a44b395b4b13f86a41e9f4f073898a183)  
  
void | [resetError](../../d2/de4/classApp_1_1DocumentObject.html#ae87602458657bc35e98dd3c2b6270085) (void)  
void | [setDocument](../../d2/de4/classApp_1_1DocumentObject.html#a043039f2703e2a1475e8476e031e8822) ([App::Document](../../d8/d3e/classApp_1_1Document.html) *doc)  
void | [setError](../../d2/de4/classApp_1_1DocumentObject.html#afe1699419952f5d9b9ea1bdac463eb62) (void)  
virtual void | [setupObject](../../d2/de4/classApp_1_1DocumentObject.html#ac677fd52efeb2a6d1e5afd71dc896e7b) ()  
| get called after a brand new object was created
[More...](../../d2/de4/classApp_1_1DocumentObject.html#ac677fd52efeb2a6d1e5afd71dc896e7b)  
  
virtual void | [unsetupObject](../../d2/de4/classApp_1_1DocumentObject.html#a2db78b2e1fbd7667aba76dfd93aa7c07) ()  
| get called when object is going to be removed from the document
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a2db78b2e1fbd7667aba76dfd93aa7c07)  
  
![-](../../closed.png) Protected Member Functions inherited from
[App::TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html)  
void | [onBeforeChangeProperty](../../d8/d00/classApp_1_1TransactionalObject.html#aefa55dd46b014db2e5dafe7310480233) ([Document](../../d8/d3e/classApp_1_1Document.html) *doc, const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
![-](../../closed.png) Protected Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
virtual const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) & | [getPropertyData](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84) (void) const  
virtual void | [handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, const char *PropName)  
|
[PropertyContainer::handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573
"PropertyContainer::handleChangedPropertyName is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of this property container.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573)  
  
virtual void | [handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
|
[PropertyContainer::handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923
"PropertyContainer::handleChangedPropertyType is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of the property container.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923)  
  
virtual void | [onBeforeChange](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
| get called before the value is changed
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057)  
  
virtual void | [onChanged](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
| get called by the container when a property has changed
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34)  
  
![-](../../closed.png) Protected Member Functions inherited from
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html)  
virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [extensionExecute](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3) () override  
| Checks integrity of the [Origin](../../d9/d8b/classApp_1_1Origin.html "Base
class of all geometric document objects.").
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#ae02f4d3ece4b2ce9710f93692832a4c3)  
  
virtual void | [onExtendedSetupObject](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb) () override  
| Creates the corresponding [Origin](../../d9/d8b/classApp_1_1Origin.html
"Base class of all geometric document objects.") object.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb)  
  
virtual void | [onExtendedUnsetupObject](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27) () override  
| Removes all planes and axis if they are still linked to the document.
[More...](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27)  
  
![-](../../closed.png) Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
void | [initExtensionType](../../d8/dc7/classApp_1_1Extension.html#a12ec705423cb1952b395a4d135f2f734) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html))  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
static const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [getPropertyDataPtr](../../d5/d48/classApp_1_1PropertyContainer.html#a8649f534ecaa91393925fa514ed29e4b) (void)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
static void | [initExtensionSubclass](../../d8/dc7/classApp_1_1Extension.html#ad89245f6dbe32a71396c452ea8148ce7) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Base::Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
std::string | [oldLabel](../../d2/de4/classApp_1_1DocumentObject.html#a9f47b6c7f6270efbe72e11fd75f1036b)  
| Old label; used for renaming expressions.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a9f47b6c7f6270efbe72e11fd75f1036b)  
  
const std::string * | [pcNameInDocument](../../d2/de4/classApp_1_1DocumentObject.html#a2e797e4bd0bfbf7ef4d3f12e220594eb)  
Py::SmartPtr | [PythonObject](../../d2/de4/classApp_1_1DocumentObject.html#a582b41c7afe40300a4984518dcecb5b1)  
| python object of this class and all descendent
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a582b41c7afe40300a4984518dcecb5b1)  
  
std::bitset< 32 > | [StatusBits](../../d2/de4/classApp_1_1DocumentObject.html#a90f8f7b8b02164e03d2d0187d4fb183e)  
| Status bits of the document object The first 8 bits are used for the base
system the rest can be used in descendent classes to mark special statuses on
the objects.
[More...](../../d2/de4/classApp_1_1DocumentObject.html#a90f8f7b8b02164e03d2d0187d4fb183e)  
  
![-](../../closed.png) Protected Attributes inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html) | [dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99)  
![-](../../closed.png) Protected Attributes inherited from
[App::Extension](../../d8/dc7/classApp_1_1Extension.html)  
[bool](../../d9/db9/classbool.html) | [m_isPythonExtension](../../d8/dc7/classApp_1_1Extension.html#aed35b8360543786d3d1ce3437234d706) = false  
Py::SmartPtr | [ExtensionPythonObject](../../d8/dc7/classApp_1_1Extension.html#a88dfbf607776831b2e2a6b72d0a25cd3)  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all geometric document objects.

## Constructor & Destructor Documentation

## ◆ Part()

App::Part::Part  | ( | | ) |   
---|---|---|---|---  
  
Constructor.

## ◆ ~Part()

| virtual App::Part::~Part  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ getPartOfObject()

| static [App::Part](../../da/d8d/classApp_1_1Part.html) * App::Part::getPartOfObject  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `true`  
| ) | |   
static  
  
Returns the part which contains this object.

In case this object does not belong to any
[Part](../../da/d8d/classApp_1_1Part.html "Base class of all geometric
document objects."), 0 is returned.

Parameters

     obj| the object to search for   
---|---  
recursive| whether to recursively find any grand parent
[Part](../../da/d8d/classApp_1_1Part.html "Base class of all geometric
document objects.") container  
  
Referenced by
[PartDesignGui::ViewProviderBody::canDropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#aecc79ac8b9648a6f38d03aa375d74989),
[PartDesignGui::ViewProviderBody::doubleClicked()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#af3c19e67cc2a25b4d54a723c15015251),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
and
[Sketcher::SketchObject::isExternalAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a15854bee280f512f617c7f34752ab823).

## ◆ getPyObject()

| virtual [PyObject](../../df/d1b/classPyObject.html) * App::Part::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
getPyObject returns the Python binding object

Returns

    the Python binding object 

Reimplemented from
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html#a6837f9af91a2619c420f361033ab0da5).

## ◆ getViewProviderName()

| virtual const char * App::Part::getViewProviderName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
returns the type name of the ViewProvider

Reimplemented from
[App::OriginGroupExtension](../../da/d09/classApp_1_1OriginGroupExtension.html#adf1af86f75a6cee95a3976bd4dac91db).

## ◆ handleChangedPropertyType()

| virtual void App::Part::handleChangedPropertyType  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_ ,   
---|---|---|---  
|  | const char *  | _TypeName_ ,   
|  | [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |   
overridevirtual  
  
[PropertyContainer::handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923
"PropertyContainer::handleChangedPropertyType is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of the property container.

This method is typically called if the property on file has changed its type
in more recent versions.

The default implementation does nothing.

Parameters

     reader| The XML stream to read from.   
---|---  
TypeName| Name of property type on file.  
prop| Pointer to property to restore. Its type differs from TypeName.  
  
Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923).

## Member Data Documentation

## ◆ Color

[App::PropertyColor](../../d9/d0b/classApp_1_1PropertyColor.html)
App::Part::Color  
---  
  
[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") color of the Item If the transparency value is 1.0
the color or the next hierarchy is used.

## ◆ Id

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Part::Id  
---  
  
Id e.g. [Part](../../da/d8d/classApp_1_1Part.html "Base class of all geometric
document objects.") number.

## ◆ License

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Part::License  
---  
  
License string Holds the short license string for the Item, e.g.

CC-BY for the Creative Commons license suit.

## ◆ LicenseURL

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Part::LicenseURL  
---  
  
License description/contract URL.

## ◆ Material

[App::PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html)
App::Part::Material  
---  
  
material descriptions

## ◆ Meta

[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html) App::Part::Meta  
---  
  
[Meta](../../d9/dcf/namespaceApp_1_1Meta.html) descriptions.

## ◆ Type

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) App::Part::Type  
---  
  
type of the part

Referenced by
[ArchPanel.CommandPanelSheet::Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation::add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[ArchStructure.StructSelectionObserver::addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchComponent.Component::execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[draftobjects.layer.LayerContainer::execute()](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a960d8cd7f03fe7426f8cac669671b513),
[Gui::ViewProviderPart::getIcon()](../../d9/d6c/classGui_1_1ViewProviderPart.html#afba5f47c9f0f811fe7983cac5c6f5fa3),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.layer.Layer::set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
and
[ArchReference.ArchReference::setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5).

## ◆ Uid

[App::PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html) App::Part::Uid  
---  
  
unique identifier of the Item

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/Part.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

