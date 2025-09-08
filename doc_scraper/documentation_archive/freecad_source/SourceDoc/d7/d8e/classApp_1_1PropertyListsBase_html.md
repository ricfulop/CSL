---
url: https://freecad.github.io/SourceDoc/d7/d8e/classApp_1_1PropertyListsBase.html
scraped_at: 2025-09-08T14:56:21.896397
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [PropertyListsBase](../../d7/d8e/classApp_1_1PropertyListsBase.html)

[List of all members](../../d2/d21/classApp_1_1PropertyListsBase-members.html) | Public Member Functions | Protected Member Functions

App::PropertyListsBase Class Referenceabstract

Helper class to construct list like properties.
[More...](../../d7/d8e/classApp_1_1PropertyListsBase.html#details)

`#include <Property.h>`

##  Public Member Functions  
  
---  
void | [clearTouchList](../../d7/d8e/classApp_1_1PropertyListsBase.html#aaca8b243e8c7606d81aa0bbadf1fefa1) ()  
virtual [int](../../d1/da0/classint.html) | [getSize](../../d7/d8e/classApp_1_1PropertyListsBase.html#acbdccea70aaba518e3af5ac37580d54d) (void) const =0  
const std::set< [int](../../d1/da0/classint.html) > & | [getTouchList](../../d7/d8e/classApp_1_1PropertyListsBase.html#a7ff4978224bd672331d098bfeeb07f09) () const  
virtual void | [setSize](../../d7/d8e/classApp_1_1PropertyListsBase.html#a59f18e45d11306be56f29104af5b2160) ([int](../../d1/da0/classint.html) newSize)=0  
  
##  Protected Member Functions  
  
---  
virtual void | [setPyValues](../../d7/d8e/classApp_1_1PropertyListsBase.html#a33a3c42a6dd5aa648329c817e8689921) (const std::vector< [PyObject](../../df/d1b/classPyObject.html) * > &vals, const std::vector< [int](../../d1/da0/classint.html) > &indices)  
  
## Detailed Description

Helper class to construct list like properties.

This class is not derived from
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") so that we can have more
that one base class for list like properties, e.g. see PropertyList, and
[PropertyLinkListBase](../../d7/d87/classApp_1_1PropertyLinkListBase.html)

## Member Function Documentation

## ◆ clearTouchList()

void App::PropertyListsBase::clearTouchList  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getSize()

| virtual [int](../../d1/da0/classint.html) App::PropertyListsBase::getSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
pure virtual  
  
Implemented in
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#ac7640f2773164fcd647c9d53f924938d),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#acf9cc589535ac3d757dbcbace37f64b8),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a86475a63b100faa4e9026d0873c34007),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#ac7640f2773164fcd647c9d53f924938d),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#ac10387ae8617d942310a4500838595e7),
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#a7ae48385c611403bd07d193c96876425),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#aa10973bbf26a90a24de1eb77f8b038c9),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#a618dc4313b673538c182cd8c78eb56d3),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#abd9a6904c00fcc1a14e52d83a612225c),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a43f7395d585b8fa0f9b10ad91f65b24d),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#ad8638b78dd2f9aa7abb0e0d7c049d170),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#a7a5cc0dba4f813d2915920b4317175a3),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#accfe26546444d16274b5c0ed9d9db656),
[App::PropertyListsT< T, ListT, ParentT
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< bool, boost::dynamic_bitset<>
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< double
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< long
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< DocumentObject *, std::vector< DocumentObject * >,
PropertyLinkListBase
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< Material
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< Base::Placement
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< std::string
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
[App::PropertyListsT< Base::Vector3d
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a8ba07a42e39278c7822e32c566faa194),
and
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#a2acba56e591248129a8fe02fda121ddf).

Referenced by
[Gui::ViewProviderLink::applyMaterial()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2116838fd198dca3f32851993fc65e2a),
[Surface::GeomFillSurface::onChanged()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
and
[Gui::ViewProviderLink::updateElementList()](../../d6/d59/classGui_1_1ViewProviderLink.html#a052097f0154c16d7e207c626e115cddf).

## ◆ getTouchList()

const std::set< [int](../../d1/da0/classint.html) > & App::PropertyListsBase::getTouchList  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ setPyValues()

| virtual void App::PropertyListsBase::setPyValues  | ( | const std::vector< [PyObject](../../df/d1b/classPyObject.html) * > & | _vals_ ,   
---|---|---|---  
|  | const std::vector< [int](../../d1/da0/classint.html) > & | _indices_  
| ) | |   
protectedvirtual  
  
Reimplemented in [App::PropertyListsT< T, ListT, ParentT
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< bool, boost::dynamic_bitset<>
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< double
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< long
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< DocumentObject *, std::vector< DocumentObject * >,
PropertyLinkListBase
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< Material
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< Base::Placement
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
[App::PropertyListsT< std::string
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e),
and [App::PropertyListsT< Base::Vector3d
>](../../d1/d0e/classApp_1_1PropertyListsT.html#ad8773f373375f670a161bca64cad259e).

## ◆ setSize()

| virtual void App::PropertyListsBase::setSize  | ( | [int](../../d1/da0/classint.html) | _newSize_| ) |   
---|---|---|---|---|---  
pure virtual  
  
Implemented in
[Inspection::PropertyDistanceList](../../d2/db9/classInspection_1_1PropertyDistanceList.html#ab2364bb0d2831094893ff3666e4b96c1),
[Mesh::PropertyNormalList](../../df/dcd/classMesh_1_1PropertyNormalList.html#ade5d8d20b945d222f9ba4a3710ac5e85),
[Mesh::PropertyCurvatureList](../../df/d3b/classMesh_1_1PropertyCurvatureList.html#acbc55731d97272fd544169554b691f05),
[Part::PropertyGeometryList](../../db/dca/classPart_1_1PropertyGeometryList.html#a6a2e6461c2bd37cd15dec978f34531a4),
[Part::PropertyShapeHistory](../../de/d7c/classPart_1_1PropertyShapeHistory.html#acda04ae40296391d7ddf13ea82bd6537),
[Part::PropertyFilletEdges](../../d4/d0b/classPart_1_1PropertyFilletEdges.html#acca9ddd2812a00af7646c13bf212977b),
[Points::PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html#a460f4f221124eec66f416d7af3549e65),
[Points::PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html#ade5d8d20b945d222f9ba4a3710ac5e85),
[Points::PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#af93946209fabd6700ca0906bae5e166c),
[TechDraw::PropertyCenterLineList](../../d7/d94/classTechDraw_1_1PropertyCenterLineList.html#a0e65ef1faab380410b4c91f299b1b526),
[TechDraw::PropertyCosmeticEdgeList](../../d6/da1/classTechDraw_1_1PropertyCosmeticEdgeList.html#aa00b73b1e0d582f0b2775a6553ae831e),
[TechDraw::PropertyCosmeticVertexList](../../d7/d50/classTechDraw_1_1PropertyCosmeticVertexList.html#ad2592b18eb696920372b71f4ac19da43),
[TechDraw::PropertyGeomFormatList](../../d2/d4f/classTechDraw_1_1PropertyGeomFormatList.html#a9d11ed2a3f2dd0d7cd3d67c809a8b37a),
[App::PropertyListsT< T, ListT, ParentT
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< bool, boost::dynamic_bitset<>
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< Color
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< double
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< long
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< DocumentObject *, std::vector< DocumentObject * >,
PropertyLinkListBase
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< Material
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< Base::Placement
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< std::string
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyListsT< Base::Vector3d
>](../../d1/d0e/classApp_1_1PropertyListsT.html#a01237b2692f43697adba2000258accc9),
[App::PropertyLinkList](../../d3/d8c/classApp_1_1PropertyLinkList.html#a05972fc1163a21a73e4526a071896f92),
and
[Sketcher::PropertyConstraintList](../../d4/dd6/classSketcher_1_1PropertyConstraintList.html#abb7ea1204c78c8ecc237283f24e7d14a).

Referenced by
[Surface::GeomFillSurface::onChanged()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#a3bfc3e08b782ee0cb3ccb98f8dd1600f),
and
[Gui::ViewProviderLink::updateElementList()](../../d6/d59/classGui_1_1ViewProviderLink.html#a052097f0154c16d7e207c626e115cddf).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Property.h
  * FreeCAD/src/App/Property.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

