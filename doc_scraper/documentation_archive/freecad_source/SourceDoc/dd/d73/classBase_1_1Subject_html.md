---
url: https://freecad.github.io/SourceDoc/dd/d73/classBase_1_1Subject.html
scraped_at: 2025-09-08T15:17:27.152655
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [Subject](../../dd/d73/classBase_1_1Subject.html)

[List of all members](../../de/dc0/classBase_1_1Subject-members.html) | Public Types | Public Member Functions

Base::Subject< _MessageType > Class Template Reference

[Subject](../../dd/d73/classBase_1_1Subject.html "Subject class Implementation
of the well known Observer Design Pattern.") class Implementation of the well
known [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Design Pattern.
[More...](../../dd/d73/classBase_1_1Subject.html#details)

`#include <Observer.h>`

##  Public Types  
  
---  
typedef _MessageType | [MessageType](../../dd/d73/classBase_1_1Subject.html#a64dbd963ab6f449d073fd9b56cc277ff)  
typedef [Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > | [ObserverType](../../dd/d73/classBase_1_1Subject.html#a058e5801b048ef298c5a58089a669f81)  
typedef [Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType > | [SubjectType](../../dd/d73/classBase_1_1Subject.html#a1c16f19b95c6fb0c33976ebb62a55b06)  
  
##  Public Member Functions  
  
---  
void | [Attach](../../dd/d73/classBase_1_1Subject.html#a18d9738775b42358d60a51103f25b52e) ([Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > *ToObserv)  
| Attach an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Attach an
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") to the list of
Observers which get called when Notify is called.
[More...](../../dd/d73/classBase_1_1Subject.html#a18d9738775b42358d60a51103f25b52e)  
  
void | [ClearObserver](../../dd/d73/classBase_1_1Subject.html#a95ae83a504ff81535df788d42864ac75) ()  
| Clears the list of all registered observers.
[More...](../../dd/d73/classBase_1_1Subject.html#a95ae83a504ff81535df788d42864ac75)  
  
void | [Detach](../../dd/d73/classBase_1_1Subject.html#afb48202759faa41b2fafe1311f8fd827) ([Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > *ToObserv)  
| Detach an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Detach an
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") from the list of
Observers which get called when Notify is called.
[More...](../../dd/d73/classBase_1_1Subject.html#afb48202759faa41b2fafe1311f8fd827)  
  
[Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > * | [Get](../../dd/d73/classBase_1_1Subject.html#a99233b1537a7a8a9603bb4bb3de9c992) (const char *Name)  
| Get an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") by name Get a
observer by name if the observer reimplements the Name() mthode.
[More...](../../dd/d73/classBase_1_1Subject.html#a99233b1537a7a8a9603bb4bb3de9c992)  
  
void | [Notify](../../dd/d73/classBase_1_1Subject.html#aa5353b733daa35b204f2990b34300b28) (_MessageType rcReason)  
| Notify all Observers Send a message to all Observers attached to this
subject.
[More...](../../dd/d73/classBase_1_1Subject.html#aa5353b733daa35b204f2990b34300b28)  
  
|
[Subject](../../dd/d73/classBase_1_1Subject.html#aba3f1e5f121fba02983c8350360022b3)
()  
| A constructor.
[More...](../../dd/d73/classBase_1_1Subject.html#aba3f1e5f121fba02983c8350360022b3)  
  
virtual | [~Subject](../../dd/d73/classBase_1_1Subject.html#aa7fda8a9539b0eb3f83e32a60de6f2a1) ()  
| A destructor.
[More...](../../dd/d73/classBase_1_1Subject.html#aa7fda8a9539b0eb3f83e32a60de6f2a1)  
  
  
## Detailed Description

template<class _MessageType>  
class Base::Subject< _MessageType >

[Subject](../../dd/d73/classBase_1_1Subject.html "Subject class Implementation
of the well known Observer Design Pattern.") class Implementation of the well
known [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Design Pattern.

The observed object, which inherit FCSubject, will call all its observers in
case of changes. A observer class has to Attach itself to the observed object.

See also

    FCObserver 

## Member Typedef Documentation

## ◆ MessageType

template<class _MessageType >

typedef _MessageType [Base::Subject](../../dd/d73/classBase_1_1Subject.html)<
_MessageType >::MessageType  
---  
  
## ◆ ObserverType

template<class _MessageType >

typedef [Observer](../../de/d63/classBase_1_1Observer.html)<_MessageType>
[Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType
>::ObserverType  
---  
  
## ◆ SubjectType

template<class _MessageType >

typedef [Subject](../../dd/d73/classBase_1_1Subject.html)<_MessageType>
[Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType
>::SubjectType  
---  
  
## Constructor & Destructor Documentation

## ◆ Subject()

template<class _MessageType >

[Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::Subject  | ( | | ) |   
---|---|---|---|---  
  
A constructor.

No special function so far.

## ◆ ~Subject()

template<class _MessageType >

| virtual [Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::~[Subject](../../dd/d73/classBase_1_1Subject.html) | ( | | ) |   
---|---|---|---|---  
virtual  
  
A destructor.

No special function so far.

## Member Function Documentation

## ◆ Attach()

template<class _MessageType >

void [Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::Attach  | ( | [Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > *  | _ToObserv_| ) |   
---|---|---|---|---|---  
  
Attach an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Attach an
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") to the list of
Observers which get called when Notify is called.

Parameters

     ToObserv| A pointer to a concrete [Observer](../../de/d63/classBase_1_1Observer.html "Observer class Implementation of the well known Observer Design Pattern.")  
---|---  
  
See also

    [Notify](../../dd/d73/classBase_1_1Subject.html#aa5353b733daa35b204f2990b34300b28 "Notify all Observers Send a message to all Observers attached to this subject.")

Referenced by
[InspectionGui::ViewProviderInspection::attach()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a79ac9ba624d2a99d8753d7ee9c7a96ad),
[MeshGui::ViewProviderMeshCurvature::attach()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad36ed9ef7edb7c4ec98d622ec6acf48c),
[FemGui::ViewProviderFemPostObject::attach()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a7dcf3dc1b7f85846e5b50cc08c7f1f46),
[SketcherGui::CurveConverter::CurveConverter()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#aedc47aa90240b39482d98c65c03197b3),
[Gui::Dialog::DlgDisplayPropertiesImp::DlgDisplayPropertiesImp()](../../df/ddf/classGui_1_1Dialog_1_1DlgDisplayPropertiesImp.html#af58cc9d688ef2c00f1184a67885e1182),
[Gui::EditorView::EditorView()](../../d4/d22/classGui_1_1EditorView.html#ae555ce1d01e06abd78b5b900fc23a689),
[Gui::GraphicsView3D::GraphicsView3D()](../../df/d0b/classGui_1_1GraphicsView3D.html#ad33d0c8f32b37ee2eff8e67494289edc),
[Gui::MacroManager::MacroManager()](../../d8/dc6/classGui_1_1MacroManager.html#a8edd22e269321504a4cbc24abb9e0043),
[NaviCubeImplementation::NaviCubeImplementation()](../../df/dc9/classNaviCubeImplementation.html#acee51772b372c1463da029f32da4ff12),
[TechDrawGui::QGVPage::Private::Private()](../../d8/d45/classQGVPage_1_1Private.html#a1a30d738251acaf2c30286e03ee87ab4),
[Gui::RecentFilesAction::Private::Private()](../../de/de4/classRecentFilesAction_1_1Private.html#a98620a9fe8680c05d704e96b252eae10),
[Gui::PythonConsole::PythonConsole()](../../d2/da0/classGui_1_1PythonConsole.html#a942d5225bd06c12a2fa25171ce476537),
[Gui::DockWnd::ReportOutput::ReportOutput()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a33a19a15d61085fb3211e7fb522c5fe3),
[Gui::StatefulLabel::setParameterGroup()](../../d8/d55/classGui_1_1StatefulLabel.html#a993db8f4a3b78c34b628eb4ee7c66b1e),
[Gui::PrefWidget::setParamGrpPath()](../../d9/d6b/classGui_1_1PrefWidget.html#ab28015e438a648affba1609c94b67861),
[Gui::AbstractSplitView::setupSettings()](../../d1/d0b/classGui_1_1AbstractSplitView.html#a76ecde0106d10edd50dff4f8bf8c448d),
[Gui::SplitView3DInventor::SplitView3DInventor()](../../da/d73/classGui_1_1SplitView3DInventor.html#ac6e97f0b7618f77a3a700db0c4ef9fc8),
[Gui::StatefulLabel::StatefulLabel()](../../d8/d55/classGui_1_1StatefulLabel.html#a9b627760a5b1c14738bc1dff671b62cf),
[Gui::StatusBarObserver::StatusBarObserver()](../../de/da6/classGui_1_1StatusBarObserver.html#ab05c62ce1106cffcd17c95732f6fd84d),
[Gui::TaskView::TaskAppearance::TaskAppearance()](../../d6/d8d/classGui_1_1TaskView_1_1TaskAppearance.html#a22f06e7b6366730aacf3d59115d603b5),
[Gui::TaskView::TaskSelectLinkProperty::TaskSelectLinkProperty()](../../d3/d1b/classGui_1_1TaskView_1_1TaskSelectLinkProperty.html#a6ec8c7b8e4d45bde4f8ce5968bdd91b4),
[Gui::TaskView::TaskSketcherCreateCommands::TaskSketcherCreateCommands()](../../d7/d1e/classGui_1_1TaskView_1_1TaskSketcherCreateCommands.html#a5c9c29e2f81d57fec80f3d7166ba8782),
[SketcherGui::TaskSketcherGeneral::TaskSketcherGeneral()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#acb35aefc057b31af4b7c6e9c87e1f0d4),
[Gui::TaskView::TaskView::TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#aa4e4f7cddfbcf1ddfc35ce4cec275b73),
[Gui::TextEditor::TextEditor()](../../de/d6e/classGui_1_1TextEditor.html#a01bf807b388aeb46fae36d32910eede0),
[Gui::TreeParams::TreeParams()](../../d0/dc9/classGui_1_1TreeParams.html#a5295206bb6c787328f8f01fa04af7bba),
[Gui::View3DInventor::View3DInventor()](../../da/d75/classGui_1_1View3DInventor.html#ac60eed69033bfadaa166619bc01f8956),
[Gui::ViewParams::ViewParams()](../../d3/d88/classGui_1_1ViewParams.html#a6d3fd098b5f3a3b421768c2130693e4e),
[FemGui::ViewProviderFemPostObject::ViewProviderFemPostObject()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a7611a4e7f63ddc0f13c45d7ca94c788a),
[InspectionGui::ViewProviderInspection::ViewProviderInspection()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ad65a72d037529a1c5c642753ec769add),
and
[MeshGui::ViewProviderMeshCurvature::ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a7204bf34002b635b512efe925c011963).

## ◆ ClearObserver()

template<class _MessageType >

void [Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::ClearObserver  | ( | | ) |   
---|---|---|---|---  
  
Clears the list of all registered observers.

Note

    Using this function in your code may be an indication of design problems. 

## ◆ Detach()

template<class _MessageType >

void [Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::Detach  | ( | [Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > *  | _ToObserv_| ) |   
---|---|---|---|---|---  
  
Detach an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") Detach an
[Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") from the list of
Observers which get called when Notify is called.

Parameters

     ToObserv| A pointer to a concrete [Observer](../../de/d63/classBase_1_1Observer.html "Observer class Implementation of the well known Observer Design Pattern.")  
---|---  
  
See also

    [Notify](../../dd/d73/classBase_1_1Subject.html#aa5353b733daa35b204f2990b34300b28 "Notify all Observers Send a message to all Observers attached to this subject.")

Referenced by
[InspectionGui::ViewProviderInspection::attach()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a79ac9ba624d2a99d8753d7ee9c7a96ad),
[MeshGui::ViewProviderMeshCurvature::attach()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad36ed9ef7edb7c4ec98d622ec6acf48c),
[FemGui::ViewProviderFemPostObject::attach()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a7dcf3dc1b7f85846e5b50cc08c7f1f46),
[Gui::AbstractSplitView::~AbstractSplitView()](../../d1/d0b/classGui_1_1AbstractSplitView.html#a39117b0e38b6beb30eb4d6de1472298c),
[SketcherGui::CurveConverter::~CurveConverter()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#ac4b31b0695f009bdc0e6464928d87c37),
[Gui::Dialog::DlgDisplayPropertiesImp::~DlgDisplayPropertiesImp()](../../df/ddf/classGui_1_1Dialog_1_1DlgDisplayPropertiesImp.html#a3c673eed36528133fc283c1aaa80e523),
[Gui::EditorView::~EditorView()](../../d4/d22/classGui_1_1EditorView.html#a93aa10f260e4b89d7502c309cace2072),
[Gui::GraphicsView3D::~GraphicsView3D()](../../df/d0b/classGui_1_1GraphicsView3D.html#adce10817027d1d136884f2278b73fcb2),
[NaviCubeImplementation::~NaviCubeImplementation()](../../df/dc9/classNaviCubeImplementation.html#aa84bddf0834589682f482c0b30a753b1),
[Gui::PrefWidget::~PrefWidget()](../../d9/d6b/classGui_1_1PrefWidget.html#a0c226117759d11941c75a7c421b09281),
[Gui::RecentFilesAction::Private::~Private()](../../de/de4/classRecentFilesAction_1_1Private.html#aa7ce238bc1315e21c931c26753211f49),
[Gui::PythonConsole::~PythonConsole()](../../d2/da0/classGui_1_1PythonConsole.html#a6720c67a127a332649f6d6556c558030),
[Gui::PythonEditor::~PythonEditor()](../../dd/dcb/classGui_1_1PythonEditor.html#a567aaa157b338f26a00feeb2d85ddc2b),
[Gui::DockWnd::ReportOutput::~ReportOutput()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#ab46b58f001ac3135ce4c6a97f225d556),
[Gui::StatusBarObserver::~StatusBarObserver()](../../de/da6/classGui_1_1StatusBarObserver.html#a5223f31e9b6ac7e865e66b413525a8c2),
[Gui::TaskView::TaskAppearance::~TaskAppearance()](../../d6/d8d/classGui_1_1TaskView_1_1TaskAppearance.html#a970eafd9dbc2ad72089e78e8165be538),
[Gui::TaskView::TaskSelectLinkProperty::~TaskSelectLinkProperty()](../../d3/d1b/classGui_1_1TaskView_1_1TaskSelectLinkProperty.html#afa0c99174c177254a097f747b8b8fe81),
[Gui::TaskView::TaskSketcherCreateCommands::~TaskSketcherCreateCommands()](../../d7/d1e/classGui_1_1TaskView_1_1TaskSketcherCreateCommands.html#a41805181e5b0510fe8466d11f1a677eb),
[SketcherGui::TaskSketcherGeneral::~TaskSketcherGeneral()](../../d6/d6e/classSketcherGui_1_1TaskSketcherGeneral.html#afa760cf3bfcf62238d1ccdacd399b17b),
[Gui::TaskView::TaskView::~TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#a7a914c394b51c4e89b5e9e4dc34039a0),
[Gui::TextEditor::~TextEditor()](../../de/d6e/classGui_1_1TextEditor.html#a67cc14c174c7b66738c40f844d4dd7d7),
[Gui::View3DInventor::~View3DInventor()](../../da/d75/classGui_1_1View3DInventor.html#ac962d8b824c5c4d1d1034182f656fcf5),
[FemGui::ViewProviderFemPostObject::~ViewProviderFemPostObject()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5af537f5c58626a42bfdde2500cbb33f),
[InspectionGui::ViewProviderInspection::~ViewProviderInspection()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a2e13185c55e6841851af3fb00043eee7),
and
[MeshGui::ViewProviderMeshCurvature::~ViewProviderMeshCurvature()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a8c25fe47cc3bfd95d1f82c450ed80d83).

## ◆ Get()

template<class _MessageType >

[Observer](../../de/d63/classBase_1_1Observer.html)< _MessageType > * [Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::Get  | ( | const char *  | _Name_| ) |   
---|---|---|---|---|---  
  
Get an [Observer](../../de/d63/classBase_1_1Observer.html "Observer class
Implementation of the well known Observer Design Pattern.") by name Get a
observer by name if the observer reimplements the Name() mthode.

See also

    [Observer](../../de/d63/classBase_1_1Observer.html "Observer class Implementation of the well known Observer Design Pattern.")

## ◆ Notify()

template<class _MessageType >

void [Base::Subject](../../dd/d73/classBase_1_1Subject.html)< _MessageType >::Notify  | ( | _MessageType  | _rcReason_| ) |   
---|---|---|---|---|---  
  
Notify all Observers Send a message to all Observers attached to this subject.

The Message depends on the implementation of a concrete Oberserver and
[Subject](../../dd/d73/classBase_1_1Subject.html "Subject class Implementation
of the well known Observer Design Pattern.").

See also

    [Notify](../../dd/d73/classBase_1_1Subject.html#aa5353b733daa35b204f2990b34300b28 "Notify all Observers Send a message to all Observers attached to this subject.")

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644).

Referenced by
[InspectionGui::ViewProviderInspection::attach()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a79ac9ba624d2a99d8753d7ee9c7a96ad),
[MeshGui::ViewProviderMeshCurvature::attach()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad36ed9ef7edb7c4ec98d622ec6acf48c),
[FemGui::ViewProviderFemPostObject::attach()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a7dcf3dc1b7f85846e5b50cc08c7f1f46),
[InspectionGui::ViewProviderInspection::onChanged()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[Gui::PrefWidget::onSave()](../../d9/d6b/classGui_1_1PrefWidget.html#a567a0f8cfa885ba8fb05e85f68fe596a),
[Gui::DockWnd::ReportOutput::ReportOutput()](../../d9/d6e/classGui_1_1DockWnd_1_1ReportOutput.html#a33a19a15d61085fb3211e7fb522c5fe3),
and
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/Observer.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

