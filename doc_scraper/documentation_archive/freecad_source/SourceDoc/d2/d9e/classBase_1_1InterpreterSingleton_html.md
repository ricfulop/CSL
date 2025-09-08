---
url: https://freecad.github.io/SourceDoc/d2/d9e/classBase_1_1InterpreterSingleton.html
scraped_at: 2025-09-08T15:16:30.052258
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [InterpreterSingleton](../../d2/d9e/classBase_1_1InterpreterSingleton.html)

[List of all members](../../d4/de7/classBase_1_1InterpreterSingleton-members.html) | Public Member Functions

Base::InterpreterSingleton Class Reference

The Interpreter class This class manage the python interpreter and hold a lot
helper functions for handling python stuff.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#details)

`#include <Interpreter.h>`

##  Public Member Functions  
  
---  
|
[InterpreterSingleton](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae5e285d3f24a70615f26b85675c80984)
()  
|
[~InterpreterSingleton](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a3f8fe04dc15b06551618ad436b24e64a)
()  
execution methods  
std::string | [runString](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a2cabac4e610e966ebc33a1e1aa5d94b6) (const char *psCmd)  
| Run a statement on the python interpreter and gives back a string with the
representation of the result.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a2cabac4e610e966ebc33a1e1aa5d94b6)  
  
std::string | [runStringWithKey](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a4c280c31dede4ae71e9170f5a868c703) (const char *psCmd, const char *key, const char *key_initial_value="")  
| Run a statement on the python interpreter with a key for exchanging strings.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a4c280c31dede4ae71e9170f5a868c703)  
  
Py::Object | [runStringObject](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6bf9609cdfb997f7c97a7b335d8c138b) (const char *sCmd)  
| Run a statement on the python interpreter and return back the result object.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6bf9609cdfb997f7c97a7b335d8c138b)  
  
void | [runInteractiveString](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ad1959d99451e06fdc2c20da250235de8) (const char *psCmd)  
| Run a statement on the python interpreter and gives back a string with the
representation of the result.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ad1959d99451e06fdc2c20da250235de8)  
  
void | [runFile](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae05d01943aa268be77244fa1e98e88f0) (const char *pxFileName, [bool](../../d9/db9/classbool.html) local)  
| Run file (script) on the python interpreter.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae05d01943aa268be77244fa1e98e88f0)  
  
void | [runStringArg](../../d2/d9e/classBase_1_1InterpreterSingleton.html#afff9e462cde2ead702ab1ff0f5ddbbad) (const char *psCom,...)  
| Run a statement with arguments on the python interpreter.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#afff9e462cde2ead702ab1ff0f5ddbbad)  
  
void | [runMethodVoid](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a91c0c86f52316b4f3191f7817ecf8365) ([PyObject](../../df/d1b/classPyObject.html) *pobject, const char *method)  
| runs a python object method with no return value and no arguments
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a91c0c86f52316b4f3191f7817ecf8365)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [runMethodObject](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6b1f62ad4b5abacc7636d2ec0ad171b8) ([PyObject](../../df/d1b/classPyObject.html) *pobject, const char *method)  
| runs a python object method which returns a arbitrary object
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6b1f62ad4b5abacc7636d2ec0ad171b8)  
  
void | [runMethod](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a332b522ee1a933d2f6c063f8ffc2a005) ([PyObject](../../df/d1b/classPyObject.html) *pobject, const char *method, const char *resfmt=nullptr, void *cresult=nullptr, const char *argfmt="()",...)  
| runs a python method with arbitrary params
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a332b522ee1a933d2f6c063f8ffc2a005)  
  
Cleanup  
[int](../../d1/da0/classint.html) | [cleanup](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a52c94c5cc89a32ddb9226ba0ae6f4d05) (void(*func)())  
| Register a cleanup function to be called by
[finalize()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a36c342466389ab64392ca10ad6d4724c
"This calls the registered cleanup functions.").
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a52c94c5cc89a32ddb9226ba0ae6f4d05)  
  
void | [finalize](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a36c342466389ab64392ca10ad6d4724c) ()  
| This calls the registered cleanup functions.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a36c342466389ab64392ca10ad6d4724c)  
  
void | [systemExit](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a84abc7f5b37993cbc7260028bb95721d) ()  
| This shuts down the application.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a84abc7f5b37993cbc7260028bb95721d)  
  
external wrapper libs  
here we can access external dynamically loaded wrapper libs done e.g. by SWIG
or SIP  
[PyObject](../../df/d1b/classPyObject.html) * | [createSWIGPointerObj](../../d2/d9e/classBase_1_1InterpreterSingleton.html#aa58e3bae949bc23bd54f760e0f2d121f) (const char *Modole, const char *TypeName, void *Pointer, [int](../../d1/da0/classint.html) own)  
| generate a SWIG object
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#aa58e3bae949bc23bd54f760e0f2d121f)  
  
[bool](../../d9/db9/classbool.html) | [convertSWIGPointerObj](../../d2/d9e/classBase_1_1InterpreterSingleton.html#aaf392875f9064578fc425608965fbd2c) (const char *Module, const char *TypeName, [PyObject](../../df/d1b/classPyObject.html) *obj, void **ptr, [int](../../d1/da0/classint.html) flags)  
void | [cleanupSWIG](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a560cebca9ef14ce122781b287c3f6b66) (const char *TypeName)  
PyTypeObject * | [getSWIGPointerTypeObj](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ab728025482cd5417a2ea003109688a68) (const char *Module, const char *TypeName)  
methods for debugging facility  
void | [dbgObserveFile](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae881ed5d0655aa77f2fcdec2e329b9a6) (const char *sFileName="")  
| sets the file name which should be debugged
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae881ed5d0655aa77f2fcdec2e329b9a6)  
  
void | [dbgSetBreakPoint](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a5e49b29dbdea4d2e581a94e336d5f005) (unsigned [int](../../d1/da0/classint.html) uiLineNumber)  
| sets a break point to a special line number in the current file
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a5e49b29dbdea4d2e581a94e336d5f005)  
  
void | [dbgUnsetBreakPoint](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a89df4eb37db08fbe98bd8fbaf5216ec8) (unsigned [int](../../d1/da0/classint.html) uiLineNumber)  
| unsets a break point to a special line number in the current file
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a89df4eb37db08fbe98bd8fbaf5216ec8)  
  
void | [dbgStep](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a87962d6d05eb07f1ad1618c09a61fec9) ()  
| One step further.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a87962d6d05eb07f1ad1618c09a61fec9)  
  
  
## Module handling  
  
---  
[bool](../../d9/db9/classbool.html) | [loadModule](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af59e1b874f05bcb2792ec395788578be) (const char *psModName)  
void | [addPythonPath](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a71c5ca5d92e31196d1d1736a12a988bc) (const char *Path)  
| Add an additional python path.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a71c5ca5d92e31196d1d1736a12a988bc)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [addModule](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af556d495376be43c3d93c9a44e6c15d3) (Py::ExtensionModuleBase *)  
| Add a module and return a [PyObject](../../df/d1b/classPyObject.html) to it.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af556d495376be43c3d93c9a44e6c15d3)  
  
void | [cleanupModules](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a3dd6afb203dcb5b1c0fdc040771b01bc) ()  
| Clean-up registered modules.
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a3dd6afb203dcb5b1c0fdc040771b01bc)  
  
static void | [addType](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ab5ecc003860947cdcd3921c249895382) (PyTypeObject *[Type](../../dc/dee/classBase_1_1Type.html), [PyObject](../../df/d1b/classPyObject.html) *Module, const char *Name)  
  
## startup and singletons  
  
---  
const char * | [init](../../d2/d9e/classBase_1_1InterpreterSingleton.html#aecdcee90ed7adb3cc5aec58560e9f3e1) ([int](../../d1/da0/classint.html) argc, char *argv[])  
| init the interpreter and returns the module search path
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#aecdcee90ed7adb3cc5aec58560e9f3e1)  
  
[int](../../d1/da0/classint.html) | [runCommandLine](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a5f7f8312974b7d1a819fa4a23f0da464) (const char *prompt)  
void | [replaceStdOutput](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6fe9717b82fe2da0e955c39e19fbeb42) ()  
static [InterpreterSingleton](../../d2/d9e/classBase_1_1InterpreterSingleton.html) & | [Instance](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a75f535aa7040f82d2f834640920f6c3a) ()  
static void | [Destruct](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a679f79c974244efc7e4e4ce686850f28) ()  
  
## static helper functions  
  
---  
[PyObject](../../df/d1b/classPyObject.html) * | [getValue](../../d2/d9e/classBase_1_1InterpreterSingleton.html#aea9468a5b47d5da5b9029c67930852e0) (const char *key, const char *result_var)  
static const std::string | [strToPython](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6d84d3d3e8f187106454074c1b2c340b) (const char *Str)  
| replaces all char with escapes for usage in python console
[More...](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a6d84d3d3e8f187106454074c1b2c340b)  
  
static const std::string | [strToPython](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a8ce8ce25ea332314576eede2750e6f69) (const std::string &Str)  
  
## Detailed Description

The Interpreter class This class manage the python interpreter and hold a lot
helper functions for handling python stuff.

## Constructor & Destructor Documentation

## ◆ InterpreterSingleton()

InterpreterSingleton::InterpreterSingleton  | ( | | ) |   
---|---|---|---|---  
  
Referenced by
[Instance()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a75f535aa7040f82d2f834640920f6c3a).

## ◆ ~InterpreterSingleton()

InterpreterSingleton::~InterpreterSingleton  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ addModule()

[PyObject](../../df/d1b/classPyObject.html) * InterpreterSingleton::addModule  | ( | Py::ExtensionModuleBase *  | _mod_| ) |   
---|---|---|---|---|---  
  
Add a module and return a [PyObject](../../df/d1b/classPyObject.html) to it.

Referenced by
[Gui::PythonDebugModule::init_module()](../../d8/dcf/classGui_1_1PythonDebugModule.html#a7c8e552e89e82e80c324201131aec9dd),
[Cloud::initModule()](../../d9/dea/namespaceCloud.html#a6d1cb462191f7ba8e39cb9ec344dc538),
[CloudGui::initModule()](../../d5/d3c/namespaceCloudGui.html#a8b11482e780345f0b0c4a79c927ed7f5),
[DraftUtils::initModule()](../../d8/dc4/namespaceDraftUtils.html#a7a78df29a04d2cdbd40ae6281b33c222),
[Drawing::initModule()](../../d2/dba/namespaceDrawing.html#a12295995f96d1a0819a3a45677ebcf82),
[DrawingGui::initModule()](../../d3/d2f/namespaceDrawingGui.html#a959425968700d3a7e83d793ca32b8849),
[Fem::initModule()](../../dd/d72/namespaceFem.html#a3db9879381427904d14862204b2e663e),
[FemGui::initModule()](../../d7/d91/namespaceFemGui.html#a2092a959d76f7c425d72e4d30cc9cc0f),
[Image::initModule()](../../d6/d82/namespaceImage.html#ad542e2ba181e3f0dbb8f9e303ed7735b),
[ImageGui::initModule()](../../d2/d5d/namespaceImageGui.html#a82701828e090d78b6ef263e66dde494b),
[Import::initModule()](../../df/df2/namespaceImport.html#ae135272a4e2942a242309bd72d802215),
[ImportGui::initModule()](../../d6/d28/namespaceImportGui.html#af7e4f1cc80c84292ee799a72d737dc6d),
[Inspection::initModule()](../../d3/dc8/namespaceInspection.html#ad71747c67df48e5259658890f9c69bf5),
[InspectionGui::initModule()](../../dd/d85/namespaceInspectionGui.html#a6c570cd5d639f8d6eea2da8a0c4a536c),
[Measure::initModule()](../../d5/d7d/namespaceMeasure.html#a424d6381a80c39aa2a64397598ed9b75),
[Mesh::initModule()](../../dc/d48/namespaceMesh.html#a0f5980336ca8d2e8bbbd444257f3f22a),
[MeshGui::initModule()](../../d6/d0f/namespaceMeshGui.html#a9d015a315cd838ad7dc29c686501c04c),
[MeshPart::initModule()](../../dd/d63/namespaceMeshPart.html#a0cb05d4775cee33eaec0ba02cd361ebc),
[MeshPartGui::initModule()](../../d1/d47/namespaceMeshPartGui.html#ae69086b583dcde8ac34b8502aea91d3e),
[Part::initModule()](../../d2/db9/namespacePart.html#af3669c97a7993f5da5f772300703523f),
[PartGui::initModule()](../../d5/d49/namespacePartGui.html#a993cd35a564d686e2431a17ab96d8cf7),
[PartDesign::initModule()](../../df/d14/namespacePartDesign.html#a3375a05ef577b0491bc43a80072c7604),
[PartDesignGui::initModule()](../../dc/d12/namespacePartDesignGui.html#a156cdfb4182c4741e2c444cb563eff73),
[Path::initModule()](../../d2/df0/namespacePath.html#a0f8702f031bc3f8ba60f84d870953aa6),
[PathGui::initModule()](../../db/d89/namespacePathGui.html#a1ad801a174d58fd85ea652068eaeecfc),
[PathSimulator::initModule()](../../d4/d3f/namespacePathSimulator.html#af81e0fced7b3cc2b52e1676e4deb9aa9),
[Points::initModule()](../../d6/dac/namespacePoints.html#a10e42a87bd0ce5a29e3294b2be4e86fa),
[PointsGui::initModule()](../../d7/d9d/namespacePointsGui.html#a8b16a9b3c7a3e15d40f0e5c3ffa98eab),
[Raytracing::initModule()](../../d3/de4/namespaceRaytracing.html#a5ca30846806691c8921e7d14a55fc823),
[RaytracingGui::initModule()](../../d5/df7/namespaceRaytracingGui.html#a91d172299c5fa8dc538f01f2ba43a950),
[Reen::initModule()](../../db/d29/namespaceReen.html#a839657a3c5d9e07379b2a94a6119f44f),
[ReverseEngineeringGui::initModule()](../../d4/da2/namespaceReverseEngineeringGui.html#a26693eec055751c4543992fea01a84cb),
[Robot::initModule()](../../da/d93/namespaceRobot.html#a1288983daf1ad6dea2d140b28bb104fa),
[RobotGui::initModule()](../../d3/dff/namespaceRobotGui.html#a69c46015392f3f4d9663bfd76e7b7aed),
[SketcherGui::initModule()](../../d6/d44/namespaceSketcherGui.html#a97be3f4ae7dd2f1c9898df87c4e3c36d),
[Spreadsheet::initModule()](../../d3/dac/namespaceSpreadsheet.html#a5ef7c574c87d22dca75e0d2457e5acd8),
[SpreadsheetGui::initModule()](../../db/d8b/namespaceSpreadsheetGui.html#ad380b5a05a57beebfbc579fa8ffc34c7),
[Start::initModule()](../../d7/d4f/namespaceStart.html#a68a7be09047fcbd030a0998ad72f7bbc),
[StartGui::initModule()](../../d9/d3b/namespaceStartGui.html#a9095e5a83a522ce8304b9100e99723e8),
[Surface::initModule()](../../db/df5/namespaceSurface.html#a28b955c1c24eaae7034e9868ceea122d),
[SurfaceGui::initModule()](../../da/db7/namespaceSurfaceGui.html#a91724469b61b99b839cc9dd3c5d2c66e),
[TechDraw::initModule()](../../d7/d31/namespaceTechDraw.html#a6d1829c006d5fd78e905fd2f1310b9e8),
[TechDrawGui::initModule()](../../dc/de6/namespaceTechDrawGui.html#a8b6752db4aecb8f0c5b390a569519bdb),
[TestGui::initModule()](../../df/d49/namespaceTestGui.html#ae23b1c05f5fe18d7106e17d63349294e),
[Web::initModule()](../../d8/d98/namespaceWeb.html#aed366988a217fee0da1df766aadabcc9),
and
[WebGui::initModule()](../../d4/da0/namespaceWebGui.html#a980652e262bbfe2e725cf4ff28a864b2).

## ◆ addPythonPath()

void InterpreterSingleton::addPythonPath  | ( | const char *  | _Path_| ) |   
---|---|---|---|---|---  
  
Add an additional python path.

Referenced by
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939).

## ◆ addType()

| void InterpreterSingleton::addType  | ( | PyTypeObject *  | _Type_ ,   
---|---|---|---  
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _Module_ ,   
|  | const char *  | _Name_  
| ) | |   
static  
  
References
[Base::getTypeAsObject()](../../db/d07/namespaceBase.html#a2c13fe795e18ca20ff9a027e93d26cea).

Referenced by
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
and [Fem::SMESH_HypothesisPy< T
>::init_type()](../../d9/d18/classFem_1_1SMESH__HypothesisPy.html#ae53f222299da75bb712785097907a969).

## ◆ cleanup()

[int](../../d1/da0/classint.html) InterpreterSingleton::cleanup  | ( | void(*)()  | _func_| ) |   
---|---|---|---|---|---  
  
Register a cleanup function to be called by
[finalize()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a36c342466389ab64392ca10ad6d4724c
"This calls the registered cleanup functions.").

The cleanup function will be called with no arguments and should return no
value. At most 32 cleanup functions can be registered. When the registration
is successful 0 is returned; on failure -1 is returned. The cleanup function
registered last is called first. Each cleanup function will be called at most
once. Since Python's internal finalization will have completed before the
cleanup function, no Python APIs should be called by _func_.

Referenced by
[PathPythonGui.simple_edit_panel.SimpleEditPanel::abort()](../../d4/d29/classPathPythonGui_1_1simple__edit__panel_1_1SimpleEditPanel.html#a158164b50132313ab366c2353beec6aa),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel::abort()](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#afdc1e68e928f69179f2274ff08e4cfe0),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel::abort()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a9593353efac333606eace7a28ad0211e),
[PathScripts.PathDressupDogbone.TaskPanel::accept()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a8212729d1d695ccf9b5404cbe2a8bbdb),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel::accept()](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#a1dacef744bbfa33af66993f6ee92a90b),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel::accept()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a67118859ed07401ad7a2e5d15f1f9a07),
[PathScripts.PathJobGui.TaskPanel::accept()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a97734a4413b7a81d15f6ce3de8bbc4e1),
[PathScripts.PathOpGui.TaskPanel::accept()](../../da/d7e/classPathScripts_1_1PathOpGui_1_1TaskPanel.html#a695051e4054ba504e41b2c9fd29b6384),
[PathScripts.PathDressupDogbone.TaskPanel::reject()](../../df/d54/classPathScripts_1_1PathDressupDogbone_1_1TaskPanel.html#a7b0a996f777862e452802db219b4172b),
[PathScripts.PathDressupPathBoundaryGui.TaskPanel::reject()](../../d4/d65/classPathScripts_1_1PathDressupPathBoundaryGui_1_1TaskPanel.html#adb7e6766fb8fbdcf814d35db4c4e52de),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel::reject()](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#ad3c45a36ea13bebdcf535850d4170b90),
[PathScripts.PathJobGui.TaskPanel::reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
and
[PathScripts.PathOpGui.TaskPanel::reject()](../../da/d7e/classPathScripts_1_1PathOpGui_1_1TaskPanel.html#a9ef68da6c4160ffa4f19aaf6b079fb0a).

## ◆ cleanupModules()

void InterpreterSingleton::cleanupModules  | ( | | ) |   
---|---|---|---|---  
  
Clean-up registered modules.

Referenced by
[finalize()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a36c342466389ab64392ca10ad6d4724c).

## ◆ cleanupSWIG()

void InterpreterSingleton::cleanupSWIG  | ( | const char *  | _TypeName_| ) |   
---|---|---|---|---|---  
  
References
[Swig_python::cleanupSWIG_T()](../../df/d2a/namespaceSwig__python.html#a18fd06e7d0d4b949b4fb6a3664466005).

Referenced by
[Gui::Application::~Application()](../../d9/da8/classGui_1_1Application.html#a748bca84fefb9c12661cfaa2f623748d).

## ◆ convertSWIGPointerObj()

[bool](../../d9/db9/classbool.html) InterpreterSingleton::convertSWIGPointerObj  | ( | const char *  | _Module_ ,   
---|---|---|---  
|  | const char *  | _TypeName_ ,   
|  | [PyObject](../../df/d1b/classPyObject.html) *  | _obj_ ,   
|  | void **  | _ptr_ ,   
|  | [int](../../d1/da0/classint.html) | _flags_  
| ) | |   
  
References
[Swig_python::convertSWIGPointerObj_T()](../../df/d2a/namespaceSwig__python.html#a8fa5e3913f9be8dd52462b5000f6c364).

Referenced by
[Gui::View3DInventorPy::addDraggerCallback()](../../d3/df7/classGui_1_1View3DInventorPy.html#ae02f32b8eff051cadf021e21c1775e44),
[Gui::View3DInventorPy::addEventCallbackPivy()](../../d3/df7/classGui_1_1View3DInventorPy.html#a1524829097b50cdb51c7f6b63b3f6559),
[Gui::View3DInventorPy::dumpNode()](../../d3/df7/classGui_1_1View3DInventorPy.html#a9e8faa2178ad4245d9f808bd35ae6a5a),
[Gui::FreeCADGui_exportSubgraph()](../../d9/dad/namespaceGui.html#ad8f91994cbe2d5fc3868245e6a7f4298),
[Gui::ViewProviderPythonFeatureImp::getDetail()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a4daa5ea512609c630c8e4e1557984c24),
[Gui::ViewProviderPythonFeatureImp::getDetailPath()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#aaee9c529dfb047b9a3b09c8bd5980b60),
[Gui::View3DInventorPy::removeDraggerCallback()](../../d3/df7/classGui_1_1View3DInventorPy.html#a0ec7edf6ca2ba0f75b632a501ce116d3),
[Gui::View3DInventorPy::removeEventCallbackPivy()](../../d3/df7/classGui_1_1View3DInventorPy.html#a160afd5b694a3162c4de895d85eacc14),
[Gui::SoQtOffscreenRendererPy::render()](../../d4/d69/classGui_1_1SoQtOffscreenRendererPy.html#ad2c7ba972114bce57794799a61cf020a),
[Gui::Application::sCoinRemoveAllChildren()](../../d9/da8/classGui_1_1Application.html#aa4485a087e8e82ed3e2ee0f8976726ef),
[Gui::View3DInventorViewerPy::setSceneGraph()](../../dc/da7/classGui_1_1View3DInventorViewerPy.html#a7b86da59eee9257c276e98bfaa91ebbd),
and
[Gui::View3DInventorViewerPy::setupEditingRoot()](../../dc/da7/classGui_1_1View3DInventorViewerPy.html#a85f19026d8988f59d70b4d9018198149).

## ◆ createSWIGPointerObj()

[PyObject](../../df/d1b/classPyObject.html) * InterpreterSingleton::createSWIGPointerObj  | ( | const char *  | _Modole_ ,   
---|---|---|---  
|  | const char *  | _TypeName_ ,   
|  | void *  | _Pointer_ ,   
|  | [int](../../d1/da0/classint.html) | _own_  
| ) | |   
  
generate a SWIG object

References
[Swig_python::createSWIGPointerObj_T()](../../df/d2a/namespaceSwig__python.html#a782c80bc8b59566e03daaf7be856d491).

Referenced by
[Gui::FreeCADGui_subgraphFromObject()](../../d9/dad/namespaceGui.html#a1562062f6fcff8f9ec05618c80435514),
[Gui::View3DInventorPy::getCameraNode()](../../d3/df7/classGui_1_1View3DInventorPy.html#a9e2c3c0de8538c39d7fc2821b9b63360),
[Gui::ViewProviderPythonFeatureImp::getDetailPath()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#aaee9c529dfb047b9a3b09c8bd5980b60),
[Gui::ViewProviderPythonFeatureImp::getElement()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#ab5a8a1843ef27213a6ca168c1a776e5d),
[Gui::ViewProviderPythonFeatureImp::getElementPicked()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#add9a46f6ae75387b61493b1fd17b5436),
[Gui::View3DInventorPy::getSceneGraph()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2ccd11b76e1727a93bad19a4870f8861),
[Gui::View3DInventorViewerPy::getSceneGraph()](../../dc/da7/classGui_1_1View3DInventorViewerPy.html#a98c44e4879f723efb02fd26304219819),
[Gui::View3DInventorViewerPy::getSoEventManager()](../../dc/da7/classGui_1_1View3DInventorViewerPy.html#a4f42357b5436d87fc1ff06e77c4181d7),
and
[Gui::View3DInventorViewerPy::getSoRenderManager()](../../dc/da7/classGui_1_1View3DInventorViewerPy.html#ac94887d74e9ee865122ed86dcf4182e3).

## ◆ dbgObserveFile()

void InterpreterSingleton::dbgObserveFile  | ( | const char *  | _sFileName_ = `""`| ) |   
---|---|---|---|---|---  
  
sets the file name which should be debugged

## ◆ dbgSetBreakPoint()

void InterpreterSingleton::dbgSetBreakPoint  | ( | unsigned [int](../../d1/da0/classint.html) | _uiLineNumber_| ) |   
---|---|---|---|---|---  
  
sets a break point to a special line number in the current file

## ◆ dbgStep()

void InterpreterSingleton::dbgStep  | ( | | ) |   
---|---|---|---|---  
  
One step further.

## ◆ dbgUnsetBreakPoint()

void InterpreterSingleton::dbgUnsetBreakPoint  | ( | unsigned [int](../../d1/da0/classint.html) | _uiLineNumber_| ) |   
---|---|---|---|---|---  
  
unsets a break point to a special line number in the current file

## ◆ Destruct()

| void InterpreterSingleton::Destruct  | ( | | ) |   
---|---|---|---|---  
static  
  
## ◆ finalize()

void InterpreterSingleton::finalize  | ( | | ) |   
---|---|---|---|---  
  
This calls the registered cleanup functions.

See also

    [cleanup()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a52c94c5cc89a32ddb9226ba0ae6f4d05 "Register a cleanup function to be called by finalize\(\).") for more details. 

References
[cleanupModules()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a3dd6afb203dcb5b1c0fdc040771b01bc).

Referenced by
[App::Application::destruct()](../../da/dbf/classApp_1_1Application.html#a2429ab2a8f4255a5ce2d970aa74ba7f3),
and
[draftguitools.gui_trackers.ghostTracker::remove()](../../d9/dc6/classdraftguitools_1_1gui__trackers_1_1ghostTracker.html#a6d3d5ac2b343751035f7e31d41c87d87).

## ◆ getSWIGPointerTypeObj()

PyTypeObject * InterpreterSingleton::getSWIGPointerTypeObj  | ( | const char *  | _Module_ ,   
---|---|---|---  
|  | const char *  | _TypeName_  
| ) | |   
  
References
[Swig_python::getSWIGPointerTypeObj_T()](../../df/d2a/namespaceSwig__python.html#ac132767092f4a53bd0aaff942aca7498).

## ◆ getValue()

[PyObject](../../df/d1b/classPyObject.html) * InterpreterSingleton::getValue  | ( | const char *  | _key_ ,   
---|---|---|---  
|  | const char *  | _result_var_  
| ) | |   
  
## ◆ init()

const char * InterpreterSingleton::init  | ( | [int](../../d1/da0/classint.html) | _argc_ ,   
---|---|---|---  
|  | char *  | _argv_[]   
| ) | |   
  
init the interpreter and returns the module search path

References
[PythonStdOutput::init_type()](../../da/d1e/classPythonStdOutput.html#a22537dd9062c68e0d87b97ef1fe4eb77).

Referenced by
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ Instance()

| [InterpreterSingleton](../../d2/d9e/classBase_1_1InterpreterSingleton.html) & InterpreterSingleton::Instance  | ( | | ) |   
---|---|---|---|---  
static  
  
References
[InterpreterSingleton()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae5e285d3f24a70615f26b85675c80984).

Referenced by
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9).

## ◆ loadModule()

[bool](../../d9/db9/classbool.html) InterpreterSingleton::loadModule  | ( | const char *  | _psModName_| ) |   
---|---|---|---|---|---  
  
Referenced by
[Base::Type::importModule()](../../dc/dee/classBase_1_1Type.html#a7e5b01ed0f09e28b038003caa13c3830),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
and
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939).

## ◆ replaceStdOutput()

void InterpreterSingleton::replaceStdOutput  | ( | | ) |   
---|---|---|---|---  
  
## ◆ runCommandLine()

[int](../../d1/da0/classint.html) InterpreterSingleton::runCommandLine  | ( | const char *  | _prompt_| ) |   
---|---|---|---|---|---  
  
Referenced by
[StdCmdCommandLine::activated()](../../d2/d16/classStdCmdCommandLine.html#a6c161075d14633a034a968185e9c71ad),
and
[App::Application::runApplication()](../../da/dbf/classApp_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c).

## ◆ runFile()

void InterpreterSingleton::runFile  | ( | const char *  | _pxFileName_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _local_  
| ) | |   
  
Run file (script) on the python interpreter.

References
[Base::FileInfo::toStdWString()](../../dd/d34/classBase_1_1FileInfo.html#adbe0c0eb1d84fc10d0b734f4cb3e1304).

Referenced by
[Gui::PreferencePack::apply()](../../d3/d54/classGui_1_1PreferencePack.html#ad5cbfc85d280322a52250e42b0dfbcf2),
[TechDraw::DrawParametricTemplate::execute()](../../d5/d13/classTechDraw_1_1DrawParametricTemplate.html#acc1380e0737504ec1d64b2bbca2380e6),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
and
[Gui::MacroManager::run()](../../d8/dc6/classGui_1_1MacroManager.html#afd22c56a284e48a4df19fa0df503826b).

## ◆ runInteractiveString()

void InterpreterSingleton::runInteractiveString  | ( | const char *  | _psCmd_| ) |   
---|---|---|---|---|---  
  
Run a statement on the python interpreter and gives back a string with the
representation of the result.

References
[Base::Exception::setMessage()](../../d8/df7/classBase_1_1Exception.html#ac112f8e1e18aa8bccc4902daae47c446).

## ◆ runMethod()

void InterpreterSingleton::runMethod  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _pobject_ ,   
---|---|---|---  
|  | const char *  | _method_ ,   
|  | const char *  | _resfmt_ = `nullptr`,   
|  | void *  | _cresult_ = `nullptr`,   
|  | const char *  | _argfmt_ = `"()"`,   
|  |  | _..._  
| ) | |   
  
runs a python method with arbitrary params

Referenced by
[Gui::PythonCommand::activated()](../../d3/d3a/classGui_1_1PythonCommand.html#ae2ed8b5ea87ffdbf33e43d5d867cac08).

## ◆ runMethodObject()

[PyObject](../../df/d1b/classPyObject.html) * InterpreterSingleton::runMethodObject  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _pobject_ ,   
---|---|---|---  
|  | const char *  | _method_  
| ) | |   
  
runs a python object method which returns a arbitrary object

Referenced by
[Gui::PythonCommand::getHelpUrl()](../../d3/d3a/classGui_1_1PythonCommand.html#a6217682204e3fa0472ea7868bce81bc8),
[Gui::PythonCommand::PythonCommand()](../../d3/d3a/classGui_1_1PythonCommand.html#aba2c547acfefa72c10080124ef51946a),
and
[Gui::PythonGroupCommand::PythonGroupCommand()](../../dc/dbb/classGui_1_1PythonGroupCommand.html#af127f486553428a15ca5fba5be1e13f3).

## ◆ runMethodVoid()

void InterpreterSingleton::runMethodVoid  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _pobject_ ,   
---|---|---|---  
|  | const char *  | _method_  
| ) | |   
  
runs a python object method with no return value and no arguments

Runs a member method of an object with no parameter and no return value void
(void).

There are other methods to run with returns

Referenced by
[Gui::PythonCommand::activated()](../../d3/d3a/classGui_1_1PythonCommand.html#ae2ed8b5ea87ffdbf33e43d5d867cac08).

## ◆ runString()

std::string InterpreterSingleton::runString  | ( | const char *  | _psCmd_| ) |   
---|---|---|---|---|---  
  
Run a statement on the python interpreter and gives back a string with the
representation of the result.

References
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

Referenced by
[Gui::Command::addModule()](../../d2/dff/classGui_1_1Command.html#a5f271fb656068e8bd1b81d6f2cb1a7da),
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[StartGui::Workbench::loadStartPage()](../../dc/d4c/classStartGui_1_1Workbench.html#a44d732f24cca88363d161155407973a6),
[TestGui::UnitTestDialog::on_startButton_clicked()](../../de/d87/classTestGui_1_1UnitTestDialog.html#a8e5cb687cbb54c454fbe298d0ae47d66),
[DraftUtils::DraftDxfRead::OnReadDimension()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#a2205e7dc4ba94a978a32ecae3191e36f),
[Import::ImpExpDxfRead::OnReadDimension()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#a630ce59f752e7f2be9c104b1dd138e7f),
[Gui::GestureNavigationStyle::onRollGesture()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#aea1942b7bbfc657cbfe2ae892811b802),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[Sandbox::PythonThread::run()](../../da/d9e/classSandbox_1_1PythonThread.html#a4c26a11ab7160b84ecebd4403ad406b6),
[App::Application::runApplication()](../../da/dbf/classApp_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::Application::runInitGuiScript()](../../d9/da8/classGui_1_1Application.html#ab700cfb3a0ee688ee8bb51274f4a737d),
[runStringArg()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#afff9e462cde2ead702ab1ff0f5ddbbad),
[Gui::Application::setActiveDocument()](../../d9/da8/classGui_1_1Application.html#a689d6d547879b12ded7364fa0fb7953c),
and
[Gui::Application::sOpen()](../../d9/da8/classGui_1_1Application.html#a3402c81d1a56dbb72d84e74047fc53e8).

## ◆ runStringArg()

void InterpreterSingleton::runStringArg  | ( | const char *  | _psCom_ ,   
---|---|---|---  
|  |  | _..._  
| ) | |   
  
Run a statement with arguments on the python interpreter.

References
[runString()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a2cabac4e610e966ebc33a1e1aa5d94b6).

Referenced by
[TechDraw::DrawViewArch::execute()](../../df/dc6/classTechDraw_1_1DrawViewArch.html#afa99f9a47bc763ef3bb9796e01ced4f8),
[TechDraw::DrawViewDraft::execute()](../../df/d84/classTechDraw_1_1DrawViewDraft.html#abb9504b3eb9d33a5d1b95678dff5fe5b),
[TechDraw::DrawDimHelper::makeDistDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#abbb31fd885c91f55267b7f8fd3945c1a),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[DraftUtils::DraftDxfRead::OnReadDimension()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#a2205e7dc4ba94a978a32ecae3191e36f),
[Import::ImpExpDxfRead::OnReadDimension()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#a630ce59f752e7f2be9c104b1dd138e7f),
[App::Application::processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[App::Application::processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[TechDraw::DrawViewCollection::unsetupObject()](../../df/d2f/classTechDraw_1_1DrawViewCollection.html#a33815aa3bc978248b9ec92b423ba7c45),
[TechDraw::DrawPage::unsetupObject()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ad65529c32a2d36f88a87e6734f093fcf),
and
[TechDraw::DrawViewPart::unsetupObject()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a404e3640464295cb65780c7374a83940).

## ◆ runStringObject()

Py::Object InterpreterSingleton::runStringObject  | ( | const char *  | _sCmd_| ) |   
---|---|---|---|---|---  
  
Run a statement on the python interpreter and return back the result object.

## ◆ runStringWithKey()

std::string InterpreterSingleton::runStringWithKey  | ( | const char *  | _psCmd_ ,   
---|---|---|---  
|  | const char *  | _key_ ,   
|  | const char *  | _key_initial_value_ = `""`  
| ) | |   
  
Run a statement on the python interpreter with a key for exchanging strings.

runStringWithKey(psCmd, key, key_initial_value) psCmd is python script to run
key is the name of a python string variable the script will have read/write
access to during script execution.

It will be our return value. key_initial_value is the initial value c++ will
set before calling the script If the script runs successfully it will be able
to change the value of key as the return value, but if there is a runtime
error key will not be changed even if the error occurs after changing it
inside the script.

References
[Base::PyException::ThrowException()](../../d6/d92/classBase_1_1PyException.html#a41cd2047f045341cd3e9db245a42e130).

## ◆ strToPython() [1/2]

| const std::string InterpreterSingleton::strToPython  | ( | const char *  | _Str_| ) |   
---|---|---|---|---|---  
static  
  
replaces all char with escapes for usage in python console

Referenced by
[Gui::PropertyEditor::PropertyEnumItem::setValue()](../../d1/dd0/classGui_1_1PropertyEditor_1_1PropertyEnumItem.html#a7c1251bfd5e2a2133e9fd826a7a33983),
[Gui::PropertyEditor::PropertyStringListItem::setValue()](../../d7/d2f/classGui_1_1PropertyEditor_1_1PropertyStringListItem.html#a1861e5c357baa67f8126d042c80bb740),
and
[Gui::Command::strToPython()](../../d2/dff/classGui_1_1Command.html#ade4c3cc22de45c333de7492b65a86340).

## ◆ strToPython() [2/2]

| static const std::string Base::InterpreterSingleton::strToPython  | ( | const std::string & | _Str_| ) |   
---|---|---|---|---|---  
static  
  
References
[strToPython()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a8ce8ce25ea332314576eede2750e6f69).

Referenced by
[strToPython()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a8ce8ce25ea332314576eede2750e6f69).

## ◆ systemExit()

void InterpreterSingleton::systemExit  | ( | | ) |   
---|---|---|---|---  
  
This shuts down the application.

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Interpreter.h
  * FreeCAD/src/Base/Interpreter.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

