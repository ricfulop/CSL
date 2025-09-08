---
url: https://freecad.github.io/SourceDoc/df/db2/namespaceClipperLib.html
scraped_at: 2025-09-08T15:19:04.711600
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Typedefs | Enumerations | Functions | Variables

ClipperLib Namespace Reference

##  Classes  
  
---  
class | [Clipper](../../d3/d1b/classClipperLib_1_1Clipper.html)  
class | [ClipperBase](../../d9/da0/classClipperLib_1_1ClipperBase.html)  
class | [clipperException](../../d1/dc3/classClipperLib_1_1clipperException.html)  
class | [ClipperOffset](../../d6/d79/classClipperLib_1_1ClipperOffset.html)  
struct | [DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html)  
class | [Int128](../../de/d97/classClipperLib_1_1Int128.html)  
struct | [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html)  
struct | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html)  
struct | [IntRect](../../d7/d16/structClipperLib_1_1IntRect.html)  
struct | [Join](../../d0/dc9/structClipperLib_1_1Join.html)  
struct | [LocalMinimum](../../d0/d4a/structClipperLib_1_1LocalMinimum.html)  
struct | [LocMinSorter](../../d5/d7a/structClipperLib_1_1LocMinSorter.html)  
struct | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html)  
struct | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html)  
class | [PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html)  
class | [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html)  
struct | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)  
  
##  Typedefs  
  
---  
typedef signed long long | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)  
typedef std::vector< [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * > | [EdgeList](../../df/db2/namespaceClipperLib.html#a86ece3ad074061d6b3d18819b1fa4ed7)  
typedef std::vector< [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) * > | [IntersectList](../../df/db2/namespaceClipperLib.html#aa619079161cda3de8197456767f54396)  
typedef std::vector< [Join](../../d0/dc9/structClipperLib_1_1Join.html) * > | [JoinList](../../df/db2/namespaceClipperLib.html#a7e09990d21008cefa4e28e9056c654c4)  
typedef signed long long | [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a)  
typedef std::vector< [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) > | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da)  
typedef std::vector< [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) > | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe)  
typedef std::vector< [PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html) * > | [PolyNodes](../../df/db2/namespaceClipperLib.html#ac9381bbff6b966df41b78667385b9c1e)  
typedef std::vector< [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) * > | [PolyOutList](../../df/db2/namespaceClipperLib.html#a955330d96f532e139adb1e52a82fcd43)  
typedef unsigned long long | [ulong64](../../df/db2/namespaceClipperLib.html#a031fec5e97eb7e08708f1cafa53a232d)  
  
##  Enumerations  
  
---  
enum | [ClipType](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46) { [ctIntersection](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46a7ab04c0263f5c01a93330dc199a1ca42) , [ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310) , [ctDifference](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46aef270504062ea1abce903af4f5be2eee) , [ctXor](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46a728726741bb2063fbb913073c5883dfe) }  
enum | [Direction](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7) { [dRightToLeft](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7a7b983c40ff2c1405f1bc0bfc079af6b0) , [dLeftToRight](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7afbbd8280f1b1879e6ed0dfadaf3b0739) }  
enum | [EdgeSide](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3f) { [esLeft](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae0e35c98eb9b5e1ea1fd643a474c2ab4) = 1 , [esRight](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3fae755211893cad1da40ec2f0d2dbd9c32) = 2 }  
enum | [EndType](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079) {   
[etClosedPolygon](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079abe139ce126eefdd24f9d947bd494404b)
,
[etClosedLine](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079aa4b6951fbc935423f51f3acee30a4c5e)
,
[etOpenButt](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079a4b95546b1ebb6771de89f131a566bc68)
,
[etOpenSquare](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079afea14e4c0b80da978d26774ca85b22f1)
,  
[etOpenRound](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079a6fa667a6be8eb9bc0f7ef92fa8505609)  
}  
enum | [InitOptions](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804) { [ioReverseSolution](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804a019c42b227a89408692e98e9312baa77) = 1 , [ioStrictlySimple](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804ad2ab367f64cd3abcf737e04acb32b9f2) = 2 , [ioPreserveCollinear](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804a5ee1ca93ff35691b7b27ce0f1bc4a898) = 4 }  
enum | [JoinType](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06e) { [jtSquare](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06ea1e73eb6e6192fffb13033a0f4d4ac87f) , [jtRound](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06ea7833a32073dc3f251ff8de93aa7b6388) , [jtMiter](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06ea27005a0d1be936fb9409535949a1c2ce) }  
enum | [NodeType](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3) { [ntAny](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3a09c9a9c0c8c053a8448acca58516d189) , [ntOpen](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3ada15652825339e4dd39f49e3ad377919) , [ntClosed](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3a8d3c6a25728d41b1de5343657e4ea070) }  
enum | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) { [pftEvenOdd](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7acede4475518a377720537448c7b2df73) , [pftNonZero](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7adbcce0eea52e627fc8ced2a93b7947ab) , [pftPositive](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7a681ce5d4d05aff1ae01842b970fe7fe8) , [pftNegative](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7a02692db143e5586a360eb686c5d1b7c2) }  
enum | [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) { [ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6) , [ptClip](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a33152b07d096815ff64f4aeab67f0335) }  
  
##  Functions  
  
---  
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [Abs](../../df/db2/namespaceClipperLib.html#ad29f252d45c594ccd3030cf966baa2e4) ([cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) val)  
void | [AddPolyNodeToPaths](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6) (const [PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html) &polynode, [NodeType](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3) nodetype, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
double | [Area](../../df/db2/namespaceClipperLib.html#ae138536c4535e0a97e2e5787ae41bac3) (const [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) &outRec)  
double | [Area](../../df/db2/namespaceClipperLib.html#a4a96cc48117e1dba6cf51bbc2d91fe97) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly)  
void | [CleanPolygon](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &in_poly, [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &out_poly, double distance)  
void | [CleanPolygon](../../df/db2/namespaceClipperLib.html#a819f3ac34feed7ca8c64c54bc534eb1b) ([Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly, double distance)  
void | [CleanPolygons](../../df/db2/namespaceClipperLib.html#a770cbc6ce4f16d02b8fe27c5abf6159c) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &in_polys, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &out_polys, double distance)  
void | [CleanPolygons](../../df/db2/namespaceClipperLib.html#aeee397f9f7e7cb5f0bb4723b7c4969e9) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &polys, double distance)  
void | [ClosedPathsFromPolyTree](../../df/db2/namespaceClipperLib.html#a83f3a341799f94dd6bd9649b319d85fa) (const [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) &polytree, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
void | [DisposeOutPts](../../df/db2/namespaceClipperLib.html#aefcf521aa7d6c94a55e4426872170bdf) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *&pp)  
double | [DistanceFromLineSqrd](../../df/db2/namespaceClipperLib.html#ac57923512d57903663fed9778585ca18) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &ln1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &ln2)  
double | [DistanceSqrd](../../df/db2/namespaceClipperLib.html#ab3ea29b9e123ab56ede03ce6946c9e7d) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2)  
[OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) * | [DupOutPt](../../df/db2/namespaceClipperLib.html#a1bc7e689896b9fdaf472cb4796aa2e83) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *outPt, [bool](../../d9/db9/classbool.html) InsertAfter)  
[bool](../../d9/db9/classbool.html) | [E2InsertsBeforeE1](../../df/db2/namespaceClipperLib.html#ae002e65db41b2e12c6a29b6c53d95e3d) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e1, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e2)  
[bool](../../d9/db9/classbool.html) | [EdgesAdjacent](../../df/db2/namespaceClipperLib.html#a178785f2e51a19d1e6bdb8848d14b924) (const [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) &inode)  
[OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) * | [ExcludeOp](../../df/db2/namespaceClipperLib.html#a0ca3049529769aa97b5af031a37bb0c4) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *op)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [FindNextLocMin](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *E)  
[bool](../../d9/db9/classbool.html) | [FirstIsBottomPt](../../df/db2/namespaceClipperLib.html#a9811846db2631994c7e6a54327bf251d) (const [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *btmPt1, const [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *btmPt2)  
[OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) * | [GetBottomPt](../../df/db2/namespaceClipperLib.html#ad7895448ee9b2d2499a57addd49b2192) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *pp)  
double | [GetDx](../../df/db2/namespaceClipperLib.html#adb890cca4fa2a71731b91968cf4ff49d) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2)  
void | [GetHorzDirection](../../df/db2/namespaceClipperLib.html#a3a6a98076d47afe4c2e033833ae89bf5) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &HorzEdge, [Direction](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7) &Dir, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) &Left, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) &Right)  
[OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) * | [GetLowermostRec](../../df/db2/namespaceClipperLib.html#a3b36c0993f124dd3235ed1dd468d4192) ([OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *outRec1, [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *outRec2)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [GetMaximaPair](../../df/db2/namespaceClipperLib.html#aeeaa3c8c25502a0bf3f4a82bf36366db) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [GetNextInAEL](../../df/db2/namespaceClipperLib.html#aa7cb7249896b67148d67619eaee44e6c) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e, [Direction](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7) dir)  
[bool](../../d9/db9/classbool.html) | [GetOverlap](../../df/db2/namespaceClipperLib.html#a489c460712308f4a5026b8618b6b319b) (const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) a1, const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) a2, const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) b1, const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) b2, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) &Left, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) &Right)  
[bool](../../d9/db9/classbool.html) | [GetOverlapSegment](../../df/db2/namespaceClipperLib.html#a8817de6dc5a080ead872b1373074c07f) ([IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1a, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1b, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2a, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2b, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2)  
[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) | [GetUnitNormal](../../df/db2/namespaceClipperLib.html#a5a62f42148b8b9991da9cfe8cb9cb065) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2)  
[bool](../../d9/db9/classbool.html) | [HorzSegmentsOverlap](../../df/db2/namespaceClipperLib.html#a8d010407c49e1ea2e092dd21d8684de4) ([cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) seg1a, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) seg1b, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) seg2a, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) seg2b)  
void | [InitEdge](../../df/db2/namespaceClipperLib.html#a1b822f020efce65b1e0c4fcdb264fd35) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *eNext, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *ePrev, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &Pt)  
void | [InitEdge2](../../df/db2/namespaceClipperLib.html#ae5ad4a2545fa1528f81bd2a89d9cddcb) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e, [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) Pt)  
[Int128](../../de/d97/classClipperLib_1_1Int128.html) | [Int128Mul](../../df/db2/namespaceClipperLib.html#a54fd38efeb2ae1bb84d1390bff3cf6bc) ([long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) lhs, [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) rhs)  
[bool](../../d9/db9/classbool.html) | [IntersectListSort](../../df/db2/namespaceClipperLib.html#aeb44a42315262aee3bfbecbc6a1eac77) ([IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) *node1, [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) *node2)  
void | [IntersectPoint](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &Edge1, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &Edge2, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &ip)  
[bool](../../d9/db9/classbool.html) | [IsHorizontal](../../df/db2/namespaceClipperLib.html#af9afcf65d7038ec26bf32b7d0c312c37) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e)  
[bool](../../d9/db9/classbool.html) | [IsIntermediate](../../df/db2/namespaceClipperLib.html#af6efe5b4046206e5c152374d384384c1) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e, const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) Y)  
[bool](../../d9/db9/classbool.html) | [IsMaxima](../../df/db2/namespaceClipperLib.html#a7a9e26585f642573f49208a47dc458c3) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e, const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) Y)  
[bool](../../d9/db9/classbool.html) | [IsMinima](../../df/db2/namespaceClipperLib.html#adebe3bd08021b5329adfc84089913b32) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e)  
[bool](../../d9/db9/classbool.html) | [JoinHorz](../../df/db2/namespaceClipperLib.html#acd026a4d43018ae65b8d253fbf44b680) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *op1, [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *op1b, [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *op2, [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *op2b, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) Pt, [bool](../../d9/db9/classbool.html) DiscardLeft)  
void | [Minkowski](../../df/db2/namespaceClipperLib.html#a63c9e744bc436b681c98c2f238e22455) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &solution, [bool](../../d9/db9/classbool.html) isSum, [bool](../../d9/db9/classbool.html) isClosed)  
void | [MinkowskiDiff](../../df/db2/namespaceClipperLib.html#a76dac24102863220c7bc13be222a1dda) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly1, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly2, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &solution)  
void | [MinkowskiSum](../../df/db2/namespaceClipperLib.html#ad12b5697c25579dce65d369a2e3cf608) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &pattern, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &solution, [bool](../../d9/db9/classbool.html) pathIsClosed)  
void | [MinkowskiSum](../../df/db2/namespaceClipperLib.html#ae4893aa579fd7c46ce695fd3d1c66e64) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &pattern, const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &solution, [bool](../../d9/db9/classbool.html) pathIsClosed)  
void | [OpenPathsFromPolyTree](../../df/db2/namespaceClipperLib.html#aa8b0b36c4c1e8108f39b10e4fba81cc5) ([PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) &polytree, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
[Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | [operator<<](../../df/db2/namespaceClipperLib.html#ad1afd510bfd5d57d68b5900ce83c7b58) ([Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p)  
[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | [operator<<](../../df/db2/namespaceClipperLib.html#a3c7e93bc95809af636fe76cfec3055b2) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &polys, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &p)  
std::ostream & | [operator<<](../../df/db2/namespaceClipperLib.html#a2e9613a92f21ac827d5b7f8b5ade5795) (std::ostream &s, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &p)  
std::ostream & | [operator<<](../../df/db2/namespaceClipperLib.html#abd88603a8c170404d069edae2e574fe9) (std::ostream &s, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &p)  
std::ostream & | [operator<<](../../df/db2/namespaceClipperLib.html#aa8b8872f6e4840cb63769a59a88eab4d) (std::ostream &s, const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &p)  
[bool](../../d9/db9/classbool.html) | [Orientation](../../df/db2/namespaceClipperLib.html#a806a3d33d76bb9d4479d384f876ce8bd) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &poly)  
[bool](../../d9/db9/classbool.html) | [Param1RightOfParam2](../../df/db2/namespaceClipperLib.html#a9fa2d4b54b71a1e746caf62d31ee0083) ([OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *outRec1, [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *outRec2)  
static [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) * | [ParseFirstLeft](../../df/db2/namespaceClipperLib.html#aefe525a9ade2358580a1b2789db553c9) ([OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *FirstLeft)  
[int](../../d1/da0/classint.html) | [PointCount](../../df/db2/namespaceClipperLib.html#a116d97a3199f4a29f2327b498af00469) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *Pts)  
[int](../../d1/da0/classint.html) | [PointInPolygon](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt, const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &path)  
[int](../../d1/da0/classint.html) | [PointInPolygon](../../df/db2/namespaceClipperLib.html#a35576f17125b022fdc726cbc4cb1ea50) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt, [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *op)  
[bool](../../d9/db9/classbool.html) | [PointIsVertex](../../df/db2/namespaceClipperLib.html#aa0616b922b887c38de1f2af2eee82357) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &Pt, [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *pp)  
[bool](../../d9/db9/classbool.html) | [PointsAreClose](../../df/db2/namespaceClipperLib.html#a52757887bc031d0052ae95dccb83cd2c) ([IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2, double distSqrd)  
[bool](../../d9/db9/classbool.html) | [Poly2ContainsPoly1](../../df/db2/namespaceClipperLib.html#a9a24c8b4723d9c93c2d3eabb139c4366) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *OutPt1, [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *OutPt2)  
void | [PolyTreeToPaths](../../df/db2/namespaceClipperLib.html#a3713b024b773e4e041f3de4595ff0f77) (const [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) &polytree, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &paths)  
[bool](../../d9/db9/classbool.html) | [Pt2IsBetweenPt1AndPt3](../../df/db2/namespaceClipperLib.html#a0a448254ee6419dfde0a539080502d88) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt3)  
void | [RangeTest](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &Pt, [bool](../../d9/db9/classbool.html) &useFullRange)  
[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * | [RemoveEdge](../../df/db2/namespaceClipperLib.html#a618e13d6a0fc1230b030ac02d70a2e0a) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *e)  
void | [ReverseHorizontal](../../df/db2/namespaceClipperLib.html#a308e107fa8e429684f57440687d77adc) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e)  
void | [ReversePath](../../df/db2/namespaceClipperLib.html#ab6376320953c60093dc73462c74589e1) ([Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &p)  
void | [ReversePaths](../../df/db2/namespaceClipperLib.html#ade103cad7caf2aa357b2d5410866ea62) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &p)  
void | [ReversePolyPtLinks](../../df/db2/namespaceClipperLib.html#a5148d4f90b324e0e4a13d1b13055661f) ([OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *pp)  
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [Round](../../df/db2/namespaceClipperLib.html#a6635b2c24fa0147ff4ecab56d80e7293) (double val)  
void | [SetDx](../../df/db2/namespaceClipperLib.html#ae6087af5cfe151e4b98723135e3575f7) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e)  
void | [SimplifyPolygon](../../df/db2/namespaceClipperLib.html#af374cea59a991e49f36c3530efc45feb) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &in_poly, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &out_polys, [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) fillType)  
void | [SimplifyPolygons](../../df/db2/namespaceClipperLib.html#ac9ebbe437e4c08816bffeced6d001cf6) (const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &in_polys, [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &out_polys, [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) fillType)  
void | [SimplifyPolygons](../../df/db2/namespaceClipperLib.html#ac43b677f95d30bd595bbdd5eb79cdcec) ([Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) &polys, [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) fillType)  
[bool](../../d9/db9/classbool.html) | [SlopesEqual](../../df/db2/namespaceClipperLib.html#a85fe5803e6f06dd9963cb4b222824ff3) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt3, [bool](../../d9/db9/classbool.html) UseFullInt64Range)  
[bool](../../d9/db9/classbool.html) | [SlopesEqual](../../df/db2/namespaceClipperLib.html#a5ce63c03021b0da24f00de41a2a72bcd) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt3, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) pt4, [bool](../../d9/db9/classbool.html) UseFullInt64Range)  
[bool](../../d9/db9/classbool.html) | [SlopesEqual](../../df/db2/namespaceClipperLib.html#a052da0ab7e1690b61e36e007769df9f8) (const [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e1, const [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &e2, [bool](../../d9/db9/classbool.html) UseFullInt64Range)  
[bool](../../d9/db9/classbool.html) | [SlopesNearCollinear](../../df/db2/namespaceClipperLib.html#a6a8d461810e4bcb5c67bf8e3026839b6) (const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2, const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt3, double distSqrd)  
void | [Swap](../../df/db2/namespaceClipperLib.html#adcb99516168fab9590baed2938996193) ([cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) &val1, [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) &val2)  
void | [SwapIntersectNodes](../../df/db2/namespaceClipperLib.html#ac299ceb4a2a28061aa452bd069e2c4a3) ([IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) &int1, [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) &int2)  
void | [SwapPoints](../../df/db2/namespaceClipperLib.html#af8338b22ca335b55a1fc1a17f0b0c453) ([IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt1, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) &pt2)  
void | [SwapPolyIndexes](../../df/db2/namespaceClipperLib.html#a17c02161ee129cdb347b0a6a18a73849) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &Edge1, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &Edge2)  
void | [SwapSides](../../df/db2/namespaceClipperLib.html#a63ceaffceda5d8e57ef98a0d7317b342) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &Edge1, [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &Edge2)  
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | [TopX](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be) ([TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) &edge, const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) currentY)  
void | [TranslatePath](../../df/db2/namespaceClipperLib.html#a3c34a4a0ea91a10f729e5ceb6cc33714) (const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &input, [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) &output, [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) delta)  
void | [UpdateOutPtIdxs](../../df/db2/namespaceClipperLib.html#a06a3e837b8fbaa3fc7e2640a8e4fe4a2) ([OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) &outrec)  
  
##  Variables  
  
---  
static double const | [def_arc_tolerance](../../df/db2/namespaceClipperLib.html#ab44dd4f071b7d92294a2af242e8c70d4) = 0.25  
static [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) const | [hiRange](../../df/db2/namespaceClipperLib.html#a65945fbc810bff7fd44c981b06e4473e) = 0x3FFFFFFFFFFFFFFFLL  
static [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) const | [loRange](../../df/db2/namespaceClipperLib.html#abc3cf08ce02b48ae18c320fd492108f1) = 0x3FFFFFFF  
static double const | [pi](../../df/db2/namespaceClipperLib.html#a3226215bdfa5b0d7f01e40fc8f131485) = 3.141592653589793238  
static [int](../../d1/da0/classint.html) const | [Skip](../../df/db2/namespaceClipperLib.html#a6e9f2a3266e14dced8a5fee78224c1bf) = -2  
static double const | [two_pi](../../df/db2/namespaceClipperLib.html#afdf9089a4f64d08fe88fa1b075fa6a71) = [pi](../../df/db2/namespaceClipperLib.html#a3226215bdfa5b0d7f01e40fc8f131485) *2  
static [int](../../d1/da0/classint.html) const | [Unassigned](../../df/db2/namespaceClipperLib.html#ae8c8149f9414a1459f7691ecd2f94669) = -1  
  
## Typedef Documentation

## ◆ cInt

typedef signed long long
[ClipperLib::cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)  
---  
  
## ◆ EdgeList

typedef std::vector< [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html)* >
[ClipperLib::EdgeList](../../df/db2/namespaceClipperLib.html#a86ece3ad074061d6b3d18819b1fa4ed7)  
---  
  
## ◆ IntersectList

typedef std::vector<
[IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html)* >
[ClipperLib::IntersectList](../../df/db2/namespaceClipperLib.html#aa619079161cda3de8197456767f54396)  
---  
  
## ◆ JoinList

typedef std::vector< [Join](../../d0/dc9/structClipperLib_1_1Join.html)* >
[ClipperLib::JoinList](../../df/db2/namespaceClipperLib.html#a7e09990d21008cefa4e28e9056c654c4)  
---  
  
## ◆ long64

typedef signed long long
[ClipperLib::long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a)  
---  
  
## ◆ Path

typedef std::vector<
[IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) >
[ClipperLib::Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da)  
---  
  
## ◆ Paths

typedef std::vector<
[Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da)
>
[ClipperLib::Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe)  
---  
  
## ◆ PolyNodes

typedef std::vector<
[PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html)* >
[ClipperLib::PolyNodes](../../df/db2/namespaceClipperLib.html#ac9381bbff6b966df41b78667385b9c1e)  
---  
  
## ◆ PolyOutList

typedef std::vector< [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html)* >
[ClipperLib::PolyOutList](../../df/db2/namespaceClipperLib.html#a955330d96f532e139adb1e52a82fcd43)  
---  
  
## ◆ ulong64

typedef unsigned long long
[ClipperLib::ulong64](../../df/db2/namespaceClipperLib.html#a031fec5e97eb7e08708f1cafa53a232d)  
---  
  
## Enumeration Type Documentation

## ◆ ClipType

enum
[ClipperLib::ClipType](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46)  
---  
  
Enumerator  
---  
ctIntersection |   
ctUnion |   
ctDifference |   
ctXor |   
  
## ◆ Direction

enum
[ClipperLib::Direction](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7)  
---  
  
Enumerator  
---  
dRightToLeft |   
dLeftToRight |   
  
## ◆ EdgeSide

enum
[ClipperLib::EdgeSide](../../df/db2/namespaceClipperLib.html#a0e8e5a1032917a06fbbf958f7a708f3f)  
---  
  
Enumerator  
---  
esLeft |   
esRight |   
  
## ◆ EndType

enum
[ClipperLib::EndType](../../df/db2/namespaceClipperLib.html#abee78a365e96a6edf45e15f885568079)  
---  
  
Enumerator  
---  
etClosedPolygon |   
etClosedLine |   
etOpenButt |   
etOpenSquare |   
etOpenRound |   
  
## ◆ InitOptions

enum
[ClipperLib::InitOptions](../../df/db2/namespaceClipperLib.html#a322ee4b6e4480f648dad8c65c58b2804)  
---  
  
Enumerator  
---  
ioReverseSolution |   
ioStrictlySimple |   
ioPreserveCollinear |   
  
## ◆ JoinType

enum
[ClipperLib::JoinType](../../df/db2/namespaceClipperLib.html#ab3880a3ca1b45df3ce93ac315a74c06e)  
---  
  
Enumerator  
---  
jtSquare |   
jtRound |   
jtMiter |   
  
## ◆ NodeType

enum
[ClipperLib::NodeType](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3)  
---  
  
Enumerator  
---  
ntAny |   
ntOpen |   
ntClosed |   
  
## ◆ PolyFillType

enum
[ClipperLib::PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7)  
---  
  
Enumerator  
---  
pftEvenOdd |   
pftNonZero |   
pftPositive |   
pftNegative |   
  
## ◆ PolyType

enum
[ClipperLib::PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960)  
---  
  
Enumerator  
---  
ptSubject |   
ptClip |   
  
## Function Documentation

## ◆ Abs()

[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) ClipperLib::Abs  | ( | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _val_| ) |   
---|---|---|---|---|---  
  
Referenced by
[GetOverlapSegment()](../../df/db2/namespaceClipperLib.html#a8817de6dc5a080ead872b1373074c07f),
and
[SlopesNearCollinear()](../../df/db2/namespaceClipperLib.html#a6a8d461810e4bcb5c67bf8e3026839b6).

## ◆ AddPolyNodeToPaths()

void ClipperLib::AddPolyNodeToPaths  | ( | const [PolyNode](../../da/d87/classClipperLib_1_1PolyNode.html) & | _polynode_ ,   
---|---|---|---  
|  | [NodeType](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3) | _nodetype_ ,   
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_  
| ) | |   
  
References
[AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6),
[ClipperLib::PolyNode::ChildCount()](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade),
[ClipperLib::PolyNode::Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d),
[ClipperLib::PolyNode::Contour](../../da/d87/classClipperLib_1_1PolyNode.html#a1d08b8a9499ff8cb89d5d63a12f881ea),
[ClipperLib::PolyNode::IsOpen()](../../da/d87/classClipperLib_1_1PolyNode.html#ac9ade640af2515976d337b65e8e84776),
[ntClosed](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3a8d3c6a25728d41b1de5343657e4ea070),
and
[ntOpen](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3ada15652825339e4dd39f49e3ad377919).

Referenced by
[AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6),
[ClosedPathsFromPolyTree()](../../df/db2/namespaceClipperLib.html#a83f3a341799f94dd6bd9649b319d85fa),
and
[PolyTreeToPaths()](../../df/db2/namespaceClipperLib.html#a3713b024b773e4e041f3de4595ff0f77).

## ◆ Area() [1/2]

double ClipperLib::Area  | ( | const [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) & | _outRec_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98),
[ClipperLib::OutRec::Pts](../../d1/d21/structClipperLib_1_1OutRec.html#a82e9cba88d46d0d60db0b0365c6bd02e),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ Area() [2/2]

double ClipperLib::Area  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ClipperLib::Clipper::ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3),
and
[Orientation()](../../df/db2/namespaceClipperLib.html#a806a3d33d76bb9d4479d384f876ce8bd).

## ◆ CleanPolygon() [1/2]

void ClipperLib::CleanPolygon  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _in_poly_ ,   
---|---|---|---  
|  | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _out_poly_ ,   
|  | double  | _distance_  
| ) | |   
  
References
[ExcludeOp()](../../df/db2/namespaceClipperLib.html#a0ca3049529769aa97b5af031a37bb0c4),
[ClipperLib::OutPt::Idx](../../d1/de7/structClipperLib_1_1OutPt.html#ad04d3691d47a5d0d9b2ae097e7e7bf10),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[PointsAreClose()](../../df/db2/namespaceClipperLib.html#a52757887bc031d0052ae95dccb83cd2c),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98),
and
[SlopesNearCollinear()](../../df/db2/namespaceClipperLib.html#a6a8d461810e4bcb5c67bf8e3026839b6).

Referenced by
[AdaptivePath::CleanPath()](../../d5/d7f/namespaceAdaptivePath.html#aead96b0a2dabc04e6fc87c735b7158c4),
[CleanPolygon()](../../df/db2/namespaceClipperLib.html#a819f3ac34feed7ca8c64c54bc534eb1b),
and
[CleanPolygons()](../../df/db2/namespaceClipperLib.html#a770cbc6ce4f16d02b8fe27c5abf6159c).

## ◆ CleanPolygon() [2/2]

void ClipperLib::CleanPolygon  | ( | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly_ ,   
---|---|---|---  
|  | double  | _distance_  
| ) | |   
  
References
[CleanPolygon()](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b).

## ◆ CleanPolygons() [1/2]

void ClipperLib::CleanPolygons  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _in_polys_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _out_polys_ ,   
|  | double  | _distance_  
| ) | |   
  
References
[CleanPolygon()](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b).

Referenced by
[CleanPolygons()](../../df/db2/namespaceClipperLib.html#aeee397f9f7e7cb5f0bb4723b7c4969e9),
and
[AdaptivePath::ClearedArea::ExpandCleared()](../../d8/d56/classAdaptivePath_1_1ClearedArea.html#a880cf981ced9aa6c2021bee6d35fc58b).

## ◆ CleanPolygons() [2/2]

void ClipperLib::CleanPolygons  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _polys_ ,   
---|---|---|---  
|  | double  | _distance_  
| ) | |   
  
References
[CleanPolygons()](../../df/db2/namespaceClipperLib.html#a770cbc6ce4f16d02b8fe27c5abf6159c).

## ◆ ClosedPathsFromPolyTree()

void ClipperLib::ClosedPathsFromPolyTree  | ( | const [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) & | _polytree_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_  
| ) | |   
  
References
[AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6),
[ntClosed](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3a8d3c6a25728d41b1de5343657e4ea070),
and
[ClipperLib::PolyTree::Total()](../../d3/d99/classClipperLib_1_1PolyTree.html#ad0d3c974bab5a30cc8c916da9fe14388).

Referenced by
[CArea::Clip()](../../d3/d52/classCArea.html#aa4cab52e8f430196b3bfec652fb633e5).

## ◆ DisposeOutPts()

void ClipperLib::DisposeOutPts  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *& | _pp_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
and
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54).

## ◆ DistanceFromLineSqrd()

double ClipperLib::DistanceFromLineSqrd  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _ln1_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _ln2_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[SlopesNearCollinear()](../../df/db2/namespaceClipperLib.html#a6a8d461810e4bcb5c67bf8e3026839b6).

## ◆ DistanceSqrd()

double ClipperLib::DistanceSqrd  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ DupOutPt()

[OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) * ClipperLib::DupOutPt  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _outPt_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _InsertAfter_  
| ) | |   
  
References
[ClipperLib::OutPt::Idx](../../d1/de7/structClipperLib_1_1OutPt.html#ad04d3691d47a5d0d9b2ae097e7e7bf10),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
and
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98).

Referenced by
[JoinHorz()](../../df/db2/namespaceClipperLib.html#acd026a4d43018ae65b8d253fbf44b680).

## ◆ E2InsertsBeforeE1()

[bool](../../d9/db9/classbool.html) ClipperLib::E2InsertsBeforeE1  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e1_ ,   
---|---|---|---  
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e2_  
| ) | |   
  
References
[ClipperLib::TEdge::Curr](../../d2/d7f/structClipperLib_1_1TEdge.html#ad5932926d3d5d6ed6ae4bc991ed7bcec),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
[TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ EdgesAdjacent()

[bool](../../d9/db9/classbool.html) ClipperLib::EdgesAdjacent  | ( | const [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) & | _inode_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::IntersectNode::Edge1](../../dd/db0/structClipperLib_1_1IntersectNode.html#a43fd790cc38441edb594841d79b25f13),
[ClipperLib::IntersectNode::Edge2](../../dd/db0/structClipperLib_1_1IntersectNode.html#afcb56e7564fedf1c90962a9f75454539),
[ClipperLib::TEdge::NextInSEL](../../d2/d7f/structClipperLib_1_1TEdge.html#a167cd4d991d27f344d875ad6fd43b862),
and
[ClipperLib::TEdge::PrevInSEL](../../d2/d7f/structClipperLib_1_1TEdge.html#aa38f572c772d0bae50323f7890334c5f).

## ◆ ExcludeOp()

[OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) * ClipperLib::ExcludeOp  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _op_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::OutPt::Idx](../../d1/de7/structClipperLib_1_1OutPt.html#ad04d3691d47a5d0d9b2ae097e7e7bf10),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
and
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54).

Referenced by
[CleanPolygon()](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b).

## ◆ FindNextLocMin()

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::FindNextLocMin  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _E_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::TEdge::Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc),
[ClipperLib::TEdge::Curr](../../d2/d7f/structClipperLib_1_1TEdge.html#ad5932926d3d5d6ed6ae4bc991ed7bcec),
[IsHorizontal()](../../df/db2/namespaceClipperLib.html#af9afcf65d7038ec26bf32b7d0c312c37),
[ClipperLib::TEdge::Next](../../d2/d7f/structClipperLib_1_1TEdge.html#af63cea19f1590922691d1a3a90e4173d),
[ClipperLib::TEdge::Prev](../../d2/d7f/structClipperLib_1_1TEdge.html#a2713de57bcc285aaee2b9e1f5023bebc),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

## ◆ FirstIsBottomPt()

[bool](../../d9/db9/classbool.html) ClipperLib::FirstIsBottomPt  | ( | const [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _btmPt1_ ,   
---|---|---|---  
|  | const [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _btmPt2_  
| ) | |   
  
References
[GetDx()](../../df/db2/namespaceClipperLib.html#adb890cca4fa2a71731b91968cf4ff49d),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
and
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98).

Referenced by
[GetBottomPt()](../../df/db2/namespaceClipperLib.html#ad7895448ee9b2d2499a57addd49b2192),
and
[GetLowermostRec()](../../df/db2/namespaceClipperLib.html#a3b36c0993f124dd3235ed1dd468d4192).

## ◆ GetBottomPt()

[OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) * ClipperLib::GetBottomPt  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _pp_| ) |   
---|---|---|---|---|---  
  
References
[FirstIsBottomPt()](../../df/db2/namespaceClipperLib.html#a9811846db2631994c7e6a54327bf251d),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[GetLowermostRec()](../../df/db2/namespaceClipperLib.html#a3b36c0993f124dd3235ed1dd468d4192).

## ◆ GetDx()

double ClipperLib::GetDx  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[FirstIsBottomPt()](../../df/db2/namespaceClipperLib.html#a9811846db2631994c7e6a54327bf251d).

## ◆ GetHorzDirection()

void ClipperLib::GetHorzDirection  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _HorzEdge_ ,   
---|---|---|---  
|  | [Direction](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7) & | _Dir_ ,   
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) & | _Left_ ,   
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) & | _Right_  
| ) | |   
  
References
[ClipperLib::TEdge::Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc),
[dLeftToRight](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7afbbd8280f1b1879e6ed0dfadaf3b0739),
[dRightToLeft](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7a7b983c40ff2c1405f1bc0bfc079af6b0),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
and
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6).

## ◆ GetLowermostRec()

[OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) * ClipperLib::GetLowermostRec  | ( | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *  | _outRec1_ ,   
---|---|---|---  
|  | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *  | _outRec2_  
| ) | |   
  
References
[ClipperLib::OutRec::BottomPt](../../d1/d21/structClipperLib_1_1OutRec.html#adc4d612df109de83dca298204176ff0c),
[FirstIsBottomPt()](../../df/db2/namespaceClipperLib.html#a9811846db2631994c7e6a54327bf251d),
[GetBottomPt()](../../df/db2/namespaceClipperLib.html#ad7895448ee9b2d2499a57addd49b2192),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98),
[ClipperLib::OutRec::Pts](../../d1/d21/structClipperLib_1_1OutRec.html#a82e9cba88d46d0d60db0b0365c6bd02e),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ GetMaximaPair()

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::GetMaximaPair  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_| ) |   
---|---|---|---|---|---  
  
References
[IsHorizontal()](../../df/db2/namespaceClipperLib.html#af9afcf65d7038ec26bf32b7d0c312c37),
and
[Skip](../../df/db2/namespaceClipperLib.html#a6e9f2a3266e14dced8a5fee78224c1bf).

## ◆ GetNextInAEL()

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::GetNextInAEL  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_ ,   
---|---|---|---  
|  | [Direction](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7) | _dir_  
| ) | |   
  
References
[dLeftToRight](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7afbbd8280f1b1879e6ed0dfadaf3b0739).

## ◆ GetOverlap()

[bool](../../d9/db9/classbool.html) ClipperLib::GetOverlap  | ( | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _a1_ ,   
---|---|---|---  
|  | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _a2_ ,   
|  | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _b1_ ,   
|  | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _b2_ ,   
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) & | _Left_ ,   
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) & | _Right_  
| ) | |   
  
## ◆ GetOverlapSegment()

[bool](../../d9/db9/classbool.html) ClipperLib::GetOverlapSegment  | ( | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1a_ ,   
---|---|---|---  
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1b_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2a_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2b_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_  
| ) | |   
  
References
[Abs()](../../df/db2/namespaceClipperLib.html#ad29f252d45c594ccd3030cf966baa2e4),
[SwapPoints()](../../df/db2/namespaceClipperLib.html#af8338b22ca335b55a1fc1a17f0b0c453),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ GetUnitNormal()

[DoublePoint](../../d5/d7f/structClipperLib_1_1DoublePoint.html) ClipperLib::GetUnitNormal  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ HorzSegmentsOverlap()

[bool](../../d9/db9/classbool.html) ClipperLib::HorzSegmentsOverlap  | ( | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _seg1a_ ,   
---|---|---|---  
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _seg1b_ ,   
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _seg2a_ ,   
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _seg2b_  
| ) | |   
  
References
[Swap()](../../df/db2/namespaceClipperLib.html#adcb99516168fab9590baed2938996193).

## ◆ InitEdge()

void ClipperLib::InitEdge  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_ ,   
---|---|---|---  
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _eNext_ ,   
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _ePrev_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _Pt_  
| ) | |   
  
References
[Unassigned](../../df/db2/namespaceClipperLib.html#ae8c8149f9414a1459f7691ecd2f94669).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

## ◆ InitEdge2()

void ClipperLib::InitEdge2  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e_ ,   
---|---|---|---  
|  | [PolyType](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960) | _Pt_  
| ) | |   
  
References
[SetDx()](../../df/db2/namespaceClipperLib.html#ae6087af5cfe151e4b98723135e3575f7).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

## ◆ Int128Mul()

[Int128](../../de/d97/classClipperLib_1_1Int128.html) ClipperLib::Int128Mul  | ( | [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) | _lhs_ ,   
---|---|---|---  
|  | [long64](../../df/db2/namespaceClipperLib.html#a7fd564bf34d174b6c96e07d01e5e7a0a) | _rhs_  
| ) | |   
  
References
[ClipperLib::Int128::hi](../../de/d97/classClipperLib_1_1Int128.html#a167643d0860a14fb563e055511e15e14),
and
[ClipperLib::Int128::lo](../../de/d97/classClipperLib_1_1Int128.html#a991b9da6e53c777a94fca640e505b258).

Referenced by
[SlopesEqual()](../../df/db2/namespaceClipperLib.html#a052da0ab7e1690b61e36e007769df9f8).

## ◆ IntersectListSort()

[bool](../../d9/db9/classbool.html) ClipperLib::IntersectListSort  | ( | [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) *  | _node1_ ,   
---|---|---|---  
|  | [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) *  | _node2_  
| ) | |   
  
References
[ClipperLib::IntersectNode::Pt](../../dd/db0/structClipperLib_1_1IntersectNode.html#a91fc92370fb47797dae0602443e6475e),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ IntersectPoint()

void ClipperLib::IntersectPoint  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _Edge1_ ,   
---|---|---|---  
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _Edge2_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _ip_  
| ) | |   
  
References
[ClipperLib::TEdge::Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc),
[ClipperLib::TEdge::Curr](../../d2/d7f/structClipperLib_1_1TEdge.html#ad5932926d3d5d6ed6ae4bc991ed7bcec),
[ClipperLib::TEdge::Delta](../../d2/d7f/structClipperLib_1_1TEdge.html#afeb7324b818fe9f667199bd18701e23c),
[ClipperLib::TEdge::Dx](../../d2/d7f/structClipperLib_1_1TEdge.html#ace215b877c384f917d18f6c1da913959),
[IsHorizontal()](../../df/db2/namespaceClipperLib.html#af9afcf65d7038ec26bf32b7d0c312c37),
[Round()](../../df/db2/namespaceClipperLib.html#a6635b2c24fa0147ff4ecab56d80e7293),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
[TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ IsHorizontal()

[bool](../../d9/db9/classbool.html) ClipperLib::IsHorizontal  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e_| ) |   
---|---|---|---|---|---  
  
Referenced by
[FindNextLocMin()](../../df/db2/namespaceClipperLib.html#a6c2a946a9f927bfd364c95b561d4191c),
[GetMaximaPair()](../../df/db2/namespaceClipperLib.html#aeeaa3c8c25502a0bf3f4a82bf36366db),
[IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
and
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ IsIntermediate()

[bool](../../d9/db9/classbool.html) ClipperLib::IsIntermediate  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_ ,   
---|---|---|---  
|  | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _Y_  
| ) | |   
  
## ◆ IsMaxima()

[bool](../../d9/db9/classbool.html) ClipperLib::IsMaxima  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_ ,   
---|---|---|---  
|  | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _Y_  
| ) | |   
  
## ◆ IsMinima()

[bool](../../d9/db9/classbool.html) ClipperLib::IsMinima  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_| ) |   
---|---|---|---|---|---  
  
## ◆ JoinHorz()

[bool](../../d9/db9/classbool.html) ClipperLib::JoinHorz  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _op1_ ,   
---|---|---|---  
|  | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _op1b_ ,   
|  | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _op2_ ,   
|  | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _op2b_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _Pt_ ,   
|  | [bool](../../d9/db9/classbool.html) | _DiscardLeft_  
| ) | |   
  
References
[dLeftToRight](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7afbbd8280f1b1879e6ed0dfadaf3b0739),
[dRightToLeft](../../df/db2/namespaceClipperLib.html#a50027cc5a43f727ff89bcadf7e4524a7a7b983c40ff2c1405f1bc0bfc079af6b0),
[DupOutPt()](../../df/db2/namespaceClipperLib.html#a1bc7e689896b9fdaf472cb4796aa2e83),
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ Minkowski()

void ClipperLib::Minkowski  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_ ,   
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _solution_ ,   
|  | [bool](../../d9/db9/classbool.html) | _isSum_ ,   
|  | [bool](../../d9/db9/classbool.html) | _isClosed_  
| ) | |   
  
References
[Orientation()](../../df/db2/namespaceClipperLib.html#a806a3d33d76bb9d4479d384f876ce8bd),
and
[ReversePath()](../../df/db2/namespaceClipperLib.html#ab6376320953c60093dc73462c74589e1).

Referenced by
[MinkowskiDiff()](../../df/db2/namespaceClipperLib.html#a76dac24102863220c7bc13be222a1dda),
and
[MinkowskiSum()](../../df/db2/namespaceClipperLib.html#ad12b5697c25579dce65d369a2e3cf608).

## ◆ MinkowskiDiff()

void ClipperLib::MinkowskiDiff  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly1_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly2_ ,   
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _solution_  
| ) | |   
  
References
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[Minkowski()](../../df/db2/namespaceClipperLib.html#a63c9e744bc436b681c98c2f238e22455),
[pftNonZero](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7adbcce0eea52e627fc8ced2a93b7947ab),
and
[ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6).

## ◆ MinkowskiSum() [1/2]

void ClipperLib::MinkowskiSum  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _pattern_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_ ,   
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _solution_ ,   
|  | [bool](../../d9/db9/classbool.html) | _pathIsClosed_  
| ) | |   
  
References
[ClipperLib::ClipperBase::AddPaths()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a2395967b47fb9f3f5846e2bf56c18f67),
[ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[Minkowski()](../../df/db2/namespaceClipperLib.html#a63c9e744bc436b681c98c2f238e22455),
[pftNonZero](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7adbcce0eea52e627fc8ced2a93b7947ab),
and
[ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6).

## ◆ MinkowskiSum() [2/2]

void ClipperLib::MinkowskiSum  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _pattern_ ,   
---|---|---|---  
|  | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_ ,   
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _solution_ ,   
|  | [bool](../../d9/db9/classbool.html) | _pathIsClosed_  
| ) | |   
  
References
[ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[Minkowski()](../../df/db2/namespaceClipperLib.html#a63c9e744bc436b681c98c2f238e22455),
[pftNonZero](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7adbcce0eea52e627fc8ced2a93b7947ab),
[ptClip](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a33152b07d096815ff64f4aeab67f0335),
[ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6),
and
[TranslatePath()](../../df/db2/namespaceClipperLib.html#a3c34a4a0ea91a10f729e5ceb6cc33714).

## ◆ OpenPathsFromPolyTree()

void ClipperLib::OpenPathsFromPolyTree  | ( | [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) & | _polytree_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_  
| ) | |   
  
References
[ClipperLib::PolyNode::ChildCount()](../../da/d87/classClipperLib_1_1PolyNode.html#a19128db6fb2aca66555231edaffa7ade),
[ClipperLib::PolyNode::Childs](../../da/d87/classClipperLib_1_1PolyNode.html#a7ac59aea508951a4c979bfca8913261d),
and
[ClipperLib::PolyTree::Total()](../../d3/d99/classClipperLib_1_1PolyTree.html#ad0d3c974bab5a30cc8c916da9fe14388).

Referenced by
[CArea::Clip()](../../d3/d52/classCArea.html#aa4cab52e8f430196b3bfec652fb633e5).

## ◆ operator<<() [1/5]

[Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & ClipperLib::operator<< | ( | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p_  
| ) | |   
  
## ◆ operator<<() [2/5]

[Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & ClipperLib::operator<< | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _polys_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _p_  
| ) | |   
  
## ◆ operator<<() [3/5]

std::ostream & ClipperLib::operator<< | ( | std::ostream & | _s_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _p_  
| ) | |   
  
## ◆ operator<<() [4/5]

std::ostream & ClipperLib::operator<< | ( | std::ostream & | _s_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _p_  
| ) | |   
  
## ◆ operator<<() [5/5]

std::ostream & ClipperLib::operator<< | ( | std::ostream & | _s_ ,   
---|---|---|---  
|  | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _p_  
| ) | |   
  
## ◆ Orientation()

[bool](../../d9/db9/classbool.html) ClipperLib::Orientation  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _poly_| ) |   
---|---|---|---|---|---  
  
References
[Area()](../../df/db2/namespaceClipperLib.html#a4a96cc48117e1dba6cf51bbc2d91fe97).

Referenced by
[Minkowski()](../../df/db2/namespaceClipperLib.html#a63c9e744bc436b681c98c2f238e22455).

## ◆ Param1RightOfParam2()

[bool](../../d9/db9/classbool.html) ClipperLib::Param1RightOfParam2  | ( | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *  | _outRec1_ ,   
---|---|---|---  
|  | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *  | _outRec2_  
| ) | |   
  
References
[ClipperLib::OutRec::FirstLeft](../../d1/d21/structClipperLib_1_1OutRec.html#aa8baa934f1a7687a16b88a579dec3dd4).

## ◆ ParseFirstLeft()

| static [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) * ClipperLib::ParseFirstLeft  | ( | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) *  | _FirstLeft_| ) |   
---|---|---|---|---|---  
static  
  
References
[ClipperLib::OutRec::FirstLeft](../../d1/d21/structClipperLib_1_1OutRec.html#aa8baa934f1a7687a16b88a579dec3dd4),
and
[ClipperLib::OutRec::Pts](../../d1/d21/structClipperLib_1_1OutRec.html#a82e9cba88d46d0d60db0b0365c6bd02e).

## ◆ PointCount()

[int](../../d1/da0/classint.html) ClipperLib::PointCount  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _Pts_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e).

## ◆ PointInPolygon() [1/2]

[int](../../d1/da0/classint.html) ClipperLib::PointInPolygon  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_ ,   
---|---|---|---  
|  | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _path_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AdaptivePath::appendDirectChildPaths()](../../d5/d7f/namespaceAdaptivePath.html#ae4de2e0c14dadfa4dd7c25b581fdb8ea),
[AdaptivePath::getPathNestingLevel()](../../d5/d7f/namespaceAdaptivePath.html#afe6b9d42c4e97db975f5acf577006f18),
[AdaptivePath::IsPointWithinCutRegion()](../../d5/d7f/namespaceAdaptivePath.html#aca8e289d9ec01dd727d3a7f033e12a66),
and
[Poly2ContainsPoly1()](../../df/db2/namespaceClipperLib.html#a9a24c8b4723d9c93c2d3eabb139c4366).

## ◆ PointInPolygon() [2/2]

[int](../../d1/da0/classint.html) ClipperLib::PointInPolygon  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt_ ,   
---|---|---|---  
|  | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _op_  
| ) | |   
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ PointIsVertex()

[bool](../../d9/db9/classbool.html) ClipperLib::PointIsVertex  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _Pt_ ,   
---|---|---|---  
|  | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _pp_  
| ) | |   
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
and
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98).

## ◆ PointsAreClose()

[bool](../../d9/db9/classbool.html) ClipperLib::PointsAreClose  | ( | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1_ ,   
---|---|---|---  
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2_ ,   
|  | double  | _distSqrd_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[CleanPolygon()](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b).

## ◆ Poly2ContainsPoly1()

[bool](../../d9/db9/classbool.html) ClipperLib::Poly2ContainsPoly1  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _OutPt1_ ,   
---|---|---|---  
|  | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _OutPt2_  
| ) | |   
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
[PointInPolygon()](../../df/db2/namespaceClipperLib.html#ac7314f2a1f45c627bac20e9ba2a68212),
and
[ClipperLib::OutPt::Pt](../../d1/de7/structClipperLib_1_1OutPt.html#aa01c2b1e9c5b2d8faa40701178ffcf98).

## ◆ PolyTreeToPaths()

void ClipperLib::PolyTreeToPaths  | ( | const [PolyTree](../../d3/d99/classClipperLib_1_1PolyTree.html) & | _polytree_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _paths_  
| ) | |   
  
References
[AddPolyNodeToPaths()](../../df/db2/namespaceClipperLib.html#a4644758856e780ca359c3e37065397a6),
[ntAny](../../df/db2/namespaceClipperLib.html#a31e9eef1fdd14cee54118420090b61d3a09c9a9c0c8c053a8448acca58516d189),
and
[ClipperLib::PolyTree::Total()](../../d3/d99/classClipperLib_1_1PolyTree.html#ad0d3c974bab5a30cc8c916da9fe14388).

## ◆ Pt2IsBetweenPt1AndPt3()

[bool](../../d9/db9/classbool.html) ClipperLib::Pt2IsBetweenPt1AndPt3  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt3_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

## ◆ RangeTest()

void ClipperLib::RangeTest  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _Pt_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) & | _useFullRange_  
| ) | |   
  
References
[hiRange](../../df/db2/namespaceClipperLib.html#a65945fbc810bff7fd44c981b06e4473e),
[loRange](../../df/db2/namespaceClipperLib.html#abc3cf08ce02b48ae18c320fd492108f1),
[RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
and
[RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908).

## ◆ RemoveEdge()

[TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) * ClipperLib::RemoveEdge  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) *  | _e_| ) |   
---|---|---|---|---|---  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

## ◆ ReverseHorizontal()

void ClipperLib::ReverseHorizontal  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e_| ) |   
---|---|---|---|---|---  
  
References
[Swap()](../../df/db2/namespaceClipperLib.html#adcb99516168fab9590baed2938996193).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
and
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ ReversePath()

void ClipperLib::ReversePath  | ( | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _p_| ) |   
---|---|---|---|---|---  
  
Referenced by
[AdaptivePath::ConnectPaths()](../../d5/d7f/namespaceAdaptivePath.html#a26e83a95426b4f1c05b3eb98b4a04a17),
[Minkowski()](../../df/db2/namespaceClipperLib.html#a63c9e744bc436b681c98c2f238e22455),
and
[ReversePaths()](../../df/db2/namespaceClipperLib.html#ade103cad7caf2aa357b2d5410866ea62).

## ◆ ReversePaths()

void ClipperLib::ReversePaths  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _p_| ) |   
---|---|---|---|---|---  
  
References
[ReversePath()](../../df/db2/namespaceClipperLib.html#ab6376320953c60093dc73462c74589e1).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071).

## ◆ ReversePolyPtLinks()

void ClipperLib::ReversePolyPtLinks  | ( | [OutPt](../../d1/de7/structClipperLib_1_1OutPt.html) *  | _pp_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::OutPt::Next](../../d1/de7/structClipperLib_1_1OutPt.html#a2d605b87f6da37dbdbef990c4fa5819e),
and
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54).

Referenced by
[ClipperLib::Clipper::ExecuteInternal()](../../d3/d1b/classClipperLib_1_1Clipper.html#a3e8757e5f8a6ffcb7fd0f9630fde02d3).

## ◆ Round()

[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) ClipperLib::Round  | ( | double  | _val_| ) |   
---|---|---|---|---|---  
  
Referenced by
[IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a),
and
[TopX()](../../df/db2/namespaceClipperLib.html#a63e0b77cf7232cbd4f9909b25bd300be).

## ◆ SetDx()

void ClipperLib::SetDx  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e_| ) |   
---|---|---|---|---|---  
  
Referenced by
[InitEdge2()](../../df/db2/namespaceClipperLib.html#ae5ad4a2545fa1528f81bd2a89d9cddcb).

## ◆ SimplifyPolygon()

void ClipperLib::SimplifyPolygon  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _in_poly_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _out_polys_ ,   
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _fillType_  
| ) | |   
  
References
[ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6),
and
[ClipperLib::Clipper::StrictlySimple()](../../d3/d1b/classClipperLib_1_1Clipper.html#a50eb4c514466ed37fd365769e0bcf67b).

## ◆ SimplifyPolygons() [1/2]

void ClipperLib::SimplifyPolygons  | ( | const [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _in_polys_ ,   
---|---|---|---  
|  | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _out_polys_ ,   
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _fillType_  
| ) | |   
  
References
[ctUnion](../../df/db2/namespaceClipperLib.html#a3db4fddd50b81ba657107505821d7f46abb57d8284f7bf1cd7b902eae5b93c310),
[ptSubject](../../df/db2/namespaceClipperLib.html#a50d662440e5e100070014ed91281e960a67607ff4c7ca5fca8302236ff9a575b6),
and
[ClipperLib::Clipper::StrictlySimple()](../../d3/d1b/classClipperLib_1_1Clipper.html#a50eb4c514466ed37fd365769e0bcf67b).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
and
[SimplifyPolygons()](../../df/db2/namespaceClipperLib.html#ac43b677f95d30bd595bbdd5eb79cdcec).

## ◆ SimplifyPolygons() [2/2]

void ClipperLib::SimplifyPolygons  | ( | [Paths](../../df/db2/namespaceClipperLib.html#a4bab1d9e10805fa6f1fd3b78c56efcfe) & | _polys_ ,   
---|---|---|---  
|  | [PolyFillType](../../df/db2/namespaceClipperLib.html#a95a41ff8fa6b351d304829c267d638d7) | _fillType_  
| ) | |   
  
References
[SimplifyPolygons()](../../df/db2/namespaceClipperLib.html#ac9ebbe437e4c08816bffeced6d001cf6).

## ◆ SlopesEqual() [1/3]

[bool](../../d9/db9/classbool.html) ClipperLib::SlopesEqual  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt3_ ,   
|  | [bool](../../d9/db9/classbool.html) | _UseFullInt64Range_  
| ) | |   
  
References
[Int128Mul()](../../df/db2/namespaceClipperLib.html#a54fd38efeb2ae1bb84d1390bff3cf6bc),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ SlopesEqual() [2/3]

[bool](../../d9/db9/classbool.html) ClipperLib::SlopesEqual  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt3_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _pt4_ ,   
|  | [bool](../../d9/db9/classbool.html) | _UseFullInt64Range_  
| ) | |   
  
References
[Int128Mul()](../../df/db2/namespaceClipperLib.html#a54fd38efeb2ae1bb84d1390bff3cf6bc),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

## ◆ SlopesEqual() [3/3]

[bool](../../d9/db9/classbool.html) ClipperLib::SlopesEqual  | ( | const [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e1_ ,   
---|---|---|---  
|  | const [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _e2_ ,   
|  | [bool](../../d9/db9/classbool.html) | _UseFullInt64Range_  
| ) | |   
  
References
[ClipperLib::TEdge::Delta](../../d2/d7f/structClipperLib_1_1TEdge.html#afeb7324b818fe9f667199bd18701e23c),
[Int128Mul()](../../df/db2/namespaceClipperLib.html#a54fd38efeb2ae1bb84d1390bff3cf6bc),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba).

## ◆ SlopesNearCollinear()

[bool](../../d9/db9/classbool.html) ClipperLib::SlopesNearCollinear  | ( | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_ ,   
|  | const [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt3_ ,   
|  | double  | _distSqrd_  
| ) | |   
  
References
[Abs()](../../df/db2/namespaceClipperLib.html#ad29f252d45c594ccd3030cf966baa2e4),
[DistanceFromLineSqrd()](../../df/db2/namespaceClipperLib.html#ac57923512d57903663fed9778585ca18),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[CleanPolygon()](../../df/db2/namespaceClipperLib.html#a9246a3146ac112581e82be58e158be7b).

## ◆ Swap()

void ClipperLib::Swap  | ( | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) & | _val1_ ,   
---|---|---|---  
|  | [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) & | _val2_  
| ) | |   
  
Referenced by
[HorzSegmentsOverlap()](../../df/db2/namespaceClipperLib.html#a8d010407c49e1ea2e092dd21d8684de4),
and
[ReverseHorizontal()](../../df/db2/namespaceClipperLib.html#a308e107fa8e429684f57440687d77adc).

## ◆ SwapIntersectNodes()

void ClipperLib::SwapIntersectNodes  | ( | [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) & | _int1_ ,   
---|---|---|---  
|  | [IntersectNode](../../dd/db0/structClipperLib_1_1IntersectNode.html) & | _int2_  
| ) | |   
  
References
[ClipperLib::IntersectNode::Edge1](../../dd/db0/structClipperLib_1_1IntersectNode.html#a43fd790cc38441edb594841d79b25f13),
[ClipperLib::IntersectNode::Edge2](../../dd/db0/structClipperLib_1_1IntersectNode.html#afcb56e7564fedf1c90962a9f75454539),
and
[ClipperLib::IntersectNode::Pt](../../dd/db0/structClipperLib_1_1IntersectNode.html#a91fc92370fb47797dae0602443e6475e).

## ◆ SwapPoints()

void ClipperLib::SwapPoints  | ( | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt1_ ,   
---|---|---|---  
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) & | _pt2_  
| ) | |   
  
Referenced by
[GetOverlapSegment()](../../df/db2/namespaceClipperLib.html#a8817de6dc5a080ead872b1373074c07f).

## ◆ SwapPolyIndexes()

void ClipperLib::SwapPolyIndexes  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _Edge1_ ,   
---|---|---|---  
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _Edge2_  
| ) | |   
  
References
[ClipperLib::TEdge::OutIdx](../../d2/d7f/structClipperLib_1_1TEdge.html#a85d226803a3c54dbc983668f430b7e28).

## ◆ SwapSides()

void ClipperLib::SwapSides  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _Edge1_ ,   
---|---|---|---  
|  | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _Edge2_  
| ) | |   
  
References
[ClipperLib::TEdge::Side](../../d2/d7f/structClipperLib_1_1TEdge.html#aa7840242535b7830744f4387aa53bdfa).

## ◆ TopX()

[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) ClipperLib::TopX  | ( | [TEdge](../../d2/d7f/structClipperLib_1_1TEdge.html) & | _edge_ ,   
---|---|---|---  
|  | const [cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa) | _currentY_  
| ) | |   
  
References
[ClipperLib::TEdge::Bot](../../d2/d7f/structClipperLib_1_1TEdge.html#adddb6b117ed14437613d26cc456bb4bc),
[ClipperLib::TEdge::Dx](../../d2/d7f/structClipperLib_1_1TEdge.html#ace215b877c384f917d18f6c1da913959),
[Round()](../../df/db2/namespaceClipperLib.html#a6635b2c24fa0147ff4ecab56d80e7293),
[ClipperLib::TEdge::Top](../../d2/d7f/structClipperLib_1_1TEdge.html#a9f09500b780f7492d8c4c511aabf1c96),
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[E2InsertsBeforeE1()](../../df/db2/namespaceClipperLib.html#ae002e65db41b2e12c6a29b6c53d95e3d),
and
[IntersectPoint()](../../df/db2/namespaceClipperLib.html#acc907411a778b9ae34f8d852aaa7622a).

## ◆ TranslatePath()

void ClipperLib::TranslatePath  | ( | const [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _input_ ,   
---|---|---|---  
|  | [Path](../../df/db2/namespaceClipperLib.html#af39c8fe00f278f18cc8142fef41242da) & | _output_ ,   
|  | [IntPoint](../../dd/d68/structClipperLib_1_1IntPoint.html) | _delta_  
| ) | |   
  
References
[ClipperLib::IntPoint::X](../../dd/d68/structClipperLib_1_1IntPoint.html#a608d16d39c8762e6c3c0a688efb310b6),
and
[ClipperLib::IntPoint::Y](../../dd/d68/structClipperLib_1_1IntPoint.html#a8445d190cd9013bb34d49b5a8a240425).

Referenced by
[AdaptivePath::Adaptive2d::Execute()](../../d6/d4d/classAdaptivePath_1_1Adaptive2d.html#a175359b1e10be8f27e20b412cbd06071),
and
[MinkowskiSum()](../../df/db2/namespaceClipperLib.html#ae4893aa579fd7c46ce695fd3d1c66e64).

## ◆ UpdateOutPtIdxs()

void ClipperLib::UpdateOutPtIdxs  | ( | [OutRec](../../d1/d21/structClipperLib_1_1OutRec.html) & | _outrec_| ) |   
---|---|---|---|---|---  
  
References
[ClipperLib::OutRec::Idx](../../d1/d21/structClipperLib_1_1OutRec.html#ae2c437dec114034a456a7238ab6d8055),
[ClipperLib::OutPt::Idx](../../d1/de7/structClipperLib_1_1OutPt.html#ad04d3691d47a5d0d9b2ae097e7e7bf10),
[ClipperLib::OutPt::Prev](../../d1/de7/structClipperLib_1_1OutPt.html#a609eb414d5764e78150cceccaffc5d54),
and
[ClipperLib::OutRec::Pts](../../d1/d21/structClipperLib_1_1OutRec.html#a82e9cba88d46d0d60db0b0365c6bd02e).

## Variable Documentation

## ◆ def_arc_tolerance

| double const ClipperLib::def_arc_tolerance = 0.25  
---  
static  
  
## ◆ hiRange

|
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
const ClipperLib::hiRange = 0x3FFFFFFFFFFFFFFFLL  
---  
static  
  
Referenced by
[RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908).

## ◆ loRange

|
[cInt](../../df/db2/namespaceClipperLib.html#a7156730a24951629192d4831334bafaa)
const ClipperLib::loRange = 0x3FFFFFFF  
---  
static  
  
Referenced by
[RangeTest()](../../df/db2/namespaceClipperLib.html#add09a980dfa1da81e1693a55cd912908).

## ◆ pi

| double const ClipperLib::pi = 3.141592653589793238  
---  
static  
  
## ◆ Skip

| [int](../../d1/da0/classint.html) const ClipperLib::Skip = -2  
---  
static  
  
Referenced by
[ClipperLib::ClipperBase::AddPath()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a7545ac6e146894dc8416887eadd01dba),
[GetMaximaPair()](../../df/db2/namespaceClipperLib.html#aeeaa3c8c25502a0bf3f4a82bf36366db),
and
[ClipperLib::ClipperBase::ProcessBound()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a292655c74a7e70a8b8829337c632bdf0).

## ◆ two_pi

| double const ClipperLib::two_pi =
[pi](../../df/db2/namespaceClipperLib.html#a3226215bdfa5b0d7f01e40fc8f131485)
*2  
---  
static  
  
## ◆ Unassigned

| [int](../../d1/da0/classint.html) const ClipperLib::Unassigned = -1  
---  
static  
  
Referenced by
[InitEdge()](../../df/db2/namespaceClipperLib.html#a1b822f020efce65b1e0c4fcdb264fd35),
and
[ClipperLib::ClipperBase::Reset()](../../d9/da0/classClipperLib_1_1ClipperBase.html#a125febb065f23fc55dafffe8d185b642).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

