---
url: https://freecad.github.io/SourceDoc/d8/d00/classApp_1_1TransactionalObject.html
scraped_at: 2025-09-08T14:57:10.149280
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html)

[List of all members](../../d5/d4b/classApp_1_1TransactionalObject-members.html) | Public Member Functions | Protected Member Functions

App::TransactionalObject Class Reference

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of transactional objects.
[More...](../../d8/d00/classApp_1_1TransactionalObject.html#details)

`#include <TransactionalObject.h>`

##  Public Member Functions  
  
---  
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
  
virtual void | [onChanged](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d) (const [Property](../../d0/da9/classApp_1_1Property.html) *) override  
| get called by the container when a property has changed
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d)  
  
virtual void | [Save](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5)  
  
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
  
  
##  Protected Member Functions  
  
---  
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
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)  
typedef std::map< [Base::Type](../../dc/dee/classBase_1_1Type.html), [App::Extension](../../d8/dc7/classApp_1_1Extension.html) * >::iterator | [ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f)  
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
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
static const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [getPropertyDataPtr](../../d5/d48/classApp_1_1PropertyContainer.html#a8649f534ecaa91393925fa514ed29e4b) (void)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html) | [dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99)  
  
## Detailed Description

[Base](../../db/d07/namespaceBase.html "Basic structures used by other FreeCAD
components \(C++ API\)") class of transactional objects.

## Constructor & Destructor Documentation

## ◆ TransactionalObject()

TransactionalObject::TransactionalObject  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Constructor.

## ◆ ~TransactionalObject()

| TransactionalObject::~TransactionalObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ detachFromDocument()

| const char * TransactionalObject::detachFromDocument  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#a18685d36a70739a43912aef660ae44fe),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a00c6b0fe1d6e386ae90e3b0e917b1556).

Referenced by
[App::Transaction::addObjectNew()](../../de/dbf/classApp_1_1Transaction.html#a33d72374a75b0138c6a5c9d71c858cff).

## ◆ isAttachedToDocument()

| [bool](../../d9/db9/classbool.html) TransactionalObject::isAttachedToDocument  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#af0c800cf501791cc2d47619d6457b978),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a162f664e8fe151ffa44f77b0bd34877d).

## ◆ onBeforeChangeProperty()

| void TransactionalObject::onBeforeChangeProperty  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_  
| ) | |   
protected  
  
Referenced by
[Gui::ViewProviderDocumentObject::onBeforeChange()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a8951ceface32a935d5305d79aa1626eb).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/TransactionalObject.h
  * FreeCAD/src/App/TransactionalObject.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

