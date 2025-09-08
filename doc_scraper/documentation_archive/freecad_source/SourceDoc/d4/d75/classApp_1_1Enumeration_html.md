---
url: https://freecad.github.io/SourceDoc/d4/d75/classApp_1_1Enumeration.html
scraped_at: 2025-09-08T14:54:34.476108
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Enumeration](../../d4/d75/classApp_1_1Enumeration.html)

[List of all members](../../d5/d9e/classApp_1_1Enumeration-members.html) | Classes | Public Member Functions | Protected Member Functions | Friends

App::Enumeration Class Reference

A bidirectional string-integer mapping.
[More...](../../d4/d75/classApp_1_1Enumeration.html#details)

`#include <Enumeration.h>`

##  Classes  
  
---  
class | [Object](../../d2/d82/classApp_1_1Enumeration_1_1Object.html)  
  
##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [contains](../../d4/d75/classApp_1_1Enumeration.html#a07f7c8edc00868eb28424d8ff3762462) (const char *value) const  
| Checks if a string is included in the enumeration.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a07f7c8edc00868eb28424d8ff3762462)  
  
|
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html#a7693f015bf00287bdc3ef367973557e7)
()  
| Constructs an empty [Enumeration](../../d4/d75/classApp_1_1Enumeration.html
"A bidirectional string-integer mapping.") object.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a7693f015bf00287bdc3ef367973557e7)  
  
|
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html#a88a0c5226f3bd07cf056b5b5e837e6cd)
(const char **list, const char *valStr)  
| Constructs an [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") using val within list.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a88a0c5226f3bd07cf056b5b5e837e6cd)  
  
|
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html#a35e8e76d1e121a1cab2ccfb0df424df9)
(const char *valStr)  
| Constructs an [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") with a single element.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a35e8e76d1e121a1cab2ccfb0df424df9)  
  
|
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html#a7c3300cb9632c355e04e4104507d81d7)
(const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) &other)  
| Standard copy constructor.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a7c3300cb9632c355e04e4104507d81d7)  
  
const char * | [getCStr](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51) () const  
| Return the value as C string.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51)  
  
std::vector< std::string > | [getEnumVector](../../d4/d75/classApp_1_1Enumeration.html#a4e3caafbda4fec69aa8c9a16702c917d) () const  
| get all possible enum values as vector of strings
[More...](../../d4/d75/classApp_1_1Enumeration.html#a4e3caafbda4fec69aa8c9a16702c917d)  
  
[int](../../d1/da0/classint.html) | [getInt](../../d4/d75/classApp_1_1Enumeration.html#ad2dc4b4973ea12da69c6307e638c2e5f) () const  
| Return value as integer.
[More...](../../d4/d75/classApp_1_1Enumeration.html#ad2dc4b4973ea12da69c6307e638c2e5f)  
  
[bool](../../d9/db9/classbool.html) | [hasEnums](../../d4/d75/classApp_1_1Enumeration.html#af4af65c15817fb827f4db45e0b00c5c9) () const  
| returns true if the enum list is non-empty, false otherwise
[More...](../../d4/d75/classApp_1_1Enumeration.html#af4af65c15817fb827f4db45e0b00c5c9)  
  
[bool](../../d9/db9/classbool.html) | [isCustom](../../d4/d75/classApp_1_1Enumeration.html#a8816197dfb18fd12eb3d33932c06c29f) () const  
| Returns true if any of the items is a user-defined string.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a8816197dfb18fd12eb3d33932c06c29f)  
  
[bool](../../d9/db9/classbool.html) | [isValid](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea) () const  
| Returns true if the instance is in a usable state.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea)  
  
[bool](../../d9/db9/classbool.html) | [isValue](../../d4/d75/classApp_1_1Enumeration.html#a8c143f4815bb15f39132e5444f832dea) (const char *value) const  
| Checks if the property is set to a certain string value.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a8c143f4815bb15f39132e5444f832dea)  
  
[int](../../d1/da0/classint.html) | [maxValue](../../d4/d75/classApp_1_1Enumeration.html#a2d7b41202527aff251f118fe7dd2b305) () const  
| Returns the highest usable integer value for this enum.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a2d7b41202527aff251f118fe7dd2b305)  
  
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | [operator=](../../d4/d75/classApp_1_1Enumeration.html#ab078ae17f674d0fd9a0ccb2493114521) (const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) &other)  
| Assignment operator.
[More...](../../d4/d75/classApp_1_1Enumeration.html#ab078ae17f674d0fd9a0ccb2493114521)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../d4/d75/classApp_1_1Enumeration.html#a8bc57ae0c64c9506d1e00b93d8b48dfe) (const char *other) const  
| true iff our string representation matches other
[More...](../../d4/d75/classApp_1_1Enumeration.html#a8bc57ae0c64c9506d1e00b93d8b48dfe)  
  
[bool](../../d9/db9/classbool.html) | [operator==](../../d4/d75/classApp_1_1Enumeration.html#a33c7e139c3b191466c764b668fd8eb17) (const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) &other) const  
| true iff our string representation matches other's
[More...](../../d4/d75/classApp_1_1Enumeration.html#a33c7e139c3b191466c764b668fd8eb17)  
  
void | [setEnums](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52) (const char **plEnums)  
| Sets the enumeration string list The list is a NULL terminated array of
pointers to const char* strings.
[More...](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52)  
  
void | [setEnums](../../d4/d75/classApp_1_1Enumeration.html#af36b32b8add6868afc210b368d9972d8) (const std::vector< std::string > &values)  
| Set all enum values as vector of strings.
[More...](../../d4/d75/classApp_1_1Enumeration.html#af36b32b8add6868afc210b368d9972d8)  
  
void | [setValue](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555) (const char *value)  
| Set the enum using a C string.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555)  
  
void | [setValue](../../d4/d75/classApp_1_1Enumeration.html#ac08c5b5ba0c5dfe05158f802ffd4fe3d) (const std::string &value)  
| Overload of [setValue(const char
*value)](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555
"Set the enum using a C string.")
[More...](../../d4/d75/classApp_1_1Enumeration.html#ac08c5b5ba0c5dfe05158f802ffd4fe3d)  
  
void | [setValue](../../d4/d75/classApp_1_1Enumeration.html#a230bcc01db0fa441c93fc2595fbb14b0) (long value, [bool](../../d9/db9/classbool.html) checkRange=false)  
| Set the enum using a long.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a230bcc01db0fa441c93fc2595fbb14b0)  
  
|
[~Enumeration](../../d4/d75/classApp_1_1Enumeration.html#a30391592983f75434851e29e912fe515)
()  
| Standard destructor.
[More...](../../d4/d75/classApp_1_1Enumeration.html#a30391592983f75434851e29e912fe515)  
  
  
##  Protected Member Functions  
  
---  
[int](../../d1/da0/classint.html) | [countItems](../../d4/d75/classApp_1_1Enumeration.html#ac33bb0b735359db9eb1714dc5f2ae55d) () const  
| Number of items.
[More...](../../d4/d75/classApp_1_1Enumeration.html#ac33bb0b735359db9eb1714dc5f2ae55d)  
  
  
##  Friends  
  
---  
class | [PropertyEnumeration](../../d4/d75/classApp_1_1Enumeration.html#aac0661aa154fa19ba1ebe5131e76eaca)  
  
## Detailed Description

A bidirectional string-integer mapping.

This is mainly intended for two purposes: working around the difficulty in C++
of sharing enumerations between different source files, namespaces, etc. and
as the data type stored by
[App::PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html
"Property wrapper around an Enumeration object.")

Internally, [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") maintains

  1. Either a const pointer to an array of C-style strings, or a vector of C++ std::strings
  2. An integer index into that array/vector representing the string representing the instance's value.

If built with FC_DEBUG defined, some boundaries of passed in pointers will be
checked. Otherwise, the caller has the responsibility of checking the limits
of given indices.

## Constructor & Destructor Documentation

## ◆ Enumeration() [1/4]

Enumeration::Enumeration  | ( | | ) |   
---|---|---|---|---  
  
Constructs an empty [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") object.

## ◆ Enumeration() [2/4]

Enumeration::Enumeration  | ( | const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | _other_| ) |   
---|---|---|---|---|---  
  
Standard copy constructor.

## ◆ Enumeration() [3/4]

Enumeration::Enumeration  | ( | const char *  | _valStr_| ) |   
---|---|---|---|---|---  
  
Constructs an [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") with a single element.

References
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555).

## ◆ Enumeration() [4/4]

Enumeration::Enumeration  | ( | const char **  | _list_ ,   
---|---|---|---  
|  | const char *  | _valStr_  
| ) | |   
  
Constructs an [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") using val within list.

References
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555).

## ◆ ~Enumeration()

Enumeration::~Enumeration  | ( | | ) |   
---|---|---|---|---  
  
Standard destructor.

## Member Function Documentation

## ◆ contains()

[bool](../../d9/db9/classbool.html) Enumeration::contains  | ( | const char *  | _value_| ) |  const  
---|---|---|---|---|---  
  
Checks if a string is included in the enumeration.

References
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea).

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12).

## ◆ countItems()

| [int](../../d1/da0/classint.html) Enumeration::countItems  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
Number of items.

Referenced by
[getCStr()](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51),
[getInt()](../../d4/d75/classApp_1_1Enumeration.html#ad2dc4b4973ea12da69c6307e638c2e5f),
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea),
and
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#a230bcc01db0fa441c93fc2595fbb14b0).

## ◆ getCStr()

const char * Enumeration::getCStr  | ( | | ) |  const  
---|---|---|---|---  
  
Return the value as C string.

Returns NULL if the enumeration is invalid.

References
[countItems()](../../d4/d75/classApp_1_1Enumeration.html#ac33bb0b735359db9eb1714dc5f2ae55d),
and
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea).

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[operator==()](../../d4/d75/classApp_1_1Enumeration.html#a8bc57ae0c64c9506d1e00b93d8b48dfe),
and
[setEnums()](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52).

## ◆ getEnumVector()

std::vector< std::string > Enumeration::getEnumVector  | ( | | ) |  const  
---|---|---|---|---  
  
get all possible enum values as vector of strings

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12).

## ◆ getInt()

[int](../../d1/da0/classint.html) Enumeration::getInt  | ( | | ) |  const  
---|---|---|---|---  
  
Return value as integer.

Returns -1 if the [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") isn't valid

References
[countItems()](../../d4/d75/classApp_1_1Enumeration.html#ac33bb0b735359db9eb1714dc5f2ae55d),
and
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea).

Referenced by
[isValue()](../../d4/d75/classApp_1_1Enumeration.html#a8c143f4815bb15f39132e5444f832dea).

## ◆ hasEnums()

[bool](../../d9/db9/classbool.html) Enumeration::hasEnums  | ( | | ) |  const  
---|---|---|---|---  
  
returns true if the enum list is non-empty, false otherwise

Referenced by
[Fem::FemPostScalarClipFilter::execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
and
[Fem::FemPostWarpVectorFilter::execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66).

## ◆ isCustom()

[bool](../../d9/db9/classbool.html) Enumeration::isCustom  | ( | | ) |  const  
---|---|---|---|---  
  
Returns true if any of the items is a user-defined string.

## ◆ isValid()

[bool](../../d9/db9/classbool.html) Enumeration::isValid  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns true if the instance is in a usable state.

References
[countItems()](../../d4/d75/classApp_1_1Enumeration.html#ac33bb0b735359db9eb1714dc5f2ae55d).

Referenced by
[contains()](../../d4/d75/classApp_1_1Enumeration.html#a07f7c8edc00868eb28424d8ff3762462),
[getCStr()](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51),
[getInt()](../../d4/d75/classApp_1_1Enumeration.html#ad2dc4b4973ea12da69c6307e638c2e5f),
and
[setEnums()](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52).

## ◆ isValue()

[bool](../../d9/db9/classbool.html) Enumeration::isValue  | ( | const char *  | _value_| ) |  const  
---|---|---|---|---|---  
  
Checks if the property is set to a certain string value.

References
[getInt()](../../d4/d75/classApp_1_1Enumeration.html#ad2dc4b4973ea12da69c6307e638c2e5f).

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
and
[TechDraw::DrawProjGroup::usedProjectionType()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a34227f080eebfad29b97318c09c59dc3).

## ◆ maxValue()

[int](../../d1/da0/classint.html) Enumeration::maxValue  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the highest usable integer value for this enum.

Returns -1 if the enumeration is not valid according to
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea
"Returns true if the instance is in a usable state.")

## ◆ operator=()

[Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & Enumeration::operator=  | ( | const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | _other_| ) |   
---|---|---|---|---|---  
  
Assignment operator.

## ◆ operator==() [1/2]

[bool](../../d9/db9/classbool.html) Enumeration::operator==  | ( | const char *  | _other_| ) |  const  
---|---|---|---|---|---  
  
true iff our string representation matches other

Returns false if [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A
bidirectional string-integer mapping.") is not valid.

References
[getCStr()](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51).

## ◆ operator==() [2/2]

[bool](../../d9/db9/classbool.html) Enumeration::operator==  | ( | const [Enumeration](../../d4/d75/classApp_1_1Enumeration.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
true iff our string representation matches other's

Returns false if either
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") is not valid.

## ◆ setEnums() [1/2]

void Enumeration::setEnums  | ( | const char **  | _plEnums_| ) |   
---|---|---|---|---|---  
  
Sets the enumeration string list The list is a NULL terminated array of
pointers to const char* strings.

const char enums[] = {"Black","White","Other",NULL}

If [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") was already valid, will attempt to preserve the
string-representation value of the
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.")

[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") does not take ownership of the passed object

References
[getCStr()](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51),
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea),
and
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555).

Referenced by
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[Fem::FemPostScalarClipFilter::execute()](../../d9/da9/classFem_1_1FemPostScalarClipFilter.html#a0aa1f4898cacdd829920492771a3931b),
[Fem::FemPostWarpVectorFilter::execute()](../../db/d33/classFem_1_1FemPostWarpVectorFilter.html#abfd97dfc34d290355149f487d5c93f66),
and
[setEnums()](../../d4/d75/classApp_1_1Enumeration.html#af36b32b8add6868afc210b368d9972d8).

## ◆ setEnums() [2/2]

void Enumeration::setEnums  | ( | const std::vector< std::string > & | _values_| ) |   
---|---|---|---|---|---  
  
Set all enum values as vector of strings.

This method causes the [Enumeration](../../d4/d75/classApp_1_1Enumeration.html
"A bidirectional string-integer mapping.") to dynamically allocate it's own
array of C Strings, which will be deleted by the destructor or subsequent
calls to
[setEnums()](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52
"Sets the enumeration string list The list is a NULL terminated array of
pointers to const char* strin..."). So, it is important to make sure the
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") stays in scope as long as values returned by getCStr
are in use.

If [Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.") was already valid, will attempt to preserve the
string-representation value of the
[Enumeration](../../d4/d75/classApp_1_1Enumeration.html "A bidirectional
string-integer mapping.")

References
[getCStr()](../../d4/d75/classApp_1_1Enumeration.html#a6d267c2e2245caa79d27e42ec36a7a51),
[isValid()](../../d4/d75/classApp_1_1Enumeration.html#a17fb03f7595f81f91ddf0bff1c4f02ea),
[setEnums()](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52),
and
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555).

## ◆ setValue() [1/3]

void Enumeration::setValue  | ( | const char *  | _value_| ) |   
---|---|---|---|---|---  
  
Set the enum using a C string.

Referenced by
[Enumeration()](../../d4/d75/classApp_1_1Enumeration.html#a35e8e76d1e121a1cab2ccfb0df424df9),
[App::FeatureTest::execute()](../../df/dea/classApp_1_1FeatureTest.html#a288578d37e4aa3f4ffa5ee8797607c12),
[setEnums()](../../d4/d75/classApp_1_1Enumeration.html#aff111b21c10b7931fcc5c4d182021e52),
and
[TechDraw::DrawProjGroup::usedProjectionType()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a34227f080eebfad29b97318c09c59dc3).

## ◆ setValue() [2/3]

void App::Enumeration::setValue  | ( | const std::string & | _value_| ) |   
---|---|---|---|---|---  
  
Overload of [setValue(const char
*value)](../../d4/d75/classApp_1_1Enumeration.html#a38ae975d6ee4b072c5a3a4aff3d2e555
"Set the enum using a C string.")

References
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#ac08c5b5ba0c5dfe05158f802ffd4fe3d).

Referenced by
[setValue()](../../d4/d75/classApp_1_1Enumeration.html#ac08c5b5ba0c5dfe05158f802ffd4fe3d).

## ◆ setValue() [3/3]

void Enumeration::setValue  | ( | long  | _value_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _checkRange_ = `false`  
| ) | |   
  
Set the enum using a long.

if checkRange is set to true, throws
[Base::ValueError](../../db/d20/classBase_1_1ValueError.html "The ValueError
can be used to indicate the usage of a wrong value.") when values are set out
of range

Checks for boundaries via assert()

References
[countItems()](../../d4/d75/classApp_1_1Enumeration.html#ac33bb0b735359db9eb1714dc5f2ae55d).

## Friends And Related Function Documentation

## ◆ PropertyEnumeration

| [friend](../../d7/d23/classfriend.html) class
[PropertyEnumeration](../../d4/df2/classApp_1_1PropertyEnumeration.html)  
---  
friend  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Enumeration.h
  * FreeCAD/src/App/Enumeration.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

