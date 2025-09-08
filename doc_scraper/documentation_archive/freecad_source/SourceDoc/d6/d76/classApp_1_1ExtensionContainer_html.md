---
url: https://freecad.github.io/SourceDoc/d6/d76/classApp_1_1ExtensionContainer.html
scraped_at: 2025-09-08T14:54:41.561076
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)

[List of all members](../../d1/da5/classApp_1_1ExtensionContainer-members.html) | Public Types | Public Member Functions

App::ExtensionContainer Class Reference

Container which can hold extensions.
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#details)

`#include <ExtensionContainer.h>`

##  Public Types  
  
---  
typedef std::map< [Base::Type](../../dc/dee/classBase_1_1Type.html), [App::Extension](../../d8/dc7/classApp_1_1Extension.html) * >::iterator | [ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f)  
  
##  Public Member Functions  
  
---  
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
Access properties  
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
  
  
##  Additional Inherited Members  
  
---  
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
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html) | [dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99)  
  
## Detailed Description

Container which can hold extensions.

In FreeCAD normally inheritance is a chain, it is not possible to use multiple
inheritance. The reason for this is that all objects need to be exposed to
python, and it is basically impossible to handle multiple inheritance in the
C-API for python extensions. Also using multiple parent classes in python is
currently not possible with the default object approach.

The concept of extensions allow to circumvent those problems. Extensions are
FreeCAD objects which work like normal objects in the sense that they use
properties and class methods to define their functionality. However, they are
not exposed as individual usable entities but are used to extend other
objects. A extended object gets all the properties and methods of the
extension. Therefore it is like c++ multiple inheritance, which is indeed used
to achieve this on c++ side, but provides a few important additional
functionalities:

  * [Property](../../d0/da9/classApp_1_1Property.html "Base class of all properties This is the father of all properties.") persistence is handled, save and restore work out of the box
  * The objects python API gets extended too with the extension python API
  * Extensions can be added from c++ and python, even from both together

The interoperability with python is highly important, as in FreeCAD all
functionality should be as easily accessible from python as from c++. To
ensure this, and as already noted, extensions can be added to a object from
python. However, this means that it is not clear from the c++ object type if
an extension was added or not. If added from c++ it becomes clear in the type
due to the use of multiple inheritance. If added from python it is a runtime
extension and not visible from type. Hence querying existing extensions of an
object and accessing its methods works not by type casting but by the
interface provided in
[ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html
"Container which can hold extensions."). The default workflow is to query if
an extension exists and then get the extension object. No matter if added from
python or c++ this interface works always the same.

if
([object](../../dc/dd8/classobject.html)->hasExtension(GroupExtension::getClassTypeId()))
{

[App::GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)* group =
object->getExtensionByType<[GroupExtension](../../da/d3a/classApp_1_1GroupExtension.html)>();

group->[hasObject](../../da/d3a/classApp_1_1GroupExtension.html#afdaf65320a0ea5c49b2e66b63fa8079a
"Checks whether the object obj is part of this group.")(...);

}

To add a extension to an object, it must comply to a single restriction: it
must be derived from
[ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html
"Container which can hold extensions."). This is important to allow adding
extensions from python and also to access the universal extension API. As
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") itself derives from
[ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html
"Container which can hold extensions.") this should be the case automatically
in most circumstances.

Note that two small boilerplate changes are needed next to the multiple
inheritance when adding extensions from c++.

  1. It must be ensured that the property and type registration is aware of the extensions by using special macros.
  2. The extensions need to be initialised in the constructor

Here is a working example:

class AppExport [Part](../../d2/db9/namespacePart.html "AttachExtensionh, .cpp
contain a extension class to derive other features from, to make them
attachab...") : public
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class
of all Classes handled in the Document."), public App::FirstExtension, public
App::SecondExtension {

PROPERTY_HEADER_WITH_EXTENSIONS([App::Part](../../da/d8d/classApp_1_1Part.html
"Base class of all geometric document objects."));

};

PROPERTY_SOURCE_WITH_EXTENSIONS([App::Part](../../da/d8d/classApp_1_1Part.html
"Base class of all geometric document objects."),
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class
of all Classes handled in the Document."))

[Part::Part](../../da/d8d/classApp_1_1Part.html#a038ec889e68c1f995f33152164985ea9
"Constructor.")(void) {

FirstExtension::initExtension(this);

SecondExtension::initExtension(this);

}

From python adding an extension is easier, it must be simply registered to a
document object at object initialisation like done with properties. Note that
the special python extension objects need to be added, not the c++ objects.
Normally the only difference in name is the additional "Python" at the end of
the extension name.

class Test():

__init(self)__:

registerExtension("App::FirstExtensionPython", self)

registerExtension("App::SecondExtensionPython", self)

Extensions can provide methods that should be overridden by the extended
object for customisation of the extension behaviour. In c++ this is as simple
as overriding the provided virtual functions. In python a class method must be
provided which has the same name as the method to override. This method must
not necessarily be in the object that is extended, it must be in the object
which is provided to the "registerExtension" call as second argument. This
second argument is used as a proxy and enqueired if the method to override
exists in this proxy before calling it.

For information on howto create extension see the documentation of
[Extension](../../d8/dc7/classApp_1_1Extension.html "Base class for all
extension that can be added to a DocumentObject.")

## Member Typedef Documentation

## ◆ ExtensionIterator

typedef
std::map<[Base::Type](../../dc/dee/classBase_1_1Type.html),[App::Extension](../../d8/dc7/classApp_1_1Extension.html)*>::iterator
[App::ExtensionContainer::ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f)  
---  
  
## Constructor & Destructor Documentation

## ◆ ExtensionContainer()

ExtensionContainer::ExtensionContainer  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~ExtensionContainer()

| ExtensionContainer::~ExtensionContainer  | ( | | ) |   
---|---|---|---|---  
virtual  
  
## Member Function Documentation

## ◆ extensionBegin()

[ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f) App::ExtensionContainer::extensionBegin  | ( | | ) |   
---|---|---|---|---  
  
## ◆ extensionEnd()

[ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f) App::ExtensionContainer::extensionEnd  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getExtension() [1/2]

[Extension](../../d8/dc7/classApp_1_1Extension.html) * ExtensionContainer::getExtension  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _t_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _derived_ = `true`,   
|  | [bool](../../d9/db9/classbool.html) | _no_except_ = `false`  
| ) | |  const  
  
Referenced by
[restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab).

## ◆ getExtension() [2/2]

[Extension](../../d8/dc7/classApp_1_1Extension.html) * ExtensionContainer::getExtension  | ( | const std::string & | _name_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getExtensionByType()

template<typename [ExtensionT](../../df/d73/classExtensionT.html) >

[ExtensionT](../../df/d73/classExtensionT.html) * App::ExtensionContainer::getExtensionByType  | ( | [bool](../../d9/db9/classbool.html) | _no_except_ = `false`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _derived_ = `true`  
| ) | |  const  
  
Referenced by
[PartGui::TaskDlgAttacher::accept()](../../db/d08/classPartGui_1_1TaskDlgAttacher.html#a52815a44f802225b7d21307dc9535346),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[Gui::ViewProviderGroupExtension::extensionCanDropObject()](../../d2/d69/classGui_1_1ViewProviderGroupExtension.html#a147fbe325cf8c816be9cdcaca1c5247a),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionClaimChildren()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#ad44762aa4bd4aa7ae5734d717c8925ed),
[Gui::ViewProviderGroupExtension::extensionClaimChildren()](../../d2/d69/classGui_1_1ViewProviderGroupExtension.html#a93c3572e5487daf68a952384be4130bb),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionClaimChildren3D()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#af55e188903f5caabbb3e86a5768731d7),
[Gui::ViewProviderGroupExtension::extensionHide()](../../d2/d69/classGui_1_1ViewProviderGroupExtension.html#ad91d9fd2d4eb6705e60e991c87f44d37),
[PartGui::ViewProviderAttachExtension::extensionMergeColorfullOverlayIcons()](../../d7/d61/classPartGui_1_1ViewProviderAttachExtension.html#ac3867c4ff9cf73edad06fa5d8f1a9606),
[Gui::ViewProviderGroupExtension::extensionOnDelete()](../../d2/d69/classGui_1_1ViewProviderGroupExtension.html#a4a9fd1abd4627d622c922839bf9eeaa2),
[Gui::ViewProviderGroupExtension::extensionShow()](../../d2/d69/classGui_1_1ViewProviderGroupExtension.html#aeccf8cf63738a6a6eb1557d09e393d00),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionUpdateData()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#aeb7b059cc68cc0d3705101a1fbcda918),
[PartGui::ViewProviderAttachExtension::extensionUpdateData()](../../d7/d61/classPartGui_1_1ViewProviderAttachExtension.html#a26d1e4000673dfcad3fc7c572768b80f),
[Gui::ViewProviderOriginGroupExtension::extensionUpdateData()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a4ee2dc9517fc63b7f3e0392aa9943a73),
[Gui::LinkInfo::get()](../../d4/da4/classGui_1_1LinkInfo.html#a59c40ce8de9324645da7fb85fa95a8b2),
[Gui::ViewProviderLink::getLinkExtension()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab75a56312dd387c3d22c1e3b17ba84cc),
[PartDesignGui::isFeatureMovable()](../../dc/d12/namespacePartDesignGui.html#a6b3f9e577dd13e884d8aca2e0ce6a6c8),
[Gui::LinkInfo::release()](../../d4/da4/classGui_1_1LinkInfo.html#a8ebcbfd5e9ce132da454913d09d07c96),
[PartDesignGui::relinkToOrigin()](../../dc/d12/namespacePartDesignGui.html#a04b9ca5c57afc44a5ab6f8bc71f9a681),
[Gui::ViewProviderOriginGroupExtension::slotChangedObjectApp()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#ab5c62634ee1ddb91f4f8eee70cf16e99),
[Gui::ViewProviderOriginGroupExtension::slotChangedObjectGui()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a302efc5ec7a5b6a38ba690fbb2ba18af),
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
[Gui::ViewProviderLink::updateLinks()](../../d6/d59/classGui_1_1ViewProviderLink.html#a5e2b967d8593728e9373a139c1b7e2fc),
and
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e).

## ◆ getExtensionsDerivedFrom()

std::vector< [Extension](../../d8/dc7/classApp_1_1Extension.html) * > ExtensionContainer::getExtensionsDerivedFrom  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _type_| ) |  const  
---|---|---|---|---|---  
  
References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ getExtensionsDerivedFromType()

template<typename [ExtensionT](../../df/d73/classExtensionT.html) >

std::vector< [ExtensionT](../../df/d73/classExtensionT.html) * > App::ExtensionContainer::getExtensionsDerivedFromType  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getPropertyByName()

| [Property](../../d0/da9/classApp_1_1Property.html) * ExtensionContainer::getPropertyByName  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
find a property by its name

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2).

Reimplemented in
[Spreadsheet::Sheet](../../d0/da8/classSpreadsheet_1_1Sheet.html#af40fb7fff53d89116462ae1816d43478),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a17a9af10ec6818cb73aff3e1fdc9c5f7).

References
[App::PropertyContainer::getPropertyByName()](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2).

Referenced by
[FemGui::TaskDlgFemConstraintFluidBoundary::accept()](../../da/d17/classFemGui_1_1TaskDlgFemConstraintFluidBoundary.html#a92106711f12fb0fb783c7e411d8f3923),
[MeshGui::ViewProviderMesh::canHighlightColors()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a4ecd94eb5619800f1ba36eb7648552bf),
[MeshGui::ViewProviderMeshCurvature::curvatureInfo()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#aa2902a6b29f9d107136899cdbf8eca28),
[App::FunctionExpression::evalAggregate()](../../d6/da3/classApp_1_1FunctionExpression.html#ad9267dc1decdafaaa129f1bd51de07e4),
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
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[App::LinkBaseExtension::extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
[InspectionGui::ViewProviderInspection::getIcon()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a76d57438c1350bd9a432557f0c23dc5e),
[TechDraw::DrawProjGroupItem::getLegacyX()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a1bc574099e0939f27ba53b10f20d147f),
[Gui::ViewProviderLink::getPropertyByName()](../../d6/d59/classGui_1_1ViewProviderLink.html#a17a9af10ec6818cb73aff3e1fdc9c5f7),
[App::ObjectIdentifier::getPyValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a51896520089a0ba883333f2a6bcb56c6),
[Spreadsheet::PropertySheet::getPyValue()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a345cfadf9398442bb9a94bd6d1fc10f0),
[TechDraw::ShapeExtractor::getShapesFromObject()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#a4043c946e78f533e4f060cb3b87b5691),
[App::ObjectIdentifier::getValue()](../../dd/d13/classApp_1_1ObjectIdentifier.html#aac60575eac174a3d02a329a96ed93e0c),
[TechDraw::DrawViewPart::getXDirection()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a0e16d51e16c7c55b75f5cfa00c037fd0),
[TechDraw::DrawProjGroupItem::getXDirection()](../../da/d03/classTechDraw_1_1DrawProjGroupItem.html#a86b744ee5d2b7ff5de819b0f23488498),
[TechDraw::DrawViewSection::getXDirection()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a0cefd62711bac9ca360a2ffc37731820),
[MeshGui::ViewProviderMesh::highlightColors()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a0877e142c07a2d4419b39cb8b01c9f85),
[InspectionGui::ViewProviderInspection::inspectDistance()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac0352eb6e4af339e08975b253269b0ab),
[App::RangeExpression::isTouched()](../../da/d8b/classApp_1_1RangeExpression.html#a93b55327da44e753b97eca89a2ec8c7c),
[Gui::ViewProviderAnnotationLabel::onChanged()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[App::ObjectIdentifier::resolveProperty()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9341d67d505f43d14f829d379ffed02e),
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[InspectionGui::ViewProviderInspection::setDistances()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a44c21c9eb69fa551a912211602ee0e70),
[App::LinkBaseExtension::setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e),
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83),
and
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239).

## ◆ getPropertyDocumentation() [1/2]

| const char * ExtensionContainer::getPropertyDocumentation  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50).

References
[App::PropertyContainer::getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912).

## ◆ getPropertyDocumentation() [2/2]

| const char * ExtensionContainer::getPropertyDocumentation  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912).

References
[App::PropertyContainer::getPropertyDocumentation()](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912).

## ◆ getPropertyGroup() [1/2]

| const char * ExtensionContainer::getPropertyGroup  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a).

References
[App::PropertyContainer::getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356).

## ◆ getPropertyGroup() [2/2]

| const char * ExtensionContainer::getPropertyGroup  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356).

References
[App::PropertyContainer::getPropertyGroup()](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356).

## ◆ getPropertyList()

| void ExtensionContainer::getPropertyList  | ( | std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > & | _List_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get all properties of the class (including properties of the parent)

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a).

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a849803da0f88ed79a6d4d24ec0e66b01).

References
[App::PropertyContainer::getPropertyList()](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a).

Referenced by
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[PartDesignGui::ViewProvider::setBodyMode()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a832d902f47a05424c29d1163b0155fb9),
[PartDesign::SubShapeBinder::setupCopyOnChange()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a3f0c1dcf0ed5800b1865c2c42f4e25f7),
[App::LinkBaseExtension::setupCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a788171077d0b1dafb936523e315b4f0e),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ getPropertyMap()

| void ExtensionContainer::getPropertyMap  | ( | std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > & | _Map_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get all properties of the class (including properties of the parent)

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8).

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a7190982dc42a5f66d3740ff5df29a294).

References
[App::PropertyContainer::getPropertyMap()](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8).

Referenced by
[PointsGui::ViewProviderScattered::cut()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#a6e93ecaa9bbca01c9cd9c294ba22f38c),
[MeshGui::ViewProviderMesh::getColorProperty()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ab3eae9bc83c8bec9cc875f7f548a9f2b),
[PointsGui::ViewProviderPoints::getDisplayModes()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a2d67beeb09773e4dc1ee1d2d00a2772d),
[Gui::ViewProviderLink::getPropertyMap()](../../d6/d59/classGui_1_1ViewProviderLink.html#a7190982dc42a5f66d3740ff5df29a294),
[Gui::PropertyView::onTimer()](../../d8/d18/classGui_1_1PropertyView.html#aa53958cefcade980c3ffe795f787d6de),
[PointsGui::ViewProviderPoints::setDisplayMode()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a6fba67f9c755f7ae29cdfe1eb581b6b1),
[MeshGui::ViewProviderMeshCurvature::setVertexCurvatureMode()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a5f3a5eba7e4ce16c86b37579a2bc4bc4),
and
[Gui::ViewProviderDocumentObject::updateView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae31dde44f114d3e90bb2e1d544f3e442).

## ◆ getPropertyName()

| const char * ExtensionContainer::getPropertyName  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the name of a property

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981).

References
[App::PropertyContainer::getPropertyName()](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981).

Referenced by
[App::TransactionObject::applyChn()](../../d9/d02/classApp_1_1TransactionObject.html#ae828131a91ad93ac2f20a51eeadecf70),
and
[Spreadsheet::SheetObserver::slotChangedObject()](../../db/d2b/classSpreadsheet_1_1SheetObserver.html#afa0379ae388031e7371193ab6c5d6296).

## ◆ getPropertyType() [1/2]

| short [int](../../d1/da0/classint.html) ExtensionContainer::getPropertyType  | ( | const char *  | _name_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4).

References
[App::PropertyContainer::getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510).

## ◆ getPropertyType() [2/2]

| short [int](../../d1/da0/classint.html) ExtensionContainer::getPropertyType  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510).

References
[App::PropertyContainer::getPropertyType()](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510).

Referenced by
[Part::Box::Restore()](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e).

## ◆ hasExtension() [1/2]

[bool](../../d9/db9/classbool.html) ExtensionContainer::hasExtension  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _t_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _derived_ = `true`  
| ) | |  const  
  
Referenced by
[Gui::ViewProviderDocumentObject::canDelete()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af693d465f282457e260eed5092506cf1),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[App::GeoFeatureGroupExtension::extensionGetSubObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a94b2f1db4a467253e0eb0e6936c97b40),
[PartGui::ViewProviderAttachExtension::extensionSetupContextMenu()](../../d7/d61/classPartGui_1_1ViewProviderAttachExtension.html#a881bdd5ca4dc26e051f378275c0765fe),
[PartDesignGui::isFeatureMovable()](../../dc/d12/namespacePartDesignGui.html#a6b3f9e577dd13e884d8aca2e0ce6a6c8),
[registerExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#a007eb07d5313eaa01d14462d7b7d960d),
[PartDesignGui::relinkToOrigin()](../../dc/d12/namespacePartDesignGui.html#a04b9ca5c57afc44a5ab6f8bc71f9a681),
[PartGui::TaskAttacher::TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
and
[Gui::DocumentItem::updateItemSelection()](../../df/d15/classGui_1_1DocumentItem.html#a14563474d7f1a9b2024cd5aa953dcbe4).

## ◆ hasExtension() [2/2]

[bool](../../d9/db9/classbool.html) ExtensionContainer::hasExtension  | ( | const std::string & | _name_| ) |  const  
---|---|---|---|---|---  
  
## ◆ hasExtensions()

[bool](../../d9/db9/classbool.html) ExtensionContainer::hasExtensions  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329),
and
[saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0).

## ◆ onChanged()

| void ExtensionContainer::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
get called by the container when a property has changed

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34).

Reimplemented in
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#a80cc75727e9f349bafe5037842c6fbcf),
[FemGui::ViewProviderFemPostPlaneFunction](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aff4da6a421671244ed9f106adbaee37a),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#aac82db0865d1e2eb55342a84cf91872e),
[Part::Vertex](../../de/d96/classPart_1_1Vertex.html#a9421cb9911928eae246b23f3590bc3ee),
[Part::Line](../../d3/dfe/classPart_1_1Line.html#ab63d1eeff0a1ad1773c06cca1d731017),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#aebecb9c21eca867973512232a720cc63),
[PartDesignGui::ViewProviderDatumCoordinateSystem](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a48324f18ce89cf9a307a32d54e3cfcc3),
[Surface::GeomFillSurface](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#a778fc5826d5950fba6fb6e5a2d2208dd),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a838e11f3f3d9b47452ece92f8057bff1),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#abbbfdc1b1e66ea1ea4ba8a483794161d),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#aa4c52719f57d011b0a4f3bef4c68a016),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a74a77269f6962a4a975229ac51c582c7),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a338b45f77e146a3a179b2f7922de8d8d),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#acad7ad25b7e30c03fc13738bce5db1de),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#a825924c3bb8e3aaed03215ef12867392),
[Gui::ViewProviderAnnotation](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[Gui::ViewProviderGeometryObject](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a55ba8a09c4ee671752b6e88c3561d9e1),
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a86520630c898707677753ccc3877eced),
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a8d87ca622183dd3077563ad3d45c479b),
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
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3d33c13c95f3a907325ad1c399dc5a14),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a13a3a3015d78a539b51f342fa516670c),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#ae95be84201f7f51ce6162468c514e33e),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5d27aeff234b60ec0214c939556b26c5),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[Mesh::Feature](../../dd/dce/classMesh_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[MeshGui::ViewProviderMeshDefects](../../da/d50/classMeshGui_1_1ViewProviderMeshDefects.html#a0d494009344982737533a865b26ce7d4),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[Part::Mirroring](../../dc/dac/classPart_1_1Mirroring.html#aa4148eb536fa6f15fb2fc21f3fe839b4),
[Part::Box](../../dc/d80/classPart_1_1Box.html#a29bcbc46ec0749e4035fffc5117e1723),
[Part::RuledSurface](../../d1/d41/classPart_1_1RuledSurface.html#a143afeec2aafb3207cd29e9ef6fc5934),
[Part::Loft](../../d3/d52/classPart_1_1Loft.html#acc65fe857c50b113cb06e0d092c83fd5),
[Part::Sweep](../../df/dc6/classPart_1_1Sweep.html#a67f346ffecb66556a70c38c9184cdd56),
[Part::Helix](../../df/d49/classPart_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[Part::Spiral](../../d2/d3f/classPart_1_1Spiral.html#a2f38f985d7c148ee3acec62a8358b4b7),
[Part::Wedge](../../d5/dc5/classPart_1_1Wedge.html#a609125d1bc02031accfc330fc2e79d08),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a04a16b5ac49a2b5df31304da0a4318ee),
[PartGui::ViewProviderCustom](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[PartGui::ViewProviderPartReference](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a8af0748ed20158c08efa16db288d3f81),
[PartDesign::Line](../../d0/d2a/classPartDesign_1_1Line.html#a9da12fed7c1a5cfa4af5c06af23c6fff),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#a82dfdf47875b49263a5275ab1ff3c686),
[PartDesign::FeatureBase](../../d2/d7c/classPartDesign_1_1FeatureBase.html#a628a37fc8716ca08f0c67bb727ac3b76),
[PartDesign::DressUp](../../df/de5/classPartDesign_1_1DressUp.html#a7f7a173d69576711009fb17aeb08f6bc),
[PartDesign::Helix](../../d3/d78/classPartDesign_1_1Helix.html#a8f7d2c5809cd60f90231a0350ea5c444),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#a2d2bbe8a83eafdedc73ae1cfa9360758),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a36fd19fd597799ebeccd8eddd104bdf4),
[PartDesignGui::ViewProviderDatumPoint](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ada6d519997cb6ca57d88957962fc1377),
[Path::Feature](../../d5/dd9/classPath_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#a136a80fff5bcb707ecb5c4d308e42c56),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ad91786e290cd4be69ef99a41c85faa32),
[Robot::Edge2TracObject](../../d8/df5/classRobot_1_1Edge2TracObject.html#a3e8b60d7dcc4abe17a0e640a0e0ef5e9),
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#abebfe59d5888146a96594cb7d31ffce8),
[Robot::TrajectoryDressUpObject](../../d6/d95/classRobot_1_1TrajectoryDressUpObject.html#a58ad4466b7239a951a9b9b4d30b7f1d3),
[Robot::TrajectoryObject](../../d7/db5/classRobot_1_1TrajectoryObject.html#aded21cc1ebf027aa6b39e81759687ea3),
[RobotGui::ViewProviderRobotObject](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a41cfa5ba4f24dacf46491cc903e5a715),
[Sandbox::SandboxObject](../../da/dd9/classSandbox_1_1SandboxObject.html#ae3e3d04a08a28cb8060a72df914f3685),
[SketcherGui::ViewProviderCustom](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
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
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#ad13417ef59c1aeb04fbc4fbcc6aa57d2),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a23482323e8ec6da0cb3dd93b00203e73),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a86b7b59890bb041b58c8e5564383e631),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a0387c427509686ba2dff332930fb5efe),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[Gui::ViewProviderPart](../../d9/d6c/classGui_1_1ViewProviderPart.html#a5e76f3437483472cd66247d0eb98aa1a),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a471b5fcc496e5d153b398a0675e2c93e),
[Part::BodyBase](../../da/dc8/classPart_1_1BodyBase.html#aad727053c5bb43ee6f065f3d0b458f16),
[Part::Revolution](../../d3/d17/classPart_1_1Revolution.html#a9940a58886c8d7d0b4b009082d81f14c),
[Part::Feature](../../d7/d7e/classPart_1_1Feature.html#a17178c5bf097534e84b20380ad13563b),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ac5544f9b57ebf2a1b626450200a4bec0),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesign::Body](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[PartDesign::Point](../../da/d0d/classPartDesign_1_1Point.html#a559cef769b27bcf8efeef552583f9aa4),
[PartDesign::Boolean](../../d2/d81/classPartDesign_1_1Boolean.html#a41c675a8b7f2f6e73b95946b99245f12),
[PartDesign::FeaturePrimitive](../../da/d0d/classPartDesign_1_1FeaturePrimitive.html#a86c00f82005801a22585584fb378e4e5),
[PartDesign::ShapeBinder](../../d0/ddd/classPartDesign_1_1ShapeBinder.html#a984513ae894c80494f6a0c3b0725f48f),
[PartDesign::SubShapeBinder](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[PartDesignGui::ViewProviderBoolean](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#ab446d9f6494af864bd745136c7e20439),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ae317a35c18a1f9b333a14655c35eb8dc),
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
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#af947ca7438432b3448358f4ebcf6bbc1),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a1a42e7ea4d5eb17c7e1f536cad241cc3),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#aada265457fade9ade61cbade5aee4f2b),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a498b66c6f2b5af184c95c4a07bc6f98e),
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a7b5d5197907bbf4cc9c65c1004a1da83),
[App::MeasureDistance](../../d7/d61/classApp_1_1MeasureDistance.html#abbccf44662823af983d2786da162cc43),
[App::TextDocument](../../d9/de9/classApp_1_1TextDocument.html#affdf6c8a48df5cea53213040c487e5f8),
and
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#aa9fcfd8db6b2ffdf46274b18b45811cf).

References
[App::PropertyContainer::onChanged()](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[Gui::ViewProvider::onChanged()](../../d3/db3/classGui_1_1ViewProvider.html#a825924c3bb8e3aaed03215ef12867392),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ registerExtension()

void ExtensionContainer::registerExtension  | ( | [Base::Type](../../dc/dee/classBase_1_1Type.html) | _extension_ ,   
---|---|---|---  
|  | [App::Extension](../../d8/dc7/classApp_1_1Extension.html) *  | _ext_  
| ) | |   
  
References
[hasExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#adae9aba02ce19d1611f1bb3447ee936e),
and
[Base::Type::isDerivedFrom()](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7).

Referenced by
[App::Extension::initExtension()](../../d8/dc7/classApp_1_1Extension.html#a1ae201ccac2b97ba9107151b9e507def).

## ◆ Restore()

| void ExtensionContainer::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5
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
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

Reimplemented in
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a2e81a7dc633df4672dac82d4e8e1792a),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[Gui::ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#a4e6bcf20d9aa065b34edc83e9619ba51),
[Part::Box](../../dc/d80/classPart_1_1Box.html#ab559727549919523e5084a642a49479e),
[Part::Circle](../../de/de4/classPart_1_1Circle.html#a31f09d03f0ee6b6f7a9e98b20b7223d4),
[Part::Ellipse](../../d6/d22/classPart_1_1Ellipse.html#a90f7d460c9b3b2d2cf7b07282ad83efd),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#af020d668456d6c40964757726bb9d1aa),
[PartDesign::Plane](../../df/df0/classPartDesign_1_1Plane.html#a0daddf322de5233314e8ec1e5d73f658),
[PartDesign::Fillet](../../d0/d50/classPartDesign_1_1Fillet.html#ab91b894b378df78eb983a34f62c5cc46),
[PartDesign::Hole](../../dd/dd0/classPartDesign_1_1Hole.html#ada1c34ac1dc39bd284a23e440d663312),
[PartDesign::ProfileBased](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a911a7f2f77e2adb2277a344a4ffb33f2),
[PartDesign::Transformed](../../dd/de1/classPartDesign_1_1Transformed.html#a4e823053076cbcb1c6a8add13d191405),
[Points::Feature](../../d8/de3/classPoints_1_1Feature.html#af3c51f0c54d5a9ec82ef35950ce21d83),
[Part::Part2DObject](../../d9/d57/classPart_1_1Part2DObject.html#a24712341d8edfa206b25b21bdda998a2),
[Part::Primitive](../../d2/d31/classPart_1_1Primitive.html#ad739d09a91f363ecaac5bce84d2271f7),
[PartDesign::Chamfer](../../da/d6f/classPartDesign_1_1Chamfer.html#aa7e36b44d9a038c47691655463d2eaf4),
and
[TechDraw::DrawViewDimension](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#afb1057b5d67039082147ba14225f1c82).

References
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
and
[restoreExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab).

Referenced by
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Robot::RobotObject::Restore()](../../db/d51/classRobot_1_1RobotObject.html#a654870e568b07840a79bd2c8e99e50d1),
[App::VRMLObject::Restore()](../../df/df6/classApp_1_1VRMLObject.html#ae08e5863309e25cd88e07e2be87c9f48),
[PartDesign::Fillet::Restore()](../../d0/d50/classPartDesign_1_1Fillet.html#ab91b894b378df78eb983a34f62c5cc46),
[PartDesign::ProfileBased::Restore()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#a911a7f2f77e2adb2277a344a4ffb33f2),
[PartDesign::Transformed::Restore()](../../dd/de1/classPartDesign_1_1Transformed.html#a4e823053076cbcb1c6a8add13d191405),
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[Part::Part2DObject::Restore()](../../d9/d57/classPart_1_1Part2DObject.html#a24712341d8edfa206b25b21bdda998a2),
[Part::Primitive::Restore()](../../d2/d31/classPart_1_1Primitive.html#ad739d09a91f363ecaac5bce84d2271f7),
[PartDesign::Chamfer::Restore()](../../da/d6f/classPartDesign_1_1Chamfer.html#aa7e36b44d9a038c47691655463d2eaf4),
and
[TechDraw::DrawViewDimension::Restore()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#afb1057b5d67039082147ba14225f1c82).

## ◆ restoreExtensions()

void ExtensionContainer::restoreExtensions  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_| ) |   
---|---|---|---|---|---  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Type::createInstance()](../../dc/dee/classBase_1_1Type.html#a2d1d33a2453ee324e07ce2412a542e44),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::Type::fromName()](../../dc/dee/classBase_1_1Type.html#a7fd6fce9272b7886af7a58d2af987c42),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[getExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#a329e85b59ccbc63a619c4d31325f23d8),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[Base::Type::isBad()](../../dc/dee/classBase_1_1Type.html#ab091b5ccf4f8e3c7c59cb05dde3c2fcb),
[Base::Type::isDerivedFrom()](../../dc/dee/classBase_1_1Type.html#abb24fc578ec80e158584f46d4a5042c7),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
and
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3).

Referenced by
[Restore()](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48).

## ◆ Save()

| void ExtensionContainer::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
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
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482).

Reimplemented in
[Robot::RobotObject](../../db/d51/classRobot_1_1RobotObject.html#ab1443831f8c6492a77f0f9483688c5b6),
[Sketcher::SketchObject](../../d9/dad/classSketcher_1_1SketchObject.html#a914f9773505d35bfd655e97abffb6d7b),
[App::VRMLObject](../../df/df6/classApp_1_1VRMLObject.html#abee995466100ec91a1ae0f2baa2feec3),
and
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html#aceb2a532b12d3ad6806562eb64bfcf06).

References
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
and
[saveExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0).

Referenced by
[Gui::Document::exportObjects()](../../de/d4e/classGui_1_1Document.html#ad5cd74e1fab4fb536910270125c5a329).

## ◆ saveExtensions()

void ExtensionContainer::saveExtensions  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | _writer_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[hasExtensions()](../../d6/d76/classApp_1_1ExtensionContainer.html#a56345b1e7049b01ee7620192f06950dd),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[Save()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ExtensionContainer.h
  * FreeCAD/src/App/ExtensionContainer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

