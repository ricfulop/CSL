---
url: https://freecad.github.io/SourceDoc/d4/d5a/group__OFFLINERENDERINGUTILS.html
scraped_at: 2025-09-08T14:52:21.909757
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Functions

OfflineRenderingUtils

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Utility
modules](../../da/d56/group__UTILITIES.html)

Utility functions to work with FreeCAD files in console mode. More...

##  Classes  
  
---  
class | [OfflineRenderingUtils.FreeCADGuiHandler](../../d6/dc4/classOfflineRenderingUtils_1_1FreeCADGuiHandler.html)  
  
##  Functions  
  
---  
def | [OfflineRenderingUtils.buildGuiDocumentFromColors](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gad2bbe5872f2ecce7d46c1da18b362e29) (document, colors, camera=None)  
def | [OfflineRenderingUtils.buildGuiDocumentFromGuiData](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga6882d47dd86bdd35e050299f95d42174) (document, guidata)  
def | [OfflineRenderingUtils.buildScene](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga30b8ebc84486d3906baa611f9558e3b0) (objects, colors=None)  
def | [OfflineRenderingUtils.embedLight](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga01d7cc061bea5151b93de247cbbd67b3) (scene, lightdir)  
def | [OfflineRenderingUtils.extract](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga5e0f573c80afa8faa06244f8631395fd) (filename, inputpath, outputpath=None)  
def | [OfflineRenderingUtils.getCamera](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga2664cc98e49e58239330671ffba59a22) (filepath)  
def | [OfflineRenderingUtils.getCoinCamera](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaffd75a6b5a5344bb49fa61c252f04587) (camerastring)  
def | [OfflineRenderingUtils.getColors](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga3f18a719ff9d44e26b05bbfcc754f2c0) (filename, nodiffuse=False)  
def | [OfflineRenderingUtils.getGuiData](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gab5314d2ba38f734b8512f3ecebb4b263) (filename)  
def | [OfflineRenderingUtils.getStepData](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga9453873ce2250ad95d8979c052620f48) (objects, colors)  
def | [OfflineRenderingUtils.getUnsigned](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gac02d3799f65688af774faca760779980) (color)  
def | [OfflineRenderingUtils.getViewProviderClass](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gac3fe9a8d7dc5d6d27cdf0b7352b3d970) (obj)  
def | [OfflineRenderingUtils.openiv](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga0fb99e05ca96f266ee39b8c8e76e9b6b) (filename)  
def | [OfflineRenderingUtils.render](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga724a60c6421493d9e4d660c1f6215dd6) (outputfile, scene=None, camera=None, zoom=False, width=400, height=300, background=(1.0, 1.0, 1.0), lightdir=None)  
def | [OfflineRenderingUtils.save](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga7b2e62960b5d1bfec184e077e47048c4) (document, filename=None, guidata=None, colors=None, camera=None)  
def | [OfflineRenderingUtils.saveDiffuseColor](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga42fa2cfdb5584cc49cf952db0fe02ff8) (colorlist)  
def | [OfflineRenderingUtils.saveiv](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga1f03ff4913580dc0cda904aa4d78a3c8) (scene, filename)  
def | [OfflineRenderingUtils.viewer](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d) (scene=None, background=(1.0, 1.0, 1.0), lightdir=None)  
  
## Detailed Description

Utility functions to work with FreeCAD files in console mode.

Offline rendering utilities

## Function Documentation

## ◆ buildGuiDocumentFromColors()

def OfflineRenderingUtils.buildGuiDocumentFromColors  | ( |  | _document_ ,   
---|---|---|---  
|  |  | _colors_ ,   
|  |  | _camera_ = `None`  
| ) | |   
      
    
    buildGuiDocumentFromColors(document,colors,camera=None): Returns the path to a temporary GuiDocument.xml for the given document.
    Colors is a color dictionary of objName:ShapeColorTuple or obj:DiffuseColorList. Camera, if given, is a string representing
    a coin camera. You must delete the temporary file after using it.

References
[OfflineRenderingUtils.getUnsigned()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gac02d3799f65688af774faca760779980),
[OfflineRenderingUtils.getViewProviderClass()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gac3fe9a8d7dc5d6d27cdf0b7352b3d970),
and
[OfflineRenderingUtils.saveDiffuseColor()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga42fa2cfdb5584cc49cf952db0fe02ff8).

Referenced by
[OfflineRenderingUtils.save()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga7b2e62960b5d1bfec184e077e47048c4).

## ◆ buildGuiDocumentFromGuiData()

def OfflineRenderingUtils.buildGuiDocumentFromGuiData  | ( |  | _document_ ,   
---|---|---|---  
|  |  | _guidata_  
| ) | |   
      
    
    buildGuiDocumentFromColors(document,guidata): Returns the path to a temporary GuiDocument.xml for the given document.
    
       GuiData is a dictionary, which can be obtained by the getGuiData() function, and has the form:
    
        { "objectName" :
            { "propertyName" :
                { "type"  : "App::PropertyString",
                  "value" : "My Value"
                }
            }
        }
    This function returns a list of (filepath,name) tuples, the first one named GuiDocument.xml and the next ones being color files
    

References
[OfflineRenderingUtils.getGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gab5314d2ba38f734b8512f3ecebb4b263),
and
[OfflineRenderingUtils.getUnsigned()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gac02d3799f65688af774faca760779980).

Referenced by
[OfflineRenderingUtils.save()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga7b2e62960b5d1bfec184e077e47048c4).

## ◆ buildScene()

def OfflineRenderingUtils.buildScene  | ( |  | _objects_ ,   
---|---|---|---  
|  |  | _colors_ = `None`  
| ) | |   
      
    
    buildScene(objects,colors=None): builds a coin node from a given list of FreeCAD
    objects. Optional colors argument can be a dictionary of objName:ShapeColorTuple
    or obj:DiffuseColorList pairs.

## ◆ embedLight()

def OfflineRenderingUtils.embedLight  | ( |  | _scene_ ,   
---|---|---|---  
|  |  | _lightdir_  
| ) | |   
      
    
    embedLight(scene,lightdir): embeds a given coin node
    inside a shadow group with directional light with the
    given direction (x,y,z) tuple. Returns the final coin node

Referenced by
[OfflineRenderingUtils.render()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga724a60c6421493d9e4d660c1f6215dd6),
and
[OfflineRenderingUtils.viewer()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaaf21c1d43de28097395975d0bfcda42d).

## ◆ extract()

def OfflineRenderingUtils.extract  | ( |  | _filename_ ,   
---|---|---|---  
|  |  | _inputpath_ ,   
|  |  | _outputpath_ = `None`  
| ) | |   
      
    
    extract(filename,inputpath,outputpath=None): extracts 'inputpath' which is a filename
    stored in filename (a FreeCAD or zip file). If outputpath is given, the file is saved as outputpath and
    nothing is returned. If not, the contents of the inputfile are returned and nothing is saved.

## ◆ getCamera()

def OfflineRenderingUtils.getCamera  | ( |  | _filepath_| ) |   
---|---|---|---|---|---  
      
    
    getCamera(filepath): Returns a string representing a coin camera node from a given FreeCAD
    file, or None if none was found inside

References
[OfflineRenderingUtils.getGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gab5314d2ba38f734b8512f3ecebb4b263).

Referenced by
[Gui::GraphicsScene.addStateMachine()](../../da/d3c/classGui_1_1GraphicsScene.html#ac760416bd68c0e573a6f159a07481507),
[importWebGL.export()](../../d9/d7c/namespaceimportWebGL.html#a3477b90d6e65d931a3277483f61131de),
and
[Mod.Show.SceneDetails.Camera.Camera.scene_value()](../../dd/d0b/classMod_1_1Show_1_1SceneDetails_1_1Camera_1_1Camera.html#a90d1963eb585ae926700b1e60af12b4a).

## ◆ getCoinCamera()

def OfflineRenderingUtils.getCoinCamera  | ( |  | _camerastring_| ) |   
---|---|---|---|---|---  
      
    
    getCoinCamera(camerastring): Returns a coin camera node from a string

Referenced by
[importWebGL.export()](../../d9/d7c/namespaceimportWebGL.html#a3477b90d6e65d931a3277483f61131de),
and
[OfflineRenderingUtils.render()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga724a60c6421493d9e4d660c1f6215dd6).

## ◆ getColors()

def OfflineRenderingUtils.getColors  | ( |  | _filename_ ,   
---|---|---|---  
|  |  | _nodiffuse_ = `False`  
| ) | |   
      
    
    getColors(filename,nodiffuse): Extracts the colors saved in a FreeCAD file
    Returns a dictionary containing ["objectName":colors] pairs.
    colrs can be either a 3-element tuple representing an RGB color, if
    the object has no per-face colors (DiffuseColor) defined, or a list
    of tuples if per-face colors are available. In case of DiffuseColors,
    tuples can have 4 values (RGBT) (T = transparency, inverse of alpha)
    This is a reduced version of getGuiData(), which returns more information.
    If nodiffuse = True, DiffuseColor info is discarded, only ShapeColor is read.

References
[OfflineRenderingUtils.getGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gab5314d2ba38f734b8512f3ecebb4b263).

## ◆ getGuiData()

def OfflineRenderingUtils.getGuiData  | ( |  | _filename_| ) |   
---|---|---|---|---|---  
      
    
    getGuiData(filename): Extract visual data from a saved FreeCAD file.
    Returns a dictionary ["objectName:dict] where dict contains properties
    keys  like ShapeColor, Transparency, DiffuseColor or Visibility. If found,
    also contains a GuiCameraSettings key with an iv repr of a coin camera

Referenced by
[OfflineRenderingUtils.buildGuiDocumentFromGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga6882d47dd86bdd35e050299f95d42174),
[OfflineRenderingUtils.getCamera()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga2664cc98e49e58239330671ffba59a22),
[OfflineRenderingUtils.getColors()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga3f18a719ff9d44e26b05bbfcc754f2c0),
and
[OfflineRenderingUtils.save()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga7b2e62960b5d1bfec184e077e47048c4).

## ◆ getStepData()

def OfflineRenderingUtils.getStepData  | ( |  | _objects_ ,   
---|---|---|---  
|  |  | _colors_  
| ) | |   
      
    
    getStepData(objects,colors): transforms the given list of objects and
    colors dictionary into a list of tuples acceptable by the STEP exporter of
    FreeCAD's Import module

## ◆ getUnsigned()

def OfflineRenderingUtils.getUnsigned  | ( |  | _color_| ) |   
---|---|---|---|---|---  
      
    
    getUnsigned(color): returns an unsigned int from a (r,g,b) color tuple

Referenced by
[OfflineRenderingUtils.buildGuiDocumentFromColors()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gad2bbe5872f2ecce7d46c1da18b362e29),
and
[OfflineRenderingUtils.buildGuiDocumentFromGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga6882d47dd86bdd35e050299f95d42174).

## ◆ getViewProviderClass()

def OfflineRenderingUtils.getViewProviderClass  | ( |  | _obj_| ) |   
---|---|---|---|---|---  
      
    
    getViewProviderClass(obj): tries to identify the associated view provider for a
       given python object. Returns a (modulename,classname) tuple if found, or None

Referenced by
[OfflineRenderingUtils.buildGuiDocumentFromColors()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gad2bbe5872f2ecce7d46c1da18b362e29).

## ◆ openiv()

def OfflineRenderingUtils.openiv  | ( |  | _filename_| ) |   
---|---|---|---|---|---  
      
    
    openiv(filename): opens an .iv file and returns a coin node from it

## ◆ render()

def OfflineRenderingUtils.render  | ( |  | _outputfile_ ,   
---|---|---|---  
|  |  | _scene_ = `None`,   
|  |  | _camera_ = `None`,   
|  |  | _zoom_ = `False`,   
|  |  | _width_ = `400`,   
|  |  | _height_ = `300`,   
|  |  | _background_ = `(1.0,1.0,1.0)`,   
|  |  | _lightdir_ = `None`  
| ) | |   
      
    
    render(outputfile,scene=None,camera=None,zoom=False,width=400,height=300,background=(1.0,1.0,1.0),lightdir=None):
    Renders a PNG image of given width and height and background color from the given coin scene, using
    the given coin camera (ortho or perspective). If zoom is True the camera will be resized to fit all
    objects. The outputfile must be a file path to save a png image. Optionally a light direction as a (x,y,z)
    tuple can be given. In this case, a directional light will be added and shadows will
    be turned on. This might not work with some 3D drivers.

References
[OfflineRenderingUtils.embedLight()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga01d7cc061bea5151b93de247cbbd67b3),
and
[OfflineRenderingUtils.getCoinCamera()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gaffd75a6b5a5344bb49fa61c252f04587).

Referenced by
[importWebGL.getHTMLTemplate()](../../d9/d7c/namespaceimportWebGL.html#a266eb359ebda752a3c51c4a05cc395b8),
[package_list.PackageListItemDelegate.paint()](../../da/dfb/classpackage__list_1_1PackageListItemDelegate.html#ad928912ca57425556ea59a75bcfdbd5d),
[DrawingGui::SvgView.paintEvent()](../../dd/d77/classDrawingGui_1_1SvgView.html#abeae5cd312210a269a7b87e50b447153),
[TechDrawGui::QGVPage.paintEvent()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#ad29c91e22f37a80df4e31ce6678c9e04),
[TechDrawGui::QGSPage.saveSvg()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a7c5dd2c51df61dba9689959c585870d2),
and
[QSint::TaskGroup.transparentRender()](../../d9/de8/classQSint_1_1TaskGroup.html#a612bc6915de05057bb0ac5085849e783).

## ◆ save()

def OfflineRenderingUtils.save  | ( |  | _document_ ,   
---|---|---|---  
|  |  | _filename_ = `None`,   
|  |  | _guidata_ = `None`,   
|  |  | _colors_ = `None`,   
|  |  | _camera_ = `None`  
| ) | |   
      
    
    save(document,filename=None,guidata=None,colors=None,camera=None): Saves the current document. If no filename
       is given, the filename stored in the document (document.FileName) is used.
    
       You can provide a guidata dictionary, which can be obtained by the getGuiData() function, and has the form:
    
        { "objectName" :
            { "propertyName" :
                { "type"  : "App::PropertyString",
                  "value" : "My Value"
                }
            }
        }
    
       The type of the "value" contents depends on the type (int, string, float,tuple...) see inside the FreeCADGuiHandler
       class to get an idea.
    
       If guidata is provided, colors and camera attributes are discarded.
    
       Alternatively, a color dictionary of objName:ShapeColorTuple or obj:DiffuseColorList pairs.can be provided,
       in that case the objects will keep their colors when opened in the FreeCAD GUI. If given, camera is a string
       representing a coin camera node.

References
[OfflineRenderingUtils.buildGuiDocumentFromColors()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gad2bbe5872f2ecce7d46c1da18b362e29),
[OfflineRenderingUtils.buildGuiDocumentFromGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga6882d47dd86bdd35e050299f95d42174),
and
[OfflineRenderingUtils.getGuiData()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gab5314d2ba38f734b8512f3ecebb4b263).

Referenced by
[Gui::MainWindow.closeAllDocuments()](../../d5/d2f/classGui_1_1MainWindow.html#a26025f09b536690547638795dfd37010),
[SMESH_Mesh.Dump()](../../d5/d97/classSMESH__Mesh.html#ac728d5c92b35cfdd82b7b4d488d13d17),
[Gui::AutoSaver.saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
[NETGENPlugin_Hypothesis.SaveTo()](../../da/d75/classNETGENPlugin__Hypothesis.html#a112432a4c202e0200088075ec0cfd27f),
[NETGENPlugin_SimpleHypothesis_2D.SaveTo()](../../d3/d02/classNETGENPlugin__SimpleHypothesis__2D.html#ad2257c00c781b6cb283f208bbf162904),
[NETGENPlugin_SimpleHypothesis_3D.SaveTo()](../../df/dd6/classNETGENPlugin__SimpleHypothesis__3D.html#a630ffbbedf52c224b7c2529b62aeb276),
[SMESH_Algo.SaveTo()](../../d4/df9/classSMESH__Algo.html#a0e6443df50fa93021852a865ba048fc2),
[StdMeshers_Adaptive1D.SaveTo()](../../da/d2d/classStdMeshers__Adaptive1D.html#a325ae4ca99a521cc7107497933685ad7),
[StdMeshers_Arithmetic1D.SaveTo()](../../d8/d86/classStdMeshers__Arithmetic1D.html#ad8a6a744dd0984003c6ca874cf55dbb8),
[StdMeshers_AutomaticLength.SaveTo()](../../de/d38/classStdMeshers__AutomaticLength.html#aa51a93cceb36548cdc6528c6a781d984),
[StdMeshers_CartesianParameters3D.SaveTo()](../../d4/df8/classStdMeshers__CartesianParameters3D.html#a142533745339f70ef69d2d8f71beddaa),
[StdMeshers_Deflection1D.SaveTo()](../../d9/d6d/classStdMeshers__Deflection1D.html#a5baf7913c32ce0e4fd591d0e0a541471),
[StdMeshers_FixedPoints1D.SaveTo()](../../d1/dfb/classStdMeshers__FixedPoints1D.html#a3cf603d83ffe9d72bca4da7fc2b5bcfa),
[StdMeshers_Geometric1D.SaveTo()](../../d1/d3a/classStdMeshers__Geometric1D.html#ad8aa7c7e61f1045c6f3380b41725c5dc),
[StdMeshers_ImportSource1D.SaveTo()](../../db/ddd/classStdMeshers__ImportSource1D.html#ac939bf6926aa9af51b585d62d7f68d23),
[StdMeshers_LayerDistribution.SaveTo()](../../dd/d92/classStdMeshers__LayerDistribution.html#a6a4abc2ec7b148dc64b7b2753ee574e6),
[StdMeshers_LengthFromEdges.SaveTo()](../../d8/d56/classStdMeshers__LengthFromEdges.html#ace235cdb15676a17c66e730c3b662f2b),
[StdMeshers_LocalLength.SaveTo()](../../dc/d7e/classStdMeshers__LocalLength.html#a9ef8aec865b70a3ea4c0e2828b405ea6),
[StdMeshers_MaxElementArea.SaveTo()](../../d4/ded/classStdMeshers__MaxElementArea.html#af5a9d39ae2262ffc602e82ae9a790d1c),
[StdMeshers_MaxElementVolume.SaveTo()](../../d3/d58/classStdMeshers__MaxElementVolume.html#a32a35868ffcfe8370cc99fd5409a5ef8),
[StdMeshers_MaxLength.SaveTo()](../../df/d34/classStdMeshers__MaxLength.html#a6de1a78a313129d840bdc836e59e70da),
[StdMeshers_NotConformAllowed.SaveTo()](../../da/db1/classStdMeshers__NotConformAllowed.html#aa4d3a7e85e7516b89673f4dba14eca58),
[StdMeshers_NumberOfLayers.SaveTo()](../../d0/d60/classStdMeshers__NumberOfLayers.html#a87ce972359e56115aa7b617c001c8eca),
[StdMeshers_NumberOfSegments.SaveTo()](../../de/d06/classStdMeshers__NumberOfSegments.html#af4521c872f76c6e3573e154d3ecd0946),
[StdMeshers_ProjectionSource1D.SaveTo()](../../df/d49/classStdMeshers__ProjectionSource1D.html#a053ffb11070fa464d8b385c143215131),
[StdMeshers_ProjectionSource2D.SaveTo()](../../d6/d99/classStdMeshers__ProjectionSource2D.html#ad0c016057902b464dd9e363e8084ef6e),
[StdMeshers_ProjectionSource3D.SaveTo()](../../dc/d12/classStdMeshers__ProjectionSource3D.html#a4d7742abbf9b9adf68b8a8c97e2c6fcf),
[StdMeshers_Propagation.SaveTo()](../../dd/d52/classStdMeshers__Propagation.html#ac04dbaaf4a7836151b097d4a10be446d),
[StdMeshers_QuadrangleParams.SaveTo()](../../da/da9/classStdMeshers__QuadrangleParams.html#ae6f1add2e37e123184be5e6779b47dff),
[StdMeshers_QuadranglePreference.SaveTo()](../../dd/d2f/classStdMeshers__QuadranglePreference.html#aec611fe62ed167d79bed595869e352a7),
[StdMeshers_QuadraticMesh.SaveTo()](../../d5/dee/classStdMeshers__QuadraticMesh.html#a8231347748b2ff2c7eaad0a1d8bdb81d),
[StdMeshers_Reversible1D.SaveTo()](../../db/dd5/classStdMeshers__Reversible1D.html#a73ea929e868c2068c67730fb2d417cef),
[StdMeshers_SegmentLengthAroundVertex.SaveTo()](../../dc/ded/classStdMeshers__SegmentLengthAroundVertex.html#a7a0ca6543c3319600f46ac37eb7576dd),
[StdMeshers_StartEndLength.SaveTo()](../../de/dfa/classStdMeshers__StartEndLength.html#a7a0193620fe883d6ec101f5c4e108a91),
[StdMeshers_TrianglePreference.SaveTo()](../../d4/d09/classStdMeshers__TrianglePreference.html#a09c584953e0fb7202f1bdb68c1eb66df),
[StdMeshers_ViscousLayers.SaveTo()](../../da/d03/classStdMeshers__ViscousLayers.html#ae18e5771956294d372b48c5ad5db94af),
and
[SandboxGui::TaskPanelView.TaskPanelView()](../../d1/d99/classSandboxGui_1_1TaskPanelView.html#a37051f4883eba702df09cf5086c3c0c4).

## ◆ saveDiffuseColor()

def OfflineRenderingUtils.saveDiffuseColor  | ( |  | _colorlist_| ) |   
---|---|---|---|---|---  
      
    
    saveDiffuseColor(colorlist): Saves the given list or tuple of
    color tuples to a temp file, suitable to include in a DiffuseColor
    property. Returns the path to the created temp file

Referenced by
[OfflineRenderingUtils.buildGuiDocumentFromColors()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#gad2bbe5872f2ecce7d46c1da18b362e29).

## ◆ saveiv()

def OfflineRenderingUtils.saveiv  | ( |  | _scene_ ,   
---|---|---|---  
|  |  | _filename_  
| ) | |   
      
    
    saveiv(scene,filename): saves an .iv file with the contents of the given coin node

## ◆ viewer()

def OfflineRenderingUtils.viewer  | ( |  | _scene_ = `None`,   
---|---|---|---  
|  |  | _background_ = `(1.0,1.0,1.0)`,   
|  |  | _lightdir_ = `None`  
| ) | |   
      
    
    viewer(scene=None,background=(1.0,1.0,1.0),lightdir=None): starts
    a standalone coin viewer with the contents of the given scene. You can
    give a background color, and optionally a light direction as a (x,y,z)
    tuple. In this case, a directional light will be added and shadows will
    be turned on. This might not work with some 3D drivers.

References
[OfflineRenderingUtils.embedLight()](../../d4/d5a/group__OFFLINERENDERINGUTILS.html#ga01d7cc061bea5151b93de247cbbd67b3).

Referenced by
[DrawingGui::TaskProjection.accept()](../../d8/dc3/classDrawingGui_1_1TaskProjection.html#abc007288878ca57e8a8b2a8b9801bf45),
[TechDrawGui::TaskProjection.accept()](../../d5/def/classTechDrawGui_1_1TaskProjection.html#abc007288878ca57e8a8b2a8b9801bf45),
[SketcherGui::DrawSketchHandler.activate()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#aa8a8de87366fa745b5426f9917af31ce),
[StdCmdAlignment.activated()](../../df/d17/classStdCmdAlignment.html#a44409be4abd266d5d5e34dacb5484101),
[StdCmdEdit.activated()](../../dd/d46/classStdCmdEdit.html#a0f64d05832844dd0219624d2807c8331),
[StdCmdDrawStyle.activated()](../../d1/d5a/classStdCmdDrawStyle.html#a9b8abf379e939278dae2fe1adc913d33),
[StdCmdToggleNavigation.activated()](../../d4/d4e/classStdCmdToggleNavigation.html#a798c62a37186af1f888fa6e0a8a4c13e),
[StdViewZoomIn.activated()](../../dc/d47/classStdViewZoomIn.html#aad9fc58906612af80512b3777c636e13),
[StdViewZoomOut.activated()](../../d7/d21/classStdViewZoomOut.html#a411a1b2d47b20d0284b8872f7a4ed81a),
[StdViewBoxZoom.activated()](../../d3/d9b/classStdViewBoxZoom.html#a30798ff04001375ebb3733f912b381ce),
[StdBoxSelection.activated()](../../d1/d61/classStdBoxSelection.html#afb98364a6158c7696de79dda11703b64),
[StdBoxElementSelection.activated()](../../de/d57/classStdBoxElementSelection.html#aaa9bc41cd8b018d223ff8c1742ffec4a),
[StdCmdMeasureDistance.activated()](../../db/dfc/classStdCmdMeasureDistance.html#a79aa6b1fca1a557886622ab524843ac0),
[CmdViewMeasureClearAll.activated()](../../d0/d63/classCmdViewMeasureClearAll.html#a140fe86c71f61dfb51496c628d23f481),
[PartGui::FaceColors::Private.addFacesToSelection()](../../d4/d4b/classFaceColors_1_1Private.html#a9eb1efd1782f31dd3bad393299212f3b),
[PartGui.addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[Gui::AlignmentGroup.addToViewer()](../../dc/d5e/classGui_1_1AlignmentGroup.html#a850c5851d5acd8eaa0cd5b275f4c5c7e),
[Gui::Command.adjustCameraPosition()](../../d2/dff/classGui_1_1Command.html#af60add42dfff945893ebce041d471045),
[SketcherGui::ViewProviderSketch.centerSelection()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a39111ad06287532f445d79a3b34017d1),
[Gui::Dialog::Clipping.Clipping()](../../d0/d8c/classGui_1_1Dialog_1_1Clipping.html#ab8f16575d84d8cfe2c34752ff4de79b9),
[TechDrawGui::Grabber3d.copyActiveViewToSvgFile()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#a44f769bea9d4e116b3667e59bec4e6da),
[MeshGui::MeshSelection.deselectTriangle()](../../d2/d86/classMeshGui_1_1MeshSelection.html#aa9ea6afdd2232a187d02f531eca1c0f3),
[SketcherGui::DrawSketchHandler.devicePixelRatio()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a10d477cda0227120510e7cbff9cb6897),
[PartGui.eraseAllDimensions()](../../d5/d49/namespacePartGui.html#ad475e7c9ea3b79ec4d821330b7717793),
[Gui::ViewProvider.eventCallback()](../../d3/db3/classGui_1_1ViewProvider.html#a2c9bbafc597aa5e02ebe9f8aac8a2c99),
[TechDrawGui::Grabber3d.execVectorizeAction()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#aac2dc1e40d1dfc85d6db0830f271f577),
[MeshGui::MeshFaceAddition.finishEditing()](../../db/d8b/classMeshGui_1_1MeshFaceAddition.html#aea3807c6a2f0a83bab86be4b716a9a78),
[MeshGui::MeshFillHole.finishEditing()](../../d5/d4f/classMeshGui_1_1MeshFillHole.html#ad909f361df2e6ff493d105c5a27a3924),
[TechDrawGui::DrawGuiUtil.get3DDirAndRot()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a6c011651124bc645ff71d71e7bd64f4d),
[Gui::ViewProvider.getBoundingBox()](../../d3/db3/classGui_1_1ViewProvider.html#a2c50bc8a5a70a3c5b696c6c60bf3b4d3),
[FemGui::ViewProviderFemPostFunction.getBoundingsOfView()](../../d5/d14/classFemGui_1_1ViewProviderFemPostFunction.html#a79bca65d489a2bbfb30a77c8e4ba7b81),
[Gui::Document.getEditingViewOfViewProvider()](../../de/d4e/classGui_1_1Document.html#a39f85fc80d3435d6cb0eb8fa960fc640),
[TechDrawGui::Grabber3d.getPaperScale()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#a9c088deb2adaa18fb00920beab8b9d3b),
[MeshGui::ViewProviderFace.getPickedPoint()](../../dc/d9d/classMeshGui_1_1ViewProviderFace.html#a7026dba7b5a2ab2e3f1ea15e1b83156c),
[Gui::ViewProviderGeometryObject.getPickedPoint()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#af08d52d891424d3757b77f743ee682bd),
[Gui::ViewProviderGeometryObject.getPickedPoints()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a4d01c35343e7b21ba2f8f1e4d82bb119),
[Gui::ViewProvider.getPointOnRay()](../../d3/db3/classGui_1_1ViewProvider.html#ad15840ae4de52552d452b3733e3c3dfa),
[PartDesignGui::ViewProviderDatum.getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ab70e87f8a87a50222337b00c4ef6d945),
[SketcherGui::ViewProviderSketch.getScaleFactor()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a98a854b6d2621eb48c51614b4cea53df),
[PartGui.getViewer()](../../d5/d49/namespacePartGui.html#a607f26e0077dd0a4f9a1e05dd3fab66f),
[MeshGui::MeshSelection.getViewer()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a5ec10e7c84177ce0509eb8c17929952f),
[Gui::View3DInventorPy.getViewer()](../../d3/df7/classGui_1_1View3DInventorPy.html#a5c078fbd0cdb3ca4c377cfe40b8efa79),
[TechDrawGui::Grabber3d.getViewerScale()](../../d7/d83/classTechDrawGui_1_1Grabber3d.html#aeaf05e0c5aba77d74e536d74f1ef0a83),
[PartGui.goDimensionAngularNoTask()](../../d5/d49/namespacePartGui.html#a22a4e967d614ba7959dc90e89f6e76dc),
[PartGui.goDimensionLinearNoTask()](../../d5/d49/namespacePartGui.html#a95a58a4eb8f790f7f2835cf162ee7edf),
[Gui::AbstractMouseSelection.grabMouseModel()](../../da/d82/classGui_1_1AbstractMouseSelection.html#a12407918ee67f06e3b84bb643d8046cb),
[StdCmdToggleNavigation.isActive()](../../d4/d4e/classStdCmdToggleNavigation.html#a2703bb81fe701b71e020113de8721e21),
[StdCmdMeasureDistance.isActive()](../../db/dfc/classStdCmdMeasureDistance.html#ae34eeedc376782cacdd1d9b6745864ad),
[PartGui::FaceColors::Private.isVisibleFace()](../../d4/d4b/classFaceColors_1_1Private.html#a45f00bc1caa544bac5d4e891763aa779),
[SketcherGui::ViewProviderSketch.mouseButtonPressed()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a265a44a9f18bd9ac103c0dd048a455e3),
[Gui::ViewProvider.mouseButtonPressed()](../../d3/db3/classGui_1_1ViewProvider.html#aef92094223e7104a02f8eab7aae50234),
[Gui::ViewProvider.mouseMove()](../../d3/db3/classGui_1_1ViewProvider.html#ac97b2006300630c2fc546f6e76381684),
[SketcherGui::ViewProviderSketch.mouseMove()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a4816546877fe55b4571250f5a6ff9afa),
[Gui::Flag.mouseMoveEvent()](../../dc/dd0/classGui_1_1Flag.html#a03078ff2e2826982ccc394b84271b68e),
[SketcherGui::ViewProviderSketch.mouseWheelEvent()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#abf568a3d758cfc6b3a2352d3079e7dad),
[Gui::ViewProvider.mouseWheelEvent()](../../d3/db3/classGui_1_1ViewProvider.html#a0d8a5bfdd103ffb0baef0efedc2b865f),
[NaviCube.NaviCube()](../../d1/d83/classNaviCube.html#a3a6650696d7c5e60568aa5cf2fda24e8),
[NaviCubeImplementation.NaviCubeImplementation()](../../df/dc9/classNaviCubeImplementation.html#acee51772b372c1463da029f32da4ff12),
[MeshGui::MeshSelection.prepareFreehandSelection()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a674ae82637715fe99543366702476e38),
[SketcherGui::ViewProviderSketch.purgeHandler()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#aeb5e54c6185930bdb0765d747f2b60e1),
[Gui::AlignmentGroup.removeFromViewer()](../../dc/d5e/classGui_1_1AlignmentGroup.html#ac48f1b2adbbf40bd0652e8f1a7e8b124),
[Gui::Application.sCreateViewer()](../../d9/da8/classGui_1_1Application.html#ade141ca54f4fdd0ce6f4677e2df08dd8),
[MeshGui::MeshSelection.selectTriangle()](../../d2/d86/classMeshGui_1_1MeshSelection.html#aeaa4625f5e9ece863193f95fa5c41bed),
[Gui::AbstractSplitViewPy.sequence_item()](../../de/ddd/classGui_1_1AbstractSplitViewPy.html#aa73fb53f48754ce920d76e596d58d826),
[SketcherGui::DrawSketchHandler.setCursor()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#a8cf59d4479ba8141f5f2ec47014faa65),
[Gui::Dialog::DlgInspector.setDocument()](../../de/d72/classGui_1_1Dialog_1_1DlgInspector.html#a01a91aa49c58687a47ab8b9809704b8c),
[SketcherGui::ViewProviderSketch.setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[Gui::ViewProviderPythonFeatureImp.setEditViewer()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#a729afac9920b04c1cf3563c7125430c4),
[Gui::ViewProviderDragger.setEditViewer()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a5746c8658c714b1910627ea804ca2353),
[Gui::ViewProviderLink.setEditViewer()](../../d6/d59/classGui_1_1ViewProviderLink.html#a3ed619a014c6054537c032ff7a524b83),
[Gui::ViewProviderPythonFeatureT< ViewProviderT
>.setEditViewer()](../../dc/d41/classGui_1_1ViewProviderPythonFeatureT.html#ace6b8aadfc49e74e8958b0fde9703817),
[MeshGui::MeshSelection.setEnabledViewerSelection()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a628ef6b58b7cfaccea945ec271bd70db),
[PartGui::BoxSelection.start()](../../d6/d56/classPartGui_1_1BoxSelection.html#aa32ce08e79bbb6efa4ccb3a33ea80dcc),
[MeshGui::MeshFaceAddition.startEditing()](../../db/d8b/classMeshGui_1_1MeshFaceAddition.html#a68bf14f1519afeea6fcfd353da96fb29),
[MeshGui::MeshFillHole.startEditing()](../../d5/d4f/classMeshGui_1_1MeshFillHole.html#a611c571141e0f653b195fcc94e68a191),
[MeshGui::MeshSelection.startInteractiveCallback()](../../d2/d86/classMeshGui_1_1MeshSelection.html#aea24e9054e4365162aa7f68a5363b966),
[MeshGui::MeshSelection.stopInteractiveCallback()](../../d2/d86/classMeshGui_1_1MeshSelection.html#adbd9e6afea02c79e6d2f2a070df38902),
[MeshGui::MeshSelection.stopSelection()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a898958b72f1968109a4001aa14919430),
[SketcherGui::DrawSketchHandler.suggestedConstraintsPixmaps()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#ac79ccc66c40320bf240a9a7d8d20dd30),
[SketcherGui::DrawSketchHandler.unsetCursor()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#af92d1d2c6a6c2e47bba74149dec50e75),
[SketcherGui::ViewProviderSketch.unsetEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a0fed482e445d662b1ab784c89d54ef8f),
[Gui::ViewProviderPythonFeatureImp.unsetEditViewer()](../../de/dbe/classGui_1_1ViewProviderPythonFeatureImp.html#aac7318912cfa4a32986c023267eaac62),
[Gui::ViewProviderDragger.unsetEditViewer()](../../d3/d04/classGui_1_1ViewProviderDragger.html#a139b6c22fd8be484d76a6eca106a3984),
[Gui::ViewProviderLink.unsetEditViewer()](../../d6/d59/classGui_1_1ViewProviderLink.html#a597f850ded2ad26d7f676088f43157cc),
[Gui::ViewProviderPythonFeatureT< ViewProviderT
>.unsetEditViewer()](../../dc/d41/classGui_1_1ViewProviderPythonFeatureT.html#a0f40569d42713f75c4358ef04bdb3ff2),
[StdCmdDrawStyle.updateIcon()](../../d1/d5a/classStdCmdDrawStyle.html#a61a93d4833e46191aac55c9f6493caeb),
[PartDesignGui::ViewProviderBody.updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0),
[Gui::ViewProviderOriginGroupExtension.updateOriginSize()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#a254bd812cc1814ed270f1d92e445ad8e),
[PartGui::Location.~Location()](../../db/d6f/classPartGui_1_1Location.html#af5be2c6550bbd96137cbb3144ec3c529),
and
[MeshGui::MeshSelection.~MeshSelection()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a74ec1892b69908b7e52ad0d41e18fdb3).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

