---
url: https://freecad.github.io/SourceDoc/d9/dfd/group__draftgeoutils.html
scraped_at: 2025-09-08T14:52:00.066296
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Namespaces | Functions | Variables

draftgeoutils

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Draft](../../d1/d35/group__DRAFT.html)

Functions that are meant to handle different geometrical operations. More...

##  Namespaces  
  
---  
namespace | [arcs](../../d0/dce/namespacearcs.html)  
| Provides various functions to work with arcs.  
  
namespace | [circle_inversion](../../df/d2b/namespacecircle__inversion.html)  
| Provides various functions for inversive geometry operations.  
  
namespace | [circles](../../dd/dfe/namespacecircles.html)  
| Provides various functions to work with circles.  
  
namespace | [circles_apollonius](../../da/d87/namespacecircles__apollonius.html)  
| Provides various functions for Apollonius and Soddy circles.  
  
namespace | [circles_incomplete](../../df/d30/namespacecircles__incomplete.html)  
| Provides various incomplete functions for creating circles.  
  
namespace | [cuboids](../../dc/db6/namespacecuboids.html)  
| Provides various functions for cubic shapes (parallelepipeds).  
  
namespace | [edges](../../d2/d06/namespaceedges.html)  
| Provides various functions to work with edges.  
  
namespace | [faces](../../dd/d01/namespacefaces.html)  
| Provides various functions to work with faces.  
  
namespace | [fillets](../../dd/dd9/namespacefillets.html)  
| Provides various functions to work with fillets.  
  
namespace | [general](../../dd/df6/namespacegeneral.html)  
| Provides general functions to work with topological shapes.  
  
namespace | [geo_arrays](../../df/d02/namespacegeo__arrays.html)  
| Provides various functions to work with arrays.  
  
namespace | [geometry](../../d5/d5f/namespacegeometry.html)  
| Provides various functions for general geometrical calculations.  
  
namespace | [intersections](../../d8/da7/namespaceintersections.html)  
| Provides various functions to calculate intersections of shapes.  
  
namespace | [linear_algebra](../../d3/d78/namespacelinear__algebra.html)  
| Provides various functions for linear algebra.  
  
namespace | [offsets](../../d9/dee/namespaceoffsets.html)  
| Provides various functions to work with offsets.  
  
namespace | [sort_edges](../../d4/de7/namespacesort__edges.html)  
| Provides various functions to sort lists of edges.  
  
namespace | [wires](../../de/d60/namespacewires.html)  
| Provides various functions to work with wires.  
  
  
##  Functions  
  
---  
def | [draftgeoutils.intersections.angleBisection](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e) (edge1, edge2)  
def | [draftgeoutils.arcs.arcFrom2Pts](../../d9/dfd/group__draftgeoutils.html#ga2d98ab13b2adf3a3eb6bdd1c559dbcb4) (firstPt, lastPt, center, axis=None)  
def | [draftgeoutils.arcs.arcFromSpline](../../d9/dfd/group__draftgeoutils.html#ga1fb3e4463c835a04a0bd4e060f2fd6f4) (edge)  
def | [draftgeoutils.geometry.are_coplanar](../../d9/dfd/group__draftgeoutils.html#ga6b2614cca55eba229be7f704b31d8701) (shape_a, shape_b, tol=-1)  
def | [draftgeoutils.general.areColinear](../../d9/dfd/group__draftgeoutils.html#ga9f5ec2b0065bccf89ab1700b8aebe673) (e1, e2)  
def | [draftgeoutils.faces.bind](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7) (w1, w2)  
def | [draftgeoutils.geometry.calculatePlacement](../../d9/dfd/group__draftgeoutils.html#gaadbede2965a30dff070b48848d7b4423) (shape)  
def | [draftgeoutils.circles_incomplete.circleFrom1Circle2Lines](../../d9/dfd/group__draftgeoutils.html#ga6a079887c301407c3eecc974f988af7a) (circle, line1, line2)  
def | [draftgeoutils.circles_incomplete.circlefrom1Circle2Points](../../d9/dfd/group__draftgeoutils.html#gabc04fff55820385b1ec052a8b3436869) (circle, point1, point2)  
def | [draftgeoutils.circles.circlefrom1Line2Points](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50) (edge, p1, p2)  
def | [draftgeoutils.circles_incomplete.circleFrom1tan1pt1rad](../../d9/dfd/group__draftgeoutils.html#gab7874bd264401d75b2ce61b2b49cfcbb) (tan1, p1, rad)  
def | [draftgeoutils.circles_incomplete.circleFrom1tan2pt](../../d9/dfd/group__draftgeoutils.html#gadc534d3f5b90e09d807910b7200aaf8e) (tan1, p1, p2)  
def | [draftgeoutils.circles_incomplete.circleFrom2Circle1Lines](../../d9/dfd/group__draftgeoutils.html#gae7a41f61a951cb4a0d0726d12364f411) (circle1, circle2, line)  
def | [draftgeoutils.circles_incomplete.circlefrom2Circles1Point](../../d9/dfd/group__draftgeoutils.html#ga95351cd26522b90bec09fbae691fd0aa) (circle1, circle2, point)  
def | [draftgeoutils.circles_incomplete.circleFrom2CirclesRadius](../../d9/dfd/group__draftgeoutils.html#gaa0d28ff4ba28d9908f1da48ed4b2c6b5) (circle1, circle2, radius)  
def | [draftgeoutils.circles.circlefrom2Lines1Point](../../d9/dfd/group__draftgeoutils.html#gaaea4d08c6dcb36855768307bb5a70aa2) (edge1, edge2, point)  
def | [draftgeoutils.circles.circleFrom2LinesRadius](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734) (edge1, edge2, radius)  
def | [draftgeoutils.circles.circleFrom2PointsRadius](../../d9/dfd/group__draftgeoutils.html#gac5ca6e04d961e3751606a1e4ccf378b4) (p1, p2, radius)  
def | [draftgeoutils.circles_incomplete.circleFrom2tan1pt](../../d9/dfd/group__draftgeoutils.html#ga739b8b437d574830d1acad7cb9047214) (tan1, tan2, point)  
def | [draftgeoutils.circles_incomplete.circleFrom2tan1rad](../../d9/dfd/group__draftgeoutils.html#ga6f89d6a8dd2947536982c3bb9c8eed9c) (tan1, tan2, rad)  
def | [draftgeoutils.circles_apollonius.circleFrom3CircleTangents](../../d9/dfd/group__draftgeoutils.html#gae3f7f09b1882e00129fe07ddc74f21b8) (circle1, circle2, circle3)  
def | [draftgeoutils.circles.circleFrom3LineTangents](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c) (edge1, edge2, edge3)  
def | [draftgeoutils.circles_incomplete.circleFrom3tan](../../d9/dfd/group__draftgeoutils.html#gab90d3a9b019b4d0f39c114d577d94746) (tan1, tan2, tan3)  
def | [draftgeoutils.circles_incomplete.circlefromCircleLinePoint](../../d9/dfd/group__draftgeoutils.html#ga7b123c7225945fa1c242f6680285ebe9) (circle, line, point)  
def | [draftgeoutils.circles_incomplete.circleFromCircleLineRadius](../../d9/dfd/group__draftgeoutils.html#gace9f8dc5910c98dd016dbcebc0614b42) (circle, line, radius)  
def | [draftgeoutils.circles_incomplete.circleFromPointCircleRadius](../../d9/dfd/group__draftgeoutils.html#gaf834e8dc620bf74d0f657cee946be020) (point, circle, radius)  
def | [draftgeoutils.circles.circleFromPointLineRadius](../../d9/dfd/group__draftgeoutils.html#ga163b5f31d9b814e500670ab9cec198b5) (point, edge, radius)  
def | [draftgeoutils.circle_inversion.circleInversion](../../d9/dfd/group__draftgeoutils.html#gaf83de47d0b318d570f1ca51dcc9cbefb) (circle, circle2)  
def | [draftgeoutils.faces.cleanFaces](../../d9/dfd/group__draftgeoutils.html#gadc094c875468b72613ed04077996cc56) (shape)  
def | [draftgeoutils.wires.cleanProjection](../../d9/dfd/group__draftgeoutils.html#gaeac487c387428b021095f192162bf91f) (shape, tessellate=True, seglength=0.05)  
def | [draftgeoutils.faces.concatenate](../../d9/dfd/group__draftgeoutils.html#ga4c22d9073a911f07ce6cb1dde09cd1c1) (shape)  
def | [draftgeoutils.intersections.connect](../../d9/dfd/group__draftgeoutils.html#ga0b7c0fe418afd94ab4e966fe53b88960) (edges, closed=False)  
def | [draftgeoutils.geo_arrays.create_frames](../../d9/dfd/group__draftgeoutils.html#gaa1ce2d95483e22c1ce443616586702c6) (obj, places)  
def | [draftgeoutils.wires.curvetosegment](../../d9/dfd/group__draftgeoutils.html#gafbf52a3d00dd3badab8d7de2bc94f785) (curve, seglen)  
def | [draftgeoutils.wires.curvetowire](../../d9/dfd/group__draftgeoutils.html#ga8b87ef4d82cdde505b429f85b838d062) (obj, steps)  
def | [draftgeoutils.linear_algebra.determinant](../../d9/dfd/group__draftgeoutils.html#ga91c0ac559cf36a56537582afdbdd5164) (mat, n)  
def | [draftgeoutils.general.edg](../../d9/dfd/group__draftgeoutils.html#gad3f6b7a08027b908170525ef5b6da7fe) (p1, p2)  
def | [draftgeoutils.fillets.fillet](../../d9/dfd/group__draftgeoutils.html#ga9ee52e4030cf753ebf972be204bdce1f) (lEdges, r, chamfer=False)  
def | [draftgeoutils.fillets.filletWire](../../d9/dfd/group__draftgeoutils.html#gaa62f069268859d613ce168c61feadaed) (aWire, r, chamfer=False)  
def | [draftgeoutils.geometry.find_plane](../../d9/dfd/group__draftgeoutils.html#ga2255544d596f3dbaa5423bb67f78f69d) (shape, tol=-1)  
def | [draftgeoutils.general.findClosest](../../d9/dfd/group__draftgeoutils.html#ga6005035718ab5b154f253b74ec11b366) (base_point, point_list)  
def | [draftgeoutils.circles.findClosestCircle](../../d9/dfd/group__draftgeoutils.html#gaeeafbd23d667381bd3d3b84c11958ab8) (point, circles)  
def | [draftgeoutils.geometry.findDistance](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca) (point, edge, strict=False)  
def | [draftgeoutils.edges.findEdge](../../d9/dfd/group__draftgeoutils.html#gacde7110bb9761e0a00c4f3393181d1c7) (anEdge, aList)  
def | [draftgeoutils.circles.findHomotheticCenterOfCircles](../../d9/dfd/group__draftgeoutils.html#ga8a2f5385b2e75457e5b317f7ba170816) (circle1, circle2)  
def | [draftgeoutils.intersections.findIntersection](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d) (edge1, edge2, infinite1=False, infinite2=False, ex1=False, ex2=False, dts=True, findAll=False)  
def | [draftgeoutils.edges.findMidpoint](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84) (edge)  
def | [draftgeoutils.geometry.findPerpendicular](../../d9/dfd/group__draftgeoutils.html#ga57ea6e5088030f3848004e83d54b352b) (point, edgeslist, force=None)  
def | [draftgeoutils.circles.findRadicalAxis](../../d9/dfd/group__draftgeoutils.html#gace97041b9159300c6ca150e0373b274c) (circle1, circle2)  
def | [draftgeoutils.circles.findRadicalCenter](../../d9/dfd/group__draftgeoutils.html#gaa0f8671fa707fb91a37636f9d9fdf2fe) (circle1, circle2, circle3)  
def | [draftgeoutils.wires.findWires](../../d9/dfd/group__draftgeoutils.html#ga6645cb7fb8fee4785c1c042a0f1f70ae) (edgeslist)  
def | [draftgeoutils.wires.findWiresOld](../../d9/dfd/group__draftgeoutils.html#gacead01a1c3f70cd7a6863559a6bdde98) (edges)  
def | [draftgeoutils.wires.findWiresOld2](../../d9/dfd/group__draftgeoutils.html#ga263bbbeab564aced2232f8134c17a7fb) (edgeslist)  
def | [draftgeoutils.wires.flattenWire](../../d9/dfd/group__draftgeoutils.html#ga8106baec211f8a64f5317e2287152a7b) (wire)  
def | [draftgeoutils.general.geomType](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737) (edge)  
def | [draftgeoutils.wires.get_extended_wire](../../d9/dfd/group__draftgeoutils.html#gae6d8e69cb869af3d1824fd750b93db3f) (wire, offset_start, offset_end)  
def | [draftgeoutils.geo_arrays.get_init_values](../../d9/dfd/group__draftgeoutils.html#gaf1a91da170d2c13a501be09b8e0822e8) (path, count=6)  
def | [draftgeoutils.geo_arrays.get_n_params](../../d9/dfd/group__draftgeoutils.html#ga703f7e9491525954e9160b8731d495c1) (edge, number, step, norm)  
def | [draftgeoutils.geometry.get_normal](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a) (shape, tol=-1)  
def | [draftgeoutils.wires.get_placement_perpendicular_to_wire](../../d9/dfd/group__draftgeoutils.html#ga3c447b4f36174cca8ff1ab7b463b3aec) (wire)  
def | [draftgeoutils.edges.get_referenced_edges](../../d9/dfd/group__draftgeoutils.html#ga85b3ba8a9ccc711bc0b09a9c9964603e) (property_value)  
def | [draftgeoutils.geometry.get_spline_normal](../../d9/dfd/group__draftgeoutils.html#ga871b3414feb189f4255dae897ee3b684) (edge, tol=-1)  
def | [draftgeoutils.geometry.get_spline_surface_normal](../../d9/dfd/group__draftgeoutils.html#ga6c059568c5d0c2621c9644d99e6aef23) (shape, tol=-1)  
def | [draftgeoutils.geo_arrays.get_twisted_array_shape](../../d9/dfd/group__draftgeoutils.html#gabd719361abde85a5f98618a9a8216578) (base, path, count=15, rot_factor=0.25)  
def | [draftgeoutils.geo_arrays.get_twisted_bridge_shape](../../d9/dfd/group__draftgeoutils.html#ga69cf1ff30ffc570bcf54fde886dff1ca) (base, path, count=15, rot_factor=0.25, width=100, thickness=10)  
def | [draftgeoutils.geo_arrays.get_twisted_placements](../../d9/dfd/group__draftgeoutils.html#ga9c5399869f1738ac24d9b6923a84c992) (path, count=15, rot_factor=0.25)  
def | [draftgeoutils.faces.getBoundary](../../d9/dfd/group__draftgeoutils.html#gaab4aa59fecdb2639faba56e457c3183e) (shape)  
def | [draftgeoutils.general.getBoundaryAngles](../../d9/dfd/group__draftgeoutils.html#ga2a13f9cd58b77895db36cb76498ca36b) (angle, [alist](../../d2/dd0/structalist.html))  
def | [draftgeoutils.circles.getCircleFromSpline](../../d9/dfd/group__draftgeoutils.html#gacde5b7f0b59d56ae852c77f40889913e) (edge)  
def | [draftgeoutils.cuboids.getCubicDimensions](../../d9/dfd/group__draftgeoutils.html#ga594409c27f69bd528d72d25ee42321ca) (shape)  
def | [draftgeoutils.general.getQuad](../../d9/dfd/group__draftgeoutils.html#ga05b3b3bca55d3b70e31c09a3903ab38e) (face)  
def | [draftgeoutils.geometry.getRotation](../../d9/dfd/group__draftgeoutils.html#ga8b265d6e556f0015d0e732088d6ad1bd) (v1, v2=App.Vector(0, 0, 1))  
def | [draftgeoutils.edges.getTangent](../../d9/dfd/group__draftgeoutils.html#gade4f4721afcac4eb74bbb38729e6b2c6) (edge, from_point=None)  
def | [draftgeoutils.general.getVerts](../../d9/dfd/group__draftgeoutils.html#gad75a2f93446368eb6d528d208c4852a6) (shape)  
def | [draftgeoutils.general.hasCurves](../../d9/dfd/group__draftgeoutils.html#ga07bdf78aee8a42b9a55f19ffe66b2e3b) (shape)  
def | [draftgeoutils.general.hasOnlyWires](../../d9/dfd/group__draftgeoutils.html#ga1c1317556633dcb677c1cabb54a385df) (shape)  
def | [draftgeoutils.circles_apollonius.innerSoddyCircle](../../d9/dfd/group__draftgeoutils.html#ga37c8fad5fc27a46258f40cac81834d74) (circle1, circle2, circle3)  
def | [draftgeoutils.edges.invert](../../d9/dfd/group__draftgeoutils.html#ga60dc82b8b95b16ffa97e1ccd715f099e) (shape)  
def | [draftgeoutils.faces.is_coplanar](../../d9/dfd/group__draftgeoutils.html#gac12735fced2e5e984d015b18ed430a5f) (faces, tol=-1)  
def | [draftgeoutils.edges.is_line](../../d9/dfd/group__draftgeoutils.html#ga3b53489edbb1dbef670e655e27b02266) (bspline)  
def | [draftgeoutils.geometry.is_planar](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4) (shape, tol=-1)  
def | [draftgeoutils.geometry.is_straight_line](../../d9/dfd/group__draftgeoutils.html#gaca3c302955adc40b70eb1d12fc43c083) (shape, tol=-1)  
def | [draftgeoutils.general.isAligned](../../d9/dfd/group__draftgeoutils.html#ga49492efd593bd9ac9b4fd584be1cd929) (edge, axis="x")  
def | [draftgeoutils.arcs.isClockwise](../../d9/dfd/group__draftgeoutils.html#gacc819a72923773e1ec59cf14f2f87f78) (edge, ref=None)  
def | [draftgeoutils.cuboids.isCubic](../../d9/dfd/group__draftgeoutils.html#ga8f0c24d453468e6cc90a97fd8ae93344) (shape)  
def | [draftgeoutils.general.isNull](../../d9/dfd/group__draftgeoutils.html#ga46bc138943ec567affb4334962cb64c5) (something)  
def | [draftgeoutils.general.isPtOnEdge](../../d9/dfd/group__draftgeoutils.html#gae92d2e4d632e3c28a4136c29eba58eb8) (pt, edge)  
def | [draftgeoutils.wires.isReallyClosed](../../d9/dfd/group__draftgeoutils.html#gaefe28a41fe05def007e8f1fd6247f247) (wire)  
def | [draftgeoutils.edges.isSameLine](../../d9/dfd/group__draftgeoutils.html#gab4ae86b3ec0b393f14d2cc9910ce7dbb) (e1, e2)  
def | [draftgeoutils.general.isValidPath](../../d9/dfd/group__draftgeoutils.html#ga7cb858fd2c7d6d7a108dbb70aaf1348d) (shape)  
def | [draftgeoutils.arcs.isWideAngle](../../d9/dfd/group__draftgeoutils.html#gabfa0e00bb4a08ea5b20fd7be3650aa96) (edge)  
def | [draftgeoutils.linear_algebra.linearFromPoints](../../d9/dfd/group__draftgeoutils.html#ga8516932a8adbcc4039516c6f930a1679) (p1, p2)  
def | [draftgeoutils.geo_arrays.make_tunnel](../../d9/dfd/group__draftgeoutils.html#ga86c918812d79995c84d2a517b49f70ca) (path, profiles)  
def | [draftgeoutils.geo_arrays.make_walkway](../../d9/dfd/group__draftgeoutils.html#gafaeaf94acb67d0e121f2462bc5d01804) (path, width=100, thickness=10)  
def | [draftgeoutils.geometry.mirror](../../d9/dfd/group__draftgeoutils.html#ga5fcd07ec3396b34feeedf021c5c4ae51) (point, edge)  
def | [draftgeoutils.offsets.offset](../../d9/dfd/group__draftgeoutils.html#gad4289006425ada5bfb41c50dd60c7b98) (edge, vector, trim=False)  
def | [draftgeoutils.offsets.offsetWire](../../d9/dfd/group__draftgeoutils.html#ga05bacae1f1c67ceaba7aa1c37c8f758f) (wire, dvec, bind=False, occ=False, widthList=None, offsetMode=None, alignList=[], normal=None, basewireOffset=0)  
def | [draftgeoutils.edges.orientEdge](../../d9/dfd/group__draftgeoutils.html#ga13b05c710ac80b4c3669ac1ae1529906) (edge, normal=None, make_arc=False)  
def | [draftgeoutils.circles_apollonius.outerSoddyCircle](../../d9/dfd/group__draftgeoutils.html#ga57eb2ca2e8dd69f6fb15182214e32b25) (circle1, circle2, circle3)  
def | [draftgeoutils.offsets.pocket2d](../../d9/dfd/group__draftgeoutils.html#ga65736a1b5af4c622ee3f176a7a288703) (shape, [offset](../../d9/dfd/group__draftgeoutils.html#gad4289006425ada5bfb41c50dd60c7b98))  
def | [draftgeoutils.circle_inversion.pointInversion](../../d9/dfd/group__draftgeoutils.html#ga2e9e5f6e50364165f9e6e1f8f5d5d8f8) (circle, point)  
def | [draftgeoutils.circle_inversion.polarInversion](../../d9/dfd/group__draftgeoutils.html#ga54bc622493ab5bc634b63a70f5fc7ef7) (circle, edge)  
def | [draftgeoutils.general.precision](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38) ()  
def | [draftgeoutils.geo_arrays.print_places](../../d9/dfd/group__draftgeoutils.html#ga50085e7d4f807221b4f3d528301a00ac) (places, title="Places")  
def | [draftgeoutils.wires.rebaseWire](../../d9/dfd/group__draftgeoutils.html#gadb63f98992b548542583b12a1b95cc95) (wire, vidx=0)  
def | [draftgeoutils.wires.removeInterVertices](../../d9/dfd/group__draftgeoutils.html#ga02af528fa3ba94a6061f7ac12c4e7cbc) (wire)  
def | [draftgeoutils.faces.removeSplitter](../../d9/dfd/group__draftgeoutils.html#ga72745ecc60b8a0bc4fa055195cc78594) (shape)  
def | [draftgeoutils.sort_edges.sortEdges](../../d9/dfd/group__draftgeoutils.html#ga92e9ec6f28e14561900f506fef0e928e) (edges)  
def | [draftgeoutils.sort_edges.sortEdgesOld](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3) (lEdges, aVertex=None)  
def | [draftgeoutils.wires.superWire](../../d9/dfd/group__draftgeoutils.html#ga55c4d57190f5e47bd7026e379d49fd01) (edgeslist, closed=False)  
def | [draftgeoutils.wires.tessellateProjection](../../d9/dfd/group__draftgeoutils.html#ga87448d4fa77c5a6539c47116c57bb6c8) (shape, seglen)  
def | [draftgeoutils.general.v1](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804) (edge)  
def | [draftgeoutils.general.vec](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c) (edge, use_orientation=False)  
def | [draftgeoutils.intersections.wiresIntersect](../../d9/dfd/group__draftgeoutils.html#ga5e7ce6b0591a23ad098be94b4c64dd67) (wire1, wire2)  
  
##  Variables  
  
---  
def | [draftgeoutils.geometry.getNormal](../../d9/dfd/group__draftgeoutils.html#ga5d0e3793d7213b7c5dc29d997aaa0af3) = [get_normal](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a)  
def | [draftgeoutils.geometry.getSplineNormal](../../d9/dfd/group__draftgeoutils.html#ga9893b69ce57998c060119a8d03a6e449) = [get_spline_normal](../../d9/dfd/group__draftgeoutils.html#ga871b3414feb189f4255dae897ee3b684)  
def | [draftgeoutils.faces.isCoplanar](../../d9/dfd/group__draftgeoutils.html#ga36dfe6563d376f8c99e9986bff47487b) = [is_coplanar](../../d9/dfd/group__draftgeoutils.html#gac12735fced2e5e984d015b18ed430a5f)  
def | [draftgeoutils.edges.isLine](../../d9/dfd/group__draftgeoutils.html#ga87b8c31cd76d4e1b5ad8ddb578655e68) = [is_line](../../d9/dfd/group__draftgeoutils.html#ga3b53489edbb1dbef670e655e27b02266)  
def | [draftgeoutils.geometry.isPlanar](../../d9/dfd/group__draftgeoutils.html#gaa187cecbe51087aa0bd6a5c41fb2d7f2) = [is_planar](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4)  
|
[draftgeoutils.general.NORM](../../d9/dfd/group__draftgeoutils.html#gaf9cab34b1a8e3ad8d86fb8e4d1e3798f)
= App.Vector(0, 0, 1)  
|
[draftgeoutils.general.PARAMGRP](../../d9/dfd/group__draftgeoutils.html#ga1a9831c55b63bf623c2b8fb44f4d206e)
= App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft")  
  
## Detailed Description

Functions that are meant to handle different geometrical operations.

## Function Documentation

## ◆ angleBisection()

def draftgeoutils.intersections.angleBisection  | ( |  | _edge1_ ,   
---|---|---|---  
|  |  | _edge2_  
| ) | |   
      
    
    Return an edge that bisects the angle between the 2 straight edges.

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1).

Referenced by
[draftgeoutils.circles.circlefrom2Lines1Point()](../../d9/dfd/group__draftgeoutils.html#gaaea4d08c6dcb36855768307bb5a70aa2),
[draftgeoutils.circles.circleFrom2LinesRadius()](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734),
and
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c).

## ◆ arcFrom2Pts()

def draftgeoutils.arcs.arcFrom2Pts  | ( |  | _firstPt_ ,   
---|---|---|---  
|  |  | _lastPt_ ,   
|  |  | _center_ ,   
|  |  | _axis_ = `None`  
| ) | |   
      
    
    Build an arc with center and 2 points, can be oriented with axis.

Referenced by
[draftgeoutils.fillets.fillet()](../../d9/dfd/group__draftgeoutils.html#ga9ee52e4030cf753ebf972be204bdce1f).

## ◆ arcFromSpline()

def draftgeoutils.arcs.arcFromSpline  | ( |  | _edge_| ) |   
---|---|---|---|---|---  
      
    
    Turn given edge into a circular arc from three points.
    
    Takes its first point, midpoint and endpoint. It works best with bspline
    segments such as those from imported svg files. Use this only
    if you are sure your edge is really an arc.
    
    It returns None if there is a problem, including passing straight edges.
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ are_coplanar()

def draftgeoutils.geometry.are_coplanar  | ( |  | _shape_a_ ,   
---|---|---|---  
|  |  | _shape_b_ ,   
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Return True if exist a plane containing both shapes.

References
[draftgeoutils.geometry.find_plane()](../../d9/dfd/group__draftgeoutils.html#ga2255544d596f3dbaa5423bb67f78f69d),
and
[draftgeoutils.geometry.is_planar()](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4).

Referenced by
[draftgeoutils.faces.is_coplanar()](../../d9/dfd/group__draftgeoutils.html#gac12735fced2e5e984d015b18ed430a5f).

## ◆ areColinear()

def draftgeoutils.general.areColinear  | ( |  | _e1_ ,   
---|---|---|---  
|  |  | _e2_  
| ) | |   
      
    
    Return True if both edges are colinear.

References
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ bind()

def draftgeoutils.faces.bind  | ( |  | _w1_ ,   
---|---|---|---  
|  |  | _w2_  
| ) | |   
      
    
    Bind 2 wires by their endpoints and returns a face.

Referenced by
[PartDesignGui::Workbench.activated()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced),
[Gui::ViewProviderDocumentObject.addDefaultAction()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#acc97bc55d9a89b187f0d6bf261e70a2d),
[Base::InventorBuilder.addMaterialBinding()](../../db/d7f/classBase_1_1InventorBuilder.html#aaf3d9b392aaa63590b3ee970943bea64),
[Gui::Application.Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[MeshPartGui::CrossSections.apply()](../../d1/d27/classMeshPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[PartGui::CrossSections.apply()](../../dc/d84/classPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[PartDesignGui::ViewProviderAddSub.attach()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a87c8377f96db07446ff81f9c0c741f22),
[PartDesignGui::ViewProviderBody.attach()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a12e5a7b4da5cecd7fe82062ad9051176),
[TechDrawGui::ViewProviderDrawingView.attach()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#ab6efd26a6629d730940224f8ee8788b6),
[TechDrawGui::ViewProviderPage.attach()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac4ba78ec2544fc891ed71efbfef08160),
[App::DocumentObserver.attachDocument()](../../d5/d52/classApp_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1),
[Gui::DocumentObserver.attachDocument()](../../d0/dbb/classGui_1_1DocumentObserver.html#a7b62ebc00f12f189dd1338cbd9817ac1),
[Gui::SelectionObserver.attachSelection()](../../dc/d3c/classGui_1_1SelectionObserver.html#a53be7b2a565108a34406ac225b0da211),
[Gui::AutoSaveProperty.AutoSaveProperty()](../../d5/dc8/classGui_1_1AutoSaveProperty.html#a4ef3eac8fbe363bced4d9ffe6b553caf),
[Gui::ExpressionBinding.bind()](../../dc/d5a/classGui_1_1ExpressionBinding.html#aba7b2c918c04b6e3f589e53876cdb761),
[Gui::Dialog::DocumentRecoveryFinder.checkForPreviousCrashes()](../../dd/dc8/classGui_1_1Dialog_1_1DocumentRecoveryFinder.html#a02d50848d09bcf7c3c8b7ae52c4f1c8a),
[MeshGui::ViewProviderMesh.clipMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2163df57149a01e40800e85a88d3ce20),
[Cloud::Module.cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4),
[MeshCore::MeshCurvature.ComputePerFace()](../../d3/d7e/classMeshCore_1_1MeshCurvature.html#a97ba030abe06bd5b51f0b1a09c3ea3b6),
[Gui::UiLoaderPy.createWidget()](../../dc/df2/classGui_1_1UiLoaderPy.html#a78eeab608660613890acc1582c1043c4),
[PartGui::DlgBooleanOperation.DlgBooleanOperation()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a9d9f1182519df949d604569a6a3e0f3d),
[Gui::Dialog::DlgDisplayPropertiesImp.DlgDisplayPropertiesImp()](../../df/ddf/classGui_1_1Dialog_1_1DlgDisplayPropertiesImp.html#af58cc9d688ef2c00f1184a67885e1182),
[PartGui::DlgFilletEdges.DlgFilletEdges()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a16463a511a5a288028ef96edb2b3aef6),
[Gui::Document.Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[Gui::DocumentItem.DocumentItem()](../../df/d15/classGui_1_1DocumentItem.html#af15fd697b501c60b7e1141865e3ccf77),
[Gui::DocumentModel.DocumentModel()](../../dc/dc8/classGui_1_1DocumentModel.html#a91f260cdfeeb43d912f106418916223c),
[Gui::DocumentObjectData.DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18),
[App::DocumentObserver.DocumentObserver()](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71),
[Gui::ElementColors.ElementColors()](../../db/d21/classGui_1_1ElementColors.html#a7d0d5836a9361c145408b75cf8b0b33c),
[Gui::ViewProvider.eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99),
[Inspection::Feature.execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Gui::ViewProviderOriginGroupExtension.extensionAttach()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#ae4e983b8437ebedcf3d8b82b3c4997ae),
[App::GroupExtension.extensionOnChanged()](../../da/d3a/classApp_1_1GroupExtension.html#a2d3ccf9dc3d911c632e1da63212c007f),
[PartGui::ViewProviderAttachExtension.extensionSetupContextMenu()](../../d7/d61/classPartGui_1_1ViewProviderAttachExtension.html#a881bdd5ca4dc26e051f378275c0765fe),
[PartGui::ViewProviderSplineExtension.extensionSetupContextMenu()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a9d9a2018c8e8f0aa8b7681aa66090d7b),
[PartGui::FaceColors.FaceColors()](../../db/d9e/classPartGui_1_1FaceColors.html#a5aef3588ddb084101d511fc687ac45d7),
[MeshGui::ViewProviderMesh.getVisibleFacets()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a9b7898ba732c24f6d717873ff851ad55),
[Gui::GraphvizView.GraphvizView()](../../dd/d86/classGui_1_1GraphvizView.html#a1e46d2a16a77346e54d76e9b8db662f7),
[App::PropertyExpressionEngine.hasSetValue()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a0a19da5a601f9a5006885b9d4c197723),
[ShapeCache.init()](../../d5/d4b/structShapeCache.html#a6928c42f75e712eb958a0624a0a1c04d),
[App::DocInfo.init()](../../d7/d23/classApp_1_1DocInfo.html#a0ffd4c2cde7fec2bb8a47d3da8cad9ca),
[Spreadsheet::PropertySheet.insertRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa84f3f19aed8b5355d16cece5eb4a5d9),
[Gui::TaskView::TaskView.keyPressEvent()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#ad4f95ef39f74949ad9d4fa5eeeab040a),
[Gui::LinkInfo.LinkInfo()](../../d4/da4/classGui_1_1LinkInfo.html#ae3618e9bfdb664830e6725d702879020),
[Gui::ManualAlignment.ManualAlignment()](../../d7/d97/classGui_1_1ManualAlignment.html#a6be1cafbf2b52f6cb5491ffff79e66ce),
[Gui::MDIView.MDIView()](../../df/d23/classGui_1_1MDIView.html#a50d7592301ab312ea3b56178ee893718),
[TechDrawGui::MDIViewPage.MDIViewPage()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5bfb8fa1e3810804cd8c7607f97a996b),
[MeasureInfo.MeasureInfo()](../../d5/dbd/structMeasureInfo.html#ac636bdb4aa3543a855c824696196b5c3),
[App::MergeDocuments.MergeDocuments()](../../d6/d0c/classApp_1_1MergeDocuments.html#aabfd8fec3eb7938a5af2e14c18e50a76),
[Gui::MergeDocuments.MergeDocuments()](../../d5/d20/classGui_1_1MergeDocuments.html#aabfd8fec3eb7938a5af2e14c18e50a76),
[Gui::DAG::Model.Model()](../../df/d26/classGui_1_1DAG_1_1Model.html#a81b067d165657725e854c9ce8e038fec),
[App::Application.newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b),
[Gui::Dialog::DocumentRecovery.on_buttonCleanup_clicked()](../../d2/da2/classGui_1_1Dialog_1_1DocumentRecovery.html#a059d2150acb8cdd134bcab32826669d3),
[Spreadsheet::PropertySheet.onAddDep()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa1281131d3e532763893e9d22544b189),
[PartDesign::SubShapeBinder.onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[DrawingGui::OrthoViews.OrthoViews()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#ad9c99867cbd96fff40a1c05750e12033),
[Gui::Dialog::Placement.Placement()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a61902824aa6953c8333e8d319eab8374),
[Gui::DocumentWeakPtrT::Private.Private()](../../df/db9/classDocumentWeakPtrT_1_1Private.html#ab5c208ca0616f4cd278925efa1c31e04),
[Gui::PropertyView.PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[Spreadsheet::PropertySheet.removeColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ada4ceb76fd79dc130476fe307f77e0a1),
[Spreadsheet::PropertySheet.removeRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5ff589d68c79b8387678e38007f8733f),
[Gui::SelectionSingleton.SelectionSingleton()](../../d4/dca/classGui_1_1SelectionSingleton.html#a7d8f654b071cb1d530bb39dadc49620f),
[App::DocumentObjectWeakPtrT::Private.set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835),
[Gui::ViewProviderWeakPtrT::Private.set()](../../d3/d91/classViewProviderWeakPtrT_1_1Private.html#a452f5031c3805a079fc1ae8a05d0a64a),
[SketcherGui::ViewProviderSketch.setEdit()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ad28c651e806a00fca15332d4c04b47c9),
[SpreadsheetGui::SheetTableView.setSheet()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a8cbd84448bed5fd18c99955d00495f8c),
[FemGui::ViewProviderFemAnalysis.setupContextMenu()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a810d529ee86207928e88da63e5c10516),
[MeshGui::ViewProviderMesh.setupContextMenu()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a14fb39b4d986d6bcd3b3d38ac6b79424),
[PartGui::ViewProviderPrimitive.setupContextMenu()](../../dd/dfd/classPartGui_1_1ViewProviderPrimitive.html#abea2a5f699192afe8ab8f6a8168cad3f),
[TechDrawGui::ViewProviderBalloon.setupContextMenu()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a565b5cb9dc2e362ef10e12bbf44a0617),
[TechDrawGui::ViewProviderDimension.setupContextMenu()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a08d18e44457f139fcb55fe8d3ea139a5),
[Gui::ViewProviderTextDocument.setupContextMenu()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a5a639a77236f3bbde9daade6cf323fe8),
[Gui::ViewProviderPart.setupContextMenu()](../../d9/d6c/classGui_1_1ViewProviderPart.html#af72e6c73209d70ff7f57643aa27adebf),
[PartDesignGui::ViewProviderBody.setupContextMenu()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a787b6db82df30a9f214e716065bc4205),
[FemGui::FunctionWidget.setViewProvider()](../../dc/d25/classFemGui_1_1FunctionWidget.html#a0083237a39c65525f04f5124c07ae2d6),
[SpreadsheetGui::SheetModel.SheetModel()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aca374b8f387985ec3756f86f3cac2c45),
[SpreadsheetGui::SheetView.SheetView()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#ad1aa4b1386fff9896ed1ecb74172b1a1),
[Sketcher::SketchObject.SketchObject()](../../d9/dad/classSketcher_1_1SketchObject.html#a79a5ce808811802e0d7c772a78248494),
[Gui::Application.slotNewDocument()](../../d9/da8/classGui_1_1Application.html#ab61252ad46efb80f5fd98cc3957e83eb),
[Reen::BSplineParameterCorrection.SolveWithSmoothing()](../../de/d74/classReen_1_1BSplineParameterCorrection.html#a57b33b7e3e48ea0d4a3fe6b3214b3015),
[Gui::ManualAlignment.startAlignment()](../../d7/d97/classGui_1_1ManualAlignment.html#adac18d1fdb3b8dce1361e26c9beba687),
[MeshGui::MeshFillHole.startEditing()](../../d5/d4f/classMeshGui_1_1MeshFillHole.html#a611c571141e0f653b195fcc94e68a191),
[StdCmdDrawStyle.StdCmdDrawStyle()](../../d1/d5a/classStdCmdDrawStyle.html#aca4a408d9e11712036a9a23c5a0f1f2d),
[StdCmdUserEditMode.StdCmdUserEditMode()](../../df/dc4/classStdCmdUserEditMode.html#a6b6c36a677649192695eaafde169e146),
[Gui::TaskView::TaskAppearance.TaskAppearance()](../../d6/d8d/classGui_1_1TaskView_1_1TaskAppearance.html#a22f06e7b6366730aacf3d59115d603b5),
[PartGui::TaskAttacher.TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
[PartDesignGui::TaskHoleParameters.TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
[SandboxGui::TaskPanelView.TaskPanelView()](../../d1/d99/classSandboxGui_1_1TaskPanelView.html#a37051f4883eba702df09cf5086c3c0c4),
[SketcherGui::TaskSketcherConstraints.TaskSketcherConstraints()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#aa7c422db0a8955ac9e5214388be93a6d),
[SketcherGui::TaskSketcherElements.TaskSketcherElements()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a58295f4cd0ec5cf69b7c36cdf9c49e12),
[SketcherGui::TaskSketcherGeneral.TaskSketcherGeneral()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#acb35aefc057b31af4b7c6e9c87e1f0d4),
[SketcherGui::TaskSketcherMessages.TaskSketcherMessages()](../../d0/dc0/classSketcherGui_1_1TaskSketcherMessages.html#afbe205caa86a38f2afe97602838de648),
[PartDesignGui::TaskTransformedMessages.TaskTransformedMessages()](../../dc/d0e/classPartDesignGui_1_1TaskTransformedMessages.html#a06cb4c20664ef8b3d4e724b45815c0d4),
[Gui::TaskView::TaskView.TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#aa4e4f7cddfbcf1ddfc35ce4cec275b73),
[Gui::TreeWidget.TreeWidget()](../../de/de0/classGui_1_1TreeWidget.html#a02ed96eef13cfa9307ee34d5c68ab7b6),
[MeshGui::ViewProviderMesh.trimMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a99db0ab49ba22437ef202c633d752b52),
[App::LinkBaseExtension.updateGroup()](../../da/dd9/classApp_1_1LinkBaseExtension.html#aa4c9b7b4b1601759cac34c3c598bcac2),
[Gui::DAG::View.View()](../../de/d24/classGui_1_1DAG_1_1View.html#a0c4a0810ba81a2cf65205ae283962cdc),
[Gui::WorkbenchGroup.WorkbenchGroup()](../../d6/d6c/classGui_1_1WorkbenchGroup.html#ac5f683dcc3817191618b0206156ef037),
and
[SMESH_Mesh.~SMESH_Mesh()](../../d5/d97/classSMESH__Mesh.html#afea0a21e6add08ac30f24f7dbbcae03b).

## ◆ calculatePlacement()

def draftgeoutils.geometry.calculatePlacement  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return a placement located in the center of gravity of the shape.
    
    If the given shape is planar, return a placement located at the center
    of gravity of the shape, and oriented towards the shape's normal.
    Otherwise, it returns a null placement.
    

References
[draftgeoutils.geometry.get_normal()](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a),
[draftgeoutils.geometry.getRotation()](../../d9/dfd/group__draftgeoutils.html#ga8b265d6e556f0015d0e732088d6ad1bd),
and
[draftgeoutils.geometry.is_planar()](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4).

## ◆ circleFrom1Circle2Lines()

def draftgeoutils.circles_incomplete.circleFrom1Circle2Lines  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _line1_ ,   
|  |  | _line2_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom3tan()](../../d9/dfd/group__draftgeoutils.html#gab90d3a9b019b4d0f39c114d577d94746).

## ◆ circlefrom1Circle2Points()

def draftgeoutils.circles_incomplete.circlefrom1Circle2Points  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _point1_ ,   
|  |  | _point2_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom1tan2pt()](../../d9/dfd/group__draftgeoutils.html#gadc534d3f5b90e09d807910b7200aaf8e).

## ◆ circlefrom1Line2Points()

def draftgeoutils.circles.circlefrom1Line2Points  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _p1_ ,   
|  |  | _p2_  
| ) | |   
      
    
    Return a list of circles created from an edge and two points.
    
    It calculates up to 2 possible centers.
    

References
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[draftgeoutils.general.edg()](../../d9/dfd/group__draftgeoutils.html#gad3f6b7a08027b908170525ef5b6da7fe),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.edges.findMidpoint()](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.circles_incomplete.circleFrom1tan2pt()](../../d9/dfd/group__draftgeoutils.html#gadc534d3f5b90e09d807910b7200aaf8e),
and
[draftgeoutils.circles.circlefrom2Lines1Point()](../../d9/dfd/group__draftgeoutils.html#gaaea4d08c6dcb36855768307bb5a70aa2).

## ◆ circleFrom1tan1pt1rad()

def draftgeoutils.circles_incomplete.circleFrom1tan1pt1rad  | ( |  | _tan1_ ,   
---|---|---|---  
|  |  | _p1_ ,   
|  |  | _rad_  
| ) | |   
      
    
    Circle from one tangent, one point, and radius.
    
    The tangents should be edges, and they may be either straight line edges
    or circular edges, so two combinations are possible.
    

References
[draftgeoutils.circles_incomplete.circleFromPointCircleRadius()](../../d9/dfd/group__draftgeoutils.html#gaf834e8dc620bf74d0f657cee946be020),
[draftgeoutils.circles.circleFromPointLineRadius()](../../d9/dfd/group__draftgeoutils.html#ga163b5f31d9b814e500670ab9cec198b5),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ circleFrom1tan2pt()

def draftgeoutils.circles_incomplete.circleFrom1tan2pt  | ( |  | _tan1_ ,   
---|---|---|---  
|  |  | _p1_ ,   
|  |  | _p2_  
| ) | |   
      
    
    Circle from one tangent and two points.
    
    The tangents should be edges, and they may be either straight line edges
    or circular edges, so two combinations are possible.
    

References
[draftgeoutils.circles_incomplete.circlefrom1Circle2Points()](../../d9/dfd/group__draftgeoutils.html#gabc04fff55820385b1ec052a8b3436869),
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ circleFrom2Circle1Lines()

def draftgeoutils.circles_incomplete.circleFrom2Circle1Lines  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _line_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom3tan()](../../d9/dfd/group__draftgeoutils.html#gab90d3a9b019b4d0f39c114d577d94746).

## ◆ circlefrom2Circles1Point()

def draftgeoutils.circles_incomplete.circlefrom2Circles1Point  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _point_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom2tan1pt()](../../d9/dfd/group__draftgeoutils.html#ga739b8b437d574830d1acad7cb9047214).

## ◆ circleFrom2CirclesRadius()

def draftgeoutils.circles_incomplete.circleFrom2CirclesRadius  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _radius_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom2tan1rad()](../../d9/dfd/group__draftgeoutils.html#ga6f89d6a8dd2947536982c3bb9c8eed9c).

## ◆ circlefrom2Lines1Point()

def draftgeoutils.circles.circlefrom2Lines1Point  | ( |  | _edge1_ ,   
---|---|---|---  
|  |  | _edge2_ ,   
|  |  | _point_  
| ) | |   
      
    
    Return a list of circles from two edges and one point.

References
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
and
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50).

Referenced by
[draftgeoutils.circles_incomplete.circleFrom2tan1pt()](../../d9/dfd/group__draftgeoutils.html#ga739b8b437d574830d1acad7cb9047214).

## ◆ circleFrom2LinesRadius()

def draftgeoutils.circles.circleFrom2LinesRadius  | ( |  | _edge1_ ,   
---|---|---|---  
|  |  | _edge2_ ,   
|  |  | _radius_  
| ) | |   
      
    
    Return a list of circles from two edges and one radius.
    
    It calculates 4 centers.
    

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.circles_incomplete.circleFrom2tan1rad()](../../d9/dfd/group__draftgeoutils.html#ga6f89d6a8dd2947536982c3bb9c8eed9c).

## ◆ circleFrom2PointsRadius()

def draftgeoutils.circles.circleFrom2PointsRadius  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_ ,   
|  |  | _radius_  
| ) | |   
      
    
    Return a list of circles from two points, and one radius.
    
    The two points must not be equal.
    
    It calculates up to 2 possible centers.
    

References
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[draftgeoutils.edges.findMidpoint()](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ circleFrom2tan1pt()

def draftgeoutils.circles_incomplete.circleFrom2tan1pt  | ( |  | _tan1_ ,   
---|---|---|---  
|  |  | _tan2_ ,   
|  |  | _point_  
| ) | |   
      
    
    Circle from two tangents and one point.
    
    The tangents should be edges, and they may be either straight line edges
    or circular edges, so four combinations are possible.
    

References
[draftgeoutils.circles_incomplete.circlefrom2Circles1Point()](../../d9/dfd/group__draftgeoutils.html#ga95351cd26522b90bec09fbae691fd0aa),
[draftgeoutils.circles.circlefrom2Lines1Point()](../../d9/dfd/group__draftgeoutils.html#gaaea4d08c6dcb36855768307bb5a70aa2),
[draftgeoutils.circles_incomplete.circlefromCircleLinePoint()](../../d9/dfd/group__draftgeoutils.html#ga7b123c7225945fa1c242f6680285ebe9),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ circleFrom2tan1rad()

def draftgeoutils.circles_incomplete.circleFrom2tan1rad  | ( |  | _tan1_ ,   
---|---|---|---  
|  |  | _tan2_ ,   
|  |  | _rad_  
| ) | |   
      
    
    Circle from two tangents and one radius.
    
    The tangents should be edges, and they may be either straight line edges
    or circular edges, so four combinations are possible.
    

References
[draftgeoutils.circles_incomplete.circleFrom2CirclesRadius()](../../d9/dfd/group__draftgeoutils.html#gaa0d28ff4ba28d9908f1da48ed4b2c6b5),
[draftgeoutils.circles.circleFrom2LinesRadius()](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734),
[draftgeoutils.circles_incomplete.circleFromCircleLineRadius()](../../d9/dfd/group__draftgeoutils.html#gace9f8dc5910c98dd016dbcebc0614b42),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ circleFrom3CircleTangents()

def draftgeoutils.circles_apollonius.circleFrom3CircleTangents  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _circle3_  
| ) | |   
      
    
    Return the circle that is tangent to three other circles.
    
    This problem is called the 'Problem of Appollonius'.
    
    A special case is that of 'Soddy circles'.
    
    To Do
    -----
    Currently not all possible solutions are found, only the Soddy circles.
    
    * Calc all 6 homothetic centers.
    * Create 3 lines from the inner and 4 from the outer h. center.
    * Calc. the 4 inversion poles of these lines for each circle.
    * Calc. the radical center of the 3 circles.
    * Calc. the intersection points (max. 8) of 4 lines (through each
      inversion pole and the radical center) with the circle.
    * This gives us all the tangent points.
    

References
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[draftgeoutils.circles_apollonius.innerSoddyCircle()](../../d9/dfd/group__draftgeoutils.html#ga37c8fad5fc27a46258f40cac81834d74),
and
[draftgeoutils.circles_apollonius.outerSoddyCircle()](../../d9/dfd/group__draftgeoutils.html#ga57eb2ca2e8dd69f6fb15182214e32b25).

Referenced by
[draftgeoutils.circles_incomplete.circleFrom3tan()](../../d9/dfd/group__draftgeoutils.html#gab90d3a9b019b4d0f39c114d577d94746).

## ◆ circleFrom3LineTangents()

def draftgeoutils.circles.circleFrom3LineTangents  | ( |  | _edge1_ ,   
---|---|---|---  
|  |  | _edge2_ ,   
|  |  | _edge3_  
| ) | |   
      
    
    Return a list of circles from three edges.
    
    It calculates up to 6 possible centers.
    

References
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1),
[draftgeoutils.general.v1()](../../d9/dfd/group__draftgeoutils.html#ga07ad5262ee7b26511c5c3592f2681804),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.circles_incomplete.circleFrom3tan()](../../d9/dfd/group__draftgeoutils.html#gab90d3a9b019b4d0f39c114d577d94746).

## ◆ circleFrom3tan()

def draftgeoutils.circles_incomplete.circleFrom3tan  | ( |  | _tan1_ ,   
---|---|---|---  
|  |  | _tan2_ ,   
|  |  | _tan3_  
| ) | |   
      
    
    Circle from three tangents.
    
    The tangents should be edges, and they may be either straight line edges
    or circular edges, so eight combinations are possible.
    

References
[draftgeoutils.circles_incomplete.circleFrom1Circle2Lines()](../../d9/dfd/group__draftgeoutils.html#ga6a079887c301407c3eecc974f988af7a),
[draftgeoutils.circles_incomplete.circleFrom2Circle1Lines()](../../d9/dfd/group__draftgeoutils.html#gae7a41f61a951cb4a0d0726d12364f411),
[draftgeoutils.circles_apollonius.circleFrom3CircleTangents()](../../d9/dfd/group__draftgeoutils.html#gae3f7f09b1882e00129fe07ddc74f21b8),
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ circlefromCircleLinePoint()

def draftgeoutils.circles_incomplete.circlefromCircleLinePoint  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _line_ ,   
|  |  | _point_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom2tan1pt()](../../d9/dfd/group__draftgeoutils.html#ga739b8b437d574830d1acad7cb9047214).

## ◆ circleFromCircleLineRadius()

def draftgeoutils.circles_incomplete.circleFromCircleLineRadius  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _line_ ,   
|  |  | _radius_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom2tan1rad()](../../d9/dfd/group__draftgeoutils.html#ga6f89d6a8dd2947536982c3bb9c8eed9c).

## ◆ circleFromPointCircleRadius()

def draftgeoutils.circles_incomplete.circleFromPointCircleRadius  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _circle_ ,   
|  |  | _radius_  
| ) | |   
      
    
    Do nothing. Placeholder function. Needs to be implemented.

Referenced by
[draftgeoutils.circles_incomplete.circleFrom1tan1pt1rad()](../../d9/dfd/group__draftgeoutils.html#gab7874bd264401d75b2ce61b2b49cfcbb).

## ◆ circleFromPointLineRadius()

def draftgeoutils.circles.circleFromPointLineRadius  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _edge_ ,   
|  |  | _radius_  
| ) | |   
      
    
    Return a list of circles from one point, one edge, and one radius.
    
    It calculates up to 2 possible centers.
    

References
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[DraftVecUtils.scaleTo()](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.circles_incomplete.circleFrom1tan1pt1rad()](../../d9/dfd/group__draftgeoutils.html#gab7874bd264401d75b2ce61b2b49cfcbb).

## ◆ circleInversion()

def draftgeoutils.circle_inversion.circleInversion  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _circle2_  
| ) | |   
      
    
    Circle inversion of a circle, inverting the center point.
    
    Returns the new circle created from the inverted center of circle2.
    

References
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[draftgeoutils.circle_inversion.pointInversion()](../../d9/dfd/group__draftgeoutils.html#ga2e9e5f6e50364165f9e6e1f8f5d5d8f8).

## ◆ cleanFaces()

def draftgeoutils.faces.cleanFaces  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Remove inner edges from coplanar faces.

References
[DraftVecUtils.find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
and
[draftgeoutils.faces.getBoundary()](../../d9/dfd/group__draftgeoutils.html#gaab4aa59fecdb2639faba56e457c3183e).

## ◆ cleanProjection()

def draftgeoutils.wires.cleanProjection  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _tessellate_ = `True`,   
|  |  | _seglength_ = `0.05`  
| ) | |   
      
    
    Return a compound of edges, optionally tessellate ellipses, splines
    and bezcurves.
    
    The function was formerly used to workaround bugs in the projection
    algorithm. These bugs have since been fixed. Now the function is only
    used when tessellation of ellipses, splines and bezcurves is required
    (DXF output and Draft_Shape2DView).
    

References
[draftgeoutils.wires.curvetowire()](../../d9/dfd/group__draftgeoutils.html#ga8b87ef4d82cdde505b429f85b838d062),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[draftgeoutils.edges.isLine](../../d9/dfd/group__draftgeoutils.html#ga87b8c31cd76d4e1b5ad8ddb578655e68).

## ◆ concatenate()

def draftgeoutils.faces.concatenate  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Turn several faces into one.

References
[draftgeoutils.faces.getBoundary()](../../d9/dfd/group__draftgeoutils.html#gaab4aa59fecdb2639faba56e457c3183e).

## ◆ connect()

def draftgeoutils.intersections.connect  | ( |  | _edges_ ,   
---|---|---|---  
|  |  | _closed_ = `False`  
| ) | |   
      
    
    Connect the edges in the given list by their intersections.

References
[DraftVecUtils.closest()](../../dc/dc3/group__DRAFTVECUTILS.html#ga8035ae4425c9330b9ba7a75ba7735749),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.edges.findMidpoint()](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

Referenced by
[Gui::Action.Action()](../../de/d94/classGui_1_1Action.html#ac1a6d356fe7379c35cec2227b543b323),
[Gui::ActionGroup.ActionGroup()](../../dc/d73/classGui_1_1ActionGroup.html#a9a79b117c1e0fb79885e6ea102dea468),
[Gui::ActionSelector.ActionSelector()](../../d1/db1/classGui_1_1ActionSelector.html#ac77b01768c1e5cde4e2f3015563c2a31),
[SpreadsheetGui::Workbench.activated()](../../d6/d95/classSpreadsheetGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced),
[StdCmdAlignment.activated()](../../df/d17/classStdCmdAlignment.html#a44409be4abd266d5d5e34dacb5484101),
[CmdTestProgress5.activated()](../../df/df0/classCmdTestProgress5.html#ad1d423187c49ef0fe01593ace22d177b),
[StdViewScreenShot.activated()](../../d9/da6/classStdViewScreenShot.html#a4229e4b93ce96f603dbfb3cdee194091),
[CmdSandboxEventLoop.activated()](../../dd/ddb/classCmdSandboxEventLoop.html#a1855363f3c57092086db6e6711015e01),
[CmdSandboxMeshLoader.activated()](../../db/d92/classCmdSandboxMeshLoader.html#a32745b05600acc57d5f7f75dbb0c8715),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.Activated()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac7fe745faef8d402397cb0641e130965),
[Mod.PartDesign.WizardShaft.WizardShaftTable.WizardShaftTable.addColumn()](../../dd/daa/classMod_1_1PartDesign_1_1WizardShaft_1_1WizardShaftTable_1_1WizardShaftTable.html#aa367ea0d077e7130ffde9a20dd1d8cc5),
[Gui::DockWindowManager.addDockWindow()](../../d9/d72/classGui_1_1DockWindowManager.html#a6f1aa2326f83c42f739260eeae1303ad),
[Gui::WorkbenchGroup.addTo()](../../d6/d6c/classGui_1_1WorkbenchGroup.html#a75c9e8681308f287a1127dfd9bf5f48e),
[Gui::UndoAction.addTo()](../../d8/da4/classGui_1_1UndoAction.html#a8014ce6ac366d584cb4521e0b1ff77da),
[Gui::RedoAction.addTo()](../../d6/dcb/classGui_1_1RedoAction.html#af9428e88d67789e960e4a6b53f3b05d2),
[Gui::DockWidgetAction.addTo()](../../d1/d3e/classGui_1_1DockWidgetAction.html#aedfa5668549a57eceee1aeaab1dfcf2d),
[Gui::ToolBarAction.addTo()](../../d5/da2/classGui_1_1ToolBarAction.html#a0ef60dd2fadc8731833b5c1f08fd83c8),
[Gui::WindowAction.addTo()](../../d1/dbf/classGui_1_1WindowAction.html#aa21a919268355a5eba4518595c7def22),
[Gui::MainWindow.addWindow()](../../d5/d2f/classGui_1_1MainWindow.html#abc89de4ead17780a1a857832c4b4ac4a),
[Gui::View3DInventorViewer.animatedViewAll()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a2dbbe5c4be1d9d305da9098e3ff06586),
[WebGui::BrowserView.BrowserView()](../../db/d47/classWebGui_1_1BrowserView.html#a82c10563f152e9af1f020d012c0f6ede),
[Gui::Dialog::DlgSettingsLazyLoadedImp.buildUnloadedWorkbenchList()](../../de/d4f/classGui_1_1Dialog_1_1DlgSettingsLazyLoadedImp.html#acc1e36963dc7e364ffc50df9ea31080a),
[Gui::ButtonGroup.ButtonGroup()](../../d2/d00/classGui_1_1ButtonGroup.html#a01a949d5b8864530b9d8ebe11fede460),
[Gui::CallTipsList.CallTipsList()](../../d0/d95/classGui_1_1CallTipsList.html#a184b70306641f6f3c30314d86efba580),
[Gui::Dialog::CameraDialog.CameraDialog()](../../d1/d6b/classGui_1_1Dialog_1_1CameraDialog.html#ac8c2bd62c58f37a54258e5e41bb8bbea),
[Gui::PythonConsole.changeEvent()](../../d2/da0/classGui_1_1PythonConsole.html#adce51573fd5c7e0c48aa63f4c1b954ac),
[MeshGui::CleanupHandler.CleanupHandler()](../../da/d87/classMeshGui_1_1CleanupHandler.html#ae6bf1c7470dbb74e1f22e1fa91cead63),
[Gui::ClearLineEdit.ClearLineEdit()](../../d0/de1/classGui_1_1ClearLineEdit.html#aaddf6367e0941d97458661e60e7bc32b),
[Gui::ColorButton.ColorButton()](../../dc/d1c/classGui_1_1ColorButton.html#a05fea219f75353e1ffd8a48c27a22624),
[ColorPickerPopup.ColorPickerPopup()](../../d2/da2/classColorPickerPopup.html#ac87f3be32750f5295804377bbbb197ef),
[Gui::DockWnd::ComboView.ComboView()](../../dc/dd3/classGui_1_1DockWnd_1_1ComboView.html#a4bb2ad428946ac056e664545bb93fd67),
[Gui::CommandIconView.CommandIconView()](../../d0/dae/classGui_1_1CommandIconView.html#a63f515c4930b29f78c2e5889ae6a47e8),
[Gui::Dialog::CommandView.CommandView()](../../d3/d65/classGui_1_1Dialog_1_1CommandView.html#acb7583a09d4eb20fd6371dcdd85f3650),
[Gui::CompletionList.CompletionList()](../../db/da5/classGui_1_1CompletionList.html#a7a9f1aa24d133e0140332eb166359f7e),
[Gui::PyResource.connect()](../../df/d89/classGui_1_1PyResource.html#a8647c48b114abe7532d68a1f2c2b52e5),
[FemGui::TaskDlgPost.connectSlots()](../../dc/d22/classFemGui_1_1TaskDlgPost.html#a861f961562edd6d1214f88e138976504),
[SketcherGui::ConstraintSettingsDialog.ConstraintSettingsDialog()](../../d7/dc6/classSketcherGui_1_1ConstraintSettingsDialog.html#abee7360633bbffabd342185a76975122),
[Gui::ContainerDialog.ContainerDialog()](../../d4/d00/classGui_1_1ContainerDialog.html#aa0692e347609def63eb0705da7bde9e1),
[Gui::TreeWidget.contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[WebGui::WebView.contextMenuEvent()](../../dd/dba/classWebGui_1_1WebView.html#a97e1557206a7d6256bb9623bb1d006da),
[ImageGui::ImageView.createActions()](../../d3/d75/classImageGui_1_1ImageView.html#a1a621d3c2f7a24512f9eeb8f2fda6abf),
[PartGui::PropertyEnumAttacherItem.createEditor()](../../dd/db5/classPartGui_1_1PropertyEnumAttacherItem.html#adc204e83a95e5e05516589cdf94e01f2),
[SpreadsheetGui::SpreadsheetDelegate.createEditor()](../../d7/da2/classSpreadsheetGui_1_1SpreadsheetDelegate.html#a13445f329d01b880b90145680187a0dd),
[Gui::PropertyEditor::PropertyItem.createExpressionEditor()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#a0d2497fd19db176a2f84f0332709a2e6),
[Gui::PropertyEditor::PropertyItem.createPropertyEditorWidget()](../../d6/db3/classGui_1_1PropertyEditor_1_1PropertyItem.html#ad85b0b41ae2d45f3be63d6f6d739e88f),
[Gui::SoFCColorGradient.customize()](../../d0/de7/classGui_1_1SoFCColorGradient.html#af1c20488dfa1c3ec77da20bc8caf30a9),
[Gui::Dialog::DemoMode.DemoMode()](../../d3/d05/classGui_1_1Dialog_1_1DemoMode.html#a9fee342162809308ebde24dc870dc069),
[PartGui::DimensionControl.DimensionControl()](../../d4/d40/classPartGui_1_1DimensionControl.html#af128386ee0190a20b578017f2d289388),
[PartDesignGui::DlgActiveBody.DlgActiveBody()](../../dc/dd5/classPartDesignGui_1_1DlgActiveBody.html#a286928f45731d5575f688ae3b871c67f),
[SpreadsheetGui::DlgBindSheet.DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[PartGui::DlgBooleanOperation.DlgBooleanOperation()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a9d9f1182519df949d604569a6a3e0f3d),
[Gui::Dialog::DlgCheckableMessageBox.DlgCheckableMessageBox()](../../d0/d87/classGui_1_1Dialog_1_1DlgCheckableMessageBox.html#a87bf1476a6657187fc1e55dea2c5f7e7),
[Gui::Dialog::DlgCreateNewPreferencePackImp.DlgCreateNewPreferencePackImp()](../../d8/d9e/classGui_1_1Dialog_1_1DlgCreateNewPreferencePackImp.html#a7dbb11da2fba28cc28eb564d84a94b59),
[Gui::Dialog::DlgCustomCommandsImp.DlgCustomCommandsImp()](../../d4/d52/classGui_1_1Dialog_1_1DlgCustomCommandsImp.html#adeabc4f425611bb6ef13764072620c92),
[Gui::Dialog::DlgCustomizeImp.DlgCustomizeImp()](../../d3/d3a/classGui_1_1Dialog_1_1DlgCustomizeImp.html#af4c47ca1eaaafb5027983955546ec086),
[Gui::Dialog::DlgCustomizeSpaceball.DlgCustomizeSpaceball()](../../d5/d50/classGui_1_1Dialog_1_1DlgCustomizeSpaceball.html#ab985f4a4ffc367712c73f2bf20166372),
[MeshGui::DlgEvaluateMeshImp.DlgEvaluateMeshImp()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a227fd7deeb9c1d8d1bfc3df0fdf04ebe),
[Gui::Dialog::DlgExpressionInput.DlgExpressionInput()](../../d5/d26/classGui_1_1Dialog_1_1DlgExpressionInput.html#aa41178b425873712e0c599430c5e79b8),
[PartGui::DlgFilletEdges.DlgFilletEdges()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a16463a511a5a288028ef96edb2b3aef6),
[Gui::Dialog::DlgGeneralImp.DlgGeneralImp()](../../df/ddc/classGui_1_1Dialog_1_1DlgGeneralImp.html#a3f63cf47d7d789edc9fe4bf8e69d3cb7),
[Gui::Dialog::DlgInputDialogImp.DlgInputDialogImp()](../../d2/d11/classGui_1_1Dialog_1_1DlgInputDialogImp.html#aa7a409caa0224a2b45479f029d578e9d),
[TechDrawGui::DlgPageChooser.DlgPageChooser()](../../de/d54/classTechDrawGui_1_1DlgPageChooser.html#acf24d9c7c983946e72efa810f6f0ed53),
[Gui::Dialog::DlgParameterImp.DlgParameterImp()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a43821f49385b7671bcef4e035a4e8ded),
[Gui::Dialog::DlgPreferencePackManagementImp.DlgPreferencePackManagementImp()](../../d0/d65/classGui_1_1Dialog_1_1DlgPreferencePackManagementImp.html#a8f2f7ecd1531283e9e2351a3d038dd29),
[Gui::Dialog::DlgPreferencesImp.DlgPreferencesImp()](../../db/dee/classGui_1_1Dialog_1_1DlgPreferencesImp.html#a37bb9a4c91c4fac35751e49f4b5862d5),
[TechDrawGui::DlgPrefsTechDrawAnnotationImp.DlgPrefsTechDrawAnnotationImp()](../../dc/dc6/classTechDrawGui_1_1DlgPrefsTechDrawAnnotationImp.html#a197023e8042b43e98001a2f29a81425c),
[TechDrawGui::DlgPrefsTechDrawScaleImp.DlgPrefsTechDrawScaleImp()](../../da/d6c/classTechDrawGui_1_1DlgPrefsTechDrawScaleImp.html#acc5e3e627455093efa497ff694e83f2e),
[PartGui::DlgPrimitives.DlgPrimitives()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a27827c66a9f047547fe0b7169251b97d),
[Gui::Dialog::DlgProjectInformationImp.DlgProjectInformationImp()](../../dc/d1b/classGui_1_1Dialog_1_1DlgProjectInformationImp.html#a63998183498977dda4fd0d0dbd62f8d8),
[Gui::Dialog::DlgPropertyLink.DlgPropertyLink()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#aa82aad5260433395c729b330ecc7ad88),
[Gui::Dialog::DlgRevertToBackupConfigImp.DlgRevertToBackupConfigImp()](../../d1/d47/classGui_1_1Dialog_1_1DlgRevertToBackupConfigImp.html#a46a46f1b5a9f676fed0a3a1d0055932d),
[PartGui::DlgRevolution.DlgRevolution()](../../d1/d83/classPartGui_1_1DlgRevolution.html#ad75370b34cc9b2f2ddb1439faa282f0d),
[Gui::Dialog::DlgRunExternal.DlgRunExternal()](../../d8/d36/classGui_1_1Dialog_1_1DlgRunExternal.html#a91407ea89e30579e1db2f4abba8c837d),
[Gui::Dialog::DlgSettingsCacheDirectory.DlgSettingsCacheDirectory()](../../df/dfb/classGui_1_1Dialog_1_1DlgSettingsCacheDirectory.html#a7ffd5b27feda47e68e7de9bc340ce064),
[Gui::Dialog::DlgSettingsDocumentImp.DlgSettingsDocumentImp()](../../d1/d93/classGui_1_1Dialog_1_1DlgSettingsDocumentImp.html#a0bcad72f09d441c73f71b3ce6cc34b02),
[FemGui::DlgSettingsFemElmerImp.DlgSettingsFemElmerImp()](../../db/db2/classFemGui_1_1DlgSettingsFemElmerImp.html#a28b3a7c7188a9db3053da7206bffbae5),
[FemGui::DlgSettingsFemZ88Imp.DlgSettingsFemZ88Imp()](../../d0/d44/classFemGui_1_1DlgSettingsFemZ88Imp.html#aa957307d31ac99d5e5e67eec5d889a68),
[SpreadsheetGui::DlgSheetConf.DlgSheetConf()](../../de/dca/classSpreadsheetGui_1_1DlgSheetConf.html#ae5a809ca03b0e1ead7ddcbe721aa1098),
[MeshGui::DlgSmoothing.DlgSmoothing()](../../d8/dcd/classMeshGui_1_1DlgSmoothing.html#ad4fe47f60c4b8b7b6e801050d2530403),
[Gui::Dialog::DlgUnitsCalculator.DlgUnitsCalculator()](../../d9/d79/classGui_1_1Dialog_1_1DlgUnitsCalculator.html#a39fcf3cbb021c22349f3d93712b613da),
[Gui::Dialog::DownloadItem.DownloadItem()](../../db/df8/classGui_1_1Dialog_1_1DownloadItem.html#a9e881969e28259033a1f38ab85dd0840),
[DrawingGui::DrawingView.DrawingView()](../../da/d65/classDrawingGui_1_1DrawingView.html#a19edc61e67a465cb0d4ceefd9c1b178d),
[Gui::EditorView.EditorView()](../../d4/d22/classGui_1_1EditorView.html#ae555ce1d01e06abd78b5b900fc23a689),
[Gui::Dialog::DlgCustomActionsImp.event()](../../df/dc6/classGui_1_1Dialog_1_1DlgCustomActionsImp.html#aa32494d6d46320c7c7dceaa7b6da1869),
[Gui::Dialog::CustomizeActionPage.event()](../../d2/dfe/classGui_1_1Dialog_1_1CustomizeActionPage.html#a694410445a7f5aae2c30f6cc7b4f7784),
[SketcherGui::EditDatumDialog.exec()](../../d6/d55/classSketcherGui_1_1EditDatumDialog.html#ae2acb3ba391ab2b817662e85aa8134fd),
[Inspection::Feature.execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Gui::ExpLineEdit.ExpLineEdit()](../../d0/d05/classGui_1_1ExpLineEdit.html#ac3c805bdb42ca010881b7f6cccf90b53),
[Gui::ExpressionLineEdit.ExpressionLineEdit()](../../d6/dad/classGui_1_1ExpressionLineEdit.html#a5d16941ac2121cc3fbe72d54cbc95b47),
[Gui::ExpressionSpinBox.ExpressionSpinBox()](../../d7/d1b/classGui_1_1ExpressionSpinBox.html#a23cbefefd650b90a3e89110cde09874f),
[Gui::ExpressionTextEdit.ExpressionTextEdit()](../../da/dc2/classGui_1_1ExpressionTextEdit.html#ab10ff944590e62d3a86670f0fd6baa13),
[WebGui::FcCookieJar.FcCookieJar()](../../da/d30/classWebGui_1_1FcCookieJar.html#a574284936a1d4a14e15688ef32e36583),
[Gui::FileChooser.FileChooser()](../../d3/de4/classGui_1_1FileChooser.html#a854c79b37cb7af0c6842644674ef911a),
[Gui::FileDialog.FileDialog()](../../de/d93/classGui_1_1FileDialog.html#a550b19b677605e277757831dd4dc0bec),
[Gui::FileOptionsDialog.FileOptionsDialog()](../../d9/daf/classGui_1_1FileOptionsDialog.html#a85790fe8e4be389bd9662175dd2418a9),
[PartGui::FilletEdgesDialog.FilletEdgesDialog()](../../d8/d3d/classPartGui_1_1FilletEdgesDialog.html#a6b828902ba284e2493c66e59b40a3126),
[SurfaceGui::FillingEdgePanel.FillingEdgePanel()](../../d0/d4b/classSurfaceGui_1_1FillingEdgePanel.html#ad5f51e59c3c41e37d49ddfe2b5f8dbf5),
[SurfaceGui::FillingPanel.FillingPanel()](../../d2/d79/classSurfaceGui_1_1FillingPanel.html#a1e4958b1ed6b6c8a6425f2740ffe96ef),
[SurfaceGui::FillingVertexPanel.FillingVertexPanel()](../../d3/d7b/classSurfaceGui_1_1FillingVertexPanel.html#a989f04062bb2b3767cbc08a2843219d9),
[SurfaceGui::GeomFillSurface.GeomFillSurface()](../../d0/d4b/classSurfaceGui_1_1GeomFillSurface.html#a9fa489d5e0c71de045c4afc8b76f0d5b),
[MeshGui::GmshWidget.GmshWidget()](../../d0/de7/classMeshGui_1_1GmshWidget.html#a2fa5f25b84aafafad640aa00ac1e6ed6),
[Gui::GraphicsScene.GraphicsScene()](../../da/d3c/classGui_1_1GraphicsScene.html#a5a6ac24fb693cce13e3d69c0c38311c9),
[Gui::GraphvizView.GraphvizView()](../../dd/d86/classGui_1_1GraphvizView.html#a1e46d2a16a77346e54d76e9b8db662f7),
[Gui::GUIApplication.GUIApplication()](../../d2/da0/classGui_1_1GUIApplication.html#af31500f9b43d60cb0a5eef50adbd3ca9),
[Gui::GUISingleApplication.GUISingleApplication()](../../df/d7d/classGui_1_1GUISingleApplication.html#afc4396a3639e30cff2825208c78f4358),
[Gui::ActionFunction.hover()](../../dd/d4d/classGui_1_1ActionFunction.html#a1f7a29a8396fe59079e703b41c0a1424),
[Gui::Dialog::IconDialog.IconDialog()](../../df/d34/classGui_1_1Dialog_1_1IconDialog.html#a324f1422dca435d0c8b68c3cee5450e9),
[Gui::Dialog::IconFolders.IconFolders()](../../d7/d06/classGui_1_1Dialog_1_1IconFolders.html#a42b57884d72ab74c4568c21e445ba446),
[ImageGui::ImageOrientationDialog.ImageOrientationDialog()](../../d0/dfa/classImageGui_1_1ImageOrientationDialog.html#a43eb1ba70580ecb00878cf46c92baf92),
[ImageGui::ImageView.ImageView()](../../d3/d75/classImageGui_1_1ImageView.html#aecd00c2699b113e2128509f5b96b49af),
[Gui::HttpServer.incomingConnection()](../../d6/d52/classGui_1_1HttpServer.html#ad7e436eb67b2c2a896d3d15013849fd8),
[Web::AppServer.incomingConnection()](../../dd/dd6/classWeb_1_1AppServer.html#a148ffeddf90c8e4e881937d36d8409a1),
[Gui::View3DInventorViewer.init()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a8688bb92e0dcb56b6b5ed7d095e07071),
[QSint::ActionGroup.init()](../../d4/da2/classQSint_1_1ActionGroup.html#a7e49dc9d1eae6e57672eed840213f720),
[CustomGLWidget.initializeGL()](../../d9/d9a/classCustomGLWidget.html#a5fec6c16b00b86be84b1682c2f8f7052),
[Gui::GuiNativeEvent.initSpaceball()](../../d6/d61/classGui_1_1GuiNativeEvent.html#aaca1647ae76006a032ef62f5eb99f858),
[TechDrawGui::TaskGeomHatch.initUi()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#acfee83bfb4690c933dc1f4149fd4c054),
[Gui::InputField.InputField()](../../da/dfa/classGui_1_1InputField.html#a4084d87bf2cb30ed76e8aa9fcda2a178),
[ColorPickerPopup.insertColor()](../../d2/da2/classColorPickerPopup.html#a03ffe41df98ef06f640d513d9604d7ec),
[Gui::LabelButton.LabelButton()](../../d0/dac/classGui_1_1LabelButton.html#a5a2961710d8b2479bce088995b8a48a9),
[Gui::LabelEditor.LabelEditor()](../../d1/d7e/classGui_1_1LabelEditor.html#ae8b18d3a2d345ed91bd7d69df408235f),
[Gui::PropertyEditor::LinkLabel.LinkLabel()](../../d5/d5f/classGui_1_1PropertyEditor_1_1LinkLabel.html#a40593aae60468379dc65a4604c406bd5),
[Gui::Dialog::DlgSettings3DViewImp.loadSettings()](../../df/d5c/classGui_1_1Dialog_1_1DlgSettings3DViewImp.html#a574045628488a5e5c1f565ebf2eebeec),
[Gui::Dialog::DlgSettingsNavigation.loadSettings()](../../d4/de0/classGui_1_1Dialog_1_1DlgSettingsNavigation.html#a535eb9332f21990bd1099737af28e64e),
[PartGui::Location.Location()](../../db/d6f/classPartGui_1_1Location.html#a2f77946d77e8f18590ccf3f7e73a18b4),
[Gui::LocationWidget.LocationWidget()](../../d9/d9a/classGui_1_1LocationWidget.html#a4a7a3f5156e1c2defce954bb3c171c27),
[PartGui::LoftWidget.LoftWidget()](../../dc/d7e/classPartGui_1_1LoftWidget.html#ada61696cbcfaf22bce2c5a8f61e6c259),
[Gui::MainWindow.MainWindow()](../../d5/d2f/classGui_1_1MainWindow.html#a84c74efa977302744093e2027b0dd801),
[TechDrawGui::MDIViewPage.MDIViewPage()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5bfb8fa1e3810804cd8c7607f97a996b),
[Gui::DAG::Model.Model()](../../df/d26/classGui_1_1DAG_1_1Model.html#a81b067d165657725e854c9ce8e038fec),
[TechDrawGui::QGIRichAnno.mouseDoubleClickEvent()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#ae314ffc101d4592c4a492f380ce72655),
[TechDrawGui::QGIViewAnnotation.mouseDoubleClickEvent()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#a0b2aec7a7e987b6deaca89c24d426c8d),
[Gui::View3DInventorViewer.moveCameraTo()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ace476aad217605a7e1cf968fac03d5f5),
[MRichTextEdit.MRichTextEdit()](../../d0/d27/classMRichTextEdit.html#af11103ab97f1027cfe3beffe3f65f860),
[NetworkAccessManager.NetworkAccessManager()](../../d2/da5/classNetworkAccessManager.html#a7e9623d8500e7e49ebb873b1ffebeb1d),
[Gui::NetworkRetriever.NetworkRetriever()](../../d9/d5c/classGui_1_1NetworkRetriever.html#a0c9cff617ab19b4b478a023ce6e0a102),
[draftgeoutils.offsets.offsetWire()](../../d9/dfd/group__draftgeoutils.html#ga05bacae1f1c67ceaba7aa1c37c8f758f),
[SketcherGui::TaskSketcherConstraints.on_settingsDialogButton_clicked()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#a4d5ce45a6132260502f7e5a2432f3f99),
[TechDrawGui::TaskWeldingSymbol.onArrowSymbolClicked()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ae759bf23081d3e3ac70606e57a49e294),
[TechDrawGui::TaskWeldingSymbol.onArrowSymbolCreateClicked()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a4966ce552885d9868a68fa5517c288cf),
[Gui::ColorButton.onChooseColor()](../../dc/d1c/classGui_1_1ColorButton.html#a0b9dcdf267ef00767b566b1d9cf93081),
[Gui::PropertyEditor::LinkLabel.onEditClicked()](../../d5/d5f/classGui_1_1PropertyEditor_1_1LinkLabel.html#a97d2305a39f48b6f29bd191e76b290f4),
[TechDrawGui::TaskRichAnno.onEditorClicked()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a62c804677b7b4120d7e1fd9b0ff33e27),
[Gui::Dialog::DlgGeneralImp.onManagePreferencePacksClicked()](../../df/ddc/classGui_1_1Dialog_1_1DlgGeneralImp.html#a76cd685953a05cdd52ea5da8402e02bc),
[TechDrawGui::TaskWeldingSymbol.onOtherSymbolClicked()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#ad97b852a309e26f2fcb1f17e25f4cbf7),
[TechDrawGui::TaskWeldingSymbol.onOtherSymbolCreateClicked()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a913a816b456e077890de8abb8b5a1e02),
[TechDrawGui::TaskLeaderLine.onTrackerClicked()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a581dcc144a5b4017a6356a89dda30abe),
[Gui::QuantitySpinBox.openFormulaDialog()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a859084d8696df9862149a6b8313e0b78),
[Gui::ExpressionSpinBox.openFormulaDialog()](../../d7/d1b/classGui_1_1ExpressionSpinBox.html#a1d92694d4771392035736efe5c2f67b4),
[MeshGui::ParametersDialog.ParametersDialog()](../../d1/de2/classMeshGui_1_1ParametersDialog.html#a2d4e91e1100f41f891b89ba9935927f1),
[Gui::Dialog::ParameterValue.ParameterValue()](../../de/d4f/classGui_1_1Dialog_1_1ParameterValue.html#ac7aafb3ec1611c190466e4b9a50e809c),
[Gui::Dialog::Placement.Placement()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a61902824aa6953c8333e8d319eab8374),
[FemGui::PlaneWidget.PlaneWidget()](../../dc/dc4/classFemGui_1_1PlaneWidget.html#ad277250040f2f1dbc27dfde2cd156abd),
[MeshGui::MeshSelection.prepareFreehandSelection()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a674ae82637715fe99543366702476e38),
[Gui::EditorView.printPreview()](../../d4/d22/classGui_1_1EditorView.html#a52ba77a828984888e75f26d9f643a3e0),
[Gui::GraphvizView.printPreview()](../../dd/d86/classGui_1_1GraphvizView.html#aaf236f756f37889b5a958a13e868e752),
[Gui::View3DInventor.printPreview()](../../da/d75/classGui_1_1View3DInventor.html#a5da15697fca08c2eb13d011a7c81b50a),
[DrawingGui::DrawingView.printPreview()](../../da/d65/classDrawingGui_1_1DrawingView.html#acc8da2cc918657759f026bc8059a1fa8),
[SpreadsheetGui::SheetView.printPreview()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#aa2180a26f766f9670935920c650c5e89),
[TechDrawGui::MDIViewPage.printPreview()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#aec77d926164ef873bc02001ec0741823),
[Gui::ProgressBar.ProgressBar()](../../d2/d04/classGui_1_1ProgressBar.html#a9586588b1dc98232192e6a1968f90389),
[Gui::ProgressDialog.ProgressDialog()](../../da/d21/classGui_1_1ProgressDialog.html#ad70c35376a195add86d0116006da95f2),
[SpreadsheetGui::PropertiesDialog.PropertiesDialog()](../../dc/d07/classSpreadsheetGui_1_1PropertiesDialog.html#a1a48a3dff37267c81257bf75efc33fdf),
[Gui::PropertyEditor::PropertyEditor.PropertyEditor()](../../d5/d10/classGui_1_1PropertyEditor_1_1PropertyEditor.html#a8251cd07cc94a95dec424eff43f9dd73),
[Gui::PropertyEditor::PropertyEditorWidget.PropertyEditorWidget()](../../db/d1c/classGui_1_1PropertyEditor_1_1PropertyEditorWidget.html#ad8dc9e4768013ec19777c40ff0217ea9),
[Gui::PropertyListEditor.PropertyListEditor()](../../db/d4e/classGui_1_1PropertyListEditor.html#ac1eb9b2008a8055999ae7436c543f62b),
[Gui::PropertyView.PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[Gui::PythonEditor.PythonEditor()](../../dd/dcb/classGui_1_1PythonEditor.html#aa2b73f626e3ff50a53c9f889d6199d08),
[Gui::PythonEditorView.PythonEditorView()](../../d9/df9/classGui_1_1PythonEditorView.html#ad9e910732552d72e9354823a2f7de483),
[TechDrawGui::QGILeaderLine.QGILeaderLine()](../../db/d57/classTechDrawGui_1_1QGILeaderLine.html#a0268c80bb2b5687e51f04494bbe8e73c),
[TechDrawGui::QGIViewBalloon.QGIViewBalloon()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#a2981a90aa8ad640bf0580ea0721ed059),
[TechDrawGui::QGIViewDimension.QGIViewDimension()](../../d1/d78/classTechDrawGui_1_1QGIViewDimension.html#a06db577baa69c3d61fd805220c6e4f5a),
[QtColorPicker.QtColorPicker()](../../dc/d28/classQtColorPicker.html#af310e90af6209605a8d408038344353c),
[Gui::QuantitySpinBox.QuantitySpinBox()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#adfbcde8a790f8c7c6a1fb22e9262f9f0),
[Gui::PythonConsole.readline()](../../d2/da0/classGui_1_1PythonConsole.html#a6c32ac8f0c5490de3bd5c015f107d1fb),
[Gui::Dialog::DlgGeneralImp.recreatePreferencePackMenu()](../../df/ddc/classGui_1_1Dialog_1_1DlgGeneralImp.html#ac16d857b8c49638342304cf2c7b7942b),
[Gui::RedoAction.RedoAction()](../../d6/dcb/classGui_1_1RedoAction.html#af788674aaba06ff8564220419707d710),
[Gui::Dialog::RedoDialog.RedoDialog()](../../d6/d1a/classGui_1_1Dialog_1_1RedoDialog.html#adbd0e41d05f1ce39b3115baf97df2701),
[MeshGui::RemoveComponentsDialog.RemoveComponentsDialog()](../../d1/d4b/classMeshGui_1_1RemoveComponentsDialog.html#a7c14afb1549f88f347f02043ba96b3e8),
[Gui::Application.runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::SearchBar.SearchBar()](../../d2/dc8/classGui_1_1SearchBar.html#a0ad58235edf9dac7e0512f08971205f3),
[PartGui::SectionCut.SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[SurfaceGui::SectionsPanel.SectionsPanel()](../../d0/dbd/classSurfaceGui_1_1SectionsPanel.html#accb447847d9edd4a29d28a152340b616),
[Gui::DockWnd::SelectionView.SelectionView()](../../d2/d84/classGui_1_1DockWnd_1_1SelectionView.html#a85f5eb827336b6aae75d40ffd609f23f),
[Gui::SelectModule.SelectModule()](../../d6/d0e/classGui_1_1SelectModule.html#a3282e9aadfac93c861ccef50787e8aed),
[Gui::Action.setCheckable()](../../de/d94/classGui_1_1Action.html#a0af06ded64fc2ee5f122a8bf7f11f001),
[Gui::ExpressionTextEdit.setDocumentObject()](../../da/dc2/classGui_1_1ExpressionTextEdit.html#a8a1f4c14350c98ac5a5842cea0cf2bdb),
[Gui::ExpressionLineEdit.setDocumentObject()](../../d6/dad/classGui_1_1ExpressionLineEdit.html#ae9878bcfd708b6eb3468b6cd4c9c8a58),
[DrawingGui::TaskOrthoViews.setPrimary()](../../d4/dd1/classDrawingGui_1_1TaskOrthoViews.html#a3fd4db79ad08f6cca0dbc6062c685795),
[TechDrawGui::TaskCenterLine.setUiConnect()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a5b174925f50709a6a5c452f261a00e8a),
[TechDrawGui::TaskSectionView.setUiEdit()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a43dc3542cf896d0778a028ae2be230ce),
[TechDrawGui::TaskCustomizeFormat.setUiEdit()](../../db/dde/classTechDrawGui_1_1TaskCustomizeFormat.html#a20843f7f5568b6ecfe6615b367235aea),
[TechDrawGui::TaskLeaderLine.setUiEdit()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a0eed6886711ee111f1ee0a8e314d6e21),
[TechDrawGui::TaskSectionView.setUiPrimary()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a07485a3822d8c672d6e4580fe4bf858c),
[Ui_DlgBindSheet.setupUi()](../../df/db8/classUi__DlgBindSheet.html#ae1de9958a07aa374f25d5afc0072b6ce),
[Ui_DlgExpressionInput.setupUi()](../../df/d80/classUi__DlgExpressionInput.html#a457d2e6db328642f33dc0ed8d432d7fe),
[Ui_DlgProcessorChooser.setupUi()](../../dc/d96/classUi__DlgProcessorChooser.html#a2fd70196d82e6c28a7f7a8796b0aa30d),
[Ui_DlgSheetConf.setupUi()](../../d2/dbc/classUi__DlgSheetConf.html#acd89621afc6e851f90e348646cae8376),
[Gui::Dialog::Ui_AboutApplication.setupUi()](../../d9/dbd/classGui_1_1Dialog_1_1Ui__AboutApplication.html#ad5236d2a4decd2be19bf6a6e7b91f177),
[Gui::Dialog::Ui_Clipping.setupUi()](../../d0/d63/classGui_1_1Dialog_1_1Ui__Clipping.html#ad64e28acf4947abcc82c63443b7e1513),
[Gui::Dialog::Ui_DemoMode.setupUi()](../../d9/d5a/classGui_1_1Dialog_1_1Ui__DemoMode.html#a5753631eb30017682a7a914576fe560a),
[Gui::Dialog::Ui_DlgActivateWindow.setupUi()](../../df/df5/classGui_1_1Dialog_1_1Ui__DlgActivateWindow.html#a3620f77e6b89f44006a884e775ddfbc3),
[Gui::Dialog::Ui_DlgAddProperty.setupUi()](../../d2/d44/classGui_1_1Dialog_1_1Ui__DlgAddProperty.html#ac703e61f60a754d1c26fafa00d3eca8b),
[Gui::Dialog::Ui_DlgCheckableMessageBox.setupUi()](../../d2/d5a/classGui_1_1Dialog_1_1Ui__DlgCheckableMessageBox.html#ac92ded949c9c99f699502fe1688bc04a),
[Gui::Dialog::Ui_DlgChooseIcon.setupUi()](../../d2/d80/classGui_1_1Dialog_1_1Ui__DlgChooseIcon.html#ac48511fe756965d96bac74ef0462cbf3),
[Gui::Dialog::Ui_DlgCreateNewPreferencePack.setupUi()](../../d6/d61/classGui_1_1Dialog_1_1Ui__DlgCreateNewPreferencePack.html#a04752a243a9b3b64f0435639c5ef5d7b),
[Gui::Dialog::Ui_DlgDisplayProperties.setupUi()](../../d1/d99/classGui_1_1Dialog_1_1Ui__DlgDisplayProperties.html#a9f17abd0ea4c50058afe95011c34cba6),
[Gui::Dialog::Ui_DlgInputDialog.setupUi()](../../df/de9/classGui_1_1Dialog_1_1Ui__DlgInputDialog.html#a6d2c132c5b7da1ba575ab0d81f13c657),
[Gui::Dialog::Ui_DlgMacroExecute.setupUi()](../../de/de8/classGui_1_1Dialog_1_1Ui__DlgMacroExecute.html#a954fa33a19856df1ce63dd0f06f177bf),
[Gui::Dialog::Ui_DlgMaterialProperties.setupUi()](../../d1/db6/classGui_1_1Dialog_1_1Ui__DlgMaterialProperties.html#aa0b1d97926e34ec576dfcb43690b5b13),
[Gui::Dialog::Ui_DlgParameterFind.setupUi()](../../d8/d0c/classGui_1_1Dialog_1_1Ui__DlgParameterFind.html#a478a87eaadbec79699ac63cece13ce05),
[Gui::Dialog::Ui_DlgPreferences.setupUi()](../../d8/d64/classGui_1_1Dialog_1_1Ui__DlgPreferences.html#ac2da2d63edceb118cd3d939ee1be5fec),
[Gui::Dialog::Ui_DlgProjectInformation.setupUi()](../../d5/dce/classGui_1_1Dialog_1_1Ui__DlgProjectInformation.html#a1b28c71aaab9490d2e0df33a6806d9a8),
[Gui::Dialog::Ui_DlgProjectUtility.setupUi()](../../dc/d4b/classGui_1_1Dialog_1_1Ui__DlgProjectUtility.html#a6912e4bbd11095cf226f3bd6bb3bf11f),
[Gui::Dialog::Ui_DlgPropertyLink.setupUi()](../../d2/d31/classGui_1_1Dialog_1_1Ui__DlgPropertyLink.html#a7c57fdf8d10124862623e7615cd2ce26),
[Gui::Dialog::Ui_DlgRevertToBackupConfig.setupUi()](../../d9/d2b/classGui_1_1Dialog_1_1Ui__DlgRevertToBackupConfig.html#a37dbdf9d17114a28cbac6cd1624f8678),
[Gui::Dialog::Ui_DlgSettingsColorGradient.setupUi()](../../d0/db6/classGui_1_1Dialog_1_1Ui__DlgSettingsColorGradient.html#a4f7a954efdaf867e898c61677dd6cb31),
[Gui::Dialog::Ui_DocumentRecovery.setupUi()](../../da/d7e/classGui_1_1Dialog_1_1Ui__DocumentRecovery.html#a9b49bc194582e1b945f563210fbb2cad),
[Gui::Dialog::Ui_InputVector.setupUi()](../../d3/db8/classGui_1_1Dialog_1_1Ui__InputVector.html#ae9cfd950d57d6abb829adfb282bf3a96),
[Gui::Dialog::Ui_MouseButtons.setupUi()](../../d4/df6/classGui_1_1Dialog_1_1Ui__MouseButtons.html#a0e2a4a4be875cd611ac323d668c16491),
[Gui::Dialog::Ui_Placement.setupUi()](../../dd/dec/classGui_1_1Dialog_1_1Ui__Placement.html#a2fa959981f443a2f50158129274a19ef),
[Gui::Dialog::Ui_SceneInspector.setupUi()](../../dc/d85/classGui_1_1Dialog_1_1Ui__SceneInspector.html#a8f935f968ef8a9f092693056e3ab7139),
[Gui::Ui_DlgTreeWidget.setupUi()](../../d7/d92/classGui_1_1Ui__DlgTreeWidget.html#a6b4b0f14db220550ac4f59352012eafa),
[Gui::Ui_VectorListEditor.setupUi()](../../d2/df3/classGui_1_1Ui__VectorListEditor.html#a0955e1e1fb37a4fd3455be50493ebee2),
[ImageGui::Ui_ImageOrientationDialog.setupUi()](../../dd/df2/classImageGui_1_1Ui__ImageOrientationDialog.html#a6b7b0dd17dea1ad2f07279af3371668a),
[InspectionGui::Ui_VisualInspection.setupUi()](../../d5/d6c/classInspectionGui_1_1Ui__VisualInspection.html#a5922c2bda03a715308a77eabf324012c),
[MeshGui::Ui_DlgEvaluateMesh.setupUi()](../../dc/da8/classMeshGui_1_1Ui__DlgEvaluateMesh.html#a9bf50a56d2917f90ab4660402afa434e),
[MeshGui::Ui_DlgEvaluateSettings.setupUi()](../../d2/d15/classMeshGui_1_1Ui__DlgEvaluateSettings.html#aa92deccda1777900883ff29277a16f0a),
[MeshGui::Ui_DlgRegularSolid.setupUi()](../../dc/ddd/classMeshGui_1_1Ui__DlgRegularSolid.html#aefa3f954d8df6946dec7281434bed9bf),
[MeshPartGui::Ui_CrossSections.setupUi()](../../df/d42/classMeshPartGui_1_1Ui__CrossSections.html#ab109cba2cf952680c6ffbfd00a60fd9b),
[PartDesignGui::Ui_DlgActiveBody.setupUi()](../../d2/d68/classPartDesignGui_1_1Ui__DlgActiveBody.html#a9cfae6673ff589cefd129fa674aa32f0),
[PartDesignGui::Ui_DlgReference.setupUi()](../../d8/d0c/classPartDesignGui_1_1Ui__DlgReference.html#a1916db5e6a58a6080e5a38b415cebd9c),
[PartGui::Ui_DlgPartBox.setupUi()](../../d4/db2/classPartGui_1_1Ui__DlgPartBox.html#ae3e6e66ce8f05f339894758a3ea02b40),
[PartGui::Ui_DlgPartCylinder.setupUi()](../../d9/d4f/classPartGui_1_1Ui__DlgPartCylinder.html#a8a598a90100e2b253ace879feb4a481a),
[PartGui::Ui_SectionCut.setupUi()](../../d1/daf/classPartGui_1_1Ui__SectionCut.html#af8c3ba2ebe75c6381dc22dd8561157b0),
[PartGui::Ui_ShapeFromMesh.setupUi()](../../d4/d56/classPartGui_1_1Ui__ShapeFromMesh.html#a5aab32dede1d6fb8089c7aa2b3dcefc0),
[Ui_PropertiesDialog.setupUi()](../../d9/d47/classUi__PropertiesDialog.html#a969aa82e87f1e84a945bfbc5a754a3e3),
[SketcherGui::Ui_InsertDatum.setupUi()](../../d1/d65/classSketcherGui_1_1Ui__InsertDatum.html#a00873ebd638a44aad1355d814e74edb4),
[SketcherGui::Ui_SketcherRegularPolygonDialog.setupUi()](../../d3/d6e/classSketcherGui_1_1Ui__SketcherRegularPolygonDialog.html#ab73d796a75224d5789e64c51b7090d75),
[SketcherGui::Ui_SketchMirrorDialog.setupUi()](../../d8/dbd/classSketcherGui_1_1Ui__SketchMirrorDialog.html#ae6d698acfedb90c3d9a292f660be3604),
[SketcherGui::Ui_SketchOrientationDialog.setupUi()](../../d5/dbf/classSketcherGui_1_1Ui__SketchOrientationDialog.html#a49a06c385d26b0f34e297c7e5c1d4967),
[SketcherGui::Ui_SketchRectangularArrayDialog.setupUi()](../../dc/dd2/classSketcherGui_1_1Ui__SketchRectangularArrayDialog.html#a55e846512aba53a16c843ef51afd1f46),
[TechDrawGui::Ui_DlgPageChooser.setupUi()](../../d1/dfa/classTechDrawGui_1_1Ui__DlgPageChooser.html#a3b4a81348d5bb58cdc1489466ad0f222),
[TechDrawGui::Ui_dlgTemplateField.setupUi()](../../d9/d04/classTechDrawGui_1_1Ui__dlgTemplateField.html#ace52655180765915067a2401c23df1dd),
[TechDrawGui::Ui_SymbolChooser.setupUi()](../../da/d4e/classTechDrawGui_1_1Ui__SymbolChooser.html#a12f6a9426a91233037ece40d460312e6),
[TestGui::Ui_UnitTest.setupUi()](../../de/d0f/classTestGui_1_1Ui__UnitTest.html#a002f4fb9944c5a9155c30a7249e846fa),
[FemGui::Ui_DlgSettingsFemCcxImp.setupUi()](../../d0/d8a/classFemGui_1_1Ui__DlgSettingsFemCcxImp.html#a315b201f1531fdff082da5a79bedd23d),
[FemGui::Ui_DlgSettingsFemElmerImp.setupUi()](../../de/dad/classFemGui_1_1Ui__DlgSettingsFemElmerImp.html#a89111a01c272cfbd76eeaeb038dece60),
[FemGui::Ui_DlgSettingsFemGeneralImp.setupUi()](../../d2/d8c/classFemGui_1_1Ui__DlgSettingsFemGeneralImp.html#ac2b5172e81dfdd499c8b781614e96065),
[FemGui::Ui_DlgSettingsFemGmshImp.setupUi()](../../d7/dc2/classFemGui_1_1Ui__DlgSettingsFemGmshImp.html#ae9a360d9f465c3ccd7ea857dceffc09b),
[FemGui::Ui_DlgSettingsFemMaterialImp.setupUi()](../../d4/db2/classFemGui_1_1Ui__DlgSettingsFemMaterialImp.html#a0fa92abddaedbb9cc604238e9ff38c41),
[FemGui::Ui_DlgSettingsFemMystranImp.setupUi()](../../d1/d8b/classFemGui_1_1Ui__DlgSettingsFemMystranImp.html#a072388dbb12259cef92d9732521fda97),
[FemGui::Ui_DlgSettingsFemZ88Imp.setupUi()](../../d1/dfa/classFemGui_1_1Ui__DlgSettingsFemZ88Imp.html#a38cffed6e14d1df4cd01d55b3de11da4),
[Gui::Dialog::Ui_DlgSettings3DView.setupUi()](../../d9/d45/classGui_1_1Dialog_1_1Ui__DlgSettings3DView.html#a01b50cbfcde5e9afe146696f2fe2a690),
[Gui::Dialog::Ui_DlgSettingsDocument.setupUi()](../../d4/d34/classGui_1_1Dialog_1_1Ui__DlgSettingsDocument.html#a4a29c75df54ae4a7a4eb6a2f4317ae37),
[Gui::Dialog::Ui_DlgSettingsImage.setupUi()](../../da/d58/classGui_1_1Dialog_1_1Ui__DlgSettingsImage.html#aec80b511eabddc7143dd99003926ed6b),
[Gui::Dialog::Ui_DlgSettingsMacro.setupUi()](../../d7/da4/classGui_1_1Dialog_1_1Ui__DlgSettingsMacro.html#a2b7b2e99a2c8dc39ac7469d60705e012),
[Gui::Dialog::Ui_DlgSettingsViewColor.setupUi()](../../d8/d30/classGui_1_1Dialog_1_1Ui__DlgSettingsViewColor.html#a74a229af5ab0a73a13549a9ea01b4399),
[Gui::TaskView::Ui_TaskAppearance.setupUi()](../../d8/dae/classGui_1_1TaskView_1_1Ui__TaskAppearance.html#a8d5ab65ab49607e10a0337dbeeb38b4e),
[MeshGui::Ui_DlgSettingsMeshView.setupUi()](../../db/dea/classMeshGui_1_1Ui__DlgSettingsMeshView.html#ac3a703c1411d53e7d61a7c4d79651d98),
[MeshGui::Ui_Segmentation.setupUi()](../../dc/df7/classMeshGui_1_1Ui__Segmentation.html#aba57ae10816d733fc03d185e05f23c7a),
[MeshPartGui::Ui_Tessellation.setupUi()](../../d3/d3c/classMeshPartGui_1_1Ui__Tessellation.html#afde4b69421106d698e7df710e5eb1776),
[PartDesignGui::Ui_TaskChamferParameters.setupUi()](../../d7/d5d/classPartDesignGui_1_1Ui__TaskChamferParameters.html#aec51000112c34d3783e3d09a1f174222),
[PartDesignGui::Ui_TaskLinearPatternParameters.setupUi()](../../d9/d7b/classPartDesignGui_1_1Ui__TaskLinearPatternParameters.html#acea28f230285c3d9ba9d2ce38e6d046e),
[PartDesignGui::Ui_TaskMirroredParameters.setupUi()](../../d8/dde/classPartDesignGui_1_1Ui__TaskMirroredParameters.html#a7f82a5904287aaa6709d4613b20f3c14),
[PartDesignGui::Ui_TaskMultiTransformParameters.setupUi()](../../d3/d21/classPartDesignGui_1_1Ui__TaskMultiTransformParameters.html#ae7d3b690dc401fc5435673c572c65188),
[PartDesignGui::Ui_TaskPipeOrientation.setupUi()](../../d6/dee/classPartDesignGui_1_1Ui__TaskPipeOrientation.html#a6ba828ff40d09ec868287c3d5eb99c90),
[PartDesignGui::Ui_TaskPipeScaling.setupUi()](../../d2/daa/classPartDesignGui_1_1Ui__TaskPipeScaling.html#a8eb9918a2ae1f72c1a7d52ee891fbd71),
[PartDesignGui::Ui_TaskPolarPatternParameters.setupUi()](../../da/d7d/classPartDesignGui_1_1Ui__TaskPolarPatternParameters.html#a70fd68f3ca03a789ca5a9985f78b26d1),
[PartGui::Ui_DlgPrimitives.setupUi()](../../d4/df2/classPartGui_1_1Ui__DlgPrimitives.html#a4a8c87f53af3139c460d79123afda78b),
[PartGui::Ui_DlgSettingsObjectColor.setupUi()](../../d4/d57/classPartGui_1_1Ui__DlgSettingsObjectColor.html#a1f055f20528a496dcf61b1204c21e7f5),
[SketcherGui::Ui_ConstraintMultiFilterDialog.setupUi()](../../db/d6d/classSketcherGui_1_1Ui__ConstraintMultiFilterDialog.html#ad8d12e87d2b5fc968ab0584286c60549),
[SketcherGui::Ui_ConstraintSettingsDialog.setupUi()](../../dc/d0f/classSketcherGui_1_1Ui__ConstraintSettingsDialog.html#ad015edebf98aa6abc8b9ff805bb12659),
[SketcherGui::Ui_SketcherSettingsDisplay.setupUi()](../../d4/de4/classSketcherGui_1_1Ui__SketcherSettingsDisplay.html#a8101196223bfcd64bd940b9eb1f0e544),
[Ui_TaskActiveView.setupUi()](../../d8/d51/classUi__TaskActiveView.html#a5cfcc5359aacba1b7f0f623af411a3e5),
[Ui_TaskHoleParameters.setupUi()](../../de/dc0/classUi__TaskHoleParameters.html#a03ebfd0561fdab141024e9e7a618cf98),
[TechDrawGui::Ui_DlgPrefsTechDrawDimensionsImp.setupUi()](../../dd/d85/classTechDrawGui_1_1Ui__DlgPrefsTechDrawDimensionsImp.html#a16610f9307a2b59d2ce4408d87eef348),
[TechDrawGui::Ui_TaskProjGroup.setupUi()](../../d0/dbc/classTechDrawGui_1_1Ui__TaskProjGroup.html#a2d50dcfe7e9125baed22364130fa233b),
[TechDrawGui::Ui_TaskRichAnno.setupUi()](../../d6/dc3/classTechDrawGui_1_1Ui__TaskRichAnno.html#a92554a147313bf89969e950191bd6b48),
[TechDrawGui::TaskProjGroup.setupViewCheckboxes()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a131cd5f853812c9378dad4b2b001fc7a),
[PartGui::ShapeBuilderWidget.ShapeBuilderWidget()](../../d8/d8d/classPartGui_1_1ShapeBuilderWidget.html#ab9755257c054ef099e882fa7d3fa5edb),
[SpreadsheetGui::SheetTableView.SheetTableView()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a635dd5f5a8cd9f534aa899320f7a4ba9),
[SpreadsheetGui::SheetView.SheetView()](../../d0/d67/classSpreadsheetGui_1_1SheetView.html#ad1aa4b1386fff9896ed1ecb74172b1a1),
[Gui::ControlSingleton.showDialog()](../../d6/d65/classGui_1_1ControlSingleton.html#a0b47653e251fa9b636d6f0f04f557020),
[Gui::TaskView::TaskView.showDialog()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#ac0735b0fa845999904ed189b3415d5d8),
[Gui::Dialog::AboutDialog.showLibraryInformation()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a5102f630fff98802fae8aa1b85f089ef),
[TechDrawGui::QGEPath.showMarkers()](../../d9/da7/classTechDrawGui_1_1QGEPath.html#a916b69472635ba66e9e8f01a76b8b540),
[Gui::StatusWidget.showText()](../../d4/dc3/classGui_1_1StatusWidget.html#ac14175ac4cd12acbd62122e5301cc4c6),
[SketcherGui::SketcherGeneralWidget.SketcherGeneralWidget()](../../da/d36/classSketcherGui_1_1SketcherGeneralWidget.html#ad8598af87de2e1edd3ee0b4d067f5575),
[SketcherGui::SketcherSettingsDisplay.SketcherSettingsDisplay()](../../d5/d61/classSketcherGui_1_1SketcherSettingsDisplay.html#ab3932b7244f54d92dda54b42278473ac),
[SketcherGui::SketchOrientationDialog.SketchOrientationDialog()](../../df/d09/classSketcherGui_1_1SketchOrientationDialog.html#a013086ee020255fad77cd5045fad3281),
[MeshGui::SmoothingDialog.SmoothingDialog()](../../d5/d32/classMeshGui_1_1SmoothingDialog.html#aa988ac7c2ed61883cc31859edf3249e2),
[FemGui::SphereWidget.SphereWidget()](../../d6/dfe/classFemGui_1_1SphereWidget.html#a71880b94214e186681351d0231a9bdde),
[Gui::ManualAlignment.startAlignment()](../../d7/d97/classGui_1_1ManualAlignment.html#adac18d1fdb3b8dce1361e26c9beba687),
[Gui::GUISingleApplication::Private.startServer()](../../de/d95/classGUISingleApplication_1_1Private.html#ad33dc4616092d90874986bc68ca3acde),
[TechDrawGui::TaskCosVertex.startTracker()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#adcadbd2d6bcbe75130b61754c78145ec),
[TechDrawGui::TaskLeaderLine.startTracker()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#ad1ddf147547e8cacbbd1d5a8e321155b),
[Gui::StdCmdDownloadOnlineHelp.StdCmdDownloadOnlineHelp()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#a646b366689fecc418bf3135926092d75),
[PartGui::SteppedSelection.SteppedSelection()](../../d8/da2/classPartGui_1_1SteppedSelection.html#a9d3141cac380fa50e5749a3ed9b90a6a),
[PartGui::SweepWidget.SweepWidget()](../../d0/dda/classPartGui_1_1SweepWidget.html#ac0ed74f687c9619b43f77dd722273c30),
[TechDrawGui::SymbolChooser.SymbolChooser()](../../d2/d51/classTechDrawGui_1_1SymbolChooser.html#a67d7962919c6a79d53b2285057e2a523),
[TechDrawGui::TaskAlignViews.TaskAlignViews()](../../d8/d23/classTechDrawGui_1_1TaskAlignViews.html#aea5d022e5e9edef8cba6f76e23327c20),
[PartGui::TaskAttacher.TaskAttacher()](../../df/d45/classPartGui_1_1TaskAttacher.html#ae3b7e331323f8a005efc1e55579240a6),
[TechDrawGui::TaskBalloon.TaskBalloon()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#a21f34d1bf15390ec9c984c7c75ab9996),
[PartDesignGui::TaskBooleanParameters.TaskBooleanParameters()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#afee7fbe402fa60d00581ce385bc8cb3c),
[PartDesignGui::TaskBoxPrimitives.TaskBoxPrimitives()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aee4936dd78a78c4d0f6fcc168d1a9c13),
[PartDesignGui::TaskChamferParameters.TaskChamferParameters()](../../d1/d5d/classPartDesignGui_1_1TaskChamferParameters.html#a30a85de6338f5d8a399de49cb4fe9014),
[PartGui::TaskCheckGeometryDialog.TaskCheckGeometryDialog()](../../dd/d83/classPartGui_1_1TaskCheckGeometryDialog.html#a1ea8f5354ec8cdf84523c2948270697f),
[TechDrawGui::TaskCosVertex.TaskCosVertex()](../../d4/d11/classTechDrawGui_1_1TaskCosVertex.html#a0f04c27182bc74d96638e6080dc44f91),
[FemGui::TaskCreateNodeSet.TaskCreateNodeSet()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#a1086e9019942d2317e5a5dc3285cb67e),
[TechDrawGui::TaskDetail.TaskDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a2017c373db55e0b43d386b536b34bc75),
[TechDrawGui::TaskDimension.TaskDimension()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#a01dec85a4db02858073f304508300ff3),
[PartDesignGui::TaskDlgPipeParameters.TaskDlgPipeParameters()](../../dc/d4b/classPartDesignGui_1_1TaskDlgPipeParameters.html#a35669d0c4d4603fe25093ae37da336c3),
[RobotGui::TaskDlgSimulate.TaskDlgSimulate()](../../da/d75/classRobotGui_1_1TaskDlgSimulate.html#ac112959f03da4004024fee05efc8315c),
[PartDesignGui::TaskDraftParameters.TaskDraftParameters()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#aafff6d5bd22406878791e8ccad20b907),
[RobotGui::TaskEdge2TracParameter.TaskEdge2TracParameter()](../../d0/dbf/classRobotGui_1_1TaskEdge2TracParameter.html#ae7d819ac74332bce0598fca6a9b79b78),
[PartDesignGui::TaskFeaturePick.TaskFeaturePick()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a6a91644eabfe77025b57d629f74ebbba),
[FemGui::TaskFemConstraint.TaskFemConstraint()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a7ea5bcd1fe75b787e72a2340fe5fa311),
[FemGui::TaskFemConstraintBearing.TaskFemConstraintBearing()](../../d5/d79/classFemGui_1_1TaskFemConstraintBearing.html#a5c48324835803c2f89e0c8a226dec9b0),
[FemGui::TaskFemConstraintContact.TaskFemConstraintContact()](../../d6/db7/classFemGui_1_1TaskFemConstraintContact.html#a45a74a3a2db13e3d87edba110a9fd7cd),
[FemGui::TaskFemConstraintDisplacement.TaskFemConstraintDisplacement()](../../d6/d75/classFemGui_1_1TaskFemConstraintDisplacement.html#ad9efd945714cedc7f6f182b3b811e089),
[FemGui::TaskFemConstraintFixed.TaskFemConstraintFixed()](../../df/db3/classFemGui_1_1TaskFemConstraintFixed.html#a7c338f2bd4c3f2e78a6b647ef4e103f7),
[FemGui::TaskFemConstraintFluidBoundary.TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1),
[FemGui::TaskFemConstraintForce.TaskFemConstraintForce()](../../d2/d46/classFemGui_1_1TaskFemConstraintForce.html#a3db3abe3cbf9a61635e1683630a55762),
[FemGui::TaskFemConstraintGear.TaskFemConstraintGear()](../../d9/d4d/classFemGui_1_1TaskFemConstraintGear.html#a9e613a0869b02375ab20ef330813dd1f),
[FemGui::TaskFemConstraintHeatflux.TaskFemConstraintHeatflux()](../../d9/dfb/classFemGui_1_1TaskFemConstraintHeatflux.html#a8e9e2cb04cc453f24e9d3ea5794cacc1),
[FemGui::TaskFemConstraintOnBoundary.TaskFemConstraintOnBoundary()](../../d5/df0/classFemGui_1_1TaskFemConstraintOnBoundary.html#a3690023aeffc09ab5ba3c8528abc6ce2),
[FemGui::TaskFemConstraintPlaneRotation.TaskFemConstraintPlaneRotation()](../../db/dc3/classFemGui_1_1TaskFemConstraintPlaneRotation.html#a8381f2d19ed24b3321d83ce4ff4f8257),
[FemGui::TaskFemConstraintPressure.TaskFemConstraintPressure()](../../dc/dd9/classFemGui_1_1TaskFemConstraintPressure.html#a00c65ac2686efb36884dcf8c6a10d76e),
[FemGui::TaskFemConstraintPulley.TaskFemConstraintPulley()](../../d3/d33/classFemGui_1_1TaskFemConstraintPulley.html#a0ae13b3d3671f9f5b94b36ca4f1bef14),
[FemGui::TaskFemConstraintSpring.TaskFemConstraintSpring()](../../d9/d3e/classFemGui_1_1TaskFemConstraintSpring.html#a0237d05805437799169e7d15e6c262fa),
[FemGui::TaskFemConstraintTemperature.TaskFemConstraintTemperature()](../../df/d19/classFemGui_1_1TaskFemConstraintTemperature.html#a33195abb4e64b5b8c79d39c7423d0a22),
[FemGui::TaskFemConstraintTransform.TaskFemConstraintTransform()](../../d9/d9b/classFemGui_1_1TaskFemConstraintTransform.html#aa2ff547501a5af38276cce0666c1920c),
[PartDesignGui::TaskFilletParameters.TaskFilletParameters()](../../db/d91/classPartDesignGui_1_1TaskFilletParameters.html#a6d39adf6b643a77ee3cecf31cdac126d),
[TechDrawGui::TaskGeomHatch.TaskGeomHatch()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a88302d91f72be3122a74e9d544792a4f),
[TechDrawGui::TaskHatch.TaskHatch()](../../d9/df5/classTechDrawGui_1_1TaskHatch.html#adceaa945f4f4d780e7aed8f01d0db366),
[QSint::TaskHeader.TaskHeader()](../../d8/dc5/classQSint_1_1TaskHeader.html#ae7222134f77c0fbdb3bde80f351377ab),
[PartDesignGui::TaskHoleParameters.TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662),
[TechDrawGui::TaskLeaderLine.TaskLeaderLine()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a873d04472b6a0de7f250ac13eef14913),
[PartDesignGui::TaskLinearPatternParameters.TaskLinearPatternParameters()](../../da/d31/classPartDesignGui_1_1TaskLinearPatternParameters.html#abeaf589b3a563a60ad122bf225528915),
[TechDrawGui::TaskLineDecor.TaskLineDecor()](../../d5/d87/classTechDrawGui_1_1TaskLineDecor.html#a0a15e804cb753e124bf7c356a1482a22),
[TechDrawGui::TaskLinkDim.TaskLinkDim()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#aed47f539a58e22dcbb1ae9c8b44a531d),
[PartDesignGui::TaskLoftParameters.TaskLoftParameters()](../../d3/dd7/classPartDesignGui_1_1TaskLoftParameters.html#ab30560915d7d39e4ff4d50b1befc36bf),
[PartDesignGui::TaskMirroredParameters.TaskMirroredParameters()](../../d8/d3c/classPartDesignGui_1_1TaskMirroredParameters.html#af2ea34bbd0c0cc40b561d9afcabcd5de),
[PartDesignGui::TaskMultiTransformParameters.TaskMultiTransformParameters()](../../d1/df7/classPartDesignGui_1_1TaskMultiTransformParameters.html#afe3826324b5f7c771d0deb67ac6fa26e),
[FemGui::TaskObjectName.TaskObjectName()](../../d3/d6b/classFemGui_1_1TaskObjectName.html#ae998f7ddece0813597d374c662db31b7),
[DrawingGui::TaskOrthoViews.TaskOrthoViews()](../../d4/dd1/classDrawingGui_1_1TaskOrthoViews.html#ae82943a42dfe2bfe1a72ace25e2ddb96),
[SandboxGui::TaskPanelView.TaskPanelView()](../../d1/d99/classSandboxGui_1_1TaskPanelView.html#a37051f4883eba702df09cf5086c3c0c4),
[PartDesignGui::TaskPipeOrientation.TaskPipeOrientation()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#ac6d362fde0b1452a942b513494180d97),
[PartDesignGui::TaskPipeParameters.TaskPipeParameters()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#ad8be386ff75b6d3c414ffbe505e48561),
[PartDesignGui::TaskPipeScaling.TaskPipeScaling()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#abec20e41dadf8a6f7e257d83647df874),
[Gui::Dialog::TaskPlacement.TaskPlacement()](../../d9/d06/classGui_1_1Dialog_1_1TaskPlacement.html#ad9461a81dc596c86eae056d3d75d3b64),
[PartDesignGui::TaskPolarPatternParameters.TaskPolarPatternParameters()](../../d7/d72/classPartDesignGui_1_1TaskPolarPatternParameters.html#a0b33e61ceed9292e29194dfeed883419),
[FemGui::TaskPostDataAlongLine.TaskPostDataAlongLine()](../../db/dfe/classFemGui_1_1TaskPostDataAlongLine.html#a63d24585168c09609383c5025fc02c61),
[FemGui::TaskPostDataAtPoint.TaskPostDataAtPoint()](../../d9/da7/classFemGui_1_1TaskPostDataAtPoint.html#a442bb680fc74fbe236c0415717eb94a4),
[TechDrawGui::TaskProjGroup.TaskProjGroup()](../../dd/d3c/classTechDrawGui_1_1TaskProjGroup.html#a81c03636578c0dd7befcb158dd86bc28),
[TechDrawGui::TaskRestoreLines.TaskRestoreLines()](../../d7/d3e/classTechDrawGui_1_1TaskRestoreLines.html#a9df3216f90a9df0e357b204a5ed9d852),
[TechDrawGui::TaskRichAnno.TaskRichAnno()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#acfd26140dce1c41560c4391c78b2fb06),
[RobotGui::TaskRobot6Axis.TaskRobot6Axis()](../../d8/d17/classRobotGui_1_1TaskRobot6Axis.html#a9276563f1d38045fd1fd074fb31ec380),
[PartDesignGui::TaskScaledParameters.TaskScaledParameters()](../../d2/d61/classPartDesignGui_1_1TaskScaledParameters.html#aeab97fa681f17c908d485e1cf9768516),
[TechDrawGui::TaskSectionView.TaskSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a146b65deaafcbc3d957c00e2814de9a1),
[SketcherGui::TaskSketcherConstraints.TaskSketcherConstraints()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#aa7c422db0a8955ac9e5214388be93a6d),
[SketcherGui::TaskSketcherElements.TaskSketcherElements()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a58295f4cd0ec5cf69b7c36cdf9c49e12),
[SketcherGui::TaskSketcherGeneral.TaskSketcherGeneral()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#acb35aefc057b31af4b7c6e9c87e1f0d4),
[SketcherGui::TaskSketcherMessages.TaskSketcherMessages()](../../d0/dc0/classSketcherGui_1_1TaskSketcherMessages.html#afbe205caa86a38f2afe97602838de648),
[MeshGui::TaskSmoothing.TaskSmoothing()](../../da/d50/classMeshGui_1_1TaskSmoothing.html#ab51dce40b8a4bd1bc653af4b18f6fda9),
[FemGui::TaskTetParameter.TaskTetParameter()](../../d9/d36/classFemGui_1_1TaskTetParameter.html#a29dc9ca508fcde30e91d9b0e306b34ce),
[PartDesignGui::TaskThicknessParameters.TaskThicknessParameters()](../../de/d75/classPartDesignGui_1_1TaskThicknessParameters.html#a43c1b021112c8995623c941d9d59a5ef),
[RobotGui::TaskTrajectory.TaskTrajectory()](../../d1/da4/classRobotGui_1_1TaskTrajectory.html#aaf520e286c3dbc0e533b6c0252a9c0ec),
[RobotGui::TaskTrajectoryDressUpParameter.TaskTrajectoryDressUpParameter()](../../dc/dba/classRobotGui_1_1TaskTrajectoryDressUpParameter.html#a291e8c4303c14a45405f67a846976168),
[TechDrawGui::TaskWeldingSymbol.TaskWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a5717b373a8983f626c7e976397803bd7),
[MeshPartGui::Tessellation.Tessellation()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#aa719fb5ab9267b9897d641cec0cb2177),
[Gui::TextEdit.TextEdit()](../../d2/dab/classGui_1_1TextEdit.html#a79f41f6d45955950885801c165464452),
[Gui::TextEditor.TextEditor()](../../de/d6e/classGui_1_1TextEditor.html#a01bf807b388aeb46fae36d32910eede0),
[Gui::ActionFunction.toggle()](../../dd/d4d/classGui_1_1ActionFunction.html#a4e13a0c393d502cf0db5be313cf641bd),
[Gui::DockWnd::ToolBox.ToolBox()](../../de/df3/classGui_1_1DockWnd_1_1ToolBox.html#ad186602a498d3a4d98a3da53ae581ef3),
[RobotGui::TrajectorySimulate.TrajectorySimulate()](../../d6/d2d/classRobotGui_1_1TrajectorySimulate.html#aff1b9df7981e9754bd422899e51b597d),
[Gui::Dialog::Transform.Transform()](../../d0/d8f/classGui_1_1Dialog_1_1Transform.html#a3180c0a9e13a3f7f8f3e2754d6136fe1),
[Gui::TreePanel.TreePanel()](../../da/d80/classGui_1_1TreePanel.html#aba64905ba98980da584f201e576dad88),
[Gui::TreeWidget.TreeWidget()](../../de/de0/classGui_1_1TreeWidget.html#a02ed96eef13cfa9307ee34d5c68ab7b6),
[Gui::ActionFunction.trigger()](../../dd/d4d/classGui_1_1ActionFunction.html#a1a0e3c8d4617ebc4a535ccadc8d7bcbb),
[Gui::UIntSpinBox.UIntSpinBox()](../../d3/ded/classGui_1_1UIntSpinBox.html#a7f163661526f09ae67eba8871518b1ee),
[Gui::UndoAction.UndoAction()](../../d8/da4/classGui_1_1UndoAction.html#aadec29d2d87c4b7666d7755d2941dc61),
[Gui::Dialog::UndoDialog.UndoDialog()](../../d6/d5d/classGui_1_1Dialog_1_1UndoDialog.html#a130fd4bd3cbfabb7b02c6aadcf516939),
[Gui::VectorListEditor.VectorListEditor()](../../d6/d5c/classGui_1_1VectorListEditor.html#ac93f557435a62159d7a3d877a06f7322),
[Gui::PropertyEditor::VectorListWidget.VectorListWidget()](../../de/d0d/classGui_1_1PropertyEditor_1_1VectorListWidget.html#acc893dc9e641f08eceda640b1ab9f306),
[Gui::DAG::View.View()](../../de/d24/classGui_1_1DAG_1_1View.html#a0c4a0810ba81a2cf65205ae283962cdc),
[Gui::View3DInventor.View3DInventor()](../../da/d75/classGui_1_1View3DInventor.html#ac60eed69033bfadaa166619bc01f8956),
[InspectionGui::VisualInspection.VisualInspection()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#aa13e595beac41fb1b077d794cd7fc0bc),
and
[Gui::WorkbenchComboBox.WorkbenchComboBox()](../../d9/df3/classGui_1_1WorkbenchComboBox.html#a87139b6992d2e792b8e9c14c903851ba).

## ◆ create_frames()

def draftgeoutils.geo_arrays.create_frames  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _places_  
| ) | |   
      
    
    Create the frames from the placements.

Referenced by
[draftgeoutils.geo_arrays.get_twisted_array_shape()](../../d9/dfd/group__draftgeoutils.html#gabd719361abde85a5f98618a9a8216578),
and
[draftgeoutils.geo_arrays.get_twisted_bridge_shape()](../../d9/dfd/group__draftgeoutils.html#ga69cf1ff30ffc570bcf54fde886dff1ca).

## ◆ curvetosegment()

def draftgeoutils.wires.curvetosegment  | ( |  | _curve_ ,   
---|---|---|---  
|  |  | _seglen_  
| ) | |   
      
    
    Discretize the curve and return a list of edges.

Referenced by
[draftgeoutils.wires.tessellateProjection()](../../d9/dfd/group__draftgeoutils.html#ga87448d4fa77c5a6539c47116c57bb6c8).

## ◆ curvetowire()

def draftgeoutils.wires.curvetowire  | ( |  | _obj_ ,   
---|---|---|---  
|  |  | _steps_  
| ) | |   
      
    
    Discretize the object and return a list of edges.

Referenced by
[draftgeoutils.wires.cleanProjection()](../../d9/dfd/group__draftgeoutils.html#gaeac487c387428b021095f192162bf91f).

## ◆ determinant()

def draftgeoutils.linear_algebra.determinant  | ( |  | _mat_ ,   
---|---|---|---  
|  |  | _n_  
| ) | |   
      
    
    Return the determinant of an N-matrix.
    
    It recursively expands the minors.
    

References
[draftgeoutils.linear_algebra.determinant()](../../d9/dfd/group__draftgeoutils.html#ga91c0ac559cf36a56537582afdbdd5164).

Referenced by
[draftgeoutils.linear_algebra.determinant()](../../d9/dfd/group__draftgeoutils.html#ga91c0ac559cf36a56537582afdbdd5164),
[OpenSCADUtils.isspecialorthogonal()](../../d4/d70/namespaceOpenSCADUtils.html#ab9920000389bbba48d6bcca154966cf0),
and
[Mod.Test.BaseTests.MatrixTestCase.testScale()](../../d3/d92/classMod_1_1Test_1_1BaseTests_1_1MatrixTestCase.html#ab11f517dcc07477537e9c579b6f05491).

## ◆ edg()

def draftgeoutils.general.edg  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_  
| ) | |   
      
    
    Return an edge from 2 vectors.

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

Referenced by
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50).

## ◆ fillet()

def draftgeoutils.fillets.fillet  | ( |  | _lEdges_ ,   
---|---|---|---  
|  |  | _r_ ,   
|  |  | _chamfer_ = `False`  
| ) | |   
      
    
    Return a list of sorted edges describing a round corner.
    
    Author: Jacques-Antoine Gaudin
    

References
[draftgeoutils.arcs.arcFrom2Pts()](../../d9/dfd/group__draftgeoutils.html#ga2d98ab13b2adf3a3eb6bdd1c559dbcb4),
and
[draftgeoutils.general.precision()](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38).

Referenced by
[PartGui::DlgFilletEdges.DlgFilletEdges()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a16463a511a5a288028ef96edb2b3aef6).

## ◆ filletWire()

def draftgeoutils.fillets.filletWire  | ( |  | _aWire_ ,   
---|---|---|---  
|  |  | _r_ ,   
|  |  | _chamfer_ = `False`  
| ) | |   
      
    
    Fillet each angle of a wire with r as radius.
    
    If chamfer is true, a `chamfer` is made instead, and `r` is the
    size of the chamfer.
    

References
[draftgeoutils.wires.isReallyClosed()](../../d9/dfd/group__draftgeoutils.html#gaefe28a41fe05def007e8f1fd6247f247).

Referenced by
[ArchRebar.makeRebar()](../../dd/de9/namespaceArchRebar.html#a4f9bf27bce35bf45fc8f02cfd5a8078d).

## ◆ find_plane()

def draftgeoutils.geometry.find_plane  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Find the plane containing the shape if possible.
    Use this function as a workaround due Part.Shape.findPlane
    fail to find plane on BSpline surfaces.

References
[draftgeoutils.geometry.get_spline_surface_normal()](../../d9/dfd/group__draftgeoutils.html#ga6c059568c5d0c2621c9644d99e6aef23),
and
[draftgeoutils.geometry.is_straight_line()](../../d9/dfd/group__draftgeoutils.html#gaca3c302955adc40b70eb1d12fc43c083).

Referenced by
[draftgeoutils.geometry.are_coplanar()](../../d9/dfd/group__draftgeoutils.html#ga6b2614cca55eba229be7f704b31d8701),
[draftgeoutils.geometry.get_normal()](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a),
and
[draftgeoutils.geometry.is_planar()](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4).

## ◆ findClosest()

def draftgeoutils.general.findClosest  | ( |  | _base_point_ ,   
---|---|---|---  
|  |  | _point_list_  
| ) | |   
      
    
    Find closest point in a list of points to the base point.
    
    Returns
    -------
    int
        An index from the list of points is returned.
    
    None
        If point_list is empty.
    

## ◆ findClosestCircle()

def draftgeoutils.circles.findClosestCircle  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _circles_  
| ) | |   
      
    
    Return the circle with closest center to a given point.

## ◆ findDistance()

def draftgeoutils.geometry.findDistance  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _edge_ ,   
|  |  | _strict_ = `False`  
| ) | |   
      
    
    Return a vector from the point to its closest point on the edge.
    
    If `strict` is `True`, the vector will be returned
    only if its endpoint lies on the `edge`.
    Edge can also be a list of 2 points.
    

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[DraftVecUtils.project()](../../dc/dc3/group__DRAFTVECUTILS.html#ga1bf889753387ffb78fb07cb90abed8bc),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
[draftgeoutils.circles.circleFromPointLineRadius()](../../d9/dfd/group__draftgeoutils.html#ga163b5f31d9b814e500670ab9cec198b5),
[draftgeoutils.geometry.findPerpendicular()](../../d9/dfd/group__draftgeoutils.html#ga57ea6e5088030f3848004e83d54b352b),
[draftgeoutils.geometry.mirror()](../../d9/dfd/group__draftgeoutils.html#ga5fcd07ec3396b34feeedf021c5c4ae51),
and
[draftgeoutils.circle_inversion.polarInversion()](../../d9/dfd/group__draftgeoutils.html#ga54bc622493ab5bc634b63a70f5fc7ef7).

## ◆ findEdge()

def draftgeoutils.edges.findEdge  | ( |  | _anEdge_ ,   
---|---|---|---  
|  |  | _aList_  
| ) | |   
      
    
    Return True if edge is found in list of edges.

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

## ◆ findHomotheticCenterOfCircles()

def draftgeoutils.circles.findHomotheticCenterOfCircles  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_  
| ) | |   
      
    
    Calculate the homothetic centers from two circles.
    
    Return None if the objects are not circles, or if they are concentric.
    
    http://en.wikipedia.org/wiki/Homothetic_center
    http://mathworld.wolfram.com/HomotheticCenter.html
    

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ findIntersection()

def draftgeoutils.intersections.findIntersection  | ( |  | _edge1_ ,   
---|---|---|---  
|  |  | _edge2_ ,   
|  |  | _infinite1_ = `False`,   
|  |  | _infinite2_ = `False`,   
|  |  | _ex1_ = `False`,   
|  |  | _ex2_ = `False`,   
|  |  | _dts_ = `True`,   
|  |  | _findAll_ = `False`  
| ) | |   
      
    
    Return a list containing the intersection points of 2 edges.
    
    You can also feed 4 points instead of `edge1` and `edge2`.
    If `dts` is used, `Shape.distToShape()` is used, which can be buggy.
    

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687),
[draftgeoutils.general.isPtOnEdge()](../../d9/dfd/group__draftgeoutils.html#gae92d2e4d632e3c28a4136c29eba58eb8),
[draftgeoutils.general.precision()](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50),
[draftgeoutils.circles.circleFrom2LinesRadius()](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734),
[draftgeoutils.circles_apollonius.circleFrom3CircleTangents()](../../d9/dfd/group__draftgeoutils.html#gae3f7f09b1882e00129fe07ddc74f21b8),
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
[draftgeoutils.intersections.connect()](../../d9/dfd/group__draftgeoutils.html#ga0b7c0fe418afd94ab4e966fe53b88960),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.circles.findRadicalCenter()](../../d9/dfd/group__draftgeoutils.html#gaa0f8671fa707fb91a37636f9d9fdf2fe),
[draftgeoutils.circles.getCircleFromSpline()](../../d9/dfd/group__draftgeoutils.html#gacde5b7f0b59d56ae852c77f40889913e),
and
[draftgeoutils.intersections.wiresIntersect()](../../d9/dfd/group__draftgeoutils.html#ga5e7ce6b0591a23ad098be94b4c64dd67).

## ◆ findMidpoint()

def draftgeoutils.edges.findMidpoint  | ( |  | _edge_| ) |   
---|---|---|---|---|---  
      
    
    Return the midpoint of an edge.

Referenced by
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50),
[draftgeoutils.circles.circleFrom2PointsRadius()](../../d9/dfd/group__draftgeoutils.html#gac5ca6e04d961e3751606a1e4ccf378b4),
[draftgeoutils.intersections.connect()](../../d9/dfd/group__draftgeoutils.html#ga0b7c0fe418afd94ab4e966fe53b88960),
[draftgeoutils.edges.invert()](../../d9/dfd/group__draftgeoutils.html#ga60dc82b8b95b16ffa97e1ccd715f099e),
[draftgeoutils.sort_edges.sortEdgesOld()](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3),
[draftgeoutils.wires.superWire()](../../d9/dfd/group__draftgeoutils.html#ga55c4d57190f5e47bd7026e379d49fd01),
and
[OpenSCAD2Dgeom.superWireReverse()](../../d0/dac/namespaceOpenSCAD2Dgeom.html#a1e11ac08bf2860f0914761e15eb4bc0d).

## ◆ findPerpendicular()

def draftgeoutils.geometry.findPerpendicular  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _edgeslist_ ,   
|  |  | _force_ = `None`  
| ) | |   
      
    
    Find the perpendicular distance between a point and a list of edges.
    
    If force is specified, only the edge[force] will be considered,
    and it will be considered infinite.
    
    Returns
    -------
    [vector_from_point_to_closest_edge, edge_index]
        The vector and the index in the list.
    
    None
        If no perpendicular vector could be found.
    

References
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca).

## ◆ findRadicalAxis()

def draftgeoutils.circles.findRadicalAxis  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_  
| ) | |   
      
    
    Calculate the radical axis of two circles.
    
    On the radical axis (also called power line) of two circles any
    tangents drawn from a point on the axis to both circles have
    the same length.
    
    http://en.wikipedia.org/wiki/Radical_axis
    http://mathworld.wolfram.com/RadicalLine.html
    
    See Also
    --------
    findRadicalCenter
    

References
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

Referenced by
[draftgeoutils.circles.findRadicalCenter()](../../d9/dfd/group__draftgeoutils.html#gaa0f8671fa707fb91a37636f9d9fdf2fe).

## ◆ findRadicalCenter()

def draftgeoutils.circles.findRadicalCenter  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _circle3_  
| ) | |   
      
    
    Calculate the radical center of three circles.
    
    It is also called the power center.
    It is the intersection point of the three radical axes of the pairs
    of circles.
    
    http://en.wikipedia.org/wiki/Power_center_(geometry)
    http://mathworld.wolfram.com/RadicalCenter.html
    
    See Also
    --------
    findRadicalAxis
    

References
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.circles.findRadicalAxis()](../../d9/dfd/group__draftgeoutils.html#gace97041b9159300c6ca150e0373b274c),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ findWires()

def draftgeoutils.wires.findWires  | ( |  | _edgeslist_| ) |   
---|---|---|---|---|---  
      
    
    Find wires in a list of edges.

## ◆ findWiresOld()

def draftgeoutils.wires.findWiresOld  | ( |  | _edges_| ) |   
---|---|---|---|---|---  
      
    
    Return a list of lists containing edges that can be connected.
    
    Find connected edges in the list.
    

## ◆ findWiresOld2()

def draftgeoutils.wires.findWiresOld2  | ( |  | _edgeslist_| ) |   
---|---|---|---|---|---  
      
    
    Find connected wires in the given list of edges.

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

## ◆ flattenWire()

def draftgeoutils.wires.flattenWire  | ( |  | _wire_| ) |   
---|---|---|---|---|---  
      
    
    Force a wire to get completely flat along its normal.

References
[draftgeoutils.geometry.get_normal()](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a),
and
[WorkingPlane.plane](../../d8/d4a/namespaceWorkingPlane.html#acd818647b5d80bd53b91ee7d60184f68).

## ◆ geomType()

def draftgeoutils.general.geomType  | ( |  | _edge_| ) |   
---|---|---|---|---|---  
      
    
    Return the type of geometry this edge is based on.

Referenced by
[draftgeoutils.intersections.angleBisection()](../../d9/dfd/group__draftgeoutils.html#ga692ff72eee5139e832fb1fc6f5ee949e),
[draftgeoutils.arcs.arcFromSpline()](../../d9/dfd/group__draftgeoutils.html#ga1fb3e4463c835a04a0bd4e060f2fd6f4),
[TechDraw::CenterLine.CenterLineBuilder()](../../d5/dd5/classTechDraw_1_1CenterLine.html#a0669426226ba9f14e5509c484b3ee6c8),
[draftgeoutils.circles_incomplete.circleFrom1tan1pt1rad()](../../d9/dfd/group__draftgeoutils.html#gab7874bd264401d75b2ce61b2b49cfcbb),
[draftgeoutils.circles_incomplete.circleFrom1tan2pt()](../../d9/dfd/group__draftgeoutils.html#gadc534d3f5b90e09d807910b7200aaf8e),
[draftgeoutils.circles_incomplete.circleFrom2tan1pt()](../../d9/dfd/group__draftgeoutils.html#ga739b8b437d574830d1acad7cb9047214),
[draftgeoutils.circles_incomplete.circleFrom2tan1rad()](../../d9/dfd/group__draftgeoutils.html#ga6f89d6a8dd2947536982c3bb9c8eed9c),
[draftgeoutils.circles_apollonius.circleFrom3CircleTangents()](../../d9/dfd/group__draftgeoutils.html#gae3f7f09b1882e00129fe07ddc74f21b8),
[draftgeoutils.circles_incomplete.circleFrom3tan()](../../d9/dfd/group__draftgeoutils.html#gab90d3a9b019b4d0f39c114d577d94746),
[draftgeoutils.circle_inversion.circleInversion()](../../d9/dfd/group__draftgeoutils.html#gaf83de47d0b318d570f1ca51dcc9cbefb),
[draftgeoutils.wires.cleanProjection()](../../d9/dfd/group__draftgeoutils.html#gaeac487c387428b021095f192162bf91f),
[draftgeoutils.intersections.connect()](../../d9/dfd/group__draftgeoutils.html#ga0b7c0fe418afd94ab4e966fe53b88960),
[draftobjects.hatch.Hatch.execute()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a45ad2594fc7bca672c66825886114e19),
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[draftgeoutils.circles.findHomotheticCenterOfCircles()](../../d9/dfd/group__draftgeoutils.html#ga8a2f5385b2e75457e5b317f7ba170816),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.circles.findRadicalAxis()](../../d9/dfd/group__draftgeoutils.html#gace97041b9159300c6ca150e0373b274c),
[draftgeoutils.circles.findRadicalCenter()](../../d9/dfd/group__draftgeoutils.html#gaa0f8671fa707fb91a37636f9d9fdf2fe),
[draftgeoutils.wires.get_extended_wire()](../../d9/dfd/group__draftgeoutils.html#gae6d8e69cb869af3d1824fd750b93db3f),
[draftgeoutils.circles.getCircleFromSpline()](../../d9/dfd/group__draftgeoutils.html#gacde5b7f0b59d56ae852c77f40889913e),
[TechDrawGui::TaskAlignViews.getSelectedEdges()](../../d8/d23/classTechDrawGui_1_1TaskAlignViews.html#a748566d07ecc0ca6df66f78ceca681a5),
[draftgeoutils.edges.getTangent()](../../d9/dfd/group__draftgeoutils.html#gade4f4721afcac4eb74bbb38729e6b2c6),
[draftgeoutils.circles_apollonius.innerSoddyCircle()](../../d9/dfd/group__draftgeoutils.html#ga37c8fad5fc27a46258f40cac81834d74),
[draftgeoutils.edges.invert()](../../d9/dfd/group__draftgeoutils.html#ga60dc82b8b95b16ffa97e1ccd715f099e),
[draftgeoutils.arcs.isClockwise()](../../d9/dfd/group__draftgeoutils.html#gacc819a72923773e1ec59cf14f2f87f78),
[draftgeoutils.cuboids.isCubic()](../../d9/dfd/group__draftgeoutils.html#ga8f0c24d453468e6cc90a97fd8ae93344),
[draftgeoutils.arcs.isWideAngle()](../../d9/dfd/group__draftgeoutils.html#gabfa0e00bb4a08ea5b20fd7be3650aa96),
[TechDraw::DrawUtil.makeGeomName()](../../da/d23/classTechDraw_1_1DrawUtil.html#a2087370c9faad8dcde61cdcd11ce2585),
[TechDraw::DrawDimHelper.minMax()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#abab3e90e8c9a8343306e4ecf0c1c64f4),
[draftgeoutils.offsets.offset()](../../d9/dfd/group__draftgeoutils.html#gad4289006425ada5bfb41c50dd60c7b98),
[draftgeoutils.circles_apollonius.outerSoddyCircle()](../../d9/dfd/group__draftgeoutils.html#ga57eb2ca2e8dd69f6fb15182214e32b25),
[draftgeoutils.circle_inversion.pointInversion()](../../d9/dfd/group__draftgeoutils.html#ga2e9e5f6e50364165f9e6e1f8f5d5d8f8),
[draftgeoutils.circle_inversion.polarInversion()](../../d9/dfd/group__draftgeoutils.html#ga54bc622493ab5bc634b63a70f5fc7ef7),
[SMESH_MeshEditor.Reorient()](../../da/d31/classSMESH__MeshEditor.html#a477b85a8240f43fc88b4fc6cb65bb6b0),
[SMDS_MeshInfo.setNb()](../../dd/dc8/classSMDS__MeshInfo.html#ac7fe6c4f8517b41ff4fdd8ae038cc741),
[draftgeoutils.sort_edges.sortEdgesOld()](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3),
[SMESH_MeshEditor.SplitVolumes()](../../da/d31/classSMESH__MeshEditor.html#a616276fed28187dfe20f73b637a883b1),
[draftgeoutils.wires.superWire()](../../d9/dfd/group__draftgeoutils.html#ga55c4d57190f5e47bd7026e379d49fd01),
[TechDrawGui::TaskCenterLine.TaskCenterLine()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a5b942888fa00c64e72a692710da1d65f),
[draftgeoutils.wires.tessellateProjection()](../../d9/dfd/group__draftgeoutils.html#ga87448d4fa77c5a6539c47116c57bb6c8),
[SMDS_MeshCell.toSmdsType()](../../d5/d2e/classSMDS__MeshCell.html#acc308be09df11165c672f1c67a2db00c),
and
[SMESH_MeshEditor.Transform()](../../da/d31/classSMESH__MeshEditor.html#af68382363ee35caa32c88acfe7f5dea7).

## ◆ get_extended_wire()

def draftgeoutils.wires.get_extended_wire  | ( |  | _wire_ ,   
---|---|---|---  
|  |  | _offset_start_ ,   
|  |  | _offset_end_  
| ) | |   
      
    
    Return a wire trimmed (negative offset) or extended (positive offset) at its first vertex, last vertex or both ends. 
    
    get_extended_wire(wire, -100.0, 0.0) -> returns a copy of the wire with its first 100 mm removed
    get_extended_wire(wire, 0.0, 100.0) -> returns a copy of the wire extended by 100 mm after it's last vertex
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[draftgeoutils.wires.get_extended_wire()](../../d9/dfd/group__draftgeoutils.html#gae6d8e69cb869af3d1824fd750b93db3f),
and
[draftgeoutils.general.precision()](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38).

Referenced by
[draftgeoutils.wires.get_extended_wire()](../../d9/dfd/group__draftgeoutils.html#gae6d8e69cb869af3d1824fd750b93db3f).

## ◆ get_init_values()

def draftgeoutils.geo_arrays.get_init_values  | ( |  | _path_ ,   
---|---|---|---  
|  |  | _count_ = `6`  
| ) | |   
      
    
    Set values needed to create the array.

Referenced by
[draftgeoutils.geo_arrays.get_twisted_placements()](../../d9/dfd/group__draftgeoutils.html#ga9c5399869f1738ac24d9b6923a84c992).

## ◆ get_n_params()

def draftgeoutils.geo_arrays.get_n_params  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _number_ ,   
|  |  | _step_ ,   
|  |  | _norm_  
| ) | |   
      
    
    Get the parameters needed in each iteration.

Referenced by
[draftgeoutils.geo_arrays.get_twisted_placements()](../../d9/dfd/group__draftgeoutils.html#ga9c5399869f1738ac24d9b6923a84c992).

## ◆ get_normal()

def draftgeoutils.geometry.get_normal  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Find the normal of a shape or list of points, if possible.

References
[draftgeoutils.geometry.find_plane()](../../d9/dfd/group__draftgeoutils.html#ga2255544d596f3dbaa5423bb67f78f69d),
and
[draftgeoutils.geometry.is_straight_line()](../../d9/dfd/group__draftgeoutils.html#gaca3c302955adc40b70eb1d12fc43c083).

Referenced by
[draftgeoutils.geometry.calculatePlacement()](../../d9/dfd/group__draftgeoutils.html#gaadbede2965a30dff070b48848d7b4423),
[draftgeoutils.wires.flattenWire()](../../d9/dfd/group__draftgeoutils.html#ga8106baec211f8a64f5317e2287152a7b),
and
[draftgeoutils.offsets.offsetWire()](../../d9/dfd/group__draftgeoutils.html#ga05bacae1f1c67ceaba7aa1c37c8f758f).

## ◆ get_placement_perpendicular_to_wire()

def draftgeoutils.wires.get_placement_perpendicular_to_wire  | ( |  | _wire_| ) |   
---|---|---|---|---|---  
      
    
    Return the placement whose base is the wire's first vertex and it's z axis aligned to the wire's tangent.

## ◆ get_referenced_edges()

def draftgeoutils.edges.get_referenced_edges  | ( |  | _property_value_| ) |   
---|---|---|---|---|---  
      
    
    Return the Edges referenced by the value of a App:PropertyLink, App::PropertyLinkList,
       App::PropertyLinkSub or App::PropertyLinkSubList property.

## ◆ get_spline_normal()

def draftgeoutils.geometry.get_spline_normal  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Find the normal of a BSpline edge.

References
[draftgeoutils.geometry.is_straight_line()](../../d9/dfd/group__draftgeoutils.html#gaca3c302955adc40b70eb1d12fc43c083).

## ◆ get_spline_surface_normal()

def draftgeoutils.geometry.get_spline_surface_normal  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Check if shape formed by BSpline surfaces is planar and get normal.
    If shape is not planar return None.

Referenced by
[draftgeoutils.geometry.find_plane()](../../d9/dfd/group__draftgeoutils.html#ga2255544d596f3dbaa5423bb67f78f69d).

## ◆ get_twisted_array_shape()

def draftgeoutils.geo_arrays.get_twisted_array_shape  | ( |  | _base_ ,   
---|---|---|---  
|  |  | _path_ ,   
|  |  | _count_ = `15`,   
|  |  | _rot_factor_ = `0.25`  
| ) | |   
      
    
    Get the twisted array shape as a compound.

References
[draftgeoutils.geo_arrays.create_frames()](../../d9/dfd/group__draftgeoutils.html#gaa1ce2d95483e22c1ce443616586702c6),
and
[draftgeoutils.geo_arrays.get_twisted_placements()](../../d9/dfd/group__draftgeoutils.html#ga9c5399869f1738ac24d9b6923a84c992).

## ◆ get_twisted_bridge_shape()

def draftgeoutils.geo_arrays.get_twisted_bridge_shape  | ( |  | _base_ ,   
---|---|---|---  
|  |  | _path_ ,   
|  |  | _count_ = `15`,   
|  |  | _rot_factor_ = `0.25`,   
|  |  | _width_ = `100`,   
|  |  | _thickness_ = `10`  
| ) | |   
      
    
    Get the twisted bridge array shape as a compound.

References
[draftgeoutils.geo_arrays.create_frames()](../../d9/dfd/group__draftgeoutils.html#gaa1ce2d95483e22c1ce443616586702c6),
[draftgeoutils.geo_arrays.get_twisted_placements()](../../d9/dfd/group__draftgeoutils.html#ga9c5399869f1738ac24d9b6923a84c992),
[draftgeoutils.geo_arrays.make_tunnel()](../../d9/dfd/group__draftgeoutils.html#ga86c918812d79995c84d2a517b49f70ca),
and
[draftgeoutils.geo_arrays.make_walkway()](../../d9/dfd/group__draftgeoutils.html#gafaeaf94acb67d0e121f2462bc5d01804).

## ◆ get_twisted_placements()

def draftgeoutils.geo_arrays.get_twisted_placements  | ( |  | _path_ ,   
---|---|---|---  
|  |  | _count_ = `15`,   
|  |  | _rot_factor_ = `0.25`  
| ) | |   
      
    
    Get the placements of the twisted array elements.

References
[draftgeoutils.geo_arrays.get_init_values()](../../d9/dfd/group__draftgeoutils.html#gaf1a91da170d2c13a501be09b8e0822e8),
and
[draftgeoutils.geo_arrays.get_n_params()](../../d9/dfd/group__draftgeoutils.html#ga703f7e9491525954e9160b8731d495c1).

Referenced by
[draftgeoutils.geo_arrays.get_twisted_array_shape()](../../d9/dfd/group__draftgeoutils.html#gabd719361abde85a5f98618a9a8216578),
and
[draftgeoutils.geo_arrays.get_twisted_bridge_shape()](../../d9/dfd/group__draftgeoutils.html#ga69cf1ff30ffc570bcf54fde886dff1ca).

## ◆ getBoundary()

def draftgeoutils.faces.getBoundary  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return the boundary edges of a group of faces.

Referenced by
[draftgeoutils.faces.cleanFaces()](../../d9/dfd/group__draftgeoutils.html#gadc094c875468b72613ed04077996cc56),
and
[draftgeoutils.faces.concatenate()](../../d9/dfd/group__draftgeoutils.html#ga4c22d9073a911f07ce6cb1dde09cd1c1).

## ◆ getBoundaryAngles()

def draftgeoutils.general.getBoundaryAngles  | ( |  | _angle_ ,   
---|---|---|---  
|  |  | _alist_  
| ) | |   
      
    
    Return the 2 closest angles that encompass the given angle.

## ◆ getCircleFromSpline()

def draftgeoutils.circles.getCircleFromSpline  | ( |  | _edge_| ) |   
---|---|---|---|---|---  
      
    
    Return a circle-based edge from a bspline-based edge.
    
    Return None if the edge is not a BSplineCurve.
    

References
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687),
and
[DraftVecUtils.rotate()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2e3351cd7a33a0d82d1da1d378e13db1).

## ◆ getCubicDimensions()

def draftgeoutils.cuboids.getCubicDimensions  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return a list containing the placement, and dimensions of the shape.
    
    The dimensios are length, width and height of a the parallelepiped,
    rounded to the value indicated by `precision`.
    The placement point is the lowest corner of the shape.
    
    If it is not a parallelepiped (cuboid), return None.
    

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftgeoutils.cuboids.isCubic()](../../d9/dfd/group__draftgeoutils.html#ga8f0c24d453468e6cc90a97fd8ae93344),
[draftgeoutils.general.precision()](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ getQuad()

def draftgeoutils.general.getQuad  | ( |  | _face_| ) |   
---|---|---|---|---|---  
      
    
    Return a list of 3 vectors if the face is a quad, ortherwise None.
    
    Returns
    -------
    basepoint, Xdir, Ydir
        If the face is a quad.
    
    None
        If the face is not a quad.
    

References
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ getRotation()

def draftgeoutils.geometry.getRotation  | ( |  | _v1_ ,   
---|---|---|---  
|  |  | _v2_ = `App.Vector(0, 0, 1)`  
| ) | |   
      
    
    Get the rotation Quaternion between 2 vectors.

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9).

Referenced by
[draftgeoutils.geometry.calculatePlacement()](../../d9/dfd/group__draftgeoutils.html#gaadbede2965a30dff070b48848d7b4423),
and
[FCSphereSheetProjector.getRotation()](../../d6/def/classFCSphereSheetProjector.html#ae1ed1f4b7796261aeef608558818c308).

## ◆ getTangent()

def draftgeoutils.edges.getTangent  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _from_point_ = `None`  
| ) | |   
      
    
    Return the tangent to an edge, including BSpline and circular arcs.
    
    If from_point is given, it is used to calculate the tangent,
    only useful for a circular arc.
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ getVerts()

def draftgeoutils.general.getVerts  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return a list containing vectors of each vertex of the shape.

## ◆ hasCurves()

def draftgeoutils.general.hasCurves  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Check if the given shape has curves.

## ◆ hasOnlyWires()

def draftgeoutils.general.hasOnlyWires  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return True if all edges are inside a wire.

## ◆ innerSoddyCircle()

def draftgeoutils.circles_apollonius.innerSoddyCircle  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _circle3_  
| ) | |   
      
    
    Compute the inner soddy circle for three tightly packed circles.
    
    Original Java code Copyright (rc) 2008 Werner Randelshofer
    Converted to python by Martin Buerbaum 2009
    http://www.randelshofer.ch/treeviz/
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

Referenced by
[draftgeoutils.circles_apollonius.circleFrom3CircleTangents()](../../d9/dfd/group__draftgeoutils.html#gae3f7f09b1882e00129fe07ddc74f21b8).

## ◆ invert()

def draftgeoutils.edges.invert  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return an inverted copy of the edge or wire contained in the shape.

References
[draftgeoutils.edges.findMidpoint()](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[draftgeoutils.edges.isLine](../../d9/dfd/group__draftgeoutils.html#ga87b8c31cd76d4e1b5ad8ddb578655e68).

Referenced by
[TechDrawGui::QGVNavStyle.mouseZoomFactor()](../../dc/d63/classTechDrawGui_1_1QGVNavStyle.html#a75173e15c44c8e0b2e6434782afa6d8a),
and
[draftgeoutils.sort_edges.sortEdges()](../../d9/dfd/group__draftgeoutils.html#ga92e9ec6f28e14561900f506fef0e928e).

## ◆ is_coplanar()

def draftgeoutils.faces.is_coplanar  | ( |  | _faces_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Return True if all faces in the given list are coplanar.
    
    Parameters
    ----------
    faces: list
        List of faces to check coplanarity.
    tol: float, optional
        It defaults to `-1`, the tolerance of confusion, equal to 1e-7.
        Is the maximum deviation to be considered coplanar.
    
    Returns
    -------
    out: bool
        True if all face are coplanar. False in other case.
    

References
[draftgeoutils.geometry.are_coplanar()](../../d9/dfd/group__draftgeoutils.html#ga6b2614cca55eba229be7f704b31d8701).

## ◆ is_line()

def draftgeoutils.edges.is_line  | ( |  | _bspline_| ) |   
---|---|---|---|---|---  
      
    
    Return True if the given BSpline curve is a straight line.

## ◆ is_planar()

def draftgeoutils.geometry.is_planar  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Return True if the given shape or list of points is planar.

References
[draftgeoutils.geometry.find_plane()](../../d9/dfd/group__draftgeoutils.html#ga2255544d596f3dbaa5423bb67f78f69d),
and
[draftgeoutils.geometry.is_straight_line()](../../d9/dfd/group__draftgeoutils.html#gaca3c302955adc40b70eb1d12fc43c083).

Referenced by
[draftgeoutils.geometry.are_coplanar()](../../d9/dfd/group__draftgeoutils.html#ga6b2614cca55eba229be7f704b31d8701),
and
[draftgeoutils.geometry.calculatePlacement()](../../d9/dfd/group__draftgeoutils.html#gaadbede2965a30dff070b48848d7b4423).

## ◆ is_straight_line()

def draftgeoutils.geometry.is_straight_line  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _tol_ = `-1`  
| ) | |   
      
    
    Return True if shape is a straight line.
    function used in other methods because Part.Shape.findPlane assign a
    plane and normal to straight wires creating privileged directions
    and to deal with straight wires with overlapped edges.

Referenced by
[draftgeoutils.geometry.find_plane()](../../d9/dfd/group__draftgeoutils.html#ga2255544d596f3dbaa5423bb67f78f69d),
[draftgeoutils.geometry.get_normal()](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a),
[draftgeoutils.geometry.get_spline_normal()](../../d9/dfd/group__draftgeoutils.html#ga871b3414feb189f4255dae897ee3b684),
[draftgeoutils.geometry.is_planar()](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4),
and
[draftfunctions.upgrade.upgrade()](../../d2/d57/group__draftfunctions.html#ga5f09a8d57bed7988f62a3e3aa27705e4).

## ◆ isAligned()

def draftgeoutils.general.isAligned  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _axis_ = `"x"`  
| ) | |   
      
    
    Check if the given edge or line is aligned to the given axis.
    
    The axis can be 'x', 'y' or 'z'.
    

## ◆ isClockwise()

def draftgeoutils.arcs.isClockwise  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _ref_ = `None`  
| ) | |   
      
    
    Return True if a circle-based edge has a clockwise direction.

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[DraftVecUtils.isNull()](../../dc/dc3/group__DRAFTVECUTILS.html#gaaccdee2ed1226b010ac7b3e04c42a687).

## ◆ isCubic()

def draftgeoutils.cuboids.isCubic  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return True if the shape is a parallelepiped (cuboid).
    
    A parallelepiped of cube-like shape has 8 vertices, 6 faces, 12 edges,
    and all angles are 90 degrees between its edges.
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[draftgeoutils.general.precision()](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[draftgeoutils.cuboids.getCubicDimensions()](../../d9/dfd/group__draftgeoutils.html#ga594409c27f69bd528d72d25ee42321ca).

## ◆ isNull()

def draftgeoutils.general.isNull  | ( |  | _something_| ) |   
---|---|---|---|---|---  
      
    
    Return True if the given shape, vector, or placement is Null.
    
    If the vector is (0, 0, 0), it will return True.
    

Referenced by
[PartGui::DlgExtrusion.apply()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a6428c7ac6585ad41ed9792aeea96d2f7),
[PartGui.hasShapesInSelection()](../../d5/d49/namespacePartGui.html#ad528565e643c4ef351810cb1cc417d30),
[Base::Vector2dPy.init_type()](../../dd/dff/classBase_1_1Vector2dPy.html#a2e059c53efba7f535487af05ce4961f4),
[PathScripts.PathUtil.isValidBaseObject()](../../d1/d92/namespacePathScripts_1_1PathUtil.html#a4fd77a9f5f8766c7efda4ea4888fb741),
[ArchRoof.makeRoof()](../../d4/d2a/namespaceArchRoof.html#ad19f0e53e9c0a79c7ac5d7cf86f73c65),
[Gui::PrefWidget.onRestore()](../../d9/d6b/classGui_1_1PrefWidget.html#a3347d166ed595dbc82cb564b7ff39ee4),
[Gui::PrefSpinBox.restorePreferences()](../../dd/d69/classGui_1_1PrefSpinBox.html#a57bdf91dee45adc3bc7bc3c9b59d8abc),
[Gui::PrefDoubleSpinBox.restorePreferences()](../../d2/d6c/classGui_1_1PrefDoubleSpinBox.html#aae6c0a9d9001f22c47e4de8b9cff1dc9),
[Gui::PrefLineEdit.restorePreferences()](../../d1/d55/classGui_1_1PrefLineEdit.html#a94c188dee418d00877ff35948a19f03e),
[Gui::PrefTextEdit.restorePreferences()](../../d8/d7e/classGui_1_1PrefTextEdit.html#a49ad0f9a2538094a854ae6e003c3592f),
[Gui::PrefFileChooser.restorePreferences()](../../d2/d98/classGui_1_1PrefFileChooser.html#af1cdc77f52a860575fac209f2be71eaf),
[Gui::PrefComboBox.restorePreferences()](../../d4/daf/classGui_1_1PrefComboBox.html#a084c013500a009e1d373aea8260c5d69),
[Gui::PrefCheckBox.restorePreferences()](../../d8/da6/classGui_1_1PrefCheckBox.html#ae569653301c04b79831cb03e6a57c272),
[Gui::PrefRadioButton.restorePreferences()](../../d1/dd4/classGui_1_1PrefRadioButton.html#a87f6e6b20175378172098090fef94e47),
[Gui::PrefSlider.restorePreferences()](../../db/d66/classGui_1_1PrefSlider.html#a518206f3445ac694b1053ec1c02d3770),
[Gui::PrefColorButton.restorePreferences()](../../d0/dc4/classGui_1_1PrefColorButton.html#aa24e8146ed8674e32919d1ee752694fd),
[Gui::PrefUnitSpinBox.restorePreferences()](../../d6/da0/classGui_1_1PrefUnitSpinBox.html#a9c04075911e79648a1ec9715cffbdca4),
[Gui::PrefQuantitySpinBox.restorePreferences()](../../da/d1b/classGui_1_1PrefQuantitySpinBox.html#a8852506223eb81fd54eddf9f7d6a592f),
[Gui::PrefFontBox.restorePreferences()](../../d6/d11/classGui_1_1PrefFontBox.html#a6c8bfa11c56a634d421e7beac1e74985),
[Gui::PrefSpinBox.savePreferences()](../../dd/d69/classGui_1_1PrefSpinBox.html#a03023ecfc7fa9756161282701d0787a7),
[Gui::PrefDoubleSpinBox.savePreferences()](../../d2/d6c/classGui_1_1PrefDoubleSpinBox.html#a8932457a0d15c7ab5decefc7d5543646),
[Gui::PrefLineEdit.savePreferences()](../../d1/d55/classGui_1_1PrefLineEdit.html#a369fc2213af1cb31599d1e3d7aed72ab),
[Gui::PrefTextEdit.savePreferences()](../../d8/d7e/classGui_1_1PrefTextEdit.html#ace85a665820dcc38994af7d7b27cf24e),
[Gui::PrefFileChooser.savePreferences()](../../d2/d98/classGui_1_1PrefFileChooser.html#a6f64f6470507a3ff909f22fda9afb640),
[Gui::PrefComboBox.savePreferences()](../../d4/daf/classGui_1_1PrefComboBox.html#a10560c8664f2431d9153ba3b5d6bf57d),
[Gui::PrefCheckBox.savePreferences()](../../d8/da6/classGui_1_1PrefCheckBox.html#a9ad9585be0e3d862b6a7822e2febf88d),
[Gui::PrefRadioButton.savePreferences()](../../d1/dd4/classGui_1_1PrefRadioButton.html#afa01a6561cf13c7d9e505cbaf7ccfb2f),
[Gui::PrefSlider.savePreferences()](../../db/d66/classGui_1_1PrefSlider.html#a86f7976c4c9aa3fd836efeb2d3f83a3b),
[Gui::PrefColorButton.savePreferences()](../../d0/dc4/classGui_1_1PrefColorButton.html#ae7c48cf879584405b9c5e4f3885eff09),
[Gui::PrefUnitSpinBox.savePreferences()](../../d6/da0/classGui_1_1PrefUnitSpinBox.html#adddfe8e9ad0cc064f7005392a6f69140),
[Gui::PrefQuantitySpinBox.savePreferences()](../../da/d1b/classGui_1_1PrefQuantitySpinBox.html#a800f80c9fb12fdd4edb91c67d38dbaba),
[Gui::PrefFontBox.savePreferences()](../../d6/d11/classGui_1_1PrefFontBox.html#a44b0b7f691a153fcb1ce895acd47820c),
[QSint::ActionLabel.sizeHint()](../../df/dcd/classQSint_1_1ActionLabel.html#af590404a93e3885b0feb89d6a8f45acd),
and
[Mod.Test.BaseTests.MatrixTestCase.testNull()](../../d3/d92/classMod_1_1Test_1_1BaseTests_1_1MatrixTestCase.html#afe1cb5766be296702e540253c4ce36bc).

## ◆ isPtOnEdge()

def draftgeoutils.general.isPtOnEdge  | ( |  | _pt_ ,   
---|---|---|---  
|  |  | _edge_  
| ) | |   
      
    
    Test if a point lies on an edge.

Referenced by
[ArchRoof.find_inters()](../../d4/d2a/namespaceArchRoof.html#ad6c2764c962fd9e59c8b69fabc16a529),
and
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d).

## ◆ isReallyClosed()

def draftgeoutils.wires.isReallyClosed  | ( |  | _wire_| ) |   
---|---|---|---|---|---  
      
    
    Check if a wire is really closed.

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

Referenced by
[draftgeoutils.fillets.filletWire()](../../d9/dfd/group__draftgeoutils.html#gaa62f069268859d613ce168c61feadaed).

## ◆ isSameLine()

def draftgeoutils.edges.isSameLine  | ( |  | _e1_ ,   
---|---|---|---  
|  |  | _e2_  
| ) | |   
      
    
    Return True if the 2 edges are lines and have the same points.

References
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33).

## ◆ isValidPath()

def draftgeoutils.general.isValidPath  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return True if the shape can be used as an extrusion path.

## ◆ isWideAngle()

def draftgeoutils.arcs.isWideAngle  | ( |  | _edge_| ) |   
---|---|---|---|---|---  
      
    
    Return True if the given edge is an arc with angle > 180 degrees.

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ linearFromPoints()

def draftgeoutils.linear_algebra.linearFromPoints  | ( |  | _p1_ ,   
---|---|---|---  
|  |  | _p2_  
| ) | |   
      
    
    Calculate linear equation from points.
    
    Calculate the slope and offset parameters of the linear equation
    of a line defined by two points.
    
    Linear equation:
    y = m * x + b
    m = dy / dx
    m ... Slope
    b ... Offset (point where the line intersects the y axis)
    dx/dy ... Delta x and y. Using both as a vector results
    in a non-offset direction vector.
    

## ◆ make_tunnel()

def draftgeoutils.geo_arrays.make_tunnel  | ( |  | _path_ ,   
---|---|---|---  
|  |  | _profiles_  
| ) | |   
      
    
    Create the tunnel shape.

Referenced by
[draftgeoutils.geo_arrays.get_twisted_bridge_shape()](../../d9/dfd/group__draftgeoutils.html#ga69cf1ff30ffc570bcf54fde886dff1ca).

## ◆ make_walkway()

def draftgeoutils.geo_arrays.make_walkway  | ( |  | _path_ ,   
---|---|---|---  
|  |  | _width_ = `100`,   
|  |  | _thickness_ = `10`  
| ) | |   
      
    
    Construct the walkway of the twisted bridge array.

Referenced by
[draftgeoutils.geo_arrays.get_twisted_bridge_shape()](../../d9/dfd/group__draftgeoutils.html#ga69cf1ff30ffc570bcf54fde886dff1ca).

## ◆ mirror()

def draftgeoutils.geometry.mirror  | ( |  | _point_ ,   
---|---|---|---  
|  |  | _edge_  
| ) | |   
      
    
    Find mirror point relative to an edge.

References
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca).

## ◆ offset()

def draftgeoutils.offsets.offset  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _vector_ ,   
|  |  | _trim_ = `False`  
| ) | |   
      
    
    Return a copy of the edge at a certain vector offset.
    
    If the edge is an arc, the vector will be added at its first point
    and a complete circle will be returned.
    
    None if there is a problem.
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ offsetWire()

def draftgeoutils.offsets.offsetWire  | ( |  | _wire_ ,   
---|---|---|---  
|  |  | _dvec_ ,   
|  |  | _bind_ = `False`,   
|  |  | _occ_ = `False`,   
|  |  | _widthList_ = `None`,   
|  |  | _offsetMode_ = `None`,   
|  |  | _alignList_ = `[]`,   
|  |  | _normal_ = `None`,   
|  |  | _basewireOffset_ = `0`  
| ) | |   
      
    
    Offset the wire along the given vector.
    
    Parameters
    ----------
    wire as a list of edges (use the list directly),
    or previously as a wire or a face (Draft Wire with MakeFace True
    or False supported).
    
    The vector will be applied at the first vertex of the wire. If bind
    is True (and the shape is open), the original wire and the offsetted one
    are bound by 2 edges, forming a face.
    
    If widthList is provided (values only, not lengths - i.e. no unit),
    each value will be used to offset each corresponding edge in the wire.
    
    The 1st value overrides 'dvec' for 1st segment of wire;
    if a value is zero, value of 'widthList[0]' will follow;
    if widthList[0]' == 0, but dvec still provided, dvec will be followed
    
    offsetMode="BasewireMode" or None
    
    If alignList is provided,
    each value will be used to offset each corresponding edge
    in the wire with corresponding index.
    
    'basewireOffset' corresponds to 'offset' in ArchWall which offset
    the basewire before creating the wall outline
    
    OffsetWire() is now aware of width and align per edge
    Primarily for use with ArchWall based on Sketch object
    
    To Do
    -----
    `dvec` vector to offset is now derived (and can be ignored)
    in this function if widthList and alignList are provided
    - 'dvec' to be obsolete in future?
    

References
[draftgeoutils.intersections.connect()](../../d9/dfd/group__draftgeoutils.html#ga0b7c0fe418afd94ab4e966fe53b88960),
[draftgeoutils.geometry.get_normal()](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a),
[DraftVecUtils.scaleTo()](../../dc/dc3/group__DRAFTVECUTILS.html#ga6b1b9879299d28cb689cbee684e9d5f3),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Part::ExtrusionHelper.makeDraft()](../../d4/dd3/classPart_1_1ExtrusionHelper.html#a29278e87069e6bf3c1281d0bce4d2ae8),
and
[Part::TopoShape.makeOffsetShape()](../../d8/ded/classPart_1_1TopoShape.html#aefba99649f708e584a01c114826affa5).

## ◆ orientEdge()

def draftgeoutils.edges.orientEdge  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _normal_ = `None`,   
|  |  | _make_arc_ = `False`  
| ) | |   
      
    
    Re-orient the edge such that it is in the XY plane.
    
    Re-orients `edge` such that it is in the XY plane.
    If `normal` is passed, this is used as the basis for the rotation,
    otherwise the placement of `edge` is used.
    

References
[DraftVecUtils.angle()](../../dc/dc3/group__DRAFTVECUTILS.html#ga9c9b4d0abb5c7441f037c924566167b9).

## ◆ outerSoddyCircle()

def draftgeoutils.circles_apollonius.outerSoddyCircle  | ( |  | _circle1_ ,   
---|---|---|---  
|  |  | _circle2_ ,   
|  |  | _circle3_  
| ) | |   
      
    
    Compute the outer soddy circle for three tightly packed circles.
    
    Original Java code Copyright (rc) 2008 Werner Randelshofer
    Converted to python by Martin Buerbaum 2009
    http://www.randelshofer.ch/treeviz/
    Either Creative Commons Attribution 3.0, the MIT license,
    or the GNU Lesser General License LGPL.
    

References
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

Referenced by
[draftgeoutils.circles_apollonius.circleFrom3CircleTangents()](../../d9/dfd/group__draftgeoutils.html#gae3f7f09b1882e00129fe07ddc74f21b8).

## ◆ pocket2d()

def draftgeoutils.offsets.pocket2d  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _offset_  
| ) | |   
      
    
    Return a list of wires obtained from offsetting wires from the shape.
    
    Return a list of wires obtained from offsetting the wires
    from the given shape by the given offset, and intersection if needed.
    

References
[draftgeoutils.intersections.wiresIntersect()](../../d9/dfd/group__draftgeoutils.html#ga5e7ce6b0591a23ad098be94b4c64dd67).

## ◆ pointInversion()

def draftgeoutils.circle_inversion.pointInversion  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _point_  
| ) | |   
      
    
    Return the circle inversion of a point.
    
    It will return `None` if the given point is equal to the center
    of the circle.
    

References
[DraftVecUtils.dist()](../../dc/dc3/group__DRAFTVECUTILS.html#ga2af953a65bfefb422584aa67c55dbc39),
[DraftVecUtils.equals()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf10d883f1703323fc5afeb8b45ff8b33),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

Referenced by
[draftgeoutils.circle_inversion.circleInversion()](../../d9/dfd/group__draftgeoutils.html#gaf83de47d0b318d570f1ca51dcc9cbefb),
and
[draftgeoutils.circle_inversion.polarInversion()](../../d9/dfd/group__draftgeoutils.html#ga54bc622493ab5bc634b63a70f5fc7ef7).

## ◆ polarInversion()

def draftgeoutils.circle_inversion.polarInversion  | ( |  | _circle_ ,   
---|---|---|---  
|  |  | _edge_  
| ) | |   
      
    
    Return the inversion pole of a line. The edge is the polar.
    
    The nearest point on the line is inversed.
    
    http://mathworld.wolfram.com/InversionPole.html
    

References
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
and
[draftgeoutils.circle_inversion.pointInversion()](../../d9/dfd/group__draftgeoutils.html#ga2e9e5f6e50364165f9e6e1f8f5d5d8f8).

## ◆ precision()

def draftgeoutils.general.precision  | ( | | ) |   
---|---|---|---|---  
      
    
    Return the Draft precision setting.

Referenced by
[Gui::SoFCColorGradient.customize()](../../d0/de7/classGui_1_1SoFCColorGradient.html#af1c20488dfa1c3ec77da20bc8caf30a9),
[draftgeoutils.fillets.fillet()](../../d9/dfd/group__draftgeoutils.html#ga9ee52e4030cf753ebf972be204bdce1f),
[SMESH_OctreeNode.FindCoincidentNodes()](../../dd/d88/classSMESH__OctreeNode.html#a8bfd8996839370aa0424f612973a0e17),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[draftgeoutils.wires.get_extended_wire()](../../d9/dfd/group__draftgeoutils.html#gae6d8e69cb869af3d1824fd750b93db3f),
[draftgeoutils.cuboids.getCubicDimensions()](../../d9/dfd/group__draftgeoutils.html#ga594409c27f69bd528d72d25ee42321ca),
[TechDraw::DrawViewDimension.getDefaultFormatSpec()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#ae6868b300206d4acd693965dbf059bc5),
[TechDrawGui::QGIDatumLabel.getPrecision()](../../d7/d0c/classTechDrawGui_1_1QGIDatumLabel.html#a56fc799073be6ccf0e45e538d1db75fe),
[draftgeoutils.cuboids.isCubic()](../../d9/dfd/group__draftgeoutils.html#ga8f0c24d453468e6cc90a97fd8ae93344),
[SMESH_OctreeNode.NodesAround()](../../dd/d88/classSMESH__OctreeNode.html#a4717ecfe40ed02d3fbb780524518d66d),
[draftgeoutils.wires.removeInterVertices()](../../d9/dfd/group__draftgeoutils.html#ga02af528fa3ba94a6061f7ac12c4e7cbc),
and
[Path::Command.toGCode()](../../d7/d2e/classPath_1_1Command.html#ac42dc79f20af29520dddda80a0a87e0a).

## ◆ print_places()

def draftgeoutils.geo_arrays.print_places  | ( |  | _places_ ,   
---|---|---|---  
|  |  | _title_ = `"Places"`  
| ) | |   
      
    
    Print a vector with a title.

## ◆ rebaseWire()

def draftgeoutils.wires.rebaseWire  | ( |  | _wire_ ,   
---|---|---|---  
|  |  | _vidx_ = `0`  
| ) | |   
      
    
    Return a copy of the wire with the first vertex indicated by the index.
    
    Return a new wire which is a copy of the current wire,
    but where the first vertex is the vertex indicated by the given
    index vidx, starting from 1.
    0 will return an exact copy of the wire.
    

Referenced by
[ShapeInfo.sortWires()](../../d9/dfa/structShapeInfo.html#a82ec1677580f6ede71e016d3e751fd5b).

## ◆ removeInterVertices()

def draftgeoutils.wires.removeInterVertices  | ( |  | _wire_| ) |   
---|---|---|---|---|---  
      
    
    Remove middle vertices from a straight wire and return a new wire.
    
    Remove unneeded vertices, those that are in the middle of a straight line,
    from a wire, return a new wire.
    

References
[draftgeoutils.general.precision()](../../d9/dfd/group__draftgeoutils.html#gaffb91e2fa71e3b1945163eac02ff3d38),
and
[draftgeoutils.general.vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

## ◆ removeSplitter()

def draftgeoutils.faces.removeSplitter  | ( |  | _shape_| ) |   
---|---|---|---|---|---  
      
    
    Return a face from removing the splitter in a list of faces.
    
    This is an alternative, shared edge-based version of Part.removeSplitter.
    Returns a face, or `None` if the operation failed.
    

Referenced by
[prototype.Node.addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.draftlink.DraftLink.buildShape()](../../d6/d1d/classdraftobjects_1_1draftlink_1_1DraftLink.html#acc5bae9c96388076d1c76aab03797f08),
[PathScripts.PathSimulatorGui.PathSimulation.GetPathSolid()](../../da/dfe/classPathScripts_1_1PathSimulatorGui_1_1PathSimulation.html#a239ea9f9aec600859382542c2ef80552),
[ArchRoof.makeRoof()](../../d4/d2a/namespaceArchRoof.html#ad19f0e53e9c0a79c7ac5d7cf86f73c65),
and
[importCSG.p_polyhedron_action()](../../d9/df6/namespaceimportCSG.html#a8aae9e8635bf33c1952fdbe297176834).

## ◆ sortEdges()

def draftgeoutils.sort_edges.sortEdges  | ( |  | _edges_| ) |   
---|---|---|---|---|---  
      
    
    Sort edges. Deprecated. Use Part.__sortEdges__ instead.

References
[draftgeoutils.edges.invert()](../../d9/dfd/group__draftgeoutils.html#ga60dc82b8b95b16ffa97e1ccd715f099e),
and
[draftgeoutils.sort_edges.sortEdgesOld()](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3).

## ◆ sortEdgesOld()

def draftgeoutils.sort_edges.sortEdgesOld  | ( |  | _lEdges_ ,   
---|---|---|---  
|  |  | _aVertex_ = `None`  
| ) | |   
      
    
    Sort edges. Deprecated. Use Part.__sortEdges__ instead.

References
[draftgeoutils.edges.findMidpoint()](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84),
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737),
[draftgeoutils.edges.isLine](../../d9/dfd/group__draftgeoutils.html#ga87b8c31cd76d4e1b5ad8ddb578655e68),
and
[draftgeoutils.sort_edges.sortEdgesOld()](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3).

Referenced by
[draftgeoutils.sort_edges.sortEdges()](../../d9/dfd/group__draftgeoutils.html#ga92e9ec6f28e14561900f506fef0e928e),
and
[draftgeoutils.sort_edges.sortEdgesOld()](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3).

## ◆ superWire()

def draftgeoutils.wires.superWire  | ( |  | _edgeslist_ ,   
---|---|---|---  
|  |  | _closed_ = `False`  
| ) | |   
      
    
    Force a wire between edges that don't have coincident endpoints.
    
    Forces a wire between edges that don't necessarily
    have coincident endpoints. If closed=True, the wire will always be closed.
    

References
[draftgeoutils.edges.findMidpoint()](../../d9/dfd/group__draftgeoutils.html#ga809766939b81c6f875420426a1b3ae84),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ tessellateProjection()

def draftgeoutils.wires.tessellateProjection  | ( |  | _shape_ ,   
---|---|---|---  
|  |  | _seglen_  
| ) | |   
      
    
    Return projection with BSplines and Ellipses broken into line segments.
    
    Useful for exporting projected views to DXF files.
    

References
[draftgeoutils.wires.curvetosegment()](../../d9/dfd/group__draftgeoutils.html#gafbf52a3d00dd3badab8d7de2bc94f785),
and
[draftgeoutils.general.geomType()](../../d9/dfd/group__draftgeoutils.html#gadebaa4c226b84107052977ebda300737).

## ◆ v1()

def draftgeoutils.general.v1  | ( |  | _edge_| ) |   
---|---|---|---|---|---  
      
    
    Return the first point of an edge.

Referenced by
[TechDraw::DrawViewPart.addShapes2d()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a2e6da23a2374976a31820441fded41e7),
[TechDraw::AOC.AOC()](../../d0/d5c/classTechDraw_1_1AOC.html#a60ad7491da14354428864adf127ea11b),
[TechDraw::AOE.AOE()](../../d6/d99/classTechDraw_1_1AOE.html#a685a68e866911f9d4fea28a4a24043c5),
[lscmrelax::LscmRelax.area_relax()](../../d5/d01/classlscmrelax_1_1LscmRelax.html#af3dc1cbd45d7cdb2751b80ae796f50f3),
[TechDraw::BSpline.BSpline()](../../d6/d09/classTechDraw_1_1BSpline.html#ab0d19db0c31b1dd84f5bdefcb2303443),
[InspectionGui.calcArea()](../../dd/d85/namespaceInspectionGui.html#a2d3d406cee568798a2947269821c1b70),
[TechDraw::CenterLine.calcEndPoints2Points()](../../d5/dd5/classTechDraw_1_1CenterLine.html#aedb72634306a11f9eb49ffac16eb7e2b),
[StdMeshers_Quadrangle_2D.check()](../../d1/db4/classStdMeshers__Quadrangle__2D.html#a54d4e01d3c35d1a2492a21a74127e875),
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
[Part.closestPointsOnLines()](../../d2/db9/namespacePart.html#a389ea20c7863562ce3513947b319f9d3),
[SandboxGui::SoWidgetShape.computeBBox()](../../d6/dc7/classSandboxGui_1_1SoWidgetShape.html#a3db0d27eedd28604d4adc4af02ecc0d8),
[geoff_geometry.corner()](../../de/d5d/namespacegeoff__geometry.html#af06ef6f222ffe93ab42a52ad7f274a1b),
[MeshPart::BrepMesh.create()](../../de/d62/classMeshPart_1_1BrepMesh.html#ad32eda06dc21d116690d1cf98568ade1),
[Surface::GeomFillSurface.createFace()](../../d7/d0d/classSurface_1_1GeomFillSurface.html#aa4c4939e9785b78b50fb4ba31554b394),
[StdMeshers_Penta_3D.CreateNode()](../../d7/d81/classStdMeshers__Penta__3D.html#ae4fc64fa29911181e1b1424692ade7ea),
[App::Expression::Component.del()](../../d5/df9/structApp_1_1Expression_1_1Component.html#aa3b85278581997ecc4206d983cde0222),
[Sketcher::SketchAnalysis.detectMissingPointOnPointConstraints()](../../d5/d89/classSketcher_1_1SketchAnalysis.html#aa3ccb4b59ed67acd26b695ac6c6e99b1),
[MeshGui::SoFCIndexedFaceSet.drawCoords()](../../d8/dcd/classMeshGui_1_1SoFCIndexedFaceSet.html#abcec7b52a15c9f5d1449a9ec0152d9a7),
[Part::RuledSurface.execute()](../../d1/d41/classPart_1_1RuledSurface.html#aaff86f64ccc1eeeb1158727285cacab0),
[Surface::Extend.execute()](../../d1/d22/classSurface_1_1Extend.html#a50a4d6f3fb960ba8acaa558639be59f0),
[Import::ImpExpDxfWrite.exportArc()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a02797fa294627a7f6fbfd9c52ca86e21),
[Import::ImpExpDxfWrite.exportEllipseArc()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a47f82be403f65b1ed6fc9ead4800b706),
[StdMeshers_ProjectionUtils.FindSubShapeAssociation()](../../d2/d9a/namespaceStdMeshers__ProjectionUtils.html#a9746e1ff09b3172761891e2d9fef5d20),
[PartGui::SoBrepFaceSet.generatePrimitives()](../../d5/dad/classPartGui_1_1SoBrepFaceSet.html#ab8188586ce27b908f8ac472473f73efd),
[SandboxGui::SoWidgetShape.generatePrimitives()](../../d6/dc7/classSandboxGui_1_1SoWidgetShape.html#a06634c2433115fc1afb5cd9b5fd9398d),
[App::Expression::Component.get()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a105ce2f55b1e32a78b7fe55f0be9789d),
[StdMeshers_Quadrangle_2D.getEnforcedUV()](../../d1/db4/classStdMeshers__Quadrangle__2D.html#a1bbffcada6260cde3d9a3341cc1fcbb7),
[Part::TopoShape.getFaces()](../../d8/ded/classPart_1_1TopoShape.html#a00b87e8480fdfd6ff72906c1018a8553),
[Part::TopoShape.getFacesFromSubElement()](../../d8/ded/classPart_1_1TopoShape.html#af27da9405b017f60101ba35b142fd3b9),
[Part::Tools.getNormal()](../../d9/d36/classPart_1_1Tools.html#a7cc4b493707602047fe7b48f30051884),
[Part::Tools.getPointNormals()](../../d9/d36/classPart_1_1Tools.html#a7804743dad14509bb6ffb830b7cf33c6),
[Part::TopoShape.getPoints()](../../d8/ded/classPart_1_1TopoShape.html#ae463bf2f67be635950e76e8c3d6eee2a),
[Part::GeomArcOfCircle.getRange()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#a3ebdcf4b08d4845e4fa0e076c95833d1),
[SMESH_Algo.GetSortedNodesOnEdge()](../../d4/df9/classSMESH__Algo.html#a37252007705488bc287970b8768bb9af),
[SMESH::Controls::Skew.GetValue()](../../d0/d43/classSMESH_1_1Controls_1_1Skew.html#a222968fba4d4811e54009e73295a474a),
[Fem::FemMesh.getVolume()](../../d3/d2e/classFem_1_1FemMesh.html#a86dfe0bdac5ccbc115b39af5780ee2b1),
[Gui::SoTextLabel.GLRender()](../../db/d67/classGui_1_1SoTextLabel.html#a91baca13d5cf73af817c5eb1b7e00aaf),
[SketcherGui::SoDatumLabel.GLRender()](../../d3/d9d/classSketcherGui_1_1SoDatumLabel.html#a4852d28cbd11ff9224b8382c455cbe84),
[geoff_geometry.IncludedAngle()](../../de/d5d/namespacegeoff__geometry.html#ad12476419f95df40f6062ad348a41352),
[MeshCore::MeshGeomFacet.IntersectBoundingBox()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a0a6b404c351030f6727713ab4b9fa805),
[MeshCore::MeshGeomFacet.IntersectWithPlane()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a1a60849171e88c8fcf54e341b36a56eb),
[VISCOUS_2D::_PolyLine.IsConcave()](../../de/d7b/structVISCOUS__2D_1_1__PolyLine.html#a08257467fef401e75df3ef6c07223828),
[SMESH_MesherHelper.IsDistorted2D()](../../db/dc6/classSMESH__MesherHelper.html#af3cc90d82a7a5dd45f78994175f5b6e2),
[VISCOUS_3D::_Simplex.IsForward()](../../d4/d59/structVISCOUS__3D_1_1__Simplex.html#a21addc74b88aedc6f582f9e67b0195c9),
[TechDraw::BSpline.isLine()](../../d6/d09/classTechDraw_1_1BSpline.html#a9389b227a2adf85540c96b481ffff118),
[SMESH_Algo.IsStraight()](../../d4/df9/classSMESH__Algo.html#a76e69103cc7ab2fd6e8a92fdf17fd4a4),
[geoff_geometry.LineArcIntof()](../../de/d5d/namespacegeoff__geometry.html#a60c2a6fdf66479451e61772695f45230),
[geoff_geometry.LineLineIntof()](../../de/d5d/namespacegeoff__geometry.html#a4e2548d8defbfedf56a5ed40b255b950),
[SMESH_Pattern.Load()](../../d0/d7d/classSMESH__Pattern.html#aada1481358a8eedfa7a175da392b9308),
[TechDraw::DrawDimHelper.makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[StdMeshers_Penta_3D.MakeNodes()](../../d7/d81/classStdMeshers__Penta__3D.html#a2143bf2b66470c3fa59946f4679193fd),
[Part::TopoShape.makeTube()](../../d8/ded/classPart_1_1TopoShape.html#ab60c88e2b5052721d132853a342dc0a8),
[MeshCore::MeshGeomFacet.MeshGeomFacet()](../../d4/d8a/classMeshCore_1_1MeshGeomFacet.html#a9889fb0ba7c453a3ae3396eff7b1d528),
[Fem::Constraint.onChanged()](../../d0/d11/classFem_1_1Constraint.html#aec25bc397a1a87056079e3cd5a59d778),
[geoff_geometry::Span.OnSpan()](../../d9/d68/classgeoff__geometry_1_1Span.html#ae0a8c1a5b14fa1db789ea76b8e25b7c2),
[SMESH_MeshEditor.OrientedAngle()](../../da/d31/classSMESH__MeshEditor.html#a69ef5cc92d15aa54d4a89984740f9b31),
[MeshCore::MeshKernel.Read()](../../dd/d95/classMeshCore_1_1MeshKernel.html#ab09d3329cbc592e606955bccf637a36b),
[lscmrelax::LscmRelax.relax()](../../d5/d01/classlscmrelax_1_1LscmRelax.html#a31024a8a4669f6e01b512128d3e490e5),
[PartGui::SoBrepFaceSet::VBO.render()](../../d0/d2e/classSoBrepFaceSet_1_1VBO.html#a958fc491955d66b04c3bf6f6a9567be7),
[App::Expression::Component.set()](../../d5/df9/structApp_1_1Expression_1_1Component.html#a8f3a5ce94e26009bf81a428ec7726910),
[Part::GeomArcOfCircle.setRange()](../../de/d1f/classPart_1_1GeomArcOfCircle.html#a1735aae861e0b32f88794d5932c21f26),
[App::OperatorExpression.simplify()](../../d1/d7d/classApp_1_1OperatorExpression.html#a350f104eaa83275378734a4bc3239ae5),
[geoff_geometry.tangential_arc()](../../de/d5d/namespacegeoff__geometry.html#a97edd9eafdffcce0f93708ba7ed7a9ec),
[Part.tangentialArc()](../../d2/db9/namespacePart.html#a39d5d9d990efef3e6581398defbda87d),
[Part::GeomSurface.toShape()](../../d7/d6d/classPart_1_1GeomSurface.html#abcf555317cf1fee102a115816dcb77c5),
[PartGui::ViewProviderPartExt.updateVisual()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a96cb6b96c8dfb082a135a31c4f554167),
and
[StringGuard.~StringGuard()](../../d2/d45/classStringGuard.html#a87e58efff991c887d64afeae28f050f7).

## ◆ vec()

def draftgeoutils.general.vec  | ( |  | _edge_ ,   
---|---|---|---  
|  |  | _use_orientation_ = `False`  
| ) | |   
      
    
    Return a vector from an edge or a Part.LineSegment.
    
    If use_orientation is True, it takes into account the edges orientation.
    If edge is not straight, you'll get strange results!
    

Referenced by
[App::GroupExtension.addObject()](../../da/d3a/classApp_1_1GroupExtension.html#a583eea19b9a0e1af43bb8aa8fdf9dbad),
[DraftUtils::DraftDxfRead.AddObject()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#aa5b12cf60ff8912314f410187655404c),
[Import::ImpExpDxfRead.AddObject()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#ac13e85924ca8c662789bbd02a2cfe889),
[Base::Builder3D.addPoint()](../../d6/d1b/classBase_1_1Builder3D.html#a4ba202347a70ab413514e8a508b288ec),
[Base::InventorBuilder.addPoint()](../../db/d7f/classBase_1_1InventorBuilder.html#a04d481e0aae6c8be35c121a5ad92bc82),
[Base::InventorBuilder.addPoints()](../../db/d7f/classBase_1_1InventorBuilder.html#af1b546025002b5ff636b17d9e7b12764),
[Base::Builder3D.addSinglePoint()](../../d6/d1b/classBase_1_1Builder3D.html#a1ef7fc99f4b70fcfa58bc787306515b3),
[Base::Builder3D.addText()](../../d6/d1b/classBase_1_1Builder3D.html#ae5f150c5f2f24fda47444f00041618d2),
[Base::InventorBuilder.addText()](../../db/d7f/classBase_1_1InventorBuilder.html#ad9a7fdefd3bb65d3c8d5b8b7b2133d9c),
[SMESH_Pattern.Apply()](../../d0/d7d/classSMESH__Pattern.html#a7bdae2f9ad68bae3cd39d60fc463371e),
[PathSimulator::PathSim.ApplyCommand()](../../d4/d82/classPathSimulator_1_1PathSim.html#a3bd3bbe370b27eabfceed51d07afef05),
[Gui::ManualAlignment.applyPickedProbe()](../../d7/d97/classGui_1_1ManualAlignment.html#ab534e0e7e979975c445625aeb9fef797),
[draftgeoutils.general.areColinear()](../../d9/dfd/group__draftgeoutils.html#ga9f5ec2b0065bccf89ab1700b8aebe673),
[AdaptivePath.averageDV()](../../d5/d7f/namespaceAdaptivePath.html#af1aa43ee514aa09b480432bed4852e81),
[draftgeoutils.circles.circlefrom1Line2Points()](../../d9/dfd/group__draftgeoutils.html#ga62f4e19d1f4b45e85467ccefd5dd8a50),
[draftgeoutils.circles.circleFrom2LinesRadius()](../../d9/dfd/group__draftgeoutils.html#gac123fb7d62899d609a3206597da6e734),
[draftgeoutils.circles.circleFrom2PointsRadius()](../../d9/dfd/group__draftgeoutils.html#gac5ca6e04d961e3751606a1e4ccf378b4),
[draftgeoutils.circles.circleFrom3LineTangents()](../../d9/dfd/group__draftgeoutils.html#gacc0f0f89c65bda5546b24a2513ed592c),
[draftgeoutils.circles.circleFromPointLineRadius()](../../d9/dfd/group__draftgeoutils.html#ga163b5f31d9b814e500670ab9cec198b5),
[Gui::ViewProvider.claimChildren()](../../d3/db3/classGui_1_1ViewProvider.html#af51254c2d4352f0c36f75c6e909ef1df),
[Gui::ViewProvider.claimChildren3D()](../../d3/db3/classGui_1_1ViewProvider.html#a94904ffbb658c5beb5f6a9bc6a4eb4cc),
[SMESHUtils.CompactVector()](../../d0/d9d/namespaceSMESHUtils.html#aa95f6449ee4de2069ab4eb05684c2ce1),
[PointsGui::ViewProviderPointsBuilder.createPoints()](../../da/d13/classPointsGui_1_1ViewProviderPointsBuilder.html#a282b9fa47719cd5c74168abf6cfd60f2),
[PointsGui::ViewProviderStructured.cut()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#a808184849a3543a6d70c263099506c98),
[FemGui::TaskCreateNodeSet.DefineNodes()](../../da/d68/classFemGui_1_1TaskCreateNodeSet.html#a6bd7d00ad2d337fbb90c45d927e80c71),
[App::FunctionExpression.evaluate()](../../d6/da3/classApp_1_1FunctionExpression.html#aea533bde72fab9803b76f53f0b02aac0),
[Fem::FemVTKTools.exportFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a37e8a3dd86851c4ce056f3cfa7ad0d89),
[Part::Extrusion.extrudeShape()](../../db/d6c/classPart_1_1Extrusion.html#a19815460f6c16ab364759969c6ea1768),
[Fem::FemPostDataAtPointFilter.FemPostDataAtPointFilter()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#a8163973079c8e060ffda0874505a87ad),
[Part::Extrusion.fetchAxisLink()](../../db/d6c/classPart_1_1Extrusion.html#aa781c2570b1b3d21e7879742e6e599ab),
[draftgeoutils.geometry.findDistance()](../../d9/dfd/group__draftgeoutils.html#gadb5e321267b39af75b106d101359e2ca),
[draftgeoutils.circles.findHomotheticCenterOfCircles()](../../d9/dfd/group__draftgeoutils.html#ga8a2f5385b2e75457e5b317f7ba170816),
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d),
[Part::TopoShape.findPlane()](../../d8/ded/classPart_1_1TopoShape.html#a3161c7009c7adeee09bc0b8c7b6b1f58),
[Part::GeomCurve.firstDerivativeAtParameter()](../../d4/dc1/classPart_1_1GeomCurve.html#a09e6ed8858b7caae93bdeebf06886601),
[Part::Geom2dCurve.firstDerivativeAtParameter()](../../d4/da9/classPart_1_1Geom2dCurve.html#a9c0bd5f343fbbde9e2acec95d777dff7),
[SMESHUtils.FreeVector()](../../d0/d9d/namespaceSMESHUtils.html#a23b7944c7ac91b3838f3154e4ceb0bfc),
[Fem::FemMesh.getBoundBox()](../../d3/d2e/classFem_1_1FemMesh.html#afb2c992ff59897fe6eb33f53604bcb1f),
[Path::Command.getCenter()](../../d7/d2e/classPath_1_1Command.html#a45d76889d196b6b95df4b886566ba53d),
[App::GeoFeatureGroupExtension.getCSRelevantLinks()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a9c85d48c46398d16073136acabc1c621),
[draftgeoutils.cuboids.getCubicDimensions()](../../d9/dfd/group__draftgeoutils.html#ga594409c27f69bd528d72d25ee42321ca),
[Fem::Constraint.getDirection()](../../d0/d11/classFem_1_1Constraint.html#a74ee50a75fff721d064b164c334e9f1b),
[Fem::Tools.getDirection()](../../d3/d28/classFem_1_1Tools.html#acfcce81ab94b147c96ef5faf088f7356),
[exportIFC.getEdgesAngle()](../../d8/d5d/namespaceexportIFC.html#a6ece09909c9354fd46a88bc5eb891e80),
[App::ExtensionContainer.getExtensionsDerivedFrom()](../../d6/d76/classApp_1_1ExtensionContainer.html#a8b1505a7cdc7d5f2c43e0d3cfaa8100c),
[App::GeoFeatureGroupExtension.getInvalidLinkObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a391e01ee323c3d9c25c8d74aa8271ae2),
[Gui::ViewProvider.getModelPoints()](../../d3/db3/classGui_1_1ViewProvider.html#a527d766474f3066fbda47b289b78b58e),
[PartGui::ViewProviderPartExt.getModelPoints()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a2221b4ae746e7a1ec366403ad725a102),
[Fem::FemMesh.getNodesByEdge()](../../d3/d2e/classFem_1_1FemMesh.html#ae1be005a643449efced00082a00dd56f),
[Fem::FemMesh.getNodesByFace()](../../d3/d2e/classFem_1_1FemMesh.html#a0f6444e1ac9bc2aa6302b4faad3e2823),
[Fem::FemMesh.getNodesBySolid()](../../d3/d2e/classFem_1_1FemMesh.html#a287b45f44f6d612bd439bfc6506e2f92),
[Fem::FemMesh.getNodesByVertex()](../../d3/d2e/classFem_1_1FemMesh.html#af06c1aed01ace452f292a1d1e11d0ce3),
[Path::Command.getPlacement()](../../d7/d2e/classPath_1_1Command.html#a24d8f7cbd0c7a627ae60673e6b8faddf),
[Gui::View3DInventorPy.getPointOnScreen()](../../d3/df7/classGui_1_1View3DInventorPy.html#a1060471902e48d31c786fcfdf9627bd9),
[exportIFC.getProfile()](../../d8/d5d/namespaceexportIFC.html#a65c4646efb7ee1f226d12147afac08bd),
[PartDesign::ProfileBased.getProfileNormal()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#af389a14c1da76e8ce4aa4dd5dc874540),
[TechDrawGui::DrawGuiUtil.getProjDirFromFace()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a1e16c708a7e2a33bd36999a5f02ae63b),
[draftgeoutils.general.getQuad()](../../d9/dfd/group__draftgeoutils.html#ga05b3b3bca55d3b70e31c09a3903ab38e),
[StdMeshers_ImportSource1D.GetResultGroups()](../../db/ddd/classStdMeshers__ImportSource1D.html#a4688298bdcecf834a3b2bc504d31fea9),
[draftgeoutils.edges.getTangent()](../../d9/dfd/group__draftgeoutils.html#gade4f4721afcac4eb74bbb38729e6b2c6),
[Gui::ViewProviderDocumentObject.getTaskViewContent()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a205ef5356cc48a8f8252c2109275cd2e),
[Base::FileInfo.getTempFileName()](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74),
[Robot::Trajectory.getVelocity()](../../d7/d14/classRobot_1_1Trajectory.html#a5f2eaa83ffa90506b54e685d8e3fd7b8),
[PartDesign::ProfileBased.handleChangedPropertyName()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[Fem::FemVTKTools.importFreeCADResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a06964ad44830b32163bedb9351fad2c8),
[draftgeoutils.cuboids.isCubic()](../../d9/dfd/group__draftgeoutils.html#ga8f0c24d453468e6cc90a97fd8ae93344),
[Fem::Tools.isLinear()](../../d3/d28/classFem_1_1Tools.html#affb9bf4553ad4a36918b3352d7e7d36f),
[Part::TopoShape.makePrism()](../../d8/ded/classPart_1_1TopoShape.html#a8db2a5cf3dd1cb27358548bae4e23c13),
[SketcherGui::ViewProviderSketch.mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[SketcherGui::ViewProviderSketch.mouseMove()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa),
[Mesh::MeshObject.movePoint()](../../d8/dcc/classMesh_1_1MeshObject.html#a439d572a2d7e77fef023679b3950285b),
[Reen::ScalarProduct.multiply()](../../d5/d4a/classReen_1_1ScalarProduct.html#a8ff6b536cd253ebcad97a6bb426f6e8b),
[draftgeoutils.offsets.offsetWire()](../../d9/dfd/group__draftgeoutils.html#ga05bacae1f1c67ceaba7aa1c37c8f758f),
[Gui::Dialog::DemoMode.on_playButton_toggled()](../../d3/d05/classGui_1_1Dialog_1_1DemoMode.html#acb902d292a633f8c4e64d7ff32d6421f),
[FemGui::PlaneWidget.onChange()](../../dc/dc4/classFemGui_1_1PlaneWidget.html#a095c8da3c4ba6837b061e9463d01459f),
[FemGui::SphereWidget.onChange()](../../d6/dfe/classFemGui_1_1SphereWidget.html#a870df1f2861c5b5e7f27c6442bf397ab),
[Fem::FemPostDataAtPointFilter.onChanged()](../../d1/d7a/classFem_1_1FemPostDataAtPointFilter.html#ae4bb2f96ee214db7c2bcb5a0afe0fdc4),
[Fem::FemPostPlaneFunction.onChanged()](../../dd/d76/classFem_1_1FemPostPlaneFunction.html#ab73b39b74f480820feda8b3f5bcad117),
[Fem::FemPostSphereFunction.onChanged()](../../d5/dcb/classFem_1_1FemPostSphereFunction.html#abffccabdacd9cbbe6e61e799c8385c59),
[Base::DualQuat.pow()](../../d4/d13/classBase_1_1DualQuat.html#a6744d98c253f5310ed8f421c54286ea4),
[VISCOUS_3D::_SolidData.PrepareEdgesToSmoothOnFace()](../../d6/d5f/structVISCOUS__3D_1_1__SolidData.html#a5394b5515a4b89bb29625025d5f94cc5),
[Gui::ManualAlignment.probePickedCallback()](../../d7/d97/classGui_1_1ManualAlignment.html#af255c1f31bf62293781d8a04cbecbceb),
[MeshPart::MeshProjection.projectOnMesh()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#ab0dd5abefe9189817d0798f118f88130),
[MeshCore::MeshGeomEdge.ProjectPointToLine()](../../db/df3/classMeshCore_1_1MeshGeomEdge.html#a99dfedd8dad3ccd89f04d3c34114db8a),
[zipios.readByteSeq()](../../de/d29/namespacezipios.html#af3bbf92e41ca7f39919136863f200fde),
[App::OriginGroupExtension.relinkToOrigin()](../../da/d09/classApp_1_1OriginGroupExtension.html#af4330ed14ea93ff3cbf7d0f952cf5e49),
[draftgeoutils.wires.removeInterVertices()](../../d9/dfd/group__draftgeoutils.html#ga02af528fa3ba94a6061f7ac12c4e7cbc),
[App::GroupExtension.removeObject()](../../da/d3a/classApp_1_1GroupExtension.html#a8cd07a1279068b8c8f68d2a7b477ac34),
[Part::Geometry.scale()](../../dc/df0/classPart_1_1Geometry.html#a51110ec18166b9281bcd7ff147409a46),
[Sketcher::ExternalGeometryFacade.scale()](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#a5e68c4641a278ad94552aa30481da7eb),
[Sketcher::GeometryFacade.scale()](../../d1/d73/classSketcher_1_1GeometryFacade.html#a8b1b95e99b46af19ef2684f716a40eb7),
[Part::GeomCurve.secondDerivativeAtParameter()](../../d4/dc1/classPart_1_1GeomCurve.html#a8ea5bf9b8f8255566dfbfb124a5b7035),
[Part::Geom2dCurve.secondDerivativeAtParameter()](../../d4/da9/classPart_1_1Geom2dCurve.html#a35de5f9700b21a1f07976948b41b22ca),
[femexamples.constraint_centrif.setup()](../../d1/def/namespacefemexamples_1_1constraint__centrif.html#a8714216d2d1b79c63ba3e4c52a742b4b),
[femexamples.material_nl_platewithhole.setup()](../../d7/d07/namespacefemexamples_1_1material__nl__platewithhole.html#a118c2cb8ccb8aac25048b9d52c0c9be2),
[femexamples.rc_wall_2d.setup()](../../df/dd4/namespacefemexamples_1_1rc__wall__2d.html#a54a2b12c1665428691517d281655ec84),
[femexamples.thermomech_flow1d.setup()](../../de/d40/namespacefemexamples_1_1thermomech__flow1d.html#a4189f8ec5b45f6645fcae656bef6882d),
[femexamples.truss_3d_cs_circle_ele_seg3.setup()](../../da/d29/namespacefemexamples_1_1truss__3d__cs__circle__ele__seg3.html#a722938de133994bbcf6ae1eafa2bfec0),
[PartGui::DimensionLinear.setupDimension()](../../d7/d39/classPartGui_1_1DimensionLinear.html#a7f6291721a252174696773093f700632),
[VISCOUS_2D::_ProxyMeshOfFace::_EdgeSubMesh.SetUVPtStructVec()](../../de/d2c/structVISCOUS__2D_1_1__ProxyMeshOfFace_1_1__EdgeSubMesh.html#ae898425988fa6ef1dd46fac8c0a40a8b),
[App::PropertyVector.setValue()](../../d5/d2b/classApp_1_1PropertyVector.html#a866a1f59e997434cbe7e642af74301db),
[StdMeshers_ProjectionUtils::TrsfFinder2D.Solve()](../../de/d7f/classStdMeshers__ProjectionUtils_1_1TrsfFinder2D.html#a018573f5ea96582ec96879eeb4c8c7a7),
[StdMeshers_ProjectionUtils::TrsfFinder3D.Solve()](../../df/dab/classStdMeshers__ProjectionUtils_1_1TrsfFinder3D.html#a126af541b14e572fa3862dec0fd46c4b),
[FemGui::TaskPostDataAtPoint.TaskPostDataAtPoint()](../../d9/da7/classFemGui_1_1TaskPostDataAtPoint.html#a442bb680fc74fbe236c0415717eb94a4),
[Base::DualQuat.theta()](../../d4/d13/classBase_1_1DualQuat.html#afaacd34fe231ad51c33082007bd96d29),
[Data::ComplexGeoData.transformToInside()](../../d8/daf/classData_1_1ComplexGeoData.html#a8b0cc05d2cf2ab2a1bb36e7f2a70949e),
[Data::ComplexGeoData.transformToOutside()](../../d8/daf/classData_1_1ComplexGeoData.html#a110e28b6e4651ae8b1683c9a31f365b1),
[Part::Geometry.translate()](../../dc/df0/classPart_1_1Geometry.html#a18252e22ce3f756c8376ad27b7899e8d),
[Sketcher::ExternalGeometryFacade.translate()](../../dd/d90/classSketcher_1_1ExternalGeometryFacade.html#a7cb1449b6fc416d91688ca1b237856bb),
[Sketcher::GeometryFacade.translate()](../../d1/d73/classSketcher_1_1GeometryFacade.html#a16be74dd72b07ef5e7d4cef37b81261e),
[FemGui::TaskPostBox.updateEnumerationList()](../../dc/d51/classFemGui_1_1TaskPostBox.html#a4e76081ba79f5c1702744d08957b2f07),
[FemGui::ViewProviderFemPostFunctionProvider.updateSize()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#ad783f019da5429b4ca0669a14d606d72),
[TechDraw::DrawUtil.vecRotate()](../../da/d23/classTechDraw_1_1DrawUtil.html#aac1da77931bff55f92121b1c93c19919),
and
[zipios.writeByteSeq()](../../de/d29/namespacezipios.html#ac06c2178288ac6f9b393ff7c3697fb92).

## ◆ wiresIntersect()

def draftgeoutils.intersections.wiresIntersect  | ( |  | _wire1_ ,   
---|---|---|---  
|  |  | _wire2_  
| ) | |   
      
    
    Return True if some of the edges of the wires are intersecting.
    
    Otherwise return `False`.
    

References
[draftgeoutils.intersections.findIntersection()](../../d9/dfd/group__draftgeoutils.html#gab253783ec92c49203fd7b110271b887d).

Referenced by
[draftgeoutils.offsets.pocket2d()](../../d9/dfd/group__draftgeoutils.html#ga65736a1b5af4c622ee3f176a7a288703).

## Variable Documentation

## ◆ getNormal

def draftgeoutils.geometry.getNormal =
[get_normal](../../d9/dfd/group__draftgeoutils.html#ga961c798fb852e8bcdbae5a5e42fc0d2a)  
---  
  
Referenced by
[Attacher::AttachEngine3D.calculateAttachedPlacement()](../../d1/db7/classAttacher_1_1AttachEngine3D.html#a91a8ba76ea3bef1c30c2d3caa5f3ed98),
and
[SketcherGui::EditModeConstraintCoinManager.processConstraints()](../../db/dab/classSketcherGui_1_1EditModeConstraintCoinManager.html#a86abd481aa8756c9ea61b10d2e624804).

## ◆ getSplineNormal

def draftgeoutils.geometry.getSplineNormal =
[get_spline_normal](../../d9/dfd/group__draftgeoutils.html#ga871b3414feb189f4255dae897ee3b684)  
---  
  
## ◆ isCoplanar

def draftgeoutils.faces.isCoplanar =
[is_coplanar](../../d9/dfd/group__draftgeoutils.html#gac12735fced2e5e984d015b18ed430a5f)  
---  
  
## ◆ isLine

def draftgeoutils.edges.isLine =
[is_line](../../d9/dfd/group__draftgeoutils.html#ga3b53489edbb1dbef670e655e27b02266)  
---  
  
Referenced by
[draftgeoutils.wires.cleanProjection()](../../d9/dfd/group__draftgeoutils.html#gaeac487c387428b021095f192162bf91f),
[draftgeoutils.edges.invert()](../../d9/dfd/group__draftgeoutils.html#ga60dc82b8b95b16ffa97e1ccd715f099e),
and
[draftgeoutils.sort_edges.sortEdgesOld()](../../d9/dfd/group__draftgeoutils.html#ga640ea179c9c4532c2fbab83a64556bc3).

## ◆ isPlanar

def draftgeoutils.geometry.isPlanar =
[is_planar](../../d9/dfd/group__draftgeoutils.html#ga2ab2c7e349dc6e0f5cfe19e9fd1608c4)  
---  
  
Referenced by
[ReverseEngineeringGui::Segmentation.accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
and
[TechDraw::EdgeWalker.perform()](../../d0/d49/classTechDraw_1_1EdgeWalker.html#ab8b30e7077326603844029c537a7ece2).

## ◆ NORM

draftgeoutils.general.NORM = App.Vector(0, 0, 1)  
---  
  
## ◆ PARAMGRP

draftgeoutils.general.PARAMGRP = App.ParamGet("User
parameter:BaseApp/Preferences/Mod/Draft")  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

