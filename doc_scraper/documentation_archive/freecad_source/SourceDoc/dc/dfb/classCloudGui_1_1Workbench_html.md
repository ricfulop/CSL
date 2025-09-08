---
url: https://freecad.github.io/SourceDoc/dc/dfb/classCloudGui_1_1Workbench.html
scraped_at: 2025-09-08T15:19:31.655211
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [CloudGui](../../d5/d3c/namespaceCloudGui.html)
  * [Workbench](../../dc/dfb/classCloudGui_1_1Workbench.html)

[List of all members](../../d3/d8f/classCloudGui_1_1Workbench-members.html) | Public Member Functions

CloudGui::Workbench Class Reference

`#include <Workbench.h>`

##  Public Member Functions  
  
---  
|
[Workbench](../../dc/dfb/classCloudGui_1_1Workbench.html#a052a62fb11c36380d04283bff6d47582)
()  
virtual | [~Workbench](../../dc/dfb/classCloudGui_1_1Workbench.html#ad0d8c30cb6c23742369688a664d34b69) ()  
![-](../../closed.png) Public Member Functions inherited from
[Gui::StdWorkbench](../../db/d0a/classGui_1_1StdWorkbench.html)  
virtual void | [createMainWindowPopupMenu](../../db/d0a/classGui_1_1StdWorkbench.html#a52a2304e849ffca650d2cde52bca4a3c) ([MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) *) const  
| Sets up the contextmenu for the main window for this workbench.
[More...](../../db/d0a/classGui_1_1StdWorkbench.html#a52a2304e849ffca650d2cde52bca4a3c)  
  
virtual void | [setupContextMenu](../../db/d0a/classGui_1_1StdWorkbench.html#a9fc2ca1a33fe4dde2a8a5e6dfc89c57d) (const char *recipient, [MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) *) const  
| Defines the standard context menu.
[More...](../../db/d0a/classGui_1_1StdWorkbench.html#a9fc2ca1a33fe4dde2a8a5e6dfc89c57d)  
  
|
[StdWorkbench](../../db/d0a/classGui_1_1StdWorkbench.html#a3e65e3116e0308cc83a31f3b007aa53e)
()  
virtual | [~StdWorkbench](../../db/d0a/classGui_1_1StdWorkbench.html#a4e057af4e2d5c69fc931c837c069f793) ()  
![-](../../closed.png) Public Member Functions inherited from
[Gui::Workbench](../../d0/d97/classGui_1_1Workbench.html)  
[bool](../../d9/db9/classbool.html) | [activate](../../d0/d97/classGui_1_1Workbench.html#af76941097c2292e88071e5bff9c54fc0) ()  
| Activates the workbench and adds/removes GUI elements.
[More...](../../d0/d97/classGui_1_1Workbench.html#af76941097c2292e88071e5bff9c54fc0)  
  
virtual void | [activated](../../d0/d97/classGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced) ()  
| Run some actions when the workbench gets activated.
[More...](../../d0/d97/classGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced)  
  
void | [addTaskWatcher](../../d0/d97/classGui_1_1Workbench.html#a7af77b8350501ea4300b280a71aabf8e) (const std::vector< [Gui::TaskView::TaskWatcher](../../d4/d50/classGui_1_1TaskView_1_1TaskWatcher.html) * > &Watcher)  
| helper to add TaskWatcher to the
[TaskView](../../d2/da7/namespaceGui_1_1TaskView.html)
[More...](../../d0/d97/classGui_1_1Workbench.html#a7af77b8350501ea4300b280a71aabf8e)  
  
virtual void | [createMainWindowPopupMenu](../../d0/d97/classGui_1_1Workbench.html#ab6e55807e71fea84fb5b6e2b847fbd15) ([MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) *) const  
| Sets up the contextmenu for the main window for this workbench.
[More...](../../d0/d97/classGui_1_1Workbench.html#ab6e55807e71fea84fb5b6e2b847fbd15)  
  
virtual void | [deactivated](../../d0/d97/classGui_1_1Workbench.html#a40a75d23990560e129800bd870f3ad87) ()  
| Run some actions when the workbench gets deactivated.
[More...](../../d0/d97/classGui_1_1Workbench.html#a40a75d23990560e129800bd870f3ad87)  
  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d0/d97/classGui_1_1Workbench.html#a0a557a7b4893cdc9fc87a458c1559ff7) ()  
| The default implementation returns an instance of
[WorkbenchPy](../../de/d8f/classWorkbenchPy.html).
[More...](../../d0/d97/classGui_1_1Workbench.html#a0a557a7b4893cdc9fc87a458c1559ff7)  
  
std::list< std::pair< std::string, std::list< std::string > > > | [getToolbarItems](../../d0/d97/classGui_1_1Workbench.html#affd93918ccb6a404d8d3041eed157a30) () const  
| Shows a list of all toolbars and their commands.
[More...](../../d0/d97/classGui_1_1Workbench.html#affd93918ccb6a404d8d3041eed157a30)  
  
std::list< std::string > | [listCommandbars](../../d0/d97/classGui_1_1Workbench.html#ae125c38af40d63008d40d0318da72692) () const  
std::list< std::string > | [listMenus](../../d0/d97/classGui_1_1Workbench.html#a8b9f2eb4b46d4faef0bb33c5d79f0035) () const  
std::list< std::string > | [listToolbars](../../d0/d97/classGui_1_1Workbench.html#a913e9b4c5fdb4db5e102ee53cae1a370) () const  
std::string | [name](../../d0/d97/classGui_1_1Workbench.html#a4e4d27d0aedddb4ff968a41dbcb25da1) () const  
| Returns the name of the workbench object.
[More...](../../d0/d97/classGui_1_1Workbench.html#a4e4d27d0aedddb4ff968a41dbcb25da1)  
  
void | [removeTaskWatcher](../../d0/d97/classGui_1_1Workbench.html#a27826a1e529c60165410d7438c1c755e) (void)  
| remove the added TaskWatcher
[More...](../../d0/d97/classGui_1_1Workbench.html#a27826a1e529c60165410d7438c1c755e)  
  
void | [retranslate](../../d0/d97/classGui_1_1Workbench.html#a5e7552775902a96a8b4dd2a314778384) () const  
| Translates the window titles of all menus, toolbars and dock windows.
[More...](../../d0/d97/classGui_1_1Workbench.html#a5e7552775902a96a8b4dd2a314778384)  
  
void | [setName](../../d0/d97/classGui_1_1Workbench.html#ab67e098e3c48ebf82b6da123f9ae1c1c) (const std::string &)  
| Set the name to the workbench object.
[More...](../../d0/d97/classGui_1_1Workbench.html#ab67e098e3c48ebf82b6da123f9ae1c1c)  
  
virtual void | [setupContextMenu](../../d0/d97/classGui_1_1Workbench.html#afe4e52847fcdbd5f5b02353482b56507) (const char *recipient, [MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) *) const  
| Sets up the contextmenu for this workbench.
[More...](../../d0/d97/classGui_1_1Workbench.html#afe4e52847fcdbd5f5b02353482b56507)  
  
|
[Workbench](../../d0/d97/classGui_1_1Workbench.html#a052a62fb11c36380d04283bff6d47582)
()  
| Constructs a workbench object.
[More...](../../d0/d97/classGui_1_1Workbench.html#a052a62fb11c36380d04283bff6d47582)  
  
virtual | [~Workbench](../../d0/d97/classGui_1_1Workbench.html#ad0d8c30cb6c23742369688a664d34b69) ()  
![-](../../closed.png) Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)
()  
| Construction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a84b1d36d0060e74a7b48255bca0d1928)  
  
|
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html#ae41bc09a1498fbd4e952e7a7dd9de791)
(const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514)  
  
virtual [Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../df/d4d/classBase_1_1BaseClass.html#addbd3a4f09fce7ce5c6bf021e4c1d566) () const  
[bool](../../d9/db9/classbool.html) | [isDerivedFrom](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127) (const [Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
[BaseClass](../../df/d4d/classBase_1_1BaseClass.html) & | [operator=](../../df/d4d/classBase_1_1BaseClass.html#ad334dfcaf7aa8b86993eaefac41207c2) (const [BaseClass](../../df/d4d/classBase_1_1BaseClass.html) &)=default  
virtual void | [setPyObject](../../df/d4d/classBase_1_1BaseClass.html#a3146be9d62368b0c207a5571ed74828e) ([PyObject](../../df/d1b/classPyObject.html) *)  
virtual | [~BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49) ()  
| Destruction.
[More...](../../df/d4d/classBase_1_1BaseClass.html#a7bd44242e16f121ed78718ee8c234f49)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[Gui::Workbench](../../d0/d97/classGui_1_1Workbench.html)  
static void | [addPermanentMenuItem](../../d0/d97/classGui_1_1Workbench.html#ab9e87194e5ac18bea35bdda500332b7c) (const std::string &cmd, const std::string &after)  
| Add a permanent menu item _cmd_ after an existing command _after_.
[More...](../../d0/d97/classGui_1_1Workbench.html#ab9e87194e5ac18bea35bdda500332b7c)  
  
static void | [createLinkMenu](../../d0/d97/classGui_1_1Workbench.html#a1809f6410626507ffcc9969e63453c9b) ([MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) *)  
static void | [removePermanentMenuItem](../../d0/d97/classGui_1_1Workbench.html#ac09f8878c263f1a55cf79f21daa9fab8) (const std::string &cmd)  
| Removes the command _cmd_ from the permanent menu items.
[More...](../../d0/d97/classGui_1_1Workbench.html#ac09f8878c263f1a55cf79f21daa9fab8)  
  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Protected Member Functions inherited from
[Gui::StdWorkbench](../../db/d0a/classGui_1_1StdWorkbench.html)  
virtual [ToolBarItem](../../dc/d03/classGui_1_1ToolBarItem.html) * | [setupCommandBars](../../db/d0a/classGui_1_1StdWorkbench.html#ab9a81fd14cf22c78644c37d8547ffc51) () const  
| Defines the standard command bars.
[More...](../../db/d0a/classGui_1_1StdWorkbench.html#ab9a81fd14cf22c78644c37d8547ffc51)  
  
virtual [DockWindowItems](../../df/d05/classGui_1_1DockWindowItems.html) * | [setupDockWindows](../../db/d0a/classGui_1_1StdWorkbench.html#a88c74a40b7a275fb0c7fa93688f82afe) () const  
| Returns a [DockWindowItems](../../df/d05/classGui_1_1DockWindowItems.html)
structure of dock windows this workbench.
[More...](../../db/d0a/classGui_1_1StdWorkbench.html#a88c74a40b7a275fb0c7fa93688f82afe)  
  
virtual [MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) * | [setupMenuBar](../../db/d0a/classGui_1_1StdWorkbench.html#a66df1faa77a4652cbf50bf8d5ca35b14) () const  
| Defines the standard menus.
[More...](../../db/d0a/classGui_1_1StdWorkbench.html#a66df1faa77a4652cbf50bf8d5ca35b14)  
  
virtual [ToolBarItem](../../dc/d03/classGui_1_1ToolBarItem.html) * | [setupToolBars](../../db/d0a/classGui_1_1StdWorkbench.html#a58d90fd3e13854799049a2d32b706093) () const  
| Defines the standard toolbars.
[More...](../../db/d0a/classGui_1_1StdWorkbench.html#a58d90fd3e13854799049a2d32b706093)  
  
![-](../../closed.png) Protected Member Functions inherited from
[Gui::Workbench](../../d0/d97/classGui_1_1Workbench.html)  
void | [addPermanentMenuItems](../../d0/d97/classGui_1_1Workbench.html#af0662cff862cc7e4d9945404c63ecf42) ([MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) *) const  
| Add permanent menu items to the structure.
[More...](../../d0/d97/classGui_1_1Workbench.html#af0662cff862cc7e4d9945404c63ecf42)  
  
virtual [ToolBarItem](../../dc/d03/classGui_1_1ToolBarItem.html) * | [setupCommandBars](../../d0/d97/classGui_1_1Workbench.html#acd15496593629bd4f65a0cfe5c637896) () const =0  
| Returns a [ToolBarItem](../../dc/d03/classGui_1_1ToolBarItem.html) tree
structure of command bars for this workbench.
[More...](../../d0/d97/classGui_1_1Workbench.html#acd15496593629bd4f65a0cfe5c637896)  
  
virtual [DockWindowItems](../../df/d05/classGui_1_1DockWindowItems.html) * | [setupDockWindows](../../d0/d97/classGui_1_1Workbench.html#a865cd438fc855d73e7ca1fa853ec1af6) () const =0  
| Returns a [DockWindowItems](../../df/d05/classGui_1_1DockWindowItems.html)
structure of dock windows this workbench.
[More...](../../d0/d97/classGui_1_1Workbench.html#a865cd438fc855d73e7ca1fa853ec1af6)  
  
virtual [MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) * | [setupMenuBar](../../d0/d97/classGui_1_1Workbench.html#a5669c13ee2759f8b779c5ebcdfc9ecfa) () const =0  
| Returns a [MenuItem](../../d0/dcb/classGui_1_1MenuItem.html) tree structure
of menus for this workbench.
[More...](../../d0/d97/classGui_1_1Workbench.html#a5669c13ee2759f8b779c5ebcdfc9ecfa)  
  
virtual [ToolBarItem](../../dc/d03/classGui_1_1ToolBarItem.html) * | [setupToolBars](../../d0/d97/classGui_1_1Workbench.html#a2c4bc1bd254e668905bb54553e5705df) () const =0  
| Returns a [ToolBarItem](../../dc/d03/classGui_1_1ToolBarItem.html) tree
structure of toolbars for this workbench.
[More...](../../d0/d97/classGui_1_1Workbench.html#a2c4bc1bd254e668905bb54553e5705df)  
  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
  
## Constructor & Destructor Documentation

## ◆ Workbench()

Workbench::Workbench  | ( | | ) |   
---|---|---|---|---  
  
## ◆ ~Workbench()

| Workbench::~Workbench  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Reimplemented from
[Gui::Workbench](../../d0/d97/classGui_1_1Workbench.html#ad0d8c30cb6c23742369688a664d34b69).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Mod/Cloud/Gui/Workbench.h
  * FreeCAD/src/Mod/Cloud/Gui/Workbench.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

