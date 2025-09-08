---
url: https://freecad.github.io/SourceDoc/d1/dc6/classApp_1_1DocumentObjectFileIncluded.html
scraped_at: 2025-09-08T14:54:20.443187
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentObjectFileIncluded](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html)

[List of all members](../../de/d5a/classApp_1_1DocumentObjectFileIncluded-members.html) | Public Member Functions | Public Attributes

App::DocumentObjectFileIncluded Class Reference

`#include <DocumentObjectFileIncluded.h>`

##  Public Member Functions  
  
---  
|
[DocumentObjectFileIncluded](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a14ee9c7ef68f9fdcfc07a24cfddce5db)
(void)  
| Constructor.
[More...](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a14ee9c7ef68f9fdcfc07a24cfddce5db)  
  
virtual const char * | [getViewProviderName](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a91002a42b9fddea0055e72f19a234362) (void) const  
| returns the type name of the ViewProvider
[More...](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a91002a42b9fddea0055e72f19a234362)  
  
virtual | [~DocumentObjectFileIncluded](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a7830f5fa4ff9933ab97c16a69f9aa0b2) ()  
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
  
  
##  Public Attributes  
  
---  
[PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html) | [File](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a15006a6f39c1b3eefec482fae0cd0093)  
| Properties.
[More...](../../d1/dc6/classApp_1_1DocumentObjectFileIncluded.html#a15006a6f39c1b3eefec482fae0cd0093)  
  
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
  
## Constructor & Destructor Documentation

## ◆ DocumentObjectFileIncluded()

DocumentObjectFileIncluded::DocumentObjectFileIncluded  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Constructor.

References
[App::Prop_None](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a32c18d11cda25e1ac1b1692aa36423e0).

## ◆ ~DocumentObjectFileIncluded()

| DocumentObjectFileIncluded::~DocumentObjectFileIncluded  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ getViewProviderName()

| virtual const char * App::DocumentObjectFileIncluded::getViewProviderName  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
returns the type name of the ViewProvider

Reimplemented from
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a6a8a0335a6da079225b433b4b291653a).

## Member Data Documentation

## ◆ File

[PropertyFileIncluded](../../d2/db3/classApp_1_1PropertyFileIncluded.html)
App::DocumentObjectFileIncluded::File  
---  
  
Properties.

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObjectFileIncluded.h
  * FreeCAD/src/App/DocumentObjectFileIncluded.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

