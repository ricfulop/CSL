---
url: https://freecad.github.io/SourceDoc/db/d34/classApp_1_1PropertyExpressionEngine.html
scraped_at: 2025-09-08T14:55:42.880537
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)

[List of all members](../../de/de7/classApp_1_1PropertyExpressionEngine-members.html) | Classes | Public Types | Public Member Functions | Public Attributes | Protected Member Functions | Friends

App::PropertyExpressionEngine Class Reference

`#include <PropertyExpressionEngine.h>`

##  Classes  
  
---  
struct | [ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html)  
| The
[ExpressionInfo](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html
"The ExpressionInfo struct encapsulates an expression.") struct encapsulates
an expression.
[More...](../../de/d4d/structApp_1_1PropertyExpressionEngine_1_1ExpressionInfo.html#details)  
  
struct | [Private](../../d3/d07/structPropertyExpressionEngine_1_1Private.html)  
  
##  Public Types  
  
---  
enum | [ExecuteOption](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329) { [ExecuteAll](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329a262f9fa9c130a157bc5f6c6d87b4b478) , [ExecuteOutput](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329a836ef973677bbaa70b463ba16bf94b62) , [ExecuteNonOutput](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329a77d97f9596a26ba622dd5d783b56af8b) , [ExecuteOnRestore](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329aa6aecd854e32277bf0cf78cea17d1cca) }  
| Execute options.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329)  
  
typedef std::function< std::string(const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, std::shared_ptr< const [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > expr)> | [ValidatorFunc](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab389bbc469930e2d1f43b3f29b3d3dac)  
![-](../../closed.png) Public Types inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
enum | [LinkFlags](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5f) {   
[LinkAllowExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fad0f16a963cb6d4ee03471a56eb0d2b2e)
,
[LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da)
,
[LinkRestoring](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa1de51bd54c0f62a03f8a15c70ed4a365)
,
[LinkAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5faa22f8833820bace817e74b03e6089f45)
,  
[LinkRestoreLabel](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fa5a4bc69cb609a1f93370ec11e29dc403)
,
[LinkSyncSubObject](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5fab29bedf78f3fa832237ffa3a544e88c8)  
}  
typedef std::pair< std::string, std::string > | [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620)  
![-](../../closed.png) Public Types inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
enum | [Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) {   
[Touched](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aa7412d0e7e6c015df9a22d89576953fe)
= 0 ,
[Immutable](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a59d0f940edf009b9ffbe01ed43d767cc)
= 1 ,
[ReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a06b1f9ba5fd320622558e264c1c096de)
= 2 ,
[Hidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014adef773114327b6ad987a0c47a4262a54)
= 3 ,  
[Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5)
= 4 ,
[MaterialEdit](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a40f41a6380775c2373e89a780bfac551)
= 5 ,
[NoMaterialListEdit](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5af65723f82e7b7f8d7fa6b2fe543b15)
= 6 ,
[Output](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a10640ff2cae2c1fda52dac13fc9a47a6)
= 7 ,  
[LockDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac134907b347ed2484e41577a88d9a06e)
= 8 ,
[NoModify](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a420f4e5f5f4d37d09078346493729ad5)
= 9 ,
[PartialTrigger](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a2a08e64817919ee4f7f35341f2e8f7f4)
= 10 ,
[NoRecompute](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a8f31692acbbf9a5b8719e48fa68c5cde)
= 11 ,  
[Single](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a9c73483be20c75fd4c35af435a108ff6)
= 12 ,
[Ordered](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a7a56d6d20d93cd99b4f8032f8dd061fb)
= 13 ,
[EvalOnRestore](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac1036b7face30993fb92e8ffd37d2636)
= 14 ,
[Busy](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5738c5d6491eb6a3385e22bb718a868a)
= 15 ,  
[CopyOnChange](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a300baf70d0747fc9f320701a04ba5499)
= 16 ,
[UserEdit](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aad5ce06614de6a327726a7d95436cec4)
= 17 ,
[PropStaticBegin](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ab0d78a081465b31f8462ce404b0aed26)
= 21 ,
[PropDynamic](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a610d527a8ef20b533504b5121a983d80)
= 21 ,  
[PropNoPersist](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ae221473138e52da3001d1de060205179)
= 22 ,
[PropNoRecompute](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a78b230717c2b517e7875c4211612b764)
= 23 ,
[PropReadOnly](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a75dc207c45c9bf592c42415e987e7d5e)
= 24 ,
[PropTransient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a49215d8e9f6a5a24523e5ce094fb867e)
= 25 ,  
[PropHidden](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aab1086519565f4fa2cc26a504daa92d3)
= 26 ,
[PropOutput](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a7610516494d96a531206dc3e1fe94f57)
= 27 ,
[PropStaticEnd](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a0a622c3dfc0aeb45722e09c18b8f8a16)
= 28 ,
[User1](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac99b647298c291251fac190ce52bda0b)
= 28 ,  
[User2](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5224f0c2368e03cdd6ab193da92a8ba3)
= 29 ,
[User3](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014aed76ddc4019f764ff7dbcb726007d14e)
= 30 ,
[User4](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a5f0e01e9cb9ad4119203788f0d6ca516)
= 31  
}  
  
##  Public Member Functions  
  
---  
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a6ef128439add23206d190bedd151f02e) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList) override  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a6ef128439add23206d190bedd151f02e)  
  
virtual void | [afterRestore](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1) () override  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1)  
  
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [canonicalPath](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &p) const override  
| Create a canonical object identifier of the given object _p_.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09)  
  
[Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a19a4bb9dfd62c2c0c82fdfc6e5df26c9) (void) const override  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a19a4bb9dfd62c2c0c82fdfc6e5df26c9)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnImportExternal](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a11bdfc2d9abf09bf1fe331f571a06b52) (const std::map< std::string, std::string > &nameMap) const override  
| Return a copy of the property if any changes caused by importing external
linked object.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a11bdfc2d9abf09bf1fe331f571a06b52)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLabelChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a66d03bca6be021be6445717920c2cc5d) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const override  
| Update object label reference in this property.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a66d03bca6be021be6445717920c2cc5d)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7d04daa6893b37a24602bb897eec8ed1) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const override  
| Return a copy of the property if the link replacement affects this property.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7d04daa6893b37a24602bb897eec8ed1)  
  
[bool](../../d9/db9/classbool.html) | [depsAreTouched](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a05382336b128fe6f5af9bd1062a0349b) () const  
| Determine whether any dependencies of any of the registered expressions have
been touched.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a05382336b128fe6f5af9bd1062a0349b)  
  
[DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * | [execute](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd) ([ExecuteOption](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329) option=[ExecuteAll](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329a262f9fa9c130a157bc5f6c6d87b4b478), [bool](../../d9/db9/classbool.html) *touched=nullptr)  
| Evaluate the expressions.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a734f6ae9dbd4df6a8ebafee9a8d8bebd)  
  
virtual std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), const [App::Expression](../../dc/d5c/classApp_1_1Expression.html) * > | [getExpressions](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a190fbdce938ee9ddee37b1d04ab95e65) () const override  
unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9c2ed33cbd8061fca8fb90a67aadf4cb) (void) const override  
| Estimate memory size of this property.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9c2ed33cbd8061fca8fb90a67aadf4cb)  
  
void | [getPathsToDocumentObject](../../db/d34/classApp_1_1PropertyExpressionEngine.html#abacf82f2397cd656b8e0cc01e0bc9295) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths) const  
| Find paths to document object.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#abacf82f2397cd656b8e0cc01e0bc9295)  
  
const boost::any | [getPathValue](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a5bc043e806eede3b4df9d21cbc2f44ef) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const override  
| Get expression for _path_.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a5bc043e806eede3b4df9d21cbc2f44ef)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0e2e176a32a6eda05d5c18a319ecd255) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0e2e176a32a6eda05d5c18a319ecd255)  
  
size_t | [numExpressions](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ac7c39b9516797e20664a6b175960d21f) () const  
| Number of expressions managed by this object.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ac7c39b9516797e20664a6b175960d21f)  
  
virtual void | [onContainerRestored](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a733f20b00486b5e21694ee2607fdae92) () override  
| Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a733f20b00486b5e21694ee2607fdae92)  
  
virtual void | [onRelabeledDocument](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab978c392422c25e6639385447cd69bc8) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc) override  
void | [Paste](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46) (const [Property](../../d0/da9/classApp_1_1Property.html) &from) override  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46)  
  
|
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa6da2921c13a1bb1dc2949fa9b762057)
()  
| Construct a new
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
object.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa6da2921c13a1bb1dc2949fa9b762057)  
  
virtual [bool](../../d9/db9/classbool.html) | [referenceChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af2b60f6411ba6c62236a29c0769b76bd) () const override  
| Test if the element reference has changed after restore.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af2b60f6411ba6c62236a29c0769b76bd)  
  
void | [renameExpressions](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a02fc7fcac9d0638d3e2385eb88b6cedc) (const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths)  
| Rename paths based on _paths_.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a02fc7fcac9d0638d3e2385eb88b6cedc)  
  
void | [renameObjectIdentifiers](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9a97068476d7bfe55e058e520eefac59) (const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths)  
| Rename object identifiers in the registered expressions.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9a97068476d7bfe55e058e520eefac59)  
  
void | [Restore](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa2bf7bff7cd8fa4cb953f5333916b0c9)  
  
void | [Save](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e)  
  
virtual void | [setExpressions](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af0f2f778f8e840efb832ef621441a3e9) (std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) > &&exprs) override  
void | [setPyObject](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a4b33a8605c64957b260f12dde55fb000) ([PyObject](../../df/d1b/classPyObject.html) *) override  
void | [setValidator](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a9f1e19b1d39a0df5fe26501308e2059e) ([ValidatorFunc](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab389bbc469930e2d1f43b3f29b3d3dac) f)  
void | [setValue](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab0b09b63154afba2b723637afed44276) ()  
void | [setValue](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > expr)  
| Set expression with optional comment for _path_.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1)  
  
virtual void | [updateElementReference](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false, [bool](../../d9/db9/classbool.html) notify=false) override  
| [Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs
These APIs are moved here so that any type of property can have the property
link behavior, e.g.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362)  
  
std::string | [validateExpression](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa259d698d63c151f459f14483346639a) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, std::shared_ptr< const [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > expr) const  
| Validate the given path and expression.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa259d698d63c151f459f14483346639a)  
  
|
[~PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a49037bf292b243fa8e245ca1eb4532ec)
()  
| Destroy the
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
object.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a49037bf292b243fa8e245ca1eb4532ec)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyExpressionContainer](../../db/da0/classApp_1_1PropertyExpressionContainer.html)  
virtual std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), const [App::Expression](../../dc/d5c/classApp_1_1Expression.html) * > | [getExpressions](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a31e577465b52bca4b154627ef8220f9a) () const =0  
|
[PropertyExpressionContainer](../../db/da0/classApp_1_1PropertyExpressionContainer.html#ad2a31b1f155cff49ba56cd43bfa0c6da)
()  
virtual void | [setExpressions](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a979ee6293a523dc1f82e074acc5e8462) (std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) > &&exprs)=0  
virtual | [~PropertyExpressionContainer](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a795a3cff495e206d3504f1e4e040bca6) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html)  
virtual void | [afterRestore](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a00e6240a9cf8e5b7dbf0cf287cbd4db1) () override  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a00e6240a9cf8e5b7dbf0cf287cbd4db1)  
  
virtual void | [breakLink](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a148b326bca33a5b23cc9434f24b569c2) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear) override  
| Called to reset this link property.
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a148b326bca33a5b23cc9434f24b569c2)  
  
virtual [int](../../d1/da0/classint.html) | [checkRestore](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ad045569aa3548d2240da8004ebdc6dec) (std::string *msg=nullptr) const override  
| Test if the link is restored unchanged.
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ad045569aa3548d2240da8004ebdc6dec)  
  
virtual void | [getLinks](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#adc29a7ff5211f6369aeab847422a2e52) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const override  
| Obtain the linked objects.
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#adc29a7ff5211f6369aeab847422a2e52)  
  
[bool](../../d9/db9/classbool.html) | [isLinkedToDocument](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a87095e7bb01de19c1e66d6dc9cba3d5e) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc) const  
|
[PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#af633f63e4452ab1c884ba9fb62da4c96)
()  
virtual void | [Restore](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4)  
  
virtual void | [Save](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676)  
  
|
[~PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a879d9c3cdc448f0198639eb01dd1dd32)
()  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
virtual [bool](../../d9/db9/classbool.html) | [adjustLink](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1ce35c00cf2495906301c94a0ea22c80) (const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &inList)=0  
| Called to adjust the link to avoid potential cyclic dependency.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1ce35c00cf2495906301c94a0ea22c80)  
  
virtual void | [breakLink](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9559e2b5adeb74b5dfa23960095b86a9) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) clear)=0  
| Called to reset this link property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9559e2b5adeb74b5dfa23960095b86a9)  
  
void | [checkLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b) (const std::vector< std::string > &subs, [bool](../../d9/db9/classbool.html) reset=true)  
| Check subnames for label registration.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6f699891cf9f008dd8875299efe2ca0b)  
  
virtual [int](../../d1/da0/classint.html) | [checkRestore](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a8d5f5505568090ea83840b00a7f140b9) (std::string *msg=nullptr) const  
| Test if the link is restored unchanged.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a8d5f5505568090ea83840b00a7f140b9)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnImportExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131) (const std::map< std::string, std::string > &nameMap) const  
| Return a copy of the property if any changes caused by importing external
linked object.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLabelChange](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel) const  
| Update object label reference in this property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [CopyOnLinkReplace](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ad21232bfd601a848542b503d73d14a9c) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj) const =0  
| Return a copy of the property if the link replacement affects this property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ad21232bfd601a848542b503d73d14a9c)  
  
void | [getLinkedElements](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a973b1ddfd9b981181395dfb2a305f36d) (std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > &elements, [bool](../../d9/db9/classbool.html) newStyle=true, [bool](../../d9/db9/classbool.html) all=true) const  
| Helper function to return a map of linked object and its subname references.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a973b1ddfd9b981181395dfb2a305f36d)  
  
template<class T >  
void | [getLinkedObjects](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1db655ff563d9cd96529cf687b3c77ea) (T &inserter, [bool](../../d9/db9/classbool.html) all=false) const  
| Helper function to return linked objects using an std::inserter.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1db655ff563d9cd96529cf687b3c77ea)  
  
virtual void | [getLinks](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9ea079fa62ec12eb6f20360e7016f43c) (std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) all=false, std::vector< std::string > *subs=nullptr, [bool](../../d9/db9/classbool.html) newStyle=true) const =0  
| Obtain the linked objects.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a9ea079fa62ec12eb6f20360e7016f43c)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const override  
| Compare if this property has the same content as the given one.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a80edc3aa77b975c9862ca4ff78179407)  
  
std::map< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > | [linkedElements](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af46505016f8488c705e72657917f1630) ([bool](../../d9/db9/classbool.html) newStyle=true, [bool](../../d9/db9/classbool.html) all=true) const  
| Helper function to return a map of linked object and its subname references.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af46505016f8488c705e72657917f1630)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [linkedObjects](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a888cdc4caeaef9a38b3479c34e472bdd) ([bool](../../d9/db9/classbool.html) all=false) const  
| Helper function to return all linked objects of this property.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a888cdc4caeaef9a38b3479c34e472bdd)  
  
|
[PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6dd04e8d33dd47193b8fc86308f1eea7)
()  
virtual [bool](../../d9/db9/classbool.html) | [referenceChanged](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0) () const  
| Test if the element reference has changed after restore.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0)  
  
void | [registerLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f) (std::vector< std::string > &&labels, [bool](../../d9/db9/classbool.html) reset=true)  
| Register label reference for future object relabel update.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f)  
  
void | [setAllowExternal](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6a771360ff664dd0f0b740ef566f4254) ([bool](../../d9/db9/classbool.html) allow)  
| Enable/disable temporary holding external object without throwing exception.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6a771360ff664dd0f0b740ef566f4254)  
  
virtual void | [setAllowPartial](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a26441b0567312a6b71c03f2f16dee982) ([bool](../../d9/db9/classbool.html) enable)  
[bool](../../d9/db9/classbool.html) | [testFlag](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef) ([int](../../d1/da0/classint.html) flag) const  
void | [unregisterElementReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29) ()  
| Clear internal element reference registration.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29)  
  
void | [unregisterLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700) ()  
| Clear internal label references registration.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aeae2e1785793525c8dd1ae4d26151700)  
  
virtual void | [updateElementReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6447c82dc0b81cea703a9a235a2448c3) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false, [bool](../../d9/db9/classbool.html) notify=false)  
| [Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs
These APIs are moved here so that any type of property can have the property
link behavior, e.g.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6447c82dc0b81cea703a9a235a2448c3)  
  
virtual | [~PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aadb029b9c4d709bffd43d43642e1eaca) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
virtual void | [aboutToSetChildValue](../../d0/da9/classApp_1_1Property.html#a9e3dfa9cc1ea03167fbe8c12f811f546) ([Property](../../d0/da9/classApp_1_1Property.html) &)  
| Called before a child property changing value.
[More...](../../d0/da9/classApp_1_1Property.html#a9e3dfa9cc1ea03167fbe8c12f811f546)  
  
virtual void | [afterRestore](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f) ()  
| Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)
[More...](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f)  
  
virtual [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [canonicalPath](../../d0/da9/classApp_1_1Property.html#a7a970c03b5e610df341e5cf464100523) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &p) const  
| Convert p to a canonical representation of it.
[More...](../../d0/da9/classApp_1_1Property.html#a7a970c03b5e610df341e5cf464100523)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [Copy](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de) (void) const =0  
| Returns a new copy of the property (mainly for Undo/Redo and transactions)
[More...](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de)  
  
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) * | [getContainer](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063) (void) const  
| Get a pointer to the
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base
class of all classes with properties.") derived class the property belongs to.
[More...](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063)  
  
const char * | [getDocumentation](../../d0/da9/classApp_1_1Property.html#ada9481ae19a85f023c5597d57f8c809b) (void) const  
| Get the documentation of this property.
[More...](../../d0/da9/classApp_1_1Property.html#ada9481ae19a85f023c5597d57f8c809b)  
  
virtual const char * | [getEditorName](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983) (void) const  
| Get the class name of the associated property editor item.
[More...](../../d0/da9/classApp_1_1Property.html#a9115e14c90e9842442d5f0c8f68ce983)  
  
std::string | [getFullName](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2) () const  
const char * | [getGroup](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee) (void) const  
| Get the group of this property.
[More...](../../d0/da9/classApp_1_1Property.html#ab815066b984a7d6c133b4c947a989fee)  
  
int64_t | [getID](../../d0/da9/classApp_1_1Property.html#ad9f8fd8cb3f719b81661ad69f5047a44) () const  
| Return a unique ID for the property.
[More...](../../d0/da9/classApp_1_1Property.html#ad9f8fd8cb3f719b81661ad69f5047a44)  
  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330) (void) const override  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB? This method is defined in
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html "Persistence
class and root of the type system.").
[More...](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330)  
  
const char * | [getName](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a) (void) const  
| Get the name of this property in the belonging container With
[hasName()](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f)
it can be checked beforehand if a valid name is set.
[More...](../../d0/da9/classApp_1_1Property.html#a95b43437b8a43e35fc1c692f5bdda00a)  
  
virtual void | [getPaths](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e) (std::vector< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths) const  
| Get valid paths for this property; used by auto completer.
[More...](../../d0/da9/classApp_1_1Property.html#a945f1c031f109242e362c5701516ff8e)  
  
virtual const boost::any | [getPathValue](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path) const  
| Get value of property.
[More...](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea)  
  
virtual [bool](../../d9/db9/classbool.html) | [getPyPathValue](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &, Py::Object &) const  
| Get Python value of property.
[More...](../../d0/da9/classApp_1_1Property.html#a55400138b9f116fa42702ed36d0511b1)  
  
unsigned long | [getStatus](../../d0/da9/classApp_1_1Property.html#a4df77b9a46967312e4a885f1a7386c16) () const  
| return the status bits
[More...](../../d0/da9/classApp_1_1Property.html#a4df77b9a46967312e4a885f1a7386c16)  
  
short | [getType](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510) (void) const  
| Get the type of the property in the container.
[More...](../../d0/da9/classApp_1_1Property.html#abc4967c88a5fc83c27a47f9534fdd510)  
  
[bool](../../d9/db9/classbool.html) | [hasName](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f) () const  
| Check if the property has a name set.
[More...](../../d0/da9/classApp_1_1Property.html#a4cb7ff34589a55dfb14f61277d04706f)  
  
virtual void | [hasSetChildValue](../../d0/da9/classApp_1_1Property.html#a35de61d1f853c6adb4e150c6cbb97ede) ([Property](../../d0/da9/classApp_1_1Property.html) &)  
| Called when a child property has changed value.
[More...](../../d0/da9/classApp_1_1Property.html#a35de61d1f853c6adb4e150c6cbb97ede)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d0/da9/classApp_1_1Property.html#a6f80d875dca2960d861f185d152e0de2) () const  
virtual [bool](../../d9/db9/classbool.html) | [isSame](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d) (const [Property](../../d0/da9/classApp_1_1Property.html) &other) const  
| Compare if this property has the same content as the given one.
[More...](../../d0/da9/classApp_1_1Property.html#a08399f877d573339ec921f08bd48ff3d)  
  
[bool](../../d9/db9/classbool.html) | [isSinglePrecision](../../d0/da9/classApp_1_1Property.html#ad35584ef2dcc3838038f69f5f1c765c4) () const  
| Gets precision of properties using floating point numbers.
[More...](../../d0/da9/classApp_1_1Property.html#ad35584ef2dcc3838038f69f5f1c765c4)  
  
[bool](../../d9/db9/classbool.html) | [isTouched](../../d0/da9/classApp_1_1Property.html#afc61f45939514cad9316d170ffa99933) (void) const  
| Test if this property is touched.
[More...](../../d0/da9/classApp_1_1Property.html#afc61f45939514cad9316d170ffa99933)  
  
virtual void | [onContainerRestored](../../d0/da9/classApp_1_1Property.html#a724e44690754d6abaff38d3131420225) ()  
| Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")
[More...](../../d0/da9/classApp_1_1Property.html#a724e44690754d6abaff38d3131420225)  
  
virtual void | [Paste](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be) (const [Property](../../d0/da9/classApp_1_1Property.html) &from)=0  
| Paste the value from the property (mainly for Undo/Redo and transactions)
[More...](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be)  
  
|
[Property](../../d0/da9/classApp_1_1Property.html#ab029377b86e5b8ae7513bf93f9c9a955)
()  
void | [purgeTouched](../../d0/da9/classApp_1_1Property.html#ac97a88a6ecc0a6644833aac52fbb4334) (void)  
| Reset this property touched.
[More...](../../d0/da9/classApp_1_1Property.html#ac97a88a6ecc0a6644833aac52fbb4334)  
  
void | [setContainer](../../d0/da9/classApp_1_1Property.html#aa03e6562bf3996db1700b0e636425257) ([PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *Father)  
| Is called by the framework to set the father (container)
[More...](../../d0/da9/classApp_1_1Property.html#aa03e6562bf3996db1700b0e636425257)  
  
virtual void | [setPathValue](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &path, const boost::any &value)  
| Set value of property.
[More...](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22)  
  
void | [setReadOnly](../../d0/da9/classApp_1_1Property.html#a8d9c78a46b9b79dc637cf70e1224c222) ([bool](../../d9/db9/classbool.html) readOnly)  
| Sets property editable/grayed out in property editor.
[More...](../../d0/da9/classApp_1_1Property.html#a8d9c78a46b9b79dc637cf70e1224c222)  
  
void | [setSinglePrecision](../../d0/da9/classApp_1_1Property.html#a552cc2dfc668452ab086f9c3903991e8) ([bool](../../d9/db9/classbool.html) single)  
| Sets precision of properties using floating point numbers to single, the
default is double.
[More...](../../d0/da9/classApp_1_1Property.html#a552cc2dfc668452ab086f9c3903991e8)  
  
void | [setStatus](../../d0/da9/classApp_1_1Property.html#a2f10dba2d265461344c6df7d0a40ad4e) ([Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) pos, [bool](../../d9/db9/classbool.html) on)  
void | [setStatusValue](../../d0/da9/classApp_1_1Property.html#a32cf2f8513b5a66b0b39c839c559f20b) (unsigned long status)  
[bool](../../d9/db9/classbool.html) | [testStatus](../../d0/da9/classApp_1_1Property.html#aa0757bcb7ff02f8ece1205afd8a05775) ([Status](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014) pos) const  
void | [touch](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475) ()  
| [Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") status handling.
[More...](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475)  
  
virtual | [~Property](../../d0/da9/classApp_1_1Property.html#a0148f620477300ca547154581828cc1c) ()  
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
[App::ScopedLink](../../df/d30/classApp_1_1ScopedLink.html)  
[LinkScope](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263) | [getScope](../../df/d30/classApp_1_1ScopedLink.html#a820666ea293f55369d42dff0b47f30c1) () const  
| Get the links scope Retrieve what kind of links are allowed.
[More...](../../df/d30/classApp_1_1ScopedLink.html#a820666ea293f55369d42dff0b47f30c1)  
  
void | [setScope](../../df/d30/classApp_1_1ScopedLink.html#a27dac823725787d1ba0db6c7186de85e) ([LinkScope](../../dd/dc2/namespaceApp.html#a1570f007f08babaa285aedc8b7a8c263) scope)  
| Set the links scope Allows to define what kind of links are allowed.
[More...](../../df/d30/classApp_1_1ScopedLink.html#a27dac823725787d1ba0db6c7186de85e)  
  
  
##  Public Attributes  
  
---  
boost::signals2::signal< void(const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &)> | [expressionChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a)  
| signal called when an expression was changed
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a)  
  
![-](../../closed.png) Public Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d0/da9/classApp_1_1Property.html#a9e9e25207ee1e619c75f835f9853cf74)  
  
##  Protected Member Functions  
  
---  
virtual void | [hasSetValue](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723) () override  
| Gets called by all
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab0b09b63154afba2b723637afed44276)
methods after the value has changed.
[More...](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723)  
  
virtual void | [onRelabeledDocument](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a09ea603415b50e5604c1551cf597a6f2) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &doc)=0  
![-](../../closed.png) Protected Member Functions inherited from
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html)  
virtual void | [aboutToSetChildValue](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ac7444aaa1de15fcae6a70b0d024723d3) ([App::Property](../../d0/da9/classApp_1_1Property.html) &prop) override  
| Called before a child property changing value.
[More...](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ac7444aaa1de15fcae6a70b0d024723d3)  
  
void | [clearDeps](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#ae68afb7d60232d3e41aca30995012143) ()  
virtual [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html) * | [createXLink](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a3346daf351462653b92e0076885a2812) ()  
virtual void | [onAddDep](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a540f89b458936458a1aa32346e35a5a1) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
virtual void | [onBreakLink](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a0ee1592cda577947e7df9f0fc1f3a8d1) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
virtual void | [onRemoveDep](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a112fda58a6fc296d3aab70ef8999857f) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
void | [updateDeps](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a83acea46b0d063043f43d99de26dfe29) (std::map< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, [bool](../../d9/db9/classbool.html) > &&newDeps)  
![-](../../closed.png) Protected Member Functions inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
virtual void | [hasSetValue](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763) () override  
| Gets called by all setValue() methods after the value has changed.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763)  
  
void | [setFlag](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1d7b18ad8ba2508cc00bc7e33c944a3f) ([int](../../d1/da0/classint.html) flag, [bool](../../d9/db9/classbool.html) value=true)  
![-](../../closed.png) Protected Member Functions inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
virtual void | [aboutToSetValue](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d) (void)  
| Gets called by all setValue() methods before the value has changed.
[More...](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d)  
  
virtual void | [hasSetValue](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d) (void)  
| Gets called by all setValue() methods after the value has changed.
[More...](../../d0/da9/classApp_1_1Property.html#a03b30d20077084ccf9633de842f0db6d)  
  
virtual void | [verifyPath](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7) (const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &p) const  
| Verify a path for the current property.
[More...](../../d0/da9/classApp_1_1Property.html#ac71239ca0d166b8e3b6ed5294f4ee4f7)  
  
  
##  Friends  
  
---  
class | [AtomicPropertyChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a94bfe6bb9050c7eaf7f379b6bfcc3c5c)  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html)  
static void | [breakLinks](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *link, const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) clear)  
| Helper function for breaking link properties.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44)  
  
static const char * | [exportSubName](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad) (std::string &output, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *subname, [bool](../../d9/db9/classbool.html) first_obj=false)  
| Helper function to export a subname reference.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad)  
  
static void | [getLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce) (std::vector< std::string > &labels, const char *subname)  
| Helper function to extract labels from a subname reference.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab56a3785dd388ecb7db50c9c0f8c8cce)  
  
static std::string | [importSubName](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *sub, [bool](../../d9/db9/classbool.html) &restoreLabel)  
| Helper function to import a subname reference.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a69a9c1fd7b0fbcd5eff4090ba640669e)  
  
static void | [restoreLabelReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, std::string &sub, [ShadowSub](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a18bf17d37c93bcf665585c9d880ca620) *shadow=nullptr)  
| Helper function to restore label references during import.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3766a9d6714b2db0ba1fa991277e6ccb)  
  
static [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [tryImport](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a2bf156dd3396caaad6204f5269698e7a) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::map< std::string, std::string > &nameMap)  
| Helper function for link import operation.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a2bf156dd3396caaad6204f5269698e7a)  
  
static std::string | [tryImportSubName](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *sub, const [App::Document](../../d8/d3e/classApp_1_1Document.html) *doc, const std::map< std::string, std::string > &nameMap)  
| Helper function for link import operation.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a368e7609bf8ee24fd6b574c392e8c6d4)  
  
static std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::string > | [tryReplaceLink](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95) (const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *owner, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj, const char *sub=nullptr)  
| Helper functions.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#acf71b9e501393cadbb7af1077561ae95)  
  
static std::pair< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, std::vector< std::string > > | [tryReplaceLinkSubs](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc) (const [App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html) *owner, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *parent, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj, const std::vector< std::string > &subs)  
| Helper function to check and replace a link with multiple subname
references.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ae7aa54cba5888dcd26d60876dd7672cc)  
  
static void | [updateElementReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a4ead775f36d2ccf4564fb59713a20d94) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *feature, [bool](../../d9/db9/classbool.html) reverse=false)  
| Update all element references in all link properties of _feature_.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a4ead775f36d2ccf4564fb59713a20d94)  
  
static std::string | [updateLabelReference](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *linked, const char *subname, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const std::string &ref, const char *newLabel)  
| Helper function to update subname reference on label change.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ac2fd4f8ba5aeea8846f1ffc1d55e02da)  
  
static std::vector< std::pair< [Property](../../d0/da9/classApp_1_1Property.html) *, std::unique_ptr< [Property](../../d0/da9/classApp_1_1Property.html) > > > | [updateLabelReferences](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a352aa734ca82348678cc710b1eead0ef) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, const char *newLabel)  
| Helper function to collect changed property when an object re-label.
[More...](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a352aa734ca82348678cc710b1eead0ef)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
static void | [destroy](../../d0/da9/classApp_1_1Property.html#a3a8325b864cd82b562eb553fe2be6d1c) ([Property](../../d0/da9/classApp_1_1Property.html) *p)  
| For safe deleting of a dynamic property.
[More...](../../d0/da9/classApp_1_1Property.html#a3a8325b864cd82b562eb553fe2be6d1c)  
  
static [bool](../../d9/db9/classbool.html) | [isValidName](../../d0/da9/classApp_1_1Property.html#ad8541be7b1fddd7f21f2ce3e18e8c06d) (const char *name)  
| Check if the passed name is valid.
[More...](../../d0/da9/classApp_1_1Property.html#ad8541be7b1fddd7f21f2ce3e18e8c06d)  
  
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
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::Property](../../d0/da9/classApp_1_1Property.html)  
std::bitset< 32 > | [StatusBits](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
| Status bits of the property The first 8 bits are used for the base system
the rest can be used in descendent classes to mark special statuses on the
objects.
[More...](../../d0/da9/classApp_1_1Property.html#ab93fa6ff45ac8bf7dcaac9ead5e09f67)  
  
  
## Member Typedef Documentation

## ◆ ValidatorFunc

typedef std::function<std::string (const
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &
path, std::shared_ptr<const
[App::Expression](../../dc/d5c/classApp_1_1Expression.html)> expr)>
[App::PropertyExpressionEngine::ValidatorFunc](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab389bbc469930e2d1f43b3f29b3d3dac)  
---  
  
## Member Enumeration Documentation

## ◆ ExecuteOption

enum
[App::PropertyExpressionEngine::ExecuteOption](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329)  
---  
  
Execute options.

Enumerator  
---  
ExecuteAll | Execute all expression.   
ExecuteOutput | Execute only output property bindings.   
ExecuteNonOutput | Execute only non-output property bindings.   
ExecuteOnRestore | Execute on document restore.   
  
## Constructor & Destructor Documentation

## ◆ PropertyExpressionEngine()

PropertyExpressionEngine::PropertyExpressionEngine  | ( | | ) |   
---|---|---|---|---  
  
Construct a new
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
object.

Referenced by
[Copy()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a19a4bb9dfd62c2c0c82fdfc6e5df26c9).

## ◆ ~PropertyExpressionEngine()

PropertyExpressionEngine::~PropertyExpressionEngine  | ( | | ) |   
---|---|---|---|---  
  
Destroy the
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
object.

## Member Function Documentation

## ◆ adjustLink()

| [bool](../../d9/db9/classbool.html) PropertyExpressionEngine::adjustLink  | ( | const std::set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _inList_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Called to adjust the link to avoid potential cyclic dependency.

Parameters

     inList| recursive in-list of the would-be parent  
---|---  
  
Returns

    Return whether the link has been adjusted

This function tries to correct the link to avoid any (sub)object inside in-
list. If the adjustment is impossible, exception will be raised

Implements
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1ce35c00cf2495906301c94a0ea22c80).

References
[AtomicPropertyChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a94bfe6bb9050c7eaf7f379b6bfcc3c5c),
[expressionChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a),
and
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063).

## ◆ afterRestore()

| void PropertyExpressionEngine::afterRestore  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Called at the beginning of
[Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5)

This function is called without dependency sorting, because some types of link
property can only reconstructs the linking information inside this function.

One example use case of this function is
[PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html "the Link
Property with sub elements This property links an object and a defined
sequence of sub eleme...") that uses
[afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1
"Called at the beginning of Document::afterRestore\(\)") to parse and restore
subname references, which may contain sub-object reference from external
document, and there will be special mapping required during object import.

Another example is
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
which only parse the restored expression in
[afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1
"Called at the beginning of Document::afterRestore\(\)"). The reason, in
addition to subname mapping like
[PropertyLinkSub](../../d3/d76/classApp_1_1PropertyLinkSub.html "the Link
Property with sub elements This property links an object and a defined
sequence of sub eleme..."), is that it can handle document name adjustment as
well. It internally relies on
[PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html "Link to an
\(sub\)object in the same or different document.") to store the external
document path for external linking. When the external document is restored,
its internal name may change due to name conflict with existing documents.
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
can now auto adjust external references without any problem.

Reimplemented from
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a00e6240a9cf8e5b7dbf0cf287cbd4db1).

References
[App::PropertyXLinkContainer::afterRestore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a00e6240a9cf8e5b7dbf0cf287cbd4db1),
[AtomicPropertyChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a94bfe6bb9050c7eaf7f379b6bfcc3c5c),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::ObjectIdentifier::parse()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a067a142eca99580ead933730b95a075b),
[App::Expression::parse()](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97),
and
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab0b09b63154afba2b723637afed44276).

## ◆ canonicalPath()

| [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) PropertyExpressionEngine::canonicalPath  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _p_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Create a canonical object identifier of the given object _p_.

Parameters

     p| ObjectIndentifier   
---|---  
  
Returns

    New [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a7a970c03b5e610df341e5cf464100523).

References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

Referenced by
[getPathValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a5bc043e806eede3b4df9d21cbc2f44ef),
[renameExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a02fc7fcac9d0638d3e2385eb88b6cedc),
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1),
and
[validateExpression()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa259d698d63c151f459f14483346639a).

## ◆ Copy()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyExpressionEngine::Copy  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Returns a new copy of the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#a1ca3b1249f2e3b7fcd29308e72ba76de).

References
[PropertyExpressionEngine()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa6da2921c13a1bb1dc2949fa9b762057).

## ◆ CopyOnImportExternal()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyExpressionEngine::CopyOnImportExternal  | ( | const std::map< std::string, std::string > & | _nameMap_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Return a copy of the property if any changes caused by importing external
linked object.

Parameters

     nameMap| a map from the original external object name to the imported new object name  
---|---  
  
Returns

    Returns a copy of the property with the updated link reference if affected. The copy will later be assgiend to this property by calling its [Paste()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46 "Paste the value from the property \(mainly for Undo/Redo and transactions\)"). 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ab29ca627684ca9a3ed573a24eb8da131).

## ◆ CopyOnLabelChange()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyExpressionEngine::CopyOnLabelChange  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | const std::string & | _ref_ ,   
|  | const char *  | _newLabel_  
| ) | |  const  
overridevirtual  
  
Update object label reference in this property.

Parameters

     obj| the object owner of the changing label   
---|---  
ref| subname reference to old label  
newLabel| the future new label  
  
Returns

    Returns a copy of the property if its link reference is affected. The copy will later be assgiend to this property by calling its [Paste()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46 "Paste the value from the property \(mainly for Undo/Redo and transactions\)"). 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a0d1a5adbda3ed0d03313b8827548c1d6).

## ◆ CopyOnLinkReplace()

| [Property](../../d0/da9/classApp_1_1Property.html) * PropertyExpressionEngine::CopyOnLinkReplace  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _parent_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |  const  
overridevirtual  
  
Return a copy of the property if the link replacement affects this property.

Parameters

     owner| the parent object whose link property is to be replace. Note that The parent may not be the container of this property. [Link](../../df/d9b/classApp_1_1Link.html) sub property can use this opportunity to adjust its relative links.   
---|---  
oldObj| object to be replaced  
newObj| object to replace with  
  
Returns

    Return a copy of the property that is adjusted for the link replacement operation. 

Implements
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#ad21232bfd601a848542b503d73d14a9c).

## ◆ depsAreTouched()

[bool](../../d9/db9/classbool.html) PropertyExpressionEngine::depsAreTouched  | ( | | ) |  const  
---|---|---|---|---  
  
Determine whether any dependencies of any of the registered expressions have
been touched.

Returns

    True if at least on dependency has been touched. 

## ◆ execute()

[DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) * App::PropertyExpressionEngine::execute  | ( | [ExecuteOption](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329) | _option_ = `[ExecuteAll](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329a262f9fa9c130a157bc5f6c6d87b4b478)`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) *  | _touched_ = `nullptr`  
| ) | |   
  
Evaluate the expressions.

Compute and update values of all registered expressions.

Parameters

     option| execution option, see ExecuteOption.  
---|---  
  
Returns

    StdReturn on success. 

References
[App::Property::EvalOnRestore](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014ac1036b7face30993fb92e8ffd37d2636),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::Property::getFullName()](../../d0/da9/classApp_1_1Property.html#a0b1289a60e57856c8dae70fafd619dd2),
[App::Property::getPathValue()](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea),
[App::isAnyEqual()](../../dd/dc2/namespaceApp.html#a47e6cc4b0e580ca6aa40e29134ebac75),
[App::Prop_Transient](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a6eefec5f03fa1d639e7fc26c5804ccf6),
[App::Property::setPathValue()](../../d0/da9/classApp_1_1Property.html#ada48246972a8f828fb73280f5dd9ce22),
[App::DocumentObject::StdReturn](../../d2/de4/classApp_1_1DocumentObject.html#af53a1c6a086c5dfe228aaefeeb7316d2),
and
[App::Property::Transient](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a14e77d5a09c2b0796490e697b68560e5).

Referenced by
[draftobjects.facebinder.Facebinder::addSubobjects()](../../d9/d57/classdraftobjects_1_1facebinder_1_1Facebinder.html#a50c77c202a034ce7109bb93322ff6e4e),
[PathScripts.PathDressupDogbone.ObjectDressup::boneStateList()](../../d5/dfa/classPathScripts_1_1PathDressupDogbone_1_1ObjectDressup.html#af7788dd97e3ca711047ebc4472cf9f21),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
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
[draftobjects.pathtwistedarray.PathTwistedArray::onDocumentRestored()](../../da/d1a/classdraftobjects_1_1pathtwistedarray_1_1PathTwistedArray.html#a780c1e365112f239b177875caa78103b),
and
[Sketcher::SketchObject::setExpression()](../../d9/dad/classSketcher_1_1SketchObject.html#ad328e83eeb43879902e8fb12f35a7be6).

## ◆ getExpressions()

| std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), const [App::Expression](../../dc/d5c/classApp_1_1Expression.html) * > PropertyExpressionEngine::getExpressions  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Implements
[App::PropertyExpressionContainer](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a31e577465b52bca4b154627ef8220f9a).

Referenced by
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
and
[Spreadsheet::Sheet::updateBindings()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a0096c4f2015e803cc39270f61aa028fb).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) PropertyExpressionEngine::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Estimate memory size of this property.

\fixme Should probably return something else than 0.

Returns

    Size of object. 

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a933a44c77e539e1942227d1f266d3330).

## ◆ getPathsToDocumentObject()

void PropertyExpressionEngine::getPathsToDocumentObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | std::vector< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_  
| ) | |  const  
  
Find paths to document object.

Parameters

     obj| [Document](../../d8/d3e/classApp_1_1Document.html "The document class.") object   
---|---  
paths| Object identifier  
  
References
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063).

## ◆ getPathValue()

| const boost::any PropertyExpressionEngine::getPathValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
Get expression for _path_.

Parameters

     path| ObjectIndentifier to query for.   
---|---  
  
Returns

    [Expression](../../dc/d5c/classApp_1_1Expression.html "Base class for expressions.") for _path_ , or empty boost::any if not found. 

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea).

References
[canonicalPath()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * PropertyExpressionEngine::getPyObject  | ( | void  | | ) |   
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

## ◆ hasSetValue()

| void PropertyExpressionEngine::hasSetValue  | ( | void  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
Gets called by all
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab0b09b63154afba2b723637afed44276)
methods after the value has changed.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763).

References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[App::ObjectIdentifier::getDep()](../../dd/d13/classApp_1_1ObjectIdentifier.html#ad17db8546af0eff5ebf0bda00c7fd948),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::PropertyLinkBase::hasSetValue()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7104d851d2fbf4be593c68edeecae763),
[App::DocumentObject::isRestoring()](../../d2/de4/classApp_1_1DocumentObject.html#ac2d5c9ca4c67cbb6dd7c22a71ce85da0),
[App::PropertyLinkBase::LinkDetached](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a1cde30375920294221bfa79025669f5facbc01e4b149e5b3049e9916b0181a7da),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[App::PropertyLinkBase::registerLabelReferences()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a513f32162e505cf9fa6cad8a2d234a1f),
[App::PropertyLinkBase::testFlag()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a7aecf32bcda9d645f8a37ece5c3598ef),
[App::PropertyLinkBase::unregisterElementReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29),
and
[App::PropertyXLinkContainer::updateDeps()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a83acea46b0d063043f43d99de26dfe29).

Referenced by
[renameExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a02fc7fcac9d0638d3e2385eb88b6cedc).

## ◆ numExpressions()

size_t PropertyExpressionEngine::numExpressions  | ( | | ) |  const  
---|---|---|---|---  
  
Number of expressions managed by this object.

Returns

    Number of expressions. 

## ◆ onContainerRestored()

| void PropertyExpressionEngine::onContainerRestored  | ( | | ) |   
---|---|---|---|---  
overridevirtual  
  
Called before calling
[DocumentObject::onDocumentRestored()](../../d2/de4/classApp_1_1DocumentObject.html#a0ee8399fa0b176c64895150691a4b604
"get called after a document has been fully restored")

This function is called after finished calling
[Property::afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)") of all properties of
objects. By then, the object dependency information is assumed ready. So,
unlike
[Property::afterRestore()](../../d0/da9/classApp_1_1Property.html#aceccc5747a2632f02391db3c714cb64f
"Called at the beginning of Document::afterRestore\(\)"), this function is
called on objects with dependency order.

Reimplemented from
[App::Property](../../d0/da9/classApp_1_1Property.html#a724e44690754d6abaff38d3131420225).

References
[App::PropertyLinkBase::unregisterElementReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29).

## ◆ onRelabeledDocument()

| void PropertyExpressionEngine::onRelabeledDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Implements
[App::PropertyExpressionContainer](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a09ea603415b50e5604c1551cf597a6f2).

## ◆ Paste()

| void PropertyExpressionEngine::Paste  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) & | _from_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Paste the value from the property (mainly for Undo/Redo and transactions)

Implements
[App::Property](../../d0/da9/classApp_1_1Property.html#acb7098807cc467d1ddda0adf4e5299be).

References
[AtomicPropertyChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a94bfe6bb9050c7eaf7f379b6bfcc3c5c),
and
[expressionChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a).

## ◆ referenceChanged()

| [bool](../../d9/db9/classbool.html) PropertyExpressionEngine::referenceChanged  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Test if the element reference has changed after restore.

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#af56b87f577368963c8aeec5a5fc74ee0).

## ◆ renameExpressions()

void PropertyExpressionEngine::renameExpressions  | ( | const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_| ) |   
---|---|---|---|---|---  
  
Rename paths based on _paths_.

Parameters

     paths| Map with current and new object identifier.   
---|---  
  
References
[App::Property::aboutToSetValue()](../../d0/da9/classApp_1_1Property.html#ac295b40ec9fa6fa180c707149329391d),
[canonicalPath()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09),
[expressionChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a),
and
[hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723).

Referenced by
[Sketcher::SketchObject::constraintsRenamed()](../../d9/dad/classSketcher_1_1SketchObject.html#aac2c8322e53a7823d1940ac93c58a87a).

## ◆ renameObjectIdentifiers()

void PropertyExpressionEngine::renameObjectIdentifiers  | ( | const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_| ) |   
---|---|---|---|---|---  
  
Rename object identifiers in the registered expressions.

Parameters

     paths| Map with current and new object identifiers.   
---|---  
  
## ◆ Restore()

| void PropertyExpressionEngine::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a69fd5b40c21af75af2a9958e2d22577e
"This method is used to save properties to an XML document.") written
information. Again the Vector as an example:

void
[PropertyVector::Restore](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c
"This method is used to restore properties from an XML
document.")([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The
XML reader class This is an important helper class for the store and retrieval
system of objects ...") &reader)

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

Reimplemented from
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4).

References
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsFloat()](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
and
[App::PropertyXLinkContainer::Restore()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#a2f32dfad13ae36382af52ed8a3bfbbb4).

## ◆ Save()

| void PropertyExpressionEngine::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[App::PropertyXLinkContainer](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676).

References
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
[App::PropertyXLinkContainer::Save()](../../d3/dcc/classApp_1_1PropertyXLinkContainer.html#aab19b94bd90c70d4fc9d1e21a1383676),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

## ◆ setExpressions()

| void PropertyExpressionEngine::setExpressions  | ( | std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ExpressionPtr](../../dd/dc2/namespaceApp.html#a87d84b6ef4dda5737e574e95320bc07f) > && | _exprs_| ) |   
---|---|---|---|---|---  
overridevirtual  
  
Implements
[App::PropertyExpressionContainer](../../db/da0/classApp_1_1PropertyExpressionContainer.html#a979ee6293a523dc1f82e074acc5e8462).

References
[AtomicPropertyChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a94bfe6bb9050c7eaf7f379b6bfcc3c5c),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab0b09b63154afba2b723637afed44276).

## ◆ setPyObject()

| void PropertyExpressionEngine::setPyObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e).

## ◆ setValidator()

void App::PropertyExpressionEngine::setValidator  | ( | [ValidatorFunc](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ab389bbc469930e2d1f43b3f29b3d3dac) | _f_| ) |   
---|---|---|---|---|---  
  
## ◆ setValue() [1/2]

void App::PropertyExpressionEngine::setValue  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[Sketcher::SketchObject::constraintsRemoved()](../../d9/dad/classSketcher_1_1SketchObject.html#a97732ef24ca9fb3fa18710fe87864ada),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
and
[setExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af0f2f778f8e840efb832ef621441a3e9).

## ◆ setValue() [2/2]

void PropertyExpressionEngine::setValue  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | std::shared_ptr< [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > | _expr_  
| ) | |   
  
Set expression with optional comment for _path_.

Parameters

     path| [Path](../../da/d2a/classApp_1_1Path.html "Base class of all geometric document objects.") to update   
---|---  
expr| New expression  
comment| Optional comment.  
  
References
[AtomicPropertyChange](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a94bfe6bb9050c7eaf7f379b6bfcc3c5c),
[canonicalPath()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09),
[expressionChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a),
[App::Property::getPathValue()](../../d0/da9/classApp_1_1Property.html#a32fb9eb4a5bc58e3afce4276a888c5ea),
[App::ObjectIdentifier::getProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#afc4aaa90cb65a96c83fd931134d26b24),
and
[validateExpression()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#aa259d698d63c151f459f14483346639a).

## ◆ updateElementReference()

| void PropertyExpressionEngine::updateElementReference  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _feature_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _reverse_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _notify_ = `false`  
| ) | |   
overridevirtual  
  
[Link](../../df/d9b/classApp_1_1Link.html) type property interface APIs These
APIs are moved here so that any type of property can have the property link
behavior, e.g.

the
[PropertyExpressionEngine](../../db/d34/classApp_1_1PropertyExpressionEngine.html)
Called to update the element reference of this link property

See also

    _updateElementReference() 

Reimplemented from
[App::PropertyLinkBase](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a6447c82dc0b81cea703a9a235a2448c3).

References
[expressionChanged](../../db/d34/classApp_1_1PropertyExpressionEngine.html#ad0a0e91de15a6a85545f19f96c47b19a),
[App::Property::getContainer()](../../d0/da9/classApp_1_1Property.html#aba33cf49df9c683abb66c7b6ed51e063),
[femsolver.signal::notify()](../../dc/de2/group__FEM.html#ga6389100f2d948a9fe194b395ac11f82c),
[App::DocumentObject::onUpdateElementReference()](../../d2/de4/classApp_1_1DocumentObject.html#a9c5de491fd49f9534bd828fea6d7d3b1),
and
[App::PropertyLinkBase::unregisterElementReference()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#aa5ec8a97f53a0928274e9d585a50fd29).

## ◆ validateExpression()

std::string PropertyExpressionEngine::validateExpression  | ( | const [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) & | _path_ ,   
---|---|---|---  
|  | std::shared_ptr< const [App::Expression](../../dc/d5c/classApp_1_1Expression.html) > | _expr_  
| ) | |  const  
  
Validate the given path and expression.

Parameters

     path| Object Identifier for expression.   
---|---  
expr| [Expression](../../dc/d5c/classApp_1_1Expression.html "Base class for
expressions.") tree.  
  
Returns

    Empty string on success, error message on failure. 

References
[canonicalPath()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a21b797539c8eef459b505be492c17f09),
[App::ObjectIdentifier::getDocumentObject()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a76e0d3d2cbbf5db98d33a9d0917a15ff),
and
[App::DocumentObject::getInListEx()](../../d2/de4/classApp_1_1DocumentObject.html#ad99e8f94b3cb435ad9346dd8616a122e).

Referenced by
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
and
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1).

## Friends And Related Function Documentation

## ◆ AtomicPropertyChange

| [friend](../../d7/d23/classfriend.html) class AtomicPropertyChange  
---  
friend  
  
Referenced by
[adjustLink()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a6ef128439add23206d190bedd151f02e),
[afterRestore()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0af83cfaff9c7f838e978e2a0634e1b1),
[Paste()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46),
[setExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#af0f2f778f8e840efb832ef621441a3e9),
and
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1).

## Member Data Documentation

## ◆ expressionChanged

boost::signals2::signal<void (const
[App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) &)>
App::PropertyExpressionEngine::expressionChanged  
---  
  
signal called when an expression was changed

Referenced by
[adjustLink()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a6ef128439add23206d190bedd151f02e),
[Gui::ExpressionBinding::bind()](../../dc/d5a/classGui_1_1ExpressionBinding.html#aba7b2c918c04b6e3f589e53876cdb761),
[Paste()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7f06f64a7f7fc8b42cc72470e96b6c46),
[renameExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a02fc7fcac9d0638d3e2385eb88b6cedc),
[setValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a8297f68f6a223f63bd084feb727ddbe1),
and
[updateElementReference()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a00a63354dd2052c675de28c01ff70362).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/PropertyExpressionEngine.h
  * FreeCAD/src/App/PropertyExpressionEngine.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

