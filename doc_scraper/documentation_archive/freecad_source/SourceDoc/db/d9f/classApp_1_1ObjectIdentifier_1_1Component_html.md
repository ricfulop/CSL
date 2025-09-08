---
url: https://freecad.github.io/SourceDoc/db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html
scraped_at: 2025-09-08T14:55:11.627356
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)
  * [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html)

[List of all members](../../d2/d7c/classApp_1_1ObjectIdentifier_1_1Component-members.html) | Public Member Functions | Static Public Member Functions | Friends

App::ObjectIdentifier::Component Class Reference

A component is a part of a [Path](../../da/d2a/classApp_1_1Path.html "Base
class of all geometric document objects.") object, and is used to either name
a property or a field within a property.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#details)

`#include <ObjectIdentifier.h>`

##  Public Member Functions  
  
---  
|
[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a32ee6d95adecc8a838b8f0ed32c4f195)
(const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
&_name=[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)(),
typeEnum _type=SIMPLE, [int](../../d1/da0/classint.html) begin=INT_MAX,
[int](../../d1/da0/classint.html) end=INT_MAX,
[int](../../d1/da0/classint.html) step=1)  
| Construct a
[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A
component is a part of a Path object, and is used to either name a property or
a field within a pro...") part.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a32ee6d95adecc8a838b8f0ed32c4f195)  
  
|
[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ac26e61e60c12c315eeebfb014c2bdc0a)
([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&_name,
typeEnum _type=SIMPLE, [int](../../d1/da0/classint.html) begin=INT_MAX,
[int](../../d1/da0/classint.html) end=INT_MAX,
[int](../../d1/da0/classint.html) step=1)  
void | [del](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad38cc5ffd0fb239b9045c184ec2b855a) (Py::Object &pyobj) const  
|
[FC_DEFAULT_CTORS](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a70f440629467801d72f7480f4f3f87e9)
([Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html))  
Py::Object | [get](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad99dffa416e065802811bcccd62bf0f7) (const Py::Object &pyobj) const  
[int](../../d1/da0/classint.html) | [getBegin](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ac9d86263ebc1acea0d9b56a6f2892507) () const  
[int](../../d1/da0/classint.html) | [getEnd](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a8e19b22bf2d54915e10c63f1ebb8e8d4) () const  
[int](../../d1/da0/classint.html) | [getIndex](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad73bf4fa909d7a063ed78e56ed69f74f) () const  
size_t | [getIndex](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a774f6f912474442e1800d1b6f3583d75) (size_t count) const  
const std::string & | [getName](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a75df2bd96a8a6cb4de583e215fb94d14) () const  
[int](../../d1/da0/classint.html) | [getStep](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad57355354dd1fa861e33dd40db2b2f98) () const  
[bool](../../d9/db9/classbool.html) | [isArray](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a3973f4df62fa5e27a56727dd464fa79b) () const  
[bool](../../d9/db9/classbool.html) | [isMap](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad42ecfc813b1cc31e8ddbc2c3ec87729) () const  
[bool](../../d9/db9/classbool.html) | [isRange](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#adbaa2229a592c3f4d800cdf5261446a4) () const  
[bool](../../d9/db9/classbool.html) | [isSimple](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ab0947be0175afc62281468806536f382) () const  
[bool](../../d9/db9/classbool.html) | [operator<](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a04c2f820057c723b2b1d8003404366f9) (const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &other) const  
[bool](../../d9/db9/classbool.html) | [operator==](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a166f04ba32197b7bef606e2dc089c9c9) (const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) &other) const  
| Comparison operator for
[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A
component is a part of a Path object, and is used to either name a property or
a field within a pro...") objects.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a166f04ba32197b7bef606e2dc089c9c9)  
  
void | [set](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ac9f438dcde3d18fac9f14fe5d2bd7bfa) (Py::Object &pyobj, const Py::Object &value) const  
void | [toString](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#af2237ebba7f2d9999b3e3f2acfd8db85) (std::ostream &ss, [bool](../../d9/db9/classbool.html) toPython=false) const  
| Create a string representation of a component.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#af2237ebba7f2d9999b3e3f2acfd8db85)  
  
  
##  Static Public Member Functions  
  
---  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [ArrayComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a53deba0e70949ab36dc1e958fe5a7359) ([int](../../d1/da0/classint.html) _index)  
| Create an array component with given name and index.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a53deba0e70949ab36dc1e958fe5a7359)  
  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [MapComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a542736c807e83fd82a2ad0e3bf266d52) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &_key)  
| Create a map component with given name and key.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a542736c807e83fd82a2ad0e3bf266d52)  
  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [MapComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#acceec2bae5724de3e15000d1747fe0e6) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&_key)  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [RangeComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a387d322ecb13eaf282245ba4fca56da4) ([int](../../d1/da0/classint.html) _begin, [int](../../d1/da0/classint.html) _end=INT_MAX, [int](../../d1/da0/classint.html) _step=1)  
| Create a range component with given begin and end.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a387d322ecb13eaf282245ba4fca56da4)  
  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [SimpleComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a312dfad6111eb04b0341ab5055f9bc44) (const char *_component)  
| Create a simple component part with the given name.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a312dfad6111eb04b0341ab5055f9bc44)  
  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [SimpleComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a38b1f099685bbe44cd286c793badfa8d) (const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &_component)  
| Create a simple component part with the given name.
[More...](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a38b1f099685bbe44cd286c793badfa8d)  
  
static [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | [SimpleComponent](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a7d80f658926d2e4b5dba9f35de242b75) ([String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) &&_component)  
  
##  Friends  
  
---  
class | [ObjectIdentifier](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#a33910ad2ce88bf67e7e0e97f08c9d5d2)  
  
## Detailed Description

A component is a part of a [Path](../../da/d2a/classApp_1_1Path.html "Base
class of all geometric document objects.") object, and is used to either name
a property or a field within a property.

A component can be either a single entry, and array, or a map to other sub-
fields.

## Constructor & Destructor Documentation

## ◆ Component() [1/2]

ObjectIdentifier::Component::Component  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | __name_ = `[String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)()`,   
---|---|---|---  
|  | typeEnum  | __type_ = `SIMPLE`,   
|  | [int](../../d1/da0/classint.html) | __begin_ = `INT_MAX`,   
|  | [int](../../d1/da0/classint.html) | __end_ = `INT_MAX`,   
|  | [int](../../d1/da0/classint.html) | __step_ = `1`  
| ) | |   
  
Construct a
[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A
component is a part of a Path object, and is used to either name a property or
a field within a pro...") part.

Parameters

     _name| Name of component   
---|---  
_type| Type; simple, array, range or map  
_begin| Array index or beginning of a
[Range](../../dd/dc1/classApp_1_1Range.html "The Range class is a spreadsheet
range iterator."), or INT_MAX for other type.  
_end| ending of a [Range](../../dd/dc1/classApp_1_1Range.html "The Range class
is a spreadsheet range iterator."), or INT_MAX for other type.  
  
## ◆ Component() [2/2]

ObjectIdentifier::Component::Component  | ( | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | __name_ ,   
---|---|---|---  
|  | typeEnum  | __type_ = `SIMPLE`,   
|  | [int](../../d1/da0/classint.html) | _begin_ = `INT_MAX`,   
|  | [int](../../d1/da0/classint.html) | _end_ = `INT_MAX`,   
|  | [int](../../d1/da0/classint.html) | _step_ = `1`  
| ) | |   
  
## Member Function Documentation

## ◆ ArrayComponent()

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::ArrayComponent  | ( | [int](../../d1/da0/classint.html) | __index_| ) |   
---|---|---|---|---|---  
static  
  
Create an array component with given name and index.

Parameters

     _component| Name of component   
---|---  
_index| Index of component  
  
Returns

    A new [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A component is a part of a Path object, and is used to either name a property or a field within a pro...") object. 

## ◆ del()

void ObjectIdentifier::Component::del  | ( | Py::Object & | _pyobj_| ) |  const  
---|---|---|---|---|---  
  
References
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ FC_DEFAULT_CTORS()

App::ObjectIdentifier::Component::FC_DEFAULT_CTORS  | ( | [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) | | ) |   
---|---|---|---|---|---  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ get()

Py::Object ObjectIdentifier::Component::get  | ( | const Py::Object & | _pyobj_| ) |  const  
---|---|---|---|---|---  
  
References
[App::ExpressionParser::isModuleImported()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ac9298ffe56af3fc4a9feb9b60583ce21),
and
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ getBegin()

[int](../../d1/da0/classint.html) App::ObjectIdentifier::Component::getBegin  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getEnd()

[int](../../d1/da0/classint.html) App::ObjectIdentifier::Component::getEnd  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getIndex() [1/2]

[int](../../d1/da0/classint.html) App::ObjectIdentifier::Component::getIndex  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getIndex() [2/2]

size_t ObjectIdentifier::Component::getIndex  | ( | size_t  | _count_| ) |  const  
---|---|---|---|---|---  
  
## ◆ getName()

const std::string & App::ObjectIdentifier::Component::getName  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ getStep()

[int](../../d1/da0/classint.html) App::ObjectIdentifier::Component::getStep  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isArray()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::Component::isArray  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isMap()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::Component::isMap  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isRange()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::Component::isRange  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isSimple()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::Component::isSimple  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ MapComponent() [1/2]

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::MapComponent  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | __key_| ) |   
---|---|---|---|---|---  
static  
  
Create a map component with given name and key.

Parameters

     _component| Name of component   
---|---  
_key| Key of component  
  
Returns

    A new [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A component is a part of a Path object, and is used to either name a property or a field within a pro...") object. 

## ◆ MapComponent() [2/2]

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::MapComponent  | ( | [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | __key_| ) |   
---|---|---|---|---|---  
static  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ operator<()

[bool](../../d9/db9/classbool.html) App::ObjectIdentifier::Component::operator< | ( | const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator==()

[bool](../../d9/db9/classbool.html) ObjectIdentifier::Component::operator==  | ( | const [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
Comparison operator for
[Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A
component is a part of a Path object, and is used to either name a property or
a field within a pro...") objects.

Parameters

     other| The object we want to compare to.   
---|---  
  
Returns

    true if they are equal, false if not. 

## ◆ RangeComponent()

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::RangeComponent  | ( | [int](../../d1/da0/classint.html) | __begin_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | __end_ = `INT_MAX`,   
|  | [int](../../d1/da0/classint.html) | __step_ = `1`  
| ) | |   
static  
  
Create a range component with given begin and end.

Parameters

     _begin| beginning index of the range   
---|---  
_end| ending index of the range  
  
Returns

    A new [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A component is a part of a Path object, and is used to either name a property or a field within a pro...") object. 

## ◆ set()

void ObjectIdentifier::Component::set  | ( | Py::Object & | _pyobj_ ,   
---|---|---|---  
|  | const Py::Object & | _value_  
| ) | |  const  
  
References
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

Referenced by
[draftguitools.gui_trackers.editTracker::move()](../../d3/dce/classdraftguitools_1_1gui__trackers_1_1editTracker.html#a6e4a060566362b1db0b5ea44c9874297).

## ◆ SimpleComponent() [1/3]

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::SimpleComponent  | ( | const char *  | __component_| ) |   
---|---|---|---|---|---  
static  
  
Create a simple component part with the given name.

Parameters

     _component| Name of component.   
---|---  
  
Returns

    A new [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A component is a part of a Path object, and is used to either name a property or a field within a pro...") object. 

Referenced by
[Part::PropertyPartShape::getPaths()](../../d7/d28/classPart_1_1PropertyPartShape.html#a613e891f4e97c366bfce9a191006e3cf),
and
[Gui::QuantitySpinBox::setBoundToByName()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a6b7ec360dc439b034f4793f05c7d074a).

## ◆ SimpleComponent() [2/3]

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::SimpleComponent  | ( | const [String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) & | __component_| ) |   
---|---|---|---|---|---  
static  
  
Create a simple component part with the given name.

Parameters

     _component| Name of component.   
---|---  
  
Returns

    A new [Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html "A component is a part of a Path object, and is used to either name a property or a field within a pro...") object. 

## ◆ SimpleComponent() [3/3]

| [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) ObjectIdentifier::Component::SimpleComponent  | ( | [ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) && | __component_| ) |   
---|---|---|---|---|---  
static  
  
References
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f).

## ◆ toString()

void ObjectIdentifier::Component::toString  | ( | std::ostream & | _ss_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _toPython_ = `false`  
| ) | |  const  
  
Create a string representation of a component.

Returns

    A string representing the component. 

## Friends And Related Function Documentation

## ◆ ObjectIdentifier

| [friend](../../d7/d23/classfriend.html) class
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)  
---  
friend  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/ObjectIdentifier.h
  * FreeCAD/src/App/ObjectIdentifier.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

