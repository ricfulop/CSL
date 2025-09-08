---
url: https://freecad.github.io/SourceDoc/d0/d61/classBase_1_1PyObjectBase.html
scraped_at: 2025-09-08T15:17:00.030259
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html)

[List of all members](../../d8/d0c/classBase_1_1PyObjectBase-members.html) | Public Types | Public Member Functions | Static Public Member Functions | Public Attributes | Static Public Attributes | Protected Member Functions | Protected Attributes

Base::PyObjectBase Class Reference

The [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The
PyObjectBase class, exports the class as a python type PyObjectBase is the
base class for all C++...") class, exports the class as a python type
[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The PyObjectBase
class, exports the class as a python type PyObjectBase is the base class for
all C++...") is the base class for all C++ classes which need to get exported
into the python namespace.
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#details)

`#include <PyObjectBase.h>`

##  Public Types  
  
---  
typedef void * | [PointerType](../../d0/d61/classBase_1_1PyObjectBase.html#a9e07714277cfa1c8de6e3fe7a37c377a)  
enum | [Status](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6d) { [Valid](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6da3ebd444ec1488b1db959538d93581148) = 0 , [Immutable](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6da4c361b263b603ff1f0f6008b242b80ab) = 1 , [Notify](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6da72bc40640c98d6b911f3e3ee7fc06571) = 2 , [NoTrack](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6da5f1551f1f33dfff82935f66e7cc6036a) = 3 }  
  
##  Public Member Functions  
  
---  
[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html) * | [DecRef](../../d0/d61/classBase_1_1PyObjectBase.html#afb57ff5b97b6393951cbb09793416ba8) ()  
| decref method wrapper (see python extending manual)
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#afb57ff5b97b6393951cbb09793416ba8)  
  
void * | [getTwinPointer](../../d0/d61/classBase_1_1PyObjectBase.html#a62e16ae2274ae14b5b36d9b0fb91eada) () const  
| Get the pointer of the twin object.
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#a62e16ae2274ae14b5b36d9b0fb91eada)  
  
virtual PyTypeObject * | [GetType](../../d0/d61/classBase_1_1PyObjectBase.html#a1e7eb1eae91abdffe955e727eafc285d) (void)  
[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html) * | [IncRef](../../d0/d61/classBase_1_1PyObjectBase.html#a1ed00d7d9b685533584d332122293188) ()  
| incref method wrapper (see python extending manual)
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#a1ed00d7d9b685533584d332122293188)  
  
[bool](../../d9/db9/classbool.html) | [isConst](../../d0/d61/classBase_1_1PyObjectBase.html#a889d534b80d703e987888042fd44dc8f) ()  
[bool](../../d9/db9/classbool.html) | [isNotTracking](../../d0/d61/classBase_1_1PyObjectBase.html#acfba68d07e4e83398b02c97758e8e695) () const  
[bool](../../d9/db9/classbool.html) | [isValid](../../d0/d61/classBase_1_1PyObjectBase.html#a50302daad2f0f22d74a9b8fb6af57022) ()  
virtual [int](../../d1/da0/classint.html) | [PyInit](../../d0/d61/classBase_1_1PyObjectBase.html#a8276b564550dea9058e32e769b3d8f20) ([PyObject](../../df/d1b/classPyObject.html) *, [PyObject](../../df/d1b/classPyObject.html) *)  
| PyInit method Override this method to initialize a newly created instance of
the class (Constructor)
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#a8276b564550dea9058e32e769b3d8f20)  
  
|
[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html#a5c865a0d688a88082e358afa12c55dd0)
(void *, PyTypeObject *T)  
| Constructor Sets the [Type](../../dc/dee/classBase_1_1Type.html "Type system
class Many of the classes in the FreeCAD must have their type information
registered befo...") of the object (for inheritance) and decrease the the
reference count of the [PyObject](../../df/d1b/classPyObject.html).
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#a5c865a0d688a88082e358afa12c55dd0)  
  
void | [setConst](../../d0/d61/classBase_1_1PyObjectBase.html#a56b700872b55aa7978d38ef5fd2abbc4) ()  
void | [setInvalid](../../d0/d61/classBase_1_1PyObjectBase.html#a476dff461414387c8518b094049dabb4) ()  
void | [setNotTracking](../../d0/d61/classBase_1_1PyObjectBase.html#aff1cc8f3be435cf65220c0eeed40dad1) ([bool](../../d9/db9/classbool.html) on=true)  
void | [setShouldNotify](../../d0/d61/classBase_1_1PyObjectBase.html#a78fddd653b0e19a59f120b29275bb004) ([bool](../../d9/db9/classbool.html) on)  
[bool](../../d9/db9/classbool.html) | [shouldNotify](../../d0/d61/classBase_1_1PyObjectBase.html#a5869b66ab5d4d38150eeb5e2ced40c51) () const  
void | [startNotify](../../d0/d61/classBase_1_1PyObjectBase.html#a68aaf30755cd812682c7f6460837438a) ()  
  
##  Static Public Member Functions  
  
---  
static void | [PyDestructor](../../d0/d61/classBase_1_1PyObjectBase.html#ae0c3962bb92591aeb7f8106400060eb5) ([PyObject](../../df/d1b/classPyObject.html) *P)  
| Wrapper for the Python destructor.
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#ae0c3962bb92591aeb7f8106400060eb5)  
  
  
##  Public Attributes  
  
---  
[PyObject](../../df/d1b/classPyObject.html) * | [baseProxy](../../d0/d61/classBase_1_1PyObjectBase.html#abd2730344de5b11f68fb50b85946bf0d)  
  
##  Static Public Attributes  
  
---  
static [PyMethodDef](../../da/dab/classPyMethodDef.html) | [Methods](../../d0/d61/classBase_1_1PyObjectBase.html#abf2cf392a3a9785752bc21209481ffec) []  
static PyTypeObject | [Type](../../d0/d61/classBase_1_1PyObjectBase.html#aa40cc61e3f6a68dd6fb81745b5fc20de)  
| Py_Header struct from python.h.
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#aa40cc61e3f6a68dd6fb81745b5fc20de)  
  
  
##  Protected Member Functions  
  
---  
void | [setTwinPointer](../../d0/d61/classBase_1_1PyObjectBase.html#a80be334eb27cd8788f0cfed77e6c7e6b) (void *ptr)  
| Overrides the pointer to the twin object.
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#a80be334eb27cd8788f0cfed77e6c7e6b)  
  
virtual | [~PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html#aa1693883212cb6724dbb2ed587bf8057) ()  
| destructor
[More...](../../d0/d61/classBase_1_1PyObjectBase.html#aa1693883212cb6724dbb2ed587bf8057)  
  
  
##  Protected Attributes  
  
---  
std::bitset< 32 > | [StatusBits](../../d0/d61/classBase_1_1PyObjectBase.html#a4f690d08621d70f8dc34ac8379c1c4a9)  
  
## Detailed Description

The [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The
PyObjectBase class, exports the class as a python type PyObjectBase is the
base class for all C++...") class, exports the class as a python type
[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The PyObjectBase
class, exports the class as a python type PyObjectBase is the base class for
all C++...") is the base class for all C++ classes which need to get exported
into the python namespace.

This class is very important because nearly all important classes in FreeCAD
are visible in python for macro recording and automation purpose. The class
[App::Document](../../d8/d3e/classApp_1_1Document.html "The document class.")
is a good expample for an exported class. There are some convenience macros to
make it easier to inherit from this class and defining new methods exported to
python. PYFUNCDEF_D defines a new exported method. PYFUNCIMP_D defines the
implementation of the new exported method. In the implementation you can use
Py_Return, Py_Error, Py_Try and Py_Assert. PYMETHODEDEF makes the entry in the
python method table.

See also

    [Document](../../d1/d67/classDocument.html)
     PYFUNCDEF_D 
     PYFUNCIMP_D 
     PYMETHODEDEF 
     Py_Return 
     Py_Error 
     Py_Try 
     Py_Assert 

## Member Typedef Documentation

## ◆ PointerType

typedef void*
[Base::PyObjectBase::PointerType](../../d0/d61/classBase_1_1PyObjectBase.html#a9e07714277cfa1c8de6e3fe7a37c377a)  
---  
  
## Member Enumeration Documentation

## ◆ Status

enum
[Base::PyObjectBase::Status](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6d)  
---  
  
Enumerator  
---  
Valid |   
Immutable |   
Notify |   
NoTrack |   
  
## Constructor & Destructor Documentation

## ◆ ~PyObjectBase()

| PyObjectBase::~PyObjectBase  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
destructor

References
[baseProxy](../../d0/d61/classBase_1_1PyObjectBase.html#abd2730344de5b11f68fb50b85946bf0d),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964).

## ◆ PyObjectBase()

PyObjectBase::PyObjectBase  | ( | void *  | _p_ ,   
---|---|---|---  
|  | PyTypeObject *  | _T_  
| ) | |   
  
Constructor Sets the [Type](../../dc/dee/classBase_1_1Type.html "Type system
class Many of the classes in the FreeCAD must have their type information
registered befo...") of the object (for inheritance) and decrease the the
reference count of the [PyObject](../../df/d1b/classPyObject.html).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[Notify](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6da72bc40640c98d6b911f3e3ee7fc06571),
[StatusBits](../../d0/d61/classBase_1_1PyObjectBase.html#a4f690d08621d70f8dc34ac8379c1c4a9),
and
[Valid](../../d0/d61/classBase_1_1PyObjectBase.html#a57108963aacd9561c74326094f218e6da3ebd444ec1488b1db959538d93581148).

## Member Function Documentation

## ◆ DecRef()

[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html) * Base::PyObjectBase::DecRef  | ( | | ) |   
---|---|---|---|---  
  
decref method wrapper (see python extending manual)

## ◆ getTwinPointer()

void * Base::PyObjectBase::getTwinPointer  | ( | | ) |  const  
---|---|---|---|---  
  
Get the pointer of the twin object.

## ◆ GetType()

| virtual PyTypeObject * Base::PyObjectBase::GetType  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
## ◆ IncRef()

[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html) * Base::PyObjectBase::IncRef  | ( | | ) |   
---|---|---|---|---  
  
incref method wrapper (see python extending manual)

## ◆ isConst()

[bool](../../d9/db9/classbool.html) Base::PyObjectBase::isConst  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isNotTracking()

[bool](../../d9/db9/classbool.html) Base::PyObjectBase::isNotTracking  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isValid()

[bool](../../d9/db9/classbool.html) Base::PyObjectBase::isValid  | ( | | ) |   
---|---|---|---|---  
  
## ◆ PyDestructor()

| static void Base::PyObjectBase::PyDestructor  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _P_| ) |   
---|---|---|---|---|---  
static  
  
Wrapper for the Python destructor.

## ◆ PyInit()

| virtual [int](../../d1/da0/classint.html) Base::PyObjectBase::PyInit  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  |   
| ) | |   
virtual  
  
PyInit method Override this method to initialize a newly created instance of
the class (Constructor)

## ◆ setConst()

void Base::PyObjectBase::setConst  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Part::PropertyPartShape::getPyObject()](../../d7/d28/classPart_1_1PropertyPartShape.html#a9881f558fdd16ec00fa7bbdbd9c17158).

## ◆ setInvalid()

void Base::PyObjectBase::setInvalid  | ( | | ) |   
---|---|---|---|---  
  
## ◆ setNotTracking()

void Base::PyObjectBase::setNotTracking  | ( | [bool](../../d9/db9/classbool.html) | _on_ = `true`| ) |   
---|---|---|---|---|---  
  
Referenced by
[Part::TopoShape::getPyObject()](../../d8/ded/classPart_1_1TopoShape.html#a218a19417db2576dbfba9238c87fbd64).

## ◆ setShouldNotify()

void Base::PyObjectBase::setShouldNotify  | ( | [bool](../../d9/db9/classbool.html) | _on_| ) |   
---|---|---|---|---|---  
  
## ◆ setTwinPointer()

| void Base::PyObjectBase::setTwinPointer  | ( | void *  | _ptr_| ) |   
---|---|---|---|---|---  
protected  
  
Overrides the pointer to the twin object.

## ◆ shouldNotify()

[bool](../../d9/db9/classbool.html) Base::PyObjectBase::shouldNotify  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[startNotify()](../../d0/d61/classBase_1_1PyObjectBase.html#a68aaf30755cd812682c7f6460837438a).

## ◆ startNotify()

void PyObjectBase::startNotify  | ( | | ) |   
---|---|---|---|---  
  
References
[shouldNotify()](../../d0/d61/classBase_1_1PyObjectBase.html#a5869b66ab5d4d38150eeb5e2ced40c51).

## Member Data Documentation

## ◆ baseProxy

[PyObject](../../df/d1b/classPyObject.html)* Base::PyObjectBase::baseProxy  
---  
  
Referenced by
[~PyObjectBase()](../../d0/d61/classBase_1_1PyObjectBase.html#aa1693883212cb6724dbb2ed587bf8057).

## ◆ Methods

| [PyMethodDef](../../da/dab/classPyMethodDef.html) PyObjectBase::Methods  
---  
static  
  
**Initial value:**

= {

{nullptr, nullptr, 0, nullptr}

}

## ◆ StatusBits

| std::bitset<32> Base::PyObjectBase::StatusBits  
---  
protected  
  
Referenced by
[PyObjectBase()](../../d0/d61/classBase_1_1PyObjectBase.html#a5c865a0d688a88082e358afa12c55dd0).

## ◆ Type

| PyTypeObject PyObjectBase::Type  
---  
static  
  
Py_Header struct from python.h.

Every [PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The
PyObjectBase class, exports the class as a python type PyObjectBase is the
base class for all C++...") object is also a python object. So you can use
every Python C-Library function also on a
[PyObjectBase](../../d0/d61/classBase_1_1PyObjectBase.html "The PyObjectBase
class, exports the class as a python type PyObjectBase is the base class for
all C++...") object

Referenced by
[ArchPanel.CommandPanelSheet::Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftobjects.draft_annotation.DraftAnnotation::add_missing_properties_0v19()](../../d4/dca/classdraftobjects_1_1draft__annotation_1_1DraftAnnotation.html#a345b51b0cfae010e7e5574f0a84dd2f3),
[ArchStructure.StructSelectionObserver::addSelection()](../../db/d76/classArchStructure_1_1StructSelectionObserver.html#ac984e4631db3078ffee1dc0fee52df74),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchComponent.Component::execute()](../../de/d87/classArchComponent_1_1Component.html#a2ab328b6ab53b7bc9017eef25870cdf0),
[draftobjects.layer.LayerContainer::execute()](../../de/d4d/classdraftobjects_1_1layer_1_1LayerContainer.html#a960d8cd7f03fe7426f8cac669671b513),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[draftobjects.layer.Layer::set_properties()](../../d0/ddc/classdraftobjects_1_1layer_1_1Layer.html#aa6a95fe93a36b884d61ef2c668de002e),
and
[ArchReference.ArchReference::setProperties()](../../d3/d06/classArchReference_1_1ArchReference.html#a41a26333eb23a48bdb3271bed98296e5).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/PyObjectBase.h
  * FreeCAD/src/Base/PyObjectBase.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

