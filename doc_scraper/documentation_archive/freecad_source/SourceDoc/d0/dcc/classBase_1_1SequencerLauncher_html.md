---
url: https://freecad.github.io/SourceDoc/d0/dcc/classBase_1_1SequencerLauncher.html
scraped_at: 2025-09-08T15:17:16.104314
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html)

[List of all members](../../dc/d66/classBase_1_1SequencerLauncher-members.html) | Public Member Functions

Base::SequencerLauncher Class Reference

The [SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html "The
SequencerLauncher class is provided for convenience.") class is provided for
convenience.
[More...](../../d0/dcc/classBase_1_1SequencerLauncher.html#details)

`#include <Sequencer.h>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [next](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a) ([bool](../../d9/db9/classbool.html) canAbort=false)  
size_t | [numberOfSteps](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab9458a363b7531131baafbd060f12608) () const  
|
[SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html#a1f72a046f7e9bab1995df453593d969d)
(const char *pszStr, size_t steps)  
void | [setProgress](../../d0/dcc/classBase_1_1SequencerLauncher.html#a74937014111344719ab100ed721b1e16) (size_t)  
void | [setText](../../d0/dcc/classBase_1_1SequencerLauncher.html#a5a3b21d5fbeeb1c5ab6d91b55b724950) (const char *pszTxt)  
[bool](../../d9/db9/classbool.html) | [wasCanceled](../../d0/dcc/classBase_1_1SequencerLauncher.html#a3dd373a3859ced0145dccc176b5ab3a0) () const  
|
[~SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html#a7471e6530431b1805b27d0e2af90b7a3)
()  
  
## Detailed Description

The [SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html "The
SequencerLauncher class is provided for convenience.") class is provided for
convenience.

It allows you to run an instance of the sequencer by instantiating an object
of this class – most suitable on the stack. So this mechanism can be used for
try-catch-blocks to destroy the object automatically if the C++ exception
mechanism cleans up the stack.

This class has been introduced to simplify the use with the sequencer. In the
FreeCAD [Gui](../../d9/dad/namespaceGui.html "The FreeCAD Graphical interface
layer.") layer there is a subclass of
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html "This class gives
the user an indication of the progress of an operation and it is used to
reassure hi...") called ProgressBar that grabs the keyboard and filters most
of the incoming events. If the programmer uses the API of
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html "This class gives
the user an indication of the progress of an operation and it is used to
reassure hi...") directly to start an instance without due diligence with
exceptions then a not handled exception could block the whole application –
the user has to kill the application then.

Below is an example of a not correctly used sequencer.

#include <Base/Sequencer.h>

void runOperation();

void myTest()

{

try{

runOperation();

} catch(...) {

// the programmer forgot to stop the sequencer here

// Under circumstances the sequencer never gets stopped so the keyboard never
gets ungrabbed and

// all Gui events still gets filtered.

}

}

void runOperation()

{

[Base::Sequencer](../../db/d07/namespaceBase.html#a975e0274696620c14016b8c54fe7634e
"Access to the only SequencerBase
instance.")().[start](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b
"Starts a new operation, returns false if there is already a pending
operation, otherwise it returns t...") ("my text", 10);

for (int i=0;
[i](../../d3/d10/namespaceSplineSurface.html#af6f043267a3c4e6ea7fe3b2466b50d21)<10;
[i](../../d3/d10/namespaceSplineSurface.html#af6f043267a3c4e6ea7fe3b2466b50d21)++)

{

// do something where an exception be thrown

...

[Base::Sequencer](../../db/d07/namespaceBase.html#a975e0274696620c14016b8c54fe7634e
"Access to the only SequencerBase
instance.")().[next](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac
"Performs the next step and returns true if the operation is not yet
finished.") ();

}

[Base::Sequencer](../../db/d07/namespaceBase.html#a975e0274696620c14016b8c54fe7634e
"Access to the only SequencerBase
instance.")().[stop](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303
"Stops the sequencer if all operations are finished.") ();

}

To avoid such problems the
[SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html "The
SequencerLauncher class is provided for convenience.") class can be used as
follows:

#include <Base/Sequencer.h>

void runOperation();

void myTest()

{

try{

runOperation();

} catch(...) {

// the programmer forgot to halt the sequencer here

// If SequencerLauncher leaves its scope the object gets destructed
automatically and

// stops the running sequencer.

}

}

void runOperation()

{

// create an instance on the stack (not on any terms on the heap)

[SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html#a1f72a046f7e9bab1995df453593d969d)
seq("my text", 10);

for (int i=0;
[i](../../d3/d10/namespaceSplineSurface.html#af6f043267a3c4e6ea7fe3b2466b50d21)<10;
[i](../../d3/d10/namespaceSplineSurface.html#af6f043267a3c4e6ea7fe3b2466b50d21)++)

{

// do something (e.g. here can be thrown an exception)

...

seq.next ();

}

}

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ SequencerLauncher()

SequencerLauncher::SequencerLauncher  | ( | const char *  | _pszStr_ ,   
---|---|---|---  
|  | size_t  | _steps_  
| ) | |   
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0),
and
[Base::SequencerBase::start()](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b).

## ◆ ~SequencerLauncher()

SequencerLauncher::~SequencerLauncher  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0),
and
[Base::SequencerBase::stop()](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303).

## Member Function Documentation

## ◆ next()

[bool](../../d9/db9/classbool.html) SequencerLauncher::next  | ( | [bool](../../d9/db9/classbool.html) | _canAbort_ = `false`| ) |   
---|---|---|---|---|---  
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0),
and
[Base::SequencerBase::next()](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac).

Referenced by
[CmdTestProgress1::activated()](../../df/d86/classCmdTestProgress1.html#a04caeda64708ef7219af52c30378bae4),
[CmdTestProgress2::activated()](../../dd/d0f/classCmdTestProgress2.html#a380cbcfd94a9246194b16ea7412a8c41),
[CmdTestProgress3::activated()](../../d1/de0/classCmdTestProgress3.html#a714b214f572b4722ec60a9994e9c7663),
[CmdTestProgress4::activated()](../../dc/d04/classCmdTestProgress4.html#ad7aa6ffccb5a17e559783304522b2dec),
[PartGui::CrossSections::apply()](../../dc/d84/classPartGui_1_1CrossSections.html#a448e9bda9e7d893edf0520bbcff985b0),
[Reen::BSplineParameterCorrection::CalcFirstSmoothMatrix()](../../de/d74/classReen_1_1BSplineParameterCorrection.html#aa90fddfef9d5763c917373de139ce44f),
[Reen::BSplineParameterCorrection::CalcSecondSmoothMatrix()](../../de/d74/classReen_1_1BSplineParameterCorrection.html#aa029e42aff357ec269498ff74182e462),
[Reen::BSplineParameterCorrection::CalcThirdSmoothMatrix()](../../de/d74/classReen_1_1BSplineParameterCorrection.html#aa4194be297542deca96e53b351e6f460),
[MeshCore::MeshAlgorithm::CheckFacets()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#ac8032a5a0a06cee43035edcb9253b731),
[MeshCore::MeshTrimming::CheckFacets()](../../d3/da1/classMeshCore_1_1MeshTrimming.html#a94a5bf3ea3f16d468c08906a5dcbb472),
[MeshCore::MeshCurvature::ComputePerFace()](../../d3/d7e/classMeshCore_1_1MeshCurvature.html#a97ba030abe06bd5b51f0b1a09c3ea3b6),
[Reen::BSplineParameterCorrection::DoParameterCorrection()](../../de/d74/classReen_1_1BSplineParameterCorrection.html#a36ce85401c8876fb595bfb4071756b72),
[MeshCore::MeshEvalTopology::Evaluate()](../../db/d16/classMeshCore_1_1MeshEvalTopology.html#a918ae73126314eae2ae1fb5406c5f067),
[MeshCore::MeshEvalSelfIntersection::Evaluate()](../../de/de7/classMeshCore_1_1MeshEvalSelfIntersection.html#a31ff983718a68a3c58463d34ebacfd38),
[MeshCore::MeshEvalNeighbourhood::Evaluate()](../../d6/d6e/classMeshCore_1_1MeshEvalNeighbourhood.html#abada32db6ae6bded5c86989d27f5c407),
[Inspection::Feature::execute()](../../d6/d23/classInspection_1_1Feature.html#aae33bbcb93f32a5c46bd78ac1d25a68e),
[Robot::Edge2TracObject::execute()](../../d8/df5/classRobot_1_1Edge2TracObject.html#a05d96baf25af72c1c01f165a8dac7f63),
[MeshCore::MeshAlgorithm::GetFacetsFromToolMesh()](../../de/db5/classMeshCore_1_1MeshAlgorithm.html#a418668b353984ce121b51244b8c64c90),
[MeshCore::MeshEvalNeighbourhood::GetIndices()](../../d6/d6e/classMeshCore_1_1MeshEvalNeighbourhood.html#a19d14d8595ff757ac18d8b100e425176),
[MeshCore::MeshIntersection::getIntersection()](../../d7/d73/classMeshCore_1_1MeshIntersection.html#a439ec08eda51ea85c9f253eec6571150),
[MeshCore::MeshEvalSelfIntersection::GetIntersections()](../../de/de7/classMeshCore_1_1MeshEvalSelfIntersection.html#a591a3a6b5c52bd9d91f814cea4140f78),
[Part::ImportIgesParts()](../../d2/db9/namespacePart.html#a10322b892abc3b1779054dacf1a49e53),
[Points::PointsAlgos::LoadAscii()](../../d8/d62/classPoints_1_1PointsAlgos.html#a75d94f79566c5ebb47f14fbafa6be26e),
[MeshCore::MeshInput::LoadInventor()](../../d9/d08/classMeshCore_1_1MeshInput.html#acf19f4238be1fd7d9f3b260af125d599),
[MeshPart::CurveProjectorWithToolMesh::makeToolMesh()](../../d8/dd2/classMeshPart_1_1CurveProjectorWithToolMesh.html#aa0428e1cea062658a882b2b5e3b9e05b),
[App::Application::openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728),
[MeshPart::CurveProjectorSimple::projectCurve()](../../db/d5f/classMeshPart_1_1CurveProjectorSimple.html#a5932b3a0d0a1ee7119cc7f7b5f180ef8),
[MeshPart::MeshProjection::projectEdgeToEdge()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#a322496a26bba88d2ff370beef12fdc3b),
[MeshPart::MeshProjection::projectOnMesh()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#ab0dd5abefe9189817d0798f118f88130),
[MeshPart::MeshProjection::projectParallelToMesh()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#ab58703eaddaaad128b4477ea26606526),
[MeshPart::MeshProjection::projectToMesh()](../../d7/dc0/classMeshPart_1_1MeshProjection.html#ada4576e6864dd8dfdae7c8917d88d069),
[Base::XMLReader::readFiles()](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16),
[BarThread::run()](../../d8/d7c/classBarThread.html#a8c0683b02f7de1024ed7a69daef8b132),
[Sandbox::WorkerThread::run()](../../d9/d50/classSandbox_1_1WorkerThread.html#ab1b55d37c2317d8799cd65ee864f7d8b),
[MeshCore::MeshOutput::SaveAsciiSTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#a978a9f0a89ca5ce4d828305f005de62b),
[MeshCore::MeshOutput::SaveBinarySTL()](../../db/d14/classMeshCore_1_1MeshOutput.html#aa319df520ea268406d3a19a1c4a4f198),
[MeshCore::MeshOutput::SaveInventor()](../../db/d14/classMeshCore_1_1MeshOutput.html#a097213739acdfb39de57ebc2f32f9908),
[MeshCore::MeshOutput::SaveNastran()](../../db/d14/classMeshCore_1_1MeshOutput.html#a832d24717641893b591f5b4d99db9e3f),
[MeshCore::MeshOutput::SaveOBJ()](../../db/d14/classMeshCore_1_1MeshOutput.html#a3d771358cea3ae77d666c54aba2692b5),
[MeshCore::MeshOutput::SaveOFF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8b4f5b020dd2b94b087ff831b7aee3c4),
[MeshCore::MeshOutput::SaveSMF()](../../db/d14/classMeshCore_1_1MeshOutput.html#a7b44d31efb50a5d64b2b08fbcc91963f),
[MeshCore::MeshOutput::SaveVRML()](../../db/d14/classMeshCore_1_1MeshOutput.html#a8fc229d0641d58846478dbcaa077e8db),
[MeshCore::MeshTrimming::TrimFacets()](../../d3/da1/classMeshCore_1_1MeshTrimming.html#a4daef4509d0ba0657601bacdb24e2b33),
[Raytracing::LuxTools::writeShape()](../../df/d50/classRaytracing_1_1LuxTools.html#ae5e2c25c3216bd520322b92ff59b4024),
[Raytracing::PovTools::writeShape()](../../d8/dea/classRaytracing_1_1PovTools.html#ad4d1b78b49ac76c10b29747c29074469),
and
[Raytracing::PovTools::writeShapeCSV()](../../d8/dea/classRaytracing_1_1PovTools.html#ae8dda49406724df95d7687d57c3a2ebc).

## ◆ numberOfSteps()

size_t SequencerLauncher::numberOfSteps  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0),
and
[Base::SequencerBase::numberOfSteps()](../../d5/d0d/classBase_1_1SequencerBase.html#ae72645f88f8f398096187bb6877e6e34).

## ◆ setProgress()

void SequencerLauncher::setProgress  | ( | size_t  | _pos_| ) |   
---|---|---|---|---|---  
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0),
and
[Base::SequencerBase::setProgress()](../../d5/d0d/classBase_1_1SequencerBase.html#a20ca12713d51a8435bca90ce7cfa3ba7).

## ◆ setText()

void SequencerLauncher::setText  | ( | const char *  | _pszTxt_| ) |   
---|---|---|---|---|---  
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0),
and
[Base::SequencerBase::setText()](../../d5/d0d/classBase_1_1SequencerBase.html#ab666acb27961c1927c77a1a82a19879f).

## ◆ wasCanceled()

[bool](../../d9/db9/classbool.html) SequencerLauncher::wasCanceled  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::SequencerBase::Instance()](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d),
and
[Base::SequencerBase::wasCanceled()](../../d5/d0d/classBase_1_1SequencerBase.html#a3e0668144ea48ef7cd9040513bcc4b3c).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Sequencer.h
  * FreeCAD/src/Base/Sequencer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

