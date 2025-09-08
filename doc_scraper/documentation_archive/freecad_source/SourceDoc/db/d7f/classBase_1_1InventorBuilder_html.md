---
url: https://freecad.github.io/SourceDoc/db/d7f/classBase_1_1InventorBuilder.html
scraped_at: 2025-09-08T15:16:30.965295
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html)

[List of all members](../../d2/da9/classBase_1_1InventorBuilder-members.html) | Public Member Functions

Base::InventorBuilder Class Reference

This class does basically the same as
[Builder3D](../../d6/d1b/classBase_1_1Builder3D.html "A Builder class for 3D
representations on App level On the application level nothing is known of the
...") except that it writes the data directly into a given stream without
buffering the output data in a string stream.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#details)

`#include <Builder3D.h>`

##  Public Member Functions  
  
---  
void | [addInfo](../../db/d7f/classBase_1_1InventorBuilder.html#a7a78081ab92fba0512fbe45377a98a95) (const char *[str](../../d9/d36/classstr.html))  
| Sets an info node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a7a78081ab92fba0512fbe45377a98a95)  
  
void | [addLabel](../../db/d7f/classBase_1_1InventorBuilder.html#aed85014e369c11c1f3a4cfcd6c1a74eb) (const char *[str](../../d9/d36/classstr.html))  
| Sets a label node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#aed85014e369c11c1f3a4cfcd6c1a74eb)  
  
void | [beginSeparator](../../db/d7f/classBase_1_1InventorBuilder.html#a363c1063803156cc05a1e057f4fc02ea) ()  
| Sets a separator node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a363c1063803156cc05a1e057f4fc02ea)  
  
void | [close](../../db/d7f/classBase_1_1InventorBuilder.html#a578c7a0e879c5b5fa8d2587bc497cd74) ()  
| If needed closes the first opened separator node. This method must not be
used more than one time for an instance.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a578c7a0e879c5b5fa8d2587bc497cd74)  
  
void | [endSeparator](../../db/d7f/classBase_1_1InventorBuilder.html#acde68aee5d63622468db3d7d911c3bd9) ()  
| Closes the last added separator node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#acde68aee5d63622468db3d7d911c3bd9)  
  
|
[InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html#abc080de907a46e75cdd584965951cae3)
(std::ostream &[str](../../d9/d36/classstr.html))  
| Construction of an
[InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html "This class
does basically the same as Builder3D except that it writes the data directly
into a given ...") instance. This automatically opens a separator node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#abc080de907a46e75cdd584965951cae3)  
  
virtual | [~InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html#a88188c4db1df50b6fd54d8e22e6a846e) ()  
| Destruction of an
[InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html "This class
does basically the same as Builder3D except that it writes the data directly
into a given ...") instance.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a88188c4db1df50b6fd54d8e22e6a846e)  
  
Appearance handling  
void | [addBaseColor](../../db/d7f/classBase_1_1InventorBuilder.html#a0b16bc0f8d6532b16d88ef82c3f35a06) (float color_r, float color_g, float color_b)  
| Sets a base color node. The colors are in the range [0, 1].
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a0b16bc0f8d6532b16d88ef82c3f35a06)  
  
void | [addMaterial](../../db/d7f/classBase_1_1InventorBuilder.html#ab037e8cc6a4dbc9ef2b512d71427abf6) (float color_r, float color_g, float color_b, float color_a=0)  
| Sets a material node. The colors are in the range [0, 1].
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ab037e8cc6a4dbc9ef2b512d71427abf6)  
  
void | [beginMaterial](../../db/d7f/classBase_1_1InventorBuilder.html#a9ffc07a550e1253fa9e2711c094a3c6d) ()  
| Starts a material node. The node must be closed with
[endMaterial](../../db/d7f/classBase_1_1InventorBuilder.html#ae4440b40a9c12a6490a9ba7fab360d0d)
and the colors must be added with
[addColor()](../../db/d7f/classBase_1_1InventorBuilder.html#ad578e90a3fd1b0c638eae078007e3a23).
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a9ffc07a550e1253fa9e2711c094a3c6d)  
  
void | [endMaterial](../../db/d7f/classBase_1_1InventorBuilder.html#ae4440b40a9c12a6490a9ba7fab360d0d) ()  
| Closes a material node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ae4440b40a9c12a6490a9ba7fab360d0d)  
  
void | [addColor](../../db/d7f/classBase_1_1InventorBuilder.html#ad578e90a3fd1b0c638eae078007e3a23) (float color_r, float color_g, float color_b)  
| Adds a color to a material node. The colors are in the range [0, 1].
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ad578e90a3fd1b0c638eae078007e3a23)  
  
void | [addMaterialBinding](../../db/d7f/classBase_1_1InventorBuilder.html#aaf3d9b392aaa63590b3ee970943bea64) (const char *binding="OVERALL")  
| Sets a material binding node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#aaf3d9b392aaa63590b3ee970943bea64)  
  
void | [addDrawStyle](../../db/d7f/classBase_1_1InventorBuilder.html#a61e2fa7459505b099c33546abccac028) (short pointSize, short lineWidth, unsigned short linePattern=0xffff, const char *style="FILLED")  
| Sets a draw style node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a61e2fa7459505b099c33546abccac028)  
  
void | [addShapeHints](../../db/d7f/classBase_1_1InventorBuilder.html#ab0144172627717721ed0b0956a1ebf58) (float crease=0.0f)  
| Sets a shape hints node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ab0144172627717721ed0b0956a1ebf58)  
  
void | [addPolygonOffset](../../db/d7f/classBase_1_1InventorBuilder.html#ad46b2b96f38360ea73367016db950529) (float factor=1.0f, float units=1.0f, const char *styles="FILLED", bool on=true)  
| Sets a polygon offset node.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ad46b2b96f38360ea73367016db950529)  
  
Add coordinates  
void | [addPoint](../../db/d7f/classBase_1_1InventorBuilder.html#a77961e2440f3bbbfebafd1c4d224e70d) (float x, float y, float z)  
| add a single point
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a77961e2440f3bbbfebafd1c4d224e70d)  
  
void | [addPoint](../../db/d7f/classBase_1_1InventorBuilder.html#a04d481e0aae6c8be35c121a5ad92bc82) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &vec)  
| add a single point
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a04d481e0aae6c8be35c121a5ad92bc82)  
  
void | [addPoints](../../db/d7f/classBase_1_1InventorBuilder.html#af1b546025002b5ff636b17d9e7b12764) (const std::vector< [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) > &vec)  
| add a list of points
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#af1b546025002b5ff636b17d9e7b12764)  
  
Point set handling  
void | [beginPoints](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917) ()  
| starts a point set
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917)  
  
void | [endPoints](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d) ()  
| ends the points set operation
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d)  
  
void | [addPointSet](../../db/d7f/classBase_1_1InventorBuilder.html#a7f9ff3a1145b4e39f8bf58a596071a50) ()  
| add an [SoPointSet](../../d0/d15/classSoPointSet.html) node
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a7f9ff3a1145b4e39f8bf58a596071a50)  
  
Normal handling  
void | [beginNormal](../../db/d7f/classBase_1_1InventorBuilder.html#a8d0af4a7525e238fb85f267081b2135f) ()  
| starts a point set
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a8d0af4a7525e238fb85f267081b2135f)  
  
void | [endNormal](../../db/d7f/classBase_1_1InventorBuilder.html#aafbbaaab75da78a87242570dfdad49cf) ()  
| ends the points set operation
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#aafbbaaab75da78a87242570dfdad49cf)  
  
void | [addNormalBinding](../../db/d7f/classBase_1_1InventorBuilder.html#aaf1fa1fb3462220546ef47e8f5ffcf07) (const char *)  
| add normal binding node
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#aaf1fa1fb3462220546ef47e8f5ffcf07)  
  
Line/Direction handling  
void | [addSingleLine](../../db/d7f/classBase_1_1InventorBuilder.html#a404c84909791311b5fe386216c074d65) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0, unsigned short linePattern=0xffff)  
| add a line defined by 2 Vector3D
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a404c84909791311b5fe386216c074d65)  
  
void | [addSingleArrow](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0, unsigned short linePattern=0xffff)  
| add a arrow (directed line) by 2 Vector3D. The arrow shows in direction of
point 2.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a075ebfc1e2f098e0e0bcf104b3cbb916)  
  
void | [addLineSet](../../db/d7f/classBase_1_1InventorBuilder.html#a49e208de6df88599638af3b91a5ddfdc) (const std::vector< [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) > &points, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0, unsigned short linePattern=0xffff)  
| add a line defined by a list of points whereat always a pair (i.e. a point
and the following point) builds a line.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a49e208de6df88599638af3b91a5ddfdc)  
  
void | [addLineSet](../../db/d7f/classBase_1_1InventorBuilder.html#ade919189aea40d70e8e226ce434437b3) ()  
| add an SoLineSet node
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ade919189aea40d70e8e226ce434437b3)  
  
Triangle handling  
void | [addSingleTriangle](../../db/d7f/classBase_1_1InventorBuilder.html#aa559cd33d73da4c7f081923dd5c9ea51) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt0, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, [bool](../../d9/db9/classbool.html) filled=true, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a (filled) triangle defined by 3 vectors
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#aa559cd33d73da4c7f081923dd5c9ea51)  
  
void | [addSinglePlane](../../db/d7f/classBase_1_1InventorBuilder.html#a7b3b6c4b92eb6b42f4ceab91ad24bc43) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &base, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &eX, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &eY, float length, float width, [bool](../../d9/db9/classbool.html) filled=true, short lineSize=2, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
void | [addIndexedFaceSet](../../db/d7f/classBase_1_1InventorBuilder.html#a0aadd1f3311e0015442c8cb2ab34bcfb) (const std::vector< [int](../../d1/da0/classint.html) > &indices)  
void | [addFaceSet](../../db/d7f/classBase_1_1InventorBuilder.html#addc1ada5522f98688ec6420eb791c671) (const std::vector< [int](../../d1/da0/classint.html) > &vertices)  
Surface handling  
void | [addNurbsSurface](../../db/d7f/classBase_1_1InventorBuilder.html#adf4a733fb20a910125bf7abbba9f49de) (const std::vector< [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) > &controlPoints, [int](../../d1/da0/classint.html) numUControlPoints, [int](../../d1/da0/classint.html) numVControlPoints, const std::vector< float > &uKnots, const std::vector< float > &vKnots)  
| The number of control points must be numUControlPoints * numVControlPoints.
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#adf4a733fb20a910125bf7abbba9f49de)  
  
void | [addCylinder](../../db/d7f/classBase_1_1InventorBuilder.html#adaa73a9b05ec4af62008341274cb238f) (float radius, float height)  
void | [addSphere](../../db/d7f/classBase_1_1InventorBuilder.html#a2c14612c661fee7e62bd6f87a6b06f6d) (float radius)  
Bounding Box handling  
void | [addBoundingBox](../../db/d7f/classBase_1_1InventorBuilder.html#a7fa4b2eb43c7d1a8df907bc949462fec) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt1, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &pt2, short lineWidth=2, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
Transformation  
void | [addTransformation](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &)  
| adds a transformation
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c)  
  
void | [addTransformation](../../db/d7f/classBase_1_1InventorBuilder.html#afd645abfb9256e9eff434730d9103c0f) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &translation, const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &rotationaxis, float fAngle)  
  
## Text handling  
  
---  
void | [addText](../../db/d7f/classBase_1_1InventorBuilder.html#a5de5b1b47988a867b0e7b3ca8c45b6d5) (float pos_x, float pos_y, float pos_z, const char *text, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a text
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#a5de5b1b47988a867b0e7b3ca8c45b6d5)  
  
void | [addText](../../db/d7f/classBase_1_1InventorBuilder.html#ad9a7fdefd3bb65d3c8d5b8b7b2133d9c) (const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) &vec, const char *text, float color_r=1.0, float color_g=1.0, float color_b=1.0)  
| add a text
[More...](../../db/d7f/classBase_1_1InventorBuilder.html#ad9a7fdefd3bb65d3c8d5b8b7b2133d9c)  
  
  
## Detailed Description

This class does basically the same as
[Builder3D](../../d6/d1b/classBase_1_1Builder3D.html "A Builder class for 3D
representations on App level On the application level nothing is known of the
...") except that it writes the data directly into a given stream without
buffering the output data in a string stream.

Compared to file streams, string streams are quite slow when writing data with
more than a few hundred lines. Due to performance reasons the user should use
a file stream in this case.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ InventorBuilder()

InventorBuilder::InventorBuilder  | ( | std::ostream & | _str_| ) |   
---|---|---|---|---|---  
  
Construction of an
[InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html "This class
does basically the same as Builder3D except that it writes the data directly
into a given ...") instance. This automatically opens a separator node.

Parameters

     str| \- stream to write the content into   
---|---  
  
References
[beginSeparator()](../../db/d7f/classBase_1_1InventorBuilder.html#a363c1063803156cc05a1e057f4fc02ea).

## ◆ ~InventorBuilder()

| InventorBuilder::~InventorBuilder  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction of an
[InventorBuilder](../../db/d7f/classBase_1_1InventorBuilder.html "This class
does basically the same as Builder3D except that it writes the data directly
into a given ...") instance.

References
[close()](../../db/d7f/classBase_1_1InventorBuilder.html#a578c7a0e879c5b5fa8d2587bc497cd74).

## Member Function Documentation

## ◆ addBaseColor()

void InventorBuilder::addBaseColor  | ( | float  | _color_r_ ,   
---|---|---|---  
|  | float  | _color_g_ ,   
|  | float  | _color_b_  
| ) | |   
  
Sets a base color node. The colors are in the range [0, 1].

Parameters

     color_r| \- red color   
---|---  
color_g| \- green color  
color_b| \- blue color  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addBoundingBox()

void InventorBuilder::addBoundingBox  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt1_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt2_ ,   
|  | short  | _lineWidth_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
References [Base::Vector3< _Precision
>::Set()](../../d1/d13/classBase_1_1Vector3.html#a961b4f52c806809737f1d6fe18c8f9f6),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ addColor()

void InventorBuilder::addColor  | ( | float  | _color_r_ ,   
---|---|---|---  
|  | float  | _color_g_ ,   
|  | float  | _color_b_  
| ) | |   
  
Adds a color to a material node. The colors are in the range [0, 1].

Parameters

     color_r| \- red color   
---|---  
color_g| \- green color  
color_b| \- blue color  
  
Referenced by
[importIFClegacy.IfcWriter::addExtrudedCircle()](../../dc/df4/classimportIFClegacy_1_1IfcWriter.html#a70486ce12f81620abcbb72895685541f),
[importIFClegacy.IfcWriter::addExtrudedCompositeCurve()](../../dc/df4/classimportIFClegacy_1_1IfcWriter.html#ae20c90d8d5b960aedee7975befc9b67f),
[importIFClegacy.IfcWriter::addExtrudedEllipse()](../../dc/df4/classimportIFClegacy_1_1IfcWriter.html#a405dcc9f171bbc597568aa00073d9e62),
and
[importIFClegacy.IfcWriter::addExtrudedPolyline()](../../dc/df4/classimportIFClegacy_1_1IfcWriter.html#a67c0c2b143eb222904067a2c4c1cca17).

## ◆ addCylinder()

void InventorBuilder::addCylinder  | ( | float  | _radius_ ,   
---|---|---|---  
|  | float  | _height_  
| ) | |   
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addDrawStyle()

void InventorBuilder::addDrawStyle  | ( | short  | _pointSize_ ,   
---|---|---|---  
|  | short  | _lineWidth_ ,   
|  | unsigned short  | _linePattern_ = `0xffff`,   
|  | const char *  | _style_ = `"FILLED"`  
| ) | |   
  
Sets a draw style node.

Parameters

     pointSize| \- the point size   
---|---  
lineWidth| \- the line width  
linePattern| \- the line pattern  
style| \- the draw style  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addFaceSet()

void InventorBuilder::addFaceSet  | ( | const std::vector< [int](../../d1/da0/classint.html) > & | _vertices_| ) |   
---|---|---|---|---|---  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addIndexedFaceSet()

void InventorBuilder::addIndexedFaceSet  | ( | const std::vector< [int](../../d1/da0/classint.html) > & | _indices_| ) |   
---|---|---|---|---|---  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40),
and
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ addInfo()

void InventorBuilder::addInfo  | ( | const char *  | _str_| ) |   
---|---|---|---|---|---  
  
Sets an info node.

Parameters

     str| \- text set to the info node   
---|---  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ addLabel()

void InventorBuilder::addLabel  | ( | const char *  | _str_| ) |   
---|---|---|---|---|---  
  
Sets a label node.

Parameters

     str| \- text set to the label node   
---|---  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ addLineSet() [1/2]

void InventorBuilder::addLineSet  | ( | | ) |   
---|---|---|---|---  
  
add an SoLineSet node

Adds a SoLineSet node after creating a SoCordinate3 node with
[beginPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917
"starts a point set") and
[endPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d
"ends the points set operation").

See also

    startPoints() 
     [beginPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917 "starts a point set")
     [endPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d "ends the points set operation")

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addLineSet() [2/2]

void InventorBuilder::addLineSet  | ( | const std::vector< [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) > & | _points_ ,   
---|---|---|---  
|  | short  | _lineSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`,   
|  | unsigned short  | _linePattern_ = `0xffff`  
| ) | |   
  
add a line defined by a list of points whereat always a pair (i.e. a point and
the following point) builds a line.

Add a line defined by a list of points whereat always a pair (i.e.

a point and the following point) builds a line. The size of the list must then
be even.

Referenced by
[Part::TopoShape::exportLineSet()](../../d8/ded/classPart_1_1TopoShape.html#adfe2d290d8a19a8026b8764529b48053).

## ◆ addMaterial()

void InventorBuilder::addMaterial  | ( | float  | _color_r_ ,   
---|---|---|---  
|  | float  | _color_g_ ,   
|  | float  | _color_b_ ,   
|  | float  | _color_a_ = `0`  
| ) | |   
  
Sets a material node. The colors are in the range [0, 1].

Parameters

     color_r| \- red color   
---|---  
color_g| \- green color  
color_b| \- blue color  
color_a| \- transparency  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40).

## ◆ addMaterialBinding()

void InventorBuilder::addMaterialBinding  | ( | const char *  | _binding_ = `"OVERALL"`| ) |   
---|---|---|---|---|---  
  
Sets a material binding node.

Parameters

     binding| \- binding of the material. Allowed values are: OVERALL, PER_PART, PER_PART_INDEXED, PER_FACE, PER_FACE_INDEXED, PER_VERTEX, PER_VERTEX_INDEXED and DEFAULT.   
---|---  
  
References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
and
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addNormalBinding()

void InventorBuilder::addNormalBinding  | ( | const char *  | _binding_| ) |   
---|---|---|---|---|---  
  
add normal binding node

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ addNurbsSurface()

void InventorBuilder::addNurbsSurface  | ( | const std::vector< [Base::Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) > & | _controlPoints_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _numUControlPoints_ ,   
|  | [int](../../d1/da0/classint.html) | _numVControlPoints_ ,   
|  | const std::vector< float > & | _uKnots_ ,   
|  | const std::vector< float > & | _vKnots_  
| ) | |   
  
The number of control points must be numUControlPoints * numVControlPoints.

The order in u or v direction of the NURBS surface is implicitly given by
number of elements in uKnots - numUControlPoints or number of elements in
vKnots - numVControlPoints.

## ◆ addPoint() [1/2]

void InventorBuilder::addPoint  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _vec_| ) |   
---|---|---|---|---|---  
  
add a single point

add a vector to a point set

References
[addPoint()](../../db/d7f/classBase_1_1InventorBuilder.html#a77961e2440f3bbbfebafd1c4d224e70d),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftguitools.gui_stretch.Stretch::action()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a23b5e547bf5d84dbecee7a970ebcb621),
and
[draftguitools.gui_stretch.Stretch::numericInput()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a5402b1eab63d5e107b781983de1bf033).

## ◆ addPoint() [2/2]

void InventorBuilder::addPoint  | ( | float  | _x_ ,   
---|---|---|---  
|  | float  | _y_ ,   
|  | float  | _z_  
| ) | |   
  
add a single point

insert a point in a point set

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[draftguitools.gui_stretch.Stretch::action()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a23b5e547bf5d84dbecee7a970ebcb621),
[addPoint()](../../db/d7f/classBase_1_1InventorBuilder.html#a04d481e0aae6c8be35c121a5ad92bc82),
[addPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#af1b546025002b5ff636b17d9e7b12764),
[draftguitools.gui_stretch.Stretch::numericInput()](../../df/d6e/classdraftguitools_1_1gui__stretch_1_1Stretch.html#a5402b1eab63d5e107b781983de1bf033),
and
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ addPoints()

void InventorBuilder::addPoints  | ( | const std::vector< [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) > & | _vec_| ) |   
---|---|---|---|---|---  
  
add a list of points

References
[addPoint()](../../db/d7f/classBase_1_1InventorBuilder.html#a77961e2440f3bbbfebafd1c4d224e70d),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40).

## ◆ addPointSet()

void InventorBuilder::addPointSet  | ( | | ) |   
---|---|---|---|---  
  
add an [SoPointSet](../../d0/d15/classSoPointSet.html) node

Adds an [SoPointSet](../../d0/d15/classSoPointSet.html) node after creating an
SoCordinate3 node with
[beginPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917
"starts a point set") and
[endPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d
"ends the points set operation").

See also

    startPoints() 
     [beginPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917 "starts a point set")
     [endPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d "ends the points set operation")

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addPolygonOffset()

void InventorBuilder::addPolygonOffset  | ( | float  | _factor_ = `1.0f`,   
---|---|---|---  
|  | float  | _units_ = `1.0f`,   
|  | const char *  | _styles_ = `"FILLED"`,   
|  | [bool](../../d9/db9/classbool.html) | _on_ = `true`  
| ) | |   
  
Sets a polygon offset node.

Parameters

     factor| \- Offset multiplication factor.   
---|---  
units| \- Offset translation multiplication factor.  
styles| \- Can be FILLED, LINES or POINTS.  
on| \- Whether the offset is on or off.  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addShapeHints()

void InventorBuilder::addShapeHints  | ( | float  | _crease_ = `0.0f`| ) |   
---|---|---|---|---|---  
  
Sets a shape hints node.

Parameters

     crease| \- the crease angle in radians   
---|---  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40).

## ◆ addSingleArrow()

void InventorBuilder::addSingleArrow  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt1_ ,   
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

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16),
[Base::Vector3< _Precision
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

void InventorBuilder::addSingleLine  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt1_ ,   
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

## ◆ addSinglePlane()

void InventorBuilder::addSinglePlane  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _base_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _eX_ ,   
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _eY_ ,   
|  | float  | _length_ ,   
|  | float  | _width_ ,   
|  | [bool](../../d9/db9/classbool.html) | _filled_ = `true`,   
|  | short  | _lineSize_ = `2`,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ addSingleTriangle()

void InventorBuilder::addSingleTriangle  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _pt0_ ,   
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

## ◆ addSphere()

void InventorBuilder::addSphere  | ( | float  | _radius_| ) |   
---|---|---|---|---|---  
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ addText() [1/2]

void InventorBuilder::addText  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _vec_ ,   
---|---|---|---  
|  | const char *  | _text_ ,   
|  | float  | _color_r_ = `1.0`,   
|  | float  | _color_g_ = `1.0`,   
|  | float  | _color_b_ = `1.0`  
| ) | |   
  
add a text

References
[addText()](../../db/d7f/classBase_1_1InventorBuilder.html#a5de5b1b47988a867b0e7b3ca8c45b6d5),
and
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ addText() [2/2]

void InventorBuilder::addText  | ( | float  | _pos_x_ ,   
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
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[addText()](../../db/d7f/classBase_1_1InventorBuilder.html#ad9a7fdefd3bb65d3c8d5b8b7b2133d9c).

## ◆ addTransformation() [1/2]

void InventorBuilder::addTransformation  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _transform_| ) |   
---|---|---|---|---|---  
  
adds a transformation

References
[addTransformation()](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[addTransformation()](../../db/d7f/classBase_1_1InventorBuilder.html#a6a994fa52660b07970bb2d9213f0257c).

## ◆ addTransformation() [2/2]

void InventorBuilder::addTransformation  | ( | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _translation_ ,   
---|---|---|---  
|  | const [Vector3f](../../db/d07/namespaceBase.html#a38ef9c7f08cd15bb67615a51ff6ad4ea) & | _rotationaxis_ ,   
|  | float  | _fAngle_  
| ) | |   
  
References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ beginMaterial()

void InventorBuilder::beginMaterial  | ( | | ) |   
---|---|---|---|---  
  
Starts a material node. The node must be closed with
[endMaterial](../../db/d7f/classBase_1_1InventorBuilder.html#ae4440b40a9c12a6490a9ba7fab360d0d)
and the colors must be added with
[addColor()](../../db/d7f/classBase_1_1InventorBuilder.html#ad578e90a3fd1b0c638eae078007e3a23).

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ beginNormal()

void InventorBuilder::beginNormal  | ( | | ) |   
---|---|---|---|---  
  
starts a point set

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ beginPoints()

void InventorBuilder::beginPoints  | ( | | ) |   
---|---|---|---|---  
  
starts a point set

Starts the definition of point set.

If possible don't make too many
[beginPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a30e15844b12bc74fc459aa3e2e0b5917
"starts a point set") and
[endPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d
"ends the points set operation") calls. Try to put all points in one set.

See also

    startPoints() 
     [endPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#a6bab7d7e13e40ca7f0f89ece9ea6860d "ends the points set operation")

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40),
and
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ beginSeparator()

void InventorBuilder::beginSeparator  | ( | | ) |   
---|---|---|---|---  
  
Sets a separator node.

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40),
[InventorBuilder()](../../db/d7f/classBase_1_1InventorBuilder.html#abc080de907a46e75cdd584965951cae3),
and
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ close()

void InventorBuilder::close  | ( | | ) |   
---|---|---|---|---  
  
If needed closes the first opened separator node. This method must not be used
more than one time for an instance.

References
[endSeparator()](../../db/d7f/classBase_1_1InventorBuilder.html#acde68aee5d63622468db3d7d911c3bd9).

Referenced by
[femexamples.examplesgui.FemExamples::reject()](../../d2/db9/classfemexamples_1_1examplesgui_1_1FemExamples.html#ade2cd979d737a9fa26b1e5f5ff8ebfcf),
and
[~InventorBuilder()](../../db/d7f/classBase_1_1InventorBuilder.html#a88188c4db1df50b6fd54d8e22e6a846e).

## ◆ endMaterial()

void InventorBuilder::endMaterial  | ( | | ) |   
---|---|---|---|---  
  
Closes a material node.

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

## ◆ endNormal()

void InventorBuilder::endNormal  | ( | | ) |   
---|---|---|---|---  
  
ends the points set operation

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ endPoints()

void InventorBuilder::endPoints  | ( | | ) |   
---|---|---|---|---  
  
ends the points set operation

Ends the point set operations and write the resulting inventor string.

See also

    startPoints() 

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40),
and
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

## ◆ endSeparator()

void InventorBuilder::endSeparator  | ( | | ) |   
---|---|---|---|---  
  
Closes the last added separator node.

References
[Base::blanks()](../../db/d07/namespaceBase.html#a176dac8c92fe83e9203268fc74e95e16).

Referenced by
[close()](../../db/d7f/classBase_1_1InventorBuilder.html#a578c7a0e879c5b5fa8d2587bc497cd74),
[Part::TopoShape::exportFaceSet()](../../d8/ded/classPart_1_1TopoShape.html#aa26580dafd44362632976faf4e694c40),
and
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Builder3D.h
  * FreeCAD/src/Base/Builder3D.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

