---
url: https://freecad.github.io/SourceDoc/dd/d13/classApp_1_1ObjectIdentifier.html
scraped_at: 2025-09-08T14:55:10.757483
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)

[List of all members](../../da/d4f/classApp_1_1ObjectIdentifier-members.html) | Classes | Public Types | Public Member Functions | Static Public Member Functions | Protected Member Functions | Static Protected Member Functions | Protected Attributes | Friends

App::ObjectIdentifier Class Reference

`#include <ObjectIdentifier.h>`

##  Classes  
  
---  
class | [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html)  
| A component is a part of a [Path](../../da/d2a/classApp_1_1Path.html "Base
class of all geometric document objects.") object, and is used to either name
a property or a field within a property.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#details)  
  
class | [DocumentMapper](../../de/d7a/classApp_1_1ObjectIdentifier_1_1DocumentMapper.html)  
struct | [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html)  
class | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)  
  
##  Public Types  
  
---  
typedef std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::set< std::string > > | [Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55)  
| Type for storing dependency of an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html).
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55)  
  
typedef std::map< std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::string >, std::string > | [SubNameMap](../../dd/d13/classApp_1_1ObjectIdentifier.html#af60f586ff5580cd84c3d6828bdc3a767)  
  
##  Public Member Functions  
  
---  
void | [addComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#ac9f36b9763a88ccb797bfa63b90635b7) ([Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &&c)  
void | [addComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#addb31e2d6808d0c9813abb25957d0112) (const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &c)  
template<typename C >  
void | [addComponents](../../dd/d13/classApp_1_1ObjectIdentifier.html#a7a10bc189326fc75d36f372fcb739566) (const C &cs)  
[bool](../../d9/db9/classbool.html) | [adjustLinks](../../dd/d13/classApp_1_1ObjectIdentifier.html#a64e384b81e6d7f8de55251a498467604) ([ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) &v, const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList)  
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [canonicalPath](../../dd/d13/classApp_1_1ObjectIdentifier.html#a7ef3ed6173cdd2276e28d4de038c1501) () const  
| Create a canonical representation of an object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a7ef3ed6173cdd2276e28d4de038c1501)  
  
|
[FC_DEFAULT_CTORS](../../dd/d13/classApp_1_1ObjectIdentifier.html#a0251f583f4962e4da5b5db149200cc19)
([ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html))  
const std::vector< [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) > & | [getComponents](../../dd/d13/classApp_1_1ObjectIdentifier.html#a351acdb5fb17960972de6136186b352e) () const  
[Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55) | [getDep](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948) ([bool](../../d9/db9/classbool.html) needProps, std::vector< std::string > *labels=nullptr) const  
| Get dependencies of this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948)  
  
void | [getDep](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8f202b77bf40dda04af2d959edecfe76) ([Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55) &deps, [bool](../../d9/db9/classbool.html) needProps, std::vector< std::string > *labels=nullptr) const  
| Get dependencies of this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8f202b77bf40dda04af2d959edecfe76)  
  
void | [getDepLabels](../../dd/d13/classApp_1_1ObjectIdentifier.html#af1194cb10949e17069375abd40d4b2bd) (std::vector< std::string > &labels) const  
| Returns all label references.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#af1194cb10949e17069375abd40d4b2bd)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) name=[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)(), [bool](../../d9/db9/classbool.html) *ambiguous=nullptr) const  
| Find a document with the given name.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f)  
  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [getDocumentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2c382cbc105126bf6b29e8b3b20bf7d3) () const  
| Get the document name from this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2c382cbc105126bf6b29e8b3b20bf7d3)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getDocumentObject](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff) () const  
| Get the document object for the object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff)  
  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [getDocumentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab65df17d00afe3649702ff6fefbe6e88) () const  
| Get the document object name.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab65df17d00afe3649702ff6fefbe6e88)  
  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getOwner](../../dd/d13/classApp_1_1ObjectIdentifier.html#aaa2484f61d4ccb57e20f6f55a283c730) () const  
[App::Property](../../d0/da9/classApp_1_1Property.html) * | [getProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#afc4aaa90cb65a96c83fd931134d26b24) ([int](../../d1/da0/classint.html) *ptype=nullptr) const  
| Get pointer to property pointed to by this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#afc4aaa90cb65a96c83fd931134d26b24)  
  
const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | [getPropertyComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#a3c92b7f5390faf85819e9ebaa7fba28c) ([int](../../d1/da0/classint.html) i, [int](../../d1/da0/classint.html) *idx=nullptr) const  
| Get [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html
"A component is a part of a Path object, and is used to either name a property
or a field within a pro...") at given index _i_.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a3c92b7f5390faf85819e9ebaa7fba28c)  
  
std::vector< [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) > | [getPropertyComponents](../../dd/d13/classApp_1_1ObjectIdentifier.html#a57264281085e983af84c5dbbfd5871e0) () const  
std::string | [getPropertyName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a60c3187087da6b2e8dd1c31e0512b591) () const  
| Get the name of the property.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a60c3187087da6b2e8dd1c31e0512b591)  
  
Py::Object | [getPyValue](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6) ([bool](../../d9/db9/classbool.html) pathValue=false, [bool](../../d9/db9/classbool.html) *isPseudoProperty=nullptr) const  
std::vector< std::string > | [getStringList](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7) () const  
| Get components as a string list.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7)  
  
const std::string & | [getSubObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae1511c1071d655b2a7be6cb811c5c4df) () const  
const std::string & | [getSubObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1111706c4bc3efd238f0066c4226421b) ([bool](../../d9/db9/classbool.html) newStyle) const  
std::string | [getSubPathStr](../../dd/d13/classApp_1_1ObjectIdentifier.html#afb76b19861a0da703aa6f869a0489931) ([bool](../../d9/db9/classbool.html) toPython=false) const  
[App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3) | [getValue](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c) ([bool](../../d9/db9/classbool.html) pathValue=false, [bool](../../d9/db9/classbool.html) *isPseudoProperty=nullptr) const  
| Get the value of the property or field pointed to by this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c)  
  
[bool](../../d9/db9/classbool.html) | [hasDocumentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a58b1475c362d8f38085e711911d2fb4e) ([bool](../../d9/db9/classbool.html) forced=false) const  
std::size_t | [hash](../../dd/d13/classApp_1_1ObjectIdentifier.html#a420e7ae702cc2d90b62fe15296980240) () const  
void | [importSubNames](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954) (const [SubNameMap](../../dd/d13/classApp_1_1ObjectIdentifier.html#af60f586ff5580cd84c3d6828bdc3a767) &subNameMap)  
[bool](../../d9/db9/classbool.html) | [isLocalProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8e6815f2e1c9bde7e770ff6f2c607277) () const  
[bool](../../d9/db9/classbool.html) | [isTouched](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14e3f2b6fbb8fbe073435a5d4830fe13) () const  
[int](../../d1/da0/classint.html) | [numComponents](../../dd/d13/classApp_1_1ObjectIdentifier.html#a69faa77214fd1a0648d2344e0f3dc286) () const  
| Return number of components.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a69faa77214fd1a0648d2344e0f3dc286)  
  
[int](../../d1/da0/classint.html) | [numSubComponents](../../dd/d13/classApp_1_1ObjectIdentifier.html#a39d5ce75322b21ac13111ff64912aa78) () const  
| Compute number of sub components, i.e excluding the property.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a39d5ce75322b21ac13111ff64912aa78)  
  
|
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2e87192f46ed457637f2b2d05abd01b7)
(const [App::Property](../../d0/da9/classApp_1_1Property.html) &prop,
[int](../../d1/da0/classint.html) index=INT_MAX)  
| Construct an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) object
given a property.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2e87192f46ed457637f2b2d05abd01b7)  
  
|
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html#aca0e583bf40fbbb5fa97a4a8c5fb6c05)
(const
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)
*_owner, [bool](../../d9/db9/classbool.html)
[localProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#af97eefc24e711f575f3af520fd6b433b))  
|
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651)
(const
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)
*_owner=nullptr, const std::string &property=std::string(),
[int](../../d1/da0/classint.html) index=INT_MAX)  
| Construct an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) object,
given an owner and a single-value property.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651)  
  
[bool](../../d9/db9/classbool.html) | [operator!=](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad5fda0eea299bc6717f2bf7076b6f132) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &other) const  
| Compare object identifier with _other_.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad5fda0eea299bc6717f2bf7076b6f132)  
  
[bool](../../d9/db9/classbool.html) | [operator<](../../dd/d13/classApp_1_1ObjectIdentifier.html#a5d31da8fcdb3a26ebcc4028bac6fe8df) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &other) const  
| Compare object identifier with other.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a5d31da8fcdb3a26ebcc4028bac6fe8df)  
  
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | [operator<<](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae4dc019b4c1ee75d7dd83a6265850d85) ([Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &&value)  
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | [operator<<](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad6467dd03d63cab9e3b068e5f9e9e4a0) (const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &value)  
| << operator, used to add a component to the object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad6467dd03d63cab9e3b068e5f9e9e4a0)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe9fa06dbf743b6233b55a11a280e349) (const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &other) const  
| Compare object identifier with _other_.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe9fa06dbf743b6233b55a11a280e349)  
  
[bool](../../d9/db9/classbool.html) | [relabeledDocument](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab762f0b511088f1aad35a265a16bf5bc) ([ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) &v, const std::string &oldLabel, const std::string &newLabel)  
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [relativeTo](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &other) const  
| Construct the simplest possible object identifier relative to another.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad)  
  
[bool](../../d9/db9/classbool.html) | [replaceObject](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f) ([ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &res, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const  
void | [resolveAmbiguity](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f) ()  
std::string | [resolveErrorString](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad22feac2744b1bebc12711be503cf2a4) () const  
void | [setComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#a470c9df4f63a6d9ddad2d71ce7affa25) ([int](../../d1/da0/classint.html) idx, [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &&comp)  
void | [setComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#ac1f3e1b26fe391d68c6561dbf3373736) ([int](../../d1/da0/classint.html) idx, const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &comp)  
void | [setDocumentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&name, [bool](../../d9/db9/classbool.html) force=false)  
| Set the document name for this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0)  
  
void | [setDocumentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) force=false, [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&subname=[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)(), [bool](../../d9/db9/classbool.html) checkImport=false)  
void | [setDocumentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&name, [bool](../../d9/db9/classbool.html) force=false, [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&subname=[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)(), [bool](../../d9/db9/classbool.html) checkImport=false)  
| Set the document object name of this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2)  
  
void | [setValue](../../dd/d13/classApp_1_1ObjectIdentifier.html#a208a7e99d236e98ca3e6165ce858480b) (const [App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3) &value) const  
| Set value of a property or field pointed to by this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a208a7e99d236e98ca3e6165ce858480b)  
  
std::string | [toEscapedString](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9c8aaa7cfadced7f02366ca502c53029) () const  
| Escape toString representation so it is suitable for being embedded in a
python command.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9c8aaa7cfadced7f02366ca502c53029)  
  
std::string | [toPersistentString](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f) () const  
const std::string & | [toString](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6) () const  
| Create a string representation of this object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6)  
  
[bool](../../d9/db9/classbool.html) | [updateElementReference](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab8fdf8392daa0dbc35aed2e2d9e90fc3) ([ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) &v, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature=nullptr, [bool](../../d9/db9/classbool.html) reverse=false)  
[bool](../../d9/db9/classbool.html) | [updateLabelReference](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const std::string &, const char *)  
[bool](../../d9/db9/classbool.html) | [verify](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae666a62d2fc3b423b86f3d370e6edb11) (const [App::Property](../../d0/da9/classApp_1_1Property.html) &prop, [bool](../../d9/db9/classbool.html) silent=false) const  
virtual | [~ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html#a3131e7c17208673fb8fe08acaff47797) ()  
  
##  Static Public Member Functions  
  
---  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [ArrayComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#a13e4caad9b9cbb9bd8aa45079e8896a4) ([int](../../d1/da0/classint.html) _index)  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [MapComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae95e6b1cd5b6d31abe8c46ad38a23f4d) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &_key)  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [MapComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#a90b99eaa77107ca2d06ce705a98addcb) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&_key)  
static [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [parse](../../dd/d13/classApp_1_1ObjectIdentifier.html#a067a142eca99580ead933730b95a075b) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *docObj, const std::string &[str](../../d9/d36/classstr.html))  
| Parse a string to create an object identifier.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a067a142eca99580ead933730b95a075b)  
  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [RangeComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#ac4a5968e4f45d718d0d8b5a75895ca62) ([int](../../d1/da0/classint.html) _begin, [int](../../d1/da0/classint.html) _end=INT_MAX, [int](../../d1/da0/classint.html) _step=1)  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [SimpleComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14c7ec6dc691f2c26f6df8386bd9db6d) (const char *_component)  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [SimpleComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#abf03db701f23f35623702c24a1a64915) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &_component)  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [SimpleComponent](../../dd/d13/classApp_1_1ObjectIdentifier.html#a771b13f5d53fb64d967b57d27bfb718d) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&_component)  
  
##  Protected Member Functions  
  
---  
Py::Object | [access](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb) (const [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) &rs, Py::Object *value=nullptr, [Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55) *deps=nullptr) const  
void | [getDepLabels](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2d8af8b84a0c426af896a2f190b692ce) (const [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) &result, std::vector< std::string > &labels) const  
void | [getSubPathStr](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae2af93c3127cefab102ecc2ed4330b57) (std::ostream &ss, const [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) &result, [bool](../../d9/db9/classbool.html) toPython=false) const  
| Get sub field part of a property as a string.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#ae2af93c3127cefab102ecc2ed4330b57)  
  
void | [resolve](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed) ([ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) &results) const  
| Resolve the object identifier to a concrete document, documentobject, and
property.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed)  
  
void | [resolveAmbiguity](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4503f7d6916abae555ddb15db1eed9ea) ([ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) &results)  
[App::Property](../../d0/da9/classApp_1_1Property.html) * | [resolveProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *propertyName, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *&sobj, [int](../../d1/da0/classint.html) &ptype) const  
  
##  Static Protected Member Functions  
  
---  
static [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getDocumentObject](../../dd/d13/classApp_1_1ObjectIdentifier.html#aafad5ca7c030567c9182b359b2eb5872) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc, const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &name, std::bitset< 32 > &flags)  
| Search for the document object given by name in doc.
[More...](../../dd/d13/classApp_1_1ObjectIdentifier.html#aafad5ca7c030567c9182b359b2eb5872)  
  
  
##  Protected Attributes  
  
---  
std::vector< [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) > | [components](../../dd/d13/classApp_1_1ObjectIdentifier.html#a0729c0985816f57435610cad91f94986)  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2)  
[bool](../../d9/db9/classbool.html) | [documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf)  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c)  
[bool](../../d9/db9/classbool.html) | [documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c)  
[bool](../../d9/db9/classbool.html) | [localProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#af97eefc24e711f575f3af520fd6b433b)  
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090)  
std::pair< std::string, std::string > | [shadowSub](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad9f06332942ff16a8b4a56132a9f5dba)  
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36)  
  
##  Friends  
  
---  
struct | [ResolveResults](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2fe14749b482d4b63926355692f9deaa)  
  
## Member Typedef Documentation

## ◆ Dependencies

typedef
std::map<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)
*, std::set<std::string> >
[App::ObjectIdentifier::Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55)  
---  
  
Type for storing dependency of an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html).

The dependency is a map from document object to a set of property names. An
object identifier may references multiple objects using syntax like
'[Part.Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb
"Properties.")[0].Width'.

Also, we use set of string instead of set of
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") pointer, because the
property may not exist at the time this
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) is
constructed.

## ◆ SubNameMap

typedef
std::map<std::pair<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*,std::string>,std::string>
[App::ObjectIdentifier::SubNameMap](../../dd/d13/classApp_1_1ObjectIdentifier.html#af60f586ff5580cd84c3d6828bdc3a767)  
---  
  
## Constructor & Destructor Documentation

## ◆ ObjectIdentifier() [1/3]

ObjectIdentifier::ObjectIdentifier  | ( | const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *  | __owner_ = `nullptr`,   
---|---|---|---  
|  | const std::string & | _property_ = `std::string()`,   
|  | [int](../../d1/da0/classint.html) | _index_ = `INT_MAX`  
| ) | |   
  
Construct an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) object,
given an owner and a single-value property.

Parameters

     _owner| Owner of property.   
---|---  
property| Name of property.  
  
References
[addComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#addb31e2d6808d0c9813abb25957d0112),
[ArrayComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a13e4caad9b9cbb9bd8aa45079e8896a4),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
and
[SimpleComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14c7ec6dc691f2c26f6df8386bd9db6d).

## ◆ ObjectIdentifier() [2/3]

ObjectIdentifier::ObjectIdentifier  | ( | const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *  | __owner_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _localProperty_  
| ) | |   
  
References
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090).

## ◆ ObjectIdentifier() [3/3]

ObjectIdentifier::ObjectIdentifier  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _index_ = `INT_MAX`  
| ) | |   
  
Construct an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) object
given a property.

The property is assumed to be single-valued.

Parameters

     prop| [Property](../../d0/da9/classApp_1_1Property.html "Base class of all properties This is the father of all properties.") to construct object identifier for.   
---|---  
  
References
[addComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#addb31e2d6808d0c9813abb25957d0112),
[ArrayComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a13e4caad9b9cbb9bd8aa45079e8896a4),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[App::Property::hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
and
[SimpleComponent()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a14c7ec6dc691f2c26f6df8386bd9db6d).

## ◆ ~ObjectIdentifier()

| virtual App::ObjectIdentifier::~ObjectIdentifier  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ access()

| Py::Object ObjectIdentifier::access  | ( | const [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) & | _rs_ ,   
---|---|---|---  
|  | Py::Object *  | _value_ = `nullptr`,   
|  | [Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55) *  | _deps_ = `nullptr`  
| ) | |  const  
protected  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

Referenced by
[getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8f202b77bf40dda04af2d959edecfe76),
[getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
and
[setValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a208a7e99d236e98ca3e6165ce858480b).

## ◆ addComponent() [1/2]

void App::ObjectIdentifier::addComponent  | ( | [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) && | _c_| ) |   
---|---|---|---|---|---  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ addComponent() [2/2]

void App::ObjectIdentifier::addComponent  | ( | const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | _c_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651).

## ◆ addComponents()

template<typename C >

void App::ObjectIdentifier::addComponents  | ( | const C & | _cs_| ) |   
---|---|---|---|---|---  
  
## ◆ adjustLinks()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::adjustLinks  | ( | [ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) & | _v_ ,   
---|---|---|---  
|  | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_  
| ) | |   
  
References
[App::PropertyLinkSub::adjustLink()](../../d3/d76/classApp_1_1PropertyLinkSub.html#ac5e4b8833d9c02383d6ce017ca6a7730),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::PropertyLinkSub::getSubValues()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a0777851ecd0b74f3fd232e6c69c7cb32),
[App::PropertyLinkSub::getValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#af444cc21b2476f99a94fa2e982c4ae86),
[App::PropertyLinkSub::setValue()](../../d3/d76/classApp_1_1PropertyLinkSub.html#a448d3ecccc89f3da177ecd35eb92b248),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ ArrayComponent()

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::ArrayComponent  | ( | [int](../../d1/da0/classint.html) | __index_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::VariableExpression::addComponent()](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0),
and
[ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651).

## ◆ canonicalPath()

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) ObjectIdentifier::canonicalPath  | ( | | ) |  const  
---|---|---|---|---  
  
Create a canonical representation of an object identifier.

The main work is actually done by the property's virtual canonicalPath(...)
method, which is invoked by this call.

Returns

    A new object identifier. 

References
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090).

## ◆ FC_DEFAULT_CTORS()

App::ObjectIdentifier::FC_DEFAULT_CTORS  | ( | [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | | ) |   
---|---|---|---|---|---  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ getComponents()

const std::vector< [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) > & App::ObjectIdentifier::getComponents  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getDep() [1/2]

[ObjectIdentifier::Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55) ObjectIdentifier::getDep  | ( | [bool](../../d9/db9/classbool.html) | _needProps_ ,   
---|---|---|---  
|  | std::vector< std::string > *  | _labels_ = `nullptr`  
| ) | |  const  
  
Get dependencies of this object identifier.

Parameters

     needProps| whether need property dependencies.   
---|---  
labels| optional return of any label references.  
  
In case of multi-object references, like
'[Part.Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb
"Properties.")[0].Width', if no property dependency is required, then this
function will only return the first referred object dependency. Or else, all
object and property dependencies will be returned.

References
[getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948).

Referenced by
[getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948),
[App::Expression::getDepObjects()](../../dc/d5c/classApp_1_1Expression.html#a1eac6a293066f71fa91fcd7d3915e5d2),
[App::Expression::getDeps()](../../dc/d5c/classApp_1_1Expression.html#aaf7a179b1fd47392d7284d7c89fae870),
and
[App::PropertyExpressionEngine::hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723).

## ◆ getDep() [2/2]

void ObjectIdentifier::getDep  | ( | [Dependencies](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6a25b42a5b3ed8b66c64c3034d6c5a55) & | _deps_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _needProps_ ,   
|  | std::vector< std::string > *  | _labels_ = `nullptr`  
| ) | |  const  
  
Get dependencies of this object identifier.

Parameters

     deps| returns the dependencies.   
---|---  
needProps| whether need property dependencies.  
labels| optional return of any label references.  
  
In case of multi-object references, like
'[Part.Group](../../da/d3a/classApp_1_1GroupExtension.html#a2ce49160a2d81ffd6aa6c181144e2ceb
"Properties.")[0].Width', if no property dependency is required, then this
function will only return the first referred object dependency. Or else, all
object and property dependencies will be returned.

References
[access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
and
[getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af1194cb10949e17069375abd40d4b2bd).

## ◆ getDepLabels() [1/2]

| void ObjectIdentifier::getDepLabels  | ( | const [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) & | _result_ ,   
---|---|---|---  
|  | std::vector< std::string > & | _labels_  
| ) | |  const  
protected  
  
References
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[App::PropertyLinkBase::getLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ getDepLabels() [2/2]

void ObjectIdentifier::getDepLabels  | ( | std::vector< std::string > & | _labels_| ) |  const  
---|---|---|---|---|---  
  
Returns all label references.

References
[getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af1194cb10949e17069375abd40d4b2bd),
and
[ResolveResults](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2fe14749b482d4b63926355692f9deaa).

Referenced by
[getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8f202b77bf40dda04af2d959edecfe76),
and
[getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af1194cb10949e17069375abd40d4b2bd).

## ◆ getDocument()

[Document](../../d8/d3e/classApp_1_1Document.html) * ObjectIdentifier::getDocument  | ( | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | _name_ = `[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)()`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) *  | _ambiguous_ = `nullptr`  
| ) | |  const  
  
Find a document with the given name.

Parameters

     name| Name of document   
---|---  
  
Returns

    Pointer to document, or 0 if it is not found or not uniquely defined by name. 

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Application::getDocument()](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d),
[getDocumentName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2c382cbc105126bf6b29e8b3b20bf7d3),
and
[App::Application::getDocuments()](../../da/dbf/classApp_1_1Application.html#a955aad8188b482bb46f74a46b1946e3a).

Referenced by
[getDocumentObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff),
and
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ getDocumentName()

[ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) ObjectIdentifier::getDocumentName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document name from this object identifier.

Returns

    [Document](../../d8/d3e/classApp_1_1Document.html "The document class.") name as a [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) object. 

Referenced by
[getDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f).

## ◆ getDocumentObject() [1/2]

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * ObjectIdentifier::getDocumentObject  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document object for the object identifier.

Returns

    Pointer to document object, or 0 if not found or uniquely defined. 

References
[getDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f),
and
[getDocumentObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff).

Referenced by
[Gui::InputField::bind()](../../da/dfa/classGui_1_1InputField.html#a17038da6cfd54acfc8f86b6597edb8a4),
[App::ObjectIdentifier::String::checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f),
[SpreadsheetGui::DlgBindSheet::DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[getDocumentObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff),
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
and
[App::PropertyExpressionEngine::validateExpression()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa259d698d63c151f459f14483346639a).

## ◆ getDocumentObject() [2/2]

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * ObjectIdentifier::getDocumentObject  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ ,   
---|---|---|---  
|  | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | _name_ ,   
|  | std::bitset< 32 > & | _flags_  
| ) | |   
staticprotected  
  
Search for the document object given by name in doc.

Name might be the internal name or a label. In any case, it must uniquely
define the document object.

Parameters

     doc| [Document](../../d8/d3e/classApp_1_1Document.html "The document class.") to search   
---|---  
name| Name to search for.  
  
Returns

    Pointer to document object if a unique pointer is found, 0 otherwise. 

## ◆ getDocumentObjectName()

[ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) ObjectIdentifier::getDocumentObjectName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document object name.

Returns

    [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) with name of document object as resolved by object identifier. 

Referenced by
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4).

## ◆ getOwner()

[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * App::ObjectIdentifier::getOwner  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad).

## ◆ getProperty()

[Property](../../d0/da9/classApp_1_1Property.html) * ObjectIdentifier::getProperty  | ( | [int](../../d1/da0/classint.html) *  | _ptype_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
Get pointer to property pointed to by this object identifier.

Returns

    [Point](../../dc/d4f/classPoint.html) to property if it is uniquely defined, or 0 otherwise. 

Referenced by
[Gui::ExpressionBinding::bind()](../../dc/d5a/classGui_1_1ExpressionBinding.html#aba7b2c918c04b6e3f589e53876cdb761),
[App::VariableExpression::getProperty()](../../df/d0f/classApp_1_1VariableExpression.html#a8211f23466f283ea3c5e4a149e904c34),
and
[App::PropertyExpressionEngine::setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1).

## ◆ getPropertyComponent()

const [App::ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & App::ObjectIdentifier::getPropertyComponent  | ( | [int](../../d1/da0/classint.html) | _i_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) *  | _idx_ = `nullptr`  
| ) | |  const  
  
Get [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A
component is a part of a Path object, and is used to either name a property or
a field within a pro...") at given index _i_.

Parameters

     i| Index to get   
---|---  
idx| optional return of adjusted component index  
  
Returns

    A component. 

## ◆ getPropertyComponents()

std::vector< [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) > ObjectIdentifier::getPropertyComponents  | ( | | ) |  const  
---|---|---|---|---  
  
References
[components](../../dd/d13/classApp_1_1ObjectIdentifier.html#a0729c0985816f57435610cad91f94986),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
and
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b).

## ◆ getPropertyName()

std::string App::ObjectIdentifier::getPropertyName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the name of the property.

Returns

    Name 

## ◆ getPyValue()

Py::Object ObjectIdentifier::getPyValue  | ( | [bool](../../d9/db9/classbool.html) | _pathValue_ = `false`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) *  | _isPseudoProperty_ = `nullptr`  
| ) | |  const  
  
References
[access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[App::Property::getPyPathValue()](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1),
[isLocalProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8e6815f2e1c9bde7e770ff6f2c607277),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[App::ObjectIdentifier::ResolveResults::propertyIndex](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a068329372c72559cc628c71c4b6e1035),
[App::ObjectIdentifier::ResolveResults::propertyType](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a4a562c0f1a5d62d4e4eacc75d8fde46f),
[App::ObjectIdentifier::ResolveResults::resolvedProperty](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aed491da2fa165a239384e218f652f500),
and
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ getStringList()

std::vector< std::string > ObjectIdentifier::getStringList  | ( | | ) |  const  
---|---|---|---|---  
  
Get components as a string list.

Returns

    List of strings. 

References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[App::ObjectIdentifier::String::toString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f).

## ◆ getSubObjectName() [1/2]

const std::string & ObjectIdentifier::getSubObjectName  | ( | | ) |  const  
---|---|---|---|---  
  
References
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ getSubObjectName() [2/2]

const std::string & ObjectIdentifier::getSubObjectName  | ( | [bool](../../d9/db9/classbool.html) | _newStyle_| ) |  const  
---|---|---|---|---|---  
  
References
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[shadowSub](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad9f06332942ff16a8b4a56132a9f5dba),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ getSubPathStr() [1/2]

std::string ObjectIdentifier::getSubPathStr  | ( | [bool](../../d9/db9/classbool.html) | _toPython_ = `false`| ) |  const  
---|---|---|---|---|---  
  
References
[getSubPathStr()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afb76b19861a0da703aa6f869a0489931),
and
[ResolveResults](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2fe14749b482d4b63926355692f9deaa).

Referenced by
[getSubPathStr()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afb76b19861a0da703aa6f869a0489931),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ getSubPathStr() [2/2]

| void ObjectIdentifier::getSubPathStr  | ( | std::ostream & | _s_ ,   
---|---|---|---  
|  | const [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) & | _result_ ,   
|  | [bool](../../d9/db9/classbool.html) | _toPython_ = `false`  
| ) | |  const  
protected  
  
Get sub field part of a property as a string.

Returns

    [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) representation of path. 

## ◆ getValue()

[App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3) ObjectIdentifier::getValue  | ( | [bool](../../d9/db9/classbool.html) | _pathValue_ = `false`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) *  | _isPseudoProperty_ = `nullptr`  
| ) | |  const  
  
Get the value of the property or field pointed to by this object identifier.

All type of objects are supported. Some types are casted to FC native type,
including: Int, Float,
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html), Unicode
[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html), and
Quantities. Others are just kept as Python object wrapped by
[App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3).

Parameters

     pathValue| if true, calls the property's getPathValue(), which is necessary for Qunatities to work.  
---|---  
  
Returns

    The value of the property or field. 

References
[access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[App::Property::getPathValue()](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea),
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[isLocalProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8e6815f2e1c9bde7e770ff6f2c607277),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[App::ObjectIdentifier::ResolveResults::propertyIndex](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a068329372c72559cc628c71c4b6e1035),
[App::ObjectIdentifier::ResolveResults::propertyType](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a4a562c0f1a5d62d4e4eacc75d8fde46f),
[App::pyObjectToAny()](../../dd/dc2/namespaceApp.html#ac51cca1568f7ffd55146499492ae1700),
[App::ObjectIdentifier::ResolveResults::resolvedProperty](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aed491da2fa165a239384e218f652f500),
and
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ hasDocumentObjectName()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::hasDocumentObjectName  | ( | [bool](../../d9/db9/classbool.html) | _forced_ = `false`| ) |  const  
---|---|---|---|---|---  
  
References
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
and
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b).

## ◆ hash()

std::size_t ObjectIdentifier::hash  | ( | | ) |  const  
---|---|---|---|---  
  
References
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ importSubNames()

void ObjectIdentifier::importSubNames  | ( | const [SubNameMap](../../dd/d13/classApp_1_1ObjectIdentifier.html#af60f586ff5580cd84c3d6828bdc3a767) & | _subNameMap_| ) |   
---|---|---|---|---|---  
  
References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[shadowSub](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad9f06332942ff16a8b4a56132a9f5dba),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ isLocalProperty()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::isLocalProperty  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
and
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f).

## ◆ isTouched()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::VariableExpression::isTouched()](../../df/d0f/classApp_1_1VariableExpression.html#a30d24a5ccb5a517237ddba1477458080).

## ◆ MapComponent() [1/2]

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::MapComponent  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | __key_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::VariableExpression::addComponent()](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0).

## ◆ MapComponent() [2/2]

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::MapComponent  | ( | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | __key_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ numComponents()

[int](../../d1/da0/classint.html) ObjectIdentifier::numComponents  | ( | | ) |  const  
---|---|---|---|---  
  
Return number of components.

Returns

    Number of components in this identifier. 

## ◆ numSubComponents()

[int](../../d1/da0/classint.html) ObjectIdentifier::numSubComponents  | ( | | ) |  const  
---|---|---|---|---  
  
Compute number of sub components, i.e excluding the property.

Returns

    Number of components. 

## ◆ operator!=()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::operator!=  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Compare object identifier with _other_.

Parameters

     other| Other object identifier   
---|---  
  
Returns

    true if they differ from each other. 

## ◆ operator<()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::operator< | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Compare object identifier with other.

Parameters

     other| Other object identifier.   
---|---  
  
Returns

    true if this object is less than the other. 

References
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ operator<<() [1/2]

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & ObjectIdentifier::operator<< | ( | [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) && | _value_| ) |   
---|---|---|---|---|---  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ operator<<() [2/2]

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & ObjectIdentifier::operator<< | ( | const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | _value_| ) |   
---|---|---|---|---|---  
  
<< operator, used to add a component to the object identifier.

Parameters

     value| [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A component is a part of a Path object, and is used to either name a property or a field within a pro...") object   
---|---  
  
Returns

    Reference to itself. 

## ◆ operator==()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::operator==  | ( | const [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Compare object identifier with _other_.

Parameters

     other| Other object identifier.   
---|---  
  
Returns

    true if they are equal. 

References
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ parse()

| [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) ObjectIdentifier::parse  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _docObj_ ,   
---|---|---|---  
|  | const std::string & | _str_  
| ) | |   
static  
  
Parse a string to create an object identifier.

This method throws an exception if the string is invalid.

Parameters

     docObj| [Document](../../d8/d3e/classApp_1_1Document.html "The document class.") object that will own this object identifier.   
---|---  
str| [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) to
parse  
  
Returns

    A new object identifier. 

References
[App::ExpressionParser::parse()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874).

Referenced by
[App::PropertyExpressionEngine::afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[Gui::ExpressionBindingPy::bind()](../../dc/d79/classGui_1_1ExpressionBindingPy.html#af65d8319d83f0ce08af580a73769582a),
[Gui::Dialog::Placement::bindObject()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a99b7a3e03b12a372318e6f2d8bb39fc1),
[BOPTools.GeneralFuseResult.GeneralFuseResult::explodeCompounds()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#acaa64b16d29f0065ce1379f8dc572649),
[Gui::TreeWidget::itemSearch()](../../de/de0/classGui_1_1TreeWidget.html#abb660e1cddeeee96c9f392c346d46700),
[PartGui::Location::Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[StdCmdExpression::pasteExpressions()](../../d2/dae/classStdCmdExpression.html#abab137615ab802f7688ff0b623022b9f),
[PartDesignGui::TaskExtrudeParameters::setupDialog()](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#a392344b2eb054d600f5c81befdc0595b),
[BOPTools.GeneralFuseResult.GeneralFuseResult::splitAggregates()](../../dd/dfc/classBOPTools_1_1GeneralFuseResult_1_1GeneralFuseResult.html#ac2dd77595b00ad1c612310df00438702),
and
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6).

## ◆ RangeComponent()

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::RangeComponent  | ( | [int](../../d1/da0/classint.html) | __begin_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | __end_ = `INT_MAX`,   
|  | [int](../../d1/da0/classint.html) | __step_ = `1`  
| ) | |   
static  
  
Referenced by
[App::VariableExpression::addComponent()](../../df/d0f/classApp_1_1VariableExpression.html#a13fe7b9451d199e5b1b2047b48b941a0),
and
[App::Expression::Component::Component()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a3d256c4ce032f643c24480f681cc52dc).

## ◆ relabeledDocument()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::relabeledDocument  | ( | [ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) & | _v_ ,   
---|---|---|---  
|  | const std::string & | _oldLabel_ ,   
|  | const std::string & | _newLabel_  
| ) | |   
  
References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
and
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18).

## ◆ relativeTo()

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) ObjectIdentifier::relativeTo  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Construct the simplest possible object identifier relative to another.

Parameters

     other| The other object identifier.   
---|---  
  
Returns

    A new simplified object identifier. 

References
[getOwner()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aaa2484f61d4ccb57e20f6f55a283c730),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::ObjectIdentifier::ResolveResults::propertyIndex](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a068329372c72559cc628c71c4b6e1035),
[App::ObjectIdentifier::ResolveResults::resolvedDocument](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab75d5ea9ec179f8eaad81531325f15c3),
[App::ObjectIdentifier::ResolveResults::resolvedDocumentName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa89b20df1e8259f4a2c894718722980a),
[App::ObjectIdentifier::ResolveResults::resolvedDocumentObject](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a75f904af9d27c4e217e770d631b6bff7),
[App::ObjectIdentifier::ResolveResults::resolvedDocumentObjectName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ad48dd81380d0620942822e0769064bcd),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ replaceObject()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::replaceObject  | ( | [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _res_ ,   
---|---|---|---  
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |  const  
  
References
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[App::PropertyLinkBase::tryReplaceLink()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95).

## ◆ resolve()

| void ObjectIdentifier::resolve  | ( | [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) & | _results_| ) |  const  
---|---|---|---|---|---  
protected  
  
Resolve the object identifier to a concrete document, documentobject, and
property.

This method is a helper method that fills out data in the given
[ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html)
object.

References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[App::ObjectIdentifier::ResolveResults::flags](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa10a3243feddcb1bbc55206d09c8a016),
[getDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[getDocumentObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff),
[App::Document::getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[App::ObjectIdentifier::ResolveResults::getProperty()](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a6cdae993b6aead3910694b1b6bc3c866),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[App::ObjectIdentifier::ResolveResults::propertyIndex](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a068329372c72559cc628c71c4b6e1035),
[App::ObjectIdentifier::ResolveResults::propertyName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a43b1f13706450b0cb1344c1aab70e8d9),
[App::ObjectIdentifier::ResolveResults::propertyType](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a4a562c0f1a5d62d4e4eacc75d8fde46f),
[App::ObjectIdentifier::ResolveResults::resolvedDocument](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab75d5ea9ec179f8eaad81531325f15c3),
[App::ObjectIdentifier::ResolveResults::resolvedDocumentName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa89b20df1e8259f4a2c894718722980a),
[App::ObjectIdentifier::ResolveResults::resolvedDocumentObject](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a75f904af9d27c4e217e770d631b6bff7),
[App::ObjectIdentifier::ResolveResults::resolvedDocumentObjectName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ad48dd81380d0620942822e0769064bcd),
[App::ObjectIdentifier::ResolveResults::resolvedProperty](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aed491da2fa165a239384e218f652f500),
[App::ObjectIdentifier::ResolveResults::resolvedSubObject](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a881b7ed3fb003986669471252d1da082),
[resolveProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e),
[App::ObjectIdentifier::ResolveResults::subObjectName](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#aa5013797852c67c1750195f9512e85e5),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

Referenced by
[App::ObjectIdentifier::ResolveResults::ResolveResults()](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ac68d2770dbaa3768a52327848a0fad41).

## ◆ resolveAmbiguity() [1/2]

void ObjectIdentifier::resolveAmbiguity  | ( | | ) |   
---|---|---|---|---  
  
References
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::ObjectIdentifier::String::isForceIdentifier()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a32064d2f8a40ae9d4965cc8893ee8563),
[isLocalProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8e6815f2e1c9bde7e770ff6f2c607277),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
and
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f).

Referenced by
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f).

## ◆ resolveAmbiguity() [2/2]

| void ObjectIdentifier::resolveAmbiguity  | ( | [ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html) & | _results_| ) |   
---|---|---|---|---|---  
protected  
  
References
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[setDocumentName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ resolveErrorString()

std::string ObjectIdentifier::resolveErrorString  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::VariableExpression::getProperty()](../../df/d0f/classApp_1_1VariableExpression.html#a8211f23466f283ea3c5e4a149e904c34).

## ◆ resolveProperty()

| [Property](../../d0/da9/classApp_1_1Property.html) * ObjectIdentifier::resolveProperty  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const char *  | _propertyName_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *& | _sobj_ ,   
|  | [int](../../d1/da0/classint.html) & | _ptype_  
| ) | |  const  
protected  
  
References
[App::ExtensionContainer::getPropertyByName()](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::DocumentObject::getSubObject()](../../d2/de4/classApp_1_1DocumentObject.html#a8f89853cff4f8111d973222a4de576e6),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

Referenced by
[App::ObjectIdentifier::ResolveResults::getProperty()](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a6cdae993b6aead3910694b1b6bc3c866),
and
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed).

## ◆ setComponent() [1/2]

void App::ObjectIdentifier::setComponent  | ( | [int](../../d1/da0/classint.html) | _idx_ ,   
---|---|---|---  
|  | [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) && | _comp_  
| ) | |   
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ setComponent() [2/2]

void App::ObjectIdentifier::setComponent  | ( | [int](../../d1/da0/classint.html) | _idx_ ,   
---|---|---|---  
|  | const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | _comp_  
| ) | |   
  
## ◆ setDocumentName()

void ObjectIdentifier::setDocumentName  | ( | [ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | _name_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _force_ = `false`  
| ) | |   
  
Set the document name for this object identifier.

If force is true, the document name will always be included in the string
representation.

Parameters

     name| Name of document object.   
---|---  
force| Force name to be set  
  
References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
and
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

Referenced by
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4503f7d6916abae555ddb15db1eed9ea),
and
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843).

## ◆ setDocumentObjectName() [1/2]

void ObjectIdentifier::setDocumentObjectName  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _force_ = `false`,   
|  | [ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | _subname_ = `[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)()`,   
|  | [bool](../../d9/db9/classbool.html) | _checkImport_ = `false`  
| ) | |   
  
References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
[localProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#af97eefc24e711f575f3af520fd6b433b),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[setDocumentName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ setDocumentObjectName() [2/2]

void ObjectIdentifier::setDocumentObjectName  | ( | [ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | _name_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _force_ = `false`,   
|  | [ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | _subname_ = `[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)()`,   
|  | [bool](../../d9/db9/classbool.html) | _checkImport_ = `false`  
| ) | |   
  
Set the document object name of this object identifier.

If force is true, the document object will not be resolved dynamically from
the object identifier's components, but used as given by this method.

Parameters

     name| Name of document object.   
---|---  
force| Force name to be set.  
  
References
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

Referenced by
[ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651),
and
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4503f7d6916abae555ddb15db1eed9ea).

## ◆ setValue()

void ObjectIdentifier::setValue  | ( | const [App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3) & | _value_| ) |  const  
---|---|---|---|---|---  
  
Set value of a property or field pointed to by this object identifier.

This method uses Python to do the actual work. and a limited set of types that
can be in the
[App::any](../../dd/dc2/namespaceApp.html#a208090b7fcb0b5ccff253a02d5819dd3)
variable is supported:
[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html "The Quantity
class."), double, char*, const char*, int, unsigned int, short, unsigned
short, char, and unsigned char.

Parameters

     value| Value to set   
---|---  
  
References
[access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[App::ObjectIdentifier::ResolveResults::propertyType](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#a4a562c0f1a5d62d4e4eacc75d8fde46f),
[App::pyObjectFromAny()](../../dd/dc2/namespaceApp.html#a0fd92b74207e681fd5b4a27a5c70f0c0),
and
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ SimpleComponent() [1/3]

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::SimpleComponent  | ( | const char *  | __component_| ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[App::PropertyVector::getPaths()](../../d5/d2b/classApp_1_1PropertyVector.html#aa19d7736475e4226446cd94cf6f52a70),
[App::PropertyPlacement::getPaths()](../../da/d51/classApp_1_1PropertyPlacement.html#a533c181be98ff243e893f11f4584b77e),
[App::PropertyRotation::getPaths()](../../df/d76/classApp_1_1PropertyRotation.html#afe01f3c5baa6287719368bf4798096f3),
and
[ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651).

## ◆ SimpleComponent() [2/3]

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::SimpleComponent  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | __component_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ SimpleComponent() [3/3]

| static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) App::ObjectIdentifier::SimpleComponent  | ( | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | __component_| ) |   
---|---|---|---|---|---  
static  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ toEscapedString()

std::string ObjectIdentifier::toEscapedString  | ( | | ) |  const  
---|---|---|---|---  
  
Escape toString representation so it is suitable for being embedded in a
python command.

Returns

    Escaped string. 

References
[Base::Tools::escapedUnicodeFromUtf8()](../../d6/dda/structBase_1_1Tools.html#a2cfe13d9b5c340ec5dc8a7b34fff8645),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

Referenced by
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a054996522e83552d345849bb9071b600).

## ◆ toPersistentString()

std::string ObjectIdentifier::toPersistentString  | ( | | ) |  const  
---|---|---|---|---  
  
References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
[App::PropertyLinkBase::exportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[getSubPathStr()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afb76b19861a0da703aa6f869a0489931),
[App::DocumentObject::isExporting()](../../d2/de4/classApp_1_1DocumentObject.html#a5483904c4a9eb870a64233ac737e4dee),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
[localProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#af97eefc24e711f575f3af520fd6b433b),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[App::ObjectIdentifier::String::toString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f).

## ◆ toString()

const std::string & ObjectIdentifier::toString  | ( | | ) |  const  
---|---|---|---|---  
  
Create a string representation of this object identifier.

An identifier is written as
document::documentobject.property.subproperty1...subpropertyN document# may be
dropped; it is assumed to be within owner's document. If documentobject is
dropped, the property is assumed to be owned by the owner specified in the
object identifiers constructor.

Returns

    A string 

References
[documentName](../../dd/d13/classApp_1_1ObjectIdentifier.html#af0442ee305343655b0ac7e5a806bf9d2),
[documentNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a37a5e2f5fbfd67516e222967f6d14edf),
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[documentObjectNameSet](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4ec7160a7b137451af0eaec61ff3c42c),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[getSubPathStr()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afb76b19861a0da703aa6f869a0489931),
[localProperty](../../dd/d13/classApp_1_1ObjectIdentifier.html#af97eefc24e711f575f3af520fd6b433b),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[App::ObjectIdentifier::String::toString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a7609abad389a5b852573213fd66a491f).

Referenced by
[access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[Gui::QuantitySpinBox::boundToName()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#aedce3c1555a077049ab3ce82870a1e45),
[Sketcher::SketchObject::carbonCopy()](../../d9/dad/classSketcher_1_1SketchObject.html#aca6b3b230ba97afe8d095b8e6cca02c4),
[hash()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a420e7ae702cc2d90b62fe15296980240),
[operator<()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a5d31da8fcdb3a26ebcc4028bac6fe8df),
[operator==()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe9fa06dbf743b6233b55a11a280e349),
and
[toEscapedString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9c8aaa7cfadced7f02366ca502c53029).

## ◆ updateElementReference()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::updateElementReference  | ( | [ExpressionVisitor](../../d8/d68/classApp_1_1ExpressionVisitor.html) & | _v_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _reverse_ = `false`  
| ) | |   
  
References
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[shadowSub](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad9f06332942ff16a8b4a56132a9f5dba),
and
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36).

## ◆ updateLabelReference()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::updateLabelReference  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |   
  
References
[documentObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab1ca904a89cc5b7d2e2fc0db6543143c),
[App::ObjectIdentifier::String::getString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a9f7793f1ebed21d71d0305c7a7fb3a7b),
[App::ObjectIdentifier::String::isForceIdentifier()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a32064d2f8a40ae9d4965cc8893ee8563),
[App::ObjectIdentifier::String::isRealString()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#ab39f355cd6d30feb9bae70fecdb63b18),
[owner](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1da5f2b5c2c9124592e6cee4319f9090),
[subObjectName](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad540cad62df0d8e23161a68b18f00a36),
and
[App::PropertyLinkBase::updateLabelReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da).

## ◆ verify()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::verify  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _silent_ = `false`  
| ) | |  const  
  
References
[App::Property::getName()](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a),
[App::CellAddress::parseAbsoluteAddress()](../../dd/d94/structApp_1_1CellAddress.html#ac349f371300d7b3ee08549f491db7f0a),
and
[App::CellAddress::ShowRowColumn](../../dd/d94/structApp_1_1CellAddress.html#a573756537af1b3daf76e70d4dfa4457da61f9d5e0dd1062ffc2e63db7c7de6345).

## Friends And Related Function Documentation

## ◆ ResolveResults

| [friend](../../d7/d23/classfriend.html) struct
[ResolveResults](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html)  
---  
friend  
  
Referenced by
[getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af1194cb10949e17069375abd40d4b2bd),
and
[getSubPathStr()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afb76b19861a0da703aa6f869a0489931).

## Member Data Documentation

## ◆ components

|
std::vector<[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html)>
App::ObjectIdentifier::components  
---  
protected  
  
Referenced by
[getPropertyComponents()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a57264281085e983af84c5dbbfd5871e0).

## ◆ documentName

| [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ObjectIdentifier::documentName  
---  
protected  
  
Referenced by
[getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[relabeledDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab762f0b511088f1aad35a265a16bf5bc),
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[setDocumentName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ documentNameSet

| [bool](../../d9/db9/classbool.html) App::ObjectIdentifier::documentNameSet  
---  
protected  
  
Referenced by
[getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[relabeledDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab762f0b511088f1aad35a265a16bf5bc),
[setDocumentName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8d99444e50797b76515cc705a04b88d0),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ documentObjectName

| [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ObjectIdentifier::documentObjectName  
---  
protected  
  
Referenced by
[adjustLinks()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a64e384b81e6d7f8de55251a498467604),
[getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2d8af8b84a0c426af896a2f190b692ce),
[getPropertyComponents()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a57264281085e983af84c5dbbfd5871e0),
[getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[hasDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a58b1475c362d8f38085e711911d2fb4e),
[importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6),
and
[updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

## ◆ documentObjectNameSet

| [bool](../../d9/db9/classbool.html)
App::ObjectIdentifier::documentObjectNameSet  
---  
protected  
  
Referenced by
[getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[hasDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a58b1475c362d8f38085e711911d2fb4e),
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ localProperty

| [bool](../../d9/db9/classbool.html) App::ObjectIdentifier::localProperty  
---  
protected  
  
Referenced by
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9ae70c738c44b6241add3657ef8af843),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
and
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6).

## ◆ owner

| [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::ObjectIdentifier::owner  
---  
protected  
  
Referenced by
[canonicalPath()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a7ef3ed6173cdd2276e28d4de038c1501),
[App::ObjectIdentifier::String::checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f),
[getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
[importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[ObjectIdentifier()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad3dfbfb2373e49652ce2f31ed92c2651),
[operator<()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a5d31da8fcdb3a26ebcc4028bac6fe8df),
[operator==()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe9fa06dbf743b6233b55a11a280e349),
[replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a61f6e189480422512a8dd0f59f69899f),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6),
and
[updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

## ◆ shadowSub

| std::pair<std::string,std::string> App::ObjectIdentifier::shadowSub  
---  
protected  
  
Referenced by
[getSubObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1111706c4bc3efd238f0066c4226421b),
[importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
and
[updateElementReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab8fdf8392daa0dbc35aed2e2d9e90fc3).

## ◆ subObjectName

| [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ObjectIdentifier::subObjectName  
---  
protected  
  
Referenced by
[access()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afe357711ff3adc68e0a69cbad332a4eb),
[adjustLinks()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a64e384b81e6d7f8de55251a498467604),
[getDepLabels()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a2d8af8b84a0c426af896a2f190b692ce),
[getStringList()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8870022fd22c692772be62dd0157b6a7),
[getSubObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a1111706c4bc3efd238f0066c4226421b),
[importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[relativeTo()](../../dd/d13/classApp_1_1ObjectIdentifier.html#af3818694d759d01636c69ca3ba6203ad),
[replaceObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a80caff359bff231c8a61c0a77bda725f),
[resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[resolveAmbiguity()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a4503f7d6916abae555ddb15db1eed9ea),
[App::ObjectIdentifier::ResolveResults::resolveErrorString()](../../d8/de6/structApp_1_1ObjectIdentifier_1_1ResolveResults.html#ab5f56590f87b6dbf5f3b3e610e08f2b8),
[resolveProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e),
[setDocumentObjectName()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a6e7c29b19494c855edd9ce6a137556d2),
[toPersistentString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a469067b76b0420cf658c4299a4877c0f),
[toString()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afa6f69e040dc39e19f8d8a5b32d52cc6),
[updateElementReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ab8fdf8392daa0dbc35aed2e2d9e90fc3),
and
[updateLabelReference()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8ee527f0da9e9a1d26e8744d048ced67).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ObjectIdentifier.h
  * FreeCAD/src/App/ObjectIdentifier.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

