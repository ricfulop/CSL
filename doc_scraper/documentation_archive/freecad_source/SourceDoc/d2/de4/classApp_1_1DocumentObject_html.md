---
url: https://freecad.github.io/SourceDoc/d2/de4/classApp_1_1DocumentObject.html
scraped_at: 2025-09-08T14:54:16.753073
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)

[List of all members](../../df/dcd/classApp_1_1DocumentObject-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes | Static Public Attributes | Protected Member Functions | Protected Attributes | Friends

App::DocumentObject Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all Classes handled in the
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.").
[More...](../../d2/de4/classApp_1_1DocumentObject.html#details)

`#include <DocumentObject.h>`

##  Public Types  
  
---  
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
  
  
##  Static Public Attributes  
  
---  
static [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [StdReturn](../../d2/de4/classApp_1_1DocumentObject.html#af53a1c6a086c5dfe228aaefeeb7316d2)  
  
##  Protected Member Functions  
  
---  
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
  
  
##  Protected Attributes  
  
---  
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
  
##  Friends  
  
---  
class | [Document](../../d2/de4/classApp_1_1DocumentObject.html#a883538034e58fc5c0de7d4e4cab3cef7)  
class | [ObjectExecution](../../d2/de4/classApp_1_1DocumentObject.html#a01e7e682f5b7a471232611195fc88aab)  
class | [Transaction](../../d2/de4/classApp_1_1DocumentObject.html#a49982aa325e19f0956d42fde9132caa2)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
static const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [getPropertyDataPtr](../../d5/d48/classApp_1_1PropertyContainer.html#a8649f534ecaa91393925fa514ed29e4b) (void)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of all Classes handled in the
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.").

## Member Enumeration Documentation

## ◆ GSReason

enum
[App::DocumentObject::GSReason](../../d2/de4/classApp_1_1DocumentObject.html#a64b88e0a6bb28c2c6f7a6c43e81e1fcf)  
---  
  
reason of calling
[getSubObjects()](../../d2/de4/classApp_1_1DocumentObject.html#a43e45965f79f8e68bda39c77764b61a0
"Return name reference of all sub-objects.")

Enumerator  
---  
GS_DEFAULT | default, mostly for exporting shape objects   
GS_SELECT | for element selection   
  
## ◆ OutListOption

enum
[App::DocumentObject::OutListOption](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0c)  
---  
  
DAG handling This part of the interface deals with viewing the document as a
DAG (directed acyclic graph).

OutList options

Enumerator  
---  
OutListNoExpression | Do not include link from expression engine.   
OutListNoHidden | Do not hide any link (i.e. include links with LinkScopeHidden)   
OutListNoXLinked | Do not include link from [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html "Link to an \(sub\)object in the same or different document.").   
  
## Constructor & Destructor Documentation

## ◆ DocumentObject()

App::DocumentObject::DocumentObject  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Constructor.

## ◆ ~DocumentObject()

| virtual App::DocumentObject::~DocumentObject  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ addDynamicProperty()

| virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * App::DocumentObject::addDynamicProperty  | ( | const char *  | _type_ ,   
---|---|---|---  
|  | const char *  | _name_ = `nullptr`,   
|  | const char *  | _group_ = `nullptr`,   
|  | const char *  | _doc_ = `nullptr`,   
|  | short  | _attr_ = `0`,   
|  | [bool](../../d9/db9/classbool.html) | _ro_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _hidden_ = `false`  
| ) | |   
overridevirtual  
  
Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6).

Referenced by
[Spreadsheet::Sheet::setFloatProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a082ddc211d51376d6d8c3c77aa4a9bb2),
[Spreadsheet::Sheet::setIntegerProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a396a15ce1feb26825369fc32d38c028e),
[Spreadsheet::Sheet::setObjectProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a24ba012f7e01418a1ee0bd5992b7c117),
[Spreadsheet::Sheet::setQuantityProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1200f02d91cc685af952ac5c7d369010),
[Spreadsheet::Sheet::setStringProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a217878fa6e8ba03d534f5f22e44bce17),
and
[App::LinkBaseExtension::setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e).

## ◆ adjustRelativeLinks()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::adjustRelativeLinks  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_ ,   
---|---|---|---  
|  | std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > *  | _visited_ = `nullptr`  
| ) | |   
virtual  
  
Called to adjust link properties to avoid cyclic links.

Parameters

     inList| the recursive in-list of the future parent object, including the parent itself.   
---|---  
visited| optional set holding the visited objects. If null then only this
object is adjusted, or else all object inside the out-list of this object will
be checked.  
  
Returns

    Return whether the object has been modified

This function tries to adjust any relative link properties (i.e. link
properties that can hold subnames) to avoid cyclic when added to the future
parent.

## ◆ allowDuplicateLabel()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::allowDuplicateLabel  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
## ◆ canLinkProperties()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::canLinkProperties  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::Link](../../df/d9b/classApp_1_1Link.html#a58725fe3daf469f7baaa2a49c7dc4ea1),
and
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#aa3ecf46c1a1da9d3f60a35d78b8006e8).

Referenced by
[Gui::ViewProviderLink::getPropertyByName()](../../d6/d59/classGui_1_1ViewProviderLink.html#a17a9af10ec6818cb73aff3e1fdc9c5f7).

## ◆ canLoadPartial()

| virtual [int](../../d1/da0/classint.html) App::DocumentObject::canLoadPartial  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
allow partial loading of dependent objects

Returns

    Returns 0 means do not support partial loading. 1 means allow dependent objects to be partially loaded, i.e. only create, but not restored. 2 means this object itself can be partially loaded. 

Reimplemented in
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a0faf56fc6f85e668bb1128a8631e9a9a).

## ◆ clearExpression()

void App::DocumentObject::clearExpression  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |   
---|---|---|---|---|---  
  
## ◆ clearOutListCache()

void App::DocumentObject::clearOutListCache  | ( | | ) |  const  
---|---|---|---|---  
  
clear internal out list cache

## ◆ detachFromDocument()

| virtual const char * App::DocumentObject::detachFromDocument  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html#a17f7538441e315b11eca8ebc047e11f4).

## ◆ enforceRecompute()

void App::DocumentObject::enforceRecompute  | ( | | ) |   
---|---|---|---|---  
  
Enforce this document object to be recomputed.

Referenced by
[Gui::TreeWidget::onMarkRecompute()](../../de/de0/classGui_1_1TreeWidget.html#a5820ccc25f0837a62eb180509d3c75fb),
and
[TechDraw::DrawViewDimExtent::unsetupObject()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#abc5c45571551383c8db0194bec4bcec6).

## ◆ execute()

| virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * App::DocumentObject::execute  | ( | void  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
get called by the document to recompute this feature Normally this method get
called in the processing of
[Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b
"Recompute touched features and return the number of recalculated features.").

In
[execute()](../../d2/de4/classApp_1_1DocumentObject.html#addd0e28aebe720807dd5c1f6790fe752
"get called by the document to recompute this feature Normally this method get
called in the processin...") the output properties get recomputed with the
data from linked objects and objects own properties.

Reimplemented in
[Fem::Constraint](../../d0/d11/classFem_1_1Constraint.html#ac7343ea84455e2331eecd8aab10b38ac),
[Mesh::Curvature](../../d2/d39/classMesh_1_1Curvature.html#a76bfebcb28cee108275564ade910411c),
[Mesh::FixDefects](../../d4/d1f/classMesh_1_1FixDefects.html#a91ee486eafe50bffa50981b6ee1919bb),
[Mesh::HarmonizeNormals](../../d8/d1c/classMesh_1_1HarmonizeNormals.html#a7f4d3c74b5c71fcb87e8467ae09a78f0),
[Mesh::FlipNormals](../../d3/d05/classMesh_1_1FlipNormals.html#a781c0a4c289cd3fecb312a743d04c2a6),
[Mesh::FixNonManifolds](../../d5/d33/classMesh_1_1FixNonManifolds.html#a1ee7ec392eeb5cb3a206989d21b3e3bc),
[Mesh::FixDuplicatedFaces](../../d9/d63/classMesh_1_1FixDuplicatedFaces.html#affadc4a69ba22744612248e94059ea13),
[Mesh::FixDuplicatedPoints](../../d1/d7b/classMesh_1_1FixDuplicatedPoints.html#abb108a05948e9906cefd394da59fdf77),
[Mesh::FixDegenerations](../../db/d8f/classMesh_1_1FixDegenerations.html#a3425c9ffba4deeb1c73c7fe910429687),
[Mesh::FixDeformations](../../d1/dbc/classMesh_1_1FixDeformations.html#a8c0ddd5b2e77c30a2466dc1fd08cdc7a),
[Mesh::FixIndices](../../d3/deb/classMesh_1_1FixIndices.html#a83eddf2883e3fc904c150d124d8aa01f),
[Mesh::FillHoles](../../d2/ddd/classMesh_1_1FillHoles.html#a21a0e0e99c2dcd82f9918fe67def820b),
[Mesh::RemoveComponents](../../da/d7a/classMesh_1_1RemoveComponents.html#a552facf8870d9ef3b36e1dee379fac07),
[Mesh::Export](../../d6/d40/classMesh_1_1Export.html#a56265dded005a8be13258af1b273ed51),
[Mesh::Import](../../d9/d29/classMesh_1_1Import.html#a744e663c172c1174c37b363372a377b2),
[Mesh::SegmentByMesh](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[Mesh::SetOperations](../../d3/d8f/classMesh_1_1SetOperations.html#a5fbee709af3e7da8f267824be4c4b370),
[Mesh::Sphere](../../d1/d57/classMesh_1_1Sphere.html#ae830b723d9c2977e6080c9e87f3ec139),
[Mesh::Ellipsoid](../../d2/dd6/classMesh_1_1Ellipsoid.html#aa7094fc5c9ce3b03b37b1875e8962b68),
[Mesh::Cylinder](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[Mesh::Torus](../../de/da3/classMesh_1_1Torus.html#a9ca70ccb5548f0852b54fe55f58f27a9),
[Mesh::Cube](../../df/d68/classMesh_1_1Cube.html#a5c7921255a963127e0496b550023f3ed),
[Mesh::Transform](../../d3/def/classMesh_1_1Transform.html#a28b6499af9da72410435606375790c1b),
[Mesh::TransformDemolding](../../dc/da9/classMesh_1_1TransformDemolding.html#abca1f141e3599f6b718d1fcbafe07c51),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a1e5ce1fb233e1b7820af42cc6758fd9f),
[PartDesign::Pad](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a1e5ce1fb233e1b7820af42cc6758fd9f),
[Points::Structured](../../d0/d43/classPoints_1_1Structured.html#a777464aea8c27ad6f8c525fb1f8ce15c),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#ac06f7886d25ae7ef0e9e635904f7997c),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a367993c31e3a6f1b62d5b93a3de0fa89),
[App::FeatureTest](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[App::FeatureTestException](../../d5/d03/classApp_1_1FeatureTestException.html#a0babd1351bb727499275331259686e29),
[App::InventorObject](../../da/d11/classApp_1_1InventorObject.html#abf0ce1809171c736570be0f9272c8af0),
[App::MeasureDistance](../../d7/d61/classApp_1_1MeasureDistance.html#aa328f58f37764c36e03ee8356325ea72),
[App::Origin](../../d9/d8b/classApp_1_1Origin.html#ae8015373defe4fb60c2a44da46721c84),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#aa3d59e0392a0bf8b954916fe8a502008),
[Drawing::FeatureClip](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Drawing::FeatureProjection](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureView](../../db/d1f/classDrawing_1_1FeatureView.html#a6722811fbd5b8e5dafc809cb147e38ba),
[Drawing::FeatureViewAnnotation](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewPart](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Drawing::FeatureViewSymbol](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a3563b4ff57807e29d705c04a53b7cd0b),
[Fem::ConstraintBearing](../../df/d0a/classFem_1_1ConstraintBearing.html#a7f4a7dfe1c4f001e52ad1720ebc4ed84),
[Fem::ConstraintContact](../../db/d7c/classFem_1_1ConstraintContact.html#a2b07cec1999129143ccd1b45fc9eeddc),
[Fem::ConstraintDisplacement](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a38ee9c197d477eca27db652614ae694a),
[Fem::ConstraintFixed](../../d1/d43/classFem_1_1ConstraintFixed.html#a6506e57dae27c9e9c105f4da75f3c3e9),
[Fem::ConstraintFluidBoundary](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#ad36bc34fcb1c89b7df0139ca1380fadb),
[Fem::ConstraintForce](../../d6/d63/classFem_1_1ConstraintForce.html#a626c09f37f1306d05a2bec3d8e19cf72),
[Fem::ConstraintGear](../../d8/d55/classFem_1_1ConstraintGear.html#a9e64f77db3ad6d0c15bb4d9629787292),
[Fem::ConstraintHeatflux](../../de/dce/classFem_1_1ConstraintHeatflux.html#ac6c7cd303380c8ea71bc8346c779be39),
[Fem::ConstraintInitialTemperature](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#ad405a46cb5b94406450e7ef0543d7c70),
[Fem::ConstraintPlaneRotation](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#ad83df18c7b020e77602c3a5be124f116),
[Fem::ConstraintPressure](../../dd/d5e/classFem_1_1ConstraintPressure.html#a07aad2f68fbdc96f761bcea906b4d28b),
[Fem::ConstraintPulley](../../d3/dec/classFem_1_1ConstraintPulley.html#a6770a31003eb8044b87d6147d828363c),
[Fem::ConstraintSpring](../../dc/d42/classFem_1_1ConstraintSpring.html#a66e86d9afaddfe681836973771400b08),
[Fem::ConstraintTemperature](../../d7/dff/classFem_1_1ConstraintTemperature.html#a0faba731da75766244414cc1a611c23f),
[Fem::ConstraintTransform](../../d8/d3c/classFem_1_1ConstraintTransform.html#a19e8c792ec5f8284c205f19ac15ef2ee),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#a63d3834bf66491db7b4f30f315f01dfb),
[Fem::FemMeshShapeNetgenObject](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Fem::FemMeshShapeObject](../../d0/d41/classFem_1_1FemMeshShapeObject.html#a52f6bff1d5da5dc0dc05d3d0a4a90e72),
[Fem::FemPostFilter](../../d8/d6f/classFem_1_1FemPostFilter.html#a6e243a1e127e9f99d015051d8ea5a8a7),
[Fem::FemPostClipFilter](../../dc/d06/classFem_1_1FemPostClipFilter.html#a11a328bac4a9ae22ba01e4696484ae06),
[Fem::FemPostDataAlongLineFilter](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#a9b411212fee9174b28bdf4a9fdbd9381),
[Fem::FemPostDataAtPointFilter](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a4f8624735a8705e58247fb9df7a7d6e5),
[Fem::FemPostScalarClipFilter](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
[Fem::FemPostCutFilter](../../da/d89/classFem_1_1FemPostCutFilter.html#a9ff7e939e5c3dc07c73dfe1a569e32d7),
[Fem::FemPostFunction](../../d3/d87/classFem_1_1FemPostFunction.html#a0227f858c3fbccc02f9574d9bcc3a621),
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a37a7074a69af004117f82d72be1701f8),
[Fem::FemResultObject](../../d3/d81/classFem_1_1FemResultObject.html#a0e4f90351e9ce40455801a43f9538e10),
[Fem::FemSetElementsObject](../../df/d49/classFem_1_1FemSetElementsObject.html#a3f567e9193f8d49bd542312ef5e6860f),
[Fem::FemSetFacesObject](../../df/d72/classFem_1_1FemSetFacesObject.html#a46ab2fff61403128815b2cb9b22314e6),
[Fem::FemSetGeometryObject](../../df/d59/classFem_1_1FemSetGeometryObject.html#a608e2e0fdf7c34beab9dbc7b01e6d66e),
[Fem::FemSetNodesObject](../../dc/d59/classFem_1_1FemSetNodesObject.html#a8d55585de3533d3b751f2724981d23e9),
[Fem::FemSetObject](../../d8/dbe/classFem_1_1FemSetObject.html#ae30787859238309a6dae394e902a1968),
[Fem::FemSolverObject](../../d1/dd0/classFem_1_1FemSolverObject.html#aef99c067ac336a7ad345866fa38c3046),
[Inspection::Feature](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Part::CustomFeature](../../da/d46/classPart_1_1CustomFeature.html#a2fe501793eddc0400a6f97b9e7af7a79),
[Part::Chamfer](../../d7/d75/classPart_1_1Chamfer.html#a4e556c2713a9af1290a0c53eeedff2f1),
[Part::Compound](../../d7/d98/classPart_1_1Compound.html#a72d02534883bc8e2b7ccb46218e87087),
[Part::Fillet](../../d4/da4/classPart_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[Part::FeatureGeometrySet](../../d6/d80/classPart_1_1FeatureGeometrySet.html#acbc44d2989a0a94e14b5100a50a1fa7f),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[Part::Boolean](../../da/d3a/classPart_1_1Boolean.html#ab93d1734459a414d09ccec9df8df7831),
[Part::Box](../../dc/d80/classPart_1_1Box.html#a69ab4139d085049cababf9b1692cf32d),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#a5353d0accb2b7c67b656632ebc23952a),
[Part::MultiCommon](../../d1/df7/classPart_1_1MultiCommon.html#ab89bf89ceaef91d77ba170a7e548040d),
[Part::CurveNet](../../d9/d41/classPart_1_1CurveNet.html#ab3d3703fdaab33d94b764c62d6739ce6),
[Part::MultiFuse](../../df/dbc/classPart_1_1MultiFuse.html#affac0f86cba2c15642f4d8a64a01c337),
[Part::ImportBrep](../../d8/d3e/classPart_1_1ImportBrep.html#a3fbd619fb350dff418fffd6b6f185ca7),
[Part::ImportIges](../../d2/d1d/classPart_1_1ImportIges.html#a1d947e212fdeb8ed2b8bb8ef3fae1041),
[Part::ImportStep](../../d4/de2/classPart_1_1ImportStep.html#a3c81f94deddd927756144ef4e8040678),
[Part::Polygon](../../d3/db3/classPart_1_1Polygon.html#ad32a5f75f338c91f0da7ae8da871956d),
[Part::FeatureReference](../../d2/da1/classPart_1_1FeatureReference.html#ae5a6fd5ceb91026f2ed196b23127ef02),
[Part::RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html#aaff86f64ccc1eeeb1158727285cacab0),
[Part::Loft](../../d3/d52/classPart_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[Part::Sweep](../../df/dc6/classPart_1_1Sweep.html#a7fdf28d346eb1b3b838ed0dea5bb40d8),
[Part::Thickness](../../db/d73/classPart_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Part::Refine](../../d4/d0a/classPart_1_1Refine.html#aa138404bf1cbb4270a6e4a9d02dffac7),
[Part::Reverse](../../d4/d24/classPart_1_1Reverse.html#a22150a83fa78387e05f60dd1e08d31f8),
[Part::Vertex](../../de/d96/classPart_1_1Vertex.html#a7f12d1239e070829c3743d2332687312),
[Part::Line](../../d3/dfe/classPart_1_1Line.html#a8a26cfef78179c3a17428b413ee487c8),
[Part::Plane](../../d0/d1c/classPart_1_1Plane.html#a92e30b6f8e6e4524886e10623f383ccf),
[Part::Sphere](../../dc/d57/classPart_1_1Sphere.html#aa2804abc812bb4e89a84ea2da733cb7a),
[Part::Ellipsoid](../../d4/dc8/classPart_1_1Ellipsoid.html#a1de2ad502eba83e4f20716aa3b81aced),
[Part::Cylinder](../../dd/d12/classPart_1_1Cylinder.html#abca3126f8a79336ae295c92cc4512e8d),
[Part::Prism](../../dc/d69/classPart_1_1Prism.html#aee3abdd806303810dee9bcb407871e8e),
[Part::RegularPolygon](../../d2/d69/classPart_1_1RegularPolygon.html#ab826050ea7815c765e6f0615554e01f0),
[Part::Cone](../../d2/d8f/classPart_1_1Cone.html#a9b18609878daf577bf7fd4cd4646ade0),
[Part::Torus](../../db/d42/classPart_1_1Torus.html#afcaa637ebac3164019e7dcb9bf15a800),
[Part::Helix](../../df/d49/classPart_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[Part::Spiral](../../d2/d3f/classPart_1_1Spiral.html#a3c18221bf2911fbbb3d36d7ace6e2215),
[Part::Wedge](../../d5/dc5/classPart_1_1Wedge.html#aaae12d496990fab3b982bbd54e79aa10),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#ac17650b02feac6d7001b52dad51c0803),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a7cc09059c368f65475f0fa3f05bc06f5),
[PartDesign::Draft](../../df/d0e/classPartDesign_1_1Draft.html#a222432999c8964780ed57beb4aeb8484),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[PartDesign::Groove](../../d7/de3/classPartDesign_1_1Groove.html#a0f3365a4df79cd6d9ec8137b32c9530c),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[PartDesign::Loft](../../d0/deb/classPartDesign_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Pipe](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[PartDesign::Box](../../df/d97/classPartDesign_1_1Box.html#a91f171c242cb7c31d3381981af2fab95),
[PartDesign::Cylinder](../../dc/d28/classPartDesign_1_1Cylinder.html#ab62f3f3e2d1c87dd9c4073378f2ca916),
[PartDesign::Sphere](../../db/d9d/classPartDesign_1_1Sphere.html#aeef6f98884ffd7532acd0274c29b1e8f),
[PartDesign::Cone](../../d4/d2b/classPartDesign_1_1Cone.html#a242c7c4d99e524f88ffca87982764ddf),
[PartDesign::Ellipsoid](../../d4/de1/classPartDesign_1_1Ellipsoid.html#abe018702f319a19bfd7faaba06b60109),
[PartDesign::Torus](../../dd/de1/classPartDesign_1_1Torus.html#a0fe8ad351f212fb151f6aab09438c4fd),
[PartDesign::Prism](../../d9/daf/classPartDesign_1_1Prism.html#afbe0d9e86e58c4781f3f58aed9371937),
[PartDesign::Wedge](../../dc/dd3/classPartDesign_1_1Wedge.html#aea929c12fd19cab20657b5dc80ced3ac),
[PartDesign::Revolution](../../d2/de6/classPartDesign_1_1Revolution.html#a1e5564f51ec710663a8002d5018b76f8),
[PartDesign::Thickness](../../d4/d22/classPartDesign_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[PartDesign::Transformed](../../dd/de1/classPartDesign_1_1Transformed.html#aef9667071a3f6bb2ed13226f84629049),
[Path::FeatureArea](../../da/d1e/classPath_1_1FeatureArea.html#af00ad2b6bd7ffa0f8db73f7b51b94fbc),
[Path::FeatureAreaView](../../d3/db4/classPath_1_1FeatureAreaView.html#a181be122ea1283aac8cb22d51edc5686),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#a80d4fdf2e0a09f51601c94668dda3ca1),
[Path::FeatureCompound](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[Path::FeatureShape](../../da/d9b/classPath_1_1FeatureShape.html#a62d47b3cb3d7ed9081cdfc0966c71c3e),
[Raytracing::LuxFeature](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::LuxProject](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayFeature](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Raytracing::RayProject](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[Raytracing::RaySegment](../../d5/d48/classRaytracing_1_1RaySegment.html#ab940ed0d8627d391c3be83800c98698c),
[Robot::Edge2TracObject](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a02d0871e02dcf31317ff7ef811980483),
[Robot::TrajectoryCompound](../../df/de7/classRobot_1_1TrajectoryCompound.html#a230683c181418d56d66a986fe5063a3a),
[Robot::TrajectoryDressUpObject](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#ad727a9f54b00d87767a06e1aec3f9044),
[Sandbox::SandboxObject](../../da/dd9/classSandbox_1_1SandboxObject.html#a96b3044625736c856e807edd11e1bc00),
[Sketcher::SketchObjectSF](../../de/da4/classSketcher_1_1SketchObjectSF.html#aee2e5bb2b2aa00817df40cae0574ef36),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#ae374761fddb3f1531d4bd1af5c7b5b49),
[Surface::Cut](../../d4/d17/classSurface_1_1Cut.html#adade24c19d386572d09157489463f785),
[Surface::Filling](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[Surface::GeomFillSurface](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a84b55d39b731f625753852ddf3672072),
[Surface::Sewing](../../d2/d52/classSurface_1_1Sewing.html#a956109125cae787085423aeb93d8e1f3),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#acc1380e0737504ec1d64b2bbca2380e6),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a69829b351153268971271cd16fb5db52),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a67d8e151c886e0ef62f246cc3a4e5ff6),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a0091941d975f15478b21d940f4c1c54c),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a1e7d8093bcb39741374d37ae57b20523),
[TechDraw::DrawViewAnnotation](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#ab6d06ddd594f58d6bb31ce52a1452a32),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a31cd0c2306b266d607e29672b3825340),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#abd5332c355e8d23d52ba435c1ba3f855),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[TechDraw::DrawViewSpreadsheet](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a2d98f05816771e2b3a057443ea2f981c),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aa63b811c7325f38b1e58840b28d8ab7d),
[TechDraw::FeatureProjection](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Part::Extrusion](../../db/d6c/classPart_1_1Extrusion.html#ab84ba0c7cd3edeec76deb2fda5303115),
[Part::Face](../../dc/dbf/classPart_1_1Face.html#a7e0c10e1928c118064cc40586322ca36),
[Part::Offset](../../d0/dda/classPart_1_1Offset.html#a342f29a6b5381db240304b9384b313dd),
[Part::Offset2D](../../d7/dcf/classPart_1_1Offset2D.html#a3eb29bb0e6404263cb3470d7ec24ea4a),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#af372e896d1d48e319db937ae1bea2bbe),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#a5ca90cc8f3599cae1a527ce96e737489),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a4abca6b2645adade81347d0e850a2659),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#a471715716cd89abfe18b9f50b7728567),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a3fc5f1e2196c59afb44e876fd05d4710),
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a2886a69e9359a73fe242378c2a7b5a27),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ae9fb1ae7a1f62e3c44879de5f6f752a9),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a06d72232cfde4ef56fd23515cf8434c4),
[Surface::Extend](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[Surface::Sections](../../d7/d6e/classSurface_1_1Sections.html#a2c9525c3b5343d49da189cd26cd2ad4e),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a8860cb23b43c1eb064578e2f50614c05),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#abc909fae985f572927d821cfb03bd3ee),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#ab5f621c70c32624c24f354f23fb2e5c3),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#aebc26d607949672b7102fc42b102edd4),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53036ad3632d51fe082b67c8f829b54f),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1afd35db151cf4ec222427f08a4f3c2a),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#a43e7256f0d0a0c60c90ed90e0e3db759),
[TechDraw::DrawViewArch](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a65223c44c0e0802569d6e8ffc102f843),
[TechDraw::DrawViewDetail](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewDraft](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewImage](../../d0/d87/classTechDraw_1_1DrawViewImage.html#af5ef1e9ad4c2d1efa858730548f9a83a),
[TechDraw::DrawViewMulti](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
and
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a628476bf5d4492109e6d1e947c15aa6d).

Referenced by
[draftobjects.facebinder.Facebinder::addSubobjects()](../../d9/d57/classdraftobjects_1_1facebinder_1_1Facebinder.html#a50c77c202a034ce7109bb93322ff6e4e),
[PathScripts.PathDressupDogbone.ObjectDressup::boneStateList()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#af7788dd97e3ca711047ebc4472cf9f21),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[App::Origin::execute()](../../d9/d8b/classApp_1_1Origin.html#ae8015373defe4fb60c2a44da46721c84),
[Fem::FemPostPipeline::execute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a37a7074a69af004117f82d72be1701f8),
[TechDraw::DrawTemplate::execute()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a67d8e151c886e0ef62f246cc3a4e5ff6),
[TechDraw::DrawPage::execute()](../../d9/d5a/classTechDraw_1_1DrawPage.html#aebc26d607949672b7102fc42b102edd4),
[TechDraw::DrawView::execute()](../../d6/d1c/classTechDraw_1_1DrawView.html#a43e7256f0d0a0c60c90ed90e0e3db759),
[TechDraw::DrawViewBalloon::execute()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a65223c44c0e0802569d6e8ffc102f843),
[PathScripts.PathDressupHoldingTags.ObjectTagDressup::generateTags()](../../de/dd2/classPathScripts_1_1PathDressupHoldingTags_1_1ObjectTagDressup.html#a0937c170df6457d4d7aa799c876584ae),
[ArchPanel.PanelCut::getWires()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a61534af5c2a0125dde05e08a22025195),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[Mod.PartDesign.Scripts.DistanceBolt.DistanceBolt::onChanged()](../../d8/d9d/classMod_1_1PartDesign_1_1Scripts_1_1DistanceBolt_1_1DistanceBolt.html#a5899c4fe94fa654ae168588d09ec3674),
[Mod.PartDesign.Scripts.Epitrochoid.Epitrochoid::onChanged()](../../da/d92/classMod_1_1PartDesign_1_1Scripts_1_1Epitrochoid_1_1Epitrochoid.html#a666d03d55a3758fd5b580ecdf83ff046),
[Mod.PartDesign.Scripts.Parallelepiped.Parallelepiped::onChanged()](../../da/db1/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1Parallelepiped.html#a7d58a665dbdb613ccf9830254b6b3a28),
[Mod.PartDesign.Scripts.Parallelepiped.BoxCylinder::onChanged()](../../dc/dc9/classMod_1_1PartDesign_1_1Scripts_1_1Parallelepiped_1_1BoxCylinder.html#a32f2314f8a81f2034ba5fb8902079e75),
[Mod.PartDesign.Scripts.Spring.MySpring::onChanged()](../../d3/d4c/classMod_1_1PartDesign_1_1Scripts_1_1Spring_1_1MySpring.html#a45b49877108608c2473da154cbf7980d),
[FeaturePython.DistanceBolt::onChanged()](../../d9/d7d/classFeaturePython_1_1DistanceBolt.html#a644c14797e2ed9043537de3c86f7fdf1),
[PathScripts.PathStock.StockFromBase::onChanged()](../../d1/d74/classPathScripts_1_1PathStock_1_1StockFromBase.html#a2c3dfa73d2881d73e95ac79cb572e9b9),
[PathScripts.PathStock.StockCreateBox::onChanged()](../../d9/dd6/classPathScripts_1_1PathStock_1_1StockCreateBox.html#ae190342a16a7a1c726c7748b85bc36d7),
[PathScripts.PathStock.StockCreateCylinder::onChanged()](../../da/de2/classPathScripts_1_1PathStock_1_1StockCreateCylinder.html#aaee43a8f62bd342d2b16ff4268dd33c9),
[draftobjects.draftlink.DraftLink::onDocumentRestored()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#ac93069a613e26475296ba7eba274a783),
[draftobjects.patharray.PathArray::onDocumentRestored()](../../de/dbe/classdraftobjects_1_1patharray_1_1PathArray.html#a6a3f3b5a3444a8e2bc12d61152100fd5),
and
[draftobjects.pathtwistedarray.PathTwistedArray::onDocumentRestored()](../../da/d1a/classdraftobjects_1_1pathtwistedarray_1_1PathTwistedArray.html#a780c1e365112f239b177875caa78103b).

## ◆ executeExtensions()

| [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * App::DocumentObject::executeExtensions  | ( | | ) |   
---|---|---|---|---  
protected  
  
Executes the extensions of a document object.

## ◆ getDocument()

[App::Document](../../d8/d3e/classApp_1_1Document.html) * App::DocumentObject::getDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
gets the document in which this Object is handled

Referenced by
[PartGui::FaceColors::accept()](../../db/d9e/classPartGui_1_1FaceColors.html#ad523c552641c93f9f457961ac51d6c38),
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06),
[PartDesignGui::TaskShapeBinder::accept()](../../d0/d2a/classPartDesignGui_1_1TaskShapeBinder.html#a5881c04fc2f30c53555576224fab3d45),
[PathGui::TaskDlgPathCompound::accept()](../../d0/d93/classPathGui_1_1TaskDlgPathCompound.html#a9b21fa4e4a95ed2b50942ac6c6adece6),
[SpreadsheetGui::DlgBindSheet::accept()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#ad6e5cb0995aaa1341a57bdb97ed49cbd),
[TechDrawGui::TaskCenterLine::accept()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a9c153de90151c4f08e9551a71213824f),
[TechDrawGui::TaskCosVertex::accept()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#ac0c6878d9764252e09f41414b44d1dd8),
[TechDrawGui::TaskDetail::accept()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#afe9aa4fe7d3b9a78a220789dbae74503),
[TechDrawGui::TaskLeaderLine::accept()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0bd9ba957974bcb35e2fd830a39b75ed),
[TechDrawGui::TaskLineDecor::accept()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#ab3f35f96c2ddd6e3e6fc4780c6be1ed1),
[TechDrawGui::TaskProjGroup::accept()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a73028edf767f28a1bdb160db31d82c44),
[TechDrawGui::TaskRichAnno::accept()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a99073745441f60a87521b744d89803d4),
[Gui::TaskCSysDragger::accept()](../../d2/dff/classGui_1_1TaskCSysDragger.html#ad513cbcf32b69dc11ee35b96cc6a2a64),
[PartGui::DlgPrimitives::accept()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a1db668afa4bde5626f25c5e34f596b82),
[PartDesignGui::TaskDressUpParameters::addAllEdges()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a8b48e7bad7912d3f55e3466bae38ab80),
[Gui::ViewProviderDocumentObject::addDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a0b66cab9ff390bb91593786721612aef),
[Sketcher::SketchObject::addExternal()](../../d9/dad/classSketcher_1_1SketchObject.html#a700c729d94352b4b144eb083980a702c),
[PartDesignGui::ComboLinks::addLink()](../../d8/df8/classPartDesignGui_1_1ComboLinks.html#a9517d700acdde45e4610fdfda7f0c41d),
[App::GroupExtension::addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a77502422ab7bde4fb01ab4474fd930af),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[App::PropertyLinkSubList::adjustLink()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525),
[PartDesignGui::ReferenceSelection::allow()](../../dd/d1c/classPartDesignGui_1_1ReferenceSelection.html#aba5a74db909e196f326ebb626e1ba150),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[Gui::ViewProviderAnnotation::attach()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#ab50892bdc3b37f9da77b36cac3014cf6),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[MeshGui::ViewProviderMesh::attach()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#adb9b6c0cd97337657aabd81bac13e35e),
[PointsGui::ViewProviderScattered::attach()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab6910e935629c8fe18fed5409c9521a0),
[PointsGui::ViewProviderStructured::attach()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#aabe6e709079ef4dd2d44b687db5f1dd7),
[PartDesignGui::ViewProviderBody::attach()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a12e5a7b4da5cecd7fe82062ad9051176),
[MeshGui::ViewProviderMeshCurvature::attach()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad36ed9ef7edb7c4ec98d622ec6acf48c),
[Gui::ViewProviderVRMLObject::attach()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a6325dc25a3b586202db6edaf20319937),
[RobotGui::ViewProviderRobotObject::attach()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#abfd62beacd9f9981515c67a20b27e813),
[RobotGui::ViewProviderTrajectory::attach()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#ae0c77a17efe78de9f375f9382cc40da2),
[Sketcher::SketchAnalysis::autoconstraint()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#a593a8426260651db5e7a7fc942b9a647),
[Gui::ExpressionBinding::bind()](../../dc/d5a/classGui_1_1ExpressionBinding.html#aba7b2c918c04b6e3f589e53876cdb761),
[Gui::ViewProviderLink::canDragAndDropObject()](../../d6/d59/classGui_1_1ViewProviderLink.html#a9efaffd7b4c0794b9a0ea98256d56852),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[App::LinkBaseExtension::checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[PartDesign::SubShapeBinder::checkCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3698bc706a89765ff35db75048a08698),
[App::LinkBaseExtension::checkGeoElementMap()](../../da/dd9/classApp_1_1LinkBaseExtension.html#ad6ede45b16c53f9facd69b1ed5ae10e1),
[App::ObjectIdentifier::String::checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f),
[SpreadsheetGui::SheetView::confirmAliasChanged()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#a417a33ce8aa3a831fed85c08876f84ba),
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[Gui::DAG::Model::contextMenuEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a929350aab7c7acb610a7d61bdcc644b6),
[App::PropertyXLink::copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::QGSPage::createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[TechDrawGui::TaskHatch::createHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ac9d417f22f5d5ed524f63d10cd4e63ef),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[TechDrawGui::TaskSectionView::createSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ac5902eeba616fd351e4de4546c7634de),
[TechDrawGui::TaskWeldingSymbol::createWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a687a7f75b421ef414ad8e8ae46dc7889),
[Gui::ViewProviderIndex::data()](../../d7/d9c/classGui_1_1ViewProviderIndex.html#a3c14909891014378c66da5b320b18214),
[SpreadsheetGui::DlgBindSheet::DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[PartDesignGui::ViewProviderBody::dropObject()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[Gui::ViewProviderOriginGroupExtension::extensionAttach()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#ae4e983b8437ebedcf3d8b82b3c4997ae),
[App::LinkBaseExtension::extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42),
[Gui::ViewProviderDocumentObject::findFrontRootOfType()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a078851e515af6065c4daeaa5f2fc654f),
[PartDesignGui::fixSketchSupport()](../../dc/d12/namespacePartDesignGui.html#a36c5ac55a4ecca36c64de785d462622a),
[Gui::ViewProviderDocumentObject::getActiveView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a9b5544179260b0a76bb265d68b79a86c),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[Gui::ViewProviderDocumentObject::getDocument()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a56bcfaa3c9490e15a59db842db78a2bb),
[Gui::ViewProviderDocumentObject::getEditingView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a28d48c52ec13ce0ea2b76a49c28188c8),
[PartDesignGui::TaskSketchBasedParameters::getFaceReference()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#adf889644d1a1d0919364029e1837faab),
[TechDrawGui::QGIView::getFrameState()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a0b7fa2dee63d2615502c7605bec81161),
[InspectionGui::ViewProviderInspection::getIcon()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a76d57438c1350bd9a432557f0c23dc5e),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[Gui::ViewProviderDocumentObject::getInventorView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a158c53de5a387702d0813bb8c044e94a),
[PartDesignGui::TaskDraftParameters::getLine()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#ac4b37f7ab747d85db228cfc413131022),
[App::GroupExtension::getObject()](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1),
[App::OriginFeature::getOrigin()](../../da/dfe/classApp_1_1OriginFeature.html#ae153618f0361a30dd55b8b0f21294cfa),
[PartDesignGui::getPartFor()](../../dc/d12/namespacePartDesignGui.html#aa97e68f5d6560bdaaad701f3cfe50dc4),
[PartDesignGui::TaskDraftParameters::getPlane()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#a721ea370a65705cc8585ed07b1479839),
[App::PropertyLinkSubList::getPyReprString()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac644eeeab4af18d5ec980d4f9640fe3b),
[App::PropertyXLinkSubList::getPyReprString()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a49dc28e937c8ffb0a0739ee83deaeb0a),
[PartDesignGui::TaskExtrudeParameters::getReferenceAxis()](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#afe979e086d9b00ec0c5dce152180b17e),
[PartDesignGui::TaskHelixParameters::getReferenceAxis()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#a5300ff77122113e8bd182eaf761db892),
[PartDesignGui::TaskRevolutionParameters::getReferenceAxis()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#ae93d24dcfea0ba9559c889738d3d3770),
[PartDesignGui::getReferencedSelection()](../../dc/d12/namespacePartDesignGui.html#a3f00fb1f14bb1e8917fe623cecd8ab59),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ab70e87f8a87a50222337b00c4ef6d945),
[TechDraw::DrawViewPart::getSourceShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aeb0d7bbe7418b86053f38713d4c91fa9),
[TechDraw::DrawViewPart::getSourceShapeFused()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a259e1a941c8e6a0651089bfa4111e3bd),
[Gui::ViewProviderDocumentObject::getViewOfNode()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a3283b0144b4a8641abc652164c882e48),
[PartDesign::ProfileBased::handleChangedPropertyName()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[App::Expression::importSubNames()](../../dc/d5c/classApp_1_1Expression.html#a6b338d5ca7344c41547dfe77019cf1e1),
[App::ObjectIdentifier::importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[PartDesignGui::TaskTransformedParameters::indexesMoved()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#a3b5b194d9abce483eb434ae97ede1fac),
[Spreadsheet::PropertySheet::insertColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a265014a33975e005189793fb75251c56),
[Spreadsheet::PropertySheet::insertRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa84f3f19aed8b5355d16cece5eb4a5d9),
[PartDesignGui::isAnyNonPartDesignLinksTo()](../../dc/d12/namespacePartDesignGui.html#a763622795328f1193ce61804dc4c61b6),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
[Sketcher::SketchObject::isExternalAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a15854bee280f512f617c7f34752ab823),
[Gui::SelectionSingleton::isSelected()](../../d4/dca/classGui_1_1SelectionSingleton.html#a821a5d7843e3c3c08e9d6244b4d21e1d),
[TechDrawGui::TaskLinkDim::loadAvailDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a3e6b427c8a0b62b4199b25d3eb07f58b),
[MeshGui::RemeshGmsh::loadOutput()](../../dd/d1b/classMeshGui_1_1RemeshGmsh.html#ae2d3d4b0bb6bf0fecd761bf42cd6fb42),
[PartDesignGui::makeBodyActive()](../../dc/d12/namespacePartDesignGui.html#ae1d1f749c569f8feca9b77df909ef722),
[App::LinkBaseExtension::makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[TechDraw::DrawDimHelper::makeDistDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#abbb31fd885c91f55267b7f8fd3945c1a),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[Gui::DAG::Model::mouseDoubleClickEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a70763eeb9c1afbd8a87f81d112f6e2b7),
[Gui::DAG::Model::mousePressEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a5507e79687e92d89464f8b95181bb4e5),
[PartDesignGui::TaskSketchBasedParameters::objectNameByLabel()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#ad328afbf02d22bd34087d9038e644c49),
[SketcherGui::TaskSketcherConstraints::on_listWidgetConstraints_itemSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#a9dfd693a935f64423cc9106430776263),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemEntered()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a2e956e6abd25667f7e59514a401b0f42),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a56cc69945924032683b1845683b9873b),
[MeshGui::DlgEvaluateMeshImp::on_repairAllTogether_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a37ba0babe8914d5dce379504b9adf12e),
[MeshGui::DlgEvaluateMeshImp::on_repairDegeneratedButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ab3cdbd594788a57c256755a837018d2f),
[MeshGui::DlgEvaluateMeshImp::on_repairDuplicatedFacesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aede555d793810d6cfc2632ecf409e5fa),
[MeshGui::DlgEvaluateMeshImp::on_repairDuplicatedPointsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aef057c023433bea4e835ee2e61dd0d17),
[MeshGui::DlgEvaluateMeshImp::on_repairFoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a492d611b70e28517f204bf25bf76184e),
[MeshGui::DlgEvaluateMeshImp::on_repairIndicesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a3da19b67de1065f6efa4da4a159d9e97),
[MeshGui::DlgEvaluateMeshImp::on_repairNonmanifoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a515dab5e6ea530b164559c860252bfae),
[MeshGui::DlgEvaluateMeshImp::on_repairOrientationButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a69c2e5330dbce392a37614ce7e27d7fe),
[MeshGui::DlgEvaluateMeshImp::on_repairSelfIntersectionButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#acd921ad6e7470851387f97162ff6e288),
[PartDesignGui::TaskSketchBasedParameters::onAddSelection()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#a21b691abf9e5be5455e3321bd7e5165a),
[PartDesignGui::TaskBoxPrimitives::onBoxHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a107f8b74cdb3bf1a45ed032a9aaf383d),
[PartDesignGui::TaskBoxPrimitives::onBoxLengthChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#abf84392ef886c69cd8a222960378acc5),
[PartDesignGui::TaskBoxPrimitives::onBoxWidthChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa371979bffbc04a3a8e1ad0a927cef13),
[FemGui::TaskFemConstraint::onButtonWizCancel()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a40568c82f18e70a3232e6d98acbeada8),
[Sketcher::SketchObject::onChanged()](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[Gui::ViewProviderOrigin::onChanged()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[PartDesign::DressUp::onChanged()](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[TechDraw::DrawTileWeld::onChanged()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[TechDraw::DrawGeomHatch::onChanged()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch::onChanged()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawViewImage::onChanged()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a42774ac4ebd8f4fc4819cf4833e779aa),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[PartDesignGui::TaskBoxPrimitives::onConeAngleChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a7728be961d4a469c0fcb7ec45aeb20af),
[PartDesignGui::TaskBoxPrimitives::onConeHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a436d997cc5ea0b81530da2cb38c1ca35),
[PartDesignGui::TaskBoxPrimitives::onConeRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa3ee11ef5378be9cb7953ddc8f7a584d),
[PartDesignGui::TaskBoxPrimitives::onConeRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a1fa0b97630162d71685b15ea1f566a50),
[PartDesignGui::TaskBoxPrimitives::onCylinderAngleChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a059ada94b80ad3d590e7d4a876873fd1),
[PartDesignGui::TaskBoxPrimitives::onCylinderHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a145b7ffb358a2329d635d9241f8fa33e),
[PartDesignGui::TaskBoxPrimitives::onCylinderRadiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a50f3f9f57898d01184274ec84003fe24),
[PartDesignGui::TaskBoxPrimitives::onCylinderXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86d82d270b60a8432e7d0dde84c18faf),
[PartDesignGui::TaskBoxPrimitives::onCylinderYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73f5a1b7f5cd33180352b92a06b78d53),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a9d43a4073114d3c77de0c3e83548e2c1),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a0fbf7eea3dc32497b8711a646862a8c1),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73425d913722a9494da32e334929c6d5),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a46c8bb8b6d9f426492b669c354baea99),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#accbe8caafcb8faa22c9c7553aa3fda23),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a35f2c2ddfe3b72affe6fb4545fab11e4),
[App::OriginGroupExtension::onExtendedSetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a0cbdf0475e8306ed1f6fab7bb2a071cb),
[App::OriginGroupExtension::onExtendedUnsetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27),
[Gui::TreeWidget::onPreSelectTimer()](../../de/de0/classGui_1_1TreeWidget.html#a0af4d1e04d145e231b0682cf1519fd96),
[PartDesignGui::TaskBoxPrimitives::onPrismCircumradiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a8701cee98cd45d672cffe4010a21ba56),
[PartDesignGui::TaskBoxPrimitives::onPrismHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab037232d561cffcd013f608ed88ce79f),
[PartDesignGui::TaskBoxPrimitives::onPrismPolygonChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a3a30191951932ad49bef38d08c4292fa),
[PartDesignGui::TaskBoxPrimitives::onPrismXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23b3eea757a08d4b2736fedb9c929066),
[PartDesignGui::TaskBoxPrimitives::onPrismYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab96618398004458953e2f5d0e1924d6a),
[Gui::ViewProviderDocumentObject::onPropertyStatusChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#aa158bb0312285eb7672f123e8a1359de),
[Gui::TreeWidget::onSelectDependents()](../../de/de0/classGui_1_1TreeWidget.html#a0927eaae2d6793801b559821c527438f),
[PartGui::FaceColors::onSelectionChanged()](../../db/d9e/classPartGui_1_1FaceColors.html#a6280483113ee1508b29134ccad6d35b1),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[PartDesignGui::TaskDraftParameters::onSelectionChanged()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#a8ca0a7704f3a4427df5c4d99eaaf58ad),
[SketcherGui::TaskSketcherConstraints::onSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#ad2aa1dfda961213561df408f2bad55df),
[SketcherGui::TaskSketcherElements::onSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#afafa9c58f43f36216447d6c7df146cfc),
[SketcherGui::DrawSketchHandlerCarbonCopy::onSelectionChanged()](../../d8/dcc/classSketcherGui_1_1DrawSketchHandlerCarbonCopy.html#a0abe4b682958afcce6e53de58d3225fa),
[SketcherGui::DrawSketchHandlerExternal::onSelectionChanged()](../../d5/d95/classSketcherGui_1_1DrawSketchHandlerExternal.html#aab1764f7bd2af3f2cf49a7131a443253),
[TechDraw::DrawWeldSymbol::onSettingDocument()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aebf48eba403fab933cfaba6f325c6bc2),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa5bfc9f1b87ced6adf49875eba7e90a2),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a27858521e805c7390d3f9039c535cdcf),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aea9a6950dd79c79bd8cb360b2b8c8784),
[PartDesignGui::TaskBoxPrimitives::onSphereRadiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a72d9233055fc77ee491dbc8f5587c09c),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ae2e874e2dad51362fd1a56aff1ba6880),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a600166782c2b17052d6236a2406a1439),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a5a528983f97adab406c5123f6474f620),
[PartDesignGui::TaskBoxPrimitives::onTorusRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a10c0def5dec5ab5ea0c5705f8cf5768a),
[PartDesignGui::TaskBoxPrimitives::onTorusRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ac449268708c99e4c2f03997e3f9553be),
[PartDesignGui::TaskBoxPrimitives::onWedgeX2maxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a1f13f84786f7ef305f26838d9f7e2081),
[PartDesignGui::TaskBoxPrimitives::onWedgeX2minChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86463e53d3b0a78c4080b51ba415c388),
[PartDesignGui::TaskBoxPrimitives::onWedgeXmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a66204103a06869337ca64985a9b8d6dc),
[PartDesignGui::TaskBoxPrimitives::onWedgeXminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa5c59aeea355f23727b8bdd8d1a515e5),
[PartDesignGui::TaskBoxPrimitives::onWedgeYmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#af07f3d7a82a59fdbfa665ddd905c3be5),
[PartDesignGui::TaskBoxPrimitives::onWedgeYminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa6fe7277dd6ab536363d7954a7d8c84b),
[PartDesignGui::TaskBoxPrimitives::onWedgeZ2maxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#af872884d5d9ecf66a5767b3ab9635383),
[PartDesignGui::TaskBoxPrimitives::onWedgeZ2minChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a57934914e027c65459bd684f13251463),
[PartDesignGui::TaskBoxPrimitives::onWedgeZmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa944b296adfac1bcf2f85eaa84b36e89),
[PartDesignGui::TaskBoxPrimitives::onWedgeZminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23f1c00dbdb3b7bbc85dc9728096fcc4),
[PartGui::FaceColors::open()](../../db/d9e/classPartGui_1_1FaceColors.html#a1244f504665b35ed2f88c0cd86219c96),
[PartDesignGui::TaskTransformedParameters::originalSelected()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#adb918122e8572632cc17114506d98ccd),
[TechDrawGui::MDIViewPage::preSelectionChanged()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a003eef537ec84dda708d22f2b57f6bcb),
[Gui::ElementColors::Private::Private()](../../d8/dc9/classElementColors_1_1Private.html#a666b8d911912be6e8e346fcb52592125),
[FemGui::TaskDlgPost::recompute()](../../dc/d22/classFemGui_1_1TaskDlgPost.html#a78cec4f51cde4277bafcd04fbeff2ca4),
[TechDrawGui::TaskBalloon::recomputeFeature()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#af5cbff4b0e924e7d68f9d4009a4a25ba),
[TechDrawGui::TaskDimension::recomputeFeature()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#ace37001c57b503aa94c7785b465a688b),
[TechDrawGui::TaskLeaderLine::recomputeFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a530363359c703cdda6b183d978d05ef2),
[PartDesignGui::ViewProviderTransformed::recomputeFeature()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a14cb4d7a2487ad732593fed6ece13ca6),
[PartDesignGui::TaskDressUpParameters::referenceSelected()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a4cbc9c9a3ab11fc80333ddf36ad442aa),
[PartDesignGui::TaskPipeParameters::referenceSelected()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a0c0361901e8218cb0848f5c13d58bb3d),
[PartDesignGui::TaskPipeOrientation::referenceSelected()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#a37effe2b23a30b99a63c7184b2175f21),
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a),
[PartGui::DlgPrimitives::reject()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a934c3b40a9db52e7a9cc8f2daffc3dba),
[PartGui::FaceColors::reject()](../../db/d9e/classPartGui_1_1FaceColors.html#a691d4b784264f80b54924ea84771b241),
[PartDesignGui::TaskDlgFeatureParameters::reject()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#ab22141db4eb33119ad64ed387063f830),
[TechDrawGui::TaskCenterLine::reject()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a68fb5c8b222e660313377b82d56a0f5a),
[TechDrawGui::TaskCosVertex::reject()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#aa783e71740a00435faf4ab69e4a1d217),
[TechDrawGui::TaskDetail::reject()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a824272a5ad9a720866d98e807fdf6cd8),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[TechDrawGui::TaskLeaderLine::reject()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#ae0d8d0522af1e96d8a3a627d96465704),
[TechDrawGui::TaskLineDecor::reject()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#a8069afd3a15d00cd83697357c4a71e48),
[TechDrawGui::TaskProjGroup::reject()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a3a27ff7496637f0d772d15140a8ab238),
[TechDrawGui::TaskRichAnno::reject()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#afdab38da6fd7ccedf964c55bb68e5b21),
[DrawSketchHandlerGenConstraint::releaseButton()](../../d7/dc2/classDrawSketchHandlerGenConstraint.html#a8c9d15e5c489ccb3f06cacaae622f0f3),
[DrawSketchHandlerCoincident::releaseButton()](../../d1/da0/classDrawSketchHandlerCoincident.html#a0aa30cef84692d6048db1607abb8b77f),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[PartDesignGui::relinkToBody()](../../dc/d12/namespacePartDesignGui.html#a5bd0f34409b95d9ccc03b0b80655b0fd),
[Spreadsheet::PropertySheet::removeColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ada4ceb76fd79dc130476fe307f77e0a1),
[Gui::ViewProviderDocumentObject::removeDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a4d47313a825a2051c9a667ed4e7a1346),
[TechDraw::DrawProjGroup::removeProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a23d2d0cb8a3447cdb912202f46f27aae),
[Spreadsheet::PropertySheet::removeRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5ff589d68c79b8387678e38007f8733f),
[TechDraw::DrawPage::removeView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47c86c19ddcbaabe9a680e836c437012),
[App::ObjectIdentifier::replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[App::ObjectIdentifier::resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4503f7d6916abae555ddb15db1eed9ea),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[Gui::SelectionSingleton::sAddSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a611e09b40ed2a13cb570ad01f2a6e059),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[TechDrawGui::QGSPage::saveSvg()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a7c5dd2c51df61dba9689959c585870d2),
[Gui::SelectionObserver::SelectionObserver()](../../dc/d3c/classGui_1_1SelectionObserver.html#adfbfb276069ea43872dcaae8bdbbc472),
[FemGui::ActiveAnalysisObserver::setActiveObject()](../../dd/df6/classFemGui_1_1ActiveAnalysisObserver.html#a668eeab67692a4bf570ccdf236264d19),
[Spreadsheet::PropertySheet::setAlias()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfe1772d3fe2f5cae99996963db17db2),
[App::ObjectIdentifier::setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843),
[RaytracingGui::ViewProviderLux::setEdit()](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a559d010dd9902addb4de84170aac9f51),
[RaytracingGui::ViewProviderPovray::setEdit()](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a76685922c30f4f6a92a74fafcc800fa2),
[TechDrawGui::ViewProviderViewPart::setEdit()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a758558e7e660c02f277bc621cb7e2e61),
[SurfaceGui::FillingPanel::setEditedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aaaeba016fe808b6dc4d3ddfc9788d380),
[SurfaceGui::FillingEdgePanel::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#aa23402d795184e9f546a933ef0820357),
[SurfaceGui::FillingVertexPanel::setEditedObject()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a927aea6ee02478a495e928a20a2c3014),
[SurfaceGui::GeomFillSurface::setEditedObject()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a5347666bfd43a7cbea08d4c179e33f5d),
[SurfaceGui::SectionsPanel::setEditedObject()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#acbe617b52e00f4d86e607c6bc5619d59),
[SketcherGui::ViewProviderSketch::setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[App::LinkBaseExtension::setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[Spreadsheet::PropertySheet::setPathValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a6838f3e16b4b7d85c2517c13aec22ede),
[PartDesignGui::TaskDressUpParameters::setSelection()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#afbe9ba507cb0b88b7ef7250c5901d975),
[TechDrawGui::ViewProviderPage::setTemplateMarkers()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#afc5258258f9e246ab22a52bb8bbbe03a),
[TechDrawGui::MDIViewPage::setTreeToSceneSelect()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a8c4e132accc95406f63a7e555cb1cbfc),
[PartDesignGui::Workbench::setupContextMenu()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
[TechDraw::DrawViewImage::setupImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a70665b6da416755ac2cdb36d9c9ecf6d),
[App::Origin::setupObject()](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9),
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275),
[TechDraw::DrawViewSection::setupSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a3736e6db938d365a0866d6704bcb3fe0),
[TechDraw::DrawTileWeld::setupSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a9a0ec49268483ff93a086ca6a58c58da),
[PartDesignGui::TaskSketchBasedParameters::setUpToFace()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#acd1f7bc55f973a0923ef8c31bf3e2ee5),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[FemGui::FunctionWidget::setViewProvider()](../../dc/d25/classFemGui_1_1FunctionWidget.html#a0083237a39c65525f04f5124c07ae2d6),
[PartDesignGui::ViewProviderBody::setVisualBodyMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a50b3de515b84c2e3e19b840ef5fc8187),
[MeshGui::Annotation::show()](../../dd/d2d/classMeshGui_1_1Annotation.html#a8e675bcb0e642864e58f2d9f3b482ca8),
[DrawingGui::ViewProviderDrawingPage::showDrawingView()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#af7cd2898c5d4d289f22f0fb7c232984f),
[TechDrawGui::ViewProviderPage::showMDIViewPage()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a73bc19f9c2666efa58194e253d2678a1),
[SpreadsheetGui::ViewProviderSheet::showSpreadsheetView()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a912de2c5ce615efc6d1e3f70f3674f1b),
[Gui::SelectionSingleton::slotDeletedObject()](../../d4/dca/classGui_1_1SelectionSingleton.html#a71d83e67e4de7417667efa24dc4c7ed5),
[Gui::DocumentItem::slotExpandObject()](../../df/d15/classGui_1_1DocumentItem.html#ae5fdb7142a8461427f530a847c8d9947),
[Gui::DocumentItem::slotHighlightObject()](../../df/d15/classGui_1_1DocumentItem.html#ad3efba34b870836512bfb35722f3719b),
[Gui::SelectionSingleton::sRemoveSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#af2933a9b72409431f7fd31d78ade3d5c),
[Gui::SelectionSingleton::sSetPreselection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a17d43ab4934b472aa7e9b5bf01127e25),
[Gui::SelectionSingleton::sUpdateSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a33194bd56bf9dc3e9e893e8b7a66153b),
[App::LinkBaseExtension::syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f),
[TechDrawGui::TaskCosVertex::TaskCosVertex()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a0f04c27182bc74d96638e6080dc44f91),
[TechDrawGui::TaskDetail::TaskDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a2017c373db55e0b43d386b536b34bc75),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[TechDrawGui::TaskLeaderLine::TaskLeaderLine()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a873d04472b6a0de7f250ac13eef14913),
[TechDrawGui::TaskProjGroup::TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[TechDrawGui::TaskRichAnno::TaskRichAnno()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#acfd26140dce1c41560c4391c78b2fb06),
[TechDrawGui::TaskSectionView::TaskSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a146b65deaafcbc3d957c00e2814de9a1),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
[PartDesignGui::ViewProvider::unsetEdit()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aeb01bc367ec2895032e0fcd1074528fb),
[TechDraw::DrawViewCollection::unsetupObject()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a33815aa3bc978248b9ec92b423ba7c45),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawViewPart::unsetupObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a404e3640464295cb65780c7374a83940),
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[DrawingGui::ViewProviderDrawingPage::updateData()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
[MeshGui::ViewProviderMeshCurvature::updateData()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033),
[TechDrawGui::TaskLinkDim::updateDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#acff44dd09f905319bf7234cd9c0afd2e),
[TechDrawGui::ViewProviderGeomHatch::updateGraphic()](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#ab2d1f97c296e75ceb36d18fd8557ba73),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
and
[PartGui::DlgExtrusion::writeParametersToFeature()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8d059573a157c9f9128d55b3c9a9fcc1).

## ◆ getExportName()

std::string App::DocumentObject::getExportName  | ( | [bool](../../d9/db9/classbool.html) | _forced_ = `false`| ) |  const  
---|---|---|---|---|---  
  
returns the name that is safe to be exported to other document

## ◆ getExpression()

| virtual const [PropertyExpressionEngine::ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html) App::DocumentObject::getExpression  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Referenced by
[Sketcher::SketchObject::addCopyOfConstraints()](../../d9/dad/classSketcher_1_1SketchObject.html#ae855d43b68feffdb57a0489777e2b9ad),
[Gui::InputField::bind()](../../da/dfa/classGui_1_1InputField.html#a17038da6cfd54acfc8f86b6597edb8a4),
[Sketcher::SketchObject::constraintHasExpression()](../../d9/dad/classSketcher_1_1SketchObject.html#a13d7d959fe45ea0b1f80b11a8337c492),
[ConstraintItem::data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[Spreadsheet::PropertySheet::getBinding()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aecdca3d5ef73919449f9b8141288f6da),
[Gui::ExpressionBinding::getExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a2af16f7694ca1c7c0465a31eddf195d5),
and
[ExpressionDelegate::paint()](../../d1/df5/classExpressionDelegate.html#ae8f09045fee240444d9d5383c8d23d0e).

## ◆ getFullName()

| virtual std::string App::DocumentObject::getFullName  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Return the object full name of the form DocName::ObjName.

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d).

Referenced by
[SpreadsheetGui::DlgSheetConf::accept()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#aa4fefe42d2485471443e738600091ce0),
[Spreadsheet::PropertySheet::adjustLink()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ad19a81a5a5f1c88bb669f91604c4fab3),
[Gui::ViewProviderLink::attach()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab31e41e9a24ec097be019cdff4fb969b),
[Spreadsheet::Sheet::execute()](../../d0/da8/classSpreadsheet_1_1Sheet.html#ae374761fddb3f1531d4bd1af5c7b5b49),
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42),
[PartDesign::DressUp::getAddSubShape()](../../df/de5/classPartDesign_1_1DressUp.html#ad0ea5289ebf6d00059754a3cd95b7981),
[App::Origin::getAxis()](../../d9/d8b/classApp_1_1Origin.html#a22ff56dd7f14783a94fe81dbb5ac648c),
[Gui::ViewProviderDocumentObject::getFullName()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a0943bc30138036868c395bd324c321b2),
[App::OriginGroupExtension::getOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#a97f3ab4c5b29de9d18b2ec7daf494fc2),
[App::Origin::getOriginFeature()](../../d9/d8b/classApp_1_1Origin.html#ac51255a58d5f06783527b973082ed634),
[App::Origin::getPlane()](../../d9/d8b/classApp_1_1Origin.html#a9079a145e03b6fb0715db0246ace036b),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[Gui::DocumentItem::getTopParent()](../../df/d15/classGui_1_1DocumentItem.html#a6cc5ada0bf41a53ded22fa99897d2c73),
[Spreadsheet::PropertySheet::invalidateDependants()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ae30f4ba5574b7048482105523fac6de0),
[Gui::LinkInfo::LinkInfo()](../../d4/da4/classGui_1_1LinkInfo.html#ae3618e9bfdb664830e6725d702879020),
[Spreadsheet::Sheet::onDocumentRestored()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a6442efcbd90e9a8099539a0e43afec68),
[Gui::DocumentItem::populateItem()](../../df/d15/classGui_1_1DocumentItem.html#a3736de97bc4cbbbe298130b4a980cf58),
[Spreadsheet::Sheet::providesTo()](../../d0/da8/classSpreadsheet_1_1Sheet.html#aa73d2443011f5a727a37485b0a84e564),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Spreadsheet::PropertySheet::setAlias()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfe1772d3fe2f5cae99996963db17db2),
[Gui::Document::setEdit()](../../de/d4e/classGui_1_1Document.html#a2064c6eb4172240d40a7f409febc81a9),
[Spreadsheet::Cell::setException()](../../d5/d22/classSpreadsheet_1_1Cell.html#aa1d867431da61d601ca3cc5cdfea20b1),
[Spreadsheet::Cell::setResolveException()](../../d5/d22/classSpreadsheet_1_1Cell.html#af61cded7731b8d417cd34604a4715c35),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb),
[App::DocInfo::slotSaveDocument()](../../d7/d23/classApp_1_1DocInfo.html#abf0047bf220d8747360cf5de8ae98c28),
[Gui::Document::slotTouchedObject()](../../de/d4e/classGui_1_1Document.html#a72811232eee73cbebccc6a0f4564f92a),
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[App::LinkBaseExtension::updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2),
and
[PartGui::ViewProviderPartExt::updateVisual()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a96cb6b96c8dfb082a135a31c4f554167).

## ◆ getGroup()

[DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html) * App::DocumentObject::getGroup  | ( | | ) |  const  
---|---|---|---|---  
  
get group if object is part of a group, otherwise 0 is returned

Referenced by
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34).

## ◆ getID()

long App::DocumentObject::getID  | ( | | ) |  const  
---|---|---|---|---  
  
Return the object ID that is unique within its owner document.

Referenced by
[Gui::DocumentItem::findRootIndex()](../../df/d15/classGui_1_1DocumentItem.html#a4e92cb1b196d77af71364ae5f8f95dc9).

## ◆ getInList()

const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & App::DocumentObject::getInList  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[TechDrawGui::ViewProviderLeader::claimChildren()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#ab90cf47c766f83da23d7f960ded3ccdd),
[TechDrawGui::ViewProviderViewPart::claimChildren()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aba1c9f4a2a6681b4ea6666ba487847c1),
[TechDrawGui::ViewProviderWeld::claimChildren()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a4e8d25b0066202499ac3da63f664db36),
[TechDraw::DrawView::countParentPages()](../../d6/d1c/classTechDraw_1_1DrawView.html#aaafae8e4da4d73fafd4212576188b326),
[TechDraw::DrawTemplate::execute()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a67d8e151c886e0ef62f246cc3a4e5ff6),
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42),
[TechDraw::DrawView::findAllParentPages()](../../d6/d1c/classTechDraw_1_1DrawView.html#a9b28f37bc7b1197a9de93065bec24190),
[TechDraw::DrawView::findParentPage()](../../d6/d1c/classTechDraw_1_1DrawView.html#a5afa0f83d15ac28c8fd00cd47663c79e),
[TechDraw::DrawViewPart::getBalloons()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a2af77af02e9b46ff8535f3c0e3d5cda3),
[TechDraw::DrawView::getClipGroup()](../../d6/d1c/classTechDraw_1_1DrawView.html#a5d4c311b15da7ecfce93f6ee47cc5326),
[TechDraw::DrawViewPart::getDetailRefs()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a55c64661c530b34d53d7bd85e2e6bc54),
[TechDraw::DrawViewPart::getDimensions()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aead97bcf62218c84e4f895b710ed1ae3),
[TechDraw::DrawViewPart::getGeomHatches()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a791ac89a7da3090c29febc0ca990c198),
[TechDraw::DrawViewPart::getHatches()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aaf6c2599b3dfdb89053d5685f33bf747),
[TechDraw::DrawView::getLeaders()](../../d6/d1c/classTechDraw_1_1DrawView.html#a06b2c3010e85ba1e320e12cad20ae5bf),
[TechDraw::DrawTemplate::getParentPage()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a14c9c348c4695881293c7ba14f8d0bb0),
[TechDraw::DrawProjGroupItem::getPGroup()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#adf1f84e5479b18e7dae605f8afb7825d),
[TechDraw::DrawViewPart::getSectionRefs()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a193d33664258d178df8d627db0b2dc39),
[TechDraw::DrawWeldSymbol::getTiles()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#a70aed4254307b5004b56244677295366),
[DrawingGui::ViewProviderDrawingView::hide()](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#af1f9e27cb4717b1eab17df64def3a5a3),
[DrawingGui::ViewProviderDrawingClip::hide()](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#ae328b7a7c463a0cfe21fb19adb6a8cab),
[TechDraw::DrawView::isInClip()](../../d6/d1c/classTechDraw_1_1DrawView.html#ac7c414b101516f9925ec8c992e71e54c),
[Gui::ViewProviderOrigin::onDelete()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#af088d91593fa59ce593fd49716356f32),
[PartDesign::ProfileBased::remapSupportShape()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#ad1985a2126f28aecb119562d9f47ba37),
[DrawingGui::ViewProviderDrawingView::show()](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a41516072b7f56cf582e8c638c6dcdf05),
[DrawingGui::ViewProviderDrawingClip::show()](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#a8f9447ce75000777ba104a171d6f85f5),
and
[PartDesignGui::ViewProviderTransformed::startEditing()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#aca65c3594f90b54775e4c73ededd1ffc).

## ◆ getInListEx() [1/2]

std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::DocumentObject::getInListEx  | ( | [bool](../../d9/db9/classbool.html) | _recursive_| ) |  const  
---|---|---|---|---|---  
  
Return a set of all objects linking to this object, including possible
external parent objects.

Parameters

     recursive| [in]: whether to obtain recursive in list   
---|---  
  
## ◆ getInListEx() [2/2]

void App::DocumentObject::getInListEx  | ( | std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inSet_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ ,   
|  | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > *  | _inList_ = `nullptr`  
| ) | |  const  
  
Get a set of all objects linking to this object, including possible external
parent objects.

Parameters

     inSet| [out]: a set containing all objects linking to this object.   
---|---  
recursive| [in]: whether to obtain recursive in list  
inList| [in, out]: optional pointer to a vector holding the output objects,
with the furthest linking object ordered last.  
  
Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[PartDesign::SubShapeBinder::setLinks()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a121c18838a25b1982d6732ec125f4eec),
and
[App::PropertyExpressionEngine::validateExpression()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa259d698d63c151f459f14483346639a).

## ◆ getInListRecursive()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::DocumentObject::getInListRecursive  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
get all objects link directly or indirectly to this object

## ◆ getLinkedObject()

| virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::DocumentObject::getLinkedObject  | ( | [bool](../../d9/db9/classbool.html) | _recurse_ = `true`,   
---|---|---|---  
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ = `false`,   
|  | [int](../../d1/da0/classint.html) | _depth_ = `0`  
| ) | |  const  
virtual  
  
Return the linked object with optional transformation.

Parameters

     recurse| If false, return the immediate linked object, or else recursively call this function to return the final linked object.  
---|---  
mat| If non zero, it is used as the current transformation matrix on input.
And output as the accumulated transformation till the final linked object.  
transform| if false, then it will not accumulate the object's own placement
into `mat`, which lets you override the object's placement.  
  
Returns

    Return the linked object. This function must return itself if the it is not a link or the link is invalid. 

Referenced by
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
[Gui::ViewProviderLink::getLinkedView()](../../d6/d59/classGui_1_1ViewProviderLink.html#ad59ee585fbf91984dde3cfa42d8d3eba),
[Gui::ViewProviderDocumentObject::getLinkedViewProvider()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae9ea14dda6e0dfc0d0cde880f8bddbf0),
[Part::Feature::getShapeOwner()](../../d7/d7e/classPart_1_1Feature.html#afc51965464e6e44329801279bad18077),
[Gui::DocumentObjectItem::isGroup()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#af6fd7fe2dbf990ec46352ba0d5d33c3c),
[Gui::DocumentObjectItem::isLink()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#afbce83c3c5391c92e7c10dc888d9677b),
[Gui::DocumentObjectItem::isLinkFinal()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#ae23a5c207b98d2815ff51ea509c3001b),
[Gui::DocumentItem::populateItem()](../../df/d15/classGui_1_1DocumentItem.html#a3736de97bc4cbbbe298130b4a980cf58),
[Gui::ViewProviderLink::startEditing()](../../d6/d59/classGui_1_1ViewProviderLink.html#aa784b328fb67782acbe474a4bf1ccafa),
and
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465).

## ◆ getNameInDocument()

const char * App::DocumentObject::getNameInDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
returns the name which is set in the document for this object (not the name
property!)

Referenced by
[FemGui::TaskDlgFemConstraint::accept()](../../d8/d18/classFemGui_1_1TaskDlgFemConstraint.html#a61fcc7a973c20d15a3f3fd173de45115),
[FemGui::TaskDlgFemConstraintBearing::accept()](../../d9/d36/classFemGui_1_1TaskDlgFemConstraintBearing.html#a8cfbe7931a50860f262cb8a8bd53174a),
[FemGui::TaskDlgFemConstraintContact::accept()](../../db/df7/classFemGui_1_1TaskDlgFemConstraintContact.html#ac8e6fda8efa657a1ac00f5c71c675ca8),
[FemGui::TaskDlgFemConstraintDisplacement::accept()](../../d8/d61/classFemGui_1_1TaskDlgFemConstraintDisplacement.html#abde076fbe625911d6fac6487d935b697),
[FemGui::TaskDlgFemConstraintFixed::accept()](../../d6/d60/classFemGui_1_1TaskDlgFemConstraintFixed.html#ab69acd464d0e98e8edc1aa56942b81aa),
[FemGui::TaskDlgFemConstraintFluidBoundary::accept()](../../da/d17/classFemGui_1_1TaskDlgFemConstraintFluidBoundary.html#a92106711f12fb0fb783c7e411d8f3923),
[FemGui::TaskDlgFemConstraintForce::accept()](../../de/d1f/classFemGui_1_1TaskDlgFemConstraintForce.html#ac3e13cbdc0d1cc146a35abcaf3d1e6ac),
[FemGui::TaskDlgFemConstraintGear::accept()](../../dc/ded/classFemGui_1_1TaskDlgFemConstraintGear.html#af8b307f6bf08021e04d3c17682437692),
[FemGui::TaskDlgFemConstraintHeatflux::accept()](../../d3/d88/classFemGui_1_1TaskDlgFemConstraintHeatflux.html#a53d610147fb72b043d50bb517a7be7c3),
[FemGui::TaskDlgFemConstraintInitialTemperature::accept()](../../d9/d8a/classFemGui_1_1TaskDlgFemConstraintInitialTemperature.html#a417fa6e0a784395a4285594b00043771),
[FemGui::TaskDlgFemConstraintPlaneRotation::accept()](../../d9/d6e/classFemGui_1_1TaskDlgFemConstraintPlaneRotation.html#a031d431276c94f688603cca52670fbce),
[FemGui::TaskDlgFemConstraintPressure::accept()](../../de/dc7/classFemGui_1_1TaskDlgFemConstraintPressure.html#ac005705a3bdb405d084f0ecbbd8315e6),
[FemGui::TaskDlgFemConstraintPulley::accept()](../../db/de8/classFemGui_1_1TaskDlgFemConstraintPulley.html#a414adb4a165a557dd1a1cd1a974d28d2),
[FemGui::TaskDlgFemConstraintSpring::accept()](../../d3/db5/classFemGui_1_1TaskDlgFemConstraintSpring.html#adb9d189ee347350b72b5e4b2ffb86479),
[FemGui::TaskDlgFemConstraintTemperature::accept()](../../d6/d9f/classFemGui_1_1TaskDlgFemConstraintTemperature.html#a420aae7c27b27ef6426e91efb1065f4c),
[FemGui::TaskDlgFemConstraintTransform::accept()](../../db/dd1/classFemGui_1_1TaskDlgFemConstraintTransform.html#a7040e08e6ad3ca411cd7fa28ae9bd67c),
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[PartGui::DlgPrimitives::accept()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a1db668afa4bde5626f25c5e34f596b82),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[App::PropertyLinkSubList::adjustLink()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525),
[App::ObjectIdentifier::adjustLinks()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a64e384b81e6d7f8de55251a498467604),
[PartDesignGui::TaskChamferParameters::apply()](../../d1/d5d/classPartDesignGui_1_1TaskChamferParameters.html#a25ef9333841ebe6ef78a1faa9fa48e8d),
[PartDesignGui::TaskFilletParameters::apply()](../../db/d91/classPartDesignGui_1_1TaskFilletParameters.html#aba0ebfd55210a4e35b3b64381e14dc13),
[PartDesignGui::TaskScaledParameters::apply()](../../d2/d61/classPartDesignGui_1_1TaskScaledParameters.html#ae371b3f88278691914f2048cb3d0be4c),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[TechDraw::DrawProjGroup::arrangeViewPointers()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a8a8bdca0831ea0e16e664ad17f0a04f8),
[Gui::ViewProviderAnnotation::attach()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#ab50892bdc3b37f9da77b36cac3014cf6),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[MeshGui::ViewProviderMesh::attach()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#adb9b6c0cd97337657aabd81bac13e35e),
[PointsGui::ViewProviderScattered::attach()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab6910e935629c8fe18fed5409c9521a0),
[PointsGui::ViewProviderStructured::attach()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#aabe6e709079ef4dd2d44b687db5f1dd7),
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[Gui::ViewProviderVRMLObject::attach()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a6325dc25a3b586202db6edaf20319937),
[RobotGui::ViewProviderRobotObject::attach()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#abfd62beacd9f9981515c67a20b27e813),
[RobotGui::ViewProviderTrajectory::attach()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#ae0c77a17efe78de9f375f9382cc40da2),
[TechDraw::DrawViewPart::buildGeometryObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a859efd3dcccfd849656ff8b436ce6d58),
[TechDraw::DrawProjGroup::calculateAutomaticScale()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#af5bbe9c992fa0e9fc83461af6931f0e0),
[TechDraw::DrawViewDimension::checkReferences2D()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6b3599cd70d672c8aa6e16e304bbb1a4),
[TechDraw::DrawViewPart::checkXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a602f73fc08211bfc4edfa1382bc0ee64),
[Gui::DAG::Model::contextMenuEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a929350aab7c7acb610a7d61bdcc644b6),
[App::PropertyXLink::copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::QGSPage::createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[TechDrawGui::TaskSectionView::createSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ac5902eeba616fd351e4de4546c7634de),
[TechDrawGui::TaskWeldingSymbol::createWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a687a7f75b421ef414ad8e8ae46dc7889),
[SpreadsheetGui::SheetTableView::deleteSelection()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a815da32c5d5f77951bce6ddf5e5954f9),
[TechDraw::DrawViewDetail::detailExec()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ac3431955f5f49dc0fca4635342a62881),
[Gui::DocumentObjectItem::displayStatusInfo()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a235f26b8fbf37e4e4efccdae9cbbada0),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Sketcher::SketchObjectSF::execute()](../../de/da4/classSketcher_1_1SketchObjectSF.html#aee2e5bb2b2aa00817df40cae0574ef36),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewMulti::execute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[PartDesignGui::TaskBooleanParameters::exitSelectionMode()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a029bb8dc4c1a01c08bebfa7b9c40cdcd),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[TechDraw::DrawViewPart::extractFaces()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aaaaf9f3bc41bcad927258ed1fdb53baa),
[MeshGui::ViewProviderMesh::faceInfo()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a82e7c934502545ca07cefba12d6d00e9),
[TechDrawGui::DrawGuiUtil::findPage()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a5e81d631634196d2c5fe0d083fd7cb9b),
[TechDrawGui::QGSPage::findParent()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#aa36872a18b939b5400ece0e09997fd0f),
[Gui::DocumentItem::findRootIndex()](../../df/d15/classGui_1_1DocumentItem.html#a4e92cb1b196d77af71364ae5f8f95dc9),
[PartDesignGui::TaskSketchBasedParameters::finishReferenceSelection()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#a39905be0e5808d97a96dfa2b3f26c8d9),
[PartDesignGui::TaskHelixParameters::finishReferenceSelection()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ada6f913b38dce43eee9bdb326fd69d06),
[TechDrawGui::MDIViewPage::fixOrphans()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#aad3fdce39513a47bae2e6fce2a7cd0d5),
[TechDraw::DrawViewDimension::formatValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2fde1e9d439af529e2aab21889bd9c17),
[PartGui::getAutoGroupCommandStr()](../../d5/d49/namespacePartGui.html#a890bd8b36c17c104d45b9ddb222ba226),
[TechDraw::DrawLeaderLine::getBaseScale()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#acab08d27991c64b4f4d19d097d8e7c26),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[TechDraw::DrawProjGroup::getDirsFromFront()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a66cbbc8038fcab5532278784cbac867b),
[Gui::LinkInfo::getLinkedName()](../../d4/da4/classGui_1_1LinkInfo.html#adb89aacf8ee954b8b9cf56313aa7b3bf),
[Gui::ViewProviderDocumentObject::getLinkedViewProvider()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae9ea14dda6e0dfc0d0cde880f8bddbf0),
[Gui::ViewProviderLink::getLinkExtension()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab75a56312dd387c3d22c1e3b17ba84cc),
[Gui::DocumentObjectItem::getName()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a2e4bf958f38f3b363b3c488ef1dee9bc),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1),
[TechDraw::DrawViewDimension::getPointsEdgeVert()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#af66b90afc565ab105dff3a850b9ccbc0),
[TechDraw::DrawViewDimension::getPointsOneEdge()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a74fb8170cf274981663bb1989bb972ca),
[TechDraw::DrawViewDimension::getPointsTwoEdges()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f77703f9d3c576d674a7468b231e1ae),
[TechDraw::DrawViewDimension::getPointsTwoVerts()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a3aeea1b6e40d2eba51a724b38db66455),
[TechDraw::DrawViewDimension::getPrefixSuffixSpec()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a6a8d79939b1d5346af1f436ce34dafcf),
[TechDraw::DrawViewPart::getProjectionCS()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ae1dd72b98fa563bf72d6c39f49577632),
[TechDraw::DrawProjGroup::getProjItem()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a717b725aa8d44d5699087bc1401e26e1),
[TechDraw::DrawProjGroup::getProjObj()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a20beaf391d87e04ad8b2cd1db7c78b6d),
[App::VRMLObject::getRelativePath()](../../df/df6/classApp_1_1VRMLObject.html#acc45a77504394dfd80e2be65376ef14a),
[TechDraw::DrawView::getScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#afc22d0aa3cc132a6c14323a50082ab1e),
[TechDraw::DrawLeaderLine::getScale()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a5df9ab095a761eaef57045a431cbb972),
[TechDraw::DrawProjGroupItem::getScale()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a8f2e3744991fded06c52c4e817aed862),
[TechDraw::DrawViewSection::getSectionCS()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#aefc378d8464959b191ac4ff96f6bca12),
[Gui::TreeWidget::getSelection()](../../de/de0/classGui_1_1TreeWidget.html#a073a56b7c3fe9c0c72cbcf84993326d4),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[Gui::LinkInfo::getSnapshot()](../../d4/da4/classGui_1_1LinkInfo.html#a5b9c21ced59932d504807f9db330bbe1),
[TechDraw::DrawViewPart::getSourceShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aeb0d7bbe7418b86053f38713d4c91fa9),
[TechDraw::DrawViewPart::getSourceShapeFused()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a259e1a941c8e6a0651089bfa4111e3bd),
[TechDraw::DrawProjGroupItem::getViewAxis()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a66cab4b4ebd52d41889c7fdb9c854821),
[TechDraw::DrawProjGroup::getViewIndex()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a92924eedc2c197844d6012d822d0bb7b),
[TechDraw::DrawProjGroup::hasProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a90a7b1897caccb65feab45425c10448d),
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[Spreadsheet::PropertySheet::hasSetValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585),
[TechDrawGui::TaskLineDecor::initUi()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#a58ab677c87cd4089a322fc2bc523b570),
[Gui::LinkInfo::isLinked()](../../d4/da4/classGui_1_1LinkInfo.html#a7792edb8ec60637b41c2c2bde4ea0efc),
[Gui::SelectionSingleton::isSelected()](../../d4/dca/classGui_1_1SelectionSingleton.html#a821a5d7843e3c3c08e9d6244b4d21e1d),
[TechDrawGui::TaskLinkDim::loadToTree()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a78901c66da67bb8e9a3a97469e4f61d4),
[TechDraw::DrawDimHelper::makeDistDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#abbb31fd885c91f55267b7f8fd3945c1a),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[TechDraw::DrawViewSection::makeLineSets()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a8673a58822bb65ebe493c128d2aef29e),
[Gui::DAG::Model::mousePressEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a5507e79687e92d89464f8b95181bb4e5),
[SketcherGui::TaskSketcherConstraints::on_listWidgetConstraints_itemSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#a9dfd693a935f64423cc9106430776263),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemEntered()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a2e956e6abd25667f7e59514a401b0f42),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a56cc69945924032683b1845683b9873b),
[MeshGui::DlgEvaluateMeshImp::on_repairAllTogether_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a37ba0babe8914d5dce379504b9adf12e),
[MeshGui::DlgEvaluateMeshImp::on_repairDegeneratedButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ab3cdbd594788a57c256755a837018d2f),
[MeshGui::DlgEvaluateMeshImp::on_repairDuplicatedFacesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aede555d793810d6cfc2632ecf409e5fa),
[MeshGui::DlgEvaluateMeshImp::on_repairDuplicatedPointsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aef057c023433bea4e835ee2e61dd0d17),
[MeshGui::DlgEvaluateMeshImp::on_repairFoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a492d611b70e28517f204bf25bf76184e),
[MeshGui::DlgEvaluateMeshImp::on_repairIndicesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a3da19b67de1065f6efa4da4a159d9e97),
[MeshGui::DlgEvaluateMeshImp::on_repairNonmanifoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a515dab5e6ea530b164559c860252bfae),
[MeshGui::DlgEvaluateMeshImp::on_repairOrientationButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a69c2e5330dbce392a37614ce7e27d7fe),
[MeshGui::DlgEvaluateMeshImp::on_repairSelfIntersectionButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#acd921ad6e7470851387f97162ff6e288),
[PartDesignGui::TaskSketchBasedParameters::onAddSelection()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#a21b691abf9e5be5455e3321bd7e5165a),
[FemGui::TaskFemConstraint::onButtonWizCancel()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a40568c82f18e70a3232e6d98acbeada8),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewSymbol::onChanged()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[App::OriginGroupExtension::onExtendedUnsetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27),
[Gui::TreeWidget::onPreSelectTimer()](../../de/de0/classGui_1_1TreeWidget.html#a0af4d1e04d145e231b0682cf1519fd96),
[PartGui::FaceColors::onSelectionChanged()](../../db/d9e/classPartGui_1_1FaceColors.html#a6280483113ee1508b29134ccad6d35b1),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[SketcherGui::TaskSketcherConstraints::onSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#ad2aa1dfda961213561df408f2bad55df),
[SketcherGui::TaskSketcherElements::onSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#afafa9c58f43f36216447d6c7df146cfc),
[TechDrawGui::QGILeaderLine::onSourceChange()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#ab3073068dad776704ac7652e79ab594d),
[App::DocumentObjectT::operator=()](../../d5/d07/classApp_1_1DocumentObjectT.html#aa6d6b6131b81ccd65364482dd799199b),
[TechDraw::DrawViewPart::partExec()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#acd86eaca34db64b94858f1baeb1e227f),
[TechDrawGui::MDIViewPage::preSelectionChanged()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a003eef537ec84dda708d22f2b57f6bcb),
[Gui::ElementColors::Private::Private()](../../d8/dc9/classElementColors_1_1Private.html#a666b8d911912be6e8e346fcb52592125),
[TechDraw::DrawProjGroup::purgeProjections()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a59234a939935212324d52d31af4c479b),
[TechDrawGui::QGSPage::QGSPage()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a011a597adde8c723bfd1e3fa2a83472b),
[TechDrawGui::QGVPage::QGVPage()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#a95b3aab530ae371e05227a290de621d7),
[Attacher::AttachEngine::readLinks()](../../d2/d85/classAttacher_1_1AttachEngine.html#ab12234c7f2b2dafd7fdb89f4faa999c7),
[App::Document::recomputeFeature()](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a),
[TechDrawGui::MDIViewPage::redraw1View()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5cec404e2ad0c0e80aa0ca32caf16ffd),
[PartDesignGui::TaskPipeParameters::referenceSelected()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a0c0361901e8218cb0848f5c13d58bb3d),
[PartDesignGui::TaskPipeOrientation::referenceSelected()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#a37effe2b23a30b99a63c7184b2175f21),
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a),
[PartGui::ThicknessWidget::reject()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#a582cad61e2769aff6b8a58c38c5cd369),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[TechDrawGui::TaskProjGroup::reject()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a3a27ff7496637f0d772d15140a8ab238),
[TechDrawGui::TaskSectionView::reject()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a06ea99abf05dde7b774ecf00deabdeb7),
[DrawSketchHandlerGenConstraint::releaseButton()](../../d7/dc2/classDrawSketchHandlerGenConstraint.html#a8c9d15e5c489ccb3f06cacaae622f0f3),
[DrawSketchHandlerCoincident::releaseButton()](../../d1/da0/classDrawSketchHandlerCoincident.html#a0aa30cef84692d6048db1607abb8b77f),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[TechDrawGui::TaskLeaderLine::removeFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a3966869ef8faf23d5293b16f335de34c),
[TechDrawGui::TaskRichAnno::removeFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a8fbd082bee0ba6db50f0a83a504f2b0b),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[TechDraw::DrawProjGroup::removeProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a23d2d0cb8a3447cdb912202f46f27aae),
[TechDraw::DrawPage::removeView()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47c86c19ddcbaabe9a680e836c437012),
[Gui::ViewProviderPythonFeatureImp::replaceObject()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a46d467216f88b4c1d0b71a3910e7da31),
[Gui::ViewProviderDocumentObject::replaceObject()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a75216597b08f62e670dc98bf829c8254),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[App::ObjectIdentifier::resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[Gui::SelectionSingleton::sAddSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a611e09b40ed2a13cb570ad01f2a6e059),
[App::Document::save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[TechDrawGui::MDIViewPage::saveDXF()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a2bfe93567b8e55b5bcda419d70b57a8e),
[TechDrawGui::QGSPage::saveSvg()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a7c5dd2c51df61dba9689959c585870d2),
[TechDrawGui::TaskProjGroup::scaleManuallyChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a40ff243eaf44f2528b05976f21fd4f67),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[Gui::SelectionObserver::SelectionObserver()](../../dc/d3c/classGui_1_1SelectionObserver.html#adfbfb276069ea43872dcaae8bdbbc472),
[PartGui::DlgExtrusion::setAxisLink()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#ab577fd456f3a91cb04046447233e5d32),
[PartGui::DlgRevolution::setAxisLink()](../../d1/d83/classPartGui_1_1DlgRevolution.html#af92441fd243089ff48d3c5cdcb56d81a),
[SpreadsheetGui::WorkbenchHelper::setBackgroundColor()](../../df/d59/classSpreadsheetGui_1_1WorkbenchHelper.html#a84a6cd19ea31a176ad4172e865a59438),
[App::ObjectIdentifier::setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843),
[PartDesignGui::setEdit()](../../dc/d12/namespacePartDesignGui.html#a17919aee7b66c9ef03076df1c8c1e406),
[PartDesignGui::ViewProviderDressUp::setEdit()](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#a4119fd1599c9378ba7b4e9185637c51c),
[TechDrawGui::ViewProviderViewPart::setEdit()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a758558e7e660c02f277bc621cb7e2e61),
[SketcherGui::ViewProviderSketch::setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[TechDrawGui::QGIWeldSymbol::setFeature()](../../da/dcd/classTechDrawGui_1_1QGIWeldSymbol.html#a60cd5c59e3ca7e7b6f62e1245c3c8abd),
[SpreadsheetGui::WorkbenchHelper::setForegroundColor()](../../df/d59/classSpreadsheetGui_1_1WorkbenchHelper.html#a0c4b0d85871687dc806b5b8f55df043e),
[PartDesignGui::TaskDressUpParameters::setSelection()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#afbe9ba507cb0b88b7ef7250c5901d975),
[TechDrawGui::MDIViewPage::setTreeToSceneSelect()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a8c4e132accc95406f63a7e555cb1cbfc),
[TechDrawGui::TaskSectionView::setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCenterLine::setUiEdit()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a44074b04e6f03fde63d2f4ac7a3f0c33),
[TechDrawGui::TaskLeaderLine::setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskRichAnno::setUiEdit()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a3659e9cb13bc53ae36a3d7d16479d017),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[TechDrawGui::TaskSectionView::setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[TechDrawGui::TaskCenterLine::setUiPrimary()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a87a1eafc1c37ac2e6c0bbf8bfb73717a),
[TechDrawGui::TaskCosVertex::setUiPrimary()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#af4b9b21bba51de589fd14887b3b82150),
[TechDrawGui::TaskLeaderLine::setUiPrimary()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#ae4079f062fea88e52c9e7242cc8ecead),
[TechDrawGui::TaskRichAnno::setUiPrimary()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#ae2285e8fe902c048c0c4d27ee93b42ec),
[TechDraw::DrawHatch::setupFileIncluded()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a0846fb8f0861b48c08a9b869612e130b),
[TechDraw::DrawViewImage::setupImageIncluded()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a70665b6da416755ac2cdb36d9c9ecf6d),
[TechDraw::DrawGeomHatch::setupPatIncluded()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a60fb2b1d4310efa884589ce415b086c9),
[TechDraw::DrawViewSection::setupPatIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#af26e22d3b0683c955561590968b25275),
[TechDraw::DrawViewSection::setupSvgIncluded()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a3736e6db938d365a0866d6704bcb3fe0),
[TechDraw::DrawTileWeld::setupSymbolIncluded()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a9a0ec49268483ff93a086ca6a58c58da),
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a9072c1b8bf3ee43a0d82c0e266cc1f33),
[Gui::SelectionSingleton::setVisible()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab23ac3091ebd5ec52d897b3416a05e2d),
[DrawingGui::ViewProviderDrawingPage::showDrawingView()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#af7cd2898c5d4d289f22f0fb7c232984f),
[Gui::SelectionSingleton::slotDeletedObject()](../../d4/dca/classGui_1_1SelectionSingleton.html#a71d83e67e4de7417667efa24dc4c7ed5),
[Sketcher::SketchObject::solve()](../../d9/dad/classSketcher_1_1SketchObject.html#a0bcef04719586a7122d762061b2d4ac4),
[MeshGui::ViewProviderMesh::splitMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a3480f540c644cb38cd0a1ed1bc304d94),
[Gui::SelectionSingleton::sRemoveSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#af2933a9b72409431f7fd31d78ade3d5c),
[Gui::SelectionSingleton::sSetPreselection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a17d43ab4934b472aa7e9b5bf01127e25),
[PartDesignGui::TaskSketchBasedParameters::startReferenceSelection()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#ab7f3e182d79cb6a61aea29f403a759fd),
[PartDesignGui::TaskHelixParameters::startReferenceSelection()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ab03d8f0485fbf4d31967cd94d8b54a23),
[Gui::SelectionSingleton::sUpdateSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a33194bd56bf9dc3e9e893e8b7a66153b),
[TechDrawGui::TaskDetail::TaskDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a2017c373db55e0b43d386b536b34bc75),
[FemGui::TaskObjectName::TaskObjectName()](../../d3/d6b/classFemGui_1_1TaskObjectName.html#ae998f7ddece0813597d374c662db31b7),
[TechDrawGui::TaskSectionView::TaskSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a146b65deaafcbc3d957c00e2814de9a1),
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465),
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[PartDesignGui::ViewProvider::unsetEdit()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aeb01bc367ec2895032e0fcd1074528fb),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawProjGroupItem::unsetupObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979),
[PartDesignGui::ViewProviderAddSub::updateAddSubShapeIndicator()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a27d23424ce72a0f362904d73928fbc6c),
[TechDraw::DrawProjGroup::updateChildrenEnforce()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53d6b329649586210ae8e5f6eb6e6a2c),
[TechDraw::DrawProjGroup::updateChildrenLock()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aa9ea74d38f2710c6690b5a69879ae23b),
[TechDraw::DrawProjGroup::updateChildrenScale()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a34817922d5abecc72163f2b968e3a627),
[TechDraw::DrawProjGroup::updateChildrenSource()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5765aa3026040998e1c20dd4b71123f4),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[TechDrawGui::TaskLinkDim::updateDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#acff44dd09f905319bf7234cd9c0afd2e),
[TechDrawGui::TaskHatch::updateHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#a885b8fcb16ca312a825e37d5f4ee11b4),
[Gui::DocumentItem::updateItemSelection()](../../df/d15/classGui_1_1DocumentItem.html#a14563474d7f1a9b2024cd5aa953dcbe4),
[App::PropertyLinkBase::updateLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da),
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461),
[TechDrawGui::TaskWeldingSymbol::updateTiles()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#aac480071122ff57d72a8cba865b1c94c),
[TechDraw::DrawProjGroup::updateViews()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a080b64dfe4a1d4456558102c2c8def62),
[TechDrawGui::TaskWeldingSymbol::updateWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ae2c10ae5d73a0018daaa7b088b67fdf9),
[TechDrawGui::TaskProjGroup::viewToggled()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a53e5f0d366028da306ce2a74f96b0c14),
and
[PartGui::DlgExtrusion::writeParametersToFeature()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8d059573a157c9f9128d55b3c9a9fcc1).

## ◆ getOldLabel()

const std::string & App::DocumentObject::getOldLabel  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getOutList() [1/3]

const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & App::DocumentObject::getOutList  | ( | | ) |  const  
---|---|---|---|---  
  
returns a list of objects this object is pointing to by Links

Referenced by
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
and
[TechDraw::DrawViewCollection::rebuildViewList()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a2cddd1c4b006821c3ec11a31dedf7338).

## ◆ getOutList() [2/3]

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::DocumentObject::getOutList  | ( | [int](../../d1/da0/classint.html) | _option_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getOutList() [3/3]

void App::DocumentObject::getOutList  | ( | [int](../../d1/da0/classint.html) | _option_ ,   
---|---|---|---  
|  | std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _res_  
| ) | |  const  
  
## ◆ getOutListOfProperty()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::DocumentObject::getOutListOfProperty  | ( | [App::Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |  const  
---|---|---|---|---|---  
  
returns a list of objects linked by the property

## ◆ getOutListRecursive()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::DocumentObject::getOutListRecursive  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
returns a list of objects this object is pointing to by Links and all further
descended

## ◆ getParents()

std::vector< std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::string > > App::DocumentObject::getParents  | ( | [int](../../d1/da0/classint.html) | _depth_ = `0`| ) |  const  
---|---|---|---|---|---  
  
Obtain top parents and subnames of this object using its InList.

Referenced by
[PartDesignGui::makeBodyActive()](../../dc/d12/namespacePartDesignGui.html#ae1d1f749c569f8feca9b77df909ef722),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ getPathsByOutList()

std::vector< std::list< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > > App::DocumentObject::getPathsByOutList  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _to_| ) |  const  
---|---|---|---|---|---  
  
get all possible paths from this to another object following the OutList

## ◆ getPyObject()

| virtual [PyObject](../../df/d1b/classPyObject.html) * App::DocumentObject::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method returns the Python wrapper for a C++ object.

It's in the responsibility of the programmer to do the correct reference
counting. Basically there are two ways how to implement that: Either always
return a new Python object then reference counting is not a matter or return
always the same Python object then the reference counter must be incremented
by one. However, it's absolutely forbidden to return always the same Python
object without incrementing the reference counter.

The default implementation returns 'None'.

Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514).

Reimplemented in
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a4b39fb08f59a125dcc783cf93e25d86d),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a7a700a82e66b15d3eb4845ad75c194ab),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a57333609c76e9d1469163c8d70f75053),
[App::DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html#a8c2a18ad6bd291d0f6657e877c4f7a92),
[App::Part](../../da/d8d/classApp_1_1Part.html#a8efaf38ed9d96a1207ff4b6bb05955e5),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#a9e28639037238df4c8dafb4518ee86c4),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#ae23b16d8ba14ec40c3cd74aca0634f2e),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#a666f699fb9530523ef6467717f385096),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a49b5d225e27f3adf2cb0b8452fa84ef8),
[App::GeoFeature](../../d7/d75/classApp_1_1GeoFeature.html#a6837f9af91a2619c420f361033ab0da5),
[App::InventorObject](../../da/d11/classApp_1_1InventorObject.html#adb3523042b8befd61616bc05fedd290f),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a5a9445b1375ded9f86617e15151ec389),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#abb0ba3282d7a1b42eaeaaee6364afd42),
[Fem::FemResultObject](../../d3/d81/classFem_1_1FemResultObject.html#af6645066e6371ce9460ca9836cd5af6b),
[Fem::FemSetElementsObject](../../df/d49/classFem_1_1FemSetElementsObject.html#a5ea9bd5b13b1f95a0058d800a6166ab1),
[Fem::FemSetFacesObject](../../df/d72/classFem_1_1FemSetFacesObject.html#a4754f40e1edf8bc0a5701fa58a525625),
[Fem::FemSetGeometryObject](../../df/d59/classFem_1_1FemSetGeometryObject.html#a96a9315d631398747b4c9fcfc784ee9a),
[Fem::FemSetNodesObject](../../dc/d59/classFem_1_1FemSetNodesObject.html#a879bdd1e2d66688ae040e2a4d51772a3),
[Fem::FemSetObject](../../d8/dbe/classFem_1_1FemSetObject.html#ac7ab5f7744ff44d8d4f6f4bb6e022f66),
[Fem::FemSolverObject](../../d1/dd0/classFem_1_1FemSolverObject.html#abf5e279df0983cef9533c8f3095e5574),
[PartDesign::Feature](../../d7/d51/classPartDesign_1_1Feature.html#a7b572936974ad2fb3d78fe729d3e1757),
[Path::FeatureArea](../../da/d1e/classPath_1_1FeatureArea.html#a71e18a904362f9e20f126aca4f13b8e8),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#ab7f800e910601271c9a4bc2480dad5f2),
[Path::FeatureCompound](../../d2/d43/classPath_1_1FeatureCompound.html#a08d674d0a02ef64d5572e51c3689fd2d),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a5b35961553442da622521648b1f50365),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#aa511366030cf224da9a3a0d17b07606e),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a446f297751fa8bd5511d4d48f6dc75ed),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a206b0ca34b87f79762924fedec8c7fd1),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#ad0a08bbe311a5147f49ab0f3647c88dd),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aead757612a7d1a557eeeb43e0caec8bd),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a0e979b8f73ef5fea5997dc8e8e12b9d4),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a00b92083449ce106a622bf7b0ca3fdea),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a4e296aa3a79c48e108afe2d9db30731f),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a9a71017db88391c3248e29a3931be915),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad9e24e34ca274c67e594e384a37e2cb9),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a9579e5a76ef1c70cc24701d4bba32c6c),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a7a2970aaacc965d3d4c3b3a949fcb21f),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#aa02555ef8da0ade9bf32d826683869d6),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a206dea2db611b805e68fc860a1032597),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a87cddb7857e5d66215c929844d3bd438),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#a55ad5df210dcaeadeaf5b8504dfdc736),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acaf6822e5ff679aae0ff66759d7135dc),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a28fc999e36c9404361ca24453f424678),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#af82b1daff82fedafa74673a607bc38a4),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a3e332a5c716d9cc5145fa9afa7fcacff),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab0f733c1df0bd35133eb9d61e5670fe4),
and
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a6406ae57714b08e7d99c03f1bb4d652c).

Referenced by
[Gui::ViewProviderPythonFeatureImp::canDropObjectEx()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a0e25683945efce8a2acca7c98288dbee),
[Gui::ViewProviderPythonFeatureImp::dropObjectEx()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#ad8b0939f5e8dce59a6217e27a5ff70f7),
[App::LinkBaseExtension::extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[Gui::MDIViewPy::getActiveObject()](../../d5/df9/classGui_1_1MDIViewPy.html#a96acaf86145df05cfb268c9e0914a7b8),
[Gui::View3DInventorPy::getActiveObject()](../../d3/df7/classGui_1_1View3DInventorPy.html#a7abd80eb00239214e914b8fa3f802eba),
[Gui::View3DInventorPy::getattr()](../../d3/df7/classGui_1_1View3DInventorPy.html#ace515e29223696787d94d3a11cc02cfd),
[App::RangeExpression::getRange()](../../da/d8b/classApp_1_1RangeExpression.html#a1fee8772a70c049b0fb2ce7c629e8fd9),
[App::FeaturePythonImp::redirectSubName()](../../de/d49/classApp_1_1FeaturePythonImp.html#aab242ba739e239fe38f7e42e1e9084c4),
and
[Gui::ViewProviderPythonFeatureImp::replaceObject()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a46d467216f88b4c1d0b71a3910e7da31).

## ◆ getStatus()

unsigned long App::DocumentObject::getStatus  | ( | | ) |  const  
---|---|---|---|---  
  
return the status bits

## ◆ getStatusString()

const char * App::DocumentObject::getStatusString  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
get the status Message

Referenced by
[FemGui::TaskDlgMeshShapeNetgen::accept()](../../dc/db4/classFemGui_1_1TaskDlgMeshShapeNetgen.html#aa88c49eb6c4ad7cd760e8fcb2c3181be),
[FemGui::TaskDlgFemConstraint::accept()](../../d8/d18/classFemGui_1_1TaskDlgFemConstraint.html#a61fcc7a973c20d15a3f3fd173de45115),
[FemGui::TaskDlgFemConstraintInitialTemperature::accept()](../../d9/d8a/classFemGui_1_1TaskDlgFemConstraintInitialTemperature.html#a417fa6e0a784395a4285594b00043771),
[PartGui::OffsetWidget::accept()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#a791a744197288c394c011dbb879a143c),
[PartGui::ThicknessWidget::accept()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#a56dbb59f2cea1ccb8c8b842997c35f48),
[PartDesignGui::TaskDlgFeatureParameters::accept()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#abfc2d8ecb714c2b558cc8feb07fa55c3),
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06),
[SurfaceGui::FillingPanel::accept()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#a310725e1fbda946f1edfb97d9fd46fbb),
[SurfaceGui::FillingEdgePanel::accept()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a8f8ff8037f61c7d70836740c12cf9e3f),
[SurfaceGui::GeomFillSurface::accept()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a21cfb55c39fdd9cbe947ef52714665dd),
[SurfaceGui::SectionsPanel::accept()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a08a26215cfddf89b23a47f3b37f8fbe5),
[SurfaceGui::GeomFillSurface::changeFillType()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#aa2180cd7b8c690d2addc40f808eefafc),
and
[Gui::DocumentObjectItem::displayStatusInfo()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a235f26b8fbf37e4e4efccdae9cbbada0).

## ◆ getSubObject()

| virtual [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::DocumentObject::getSubObject  | ( | const char *  | _subname_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ = `nullptr`,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ = `true`,   
|  | [int](../../d1/da0/classint.html) | _depth_ = `0`  
| ) | |  const  
virtual  
  
Get the sub element/object by name.

Parameters

     subname| a string which is dot separated name to refer to a sub element or object. An empty string can be used to refer to the object itself  
---|---  
pyObj| if non zero, returns the python object corresponding to this sub
object. The actual type of this python object is implementation dependent. For
example, The current implementation of
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html "Base class of all
shape feature classes in FreeCAD.") will return the TopoShapePy, event if
there is no sub-element reference, in which case it returns the whole shape.  
mat| If non zero, it is used as the current transformation matrix on input.
And output as the accumulated transformation up until and include the
transformation applied by the final object reference in `subname`. For
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html "Base class of all
shape feature classes in FreeCAD."), the transformation is applied to the
TopoShape inside `pyObj` before returning.  
transform| if false, then it will not apply the object's own transformation to
`mat`, which lets you override the object's placement (and possibly scale).  
depth| depth limitation as hint for cyclic link detection  
  
Returns

    The last document object referred in subname. If subname is empty, then it shall return itself. If subname is invalid, then it shall return zero. 

Reimplemented in
[Part::Datum](../../db/d0b/classPart_1_1Datum.html#ac5c48627e7edd4fde0e66a86603a0ca8),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#aecc131a5ce7f03c5041a475003456b38),
[PartDesign::CoordinateSystem](../../db/d46/classPartDesign_1_1CoordinateSystem.html#aeb5d09866ebc21adafb8ee43acc9205b),
and
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#afb7e01deac9646afcd5dc1b2aa07042b).

Referenced by
[App::PropertyLinkSubList::adjustLink()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ab5bc8a3cb854f5b7643bfdcc4d0cb525),
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[App::GroupExtension::extensionGetSubObject()](../../da/d3a/classApp_1_1GroupExtension.html#a9f6afe4878329f62b99288df7224cec2),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[App::LinkBaseExtension::extensionGetSubObject()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a1fc10a398449cc2f971457df8038ef0a),
[Gui::DocumentItem::findItem()](../../df/d15/classGui_1_1DocumentItem.html#ac20f1bb6efdbc301be559e6a0260ca28),
[Part::Feature::getShapeOwner()](../../d7/d7e/classPart_1_1Feature.html#afc51965464e6e44329801279bad18077),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[App::ObjectIdentifier::resolveProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e),
[App::PropertyLinkBase::restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb),
[Gui::Document::setEdit()](../../de/d4e/classGui_1_1Document.html#a2064c6eb4172240d40a7f409febc81a9),
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[App::PropertyLinkBase::updateLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da),
and
[Gui::LinkView::updateLink()](../../da/d11/classGui_1_1LinkView.html#a956208e8fec0e73f0ba22880cbb3e6d2).

## ◆ getSubObjectList()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > App::DocumentObject::getSubObjectList  | ( | const char *  | _subname_| ) |  const  
---|---|---|---|---|---  
  
Return a list of objects referenced by a given subname including this object.

## ◆ getSubObjects()

| virtual std::vector< std::string > App::DocumentObject::getSubObjects  | ( | [int](../../d1/da0/classint.html) | _reason_ = `0`| ) |  const  
---|---|---|---|---|---  
virtual  
  
Return name reference of all sub-objects.

Parameters

     reason| indicate reason of obtaining the sub objects  
---|---  
  
The default implementation returns all object references in
[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html "The general Link
Property Main Purpose of this property is to Link Objects and Features in a
document..."), and
[PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html), if any

Returns

    Return a vector of subname references for all sub-objects. In most cases, the name returned will be the object name plus an ending '.', which can be passed directly to [getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6 "Get the sub element/object by name.") to retrieve the name. The reason to return the name reference instead of the sub object itself is because there may be no real sub object, or the sub object need special transformation. For example, sub objects of an array type of object. 

Reimplemented in
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a77c492fd94c081dc46522355954679cc).

Referenced by
[App::LinkBaseExtension::extensionGetSubObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a666a0bbcc82f6538d3dfca95e4937ad5),
and
[PartDesign::Body::getSubObjects()](../../dd/db8/classPartDesign_1_1Body.html#a77c492fd94c081dc46522355954679cc).

## ◆ getViewProviderName()

| virtual const char * App::DocumentObject::getViewProviderName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
returns the type name of the ViewProvider

Reimplemented in
[App::TextDocument](../../d9/de9/classApp_1_1TextDocument.html#a010efb1a1a5819713c16b16e5f6f8f5d),
[Fem::FemAnalysis](../../de/d36/classFem_1_1FemAnalysis.html#a75d52095461733112cac51f28865f75a),
[Fem::Constraint](../../d0/d11/classFem_1_1Constraint.html#a065453c93475148e65186c29361f50aa),
[Image::ImagePlane](../../dd/d68/classImage_1_1ImagePlane.html#a883ea4d4461d7afdf00611dab95f3280),
[Mesh::Curvature](../../d2/d39/classMesh_1_1Curvature.html#a422aa32099ce3ff70d074b912364bc8b),
[Mesh::Export](../../d6/d40/classMesh_1_1Export.html#aabd85f6fc831835e94463a518e9d9a01),
[Mesh::Transform](../../d3/def/classMesh_1_1Transform.html#a568b7a70eb8e58db1240aca9cb8002dd),
[Mesh::TransformDemolding](../../dc/da9/classMesh_1_1TransformDemolding.html#a24ee0e78f020046e18c1c765ac56faf1),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a17ceb6d89b91ff5f9e343ce1d61c311f),
[PartDesign::Feature](../../d7/d51/classPartDesign_1_1Feature.html#a2c03b79f943c5cc5d6c48c7d5412c2c4),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#abeb6ef081749cf15b04eb5d4bc0b7660),
[PartDesign::Pad](../../d9/d14/classPartDesign_1_1Pad.html#ad9fe085505d772f5b5f8577efafa750b),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a37828247f292a1c891a1a851b8bb9439),
[Points::Structured](../../d0/d43/classPoints_1_1Structured.html#a4bf8c168e9ea1057825d477744a2392a),
[App::DocumentObjectGroup](../../d8/d75/classApp_1_1DocumentObjectGroup.html#a4329c36cf27e6abab9126a75545335b0),
[App::Part](../../da/d8d/classApp_1_1Part.html#a11fd84ec6cafdffb21365168b44f427a),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#ab165a67d5f1065c03fd7a81e0b0a8218),
[App::Annotation](../../d2/d97/classApp_1_1Annotation.html#ae6511d3c419dd73dd5218b3a21bee1be),
[App::AnnotationLabel](../../dc/d4a/classApp_1_1AnnotationLabel.html#a51903cdbfb1f3a3659555d029c72b746),
[App::DocumentObjectFileIncluded](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a91002a42b9fddea0055e72f19a234362),
[App::FeatureTest](../../df/dea/classApp_1_1FeatureTest.html#a79060d534810c7f911142f7e51fb9df3),
[App::FeatureTestException](../../d5/d03/classApp_1_1FeatureTestException.html#a84420cfb0409a3e99a91e257c262e03b),
[App::InventorObject](../../da/d11/classApp_1_1InventorObject.html#ab214fd7e4fc959d34edf7a471ceb1f2b),
[App::MaterialObject](../../da/d09/classApp_1_1MaterialObject.html#adb6b47472dca726113243198293cc2f3),
[App::MeasureDistance](../../d7/d61/classApp_1_1MeasureDistance.html#a06da51e198498a0e7238ea8397e7e982),
[App::Origin](../../d9/d8b/classApp_1_1Origin.html#aed36cdb6e29802acaaff45f2a4ea93b5),
[App::Plane](../../d3/dc3/classApp_1_1Plane.html#a91d14af3c788f84530a83994920e3ece),
[App::Line](../../d1/db2/classApp_1_1Line.html#a62e61ffd2c76ab3a54d08e527ad67eb7),
[App::Placement](../../d7/d32/classApp_1_1Placement.html#a7807796197a47aed157058636e0008fd),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#aa7698fae4d110c9be01c3348dbc1d215),
[Drawing::FeatureClip](../../d5/d4a/classDrawing_1_1FeatureClip.html#a23ee76ebfd7ff960495b5ef87a3a23e2),
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a3963bdbbb1b8302ab922ec9579bdb35c),
[Drawing::FeatureView](../../db/d1f/classDrawing_1_1FeatureView.html#af13c6e75624fc003e6b9eff0182d2c8b),
[Drawing::FeatureViewAnnotation](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a35c788cd94e0d186b331b42ecabcf699),
[Drawing::FeatureViewPart](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a0c567f571981b9e22ac30e93c165a07c),
[Drawing::FeatureViewSpreadsheet](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#ad70e3f8ae876b530833bbeaf0652ed9d),
[Drawing::FeatureViewSymbol](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a7aa9d8bd4aa8db63976ac0945d0907f5),
[Drawing::PageGroup](../../d5/d47/classDrawing_1_1PageGroup.html#a139a0f1a8a0661fb1dc1721e9792cbb7),
[Fem::ConstraintBearing](../../df/d0a/classFem_1_1ConstraintBearing.html#affb39b726801ee3550a835011a5590b9),
[Fem::ConstraintContact](../../db/d7c/classFem_1_1ConstraintContact.html#ad5b0d250bf04ad2ce7f4c2caa0fcb11f),
[Fem::ConstraintDisplacement](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a5a72d4921385c74653c7e870bd42c107),
[Fem::ConstraintFixed](../../d1/d43/classFem_1_1ConstraintFixed.html#a7329ffeb4af01c015e67fbd875c00b2a),
[Fem::ConstraintFluidBoundary](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#a5db1fdb44a292d4cfd05d5e510e65076),
[Fem::ConstraintForce](../../d6/d63/classFem_1_1ConstraintForce.html#ad4a16b665e850a75cdb09da98b896ef7),
[Fem::ConstraintGear](../../d8/d55/classFem_1_1ConstraintGear.html#a8dccf82b270c0b353562a5491ca11e47),
[Fem::ConstraintHeatflux](../../de/dce/classFem_1_1ConstraintHeatflux.html#ae6d271f8e0f3ae228d17ac041bf59b4d),
[Fem::ConstraintInitialTemperature](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#a572b9a7a76173b11a7122c4cff20d044),
[Fem::ConstraintPlaneRotation](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#a538ba5bb85f422ee5eb8336d35057bc5),
[Fem::ConstraintPressure](../../dd/d5e/classFem_1_1ConstraintPressure.html#a62190ab9a7fadd56435473a94cfca807),
[Fem::ConstraintPulley](../../d3/dec/classFem_1_1ConstraintPulley.html#aad27b1d1f07f04761136bc22975bdefa),
[Fem::ConstraintSpring](../../dc/d42/classFem_1_1ConstraintSpring.html#ad07594106177b630b282573b8fa50b33),
[Fem::ConstraintTemperature](../../d7/dff/classFem_1_1ConstraintTemperature.html#a45212948bb3565ba63081b688d41d83b),
[Fem::ConstraintTransform](../../d8/d3c/classFem_1_1ConstraintTransform.html#a0c0871634fc1ce302425beaf255f8b74),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#aabec8c9798199d550f63dd728dc826d5),
[Fem::FemMeshShapeNetgenObject](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#a7638c2d7108796448091b0428308c57e),
[Fem::FemMeshShapeObject](../../d0/d41/classFem_1_1FemMeshShapeObject.html#a10ebec1a486ee5f074c5da8dfc8c8c01),
[Fem::FemPostClipFilter](../../dc/d06/classFem_1_1FemPostClipFilter.html#a680167a92d723a5f64537b1441b109c9),
[Fem::FemPostDataAlongLineFilter](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#a02e8397b30a676a2c624c5b60ee1261a),
[Fem::FemPostDataAtPointFilter](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ac1273c02e27e83e7e4f8cc3da4233671),
[Fem::FemPostScalarClipFilter](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a2b984c422c96fe04c111d771f586f1c4),
[Fem::FemPostWarpVectorFilter](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a7d2fb1b28fc12fc0916bdc02d71afcae),
[Fem::FemPostCutFilter](../../da/d89/classFem_1_1FemPostCutFilter.html#a63cc945122dd37ee05da120713a8664b),
[Fem::FemPostFunction](../../d3/d87/classFem_1_1FemPostFunction.html#a8afa80ed93657aa3496ac8b5a0c4047c),
[Fem::FemPostFunctionProvider](../../dd/d47/classFem_1_1FemPostFunctionProvider.html#afdf4500f773b6197173beb01d902ba99),
[Fem::FemPostPlaneFunction](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#a5f62a965cf1720317225251b0ecef0e3),
[Fem::FemPostSphereFunction](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#a615f7fbf867a46413daa16ada12467c7),
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a152fb134d8268cd5b70393c72a7b0b50),
[Fem::FemResultObject](../../d3/d81/classFem_1_1FemResultObject.html#a1d1a6b29980f3ebd523cebb1f5f1232f),
[Fem::FemSetElementsObject](../../df/d49/classFem_1_1FemSetElementsObject.html#ad8cb910faaf29ce4f82e1a268e47f465),
[Fem::FemSetFacesObject](../../df/d72/classFem_1_1FemSetFacesObject.html#a1306e67ec58a3abcd1af10017caccff7),
[Fem::FemSetGeometryObject](../../df/d59/classFem_1_1FemSetGeometryObject.html#a3be9b45308762a438e684632b824c3e6),
[Fem::FemSetNodesObject](../../dc/d59/classFem_1_1FemSetNodesObject.html#a306a13a58edf2720872f96b2ef3ea46c),
[Fem::FemSolverObject](../../d1/dd0/classFem_1_1FemSolverObject.html#a66b619f3ead985154fbf9a45bedeb877),
[Inspection::Feature](../../d6/d23/classInspection_1_1Feature.html#a563c47162d9d913e5844369560248bb6),
[Inspection::Group](../../d7/d0a/classInspection_1_1Group.html#a9b419caa870718a97c01c874e6b325a1),
[Part::CustomFeature](../../da/d46/classPart_1_1CustomFeature.html#affb375985571715ac26ef830b122299c),
[Part::Chamfer](../../d7/d75/classPart_1_1Chamfer.html#a21e81e1def93e26608031616ee73306a),
[Part::Compound](../../d7/d98/classPart_1_1Compound.html#a1b7a36f1252452d8761827310cdd37d8),
[Part::Fillet](../../d4/da4/classPart_1_1Fillet.html#a4528bebcff91d76e581d47abca948d22),
[Part::FeatureGeometrySet](../../d6/d80/classPart_1_1FeatureGeometrySet.html#ac5c00974b397f98753a7cf8a6e6b2fec),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#ac91562e02988ffa881af6cc3d6bb0b97),
[Part::Boolean](../../da/d3a/classPart_1_1Boolean.html#a165c44282a7bae9aa7ae2af3d758e1c3),
[Part::Box](../../dc/d80/classPart_1_1Box.html#aa16e40176b08021a2e038f67eb8e99a4),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#a816d4daf4c875fee9b59eba4e0977b28),
[Part::MultiCommon](../../d1/df7/classPart_1_1MultiCommon.html#a6f3f1cc19a4e7d99438944e1facc7859),
[Part::CurveNet](../../d9/d41/classPart_1_1CurveNet.html#a6a3567107331b1b32c73b09a4c3cee9d),
[Part::MultiFuse](../../df/dbc/classPart_1_1MultiFuse.html#a0edc68780b1d845e9d9cc2cde41e3676),
[Part::ImportBrep](../../d8/d3e/classPart_1_1ImportBrep.html#a69e65f393e994566f374ae4b46f383e1),
[Part::ImportIges](../../d2/d1d/classPart_1_1ImportIges.html#a3cfeb6c946820acc58ba302b16a13b2d),
[Part::ImportStep](../../d4/de2/classPart_1_1ImportStep.html#a67bea9be9b63959c47a09807d981bb0d),
[Part::Spline](../../da/d0b/classPart_1_1Spline.html#aab4528bfb2d41a1cf6efc7e72084e106),
[Part::FeatureExt](../../d5/de3/classPart_1_1FeatureExt.html#a2fcfcb4710f8e3633a19daf5492ac029),
[Part::FeatureReference](../../d2/da1/classPart_1_1FeatureReference.html#a7afd4f26453f5304b21c92d35d3780c3),
[Part::RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html#a9dcd5d81fb8a64fdaecfcbd7476cbacf),
[Part::Loft](../../d3/d52/classPart_1_1Loft.html#a5c557a0df8854a6e77e2acb896078026),
[Part::Sweep](../../df/dc6/classPart_1_1Sweep.html#ac8c23359e337fca4dee8ec0ade8f65ec),
[Part::Thickness](../../db/d73/classPart_1_1Thickness.html#a696c6f9cb84d5522637eac4038ee25bb),
[Part::Refine](../../d4/d0a/classPart_1_1Refine.html#a1adc90330af745c00fcb808c510fa240),
[Part::Reverse](../../d4/d24/classPart_1_1Reverse.html#a1f26d0d26f17e2198de8fb96ead38ba5),
[Part::Vertex](../../de/d96/classPart_1_1Vertex.html#a6e398a3c8a0b9185d296706a76dd15ba),
[Part::Line](../../d3/dfe/classPart_1_1Line.html#a90ccc0d13e5eedfc70572927c413cbd3),
[Part::Plane](../../d0/d1c/classPart_1_1Plane.html#ac53bad6b7c232cd6680694ef4a22dc6d),
[Part::Sphere](../../dc/d57/classPart_1_1Sphere.html#ab7a85b4d1da57b8ed605b0fab269371b),
[Part::Ellipsoid](../../d4/dc8/classPart_1_1Ellipsoid.html#a808563f083e36371d964b61e7a89e7bf),
[Part::Cylinder](../../dd/d12/classPart_1_1Cylinder.html#a63e510589648eb91092ae694d97e01b4),
[Part::Prism](../../dc/d69/classPart_1_1Prism.html#a5fcf5aa3b34c92b830067724968871a8),
[Part::RegularPolygon](../../d2/d69/classPart_1_1RegularPolygon.html#a667d0c9020947057a168400aefa83ca7),
[Part::Cone](../../d2/d8f/classPart_1_1Cone.html#a8f3efad96afea5ff1b31eccb344d0e88),
[Part::Torus](../../db/d42/classPart_1_1Torus.html#a58661678e7e24e89dcbded23ed12b367),
[Part::Helix](../../df/d49/classPart_1_1Helix.html#a69947cc9b2cd30bee890bd488b6bb6a5),
[Part::Spiral](../../d2/d3f/classPart_1_1Spiral.html#aa2b29c6b8066e8078ba8aa3006c6ba93),
[Part::Wedge](../../d5/dc5/classPart_1_1Wedge.html#a6b9e077460570ceefc0f6887a32de629),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#ad6d85d697bfa52a3f177fdd98e7d7b3b),
[PartDesign::Line](../../d0/d2a/classPartDesign_1_1Line.html#aa71c5348fb3c20ab7f332b3b644050f2),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#af3f2c24d2138d62d39c5c37851123564),
[PartDesign::Draft](../../df/d0e/classPartDesign_1_1Draft.html#a2555627f497214be1ecae19f539ef028),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#ad0661790f27b59afc62555b81cec06ac),
[PartDesign::Groove](../../d7/de3/classPartDesign_1_1Groove.html#a991f5a25b326c186172dc2d5920440b8),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#aaf4182ab997d63f545bfb3b14118d3b2),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#a9581e306f8bcc9678d8332a2ab167f4b),
[PartDesign::LinearPattern](../../d2/d86/classPartDesign_1_1LinearPattern.html#ae74ebc2f26b00b94bdfd73ca865aab2c),
[PartDesign::Loft](../../d0/deb/classPartDesign_1_1Loft.html#ae60110396ba0db126cc27f2a2e8f1e67),
[PartDesign::Mirrored](../../d6/d91/classPartDesign_1_1Mirrored.html#aadf18874aa9105a6c06db4267434420a),
[PartDesign::MultiTransform](../../d2/df8/classPartDesign_1_1MultiTransform.html#a11646a9d772a2d683f924487fe501b7d),
[PartDesign::Pipe](../../da/d61/classPartDesign_1_1Pipe.html#ad5ba91ee349c120ba85a7adecc980413),
[PartDesign::Pocket](../../d1/d89/classPartDesign_1_1Pocket.html#a763760cb9806196766f3d06580c5d594),
[PartDesign::PolarPattern](../../da/d5b/classPartDesign_1_1PolarPattern.html#a9a9d5989d27b03c2943e0e7ff4f37a7d),
[PartDesign::Revolution](../../d2/de6/classPartDesign_1_1Revolution.html#ab59e84385ede3a181fb26adf949ab382),
[PartDesign::Scaled](../../db/dce/classPartDesign_1_1Scaled.html#a37d25c929fd275dfc413b91e3d5c4535),
[PartDesign::Thickness](../../d4/d22/classPartDesign_1_1Thickness.html#aab2ae40305384c87c6bfc6b27f78f83f),
[Path::FeatureArea](../../da/d1e/classPath_1_1FeatureArea.html#aa2c3d370ea92219ffea0743ff6971a0c),
[Path::FeatureAreaView](../../d3/db4/classPath_1_1FeatureAreaView.html#ad8cafa2bf026258985f17d6be1dcb699),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#a38f46f457634b96358bb2bcfb83bd431),
[Path::FeatureCompound](../../d2/d43/classPath_1_1FeatureCompound.html#a1695d8fa0c9b3e1fa9ec7cf52ae5f971),
[Path::FeatureShape](../../da/d9b/classPath_1_1FeatureShape.html#afd3d31bb8623b0d7122c1e101b4a8b29),
[Raytracing::LuxFeature](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a587597dd339344c9531c233715555809),
[Raytracing::LuxProject](../../d5/de6/classRaytracing_1_1LuxProject.html#acc1ec11628af262ccc31bc6a6a29d94f),
[Raytracing::RayFeature](../../d4/df2/classRaytracing_1_1RayFeature.html#ae50fc985618304a5ad6f280ff5d47649),
[Raytracing::RayProject](../../d2/d89/classRaytracing_1_1RayProject.html#abcb645da3a29f76716eb3717d8f847ff),
[Raytracing::RaySegment](../../d5/d48/classRaytracing_1_1RaySegment.html#a35859fdae074a03569127601ceb91df6),
[Robot::Edge2TracObject](../../d8/df5/classRobot_1_1Edge2TracObject.html#a0030a34a00e7a00bae9e8ddf4eb5c514),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a45890ed626a192fe904d609c97d36096),
[Robot::TrajectoryCompound](../../df/de7/classRobot_1_1TrajectoryCompound.html#a7c47e928f7a6fe8decc4fc33f0a44450),
[Robot::TrajectoryDressUpObject](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a4258df3457be1c6109a118c264d1680b),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#a342c6966cd842bdeec954dad3ad52b02),
[Sandbox::SandboxObject](../../da/dd9/classSandbox_1_1SandboxObject.html#a6aba67b66139deec9d0c04622c4a9ed8),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a535479159355c13597c8cdfc991be62c),
[Surface::Filling](../../d8/df7/classSurface_1_1Filling.html#aeb1fad678e91e900516ed1d21f51ab84),
[Surface::GeomFillSurface](../../d7/d0d/classSurface_1_1GeomFillSurface.html#aa74aedc046948d5446ca742fe9b74b7d),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a69bf45d6bc01eab28f0dfff7739ef0ca),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a1e0a5a27731a6dc2f85861db1e93b94a),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#aa7cf59af52e410f785e4ba6049ea8729),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a5667f597bf3237483bfc1c334b2b77e9),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a5e2bb34cb5665367c3cbf87931f2f94b),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a47621a22b8c723e02b447293dc00666b),
[TechDraw::DrawViewAnnotation](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a6f95877fe65870bfec4c1898c74f0edc),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a92f82cf15f2d9de14ea4da8eebb2d675),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a4f6bac9b3212856785d8d6fd773bf513),
[TechDraw::DrawViewSpreadsheet](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a3d2759e12c7516cf144e407dcd77dfd5),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#a793a33c2f16fee0d56258247808ec90a),
[App::Link](../../df/d9b/classApp_1_1Link.html#ac2998ffbd4d24e3f15999d7a0b0e0e6d),
[App::LinkElement](../../d0/d3e/classApp_1_1LinkElement.html#a276cc87d8f60b9c61a6a62170dc06416),
[App::LinkGroup](../../de/d15/classApp_1_1LinkGroup.html#ad3604a6d0169d04afd2e718a2e542394),
[Part::Extrusion](../../db/d6c/classPart_1_1Extrusion.html#a9e1a440c949a43f27aabc36cd37a0d05),
[Part::Face](../../dc/dbf/classPart_1_1Face.html#a2bab6a64261b1b7ae6dadec292bae098),
[Part::Offset](../../d0/dda/classPart_1_1Offset.html#adb16278676d5708a4afcd7dc8a13baf4),
[Part::Offset2D](../../d7/dcf/classPart_1_1Offset2D.html#a865aa4949e3a97d5e935df05a355d53c),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a294e315a6d8c291d1cf844048360f5be),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#a02d5bc5612b8e00b2e05e2db7b5060c3),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a1bc5f1dfdd6f45caea39870264b4f6a3),
[PartDesign::CoordinateSystem](../../db/d46/classPartDesign_1_1CoordinateSystem.html#a2f643a3020f265227af019b5b1dba3db),
[PartDesign::Point](../../da/d0d/classPartDesign_1_1Point.html#ae5ffeef9552a4897bbfc49aeb7f12d9b),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#a7b5a61b482d48b18bdb2cd3c6d10057f),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a7b6d5aa1576e82a98538b8a54e31715f),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#abc291e7631842e2ff02f416512f76871),
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#ab619be5d78bd54c93fb9d513bd3027e3),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a1ba12b501c1b2932562ab2ef7c24fcf2),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a83f2e3a4b335b6bba0234e4dbe8dbd08),
[Surface::Extend](../../d1/d22/classSurface_1_1Extend.html#afa0c450c1f4382efdb3825abfa2b9ce1),
[Surface::Sections](../../d7/d6e/classSurface_1_1Sections.html#a7e679c7d552bf4796a8634bd461dfffe),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a1aa5204cf43dc4859cddde2a3aea0298),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a5f8df26507de585e09689772a2efece1),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#ab40cfc82ad6c77c90f9c9f86462aa9d1),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#afdaea195c692e846577b9d0f1336a765),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aacb532017332cd9448b165ca62b49faf),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#ae27b46faa2771de204c9f402cfee6123),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#a84501d01185b2565ad4402d615bd3225),
[TechDraw::DrawViewArch](../../df/dc6/classTechDraw_1_1DrawViewArch.html#a3e06cc9fbcc8fa30ee183b5ef50f9280),
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a7a948475e166e0d10b73ae474828e70a),
[TechDraw::DrawViewDetail](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#a15105110ebf6ea925fe8bb8c7febc9fd),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2d1ff26cc82e13f769a4979c1f120c41),
[TechDraw::DrawViewDraft](../../df/d84/classTechDraw_1_1DrawViewDraft.html#a18182ff09a62b6f4d71b7cb77b2ddc86),
[TechDraw::DrawViewImage](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a81f1f30167f0aa59169ff6dabe36c3c9),
[TechDraw::DrawViewMulti](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a366d14c81f0f50d4a30b497aef29a779),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a7d22e36327ea0bd5d3763c453da5523b),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4022e055d9c94dfb51918502164821f4),
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a49779da8a409a729617b27c133339abf),
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a27eb7814af6dadf93def2e6ea142dfb7),
and
[Part::Datum](../../db/d0b/classPart_1_1Datum.html#a2d48d3315e6408d56e28aa806fc88a24).

Referenced by
[Gui::FreeCADGui_subgraphFromObject()](../../d9/dad/namespaceGui.html#a1562062f6fcff8f9ec05618c80435514),
and
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb).

## ◆ getViewProviderNameOverride()

| virtual const char * App::DocumentObject::getViewProviderNameOverride  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
This function is introduced to allow Python feature override its view
provider.

The default implementation just returns
[getViewProviderName()](../../d2/de4/classApp_1_1DocumentObject.html#a6a8a0335a6da079225b433b4b291653a).

The core will only accept the overridden view provider if it returns true when
calling Gui::ViewProviderDocumentObject::allowOverride(obj). If not, the view
provider will be reverted to the one returned from
[getViewProviderName()](../../d2/de4/classApp_1_1DocumentObject.html#a6a8a0335a6da079225b433b4b291653a).

Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
and
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4).

## ◆ getViewProviderNameStored()

const char * App::DocumentObject::getViewProviderNameStored  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb).

## ◆ hasChildElement()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::hasChildElement  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
return true to activate tree view group object handling and element visibility

Referenced by
[App::LinkBaseExtension::extensionHasChildElement()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aff055283d9be0810467d1e9540243415).

## ◆ hasHiddenMarker()

| static const char * App::DocumentObject::hasHiddenMarker  | ( | const char *  | _subname_| ) |   
---|---|---|---|---|---  
static  
  
Check if the subname reference ends with hidden marker.

Referenced by
[Gui::ViewProvider::hasHiddenMarker()](../../d3/db3/classGui_1_1ViewProvider.html#a7a9cd7fe3f4d16e3094e5178cefdc45f),
and
[App::GeoFeature::resolveElement()](../../d7/d75/classApp_1_1GeoFeature.html#aef8b2a9f75e796e56f7921d93b2f2a8a).

## ◆ hiddenMarker()

| static const std::string & App::DocumentObject::hiddenMarker  | ( | | ) |   
---|---|---|---|---  
static  
  
Special marker to mark the object as hidden.

It is used by
[Gui::ViewProvider::getElementColors()](../../d3/db3/classGui_1_1ViewProvider.html#adb2812496e4e7143f9751c3143a42e78),
but exposed here for convenience

Referenced by
[Gui::ViewProvider::hiddenMarker()](../../d3/db3/classGui_1_1ViewProvider.html#ad7ec8cdec25d51ca8309c477c6728a3c).

## ◆ isAttachedToDocument()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::isAttachedToDocument  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html#aa76992a5607128ed5a5a7434cbd857c0).

## ◆ isElementVisible()

| virtual [int](../../d1/da0/classint.html) App::DocumentObject::isElementVisible  | ( | const char *  | _element_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Get sub-element visibility.

Returns

    -1 if element visibility is not supported or element not found, 0 if element is invisible, or else 1 

Referenced by
[App::LinkBaseExtension::extensionIsElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#acf07fd549eb15bb1f7a3533b2ee58925),
and
[Gui::SelectionSingleton::setVisible()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab23ac3091ebd5ec52d897b3416a05e2d).

## ◆ isError()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isError  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
set this feature to error

Referenced by
[Gui::DocumentObjectItem::displayStatusInfo()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a235f26b8fbf37e4e4efccdae9cbbada0),
[Mesh::Curvature::execute()](../../d2/d39/classMesh_1_1Curvature.html#a76bfebcb28cee108275564ade910411c),
[Mesh::Export::execute()](../../d6/d40/classMesh_1_1Export.html#a56265dded005a8be13258af1b273ed51),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[PartDesignGui::TaskDressUpParameters::hideOnError()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#aab09b985154e8e03796ddf05f0d36f81),
[PartDesignGui::ViewProviderTransformed::recomputeFeature()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a14cb4d7a2487ad732593fed6ece13ca6),
and
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465).

## ◆ isExporting()

[int](../../d1/da0/classint.html) App::DocumentObject::isExporting  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::ObjectIdentifier::toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f).

## ◆ isInInList()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isInInList  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _objToTest_| ) |  const  
---|---|---|---|---|---  
  
test if this object is directly (non recursive) in the InList

## ◆ isInInListRecursive()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isInInListRecursive  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _objToTest_| ) |  const  
---|---|---|---|---|---  
  
test if this object is in the InList and recursive further down

## ◆ isInOutList()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isInOutList  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _objToTest_| ) |  const  
---|---|---|---|---|---  
  
test if this object is directly (non recursive) in the OutList

## ◆ isInOutListRecursive()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isInOutListRecursive  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _objToTest_| ) |  const  
---|---|---|---|---|---  
  
test if the given object is in the OutList and recursive further down

## ◆ isRecomputing()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isRecomputing  | ( | | ) |  const  
---|---|---|---|---  
  
returns true if this objects is currently recomputing

Referenced by
[Fem::Constraint::onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[Part::Feature::onChanged()](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
and
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710).

## ◆ isRemoving()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isRemoving  | ( | | ) |  const  
---|---|---|---|---  
  
returns true if this objects is currently removed from the document

Referenced by
[App::OriginGroupExtension::onExtendedUnsetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27),
[TechDrawGui::ViewProviderDrawingView::onGuiRepaint()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a5b4c6e2fd917962e77d9f9dcb8432405),
and
[TechDrawGui::MDIViewPage::setTreeToSceneSelect()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a8c4e132accc95406f63a7e555cb1cbfc).

## ◆ isRestoring()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isRestoring  | ( | | ) |  const  
---|---|---|---|---  
  
returns true if this objects is currently restoring from file

Referenced by
[PartDesign::ShapeBinder::execute()](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a2886a69e9359a73fe242378c2a7b5a27),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[TechDraw::DrawViewPart::getSourceShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aeb0d7bbe7418b86053f38713d4c91fa9),
[TechDraw::DrawViewPart::getSourceShapeFused()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a259e1a941c8e6a0651089bfa4111e3bd),
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[Spreadsheet::PropertySheet::hasSetValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ade4669436aaa4ddc2130f8756ca08585),
[TechDraw::DrawRichAnno::mustExecute()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a0341116c3475965fc7cc3a586c8bd04f),
[TechDraw::DrawViewClip::mustExecute()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a27db71239b73197269ace8ca79e9dcb2),
[TechDraw::DrawViewSpreadsheet::mustExecute()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a0d02700cc490d94542c4508ccfc9757e),
[TechDraw::DrawGeomHatch::mustExecute()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a261eed9b0f2c16df4253f8e782cf6e22),
[TechDraw::DrawHatch::mustExecute()](../../d0/d97/classTechDraw_1_1DrawHatch.html#af5ab8197a7fd3f3e1656978578ddd30f),
[TechDraw::DrawLeaderLine::mustExecute()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#aa1f85707a4c5d5974a462a801a9199c5),
[TechDraw::DrawPage::mustExecute()](../../d9/d5a/classTechDraw_1_1DrawPage.html#af83c44feed62a393d9c5ea850bbaed6b),
[TechDraw::DrawProjGroup::mustExecute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaa53b26d779cb3e5913afb2637fcf86e),
[TechDraw::DrawProjGroupItem::mustExecute()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1bac249755bbc6f7881cd128158ae2a8),
[TechDraw::DrawView::mustExecute()](../../d6/d1c/classTechDraw_1_1DrawView.html#aecb782507679f383bfd5a8cb8ca285aa),
[TechDraw::DrawViewArch::mustExecute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#ac0b004990afa16dc78271e9c4cc24066),
[TechDraw::DrawViewBalloon::mustExecute()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed4962d1295f9c197a7abf5187884606),
[TechDraw::DrawViewDetail::mustExecute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#aab3cbf1f8a5acb302771e4a23d5914fe),
[TechDraw::DrawViewDimension::mustExecute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a0e048384fc02fd7ef9f4a79bcfeb247b),
[TechDraw::DrawViewDraft::mustExecute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#ad28b6173d701cf3d0b168cfb8505b68a),
[TechDraw::DrawViewImage::mustExecute()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a6ea5454abb51f0c48c8a790dbf5a86c9),
[TechDraw::DrawViewMulti::mustExecute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a883d222a6968a9cc812f483772dccf3d),
[TechDraw::DrawViewPart::mustExecute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#abd4f001ec919dbcad7113202c3cb9349),
[TechDraw::DrawViewSection::mustExecute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a654004aaa97316eb1174ee24199227b1),
[TechDraw::DrawViewSymbol::mustExecute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a9f50f90e3bb3f3304e78d31e32202088),
[Part::Circle::onChanged()](../../de/de4/classPart_1_1Circle.html#aac82db0865d1e2eb55342a84cf91872e),
[Part::Vertex::onChanged()](../../de/d96/classPart_1_1Vertex.html#a9421cb9911928eae246b23f3590bc3ee),
[Part::Line::onChanged()](../../d3/dfe/classPart_1_1Line.html#ab63d1eeff0a1ad1773c06cca1d731017),
[Part::Ellipse::onChanged()](../../d6/d22/classPart_1_1Ellipse.html#aebecb9c21eca867973512232a720cc63),
[Surface::GeomFillSurface::onChanged()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
[Sketcher::SketchObject::onChanged()](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[Drawing::FeatureViewSymbol::onChanged()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#aaf6475415e3e3e4e35ad6d1cd034f7fc),
[Part::Mirroring::onChanged()](../../dc/dac/classPart_1_1Mirroring.html#aa4148eb536fa6f15fb2fc21f3fe839b4),
[Part::Box::onChanged()](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[Part::Helix::onChanged()](../../df/d49/classPart_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[Part::Spiral::onChanged()](../../d2/d3f/classPart_1_1Spiral.html#a2f38f985d7c148ee3acec62a8358b4b7),
[Part::Wedge::onChanged()](../../d5/dc5/classPart_1_1Wedge.html#a609125d1bc02031accfc330fc2e79d08),
[PartDesign::Hole::onChanged()](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[TechDraw::DrawRichAnno::onChanged()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#aca7c4594d99963f20955aaaea06f9fbc),
[TechDraw::DrawSVGTemplate::onChanged()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#afa43ef4d1bf529675b75c5d31fff582b),
[TechDraw::DrawTile::onChanged()](../../da/d56/classTechDraw_1_1DrawTile.html#a0a7ecfbee9fbaf70d3d69acfd16c62e7),
[TechDraw::DrawTileWeld::onChanged()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawViewAnnotation::onChanged()](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a6566da76a48d680dc1cc90db63e0c60a),
[TechDraw::DrawViewDimExtent::onChanged()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a33e7b8c64f2983f2b81608bd1ebfc494),
[TechDraw::DrawWeldSymbol::onChanged()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad0b71b97ee45320fc8e8634e98b935cb),
[Part::Revolution::onChanged()](../../d3/d17/classPart_1_1Revolution.html#a9940a58886c8d7d0b4b009082d81f14c),
[Part::Primitive::onChanged()](../../d2/d31/classPart_1_1Primitive.html#ac5544f9b57ebf2a1b626450200a4bec0),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesign::SubShapeBinder::onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[TechDraw::DrawGeomHatch::onChanged()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch::onChanged()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewBalloon::onChanged()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed3817b8e495aca5729e5bed436cca6c),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension::onChanged()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewImage::onChanged()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a42774ac4ebd8f4fc4819cf4833e779aa),
[TechDraw::DrawViewMulti::onChanged()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#aa73d9e1a0934d049da29a63f2c5ddddd),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawViewSymbol::onChanged()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[TechDraw::LandmarkDimension::onChanged()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a9c8e7f17abdc4acecdc7e6670328f7a6),
[App::MeasureDistance::onChanged()](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
[TechDrawGui::ViewProviderDrawingView::onGuiRepaint()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a5b4c6e2fd917962e77d9f9dcb8432405),
[Spreadsheet::Cell::setContent()](../../d5/d22/classSpreadsheet_1_1Cell.html#a4d07e67e0412f933cb7306ee3e6b962c),
and
[Gui::ViewProviderLink::updateData()](../../d6/d59/classGui_1_1ViewProviderLink.html#a73f73f368cb176bf9a7f2371e4e9ec93).

## ◆ isTouched()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
test if this document object is touched

Referenced by
[App::OriginGroupExtension::extensionMustExecute()](../../da/d09/classApp_1_1OriginGroupExtension.html#ad2e1bce76ecdcd255084312b108a9bf5),
[Mesh::Curvature::mustExecute()](../../d2/d39/classMesh_1_1Curvature.html#a6af7b48ccba04340a5a6a2d1b683b86f),
[Mesh::SegmentByMesh::mustExecute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#ae266a9b9fa667055d01165b431ea99eb),
[Part::Prism::mustExecute()](../../dc/d69/classPart_1_1Prism.html#acbfb605c398b843511d88049827933f0),
[Part::RegularPolygon::mustExecute()](../../d2/d69/classPart_1_1RegularPolygon.html#ade525f0226ae5b2724a38c311afca7cc),
[TechDraw::DrawLeaderLine::mustExecute()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#aa1f85707a4c5d5974a462a801a9199c5),
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465),
and
[TechDrawGui::MDIViewPage::updateTemplate()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5dad0574c1df0a7c6398e90173300461).

## ◆ isValid()

[bool](../../d9/db9/classbool.html) App::DocumentObject::isValid  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[FemGui::TaskDlgFemConstraint::accept()](../../d8/d18/classFemGui_1_1TaskDlgFemConstraint.html#a61fcc7a973c20d15a3f3fd173de45115),
[FemGui::TaskDlgFemConstraintInitialTemperature::accept()](../../d9/d8a/classFemGui_1_1TaskDlgFemConstraintInitialTemperature.html#a417fa6e0a784395a4285594b00043771),
[PartGui::OffsetWidget::accept()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#a791a744197288c394c011dbb879a143c),
[PartGui::ThicknessWidget::accept()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#a56dbb59f2cea1ccb8c8b842997c35f48),
[PartDesignGui::TaskDlgFeatureParameters::accept()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#abfc2d8ecb714c2b558cc8feb07fa55c3),
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06),
[SurfaceGui::FillingPanel::accept()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#a310725e1fbda946f1edfb97d9fd46fbb),
[SurfaceGui::FillingEdgePanel::accept()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a8f8ff8037f61c7d70836740c12cf9e3f),
[SurfaceGui::GeomFillSurface::accept()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a21cfb55c39fdd9cbe947ef52714665dd),
[SurfaceGui::SectionsPanel::accept()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a08a26215cfddf89b23a47f3b37f8fbe5),
[SurfaceGui::GeomFillSurface::changeFillType()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#aa2180cd7b8c690d2addc40f808eefafc),
[Spreadsheet::Sheet::getCharsFromPrefs()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a144aba1b77f58bcd343d16c12d4df49c),
[App::Document::recomputeFeature()](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a),
[Fem::FemPostFilter::setActiveFilterPipeline()](../../d8/d6f/classFem_1_1FemPostFilter.html#af110fcc1443842b6a9deb74387975a6b),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ mustExecute()

| virtual short App::DocumentObject::mustExecute  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
mustExecute We call this method to check if the object was modified to be
invoked.

If the object label or an argument is modified. If we must recompute the
object - to call the method
[execute()](../../d2/de4/classApp_1_1DocumentObject.html#addd0e28aebe720807dd5c1f6790fe752
"get called by the document to recompute this feature Normally this method get
called in the processin..."). 0: no recomputation is needed 1: recomputation
needed

Remarks

    If an object is marked as 'touched' then this does not necessarily mean that it will be recomputed. It only means that all objects that link it (i.e. its InList) will be recomputed. 

Reimplemented in
[Inspection::Feature](../../d6/d23/classInspection_1_1Feature.html#a0d724ccdc0ab0a12d64857429f8ed6e5),
[Mesh::Curvature](../../d2/d39/classMesh_1_1Curvature.html#a6af7b48ccba04340a5a6a2d1b683b86f),
[Mesh::FixDefects](../../d4/d1f/classMesh_1_1FixDefects.html#a60719ab5d4ea4f23061a3cd88913f9c8),
[Mesh::Export](../../d6/d40/classMesh_1_1Export.html#af08e8f0650d1a809006084471fe51e10),
[Mesh::Import](../../d9/d29/classMesh_1_1Import.html#aa1fcc3c110cdd83510ccd3bb6fffe0d1),
[Mesh::SegmentByMesh](../../d0/ddf/classMesh_1_1SegmentByMesh.html#ae266a9b9fa667055d01165b431ea99eb),
[Mesh::SetOperations](../../d3/d8f/classMesh_1_1SetOperations.html#a4f5806f8ade3aad44cb8e973436418aa),
[Mesh::Sphere](../../d1/d57/classMesh_1_1Sphere.html#af382230622ae40b9001837c010914d55),
[Mesh::Ellipsoid](../../d2/dd6/classMesh_1_1Ellipsoid.html#a04b71856c085f1d22a52051fbfbdeab2),
[Mesh::Cylinder](../../df/def/classMesh_1_1Cylinder.html#a378eb9b322c47ba68f82b63a3ba8a774),
[Mesh::Cone](../../d4/dbc/classMesh_1_1Cone.html#a3e9ef98790cc1bb43811caad58800b6d),
[Mesh::Torus](../../de/da3/classMesh_1_1Torus.html#a9ba7a1c1f9c10906a6b2871015a245ed),
[Mesh::Cube](../../df/d68/classMesh_1_1Cube.html#a17e86f858cd8e0e152bed618bc89f8ab),
[Part::Compound](../../d7/d98/classPart_1_1Compound.html#a9aa9e6647f6cff757c27044a8761589b),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#a73f8f26306e463477a806f64f8dc6bc9),
[Part::Boolean](../../da/d3a/classPart_1_1Boolean.html#af3f085bc4a0685aa0b35b9ed302909ed),
[Part::Box](../../dc/d80/classPart_1_1Box.html#a9f9122055de9f9f54330344d6f0f4d2f),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#ae53749f4a3ec7d47c793836e8b434e39),
[Part::MultiCommon](../../d1/df7/classPart_1_1MultiCommon.html#aff038d0605f8d867e78b1f476d13a423),
[Part::CurveNet](../../d9/d41/classPart_1_1CurveNet.html#a14c067b4244e435b95caed0239061a67),
[Part::MultiFuse](../../df/dbc/classPart_1_1MultiFuse.html#a78d68db386d413d51ceee293c9c69f72),
[Part::ImportBrep](../../d8/d3e/classPart_1_1ImportBrep.html#ac9a27ad3e42210d02c9e37e13de11225),
[Part::ImportIges](../../d2/d1d/classPart_1_1ImportIges.html#a5e6c69a25c001e6fce1c225bb00946d8),
[Part::ImportStep](../../d4/de2/classPart_1_1ImportStep.html#a4a9b9f2ccd0f686db6f8b17913f497f2),
[Part::Polygon](../../d3/db3/classPart_1_1Polygon.html#a0dee3190c0e2a5daf90b8f2de9197fd6),
[Part::Section](../../d8/dea/classPart_1_1Section.html#a59b8614ab4d782e3a75c19f4eb7ac04c),
[Part::FilletBase](../../df/d7d/classPart_1_1FilletBase.html#a1605b11985fc17752b770a2d6345912c),
[Part::RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html#a58f9902136f476eb15446fc2ee5d8736),
[Part::Loft](../../d3/d52/classPart_1_1Loft.html#a4268e155f3ca5d5454ba26a201b46a8c),
[Part::Sweep](../../df/dc6/classPart_1_1Sweep.html#abad4b8648adea18b61116ac5bd589f16),
[Part::Thickness](../../db/d73/classPart_1_1Thickness.html#a5e19889c98eff816988ec695a3630027),
[Part::Vertex](../../de/d96/classPart_1_1Vertex.html#a070647e2216331349695e034b7953b11),
[Part::Line](../../d3/dfe/classPart_1_1Line.html#a52dc004fe03c7c0b2533a79e90582b76),
[Part::Plane](../../d0/d1c/classPart_1_1Plane.html#adeb8f292f17dd8ea85f6a10e4ff5a217),
[Part::Sphere](../../dc/d57/classPart_1_1Sphere.html#af382230622ae40b9001837c010914d55),
[Part::Ellipsoid](../../d4/dc8/classPart_1_1Ellipsoid.html#a04b71856c085f1d22a52051fbfbdeab2),
[Part::Cylinder](../../dd/d12/classPart_1_1Cylinder.html#a378eb9b322c47ba68f82b63a3ba8a774),
[Part::Prism](../../dc/d69/classPart_1_1Prism.html#acbfb605c398b843511d88049827933f0),
[Part::RegularPolygon](../../d2/d69/classPart_1_1RegularPolygon.html#ade525f0226ae5b2724a38c311afca7cc),
[Part::Cone](../../d2/d8f/classPart_1_1Cone.html#a3e9ef98790cc1bb43811caad58800b6d),
[Part::Torus](../../db/d42/classPart_1_1Torus.html#a9ba7a1c1f9c10906a6b2871015a245ed),
[Part::Helix](../../df/d49/classPart_1_1Helix.html#a8b11a6cb96966e4d2f78bc2aa6202e8b),
[Part::Spiral](../../d2/d3f/classPart_1_1Spiral.html#a9cba924aad8fd3e76ff441a3961226f8),
[Part::Wedge](../../d5/dc5/classPart_1_1Wedge.html#a9ecc8acaa8cad5f383598c95e8f81b9f),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#aadc4a277ba0371628877326ccb173656),
[PartDesign::Feature](../../d7/d51/classPartDesign_1_1Feature.html#a0f9eff61e64c94469fa96cdba046c4bd),
[PartDesign::Draft](../../df/d0e/classPartDesign_1_1Draft.html#a2ebb73aa30040bde4ca5c01b47301be3),
[PartDesign::DressUp](../../df/de5/classPartDesign_1_1DressUp.html#aa08c6bf93ff049780947659881837c69),
[PartDesign::FeatureExtrude](../../da/d12/classPartDesign_1_1FeatureExtrude.html#a7416081060d0046a4ee5f75b6cf96745),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#a5b3a59c8e278d4f36512e98f3c29c5e3),
[PartDesign::Groove](../../d7/de3/classPartDesign_1_1Groove.html#af2c45ee71298e5f2243c8ea28f2d5f06),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#a8b11a6cb96966e4d2f78bc2aa6202e8b),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#aabba1b579d01ed80e02dd3cbe96e268f),
[PartDesign::LinearPattern](../../d2/d86/classPartDesign_1_1LinearPattern.html#af148fe0fbc866c4e875f348ee00ac15b),
[PartDesign::Loft](../../d0/deb/classPartDesign_1_1Loft.html#a4268e155f3ca5d5454ba26a201b46a8c),
[PartDesign::Mirrored](../../d6/d91/classPartDesign_1_1Mirrored.html#ad52caeb5b8f56f79ff493ad0e055fc4c),
[PartDesign::MultiTransform](../../d2/df8/classPartDesign_1_1MultiTransform.html#a6ac7f7f11d9b701e73a719ba2ca8c273),
[PartDesign::Pipe](../../da/d61/classPartDesign_1_1Pipe.html#a1be7d941c0a219aac9b3e1f6bce37725),
[PartDesign::PolarPattern](../../da/d5b/classPartDesign_1_1PolarPattern.html#a5ec374b41f2ef38848bc86424ff95740),
[PartDesign::Box](../../df/d97/classPartDesign_1_1Box.html#ad4c0259f9361582e56b130542f075c94),
[PartDesign::Cylinder](../../dc/d28/classPartDesign_1_1Cylinder.html#a34b2d2eaaa139e81d104668a55b528df),
[PartDesign::Sphere](../../db/d9d/classPartDesign_1_1Sphere.html#a7af784560b0e4a7f02feffe2b50e9a20),
[PartDesign::Cone](../../d4/d2b/classPartDesign_1_1Cone.html#aaf85a9e73ac84c02c4ae965bf301794b),
[PartDesign::Ellipsoid](../../d4/de1/classPartDesign_1_1Ellipsoid.html#ab9deacc288cf4f1294f063d5fabfaf95),
[PartDesign::Torus](../../dd/de1/classPartDesign_1_1Torus.html#a9c940d8c26ff13297f4d8352a547fde5),
[PartDesign::Prism](../../d9/daf/classPartDesign_1_1Prism.html#a22492cb9418358d702012f95e64c5381),
[PartDesign::Wedge](../../dc/dd3/classPartDesign_1_1Wedge.html#a18c1e204e8024c403d34e3b075a04ed9),
[PartDesign::Revolution](../../d2/de6/classPartDesign_1_1Revolution.html#a3a2eebb70794151bf41bbfdfd374eae6),
[PartDesign::Scaled](../../db/dce/classPartDesign_1_1Scaled.html#aa2be088b02bd721f4b4d4b598950958a),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a4b3aef4d73c5e46762d8425eacf4594f),
[PartDesign::Thickness](../../d4/d22/classPartDesign_1_1Thickness.html#a5e19889c98eff816988ec695a3630027),
[PartDesign::Transformed](../../dd/de1/classPartDesign_1_1Transformed.html#aca66717047b204e50ad27e3929aea1cb),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a0d724ccdc0ab0a12d64857429f8ed6e5),
[Raytracing::LuxFeature](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a3f50e58889e6b8f6038ac7cd53264696),
[Raytracing::LuxProject](../../d5/de6/classRaytracing_1_1LuxProject.html#a748457d7f93d46b6fa8fb16386969d9f),
[Raytracing::RayFeature](../../d4/df2/classRaytracing_1_1RayFeature.html#a1f423b19b1164c9526bc19db42232bcb),
[Raytracing::RayProject](../../d2/d89/classRaytracing_1_1RayProject.html#af0f006304c9fe6e872879522904f0a4c),
[Sketcher::SketchObjectSF](../../de/da4/classSketcher_1_1SketchObjectSF.html#ae6f07ad80580bdc95ba0bf4b2719b3c6),
[Surface::Cut](../../d4/d17/classSurface_1_1Cut.html#a55fae0653fcb2808913a690f838f6842),
[Surface::Filling](../../d8/df7/classSurface_1_1Filling.html#aa4e2a1f2b2ecdfcbd01ac7a1be5eb36b),
[Surface::GeomFillSurface](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a6b2b02a9d8eaa29985780aa19cdd8d5e),
[Surface::Sewing](../../d2/d52/classSurface_1_1Sewing.html#a4f9f2fc30c894b4b2a23978b2bee7456),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#af2a22b7489ff1ed49acb9d0aa5f092e7),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a0341116c3475965fc7cc3a586c8bd04f),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a9b9fc4ebbbe32a111f0799f9fb9777da),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aa7dda17035d2e04d2c267c176db6bf46),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a2e30451cb7cf91ce2b04053a38e53fdd),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a3e7cdb271cc9d6216092c172446d4a4f),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a27db71239b73197269ace8ca79e9dcb2),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a3ff9756e1b5b8cb29c5b0f775a8d8c01),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a17de3a00134150ee4aa3a72b6a9b2d1c),
[TechDraw::DrawViewSpreadsheet](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a0d02700cc490d94542c4508ccfc9757e),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#afe50cb72bee8e16f9135f44af7d6c970),
[Part::Extrusion](../../db/d6c/classPart_1_1Extrusion.html#a228b96c5264e131bf450cc5bf8674fe1),
[Part::Face](../../dc/dbf/classPart_1_1Face.html#ae50cc97eb56db33e2878a41283101cc7),
[Part::Offset](../../d0/dda/classPart_1_1Offset.html#a0d2e23d767643dc89b30cce4c84a1132),
[Part::Offset2D](../../d7/dcf/classPart_1_1Offset2D.html#aff31be8bdeac470626e5208a65edc610),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a2e361e3b8f4ad563de04c16977530c80),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#a345765b0793de0d4e50cf44c1357a07b),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#a4d5a71d5b78479da43d7b0eee06e240f),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a7b11bf3c246fb3c0feb327b4cc2eb259),
[PartDesign::FeatureAddSub](../../d0/dd5/classPartDesign_1_1FeatureAddSub.html#a9d10deea7eb3a39ef2064c07ce89a74b),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#acc9ed4028be42a906bc3c46697efe969),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a3f61714b5aa58b68ccb2ac3f0fed02c9),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#ad0e97ac78dbd3665e8a8ce21d2b45a2e),
[Surface::Extend](../../d1/d22/classSurface_1_1Extend.html#a157b5d79910ff33715ba9bca92a5fde4),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a261eed9b0f2c16df4253f8e782cf6e22),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#af5ab8197a7fd3f3e1656978578ddd30f),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#aa1f85707a4c5d5974a462a801a9199c5),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#af83c44feed62a393d9c5ea850bbaed6b),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaa53b26d779cb3e5913afb2637fcf86e),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1bac249755bbc6f7881cd128158ae2a8),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#aecb782507679f383bfd5a8cb8ca285aa),
[TechDraw::DrawViewArch](../../df/dc6/classTechDraw_1_1DrawViewArch.html#ac0b004990afa16dc78271e9c4cc24066),
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed4962d1295f9c197a7abf5187884606),
[TechDraw::DrawViewDetail](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#aab3cbf1f8a5acb302771e4a23d5914fe),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a0e048384fc02fd7ef9f4a79bcfeb247b),
[TechDraw::DrawViewDraft](../../df/d84/classTechDraw_1_1DrawViewDraft.html#ad28b6173d701cf3d0b168cfb8505b68a),
[TechDraw::DrawViewImage](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a6ea5454abb51f0c48c8a790dbf5a86c9),
[TechDraw::DrawViewMulti](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a883d222a6968a9cc812f483772dccf3d),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#abd4f001ec919dbcad7113202c3cb9349),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a654004aaa97316eb1174ee24199227b1),
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a9f50f90e3bb3f3304e78d31e32202088),
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a2c3b899415fe85cd4c0962a4e1f1a34a),
[App::FeatureTest](../../df/dea/classApp_1_1FeatureTest.html#a3252f29ad06a99d4e9f44475b2f737f3),
[App::InventorObject](../../da/d11/classApp_1_1InventorObject.html#aa93fbad386eeaa32e5cc5000774f24bd),
[App::Origin](../../d9/d8b/classApp_1_1Origin.html#a01df202f898e80abb2fcca9c95f75d10),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a73b930f29d9fd108ebdebffaced9dd9c),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#a9d6d243d041986720fe0d20fb224fec0),
[Fem::FemPostClipFilter](../../dc/d06/classFem_1_1FemPostClipFilter.html#ad9b5a128c02d29ef5fdcc762716240ac),
[Fem::FemPostDataAlongLineFilter](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#af836732e27e998bcfc2791ecf7b78e6b),
[Fem::FemPostDataAtPointFilter](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a129b8b6e1e1e568884df55b28887cfa3),
[Fem::FemPostScalarClipFilter](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#ae46d689646a2b308e078cbeac3d32f4f),
[Fem::FemPostWarpVectorFilter](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a2845626ff54c894fcdfc595e3b877cf0),
[Fem::FemPostCutFilter](../../da/d89/classFem_1_1FemPostCutFilter.html#a8878962978592c040f1f90e389b4b6d0),
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a078fd5b14f636a2d1eb723edd86bc761),
[Fem::FemResultObject](../../d3/d81/classFem_1_1FemResultObject.html#aa851e1f775a4a57eaf9d37b28fd0dc2d),
[Fem::FemSetElementsObject](../../df/d49/classFem_1_1FemSetElementsObject.html#a74c3c234c2f5b11cca6449d5bcf59a57),
[Fem::FemSetFacesObject](../../df/d72/classFem_1_1FemSetFacesObject.html#a719add6e80292c3846f72d4ddf13e68b),
[Fem::FemSetGeometryObject](../../df/d59/classFem_1_1FemSetGeometryObject.html#a84422beaf7c5e03b269e6688a81f70ce),
[Fem::FemSetNodesObject](../../dc/d59/classFem_1_1FemSetNodesObject.html#a0f10e5593da3237f007688c541a7fd54),
[Fem::FemSetObject](../../d8/dbe/classFem_1_1FemSetObject.html#abc3bc7970811cbc3a0664de4ff4e5d37),
[Fem::FemSolverObject](../../d1/dd0/classFem_1_1FemSolverObject.html#a60a68417774ac74253c3db4e31a63c31),
[Part::CustomFeature](../../da/d46/classPart_1_1CustomFeature.html#a58d1423bbb29242377e3493fd30c9f04),
[Part::FeatureReference](../../d2/da1/classPart_1_1FeatureReference.html#a56897f6c6e4773ab3d2d2095a51fe0ea),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#adb39ba7172cf948740e55f8d00daeb96),
[Path::FeatureArea](../../da/d1e/classPath_1_1FeatureArea.html#a8a8d2ce2448e55746f37e77c283361bd),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#a0d330196316566d337df0cd3b3eaaac2),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a8cb25af4880561dd57b3bbfbe5ca0657),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#a05eaffc667a9956fc5270bdb78bc0715),
[Sandbox::SandboxObject](../../da/dd9/classSandbox_1_1SandboxObject.html#a020585a3fecab3300bfcc90d7a396db8),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a8ee2b249acb7d27d24a35e5e4d40d350),
and
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#ad87d2c4e8ff00afa0730be5b3c7dae94).

Referenced by
[Gui::DocumentObjectItem::displayStatusInfo()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a235f26b8fbf37e4e4efccdae9cbbada0),
[Mesh::Sphere::mustExecute()](../../d1/d57/classMesh_1_1Sphere.html#af382230622ae40b9001837c010914d55),
[Mesh::Ellipsoid::mustExecute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#a04b71856c085f1d22a52051fbfbdeab2),
[Mesh::Cylinder::mustExecute()](../../df/def/classMesh_1_1Cylinder.html#a378eb9b322c47ba68f82b63a3ba8a774),
[Mesh::Cone::mustExecute()](../../d4/dbc/classMesh_1_1Cone.html#a3e9ef98790cc1bb43811caad58800b6d),
[Mesh::Torus::mustExecute()](../../de/da3/classMesh_1_1Torus.html#a9ba7a1c1f9c10906a6b2871015a245ed),
[Mesh::Cube::mustExecute()](../../df/d68/classMesh_1_1Cube.html#a17e86f858cd8e0e152bed618bc89f8ab),
[Raytracing::LuxFeature::mustExecute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a3f50e58889e6b8f6038ac7cd53264696),
[Raytracing::RayFeature::mustExecute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a1f423b19b1164c9526bc19db42232bcb),
[TechDraw::DrawParametricTemplate::mustExecute()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#af2a22b7489ff1ed49acb9d0aa5f092e7),
[TechDraw::DrawTemplate::mustExecute()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aa7dda17035d2e04d2c267c176db6bf46),
[TechDraw::DrawGeomHatch::mustExecute()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a261eed9b0f2c16df4253f8e782cf6e22),
[TechDraw::DrawHatch::mustExecute()](../../d0/d97/classTechDraw_1_1DrawHatch.html#af5ab8197a7fd3f3e1656978578ddd30f),
[TechDraw::DrawPage::mustExecute()](../../d9/d5a/classTechDraw_1_1DrawPage.html#af83c44feed62a393d9c5ea850bbaed6b),
[TechDraw::DrawView::mustExecute()](../../d6/d1c/classTechDraw_1_1DrawView.html#aecb782507679f383bfd5a8cb8ca285aa),
[TechDraw::DrawViewImage::mustExecute()](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a6ea5454abb51f0c48c8a790dbf5a86c9),
[App::FeatureTest::mustExecute()](../../df/dea/classApp_1_1FeatureTest.html#a3252f29ad06a99d4e9f44475b2f737f3),
[App::Origin::mustExecute()](../../d9/d8b/classApp_1_1Origin.html#a01df202f898e80abb2fcca9c95f75d10),
[Fem::FemPostClipFilter::mustExecute()](../../dc/d06/classFem_1_1FemPostClipFilter.html#ad9b5a128c02d29ef5fdcc762716240ac),
[Fem::FemPostDataAlongLineFilter::mustExecute()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#af836732e27e998bcfc2791ecf7b78e6b),
[Fem::FemPostDataAtPointFilter::mustExecute()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a129b8b6e1e1e568884df55b28887cfa3),
[Fem::FemPostScalarClipFilter::mustExecute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#ae46d689646a2b308e078cbeac3d32f4f),
[Fem::FemPostWarpVectorFilter::mustExecute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a2845626ff54c894fcdfc595e3b877cf0),
[Fem::FemPostCutFilter::mustExecute()](../../da/d89/classFem_1_1FemPostCutFilter.html#a8878962978592c040f1f90e389b4b6d0),
[Fem::FemPostPipeline::mustExecute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a078fd5b14f636a2d1eb723edd86bc761),
[Path::Feature::mustExecute()](../../d5/dd9/classPath_1_1Feature.html#a0d330196316566d337df0cd3b3eaaac2),
and
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465).

## ◆ mustRecompute()

[bool](../../d9/db9/classbool.html) App::DocumentObject::mustRecompute  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Test if this document object must be recomputed.

## ◆ onBeforeChange()

| virtual void App::DocumentObject::onBeforeChange  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
get called before the value is changed

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057).

Reimplemented in
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a7c55c251b8fe8c83f98a5e0defb88070),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#a3bfb2f868776a6dddcc69f83842e8f44),
and
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac9e00650dfe413e2c360aeb310020556).

Referenced by
[Drawing::FeaturePage::onBeforeChange()](../../db/d0f/classDrawing_1_1FeaturePage.html#a7c55c251b8fe8c83f98a5e0defb88070),
[Part::BodyBase::onBeforeChange()](../../da/dc8/classPart_1_1BodyBase.html#a3bfb2f868776a6dddcc69f83842e8f44),
[TechDraw::DrawPage::onBeforeChange()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ac9e00650dfe413e2c360aeb310020556),
and
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onBeforeChangeLabel()

| virtual void App::DocumentObject::onBeforeChangeLabel  | ( | std::string & | _newLabel_| ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ onChanged()

| virtual void App::DocumentObject::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
get called by the container when a property was changed

Reimplemented from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d).

Reimplemented in
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#aac82db0865d1e2eb55342a84cf91872e),
[Part::Vertex](../../de/d96/classPart_1_1Vertex.html#a9421cb9911928eae246b23f3590bc3ee),
[Part::Line](../../d3/dfe/classPart_1_1Line.html#ab63d1eeff0a1ad1773c06cca1d731017),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#aebecb9c21eca867973512232a720cc63),
[Surface::GeomFillSurface](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a778fc5826d5950fba6fb6e5a2d2208dd),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[Drawing::FeatureClip](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2f703cc6f8d0f4d9e953a80ec936b8f0),
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[Drawing::FeatureViewSymbol](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#aaf6475415e3e3e4e35ad6d1cd034f7fc),
[Fem::Constraint](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[Fem::ConstraintBearing](../../df/d0a/classFem_1_1ConstraintBearing.html#ae81d9fda05994bd43bf81faf3acae5d6),
[Fem::ConstraintContact](../../db/d7c/classFem_1_1ConstraintContact.html#a2470d9364e84ea3c15f5873073f26539),
[Fem::ConstraintDisplacement](../../d5/d1c/classFem_1_1ConstraintDisplacement.html#a8525892f2c7183b75c1d8f2052f82401),
[Fem::ConstraintFixed](../../d1/d43/classFem_1_1ConstraintFixed.html#a2b9b87e9151f1571ab9cff619ec5547c),
[Fem::ConstraintFluidBoundary](../../d6/dbc/classFem_1_1ConstraintFluidBoundary.html#acee1bd2b1d9f5b712253eaf827c00110),
[Fem::ConstraintForce](../../d6/d63/classFem_1_1ConstraintForce.html#aa19098735f62c480439948314f6532b3),
[Fem::ConstraintGear](../../d8/d55/classFem_1_1ConstraintGear.html#a971506b4ca246c3378e2755160ed4772),
[Fem::ConstraintHeatflux](../../de/dce/classFem_1_1ConstraintHeatflux.html#a0caeab069cf3e2fc8246aa163735d1e9),
[Fem::ConstraintInitialTemperature](../../da/d91/classFem_1_1ConstraintInitialTemperature.html#aa21e4c9c6cc31312e5147bbe1f8fcf05),
[Fem::ConstraintPlaneRotation](../../d7/d08/classFem_1_1ConstraintPlaneRotation.html#a668aafd16c5cf0565dde1072dd55a34a),
[Fem::ConstraintPressure](../../dd/d5e/classFem_1_1ConstraintPressure.html#a05ca046143c094c241c12702f7b820f7),
[Fem::ConstraintPulley](../../d3/dec/classFem_1_1ConstraintPulley.html#a6c23af9b8ba29b03f25163da9b75a41f),
[Fem::ConstraintSpring](../../dc/d42/classFem_1_1ConstraintSpring.html#ae67112c14de2dc75f749842b6591fcf8),
[Fem::ConstraintTemperature](../../d7/dff/classFem_1_1ConstraintTemperature.html#a74f2f9e94a2d9011490c09caab3c0da9),
[Fem::ConstraintTransform](../../d8/d3c/classFem_1_1ConstraintTransform.html#a38b893dee34272ad6bf0c6126aad561f),
[Fem::FemMeshObject](../../d5/d68/classFem_1_1FemMeshObject.html#aeea4f2e58af23fcd160a31ccea76cc6e),
[Fem::FemPostClipFilter](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostDataAlongLineFilter](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[Fem::FemPostDataAtPointFilter](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ae4bb2f96ee214db7c2bcb5a0afe0fdc4),
[Fem::FemPostScalarClipFilter](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[Fem::FemPostCutFilter](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[Fem::FemPostFunctionProvider](../../dd/d47/classFem_1_1FemPostFunctionProvider.html#a5d57b8e7aadfb627843050d88d933911),
[Fem::FemPostPlaneFunction](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#ab73b39b74f480820feda8b3f5bcad117),
[Fem::FemPostSphereFunction](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[Fem::FemPostPipeline](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#aa4148eb536fa6f15fb2fc21f3fe839b4),
[Part::Box](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[Part::RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html#a143afeec2aafb3207cd29e9ef6fc5934),
[Part::Loft](../../d3/d52/classPart_1_1Loft.html#acc65fe857c50b113cb06e0d092c83fd5),
[Part::Sweep](../../df/dc6/classPart_1_1Sweep.html#a67f346ffecb66556a70c38c9184cdd56),
[Part::Helix](../../df/d49/classPart_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[Part::Spiral](../../d2/d3f/classPart_1_1Spiral.html#a2f38f985d7c148ee3acec62a8358b4b7),
[Part::Wedge](../../d5/dc5/classPart_1_1Wedge.html#a609125d1bc02031accfc330fc2e79d08),
[PartDesign::Line](../../d0/d2a/classPartDesign_1_1Line.html#a9da12fed7c1a5cfa4af5c06af23c6fff),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#a82dfdf47875b49263a5275ab1ff3c686),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a628a37fc8716ca08f0c67bb727ac3b76),
[PartDesign::DressUp](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a36fd19fd597799ebeccd8eddd104bdf4),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Robot::Edge2TracObject](../../d8/df5/classRobot_1_1Edge2TracObject.html#a3e8b60d7dcc4abe17a0e640a0e0ef5e9),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Robot::TrajectoryDressUpObject](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a58ad4466b7239a951a9b9b4d30b7f1d3),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#aded21cc1ebf027aa6b39e81759687ea3),
[Sandbox::SandboxObject](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a50d56147d2f6d3cf3329413baef6e66d),
[TechDraw::DrawParametricTemplate](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a98d6a8c0896aca4d3fa549700b8a4eb6),
[TechDraw::DrawRichAnno](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#aca7c4594d99963f20955aaaea06f9fbc),
[TechDraw::DrawSVGTemplate](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#afa43ef4d1bf529675b75c5d31fff582b),
[TechDraw::DrawTemplate](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a6d7ffefeb992220357cf4dab59576919),
[TechDraw::DrawTile](../../da/d56/classTechDraw_1_1DrawTile.html#a0a7ecfbee9fbaf70d3d69acfd16c62e7),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a4241390f45c70002f410b5c78a4d0452),
[TechDraw::DrawViewAnnotation](../../d5/d65/classTechDraw_1_1DrawViewAnnotation.html#a6566da76a48d680dc1cc90db63e0c60a),
[TechDraw::DrawViewClip](../../dd/de8/classTechDraw_1_1DrawViewClip.html#afb0fdb6bcca35df389d3cd1632191706),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a5897d64ff7b47d70c7f4bddce6ac17ce),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a33e7b8c64f2983f2b81608bd1ebfc494),
[TechDraw::DrawViewSpreadsheet](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#ab3c3a1352fddadb8dea1ef9ec40acd91),
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad0b71b97ee45320fc8e8634e98b935cb),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#aad727053c5bb43ee6f065f3d0b458f16),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a9940a58886c8d7d0b4b009082d81f14c),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ac5544f9b57ebf2a1b626450200a4bec0),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesign::Point](../../da/d0d/classPartDesign_1_1Point.html#a559cef769b27bcf8efeef552583f9aa4),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#a41c675a8b7f2f6e73b95946b99245f12),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a86c00f82005801a22585584fb378e4e5),
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a984513ae894c80494f6a0c3b0725f48f),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[Surface::Extend](../../d1/d22/classSurface_1_1Extend.html#ac33fb0ebd31edae770d009cc24c58df9),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawLeaderLine](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a289014293fbb3c42b8c46416e261530a),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawProjGroup](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aea5cc872256320be7112396d84b3fee5),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewBalloon](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#aed3817b8e495aca5729e5bed436cca6c),
[TechDraw::DrawViewDetail](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a2f650d374435ed4a7ee16ed101674296),
[TechDraw::DrawViewImage](../../d0/d87/classTechDraw_1_1DrawViewImage.html#a42774ac4ebd8f4fc4819cf4833e779aa),
[TechDraw::DrawViewMulti](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#aa73d9e1a0934d049da29a63f2c5ddddd),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6a340bbf67a96de757e412b21d7a5491),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[TechDraw::DrawViewSymbol](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#adb3364984aac5da2ff804a43845ceee4),
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a9c8e7f17abdc4acecdc7e6670328f7a6),
[App::MeasureDistance](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
and
[App::TextDocument](../../d9/de9/classApp_1_1TextDocument.html#affdf6c8a48df5cea53213040c487e5f8).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[App::VRMLObject::onChanged()](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[Drawing::FeatureClip::onChanged()](../../d5/d4a/classDrawing_1_1FeatureClip.html#a2f703cc6f8d0f4d9e953a80ec936b8f0),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[Drawing::FeatureViewSymbol::onChanged()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#aaf6475415e3e3e4e35ad6d1cd034f7fc),
[Fem::Constraint::onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[Fem::FemMeshObject::onChanged()](../../d5/d68/classFem_1_1FemMeshObject.html#aeea4f2e58af23fcd160a31ccea76cc6e),
[Fem::FemPostClipFilter::onChanged()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a696285744236a6bf6e8c14f735034705),
[Fem::FemPostDataAlongLineFilter::onChanged()](../../da/d26/classFem_1_1FemPostDataAlongLineFilter.html#ae418afcb8e18abba84d16c2a645a434e),
[Fem::FemPostDataAtPointFilter::onChanged()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ae4bb2f96ee214db7c2bcb5a0afe0fdc4),
[Fem::FemPostScalarClipFilter::onChanged()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a6c5243b230b4dac2cde71f28d04dcd53),
[Fem::FemPostWarpVectorFilter::onChanged()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#a64c913cbc86feb708504b94b931f1085),
[Fem::FemPostCutFilter::onChanged()](../../da/d89/classFem_1_1FemPostCutFilter.html#a682758b8e3c1c8cf8b272d2244321913),
[Fem::FemPostFunctionProvider::onChanged()](../../dd/d47/classFem_1_1FemPostFunctionProvider.html#a5d57b8e7aadfb627843050d88d933911),
[Fem::FemPostPlaneFunction::onChanged()](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#ab73b39b74f480820feda8b3f5bcad117),
[Fem::FemPostSphereFunction::onChanged()](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[Fem::FemPostPipeline::onChanged()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a333b47057bc9b7691cc0c9db9b0c79ba),
[Path::Feature::onChanged()](../../d5/dd9/classPath_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[Robot::Edge2TracObject::onChanged()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a3e8b60d7dcc4abe17a0e640a0e0ef5e9),
[Robot::RobotObject::onChanged()](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Robot::TrajectoryDressUpObject::onChanged()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a58ad4466b7239a951a9b9b4d30b7f1d3),
[Robot::TrajectoryObject::onChanged()](../../d7/db5/classRobot_1_1TrajectoryObject.html#aded21cc1ebf027aa6b39e81759687ea3),
[Sandbox::SandboxObject::onChanged()](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[Spreadsheet::Sheet::onChanged()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a50d56147d2f6d3cf3329413baef6e66d),
[TechDraw::DrawParametricTemplate::onChanged()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a98d6a8c0896aca4d3fa549700b8a4eb6),
[TechDraw::DrawTemplate::onChanged()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#a6d7ffefeb992220357cf4dab59576919),
[PartDesign::Point::onChanged()](../../da/d0d/classPartDesign_1_1Point.html#a559cef769b27bcf8efeef552583f9aa4),
[TechDraw::DrawGeomHatch::onChanged()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a9942ef5dd5ecef6dba83a1245a0840ca),
[TechDraw::DrawHatch::onChanged()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a655588bfe5d6ff663e4aefc40c118a58),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[App::MeasureDistance::onChanged()](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
[App::TextDocument::onChanged()](../../d9/de9/classApp_1_1TextDocument.html#affdf6c8a48df5cea53213040c487e5f8),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDocumentRestored()

| virtual void App::DocumentObject::onDocumentRestored  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
get called after a document has been fully restored

Reimplemented in
[Drawing::FeaturePage](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Fem::Constraint](../../d0/d11/classFem_1_1Constraint.html#abfe82aef4be1b70b5f33c93b6ba6da33),
[Fem::FemPostPlaneFunction](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#a0073f416d7cb5a2ce3f3a97d9459f1c8),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a88645629a13677f1034ae2023481c2a1),
[Raytracing::LuxProject](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a6442efcbd90e9a8099539a0e43afec68),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a7a4b1b5d8aac6cdb9a3a16997934c000),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a2c6590d47665c960d69c0e7cf287a4be),
[App::Link](../../df/d9b/classApp_1_1Link.html#a800f7ee69e840bf2914b8d0d6d66bce7),
[App::LinkElement](../../d0/d3e/classApp_1_1LinkElement.html#a31078c0a92bd606998f4f1fb754d7ac3),
[App::LinkGroup](../../de/d15/classApp_1_1LinkGroup.html#a3fd7a4419ef20f719bdff1ea162613c8),
[Part::Datum](../../db/d0b/classPart_1_1Datum.html#aee993e2bbdc3cc6997f293b29bdad4b3),
[Part::Compound2](../../d5/dab/classPart_1_1Compound2.html#ac69720b1ba091dcdfac8b07ffbbf6048),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[PartDesign::Point](../../da/d0d/classPartDesign_1_1Point.html#aa5d45ccfd155f9a1761994c5eca092f6),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ac7f22f3e6072c5072f234496e8dfbe62),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a8b3b30c7b518da737c30c6c779b91b50),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a236c7efbf2e991277bd53a914eb247bb),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a3437412caff103d7c68842db2e694a7b),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#a2b4ab549d2874893f4d9f58e6b1e0757),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#ad9102272119caa28ba247eda173dda3d),
[TechDraw::DrawView](../../d6/d1c/classTechDraw_1_1DrawView.html#a58316a6a9c6ed2971c132af9751171da),
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a899ec15c087cd8a0c38e05fda6f4a647),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a4e1308cb2966a8d954d4adc0fd21cd91),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a639636de121b31e8f97a010b214fb71e),
and
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a849ea840f2577855fc6365b0481bd8cc).

Referenced by
[Fem::Constraint::onDocumentRestored()](../../d0/d11/classFem_1_1Constraint.html#abfe82aef4be1b70b5f33c93b6ba6da33),
[TechDraw::DrawTileWeld::onDocumentRestored()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a7a4b1b5d8aac6cdb9a3a16997934c000),
[Part::Datum::onDocumentRestored()](../../db/d0b/classPart_1_1Datum.html#aee993e2bbdc3cc6997f293b29bdad4b3),
[PartDesign::SubShapeBinder::onDocumentRestored()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ac7f22f3e6072c5072f234496e8dfbe62),
[Sketcher::SketchObject::onDocumentRestored()](../../d9/dad/classSketcher_1_1SketchObject.html#a8b3b30c7b518da737c30c6c779b91b50),
[TechDraw::DrawGeomHatch::onDocumentRestored()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a236c7efbf2e991277bd53a914eb247bb),
[TechDraw::DrawHatch::onDocumentRestored()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a3437412caff103d7c68842db2e694a7b),
and
[TechDraw::DrawPage::onDocumentRestored()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a2b4ab549d2874893f4d9f58e6b1e0757).

## ◆ onLostLinkToObject()

| virtual void App::DocumentObject::onLostLinkToObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | | ) |   
---|---|---|---|---|---  
virtual  
  
Called in case of losing a link Get called by the document when a object got
deleted a link property of this object ist pointing to.

The standard behaviour of the
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") implementation is to reset the links to
nothing. You may override this method to implement additional or different
behavior.

## ◆ onPropertyStatusChanged()

| virtual void App::DocumentObject::onPropertyStatusChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _prop_ ,   
---|---|---|---  
|  | unsigned long  | _oldStatus_  
| ) | |   
overrideprotectedvirtual  
  
get called when a property status has changed

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a25dc796f1aecab39ceeed8335097b758).

## ◆ onSettingDocument()

| virtual void App::DocumentObject::onSettingDocument  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
get called after setting the document

Reimplemented in
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#a374171f408a48ac1a83dd012d6a34b14),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#aa551cbc8ad4811d267637daa1a8dee8e),
and
[TechDraw::DrawWeldSymbol](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aebf48eba403fab933cfaba6f325c6bc2).

Referenced by
[PartDesign::Body::onSettingDocument()](../../dd/db8/classPartDesign_1_1Body.html#aa551cbc8ad4811d267637daa1a8dee8e),
and
[TechDraw::DrawWeldSymbol::onSettingDocument()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aebf48eba403fab933cfaba6f325c6bc2).

## ◆ onUndoRedoFinished()

| virtual void App::DocumentObject::onUndoRedoFinished  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
get called after an undo/redo transaction is finished

Reimplemented in
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#ada1d20f584b972886a216efcffc68c14).

## ◆ onUpdateElementReference()

| virtual void App::DocumentObject::onUpdateElementReference  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |   
---|---|---|---|---|---  
virtual  
  
Referenced by
[App::PropertyExpressionEngine::updateElementReference()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362),
and
[Spreadsheet::PropertySheet::updateElementReference()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a35d58b0bf7eac198ffdae31e16f3173f).

## ◆ purgeError()

void App::DocumentObject::purgeError  | ( | void  | | ) |   
---|---|---|---|---|---  
  
remove the error from the object

## ◆ purgeTouched()

void App::DocumentObject::purgeTouched  | ( | void  | | ) |   
---|---|---|---|---|---  
  
reset this document object touched

Referenced by
[TechDrawGui::TaskBalloon::accept()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#ad0a46dd67ed055b9027669202671989d),
[TechDrawGui::TaskDimension::accept()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a9bf2aebd177a6bdc085a6f2dfc890bea),
[TechDraw::DrawProjGroupItem::autoPosition()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aed7c8d696a4a2b4f3a172ebc3789cbf7),
[PointsGui::ViewProviderScattered::cut()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#a6e93ecaa9bbca01c9cd9c294ba22f38c),
[PointsGui::ViewProviderStructured::cut()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#a808184849a3543a6d70c263099506c98),
[TechDraw::DrawView::execute()](../../d6/d1c/classTechDraw_1_1DrawView.html#a43e7256f0d0a0c60c90ed90e0e3db759),
[Mesh::Importer::load()](../../dc/d56/classMesh_1_1Importer.html#ac634b94b2bebfba4e4dd119df0560db6),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawProjGroup::onChanged()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#afe9cc0a3218a4c8037a9a6b67642d450),
[PartDesign::MultiTransform::positionBySupport()](../../d2/df8/classPartDesign_1_1MultiTransform.html#a3d4f1facdf2a2ca1233b9e6e09ec7710),
[TechDrawGui::TaskBalloon::reject()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a89f74323228065dc56b8c71aa6ab3ae3),
[TechDrawGui::TaskDimension::reject()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a9cd2604c7506ed218f1fed530520e8ff),
[MeshGui::ViewProviderMesh::removeFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#aef4f7c4dfe1a66027828a011eea2651f),
and
[MeshGui::ViewProviderMesh::trimMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a265b2a1e25e284315a52153b8b6c4d71).

## ◆ recompute()

| virtual [App::DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * App::DocumentObject::recompute  | ( | void  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
recompute only this object

Reimplemented in
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#af8e48855174f6654908ab62d5c2ae303),
and
[Drawing::FeatureView](../../db/d1f/classDrawing_1_1FeatureView.html#ae78f9935f1cc6e5380326e0045bac1d0).

Referenced by
[App::MeasureDistance::onChanged()](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
[Part::Feature::recompute()](../../d7/d7e/classPart_1_1Feature.html#af8e48855174f6654908ab62d5c2ae303),
[Drawing::FeatureView::recompute()](../../db/d1f/classDrawing_1_1FeatureView.html#ae78f9935f1cc6e5380326e0045bac1d0),
[draftguitools.gui_trackers.arcTracker::setApertureAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#ae8184e1cc740890318e7ff1f47d6e39c),
[draftguitools.gui_trackers.arcTracker::setEndAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#ab89eccea794aaac46af78d966fc93936),
[draftguitools.gui_trackers.arcTracker::setStartAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#a34fd35c94ca62926f6c3e741fabfd8df),
[draftguitools.gui_trackers.bsplineTracker::update()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a780d90044fb459aa47487afc9d7979c9),
and
[draftguitools.gui_trackers.bezcurveTracker::update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63).

## ◆ recomputeFeature()

[bool](../../d9/db9/classbool.html) App::DocumentObject::recomputeFeature  | ( | [bool](../../d9/db9/classbool.html) | _recursive_ = `false`| ) |   
---|---|---|---|---|---  
  
Recompute only this feature.

Parameters

     recursive| set to true to recompute any dependent objects as well   
---|---  
  
Referenced by
[FemGui::TaskDlgCreateNodeSet::accept()](../../d9/d8f/classFemGui_1_1TaskDlgCreateNodeSet.html#aae7b7afa431004b899003fe789f532bb),
[FemGui::TaskDlgMeshShapeNetgen::accept()](../../dc/db4/classFemGui_1_1TaskDlgMeshShapeNetgen.html#aa88c49eb6c4ad7cd760e8fcb2c3181be),
[RobotGui::TaskDlgEdge2Trac::accept()](../../d6/da9/classRobotGui_1_1TaskDlgEdge2Trac.html#a8fae3bae30ab8e9c0bcb0034113f72a1),
[RobotGui::TaskDlgTrajectoryDressUp::accept()](../../dd/d12/classRobotGui_1_1TaskDlgTrajectoryDressUp.html#ae33084b2042760869e0f31c901807ca7),
[SurfaceGui::FillingPanel::accept()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#a310725e1fbda946f1edfb97d9fd46fbb),
[SurfaceGui::FillingEdgePanel::accept()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a8f8ff8037f61c7d70836740c12cf9e3f),
[SurfaceGui::GeomFillSurface::accept()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a21cfb55c39fdd9cbe947ef52714665dd),
[SurfaceGui::SectionsPanel::accept()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a08a26215cfddf89b23a47f3b37f8fbe5),
[TechDrawGui::TaskActiveView::accept()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a17c1dd2c632f5624c7edc69cacd32a73),
[TechDrawGui::TaskCosVertex::accept()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#ac0c6878d9764252e09f41414b44d1dd8),
[TechDrawGui::TaskGeomHatch::accept()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a0bf5ab07f9ff3b95e6d3343b52b1111b),
[TechDrawGui::TaskProjGroup::accept()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a73028edf767f28a1bdb160db31d82c44),
[TechDrawGui::TaskWeldingSymbol::accept()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ad91ef56ef584a69a7b67e440066ebec8),
[TechDrawGui::TaskProjGroup::apply()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a1140087ba7b34ac60a38cace5b6e5ea3),
[TechDrawGui::TaskHatch::apply()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#ad0db5ee1db83dbec34eda3a85013b4fe),
[TechDrawGui::TaskSectionView::applyQuick()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a64b429688f97823f132a2d6e736ce05c),
[TechDrawGui::TaskProjGroup::AutoDistributeClicked()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#ae38b7ea40b031895834fbce113cd0943),
[SurfaceGui::GeomFillSurface::changeFillType()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#aa2180cd7b8c690d2addc40f808eefafc),
[RobotGui::TaskDlgTrajectoryDressUp::clicked()](../../dd/d12/classRobotGui_1_1TaskDlgTrajectoryDressUp.html#abb6a4401e0058980f244e13199be1ca9),
[TechDrawGui::TaskCenterLine::createCenterLine()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a9fb5dd30626ee43ec4671c9ea2ce150b),
[SurfaceGui::GeomFillSurface::flipOrientation()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#ab1c5852e31a51289830861fd70be5f58),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[TechDraw::DrawDimHelper::makeDistDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#abbb31fd885c91f55267b7f8fd3945c1a),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[TechDraw::DrawViewPart::onDocumentRestored()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a4e1308cb2966a8d954d4adc0fd21cd91),
[PartGui::SectionCut::onFlipXclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a5fbc3a06b93ca2cc623e4c60b2d8b0cd),
[PartGui::SectionCut::onFlipYclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a086343100aa8f33a1f885130b13fa4ad),
[PartGui::SectionCut::onFlipZclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a56a8cd5a5ec5c2228e4d5a5f8a8c232a),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::GeomFillSurface::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#acd70791d15b148166826bac85bc802e9),
[SurfaceGui::SectionsPanel::onSelectionChanged()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a919af91b2e734c27e20773a1f737a49c),
[TechDrawGui::TaskProjGroup::projectionTypeChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81ab26f8c5a6b8a0aed58753142f8d7b),
[PartDesignGui::ViewProviderTransformed::recomputeFeature()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a14cb4d7a2487ad732593fed6ece13ca6),
[TechDrawGui::TaskCenterLine::reject()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a68fb5c8b222e660313377b82d56a0f5a),
[TechDrawGui::TaskDetail::reject()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a824272a5ad9a720866d98e807fdf6cd8),
[TechDrawGui::TaskSectionView::reject()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a06ea99abf05dde7b774ecf00deabdeb7),
[TechDrawGui::TaskProjGroup::scaleManuallyChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a40ff243eaf44f2528b05976f21fd4f67),
[TechDrawGui::TaskProjGroup::spacingChanged()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a898e358b0ef66513b1b38788aa5374ec),
[FemGui::TaskPostDataAtPoint::TaskPostDataAtPoint()](../../d9/da7/classFemGui_1_1TaskPostDataAtPoint.html#a442bb680fc74fbe236c0415717eb94a4),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
[TechDraw::DrawPage::updateAllViews()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a9e5d21f7a91e35e5981363a597a89717),
[TechDrawGui::TaskDetail::updateDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a9531ab9a77b992bbde7893f620cddd9f),
[TechDrawGui::TaskCenterLine::updateOrientation()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#ad9dd59e9e085e5605768c304db9defc0),
and
[DrawingGui::OrthoViews::~OrthoViews()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#af83325cf7209c3e1a29815419bf007b1).

## ◆ redirectSubName()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::redirectSubName  | ( | std::ostringstream & | _ss_ ,   
---|---|---|---  
|  | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _topParent_ ,   
|  | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _child_  
| ) | |  const  
virtual  
  
Allow object to redirect a subname path.

Parameters

     ss| input as the current subname path from _topParent_ leading just before this object, i.e. ends at the parent of this object. This function should append its own name to this path, or redirect the subname to other place.   
---|---  
topParent| top parent of this subname path  
child| the immediate child object in the path  
  
This function is called by tree view to generate a subname path when an item
is selected in the tree. [Document](../../d8/d3e/classApp_1_1Document.html
"The document class.") object can use this function to redirect the selection
to some other objects.

## ◆ removeDynamicProperty()

| virtual [bool](../../d9/db9/classbool.html) App::DocumentObject::removeDynamicProperty  | ( | const char *  | _prop_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a7e5425268a06b3e8a12f45abbbcfd653).

Referenced by
[Spreadsheet::Sheet::clear()](../../d0/da8/classSpreadsheet_1_1Sheet.html#aa8c30f5ab2af03e8e64231356b208b0c),
[Spreadsheet::Sheet::clearAll()](../../d0/da8/classSpreadsheet_1_1Sheet.html#ab0307b7c79c21448a9360d25dc993224),
[Spreadsheet::Sheet::removeColumns()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a75afad7e20342f29f1766cf48eab275a),
[Spreadsheet::Sheet::removeRows()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a0f72b1911b8c58350ba9a868328e9b57),
[Spreadsheet::Cell::setAlias()](../../d5/d22/classSpreadsheet_1_1Cell.html#a31072bb3341e28b9398d044d34b1a557),
[Spreadsheet::Sheet::setFloatProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a082ddc211d51376d6d8c3c77aa4a9bb2),
[Spreadsheet::Sheet::setIntegerProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a396a15ce1feb26825369fc32d38c028e),
[Spreadsheet::Sheet::setObjectProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a24ba012f7e01418a1ee0bd5992b7c117),
[Spreadsheet::Sheet::setQuantityProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a1200f02d91cc685af952ac5c7d369010),
[Spreadsheet::Sheet::setStringProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a217878fa6e8ba03d534f5f22e44bce17),
[PartDesign::SubShapeBinder::setupCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3f0c1dcf0ed5800b1865c2c42f4e25f7),
[App::LinkBaseExtension::setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e),
and
[Spreadsheet::Sheet::updateProperty()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a9a0640fab46ed529fc1c4de49b0bb699).

## ◆ renameObjectIdentifiers()

| virtual void App::DocumentObject::renameObjectIdentifiers  | ( | const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#ac1686eaca6179a2f346760661a24c7ef).

## ◆ resetError()

| void App::DocumentObject::resetError  | ( | void  | | ) |   
---|---|---|---|---|---  
protected  
  
## ◆ resolve()

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::DocumentObject::resolve  | ( | const char *  | _subname_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) **  | _parent_ = `nullptr`,   
|  | std::string *  | _childName_ = `nullptr`,   
|  | const char **  | _subElement_ = `nullptr`,   
|  | [PyObject](../../df/d1b/classPyObject.html) **  | _pyObj_ = `nullptr`,   
|  | [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) *  | _mat_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _transform_ = `true`,   
|  | [int](../../d1/da0/classint.html) | _depth_ = `0`  
| ) | |  const  
  
Resolve the last document object referenced in the subname.

Parameters

     subname| dot separated subname   
---|---  
parent| return the direct parent of the object  
childName| return child name to be passed to is/setElementVisible()  
subElement| return non-object sub-element name if found. The pointer is
guaranteed to be within the buffer pointed to by 'subname'  
  
See also

    [getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6 "Get the sub element/object by name.")

Returns

    Returns the last referenced document object in the subname. If no such object in subname, return pObject. 

Referenced by
[Gui::ViewProviderLink::applyColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a870666ac3bc9da51dc3b8cab2a0874cb),
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
and
[Gui::SelectionSingleton::setVisible()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab23ac3091ebd5ec52d897b3416a05e2d).

## ◆ resolveRelativeLink()

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::DocumentObject::resolveRelativeLink  | ( | std::string & | _subname_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _link_ ,   
|  | std::string & | _linkSub_  
| ) | |  const  
  
Resolve a link reference that is relative to this object reference.

Parameters

     subname| on input, this is the subname reference to the object that is to be assigned a link. On output, the reference may be offset to be rid of any common parent.   
---|---  
link| on input, this is the top parent of the link reference. On output, it
may be altered to one of its child to be rid off any common parent.  
linkSub| on input, this the subname of the link reference. On output, it may
be offset to be rid off any common parent.  
  
Returns

    The corrected top parent of the object that is to be assigned the link. If the output 'subname' is empty, then return the object itself.

To avoid any cyclic reference, an object must not be assign a link to any of
the object in its parent. This function can be used to resolve any common
parents of an object and its link target.

For example, with the following object hierarchy

Group |–Group001 | |–Box | |–Cylinder |–Group002 |–Box001 |–Cylinder001

If you want add a link of Group.Group002.Box001 to Group.Group001, you can
call with the following parameter (which are usually obtained from
[Selection.getSelectionEx()](../../de/d75/group__draftutils.html#ga5e10006927dba21622a83c5f6d42829a),
check usage in TreeWidget::onDropEvent()): std::string subname("Group002.");
auto link = Group; std::string linkSub("Group001.Box001."); parent =
Group.resolveRelativeLink(subname,link,linkSub);

The resolving result is as follow: return -> Group001 subname -> "" link ->
Group002 linkSub -> "Box001."

The common parent 'Group' is removed.

## ◆ Save()

| virtual void App::DocumentObject::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
This method is used to save properties to an XML document.

A good example you'll find in PropertyStandard.cpp, e.g. the vector:

void
[PropertyVector::Save](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10
"This method is used to save properties to an XML document.") (Writer &writer)
const

{

writer << writer.ind() << "<PropertyVector valueX=\"" << _cVec.x <<

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

Reimplemented from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5).

Reimplemented in
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#ab1443831f8c6492a77f0f9483688c5b6),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a914f9773505d35bfd655e97abffb6d7b),
and
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3).

Referenced by
[Robot::RobotObject::Save()](../../db/d51/classRobot_1_1RobotObject.html#ab1443831f8c6492a77f0f9483688c5b6),
[Sketcher::SketchObject::Save()](../../d9/dad/classSketcher_1_1SketchObject.html#a914f9773505d35bfd655e97abffb6d7b),
and
[App::VRMLObject::Save()](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3).

## ◆ setDocument()

| void App::DocumentObject::setDocument  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
protected  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
and
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4).

## ◆ setElementVisible()

| virtual [int](../../d1/da0/classint.html) App::DocumentObject::setElementVisible  | ( | const char *  | _element_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _visible_  
| ) | |   
virtual  
  
Child element handling.

Set sub-element visibility

For performance reason, `element` must not contain any further sub-elements,
i.e. there should be no '.' inside `element`.

Returns

    -1 if element visibility is not supported, 0 if element is not found, 1 if success 

Referenced by
[App::LinkBaseExtension::extensionSetElementVisible()](../../da/dd9/classApp_1_1LinkBaseExtension.html#af0547afce075bf3860bd9afe3052a61b),
and
[Gui::SelectionSingleton::setVisible()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab23ac3091ebd5ec52d897b3416a05e2d).

## ◆ setError()

| void App::DocumentObject::setError  | ( | void  | | ) |   
---|---|---|---|---|---  
protected  
  
Referenced by
[App::Origin::execute()](../../d9/d8b/classApp_1_1Origin.html#ae8015373defe4fb60c2a44da46721c84),
and
[Import::FeatureImportStep::Execute()](../../da/dde/classImport_1_1FeatureImportStep.html#a42d170d40ce67819f931b5894145d229).

## ◆ setExpression()

| virtual void App::DocumentObject::setExpression  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > | _expr_  
| ) | |   
virtual  
  
Reimplemented in
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#ad328e83eeb43879902e8fb12f35a7be6).

## ◆ setStatus()

void App::DocumentObject::setStatus  | ( | [ObjectStatus](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3a) | _pos_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _on_  
| ) | |   
  
Referenced by
[PartDesign::AdditiveHelix::AdditiveHelix()](../../d9/d78/classPartDesign_1_1AdditiveHelix.html#a05ce97b581300720e4ec60944002796f),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::DocumentP::addRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#ae3969263ba43a8c8e9f3ebe393143523),
[PartDesign::Body::Body()](../../dd/db8/classPartDesign_1_1Body.html#a7727b0d8c998bbc2942e4c802e31e2eb),
[Part::AttachExtension::extensionOnChanged()](../../dc/d47/classPart_1_1AttachExtension.html#ac73db2d8f32ca41b89157b47edce44c1),
[PartDesign::FeatureBase::FeatureBase()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a3b5d97eb5e676bac4a5b3819a5655b78),
[Part::Offset2D::Offset2D()](../../d7/dcf/classPart_1_1Offset2D.html#ada731a1553ffbd64cf44a218fbfffd05),
[Sketcher::SketchObject::onChanged()](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[PartDesign::Body::onDocumentRestored()](../../dd/db8/classPartDesign_1_1Body.html#aa6affc475d3884d9570838e731749605),
[App::Origin::Origin()](../../d9/d8b/classApp_1_1Origin.html#a35b6b6a5291bedf81b48914defa0d210),
[App::OriginFeature::OriginFeature()](../../da/dfe/classApp_1_1OriginFeature.html#a6d4c4d2f32a215e2ac438c897f0de70a),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[Path::PropertyPath::RestoreDocFile()](../../da/d75/classPath_1_1PropertyPath.html#a6ee2ea90ed9f02be32225df050ee9034),
[Gui::DocumentObjectItem::setExpandedStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#aab392a92c88bc1d5248cc08710dda93c),
and
[PartDesign::SubtractiveHelix::SubtractiveHelix()](../../d4/d97/classPartDesign_1_1SubtractiveHelix.html#a3dba8f9972d539c195e894d74fbb849f).

## ◆ setupObject()

| virtual void App::DocumentObject::setupObject  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
get called after a brand new object was created

Reimplemented in
[App::Origin](../../d9/d8b/classApp_1_1Origin.html#af5708fed01b27a82a33d8b06d02e89e6),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#ace3e681c5be8bc26572497dea2ed09cd),
[TechDraw::DrawTileWeld](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#ae5e7260e00acfb89459c7efc05371ff5),
[Part::Extrusion](../../db/d6c/classPart_1_1Extrusion.html#a96c319a1198a497416ce1525ad8bde71),
[Part::Face](../../dc/dbf/classPart_1_1Face.html#ac21ea7f5cfc94b6dc0473be52f3b2009),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a6e1142caeefe37b0220774080bd351c3),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#a48d6d2b6f190df1e9929fb34966adc12),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a788801f841b2c6dfcb6493aa6a69aacd),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a5daedfa385237ef05b52c5316d05a391),
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a6d7ba4e15ae9e6df91f2360740d682d5),
and
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab1f22c26a62a06b470bb8b5dff7df69f).

Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[TechDraw::DrawTileWeld::setupObject()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#ae5e7260e00acfb89459c7efc05371ff5),
[Part::Extrusion::setupObject()](../../db/d6c/classPart_1_1Extrusion.html#a96c319a1198a497416ce1525ad8bde71),
[Part::Face::setupObject()](../../dc/dbf/classPart_1_1Face.html#ac21ea7f5cfc94b6dc0473be52f3b2009),
[Part::Revolution::setupObject()](../../d3/d17/classPart_1_1Revolution.html#a6e1142caeefe37b0220774080bd351c3),
[PartDesign::Body::setupObject()](../../dd/db8/classPartDesign_1_1Body.html#a48d6d2b6f190df1e9929fb34966adc12),
[TechDraw::DrawGeomHatch::setupObject()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a5daedfa385237ef05b52c5316d05a391),
[TechDraw::DrawHatch::setupObject()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a6d7ba4e15ae9e6df91f2360740d682d5),
and
[TechDraw::DrawViewSection::setupObject()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab1f22c26a62a06b470bb8b5dff7df69f).

## ◆ testIfLinkDAGCompatible() [1/4]

[bool](../../d9/db9/classbool.html) App::DocumentObject::testIfLinkDAGCompatible  | ( | [App::PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html) & | _linkTo_| ) |  const  
---|---|---|---|---|---  
  
## ◆ testIfLinkDAGCompatible() [2/4]

[bool](../../d9/db9/classbool.html) App::DocumentObject::testIfLinkDAGCompatible  | ( | [App::PropertyLinkSubList](../../d9/d92/classApp_1_1PropertyLinkSubList.html) & | _linksTo_| ) |  const  
---|---|---|---|---|---  
  
## ◆ testIfLinkDAGCompatible() [3/4]

[bool](../../d9/db9/classbool.html) App::DocumentObject::testIfLinkDAGCompatible  | ( | const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _linksTo_| ) |  const  
---|---|---|---|---|---  
  
## ◆ testIfLinkDAGCompatible() [4/4]

[bool](../../d9/db9/classbool.html) App::DocumentObject::testIfLinkDAGCompatible  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _linkTo_| ) |  const  
---|---|---|---|---|---  
  
testIfLinkIsDAG tests a link that is about to be created for circular
references.

Parameters

     objToLinkIn| (input). The object this object is to depend on after the link is going to be created.   
---|---  
  
Returns

    true if link can be created (no cycles will be made). False if the link will cause a circular dependency and break recomputes. Throws an error if the document already has a circular dependency. That is, if the return is true, the link is allowed. 

Referenced by
[PartDesignGui::NoDependentsSelection::allow()](../../d5/dea/classPartDesignGui_1_1NoDependentsSelection.html#ae8f4af78e4c1c096ec1c2ffaa6ec56d5),
[Sketcher::SketchObject::isCarbonCopyAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a9410a860724556bf47d88a993e080435),
and
[Sketcher::SketchObject::isExternalAllowed()](../../d9/dad/classSketcher_1_1SketchObject.html#a15854bee280f512f617c7f34752ab823).

## ◆ testStatus()

[bool](../../d9/db9/classbool.html) App::DocumentObject::testStatus  | ( | [ObjectStatus](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3a) | _pos_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::PropertyLinkSubList::addValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17cad50fa5ecc14fafcfc99e3cba7bbd),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewDimension::getDimValue()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a617487ea202ee4a1a61972d6e1cd894c),
[App::PropertyXLink::getDocumentInList()](../../d2/de2/classApp_1_1PropertyXLink.html#ad702be5a5d5a8c7cdf8f10cd4c22f26d),
[App::PropertyXLink::getDocumentOutList()](../../d2/de2/classApp_1_1PropertyXLink.html#af1f6b642c153368da2ec154538106914),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[PartDesign::DressUp::onChanged()](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[App::PropertyLink::resetLink()](../../d4/d77/classApp_1_1PropertyLink.html#a0461c85fa8e082a75df6e848f94d8c39),
[App::PropertyLinkList::set1Value()](../../d3/d8c/classApp_1_1PropertyLinkList.html#a7a16fe45fc1c04feba8b79c9cd463f4d),
[App::PropertyLinkSubList::setValue()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ace25e03cde7c0f0f8f279fedb961708f),
[App::PropertyLinkSubList::setValues()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#aa58017810599c4b0262c106696d6d0c7),
[PartDesign::SubShapeBinder::slotRecomputedObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ac6e4df134bd3f3a857d65e27b7b46cb5),
[App::PropertyLinkList::~PropertyLinkList()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aef7be25314c8c5441d9baa207ddd51c1),
[App::PropertyLinkSub::~PropertyLinkSub()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac2366078790473115b614fdc02345a4a),
and
[App::PropertyLinkSubList::~PropertyLinkSubList()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a17189b0ae71b797884f1ca041cfe263f).

## ◆ touch()

void App::DocumentObject::touch  | ( | [bool](../../d9/db9/classbool.html) | _noRecompute_ = `false`| ) |   
---|---|---|---|---|---  
  
Set the property touched -> changed, cause recomputation in Update()

set this document object touched (cause recomputation on dependent features)

Referenced by
[Gui::ElementColors::Private::accept()](../../d8/dc9/classElementColors_1_1Private.html#a5704a7d026d4033d6f6b98086de77f53),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[Gui::ViewProviderGeometryObject::onChanged()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Drawing::FeaturePage::onChanged()](../../db/d0f/classDrawing_1_1FeaturePage.html#a9c6b6897f29ff589163044d51b7e5c04),
[PartDesign::Boolean::onChanged()](../../d2/d81/classPartDesign_1_1Boolean.html#a41c675a8b7f2f6e73b95946b99245f12),
[TechDraw::DrawProjGroupItem::onChanged()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#aea5cc872256320be7112396d84b3fee5),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[PartGui::ViewProviderPartExt::setHighlightedEdges()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a8a3906f845faf45e648ef05e1bc6fa45),
[PartGui::ViewProviderPartExt::setHighlightedFaces()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ae3121cead5ae89980439ae2b9dfe4b3a),
and
[PartGui::ViewProviderPartExt::setHighlightedPoints()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a6158c410a40ace62d95eabaddf942d9b).

## ◆ unsetupObject()

| virtual void App::DocumentObject::unsetupObject  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
get called when object is going to be removed from the document

Reimplemented in
[App::Origin](../../d9/d8b/classApp_1_1Origin.html#ace2a648f85e06a55346df50a6fad40fe),
[TechDraw::DrawViewCollection](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a33815aa3bc978248b9ec92b423ba7c45),
[TechDraw::DrawViewDimExtent](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#abc5c45571551383c8db0194bec4bcec6),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#afdfa500297e96c8fb586187144713bd8),
[TechDraw::DrawPage](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
[TechDraw::DrawProjGroupItem](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
[TechDraw::DrawViewDetail](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#a94df756e01896f5fc84f7b68edf0cd87),
[TechDraw::DrawViewPart](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a404e3640464295cb65780c7374a83940),
[TechDraw::DrawViewSection](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a59ffd784347ce60563b9778860a5da32),
[TechDraw::LandmarkDimension](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a238125d961e1b341b853671cf6e62c1e),
[TechDraw::DrawGeomHatch](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a5a282d1f6d612cb617d3e7d59ed29d22),
and
[TechDraw::DrawHatch](../../d0/d97/classTechDraw_1_1DrawHatch.html#a4d500170f5a932de1b90886ec00c0506).

Referenced by
[TechDraw::DrawViewDimExtent::unsetupObject()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#abc5c45571551383c8db0194bec4bcec6),
[PartDesign::Body::unsetupObject()](../../dd/db8/classPartDesign_1_1Body.html#afdfa500297e96c8fb586187144713bd8),
[TechDraw::DrawGeomHatch::unsetupObject()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a5a282d1f6d612cb617d3e7d59ed29d22),
and
[TechDraw::DrawHatch::unsetupObject()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a4d500170f5a932de1b90886ec00c0506).

## Friends And Related Function Documentation

## ◆ Document

| [friend](../../d7/d23/classfriend.html) class
[Document](../../d8/d3e/classApp_1_1Document.html)  
---  
friend  
  
## ◆ ObjectExecution

| [friend](../../d7/d23/classfriend.html) class ObjectExecution  
---  
friend  
  
## ◆ Transaction

| [friend](../../d7/d23/classfriend.html) class
[Transaction](../../de/dbf/classApp_1_1Transaction.html)  
---  
friend  
  
## Member Data Documentation

## ◆ ExpressionEngine

[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
App::DocumentObject::ExpressionEngine  
---  
  
Referenced by
[Gui::ExpressionBinding::bind()](../../dc/d5a/classGui_1_1ExpressionBinding.html#aba7b2c918c04b6e3f589e53876cdb761),
[Sketcher::SketchObject::constraintsRemoved()](../../d9/dad/classSketcher_1_1SketchObject.html#a97732ef24ca9fb3fa18710fe87864ada),
[Sketcher::SketchObject::constraintsRenamed()](../../d9/dad/classSketcher_1_1SketchObject.html#aac2c8322e53a7823d1940ac93c58a87a),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[Sketcher::SketchObject::setExpression()](../../d9/dad/classSketcher_1_1SketchObject.html#ad328e83eeb43879902e8fb12f35a7be6),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
and
[Spreadsheet::Sheet::updateBindings()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a0096c4f2015e803cc39270f61aa028fb).

## ◆ Label

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::DocumentObject::Label  
---  
  
Referenced by
[FemGui::TaskDlgCreateNodeSet::accept()](../../d9/d8f/classFemGui_1_1TaskDlgCreateNodeSet.html#aae7b7afa431004b899003fe789f532bb),
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[PartGui::SweepWidget::accept()](../../d0/dda/classPartGui_1_1SweepWidget.html#ac9e4d005b6e7ecc3ddae3c22258fd8a5),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[Gui::ViewProviderPythonFeatureImp::attach()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a7fe9943f935cd2bd115ffc3814901564),
[SurfaceGui::FillingPanel::checkOpenCommand()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#af89e0fc6c9df9e0a5f3e4e966fcbd76f),
[SurfaceGui::FillingEdgePanel::checkOpenCommand()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a5a9ee6e2c42e74538ab2ca085fe087cb),
[SurfaceGui::FillingVertexPanel::checkOpenCommand()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a90551017148fdaedcce1af12566687da),
[SurfaceGui::GeomFillSurface::checkOpenCommand()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a184573c3baebee00c61b77bdad207b9e),
[SurfaceGui::SectionsPanel::checkOpenCommand()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#ab9168c66c4f0a26633cbaa855d1743a7),
[Import::ExportOCAF::createNode()](../../d2/dda/classImport_1_1ExportOCAF.html#a2f16971e3d1d6b6f1c5a7b0da2c24636),
[Gui::PointMarker::customEvent()](../../d6/deb/classGui_1_1PointMarker.html#af3aff66aa9cfaaff337386e66a61c0f4),
[SpreadsheetGui::DlgBindSheet::DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[PartGui::DlgProjectionOnSurface::DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a280d8ac8bf690484a268f54625c2c7e2),
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18),
[PartDesignGui::ViewProviderDatum::doubleClicked()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a588caea71c3f6afedfddf98adfb9f038),
[Gui::ElementColors::ElementColors()](../../db/d21/classGui_1_1ElementColors.html#a7d0d5836a9361c145408b75cf8b0b33c),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[MeshGui::ViewProviderMesh::exportMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a7e475ac2c734112a916b21ec3ffa8f8c),
[App::OriginGroupExtension::extensionGetSubObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a3ef5473d30e6ceafb86e8d643f0b2f11),
[PartGui::FaceColors::FaceColors()](../../db/d9e/classPartGui_1_1FaceColors.html#a5aef3588ddb084101d511fc687ac45d7),
[TechDraw::DrawProjGroup::getDirsFromFront()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a66cbbc8038fcab5532278784cbac867b),
[Gui::LinkInfo::getLinkedLabel()](../../d4/da4/classGui_1_1LinkInfo.html#a159af4c143bfb19a75233b87d6a780c8),
[TechDraw::DrawViewSpreadsheet::getSheetImage()](../../db/d3e/classTechDraw_1_1DrawViewSpreadsheet.html#a22203364d476a484dbe0574b33fdba5b),
[Part::ImportIgesParts()](../../d2/db9/namespacePart.html#a10322b892abc3b1779054dacf1a49e53),
[MeshPartGui::Mesh2ShapeGmsh::loadOutput()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a44307c501da72ba058c29e10998ef358),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[TechDrawGui::TaskLinkDim::loadToTree()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a78901c66da67bb8e9a3a97469e4f61d4),
[MeshGui::MeshSplit::makeCopy()](../../d9/de5/classMeshGui_1_1MeshSplit.html#aae5f989f78a6a83f6f2f1f8dabfd1a56),
[TechDraw::DrawPage::onChanged()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a883373ce2f6c8d3335c3074c1f7866ed),
[TechDraw::DrawView::onChanged()](../../d6/d1c/classTechDraw_1_1DrawView.html#a2980fbae4ce0a12aae609193764465cf),
[TechDraw::DrawViewDetail::onChanged()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad6ccb9e626c3e77b1228188eb2fab34c),
[TechDraw::DrawViewSection::onChanged()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9ddcd143279f82644cdcc124c6a71419),
[App::TextDocument::onChanged()](../../d9/de9/classApp_1_1TextDocument.html#affdf6c8a48df5cea53213040c487e5f8),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[SurfaceGui::FillingPanel::onSelectionChanged()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#ac8f46981ec84ea0a20faf5791db7cb4b),
[SurfaceGui::FillingEdgePanel::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#a13eada025c84a3c28016f3c3974d089d),
[SurfaceGui::FillingVertexPanel::onSelectionChanged()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a67388941ba03ae81ee5e15d8043bbc02),
[SurfaceGui::GeomFillSurface::onSelectionChanged()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#acd70791d15b148166826bac85bc802e9),
[SurfaceGui::SectionsPanel::onSelectionChanged()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#a919af91b2e734c27e20773a1f737a49c),
[App::PropertyLinkBase::restoreLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb),
[Import::ExportOCAF::saveShape()](../../d2/dda/classImport_1_1ExportOCAF.html#a0a7a04ae4b422b40b93d76a1f6966b9c),
[TechDraw::DrawViewSection::sectionExec()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a79c8f60f63dd54684af4cad42f91ee4e),
[DrawingGui::orthoview::set_data()](../../db/df8/classDrawingGui_1_1orthoview.html#a3395e8771fab71cac84a95eeae04c721),
[SurfaceGui::FillingPanel::setEditedObject()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#aaaeba016fe808b6dc4d3ddfc9788d380),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
[RobotGui::TaskEdge2TracParameter::setHideShowObject()](../../d0/dbf/classRobotGui_1_1TaskEdge2TracParameter.html#a4f0db452c19a0f88335d993d587a371b),
[App::LinkBaseExtension::setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[TechDrawGui::TaskDetail::setUiFromFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#ab79d692d4be08f631cc8902f54e1f0dc),
[PartDesignGui::TaskDressUpParameters::setupTransaction()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a6f99d504a2dbb11111be017f2bfe4bbf),
[MeshGui::Annotation::show()](../../dd/d2d/classMeshGui_1_1Annotation.html#a8e675bcb0e642864e58f2d9f3b482ca8),
[DrawingGui::ViewProviderDrawingPage::showDrawingView()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#af7cd2898c5d4d289f22f0fb7c232984f),
[SpreadsheetGui::ViewProviderSheet::showSpreadsheetView()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a912de2c5ce615efc6d1e3f70f3674f1b),
[Spreadsheet::SheetObserver::slotChangedObject()](../../db/d2b/classSpreadsheet_1_1SheetObserver.html#afa0379ae388031e7371193ab6c5d6296),
[FemGui::TaskObjectName::TaskObjectName()](../../d3/d6b/classFemGui_1_1TaskObjectName.html#ae998f7ddece0813597d374c662db31b7),
[PartDesignGui::TaskPipeOrientation::TaskPipeOrientation()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#ac6d362fde0b1452a942b513494180d97),
[PartDesignGui::TaskPipeParameters::TaskPipeParameters()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#ad8be386ff75b6d3c414ffbe505e48561),
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95),
[TechDraw::DrawProjGroupItem::unsetupObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a74c1e831d9704f99007d0b9398001f90),
[SpreadsheetGui::SheetView::updateCell()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#afe16747ee261395854ecdfb7d5326901),
[DrawingGui::ViewProviderDrawingPage::updateData()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
and
[MeshPartGui::Mesh2ShapeGmsh::writeProject()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#a3931d67654b40d307417d697e6291ab3).

## ◆ Label2

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::DocumentObject::Label2  
---  
  
Referenced by
[Gui::TreeWidgetEditDelegate::createEditor()](../../db/d6e/classGui_1_1TreeWidgetEditDelegate.html#ad2db8c1dd8e1914745c0a1b7fc111484),
and
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18).

## ◆ oldLabel

| std::string App::DocumentObject::oldLabel  
---  
protected  
  
Old label; used for renaming expressions.

## ◆ pcNameInDocument

| const std::string* App::DocumentObject::pcNameInDocument  
---  
protected  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
and
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4).

## ◆ PythonObject

| Py::SmartPtr App::DocumentObject::PythonObject  
---  
protected  
  
python object of this class and all descendent

Referenced by
[Fem::FemPostPipeline::getPyObject()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a4b39fb08f59a125dcc783cf93e25d86d),
[Mesh::Feature::getPyObject()](../../dd/dce/classMesh_1_1Feature.html#a7a700a82e66b15d3eb4845ad75c194ab),
[Spreadsheet::Sheet::getPyObject()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a57333609c76e9d1469163c8d70f75053),
[App::DocumentObjectGroup::getPyObject()](../../d8/d75/classApp_1_1DocumentObjectGroup.html#a8c2a18ad6bd291d0f6657e877c4f7a92),
[Part::BodyBase::getPyObject()](../../da/dc8/classPart_1_1BodyBase.html#a9e28639037238df4c8dafb4518ee86c4),
[Part::Feature::getPyObject()](../../d7/d7e/classPart_1_1Feature.html#ae23b16d8ba14ec40c3cd74aca0634f2e),
[Part::Primitive::getPyObject()](../../d2/d31/classPart_1_1Primitive.html#a666f699fb9530523ef6467717f385096),
[PartDesign::FeaturePrimitive::getPyObject()](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a49b5d225e27f3adf2cb0b8452fa84ef8),
[App::GeoFeature::getPyObject()](../../d7/d75/classApp_1_1GeoFeature.html#a6837f9af91a2619c420f361033ab0da5),
[App::InventorObject::getPyObject()](../../da/d11/classApp_1_1InventorObject.html#adb3523042b8befd61616bc05fedd290f),
[App::VRMLObject::getPyObject()](../../df/df6/classApp_1_1VRMLObject.html#a5a9445b1375ded9f86617e15151ec389),
[Fem::FemMeshObject::getPyObject()](../../d5/d68/classFem_1_1FemMeshObject.html#abb0ba3282d7a1b42eaeaaee6364afd42),
[Fem::FemResultObject::getPyObject()](../../d3/d81/classFem_1_1FemResultObject.html#af6645066e6371ce9460ca9836cd5af6b),
[Fem::FemSetElementsObject::getPyObject()](../../df/d49/classFem_1_1FemSetElementsObject.html#a5ea9bd5b13b1f95a0058d800a6166ab1),
[Fem::FemSetFacesObject::getPyObject()](../../df/d72/classFem_1_1FemSetFacesObject.html#a4754f40e1edf8bc0a5701fa58a525625),
[Fem::FemSetGeometryObject::getPyObject()](../../df/d59/classFem_1_1FemSetGeometryObject.html#a96a9315d631398747b4c9fcfc784ee9a),
[Fem::FemSetNodesObject::getPyObject()](../../dc/d59/classFem_1_1FemSetNodesObject.html#a879bdd1e2d66688ae040e2a4d51772a3),
[Fem::FemSetObject::getPyObject()](../../d8/dbe/classFem_1_1FemSetObject.html#ac7ab5f7744ff44d8d4f6f4bb6e022f66),
[Fem::FemSolverObject::getPyObject()](../../d1/dd0/classFem_1_1FemSolverObject.html#abf5e279df0983cef9533c8f3095e5574),
[Path::FeatureArea::getPyObject()](../../da/d1e/classPath_1_1FeatureArea.html#a71e18a904362f9e20f126aca4f13b8e8),
[Path::Feature::getPyObject()](../../d5/dd9/classPath_1_1Feature.html#ab7f800e910601271c9a4bc2480dad5f2),
[Path::FeatureCompound::getPyObject()](../../d2/d43/classPath_1_1FeatureCompound.html#a08d674d0a02ef64d5572e51c3689fd2d),
[Robot::RobotObject::getPyObject()](../../db/d51/classRobot_1_1RobotObject.html#a5b35961553442da622521648b1f50365),
[Robot::TrajectoryObject::getPyObject()](../../d7/db5/classRobot_1_1TrajectoryObject.html#aa511366030cf224da9a3a0d17b07606e),
[TechDraw::DrawParametricTemplate::getPyObject()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#a446f297751fa8bd5511d4d48f6dc75ed),
[TechDraw::DrawRichAnno::getPyObject()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a206b0ca34b87f79762924fedec8c7fd1),
[TechDraw::DrawSVGTemplate::getPyObject()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#ad0a08bbe311a5147f49ab0f3647c88dd),
[TechDraw::DrawTemplate::getPyObject()](../../d8/d95/classTechDraw_1_1DrawTemplate.html#aead757612a7d1a557eeeb43e0caec8bd),
[TechDraw::DrawTile::getPyObject()](../../da/d56/classTechDraw_1_1DrawTile.html#a0e979b8f73ef5fea5997dc8e8e12b9d4),
[TechDraw::DrawTileWeld::getPyObject()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a00b92083449ce106a622bf7b0ca3fdea),
[TechDraw::DrawViewClip::getPyObject()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a4e296aa3a79c48e108afe2d9db30731f),
[TechDraw::DrawViewDimExtent::getPyObject()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#a9a71017db88391c3248e29a3931be915),
[TechDraw::DrawWeldSymbol::getPyObject()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#ad9e24e34ca274c67e594e384a37e2cb9),
[PartDesign::Body::getPyObject()](../../dd/db8/classPartDesign_1_1Body.html#a9579e5a76ef1c70cc24701d4bba32c6c),
[Sketcher::SketchObject::getPyObject()](../../d9/dad/classSketcher_1_1SketchObject.html#a7a2970aaacc965d3d4c3b3a949fcb21f),
[TechDraw::DrawGeomHatch::getPyObject()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#aa02555ef8da0ade9bf32d826683869d6),
[TechDraw::DrawHatch::getPyObject()](../../d0/d97/classTechDraw_1_1DrawHatch.html#a206dea2db611b805e68fc860a1032597),
[TechDraw::DrawLeaderLine::getPyObject()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a87cddb7857e5d66215c929844d3bd438),
[TechDraw::DrawPage::getPyObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a55ad5df210dcaeadeaf5b8504dfdc736),
[TechDraw::DrawProjGroup::getPyObject()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acaf6822e5ff679aae0ff66759d7135dc),
[TechDraw::DrawProjGroupItem::getPyObject()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a28fc999e36c9404361ca24453f424678),
[TechDraw::DrawView::getPyObject()](../../d6/d1c/classTechDraw_1_1DrawView.html#af82b1daff82fedafa74673a607bc38a4),
[TechDraw::DrawViewDimension::getPyObject()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a3e332a5c716d9cc5145fa9afa7fcacff),
[TechDraw::DrawViewPart::getPyObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab0f733c1df0bd35133eb9d61e5670fe4),
and
[TechDraw::DrawViewSymbol::getPyObject()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a6406ae57714b08e7d99c03f1bb4d652c).

## ◆ signalBeforeChange

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::DocumentObject::signalBeforeChange  
---  
  
signal before changing a property of this object

## ◆ signalChanged

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::DocumentObject::signalChanged  
---  
  
signal on changed property of this object

## ◆ StatusBits

| std::bitset<32> App::DocumentObject::StatusBits  
---  
protected  
  
Status bits of the document object The first 8 bits are used for the base
system the rest can be used in descendent classes to mark special statuses on
the objects.

The bits and their meaning are listed below: 0 - object is marked as 'touched'
1 - object is marked as 'erroneous' 2 - object is marked as 'new' 3 - object
is marked as 'recompute', i.e. the object gets recomputed now 4 - object is
marked as 'restoring', i.e. the object gets loaded at the moment 5 - object is
marked as 'deleting', i.e. the object gets deleted at the moment 6 - reserved
7 - reserved 16 - object is marked as 'expanded' in the tree view

Referenced by
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e).

## ◆ StdReturn

|
[DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html)*
App::DocumentObject::StdReturn  
---  
static  
  
Referenced by
[App::Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526),
[Fem::Constraint::execute()](../../d0/d11/classFem_1_1Constraint.html#ac7343ea84455e2331eecd8aab10b38ac),
[Mesh::Curvature::execute()](../../d2/d39/classMesh_1_1Curvature.html#a76bfebcb28cee108275564ade910411c),
[Mesh::FixDefects::execute()](../../d4/d1f/classMesh_1_1FixDefects.html#a91ee486eafe50bffa50981b6ee1919bb),
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
[Mesh::Export::execute()](../../d6/d40/classMesh_1_1Export.html#a56265dded005a8be13258af1b273ed51),
[Mesh::Import::execute()](../../d9/d29/classMesh_1_1Import.html#a744e663c172c1174c37b363372a377b2),
[Mesh::SegmentByMesh::execute()](../../d0/ddf/classMesh_1_1SegmentByMesh.html#a0fd4604225620a5902f526c867f0a7ed),
[Mesh::SetOperations::execute()](../../d3/d8f/classMesh_1_1SetOperations.html#a5fbee709af3e7da8f267824be4c4b370),
[Mesh::Sphere::execute()](../../d1/d57/classMesh_1_1Sphere.html#ae830b723d9c2977e6080c9e87f3ec139),
[Mesh::Ellipsoid::execute()](../../d2/dd6/classMesh_1_1Ellipsoid.html#aa7094fc5c9ce3b03b37b1875e8962b68),
[Mesh::Cylinder::execute()](../../df/def/classMesh_1_1Cylinder.html#a7f0a6253a8936e26fdd2794992f9cbb4),
[Mesh::Cone::execute()](../../d4/dbc/classMesh_1_1Cone.html#a23701269832147c5746476d7e6b3b8af),
[Mesh::Torus::execute()](../../de/da3/classMesh_1_1Torus.html#a9ca70ccb5548f0852b54fe55f58f27a9),
[Mesh::Cube::execute()](../../df/d68/classMesh_1_1Cube.html#a5c7921255a963127e0496b550023f3ed),
[Mesh::Transform::execute()](../../d3/def/classMesh_1_1Transform.html#a28b6499af9da72410435606375790c1b),
[Mesh::TransformDemolding::execute()](../../dc/da9/classMesh_1_1TransformDemolding.html#abca1f141e3599f6b718d1fcbafe07c51),
[Mesh::Feature::execute()](../../dd/dce/classMesh_1_1Feature.html#a1e5ce1fb233e1b7820af42cc6758fd9f),
[PartDesign::Pad::execute()](../../d9/d14/classPartDesign_1_1Pad.html#a17b37a5aaa299709fbb066564ef25b3e),
[PartDesign::Pocket::execute()](../../d1/d89/classPartDesign_1_1Pocket.html#aac791837d2ea389e30768f0fb6d25935),
[Points::Feature::execute()](../../d8/de3/classPoints_1_1Feature.html#a1e5ce1fb233e1b7820af42cc6758fd9f),
[Points::Structured::execute()](../../d0/d43/classPoints_1_1Structured.html#a777464aea8c27ad6f8c525fb1f8ce15c),
[PartDesign::FeaturePrimitive::execute()](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a6fa8b868671829d71cf102075dbab404),
[App::PropertyExpressionEngine::execute()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd),
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[App::InventorObject::execute()](../../da/d11/classApp_1_1InventorObject.html#abf0ce1809171c736570be0f9272c8af0),
[App::MeasureDistance::execute()](../../d7/d61/classApp_1_1MeasureDistance.html#aa328f58f37764c36e03ee8356325ea72),
[App::VRMLObject::execute()](../../df/df6/classApp_1_1VRMLObject.html#aa3d59e0392a0bf8b954916fe8a502008),
[Drawing::FeatureClip::execute()](../../d5/d4a/classDrawing_1_1FeatureClip.html#afed75650f49849b96c65ef93795800e5),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[Drawing::FeatureProjection::execute()](../../d8/d73/classDrawing_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[Drawing::FeatureView::execute()](../../db/d1f/classDrawing_1_1FeatureView.html#a6722811fbd5b8e5dafc809cb147e38ba),
[Drawing::FeatureViewAnnotation::execute()](../../d6/de7/classDrawing_1_1FeatureViewAnnotation.html#a74171a078f54a6d0ee13242e3b014751),
[Drawing::FeatureViewPart::execute()](../../d7/d27/classDrawing_1_1FeatureViewPart.html#a3ea73c1aee48b5bd0884ef9facadf84c),
[Drawing::FeatureViewSpreadsheet::execute()](../../de/d18/classDrawing_1_1FeatureViewSpreadsheet.html#aada40dc08dcdefc630eb0ad4ff69fe74),
[Drawing::FeatureViewSymbol::execute()](../../da/d14/classDrawing_1_1FeatureViewSymbol.html#a3563b4ff57807e29d705c04a53b7cd0b),
[Fem::FemMeshObject::execute()](../../d5/d68/classFem_1_1FemMeshObject.html#a63d3834bf66491db7b4f30f315f01dfb),
[Fem::FemMeshShapeNetgenObject::execute()](../../d9/df4/classFem_1_1FemMeshShapeNetgenObject.html#ad38e08d369e0a9c44588e98bc5ffb3ed),
[Fem::FemMeshShapeObject::execute()](../../d0/d41/classFem_1_1FemMeshShapeObject.html#a52f6bff1d5da5dc0dc05d3d0a4a90e72),
[Fem::FemPostFilter::execute()](../../d8/d6f/classFem_1_1FemPostFilter.html#a6e243a1e127e9f99d015051d8ea5a8a7),
[Fem::FemPostClipFilter::execute()](../../dc/d06/classFem_1_1FemPostClipFilter.html#a11a328bac4a9ae22ba01e4696484ae06),
[Fem::FemPostScalarClipFilter::execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter::execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
[Fem::FemPostCutFilter::execute()](../../da/d89/classFem_1_1FemPostCutFilter.html#a9ff7e939e5c3dc07c73dfe1a569e32d7),
[Fem::FemPostFunction::execute()](../../d3/d87/classFem_1_1FemPostFunction.html#a0227f858c3fbccc02f9574d9bcc3a621),
[Fem::FemPostPipeline::execute()](../../d5/d4b/classFem_1_1FemPostPipeline.html#a37a7074a69af004117f82d72be1701f8),
[Fem::FemResultObject::execute()](../../d3/d81/classFem_1_1FemResultObject.html#a0e4f90351e9ce40455801a43f9538e10),
[Fem::FemSetElementsObject::execute()](../../df/d49/classFem_1_1FemSetElementsObject.html#a3f567e9193f8d49bd542312ef5e6860f),
[Fem::FemSetFacesObject::execute()](../../df/d72/classFem_1_1FemSetFacesObject.html#a46ab2fff61403128815b2cb9b22314e6),
[Fem::FemSetGeometryObject::execute()](../../df/d59/classFem_1_1FemSetGeometryObject.html#a608e2e0fdf7c34beab9dbc7b01e6d66e),
[Fem::FemSetNodesObject::execute()](../../dc/d59/classFem_1_1FemSetNodesObject.html#a8d55585de3533d3b751f2724981d23e9),
[Fem::FemSetObject::execute()](../../d8/dbe/classFem_1_1FemSetObject.html#ae30787859238309a6dae394e902a1968),
[Fem::FemSolverObject::execute()](../../d1/dd0/classFem_1_1FemSolverObject.html#aef99c067ac336a7ad345866fa38c3046),
[Part::CustomFeature::execute()](../../da/d46/classPart_1_1CustomFeature.html#a2fe501793eddc0400a6f97b9e7af7a79),
[Part::Chamfer::execute()](../../d7/d75/classPart_1_1Chamfer.html#a4e556c2713a9af1290a0c53eeedff2f1),
[Part::Compound::execute()](../../d7/d98/classPart_1_1Compound.html#a72d02534883bc8e2b7ccb46218e87087),
[Part::Fillet::execute()](../../d4/da4/classPart_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[Part::FeatureGeometrySet::execute()](../../d6/d80/classPart_1_1FeatureGeometrySet.html#acbc44d2989a0a94e14b5100a50a1fa7f),
[Part::Mirroring::execute()](../../dc/dac/classPart_1_1Mirroring.html#aed38846265cf2381aae85d15dfb74be7),
[Part::Boolean::execute()](../../da/d3a/classPart_1_1Boolean.html#ab93d1734459a414d09ccec9df8df7831),
[Part::MultiCommon::execute()](../../d1/df7/classPart_1_1MultiCommon.html#ab89bf89ceaef91d77ba170a7e548040d),
[Part::CurveNet::execute()](../../d9/d41/classPart_1_1CurveNet.html#ab3d3703fdaab33d94b764c62d6739ce6),
[Part::MultiFuse::execute()](../../df/dbc/classPart_1_1MultiFuse.html#affac0f86cba2c15642f4d8a64a01c337),
[Part::ImportBrep::execute()](../../d8/d3e/classPart_1_1ImportBrep.html#a3fbd619fb350dff418fffd6b6f185ca7),
[Part::ImportIges::execute()](../../d2/d1d/classPart_1_1ImportIges.html#a1d947e212fdeb8ed2b8bb8ef3fae1041),
[Part::ImportStep::execute()](../../d4/de2/classPart_1_1ImportStep.html#a3c81f94deddd927756144ef4e8040678),
[Part::Polygon::execute()](../../d3/db3/classPart_1_1Polygon.html#ad32a5f75f338c91f0da7ae8da871956d),
[Part::FeatureReference::execute()](../../d2/da1/classPart_1_1FeatureReference.html#ae5a6fd5ceb91026f2ed196b23127ef02),
[Part::RuledSurface::execute()](../../d1/d41/classPart_1_1RuledSurface.html#aaff86f64ccc1eeeb1158727285cacab0),
[Part::Loft::execute()](../../d3/d52/classPart_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[Part::Sweep::execute()](../../df/dc6/classPart_1_1Sweep.html#a7fdf28d346eb1b3b838ed0dea5bb40d8),
[Part::Thickness::execute()](../../db/d73/classPart_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[Part::Refine::execute()](../../d4/d0a/classPart_1_1Refine.html#aa138404bf1cbb4270a6e4a9d02dffac7),
[Part::Reverse::execute()](../../d4/d24/classPart_1_1Reverse.html#a22150a83fa78387e05f60dd1e08d31f8),
[PartDesign::FeatureBase::execute()](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a7cc09059c368f65475f0fa3f05bc06f5),
[PartDesign::Fillet::execute()](../../d0/d50/classPartDesign_1_1Fillet.html#a3d2e483fe0b72a9d09d5945fe7e36e65),
[PartDesign::Groove::execute()](../../d7/de3/classPartDesign_1_1Groove.html#a0f3365a4df79cd6d9ec8137b32c9530c),
[PartDesign::Helix::execute()](../../d3/d78/classPartDesign_1_1Helix.html#a27fec701529ccafecb472fb49925b698),
[PartDesign::Hole::execute()](../../dd/dd0/classPartDesign_1_1Hole.html#ad3161d80bf31dc136534283281a5b3ad),
[PartDesign::Loft::execute()](../../d0/deb/classPartDesign_1_1Loft.html#a4b93c0b07d89ef905c488f2d0aeec258),
[PartDesign::Pipe::execute()](../../da/d61/classPartDesign_1_1Pipe.html#a860c1038a89156936a4d1fd44481cfbd),
[PartDesign::Cylinder::execute()](../../dc/d28/classPartDesign_1_1Cylinder.html#ab62f3f3e2d1c87dd9c4073378f2ca916),
[PartDesign::Sphere::execute()](../../db/d9d/classPartDesign_1_1Sphere.html#aeef6f98884ffd7532acd0274c29b1e8f),
[PartDesign::Cone::execute()](../../d4/d2b/classPartDesign_1_1Cone.html#a242c7c4d99e524f88ffca87982764ddf),
[PartDesign::Ellipsoid::execute()](../../d4/de1/classPartDesign_1_1Ellipsoid.html#abe018702f319a19bfd7faaba06b60109),
[PartDesign::Torus::execute()](../../dd/de1/classPartDesign_1_1Torus.html#a0fe8ad351f212fb151f6aab09438c4fd),
[PartDesign::Prism::execute()](../../d9/daf/classPartDesign_1_1Prism.html#afbe0d9e86e58c4781f3f58aed9371937),
[PartDesign::Wedge::execute()](../../dc/dd3/classPartDesign_1_1Wedge.html#aea929c12fd19cab20657b5dc80ced3ac),
[PartDesign::Revolution::execute()](../../d2/de6/classPartDesign_1_1Revolution.html#a1e5564f51ec710663a8002d5018b76f8),
[PartDesign::Thickness::execute()](../../d4/d22/classPartDesign_1_1Thickness.html#a773b84ae5c846c3cfc1c099ab47887da),
[PartDesign::Transformed::execute()](../../dd/de1/classPartDesign_1_1Transformed.html#aef9667071a3f6bb2ed13226f84629049),
[Path::Feature::execute()](../../d5/dd9/classPath_1_1Feature.html#a80d4fdf2e0a09f51601c94668dda3ca1),
[Path::FeatureCompound::execute()](../../d2/d43/classPath_1_1FeatureCompound.html#a0db05b4845d8e9cf2dc1ab83a02a875b),
[Path::FeatureShape::execute()](../../da/d9b/classPath_1_1FeatureShape.html#a62d47b3cb3d7ed9081cdfc0966c71c3e),
[Raytracing::LuxFeature::execute()](../../d1/d8f/classRaytracing_1_1LuxFeature.html#a235b146fb9255cb705a6b86fb6967c3d),
[Raytracing::LuxProject::execute()](../../d5/de6/classRaytracing_1_1LuxProject.html#aec1cca02194001c5b054810640a318f3),
[Raytracing::RayFeature::execute()](../../d4/df2/classRaytracing_1_1RayFeature.html#a0564ae7028e1436125a4f09181b6bd07),
[Raytracing::RayProject::execute()](../../d2/d89/classRaytracing_1_1RayProject.html#ab700f7555dda7afe67c930effe80bc33),
[Raytracing::RaySegment::execute()](../../d5/d48/classRaytracing_1_1RaySegment.html#ab940ed0d8627d391c3be83800c98698c),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[Robot::RobotObject::execute()](../../db/d51/classRobot_1_1RobotObject.html#a02d0871e02dcf31317ff7ef811980483),
[Robot::TrajectoryCompound::execute()](../../df/de7/classRobot_1_1TrajectoryCompound.html#a230683c181418d56d66a986fe5063a3a),
[Robot::TrajectoryDressUpObject::execute()](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a1b311e580c396667d0625866517497e0),
[Robot::TrajectoryObject::execute()](../../d7/db5/classRobot_1_1TrajectoryObject.html#ad727a9f54b00d87767a06e1aec3f9044),
[Sketcher::SketchObjectSF::execute()](../../de/da4/classSketcher_1_1SketchObjectSF.html#aee2e5bb2b2aa00817df40cae0574ef36),
[Surface::Filling::execute()](../../d8/df7/classSurface_1_1Filling.html#ab31cd9c2fd6bd4e15a80b7065c071eae),
[Surface::GeomFillSurface::execute()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a84b55d39b731f625753852ddf3672072),
[Surface::Sewing::execute()](../../d2/d52/classSurface_1_1Sewing.html#a956109125cae787085423aeb93d8e1f3),
[TechDraw::DrawParametricTemplate::execute()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#acc1380e0737504ec1d64b2bbca2380e6),
[TechDraw::DrawRichAnno::execute()](../../da/d5f/classTechDraw_1_1DrawRichAnno.html#a69829b351153268971271cd16fb5db52),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawViewClip::execute()](../../dd/de8/classTechDraw_1_1DrawViewClip.html#a31cd0c2306b266d607e29672b3825340),
[TechDraw::DrawViewCollection::execute()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#abd5332c355e8d23d52ba435c1ba3f855),
[TechDraw::DrawViewDimExtent::execute()](../../d9/d77/classTechDraw_1_1DrawViewDimExtent.html#ac856c6f8b2f5504087090cc122d82891),
[TechDraw::DrawWeldSymbol::execute()](../../dd/d15/classTechDraw_1_1DrawWeldSymbol.html#aa63b811c7325f38b1e58840b28d8ab7d),
[TechDraw::FeatureProjection::execute()](../../dd/ddc/classTechDraw_1_1FeatureProjection.html#a7c0a9490e884924ab967bbdd06bafecf),
[App::FeaturePythonT< FeatureT
>::execute()](../../d2/d2f/classApp_1_1FeaturePythonT.html#aff89f1dafffac9466b7f498c2fc00e4f),
[Part::Extrusion::execute()](../../db/d6c/classPart_1_1Extrusion.html#ab84ba0c7cd3edeec76deb2fda5303115),
[Part::Face::execute()](../../dc/dbf/classPart_1_1Face.html#a7e0c10e1928c118064cc40586322ca36),
[Part::Offset::execute()](../../d0/dda/classPart_1_1Offset.html#a342f29a6b5381db240304b9384b313dd),
[Part::Offset2D::execute()](../../d7/dcf/classPart_1_1Offset2D.html#a3eb29bb0e6404263cb3470d7ec24ea4a),
[Part::Revolution::execute()](../../d3/d17/classPart_1_1Revolution.html#a0406e2da5876bbf2351991c6b48b7185),
[PartDesign::Body::execute()](../../dd/db8/classPartDesign_1_1Body.html#a4abca6b2645adade81347d0e850a2659),
[PartDesign::Boolean::execute()](../../d2/d81/classPartDesign_1_1Boolean.html#a471715716cd89abfe18b9f50b7728567),
[PartDesign::Chamfer::execute()](../../da/d6f/classPartDesign_1_1Chamfer.html#a3fc5f1e2196c59afb44e876fd05d4710),
[Sketcher::SketchObject::execute()](../../d9/dad/classSketcher_1_1SketchObject.html#a06d72232cfde4ef56fd23515cf8434c4),
[Surface::Extend::execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[Surface::Sections::execute()](../../d7/d6e/classSurface_1_1Sections.html#a2c9525c3b5343d49da189cd26cd2ad4e),
[TechDraw::DrawGeomHatch::execute()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a8860cb23b43c1eb064578e2f50614c05),
[TechDraw::DrawHatch::execute()](../../d0/d97/classTechDraw_1_1DrawHatch.html#abc909fae985f572927d821cfb03bd3ee),
[TechDraw::DrawLeaderLine::execute()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#ab5f621c70c32624c24f354f23fb2e5c3),
[TechDraw::DrawProjGroup::execute()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a53036ad3632d51fe082b67c8f829b54f),
[TechDraw::DrawProjGroupItem::execute()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1afd35db151cf4ec222427f08a4f3c2a),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewDimension::execute()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a385455a827c3e7363329a86b8b63f555),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawViewMulti::execute()](../../d1/d80/classTechDraw_1_1DrawViewMulti.html#a9d04a96ccac9fad6d125e478b91b7f30),
[TechDraw::DrawViewPart::execute()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a1fcf644b19e25ef630eb6cc384e699ec),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[TechDraw::DrawViewSymbol::execute()](../../d3/d02/classTechDraw_1_1DrawViewSymbol.html#a44eea88d3e8522c41e9dcee9acff10ce),
[TechDraw::LandmarkDimension::execute()](../../d8/d4f/classTechDraw_1_1LandmarkDimension.html#a628476bf5d4492109e6d1e947c15aa6d),
and
[App::DocumentObjectExtension::extensionExecute()](../../d4/d81/classApp_1_1DocumentObjectExtension.html#aa8a99ad96497244412b31eb8cfd4079e).

## ◆ Visibility

[PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html)
App::DocumentObject::Visibility  
---  
  
Allow control visibility status in [App](../../dd/dc2/namespaceApp.html "The
FreeCAD Application layer.") name space.

Referenced by
[PartDesign::Body::addObject()](../../dd/db8/classPartDesign_1_1Body.html#a93c6ad704fcbbcb94f31586ad293f605),
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[ReverseEngineeringGui::SegmentationManual::createSegment()](../../dc/d04/classReverseEngineeringGui_1_1SegmentationManual.html#a95ac22eb241f58d992ffe08f784eb5d0),
[PartDesignGui::TaskDressUpParameters::hideObject()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#af899ee96527f085fc3568e108714caba),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[Gui::ViewProviderDocumentObject::show()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae42de285d193c43881fa6019b902fec1),
and
[PartDesignGui::TaskDressUpParameters::showObject()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a8de298ef5f0b2f224b75f7a8a3f806ee).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObject.h
  * FreeCAD/src/App/DocumentObject.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

