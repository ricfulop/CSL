---
url: https://freecad.github.io/SourceDoc/d8/d12/classBase_1_1BoundBox3.html
scraped_at: 2025-09-08T15:15:45.847170
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)

[List of all members](../../dd/d88/classBase_1_1BoundBox3-members.html) | Public Types | Public Member Functions | Public Attributes

Base::BoundBox3< _Precision > Class Template Reference

The 3D bounding box class.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#details)

`#include <BoundBox.h>`

##  Public Types  
  
---  
typedef _Precision | [num_type](../../d8/d12/classBase_1_1BoundBox3.html#ab07524e26e6bfa3a33a5c9b3672b4b04)  
enum | [OCTANT](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7) {   
[OCT_LDB](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7a45a16a865434194e8a4edd3ebbaf5ed5)
= 0 ,
[OCT_RDB](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7acc063026e099a227bb5c9fa09d8e3931)
,
[OCT_LUB](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7afc0eb29cba167c0c9faaa92fe4436533)
,
[OCT_RUB](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7a187e906c9ef8b6aa9db954623b88b6cf)
,  
[OCT_LDF](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7a8b7cfac8b42bb8dd97592ec04d2bb1d0)
,
[OCT_RDF](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7a8952c075659192970c9493ed2d305fc2)
,
[OCT_LUF](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7a03ba74c139e74af105821fda5440d3c7)
,
[OCT_RUF](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7a6cb9de3879129a9e5f9879b5c9165076)  
}  
enum | [SIDE](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273d) {   
[LEFT](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273da95bcc23809908928f5694223ba8683c4)
=0 ,
[RIGHT](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273da33e517df634cae411fd27748a5d32b4c)
=1 ,
[TOP](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273da4019873e90196ed2fed1e148ed9e1fc8)
=2 ,
[BOTTOM](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273dac5f3fd886220439532bc77dc888b7be1)
=3 ,  
[FRONT](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273da6436f2bd0406597413c6d94501919c19)
=4 ,
[BACK](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273da5acb65a911ef80581cd7047e5423cb93)
=5 ,
[INVALID](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273da4e33f60e66ff0185f6c1a912fef6b6d4)
=255  
}  
typedef [float_traits](../../d5/d79/structBase_1_1float__traits.html)< [num_type](../../d8/d12/classBase_1_1BoundBox3.html#ab07524e26e6bfa3a33a5c9b3672b4b04) > | [traits_type](../../d8/d12/classBase_1_1BoundBox3.html#a1300171d6ab00e0daa921b0b7c979b57)  
  
##  Public Member Functions  
  
---  
void | [Add](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBB)  
| Appends the bounding box to this box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74)  
  
void | [Add](../../d8/d12/classBase_1_1BoundBox3.html#ac9052e09ea4470fc68fb18b70ac608af) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclVect)  
| Appends the point to the box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ac9052e09ea4470fc68fb18b70ac608af)  
  
|
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html#aa56b9e08b541ba4a8ac1d78c16f0c2e1)
(_Precision fMinX=std::numeric_limits< _Precision >::max(), _Precision
fMinY=std::numeric_limits< _Precision >::max(), _Precision
fMinZ=std::numeric_limits< _Precision >::max(), _Precision
fMaxX=-std::numeric_limits< _Precision >::max(), _Precision
fMaxY=-std::numeric_limits< _Precision >::max(), _Precision
fMaxZ=-std::numeric_limits< _Precision >::max())  
| Builds box from pairs of x,y,z values.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#aa56b9e08b541ba4a8ac1d78c16f0c2e1)  
  
|
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html#a40e6f32a23d26220af8ede3f41450048)
(const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >
&rcBB)  
|
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html#a9487a0fd56ea3aeb25aa4887029571a4)
(const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcCnt,
_Precision fDistance)  
| Defines a bounding box around the center _rcCnt_ with the distances
_fDistance_ in each coordinate.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a9487a0fd56ea3aeb25aa4887029571a4)  
  
|
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38)
(const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >
*pclVect, unsigned long ulCt)  
| Builds box from an array of points.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38)  
  
_Precision | [CalcDiagonalLength](../../d8/d12/classBase_1_1BoundBox3.html#a1750698c5ea174a85685fe67a6b750f1) () const  
| Compute the diagonal length of this bounding box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a1750698c5ea174a85685fe67a6b750f1)  
  
[bool](../../d9/db9/classbool.html) | [CalcEdge](../../d8/d12/classBase_1_1BoundBox3.html#ad2bfe693d14b2d8b501fa58e7fe9a0c6) (unsigned short usEdge, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcP0, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcP1) const  
| Calculates the two points of an edge.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ad2bfe693d14b2d8b501fa58e7fe9a0c6)  
  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > | [CalcOctant](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9) (typename [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >[::OCTANT](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7) Octant) const  
void | [CalcPlane](../../d8/d12/classBase_1_1BoundBox3.html#ae34731e1d63a61b2d83e411a5043ebd6) (unsigned short usPlane, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rBase, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rNormal) const  
| Returns the plane of the given side.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ae34731e1d63a61b2d83e411a5043ebd6)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > | [CalcPoint](../../d8/d12/classBase_1_1BoundBox3.html#a2ea223d76776c01f64b54d0ceebb2eb2) (unsigned short usPoint) const  
| Returns the corner point _usPoint_.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a2ea223d76776c01f64b54d0ceebb2eb2)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > | [ClosestPoint](../../d8/d12/classBase_1_1BoundBox3.html#a9f500110c95df8ca0b5e71e371d64149) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclPt) const  
| Searches for the closest point of the bounding box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a9f500110c95df8ca0b5e71e371d64149)  
  
void | [Enlarge](../../d8/d12/classBase_1_1BoundBox3.html#a0e16270de1f992b79ccff5b987cf20b1) (_Precision fLen)  
| Enlarges the box with factor _fLen_.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a0e16270de1f992b79ccff5b987cf20b1)  
  
[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > | [GetCenter](../../d8/d12/classBase_1_1BoundBox3.html#a552c8fca25d9bb637d3230c4eaf0cd36) () const  
| Returns the center.of the box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a552c8fca25d9bb637d3230c4eaf0cd36)  
  
[bool](../../d9/db9/classbool.html) | [GetOctantFromVector](../../d8/d12/classBase_1_1BoundBox3.html#ae68b2abe794808185a01fd6cb01fad42) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclVct, [OCTANT](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7) &rclOctant) const  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >[::SIDE](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273d) | [GetSideFromRay](../../d8/d12/classBase_1_1BoundBox3.html#ad38d73691548d2736e883838cd400750) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclPt, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclDir) const  
| Returns the side of the bounding box the ray exits.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ad38d73691548d2736e883838cd400750)  
  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >[::SIDE](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273d) | [GetSideFromRay](../../d8/d12/classBase_1_1BoundBox3.html#a900e54e09a7e5ba1909a10a0d83c40ea) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclPt, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclDir, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcInt) const  
| Returns the side of the bounding box the ray exits.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a900e54e09a7e5ba1909a10a0d83c40ea)  
  
[bool](../../d9/db9/classbool.html) | [Intersect](../../d8/d12/classBase_1_1BoundBox3.html#a57f8a89fa940fae5c0921ee09686e7a1) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rcBB) const  
| Checks for intersection.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a57f8a89fa940fae5c0921ee09686e7a1)  
  
[bool](../../d9/db9/classbool.html) | [Intersect](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBB) const  
| Methods for intersection, cuttíng and union of bounding boxes.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2)  
  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > | [Intersected](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBB) const  
| Computes the intersection between two bounding boxes.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea)  
  
[bool](../../d9/db9/classbool.html) | [IntersectionPoint](../../d8/d12/classBase_1_1BoundBox3.html#a49b3e75c0752b639e1efa1a3b2a01e74) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVctDir, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &cVctRes, _Precision epsilon) const  
| Intersection point of an inner search ray with the bounding box, built of
the base _rcVct_ and the direction _rcVctDir_.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a49b3e75c0752b639e1efa1a3b2a01e74)  
  
[bool](../../d9/db9/classbool.html) | [IntersectPlaneWithLine](../../d8/d12/classBase_1_1BoundBox3.html#a5754b8ae362cd53be98a930be6b0cd73) (unsigned short usSide, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcDir, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcP0) const  
| Computes the intersection point of line and a plane of the bounding box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a5754b8ae362cd53be98a930be6b0cd73)  
  
[bool](../../d9/db9/classbool.html) | [IntersectWithLine](../../d8/d12/classBase_1_1BoundBox3.html#aa1b97e4eab9eecfd4711d01a3b9ed533) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcDir, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcP0, [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcP1) const  
| Computes the intersection points of line and bounding box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#aa1b97e4eab9eecfd4711d01a3b9ed533)  
  
[bool](../../d9/db9/classbool.html) | [IsCutLine](../../d8/d12/classBase_1_1BoundBox3.html#a55a718fe21f7a5240ac7b6651b4c5822) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcDir, _Precision fTolerance=0.0f) const  
| Checks for intersection with line incl.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a55a718fe21f7a5240ac7b6651b4c5822)  
  
[bool](../../d9/db9/classbool.html) | [IsCutPlane](../../d8/d12/classBase_1_1BoundBox3.html#aba2def5f3f50102ba0b0cf50cf89b4de) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclBase, const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rclNormal) const  
| Checks if this plane specified by (point,normal) cuts this box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#aba2def5f3f50102ba0b0cf50cf89b4de)  
  
[bool](../../d9/db9/classbool.html) | [IsInBox](../../d8/d12/classBase_1_1BoundBox3.html#a93832ed4c78a3bfb5807a312f12bd5c2) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rcbb) const  
| Checks if this 2D box lies inside the box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a93832ed4c78a3bfb5807a312f12bd5c2)  
  
[bool](../../d9/db9/classbool.html) | [IsInBox](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBB) const  
| Checks if this 3D box lies inside the box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2)  
  
[bool](../../d9/db9/classbool.html) | [IsInBox](../../d8/d12/classBase_1_1BoundBox3.html#a755404902a0ec9b28e954657ba887307) (const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > &rcVct) const  
| Test methods.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a755404902a0ec9b28e954657ba887307)  
  
[bool](../../d9/db9/classbool.html) | [IsValid](../../d8/d12/classBase_1_1BoundBox3.html#a81ee2af5e8251b05ca5e640d78cdde8d) () const  
| Checks whether the bounding box is valid.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a81ee2af5e8251b05ca5e640d78cdde8d)  
  
_Precision | [LengthX](../../d8/d12/classBase_1_1BoundBox3.html#a0e6d8154b86f07ef7f30df18d61b3825) () const  
| Calculates expansion in x-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a0e6d8154b86f07ef7f30df18d61b3825)  
  
_Precision | [LengthY](../../d8/d12/classBase_1_1BoundBox3.html#aef2b52c1723633cec62a66282367e248) () const  
| Calculates expansion in y-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#aef2b52c1723633cec62a66282367e248)  
  
_Precision | [LengthZ](../../d8/d12/classBase_1_1BoundBox3.html#a7f4d3366a1a36a5f2ea3e4898592ceb2) () const  
| Calculates expansion in z-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a7f4d3366a1a36a5f2ea3e4898592ceb2)  
  
void | [MoveX](../../d8/d12/classBase_1_1BoundBox3.html#a3a8d9d97b638fcbdbddb0b9207a1c6ed) (_Precision f)  
| Moves in x-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a3a8d9d97b638fcbdbddb0b9207a1c6ed)  
  
void | [MoveY](../../d8/d12/classBase_1_1BoundBox3.html#a65e24b3a2e5bb42fa521e7de398a4da1) (_Precision f)  
| Moves in y-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a65e24b3a2e5bb42fa521e7de398a4da1)  
  
void | [MoveZ](../../d8/d12/classBase_1_1BoundBox3.html#ab35daacaf52aa276dfafb71724e64d59) (_Precision f)  
| Moves in z-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ab35daacaf52aa276dfafb71724e64d59)  
  
[bool](../../d9/db9/classbool.html) | [operator&&](../../d8/d12/classBase_1_1BoundBox3.html#accc21c947b51f060b7fbdcb2b30e672b) (const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) &rcBB) const  
| Checks for intersection.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#accc21c947b51f060b7fbdcb2b30e672b)  
  
[bool](../../d9/db9/classbool.html) | [operator&&](../../d8/d12/classBase_1_1BoundBox3.html#aa9a296aff571155ea64e7751ee64970b) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBB) const  
| Checks for intersection.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#aa9a296aff571155ea64e7751ee64970b)  
  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | [operator=](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBound)  
| Assignment operator.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004)  
  
void | [Print](../../d8/d12/classBase_1_1BoundBox3.html#a5d47e9f92091d22702254a5394522e1e) (std::ostream &) const  
| Prints the values to stream.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a5d47e9f92091d22702254a5394522e1e)  
  
[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) | [ProjectBox](../../d8/d12/classBase_1_1BoundBox3.html#a4d8b86292716416ed2151d4190291ad1) (const [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) *rclP) const  
| Projects the box onto a plane and returns a 2D box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a4d8b86292716416ed2151d4190291ad1)  
  
void | [ScaleX](../../d8/d12/classBase_1_1BoundBox3.html#ac4c35b32497f9c69862853a0063db925) (_Precision f)  
| Scales in x-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ac4c35b32497f9c69862853a0063db925)  
  
void | [ScaleY](../../d8/d12/classBase_1_1BoundBox3.html#a5f8ab28d01a850e0bba3eab8f2c69d15) (_Precision f)  
| Scales in y-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a5f8ab28d01a850e0bba3eab8f2c69d15)  
  
void | [ScaleZ](../../d8/d12/classBase_1_1BoundBox3.html#a2ba8b887a9017cf134fb97b0ffd9da6e) (_Precision f)  
| Scales in z-direction.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a2ba8b887a9017cf134fb97b0ffd9da6e)  
  
void | [SetVoid](../../d8/d12/classBase_1_1BoundBox3.html#a6400de03cf8abef95e764ce03a1d3f18) ()  
void | [Shrink](../../d8/d12/classBase_1_1BoundBox3.html#ac3a36dd26125c64f822bd6d993589522) (_Precision fLen)  
| Shrinks the box with factor _fLen_.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ac3a36dd26125c64f822bd6d993589522)  
  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > | [Transformed](../../d8/d12/classBase_1_1BoundBox3.html#ad3f66316cd3482e883bb35eff80aae7a) (const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &mat) const  
| Transform the corners of this box with the given matrix and create a new
bounding box.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ad3f66316cd3482e883bb35eff80aae7a)  
  
[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > | [United](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c) (const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > &rcBB) const  
| The union of two bounding boxes.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c)  
  
|
[~BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html#a3a11b485cd2c1abfd5fad90d3a9eccb5)
()  
  
##  Public Attributes  
  
---  
_Precision | [MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a)  
_Precision | [MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1)  
_Precision | [MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a)  
_Precision | [MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6)  
| Public attributes.
[More...](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6)  
  
_Precision | [MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd)  
_Precision | [MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d)  
  
## Detailed Description

template<class _Precision>  
class Base::BoundBox3< _Precision >

The 3D bounding box class.

## Member Typedef Documentation

## ◆ num_type

template<class _Precision >

typedef _Precision
[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision
>::num_type  
---  
  
## ◆ traits_type

template<class _Precision >

typedef
[float_traits](../../d5/d79/structBase_1_1float__traits.html)<[num_type](../../d8/d12/classBase_1_1BoundBox3.html#ab07524e26e6bfa3a33a5c9b3672b4b04)>
[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision
>::traits_type  
---  
  
## Member Enumeration Documentation

## ◆ OCTANT

template<class _Precision >

enum
[Base::BoundBox3::OCTANT](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7)  
---  
  
Enumerator  
---  
OCT_LDB |   
OCT_RDB |   
OCT_LUB |   
OCT_RUB |   
OCT_LDF |   
OCT_RDF |   
OCT_LUF |   
OCT_RUF |   
  
## ◆ SIDE

template<class _Precision >

enum
[Base::BoundBox3::SIDE](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273d)  
---  
  
Enumerator  
---  
LEFT |   
RIGHT |   
TOP |   
BOTTOM |   
FRONT |   
BACK |   
INVALID |   
  
## Constructor & Destructor Documentation

## ◆ BoundBox3() [1/4]

template<class _Precision >

| [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::BoundBox3  | ( | _Precision  | _fMinX_ = `std::numeric_limits<_Precision>::max()`,   
---|---|---|---  
|  | _Precision  | _fMinY_ = `std::numeric_limits<_Precision>::max()`,   
|  | _Precision  | _fMinZ_ = `std::numeric_limits<_Precision>::max()`,   
|  | _Precision  | _fMaxX_ = `-std::numeric_limits<_Precision>::max()`,   
|  | _Precision  | _fMaxY_ = `-std::numeric_limits<_Precision>::max()`,   
|  | _Precision  | _fMaxZ_ = `-std::numeric_limits<_Precision>::max()`  
| ) | |   
explicit  
  
Builds box from pairs of x,y,z values.

## ◆ BoundBox3() [2/4]

template<class _Precision >

[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::BoundBox3  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |   
---|---|---|---|---|---  
  
## ◆ BoundBox3() [3/4]

template<class _Precision >

[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::BoundBox3  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > *  | _pclVect_ ,   
---|---|---|---  
|  | unsigned long  | _ulCt_  
| ) | |   
  
Builds box from an array of points.

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
[Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ BoundBox3() [4/4]

template<class _Precision >

[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::BoundBox3  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcCnt_ ,   
---|---|---|---  
|  | _Precision  | _fDistance_  
| ) | |   
  
Defines a bounding box around the center _rcCnt_ with the distances
_fDistance_ in each coordinate.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ ~BoundBox3()

template<class _Precision >

[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision
>::~[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)  
---  
  
## Member Function Documentation

## ◆ Add() [1/2]

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Add  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |   
---|---|---|---|---|---  
  
Appends the bounding box to this box.

The box can grow but not shrink.

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## ◆ Add() [2/2]

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Add  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclVect_| ) |   
---|---|---|---|---|---  
  
Appends the point to the box.

The box can grow but not shrink.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[Points::PointsGrid::CalculateGridLength()](../../d1/d4d/classPoints_1_1PointsGrid.html#af3e2df12b8f034526f11cbd50d1d7e9d),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::PlaneFit::Dimension()](../../db/dab/classMeshCore_1_1PlaneFit.html#a4044cefa963dbb89b1fea7e4044346b5),
[Mesh::MeshObject::getBoundBox()](../../d8/dcc/classMesh_1_1MeshObject.html#add804b7a6018ab865237929ba06d0e35),
[Points::PointKernel::getBoundBox()](../../dc/de1/classPoints_1_1PointKernel.html#a3e0d8fba9c620059b9ae568fcf6e3630),
[Gui::MovableGroupModel::getBoundingBox()](../../d9/d7f/classGui_1_1MovableGroupModel.html#a9d5d88271a950395efdf91e5eaa18cec),
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
[MeshCore::PlaneFit::GetBoundings()](../../db/dab/classMeshCore_1_1PlaneFit.html#ac3efc54a2ec8ac721de2ad9952750897),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[DrawingGui::OrthoViews::OrthoViews()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#ad9c99867cbd96fff40a1c05750e12033),
[Points::PointsGrid::PointsGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a72b425922922e205bd3234ac832001f2),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[Base::BoundBox3< _Precision
>::Transformed()](../../d8/d12/classBase_1_1BoundBox3.html#ad3f66316cd3482e883bb35eff80aae7a),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ CalcDiagonalLength()

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::CalcDiagonalLength  
---  
  
Compute the diagonal length of this bounding box.

Note

    It's up to the client programmer to make sure that this bounding box is valid. 

Referenced by
[MeshCore::MeshProjection::bboxInsideRectangle()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a539d9b10cf1f5f07d00b366af8789f51),
[MeshCore::MeshGrid::CalculateGridLength()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a6bc8b7f82e0bb07ef2b52f910a1ecb39),
[Points::PointsGrid::CalculateGridLength()](../../d1/d4d/classPoints_1_1PointsGrid.html#a4346ee79c412269f8af15c6bb041b377),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a4db9b92568def721bfcaf960a31ba895),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a4171c1693e3a0aa5f18480425095da45),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
and
[PartGui::ViewProviderMirror::setEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a).

## ◆ CalcEdge()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::CalcEdge  | ( | unsigned short  | _usEdge_ ,   
---|---|---|---  
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcP0_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcP1_  
| ) | |  const  
  
Calculates the two points of an edge.

0\. edge P0-P1 1. edge P1-P2 2. edge P2-P3

  1. edge P3-P0 4. edge P4-P5 5. edge P5-P6
  2. edge P6-P7 7. edge P7-P4 8. edge P0-P4
  3. edge P1-P5 10. edge P2-P6 11. edge P3-P7 

## ◆ CalcOctant()

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::CalcOctant  | ( | typename [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >[::OCTANT](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7) | _Octant_| ) |  const  
---|---|---|---|---|---  
  
References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## ◆ CalcPlane()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::CalcPlane  | ( | unsigned short  | _usPlane_ ,   
---|---|---|---  
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rBase_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rNormal_  
| ) | |  const  
  
Returns the plane of the given side.

References [Base::Vector3< _Precision
>::Set()](../../d1/d13/classBase_1_1Vector3.html#a961b4f52c806809737f1d6fe18c8f9f6).

## ◆ CalcPoint()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::CalcPoint  | ( | unsigned short  | _usPoint_| ) |  const  
---|---|---|---|---|---  
  
Returns the corner point _usPoint_.

0: front,bottom,left 1: front,bottom,right 2: front,top,right 3:
front,top,left 4: back,bottom,left 5: back,bottom,right 6: back,top,right 7:
back,top,left

Referenced by
[MeshCore::MeshTrimByPlane::CheckFacets()](../../d0/d5e/classMeshCore_1_1MeshTrimByPlane.html#a64e328aeacc7da30a2b0c5e417e385b8),
[Mesh::MeshObject::createCube()](../../d8/dcc/classMesh_1_1MeshObject.html#ad110a7788a6987fc4a413cee977548ac),
and
[Mesh::MeshObject::getBoundBox()](../../d8/dcc/classMesh_1_1MeshObject.html#add804b7a6018ab865237929ba06d0e35).

## ◆ ClosestPoint()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::ClosestPoint  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclPt_| ) |  const  
---|---|---|---|---|---  
  
Searches for the closest point of the bounding box.

References
[DraftVecUtils::closest()](../../dc/dc3/group__DRAFTVECUTILS.html#ga8035ae4425c9330b9ba7a75ba7735749),
and [Base::Vector3< _Precision
>::ProjectToPlane()](../../d1/d13/classBase_1_1Vector3.html#a24f91e91499245ab4282c6d0d0b7630c).

## ◆ Enlarge()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Enlarge  | ( | _Precision  | _fLen_| ) |   
---|---|---|---|---|---  
  
Enlarges the box with factor _fLen_.

Referenced by
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::MeshGrid::GetMeshBoundBox()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a374d3cd6548b99b34f8edca08feb2826),
[Base::BoundBox3< _Precision
>::IntersectionPoint()](../../d8/d12/classBase_1_1BoundBox3.html#a49b3e75c0752b639e1efa1a3b2a01e74),
and
[MeshCore::MeshGeomFacet::IntersectWithFacet()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a4324352edc96819d5ce83009cd1ed2df).

## ◆ GetCenter()

template<class _Precision >

[Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision >
[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision
>::GetCenter  
---  
  
Returns the center.of the box.

Referenced by
[MeshCore::MeshProjection::bboxInsideRectangle()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a539d9b10cf1f5f07d00b366af8789f51),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[MeshPartGui::CrossSections::CrossSections()](../../d1/d27/classMeshPartGui_1_1CrossSections.html#a884529081216e2c462f3f2906f602c68),
[PartGui::CrossSections::CrossSections()](../../dc/d84/classPartGui_1_1CrossSections.html#a884529081216e2c462f3f2906f602c68),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[Points::PointsGrid::SearchNearestFromPoint()](../../d1/d4d/classPoints_1_1PointsGrid.html#a9e8a253646681956b8c76b82ae8b9032),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[MeshCore::MeshGrid::SearchNearestFromPoint()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a77ba9a4de41afd3a10ece52f565f0832),
and
[PartGui::ViewProviderMirror::setEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a).

## ◆ GetOctantFromVector()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::GetOctantFromVector  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclVct_ ,   
---|---|---|---  
|  | [OCTANT](../../d8/d12/classBase_1_1BoundBox3.html#a99d39b28f1137245c60cb85d9541aba7) & | _rclOctant_  
| ) | |  const  
  
References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ GetSideFromRay() [1/2]

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >[::SIDE](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273d) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::GetSideFromRay  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclPt_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclDir_  
| ) | |  const  
  
Returns the side of the bounding box the ray exits.

Referenced by
[Points::PointsGrid::SearchNearestFromPoint()](../../d1/d4d/classPoints_1_1PointsGrid.html#a9e8a253646681956b8c76b82ae8b9032),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
and
[MeshCore::MeshGrid::SearchNearestFromPoint()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a77ba9a4de41afd3a10ece52f565f0832).

## ◆ GetSideFromRay() [2/2]

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >[::SIDE](../../d8/d12/classBase_1_1BoundBox3.html#a34fea7cd7f36ef9cee828a35931e273d) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::GetSideFromRay  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclPt_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclDir_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcInt_  
| ) | |  const  
  
Returns the side of the bounding box the ray exits.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ Intersect() [1/2]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Intersect  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
Checks for intersection.

References
[Base::BoundBox2d::MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[Base::BoundBox2d::MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[Base::BoundBox2d::MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[Base::BoundBox2d::MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ Intersect() [2/2]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Intersect  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
Methods for intersection, cuttíng and union of bounding boxes.

Checks for intersection.

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## ◆ Intersected()

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Intersected  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
Computes the intersection between two bounding boxes.

The result is also a bounding box.

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## ◆ IntersectionPoint()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IntersectionPoint  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVctDir_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _cVctRes_ ,   
|  | _Precision  | _epsilon_  
| ) | |  const  
  
Intersection point of an inner search ray with the bounding box, built of the
base _rcVct_ and the direction _rcVctDir_.

_rcVct_ must lie inside the bounding box.

References [Base::BoundBox3< _Precision
>::Enlarge()](../../d8/d12/classBase_1_1BoundBox3.html#a0e16270de1f992b79ccff5b987cf20b1),
[draftutils.utils::epsilon()](../../de/d75/group__draftutils.html#ga7ca4044874669855d2291d7990debb22),
and [Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#a755404902a0ec9b28e954657ba887307).

## ◆ IntersectPlaneWithLine()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IntersectPlaneWithLine  | ( | unsigned short  | _usSide_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcBase_ ,   
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcDir_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcP0_  
| ) | |  const  
  
Computes the intersection point of line and a plane of the bounding box.

References [Base::Vector3< _Precision
>::Scale()](../../d1/d13/classBase_1_1Vector3.html#aff9627b9ca6eb620fbfe189e83aab8d5).

## ◆ IntersectWithLine()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IntersectWithLine  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcDir_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcP0_ ,   
|  | [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcP1_  
| ) | |  const  
  
Computes the intersection points of line and bounding box.

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ IsCutLine()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IsCutLine  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcDir_ ,   
|  | _Precision  | _fTolerance_ = `0.0f`  
| ) | |  const  
  
Checks for intersection with line incl.

search tolerance.

References [Base::Vector3< _Precision
>::Length()](../../d1/d13/classBase_1_1Vector3.html#ad81a005a667df9bbbddb6396d0d11a1a),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

## ◆ IsCutPlane()

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IsCutPlane  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclBase_ ,   
---|---|---|---  
|  | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rclNormal_  
| ) | |  const  
  
Checks if this plane specified by (point,normal) cuts this box.

Note

    It's up to the client programmer to make sure that this bounding box is valid. 

Referenced by
[MeshCore::MeshProjection::bboxInsideRectangle()](../../d8/d39/classMeshCore_1_1MeshProjection.html#a539d9b10cf1f5f07d00b366af8789f51),
[MeshCore::MeshTrimByPlane::CheckFacets()](../../d0/d5e/classMeshCore_1_1MeshTrimByPlane.html#a64e328aeacc7da30a2b0c5e417e385b8),
[MeshCore::MeshAlgorithm::CutWithPlane()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a0db4deb449910dd85fb28ea19e363e1f),
and
[MeshCore::MeshAlgorithm::GetFacetsFromPlane()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a1de62d26b8126163d7359d905c8186c5).

## ◆ IsInBox() [1/3]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IsInBox  | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rcbb_| ) |  const  
---|---|---|---|---|---  
  
Checks if this 2D box lies inside the box.

Note

    It's up to the client programmer to make sure that both bounding boxes are valid. 

References
[Base::BoundBox2d::MaxX](../../de/db4/classBase_1_1BoundBox2d.html#a945cf6dbf19794fadf57611c743d4af1),
[Base::BoundBox2d::MaxY](../../de/db4/classBase_1_1BoundBox2d.html#a16e40b1b2005f47d75fba6802dcd8f80),
[Base::BoundBox2d::MinX](../../de/db4/classBase_1_1BoundBox2d.html#a463231b777b4ac6a329167866d054d36),
and
[Base::BoundBox2d::MinY](../../de/db4/classBase_1_1BoundBox2d.html#acd6ec6a1cc10a691503379e335a24133).

## ◆ IsInBox() [2/3]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IsInBox  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
Checks if this 3D box lies inside the box.

Note

    It's up to the client programmer to make sure that both bounding boxes are valid. 

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## ◆ IsInBox() [3/3]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::IsInBox  | ( | const [Vector3](../../d1/d13/classBase_1_1Vector3.html)< _Precision > & | _rcVct_| ) |  const  
---|---|---|---|---|---  
  
Test methods.

Checks if this point lies inside the box.

Note

    It's up to the client programmer to make sure that this bounding box is valid. 

References [Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
[Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6),
and [Base::Vector3< _Precision
>::z](../../d1/d13/classBase_1_1Vector3.html#a173b74fd2154f7bc808b36e94b4761da).

Referenced by
[MeshCore::MeshGeomFacet::ContainedByOrIntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#ab69acd5404d7fb80317999198cbbf5d5),
[MeshCore::MeshGeomEdge::ContainedByOrIntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#adec15290b8b7c3ef8efdef55ffcf2f57),
[MeshCore::MeshEvalPointOnEdge::Evaluate()](../../d1/dc7/classMeshCore_1_1MeshEvalPointOnEdge.html#a27a96ed60ac713ac411ce61ddbce1722),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[Base::BoundBox3< _Precision
>::IntersectionPoint()](../../d8/d12/classBase_1_1BoundBox3.html#a49b3e75c0752b639e1efa1a3b2a01e74),
[MeshCore::MeshGeomFacet::IntersectWithFacet()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a4324352edc96819d5ce83009cd1ed2df),
[Points::PointsGrid::SearchNearestFromPoint()](../../d1/d4d/classPoints_1_1PointsGrid.html#a9e8a253646681956b8c76b82ae8b9032),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[MeshCore::MeshGrid::SearchNearestFromPoint()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a77ba9a4de41afd3a10ece52f565f0832),
[MeshCore::MeshPointGrid::Verify()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a589ee29752152761422a2c6640e5d4a4),
and
[Points::PointsGrid::Verify()](../../d1/d4d/classPoints_1_1PointsGrid.html#af25ab4e24e21a7e9270fcc06b3ad72d5).

## ◆ IsValid()

template<class _Precision >

[bool](../../d9/db9/classbool.html)
[Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision
>::IsValid  
---  
  
Checks whether the bounding box is valid.

Referenced by
[Mesh::MeshObject::getBoundBox()](../../d8/dcc/classMesh_1_1MeshObject.html#add804b7a6018ab865237929ba06d0e35),
[TechDraw::DrawProjGroup::getXYPosition()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#aaeadc17847095c9f9d5ff6db786e04bd),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ LengthX()

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::LengthX  
---  
  
Calculates expansion in x-direction.

Referenced by
[PathSimulator::PathSim::BeginSimulation()](../../d4/d82/classPathSimulator_1_1PathSim.html#af1e50ef034b9f7be6cc964ba652b81be),
[MeshCore::MeshGrid::CalculateGridLength()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#acf2faee36252826bccea772043200eba),
[Points::PointsGrid::CalculateGridLength()](../../d1/d4d/classPoints_1_1PointsGrid.html#af3e2df12b8f034526f11cbd50d1d7e9d),
[MeshCore::MeshAlgorithm::CalculateMinimumGridLength()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a1211f8ecc192a1f1e18b7493a63196d9),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::MeshGrid::InitGrid()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a2eb04d164c6736d2fb22c3f17cde0a8c),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Inspection::InspectActualShape::InspectActualShape()](../../d8/d95/classInspection_1_1InspectActualShape.html#a56bdfb58a9bb2d1912bb223440fecfb9),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[MeshCore::MeshEigensystem::MeshEigensystem()](../../d1/dba/classMeshCore_1_1MeshEigensystem.html#a7eded057349a45c8986f2da2ceec7674),
[MeshCore::MeshFacetGrid::MeshFacetGrid()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#ae3e86ffb4395165ecbc285e1ca5f7364),
[Inspection::MeshInspectGrid::MeshInspectGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a3e5161b31db9e81a1dcc5b9a60b2b9b1),
[MeshCore::MeshPointGrid::MeshPointGrid()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a067774c9ff6dea0a48b8bb28b33643cf),
[TechDraw::DrawProjGroup::minimumBbViews()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a73d001d82e38bd552fe5518d194a03c3),
[Points::PointsGrid::PointsGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a72b425922922e205bd3234ac832001f2),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[DrawingGui::OrthoViews::set_primary()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a831e5e1c077c72aac518c818122549e0),
[PartDesignGui::ViewProviderDatumCoordinateSystem::setExtents()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#aca9445d2a12b85efb9be68e484501cf9),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
and
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239).

## ◆ LengthY()

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::LengthY  
---  
  
Calculates expansion in y-direction.

Referenced by
[PathSimulator::PathSim::BeginSimulation()](../../d4/d82/classPathSimulator_1_1PathSim.html#af1e50ef034b9f7be6cc964ba652b81be),
[MeshCore::MeshGrid::CalculateGridLength()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#acf2faee36252826bccea772043200eba),
[Points::PointsGrid::CalculateGridLength()](../../d1/d4d/classPoints_1_1PointsGrid.html#af3e2df12b8f034526f11cbd50d1d7e9d),
[MeshCore::MeshAlgorithm::CalculateMinimumGridLength()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a1211f8ecc192a1f1e18b7493a63196d9),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::MeshGrid::InitGrid()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a2eb04d164c6736d2fb22c3f17cde0a8c),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Inspection::InspectActualShape::InspectActualShape()](../../d8/d95/classInspection_1_1InspectActualShape.html#a56bdfb58a9bb2d1912bb223440fecfb9),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[MeshCore::MeshFacetGrid::MeshFacetGrid()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#ae3e86ffb4395165ecbc285e1ca5f7364),
[Inspection::MeshInspectGrid::MeshInspectGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a3e5161b31db9e81a1dcc5b9a60b2b9b1),
[MeshCore::MeshPointGrid::MeshPointGrid()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a067774c9ff6dea0a48b8bb28b33643cf),
[Points::PointsGrid::PointsGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a72b425922922e205bd3234ac832001f2),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[DrawingGui::OrthoViews::set_primary()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a831e5e1c077c72aac518c818122549e0),
[PartDesignGui::ViewProviderDatumCoordinateSystem::setExtents()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#aca9445d2a12b85efb9be68e484501cf9),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
and
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239).

## ◆ LengthZ()

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::LengthZ  
---  
  
Calculates expansion in z-direction.

Referenced by
[PathSimulator::PathSim::BeginSimulation()](../../d4/d82/classPathSimulator_1_1PathSim.html#af1e50ef034b9f7be6cc964ba652b81be),
[MeshCore::MeshGrid::CalculateGridLength()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#acf2faee36252826bccea772043200eba),
[Points::PointsGrid::CalculateGridLength()](../../d1/d4d/classPoints_1_1PointsGrid.html#af3e2df12b8f034526f11cbd50d1d7e9d),
[MeshCore::MeshAlgorithm::CalculateMinimumGridLength()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a1211f8ecc192a1f1e18b7493a63196d9),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::MeshGrid::InitGrid()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a2eb04d164c6736d2fb22c3f17cde0a8c),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Inspection::InspectActualShape::InspectActualShape()](../../d8/d95/classInspection_1_1InspectActualShape.html#a56bdfb58a9bb2d1912bb223440fecfb9),
[MeshCore::MeshGeomEdge::IntersectBoundingBox()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#aa33bee65b66dc0904e254e42f20bf02d),
[MeshCore::MeshGeomFacet::IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[MeshCore::MeshFacetGrid::MeshFacetGrid()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#ae3e86ffb4395165ecbc285e1ca5f7364),
[Inspection::MeshInspectGrid::MeshInspectGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a3e5161b31db9e81a1dcc5b9a60b2b9b1),
[MeshCore::MeshPointGrid::MeshPointGrid()](../../dc/de4/classMeshCore_1_1MeshPointGrid.html#a067774c9ff6dea0a48b8bb28b33643cf),
[Points::PointsGrid::PointsGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a72b425922922e205bd3234ac832001f2),
[MeshCore::MeshOutput::SaveAsymptote()](../../db/d14/classMeshCore_1_1MeshOutput.html#a31276c848ed13571a0e7f6f932e5a45e),
[DrawingGui::OrthoViews::set_primary()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a831e5e1c077c72aac518c818122549e0),
[PartDesignGui::ViewProviderDatumCoordinateSystem::setExtents()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#aca9445d2a12b85efb9be68e484501cf9),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
and
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239).

## ◆ MoveX()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::MoveX  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
Moves in x-direction.

Referenced by
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686).

## ◆ MoveY()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::MoveY  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
Moves in y-direction.

Referenced by
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686).

## ◆ MoveZ()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::MoveZ  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
Moves in z-direction.

## ◆ operator&&() [1/2]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::operator&& | ( | const [BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
Checks for intersection.

## ◆ operator&&() [2/2]

template<class _Precision >

[bool](../../d9/db9/classbool.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::operator&& | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
Checks for intersection.

## ◆ operator=()

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::operator=  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBound_| ) |   
---|---|---|---|---|---  
  
Assignment operator.

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## ◆ Print()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Print  | ( | std::ostream & | | ) |  const  
---|---|---|---|---|---  
  
Prints the values to stream.

## ◆ ProjectBox()

template<class _Precision >

[BoundBox2d](../../de/db4/classBase_1_1BoundBox2d.html) [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::ProjectBox  | ( | const [ViewProjMethod](../../de/daf/classBase_1_1ViewProjMethod.html) *  | _rclP_| ) |  const  
---|---|---|---|---|---  
  
Projects the box onto a plane and returns a 2D box.

References
[Base::BoundBox2d::Add()](../../de/db4/classBase_1_1BoundBox2d.html#a431c0efe7a152057de5551473e1ce330),
[Base::BoundBox2d::SetVoid()](../../de/db4/classBase_1_1BoundBox2d.html#a04f0131a87de65c00a2de633e6255e61),
[Base::Vector3< _Precision
>::x](../../d1/d13/classBase_1_1Vector3.html#ab22366936bae9afc5481c3afdaf5186c),
and [Base::Vector3< _Precision
>::y](../../d1/d13/classBase_1_1Vector3.html#acafa4f9df0fd3150f73b3e9cbee58fd6).

Referenced by
[MeshCore::MeshTrimming::CheckFacets()](../../d3/da1/classMeshCore_1_1MeshTrimming.html#a94a5bf3ea3f16d468c08906a5dcbb472),
and
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f).

## ◆ ScaleX()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::ScaleX  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
Scales in x-direction.

Referenced by
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
and
[TechDraw::DrawProjGroup::makeViewBbs()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a241ecc0ded57718ae3b9c2404bb0e6c9).

## ◆ ScaleY()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::ScaleY  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
Scales in y-direction.

Referenced by
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
and
[TechDraw::DrawProjGroup::makeViewBbs()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a241ecc0ded57718ae3b9c2404bb0e6c9).

## ◆ ScaleZ()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::ScaleZ  | ( | _Precision  | _f_| ) |   
---|---|---|---|---|---  
  
Scales in z-direction.

Referenced by
[TechDraw::DrawProjGroup::getBoundingBox()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a5059b13676a355f63c69411f4a298686),
and
[TechDraw::DrawProjGroup::makeViewBbs()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a241ecc0ded57718ae3b9c2404bb0e6c9).

## ◆ SetVoid()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision
>::SetVoid  
---  
  
## ◆ Shrink()

template<class _Precision >

void [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Shrink  | ( | _Precision  | _fLen_| ) |   
---|---|---|---|---|---  
  
Shrinks the box with factor _fLen_.

## ◆ Transformed()

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::Transformed  | ( | const [Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _mat_| ) |  const  
---|---|---|---|---|---  
  
Transform the corners of this box with the given matrix and create a new
bounding box.

Note

    It's up to the client programmer to make sure that this bounding box is valid. 

References [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#ac9052e09ea4470fc68fb18b70ac608af).

Referenced by
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Inspection::InspectNominalFastMesh::InspectNominalFastMesh()](../../d7/d5d/classInspection_1_1InspectNominalFastMesh.html#a78a893bfa4316faed6b3ee872f47afa1),
[Inspection::InspectNominalMesh::InspectNominalMesh()](../../d6/db5/classInspection_1_1InspectNominalMesh.html#a1acc3cea60a1d6a54804c8d8cf3fd36a),
[Inspection::MeshInspectGrid::MeshInspectGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a3e5161b31db9e81a1dcc5b9a60b2b9b1),
[MeshCore::MeshOutput::SaveX3DContent()](../../db/d14/classMeshCore_1_1MeshOutput.html#acbe6873a664389ec4baaf092be489705),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
and
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5).

## ◆ United()

template<class _Precision >

[BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision >::United  | ( | const [BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)< _Precision > & | _rcBB_| ) |  const  
---|---|---|---|---|---  
  
The union of two bounding boxes.

References [Base::BoundBox3< _Precision
>::MaxX](../../d8/d12/classBase_1_1BoundBox3.html#aa9f944ac2fbb46dc4c55955945b8e33a),
[Base::BoundBox3< _Precision
>::MaxY](../../d8/d12/classBase_1_1BoundBox3.html#a8b26d57de8efd3a97f9591f7f76ae2a1),
[Base::BoundBox3< _Precision
>::MaxZ](../../d8/d12/classBase_1_1BoundBox3.html#a1cbf94a72d1eeeabe5a8029f86f9003a),
[Base::BoundBox3< _Precision
>::MinX](../../d8/d12/classBase_1_1BoundBox3.html#a31f68e191aebba3347c19f10280255e6),
[Base::BoundBox3< _Precision
>::MinY](../../d8/d12/classBase_1_1BoundBox3.html#a699bd0668dbe671a4d7f575fbf40acdd),
and [Base::BoundBox3< _Precision
>::MinZ](../../d8/d12/classBase_1_1BoundBox3.html#a2f1f6a9f2e7a5cc7524ff96e863cdf6d).

## Member Data Documentation

## ◆ MaxX

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::MaxX  
---  
  
Referenced by [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74),
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[Base::BoundBox3< _Precision
>::CalcOctant()](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9),
[MeshGui::SoFCMeshFaceSet::computeBBox()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#ae0221b578f133f244137e9b054d1889b),
[MeshGui::SoFCMeshOpenEdgeSet::computeBBox()](../../d7/d45/classMeshGui_1_1SoFCMeshOpenEdgeSet.html#a7c463febb13e521a77ea2af5b9d28b77),
[MeshGui::SoFCMeshNode::computeBBox()](../../d8/dc1/classMeshGui_1_1SoFCMeshNode.html#aa44c8d0e8f53e3c5e6a0a566efcf8643),
[MeshGui::SoFCMeshOpenEdge::computeBBox()](../../dc/d06/classMeshGui_1_1SoFCMeshOpenEdge.html#a4324762f320719b9c6ed2f672fee9b8e),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[MeshCore::PlaneFit::Dimension()](../../db/dab/classMeshCore_1_1PlaneFit.html#a4044cefa963dbb89b1fea7e4044346b5),
[TechDraw::DrawViewPart::getBoxX()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab9b543a2b059e0d4276b486ac6ba42e7),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a0089586e6b8ecd5db479cd5c276e357c),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a1d4e7ffe0ec553518864d10b1d2c4f85),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2),
[Base::BoundBox3< _Precision
>::Intersected()](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2),
[TechDraw::DrawViewSection::isReallyInBox()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac9213e88b6214016bb7326f4dbe485d8),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[Base::BoundBox3< _Precision
>::operator=()](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004),
[TechDraw::DrawViewSection::sectionLineEnds()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a4f8580c4dea1570bca8520f11f871ebe),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[MeshCore::MeshAlgorithm::Surround()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a29b0bb15913886d98fddbf992ad8083d),
[Base::BoundBox3< _Precision
>::United()](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ MaxY

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::MaxY  
---  
  
Referenced by [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74),
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[Base::BoundBox3< _Precision
>::CalcOctant()](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9),
[MeshGui::SoFCMeshFaceSet::computeBBox()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#ae0221b578f133f244137e9b054d1889b),
[MeshGui::SoFCMeshOpenEdgeSet::computeBBox()](../../d7/d45/classMeshGui_1_1SoFCMeshOpenEdgeSet.html#a7c463febb13e521a77ea2af5b9d28b77),
[MeshGui::SoFCMeshNode::computeBBox()](../../d8/dc1/classMeshGui_1_1SoFCMeshNode.html#aa44c8d0e8f53e3c5e6a0a566efcf8643),
[MeshGui::SoFCMeshOpenEdge::computeBBox()](../../dc/d06/classMeshGui_1_1SoFCMeshOpenEdge.html#a4324762f320719b9c6ed2f672fee9b8e),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[MeshCore::PlaneFit::Dimension()](../../db/dab/classMeshCore_1_1PlaneFit.html#a4044cefa963dbb89b1fea7e4044346b5),
[TechDraw::DrawViewPart::getBoxY()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a5f64214b563dce3e05d03db2871e770b),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a0089586e6b8ecd5db479cd5c276e357c),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a1d4e7ffe0ec553518864d10b1d2c4f85),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2),
[Base::BoundBox3< _Precision
>::Intersected()](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2),
[TechDraw::DrawViewSection::isReallyInBox()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac9213e88b6214016bb7326f4dbe485d8),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[Base::BoundBox3< _Precision
>::operator=()](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[MeshCore::MeshAlgorithm::Surround()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a29b0bb15913886d98fddbf992ad8083d),
[Base::BoundBox3< _Precision
>::United()](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ MaxZ

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::MaxZ  
---  
  
Referenced by [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74),
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[Base::BoundBox3< _Precision
>::CalcOctant()](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9),
[MeshGui::SoFCMeshFaceSet::computeBBox()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#ae0221b578f133f244137e9b054d1889b),
[MeshGui::SoFCMeshOpenEdgeSet::computeBBox()](../../d7/d45/classMeshGui_1_1SoFCMeshOpenEdgeSet.html#a7c463febb13e521a77ea2af5b9d28b77),
[MeshGui::SoFCMeshNode::computeBBox()](../../d8/dc1/classMeshGui_1_1SoFCMeshNode.html#aa44c8d0e8f53e3c5e6a0a566efcf8643),
[MeshGui::SoFCMeshOpenEdge::computeBBox()](../../dc/d06/classMeshGui_1_1SoFCMeshOpenEdge.html#a4324762f320719b9c6ed2f672fee9b8e),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a0089586e6b8ecd5db479cd5c276e357c),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a1d4e7ffe0ec553518864d10b1d2c4f85),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2),
[Base::BoundBox3< _Precision
>::Intersected()](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2),
[TechDraw::DrawViewSection::isReallyInBox()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac9213e88b6214016bb7326f4dbe485d8),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[Base::BoundBox3< _Precision
>::operator=()](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[MeshCore::MeshAlgorithm::Surround()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a29b0bb15913886d98fddbf992ad8083d),
[Base::BoundBox3< _Precision
>::United()](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ MinX

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::MinX  
---  
  
Public attributes.

Referenced by [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74),
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[PathSimulator::PathSim::BeginSimulation()](../../d4/d82/classPathSimulator_1_1PathSim.html#af1e50ef034b9f7be6cc964ba652b81be),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[Base::BoundBox3< _Precision
>::CalcOctant()](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9),
[MeshGui::SoFCMeshFaceSet::computeBBox()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#ae0221b578f133f244137e9b054d1889b),
[MeshGui::SoFCMeshOpenEdgeSet::computeBBox()](../../d7/d45/classMeshGui_1_1SoFCMeshOpenEdgeSet.html#a7c463febb13e521a77ea2af5b9d28b77),
[MeshGui::SoFCMeshNode::computeBBox()](../../d8/dc1/classMeshGui_1_1SoFCMeshNode.html#aa44c8d0e8f53e3c5e6a0a566efcf8643),
[MeshGui::SoFCMeshOpenEdge::computeBBox()](../../dc/d06/classMeshGui_1_1SoFCMeshOpenEdge.html#a4324762f320719b9c6ed2f672fee9b8e),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::PlaneFit::Dimension()](../../db/dab/classMeshCore_1_1PlaneFit.html#a4044cefa963dbb89b1fea7e4044346b5),
[TechDraw::DrawViewPart::getBoxX()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab9b543a2b059e0d4276b486ac6ba42e7),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[MeshCore::MeshGrid::InitGrid()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a2eb04d164c6736d2fb22c3f17cde0a8c),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a0089586e6b8ecd5db479cd5c276e357c),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a1d4e7ffe0ec553518864d10b1d2c4f85),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2),
[Base::BoundBox3< _Precision
>::Intersected()](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2),
[TechDraw::DrawViewSection::isReallyInBox()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac9213e88b6214016bb7326f4dbe485d8),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[Base::BoundBox3< _Precision
>::operator=()](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[MeshCore::MeshAlgorithm::Surround()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a29b0bb15913886d98fddbf992ad8083d),
[Base::BoundBox3< _Precision
>::United()](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ MinY

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::MinY  
---  
  
Referenced by [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74),
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[PathSimulator::PathSim::BeginSimulation()](../../d4/d82/classPathSimulator_1_1PathSim.html#af1e50ef034b9f7be6cc964ba652b81be),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[Base::BoundBox3< _Precision
>::CalcOctant()](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9),
[MeshGui::SoFCMeshFaceSet::computeBBox()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#ae0221b578f133f244137e9b054d1889b),
[MeshGui::SoFCMeshOpenEdgeSet::computeBBox()](../../d7/d45/classMeshGui_1_1SoFCMeshOpenEdgeSet.html#a7c463febb13e521a77ea2af5b9d28b77),
[MeshGui::SoFCMeshNode::computeBBox()](../../d8/dc1/classMeshGui_1_1SoFCMeshNode.html#aa44c8d0e8f53e3c5e6a0a566efcf8643),
[MeshGui::SoFCMeshOpenEdge::computeBBox()](../../dc/d06/classMeshGui_1_1SoFCMeshOpenEdge.html#a4324762f320719b9c6ed2f672fee9b8e),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[MeshCore::PlaneFit::Dimension()](../../db/dab/classMeshCore_1_1PlaneFit.html#a4044cefa963dbb89b1fea7e4044346b5),
[TechDraw::DrawViewPart::getBoxY()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a5f64214b563dce3e05d03db2871e770b),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[MeshCore::MeshGrid::InitGrid()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a2eb04d164c6736d2fb22c3f17cde0a8c),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a0089586e6b8ecd5db479cd5c276e357c),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a1d4e7ffe0ec553518864d10b1d2c4f85),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2),
[Base::BoundBox3< _Precision
>::Intersected()](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2),
[TechDraw::DrawViewSection::isReallyInBox()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac9213e88b6214016bb7326f4dbe485d8),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[Base::BoundBox3< _Precision
>::operator=()](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[PartDesignGui::ViewProviderDatumPlane::setExtents()](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a46c389e51c90183085c76914c9688ec5),
[MeshCore::MeshAlgorithm::Surround()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a29b0bb15913886d98fddbf992ad8083d),
[Base::BoundBox3< _Precision
>::United()](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

## ◆ MinZ

template<class _Precision >

_Precision [Base::BoundBox3](../../d8/d12/classBase_1_1BoundBox3.html)<
_Precision >::MinZ  
---  
  
Referenced by [Base::BoundBox3< _Precision
>::Add()](../../d8/d12/classBase_1_1BoundBox3.html#a32ba2ad27be80f795f7c3fd8b72a4f74),
[Inspection::MeshInspectGrid::AddFacet()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a81c088398a31b7cec75e1da565c8b60b),
[MeshCore::MeshFacetGrid::AddFacet()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#a737435f8d440d1597f019c3ac99b5ceb),
[PathSimulator::PathSim::BeginSimulation()](../../d4/d82/classPathSimulator_1_1PathSim.html#af1e50ef034b9f7be6cc964ba652b81be),
[Base::BoundBox3< _Precision
>::BoundBox3()](../../d8/d12/classBase_1_1BoundBox3.html#a4eaed3aa1e9b2aca93bac60eccc58d38),
[Base::BoundBox3< _Precision
>::CalcOctant()](../../d8/d12/classBase_1_1BoundBox3.html#af263a16d1c1529a6368b1af10e6067c9),
[MeshGui::SoFCMeshFaceSet::computeBBox()](../../d2/d7f/classMeshGui_1_1SoFCMeshFaceSet.html#ae0221b578f133f244137e9b054d1889b),
[MeshGui::SoFCMeshOpenEdgeSet::computeBBox()](../../d7/d45/classMeshGui_1_1SoFCMeshOpenEdgeSet.html#a7c463febb13e521a77ea2af5b9d28b77),
[MeshGui::SoFCMeshNode::computeBBox()](../../d8/dc1/classMeshGui_1_1SoFCMeshNode.html#aa44c8d0e8f53e3c5e6a0a566efcf8643),
[MeshGui::SoFCMeshOpenEdge::computeBBox()](../../dc/d06/classMeshGui_1_1SoFCMeshOpenEdge.html#a4324762f320719b9c6ed2f672fee9b8e),
[MeshGui::SoFCMeshObjectShape::computeBBox()](../../d6/d4f/classMeshGui_1_1SoFCMeshObjectShape.html#a40353cfec2395853aaf8972b867020ed),
[MeshGui::SoFCMeshSegmentShape::computeBBox()](../../d2/d06/classMeshGui_1_1SoFCMeshSegmentShape.html#a45c1ee4441e2a9574f7e0af57657824d),
[MeshGui::SoFCMeshObjectBoundary::computeBBox()](../../dd/dd8/classMeshGui_1_1SoFCMeshObjectBoundary.html#ac008cb8c308bbf55fd6d6eb751cc4cdf),
[FemGui::ViewProviderFEMMeshBuilder::createMesh()](../../dd/dad/classFemGui_1_1ViewProviderFEMMeshBuilder.html#ac4c8b8bc7ab1529efaec1f952dd5e4cb),
[Gui::Dialog::TransformStrategy::getRotationCenter()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a6776dbad4e3e8fe5014cbaa281bfafc2),
[MeshCore::MeshGrid::InitGrid()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a2eb04d164c6736d2fb22c3f17cde0a8c),
[Points::PointsGrid::InitGrid()](../../d1/d4d/classPoints_1_1PointsGrid.html#a5fab2d8d40bd3efa1bdb0f61cefc4109),
[Inspection::MeshInspectGrid::InitGrid()](../../db/d2a/classInspection_1_1MeshInspectGrid.html#a98073d7ba52629f6a48c813a7dd9a8f6),
[Points::PointsGrid::InSide()](../../d1/d4d/classPoints_1_1PointsGrid.html#a0089586e6b8ecd5db479cd5c276e357c),
[MeshCore::MeshGrid::Inside()](../../d7/ddd/classMeshCore_1_1MeshGrid.html#a1d4e7ffe0ec553518864d10b1d2c4f85),
[Base::BoundBox3< _Precision
>::Intersect()](../../d8/d12/classBase_1_1BoundBox3.html#a92c293ab44b0212e213bf0ce1da39bd2),
[Base::BoundBox3< _Precision
>::Intersected()](../../d8/d12/classBase_1_1BoundBox3.html#a2cb80bd333614f0cf03fe69457a746ea),
[Base::BoundBox3< _Precision
>::IsInBox()](../../d8/d12/classBase_1_1BoundBox3.html#adc20299c09dc4e57c6f92ebf9d6945c2),
[TechDraw::DrawViewSection::isReallyInBox()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac9213e88b6214016bb7326f4dbe485d8),
[MeshInfoWatcher::onSelectionChanged()](../../da/df7/classMeshInfoWatcher.html#a721a471d6b4b2e6df04c09cb7c6bcfd8),
[Base::BoundBox3< _Precision
>::operator=()](../../d8/d12/classBase_1_1BoundBox3.html#a33b357da9b0753779a29be4740f29004),
[MeshCore::MeshFacetGrid::SearchNearestFromPoint()](../../da/d34/classMeshCore_1_1MeshFacetGrid.html#afbb767d3a8804d125b5d7b80db72d471),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[PartDesignGui::ViewProviderDatumLine::setExtents()](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a30452eb54c45ae8038b617ca58b8c279),
[MeshCore::MeshAlgorithm::Surround()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a29b0bb15913886d98fddbf992ad8083d),
[Base::BoundBox3< _Precision
>::United()](../../d8/d12/classBase_1_1BoundBox3.html#ac20e6411440cd40ff2ee9f402efb9e8c),
and
[Gui::View3DInventorViewer::viewSelection()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a78a46f0773870b552b8c2da284610af8).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/BoundBox.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

