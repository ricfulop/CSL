---
url: https://freecad.github.io/SourceDoc/d7/d75/classApp_1_1GeoFeature.html
scraped_at: 2025-09-08T14:54:50.608073
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html)

[List of all members](../../d3/dc6/classApp_1_1GeoFeature-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes

App::GeoFeature Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all geometric document objects.
[More...](../../d7/d75/classApp_1_1GeoFeature.html#details)

`#include <GeoFeature.h>`

##  Public Types  
  
---  
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
  
##  Public Member Functions  
  
---  
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
  
  
##  Static Public Member Functions  
  
---  
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
  
##  Public Attributes  
  
---  
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
  
  
##  Additional Inherited Members  
  
---  
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
  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
static const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [getPropertyDataPtr](../../d5/d48/classApp_1_1PropertyContainer.html#a8649f534ecaa91393925fa514ed29e4b) (void)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
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
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all geometric document objects.

## Member Enumeration Documentation

## ◆ ElementNameType

enum
[App::GeoFeature::ElementNameType](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430)  
---  
  
Specify the type of element name to return when calling
[getElementName()](../../d7/d75/classApp_1_1GeoFeature.html#a13eb06dab99e7fbdd2dee9bb3db1d30d
"Return the new and old style sub-element name.")

Enumerator  
---  
Normal | Normal usage.   
Import | For importing.   
Export | For exporting.   
  
## Constructor & Destructor Documentation

## ◆ GeoFeature()

GeoFeature::GeoFeature  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Constructor.

References
[App::Prop_NoRecompute](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a23b6163dbf57aa55ebea576f60b58077).

## ◆ ~GeoFeature()

| GeoFeature::~GeoFeature  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ getElementName()

| std::pair< std::string, std::string > GeoFeature::getElementName  | ( | const char *  | _name_ ,   
---|---|---|---  
|  | [ElementNameType](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430) | _type_ = `[Normal](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430a97a46c8f318c64f007d9a0fc40601007)`  
| ) | |  const  
virtual  
  
Return the new and old style sub-element name.

Parameters

     name| input name   
---|---  
type| desired element name type to return  
  
Returns

    a pair(newName,oldName). New element name may be empty.

This function currently is does nothing. The new style element name generation
will be added in the next batch of patches.

## ◆ getPropertyOfGeometry()

| const [PropertyComplexGeoData](../../d7/d28/classApp_1_1PropertyComplexGeoData.html) * GeoFeature::getPropertyOfGeometry  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
This method returns the main property of a geometric object that holds the
actual geometry.

For a part object this is the Shape property, for a mesh object the
[Mesh](../../dc/d48/namespaceMesh.html "The namespace of the Mesh Application
layer library.") property and so on. The default implementation returns null.

Reimplemented in
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a9dae4a51cd5200b930387b4eb7e18ce5),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a3b3867040ca9acc69943106d4578bc5c),
and
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#a76b46645f13fa2c2a41dcd921f9788d9).

Referenced by
[Gui::AlignmentGroup::getBoundingBox()](../../dc/d5e/classGui_1_1AlignmentGroup.html#a61b723faec476204d9ef279204fce7bf),
and
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * GeoFeature::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
getPyObject returns the Python binding object

Returns

    the Python binding object 

Reimplemented from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a1adfcfb2169b5c31374e07346256648f).

Reimplemented in
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a4b39fb08f59a125dcc783cf93e25d86d),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a7a700a82e66b15d3eb4845ad75c194ab),
[App::Part](../../da/d8d/classApp_1_1Part.html#a8efaf38ed9d96a1207ff4b6bb05955e5),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#a9e28639037238df4c8dafb4518ee86c4),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#ae23b16d8ba14ec40c3cd74aca0634f2e),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#a666f699fb9530523ef6467717f385096),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a49b5d225e27f3adf2cb0b8452fa84ef8),
[App::InventorObject](../../da/d11/classApp_1_1InventorObject.html#adb3523042b8befd61616bc05fedd290f),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a5a9445b1375ded9f86617e15151ec389),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#abb0ba3282d7a1b42eaeaaee6364afd42),
[PartDesign::Feature](../../d7/d51/classPartDesign_1_1Feature.html#a7b572936974ad2fb3d78fe729d3e1757),
[Path::FeatureArea](../../da/d1e/classPath_1_1FeatureArea.html#a71e18a904362f9e20f126aca4f13b8e8),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#ab7f800e910601271c9a4bc2480dad5f2),
[Path::FeatureCompound](../../d2/d43/classPath_1_1FeatureCompound.html#a08d674d0a02ef64d5572e51c3689fd2d),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a5b35961553442da622521648b1f50365),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#aa511366030cf224da9a3a0d17b07606e),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a9579e5a76ef1c70cc24701d4bba32c6c),
and
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a7a2970aaacc965d3d4c3b3a949fcb21f).

References
[App::DocumentObject::PythonObject](../../d2/de4/classApp_1_1DocumentObject.html#a582b41c7afe40300a4984518dcecb5b1).

## ◆ globalPlacement()

[Base::Placement](../../d1/d10/classBase_1_1Placement.html) GeoFeature::globalPlacement  | ( | | ) |  const  
---|---|---|---|---  
  
Calculates the placement in the global reference coordinate system.

In FreeCAD the [GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html "Base
class of all geometric document objects.") placement describes the local
placement of the object in its parent coordinate system. This is however not
always the same as the global reference system. If the object is in a
GeoFeatureGroup, hence in another local coordinate system, the
[Placement](../../d7/d32/classApp_1_1Placement.html "Placement Object Handles
the repositioning of data.") property does only give the local transformation.
This function can be used to calculate the placement of the object in the
global reference coordinate system taking all stacked local systems into
account.

Returns

    [Base::Placement](../../d1/d10/classBase_1_1Placement.html "The Placement class.") The transformation from the global reference coordinate system 

References
[App::GeoFeatureGroupExtension::getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13).

Referenced by
[MeshGui::ViewProviderMesh::exportMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a7e475ac2c734112a916b21ec3ffa8f8c),
[TechDraw::ShapeExtractor::getLocation3dFromFeat()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a36c387125006e94abaed1350c0079821),
[TechDraw::ShapeExtractor::getShapes2d()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a7b6b34e0c817f34b537bdb53b36956f1),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
and
[PartDesign::ShapeBinder::updatedShape()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a126f8b03ab46e56d65b7fbd3d41b98e8).

## ◆ resolveElement()

| [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * GeoFeature::resolveElement  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const char *  | _subname_ ,   
|  | std::pair< std::string, std::string > & | _elementName_ ,   
|  | [bool](../../d9/db9/classbool.html) | _append_ = `false`,   
|  | [ElementNameType](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430) | _type_ = `[Normal](../../d7/d75/classApp_1_1GeoFeature.html#aa72490acf929b1c342b4031268fc4430a97a46c8f318c64f007d9a0fc40601007)`,   
|  | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _filter_ = `nullptr`,   
|  | const char **  | _element_ = `nullptr`,   
|  | [GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html) **  | _geo_ = `nullptr`  
| ) | |   
static  
  
Resolve both the new and old style element name.

Parameters

     obj| top parent object   
---|---  
subname| subname reference  
elementName| output of a pair(newElementName,oldElementName)  
append| Whether to include subname prefix into the returned element name  
type| the type of element name to request  
filter| If none zero, then only perform lookup when the element owner object
is the same as this filter  
element| return the start of element name in subname  
  
Returns

    Return the owner object of the element 

References
[Data::ComplexGeoData::findElementName()](../../d8/daf/classData_1_1ComplexGeoData.html#a7a2ff773f05abdf81ee7194a81788085),
[App::DocumentObject::hasHiddenMarker()](../../d2/de4/classApp_1_1DocumentObject.html#a613d0852b3963076e958e19a7c657c06),
and
[Data::ComplexGeoData::oldElementName()](../../d8/daf/classData_1_1ComplexGeoData.html#a986602023d21d9df13e82459732cf7ab).

Referenced by
[Gui::SelectionSingleton::checkSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a67f694d0e8ed1e9acc858e0827202122),
[App::SubObjectT::getNewElementName()](../../dd/d78/classApp_1_1SubObjectT.html#a3f4df581957c8dbc1ffaee6d315ea452),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1),
[App::SubObjectT::getOldElementName()](../../dd/d78/classApp_1_1SubObjectT.html#a91100833ef50109008ae5deff6cd2441),
[Gui::Dialog::DlgPropertyLink::onSelectionChanged()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#ad4da9c97e410c3e08dfcdf4f51e829c4),
[Gui::SelectionSingleton::setPreselect()](../../d4/dca/classGui_1_1SelectionSingleton.html#a4606b917610c1a4ba91821e5405973ab),
and
[Gui::SelectionSingleton::slotSelectionChanged()](../../d4/dca/classGui_1_1SelectionSingleton.html#ae0bb1709723ef769a331ac020f67d7b0).

## ◆ transformPlacement()

| void GeoFeature::transformPlacement  | ( | const [Base::Placement](../../d1/d10/classBase_1_1Placement.html) & | _transform_| ) |   
---|---|---|---|---|---  
virtual  
  
transformPlacement applies transform to placement of this shape.

Override this function to propagate the change of placement to base features,
for example. By the time of writing this comment, the function was only called
by alignment task (Edit->Alignment)

Parameters

     transform| (input).   
---|---  
  
Reimplemented in
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a45f459f55e1cc4efda51100e636056af),
and
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#ac943e32302f22b54d748ce9b04ecbdfe).

Referenced by
[Gui::ManualAlignment::alignObject()](../../d7/d97/classGui_1_1ManualAlignment.html#abfc74600e952621993594238eae06219),
and
[PartDesign::ProfileBased::transformPlacement()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a45f459f55e1cc4efda51100e636056af).

## Member Data Documentation

## ◆ Placement

[PropertyPlacement](../../da/d51/classApp_1_1PropertyPlacement.html) App::GeoFeature::Placement  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Referenced by
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Mesh::Sphere::execute()](../../d1/d57/classMesh_1_1Sphere.html#ae830b723d9c2977e6080c9e87f3ec139),
[Mesh::Ellipsoid::execute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#aa7094fc5c9ce3b03b37b1875e8962b68),
[Mesh::Cylinder::execute()](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone::execute()](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[Mesh::Torus::execute()](../../de/da3/classMesh_1_1Torus.html#a9ca70ccb5548f0852b54fe55f58f27a9),
[Mesh::Cube::execute()](../../df/d68/classMesh_1_1Cube.html#a5c7921255a963127e0496b550023f3ed),
[Part::Reverse::execute()](../../d4/d24/classPart_1_1Reverse.html#a22150a83fa78387e05f60dd1e08d31f8),
[Path::FeatureCompound::execute()](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[PartDesign::ShapeBinder::execute()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a2886a69e9359a73fe242378c2a7b5a27),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[PartDesign::ProfileBased::getAxis()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#abe9168708b58b480c50e6d8473f212da),
[Part::Datum::getBasePoint()](../../db/d0b/classPart_1_1Datum.html#a616fe8e09f6a099b06a100535175c50c),
[PartDesign::Line::getDirection()](../../d0/d2a/classPartDesign_1_1Line.html#af89a81d14e0ccb27353122f43844600c),
[Part::Feature::getLocation()](../../d7/d7e/classPart_1_1Feature.html#a84164b4adfe9b6ecef87da8d7aa1ac9d),
[Part::FeatureReference::getLocation()](../../d2/da1/classPart_1_1FeatureReference.html#aee6f4d426e17d5a0193108fd06f7309c),
[PartDesign::Plane::getNormal()](../../df/df0/classPartDesign_1_1Plane.html#ad208270773ba2e063212171e36895e6e),
[Sketcher::SketchAnalysis::getOpenVertices()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#ab5e084231887ad48de90a03ec8aa3f62),
[PartDesign::Point::getPoint()](../../da/d0d/classPartDesign_1_1Point.html#a425bd8831010df262ca4482511fca22a),
[Part::Datum::getShape()](../../db/d0b/classPart_1_1Datum.html#ae9a416dc1bded6e9d81bdd7ae92540ca),
[Part::Datum::getSubObject()](../../db/d0b/classPart_1_1Datum.html#ac5c48627e7edd4fde0e66a86603a0ca8),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[PartDesign::Body::getSubObject()](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[PartDesign::CoordinateSystem::getSubObject()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#aeb5d09866ebc21adafb8ee43acc9205b),
[PartDesign::SubShapeBinder::getSubObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#afb7e01deac9646afcd5dc1b2aa07042b),
[PartDesign::LinearPattern::getTransformations()](../../d2/d86/classPartDesign_1_1LinearPattern.html#a4073f45eb14b14ad76fd28e8e28d778f),
[PartDesign::Mirrored::getTransformations()](../../d6/d91/classPartDesign_1_1Mirrored.html#a1744f94215d478f3cf8852295103f773),
[PartDesign::PolarPattern::getTransformations()](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5207730b9af6a120d0f3d932fc5d74b0),
[PartDesign::CoordinateSystem::getXAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a04498f548e650362eb2c094f89f5470b),
[PartDesign::CoordinateSystem::getYAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a38beb2d58454d7cb970b4dfb222fe8d3),
[PartDesign::CoordinateSystem::getZAxis()](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a4b9edd67bb7f8c895a9f5bd726fb92e2),
[PartDesign::ShapeBinder::hasPlacementChanged()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a6d80126d976410405532fabeced0feaa),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[PartDesign::FeatureExtrude::mustExecute()](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a7416081060d0046a4ee5f75b6cf96745),
[PartDesign::Fillet::mustExecute()](../../d0/d50/classPartDesign_1_1Fillet.html#a5b3a59c8e278d4f36512e98f3c29c5e3),
[PartDesign::Groove::mustExecute()](../../d7/de3/classPartDesign_1_1Groove.html#af2c45ee71298e5f2243c8ea28f2d5f06),
[PartDesign::Helix::mustExecute()](../../d3/d78/classPartDesign_1_1Helix.html#a8b11a6cb96966e4d2f78bc2aa6202e8b),
[PartDesign::Revolution::mustExecute()](../../d2/de6/classPartDesign_1_1Revolution.html#a3a2eebb70794151bf41bbfdfd374eae6),
[PartDesign::Thickness::mustExecute()](../../d4/d22/classPartDesign_1_1Thickness.html#a5e19889c98eff816988ec695a3630027),
[PartDesign::Chamfer::mustExecute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3f61714b5aa58b68ccb2ac3f0fed02c9),
[Mesh::Feature::onChanged()](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PartDesign::ProfileBased::onChanged()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a36fd19fd597799ebeccd8eddd104bdf4),
[Points::Feature::onChanged()](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Part::Feature::onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[PartDesign::FeatureBase::onDocumentRestored()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a88645629a13677f1034ae2023481c2a1),
[Part::Compound2::onDocumentRestored()](../../d5/dab/classPart_1_1Compound2.html#ac69720b1ba091dcdfac8b07ffbbf6048),
[PartDesign::DressUp::positionByBaseFeature()](../../df/de5/classPartDesign_1_1DressUp.html#ad0f7b71428ae5784d44e9a75f810ff3c),
[PartDesign::ProfileBased::positionByPrevious()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#acdddc3b78089a2b2dbd5c567998c9039),
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710),
[PartDesign::Transformed::positionBySupport()](../../dd/de1/classPartDesign_1_1Transformed.html#a99fa3cb882eea77aa22da310efdafdb7),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[Sketcher::SketchObject::rebuildExternalGeometry()](../../d9/dad/classSketcher_1_1SketchObject.html#a67f9ae7c2ea6a9f5e72456b2491d2325),
[PathGui::ViewProviderPath::recomputeBoundingBox()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a4a681a533fc16dba93a80bc3fdfc21c3),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[Gui::ViewProviderDragger::setEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[Gui::ViewProviderDragger::setEditViewer()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5746c8658c714b1910627ea804ca2353),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[App::Origin::setupObject()](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[PartDesignGui::ViewProviderBody::slotChangedObjectApp()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac2b54ba3e85e13c4e5a63fe12dcc17bf),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
and
[PartDesign::ShapeBinder::updatedShape()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a126f8b03ab46e56d65b7fbd3d41b98e8).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/GeoFeature.h
  * FreeCAD/src/App/GeoFeature.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

