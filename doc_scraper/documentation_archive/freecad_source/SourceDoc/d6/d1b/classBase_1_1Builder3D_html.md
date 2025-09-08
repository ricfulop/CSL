---
url: https://freecad.github.io/SourceDoc/d6/d1b/classBase_1_1Builder3D.html
scraped_at: 2025-09-08T15:15:46.722380
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Builder3D](../../d6/d1b/classBase_1_1Builder3D.html)

[List of all members](../../d8/d8d/classBase_1_1Builder3D-members.html) | Public Member Functions

Base::Builder3D Class Reference

A Builder class for 3D representations on [App](../../dd/dc2/namespaceApp.html
"The FreeCAD Application layer.") level On the application level nothing is
known of the visual representation of data.
[More...](../../d6/d1b/classBase_1_1Builder3D.html#details)

`#include <Builder3D.h>`

##  Public Member Functions  
  
---  
|
[Builder3D](../../d6/d1b/classBase_1_1Builder3D.html#aec17836f999f17116f807b9275d91638)
()  
| Construction.
[More...](../../d6/d1b/classBase_1_1Builder3D.html#aec17836f999f17116f807b9275d91638)  
  
virtual | [~Builder3D](../../d6/d1b/classBase_1_1Builder3D.html#a8ffd9131f589e3178dd43ef5612cd485) ()  
| Destruction.
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a8ffd9131f589e3178dd43ef5612cd485)  
  
point set handling  
void | [startPoints](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4) (short pointSize=2, float color_r=1.0, float color_g=0.0, float color_b=0.0)  
| starts a point set
[More...](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4)  
  
void | [addPoint](../../d6/d1b/classBase_1_1Builder3D.html#a989376d776506093cd4c4134621049a9) (float x, float y, float z)  
| insert a point in an point set
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a989376d776506093cd4c4134621049a9)  
  
void | [addPoint](../../d6/d1b/classBase_1_1Builder3D.html#a4ba202347a70ab413514e8a508b288ec) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &vec)  
| add a vector to a point set
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a4ba202347a70ab413514e8a508b288ec)  
  
void | [endPoints](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915) ()  
| ends the points set operation
[More...](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915)  
  
void | [addSinglePoint](../../d6/d1b/classBase_1_1Builder3D.html#a4615a7a86b2d7498e9e655e596534f3a) (float x, float y, float z, short pointSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a singular point (without
[startPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4
"starts a point set") &
[endPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915
"ends the points set operation") )
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a4615a7a86b2d7498e9e655e596534f3a)  
  
void | [addSinglePoint](../../d6/d1b/classBase_1_1Builder3D.html#a1ef7fc99f4b70fcfa58bc787306515b3) (const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &vec, short pointSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a singular point (without
[startPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4
"starts a point set") &
[endPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915
"ends the points set operation") )
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a1ef7fc99f4b70fcfa58bc787306515b3)  
  
line/direction handling  
void | [addSingleLine](../../d6/d1b/classBase_1_1Builder3D.html#accf2a8116bd1142069e93a4eac808d7b) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0, unsigned short linePattern=0xffff)  
| add a line defined by 2 Vector3D
[More...](../../d6/d1b/classBase_1_1Builder3D.html#accf2a8116bd1142069e93a4eac808d7b)  
  
void | [addSingleArrow](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0, unsigned short linePattern=0xffff)  
| add a arrow (directed line) by 2 Vector3D. The arrow shows in direction of
point 2.
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a000b4d9d1342d22dcb7c0ded96ad45b2)  
  
triangle handling  
void | [addSingleTriangle](../../d6/d1b/classBase_1_1Builder3D.html#a536ca5856ad41bf83a85d68af4ec5f68) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt0, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, [bool](../../d9/db9/classbool.html) filled=true, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a (filled) triangle defined by 3 vectors
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a536ca5856ad41bf83a85d68af4ec5f68)  
  
Transformation  
void | [addTransformation](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5) (const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &)  
| adds a transformation
[More...](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5)  
  
void | [addTransformation](../../d6/d1b/classBase_1_1Builder3D.html#a58a5885eaf6eabc1113eefb6b69148e3) (const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &translation, const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rotationaxis, float fAngle)  
text handling  
void | [addText](../../d6/d1b/classBase_1_1Builder3D.html#ac08b052650a94b0edbe25013eafcf935) (float pos_x, float pos_y, float pos_z, const char *text, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a text
[More...](../../d6/d1b/classBase_1_1Builder3D.html#ac08b052650a94b0edbe25013eafcf935)  
  
void | [addText](../../d6/d1b/classBase_1_1Builder3D.html#ae5f150c5f2f24fda47444f00041618d2) (const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &vec, const char *text, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a text
[More...](../../d6/d1b/classBase_1_1Builder3D.html#ae5f150c5f2f24fda47444f00041618d2)  
  
void | [clear](../../d6/d1b/classBase_1_1Builder3D.html#a1901306f0d632b88bdb1c218b20704a4) ()  
| clear the string buffer
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a1901306f0d632b88bdb1c218b20704a4)  
  
  
## write the result  
  
---  
void | [saveToLog](../../d6/d1b/classBase_1_1Builder3D.html#a219f6a61f1f9f0216ab0b47e0efddfa6) ()  
| sends the result to the log and gui
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a219f6a61f1f9f0216ab0b47e0efddfa6)  
  
void | [saveToFile](../../d6/d1b/classBase_1_1Builder3D.html#a0fe240932e027fdaf954dfdd11a9c098) (const char *FileName)  
| save the result to a file (*.iv)
[More...](../../d6/d1b/classBase_1_1Builder3D.html#a0fe240932e027fdaf954dfdd11a9c098)  
  
  
## Detailed Description

A Builder class for 3D representations on [App](../../dd/dc2/namespaceApp.html
"The FreeCAD Application layer.") level On the application level nothing is
known of the visual representation of data.

Nevertheless it's often needed to see some 3D information, e.g. points,
directions, when you program or debug an algorithm.
[Builder3D](../../d6/d1b/classBase_1_1Builder3D.html "A Builder class for 3D
representations on App level On the application level nothing is known of the
...") was made for this specific purpose. This class allows you to easily
build up a 3D representation of some mathematical and algorithm internals. You
can save this representation to a file and view it in an Inventor viewer, or
send it to the log. In the case of using the log and a debug FreeCAD the
representation will be loaded into the active viewer.

    The workflow goes as follows: Create the a [Builder3D](../../d6/d1b/classBase_1_1Builder3D.html "A Builder class for 3D representations on App level On the application level nothing is known of the ...") object and call the methods to insert the graphical elements. After that call either [saveToLog()](../../d6/d1b/classBase_1_1Builder3D.html#a219f6a61f1f9f0216ab0b47e0efddfa6 "sends the result to the log and gui") or [saveToFile()](../../d6/d1b/classBase_1_1Builder3D.html#a0fe240932e027fdaf954dfdd11a9c098 "save the result to a file \(*.iv\)"). 

    Usage: 

[Base::Builder3D](../../d6/d1b/classBase_1_1Builder3D.html "A Builder class
for 3D representations on App level On the application level nothing is known
of the ...") log3D;

for ( unsigned long i=0; i<pMesh->CountPoints(); i++ )

{

log3D.[addSinglePoint](../../d6/d1b/classBase_1_1Builder3D.html#a4615a7a86b2d7498e9e655e596534f3a
"add a singular point \(without startPoints\(\) & endPoints\(\)
\)")(pMesh->GetPoint(i));

log3D.[addText](../../d6/d1b/classBase_1_1Builder3D.html#ac08b052650a94b0edbe25013eafcf935
"add a text")(pMesh->GetPoint(i),"Point");

...

}

log3D.[saveToLog](../../d6/d1b/classBase_1_1Builder3D.html#a219f6a61f1f9f0216ab0b47e0efddfa6
"sends the result to the log and gui")();

See also

    [Base::ConsoleSingleton](../../df/dca/classBase_1_1ConsoleSingleton.html "The console class This class manage all the stdio stuff.")

## Constructor & Destructor Documentation

## ◆ Builder3D()

Builder3D::Builder3D  | ( | | ) |   
---|---|---|---|---  
  
Construction.

A constructor.

A more elaborate description of the constructor.

## ◆ ~Builder3D()

| Builder3D::~Builder3D  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

A destructor.

A more elaborate description of the destructor.

## Member Function Documentation

## ◆ addPoint() [1/2]

void Builder3D::addPoint  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _vec_| ) |   
---|---|---|---|---|---  
  
add a vector to a point set

References
[addPoint()](../../d6/d1b/classBase_1_1Builder3D.html#a989376d776506093cd4c4134621049a9),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftguitools.gui_stretch.Stretch::action()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a23b5e547bf5d84dbecee7a970ebcb621),
and
[draftguitools.gui_stretch.Stretch::numericInput()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a5402b1eab63d5e107b781983de1bf033).

## ◆ addPoint() [2/2]

void Builder3D::addPoint  | ( | float  | _x_ ,   
---|---|---|---  
|  | float  | _y_ ,   
|  | float  | _z_  
| ) | |   
  
insert a point in an point set

insert a point in a point set

Referenced by
[draftguitools.gui_stretch.Stretch::action()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a23b5e547bf5d84dbecee7a970ebcb621),
[addPoint()](../../d6/d1b/classBase_1_1Builder3D.html#a4ba202347a70ab413514e8a508b288ec),
and
[draftguitools.gui_stretch.Stretch::numericInput()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a5402b1eab63d5e107b781983de1bf033).

## ◆ addSingleArrow()

void Builder3D::addSingleArrow  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt1_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt2_ ,   
|  | short  | _lineSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`,   
|  | unsigned short  | _linePattern_ = `0xffff`  
| ) | |   
  
add a arrow (directed line) by 2 Vector3D. The arrow shows in direction of
point 2.

References [Base::Vector3< _Precision
>::GetAngle()](../../d1/d13/classBase_1_1Vector3.html#aa7649aaf126c62148c8ebc54ad38ce27),
[Base::Vector3< _Precision
>::Normalize()](../../d1/d13/classBase_1_1Vector3.html#aabc9ab5341e2d5c11a181ec428742983),
[Base::Vector3< _Precision
>::Scale()](../../d1/d13/classBase_1_1Vector3.html#aff9627b9ca6eb620fbfe189e83aab8d5),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ addSingleLine()

void Builder3D::addSingleLine  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt1_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt2_ ,   
|  | short  | _lineSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`,   
|  | unsigned short  | _linePattern_ = `0xffff`  
| ) | |   
  
add a line defined by 2 Vector3D

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[Mesh::MeshObject::offsetSpecial2()](../../d8/dcc/classMesh_1_1MeshObject.html#a2be16c1ce13a5f5eecb318c442d64b20),
and
[MeshPart::MeshAlgos::offsetSpecial2()](../../db/d67/classMeshPart_1_1MeshAlgos.html#a9fd929c87723fd546563717fac248d11).

## ◆ addSinglePoint() [1/2]

void Builder3D::addSinglePoint  | ( | const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _vec_ ,   
---|---|---|---  
|  | short  | _pointSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
add a singular point (without
[startPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4
"starts a point set") &
[endPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915
"ends the points set operation") )

References
[addSinglePoint()](../../d6/d1b/classBase_1_1Builder3D.html#a4615a7a86b2d7498e9e655e596534f3a),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ addSinglePoint() [2/2]

void Builder3D::addSinglePoint  | ( | float  | _x_ ,   
---|---|---|---  
|  | float  | _y_ ,   
|  | float  | _z_ ,   
|  | short  | _pointSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
add a singular point (without
[startPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4
"starts a point set") &
[endPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915
"ends the points set operation") )

Referenced by
[addSinglePoint()](../../d6/d1b/classBase_1_1Builder3D.html#a1ef7fc99f4b70fcfa58bc787306515b3),
[Mesh::MeshObject::offsetSpecial2()](../../d8/dcc/classMesh_1_1MeshObject.html#a2be16c1ce13a5f5eecb318c442d64b20),
and
[MeshPart::MeshAlgos::offsetSpecial2()](../../db/d67/classMeshPart_1_1MeshAlgos.html#a9fd929c87723fd546563717fac248d11).

## ◆ addSingleTriangle()

void Builder3D::addSingleTriangle  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt0_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt1_ ,   
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt2_ ,   
|  | [bool](../../d9/db9/classbool.html) | _filled_ = `true`,   
|  | short  | _lineSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
add a (filled) triangle defined by 3 vectors

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ addText() [1/2]

void Builder3D::addText  | ( | const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _vec_ ,   
---|---|---|---  
|  | const char *  | _text_ ,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
add a text

References
[addText()](../../d6/d1b/classBase_1_1Builder3D.html#ac08b052650a94b0edbe25013eafcf935),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ addText() [2/2]

void Builder3D::addText  | ( | float  | _pos_x_ ,   
---|---|---|---  
|  | float  | _pos_y_ ,   
|  | float  | _pos_z_ ,   
|  | const char *  | _text_ ,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
add a text

Add a Text with a given position to the 3D set.

The origin is the lower leftmost corner.

Parameters

     pos_x,pos_y,pos_z| origin of the text   
---|---  
text| the text to display.  
color_r| red part of the text color (0.0 - 1.0).  
color_g| green part of the text color (0.0 - 1.0).  
color_b| blue part of the text color (0.0 - 1.0).  
  
Referenced by
[addText()](../../d6/d1b/classBase_1_1Builder3D.html#ae5f150c5f2f24fda47444f00041618d2).

## ◆ addTransformation() [1/2]

void Builder3D::addTransformation  | ( | const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _transform_| ) |   
---|---|---|---|---|---  
  
adds a transformation

References
[addTransformation()](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[addTransformation()](../../d6/d1b/classBase_1_1Builder3D.html#ac722adc9f5581af07ee4fb411e5bb7f5).

## ◆ addTransformation() [2/2]

void Builder3D::addTransformation  | ( | const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _translation_ ,   
---|---|---|---  
|  | const [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rotationaxis_ ,   
|  | float  | _fAngle_  
| ) | |   
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ clear()

void Builder3D::clear  | ( | | ) |   
---|---|---|---|---  
  
clear the string buffer

## ◆ endPoints()

void Builder3D::endPoints  | ( | | ) |   
---|---|---|---|---  
  
ends the points set operation

Ends the point set operations and write the resulting inventor string.

See also

    [startPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4 "starts a point set")

## ◆ saveToFile()

void Builder3D::saveToFile  | ( | const char *  | _FileName_| ) |   
---|---|---|---|---|---  
  
save the result to a file (*.iv)

Save the resulting inventor 3D representation to a file.

Ending should be *.iv. That enables you to show the result in a Inventor
Viewer or in FreeCAD by: /code
Gui.document().addAnnotation("Debug","MyFile.iv") /endcode

See also

    [saveToFile()](../../d6/d1b/classBase_1_1Builder3D.html#a0fe240932e027fdaf954dfdd11a9c098 "save the result to a file \(*.iv\)")

## ◆ saveToLog()

void Builder3D::saveToLog  | ( | | ) |   
---|---|---|---|---  
  
sends the result to the log and gui

Save the resulting inventor 3D representation to the
[Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729
"Access to the Console This method is used to gain access to the one and only
instance of the ConsoleS...").Log() facility.

In DEBUG mode the [Gui](../../d9/dad/namespaceGui.html "The FreeCAD Graphical
interface layer.") (if running) will trigger on that and show the
representation in the active Viewer/Document. It shows only one representation
on time. If you need to show more then one representation use
[saveToFile()](../../d6/d1b/classBase_1_1Builder3D.html#a0fe240932e027fdaf954dfdd11a9c098
"save the result to a file \(*.iv\)") instead.

See also

    [saveToFile()](../../d6/d1b/classBase_1_1Builder3D.html#a0fe240932e027fdaf954dfdd11a9c098 "save the result to a file \(*.iv\)")

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Get()](../../df/dca/classBase_1_1ConsoleSingleton.html#ae4ca9fea6787c5acd17c66dbfbbe374b),
[Base::Log](../../db/d07/namespaceBase.html#ae2bba22932ed35d81c0e63b78c792126ace0be71e33226e4c1db2bcea5959f16b),
and
[Base::ILogger::SendLog()](../../d8/d26/classBase_1_1ILogger.html#a6de9b82c247a06262f8e592b427f3be7).

Referenced by
[Mesh::MeshObject::offsetSpecial2()](../../d8/dcc/classMesh_1_1MeshObject.html#a2be16c1ce13a5f5eecb318c442d64b20),
and
[MeshPart::MeshAlgos::offsetSpecial2()](../../db/d67/classMeshPart_1_1MeshAlgos.html#a9fd929c87723fd546563717fac248d11).

## ◆ startPoints()

void Builder3D::startPoints  | ( | short  | _pointSize_ = `2`,   
---|---|---|---  
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `0.0`,   
|  | float  | _color_b_ = `0.0`  
| ) | |   
  
starts a point set

Starts the definition of point set with the given point size and color.

If possible don't make too many
[startPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ab790661c95f5ac4f5a712916589a67f4
"starts a point set") and
[endPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915
"ends the points set operation") calls. Try to put all points in one set.

See also

    [endPoints()](../../d6/d1b/classBase_1_1Builder3D.html#ace39e2a6cdb7c020dde671a7deed2915 "ends the points set operation")

Parameters

     pointSize| the point size in pixel that are displayed.   
---|---  
color_r| red part of the point color (0.0 - 1.0).  
color_g| green part of the point color (0.0 - 1.0).  
color_b| blue part of the point color (0.0 - 1.0).  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Builder3D.h
  * FreeCAD/src/Base/Builder3D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

