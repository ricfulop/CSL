---
url: https://freecad.github.io/SourceDoc/d5/d7f/namespaceAdaptivePath.html
scraped_at: 2025-09-08T14:52:39.034288
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Enumerations | Functions | Variables

AdaptivePath Namespace Reference

##  Classes  
  
---  
class | [Adaptive2d](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html)  
struct | [AdaptiveOutput](../../d4/de0/structAdaptivePath_1_1AdaptiveOutput.html)  
class | [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html)  
class | [ClearedArea](../../d8/d56/classAdaptivePath_1_1ClearedArea.html)  
class | [EngagePoint](../../de/d69/classAdaptivePath_1_1EngagePoint.html)  
class | [Interpolation](../../d1/d41/classAdaptivePath_1_1Interpolation.html)  
class | [PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html)  
  
##  Typedefs  
  
---  
typedef std::vector< [DPoint](../../d5/d7f/namespaceAdaptivePath.html#a20f9e7349f07dd1934a6cdc1624249e4) > | [DPath](../../d5/d7f/namespaceAdaptivePath.html#afab810c69c26744ebbeebc445bc2945f)  
typedef std::vector< [DPath](../../d5/d7f/namespaceAdaptivePath.html#afab810c69c26744ebbeebc445bc2945f) > | [DPaths](../../d5/d7f/namespaceAdaptivePath.html#a3e730733009ac85e2afe8df986221df6)  
typedef std::pair< double, double > | [DPoint](../../d5/d7f/namespaceAdaptivePath.html#a20f9e7349f07dd1934a6cdc1624249e4)  
typedef std::pair< [int](../../d1/da0/classint.html), [DPath](../../d5/d7f/namespaceAdaptivePath.html#afab810c69c26744ebbeebc445bc2945f) > | [TPath](../../d5/d7f/namespaceAdaptivePath.html#ab3cb2e8660d7a1d22c0fc7b0a822386e)  
typedef std::vector< [TPath](../../d5/d7f/namespaceAdaptivePath.html#ab3cb2e8660d7a1d22c0fc7b0a822386e) > | [TPaths](../../d5/d7f/namespaceAdaptivePath.html#a111e8ff22b4a96deb14103b0ca204475)  
  
##  Enumerations  
  
---  
enum | [MotionType](../../d5/d7f/namespaceAdaptivePath.html#a4312e82e30aab678d37f6cd6a038cf30) { [mtCutting](../../d5/d7f/namespaceAdaptivePath.html#a4312e82e30aab678d37f6cd6a038cf30aa65deb754cbf35b43eb54dd161aa39fe) = 0 , [mtLinkClear](../../d5/d7f/namespaceAdaptivePath.html#a4312e82e30aab678d37f6cd6a038cf30a8f929fd43e185d8f621a604410144148) = 1 , [mtLinkNotClear](../../d5/d7f/namespaceAdaptivePath.html#a4312e82e30aab678d37f6cd6a038cf30a90bc37450179f21697d35bc8fd815b0b) = 2 , [mtLinkClearAtPrevPass](../../d5/d7f/namespaceAdaptivePath.html#a4312e82e30aab678d37f6cd6a038cf30ae8eacbec659824c6bbf1a2821e808963) = 3 }  
enum | [OperationType](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74) { [otClearingInside](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74a6b21425fde7ddf7144c12c1ce3050ba9) = 0 , [otClearingOutside](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74a05470e39492cd9d4abe718c0c7b03cde) = 1 , [otProfilingInside](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74a894933a048131ef89bfc07fb708c5f8d) = 2 , [otProfilingOutside](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74ae15cbf7a7a66441a52470c644d87f2fd) = 3 }  
  
##  Functions  
  
---  
double | [Angle3Points](../../d5/d7f/namespaceAdaptivePath.html#a22d57a69db291bf571f2f87bc771f549) (const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) &p1, const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) &p2, const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) &p3)  
void | [appendDirectChildPaths](../../d5/d7f/namespaceAdaptivePath.html#ae4de2e0c14dadfa4dd7c25b581fdb8ea) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &outPaths, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path, const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
void | [AverageDirection](../../d5/d7f/namespaceAdaptivePath.html#a53e335e8d70a48d2e258016ca36310f3) (const vector< [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) > &unityVectors, [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) &output)  
double | [averageDV](../../d5/d7f/namespaceAdaptivePath.html#af1aa43ee514aa09b480432bed4852e81) (const vector< double > &vec)  
[bool](../../d9/db9/classbool.html) | [Circle2CircleIntersect](../../d5/d7f/namespaceAdaptivePath.html#aa4cc9428e38c16e83c2a1a8dfa7259ba) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &c1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &c2, double radius, pair< [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html), [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) > &intersections)  
void | [CleanPath](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &inp, [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &outpt, double tolerance)  
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | [Compute2DPolygonCentroid](../../d5/d7f/namespaceAdaptivePath.html#a7e3ab5cf7e4195ca49aafc4384c26b35) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &vertices)  
void | [ConnectPaths](../../d5/d7f/namespaceAdaptivePath.html#a26e83a95426b4f1c05b3eb98b4a04a17) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) input, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &output)  
void | [DeduplicatePaths](../../d5/d7f/namespaceAdaptivePath.html#a37e54774ebe2ecb52e17897441349d53) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &inputs, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &outputs)  
[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) | [DirectionV](../../d5/d7f/namespaceAdaptivePath.html#a6e0b5d3a809d33ef38b51885367e5805) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2)  
double | [DistancePointToLineSegSquared](../../d5/d7f/namespaceAdaptivePath.html#aba8ae65365f5e2bbb8523972dcfd5fb2) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &closestPoint, double &ptParameter, [bool](../../d9/db9/classbool.html) clamp=true)  
double | [DistancePointToPathsSqrd](../../d5/d7f/namespaceAdaptivePath.html#a89520a92ca7969451829159fb5bd2e1e) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &closestPointOnPath, size_t &clpPathIndex, size_t &clpSegmentIndex, double &clpParameter)  
double | [DistanceSqrd](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2)  
[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) | [GetPathDirectionV](../../d5/d7f/namespaceAdaptivePath.html#a22a79624aeb88db033fcc505612cc874) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &pth, size_t pointIndex)  
[int](../../d1/da0/classint.html) | [getPathNestingLevel](../../d5/d7f/namespaceAdaptivePath.html#afe6b9d42c4e97db975f5acf577006f18) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path, const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
[bool](../../d9/db9/classbool.html) | [HasAnyPath](../../d5/d7f/namespaceAdaptivePath.html#a7713b0ac1107929fe11ef5082ef1f11e) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
[bool](../../d9/db9/classbool.html) | [IntersectionPoint](../../d5/d7f/namespaceAdaptivePath.html#ac652f5c393ef400162a3673caf7da369) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &s1p1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &s1p2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &s2p1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &s2p2, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &intersection)  
[bool](../../d9/db9/classbool.html) | [IntersectionPoint](../../d5/d7f/namespaceAdaptivePath.html#a393af31a1bf0ed6ef6428832dd4a596b) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p2, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &intersection)  
[bool](../../d9/db9/classbool.html) | [IsPointWithinCutRegion](../../d5/d7f/namespaceAdaptivePath.html#aca8e289d9ec01dd727d3a7f033e12a66) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &toolBoundPaths, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &point)  
[bool](../../d9/db9/classbool.html) | [Line2CircleIntersect](../../d5/d7f/namespaceAdaptivePath.html#a162b44dbc1289576521d7d3e3084562f) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &c, double radius, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p2, vector< [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) > &result, [bool](../../d9/db9/classbool.html) clamp=true)  
void | [NormalizeV](../../d5/d7f/namespaceAdaptivePath.html#a3bef0f614a61133f0b91faaaebf0813b) ([DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) &pt)  
std::ostream & | [operator<<](../../d5/d7f/namespaceAdaptivePath.html#a7581832785c462a61224cb1b530d709e) (std::ostream &s, const [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html) &p)  
double | [PathLength](../../d5/d7f/namespaceAdaptivePath.html#a1932f3bdb66c3d46bb2ae0ab68b03b7c) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path)  
double | [PointSideOfLine](../../d5/d7f/namespaceAdaptivePath.html#a443621d89fda38d492b838c7914e3dc7) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt)  
[bool](../../d9/db9/classbool.html) | [PopPathWithClosestPoint](../../d5/d7f/namespaceAdaptivePath.html#a42481360e50af9d93ddfabe9d89bc66b) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) p1, [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &result)  
[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) | [rotate](../../d5/d7f/namespaceAdaptivePath.html#a2b3cf70176f74575cc881038c11ff0ed) (const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) &in, double rad)  
void | [ScaleDownPaths](../../d5/d7f/namespaceAdaptivePath.html#a5e663fe75845628f35785043c4dd7077) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, long scaleFactor)  
void | [ScaleUpPaths](../../d5/d7f/namespaceAdaptivePath.html#ab9301ab629d4e88b24a71eb54755114a) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, long scaleFactor)  
[bool](../../d9/db9/classbool.html) | [SetSegmentLength](../../d5/d7f/namespaceAdaptivePath.html#aace2cca9424c6fa5bb3f7302878b0a29) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2, double new_length)  
void | [SmoothPaths](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, double stepSize, long pointCount, long iterations)  
  
##  Variables  
  
---  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_AppendToolPath](../../d5/d7f/namespaceAdaptivePath.html#a06a9326d821c12fbdd404c6d77de646c) ("AppendToolPath")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_CalcCutAreaCirc](../../d5/d7f/namespaceAdaptivePath.html#aa770bc00b527a7a1a909097b112542e6) ("CalcCutArea")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_CalcCutAreaClip](../../d5/d7f/namespaceAdaptivePath.html#a47c2fdc83128d7f53f196dd1b64bebd6) ("CalcCutAreaClip")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_DistanceToBoundary](../../d5/d7f/namespaceAdaptivePath.html#ad855ff1a739bca823544cb51f3f92de4) ("DistanceToBoundary")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_ExpandCleared](../../d5/d7f/namespaceAdaptivePath.html#a50017e1cb8671a90d2a954c13b84aa49) ("ExpandCleared")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_IsAllowedToCutTrough](../../d5/d7f/namespaceAdaptivePath.html#afffc37348a653316e37a1558f0aaae5f) ("IsAllowedToCutTrough")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_IsClearPath](../../d5/d7f/namespaceAdaptivePath.html#a0b58c68f81583306b8c62502b42e3ae4) ("IsClearPath")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_NextEngagePoint](../../d5/d7f/namespaceAdaptivePath.html#ada87d43aa4289654662208cf8a063726) ("NextEngagePoint")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_PointIterations](../../d5/d7f/namespaceAdaptivePath.html#a3c15f08d7bc103fa61a7c0ed7fd0acc4) ("PointIterations")  
[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) | [Perf_ProcessPolyNode](../../d5/d7f/namespaceAdaptivePath.html#aa71e6b6113bfdb0433ac04cb361b11e2) ("ProcessPolyNode")  
  
## Typedef Documentation

## ◆ DPath

typedef
std::vector<[DPoint](../../d5/d7f/namespaceAdaptivePath.html#a20f9e7349f07dd1934a6cdc1624249e4)>
[AdaptivePath::DPath](../../d5/d7f/namespaceAdaptivePath.html#afab810c69c26744ebbeebc445bc2945f)  
---  
  
## ◆ DPaths

typedef
std::vector<[DPath](../../d5/d7f/namespaceAdaptivePath.html#afab810c69c26744ebbeebc445bc2945f)>
[AdaptivePath::DPaths](../../d5/d7f/namespaceAdaptivePath.html#a3e730733009ac85e2afe8df986221df6)  
---  
  
## ◆ DPoint

typedef std::pair<double, double>
[AdaptivePath::DPoint](../../d5/d7f/namespaceAdaptivePath.html#a20f9e7349f07dd1934a6cdc1624249e4)  
---  
  
## ◆ TPath

typedef std::pair<[int](../../d1/da0/classint.html),
[DPath](../../d5/d7f/namespaceAdaptivePath.html#afab810c69c26744ebbeebc445bc2945f)>
[AdaptivePath::TPath](../../d5/d7f/namespaceAdaptivePath.html#ab3cb2e8660d7a1d22c0fc7b0a822386e)  
---  
  
## ◆ TPaths

typedef
std::vector<[TPath](../../d5/d7f/namespaceAdaptivePath.html#ab3cb2e8660d7a1d22c0fc7b0a822386e)>
[AdaptivePath::TPaths](../../d5/d7f/namespaceAdaptivePath.html#a111e8ff22b4a96deb14103b0ca204475)  
---  
  
## Enumeration Type Documentation

## ◆ MotionType

enum
[AdaptivePath::MotionType](../../d5/d7f/namespaceAdaptivePath.html#a4312e82e30aab678d37f6cd6a038cf30)  
---  
  
Enumerator  
---  
mtCutting |   
mtLinkClear |   
mtLinkNotClear |   
mtLinkClearAtPrevPass |   
  
## ◆ OperationType

enum
[AdaptivePath::OperationType](../../d5/d7f/namespaceAdaptivePath.html#ae84b50235dbf1d89c136982756c1bb74)  
---  
  
Enumerator  
---  
otClearingInside |   
otClearingOutside |   
otProfilingInside |   
otProfilingOutside |   
  
## Function Documentation

## ◆ Angle3Points()

double AdaptivePath::Angle3Points  | ( | const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) & | _p1_ ,   
---|---|---|---  
|  | const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) & | _p2_ ,   
|  | const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) & | _p3_  
| ) | |   
  
References
[ClipperLib::DoublePoint::X](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a675837cc05f20447313789b82d84ad31),
and
[ClipperLib::DoublePoint::Y](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a49774a93540882d88448badf37034454).

## ◆ appendDirectChildPaths()

void AdaptivePath::appendDirectChildPaths  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _outPaths_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_ ,   
|  | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_  
| ) | |   
  
References
[getPathNestingLevel()](../../d5/d7f/namespaceAdaptivePath.html#afe6b9d42c4e97db975f5acf577006f18),
and
[ClipperLib::PointInPolygon()](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ AverageDirection()

void AdaptivePath::AverageDirection  | ( | const vector< [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) > & | _unityVectors_ ,   
---|---|---|---  
|  | [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) & | _output_  
| ) | |   
  
References
[ClipperLib::DoublePoint::X](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a675837cc05f20447313789b82d84ad31),
and
[ClipperLib::DoublePoint::Y](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a49774a93540882d88448badf37034454).

## ◆ averageDV()

double AdaptivePath::averageDV  | ( | const vector< double > & | _vec_| ) |   
---|---|---|---|---|---  
  
References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ Circle2CircleIntersect()

[bool](../../d9/db9/classbool.html) AdaptivePath::Circle2CircleIntersect  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _c1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _c2_ ,   
|  | double  | _radius_ ,   
|  | pair< [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html), [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) > & | _intersections_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ CleanPath()

void AdaptivePath::CleanPath  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _inp_ ,   
---|---|---|---  
|  | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _outpt_ ,   
|  | double  | _tolerance_  
| ) | |   
  
References
[ClipperLib::CleanPolygon()](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b),
[DistancePointToPathsSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a89520a92ca7969451829159fb5bd2e1e),
[DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
and
[draftutils.utils::tolerance()](../../de/d75/group__draftutils.html#ga1f502535eabb15dc7272a379b2ce858e).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
and
[SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962).

## ◆ Compute2DPolygonCentroid()

[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) AdaptivePath::Compute2DPolygonCentroid  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _vertices_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::DoublePoint::X](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a675837cc05f20447313789b82d84ad31),
and
[ClipperLib::DoublePoint::Y](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a49774a93540882d88448badf37034454).

## ◆ ConnectPaths()

void AdaptivePath::ConnectPaths  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) | _input_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _output_  
| ) | |   
  
References
[DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
and
[ClipperLib::ReversePath()](../../df/db2/namespaceClipperLib.html#ab6376320953c60093dc73462c74589e1).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ DeduplicatePaths()

void AdaptivePath::DeduplicatePaths  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _inputs_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _outputs_  
| ) | |   
  
References
[DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ DirectionV()

[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) AdaptivePath::DirectionV  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[GetPathDirectionV()](../../d5/d7f/namespaceAdaptivePath.html#a22a79624aeb88db033fcc505612cc874).

## ◆ DistancePointToLineSegSquared()

double AdaptivePath::DistancePointToLineSegSquared  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _closestPoint_ ,   
|  | double & | _ptParameter_ ,   
|  | [bool](../../d9/db9/classbool.html) | _clamp_ = `true`  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[DistancePointToPathsSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a89520a92ca7969451829159fb5bd2e1e).

## ◆ DistancePointToPathsSqrd()

double AdaptivePath::DistancePointToPathsSqrd  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _closestPointOnPath_ ,   
|  | size_t & | _clpPathIndex_ ,   
|  | size_t & | _clpSegmentIndex_ ,   
|  | double & | _clpParameter_  
| ) | |   
  
References
[DistancePointToLineSegSquared()](../../d5/d7f/namespaceAdaptivePath.html#aba8ae65365f5e2bbb8523972dcfd5fb2).

Referenced by
[CleanPath()](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4).

## ◆ DistanceSqrd()

double AdaptivePath::DistanceSqrd  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[CleanPath()](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4),
[ConnectPaths()](../../d5/d7f/namespaceAdaptivePath.html#a26e83a95426b4f1c05b3eb98b4a04a17),
[DeduplicatePaths()](../../d5/d7f/namespaceAdaptivePath.html#a37e54774ebe2ecb52e17897441349d53),
[AdaptivePath::EngagePoint::getCurrentDir()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a64238fcdbfa9f4bf6a2fc4f000405339),
[AdaptivePath::EngagePoint::getCurrentPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a4a25dac76882d1527f13a9f4683024a2),
[AdaptivePath::EngagePoint::moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310),
[PathLength()](../../d5/d7f/namespaceAdaptivePath.html#a1932f3bdb66c3d46bb2ae0ab68b03b7c),
[PopPathWithClosestPoint()](../../d5/d7f/namespaceAdaptivePath.html#a42481360e50af9d93ddfabe9d89bc66b),
and
[SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962).

## ◆ GetPathDirectionV()

[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) AdaptivePath::GetPathDirectionV  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _pth_ ,   
---|---|---|---  
|  | size_t  | _pointIndex_  
| ) | |   
  
References
[DirectionV()](../../d5/d7f/namespaceAdaptivePath.html#a6e0b5d3a809d33ef38b51885367e5805).

## ◆ getPathNestingLevel()

[int](../../d1/da0/classint.html) AdaptivePath::getPathNestingLevel  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_ ,   
---|---|---|---  
|  | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_  
| ) | |   
  
References
[ClipperLib::PointInPolygon()](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212).

Referenced by
[appendDirectChildPaths()](../../d5/d7f/namespaceAdaptivePath.html#ae4de2e0c14dadfa4dd7c25b581fdb8ea),
and
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ HasAnyPath()

[bool](../../d9/db9/classbool.html) AdaptivePath::HasAnyPath  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_| ) |   
---|---|---|---|---|---  
  
## ◆ IntersectionPoint() [1/2]

[bool](../../d9/db9/classbool.html) AdaptivePath::IntersectionPoint  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _s1p1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _s1p2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _s2p1_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _s2p2_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _intersection_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ IntersectionPoint() [2/2]

[bool](../../d9/db9/classbool.html) AdaptivePath::IntersectionPoint  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p2_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _intersection_  
| ) | |   
  
References
[AdaptivePath::BoundBox::AddPoint()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a47b23bb75413d049f127728ad178ea76),
[AdaptivePath::BoundBox::CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ IsPointWithinCutRegion()

[bool](../../d9/db9/classbool.html) AdaptivePath::IsPointWithinCutRegion  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _toolBoundPaths_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _point_  
| ) | |   
  
References
[ClipperLib::PointInPolygon()](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212).

## ◆ Line2CircleIntersect()

[bool](../../d9/db9/classbool.html) AdaptivePath::Line2CircleIntersect  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _c_ ,   
---|---|---|---  
|  | double  | _radius_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p2_ ,   
|  | vector< [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) > & | _result_ ,   
|  | [bool](../../d9/db9/classbool.html) | _clamp_ = `true`  
| ) | |   
  
References
[AdaptivePath::BoundBox::CollidesWith()](../../d6/dc3/classAdaptivePath_1_1BoundBox.html#a2bbbd18bf8af744a2b9fd7a8f67409ea),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ NormalizeV()

void AdaptivePath::NormalizeV  | ( | [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) & | _pt_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::DoublePoint::X](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a675837cc05f20447313789b82d84ad31),
and
[ClipperLib::DoublePoint::Y](../../d5/d7f/structClipperLib_1_1DoublePoint.html#a49774a93540882d88448badf37034454).

## ◆ operator<<()

std::ostream & AdaptivePath::operator<< | ( | std::ostream & | _s_ ,   
---|---|---|---  
|  | const [BoundBox](../../d6/dc3/classAdaptivePath_1_1BoundBox.html) & | _p_  
| ) | |   
  
## ◆ PathLength()

double AdaptivePath::PathLength  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_| ) |   
---|---|---|---|---|---  
  
References
[DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1).

## ◆ PointSideOfLine()

double AdaptivePath::PointSideOfLine  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ PopPathWithClosestPoint()

[bool](../../d9/db9/classbool.html) AdaptivePath::PopPathWithClosestPoint  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _p1_ ,   
|  | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _result_  
| ) | |   
  
References
[DraftVecUtils::dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
and
[DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1).

Referenced by
[AdaptivePath::EngagePoint::moveToClosestPoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#ab82d771a0d521b9b13fb15f6373df310).

## ◆ rotate()

[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) AdaptivePath::rotate  | ( | const [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) & | _in_ ,   
---|---|---|---  
|  | double  | _rad_  
| ) | |   
  
## ◆ ScaleDownPaths()

void AdaptivePath::ScaleDownPaths  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | long  | _scaleFactor_  
| ) | |   
  
Referenced by
[SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962).

## ◆ ScaleUpPaths()

void AdaptivePath::ScaleUpPaths  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | long  | _scaleFactor_  
| ) | |   
  
Referenced by
[SmoothPaths()](../../d5/d7f/namespaceAdaptivePath.html#a08e27d008713754b5d5efca8ef13b962).

## ◆ SetSegmentLength()

[bool](../../d9/db9/classbool.html) AdaptivePath::SetSegmentLength  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_ ,   
|  | double  | _new_length_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ SmoothPaths()

void AdaptivePath::SmoothPaths  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
---|---|---|---  
|  | double  | _stepSize_ ,   
|  | long  | _pointCount_ ,   
|  | long  | _iterations_  
| ) | |   
  
References
[CleanPath()](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4),
[DistanceSqrd()](../../d5/d7f/namespaceAdaptivePath.html#a8ba2907627cf52f54a10caa7ffbe4ac1),
[draftfunctions.scale::scale()](../../d2/d57/group__draftfunctions.html#ga98e60f6bc0ddfcb3ea15feee66713a10),
[ScaleDownPaths()](../../d5/d7f/namespaceAdaptivePath.html#a5e663fe75845628f35785043c4dd7077),
[ScaleUpPaths()](../../d5/d7f/namespaceAdaptivePath.html#ab9301ab629d4e88b24a71eb54755114a),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## Variable Documentation

## ◆ Perf_AppendToolPath

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_AppendToolPath("AppendToolPath")  | ( | "AppendToolPath"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_CalcCutAreaCirc

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_CalcCutAreaCirc("CalcCutArea")  | ( | "CalcCutArea"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_CalcCutAreaClip

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_CalcCutAreaClip("CalcCutAreaClip")  | ( | "CalcCutAreaClip"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_DistanceToBoundary

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_DistanceToBoundary("DistanceToBoundary")  | ( | "DistanceToBoundary"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_ExpandCleared

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_ExpandCleared("ExpandCleared")  | ( | "ExpandCleared"  | | ) |   
---|---|---|---|---|---  
  
Referenced by
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b).

## ◆ Perf_IsAllowedToCutTrough

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_IsAllowedToCutTrough("IsAllowedToCutTrough")  | ( | "IsAllowedToCutTrough"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_IsClearPath

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_IsClearPath("IsClearPath")  | ( | "IsClearPath"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_NextEngagePoint

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_NextEngagePoint("NextEngagePoint")  | ( | "NextEngagePoint"  | | ) |   
---|---|---|---|---|---  
  
Referenced by
[AdaptivePath::EngagePoint::nextEngagePoint()](../../de/d69/classAdaptivePath_1_1EngagePoint.html#a853203bca004d7d69e68fed5a17e049f).

## ◆ Perf_PointIterations

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_PointIterations("PointIterations")  | ( | "PointIterations"  | | ) |   
---|---|---|---|---|---  
  
## ◆ Perf_ProcessPolyNode

[PerfCounter](../../d2/d12/classAdaptivePath_1_1PerfCounter.html) AdaptivePath::Perf_ProcessPolyNode("ProcessPolyNode")  | ( | "ProcessPolyNode"  | | ) |   
---|---|---|---|---|---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

