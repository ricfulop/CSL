---
url: https://freecad.github.io/SourceDoc/d6/dac/namespacePoints.html
scraped_at: 2025-09-08T14:51:45.765824
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Functions

Points Namespace Reference

##  Classes  
  
---  
class | [AscReader](../../d8/d6d/classPoints_1_1AscReader.html)  
class | [AscWriter](../../d1/d45/classPoints_1_1AscWriter.html)  
class | [Converter](../../d9/d0c/classPoints_1_1Converter.html)  
class | [ConverterT](../../d5/d4a/classPoints_1_1ConverterT.html)  
struct | [CurvatureInfo](../../d9/d70/structPoints_1_1CurvatureInfo.html)  
| Curvature information.
[More...](../../d9/d70/structPoints_1_1CurvatureInfo.html#details)  
  
class | [DataStreambuf](../../dd/dba/classPoints_1_1DataStreambuf.html)  
class | [E57Reader](../../d2/dfb/classPoints_1_1E57Reader.html)  
class | [Feature](../../d8/de3/classPoints_1_1Feature.html)  
| [Base](../../db/d07/namespaceBase.html "Basic structures used by other
FreeCAD components \(C++ API\)") class of all
[Points](../../d6/dac/namespacePoints.html) feature classes in FreeCAD.
[More...](../../d8/de3/classPoints_1_1Feature.html#details)  
  
class | [Module](../../d4/d06/classPoints_1_1Module.html)  
class | [PcdReader](../../d1/da3/classPoints_1_1PcdReader.html)  
class | [PcdWriter](../../df/dc2/classPoints_1_1PcdWriter.html)  
class | [PlyReader](../../d4/d25/classPoints_1_1PlyReader.html)  
class | [PlyWriter](../../d4/d57/classPoints_1_1PlyWriter.html)  
class | [PointKernel](../../dc/de1/classPoints_1_1PointKernel.html)  
| [Point](../../dc/d4f/classPoint.html) kernel.
[More...](../../dc/de1/classPoints_1_1PointKernel.html#details)  
  
class | [PointsAlgos](../../d8/d62/classPoints_1_1PointsAlgos.html)  
| The [Points](../../d6/dac/namespacePoints.html) algorithms container class.
[More...](../../d8/d62/classPoints_1_1PointsAlgos.html#details)  
  
class | [PointsGrid](../../d1/d4d/classPoints_1_1PointsGrid.html)  
| The [PointsGrid](../../d1/d4d/classPoints_1_1PointsGrid.html "The PointsGrid
allows to divide a global point cloud into smaller regions of elements
depending on th...") allows to divide a global point cloud into smaller
regions of elements depending on the resolution of the grid.
[More...](../../d1/d4d/classPoints_1_1PointsGrid.html#details)  
  
class | [PointsGridIterator](../../d5/d1b/classPoints_1_1PointsGridIterator.html)  
| The [PointsGridIterator](../../d5/d1b/classPoints_1_1PointsGridIterator.html
"The PointsGridIterator class provides an interface to walk through all grid
elements of a point grid.") class provides an interface to walk through all
grid elements of a point grid.
[More...](../../d5/d1b/classPoints_1_1PointsGridIterator.html#details)  
  
class | [PropertyCurvatureList](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html)  
| The Curvature property class.
[More...](../../dd/d6e/classPoints_1_1PropertyCurvatureList.html#details)  
  
class | [PropertyGreyValue](../../da/d08/classPoints_1_1PropertyGreyValue.html)  
| Greyvalue property.
[More...](../../da/d08/classPoints_1_1PropertyGreyValue.html#details)  
  
class | [PropertyGreyValueList](../../d2/dbc/classPoints_1_1PropertyGreyValueList.html)  
class | [PropertyNormalList](../../d0/d1e/classPoints_1_1PropertyNormalList.html)  
class | [PropertyPointKernel](../../d7/dfa/classPoints_1_1PropertyPointKernel.html)  
| The point kernel property.
[More...](../../d7/dfa/classPoints_1_1PropertyPointKernel.html#details)  
  
class | [Reader](../../dc/d70/classPoints_1_1Reader.html)  
class | [Structured](../../d0/d43/classPoints_1_1Structured.html)  
class | [Writer](../../d1/de9/classPoints_1_1Writer.html)  
  
##  Typedefs  
  
---  
typedef std::shared_ptr< [Converter](../../d9/d0c/classPoints_1_1Converter.html) > | [ConverterPtr](../../d6/dac/namespacePoints.html#a6af7d0af92b0c32f93efb5070d5318e2)  
typedef [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [Feature](../../d8/de3/classPoints_1_1Feature.html) > | [FeatureCustom](../../d6/dac/namespacePoints.html#a9beb79e2f21e58d1263fa6e4da961bdb)  
typedef [App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)< [Feature](../../d8/de3/classPoints_1_1Feature.html) > | [FeaturePython](../../d6/dac/namespacePoints.html#af62d36f2228a50cdb156456b575e1a3a)  
typedef [App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)< [Structured](../../d0/d43/classPoints_1_1Structured.html) > | [StructuredCustom](../../d6/dac/namespacePoints.html#a455d9f3a779a188e3a642c80a2b93d76)  
  
##  Functions  
  
---  
[PyObject](../../df/d1b/classPyObject.html) * | [initModule](../../d6/dac/namespacePoints.html#a10e42a87bd0ce5a29e3294b2be4e86fa) ()  
unsigned [int](../../d1/da0/classint.html) | [lzfDecompress](../../d6/dac/namespacePoints.html#a0ee5d29a8da3a1164dcedc9679f5a3b1) (const void *const in_data, unsigned [int](../../d1/da0/classint.html) in_len, void *out_data, unsigned [int](../../d1/da0/classint.html) out_len)  
  
## Typedef Documentation

## ◆ ConverterPtr

typedef
std::shared_ptr<[Converter](../../d9/d0c/classPoints_1_1Converter.html)>
[Points::ConverterPtr](../../d6/dac/namespacePoints.html#a6af7d0af92b0c32f93efb5070d5318e2)  
---  
  
## ◆ FeatureCustom

typedef
[App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)<[Feature](../../d8/de3/classPoints_1_1Feature.html)>
[Points::FeatureCustom](../../d6/dac/namespacePoints.html#a9beb79e2f21e58d1263fa6e4da961bdb)  
---  
  
## ◆ FeaturePython

typedef
[App::FeaturePythonT](../../d2/d2f/classApp_1_1FeaturePythonT.html)<[Feature](../../d8/de3/classPoints_1_1Feature.html)>
[Points::FeaturePython](../../d6/dac/namespacePoints.html#af62d36f2228a50cdb156456b575e1a3a)  
---  
  
## ◆ StructuredCustom

typedef
[App::FeatureCustomT](../../d7/d3f/classApp_1_1FeatureCustomT.html)<[Structured](../../d0/d43/classPoints_1_1Structured.html)>
[Points::StructuredCustom](../../d6/dac/namespacePoints.html#a455d9f3a779a188e3a642c80a2b93d76)  
---  
  
## Function Documentation

## ◆ initModule()

[PyObject](../../df/d1b/classPyObject.html) * Points::initModule  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::InterpreterSingleton::addModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af556d495376be43c3d93c9a44e6c15d3),
and
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9).

## ◆ lzfDecompress()

unsigned [int](../../d1/da0/classint.html) Points::lzfDecompress  | ( | const void *const  | _in_data_ ,   
---|---|---|---  
|  | unsigned [int](../../d1/da0/classint.html) | _in_len_ ,   
|  | void *  | _out_data_ ,   
|  | unsigned [int](../../d1/da0/classint.html) | _out_len_  
| ) | |   
  
Referenced by
[Points::PcdReader::read()](../../d1/da3/classPoints_1_1PcdReader.html#ab7ee26c11617aff96332fdd092ebe0e7).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

