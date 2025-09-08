---
url: https://freecad.github.io/SourceDoc/d3/db3/classGui_1_1ViewProvider.html
scraped_at: 2025-09-08T15:17:33.502764
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Gui](../../d9/dad/namespaceGui.html)
  * [ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html)

[List of all members](../../d6/d7b/classGui_1_1ViewProvider-members.html) | Public Member Functions

Gui::ViewProvider Class Reference

General interface for all visual stuff in FreeCAD This class is used to
generate and handle all around visualizing and presenting objects from the
FreeCAD [App](../../dd/dc2/namespaceApp.html "The FreeCAD Application layer.")
layer to the user.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#details)

`#include <ViewProvider.h>`

##  Public Member Functions  
  
---  
virtual [bool](../../d9/db9/classbool.html) | [canAddToSceneGraph](../../d3/db3/classGui_1_1ViewProvider.html#ab546c45d7faf778ee40bb4d2346eb1e8) () const  
| Indicate whether to be added to scene graph or not.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ab546c45d7faf778ee40bb4d2346eb1e8)  
  
virtual std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [claimChildren3D](../../d3/db3/classGui_1_1ViewProvider.html#a94904ffbb658c5beb5f6a9bc6a4eb4cc) (void) const  
| deliver the children belonging to this object this method is used to deliver
the objects to the 3DView which should be grouped under its scene graph.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a94904ffbb658c5beb5f6a9bc6a4eb4cc)  
  
[SoSeparator](../../de/d78/classSoSeparator.html) * | [getAnnotation](../../d3/db3/classGui_1_1ViewProvider.html#a1c8bc4440ecc28cc6d0bfe8456fd0d17) (void)  
virtual [SoSeparator](../../de/d78/classSoSeparator.html) * | [getBackRoot](../../d3/db3/classGui_1_1ViewProvider.html#a055407a1787db878feacee439e690726) (void) const  
virtual [SoGroup](../../d1/d22/classSoGroup.html) * | [getChildRoot](../../d3/db3/classGui_1_1ViewProvider.html#a0dbfaafbec7fd04abd0879f43256eaf3) (void) const  
virtual [SoSeparator](../../de/d78/classSoSeparator.html) * | [getFrontRoot](../../d3/db3/classGui_1_1ViewProvider.html#a6297b38a3fbcda85e28139d58d3b94a7) (void) const  
SoSwitch * | [getModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a21e446fd34aa26bb8461723ee4076a89) (void) const  
virtual [SoSeparator](../../de/d78/classSoSeparator.html) * | [getRoot](../../d3/db3/classGui_1_1ViewProvider.html#a8e06bcc13d05e320094339976bbcc7a9) (void) const  
SoTransform * | [getTransformNode](../../d3/db3/classGui_1_1ViewProvider.html#a1be61de90c4aa986f8be6b3446e6a52a) () const  
|
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#aa9e2dc9a40d2e0f70d562c32078a8293)
()  
| constructor.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aa9e2dc9a40d2e0f70d562c32078a8293)  
  
virtual | [~ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb) ()  
| destructor.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb)  
  
Selection handling  
This group of methods do the selection handling. Here you can define how the
selection for your ViewProfider works.  
virtual [bool](../../d9/db9/classbool.html) | [useNewSelectionModel](../../d3/db3/classGui_1_1ViewProvider.html#a7296be02657836526e5a6cfd9a828d2d) (void) const  
| indicates if the [ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html
"General interface for all visual stuff in FreeCAD This class is used to
generate and handle all aroun...") use the new Selection model
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a7296be02657836526e5a6cfd9a828d2d)  
  
virtual [bool](../../d9/db9/classbool.html) | [isSelectable](../../d3/db3/classGui_1_1ViewProvider.html#af1f5bb44d21931a4bbc9dc87c5ad900c) (void) const  
virtual [bool](../../d9/db9/classbool.html) | [getElementPicked](../../d3/db3/classGui_1_1ViewProvider.html#a0532bd84b0b7f7d57da7a868f3bf90f5) (const SoPickedPoint *, std::string &subname) const  
| return a hit element given the picked point which contains the full node
path
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a0532bd84b0b7f7d57da7a868f3bf90f5)  
  
virtual std::string | [getElement](../../d3/db3/classGui_1_1ViewProvider.html#ac16e04f53374801a23bf5643d30e0ecf) (const SoDetail *) const  
| return a hit element to the selection path or 0
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ac16e04f53374801a23bf5643d30e0ecf)  
  
virtual SoDetail * | [getDetail](../../d3/db3/classGui_1_1ViewProvider.html#aeef7227fd0a9a5ff3a70515d0e20c2d0) (const char *) const  
| return the coin node detail of the subelement
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aeef7227fd0a9a5ff3a70515d0e20c2d0)  
  
virtual [bool](../../d9/db9/classbool.html) | [getDetailPath](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd) (const char *subname, SoFullPath *pPath, [bool](../../d9/db9/classbool.html) append, SoDetail *&det) const  
| return the coin node detail and path to the node of the subelement
[More...](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd)  
  
[int](../../d1/da0/classint.html) | [partialRender](../../d3/db3/classGui_1_1ViewProvider.html#a1ad7f52f266a58575a0f8c67c3d7caf3) (const std::vector< std::string > &subelements, [bool](../../d9/db9/classbool.html) clear)  
| partial rendering setup
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a1ad7f52f266a58575a0f8c67c3d7caf3)  
  
virtual std::vector< [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) > | [getModelPoints](../../d3/db3/classGui_1_1ViewProvider.html#a527d766474f3066fbda47b289b78b58e) (const SoPickedPoint *) const  
virtual std::vector< [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) > | [getSelectionShape](../../d3/db3/classGui_1_1ViewProvider.html#ad541012d1e0bde6dc72cf6f78ee118e1) (const char *Element) const  
| return the highlight lines for a given element or the whole shape
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ad541012d1e0bde6dc72cf6f78ee118e1)  
  
[Base::BoundBox3d](../../db/d07/namespaceBase.html#a0e81c8419e84c4905e08106de65eff54) | [getBoundingBox](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3) (const char *subname=nullptr, [bool](../../d9/db9/classbool.html) transform=true, [MDIView](../../df/d23/classGui_1_1MDIView.html) *view=nullptr) const  
| Return the bound box of this view object.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3)  
  
virtual [bool](../../d9/db9/classbool.html) | [onDelete](../../d3/db3/classGui_1_1ViewProvider.html#a2a15a8d5c80ecec42abe4f53dd8c46da) (const std::vector< std::string > &subNames)  
| Get called if the object is about to get deleted.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a2a15a8d5c80ecec42abe4f53dd8c46da)  
  
virtual void | [beforeDelete](../../d3/db3/classGui_1_1ViewProvider.html#a11add40f80f708b21f13cb66e95fd45a) ()  
| Called before deletion.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a11add40f80f708b21f13cb66e95fd45a)  
  
virtual [bool](../../d9/db9/classbool.html) | [canDelete](../../d3/db3/classGui_1_1ViewProvider.html#abff2f379b2788575b1e27190980bb29d) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj) const  
| Asks the view provider if the given object that is part of its outlist can
be removed from there without breaking it.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#abff2f379b2788575b1e27190980bb29d)  
  
Drag and drop  
To enable drag and drop you have to re-implement
[canDragObjects()](../../d3/db3/classGui_1_1ViewProvider.html#aa2397a3565d308cb853ef70ea172d4eb)
and
[canDropObjects()](../../d3/db3/classGui_1_1ViewProvider.html#aa54f2a8e7f49396d367205a40746d1b8)
to return true. For finer control you can also re-implement
[canDragObject()](../../d3/db3/classGui_1_1ViewProvider.html#abee95130562934e6f6a119064bbae01b)
or
[canDropObject()](../../d3/db3/classGui_1_1ViewProvider.html#a4e729f5e7bcfadb98dcf324cf1f4e78f)
to filter certain object types, by default these methods don't filter any
types. To take action of drag and drop the method
[dragObject()](../../d3/db3/classGui_1_1ViewProvider.html#a42b5e75c0ec1d0169377ce4403cb3b14)
and
[dropObject()](../../d3/db3/classGui_1_1ViewProvider.html#ab8848838fefc7bc36e30c25cb937528e)
must be re-implemented, too.  
virtual [bool](../../d9/db9/classbool.html) | [canDragObjects](../../d3/db3/classGui_1_1ViewProvider.html#aa2397a3565d308cb853ef70ea172d4eb) () const  
| Check whether children can be removed from the view provider by drag and
drop.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aa2397a3565d308cb853ef70ea172d4eb)  
  
virtual [bool](../../d9/db9/classbool.html) | [canDragObject](../../d3/db3/classGui_1_1ViewProvider.html#abee95130562934e6f6a119064bbae01b) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) const  
| Check whether the object can be removed from the view provider by drag and
drop.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#abee95130562934e6f6a119064bbae01b)  
  
virtual void | [dragObject](../../d3/db3/classGui_1_1ViewProvider.html#a42b5e75c0ec1d0169377ce4403cb3b14) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
| Remove a child from the view provider by drag and drop.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a42b5e75c0ec1d0169377ce4403cb3b14)  
  
virtual [bool](../../d9/db9/classbool.html) | [canDropObjects](../../d3/db3/classGui_1_1ViewProvider.html#aa54f2a8e7f49396d367205a40746d1b8) () const  
| Check whether objects can be added to the view provider by drag and drop or
drop only.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aa54f2a8e7f49396d367205a40746d1b8)  
  
virtual [bool](../../d9/db9/classbool.html) | [canDropObject](../../d3/db3/classGui_1_1ViewProvider.html#a4e729f5e7bcfadb98dcf324cf1f4e78f) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) const  
| Check whether the object can be dropped to the view provider by drag and
drop or drop only.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a4e729f5e7bcfadb98dcf324cf1f4e78f)  
  
virtual [bool](../../d9/db9/classbool.html) | [canDragAndDropObject](../../d3/db3/classGui_1_1ViewProvider.html#a4507db15eafbc8b35175a1e2811fa2f7) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) const  
| Return false to force drop only operation for a given object.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a4507db15eafbc8b35175a1e2811fa2f7)  
  
virtual void | [dropObject](../../d3/db3/classGui_1_1ViewProvider.html#ab8848838fefc7bc36e30c25cb937528e) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)  
| Add an object to the view provider by drag and drop.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ab8848838fefc7bc36e30c25cb937528e)  
  
virtual [bool](../../d9/db9/classbool.html) | [canDropObjectEx](../../d3/db3/classGui_1_1ViewProvider.html#a59a1163a60fc6339403df074b65f7858) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *owner, const char *subname, const std::vector< std::string > &elements) const  
| Query object dropping with full qualified name.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a59a1163a60fc6339403df074b65f7858)  
  
virtual std::string | [getDropPrefix](../../d3/db3/classGui_1_1ViewProvider.html#ac2fe674ea09e8f61661baf8b76d2d622) () const  
| return a subname referencing the sub-object holding the dropped objects
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ac2fe674ea09e8f61661baf8b76d2d622)  
  
virtual std::string | [dropObjectEx](../../d3/db3/classGui_1_1ViewProvider.html#ae1b56e5b74e1015f5bc8021f033d9e74) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *owner, const char *subname, const std::vector< std::string > &elements)  
| Add an object with full qualified name to the view provider by drag and
drop.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ae1b56e5b74e1015f5bc8021f033d9e74)  
  
virtual [int](../../d1/da0/classint.html) | [replaceObject](../../d3/db3/classGui_1_1ViewProvider.html#aa87bbb79d39fe7e9cfd75e626a2c9454) ([App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *oldObj, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *newObj)  
| Replace an object to the view provider by drag and drop.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aa87bbb79d39fe7e9cfd75e626a2c9454)  
  
virtual [bool](../../d9/db9/classbool.html) | [showInTree](../../d3/db3/classGui_1_1ViewProvider.html#abaa445361c7608fd6bf30894c3d7aa19) () const  
| Tell the tree view if this object should appear there.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#abaa445361c7608fd6bf30894c3d7aa19)  
  
virtual [bool](../../d9/db9/classbool.html) | [canRemoveChildrenFromRoot](../../d3/db3/classGui_1_1ViewProvider.html#a27ba1150b17ca759a94ee5480cae7ffe) () const  
| Tell the tree view to remove children items from the tree root.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a27ba1150b17ca759a94ee5480cae7ffe)  
  
Display mode methods  
std::string | [getActiveDisplayMode](../../d3/db3/classGui_1_1ViewProvider.html#a032e4e1f1963e1f3293ead1fd8b05fa6) (void) const  
virtual void | [setDisplayMode](../../d3/db3/classGui_1_1ViewProvider.html#ad8b27b6b9b9bd5bb74b09d61d972d385) (const char *ModeName)  
| set the display mode
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ad8b27b6b9b9bd5bb74b09d61d972d385)  
  
virtual const char * | [getDefaultDisplayMode](../../d3/db3/classGui_1_1ViewProvider.html#a8c9fff5b7609631ff18bb9e06530c99a) () const  
| get the default display mode
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a8c9fff5b7609631ff18bb9e06530c99a)  
  
virtual std::vector< std::string > | [getDisplayModes](../../d3/db3/classGui_1_1ViewProvider.html#a26e55171275bb4a559d91698b170b066) (void) const  
| returns a list of all possible display modes
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a26e55171275bb4a559d91698b170b066)  
  
virtual void | [hide](../../d3/db3/classGui_1_1ViewProvider.html#a6ebeb34c881fe262bfa6660683b52319) (void)  
| Hides the view provider.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a6ebeb34c881fe262bfa6660683b52319)  
  
virtual void | [show](../../d3/db3/classGui_1_1ViewProvider.html#a8cb686581d004ed322be5af4cc876301) (void)  
| Shows the view provider.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a8cb686581d004ed322be5af4cc876301)  
  
virtual [bool](../../d9/db9/classbool.html) | [isShow](../../d3/db3/classGui_1_1ViewProvider.html#a002feec6611feb7ea07be1878a5864a3) (void) const  
| checks whether the view provider is visible or not
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a002feec6611feb7ea07be1878a5864a3)  
  
void | [setVisible](../../d3/db3/classGui_1_1ViewProvider.html#a839be69bcafa02679cfa0881b09cc5ed) ([bool](../../d9/db9/classbool.html))  
[bool](../../d9/db9/classbool.html) | [isVisible](../../d3/db3/classGui_1_1ViewProvider.html#a3df346ae0a318f1abe550f869e3c058b) () const  
void | [setLinkVisible](../../d3/db3/classGui_1_1ViewProvider.html#a70a7db3fc975908e585f82bddd96826a) ([bool](../../d9/db9/classbool.html))  
[bool](../../d9/db9/classbool.html) | [isLinkVisible](../../d3/db3/classGui_1_1ViewProvider.html#af0d83b8903606e954fee201cf0847fb9) () const  
virtual void | [setOverrideMode](../../d3/db3/classGui_1_1ViewProvider.html#ad74c21d50c90ffcdca8a7f274f697943) (const std::string &mode)  
| Overrides the display mode with mode.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ad74c21d50c90ffcdca8a7f274f697943)  
  
const std::string | [getOverrideMode](../../d3/db3/classGui_1_1ViewProvider.html#a851989cf62aaf94cc05f6f24a44fbe8a) ()  
Task panel  
With this interface the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...") can steer the appearance of widgets in the task view  
virtual void | [getTaskViewContent](../../d3/db3/classGui_1_1ViewProvider.html#ac44a6d6f5a028f71e4e51a8ab96b6365) (std::vector< [Gui::TaskView::TaskContent](../../d0/d97/classGui_1_1TaskView_1_1TaskContent.html) * > &) const  
| get a list of TaskBoxes associated with this object
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ac44a6d6f5a028f71e4e51a8ab96b6365)  
  
virtual [bool](../../d9/db9/classbool.html) | [keyPressed](../../d3/db3/classGui_1_1ViewProvider.html#a491c4885615fa91504d1e06117a98898) ([bool](../../d9/db9/classbool.html) pressed, [int](../../d1/da0/classint.html) key)  
| is called when the provider is in edit and a key event occurs. Only ESC ends
edit.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a491c4885615fa91504d1e06117a98898)  
  
virtual const char * | [getTransactionText](../../d3/db3/classGui_1_1ViewProvider.html#a0db4e499a881616c4b126efd4341b813) () const  
| Is called by the tree if the user double clicks on the object.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a0db4e499a881616c4b126efd4341b813)  
  
virtual [bool](../../d9/db9/classbool.html) | [doubleClicked](../../d3/db3/classGui_1_1ViewProvider.html#ab692358c177dbbcdeb8599c4576c3846) (void)  
| is called by the tree if the user double clicks on the object
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ab692358c177dbbcdeb8599c4576c3846)  
  
virtual [bool](../../d9/db9/classbool.html) | [mouseMove](../../d3/db3/classGui_1_1ViewProvider.html#ac97b2006300630c2fc546f6e76381684) (const SbVec2s &cursorPos, [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *viewer)  
| is called when the provider is in edit and the mouse is moved
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ac97b2006300630c2fc546f6e76381684)  
  
virtual [bool](../../d9/db9/classbool.html) | [mouseButtonPressed](../../d3/db3/classGui_1_1ViewProvider.html#aef92094223e7104a02f8eab7aae50234) ([int](../../d1/da0/classint.html) button, [bool](../../d9/db9/classbool.html) pressed, const SbVec2s &cursorPos, const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *viewer)  
| is called when the Provider is in edit and the mouse is clicked
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aef92094223e7104a02f8eab7aae50234)  
  
virtual [bool](../../d9/db9/classbool.html) | [mouseWheelEvent](../../d3/db3/classGui_1_1ViewProvider.html#a0d8a5bfdd103ffb0baef0efedc2b865f) ([int](../../d1/da0/classint.html) delta, const SbVec2s &cursorPos, const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *viewer)  
virtual void | [setupContextMenu](../../d3/db3/classGui_1_1ViewProvider.html#a88a89dfe152615b427c8bf6f3747a07b) ([QMenu](../../de/d3d/classQMenu.html) *, [QObject](../../d9/d5b/classQObject.html) *, const char *)  
| set up the context-menu with the supported edit modes
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a88a89dfe152615b427c8bf6f3747a07b)  
  
![-](../../closed.png) Public Member Functions inherited from
[App::TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html)  
virtual const char * | [detachFromDocument](../../d8/d00/classApp_1_1TransactionalObject.html#a17f7538441e315b11eca8ebc047e11f4) ()  
virtual [bool](../../d9/db9/classbool.html) | [isAttachedToDocument](../../d8/d00/classApp_1_1TransactionalObject.html#aa76992a5607128ed5a5a7434cbd857c0) () const  
|
[TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html#af99f0a5b4acf9844a47cbe9a9d626689)
(void)  
| Constructor.
[More...](../../d8/d00/classApp_1_1TransactionalObject.html#af99f0a5b4acf9844a47cbe9a9d626689)  
  
virtual | [~TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html#a995b51d768813d09ffa5620375d304dc) ()  
![-](../../closed.png) Public Member Functions inherited from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)  
[ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f) | [extensionBegin](../../d6/d76/classApp_1_1ExtensionContainer.html#ab709bb3d6a2e77fcdf71323659e26fe3) ()  
|
[ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a1576c15e0c5c9c3866a671c81b410670)
()  
[ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f) | [extensionEnd](../../d6/d76/classApp_1_1ExtensionContainer.html#ade70d6e46e548f4a8f8ff9bc2a277f83) ()  
[App::Extension](../../d8/dc7/classApp_1_1Extension.html) * | [getExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a329e85b59ccbc63a619c4d31325f23d8) ([Base::Type](../../dc/dee/classBase_1_1Type.html), [bool](../../d9/db9/classbool.html) derived=true, [bool](../../d9/db9/classbool.html) no_except=false) const  
[App::Extension](../../d8/dc7/classApp_1_1Extension.html) * | [getExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a7ccfc3ce3ac85344e07766d3d7760f50) (const std::string &name) const  
template<typename [ExtensionT](../../df/d73/classExtensionT.html) >  
[ExtensionT](../../df/d73/classExtensionT.html) * | [getExtensionByType](../../d6/d76/classApp_1_1ExtensionContainer.html#a0711e5ec3feeac1afc569569784a4994) ([bool](../../d9/db9/classbool.html) no_except=false, [bool](../../d9/db9/classbool.html) derived=true) const  
std::vector< [Extension](../../d8/dc7/classApp_1_1Extension.html) * > | [getExtensionsDerivedFrom](../../d6/d76/classApp_1_1ExtensionContainer.html#a8b1505a7cdc7d5f2c43e0d3cfaa8100c) ([Base::Type](../../dc/dee/classBase_1_1Type.html) [type](../../d9/d98/classtype.html)) const  
template<typename [ExtensionT](../../df/d73/classExtensionT.html) >  
std::vector< [ExtensionT](../../df/d73/classExtensionT.html) * > | [getExtensionsDerivedFromType](../../d6/d76/classApp_1_1ExtensionContainer.html#a9f5f7c38f59fde6f0d7a22d242ac7aa6) () const  
[bool](../../d9/db9/classbool.html) | [hasExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#adae9aba02ce19d1611f1bb3447ee936e) ([Base::Type](../../dc/dee/classBase_1_1Type.html), [bool](../../d9/db9/classbool.html) derived=true) const  
[bool](../../d9/db9/classbool.html) | [hasExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a8e5befbc7a981a91f6912697dea587e1) (const std::string &name) const  
[bool](../../d9/db9/classbool.html) | [hasExtensions](../../d6/d76/classApp_1_1ExtensionContainer.html#a56345b1e7049b01ee7620192f06950dd) () const  
void | [registerExtension](../../d6/d76/classApp_1_1ExtensionContainer.html#a007eb07d5313eaa01d14462d7b7d960d) ([Base::Type](../../dc/dee/classBase_1_1Type.html) extension, [App::Extension](../../d8/dc7/classApp_1_1Extension.html) *ext)  
virtual | [~ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a3590d0f208eaf38fd6fdde59534c5a02) ()  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [getPropertyByName](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897) (const char *name) const override  
| find a property by its name
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a18f4294fbe017fea5ee3ee487fb7e897)  
  
virtual const char * | [getPropertyName](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the name of a property
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a5d91112962ee5c459efa09469ebce4d0)  
  
virtual void | [getPropertyMap](../../d6/d76/classApp_1_1ExtensionContainer.html#a12d88a996edd035623450a5b8da10d03) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const override  
| get all properties of the class (including properties of the parent)
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a12d88a996edd035623450a5b8da10d03)  
  
virtual void | [getPropertyList](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const override  
| get all properties of the class (including properties of the parent)
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a4b980230637c28a4159575a8955c9fe6)  
  
virtual short | [getPropertyType](../../d6/d76/classApp_1_1ExtensionContainer.html#afd7697c47292ff6d6b7fce5bff86941f) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#afd7697c47292ff6d6b7fce5bff86941f)  
  
virtual short | [getPropertyType](../../d6/d76/classApp_1_1ExtensionContainer.html#afc5151a1d5fa7822d9f6fd1bb4bc4004) (const char *name) const override  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#afc5151a1d5fa7822d9f6fd1bb4bc4004)  
  
virtual const char * | [getPropertyGroup](../../d6/d76/classApp_1_1ExtensionContainer.html#a0667cf5204a8854212a23fd5d53f5b1d) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a0667cf5204a8854212a23fd5d53f5b1d)  
  
virtual const char * | [getPropertyGroup](../../d6/d76/classApp_1_1ExtensionContainer.html#a4fba6aeb529e0bbe523bb2cd62d191fc) (const char *name) const override  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a4fba6aeb529e0bbe523bb2cd62d191fc)  
  
virtual const char * | [getPropertyDocumentation](../../d6/d76/classApp_1_1ExtensionContainer.html#a4f2af686b6d232b650bf512e0bbdc223) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const override  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#a4f2af686b6d232b650bf512e0bbdc223)  
  
virtual const char * | [getPropertyDocumentation](../../d6/d76/classApp_1_1ExtensionContainer.html#afd218927cb4c252f090dd1f377ced7de) (const char *name) const override  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#afd218927cb4c252f090dd1f377ced7de)  
  
virtual void | [Save](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5)  
  
void | [saveExtensions](../../d6/d76/classApp_1_1ExtensionContainer.html#a8f71a6ea625198e2d2e3067f2a367df0) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
void | [restoreExtensions](../../d6/d76/classApp_1_1ExtensionContainer.html#ab55b9130d18351d880910dd869efd9ab) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
![-](../../closed.png) Public Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [addDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#aeb460dcdedde87f84dbab68d0865bfa6) (const char *[type](../../d9/d98/classtype.html), const char *name=nullptr, const char *group=nullptr, const char *doc=nullptr, short attr=0, [bool](../../d9/db9/classbool.html) ro=false, [bool](../../d9/db9/classbool.html) hidden=false)  
[bool](../../d9/db9/classbool.html) | [changeDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a322267f4f7ee6ee360535cdc5dce3612) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop, const char *group, const char *doc)  
virtual void | [editProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a001e36affede2983bb0ac4852f2fc617) (const char *)  
virtual [App::Property](../../d0/da9/classApp_1_1Property.html) * | [getDynamicPropertyByName](../../d5/d48/classApp_1_1PropertyContainer.html#aa61e4c2e94abf8310ff9d790e4b54564) (const char *name) const  
[DynamicProperty::PropData](../../d8/df9/structApp_1_1DynamicProperty_1_1PropData.html) | [getDynamicPropertyData](../../d5/d48/classApp_1_1PropertyContainer.html#aa6ac51c527bc5f13d8d6d5ddc4e51f2e) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
virtual std::vector< std::string > | [getDynamicPropertyNames](../../d5/d48/classApp_1_1PropertyContainer.html#a71fa8d125dc74b919e994a79985f601b) () const  
virtual std::string | [getFullName](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d) () const  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694) (void) const  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694)  
  
virtual [Property](../../d0/da9/classApp_1_1Property.html) * | [getPropertyByName](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2) (const char *name) const  
| find a property by its name
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a503f7cfc13b71bc44e7adc69c5386ff2)  
  
virtual const char * | [getPropertyDocumentation](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50) (const char *name) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ad0513de3a16613c999042b9e6f7a2b50)  
  
virtual const char * | [getPropertyDocumentation](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#af99578209df21cea05c3ac58eef29912)  
  
virtual const char * | [getPropertyGroup](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a) (const char *name) const  
| get the Group of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a88ec0df8c43f5dd99b8ec7290dfc0c4a)  
  
virtual const char * | [getPropertyGroup](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Group of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a73646926e3c95d14191f517d0eef1356)  
  
virtual void | [getPropertyList](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a) (std::vector< [Property](../../d0/da9/classApp_1_1Property.html) * > &List) const  
| get all properties of the class (including properties of the parent)
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ae56a9bf84f00676cc6e75ebba374c74a)  
  
virtual void | [getPropertyMap](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8) (std::map< std::string, [Property](../../d0/da9/classApp_1_1Property.html) * > &Map) const  
| get all properties of the class (including properties of the parent)
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a2f1fd43422927629672f2ee616a7f3a8)  
  
virtual const char * | [getPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the name of a property
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a9012f48b9db8334529d0ad9ea258c981)  
  
virtual void | [getPropertyNamedList](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f) (std::vector< std::pair< const char *, [Property](../../d0/da9/classApp_1_1Property.html) * > > &List) const  
| get all properties with their names, may contain duplicates and aliases
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ac1db173138f821f169de2b20111c935f)  
  
const char * | [getPropertyPrefix](../../d5/d48/classApp_1_1PropertyContainer.html#afd2652f19f3b1db90309c5a69713507c) () const  
virtual short | [getPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4) (const char *name) const  
| get the Type of a named [Property](../../d0/da9/classApp_1_1Property.html
"Base class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a4bd6348aaae6cbfbcbf45bd5077e4dc4)  
  
virtual short | [getPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| get the Type of a [Property](../../d0/da9/classApp_1_1Property.html "Base
class of all properties This is the father of all properties.")
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a28b916a6e04caaefe7823d39eabb0510)  
  
[bool](../../d9/db9/classbool.html) | [isHidden](../../d5/d48/classApp_1_1PropertyContainer.html#a1a89b20166f4e4a3feea04a84179d1ed) (const char *name) const  
| check if the named property is hidden
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a1a89b20166f4e4a3feea04a84179d1ed)  
  
[bool](../../d9/db9/classbool.html) | [isHidden](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| check if the property is hidden
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a70f7657757146a64ef861f0490b02374)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d5/d48/classApp_1_1PropertyContainer.html#a7375800ad653da01d4b5a98f5fb69799) (const char *name) const  
| check if the named property is read-only
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a7375800ad653da01d4b5a98f5fb69799)  
  
[bool](../../d9/db9/classbool.html) | [isReadOnly](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) const  
| check if the property is read-only
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ae9a54472ac2185af2717b4b220439082)  
  
virtual void | [onPropertyStatusChanged](../../d5/d48/classApp_1_1PropertyContainer.html#a25dc796f1aecab39ceeed8335097b758) (const [Property](../../d0/da9/classApp_1_1Property.html) &prop, unsigned long oldStatus)  
|
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#af08e2297f31f338356f8eb8f2000ff97)
()  
| A constructor.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#af08e2297f31f338356f8eb8f2000ff97)  
  
virtual [bool](../../d9/db9/classbool.html) | [removeDynamicProperty](../../d5/d48/classApp_1_1PropertyContainer.html#a7e5425268a06b3e8a12f45abbbcfd653) (const char *name)  
virtual void | [Restore](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944)  
  
virtual void | [Save](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
| This method is used to save properties to an XML document.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482)  
  
void | [setPropertyPrefix](../../d5/d48/classApp_1_1PropertyContainer.html#aeac678dd3506bf850148f891fe368446) (const char *prefix)  
void | [setPropertyStatus](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed) (unsigned char bit, [bool](../../d9/db9/classbool.html) value)  
| set the Status bit of all properties at once
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a6be7980b23d8805f2b19daf2b70778ed)  
  
virtual | [~PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#abca525c7322e6aa891390002c1b8b309) ()  
| A destructor.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#abca525c7322e6aa891390002c1b8b309)  
  
![-](../../closed.png) Public Member Functions inherited from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)  
void | [dumpToStream](../../d9/d25/classBase_1_1Persistence.html#a3f09f422620031b240b4f01c044b49c7) (std::ostream &stream, [int](../../d1/da0/classint.html) compression)  
virtual unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9) () const =0  
| This method is used to get the size of objects It is not meant to have the
exact size, it is more or less an estimation which runs fast! Is it two bytes
or a GB?
[More...](../../d9/d25/classBase_1_1Persistence.html#a8fb0589baca20935e80323d914b91ba9)  
  
virtual [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getTypeId](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596) (void) const  
virtual void | [Restore](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc) ([XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)=0  
| This method is used to restore properties from an XML document.
[More...](../../d9/d25/classBase_1_1Persistence.html#ad51f9a87f0e35c859aa446f7a05d2dbc)  
  
virtual void | [RestoreDocFile](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b) ([Reader](../../d1/d1f/classBase_1_1Reader.html) &)  
| This method is used to restore large amounts of data from a file In this
method you simply stream in your
[SaveDocFile()](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45
"This method is used to save large amounts of data to a binary file.") saved
data.
[More...](../../d9/d25/classBase_1_1Persistence.html#a65260f99c6e0449f6caca2bc71efe37b)  
  
void | [restoreFromStream](../../d9/d25/classBase_1_1Persistence.html#acf69a699ddf6fc30ff05fa70a27cc2dd) (std::istream &stream)  
virtual void | [Save](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436) ([Writer](../../dd/d4d/classBase_1_1Writer.html) &) const =0  
| This method is used to save properties to an XML document.
[More...](../../d9/d25/classBase_1_1Persistence.html#a0045bae1285a7176f3012454c4953436)  
  
virtual void | [SaveDocFile](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45) ([Writer](../../dd/d4d/classBase_1_1Writer.html) &) const  
| This method is used to save large amounts of data to a binary file.
[More...](../../d9/d25/classBase_1_1Persistence.html#af6ddc03fc798b7eb485afe4d98ec5e45)  
  
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
  
  
## Edit methods  
  
---  
if the Viewprovider goes in edit mode you can handle most of the events in the
viewer by yourself  
enum | [EditMode](../../d3/db3/classGui_1_1ViewProvider.html#a79aefd2d455334520a6c768dea02f077) { [Default](../../d3/db3/classGui_1_1ViewProvider.html#a79aefd2d455334520a6c768dea02f077a58935290bc46b4a9ef146b3c90ef256f) = 0 , [Transform](../../d3/db3/classGui_1_1ViewProvider.html#a79aefd2d455334520a6c768dea02f077aa0fa1997044be598cad8a63cfceb3946) , [Cutting](../../d3/db3/classGui_1_1ViewProvider.html#a79aefd2d455334520a6c768dea02f077a2d8cd4ed8f5b6ad6d7e9038f1ecc3969) , [Color](../../d3/db3/classGui_1_1ViewProvider.html#a79aefd2d455334520a6c768dea02f077a700bd26384325e1e2ac30806c9d34a7d) }  
virtual [ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html) * | [startEditing](../../d3/db3/classGui_1_1ViewProvider.html#a4e61647f7d508c3472f202661c4fb8a8) ([int](../../d1/da0/classint.html) ModNum=0)  
[bool](../../d9/db9/classbool.html) | [isEditing](../../d3/db3/classGui_1_1ViewProvider.html#a710882933315d6c4f596afe07ebc96f1) () const  
void | [finishEditing](../../d3/db3/classGui_1_1ViewProvider.html#ae3a70413039e06002dd1875fa9595ecb) ()  
virtual void | [setEditViewer](../../d3/db3/classGui_1_1ViewProvider.html#a17d5877e78478bbcd46608e3438b4c60) ([View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *, [int](../../d1/da0/classint.html) ModNum)  
| adjust viewer settings when editing a view provider
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a17d5877e78478bbcd46608e3438b4c60)  
  
virtual void | [unsetEditViewer](../../d3/db3/classGui_1_1ViewProvider.html#aa2eb675d9f93519b94101690af7e95bd) ([View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *)  
| restores viewer settings when leaving editing mode
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aa2eb675d9f93519b94101690af7e95bd)  
  
virtual [bool](../../d9/db9/classbool.html) | [setEdit](../../d3/db3/classGui_1_1ViewProvider.html#a99bfa17a3eedcec978d56b252a653fea) ([int](../../d1/da0/classint.html) ModNum)  
| is called by the document when the provider goes in edit mode
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a99bfa17a3eedcec978d56b252a653fea)  
  
virtual void | [unsetEdit](../../d3/db3/classGui_1_1ViewProvider.html#ae74f9e97a6f5f027bb25fb93debc5fa9) ([int](../../d1/da0/classint.html) ModNum)  
| is called when you lose the edit mode
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ae74f9e97a6f5f027bb25fb93debc5fa9)  
  
[int](../../d1/da0/classint.html) | [getEditingMode](../../d3/db3/classGui_1_1ViewProvider.html#a6b5e1f18cdd2fcc2f27c80610a5d632b) () const  
| return the edit mode or -1 if nothing is being edited
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a6b5e1f18cdd2fcc2f27c80610a5d632b)  
  
  
## Signals of the view provider  
  
---  
boost::signals2::signal< void()> | [signalChangeIcon](../../d3/db3/classGui_1_1ViewProvider.html#a86939f66116352ceba8ece6d9543a9b7)  
| signal on icon change
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a86939f66116352ceba8ece6d9543a9b7)  
  
boost::signals2::signal< void(const QString &)> | [signalChangeToolTip](../../d3/db3/classGui_1_1ViewProvider.html#af840db43ac4f631a871782ea0bfa41b7)  
| signal on tooltip change
[More...](../../d3/db3/classGui_1_1ViewProvider.html#af840db43ac4f631a871782ea0bfa41b7)  
  
boost::signals2::signal< void(const QString &)> | [signalChangeStatusTip](../../d3/db3/classGui_1_1ViewProvider.html#a82a7217508422a72398bc1fe0106eb25)  
| signal on status tip change
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a82a7217508422a72398bc1fe0106eb25)  
  
virtual void | [update](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8) (const [App::Property](../../d0/da9/classApp_1_1Property.html) *)  
| update the content of the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...") this method have to implement the recalculation of the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...").
[More...](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8)  
  
virtual void | [updateData](../../d3/db3/classGui_1_1ViewProvider.html#a84b28e19898179755940c2b77e03b56a) (const [App::Property](../../d0/da9/classApp_1_1Property.html) *)  
[bool](../../d9/db9/classbool.html) | [isUpdatesEnabled](../../d3/db3/classGui_1_1ViewProvider.html#aad2c2352ff074e6049c65190a2ad908d) () const  
void | [setUpdatesEnabled](../../d3/db3/classGui_1_1ViewProvider.html#aa6c012b46ca6ba7d41814323b3c0f9e1) ([bool](../../d9/db9/classbool.html) enable)  
unsigned long | [getStatus](../../d3/db3/classGui_1_1ViewProvider.html#a6ea47342a5d93866f72ae6539a2f0e55) () const  
| return the status bits
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a6ea47342a5d93866f72ae6539a2f0e55)  
  
[bool](../../d9/db9/classbool.html) | [testStatus](../../d3/db3/classGui_1_1ViewProvider.html#ae87ece80cde8573867485f8e091f18fe) ([ViewStatus](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ff) pos) const  
void | [setStatus](../../d3/db3/classGui_1_1ViewProvider.html#a7a2d73b62ec2e1290f3db16c1af5e0a1) ([ViewStatus](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ff) pos, [bool](../../d9/db9/classbool.html) on)  
std::string | [toString](../../d3/db3/classGui_1_1ViewProvider.html#afcc561b1e8fdd949139f3e58a68e5b05) () const  
[PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d3/db3/classGui_1_1ViewProvider.html#aedc8b6ee0d29756e6be6d0c3ed0a0aee) ()  
| This method returns the Python wrapper for a C++ object.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aedc8b6ee0d29756e6be6d0c3ed0a0aee)  
  
  
## Methods used by the Tree  
  
---  
If you want to take control over the viewprovider specific overlay icons, that
will be grayed out together with the base icon, you can reimplement this
method.  
[SoSeparator](../../de/d78/classSoSeparator.html) * | [pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e)  
| The root Separator of the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...").
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e)  
  
SoTransform * | [pcTransform](../../d3/db3/classGui_1_1ViewProvider.html#a310fa4e016c1c6fb01a075710eb666a7)  
| this is transformation for the provider
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a310fa4e016c1c6fb01a075710eb666a7)  
  
const char * | [sPixmap](../../d3/db3/classGui_1_1ViewProvider.html#a8ecdd67f362fd1a409053e3562ba5ba1)  
SoSwitch * | [pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54)  
| this is the mode switch, all the different viewing modes are collected here
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54)  
  
[SoSeparator](../../de/d78/classSoSeparator.html) * | [pcAnnotation](../../d3/db3/classGui_1_1ViewProvider.html#ab23920cdacf0330b04a7504f14e8f7e0)  
| The root separator for annotations.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ab23920cdacf0330b04a7504f14e8f7e0)  
  
ViewProviderPy * | [pyViewObject](../../d3/db3/classGui_1_1ViewProvider.html#a943e4042fb9fef225bcc04083fa904df)  
std::string | [overrideMode](../../d3/db3/classGui_1_1ViewProvider.html#a30d0a73702d5fe359395cad8e978941a)  
std::bitset< 32 > | [StatusBits](../../d3/db3/classGui_1_1ViewProvider.html#a2217a1828a2a84aa02177f06a33e9884)  
virtual QIcon | [getIcon](../../d3/db3/classGui_1_1ViewProvider.html#af6bd43d711cf91767cadf6fcd2827b47) (void) const  
| deliver the icon shown in the tree view
[More...](../../d3/db3/classGui_1_1ViewProvider.html#af6bd43d711cf91767cadf6fcd2827b47)  
  
virtual QIcon | [mergeColorfulOverlayIcons](../../d3/db3/classGui_1_1ViewProvider.html#ad945a3a5e29139bc6823ad80152e9f87) (const QIcon &orig) const  
virtual std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [claimChildren](../../d3/db3/classGui_1_1ViewProvider.html#af51254c2d4352f0c36f75c6e909ef1df) (void) const  
| deliver the children belonging to this object this method is used to deliver
the objects to the tree framework which should be grouped under its label.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#af51254c2d4352f0c36f75c6e909ef1df)  
  
virtual QIcon | [mergeGreyableOverlayIcons](../../d3/db3/classGui_1_1ViewProvider.html#aec47e82b8933db21dde528746150e3d2) (const QIcon &orig) const  
virtual void | [setModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#aebaedef79623db445f3ec055c365d97f) ()  
| Turn on mode switch.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aebaedef79623db445f3ec055c365d97f)  
  
  
## Color management methods  
  
---  
virtual std::map< std::string, [App::Color](../../d3/d3a/classApp_1_1Color.html) > | [getElementColors](../../d3/db3/classGui_1_1ViewProvider.html#adb2812496e4e7143f9751c3143a42e78) (const char *element=nullptr) const  
virtual void | [setElementColors](../../d3/db3/classGui_1_1ViewProvider.html#ac040c8df19e9d99891f668c84b7c37e4) (const std::map< std::string, [App::Color](../../d3/d3a/classApp_1_1Color.html) > &colors)  
static const std::string & | [hiddenMarker](../../d3/db3/classGui_1_1ViewProvider.html#ad7ec8cdec25d51ca8309c477c6728a3c) ()  
static const char * | [hasHiddenMarker](../../d3/db3/classGui_1_1ViewProvider.html#a7a9cd7fe3f4d16e3094e5178cefdc45f) (const char *subname)  
  
## direct handling methods  
  
---  
This group of methods is to direct influence the appearance of the viewed
content. It's only for fast interactions! If you want to set the visual
parameters you have to do it on the object viewed by this provider!  
virtual void | [setTransformation](../../d3/db3/classGui_1_1ViewProvider.html#a8d06af6b975e2907f1971bd712f95cf0) (const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rcMatrix)  
| set the viewing transformation of the provider
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a8d06af6b975e2907f1971bd712f95cf0)  
  
virtual void | [setTransformation](../../d3/db3/classGui_1_1ViewProvider.html#aa1f2629567be76436b9ae3aebac1779d) (const SbMatrix &rcMatrix)  
virtual [MDIView](../../df/d23/classGui_1_1MDIView.html) * | [getMDIView](../../d3/db3/classGui_1_1ViewProvider.html#a6675596e2c8b6e05d13212d468d8f201) () const  
virtual void | [Restore](../../d3/db3/classGui_1_1ViewProvider.html#a4e6bcf20d9aa065b34edc83e9619ba51) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
| This method is used to restore properties from an XML document.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a4e6bcf20d9aa065b34edc83e9619ba51)  
  
[bool](../../d9/db9/classbool.html) | [isRestoring](../../d3/db3/classGui_1_1ViewProvider.html#a02fb7fa1935105bf536642b12932a64e) ()  
static SbMatrix | [convert](../../d3/db3/classGui_1_1ViewProvider.html#a5818a11a94776a34ad509c27d824c90d) (const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) &rcMatrix)  
static [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) | [convert](../../d3/db3/classGui_1_1ViewProvider.html#ade9332382bcb86d072cc033c9ae62d4f) (const SbMatrix &sbMat)  
static void | [eventCallback](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99) (void *ud, SoEventCallback *node)  
  
## Display mask modes  
  
---  
Mainly controls an SoSwitch node which selects the display mask modes. The
number of display mask modes doesn't necessarily match with the number of
display modes. E.g. various display modes like Gaussian curvature, mean
curvature or gray values are displayed by one display mask mode that handles
color values.  
void | [addDisplayMaskMode](../../d3/db3/classGui_1_1ViewProvider.html#af61b54ac266120fb12c5cdacf3f17b43) ([SoNode](../../d0/d2d/classSoNode.html) *node, const char *[type](../../d9/d98/classtype.html))  
| Adds a new display mask mode.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#af61b54ac266120fb12c5cdacf3f17b43)  
  
void | [setDisplayMaskMode](../../d3/db3/classGui_1_1ViewProvider.html#a564f691d12e5fd38892c1bcb7070bd64) (const char *[type](../../d9/d98/classtype.html))  
| Activates the display mask mode _type_.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a564f691d12e5fd38892c1bcb7070bd64)  
  
[SoNode](../../d0/d2d/classSoNode.html) * | [getDisplayMaskMode](../../d3/db3/classGui_1_1ViewProvider.html#a85cd744e0f609177ccd9c12c8180e0e5) (const char *[type](../../d9/d98/classtype.html)) const  
| Get the node to the display mask mode _type_.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a85cd744e0f609177ccd9c12c8180e0e5)  
  
std::vector< std::string > | [getDisplayMaskModes](../../d3/db3/classGui_1_1ViewProvider.html#a50c5f8db7d62c9af69df1ebec2629dcb) () const  
| Returns a list of added display mask modes.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a50c5f8db7d62c9af69df1ebec2629dcb)  
  
void | [setDefaultMode](../../d3/db3/classGui_1_1ViewProvider.html#af8825fd59edf8fbfd55afc23d32f97e6) ([int](../../d1/da0/classint.html))  
[int](../../d1/da0/classint.html) | [getDefaultMode](../../d3/db3/classGui_1_1ViewProvider.html#a6440355d2a65c3cb4d76c6ff95a05292) () const  
virtual void | [setRenderCacheMode](../../d3/db3/classGui_1_1ViewProvider.html#adfec94f0ed4b8564d5dc77c92e57d088) ([int](../../d1/da0/classint.html))  
[bool](../../d9/db9/classbool.html) | [checkRecursion](../../d3/db3/classGui_1_1ViewProvider.html#ac6e1013345d847abd378ccc0b4461fbc) ([SoNode](../../d0/d2d/classSoNode.html) *)  
| Helper method to check that the node is valid, i.e.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ac6e1013345d847abd378ccc0b4461fbc)  
  
SoPickedPoint * | [getPointOnRay](../../d3/db3/classGui_1_1ViewProvider.html#ad15840ae4de52552d452b3733e3c3dfa) (const SbVec2s &pos, const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *viewer) const  
| Helper method to get picked entities while editing.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#ad15840ae4de52552d452b3733e3c3dfa)  
  
SoPickedPoint * | [getPointOnRay](../../d3/db3/classGui_1_1ViewProvider.html#aec3cae0d3db88007897e3f7eb86df2a8) (const SbVec3f &pos, const SbVec3f &dir, const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *viewer) const  
| Helper method to get picked entities while editing.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#aec3cae0d3db88007897e3f7eb86df2a8)  
  
void | [onBeforeChange](../../d3/db3/classGui_1_1ViewProvider.html#a4ffbd2052a9e36ebb8047bb5f855c650) (const [App::Property](../../d0/da9/classApp_1_1Property.html) *prop)  
| Reimplemented from subclass.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a4ffbd2052a9e36ebb8047bb5f855c650)  
  
void | [onChanged](../../d3/db3/classGui_1_1ViewProvider.html#a825924c3bb8e3aaed03215ef12867392) (const [App::Property](../../d0/da9/classApp_1_1Property.html) *prop)  
| Reimplemented from subclass.
[More...](../../d3/db3/classGui_1_1ViewProvider.html#a825924c3bb8e3aaed03215ef12867392)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Public Types inherited from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)  
typedef std::map< [Base::Type](../../dc/dee/classBase_1_1Type.html), [App::Extension](../../d8/dc7/classApp_1_1Extension.html) * >::iterator | [ExtensionIterator](../../d6/d76/classApp_1_1ExtensionContainer.html#a4e22c5f8e80b19a76ae50715a218aa7f)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::Persistence](../../d9/d25/classBase_1_1Persistence.html)  
static void * | [create](../../d9/d25/classBase_1_1Persistence.html#a8cecc55259bc79661a33a2d8df9764b7) (void)  
static std::string | [encodeAttribute](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec) (const std::string &)  
| Encodes an attribute upon saving.
[More...](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec)  
  
static [Base::Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56) (void)  
static void | [init](../../d9/d25/classBase_1_1Persistence.html#a4e9f73ac099dd794f6c87946f61cee0e) (void)  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void * | [create](../../df/d4d/classBase_1_1BaseClass.html#a4e83383416327822cfbc39e264c43d6a) ()  
static [Type](../../dc/dee/classBase_1_1Type.html) | [getClassTypeId](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca) ()  
static void | [init](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7) ()  
![-](../../closed.png) Protected Member Functions inherited from
[App::TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html)  
void | [onBeforeChangeProperty](../../d8/d00/classApp_1_1TransactionalObject.html#aefa55dd46b014db2e5dafe7310480233) ([Document](../../d8/d3e/classApp_1_1Document.html) *doc, const [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
![-](../../closed.png) Protected Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
virtual const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) & | [getPropertyData](../../d5/d48/classApp_1_1PropertyContainer.html#ae924a438accf1e0dbe369449ffbc9c84) (void) const  
virtual void | [handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, const char *PropName)  
|
[PropertyContainer::handleChangedPropertyName](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573
"PropertyContainer::handleChangedPropertyName is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of this property container.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a07d0bff09366c73e5d5e4f319b9e2573)  
  
virtual void | [handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader, const char *TypeName, [Property](../../d0/da9/classApp_1_1Property.html) *prop)  
|
[PropertyContainer::handleChangedPropertyType](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923
"PropertyContainer::handleChangedPropertyType is called during restore to
possibly fix reading of olde...") is called during restore to possibly fix
reading of older versions of the property container.
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ac744fd831934155ea03011e63c280923)  
  
virtual void | [onBeforeChange](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
| get called before the value is changed
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057)  
  
virtual void | [onChanged](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34) (const [Property](../../d0/da9/classApp_1_1Property.html) *)  
| get called by the container when a property has changed
[More...](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34)  
  
![-](../../closed.png) Static Protected Member Functions inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
static const [PropertyData](../../d2/d02/structApp_1_1PropertyData.html) * | [getPropertyDataPtr](../../d5/d48/classApp_1_1PropertyContainer.html#a8649f534ecaa91393925fa514ed29e4b) (void)  
![-](../../closed.png) Static Protected Member Functions inherited from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html)  
static void | [initSubclass](../../df/d4d/classBase_1_1BaseClass.html#a09c22c2a82083180f9ba04b04ca6e7e2) ([Base::Type](../../dc/dee/classBase_1_1Type.html) &toInit, const char *ClassName, const char *ParentName, [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) method=nullptr)  
![-](../../closed.png) Protected Attributes inherited from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html)  
[DynamicProperty](../../d5/d76/classApp_1_1DynamicProperty.html) | [dynamicProps](../../d5/d48/classApp_1_1PropertyContainer.html#a294ab9bc379f24c43b2aeeb39ccd0f99)  
  
## Detailed Description

General interface for all visual stuff in FreeCAD This class is used to
generate and handle all around visualizing and presenting objects from the
FreeCAD [App](../../dd/dc2/namespaceApp.html "The FreeCAD Application layer.")
layer to the user.

This class and its descendents have to be implemented for any object type in
order to show them in the 3DView and
[TreeView](../../d9/ddf/classGui_1_1TreeView.html).

## Member Enumeration Documentation

## ◆ EditMode

enum
[Gui::ViewProvider::EditMode](../../d3/db3/classGui_1_1ViewProvider.html#a79aefd2d455334520a6c768dea02f077)  
---  
  
Enumerator  
---  
Default |   
Transform |   
Cutting |   
Color |   
  
## Constructor & Destructor Documentation

## ◆ ViewProvider()

ViewProvider::ViewProvider  | ( | | ) |   
---|---|---|---|---  
  
constructor.

References
[Gui::UpdateData](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ffa9867733e397c214c7d749fab0c326cf7).

## ◆ ~ViewProvider()

| ViewProvider::~ViewProvider  | ( | | ) |   
---|---|---|---|---  
virtual  
  
destructor.

Reimplemented in
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb).

References
[pcAnnotation](../../d3/db3/classGui_1_1ViewProvider.html#ab23920cdacf0330b04a7504f14e8f7e0),
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54),
[pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e),
[pcTransform](../../d3/db3/classGui_1_1ViewProvider.html#a310fa4e016c1c6fb01a075710eb666a7),
and
[pyViewObject](../../d3/db3/classGui_1_1ViewProvider.html#a943e4042fb9fef225bcc04083fa904df).

## Member Function Documentation

## ◆ addDisplayMaskMode()

void ViewProvider::addDisplayMaskMode  | ( | [SoNode](../../d0/d2d/classSoNode.html) *  | _node_ ,   
---|---|---|---  
|  | const char *  | _type_  
| ) | |   
  
Adds a new display mask mode.

References
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54).

Referenced by
[Gui::ViewProviderAnnotation::attach()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#ab50892bdc3b37f9da77b36cac3014cf6),
[Gui::ViewProviderAnnotationLabel::attach()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a8f11a6d6720e62e7faafaadb5f6748be),
[Gui::ViewProviderMeasureDistance::attach()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a6dc8ac66e44cb7cc2804cecf07715523),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[FemGui::ViewProviderFemConstraint::attach()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a1fd0a4f1a9e50b9f8da2146c69a3c0f9),
[MeshGui::ViewProviderMesh::attach()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#adb9b6c0cd97337657aabd81bac13e35e),
[MeshGui::ViewProviderMeshTransform::attach()](../../d2/d2b/classMeshGui_1_1ViewProviderMeshTransform.html#a97ee480b01611a1b76f3639ea069c3aa),
[MeshGui::ViewProviderMeshTransformDemolding::attach()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ad48bd55861a901d4920e4fc20a420e9d),
[PartGui::ViewProviderCurveNet::attach()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#a726ef860fd05b8c00a5aa608c6658cb7),
[PartGui::ViewProviderPartReference::attach()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#aea0960774c483564bd0bd9f284e9ca28),
[PartDesignGui::ViewProviderAddSub::attach()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a87c8377f96db07446ff81f9c0c741f22),
[PointsGui::ViewProviderScattered::attach()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab6910e935629c8fe18fed5409c9521a0),
[PointsGui::ViewProviderStructured::attach()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#aabe6e709079ef4dd2d44b687db5f1dd7),
[Gui::ViewProviderPlacement::attach()](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a52f3c94abcc3e4ca1a6632cde18a0955),
[PartGui::ViewProviderPartExt::attach()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a797fa2d8c1b12da5c8fccb3faaf033d6),
[PartDesignGui::ViewProviderDatum::attach()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a68c38571568f0796648a34849f99d36a),
[MeshGui::ViewProviderFace::attach()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#ad7b2603bd549bbf7120aa424fc0adf77),
[InspectionGui::ViewProviderInspection::attach()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a79ac9ba624d2a99d8753d7ee9c7a96ad),
[MeshGui::ViewProviderMeshNode::attach()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6a5ec09c3510569615ddd8290875351a),
[MeshGui::ViewProviderMeshCurvature::attach()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad36ed9ef7edb7c4ec98d622ec6acf48c),
[MeshGui::ViewProviderMeshOrientation::attach()](../../d1/d8e/classMeshGui_1_1ViewProviderMeshOrientation.html#a215b5950716e55e703afb5dc616453bb),
[MeshGui::ViewProviderMeshNonManifolds::attach()](../../d5/d95/classMeshGui_1_1ViewProviderMeshNonManifolds.html#a12f184db6b3861d1d7154568db668dc8),
[MeshGui::ViewProviderMeshNonManifoldPoints::attach()](../../d6/d60/classMeshGui_1_1ViewProviderMeshNonManifoldPoints.html#a349ab901bdc21b06b57bd312e0ed9271),
[MeshGui::ViewProviderMeshDuplicatedFaces::attach()](../../d1/d9b/classMeshGui_1_1ViewProviderMeshDuplicatedFaces.html#ab75835f606f943fe96ad4a8002d09cfa),
[MeshGui::ViewProviderMeshDegenerations::attach()](../../d2/da9/classMeshGui_1_1ViewProviderMeshDegenerations.html#a106d930fd275643d8122f5b8013032e2),
[MeshGui::ViewProviderMeshDuplicatedPoints::attach()](../../d5/d26/classMeshGui_1_1ViewProviderMeshDuplicatedPoints.html#aaf70aaac62a6aaea8f374c91a713a3ba),
[MeshGui::ViewProviderMeshIndices::attach()](../../dd/d71/classMeshGui_1_1ViewProviderMeshIndices.html#a79ed12e01de225656ea5769dee03f949),
[MeshGui::ViewProviderMeshSelfIntersections::attach()](../../d0/d67/classMeshGui_1_1ViewProviderMeshSelfIntersections.html#a8495baaa753c77467eb0c73eea448e69),
[MeshGui::ViewProviderMeshFolds::attach()](../../d8/d06/classMeshGui_1_1ViewProviderMeshFolds.html#a0789cee0d11be6e8413d1a8a6f44ee15),
[Gui::ViewProviderLink::attach()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab31e41e9a24ec097be019cdff4fb969b),
[Gui::ViewProviderInventorObject::attach()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#aff4e099b47f57184e70e695ea6345e4b),
[Gui::ViewProviderOrigin::attach()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a8cf194c6760588fde8cab14ded411398),
[Gui::ViewProviderVRMLObject::attach()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a6325dc25a3b586202db6edaf20319937),
[FemGui::ViewProviderFemMesh::attach()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a3a6ac9c1eebd29aa9c649e12b4987bc9),
[FemGui::ViewProviderFemPostFunction::attach()](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#a1cd9009bd8fb1f598b2d9ebf797f1aaf),
[FemGui::ViewProviderFemPostObject::attach()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a7dcf3dc1b7f85846e5b50cc08c7f1f46),
[ImageGui::ViewProviderImagePlane::attach()](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#a4b3ddff39036fec0bb1ed7d237c88046),
[PathGui::ViewProviderPath::attach()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a8bd5bb63583a3cb16b91696322881c5f),
[RobotGui::ViewProviderRobotObject::attach()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#abfd62beacd9f9981515c67a20b27e813),
[RobotGui::ViewProviderTrajectory::attach()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#ae0c77a17efe78de9f375f9382cc40da2),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionAttach()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#a1350dd14837e4ecb73f6d28191d3fb1f),
and
[Gui::ViewProviderExtern::setModeBySoInput()](../../dd/d9c/classGui_1_1ViewProviderExtern.html#acbf98598a34ab1f2ec5893c44851964c).

## ◆ beforeDelete()

| void ViewProvider::beforeDelete  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Called before deletion.

Unlike
[onDelete()](../../d3/db3/classGui_1_1ViewProvider.html#a2a15a8d5c80ecec42abe4f53dd8c46da
"Get called if the object is about to get deleted."), this function is
guaranteed to be called before deletion, either by Document::remObject(), or
on document deletion.

Reimplemented in
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a1de1e7f7c64eaad7bdba94ee03783e20).

Referenced by
[Gui::ViewProviderLink::onBeforeChange()](../../d6/d59/classGui_1_1ViewProviderLink.html#aefc3f174999bdd4648769e65cfbcf399),
and
[Gui::Document::slotDeletedObject()](../../de/d4e/classGui_1_1Document.html#a02acfc1218f2666ad7e6b80c804abc99).

## ◆ canAddToSceneGraph()

| virtual [bool](../../d9/db9/classbool.html) Gui::ViewProvider::canAddToSceneGraph  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Indicate whether to be added to scene graph or not.

Referenced by
[Gui::View3DInventorViewer::addViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a3a675a24c21e175605a6795b2b033ba5),
and
[Gui::Document::toggleInSceneGraph()](../../de/d4e/classGui_1_1Document.html#a97eb15cf990d9cd6a95fd6d28c1ad7ff).

## ◆ canDelete()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDelete  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Asks the view provider if the given object that is part of its outlist can be
removed from there without breaking it.

Parameters

     obj| is part of the outlist of the object associated to the view provider   
---|---  
  
Returns

    true if the removal is approved by the view provider. 

Reimplemented in
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#ad3e1a0f540e994cc6201d8ba9fa6c796),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a68994c89e15a064934005a4b2070f1b7),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#af20d0590d8a8e1685e53047da3860e97),
[FemGui::ViewProviderSolver](../../d9/d54/classFemGui_1_1ViewProviderSolver.html#a2104d4a0b43a2bedfb34041ef5ccc45e),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a05053e1a9eefc1cb745e1da0a6e50e3e),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a3241024f2ff866526ce385ad692d3ea5),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a5f146b8dddc16c278208f486266530bf),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#aa53d59ca09fff8bc70088a50b487c4b6),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a41e58da6f754152c89c63cb592e3fdf1),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#ac392f528d029b626cfd33690e0da8a4b),
[TechDrawGui::ViewProviderTile](../../d1/daa/classTechDrawGui_1_1ViewProviderTile.html#a3a7b268b8016bdcb9640964cc8544b9c),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#ab542321281a6e97f1d32c49344184137),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a5f20e5f01473c6c8232df5c74d9a3258),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a4945affe98ab80c97ec62230a452b093),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#ab47d017d461d1d4798575bedbc67a511),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af693d465f282457e260eed5092506cf1),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a4a057dcb46adbe540a8ef607d8d80d9f),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a3adb6e8979f16d47edccd820876daa9e),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#acb663d713a24f23097c9ac5d2dc4419c),
and
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ab5e884afd3aee58a88d0f194388a5241).

Referenced by
[StdCmdDelete::activated()](../../da/dc8/classStdCmdDelete.html#a120710ae4a8c0f26451596002a176ee7).

## ◆ canDragAndDropObject()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDragAndDropObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Return false to force drop only operation for a given object.

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a9efaffd7b4c0794b9a0ea98256d56852),
and
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#a0dfa5eb571c55987ae1ef48f102abedc).

Referenced by
[Gui::TreeWidget::dragMoveEvent()](../../de/de0/classGui_1_1TreeWidget.html#a955dd781ffd85d51f835ecae42d9ade8),
and
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f).

## ◆ canDragObject()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDragObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Check whether the object can be removed from the view provider by drag and
drop.

Reimplemented in
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a2d0a02dafcabd5a3d2217137fe2fe63c),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#abd0203ea97bb831d1cc3f2f305650a3c),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a95507a31453751ca0b65224cc520fe7e),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a8a192ed62ba8fbde86da9d6c95839e14),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a0f925ff7fc6d8a3fafaee7dc43b61222),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a5b23b48a685f856df048e89dfbb96595),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a7b07997b0a797986bdf725f3541027dd),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a4219b43bf6f1ab5eb62561faa97daa34),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a7fe65ef7ba5b511d83a0718f43dbd1fb).

## ◆ canDragObjects()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDragObjects  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Check whether children can be removed from the view provider by drag and drop.

Reimplemented in
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a048d562c33fa221857d89ec12ac3864d),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a1731d8da4c2eee22867f4a649570dc98),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a6ff9ec92ccf23986b195927ba5793dc0),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a5a520e7990a5781a19ceacda648acebb),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#ae97431d3f4bc86584e69109e5e25bfaa),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#ae01b3e15ed9d172eaaf1096b2a7c054b),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#ae248c51108c170b6152da1c4fa1d9dda),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a1c644b34413448851100319eb59c4662),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#a2bdd66efe24577676733150b822501f8),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ab16c13a6b2ba1ff7dbf894f95477f970),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a8e6fa789a4292d354072857361babeae).

## ◆ canDropObject()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDropObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Check whether the object can be dropped to the view provider by drag and drop
or drop only.

Reimplemented in
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#ab8ef954e9ad27dd8b1cac357ef90daf1),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#ae9d030adb1625a5cd8779127874158f5),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#ae6c9d4668b752005c3897320076568f4),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#aeed1231298a5c85b3bcde059a5c1e81e),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#ae0c0ee3fed339afed862aeff120c96e1),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a9d9961276926439991aa81f3dc0c2b82),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a725ea99f0402843f64f013fa979f2704),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a8c12d0d3c78a08d12eeda276cfb63b0a),
and
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#aecc79ac8b9648a6f38d03aa375d74989).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964).

Referenced by
[Gui::ViewProviderDocumentObject::canDropObjectEx()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a9338ac804f5e73cea734af9bb02524e0),
and
[canDropObjectEx()](../../d3/db3/classGui_1_1ViewProvider.html#a59a1163a60fc6339403df074b65f7858).

## ◆ canDropObjectEx()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDropObjectEx  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
|  | const char *  | _subname_ ,   
|  | const std::vector< std::string > & | _elements_  
| ) | |  const  
virtual  
  
Query object dropping with full qualified name.

Tree view now calls this function instead of
[canDropObject()](../../d3/db3/classGui_1_1ViewProvider.html#a4e729f5e7bcfadb98dcf324cf1f4e78f
"Check whether the object can be dropped to the view provider by drag and drop
or drop only."), and may query for objects from other document. The default
implementation (actually in
[ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html))
inhibites cross document dropping, and calls canDropObject(obj) for the rest.
Override this function to enable cross document linking.

Parameters

     obj| the object being dropped  
---|---  
owner| the (grand)parent object of the dropping object. Maybe null. This may
not be the top parent object, as tree view will try to find a parent of the
dropping object relative to this object to avoid cyclic dependency  
subname| subname reference to the dropping object  
elements| non-object sub-elements, e.g. Faces, Edges, selected when the object
is being dropped  
  
Returns

    Return whether the dropping action is allowed. 

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a9338ac804f5e73cea734af9bb02524e0),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#af425c71b0e1e09fa58cd5cb92911e35f),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a8b8b4ab90fa2b9b21b4335cacee28edd).

References
[canDropObject()](../../d3/db3/classGui_1_1ViewProvider.html#a4e729f5e7bcfadb98dcf324cf1f4e78f).

## ◆ canDropObjects()

| [bool](../../d9/db9/classbool.html) ViewProvider::canDropObjects  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Check whether objects can be added to the view provider by drag and drop or
drop only.

Reimplemented in
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a8930a33004bf8a5866be41e882c33b30),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a23173a2141eaa30eea996b75b35f6751),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#aec8b46b41eaface305b68c99deeb2d1b),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a299bb1b3edff0fffd08805b9bd37110f),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#aa7b15e052cf4f8825b3017514cb42a36),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#ae76ea97193d626edb27116d3016c3a97),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a91211ff5df76d825e4d23b25eeba1b86),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#a4a322108fa34b7c4ce9d43592b02bc17),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ab572932625bba4219c1fbceaa7de15ae),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a689a3bdf79972243615d49c08f62ecf3),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adcc9d80b22970ff32d5f7663363f6c63),
and
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#ae463715c1d61d41504431745e7d0c43e).

Referenced by
[Gui::TreeWidget::dragMoveEvent()](../../de/de0/classGui_1_1TreeWidget.html#a955dd781ffd85d51f835ecae42d9ade8),
and
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f).

## ◆ canRemoveChildrenFromRoot()

| virtual [bool](../../d9/db9/classbool.html) Gui::ViewProvider::canRemoveChildrenFromRoot  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Tell the tree view to remove children items from the tree root.

Referenced by
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18).

## ◆ checkRecursion()

| [bool](../../d9/db9/classbool.html) ViewProvider::checkRecursion  | ( | [SoNode](../../d0/d2d/classSoNode.html) *  | _node_| ) |   
---|---|---|---|---|---  
protected  
  
Helper method to check that the node is valid, i.e.

it must not cause and infinite recursion.

References
[Gui::addNodes()](../../d9/dad/namespaceGui.html#ab6a4fbdaae1dc8271efade6f5be8bf48).

Referenced by
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214).

## ◆ claimChildren()

| std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > ViewProvider::claimChildren  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
deliver the children belonging to this object this method is used to deliver
the objects to the tree framework which should be grouped under its label.

Obvious is the usage in the group but it can be used for any kind of grouping
needed for a special purpose.

Reimplemented in
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a8e5d16c05e27ff22d077c79d43520f2b),
[PartGui::ViewProviderMirror](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a2d89dd0a0fc37e95b48e979b8b81408a),
[PartGui::ViewProviderFillet](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a6d3129fc39ba787229812c61d8b751a9),
[PartGui::ViewProviderChamfer](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a7d796ef8d2a8cd022982342ce798ee98),
[PartGui::ViewProviderRuledSurface](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#a8f7d6bf9c5c95fc9c085581c4589b645),
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#afd2e9b23fb332226846d2b13edf9e6ba),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a37458e3a42b6d8e7a53bc0b07f720c02),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a45b2f43632cae53dfefcce10f30ae398),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a93fdb079614b29a6658a4596881405fb),
[FemGui::ViewProviderFemPostPipeline](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#ac5626a9e2850eeb26ecff5a70bf2d941),
[PartGui::ViewProviderBoolean](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a2ddf6a6611da27e24b5c177fa82179e9),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a0045707f443193b046cb01b7c139b652),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#ab7e6ca8e32fb15358223c7eb8dc97b49),
[PartGui::ViewProviderExtrusion](../../d7/dc8/classPartGui_1_1ViewProviderExtrusion.html#ae591beb9bf81e182debee47b7a0ca814),
[PartGui::ViewProviderRevolution](../../dc/d27/classPartGui_1_1ViewProviderRevolution.html#a6a7ba941a61a447fb9a6e4e5246c4cee),
[PartGui::ViewProviderLoft](../../d5/d42/classPartGui_1_1ViewProviderLoft.html#ac368f091664f727043f69262f84d3d3a),
[PartGui::ViewProviderSweep](../../d7/d5f/classPartGui_1_1ViewProviderSweep.html#a91b5fe397c600d5fe79e69c62c3ac22e),
[PartGui::ViewProviderOffset](../../df/ded/classPartGui_1_1ViewProviderOffset.html#a16ecb9054d6817296a620fdf43b90154),
[PartGui::ViewProviderThickness](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#a8de30390b0f529bf7aa199a226628bc7),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a2455deb85cf98bb710dd4322ad07854c),
[PartDesignGui::ViewProviderHelix](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a27d75e659da5ae824301907d1f95fe4d),
[PartDesignGui::ViewProviderHole](../../df/dda/classPartDesignGui_1_1ViewProviderHole.html#abee71c6672e4a1f8a5b6d6bfe1423371),
[PartDesignGui::ViewProviderLoft](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#ac368f091664f727043f69262f84d3d3a),
[PartDesignGui::ViewProviderMainPart](../../d4/d87/classPartDesignGui_1_1ViewProviderMainPart.html#ab287f6031d8457881ed450ff0028298e),
[PartDesignGui::ViewProviderMultiTransform](../../d6/d05/classPartDesignGui_1_1ViewProviderMultiTransform.html#af5e53bee082a9a57e0e69dd5e6070035),
[PartDesignGui::ViewProviderPipe](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a4c581523b2a518090737db2569d91dfa),
[PartDesignGui::ViewProviderSketchBased](../../d3/d7d/classPartDesignGui_1_1ViewProviderSketchBased.html#a4552ed8301193054b5f18e6d1b445b89),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a3ee6f619b68b35b3ec246a7873fa6653),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#af7f604bd9905d7b5488f874185e867d9),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#ad25e77d61c55b396d049d51301d0cfc7),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a07694ec29ec000ec830fc3988076fab1),
[RobotGui::ViewProviderTrajectoryCompound](../../d7/d47/classRobotGui_1_1ViewProviderTrajectoryCompound.html#ae747a93e2570dde9f2d60ba618be32d2),
[RobotGui::ViewProviderTrajectoryDressUp](../../da/dff/classRobotGui_1_1ViewProviderTrajectoryDressUp.html#a7bc4e3cb415db601995399924a6d5435),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#ab90cf47c766f83da23d7f960ded3ccdd),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a702e5f00c38dcb77490c48b4018d093e),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#ab19cf412f22ca45bce0de2d22f88b7bb),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aba1c9f4a2a6681b4ea6666ba487847c1),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a476e979878e83b84e952c2949d3d007a),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a4e8d25b0066202499ac3da63f664db36),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a3cba171d1aa19a5462fa22825dcc2047),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#ac4ec5b8a1cc9767dcf24f5b49a2d7522),
and
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abaf1943763d885917f20c4a78a8e2ef5).

References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Gui::Document::addRootObjectsToGroup()](../../de/d4e/classGui_1_1Document.html#a7e7018c0c6b8ee7bc2eb987dc60c2a6a),
[FemGui::ViewProviderFemAnalysis::claimChildren()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a37458e3a42b6d8e7a53bc0b07f720c02),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionClaimChildren()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#ad44762aa4bd4aa7ae5734d717c8925ed),
[FemGui::ViewProviderFemPostObject::onDelete()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a9a6f16c2754b100a96f37a11efac104d),
[FemGui::ViewProviderSolver::onDelete()](../../d9/d54/classFemGui_1_1ViewProviderSolver.html#a4cdfba50783d5bffd25927bc99ec0735),
[femviewprovider.view_mesh_gmsh.VPMeshGmsh::onDelete()](../../df/dbc/classfemviewprovider_1_1view__mesh__gmsh_1_1VPMeshGmsh.html#ae4c9ca343356d3acf252b0566b3ff01c),
[femviewprovider.view_result_mechanical.VPResultMechanical::onDelete()](../../d7/d8f/classfemviewprovider_1_1view__result__mechanical_1_1VPResultMechanical.html#a6bde7f2d215b4399295a2d2b426d6f4f),
[BOPTools.JoinFeatures.ViewProviderConnect::onDelete()](../../da/d91/classBOPTools_1_1JoinFeatures_1_1ViewProviderConnect.html#a7578eaa093ec056d3080b03f20244ca8),
[BOPTools.SplitFeatures.ViewProviderBooleanFragments::onDelete()](../../d0/d5a/classBOPTools_1_1SplitFeatures_1_1ViewProviderBooleanFragments.html#a1a561237cd3f10b60c442c5b6e63b794),
[BOPTools.SplitFeatures.ViewProviderSlice::onDelete()](../../d5/d19/classBOPTools_1_1SplitFeatures_1_1ViewProviderSlice.html#a20a3b8fa1e0921831683ebaae84baa98),
[BOPTools.SplitFeatures.ViewProviderXOR::onDelete()](../../d9/de4/classBOPTools_1_1SplitFeatures_1_1ViewProviderXOR.html#a199d8da22e104fa58c6b88685ffdfec1),
and
[Gui::DocumentObjectData::updateChildren()](../../d6/d82/classGui_1_1DocumentObjectData.html#a27646637e6cde16c2bd71f38917f5771).

## ◆ claimChildren3D()

| std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > ViewProvider::claimChildren3D  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
deliver the children belonging to this object this method is used to deliver
the objects to the 3DView which should be grouped under its scene graph.

This affects the visibility and the 3D position of the object.

Reimplemented in
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a0f74786c70082bf266cd8874766edb30),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a10ae5842f49a6b47f09fb3df513d1f14),
and
[FemGui::ViewProviderFemPostPipeline](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#aff6a71e3fe4e944c1ce1ac6cd793d7d1).

References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Gui::LinkInfo::updateChildren()](../../d4/da4/classGui_1_1LinkInfo.html#a2e43c0079db6d71372bd878d1bcaf68d).

## ◆ convert() [1/2]

| SbMatrix ViewProvider::convert  | ( | const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rcMatrix_| ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Matrix4D::getGLMatrix()](../../d5/db4/classBase_1_1Matrix4D.html#a8bb6545451679312a37458ea2760d18e).

Referenced by
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d),
and
[Gui::ViewProviderLink::updateDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a30d3a1d233bff54143b068d64af490eb).

## ◆ convert() [2/2]

| [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) ViewProvider::convert  | ( | const SbMatrix & | _sbMat_| ) |   
---|---|---|---|---|---  
static  
  
## ◆ doubleClicked()

| virtual [bool](../../d9/db9/classbool.html) Gui::ViewProvider::doubleClicked  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
is called by the tree if the user double clicks on the object

Reimplemented in
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a5e666f0a1cab99aba3ce00094a9cb351),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a6d8d84c4602b182b7f43c4e9f26ea17b),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#ad7348ef1984131dbf8b73e578898f395),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#ab30ddfc4f28d7e385b73610be8c01c49),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#aaa7b18c3324f7b0ad5e77c17eb1b3fac),
[Gui::ViewProviderMaterialObject](../../d3/d1a/classGui_1_1ViewProviderMaterialObject.html#a5f6b5794ac93c33c0f3d8b22c5f7b449),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a6e368b2cf1d5c715ed916e905c98f4a7),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#af8a693be07c1ddffdf657ee8439b9171),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#aa1b6c15194b4b7f5f74f58d4a944d729),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#abe833e8299e59bd079273f4c30af4067),
[FemGui::ViewProviderSetElements](../../dd/d62/classFemGui_1_1ViewProviderSetElements.html#aae84dbef4c6b2d1648dda09591b492f5),
[FemGui::ViewProviderSetFaces](../../d9/d46/classFemGui_1_1ViewProviderSetFaces.html#a4b30e4dc0fdd0521775b8a4715c8d189),
[FemGui::ViewProviderSetGeometry](../../dd/d48/classFemGui_1_1ViewProviderSetGeometry.html#a96fdd985d0e3e7ea1f86153a7b61b0a7),
[FemGui::ViewProviderSetNodes](../../d5/d44/classFemGui_1_1ViewProviderSetNodes.html#ae4d23b65acdbaa2d534da33c087b6047),
[PartGui::ViewProviderPart](../../d0/dd0/classPartGui_1_1ViewProviderPart.html#af84f7e3575cbacaf3750d005dce3b9e5),
[PartDesignGui::ViewProviderBase](../../d7/d54/classPartDesignGui_1_1ViewProviderBase.html#a7fffda76ce7fa0ec5358a08095625e86),
[RaytracingGui::ViewProviderLux](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a1998a73f0993fd6df972c5dbd0c63808),
[RaytracingGui::ViewProviderPovray](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a0dc312db3eae1afb75584cd3c221b7e3),
[RobotGui::ViewProviderEdge2TracObject](../../da/d5e/classRobotGui_1_1ViewProviderEdge2TracObject.html#ac3e7ed08ba43348469e01b193a0bfec6),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a2ed40a9987c09471ccf3086d92e3b50e),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a239a7beaa867f79a66a7776e44b40f66),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#abcc7ccb1e27d54ff86ad2e3f70eb44a2),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a6e2998a2690e2cb8fcd1480454065bf3),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a4fd358d2526c879db366a35f436a250e),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a3bb1124d5937e945558b555ab1544d61),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a42020a199ad55a96f41278896d896735),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a847568aa29ceeb447df124d1154c1476),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a4327a2958caa536983a1b11f5b86e350),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a44360fc918919048f24d0ef9e4eaa1e2),
[Gui::ViewProviderPart](../../d9/d6c/classGui_1_1ViewProviderPart.html#a0b5b05396bfb004b06bb38f41c9f3d23),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a28ca5432772a9ef33f88cced0c4994e3),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#af3c19e67cc2a25b4d54a723c15015251),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a588caea71c3f6afedfddf98adfb9f038),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7475f41cc0515bc4f46f906626715863),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#aad8a0cf972972419f70c1eb2bb2ee615),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#ae2d54ead9e9d604590ad03b2a55e6732),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a2f90ad8734a3a7d05d6d94885a05ab34),
and
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a97de84af6c453de32850b9790bb5041e).

Referenced by
[Gui::ViewProviderLink::doubleClicked()](../../d6/d59/classGui_1_1ViewProviderLink.html#ad7348ef1984131dbf8b73e578898f395),
and
[Gui::TreeWidget::mouseDoubleClickEvent()](../../de/de0/classGui_1_1TreeWidget.html#aa3c3121b950b3f9b0d134710879cf820).

## ◆ dragObject()

| void ViewProvider::dragObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Remove a child from the view provider by drag and drop.

Reimplemented in
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#aa329c77eb17a3b9f6acd5f03257c8a4f),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a32b33e83e13994afaf935e456e0b57f0),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a1e67ab8efea8e70aaba3b8c11520b457),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a8ac5bc65eca40dc6643130c34aba6204),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a8ee9184812e792b5581aece499e8383c),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a21aec54554c05f358ef3b348e5bbd7bf),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a3149f241f25662de8f6ff77377188f5e),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#ae97173b3cc07e61146054261de3f5381),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ad50efc30b828dbc7635de3f3fa82af31),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a82a0fefce2cf3183da16ab509943d073).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f).

## ◆ dropObject()

| void ViewProvider::dropObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
virtual  
  
Add an object to the view provider by drag and drop.

Reimplemented in
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#aa687ac2e34785ff95b5ca780dbf01e48),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a586957f2b53d8314a6b029c210db1b1f),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a7e7159c88b68bce0a30ef2b3b9112441),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#afa57525b6024724ed1a6de30e19c8439),
[PartGui::ViewProviderFace](../../d9/dba/classPartGui_1_1ViewProviderFace.html#a13281a3ef2aa0f0751e28766b637caf3),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#acaa0088c9df488727e02cd749f22f457),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a42e56c173ddcbe847f69e2765497244a),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#a9603231c83b56b26bcd9bdb9bba4a3ef),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a264c4c2055e7bb5a27daaad6d8466668),
and
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3e245daa7cd5dbb26f3603f2e93f68fe).

Referenced by
[dropObjectEx()](../../d3/db3/classGui_1_1ViewProvider.html#ae1b56e5b74e1015f5bc8021f033d9e74).

## ◆ dropObjectEx()

| std::string ViewProvider::dropObjectEx  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
|  | const char *  | _subname_ ,   
|  | const std::vector< std::string > & | _elements_  
| ) | |   
virtual  
  
Add an object with full qualified name to the view provider by drag and drop.

Parameters

     obj| the object being dropped  
---|---  
owner| the (grand)parent object of the dropping object. Maybe null. This may
not be the top parent object, as tree view will try to find a parent of the
dropping object relative to this object to avoid cyclic dependency  
subname| subname reference to the dropping object  
elements| non-object sub-elements, e.g. Faces, Edges, selected when the object
is being dropped  
  
Returns

    Optionally returns a subname reference locating the dropped object, which may or may not be the actual dropped object, e.g. it may be a link. 

Reimplemented in
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#abdd84ec90fe95fc762d7cc1d7331b5b1),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#abde14dc0c89fb6cd50089fda27e4d6c9).

References
[dropObject()](../../d3/db3/classGui_1_1ViewProvider.html#ab8848838fefc7bc36e30c25cb937528e).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f).

## ◆ eventCallback()

| void ViewProvider::eventCallback  | ( | void *  | _ud_ ,   
---|---|---|---  
|  | SoEventCallback *  | _node_  
| ) | |   
static  
  
References
[Gui::Application::activeDocument()](../../d9/da8/classGui_1_1Application.html#a2a8d3f8a833752db7b02014a4a921ab6),
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[Gui::Application::Instance](../../d9/da8/classGui_1_1Application.html#ac23ff9ca7b7bfc047f7a2c00e8119df3),
[keyPressed()](../../d3/db3/classGui_1_1ViewProvider.html#a491c4885615fa91504d1e06117a98898),
[mouseButtonPressed()](../../d3/db3/classGui_1_1ViewProvider.html#aef92094223e7104a02f8eab7aae50234),
[mouseMove()](../../d3/db3/classGui_1_1ViewProvider.html#ac97b2006300630c2fc546f6e76381684),
[mouseWheelEvent()](../../d3/db3/classGui_1_1ViewProvider.html#a0d8a5bfdd103ffb0baef0efedc2b865f),
[Gui::Document::resetEdit()](../../de/d4e/classGui_1_1Document.html#a778e60f55ce80a2d722d466eb21d0754),
and
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

Referenced by
[Gui::View3DInventorViewer::resetEditingViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a94d416fa9d5e705fdf6bb89cc467739a),
and
[Gui::View3DInventorViewer::setEditingViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a7067bcaa7dd4a8b2835582ce30c2c385).

## ◆ finishEditing()

void ViewProvider::finishEditing  | ( | | ) |   
---|---|---|---|---  
  
References
[unsetEdit()](../../d3/db3/classGui_1_1ViewProvider.html#ae74f9e97a6f5f027bb25fb93debc5fa9).

Referenced by
[MeshGui::ViewProviderMesh::clipMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2163df57149a01e40800e85a88d3ce20),
[PointsGui::ViewProviderPoints::clipPointsCallback()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a4245d12144abe01706409cd10565cd60),
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
[MeshGui::ViewProviderMesh::selectGLCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2b53e6d9eccae0cd2400b98862e20979),
and
[MeshGui::ViewProviderMesh::trimMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a99db0ab49ba22437ef202c633d752b52).

## ◆ getActiveDisplayMode()

std::string ViewProvider::getActiveDisplayMode  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[MeshGui::ViewProviderMeshCurvature::curvatureInfo()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#aa2902a6b29f9d107136899cdbf8eca28),
[PartDesignGui::ViewProviderAddSub::setPreviewDisplayMode()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#af83ba83cdbf7dad8bba49c1ef5db6963),
[PartGui::ViewProviderCustom::updateData()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
and
[SketcherGui::ViewProviderCustom::updateData()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e).

## ◆ getAnnotation()

[SoSeparator](../../de/d78/classSoSeparator.html) * ViewProvider::getAnnotation  | ( | void  | | ) |   
---|---|---|---|---|---  
  
References
[pcAnnotation](../../d3/db3/classGui_1_1ViewProvider.html#ab23920cdacf0330b04a7504f14e8f7e0),
and
[pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e).

## ◆ getBackRoot()

| [SoSeparator](../../de/d78/classSoSeparator.html) * ViewProvider::getBackRoot  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Referenced by
[Gui::View3DInventorViewer::addViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a3a675a24c21e175605a6795b2b033ba5),
and
[Gui::View3DInventorViewer::removeViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ada2a7eafd9bdc5f6b02a68e6f75eaaec).

## ◆ getBoundingBox()

[Base::BoundBox3d](../../db/d07/namespaceBase.html#a0e81c8419e84c4905e08106de65eff54) ViewProvider::getBoundingBox  | ( | const char *  | _subname_ = `nullptr`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _transform_ = `true`,   
|  | [MDIView](../../df/d23/classGui_1_1MDIView.html) *  | _view_ = `nullptr`  
| ) | |  const  
  
Return the bound box of this view object.

This method shall work regardless whether the current view object is visible
or not.

References
[Gui::Application::activeDocument()](../../d9/da8/classGui_1_1Application.html#a2a8d3f8a833752db7b02014a4a921ab6),
[Gui::Application::activeView()](../../d9/da8/classGui_1_1Application.html#afa61f95bbe6a05b037d3c368d01ff38a),
[Base::BaseClass::getClassTypeId()](../../df/d4d/classBase_1_1BaseClass.html#a1e2a449672f9d4f63dffde25182e39ca),
[getDefaultMode()](../../d3/db3/classGui_1_1ViewProvider.html#a6440355d2a65c3cb4d76c6ff95a05292),
[getDetailPath()](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd),
[Gui::Application::Instance](../../d9/da8/classGui_1_1Application.html#ac23ff9ca7b7bfc047f7a2c00e8119df3),
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54),
[pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e),
and
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

Referenced by
[Gui::ViewProviderLink::initDraggingPlacement()](../../d6/d59/classGui_1_1ViewProviderLink.html#a1386127ddc37cfa7078215b347149a71),
[Gui::ViewProviderGeometryObject::updateData()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a4818bdc22e4b19444d703d72bec9d7ca),
[PartGui::ViewProvider2DObjectGrid::updateData()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
and
[FemGui::ViewProviderFemPostPipeline::updateFunctionSize()](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#a015e75189dd7b4b8719fce0c264388f5).

## ◆ getChildRoot()

| [SoGroup](../../d1/d22/classSoGroup.html) * ViewProvider::getChildRoot  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a0fe0443c2cf8ffff1c06248f391cdce5).

Referenced by
[Gui::View3DInventorViewer::checkGroupOnTop()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a1d4b9b9b5d9604967758304ac274d931),
[Gui::LinkInfo::getDetail()](../../d4/da4/classGui_1_1LinkInfo.html#ae009d37fee490ae3bb8feedb22572f25),
[Gui::ViewProviderDocumentObject::getDetailPath()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a2b877c2c199d31afe6d958825da2c360),
[Gui::ViewProviderDocumentObject::getElementPicked()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a1aa14689a5cc02702f75e171cc19cfb8),
[Gui::LinkInfo::getSnapshot()](../../d4/da4/classGui_1_1LinkInfo.html#a5b9c21ced59932d504807f9db330bbe1),
and
[Gui::LinkInfo::updateChildren()](../../d4/da4/classGui_1_1LinkInfo.html#a2e43c0079db6d71372bd878d1bcaf68d).

## ◆ getDefaultDisplayMode()

| const char * ViewProvider::getDefaultDisplayMode  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
get the default display mode

Reimplemented in
[Gui::ViewProviderExtern](../../dd/d9c/classGui_1_1ViewProviderExtern.html#a71e55269dcc57578d170fe36314575f9),
[MeshGui::ViewProviderFace](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#a4811c333cca59838d2f8b7c110c8bf64),
[MeshGui::ViewProviderExport](../../da/dd4/classMeshGui_1_1ViewProviderExport.html#a874522fc8ffb6f3cad97e196748c6223),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad07e7d98d7e8e1846f5587796e4801af),
[MeshGui::ViewProviderMeshTransform](../../d2/d2b/classMeshGui_1_1ViewProviderMeshTransform.html#a11b808c3896f594746a6730cc5ff0e49),
[MeshGui::ViewProviderMeshTransformDemolding](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#a08557b7239fd2fb116e968859a251e85),
[MeshPartGui::ViewProviderCrossSections](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#ac9f524d0eca74302ac2a5ab45d7af244),
[PartGui::ViewProviderCrossSections](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#aa95338efe0b5e2e16e6dc8bb0734b92a),
and
[PartGui::ViewProvider2DObject](../../d3/d17/classPartGui_1_1ViewProvider2DObject.html#a848d81969e4339fa6a1c76e81553dfda).

Referenced by
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57).

## ◆ getDefaultMode()

[int](../../d1/da0/classint.html) ViewProvider::getDefaultMode  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[getBoundingBox()](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3),
[Gui::ViewProviderLink::getDetailPath()](../../d6/d59/classGui_1_1ViewProviderLink.html#a631a96d7ef6239aabe05c86cf3c20d31),
[PartDesignGui::ViewProviderAddSub::setPreviewDisplayMode()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#af83ba83cdbf7dad8bba49c1ef5db6963),
[Gui::LinkInfo::setVisible()](../../d4/da4/classGui_1_1LinkInfo.html#a7a0db4bbe9fe9f25e5a352c8bc92a6bf),
and
[Gui::LinkInfo::updateSwitch()](../../d4/da4/classGui_1_1LinkInfo.html#a634497ddae09590573c5d6a6c7a70af3).

## ◆ getDetail()

| virtual SoDetail * Gui::ViewProvider::getDetail  | ( | const char *  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
return the coin node detail of the subelement

Reimplemented in
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2dcccce8967e7d05a5ddaf9e769ea83f),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ab95cfd02cb3db5c746b6ddcce13c8129),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#af6f7f0b5652f6f5450285bb1bb9e68bb),
[PartDesignGui::ViewProviderDatumCoordinateSystem](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a4f824c0724ad157536f9c7abe3e6ae3f),
and
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#a8359d806b18ddb2711fbef0edf9093a2).

Referenced by
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[getDetailPath()](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd),
and
[MeshPartGui::CurveOnMeshHandler::Private::vertexCallback()](../../d2/d9f/classCurveOnMeshHandler_1_1Private.html#a373137b450a6003db4057cc546930264).

## ◆ getDetailPath()

| [bool](../../d9/db9/classbool.html) ViewProvider::getDetailPath  | ( | const char *  | _subname_ ,   
---|---|---|---  
|  | SoFullPath *  | _pPath_ ,   
|  | [bool](../../d9/db9/classbool.html) | _append_ ,   
|  | SoDetail *& | _det_  
| ) | |  const  
virtual  
  
return the coin node detail and path to the node of the subelement

Parameters

     subname| dot separated string reference to the sub element   
---|---  
pPath| output coin path leading to the returned element detail  
append| If true, pPath will be first appended with the root node and the mode
switch node of this view provider.  
  
Returns

    the coint detail of the subelement

If this view provider links to other view provider, then the implementation of
[getDetailPath()](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd
"return the coin node detail and path to the node of the subelement") shall
also append all intermediate nodes starting just after the mode switch node up
till the mode switch of the linked view provider.

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a631a96d7ef6239aabe05c86cf3c20d31),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a166b1adf706ec848ee1ea85ddb941d86),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a2b877c2c199d31afe6d958825da2c360).

References
[getDetail()](../../d3/db3/classGui_1_1ViewProvider.html#aeef7227fd0a9a5ff3a70515d0e20c2d0),
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54),
and
[pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e).

Referenced by
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[getBoundingBox()](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3),
[Gui::ViewProviderDocumentObject::getDetailPath()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a2b877c2c199d31afe6d958825da2c360),
and
[partialRender()](../../d3/db3/classGui_1_1ViewProvider.html#a1ad7f52f266a58575a0f8c67c3d7caf3).

## ◆ getDisplayMaskMode()

[SoNode](../../d0/d2d/classSoNode.html) * ViewProvider::getDisplayMaskMode  | ( | const char *  | _type_| ) |  const  
---|---|---|---|---|---  
  
Get the node to the display mask mode _type_.

References
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54).

Referenced by
[Gui::Dialog::DlgInspector::setNodeNames()](../../de/d72/classGui_1_1Dialog_1_1DlgInspector.html#a76de55354260496b98e1f50d29598a19).

## ◆ getDisplayMaskModes()

std::vector< std::string > ViewProvider::getDisplayMaskModes  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of added display mask modes.

Referenced by
[Gui::Dialog::DlgInspector::setNodeNames()](../../de/d72/classGui_1_1Dialog_1_1DlgInspector.html#a76de55354260496b98e1f50d29598a19).

## ◆ getDisplayModes()

| vector< std::string > ViewProvider::getDisplayModes  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
returns a list of all possible display modes

Reimplemented in
[Gui::ViewProviderInventorObject](../../de/ded/classGui_1_1ViewProviderInventorObject.html#a3f3b37aabbd2470d43fcd9ed2bad621f),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a3fc6820cd9ef01bb77c7df551c60c556),
[Gui::ViewProviderVRMLObject](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#aaf3e919fdba10a99cb86e0423b54c21b),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ad35345ff81ca175bd59760f47acbca23),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#a66103afe82f4b20c6160b9e04b241871),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#ac8181a110b804fb87e8cea9cb45b0edf),
[ImageGui::ViewProviderImagePlane](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#af03a6ef38b62d100f15c734659907725),
[MeshGui::ViewProviderFace](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#a83d236b858ba33c90121b8cd9ab86eb2),
[MeshGui::ViewProviderExport](../../da/dd4/classMeshGui_1_1ViewProviderExport.html#a9d866f1671edd6a9cec6dac7621590cd),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a28fa33508d58572f65b2c37151f2e2f4),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ab9f8f33f15bb315f186341eb17a22084),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a76a935c61474d3219784eb6c18821c72),
[MeshGui::ViewProviderMeshTransform](../../d2/d2b/classMeshGui_1_1ViewProviderMeshTransform.html#a1a42f721a17a9050de91d5c029bd022b),
[MeshGui::ViewProviderMeshTransformDemolding](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#af8412b295259ef5be7e7df31576dac32),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ad20940e6baf90b4261d3177f1ebb7946),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a2d67beeb09773e4dc1ee1d2d00a2772d),
[RobotGui::ViewProviderRobotObject](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a44d2e6d379e1912dea8be47ca13cb90b),
[RobotGui::ViewProviderTrajectory](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#aebcf68d825187c71a650de621dab26b6),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a2ecacfc0cece29631d78d8adee7079d7),
[Gui::ViewProviderAnnotation](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a750d176e978ebe11bf6371a75e342283),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a822d74b52d414c3d27e9e0794c24a989),
[Gui::ViewProviderExtern](../../dd/d9c/classGui_1_1ViewProviderExtern.html#a94750c2d0afd01c221f183d8467553d7),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a2fec17766dffe2f1c35602b77f24182d),
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#ae56b67ffcae6d5d5d96f44fbc666c5e8),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a4ed449ac5d9a00d5a0cfbed7f6af301a),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a801c626a05307a2d97c056b0d39d13b2),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#a001910ec134ecf16a1379179a4ef9ac7),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a7ec40da0d220d2e964e56b0c40427574),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a9e4f4aa16053b588ad93e2eea896bd7b),
[FemGui::ViewProviderSolver](../../d9/d54/classFemGui_1_1ViewProviderSolver.html#a6d6efe38e094ef21a9fff71e16a567c8),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a4359bccefa8b20a14ed7ce8bcf66b6e0),
[MeshPartGui::ViewProviderCrossSections](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#ad00b39b4066cd7235d41bcba108e4bba),
[PartGui::ViewProviderCrossSections](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#a967bedc44c44cf25131fd200d47068b4),
[PartGui::ViewProvider2DObject](../../d3/d17/classPartGui_1_1ViewProvider2DObject.html#a39aec2fd14457ca7d0927b4da1c7c912),
[PartGui::ViewProviderBox](../../d2/d51/classPartGui_1_1ViewProviderBox.html#ae324e88123143c2c50432fe463397234),
[PartGui::ViewProviderCircleParametric](../../df/df9/classPartGui_1_1ViewProviderCircleParametric.html#ac664fa78ecbd52ef825bb5fa9435cbeb),
[PartGui::ViewProviderConeParametric](../../d0/d1b/classPartGui_1_1ViewProviderConeParametric.html#ab0efee800232cdb00dc5caeb8d31290b),
[PartGui::ViewProviderCurveNet](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#ac83dc3a0696ed30f294e0bf5a4456c70),
[PartGui::ViewProviderCylinderParametric](../../db/d25/classPartGui_1_1ViewProviderCylinderParametric.html#a88f2ee6788c134cb2b4ac7ddab6c0d19),
[PartGui::ViewProviderEllipseParametric](../../db/d7d/classPartGui_1_1ViewProviderEllipseParametric.html#adc28d1ed448294e8c25a7fc83b7121df),
[PartGui::ViewProviderHelixParametric](../../d2/db8/classPartGui_1_1ViewProviderHelixParametric.html#ae16a34ff6094189facef1396d58aacc1),
[PartGui::ViewProviderSpiralParametric](../../d6/dc3/classPartGui_1_1ViewProviderSpiralParametric.html#aeb1bd2b59f4ebae0e7690e8754a694ab),
[PartGui::ViewProviderLineParametric](../../d6/def/classPartGui_1_1ViewProviderLineParametric.html#afc6c6fbeb09e3219ec6ac29a1fbeadf2),
[PartGui::ViewProviderPlaneParametric](../../db/d0e/classPartGui_1_1ViewProviderPlaneParametric.html#a2018ee708249ba2e6b954ba0b258beff),
[PartGui::ViewProviderPointParametric](../../d8/d75/classPartGui_1_1ViewProviderPointParametric.html#a76d0adfa1c401512484b6a4073c94759),
[PartGui::ViewProviderPrism](../../d3/d87/classPartGui_1_1ViewProviderPrism.html#a7fdafcd6b45c4b5dfe6f03e82f49fd69),
[PartGui::ViewProviderWedge](../../d5/da4/classPartGui_1_1ViewProviderWedge.html#a5d73c018eaa5f58aa8d113e04097ab3e),
[PartGui::ViewProviderPartReference](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a5dd79875d25011e2ec5adade8b10730c),
[PartGui::ViewProviderRegularPolygon](../../de/d15/classPartGui_1_1ViewProviderRegularPolygon.html#a6014749d8bac787640364a4d85853a3c),
[PartGui::ViewProviderRuledSurface](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#ae05ebcd7a097355c442736f45de43002),
[PartGui::ViewProviderSphereParametric](../../d1/d19/classPartGui_1_1ViewProviderSphereParametric.html#af7dae7b51e6a0ef6e18b9d93464222f1),
[PartGui::ViewProviderEllipsoid](../../dd/d2a/classPartGui_1_1ViewProviderEllipsoid.html#a497894a7ab50f45b0e58e09373651ec1),
[PartGui::ViewProviderTorusParametric](../../dd/de7/classPartGui_1_1ViewProviderTorusParametric.html#a55a0965722ee66bb2209beb493a5f06c),
[TechDrawGui::ViewProviderAnnotation](../../d8/dd5/classTechDrawGui_1_1ViewProviderAnnotation.html#a750d176e978ebe11bf6371a75e342283),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a28c3eccb6753a9cf0c67b2949238c2e1),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a97a60fb0b8b759a851135ed1a011c909),
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#a8ccd53a43937ba4dcc76ae11d91bac32),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#abec72fb4e5f260f4ccbdc0b129e40ae6),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a8925d648d70ee8907c5b60923e1c47db),
[TechDrawGui::ViewProviderSpreadsheet](../../d1/d67/classTechDrawGui_1_1ViewProviderSpreadsheet.html#abae36c3ea277a14d12c3442e950281c6),
[TechDrawGui::ViewProviderSymbol](../../da/de5/classTechDrawGui_1_1ViewProviderSymbol.html#a039a72e2b658445dfa483c9ebb9b26c9),
[TechDrawGui::ViewProviderTile](../../d1/daa/classTechDrawGui_1_1ViewProviderTile.html#a0ed39b4ce5e6861ff2feee08e17f9fdc),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a99cc0087cf044c1f38850f3dc1c9f529),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a0e23d071280e04d7ab452994db4dccfe),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#aaf85617fb5816b9ec4ec35abd56aebf9),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a92f1b4fc9aacd6234d4bb1855aaa0234),
[Gui::ViewProviderDocumentObjectGroup](../../df/d84/classGui_1_1ViewProviderDocumentObjectGroup.html#a4f19aa10c9bcbb8081c072f4301fb916),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a8ea8db538b85465870b4e23df96b2b43),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a3a31eebcc39273c8fc5ca3a15df4afd7),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#af54f570cbb74deacf57113c13ce9b795),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a8332d1c9f0acdcc3284ac2629c78c1b1),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#aab11d4f514b6e4ddb9faeca2d6c0e7c3),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#abcbf0a19619f819a2c3e6d52d39a627f),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#ac3ec0e54295b0cb93fd56f1bc9c20ff7),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a0adf9f4b7f14323e8d24d4c7888d2173),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#abab4f7a96110a80e85f6b31001f9fb5d),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#aabdfa86e153c6236977f78725471fccb).

Referenced by
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[MeshGui::ViewProviderMeshCurvature::getDisplayModes()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ab9f8f33f15bb315f186341eb17a22084),
and
[Gui::ViewProviderLink::getDisplayModes()](../../d6/d59/classGui_1_1ViewProviderLink.html#a8ea8db538b85465870b4e23df96b2b43).

## ◆ getDropPrefix()

| virtual std::string Gui::ViewProvider::getDropPrefix  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
return a subname referencing the sub-object holding the dropped objects

## ◆ getEditingMode()

| [int](../../d1/da0/classint.html) ViewProvider::getEditingMode  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
return the edit mode or -1 if nothing is being edited

Referenced by
[MeshGui::ViewProviderMesh::clipMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2163df57149a01e40800e85a88d3ce20),
[PointsGui::ViewProviderPoints::clipPointsCallback()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a4245d12144abe01706409cd10565cd60),
[isEditing()](../../d3/db3/classGui_1_1ViewProvider.html#a710882933315d6c4f596afe07ebc96f1),
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4),
[MeshGui::ViewProviderMesh::selectGLCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a2b53e6d9eccae0cd2400b98862e20979),
and
[MeshGui::ViewProviderMesh::trimMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a99db0ab49ba22437ef202c633d752b52).

## ◆ getElement()

| virtual std::string Gui::ViewProvider::getElement  | ( | const SoDetail *  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
return a hit element to the selection path or 0

Reimplemented in
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a7e818da861887976069d0233a395805f),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ab3cfe9f795700f105abdf7e25fbd2290),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#aa337969c6af75c8dc24bf671ea8cd1ce),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a9ecc579f953603ef52dd4cdb345f0089),
and
[PartDesignGui::ViewProviderDatumCoordinateSystem](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#abab01394b255ae6afc9cca910eff01ae).

Referenced by
[getElementPicked()](../../d3/db3/classGui_1_1ViewProvider.html#a0532bd84b0b7f7d57da7a868f3bf90f5).

## ◆ getElementColors()

| virtual std::map< std::string, [App::Color](../../d3/d3a/classApp_1_1Color.html) > Gui::ViewProvider::getElementColors  | ( | const char *  | _element_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a15bdce85211acfec231620d1fea14805),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102).

Referenced by
[Gui::ElementColors::Private::addItem()](../../d8/dc9/classElementColors_1_1Private.html#a5344ba7cfcaf3a900e6b0c78535fbab6),
and
[Gui::ElementColors::Private::populate()](../../d8/dc9/classElementColors_1_1Private.html#abddd713e9556ea17b5ddb09fb3eb184b).

## ◆ getElementPicked()

| [bool](../../d9/db9/classbool.html) ViewProvider::getElementPicked  | ( | const SoPickedPoint *  | _pp_ ,   
---|---|---|---  
|  | std::string & | _subname_  
| ) | |  const  
virtual  
  
return a hit element given the picked point which contains the full node path

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#aa91a21df3ac8db004ca030c1bf57620b),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a1aa14689a5cc02702f75e171cc19cfb8),
and
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a43546cfaab3e2959f94362ccf9a8a720).

References
[getElement()](../../d3/db3/classGui_1_1ViewProvider.html#ac16e04f53374801a23bf5643d30e0ecf),
and
[isSelectable()](../../d3/db3/classGui_1_1ViewProvider.html#af1f5bb44d21931a4bbc9dc87c5ad900c).

Referenced by
[Gui::ViewProviderDocumentObject::getElementPicked()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a1aa14689a5cc02702f75e171cc19cfb8),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
and
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1).

## ◆ getFrontRoot()

| [SoSeparator](../../de/d78/classSoSeparator.html) * ViewProvider::getFrontRoot  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a1e128a68813613ee7ce06566b298037c),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#accb29ea740ec6d7d066b2c14783fc022),
and
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a2041ba4141df10b451de99e9706102e9).

Referenced by
[Gui::View3DInventorViewer::addViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a3a675a24c21e175605a6795b2b033ba5),
[Gui::ViewProviderDocumentObject::findFrontRootOfType()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a078851e515af6065c4daeaa5f2fc654f),
and
[Gui::View3DInventorViewer::removeViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ada2a7eafd9bdc5f6b02a68e6f75eaaec).

## ◆ getIcon()

| QIcon ViewProvider::getIcon  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
deliver the icon shown in the tree view

Reimplemented in
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a76d57438c1350bd9a432557f0c23dc5e),
[InspectionGui::ViewProviderInspectionGroup](../../d0/d31/classInspectionGui_1_1ViewProviderInspectionGroup.html#a5762c48b10f2b7d3f9ef111097445d86),
[MeshGui::ViewProviderExport](../../da/dd4/classMeshGui_1_1ViewProviderExport.html#a4a3a3a13e4ad1ae98d13605a234ecfe2),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a35929524168605f2222076a461a39745),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#abd164322320925399c1f71e15eb8cdd3),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a2cb6545fdca51454ef62e9bfafdb5870),
[PartGui::ViewProviderSpline](../../d6/d09/classPartGui_1_1ViewProviderSpline.html#aba3eb8121c249090ecb9d0491da81f0c),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ad6447703b334aa5fe610f2172a1c5b80),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ab7efb064884ad8646543e29a67425636),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a66f54ecbc61ecc56ddb807efc4f69b83),
[Gui::ViewProviderMaterialObject](../../d3/d1a/classGui_1_1ViewProviderMaterialObject.html#a4540a53ea393358e997546da35619fd4),
[PartGui::ViewProviderBoolean](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a61052fd656138212b0088e7a8d081599),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a6fbc123845a2eb1bc336e464164decac),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a8dcdf5e72e37898498854f17c75f33c8),
[PartDesignGui::ViewProviderHelix](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#aaf4fc8a40461a239f0e795227ea3bbae),
[PartDesignGui::ViewProviderLoft](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a79b678e71232046c0c9cc4c9fe7ad6ee),
[PartDesignGui::ViewProviderPipe](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a1fd80b0c0d51dbda347721c5c07e43ba),
[PartDesignGui::ViewProviderPrimitive](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a96f5121e8ac1cdfe2619b5aff372b1dd),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#ac73cc1ff448094669532b8f953e7d251),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#a4b6009ee924792b3c20da45fa354137e),
[SurfaceGui::ViewProviderFilling](../../d0/dac/classSurfaceGui_1_1ViewProviderFilling.html#a39143f23e829304234e148be2e57b4f6),
[SurfaceGui::ViewProviderGeomFillSurface](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#ab666a3ca1e414f265e3d0fb392686728),
[SurfaceGui::ViewProviderSections](../../da/dd0/classSurfaceGui_1_1ViewProviderSections.html#a342255bd0a0388266ae2aefdb7d65870),
[SurfaceGui::ViewProviderExtend](../../d1/d3c/classSurfaceGui_1_1ViewProviderExtend.html#a469543e731447ebade86e911f6ba8761),
[Gui::ViewProviderDocumentObjectGroup](../../df/d84/classGui_1_1ViewProviderDocumentObjectGroup.html#ad62b53c0a798c9a13f3882a3a7641958),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a9fae57bc9689e1d1c9b5377f340da728),
and
[Gui::ViewProviderPart](../../d9/d6c/classGui_1_1ViewProviderPart.html#afba5f47c9f0f811fe7983cac5c6f5fa3).

References
[Gui::BitmapFactory()](../../d9/dad/namespaceGui.html#ade78142fe51fcec686a304280cc472c2),
[mergeGreyableOverlayIcons()](../../d3/db3/classGui_1_1ViewProvider.html#aec47e82b8933db21dde528746150e3d2),
and
[sPixmap](../../d3/db3/classGui_1_1ViewProvider.html#a8ecdd67f362fd1a409053e3562ba5ba1).

Referenced by
[PartGui::DlgExtrusion::findShapes()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8976c72de1970766d8d2dc5391e34903),
[Gui::LinkInfo::getIcon()](../../d4/da4/classGui_1_1LinkInfo.html#a412d0473bff864ccdf631779afef32b9),
[PartGui::ViewProviderBoolean::getIcon()](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a61052fd656138212b0088e7a8d081599),
[TechDrawGui::TaskLinkDim::loadToTree()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#a78901c66da67bb8e9a3a97469e4f61d4),
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465),
[ArchAxisSystem.AxisSystemTaskPanel::update()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a376cbba2ccee6efd86c46d0f0a8e99e3),
[ArchComponent.ComponentTaskPanel::update()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#af95b36032a3837b4bf1b92fe7c6a47e0),
and
[ArchSectionPlane.SectionPlaneTaskPanel::update()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#aab4bcd7b08950b8e3b37d801381c5162).

## ◆ getMDIView()

| virtual [MDIView](../../df/d23/classGui_1_1MDIView.html) * Gui::ViewProvider::getMDIView  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a53a587aed195ed229d4e3bd990c6f019),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a4f9d80cf13870a0dc1ff07cd4a7c6424),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a30697eb4b828a075973c593c5610d554),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#afd2800fc162a36262dfdd73f6ab03000),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a4251ca74254acceef6b9ab6b0db5a000),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a68705030d80d2ae13a29e04203630f2c),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a27ee3ccdf43393bc2859bb6577992918).

Referenced by
[TechDrawGui::ViewProviderGeomHatch::getMDIView()](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#afd2800fc162a36262dfdd73f6ab03000),
[TechDrawGui::ViewProviderHatch::getMDIView()](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a4251ca74254acceef6b9ab6b0db5a000),
and
[Gui::Document::setActiveView()](../../de/d4e/classGui_1_1Document.html#a1933003b2ee08a001a5858c0e8d71e93).

## ◆ getModelPoints()

| std::vector< [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) > ViewProvider::getModelPoints  | ( | const SoPickedPoint *  | _pp_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a2221b4ae746e7a1ec366403ad725a102).

References
[draftgeoutils.general::vec()](../../d9/dfd/group__draftgeoutils.html#gad8ccb48490b88fe43f234c673531265c).

Referenced by
[Gui::ManualAlignment::applyPickedProbe()](../../d7/d97/classGui_1_1ManualAlignment.html#ab534e0e7e979975c445625aeb9fef797).

## ◆ getModeSwitch()

SoSwitch * Gui::ViewProvider::getModeSwitch  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Gui::LinkInfo::getSnapshot()](../../d4/da4/classGui_1_1LinkInfo.html#a5b9c21ced59932d504807f9db330bbe1),
and
[Gui::ViewProviderDocumentObject::setShowable()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a54ababa45b83ed9af26076c3a1c26ad7).

## ◆ getOverrideMode()

const string ViewProvider::getOverrideMode  | ( | | ) |   
---|---|---|---|---  
  
References
[overrideMode](../../d3/db3/classGui_1_1ViewProvider.html#a30d0a73702d5fe359395cad8e978941a).

Referenced by
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922).

## ◆ getPointOnRay() [1/2]

| SoPickedPoint * ViewProvider::getPointOnRay  | ( | const SbVec2s & | _pos_ ,   
---|---|---|---  
|  | const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | _viewer_  
| ) | |  const  
protected  
  
Helper method to get picked entities while editing.

It's in the responsibility of the caller to delete the returned instance.

References
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

Referenced by
[SketcherGui::ViewProviderSketch::mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
and
[SketcherGui::ViewProviderSketch::mouseMove()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa).

## ◆ getPointOnRay() [2/2]

| SoPickedPoint * ViewProvider::getPointOnRay  | ( | const SbVec3f & | _pos_ ,   
---|---|---|---  
|  | const SbVec3f & | _dir_ ,   
|  | const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | _viewer_  
| ) | |  const  
protected  
  
Helper method to get picked entities while editing.

It's in the responsibility of the caller to delete the returned instance.

References
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * ViewProvider::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
This method returns the Python wrapper for a C++ object.

It's in the responsibility of the programmer to do the correct reference
counting. Basically there are two ways how to implement that: Either always
return a new Python object then reference counting is not a matter or return
always the same Python object then the reference counter must be incremented
by one. However, it's absolutely forbidden to return always the same Python
object without incrementing the reference counter.

The default implementation returns 'None'.

Reimplemented from
[Base::BaseClass](../../df/d4d/classBase_1_1BaseClass.html#a5abe791f44a7691c96c166820f823514).

Reimplemented in
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a8717b8a5a6c79e899c780233348941de),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a491c9250dd9372b18d0296cedfb01701),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a256b755ac0eba62bb50670e75874bed9),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#ae9a76a67e95cadc3bbf289d9e5a3ad84),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a31c2af0bf22d66f737d3ed06bf7a5a1c),
and
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ac03971ba790eda722f46e82c1126300f).

References
[pyViewObject](../../d3/db3/classGui_1_1ViewProvider.html#a943e4042fb9fef225bcc04083fa904df).

## ◆ getRoot()

| virtual [SoSeparator](../../de/d78/classSoSeparator.html) * Gui::ViewProvider::getRoot  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[MeshGui::ViewProviderExport](../../da/dd4/classMeshGui_1_1ViewProviderExport.html#acb710add32a3e1bdc20af5e8dc331d5e).

Referenced by
[Gui::Document::addViewProvider()](../../de/d4e/classGui_1_1Document.html#aa66c8ca1ccffd5f1acca25e54cae5772),
[Gui::View3DInventorViewer::addViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a3a675a24c21e175605a6795b2b033ba5),
[Gui::View3DInventorViewer::containsViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a59831025e250f9a25e2c80e9d45ae0e5),
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[Gui::ViewProviderGeometryObject::getPickedPoint()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#af08d52d891424d3757b77f743ee682bd),
[Gui::ViewProviderGeometryObject::getPickedPoints()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a4d01c35343e7b21ba2f8f1e4d82bb119),
[Gui::View3DInventorViewer::getPointOnRay()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a60b1413306ff09c6db249439a3a097e4),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a8437c5be88154b9cb0bd2bae5ef94db3),
[Gui::LinkInfo::getSnapshot()](../../d4/da4/classGui_1_1LinkInfo.html#a5b9c21ced59932d504807f9db330bbe1),
[Gui::Document::getViewOfViewProvider()](../../de/d4e/classGui_1_1Document.html#ae28e7e3595864209f4df9fb68914e94b),
[PartGui::TaskCheckGeometryResults::goCheck()](../../d6/de5/classPartGui_1_1TaskCheckGeometryResults.html#aa4a2798e3f0d1217a8469bfd11093ac2),
[PartGui::FaceColors::Private::isVisibleFace()](../../d4/d4b/classFaceColors_1_1Private.html#a45f00bc1caa544bac5d4e891763aa779),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::View3DInventorViewer::removeViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ada2a7eafd9bdc5f6b02a68e6f75eaaec),
[Gui::View3DInventorViewer::resetEditingRoot()](../../d5/d29/classGui_1_1View3DInventorViewer.html#aab89c5619d8a9f8f32b5610f6f48662a),
[Gui::Dialog::DlgInspector::setNodeNames()](../../de/d72/classGui_1_1Dialog_1_1DlgInspector.html#a76de55354260496b98e1f50d29598a19),
[Gui::View3DInventorViewer::setupEditingRoot()](../../d5/d29/classGui_1_1View3DInventorViewer.html#aaaef315b458c0c4d619771353f99888a),
[Gui::Application::sExport()](../../d9/da8/classGui_1_1Application.html#ade16ea2f01b001288ff3cd962a85b8b5),
[PartGui::ViewProviderSplineExtension::showControlPoints()](../../db/ddd/classPartGui_1_1ViewProviderSplineExtension.html#a47ebeaa5788d9341eaa389b79acdf55d),
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb),
[Gui::Document::slotTransactionRemove()](../../de/d4e/classGui_1_1Document.html#acf76be063eb0e3252ed3c37782417e29),
[Gui::Document::toggleInSceneGraph()](../../de/d4e/classGui_1_1Document.html#a97eb15cf990d9cd6a95fd6d28c1ad7ff),
[PartGui::ViewProviderCustom::updateData()](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[SketcherGui::ViewProviderCustom::updateData()](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
and
[Gui::ViewProviderOriginGroupExtension::updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e).

## ◆ getSelectionShape()

| virtual std::vector< [Base::Vector3d](../../db/d07/namespaceBase.html#a5efb391dcd31b7783e4987cc87728f3e) > Gui::ViewProvider::getSelectionShape  | ( | const char *  | _Element_| ) |  const  
---|---|---|---|---|---  
virtual  
  
return the highlight lines for a given element or the whole shape

Reimplemented in
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#aa88ea470502cb9d4b79958f1f09a240a),
and
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ab6ac183c0ba4b2aaeecc1ccb392da683).

## ◆ getStatus()

unsigned long Gui::ViewProvider::getStatus  | ( | | ) |  const  
---|---|---|---|---  
  
return the status bits

## ◆ getTaskViewContent()

| virtual void Gui::ViewProvider::getTaskViewContent  | ( | std::vector< [Gui::TaskView::TaskContent](../../d0/d97/classGui_1_1TaskView_1_1TaskContent.html) * > & | | ) |  const  
---|---|---|---|---|---  
virtual  
  
get a list of TaskBoxes associated with this object

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a205ef5356cc48a8f8252c2109275cd2e).

## ◆ getTransactionText()

| virtual const char * Gui::ViewProvider::getTransactionText  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Is called by the tree if the user double clicks on the object.

It returns the string for the transaction that will be shown in the undo/redo
dialog. If null is returned then no transaction will be opened.

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a6622915272f0a21c7d7dacda5f93df65),
and
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aa79e07be3f353a90e0f67d0b4f854e51).

## ◆ getTransformNode()

SoTransform * Gui::ViewProvider::getTransformNode  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Gui::LinkInfo::getSnapshot()](../../d4/da4/classGui_1_1LinkInfo.html#a5b9c21ced59932d504807f9db330bbe1),
[Gui::View3DInventorViewer::resetEditingRoot()](../../d5/d29/classGui_1_1View3DInventorViewer.html#aab89c5619d8a9f8f32b5610f6f48662a),
and
[Gui::View3DInventorViewer::setupEditingRoot()](../../d5/d29/classGui_1_1View3DInventorViewer.html#aaaef315b458c0c4d619771353f99888a).

## ◆ hasHiddenMarker()

| const char * ViewProvider::hasHiddenMarker  | ( | const char *  | _subname_| ) |   
---|---|---|---|---|---  
static  
  
References
[App::DocumentObject::hasHiddenMarker()](../../d2/de4/classApp_1_1DocumentObject.html#a613d0852b3963076e958e19a7c657c06).

Referenced by
[partialRender()](../../d3/db3/classGui_1_1ViewProvider.html#a1ad7f52f266a58575a0f8c67c3d7caf3).

## ◆ hiddenMarker()

| const std::string & ViewProvider::hiddenMarker  | ( | | ) |   
---|---|---|---|---  
static  
  
References
[App::DocumentObject::hiddenMarker()](../../d2/de4/classApp_1_1DocumentObject.html#ad48238ffb00b5919695aeed71f5c1e37).

Referenced by
[Gui::ViewProviderLink::applyColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a870666ac3bc9da51dc3b8cab2a0874cb),
[Gui::ViewProviderLink::getElementColors()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2b9c2eef2778031596f93f33b2980102),
and
[partialRender()](../../d3/db3/classGui_1_1ViewProvider.html#a1ad7f52f266a58575a0f8c67c3d7caf3).

## ◆ hide()

| void ViewProvider::hide  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Hides the view provider.

Reimplemented in
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#ad83ab0bef7709bfdb7bd2ff4471d8ada),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a1a835fe20339fa1ff3a825c6481296e9),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#af1f9e27cb4717b1eab17df64def3a5a3),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#ae328b7a7c463a0cfe21fb19adb6a8cab),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a4850a42a90d0220afedd7226c2cb95d5),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#ad194bdde945ec44c617d1974ec5351f9),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a2c2b1c3a15d359f94134528eea3c370a),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a0dad53d8ccb241aa1ffaa1ca6cd0e85b),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af961215142d52e0e355a89df19610333),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a76b2851b249a59575433a30cc5776432),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#afd1cfb51b69db6ac5816cf42df10eb2d),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#add04ca12b8bd9d195f0d691688ae3e7a).

References
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54).

Referenced by
[ArchComponent.ArchSelectionObserver::addSelection()](../../df/d0d/classArchComponent_1_1ArchSelectionObserver.html#abd6b916e9a66ac26700ad6f4d0c2d30c),
[DrawingGui::DrawingView::closeEvent()](../../da/d65/classDrawingGui_1_1DrawingView.html#a561c4a02c6108e3e1e99dedbd858d616),
[TechDrawGui::MDIViewPage::closeEvent()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a1b06900ff8d084242b445d3abc85b21c),
[Gui::ViewProviderDocumentObject::hide()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#af961215142d52e0e355a89df19610333),
[Mod.Show.mTempoVis.TempoVis::hide_all_dependencies()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a3e3225ff34a80f32b99dd564b4eb3657),
[Mod.Show.mTempoVis.TempoVis::hide_all_dependent()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a5092d1f6ba718c2056c4de9d0df34f61),
[Gui::Application::hideViewProvider()](../../d9/da8/classGui_1_1Application.html#a69a9a3a7108ec785583cbfb3770f1757),
[Gui::MergeDocuments::importObject()](../../d5/d20/classGui_1_1MergeDocuments.html#aabdb85b2cd55e6354b1a706a8bf912b4),
[PartDesignGui::ViewProvider::makeTemporaryVisible()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a91ffb650f8e0b3a88c37ab3018aa6299),
[Gui::ViewProviderDocumentObject::setActiveMode()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a680b6d8d00fa1135eee59edbda9f3bd0),
[Gui::ViewProviderDocumentObject::setShowable()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a54ababa45b83ed9af26076c3a1c26ad7),
[PartGui::DlgFilletEdges::setupFillet()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a1276cdf00c4f3436317932a8da913a5e),
[PathScripts.PathToolEdit.ToolEditorImage::setupUI()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#a084ad5441e84f4bab1e2ab96bb45e09f),
[setVisible()](../../d3/db3/classGui_1_1ViewProvider.html#a839be69bcafa02679cfa0881b09cc5ed),
[update()](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8),
[PathScripts.PathToolEdit.ToolEditorImage::updateTool()](../../dd/df1/classPathScripts_1_1PathToolEdit_1_1ToolEditorImage.html#acc3d4c7e3670300bb09c552d68664e00),
and
[Gui::ViewProviderDocumentObject::updateView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae31dde44f114d3e90bb2e1d544f3e442).

## ◆ isEditing()

[bool](../../d9/db9/classbool.html) ViewProvider::isEditing  | ( | | ) |  const  
---|---|---|---|---  
  
References
[getEditingMode()](../../d3/db3/classGui_1_1ViewProvider.html#a6b5e1f18cdd2fcc2f27c80610a5d632b).

Referenced by
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
and
[SketcherGui::ViewProviderSketch::isSelectable()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a16cad05d391f2022c154270ffe42759b).

## ◆ isLinkVisible()

[bool](../../d9/db9/classbool.html) ViewProvider::isLinkVisible  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ isRestoring()

[bool](../../d9/db9/classbool.html) Gui::ViewProvider::isRestoring  | ( | void  | | ) |   
---|---|---|---|---|---  
  
References
[Gui::isRestoring](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ffac69bf9ed9698059aeca3a94d3cb46169).

Referenced by
[Gui::ViewProviderDocumentObject::attach()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a915f1f11451e769f91b1137d1527fc57),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[PartDesignGui::ViewProviderBody::slotChangedObjectApp()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac2b54ba3e85e13c4e5a63fe12dcc17bf),
[PartDesignGui::ViewProviderBody::unifyVisualProperty()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a9622d1e6a23c6497bea610755aea5713),
[Gui::LinkInfo::update()](../../d4/da4/classGui_1_1LinkInfo.html#a7dd19269fe6dd6676db6bfea88888bd2),
[Gui::ViewProviderDocumentObject::update()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a6e0dd163d7555c35d78c29a504c0b2ce),
[TechDrawGui::ViewProviderLeader::updateData()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9885aee56382e6ad1e6e69b583197aa1),
and
[Gui::ViewProviderLink::updateData()](../../d6/d59/classGui_1_1ViewProviderLink.html#a73f73f368cb176bf9a7f2371e4e9ec93).

## ◆ isSelectable()

| virtual [bool](../../d9/db9/classbool.html) Gui::ViewProvider::isSelectable  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderGeometryObject](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a1d9af3261374f6349b80de8143f37f28),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#ae7302fe3f47eecd4610145dc35a13791),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a72bc03e2ca46d2609e2d881ceb3227b3),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#afec1edf8b96b6cfea2ad7a55ab13843d),
and
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a16cad05d391f2022c154270ffe42759b).

Referenced by
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[Gui::LinkInfo::getElementPicked()](../../d4/da4/classGui_1_1LinkInfo.html#a54b2534133ea222b65a163d226c1be5c),
[getElementPicked()](../../d3/db3/classGui_1_1ViewProvider.html#a0532bd84b0b7f7d57da7a868f3bf90f5),
[Gui::ViewProviderDocumentObject::getElementPicked()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a1aa14689a5cc02702f75e171cc19cfb8),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
and
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1).

## ◆ isShow()

| [bool](../../d9/db9/classbool.html) ViewProvider::isShow  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
checks whether the view provider is visible or not

Reimplemented in
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a078fcadcd3b6dc57ef19cd7e18cffd31),
[Gui::ViewProviderMaterialObject](../../d3/d1a/classGui_1_1ViewProviderMaterialObject.html#a13fbb80e7c364577e32efb78db4eef3d),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#aa1e37497d9c9dc62cfa47e9eeee09042),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#a2495dde72f2ed6cdf5b3a602fd89c2d0),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a527ab1527816b50c089b862399bdc607),
[FemGui::ViewProviderResult](../../d6/d0a/classFemGui_1_1ViewProviderResult.html#a5fd4de7da3ebd5a367bfc5647c8d0938),
[FemGui::ViewProviderSolver](../../d9/d54/classFemGui_1_1ViewProviderSolver.html#a780c949b906063a1782dccca769d45db),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a10b3eeca8648969ee3b2eef152e69278),
[Gui::ViewProviderDocumentObjectGroup](../../df/d84/classGui_1_1ViewProviderDocumentObjectGroup.html#aec0a9064a4bf7d8b4f35a0e6c0ebf88c),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a6875ceb001909d72b9cb43421b8451ae),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a2824961e0bd467a2ae3ae9a50016bd55),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a5463d5c49f1b35d176e467a359364401),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a21113d95073bbcf4ccedcc0282958e53).

References
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54).

Referenced by
[PartGui::ViewProviderPartExt::forceUpdate()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#acd71cb6befca8d6274f7f642266b7bb9),
[Gui::Document::isShow()](../../de/d4e/classGui_1_1Document.html#a676f8f70f1d1d223f60986e8527b31f2),
[isVisible()](../../d3/db3/classGui_1_1ViewProvider.html#a3df346ae0a318f1abe550f869e3c058b),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PartDesignGui::ViewProvider::onDelete()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae369224b0333fe874ef00f3a7d168fe7),
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465),
[update()](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8),
and
[Gui::ViewProviderDocumentObject::updateView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae31dde44f114d3e90bb2e1d544f3e442).

## ◆ isUpdatesEnabled()

[bool](../../d9/db9/classbool.html) ViewProvider::isUpdatesEnabled  | ( | | ) |  const  
---|---|---|---|---  
  
References
[testStatus()](../../d3/db3/classGui_1_1ViewProvider.html#ae87ece80cde8573867485f8e091f18fe),
and
[Gui::UpdateData](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ffa9867733e397c214c7d749fab0c326cf7).

Referenced by
[update()](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8).

## ◆ isVisible()

[bool](../../d9/db9/classbool.html) ViewProvider::isVisible  | ( | | ) |  const  
---|---|---|---|---  
  
References
[isShow()](../../d3/db3/classGui_1_1ViewProvider.html#a002feec6611feb7ea07be1878a5864a3).

Referenced by
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a8437c5be88154b9cb0bd2bae5ef94db3),
[MeshGui::MeshSelection::getViewProviders()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a13d49d4d64c535509228e1f548671aa3),
[ArchVRM.Renderer::removeHidden()](../../d5/dfd/classArchVRM_1_1Renderer.html#a61819c30358d66516bdad27291128881),
and
[Gui::ViewProviderOrigin::setTemporaryVisibility()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#abb766d6f4587e4a16c4d929200944ca1).

## ◆ keyPressed()

| [bool](../../d9/db9/classbool.html) ViewProvider::keyPressed  | ( | [bool](../../d9/db9/classbool.html) | _pressed_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _key_  
| ) | |   
virtual  
  
is called when the provider is in edit and a key event occurs. Only ESC ends
edit.

Reimplemented in
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a5a74f55b08807c4ee6f02c033ddfe104).

Referenced by
[eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99).

## ◆ mergeColorfulOverlayIcons()

| QIcon ViewProvider::mergeColorfulOverlayIcons  | ( | const QIcon & | _orig_| ) |  const  
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a1a0e02c8f62d74cf9d6cc9c5966553f3),
and
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a8b30e2bf90f03ad500516f0dc529d83b).

Referenced by
[PartDesignGui::ViewProvider::mergeColorfulOverlayIcons()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a1a0e02c8f62d74cf9d6cc9c5966553f3),
[SketcherGui::ViewProviderSketch::mergeColorfulOverlayIcons()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a8b30e2bf90f03ad500516f0dc529d83b),
and
[Gui::DocumentObjectItem::testStatus()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a9a6d5067d669995a492431b36676a465).

## ◆ mergeGreyableOverlayIcons()

| QIcon ViewProvider::mergeGreyableOverlayIcons  | ( | const QIcon & | _orig_| ) |  const  
---|---|---|---|---|---  
protectedvirtual  
  
Referenced by
[getIcon()](../../d3/db3/classGui_1_1ViewProvider.html#af6bd43d711cf91767cadf6fcd2827b47),
[PartDesignGui::ViewProviderHelix::getIcon()](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#aaf4fc8a40461a239f0e795227ea3bbae),
[PartDesignGui::ViewProviderLoft::getIcon()](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a79b678e71232046c0c9cc4c9fe7ad6ee),
[PartDesignGui::ViewProviderPipe::getIcon()](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a1fd80b0c0d51dbda347721c5c07e43ba),
[PartDesignGui::ViewProviderPrimitive::getIcon()](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a96f5121e8ac1cdfe2619b5aff372b1dd),
[Gui::ViewProviderDocumentObjectGroup::getIcon()](../../df/d84/classGui_1_1ViewProviderDocumentObjectGroup.html#ad62b53c0a798c9a13f3882a3a7641958),
[Gui::ViewProviderPart::getIcon()](../../d9/d6c/classGui_1_1ViewProviderPart.html#afba5f47c9f0f811fe7983cac5c6f5fa3),
[Gui::ViewProviderDragger::setupContextMenu()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a0e726fd7e3ac87ffba549176445ea15c),
[PartGui::ViewProviderPartExt::setupContextMenu()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#aaa417dd3ca65be537d40605cbb3f3879),
and
[PartDesignGui::ViewProvider::setupContextMenu()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aebfd33a422ee327d6ab76c4f9ebb4b9b).

## ◆ mouseButtonPressed()

| [bool](../../d9/db9/classbool.html) ViewProvider::mouseButtonPressed  | ( | [int](../../d1/da0/classint.html) | _button_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _pressed_ ,   
|  | const SbVec2s & | _cursorPos_ ,   
|  | const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | _viewer_  
| ) | |   
virtual  
  
is called when the Provider is in edit and the mouse is clicked

Reimplemented in
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3).

References
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

Referenced by
[eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99).

## ◆ mouseMove()

| [bool](../../d9/db9/classbool.html) ViewProvider::mouseMove  | ( | const SbVec2s & | _cursorPos_ ,   
---|---|---|---  
|  | [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | _viewer_  
| ) | |   
virtual  
  
is called when the provider is in edit and the mouse is moved

Reimplemented in
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa).

References
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

Referenced by
[eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99).

## ◆ mouseWheelEvent()

| [bool](../../d9/db9/classbool.html) ViewProvider::mouseWheelEvent  | ( | [int](../../d1/da0/classint.html) | _delta_ ,   
---|---|---|---  
|  | const SbVec2s & | _cursorPos_ ,   
|  | const [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | _viewer_  
| ) | |   
virtual  
  
Reimplemented in
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#abf568a3d758cfc6b3a2352d3079e7dad).

References
[OfflineRenderingUtils::viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

Referenced by
[eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99).

## ◆ onBeforeChange()

| void ViewProvider::onBeforeChange  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Reimplemented from subclass.

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057).

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#aefc3f174999bdd4648769e65cfbcf399),
and
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a8951ceface32a935d5305d79aa1626eb).

References
[Gui::Application::Instance](../../d9/da8/classGui_1_1Application.html#ac23ff9ca7b7bfc047f7a2c00e8119df3),
[App::PropertyContainer::onBeforeChange()](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057),
and
[Gui::Application::signalBeforeChangeObject](../../d9/da8/classGui_1_1Application.html#aca05772f45c19b3f5c7b47fb3d8ee7ad).

Referenced by
[Gui::ViewProviderDocumentObject::onBeforeChange()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a8951ceface32a935d5305d79aa1626eb),
and
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onChanged()

| void ViewProvider::onChanged  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Reimplemented from subclass.

Reimplemented from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d).

Reimplemented in
[FemGui::ViewProviderFemPostPlaneFunction](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aff4da6a421671244ed9f106adbaee37a),
[PartDesignGui::ViewProviderDatumCoordinateSystem](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a48324f18ce89cf9a307a32d54e3cfcc3),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#abbbfdc1b1e66ea1ea4ba8a483794161d),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#aa4c52719f57d011b0a4f3bef4c68a016),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a74a77269f6962a4a975229ac51c582c7),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a338b45f77e146a3a179b2f7922de8d8d),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#acad7ad25b7e30c03fc13738bce5db1de),
[Gui::ViewProviderAnnotation](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#a789aabe3e009284175581640dec663c3),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a53d7de6d67521a3dadb7ae43c96869bc),
[Gui::ViewProviderGeometryObject](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#ac9e49ff9d0f734482071f412b15b934c),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a55ba8a09c4ee671752b6e88c3561d9e1),
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#acba30fffb482dd3f286e36fff1dfee5c),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a86520630c898707677753ccc3877eced),
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a8d87ca622183dd3077563ad3d45c479b),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3d33c13c95f3a907325ad1c399dc5a14),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ab319d4e3659d8c99309bd397af321308),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a13a3a3015d78a539b51f342fa516670c),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#ae95be84201f7f51ce6162468c514e33e),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a5d27aeff234b60ec0214c939556b26c5),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#a75537f17b213bb2c7ea45b374ed65375),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae9ec71d871b59be4a532fb2be2cb8d52),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#acd7c344f3f6180e42b53db82ddc998a6),
[MeshGui::ViewProviderMeshDefects](../../da/d50/classMeshGui_1_1ViewProviderMeshDefects.html#a0d494009344982737533a865b26ce7d4),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a6f37857950fa14e1e1978c56706d0797),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a04a16b5ac49a2b5df31304da0a4318ee),
[PartGui::ViewProviderCustom](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[PartGui::ViewProviderPartReference](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a8af0748ed20158c08efa16db288d3f81),
[PartDesignGui::ViewProviderDatumPoint](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ada6d519997cb6ca57d88957962fc1377),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#ad91786e290cd4be69ef99a41c85faa32),
[RobotGui::ViewProviderRobotObject](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a41cfa5ba4f24dacf46491cc903e5a715),
[SketcherGui::ViewProviderCustom](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#a326f53617a41a940cb743b45853c0780),
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#ad13417ef59c1aeb04fbc4fbcc6aa57d2),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a23482323e8ec6da0cb3dd93b00203e73),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a86b7b59890bb041b58c8e5564383e631),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a0387c427509686ba2dff332930fb5efe),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[Gui::ViewProviderPart](../../d9/d6c/classGui_1_1ViewProviderPart.html#a5e76f3437483472cd66247d0eb98aa1a),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a471b5fcc496e5d153b398a0675e2c93e),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a52ae16d5a0dbe879343e3dad26d9e30b),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a257ca77e2256cbd8df847cedc5892289),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[PartDesignGui::ViewProviderBoolean](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#ab446d9f6494af864bd745136c7e20439),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ae317a35c18a1f9b333a14655c35eb8dc),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#af947ca7438432b3448358f4ebcf6bbc1),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a1a42e7ea4d5eb17c7e1f536cad241cc3),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#aada265457fade9ade61cbade5aee4f2b),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a498b66c6f2b5af184c95c4a07bc6f98e),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a7b5d5197907bbf4cc9c65c1004a1da83).

References
[Gui::Application::Instance](../../d9/da8/classGui_1_1Application.html#ac23ff9ca7b7bfc047f7a2c00e8119df3),
[App::ExtensionContainer::onChanged()](../../d6/d76/classApp_1_1ExtensionContainer.html#ad571ff1df010fb7f617689f0e4ff360d),
[Gui::Application::signalChangedObject](../../d9/da8/classGui_1_1Application.html#a7b5ee81dfdfc142b5e0080d1517a8f5d),
and
[Gui::Application::updateActions()](../../d9/da8/classGui_1_1Application.html#a9aa995deb66548d4d8bcf2565beae01c).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onDelete()

| [bool](../../d9/db9/classbool.html) ViewProvider::onDelete  | ( | const std::vector< std::string > & | _subNames_| ) |   
---|---|---|---|---|---  
virtual  
  
Get called if the object is about to get deleted.

Here you can delete other objects, switch their visibility or prevent the
deletion of the object.

Parameters

     subNames| list of selected subelements   
---|---  
  
Returns

    true if the deletion is approved by the view provider. 

Reimplemented in
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#af088d91593fa59ce593fd49716356f32),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#ad0b0713ab92771ae7b95092141223bfb),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a6a44b138d08201a189d8db73fbbee8be),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a1268cee8746e053148fe49cfc61f9e9e),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a3faef51e9f2e5aae49a60b043af9291c),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a9a6f16c2754b100a96f37a11efac104d),
[FemGui::ViewProviderSolver](../../d9/d54/classFemGui_1_1ViewProviderSolver.html#a4cdfba50783d5bffd25927bc99ec0735),
[PartGui::ViewProviderBoolean](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#a373d00ad4fff430f80363ff4e3fa7eec),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#ab048345dbd6162a3f90389c7fa398e02),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#a26b5c231ca52bd3221b392cabee8f431),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#adfb588dd213e7d043ac042a7dda8050e),
[PartGui::ViewProviderMirror](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a952479217b74ad64994248d817c055fd),
[PartGui::ViewProviderFillet](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a923e0a83b084654171dd99eecdc464dd),
[PartGui::ViewProviderChamfer](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a475ba4ccc420a1807fc61b5fe01f462d),
[PartGui::ViewProviderRevolution](../../dc/d27/classPartGui_1_1ViewProviderRevolution.html#a60400330db6dc99c3795e9ac308e1aa2),
[PartGui::ViewProviderLoft](../../d5/d42/classPartGui_1_1ViewProviderLoft.html#a658cffb1bd48ef10e096e9c277a0d22e),
[PartGui::ViewProviderSweep](../../d7/d5f/classPartGui_1_1ViewProviderSweep.html#a4689517481f449c8b291acfcb56d2c45),
[PartGui::ViewProviderOffset](../../df/ded/classPartGui_1_1ViewProviderOffset.html#a58ad6004177fdd87e4c05d3ffb720ac0),
[PartGui::ViewProviderThickness](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#abfbe742067780f3d1ad6f4b8b8d2bc67),
[PartGui::ViewProviderRuledSurface](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#a7255ef1f46cfb225c143bf8e1e6ac0da),
[PartDesignGui::ViewProviderHelix](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a4452f1e116772a2f6fbe29464bc26fc1),
[PartDesignGui::ViewProviderLoft](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a658cffb1bd48ef10e096e9c277a0d22e),
[PartDesignGui::ViewProviderMultiTransform](../../d6/d05/classPartDesignGui_1_1ViewProviderMultiTransform.html#a85c1d63c3e95cdacf8d7e40cec2f3567),
[PartDesignGui::ViewProviderPipe](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#a340ec61aace47f884e0971722e1dac66),
[PartDesignGui::ViewProviderSketchBased](../../d3/d7d/classPartDesignGui_1_1ViewProviderSketchBased.html#ac27bf48431a8f494ce6f6b3c764ef900),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a5672119b22fe16ed78c9732c2e5fbc62),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a81773c64dfc95d972592c1ff76a798d9),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#acdc1c8af04392a2750bef73c0c1f5463),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a837cb333ecc1549e424cff1a8f3ceaf7),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a261f817741efd15a08552b403bd8cdf5),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#ac4f0ad8f27db7108aaf102177217d998),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a53e5f8439ae4f7f01dca9288608eea7c),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a1a45c590fcdae9b3c7edcffb45eb73eb),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#acf76aee7fb1e9e424b20a904245ff226),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae369224b0333fe874ef00f3a7d168fe7),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adec4b2c1311dcb2556764798acfea83a),
[PartDesignGui::ViewProviderBoolean](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#aabf46492095e0512b7b9ef7b475f8228),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a1bb5be52ff0402fa9c980ba768269613),
[PartDesignGui::ViewProviderTransformed](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a37374f5bae033d65e7835b78c2a8ae79),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a83277547707db7a956f740a550845361),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ae1bf897b0b39fd41b8f753be740e0aa7),
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a76255e855deb2936dc630cc4ae63b68d),
and
[PartDesignGui::ViewProviderHole](../../df/dda/classPartDesignGui_1_1ViewProviderHole.html#ab5388b3747ed0c2ec65da23fe401633a).

Referenced by
[StdCmdDelete::activated()](../../da/dc8/classStdCmdDelete.html#a120710ae4a8c0f26451596002a176ee7),
[SketcherGui::ConstraintView::deleteSelectedItems()](../../df/d7b/classSketcherGui_1_1ConstraintView.html#a889547f07246319b638484850553f0d8),
[SketcherGui::ElementView::deleteSelectedItems()](../../dd/d88/classSketcherGui_1_1ElementView.html#aef0f7256d4d6f95265d6c2c1f0ea17ac),
[SketcherGui::ViewProviderSketch::onDelete()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a83277547707db7a956f740a550845361),
and
[Gui::Document::slotDeletedObject()](../../de/d4e/classGui_1_1Document.html#a02acfc1218f2666ad7e6b80c804abc99).

## ◆ partialRender()

[int](../../d1/da0/classint.html) ViewProvider::partialRender  | ( | const std::vector< std::string > & | _subelements_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clear_  
| ) | |   
  
partial rendering setup

Parameters

     subelements| a list of dot separated string refer to the sub element   
---|---  
clear| if true, remove the the subelement from partial rendering. If else, add
the subelement for rendering.  
  
Returns

    Return the number of subelement found

Partial rendering only works if there is at least one SoFCSelectRoot node in
this view provider

References
[Gui::SoSelectionElementAction::Append](../../d6/dce/classGui_1_1SoSelectionElementAction.html#a120acd6a064047dc29eb3531a782f372a7fb11651edff3b1f953a3815c4783753),
[getDetailPath()](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd),
[hasHiddenMarker()](../../d3/db3/classGui_1_1ViewProvider.html#a7a9cd7fe3f4d16e3094e5178cefdc45f),
[hiddenMarker()](../../d3/db3/classGui_1_1ViewProvider.html#ad7ec8cdec25d51ca8309c477c6728a3c),
[Gui::SoSelectionElementAction::Hide](../../d6/dce/classGui_1_1SoSelectionElementAction.html#a120acd6a064047dc29eb3531a782f372a0cb3584de1ded01dc43dad58a8e72ddb),
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54),
[Gui::SoSelectionElementAction::Remove](../../d6/dce/classGui_1_1SoSelectionElementAction.html#a120acd6a064047dc29eb3531a782f372a366675cf5f7f0dce288367062eb40bac),
and
[Gui::SoSelectionElementAction::Show](../../d6/dce/classGui_1_1SoSelectionElementAction.html#a120acd6a064047dc29eb3531a782f372ae3d182a491d7f59947ad2014bcc7b24e).

Referenced by
[Gui::ElementColors::leaveEvent()](../../db/d21/classGui_1_1ElementColors.html#af87efd064a8e813d479f8580fd92d0be).

## ◆ replaceObject()

| [int](../../d1/da0/classint.html) ViewProvider::replaceObject  | ( | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _oldObj_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _newObj_  
| ) | |   
virtual  
  
Replace an object to the view provider by drag and drop.

Parameters

     oldObj| object to be replaced   
---|---  
newObj| object to replace with  
  
Returns

    Returns 0 if not found, 1 if succeeded, -1 if not supported 

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a75216597b08f62e670dc98bf829c8254).

Referenced by
[Gui::ViewProviderDocumentObject::replaceObject()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a75216597b08f62e670dc98bf829c8254).

## ◆ Restore()

| void ViewProvider::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
virtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d6/d76/classApp_1_1ExtensionContainer.html#ab69e6989a20f716411d603c6f40dd3d5
"This method is used to save properties to an XML document.") written
information. Again the Vector as an example:

void
PropertyVector::Restore([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html
"The XML reader class This is an important helper class for the store and
retrieval system of objects ...") &reader)

{

// read my Element

reader.[readElement](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e
"read until a start element is found \(<name>\) or start-end element
\(<name/>\) \(with special name if giv...")("PropertyVector");

// get the value of my Attribute

_cVec.x =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueX");

_cVec.y =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueY");

_cVec.z =
reader.[getAttributeAsFloat](../../dc/d95/classBase_1_1XMLReader.html#ae9307e54ece4b081b9fb227151832820
"return the named attribute as a double floating point \(does type
checking\)")("valueZ");

}

Reimplemented from
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48).

Reimplemented in
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#af020d668456d6c40964757726bb9d1aa).

Referenced by
[Gui::Document::importObjects()](../../de/d4e/classGui_1_1Document.html#a675984f27d23848474de765525202373),
[PartGui::ViewProvider2DObjectGrid::Restore()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#af020d668456d6c40964757726bb9d1aa),
and
[Gui::Document::RestoreDocFile()](../../de/d4e/classGui_1_1Document.html#ac4b89a171b3259b15facb5b1b85b0d09).

## ◆ setDefaultMode()

void ViewProvider::setDefaultMode  | ( | [int](../../d1/da0/classint.html) | _val_| ) |   
---|---|---|---|---|---  
  
## ◆ setDisplayMaskMode()

void ViewProvider::setDisplayMaskMode  | ( | const char *  | _type_| ) |   
---|---|---|---|---|---  
  
Activates the display mask mode _type_.

References
[setModeSwitch()](../../d3/db3/classGui_1_1ViewProvider.html#aebaedef79623db445f3ec055c365d97f).

Referenced by
[Gui::ViewProviderLink::attach()](../../d6/d59/classGui_1_1ViewProviderLink.html#ab31e41e9a24ec097be019cdff4fb969b),
[FemGui::ViewProviderFemPostFunction::attach()](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#a1cd9009bd8fb1f598b2d9ebf797f1aaf),
[FemGui::ViewProviderFemPostObject::attach()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a7dcf3dc1b7f85846e5b50cc08c7f1f46),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionSetDisplayMode()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#a71e307c408049d4af1acd5015e7a6a09),
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[Gui::ViewProviderAnnotation::setDisplayMode()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#af361d4f7a59c8783cf867f8202dc87ee),
[Gui::ViewProviderAnnotationLabel::setDisplayMode()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a6d7f52543d0b7dcca2bcce3e19e750fd),
[Gui::ViewProviderInventorObject::setDisplayMode()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#ae0408363786c66c11023d24fb9b233d0),
[Gui::ViewProviderMeasureDistance::setDisplayMode()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a6c4e08cb2d9b70342b56f9f9f6360113),
[Gui::ViewProviderOrigin::setDisplayMode()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a40b32ada5edb5ebb059e2b877183a735),
[Gui::ViewProviderOriginFeature::setDisplayMode()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a72b50faa11adc7439eca49a88091d9cf),
[Gui::ViewProviderVRMLObject::setDisplayMode()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a4498c81c14269206e593cc222a8e5fdf),
[FemGui::ViewProviderFemConstraint::setDisplayMode()](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#aa8faf9322ef36bfbabd9754e01c45c1b),
[FemGui::ViewProviderFemMesh::setDisplayMode()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ad913bd04802120b611dcc93ad2e8d25a),
[ImageGui::ViewProviderImagePlane::setDisplayMode()](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#affd0c4c45eef027c1903fb3fd297b1f3),
[InspectionGui::ViewProviderInspection::setDisplayMode()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ad4e03e09fda299c351f9a4157eb43c3e),
[MeshGui::ViewProviderFace::setDisplayMode()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#a888234c1802692a99e4650958f185794),
[MeshGui::ViewProviderMesh::setDisplayMode()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ad57706a014c8ff1702534d78c7ebf871),
[MeshGui::ViewProviderMeshCurvature::setDisplayMode()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a91cf69c4c696f02473154bec8fb64dd9),
[MeshGui::ViewProviderMeshNode::setDisplayMode()](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#adf994cdb2b19cebb24da4c8ce759ae09),
[MeshGui::ViewProviderMeshTransform::setDisplayMode()](../../d2/d2b/classMeshGui_1_1ViewProviderMeshTransform.html#aa74e017db9ac4741cdc4ab8ddf9abf42),
[MeshGui::ViewProviderMeshTransformDemolding::setDisplayMode()](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ae476fa70d2ee5e795409c65f4a149fdf),
[MeshPartGui::ViewProviderCurveOnMesh::setDisplayMode()](../../d3/dba/classMeshPartGui_1_1ViewProviderCurveOnMesh.html#a275836df61babb2dea64545d2303952f),
[PartGui::ViewProviderCurveNet::setDisplayMode()](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#a10ae8d56c1d9badd51c68137e9191ba0),
[PartGui::ViewProviderPartReference::setDisplayMode()](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a1c02910cbebda3a04bc9706a0d8acd47),
[PathGui::ViewProviderPath::setDisplayMode()](../../db/d31/classPathGui_1_1ViewProviderPath.html#af0a094fc86851393850e8f477f959bea),
[PointsGui::ViewProviderPoints::setDisplayMode()](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a6fba67f9c755f7ae29cdfe1eb581b6b1),
[RobotGui::ViewProviderRobotObject::setDisplayMode()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a4403e558abdd0ad19304839c2a3552c0),
[RobotGui::ViewProviderTrajectory::setDisplayMode()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#a87f43f3e45746dac93815dc41284a092),
[Gui::ViewProviderPlacement::setDisplayMode()](../../da/d5e/classGui_1_1ViewProviderPlacement.html#aebc8060c36f38417cae67d944f29d93d),
[PartGui::ViewProviderPartExt::setDisplayMode()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a87d4c4813f501412ce70c33e422ba9eb),
[PartDesignGui::ViewProviderDatum::setDisplayMode()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#acbcff6cf3737b6dc7585d1cb1441e7c5),
[Gui::ViewProviderExtern::setModeBySoInput()](../../dd/d9c/classGui_1_1ViewProviderExtern.html#acbf98598a34ab1f2ec5893c44851964c),
[PartDesignGui::ViewProviderAddSub::setPreviewDisplayMode()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#af83ba83cdbf7dad8bba49c1ef5db6963),
[MeshGui::ViewProviderMeshOrientation::showDefects()](../../d1/d8e/classMeshGui_1_1ViewProviderMeshOrientation.html#acad074355a307b6f0e8059ae22ba8d54),
[MeshGui::ViewProviderMeshNonManifolds::showDefects()](../../d5/d95/classMeshGui_1_1ViewProviderMeshNonManifolds.html#aa021d71ade5620d8dc36c94220862be8),
[MeshGui::ViewProviderMeshNonManifoldPoints::showDefects()](../../d6/d60/classMeshGui_1_1ViewProviderMeshNonManifoldPoints.html#ad648ec1aee86628d91e6aec48eafaa42),
[MeshGui::ViewProviderMeshDuplicatedFaces::showDefects()](../../d1/d9b/classMeshGui_1_1ViewProviderMeshDuplicatedFaces.html#a435c5361ffb8312295cc076da55d56a8),
[MeshGui::ViewProviderMeshDegenerations::showDefects()](../../d2/da9/classMeshGui_1_1ViewProviderMeshDegenerations.html#a954810db894668aaea3d6a26f310f2ea),
[MeshGui::ViewProviderMeshDuplicatedPoints::showDefects()](../../d5/d26/classMeshGui_1_1ViewProviderMeshDuplicatedPoints.html#af52e3e5a78f9c0ecceab7bb945b1c075),
[MeshGui::ViewProviderMeshIndices::showDefects()](../../dd/d71/classMeshGui_1_1ViewProviderMeshIndices.html#abcb21eec9d9285a3d13ee103e03beaaa),
[MeshGui::ViewProviderMeshSelfIntersections::showDefects()](../../d0/d67/classMeshGui_1_1ViewProviderMeshSelfIntersections.html#aafee413a88509d1d7a81df3687c64726),
and
[MeshGui::ViewProviderMeshFolds::showDefects()](../../d8/d06/classMeshGui_1_1ViewProviderMeshFolds.html#a1a9474aafd32ff0b730a7c795a8fc5e9).

## ◆ setDisplayMode()

| void ViewProvider::setDisplayMode  | ( | const char *  | _ModeName_| ) |   
---|---|---|---|---|---  
virtual  
  
set the display mode

If you add new viewing modes in
[getDisplayModes()](../../d3/db3/classGui_1_1ViewProvider.html#a26e55171275bb4a559d91698b170b066)
then you need to reimplement also seDisplaytMode() to handle these new modes
by setting the appropriate display mode.

Reimplemented in
[Gui::ViewProviderAnnotation](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#af361d4f7a59c8783cf867f8202dc87ee),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a6d7f52543d0b7dcca2bcce3e19e750fd),
[Gui::ViewProviderInventorObject](../../de/ded/classGui_1_1ViewProviderInventorObject.html#ae0408363786c66c11023d24fb9b233d0),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a6c4e08cb2d9b70342b56f9f9f6360113),
[Gui::ViewProviderOrigin](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a40b32ada5edb5ebb059e2b877183a735),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a72b50faa11adc7439eca49a88091d9cf),
[Gui::ViewProviderVRMLObject](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a4498c81c14269206e593cc222a8e5fdf),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#ae363d234e05309614584ac4c1b5614af),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#ac4d478a1601d0a926493914bf64957b4),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#ae7b71f59ccc5e03052b67507bac6bc5f),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#aa8faf9322ef36bfbabd9754e01c45c1b),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#ad913bd04802120b611dcc93ad2e8d25a),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a999592908e3e60037b769402537caf0b),
[ImageGui::ViewProviderImagePlane](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#affd0c4c45eef027c1903fb3fd297b1f3),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ad4e03e09fda299c351f9a4157eb43c3e),
[MeshGui::ViewProviderFace](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#a888234c1802692a99e4650958f185794),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ad57706a014c8ff1702534d78c7ebf871),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a91cf69c4c696f02473154bec8fb64dd9),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#adf994cdb2b19cebb24da4c8ce759ae09),
[MeshGui::ViewProviderMeshTransform](../../d2/d2b/classMeshGui_1_1ViewProviderMeshTransform.html#aa74e017db9ac4741cdc4ab8ddf9abf42),
[MeshGui::ViewProviderMeshTransformDemolding](../../d2/df5/classMeshGui_1_1ViewProviderMeshTransformDemolding.html#ae476fa70d2ee5e795409c65f4a149fdf),
[MeshPartGui::ViewProviderCurveOnMesh](../../d3/dba/classMeshPartGui_1_1ViewProviderCurveOnMesh.html#a275836df61babb2dea64545d2303952f),
[PartGui::ViewProviderCurveNet](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#a10ae8d56c1d9badd51c68137e9191ba0),
[PartGui::ViewProviderPartReference](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a1c02910cbebda3a04bc9706a0d8acd47),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#af0a094fc86851393850e8f477f959bea),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a6fba67f9c755f7ae29cdfe1eb581b6b1),
[RobotGui::ViewProviderRobotObject](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a4403e558abdd0ad19304839c2a3552c0),
[RobotGui::ViewProviderTrajectory](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#a87f43f3e45746dac93815dc41284a092),
[TechDrawGui::ViewProviderAnnotation](../../d8/dd5/classTechDrawGui_1_1ViewProviderAnnotation.html#af361d4f7a59c8783cf867f8202dc87ee),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#acd794b93c525381e9add0c7c452cd86a),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a55cddfa8f12ed85bdfcc017c3442e46c),
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#af427e4af063955a685a9c4a263607a01),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a9a89cc94c304b214e0988cd20f607fbf),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#ab78cab034771b7f02011a335b6b48b6c),
[TechDrawGui::ViewProviderSpreadsheet](../../d1/d67/classTechDrawGui_1_1ViewProviderSpreadsheet.html#a9e844a637ece738d54a6797cb6f43dd4),
[TechDrawGui::ViewProviderSymbol](../../da/de5/classTechDrawGui_1_1ViewProviderSymbol.html#a0c295a1769eb08cef2efe1bcc7625652),
[TechDrawGui::ViewProviderTile](../../d1/daa/classTechDrawGui_1_1ViewProviderTile.html#a038e383ed004bd549dc9897096fd5a72),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a9361c2855a4cf5917620b263384a23d8),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#add89addc7af2e48fa74fd8b33247a883),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#ab2c93413df70ffcce959793fb0e9ee62),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#ae299478f48ecc19160cf9f29955b9ff5),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#aebc8060c36f38417cae67d944f29d93d),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a87d4c4813f501412ce70c33e422ba9eb),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a685366158948c29702fd282bc927fd25),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#acbcff6cf3737b6dc7585d1cb1441e7c5),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a0ed7017ac337279b5964da31d6b541d2),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#a07010a87c4c28257720597894c005252),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a210d93c1c15933936d7aa41dcb76e1b7),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a58627ea8c47bbefcb80ba69afa7e101e),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a04571c7ba8f4995d7d3419892e2805d2),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#aee6a0f3aacf87324d554f5c0f4ad00e8).

Referenced by
[Gui::ViewProviderDocumentObject::setActiveMode()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a680b6d8d00fa1135eee59edbda9f3bd0),
[Gui::ViewProviderAnnotation::setDisplayMode()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#af361d4f7a59c8783cf867f8202dc87ee),
[Gui::ViewProviderAnnotationLabel::setDisplayMode()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a6d7f52543d0b7dcca2bcce3e19e750fd),
[Gui::ViewProviderInventorObject::setDisplayMode()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#ae0408363786c66c11023d24fb9b233d0),
[Gui::ViewProviderMeasureDistance::setDisplayMode()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a6c4e08cb2d9b70342b56f9f9f6360113),
[Gui::ViewProviderOrigin::setDisplayMode()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#a40b32ada5edb5ebb059e2b877183a735),
[Gui::ViewProviderOriginFeature::setDisplayMode()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a72b50faa11adc7439eca49a88091d9cf),
[Gui::ViewProviderVRMLObject::setDisplayMode()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a4498c81c14269206e593cc222a8e5fdf),
[MeshGui::ViewProviderMeshCurvature::setDisplayMode()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a91cf69c4c696f02473154bec8fb64dd9),
and
[Gui::ViewProviderPlacement::setDisplayMode()](../../da/d5e/classGui_1_1ViewProviderPlacement.html#aebc8060c36f38417cae67d944f29d93d).

## ◆ setEdit()

| [bool](../../d9/db9/classbool.html) ViewProvider::setEdit  | ( | [int](../../d1/da0/classint.html) | _ModNum_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
is called by the document when the provider goes in edit mode

Reimplemented in
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a9e6d7fb0b017900b7ac12e21c88ceabc),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a332f677694e4eb770dccc6698df4a27e),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#ad43efa79b2a2ae8acb280614155105a6),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#afccdf7d794c7c6eb07c06404574c0b45),
[FemGui::ViewProviderFemConstraintBearing](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#ada0e85289207db1bc3b9ca4b1f03e6fc),
[FemGui::ViewProviderFemConstraintContact](../../d9/d3d/classFemGui_1_1ViewProviderFemConstraintContact.html#ab6aafc618f8c7b4737ef4d06dca0b739),
[FemGui::ViewProviderFemConstraintDisplacement](../../d7/d3f/classFemGui_1_1ViewProviderFemConstraintDisplacement.html#aa763ff22c3aa35dc8c6f3265b307287e),
[FemGui::ViewProviderFemConstraintFixed](../../d4/d9c/classFemGui_1_1ViewProviderFemConstraintFixed.html#a813e76666d3bc3aca1e3e47565c872e7),
[FemGui::ViewProviderFemConstraintFluidBoundary](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#adce6e7f53edbdcfdae6d45365ba57f0f),
[FemGui::ViewProviderFemConstraintForce](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#a39e8664ff886cf249a80a72df142ffa9),
[FemGui::ViewProviderFemConstraintGear](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#aeaddd287de5da327467599e4fd5db37b),
[FemGui::ViewProviderFemConstraintHeatflux](../../d0/dea/classFemGui_1_1ViewProviderFemConstraintHeatflux.html#a097b2df936bd0057bc591268cff63859),
[FemGui::ViewProviderFemConstraintInitialTemperature](../../d8/d07/classFemGui_1_1ViewProviderFemConstraintInitialTemperature.html#a009f5341493d283dbd42b82f7fd27b68),
[FemGui::ViewProviderFemConstraintPlaneRotation](../../d7/d0a/classFemGui_1_1ViewProviderFemConstraintPlaneRotation.html#a206254f1c763260f072c36a215456a3d),
[FemGui::ViewProviderFemConstraintPressure](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a263f869ac7b10ee53176680a362e308a),
[FemGui::ViewProviderFemConstraintPulley](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#af3e6550cd186ed7c85d3a1e5a1ed5034),
[FemGui::ViewProviderFemConstraintSpring](../../d5/d4f/classFemGui_1_1ViewProviderFemConstraintSpring.html#a7707003f9949bc205321d51c3fa2307b),
[FemGui::ViewProviderFemConstraintTemperature](../../d1/df6/classFemGui_1_1ViewProviderFemConstraintTemperature.html#aeda5483ccbf96c4fe6eb2ca7a9613d67),
[FemGui::ViewProviderFemConstraintTransform](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#aa18e9edaaaca3d70ecaa70c7324d9cb8),
[FemGui::ViewProviderFemMeshShapeNetgen](../../df/db3/classFemGui_1_1ViewProviderFemMeshShapeNetgen.html#aadc0d17d1ae76eb0a0ea3e5aca6cd5bd),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#a6b9d37dcfe0a7353636f93a552e26e31),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a0061e5e27869609b71c4ea0c5af8b619),
[FemGui::ViewProviderSetElements](../../dd/d62/classFemGui_1_1ViewProviderSetElements.html#a73a081f3347b902c5dab471685962630),
[FemGui::ViewProviderSetFaces](../../d9/d46/classFemGui_1_1ViewProviderSetFaces.html#ad00b9493187b0c5a672120f53335c253),
[FemGui::ViewProviderSetGeometry](../../dd/d48/classFemGui_1_1ViewProviderSetGeometry.html#a273f5ea4cda8beaca861257a9cabb556),
[FemGui::ViewProviderSetNodes](../../d5/d44/classFemGui_1_1ViewProviderSetNodes.html#afa5974e28b2cc9cf53c07adad3170aae),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a40deb657f9bdff42591951bab87920d0),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a9fa0acb41e43ce0dd79d58330cd10ffe),
[PartGui::ViewProviderCurveNet](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#aff7108f2d0ef7759484b9446b252b917),
[PartGui::ViewProviderImport](../../d0/d76/classPartGui_1_1ViewProviderImport.html#a3f7d8b2fd75fb4f36bdbb7d4ce14b26c),
[PartGui::ViewProviderMirror](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a),
[PartGui::ViewProviderFillet](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#ac9dbcc3535eb12550c5825593f533e25),
[PartGui::ViewProviderChamfer](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a955c6e923d41c98de7aed8ee8ea8b2ba),
[PartGui::ViewProviderOffset](../../df/ded/classPartGui_1_1ViewProviderOffset.html#aba844b2a4f4129a7ed239641d7978851),
[PartGui::ViewProviderThickness](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#a6cabec4fc1ea58cd5ba6a66f8b279fc6),
[PartGui::ViewProviderPrimitive](../../dd/dfd/classPartGui_1_1ViewProviderPrimitive.html#a830586f4badf80a1ec8e9e2d02f280d5),
[PartDesignGui::ViewProviderBase](../../d7/d54/classPartDesignGui_1_1ViewProviderBase.html#a4609b7dfe7e5fdc6ae721a101bccfd4e),
[PartDesignGui::ViewProviderDressUp](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#a4119fd1599c9378ba7b4e9185637c51c),
[PartDesignGui::ViewProviderHelix](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#a2fe0852e9a26cb1e399ac84be8251d9c),
[PartDesignGui::ViewProviderHole](../../df/dda/classPartDesignGui_1_1ViewProviderHole.html#aa1c50b1c4e8d2446e8f91b3d79c2d9b4),
[PartDesignGui::ViewProviderLoft](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#ae908f2000b0bed946505fd8d96a20236),
[PartDesignGui::ViewProviderPipe](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#acc714758bdf79639a8a30c99e1e8e21b),
[PartDesignGui::ViewProviderPrimitive](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a830586f4badf80a1ec8e9e2d02f280d5),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#a98bbbb533d93a02c594c80f10ce780db),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a0b86e870101c6db6e59da6632b15da1a),
[RaytracingGui::ViewProviderLux](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a559d010dd9902addb4de84170aac9f51),
[RaytracingGui::ViewProviderPovray](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a76685922c30f4f6a92a74fafcc800fa2),
[RobotGui::ViewProviderEdge2TracObject](../../da/d5e/classRobotGui_1_1ViewProviderEdge2TracObject.html#af62127f819ab7dd2f1cb94e041f04381),
[RobotGui::ViewProviderTrajectoryCompound](../../d7/d47/classRobotGui_1_1ViewProviderTrajectoryCompound.html#aef2ee5ba2388c7dd85aef72656a6c297),
[RobotGui::ViewProviderTrajectoryDressUp](../../da/dff/classRobotGui_1_1ViewProviderTrajectoryDressUp.html#aba54ff221e761e23bd2c887b39fd876e),
[SurfaceGui::ViewProviderFilling](../../d0/dac/classSurfaceGui_1_1ViewProviderFilling.html#a5f6e7210301bf80e264d2209c92e67d4),
[SurfaceGui::ViewProviderGeomFillSurface](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#ae59f5b76efea8f8d54f7eb93fb42b7b6),
[SurfaceGui::ViewProviderSections](../../da/dd0/classSurfaceGui_1_1ViewProviderSections.html#a2c85256da171bcbd0547974f29ead549),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a2e025ddacfaa37230ff483b91d273338),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#ad0f391bd413a036384a01912569d5bc4),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9e6409e4b7a5516b47b05ed3945fca40),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#ac5dcab3a423587bd0dc448c46a7b6d35),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a765bef926a390295b2440caf41c7001e),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#abe7e29edccb3b64c78291d246c9d22b1),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a758558e7e660c02f277bc621cb7e2e61),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a38606dd2e773bcb04de0fa4be2c4c0b7),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#ad9430bcd1a82544e7d00ed2b2ebeffdc),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a72f3abcc67100d8740725e3344df323d),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a1181d53d0a1c61ea05d59905c4b4e0cd),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a6f3f1f8893820843dd51f280ca8a3dec),
[PartDesignGui::ViewProviderBoolean](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#a8332deec17f6d74c084a3b935c9aa6a0),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ac56d3ca4da8d5573b3496ee332304919),
[PartDesignGui::ViewProviderShapeBinder](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a8ab60c5d127611b0a984fedcc5d286a9),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#ab69265d464691c650bb6bd89015af92e),
[PartDesignGui::ViewProviderTransformed](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a5d37e6ba0bf8efbd6ebea83c4c331bb2),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#ad28c651e806a00fca15332d4c04b47c9),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a2bc7d2572d6e443dd7e60728404aa8bb),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a28afe467eff5280ce4f2f4c06c334403),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a9e2a641e6843356f975b70dc8327411d),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#aa4d620f567a62273aff719609d2e0590),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a17780fa2e133a40608c422364b034e25),
and
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a454f195000fee3cbed596d1b4c20fa49).

Referenced by
[ArchGrid.ViewProviderArchGrid::doubleClicked()](../../d4/dbf/classArchGrid_1_1ViewProviderArchGrid.html#a35948c50ff2dccdada47d584d8bf32bd),
[ArchReference.ViewProviderArchReference::doubleClicked()](../../d2/dfd/classArchReference_1_1ViewProviderArchReference.html#a921a71a757c5853c3331216eefb23703),
[draftviewproviders.view_dimension.ViewProviderDimensionBase::doubleClicked()](../../d6/d45/classdraftviewproviders_1_1view__dimension_1_1ViewProviderDimensionBase.html#a164ae40613358c396be3f6b9fae3937d),
[draftviewproviders.view_hatch.ViewProviderDraftHatch::doubleClicked()](../../dd/d75/classdraftviewproviders_1_1view__hatch_1_1ViewProviderDraftHatch.html#a9274ff72268d6c1a4337118b5db8bcc4),
[draftviewproviders.view_text.ViewProviderText::doubleClicked()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#adc22c64d135df407787ca53f9029c3a0),
[PathScripts.PathPropertyBagGui.ViewProvider::doubleClicked()](../../d5/d77/classPathScripts_1_1PathPropertyBagGui_1_1ViewProvider.html#a915f858e0483981f8124bdf4df7e02d4),
[PathScripts.PathSetupSheetGui.ViewProvider::doubleClicked()](../../dc/dc3/classPathScripts_1_1PathSetupSheetGui_1_1ViewProvider.html#a9b1b82571f01e8e740eadabfec88b9f3),
[PathScripts.PathToolBitGui.ViewProvider::doubleClicked()](../../d0/d90/classPathScripts_1_1PathToolBitGui_1_1ViewProvider.html#a7265835d9e6286fa1e48f47a0f2b82f0),
[Spreadsheet_legacy.ViewProviderSpreadsheet::doubleClicked()](../../d6/d84/classSpreadsheet__legacy_1_1ViewProviderSpreadsheet.html#aa89fcb2be2b67b2f1d210bd06ea9e55a),
[ArchSchedule.CommandArchSchedule::IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[FemGui::ViewProviderFemAnalysis::setEdit()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#ad43efa79b2a2ae8acb280614155105a6),
[TechDrawGui::ViewProviderBalloon::setEdit()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a2e025ddacfaa37230ff483b91d273338),
[TechDrawGui::ViewProviderDimension::setEdit()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#ad0f391bd413a036384a01912569d5bc4),
[TechDrawGui::ViewProviderLeader::setEdit()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9e6409e4b7a5516b47b05ed3945fca40),
[TechDrawGui::ViewProviderRichAnno::setEdit()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#abe7e29edccb3b64c78291d246c9d22b1),
[TechDrawGui::ViewProviderViewPart::setEdit()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a758558e7e660c02f277bc621cb7e2e61),
[TechDrawGui::ViewProviderViewSection::setEdit()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a38606dd2e773bcb04de0fa4be2c4c0b7),
[TechDrawGui::ViewProviderWeld::setEdit()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#ad9430bcd1a82544e7d00ed2b2ebeffdc),
[Gui::ViewProviderLink::setEdit()](../../d6/d59/classGui_1_1ViewProviderLink.html#a72f3abcc67100d8740725e3344df323d),
[TechDrawGui::ViewProviderHatch::setEdit()](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a9e2a641e6843356f975b70dc8327411d),
[TechDrawGui::ViewProviderPage::setEdit()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#aa4d620f567a62273aff719609d2e0590),
[PathScripts.PathIconViewProvider.ViewProvider::setupContextMenu()](../../d6/d55/classPathScripts_1_1PathIconViewProvider_1_1ViewProvider.html#a9a8ca3029fe2523b0d7736c1d4e611a7),
[PathScripts.PathJobGui.ViewProvider::setupContextMenu()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#ab8dd16390af82dadddf816c3a85cae0b),
[PathScripts.PathOpGui.ViewProvider::setupContextMenu()](../../db/df9/classPathScripts_1_1PathOpGui_1_1ViewProvider.html#a79f8f54d1d96c0a29b00b0775e5231ac),
[PathScripts.PathToolControllerGui.ViewProvider::setupContextMenu()](../../db/db5/classPathScripts_1_1PathToolControllerGui_1_1ViewProvider.html#a2f21a1b07712507aedc89ac30d8379c5),
and
[startEditing()](../../d3/db3/classGui_1_1ViewProvider.html#a4e61647f7d508c3472f202661c4fb8a8).

## ◆ setEditViewer()

| void ViewProvider::setEditViewer  | ( | [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _ModNum_  
| ) | |   
virtual  
  
adjust viewer settings when editing a view provider

Reimplemented in
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5746c8658c714b1910627ea804ca2353),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a3ed619a014c6054537c032ff7a524b83).

Referenced by
[Gui::View3DInventorViewer::setEditingViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a7067bcaa7dd4a8b2835582ce30c2c385).

## ◆ setElementColors()

| virtual void Gui::ViewProvider::setElementColors  | ( | const std::map< std::string, [App::Color](../../d3/d3a/classApp_1_1Color.html) > & | _colors_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#af274c7d8619bfae997be5ea17b7c72b3).

Referenced by
[Gui::ElementColors::Private::apply()](../../d8/dc9/classElementColors_1_1Private.html#a66e40ead78f26aa47dc150184afb9a06).

## ◆ setLinkVisible()

void ViewProvider::setLinkVisible  | ( | [bool](../../d9/db9/classbool.html) | _visible_| ) |   
---|---|---|---|---|---  
  
## ◆ setModeSwitch()

| void ViewProvider::setModeSwitch  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Turn on mode switch.

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ab6efd4382f287dbf02a7ed30f10873a8).

References
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54).

Referenced by
[setDisplayMaskMode()](../../d3/db3/classGui_1_1ViewProvider.html#a564f691d12e5fd38892c1bcb7070bd64),
[Gui::ViewProviderDocumentObject::setModeSwitch()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ab6efd4382f287dbf02a7ed30f10873a8),
[setOverrideMode()](../../d3/db3/classGui_1_1ViewProvider.html#ad74c21d50c90ffcdca8a7f274f697943),
and
[show()](../../d3/db3/classGui_1_1ViewProvider.html#a8cb686581d004ed322be5af4cc876301).

## ◆ setOverrideMode()

| void ViewProvider::setOverrideMode  | ( | const std::string & | _mode_| ) |   
---|---|---|---|---|---  
virtual  
  
Overrides the display mode with mode.

Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a0cb2482084a8349fea2b4f59e0ca9e0f),
and
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac0025966b6885197861269fee3a65e60).

References
[overrideMode](../../d3/db3/classGui_1_1ViewProvider.html#a30d0a73702d5fe359395cad8e978941a),
[pcModeSwitch](../../d3/db3/classGui_1_1ViewProvider.html#a4d14215b1b0729f2534057f9b0139d54),
and
[setModeSwitch()](../../d3/db3/classGui_1_1ViewProvider.html#aebaedef79623db445f3ec055c365d97f).

Referenced by
[Gui::View3DInventorViewer::addViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a3a675a24c21e175605a6795b2b033ba5),
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[Gui::ViewProviderLink::setOverrideMode()](../../d6/d59/classGui_1_1ViewProviderLink.html#a0cb2482084a8349fea2b4f59e0ca9e0f),
and
[PartDesignGui::ViewProviderBody::setOverrideMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac0025966b6885197861269fee3a65e60).

## ◆ setRenderCacheMode()

| void ViewProvider::setRenderCacheMode  | ( | [int](../../d1/da0/classint.html) | _mode_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e).

## ◆ setStatus()

void Gui::ViewProvider::setStatus  | ( | [ViewStatus](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ff) | _pos_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _on_  
| ) | |   
  
Referenced by
[Gui::Document::addViewProvider()](../../de/d4e/classGui_1_1Document.html#aa66c8ca1ccffd5f1acca25e54cae5772),
[Gui::ViewProviderDocumentObject::detachFromDocument()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a00c6b0fe1d6e386ae90e3b0e917b1556),
[Gui::Document::importObjects()](../../de/d4e/classGui_1_1Document.html#a675984f27d23848474de765525202373),
[setUpdatesEnabled()](../../d3/db3/classGui_1_1ViewProvider.html#aa6c012b46ca6ba7d41814323b3c0f9e1),
[Gui::Document::slotFinishRestoreObject()](../../de/d4e/classGui_1_1Document.html#abb764b718e18f1922ea3dff2db0986e3),
[Gui::Document::slotNewObject()](../../de/d4e/classGui_1_1Document.html#a73fa9bf80a6dc858e853771c6e3f4cdb),
[PartDesignGui::ViewProviderDatumPoint::ViewProviderDatumPoint()](../../dc/d9d/classPartDesignGui_1_1ViewProviderDatumPoint.html#ad205837386268027a4644450a27b1393),
[DrawingGui::ViewProviderDrawingClip::ViewProviderDrawingClip()](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#aae6b494db32aabadde6d7dd2a27292a9),
[DrawingGui::ViewProviderDrawingView::ViewProviderDrawingView()](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a2e148b765824dd0176d03f0c59609458),
[PartDesignGui::ViewProviderShapeBinder::ViewProviderShapeBinder()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a530772439eebfaf7678a3442bb62fd31),
[TechDrawGui::ViewProviderTemplate::ViewProviderTemplate()](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a7c38fd3cf4fd78ec53c97f14217613d9),
and
[TechDrawGui::ViewProviderViewClip::ViewProviderViewClip()](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#a129ec0fd4acf31f99cee3efb79f9e766).

## ◆ setTransformation() [1/2]

| void ViewProvider::setTransformation  | ( | const [Base::Matrix4D](../../d5/db4/classBase_1_1Matrix4D.html) & | _rcMatrix_| ) |   
---|---|---|---|---|---  
virtual  
  
set the viewing transformation of the provider

References
[Base::Matrix4D::getGLMatrix()](../../d5/db4/classBase_1_1Matrix4D.html#a8bb6545451679312a37458ea2760d18e),
and
[pcTransform](../../d3/db3/classGui_1_1ViewProvider.html#a310fa4e016c1c6fb01a075710eb666a7).

Referenced by
[Gui::Dialog::TransformStrategy::acceptDataTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a7eef0b122a11900cca84fcf149180e90),
[Gui::Dialog::TransformStrategy::applyViewTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#a3b0ef5872b6be50f8e2cb58b460113f3),
[Gui::ViewProviderGeoFeatureGroupExtension::extensionUpdateData()](../../d2/de9/classGui_1_1ViewProviderGeoFeatureGroupExtension.html#aeb7b059cc68cc0d3705101a1fbcda918),
[Gui::Dialog::TransformStrategy::resetViewTransform()](../../d9/d93/classGui_1_1Dialog_1_1TransformStrategy.html#af5a0cbfc3f8a966c735d6a8ea0ddc451),
[RobotGui::ViewProviderRobotObject::setAxisTo()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#aed595606c9254fe301f2c69741204058),
[Gui::Document::setPos()](../../de/d4e/classGui_1_1Document.html#a7211acb1910429e23a86afffbcbbe875),
and
[RobotGui::ViewProviderRobotObject::updateData()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747).

## ◆ setTransformation() [2/2]

| void ViewProvider::setTransformation  | ( | const SbMatrix & | _rcMatrix_| ) |   
---|---|---|---|---|---  
virtual  
  
References
[pcTransform](../../d3/db3/classGui_1_1ViewProvider.html#a310fa4e016c1c6fb01a075710eb666a7).

## ◆ setupContextMenu()

| void ViewProvider::setupContextMenu  | ( | [QMenu](../../de/d3d/classQMenu.html) *  | _menu_ ,   
---|---|---|---  
|  | [QObject](../../d9/d5b/classQObject.html) *  | _receiver_ ,   
|  | const char *  | _method_  
| ) | |   
virtual  
  
set up the context-menu with the supported edit modes

Reimplemented in
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a8902eb5b9df4ec0e12f68e2eee3fd30d),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#ad81e51f4ed675f076097e7c13a270aa8),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a810d529ee86207928e88da63e5c10516),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#ad64c637945fcd0c61ae4ad1b210ca769),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a14fb39b4d986d6bcd3b3d38ac6b79424),
[PartGui::ViewProviderHelixParametric](../../d2/db8/classPartGui_1_1ViewProviderHelixParametric.html#afe4870579984f9ee9e385aada191e940),
[PartGui::ViewProviderSpiralParametric](../../d6/dc3/classPartGui_1_1ViewProviderSpiralParametric.html#adefbe81b4949453d45d05f61ba0b9dc3),
[PartGui::ViewProviderMirror](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a769ac91deab77dcb92da61aba0413fc3),
[PartGui::ViewProviderFillet](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#acd52791939a7c78d8582f4d346015bbb),
[PartGui::ViewProviderChamfer](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a580781b5d0d387cd51ca7b750bf9a13d),
[PartGui::ViewProviderOffset](../../df/ded/classPartGui_1_1ViewProviderOffset.html#ac193fbdb9e3fc445afa057bcb9db1b4c),
[PartGui::ViewProviderThickness](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#ac77c8fd3a3756238857703cbc6554b08),
[PartGui::ViewProviderPrimitive](../../dd/dfd/classPartGui_1_1ViewProviderPrimitive.html#abea2a5f699192afe8ab8f6a8168cad3f),
[PartDesignGui::ViewProviderDressUp](../../dd/dfd/classPartDesignGui_1_1ViewProviderDressUp.html#abebd5378c17a70d360df64478b59fa6f),
[PartDesignGui::ViewProviderGroove](../../d7/de1/classPartDesignGui_1_1ViewProviderGroove.html#a9f04f8149fd0667ebf8d171ebefa0675),
[PartDesignGui::ViewProviderHelix](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#ab9906c1ca815a842db762b7c4b4280bb),
[PartDesignGui::ViewProviderLoft](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a97d457a1a8f4cee8a2c92fe2d9ddf834),
[PartDesignGui::ViewProviderMultiTransform](../../d6/d05/classPartDesignGui_1_1ViewProviderMultiTransform.html#aa602ff4d701f9186e2d0b178ac20d989),
[PartDesignGui::ViewProviderPad](../../d5/df6/classPartDesignGui_1_1ViewProviderPad.html#ae8447b21aa001a68920999b695690faf),
[PartDesignGui::ViewProviderPipe](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#aa4fe2744d1d265170b7aa27801b36eb3),
[PartDesignGui::ViewProviderPocket](../../dc/d38/classPartDesignGui_1_1ViewProviderPocket.html#adedbb3f9720641287196e543c9755597),
[PartDesignGui::ViewProviderRevolution](../../df/db0/classPartDesignGui_1_1ViewProviderRevolution.html#a7fe1c6d1811e2b411a763b549332d97c),
[SurfaceGui::ViewProviderFilling](../../d0/dac/classSurfaceGui_1_1ViewProviderFilling.html#a50386a1da0181e2407a2d4292fdd69fa),
[SurfaceGui::ViewProviderGeomFillSurface](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#a97487f389a05971ef3b3d20f7b937e7d),
[SurfaceGui::ViewProviderSections](../../da/dd0/classSurfaceGui_1_1ViewProviderSections.html#a4eb1d777d5b2c7b12e43e0cf61c879f1),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a565b5cb9dc2e362ef10e12bbf44a0617),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a08d18e44457f139fcb55fe8d3ea139a5),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a1796fb4ffd38967bbf3b147056418392),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#aa0f5f9f95880a6812ec06d6e65a630b6),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a0e726fd7e3ac87ffba549176445ea15c),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a1e5de483828c97463a497ac82bc5df49),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#aaa417dd3ca65be537d40605cbb3f3879),
[PartDesignGui::ViewProviderBoolean](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#a00943b65bfc1cecb933632813837e096),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ab1ef47ab6a3ae90671330b4a34d18bfe),
[PartDesignGui::ViewProviderShapeBinder](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#ac8884ad8eaf080377ba8e6f202046ffb),
[PartDesignGui::ViewProviderTransformed](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a87849672c8acf98e6f2f6abf26abca75),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a5335f8b65f3f5862801462fdc1c6a81a),
[Gui::ViewProviderTextDocument](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a5a639a77236f3bbde9daade6cf323fe8),
[FemGui::ViewProviderFemMeshShapeNetgen](../../df/db3/classFemGui_1_1ViewProviderFemMeshShapeNetgen.html#a20365a2f7bd1919d24c352beada050f1),
[PartDesignGui::ViewProviderBase](../../d7/d54/classPartDesignGui_1_1ViewProviderBase.html#a5cd2b624bcbc130feb179fa03fff4431),
[PartDesignGui::ViewProviderHole](../../df/dda/classPartDesignGui_1_1ViewProviderHole.html#a4d8c88fba840b21062b4e1fabdb7861c),
[PartDesignGui::ViewProviderPrimitive](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a0dfd73206f062385db28131e7a735b66),
[RaytracingGui::ViewProviderLux](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a66c44946a08d2b6018a30e5d0bce8317),
[RaytracingGui::ViewProviderPovray](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#ae6cf477c9696cdaef8f56b25a01185a3),
[RobotGui::ViewProviderTrajectory](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#a8340f50ecc730d10fae13e983317b369),
[Gui::ViewProviderPart](../../d9/d6c/classGui_1_1ViewProviderPart.html#af72e6c73209d70ff7f57643aa27adebf),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aebfd33a422ee327d6ab76c4f9ebb4b9b),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a787b6db82df30a9f214e716065bc4205),
[PartDesignGui::ViewProviderSubShapeBinder](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#a5f51564a8bdd91ee8ba79e4893016b00),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aed0d828977331c8405d16243b500b70a),
and
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a4f6059608ab3e2c0a4a98cd4699a6efd).

Referenced by
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[TechDrawGui::ViewProviderBalloon::setupContextMenu()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a565b5cb9dc2e362ef10e12bbf44a0617),
[TechDrawGui::ViewProviderDimension::setupContextMenu()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a08d18e44457f139fcb55fe8d3ea139a5),
[Gui::ViewProviderDragger::setupContextMenu()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a0e726fd7e3ac87ffba549176445ea15c),
[PartDesignGui::ViewProviderDatum::setupContextMenu()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ab1ef47ab6a3ae90671330b4a34d18bfe),
[TechDrawGui::ViewProviderPage::setupContextMenu()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a5335f8b65f3f5862801462fdc1c6a81a),
[Gui::ViewProviderTextDocument::setupContextMenu()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a5a639a77236f3bbde9daade6cf323fe8),
[PartDesignGui::ViewProvider::setupContextMenu()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aebfd33a422ee327d6ab76c4f9ebb4b9b),
and
[SketcherGui::ViewProviderSketch::setupContextMenu()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aed0d828977331c8405d16243b500b70a).

## ◆ setUpdatesEnabled()

void ViewProvider::setUpdatesEnabled  | ( | [bool](../../d9/db9/classbool.html) | _enable_| ) |   
---|---|---|---|---|---  
  
References
[setStatus()](../../d3/db3/classGui_1_1ViewProvider.html#a7a2d73b62ec2e1290f3db16c1af5e0a1),
and
[Gui::UpdateData](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ffa9867733e397c214c7d749fab0c326cf7).

## ◆ setVisible()

void ViewProvider::setVisible  | ( | [bool](../../d9/db9/classbool.html) | _s_| ) |   
---|---|---|---|---|---  
  
References
[hide()](../../d3/db3/classGui_1_1ViewProvider.html#a6ebeb34c881fe262bfa6660683b52319),
and
[show()](../../d3/db3/classGui_1_1ViewProvider.html#a8cb686581d004ed322be5af4cc876301).

Referenced by
[FemGui::TaskDlgFemConstraint::open()](../../d8/d18/classFemGui_1_1TaskDlgFemConstraint.html#aed285387fa14486ce70b705c80a02fe3),
[FemGui::TaskDlgFemConstraintContact::open()](../../db/df7/classFemGui_1_1TaskDlgFemConstraintContact.html#ae2e89ff65bd651cc5992298ff0c13f72),
[FemGui::TaskDlgFemConstraintDisplacement::open()](../../d8/d61/classFemGui_1_1TaskDlgFemConstraintDisplacement.html#a761339d7a3df143c3edb206d00839488),
[FemGui::TaskDlgFemConstraintFixed::open()](../../d6/d60/classFemGui_1_1TaskDlgFemConstraintFixed.html#a730e3071c4e5a5224961a5410c7da4ea),
[FemGui::TaskDlgFemConstraintForce::open()](../../de/d1f/classFemGui_1_1TaskDlgFemConstraintForce.html#ae8ab2031eba3cf03bedbb36ed1bd4e79),
[FemGui::TaskDlgFemConstraintHeatflux::open()](../../d3/d88/classFemGui_1_1TaskDlgFemConstraintHeatflux.html#a2d848e40dcb6f5cb3daefc7eb6c4d131),
[FemGui::TaskDlgFemConstraintInitialTemperature::open()](../../d9/d8a/classFemGui_1_1TaskDlgFemConstraintInitialTemperature.html#ac2d97a2a85e7c9d6b237d5fa80e597ef),
[FemGui::TaskDlgFemConstraintPlaneRotation::open()](../../d9/d6e/classFemGui_1_1TaskDlgFemConstraintPlaneRotation.html#ada4aaa45600edb734c91b9b8d81f8234),
[FemGui::TaskDlgFemConstraintPressure::open()](../../de/dc7/classFemGui_1_1TaskDlgFemConstraintPressure.html#a55261ba493cc5b78e55561332bc15861),
[FemGui::TaskDlgFemConstraintPulley::open()](../../db/de8/classFemGui_1_1TaskDlgFemConstraintPulley.html#a54df07217aadf8dc46360bd46e1b8360),
[FemGui::TaskDlgFemConstraintSpring::open()](../../d3/db5/classFemGui_1_1TaskDlgFemConstraintSpring.html#aac8638062d69eed86dc9cfd47dfc8717),
[FemGui::TaskDlgFemConstraintTemperature::open()](../../d6/d9f/classFemGui_1_1TaskDlgFemConstraintTemperature.html#a716c278e9c0cc35ec04ac121dfe338b4),
[FemGui::TaskDlgFemConstraintTransform::open()](../../db/dd1/classFemGui_1_1TaskDlgFemConstraintTransform.html#acd78f3e4810deca0b614cdc7508963d4),
and
[Gui::ViewProviderOrigin::setTemporaryVisibility()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#abb766d6f4587e4a16c4d929200944ca1).

## ◆ show()

| void ViewProvider::show  | ( | void  | | ) |   
---|---|---|---|---|---  
virtual  
  
Shows the view provider.

Reimplemented in
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a9474d1b5a695e58aa1d791ad79f48606),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#af89f42542c65ff6121caef78bce7c0e1),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a41516072b7f56cf582e8c638c6dcdf05),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#a8f9447ce75000777ba104a171d6f85f5),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a36f546bdabde88aa924668b9269e4716),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a3efd2508b44ff3c6c4b72336bcb10c22),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ab07df89dd5a02b97bcddef454dbbd9e5),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#abd596bd2eafad6eb412c38723c2fb972),
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae42de285d193c43881fa6019b902fec1),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#aae97a088f034e7f01fb29c28bd2b812a),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ad00aa5e18628bd79f98a81dbeebfaf5b),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a8ab74295b26124cb7d2ecd8f765ea493).

References
[setModeSwitch()](../../d3/db3/classGui_1_1ViewProvider.html#aebaedef79623db445f3ec055c365d97f).

Referenced by
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartDesignGui::ViewProvider::makeTemporaryVisible()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a91ffb650f8e0b3a88c37ab3018aa6299),
[PartGui::ViewProviderOffset::onDelete()](../../df/ded/classPartGui_1_1ViewProviderOffset.html#a58ad6004177fdd87e4c05d3ffb720ac0),
[PartGui::ViewProviderThickness::onDelete()](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#abfbe742067780f3d1ad6f4b8b8d2bc67),
[PartDesignGui::ViewProvider::onDelete()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae369224b0333fe874ef00f3a7d168fe7),
[PartGui::OffsetWidget::reject()](../../d9/d6d/classPartGui_1_1OffsetWidget.html#ab7d737c4b146e651782a10b5669b873c),
[PartGui::ThicknessWidget::reject()](../../d5/d25/classPartGui_1_1ThicknessWidget.html#a582cad61e2769aff6b8a58c38c5cd369),
[PartDesignGui::TaskDlgFeatureParameters::reject()](../../df/d42/classPartDesignGui_1_1TaskDlgFeatureParameters.html#ab22141db4eb33119ad64ed387063f830),
[PartDesignGui::TaskDlgSketchBasedParameters::reject()](../../da/def/classPartDesignGui_1_1TaskDlgSketchBasedParameters.html#af410e02c04329e37c65f34452f4ce972),
[PartGui::DlgFilletEdges::setupFillet()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a1276cdf00c4f3436317932a8da913a5e),
[setVisible()](../../d3/db3/classGui_1_1ViewProvider.html#a839be69bcafa02679cfa0881b09cc5ed),
[Gui::ViewProviderDocumentObject::show()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae42de285d193c43881fa6019b902fec1),
[Mod.Show.mTempoVis.TempoVis::show_all_dependencies()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a7ccd7b0b980b37bc61025400bcddc632),
[Mod.Show.mTempoVis.TempoVis::show_all_dependent()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#aebdf1f88e101dc1a927b20477f6e5730),
[Gui::Application::showViewProvider()](../../d9/da8/classGui_1_1Application.html#a874e12dc7720809f998b88844bc9f5f0),
[update()](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8),
and
[Gui::ViewProviderDocumentObject::updateView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae31dde44f114d3e90bb2e1d544f3e442).

## ◆ showInTree()

| virtual [bool](../../d9/db9/classbool.html) Gui::ViewProvider::showInTree  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Tell the tree view if this object should appear there.

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7a74cd8717daf43e557ee87654f4d7a).

## ◆ startEditing()

| [ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html) * ViewProvider::startEditing  | ( | [int](../../d1/da0/classint.html) | _ModNum_ = `0`| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#aa784b328fb67782acbe474a4bf1ccafa),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a180f1f91d3c234cdab76c3b3f4d71946),
and
[PartDesignGui::ViewProviderTransformed](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#aca65c3594f90b54775e4c73ededd1ffc).

References
[setEdit()](../../d3/db3/classGui_1_1ViewProvider.html#a99bfa17a3eedcec978d56b252a653fea).

Referenced by
[draftguitools.gui_edit.Edit::mousePressed()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#acb63bdf517177a4e38d5b6abe23e56f6),
[SpreadsheetGui::ViewProviderSheet::showSpreadsheetView()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a912de2c5ce615efc6d1e3f70f3674f1b),
[Gui::ViewProviderLink::startEditing()](../../d6/d59/classGui_1_1ViewProviderLink.html#aa784b328fb67782acbe474a4bf1ccafa),
[Gui::ViewProviderDragger::startEditing()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a180f1f91d3c234cdab76c3b3f4d71946),
and
[PartDesignGui::ViewProviderTransformed::startEditing()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#aca65c3594f90b54775e4c73ededd1ffc).

## ◆ testStatus()

[bool](../../d9/db9/classbool.html) Gui::ViewProvider::testStatus  | ( | [ViewStatus](../../d9/dad/namespaceGui.html#aa5a2a141f29bd3bbe36050bcec7bb6ff) | _pos_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Gui::ViewProviderDocumentObject::isAttachedToDocument()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a162f664e8fe151ffa44f77b0bd34877d),
[isUpdatesEnabled()](../../d3/db3/classGui_1_1ViewProvider.html#aad2c2352ff074e6049c65190a2ad908d),
[Gui::ViewProviderDocumentObject::onChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ac7163501426771c94bb2026224ec94d8),
[PartGui::ViewProviderPartExt::setHighlightedEdges()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a8a3906f845faf45e648ef05e1bc6fa45),
[PartGui::ViewProviderPartExt::setHighlightedFaces()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ae3121cead5ae89980439ae2b9dfe4b3a),
[PartGui::ViewProviderPartExt::setHighlightedPoints()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a6158c410a40ace62d95eabaddf942d9b),
and
[Gui::ViewProviderDocumentObject::updateView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae31dde44f114d3e90bb2e1d544f3e442).

## ◆ toString()

std::string ViewProvider::toString  | ( | | ) |  const  
---|---|---|---|---  
  
References
[pcRoot](../../d3/db3/classGui_1_1ViewProvider.html#ad145dceec172bd73c1d91cb4c916889e),
and
[Gui::SoFCDB::writeNodesToString()](../../d3/d6d/classGui_1_1SoFCDB.html#ace7b94c6c19aebc4cfcb7221366eecec).

## ◆ unsetEdit()

| void ViewProvider::unsetEdit  | ( | [int](../../d1/da0/classint.html) | _ModNum_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
is called when you lose the edit mode

Reimplemented in
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a5da12856b6d51ceac16b21fb5a5fa94d),
[FemGui::ViewProviderFemAnalysis](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a9f65e612e7e3003356e56502fd78dd69),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a3be2fba780c90af8f5fbabebb8d93e36),
[FemGui::ViewProviderFemPostFunction](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#ae27715adf749293e9c3e8553a073b048),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a146e2491fea7a549ca2f1302397c6093),
[FemGui::ViewProviderSetElements](../../dd/d62/classFemGui_1_1ViewProviderSetElements.html#a824332264c7eb0a1c68d7856c39447c1),
[FemGui::ViewProviderSetFaces](../../d9/d46/classFemGui_1_1ViewProviderSetFaces.html#a96e4fbfb3ecaa20b0ea59008e6ef6d40),
[FemGui::ViewProviderSetGeometry](../../dd/d48/classFemGui_1_1ViewProviderSetGeometry.html#ad7b782ade9cf93a512ce006a54cbb53d),
[FemGui::ViewProviderSetNodes](../../d5/d44/classFemGui_1_1ViewProviderSetNodes.html#a6786e9289c1b140de34fd6184b079791),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a332d4d8e0dc32e9415ac6fb296bbd97f),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a036451869ccec14b115760e67eeea52a),
[PartGui::ViewProviderCurveNet](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#a944f115778659ff742771d5caf9e726a),
[PartGui::ViewProviderImport](../../d0/d76/classPartGui_1_1ViewProviderImport.html#a1f7384baeec15b760192ad1bad73fd50),
[PartGui::ViewProviderMirror](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a72ba82b453ad60568eb3bd6aa7a518f0),
[PartGui::ViewProviderFillet](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a403c40596d10cd796293baa5c63baf0a),
[PartGui::ViewProviderChamfer](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a9c31f769d348817db15656c769b2731b),
[PartGui::ViewProviderOffset](../../df/ded/classPartGui_1_1ViewProviderOffset.html#a56addcc98c66943c7d3db752cc343568),
[PartGui::ViewProviderThickness](../../d1/d8f/classPartGui_1_1ViewProviderThickness.html#a3a6f622621c73eca40725cd39f7ee095),
[PartGui::ViewProviderPrimitive](../../dd/dfd/classPartGui_1_1ViewProviderPrimitive.html#a75517b8bac95d56cf8c249ca5a67b568),
[PartDesignGui::ViewProviderBase](../../d7/d54/classPartDesignGui_1_1ViewProviderBase.html#a428b3c775921ead1b1d7ece27fc43250),
[PartDesignGui::ViewProviderHelix](../../da/d62/classPartDesignGui_1_1ViewProviderHelix.html#ad60273f3cc3ff7698e6a3e853891735b),
[PartDesignGui::ViewProviderLoft](../../d9/d6e/classPartDesignGui_1_1ViewProviderLoft.html#a335ff8a7a3331e4cbfa110fc6242853d),
[PartDesignGui::ViewProviderPipe](../../d8/dc8/classPartDesignGui_1_1ViewProviderPipe.html#ab1d0cc502b695892c104af8ae2caadd2),
[PartDesignGui::ViewProviderPrimitive](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a75517b8bac95d56cf8c249ca5a67b568),
[PathGui::ViewProviderPathCompound](../../db/d9a/classPathGui_1_1ViewProviderPathCompound.html#aadd896bb7059bfb27dcc21f83914d607),
[PointsGui::ViewProviderPoints](../../d2/d23/classPointsGui_1_1ViewProviderPoints.html#a1820f7628e20ae7f37a79fdbf8792f3e),
[RaytracingGui::ViewProviderLux](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a42c55d3c8618ed9908a5def744f01b70),
[RaytracingGui::ViewProviderPovray](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a77847b6dd898624e4806deb6b4941718),
[RobotGui::ViewProviderEdge2TracObject](../../da/d5e/classRobotGui_1_1ViewProviderEdge2TracObject.html#ae5f4248d2a7ff9fa7373c10697db9723),
[RobotGui::ViewProviderTrajectoryCompound](../../d7/d47/classRobotGui_1_1ViewProviderTrajectoryCompound.html#a18cc53ffaea8a351fbd683918edf799a),
[RobotGui::ViewProviderTrajectoryDressUp](../../da/dff/classRobotGui_1_1ViewProviderTrajectoryDressUp.html#a1aa0a912368776c84b78358ad582bd66),
[SurfaceGui::ViewProviderFilling](../../d0/dac/classSurfaceGui_1_1ViewProviderFilling.html#a21fb8f85ca607774e759a2200af87669),
[SurfaceGui::ViewProviderGeomFillSurface](../../d8/d03/classSurfaceGui_1_1ViewProviderGeomFillSurface.html#adb425599ac4406a2fd7f716be219fb17),
[SurfaceGui::ViewProviderSections](../../da/dd0/classSurfaceGui_1_1ViewProviderSections.html#aa9fe2b7475ec78d7b399662c37741141),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a47878ef47453b5c80f8cc349d74700ba),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a6b5421ab614cca1db003bc21841b57c4),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#ad585848d8d7ce594b4508554857e5007),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#aad88c0e3dbf5636191db38253b4ff384),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a0b210e9314969058a242d2833a6be43d),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a354a767468724014a76652bdc6353288),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#af9970c81f0210dbc28a8e16b221e475b),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a458108c8e54b6e489391d842e0e3b328),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#aacf8ca54345033451026bd7f6483d1af),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a10c5a11ef248cd9364b99efeb6f1ac33),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a8660f36b79b9cf2692dcd696878e6789),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aeb01bc367ec2895032e0fcd1074528fb),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#acae565f87c877586b89508ebdb95f199),
[PartDesignGui::ViewProviderShapeBinder](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a4a6159366da16ea7e7337a4078b3a5d8),
[PartDesignGui::ViewProviderTransformed](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a30b1e3fa317ddd2654853040be2f94d9),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a292cf2c15b300787b74fa8b2bc248388),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#aeea46b7057bc891730a4570b9218c7c7),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#ae6d12522555f900df50515afb5dbb2ac),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a5dbad13a97973b5844de4c77490e9887),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#adb66d38ffbf8b0883b835a59efee33a6),
and
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a23586e7d84815fe353d6a5f73c7d4ef4).

Referenced by
[finishEditing()](../../d3/db3/classGui_1_1ViewProvider.html#ae3a70413039e06002dd1875fa9595ecb),
[PathScripts.PathJobGui.ViewProvider::uneditObject()](../../d3/d3e/classPathScripts_1_1PathJobGui_1_1ViewProvider.html#aa663c276d96715669b3d07c7d2e34790),
[FemGui::ViewProviderFemAnalysis::unsetEdit()](../../d7/d81/classFemGui_1_1ViewProviderFemAnalysis.html#a9f65e612e7e3003356e56502fd78dd69),
and
[TechDrawGui::ViewProviderDrawingView::unsetEdit()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#aeea46b7057bc891730a4570b9218c7c7).

## ◆ unsetEditViewer()

| void ViewProvider::unsetEditViewer  | ( | [View3DInventorViewer](../../d5/d29/classGui_1_1View3DInventorViewer.html) *  | | ) |   
---|---|---|---|---|---  
virtual  
  
restores viewer settings when leaving editing mode

Reimplemented in
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a0fed482e445d662b1ab784c89d54ef8f),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a139b6c22fd8be484d76a6eca106a3984),
and
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a597f850ded2ad26d7f676088f43157cc).

Referenced by
[Gui::View3DInventorViewer::resetEditingViewProvider()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a94d416fa9d5e705fdf6bb89cc467739a).

## ◆ update()

| void ViewProvider::update  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
virtual  
  
update the content of the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...") this method have to implement the recalculation of the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...").

There are different reasons to update. E.g. only the view attribute has
changed, or the data has manipulated.

Reimplemented in
[Gui::ViewProviderDocumentObject](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a6e0dd163d7555c35d78c29a504c0b2ce).

References
[hide()](../../d3/db3/classGui_1_1ViewProvider.html#a6ebeb34c881fe262bfa6660683b52319),
[isShow()](../../d3/db3/classGui_1_1ViewProvider.html#a002feec6611feb7ea07be1878a5864a3),
[isUpdatesEnabled()](../../d3/db3/classGui_1_1ViewProvider.html#aad2c2352ff074e6049c65190a2ad908d),
[show()](../../d3/db3/classGui_1_1ViewProvider.html#a8cb686581d004ed322be5af4cc876301),
and
[updateData()](../../d3/db3/classGui_1_1ViewProvider.html#a84b28e19898179755940c2b77e03b56a).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchAxisSystem.AxisSystemTaskPanel::addElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a68544065aac91fa78a8bddb3e6ed5a99),
[ArchComponent.ComponentTaskPanel::addElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#a21a385085defc9e8ccca8b2261a57314),
[ArchSectionPlane.SectionPlaneTaskPanel::addElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a6317c0ca7eb0c28e60b863f96ddeb81f),
[DraftGui.FacebinderTaskPanel::addElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a7642fdc6d6fa90afec25930af3b0a66e),
[femtaskpanels.task_result_mechanical._TaskPanel::calculate()](../../d1/d11/classfemtaskpanels_1_1task__result__mechanical_1_1__TaskPanel.html#aa2b98b5a9e12d62038ea9cc00366ecb6),
[Spreadsheet_legacy.SpreadsheetView::changeCell()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a897cda21a4a4f34431c371a31579706e),
[draftguitools.gui_edit.Edit::endEditing()](../../d8/d68/classdraftguitools_1_1gui__edit_1_1Edit.html#ab9797631ba43c7855016e2552c21834f),
[draftguitools.gui_trackers.boxTracker::height()](../../d5/dca/classdraftguitools_1_1gui__trackers_1_1boxTracker.html#a25f7d7bbd56b5ff5ef5da124e515dd00),
[draftguitools.gui_trackers.rectangleTracker::p3()](../../d7/d8d/classdraftguitools_1_1gui__trackers_1_1rectangleTracker.html#a1bf47cdde1ea165a58946f1a5fdc6c8e),
[Plot.Plot::plot()](../../d3/d54/classPlot_1_1Plot.html#a8b670f38324a7fae1c7128e117cba688),
[Spreadsheet_legacy.SpreadsheetView::recompute()](../../d7/d03/classSpreadsheet__legacy_1_1SpreadsheetView.html#a1d8b8256ad183347aedaf40a269c2d3a),
[ArchAxisSystem.AxisSystemTaskPanel::removeElement()](../../dd/d11/classArchAxisSystem_1_1AxisSystemTaskPanel.html#a27e3fe8ffbc52acfd92f2d333626a76d),
[ArchComponent.ComponentTaskPanel::removeElement()](../../dd/d1d/classArchComponent_1_1ComponentTaskPanel.html#ad9d18ffd3ef7556affab6b62a6acceb5),
[ArchSectionPlane.SectionPlaneTaskPanel::removeElement()](../../d5/d70/classArchSectionPlane_1_1SectionPlaneTaskPanel.html#a544dbf3def03e06b86e6f32c390fd46a),
[DraftGui.FacebinderTaskPanel::removeElement()](../../d2/d61/classDraftGui_1_1FacebinderTaskPanel.html#a8ce5c644e81d1fbb3907e351e2050a0a),
[draftguitools.gui_trackers.gridTracker::reset()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a2c6f7e1d0a817adacef8297962691a9c),
[ArchNesting.Nester::run()](../../d0/df4/classArchNesting_1_1Nester.html#af4bd331488aca3d29d5ade158e30b102),
[draftguitools.gui_trackers.gridTracker::setMainlines()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#ac1c96a4a6282724211bc61a37ffa5a05),
[draftguitools.gui_trackers.gridTracker::setSize()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a6bb2d86a97781159c083a23a30f9fb9a),
[draftguitools.gui_trackers.gridTracker::setSpacing()](../../d5/d75/classdraftguitools_1_1gui__trackers_1_1gridTracker.html#a67fe5637d9f2b95d4c6c6a717f41e6e4),
[Gui::Document::slotChangedObject()](../../de/d4e/classGui_1_1Document.html#a3886f48ebea3c1a519f8f0f1cf3f9d3e),
[Gui::ViewProviderDocumentObject::update()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a6e0dd163d7555c35d78c29a504c0b2ce),
and
[draftguitools.gui_edit_arch_objects.ArchWallGuiTools::update_object_from_edit_points()](../../d1/d46/classdraftguitools_1_1gui__edit__arch__objects_1_1ArchWallGuiTools.html#a1340bdc87e40eb0a04ba856255ae0f93).

## ◆ updateData()

| void ViewProvider::updateData  | ( | const [App::Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_| ) |   
---|---|---|---|---|---  
virtual  
  
Reimplemented in
[Gui::ViewProviderAnnotation](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#acaee4ade8605ecc0ce997f273a931986),
[Gui::ViewProviderAnnotationLabel](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#aa2e79cd63adfc0a43501b66ffa4438dd),
[Gui::ViewProviderExtern](../../dd/d9c/classGui_1_1ViewProviderExtern.html#a94e36903a60cf12174a60243ba1896b8),
[Gui::ViewProviderGeometryObject](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a4818bdc22e4b19444d703d72bec9d7ca),
[Gui::ViewProviderInventorObject](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[Gui::ViewProviderOriginFeature](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#a68bb661a5e0c565c16b2790d875cb6ce),
[Gui::ViewProviderVRMLObject](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a333658725d74f95a0e3ff3ed6110bce8),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#a4b29dd7d5bedeed637c250a09213c487),
[FemGui::ViewProviderFemConstraintBearing](../../d1/d76/classFemGui_1_1ViewProviderFemConstraintBearing.html#a3b3cf2fa05760751890d9e1cf51f178f),
[FemGui::ViewProviderFemConstraintContact](../../d9/d3d/classFemGui_1_1ViewProviderFemConstraintContact.html#a3ecf76e65206672a9355c60a533550c8),
[FemGui::ViewProviderFemConstraintDisplacement](../../d7/d3f/classFemGui_1_1ViewProviderFemConstraintDisplacement.html#afb4b851d45e12b8639d1c4bedcaba4db),
[FemGui::ViewProviderFemConstraintFixed](../../d4/d9c/classFemGui_1_1ViewProviderFemConstraintFixed.html#ab0717083d8637965bcafa54bfd839893),
[FemGui::ViewProviderFemConstraintFluidBoundary](../../da/d06/classFemGui_1_1ViewProviderFemConstraintFluidBoundary.html#a4d504b5a6630b9045bf605a95bc6aafb),
[FemGui::ViewProviderFemConstraintForce](../../da/dc5/classFemGui_1_1ViewProviderFemConstraintForce.html#ad691cf23756106d6b0ea043ddebd1b94),
[FemGui::ViewProviderFemConstraintGear](../../d1/d2f/classFemGui_1_1ViewProviderFemConstraintGear.html#a56f097a322b6fe5b2b4b7eead3374c49),
[FemGui::ViewProviderFemConstraintHeatflux](../../d0/dea/classFemGui_1_1ViewProviderFemConstraintHeatflux.html#a3f1a55d2e70a5dca6b97d52c3e103aa0),
[FemGui::ViewProviderFemConstraintInitialTemperature](../../d8/d07/classFemGui_1_1ViewProviderFemConstraintInitialTemperature.html#a22121300d25709afab92e6b6c131f12c),
[FemGui::ViewProviderFemConstraintPlaneRotation](../../d7/d0a/classFemGui_1_1ViewProviderFemConstraintPlaneRotation.html#a2b385e8a4903df418ef331257ad13a64),
[FemGui::ViewProviderFemConstraintPressure](../../d4/d18/classFemGui_1_1ViewProviderFemConstraintPressure.html#a0280a478dea5288d50ba390ed1a50ca7),
[FemGui::ViewProviderFemConstraintPulley](../../d8/dfc/classFemGui_1_1ViewProviderFemConstraintPulley.html#a7ba40d63d4dff464026a808438d3630b),
[FemGui::ViewProviderFemConstraintSpring](../../d5/d4f/classFemGui_1_1ViewProviderFemConstraintSpring.html#a44c1119dd7d0bef3d9ef9c3229057e53),
[FemGui::ViewProviderFemConstraintTemperature](../../d1/df6/classFemGui_1_1ViewProviderFemConstraintTemperature.html#a4c6f2f24780c8171d293ec933ae942ac),
[FemGui::ViewProviderFemConstraintTransform](../../db/d32/classFemGui_1_1ViewProviderFemConstraintTransform.html#a2adf8aba7f15f7b95399068ab39c47b8),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a2b42be80762272d7f6be0b30e7d6a3f5),
[FemGui::ViewProviderFemMeshShapeNetgen](../../df/db3/classFemGui_1_1ViewProviderFemMeshShapeNetgen.html#a30b8650c623117ac70a0585240e76ba8),
[FemGui::ViewProviderFemPostFunctionProvider](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a97688d1ce128f8dd922c10533f41d061),
[FemGui::ViewProviderFemPostPlaneFunction](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[FemGui::ViewProviderFemPostSphereFunction](../../d4/da4/classFemGui_1_1ViewProviderFemPostSphereFunction.html#a9fac4b851c890977a0c56223e6dcf40d),
[FemGui::ViewProviderFemPostObject](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#a70dda6c85f13bcb560d19bfcdd68be17),
[ImageGui::ViewProviderImagePlane](../../db/d5a/classImageGui_1_1ViewProviderImagePlane.html#ae91df03af7efab412ed649b8db50463e),
[InspectionGui::ViewProviderInspection](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#acfabc68fbd4cb6188071e498739066d8),
[MeshGui::ViewProviderIndexedFaceSet](../../d8/d12/classMeshGui_1_1ViewProviderIndexedFaceSet.html#a18d4f21152ed2f96bfcec096aa0e639c),
[MeshGui::ViewProviderMeshObject](../../db/d49/classMeshGui_1_1ViewProviderMeshObject.html#ab567af502db9d5a8e0beba2181fb39b3),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033),
[MeshGui::ViewProviderMeshFaceSet](../../df/de9/classMeshGui_1_1ViewProviderMeshFaceSet.html#a1a79e8c47f1e048e3027f7908856d85f),
[MeshGui::ViewProviderMeshNode](../../dc/d89/classMeshGui_1_1ViewProviderMeshNode.html#a1f842f4aab9c6924fa2390d536ad571e),
[MeshGui::ViewProviderMeshTransform](../../d2/d2b/classMeshGui_1_1ViewProviderMeshTransform.html#a33448b7e01bdff92e71496a98ccef39a),
[MeshPartGui::ViewProviderCrossSections](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#ab80442b7cbfc2de66b5914468279d003),
[PartGui::ViewProviderCrossSections](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#a7143081db3a8d22e8df2ec7663810561),
[PartGui::ViewProvider2DObjectGrid](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a90b368f7f4f6e6a9a2806ccbeef15a1f),
[PartGui::ViewProviderBoolean](../../df/dcc/classPartGui_1_1ViewProviderBoolean.html#ae38d6575df4dd650428a3d5873874d94),
[PartGui::ViewProviderMultiFuse](../../db/d93/classPartGui_1_1ViewProviderMultiFuse.html#a2dd30d90dd627899aae55dd7f6082bfd),
[PartGui::ViewProviderMultiCommon](../../db/daf/classPartGui_1_1ViewProviderMultiCommon.html#afd2565caa649c9122a8da1bad7217b88),
[PartGui::ViewProviderCompound](../../d1/d39/classPartGui_1_1ViewProviderCompound.html#a864f55403bd4a3b5a81834205fe9561d),
[PartGui::ViewProviderCurveNet](../../d9/d90/classPartGui_1_1ViewProviderCurveNet.html#ac10fc8ddaf0e0f8b4fed8ed9f957073a),
[PartGui::ViewProviderFillet](../../de/dd4/classPartGui_1_1ViewProviderFillet.html#a681e5f4afcfbf90240da46de01068325),
[PartGui::ViewProviderChamfer](../../db/d6b/classPartGui_1_1ViewProviderChamfer.html#a33e0d402eb35a8d3bf589039003c4f0d),
[PartGui::ViewProviderCustom](../../d5/d45/classPartGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[PartGui::ViewProviderPartReference](../../d8/df3/classPartGui_1_1ViewProviderPartReference.html#a4184f94dd00fa6c204fe4880c1fcd541),
[PartGui::ViewProviderRuledSurface](../../d3/d74/classPartGui_1_1ViewProviderRuledSurface.html#af8ea975ad249bc60db35caf151b9908b),
[PartDesignGui::ViewProviderAddSub](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#a673c166a604d568484431b0270c168e3),
[PartDesignGui::ViewProviderDatumCoordinateSystem](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a4ab1e86010986173acb70e3476f46a36),
[PartDesignGui::ViewProviderDatumLine](../../d8/d91/classPartDesignGui_1_1ViewProviderDatumLine.html#a7ebcf854d3c32486f47eb377a39f4fa7),
[PartDesignGui::ViewProviderDatumPlane](../../da/dc4/classPartDesignGui_1_1ViewProviderDatumPlane.html#a0a10ea46fffce183ae92074bd2c6d754),
[PartDesignGui::ViewProviderPrimitive](../../d9/d7a/classPartDesignGui_1_1ViewProviderPrimitive.html#a463587fc3ef266044d94f23277c990d0),
[PathGui::ViewProviderArea](../../d3/d66/classPathGui_1_1ViewProviderArea.html#a33f43f1d72596152fa4d6944b59360b0),
[PathGui::ViewProviderAreaView](../../dc/d0c/classPathGui_1_1ViewProviderAreaView.html#a5681f9ff35ad2a07e43b5847ebe09f15),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#abf0eee82b2cd3fd757ebec5feb95b8ed),
[PathGui::ViewProviderPathShape](../../d9/d9e/classPathGui_1_1ViewProviderPathShape.html#ac696ef550f0e27b0665de391ca5891a9),
[PointsGui::ViewProviderScattered](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab2bc3db5bc92357f983d5c88d287df35),
[PointsGui::ViewProviderStructured](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#afdfd3564ae817f52b13b4ba6f6e093e8),
[RobotGui::ViewProviderRobotObject](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#a3d13aa6f344faf42bd42462a781c2747),
[RobotGui::ViewProviderTrajectory](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#a653032eb34a2fc66e326c0d0e9066287),
[SketcherGui::ViewProviderCustom](../../d9/d6b/classSketcherGui_1_1ViewProviderCustom.html#af15253579cb4a1c9b7d7c06e87a02c7e),
[TechDrawGui::ViewProviderAnnotation](../../d8/dd5/classTechDrawGui_1_1ViewProviderAnnotation.html#acaee4ade8605ecc0ce997f273a931986),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#ad01f0112c0c9c05c28063d4ca902d127),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a67972f9204e723e1b39e2d561e12b347),
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#ab3b620cbd5661705ba1b675a9f1c3ea5),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a9885aee56382e6ad1e6e69b583197aa1),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a0b73a2cf555b860a1fd6dc0749eceb1d),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#aa193f03d76fb1ecdf199186e888354ce),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a4e1c30466784136f53ab33c2cdee4b16),
[TechDrawGui::ViewProviderSpreadsheet](../../d1/d67/classTechDrawGui_1_1ViewProviderSpreadsheet.html#abfea73ebb287277b0b3cfe4fa092f99b),
[TechDrawGui::ViewProviderSymbol](../../da/de5/classTechDrawGui_1_1ViewProviderSymbol.html#aa09633150b91b1f929553e9fb6f901da),
[TechDrawGui::ViewProviderTile](../../d1/daa/classTechDrawGui_1_1ViewProviderTile.html#a2661f79de8d7be35706b9397dcdfc260),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a973e2df5e757b16a3117e897301f5014),
[TechDrawGui::ViewProviderViewSection](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#ac083e7ff9d0e7109ffab541011348f34),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#ae01697f9c3d9dad3a8dad2aa62953f9a),
[Gui::ViewProviderDragger](../../d3/d04/classGui_1_1ViewProviderDragger.html#a6d433c9fe9d47fa7ab9be6d7e01d6509),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#a73f73f368cb176bf9a7f2371e4e9ec93),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#aeed0fe8c30da98ed16d079df09d8750f),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a5e0cc45b4148eee1b13cc43e9ff2518c),
[PartDesignGui::ViewProvider](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ae230b789ddc5d513656f4e87964bd01e),
[SketcherGui::ViewProviderSketch](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aa3039dd97c10d7c17a0c9e193ff059f4),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#adbe2a0c702e5a933b6b6464684e1f3da),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a5d606c0b642371b2f41a07cc1d80d9b8),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a8c1850a8463be2485aad3fbfbe06b59a),
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#af08c8e552302f0c07734e06211b6fb17),
[FemGui::ViewProviderFemConstraint](../../d7/dc7/classFemGui_1_1ViewProviderFemConstraint.html#a8d3f57e3986857c2cf91396ed274fe84),
[FemGui::ViewProviderFemPostPipeline](../../df/d95/classFemGui_1_1ViewProviderFemPostPipeline.html#af073f80f627dfd4185dd1db10d56e79b),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#ab549ff4e3d3f11a40457044cbb1b158f),
[PartDesignGui::ViewProviderBody](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a2a541fb893a7130314f3c7161c33477e),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a07759d29f22334536525b21068241ab3),
and
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac28b3c92f87b718452fddd90fe4f2f4f).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[PathScripts.PathJobDlg.JobCreate::exec_()](../../df/d6d/classPathScripts_1_1PathJobDlg_1_1JobCreate.html#a3949bbe83170d8e065b74724bcde9e2a),
[draftviewproviders.view_dimension.ViewProviderLinearDimension::onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension::onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[draftviewproviders.view_wire.ViewProviderWire::onChanged()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a45511b113b62eba083c491b40c7fe3e8),
[PathScripts.PathOpGui.TaskPanelPage::pageUpdateData()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#ac7aeda3cf19b74fa6d6a620db8140a66),
[PathScripts.PathPropertyBagGui.TaskPanel::setupUi()](../../d3/d93/classPathScripts_1_1PathPropertyBagGui_1_1TaskPanel.html#a0e7d9c2f42ae50ec45505059011deba5),
[PathScripts.PathSetupSheetGui.OpTaskPanel::setupUi()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a03e427ec6574bd249d859f5bd2496576),
[update()](../../d3/db3/classGui_1_1ViewProvider.html#abe1fb2bbe6e5b05d95bb6dc9798016d8),
[Gui::ViewProviderAnnotation::updateData()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#acaee4ade8605ecc0ce997f273a931986),
[Gui::ViewProviderAnnotationLabel::updateData()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#aa2e79cd63adfc0a43501b66ffa4438dd),
[Gui::ViewProviderMeasureDistance::updateData()](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a260762ea126ca4a70b60e5a825f2448d),
[DrawingGui::ViewProviderDrawingPage::updateData()](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a885c2ea64eae6ad57aeed5d42a1a05dd),
[FemGui::ViewProviderFemPostFunctionProvider::updateData()](../../df/d22/classFemGui_1_1ViewProviderFemPostFunctionProvider.html#a97688d1ce128f8dd922c10533f41d061),
[FemGui::ViewProviderFemPostPlaneFunction::updateData()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#a6ec898b1ee3b9ae2983c1f424b2a55f4),
[FemGui::ViewProviderFemPostSphereFunction::updateData()](../../d4/da4/classFemGui_1_1ViewProviderFemPostSphereFunction.html#a9fac4b851c890977a0c56223e6dcf40d),
[TechDrawGui::ViewProviderBalloon::updateData()](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#ad01f0112c0c9c05c28063d4ca902d127),
[TechDrawGui::ViewProviderDimension::updateData()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a67972f9204e723e1b39e2d561e12b347),
[TechDrawGui::ViewProviderProjGroupItem::updateData()](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#aa193f03d76fb1ecdf199186e888354ce),
[Gui::ViewProviderDragger::updateData()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a6d433c9fe9d47fa7ab9be6d7e01d6509),
[Gui::ViewProviderLink::updateData()](../../d6/d59/classGui_1_1ViewProviderLink.html#a73f73f368cb176bf9a7f2371e4e9ec93),
[TechDrawGui::ViewProviderDrawingView::updateData()](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#adbe2a0c702e5a933b6b6464684e1f3da),
[TechDrawGui::ViewProviderGeomHatch::updateData()](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a5d606c0b642371b2f41a07cc1d80d9b8),
[TechDrawGui::ViewProviderHatch::updateData()](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#a8c1850a8463be2485aad3fbfbe06b59a),
[TechDrawGui::ViewProviderTemplate::updateData()](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#af08c8e552302f0c07734e06211b6fb17),
[TechDrawGui::ViewProviderPage::updateData()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac28b3c92f87b718452fddd90fe4f2f4f),
and
[Gui::ViewProviderDocumentObject::updateView()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#ae31dde44f114d3e90bb2e1d544f3e442).

## ◆ useNewSelectionModel()

| [bool](../../d9/db9/classbool.html) ViewProvider::useNewSelectionModel  | ( | void  | | ) |  const  
---|---|---|---|---|---  
virtual  
  
indicates if the [ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html
"General interface for all visual stuff in FreeCAD This class is used to
generate and handle all aroun...") use the new Selection model

Reimplemented in
[MeshGui::ViewProviderMesh](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af6bb580195ab0a211113b8922ff7e22d),
[MeshGui::ViewProviderMeshCurvature](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a42d8803b1c27c55e82cab2c16a9680c7),
[Gui::ViewProviderInventorObject](../../de/ded/classGui_1_1ViewProviderInventorObject.html#a24931958eb1a4c13acb22795d5b24481),
[Gui::ViewProviderMeasureDistance](../../dd/d89/classGui_1_1ViewProviderMeasureDistance.html#a14fa60c926b9fc0d32d3c78b52b9b64d),
[DrawingGui::ViewProviderDrawingPage](../../d7/d4d/classDrawingGui_1_1ViewProviderDrawingPage.html#a9c3249b8f850045beaab200b8f4334db),
[DrawingGui::ViewProviderDrawingView](../../d2/dce/classDrawingGui_1_1ViewProviderDrawingView.html#a4a5e1541e00ee8d3dfcd2d7fc686ce6c),
[DrawingGui::ViewProviderDrawingClip](../../d3/d00/classDrawingGui_1_1ViewProviderDrawingClip.html#ae24bea298375001ab3db8f8bd96db248),
[FemGui::ViewProviderFemMesh](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a12952e9235633e520260201e848f5c85),
[PathGui::ViewProviderPath](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac4369bd741dd06af6966ed030a18d363),
[TechDrawGui::ViewProviderAnnotation](../../d8/dd5/classTechDrawGui_1_1ViewProviderAnnotation.html#ac80f0bdcf389f292be2e47d55700d88d),
[TechDrawGui::ViewProviderBalloon](../../d2/dd9/classTechDrawGui_1_1ViewProviderBalloon.html#a40fb4a5be226d528b0dead19f241cdea),
[TechDrawGui::ViewProviderDimension](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a4f41a66662f3cb4dc739d9d9cf739c04),
[TechDrawGui::ViewProviderImage](../../d3/d5b/classTechDrawGui_1_1ViewProviderImage.html#a3ce1c50e1f918b1b6383dfa344820b9d),
[TechDrawGui::ViewProviderLeader](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#aa2d1e598de077239d7b060321f6a3d06),
[TechDrawGui::ViewProviderProjGroup](../../d6/dc7/classTechDrawGui_1_1ViewProviderProjGroup.html#a524efe274cb762bfca03f36a27d1174b),
[TechDrawGui::ViewProviderProjGroupItem](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#a1a871afae6935262b5b0a03890909673),
[TechDrawGui::ViewProviderRichAnno](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#a1643c2e6be05bdb3fd4889e9f5079bc4),
[TechDrawGui::ViewProviderSpreadsheet](../../d1/d67/classTechDrawGui_1_1ViewProviderSpreadsheet.html#a0557f53d17f32c329b7ea69fdded393a),
[TechDrawGui::ViewProviderSymbol](../../da/de5/classTechDrawGui_1_1ViewProviderSymbol.html#a4785584ca243b5783767399339b19796),
[TechDrawGui::ViewProviderTile](../../d1/daa/classTechDrawGui_1_1ViewProviderTile.html#a0c3314dcdb7f023b27a66eeaedd1658d),
[TechDrawGui::ViewProviderViewClip](../../d1/dc2/classTechDrawGui_1_1ViewProviderViewClip.html#ad521b3d3eb238430fb32a9d564ecac1c),
[TechDrawGui::ViewProviderViewPart](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aa5a1a83ac4c612c9963962c320bcb22d),
[TechDrawGui::ViewProviderWeld](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a004be5d8ae25d17b3dca335689fb7ee8),
[Gui::ViewProviderLink](../../d6/d59/classGui_1_1ViewProviderLink.html#ab056943a6295ef043dcdaf7c726d06e4),
[Gui::ViewProviderPlacement](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a0a6768e6eca62963c64e337b61a015be),
[PartGui::ViewProviderPartExt](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#af9061f539a0e8e14e1c83c349b22c59a),
[PartDesignGui::ViewProviderDatum](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#a688bafdc047c07b45573a109704eada1),
[SpreadsheetGui::ViewProviderSheet](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a294aaf1faa8e7e93d078b4cecbd767fe),
[TechDrawGui::ViewProviderDrawingView](../../db/d6f/classTechDrawGui_1_1ViewProviderDrawingView.html#acd6e257a4a5837cc91dfaa329d72ca40),
[TechDrawGui::ViewProviderGeomHatch](../../db/dbe/classTechDrawGui_1_1ViewProviderGeomHatch.html#a2979504b5665029ac7a12101e0c2f980),
[TechDrawGui::ViewProviderHatch](../../de/d1a/classTechDrawGui_1_1ViewProviderHatch.html#af60995c49e0ed0cda81f7fe537218a15),
[TechDrawGui::ViewProviderPage](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac5695a85ccdd5172152956d58166d5ab),
and
[TechDrawGui::ViewProviderTemplate](../../dc/d9b/classTechDrawGui_1_1ViewProviderTemplate.html#a5df89d98d7b94093cfa81e40585838a1).

References
[Gui::ViewParams::instance()](../../d3/d88/classGui_1_1ViewParams.html#ad2e358ade7b93b19ca41aef23fa30459).

Referenced by
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
and
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1).

## Member Data Documentation

## ◆ overrideMode

| std::string Gui::ViewProvider::overrideMode  
---  
protected  
  
Referenced by
[getOverrideMode()](../../d3/db3/classGui_1_1ViewProvider.html#a851989cf62aaf94cc05f6f24a44fbe8a),
[PartDesignGui::ViewProviderBody::onChanged()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#adf615077f77d932ed33b637b2e87e922),
[setOverrideMode()](../../d3/db3/classGui_1_1ViewProvider.html#ad74c21d50c90ffcdca8a7f274f697943),
and
[PartDesignGui::ViewProviderBody::setOverrideMode()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#ac0025966b6885197861269fee3a65e60).

## ◆ pcAnnotation

| [SoSeparator](../../de/d78/classSoSeparator.html)*
Gui::ViewProvider::pcAnnotation  
---  
protected  
  
The root separator for annotations.

Referenced by
[getAnnotation()](../../d3/db3/classGui_1_1ViewProvider.html#a1c8bc4440ecc28cc6d0bfe8456fd0d17),
and
[~ViewProvider()](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb).

## ◆ pcModeSwitch

| SoSwitch* Gui::ViewProvider::pcModeSwitch  
---  
protected  
  
this is the mode switch, all the different viewing modes are collected here

Referenced by
[addDisplayMaskMode()](../../d3/db3/classGui_1_1ViewProvider.html#af61b54ac266120fb12c5cdacf3f17b43),
[Gui::ViewProviderExtern::adjustDocumentName()](../../dd/d9c/classGui_1_1ViewProviderExtern.html#ab4ce3336eb37079f5bc18dc94fb7924f),
[PartGui::ViewProviderPartExt::attach()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a797fa2d8c1b12da5c8fccb3faaf033d6),
[getBoundingBox()](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3),
[Gui::ViewProviderLink::getDetailPath()](../../d6/d59/classGui_1_1ViewProviderLink.html#a631a96d7ef6239aabe05c86cf3c20d31),
[Gui::ViewProviderPlacement::getDetailPath()](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a166b1adf706ec848ee1ea85ddb941d86),
[getDetailPath()](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd),
[Gui::ViewProviderDocumentObject::getDetailPath()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a2b877c2c199d31afe6d958825da2c360),
[getDisplayMaskMode()](../../d3/db3/classGui_1_1ViewProvider.html#a85cd744e0f609177ccd9c12c8180e0e5),
[Gui::ViewProviderDocumentObject::getElementPicked()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a1aa14689a5cc02702f75e171cc19cfb8),
[hide()](../../d3/db3/classGui_1_1ViewProvider.html#a6ebeb34c881fe262bfa6660683b52319),
[isShow()](../../d3/db3/classGui_1_1ViewProvider.html#a002feec6611feb7ea07be1878a5864a3),
[Gui::ViewProviderLink::onBeforeChange()](../../d6/d59/classGui_1_1ViewProviderLink.html#aefc3f174999bdd4648769e65cfbcf399),
[Gui::ViewProviderLink::onChanged()](../../d6/d59/classGui_1_1ViewProviderLink.html#a07a0d46d41cc066a8b7da7cab6d0e1a1),
[partialRender()](../../d3/db3/classGui_1_1ViewProvider.html#a1ad7f52f266a58575a0f8c67c3d7caf3),
[setModeSwitch()](../../d3/db3/classGui_1_1ViewProvider.html#aebaedef79623db445f3ec055c365d97f),
[setOverrideMode()](../../d3/db3/classGui_1_1ViewProvider.html#ad74c21d50c90ffcdca8a7f274f697943),
[PartDesignGui::ViewProviderAddSub::setPreviewDisplayMode()](../../da/d6b/classPartDesignGui_1_1ViewProviderAddSub.html#af83ba83cdbf7dad8bba49c1ef5db6963),
and
[~ViewProvider()](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb).

## ◆ pcRoot

| [SoSeparator](../../de/d78/classSoSeparator.html)* Gui::ViewProvider::pcRoot  
---  
protected  
  
The root Separator of the
[ViewProvider](../../d3/db3/classGui_1_1ViewProvider.html "General interface
for all visual stuff in FreeCAD This class is used to generate and handle all
aroun...").

Referenced by
[PartGui::ViewProviderPartExt::attach()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a797fa2d8c1b12da5c8fccb3faaf033d6),
[getAnnotation()](../../d3/db3/classGui_1_1ViewProvider.html#a1c8bc4440ecc28cc6d0bfe8456fd0d17),
[getBoundingBox()](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3),
[Gui::ViewProviderLink::getDetailPath()](../../d6/d59/classGui_1_1ViewProviderLink.html#a631a96d7ef6239aabe05c86cf3c20d31),
[Gui::ViewProviderPlacement::getDetailPath()](../../da/d5e/classGui_1_1ViewProviderPlacement.html#a166b1adf706ec848ee1ea85ddb941d86),
[getDetailPath()](../../d3/db3/classGui_1_1ViewProvider.html#af12296bf030b3aeafb644af7d28957cd),
[Gui::ViewProviderAnnotationLabel::setEdit()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a9e6d7fb0b017900b7ac12e21c88ceabc),
[PartGui::ViewProviderMirror::setEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a1f2db7361989a26090e6071227f1562a),
[PartDesignGui::ViewProviderTransformed::setEdit()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a5d37e6ba0bf8efbd6ebea83c4c331bb2),
[setRenderCacheMode()](../../d3/db3/classGui_1_1ViewProvider.html#adfec94f0ed4b8564d5dc77c92e57d088),
[Gui::ViewProviderGeometryObject::setSelectable()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a35686717f6c0c237ac862c053364df52),
[Gui::ViewProviderGeometryObject::showBoundingBox()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a836a76dade7a4b231046b04b90502088),
[MeshGui::ViewProviderIndexedFaceSet::showOpenEdges()](../../d8/d12/classMeshGui_1_1ViewProviderIndexedFaceSet.html#a65b8ecfe86530ac341627de87f7abfa6),
[MeshGui::ViewProviderMeshObject::showOpenEdges()](../../db/d49/classMeshGui_1_1ViewProviderMeshObject.html#ae82a031b38818acf426de7662d888138),
[MeshGui::ViewProviderMeshFaceSet::showOpenEdges()](../../df/de9/classMeshGui_1_1ViewProviderMeshFaceSet.html#a279ccf4672fe9e8fe3e81d0d6d709332),
[toString()](../../d3/db3/classGui_1_1ViewProvider.html#afcc561b1e8fdd949139f3e58a68e5b05),
[Gui::ViewProviderAnnotationLabel::unsetEdit()](../../da/d05/classGui_1_1ViewProviderAnnotationLabel.html#a5da12856b6d51ceac16b21fb5a5fa94d),
[PartGui::ViewProviderMirror::unsetEdit()](../../d2/d29/classPartGui_1_1ViewProviderMirror.html#a72ba82b453ad60568eb3bd6aa7a518f0),
[PartDesignGui::ViewProviderTransformed::unsetEdit()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a30b1e3fa317ddd2654853040be2f94d9),
[MeshPartGui::ViewProviderCrossSections::ViewProviderCrossSections()](../../dc/dfe/classMeshPartGui_1_1ViewProviderCrossSections.html#abe88a4d3faa31a555ff3f9fbc9561503),
[PartGui::ViewProviderCrossSections::ViewProviderCrossSections()](../../d8/df0/classPartGui_1_1ViewProviderCrossSections.html#ad1efdfa14f5c3030c1449fb04cbacaff),
and
[~ViewProvider()](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb).

## ◆ pcTransform

| SoTransform* Gui::ViewProvider::pcTransform  
---  
protected  
  
this is transformation for the provider

Referenced by
[Gui::ViewProviderDragger::setEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#ae112bfbf937f2ec8a8efd24fd432acc5),
[setTransformation()](../../d3/db3/classGui_1_1ViewProvider.html#a8d06af6b975e2907f1971bd712f95cf0),
[Gui::ViewProviderDragger::unsetEdit()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a10c5a11ef248cd9364b99efeb6f1ac33),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[Gui::ViewProviderVRMLObject::updateData()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a82a208dd8c96cf38b242d57948134214),
[MeshGui::ViewProviderMeshCurvature::updateData()](../../db/d1c/classMeshGui_1_1ViewProviderMeshCurvature.html#a50f18a08491899786bd7afbcffe50033),
[Gui::ViewProviderDragger::updateData()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a6d433c9fe9d47fa7ab9be6d7e01d6509),
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d),
and
[~ViewProvider()](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb).

## ◆ pyViewObject

| ViewProviderPy* Gui::ViewProvider::pyViewObject  
---  
protected  
  
Referenced by
[getPyObject()](../../d3/db3/classGui_1_1ViewProvider.html#aedc8b6ee0d29756e6be6d0c3ed0a0aee),
[MeshGui::ViewProviderMesh::getPyObject()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a491c9250dd9372b18d0296cedfb01701),
[Gui::ViewProviderDocumentObject::getPyObject()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a256b755ac0eba62bb50670e75874bed9),
[Gui::ViewProviderLink::getPyObject()](../../d6/d59/classGui_1_1ViewProviderLink.html#ae9a76a67e95cadc3bbf289d9e5a3ad84),
[SpreadsheetGui::ViewProviderSheet::getPyObject()](../../d9/df2/classSpreadsheetGui_1_1ViewProviderSheet.html#a31c2af0bf22d66f737d3ed06bf7a5a1c),
[PartDesignGui::ViewProvider::getPyObject()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#ac03971ba790eda722f46e82c1126300f),
and
[~ViewProvider()](../../d3/db3/classGui_1_1ViewProvider.html#af8591f97f9dccf9e9c47fc97c8945ecb).

## ◆ signalChangeIcon

boost::signals2::signal<void ()> Gui::ViewProvider::signalChangeIcon  
---  
  
signal on icon change

Referenced by
[Gui::ViewProviderLink::checkIcon()](../../d6/d59/classGui_1_1ViewProviderLink.html#a91c006789903dc70925730bc04557013),
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18),
[PartGui::ViewProviderAttachExtension::extensionUpdateData()](../../d7/d61/classPartGui_1_1ViewProviderAttachExtension.html#a26d1e4000673dfcad3fc7c572768b80f),
[Gui::LinkInfo::LinkInfo()](../../d4/da4/classGui_1_1LinkInfo.html#ae3618e9bfdb664830e6725d702879020),
[PartDesignGui::ViewProvider::setTipIcon()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#a15e4f081d6f3febfbad985778e4c3587),
[TechDrawGui::ViewProviderPage::updateData()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac28b3c92f87b718452fddd90fe4f2f4f),
and
[Gui::ViewProviderLink::updateDataPrivate()](../../d6/d59/classGui_1_1ViewProviderLink.html#a2f2113e0017af3819a9064380ed30d0d).

## ◆ signalChangeStatusTip

boost::signals2::signal<void (const QString&)>
Gui::ViewProvider::signalChangeStatusTip  
---  
  
signal on status tip change

Referenced by
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18).

## ◆ signalChangeToolTip

boost::signals2::signal<void (const QString&)>
Gui::ViewProvider::signalChangeToolTip  
---  
  
signal on tooltip change

Referenced by
[Gui::DocumentObjectData::DocumentObjectData()](../../d6/d82/classGui_1_1DocumentObjectData.html#aef9adb6717b71286982c27610e989f18).

## ◆ sPixmap

| const char* Gui::ViewProvider::sPixmap  
---  
protected  
  
Referenced by
[TechDrawGui::ViewProviderDimension::attach()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a074916255bd70c0cd57d36b717586f4d),
[TechDrawGui::ViewProviderViewPart::attach()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a5b6c85e22973c70244cbb269ddd9b7f8),
[Gui::ViewProviderLink::checkIcon()](../../d6/d59/classGui_1_1ViewProviderLink.html#a91c006789903dc70925730bc04557013),
[PartGui::ViewProviderSpline::getIcon()](../../d6/d09/classPartGui_1_1ViewProviderSpline.html#aba3eb8121c249090ecb9d0491da81f0c),
[getIcon()](../../d3/db3/classGui_1_1ViewProvider.html#af6bd43d711cf91767cadf6fcd2827b47),
[Gui::ViewProviderDocumentObjectGroup::getIcon()](../../df/d84/classGui_1_1ViewProviderDocumentObjectGroup.html#ad62b53c0a798c9a13f3882a3a7641958),
[Gui::ViewProviderLink::getIcon()](../../d6/d59/classGui_1_1ViewProviderLink.html#a9fae57bc9689e1d1c9b5377f340da728),
[Gui::ViewProviderPart::getIcon()](../../d9/d6c/classGui_1_1ViewProviderPart.html#afba5f47c9f0f811fe7983cac5c6f5fa3),
[TechDrawGui::ViewProviderDimension::updateData()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a67972f9204e723e1b39e2d561e12b347),
[TechDrawGui::ViewProviderProjGroupItem::updateData()](../../d1/d88/classTechDrawGui_1_1ViewProviderProjGroupItem.html#aa193f03d76fb1ecdf199186e888354ce),
[TechDrawGui::ViewProviderPage::updateData()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#ac28b3c92f87b718452fddd90fe4f2f4f),
[PartDesignGui::ViewProviderBoolean::ViewProviderBoolean()](../../d7/d09/classPartDesignGui_1_1ViewProviderBoolean.html#accb99f2dc304e0aec6d077bad7e4b48c),
[PartDesignGui::ViewProviderDatumCoordinateSystem::ViewProviderDatumCoordinateSystem()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a53832f895c08903546a696bd6e667100),
[FemGui::ViewProviderFemMesh::ViewProviderFemMesh()](../../d7/def/classFemGui_1_1ViewProviderFemMesh.html#a357c245ca2e9b478429c31fd3401e9d7),
[FemGui::ViewProviderFemPostPlaneFunction::ViewProviderFemPostPlaneFunction()](../../d8/ddd/classFemGui_1_1ViewProviderFemPostPlaneFunction.html#aa66925aa45db6811cee9b19fe136fb66),
[Gui::ViewProviderGeometryObject::ViewProviderGeometryObject()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a2b9a89fc4a6101419f4783032d3edfcb),
[TechDrawGui::ViewProviderLeader::ViewProviderLeader()](../../da/d6b/classTechDrawGui_1_1ViewProviderLeader.html#a138a6a73f5f86c9ea59deec4d925ebe5),
[Gui::ViewProviderLink::ViewProviderLink()](../../d6/d59/classGui_1_1ViewProviderLink.html#ac80b32ec9821edd74f1e39d58951773d),
[PartGui::ViewProviderOffset2D::ViewProviderOffset2D()](../../dc/d97/classPartGui_1_1ViewProviderOffset2D.html#afa84d419146f95f02baaa47eaf293826),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
[TechDrawGui::ViewProviderRichAnno::ViewProviderRichAnno()](../../d2/d72/classTechDrawGui_1_1ViewProviderRichAnno.html#aa9e7ef3ef91f11afa7845443982c7943),
[Gui::ViewProviderTextDocument::ViewProviderTextDocument()](../../dc/d65/classGui_1_1ViewProviderTextDocument.html#a64987c999f5eadaa7f68cd0756578af4),
and
[TechDrawGui::ViewProviderViewPart::ViewProviderViewPart()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aa788186aa3b1edf4937b903368b9a626).

## ◆ StatusBits

| std::bitset<32> Gui::ViewProvider::StatusBits  
---  
protected  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Gui/ViewProvider.h
  * FreeCAD/src/Gui/ViewProvider.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

