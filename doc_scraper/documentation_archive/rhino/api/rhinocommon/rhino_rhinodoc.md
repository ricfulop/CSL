---
url: https://developer.rhino3d.com/api/rhinocommon/rhino.rhinodoc
scraped_at: 2025-09-08T16:05:16.562358
title: Untitled
---

[_home_](/api/rhinocommon/)

/

[Rhino](/api/rhinocommon/rhino)

/

RhinoDoc

# RhinoDoc class

Represents an active model.

  
_Derived Classes:_

_Namespace:[Rhino](/api/rhinocommon/rhino)_  
 _RhinoDoc:[references](/api/rhinocommon/references/rhino.rhinodoc)_

 _keyboard_arrow_down_

Constructors (1)

[**RhinoDoc**() Initializes a new instance of the RhinoDoc
class](/api/rhinocommon/rhino.rhinodoc/rhinodoc#\(\))

* * *

 _keyboard_arrow_down_

Properties (82)

[**ActiveCommandId** Get the ID of the active
command.](/api/rhinocommon/rhino.rhinodoc/activecommandid#)

* * *

[**ActiveDoc** WARNING!! Do not use the ActiveDoc if you don't have to. Under
Mac Rhino the ActiveDoc can change while a command is running. Use the doc
that is passed to you in your RunCommand function or continue to use the same
doc after the first call to
ActiveDoc.](/api/rhinocommon/rhino.rhinodoc/activedoc#)

* * *

[**ActiveSpace** Get the space associated with the active viewport for this
document](/api/rhinocommon/rhino.rhinodoc/activespace#)

* * *

[**AnimationProperties**
](/api/rhinocommon/rhino.rhinodoc/animationproperties#)

* * *

[**Bitmaps** bitmaps used in textures, backgrounds, wallpapers,
...](/api/rhinocommon/rhino.rhinodoc/bitmaps#)

* * *

[**CurrentEnvironment** __ Access to the current environment for various
uses](/api/rhinocommon/rhino.rhinodoc/currentenvironment#)

* * *

[**CurrentUndoRecordSerialNumber** >0: undo recording is active and being
saved on the undo record with the specified serial number. 0: undo recording
is not active. (Disabled or nothing is being
recorded.)](/api/rhinocommon/rhino.rhinodoc/currentundorecordserialnumber#)

* * *

[**CustomRenderSizes** ](/api/rhinocommon/rhino.rhinodoc/customrendersizes#)

* * *

[**DateCreated** ](/api/rhinocommon/rhino.rhinodoc/datecreated#)

* * *

[**DateLastEdited** Returns the date the document was created in Coordinated
Universal Time (UTC). Use DateTime.ToLocalTime to convert to local
time.](/api/rhinocommon/rhino.rhinodoc/datelastedited#)

* * *

[**DimStyles** ](/api/rhinocommon/rhino.rhinodoc/dimstyles#)

* * *

[**DistanceDisplayPrecision**
](/api/rhinocommon/rhino.rhinodoc/distancedisplayprecision#)

* * *

[**DocumentId** __ Gets the Document
Id.](/api/rhinocommon/rhino.rhinodoc/documentid#)

* * *

[**EarthAnchorPoint** ](/api/rhinocommon/rhino.rhinodoc/earthanchorpoint#)

* * *

[**Fonts** __](/api/rhinocommon/rhino.rhinodoc/fonts#)

* * *

[**GroundPlane** __ Gets the ground plane of this
document.](/api/rhinocommon/rhino.rhinodoc/groundplane#)

* * *

[**Groups** ](/api/rhinocommon/rhino.rhinodoc/groups#)

* * *

[**HatchPatterns** ](/api/rhinocommon/rhino.rhinodoc/hatchpatterns#)

* * *

[**InGetPoint** Returns True if currently in a
GetPoint.Get().](/api/rhinocommon/rhino.rhinodoc/ingetpoint#)

* * *

[**InstanceDefinitions**
](/api/rhinocommon/rhino.rhinodoc/instancedefinitions#)

* * *

[**IsAvailable** ](/api/rhinocommon/rhino.rhinodoc/isavailable#)

* * *

[**IsClosing** ](/api/rhinocommon/rhino.rhinodoc/isclosing#)

* * *

[**IsCommandRunning** Returns True if Rhino is currently running a
command.](/api/rhinocommon/rhino.rhinodoc/iscommandrunning#)

* * *

[**IsCreating** ](/api/rhinocommon/rhino.rhinodoc/iscreating#)

* * *

[**IsHeadless** ](/api/rhinocommon/rhino.rhinodoc/isheadless#)

* * *

[**IsInitializing** ](/api/rhinocommon/rhino.rhinodoc/isinitializing#)

* * *

[**IsLocked** Check to see if the file associated with this document is
locked. If it is locked then this is the only document that will be able to
write the file. Other instances of Rhino will fail to write this
document.](/api/rhinocommon/rhino.rhinodoc/islocked#)

* * *

[**IsOpening** ](/api/rhinocommon/rhino.rhinodoc/isopening#)

* * *

[**IsReadOnly** Current read-only mode for this document. True if the document
can be viewed but NOT saved. False if document can be viewed and
saved.](/api/rhinocommon/rhino.rhinodoc/isreadonly#)

* * *

[**IsSendingMail** True if Rhino is in the process of sending this document as
an email attachment.](/api/rhinocommon/rhino.rhinodoc/issendingmail#)

* * *

[**Layers** Layers in the document.](/api/rhinocommon/rhino.rhinodoc/layers#)

* * *

[**LayoutSpaceAnnotationScalingEnabled** If LayoutSpaceAnnotationScaling is
on, sizes in dimstyles are multiplied by dimscale when the annotation is
displayed in a detail viewport not in a
detail](/api/rhinocommon/rhino.rhinodoc/layoutspaceannotationscalingenabled#)

* * *

[**Lights** ](/api/rhinocommon/rhino.rhinodoc/lights#)

* * *

[**Linetypes** Linetypes in the
document.](/api/rhinocommon/rhino.rhinodoc/linetypes#)

* * *

[**Manifest** ](/api/rhinocommon/rhino.rhinodoc/manifest#)

* * *

[**Materials** Materials in the
document.](/api/rhinocommon/rhino.rhinodoc/materials#)

* * *

[**MeshingParameterStyle** Type of MeshingParameters currently used by the
document to mesh
objects](/api/rhinocommon/rhino.rhinodoc/meshingparameterstyle#)

* * *

[**ModelAbsoluteTolerance** Model space absolute
tolerance.](/api/rhinocommon/rhino.rhinodoc/modelabsolutetolerance#)

* * *

[**ModelAngleToleranceDegrees** Model space angle
tolerance.](/api/rhinocommon/rhino.rhinodoc/modelangletolerancedegrees#)

* * *

[**ModelAngleToleranceRadians** Model space angle
tolerance.](/api/rhinocommon/rhino.rhinodoc/modelangletoleranceradians#)

* * *

[**ModelBasepoint** The base point in the model that is used when inserting
the model into another as a block definition. By default the base point in any
model is 0,0,0.](/api/rhinocommon/rhino.rhinodoc/modelbasepoint#)

* * *

[**ModelDistanceDisplayPrecision**
](/api/rhinocommon/rhino.rhinodoc/modeldistancedisplayprecision#)

* * *

[**ModelRelativeTolerance** Model space relative
tolerance.](/api/rhinocommon/rhino.rhinodoc/modelrelativetolerance#)

* * *

[**ModelSpaceAnnotationScalingEnabled** If ModelSpaceAnnotationScaling is on,
sizes in dimstyles are multiplied by dimscale when the annotation is displayed
in a model space viewport not in a
detail](/api/rhinocommon/rhino.rhinodoc/modelspaceannotationscalingenabled#)

* * *

[**ModelSpaceHatchScale** The scale factor for hatches in model space when
Hatch Scaling is
enabled](/api/rhinocommon/rhino.rhinodoc/modelspacehatchscale#)

* * *

[**ModelSpaceHatchScalingEnabled** True if hatch scaling is enabled, False if
not.](/api/rhinocommon/rhino.rhinodoc/modelspacehatchscalingenabled#)

* * *

[**ModelSpaceTextScale** The scale factor for text in model space when
Annotation Scaling is
enabled](/api/rhinocommon/rhino.rhinodoc/modelspacetextscale#)

* * *

[**ModelUnitSystem** ](/api/rhinocommon/rhino.rhinodoc/modelunitsystem#)

* * *

[**Modified** Returns or sets the document's modified
flag.](/api/rhinocommon/rhino.rhinodoc/modified#)

* * *

[**Name** Returns the name of the currently loaded Rhino document (3DM
file).](/api/rhinocommon/rhino.rhinodoc/name#)

* * *

[**NamedConstructionPlanes** Collection of named construction
planes.](/api/rhinocommon/rhino.rhinodoc/namedconstructionplanes#)

* * *

[**NamedLayerStates** Collection of named layer
states.](/api/rhinocommon/rhino.rhinodoc/namedlayerstates#)

* * *

[**NamedPositions** Collection of named
positions.](/api/rhinocommon/rhino.rhinodoc/namedpositions#)

* * *

[**NamedViews** Collection of named
views.](/api/rhinocommon/rhino.rhinodoc/namedviews#)

* * *

[**NextUndoRecordSerialNumber** The serial number that will be assigned to the
next undo record that is
constructed.](/api/rhinocommon/rhino.rhinodoc/nextundorecordserialnumber#)

* * *

[**Notes** Returns or sets the document's
notes.](/api/rhinocommon/rhino.rhinodoc/notes#)

* * *

[**NotesLocked** ](/api/rhinocommon/rhino.rhinodoc/noteslocked#)

* * *

[**Objects** ](/api/rhinocommon/rhino.rhinodoc/objects#)

* * *

[**PageAbsoluteTolerance** Page space absolute
tolerance.](/api/rhinocommon/rhino.rhinodoc/pageabsolutetolerance#)

* * *

[**PageAngleToleranceDegrees** Page space angle
tolerance.](/api/rhinocommon/rhino.rhinodoc/pageangletolerancedegrees#)

* * *

[**PageAngleToleranceRadians** Page space angle
tolerance.](/api/rhinocommon/rhino.rhinodoc/pageangletoleranceradians#)

* * *

[**PageDistanceDisplayPrecision**
](/api/rhinocommon/rhino.rhinodoc/pagedistancedisplayprecision#)

* * *

[**PageRelativeTolerance** Page space relative
tolerance.](/api/rhinocommon/rhino.rhinodoc/pagerelativetolerance#)

* * *

[**PageUnitSystem** ](/api/rhinocommon/rhino.rhinodoc/pageunitsystem#)

* * *

[**Path** Returns the path of the currently loaded Rhino document (3DM
file).](/api/rhinocommon/rhino.rhinodoc/path#)

* * *

[**PostEffects** __ Access to the post
effects](/api/rhinocommon/rhino.rhinodoc/posteffects#)

* * *

[**RedoActive** Returns True if Redo is currently
active.](/api/rhinocommon/rhino.rhinodoc/redoactive#)

* * *

[**RenderEnvironments** ](/api/rhinocommon/rhino.rhinodoc/renderenvironments#)

* * *

[**RenderMaterials** ](/api/rhinocommon/rhino.rhinodoc/rendermaterials#)

* * *

[**RenderSettings** ](/api/rhinocommon/rhino.rhinodoc/rendersettings#)

* * *

[**RenderTextures** ](/api/rhinocommon/rhino.rhinodoc/rendertextures#)

* * *

[**RuntimeData** Collection of document runtime data. This is a good place to
put non-serializable, per document data, such as panel view models. Note well:
This data will be dispose with the document and does not get
serialized.](/api/rhinocommon/rhino.rhinodoc/runtimedata#)

* * *

[**RuntimeSerialNumber** Unique serialNumber for the document while the
application is running. This is not a persistent
value.](/api/rhinocommon/rhino.rhinodoc/runtimeserialnumber#)

* * *

[**Snapshots** Collection of
snapshots.](/api/rhinocommon/rhino.rhinodoc/snapshots#)

* * *

[**Strings** Collection of document user data strings in this
document](/api/rhinocommon/rhino.rhinodoc/strings#)

* * *

[**SubDAppearance** Returns or sets the appearance of all SubD objects in the
document.](/api/rhinocommon/rhino.rhinodoc/subdappearance#)

* * *

[**TemplateFileUsed** name of the template file used to create this document.
This is a runtime value only present if the document was newly
created.](/api/rhinocommon/rhino.rhinodoc/templatefileused#)

* * *

[**UndoActive** Returns True if Undo is currently
active.](/api/rhinocommon/rhino.rhinodoc/undoactive#)

* * *

[**UndoRecordingEnabled**
](/api/rhinocommon/rhino.rhinodoc/undorecordingenabled#)

* * *

[**UndoRecordingIsActive** True if undo recording is actually happening
now.](/api/rhinocommon/rhino.rhinodoc/undorecordingisactive#)

* * *

[**Views** ](/api/rhinocommon/rhino.rhinodoc/views#)

* * *

[**Worksession** Provides access to the document's
worksession.](/api/rhinocommon/rhino.rhinodoc/worksession#)

* * *

_keyboard_arrow_down_

Methods (70)

[**AddCustomUndoEvent**(String description, EventHandler<CustomUndoEventArgs>
handler,Object tag) Add a custom undo event so you can undo private plug-in
data when the user performs an undo or
redo](/api/rhinocommon/rhino.rhinodoc/addcustomundoevent#\(string,eventhandler<customundoeventargs>,object\))

* * *

[**AddCustomUndoEvent**(String description, EventHandler<CustomUndoEventArgs>
handler)
](/api/rhinocommon/rhino.rhinodoc/addcustomundoevent#\(string,eventhandler<customundoeventargs>\))

* * *

[**AdjustModelUnitSystem**(UnitSystem newUnitSystem,Boolean scale)
](/api/rhinocommon/rhino.rhinodoc/adjustmodelunitsystem#\(unitsystem,boolean\))

* * *

[**AdjustPageUnitSystem**(UnitSystem newUnitSystem,Boolean scale)
](/api/rhinocommon/rhino.rhinodoc/adjustpageunitsystem#\(unitsystem,boolean\))

* * *

[**Audit**(TextLog textLog,Boolean attemptRepair) Audits the contents of the
document.](/api/rhinocommon/rhino.rhinodoc/audit#\(textlog,boolean\))

* * *

[**BeginUndoRecord**(String description) Instructs Rhino to begin recording
undo information when the document is changed outside of a command. We use
this, e.g., to save changes caused by the modeless layer or object properties
dialogs when commands are not
running.](/api/rhinocommon/rhino.rhinodoc/beginundorecord#\(string\))

* * *

[**ClearRedoRecords**()
](/api/rhinocommon/rhino.rhinodoc/clearredorecords#\(\))

* * *

[**ClearUndoRecords**(Boolean purgeDeletedObjects)
](/api/rhinocommon/rhino.rhinodoc/clearundorecords#\(boolean\))

* * *

[**ClearUndoRecords**(UInt32 undoSerialNumber,Boolean purgeDeletedObjects)
](/api/rhinocommon/rhino.rhinodoc/clearundorecords#\(uint32,boolean\))

* * *

[**Create**(String modelTemplateFileName) Creates a new
RhinoDoc](/api/rhinocommon/rhino.rhinodoc/create#\(string\))

* * *

[**CreateDefaultAttributes**() Gets the default object attributes for this
document. The attributes will be linked to the currently active layer and they
will inherit the Document WireDensity
setting.](/api/rhinocommon/rhino.rhinodoc/createdefaultattributes#\(\))

* * *

[**CreateHeadless**(String file3dmTemplatePath) Create a new headless RhinoDoc
from a template
file](/api/rhinocommon/rhino.rhinodoc/createheadless#\(string\))

* * *

[**CustomRenderMeshesBoundingBox**(MeshType mt, ViewportInfo vp,Flags
flags,PlugIn plugin,DisplayPipelineAttributes attrs, out BoundingBox
boundingBox) Returns the bounding box of custom render primitives for this
object
.](/api/rhinocommon/rhino.rhinodoc/customrendermeshesboundingbox#\(meshtype,viewportinfo,ref,plugin,displaypipelineattributes,out\))

* * *

[**Dispose**() ](/api/rhinocommon/rhino.rhinodoc/dispose#\(\))

* * *

[**EndUndoRecord**(UInt32 undoRecordSerialNumber) Ends the undo
record.](/api/rhinocommon/rhino.rhinodoc/endundorecord#\(uint32\))

* * *

[**Equals**(Object obj) ](/api/rhinocommon/rhino.rhinodoc/equals#\(object\))

* * *

[**Export**(String filePath, ArchivableDictionary options) Export the entire
document to a file. All file formats that Rhino can export to are supported by
this
function.](/api/rhinocommon/rhino.rhinodoc/export#\(string,archivabledictionary\))

* * *

[**Export**(String filePath) Export the entire document to a file. All file
formats that Rhino can export to are supported by this
function.](/api/rhinocommon/rhino.rhinodoc/export#\(string\))

* * *

[**ExportSelected**(String filePath, ArchivableDictionary options) Export
selected geometry to a file. All file formats that Rhino can export to are
supported by this
function.](/api/rhinocommon/rhino.rhinodoc/exportselected#\(string,archivabledictionary\))

* * *

[**ExportSelected**(String filePath) Export selected geometry to a file. All
file formats that Rhino can export to are supported by this
function.](/api/rhinocommon/rhino.rhinodoc/exportselected#\(string\))

* * *

[**ExtractPreviewImage**(String path) Extracts the bitmap preview image from
the specified .3dm
file.](/api/rhinocommon/rhino.rhinodoc/extractpreviewimage#\(string\))

* * *

[**FindFile**(String filename) Search for a file using Rhino's search path.
Rhino will look in the following places: 1. Current model folder 2. Path
specified in options dialog/File tab 3. Rhino system folders 4. Rhino
executable folder](/api/rhinocommon/rhino.rhinodoc/findfile#\(string\))

* * *

[**FormatNumber**(Double value,Boolean appendUnitSystemName,Boolean
abbreviate) Call this method to get string representing the specified value
using the documents display coordinate system and display
precision.](/api/rhinocommon/rhino.rhinodoc/formatnumber#\(double,boolean,boolean\))

* * *

[**FormatNumber**(Double value) Call this method to get string representing
the specified value using the documents display coordinate system and display
precision.](/api/rhinocommon/rhino.rhinodoc/formatnumber#\(double\))

* * *

[**FromFilePath**(String filePath) Search the open document list for a
document with a Path equal to the specified file
path.](/api/rhinocommon/rhino.rhinodoc/fromfilepath#\(string\))

* * *

[**FromId**(Int32 docId) __](/api/rhinocommon/rhino.rhinodoc/fromid#\(int32\))

* * *

[**FromRuntimeSerialNumber**(UInt32 serialNumber)
](/api/rhinocommon/rhino.rhinodoc/fromruntimeserialnumber#\(uint32\))

* * *

[**GetAnalysisMeshingParameters**() Get analysis meshing parameters currently
used by the
document](/api/rhinocommon/rhino.rhinodoc/getanalysismeshingparameters#\(\))

* * *

[**GetCurrentMeshingParameters**() Get the custom meshing parameters that this
document will
use.](/api/rhinocommon/rhino.rhinodoc/getcurrentmeshingparameters#\(\))

* * *

[**GetCustomUnitSystem**(Boolean modelUnits,String customUnitName,Double
metersPerCustomUnit) Get the custom unit system name and custom unit
scale.](/api/rhinocommon/rhino.rhinodoc/getcustomunitsystem#\(boolean,out,out\))

* * *

[**GetEmbeddedFilesList**(Boolean missingOnly)
](/api/rhinocommon/rhino.rhinodoc/getembeddedfileslist#\(boolean\))

* * *

[**GetGridDefaults**() ](/api/rhinocommon/rhino.rhinodoc/getgriddefaults#\(\))

* * *

[**GetGumballPlane**(out Plane plane) Returns the active plane of Rhino's
auto-gumball widget. Note, when calling from a Rhino command, make sure the
command class has the Rhino.Commands.Style.Transparent command style
attribute.](/api/rhinocommon/rhino.rhinodoc/getgumballplane#\(out\))

* * *

[**GetHashCode**() ](/api/rhinocommon/rhino.rhinodoc/gethashcode#\(\))

* * *

[**GetMeshingParameters**(MeshingParameterStyle style) Get MeshingParameters
currently used by the
document](/api/rhinocommon/rhino.rhinodoc/getmeshingparameters#\(meshingparameterstyle\))

* * *

[**GetRenderPrimitiveList**(ViewportInfo viewport,DisplayPipelineAttributes
attrs) __ Build custom render mesh(es) for this document (i.e. - GH
meshes).](/api/rhinocommon/rhino.rhinodoc/getrenderprimitivelist#\(viewportinfo,displaypipelineattributes\))

* * *

[**GetRenderPrimitives**(ViewportInfo viewport,Boolean
forceTriangleMeshes,Boolean quietly) __ Get a enumerable list of custom mesh
primitives](/api/rhinocommon/rhino.rhinodoc/getrenderprimitives#\(viewportinfo,boolean,boolean\))

* * *

[**GetRenderPrimitives**(Boolean forceTriangleMeshes,Boolean quietly) __ Get a
enumerable list of custom mesh
primitives](/api/rhinocommon/rhino.rhinodoc/getrenderprimitives#\(boolean,boolean\))

* * *

[**GetRenderPrimitives**(Guid plugInId,ViewportInfo viewport,Boolean
forceTriangleMeshes,Boolean quietly) __ Get a enumerable list of custom mesh
primitives](/api/rhinocommon/rhino.rhinodoc/getrenderprimitives#\(guid,viewportinfo,boolean,boolean\))

* * *

[**GetUnitSystemName**(Boolean modelUnits,Boolean capitalize,Boolean
singular,Boolean abbreviate)
](/api/rhinocommon/rhino.rhinodoc/getunitsystemname#\(boolean,boolean,boolean,boolean\))

* * *

[**HasCustomRenderMeshes**(MeshType mt, ViewportInfo vp,Flags flags,PlugIn
plugin,DisplayPipelineAttributes attrs) Returns True if the document has a set
of custom render primitives - ie, CustomRenderMeshes will return non-
null.](/api/rhinocommon/rhino.rhinodoc/hascustomrendermeshes#\(meshtype,viewportinfo,ref,plugin,displaypipelineattributes\))

* * *

[**Import**(String filePath, ArchivableDictionary options) Import geometry
into a RhinoDoc from a file. This can be any file format that Rhino can
import](/api/rhinocommon/rhino.rhinodoc/import#\(string,archivabledictionary\))

* * *

[**Import**(String filePath) Import geometry into a RhinoDoc from a file. This
can be any file format that Rhino can
import](/api/rhinocommon/rhino.rhinodoc/import#\(string\))

* * *

[**InCommand**(Boolean bIgnoreScriptRunnerCommands) This is a low level tool
to determine if Rhino is currently running a
command.](/api/rhinocommon/rhino.rhinodoc/incommand#\(boolean\))

* * *

[**IsMetricUnitSystem**(Boolean modelUnits) Determines if a document unit
system is a metric unit
system.](/api/rhinocommon/rhino.rhinodoc/ismetricunitsystem#\(boolean\))

* * *

[**Open**(String filePath,Boolean wasAlreadyOpen) Opens a 3dm file and makes
it the active document. If called on windows the active document will be saved
and closed and the new document will be opened and become the active document.
If called on the Mac the file will be opened in a new document
window.](/api/rhinocommon/rhino.rhinodoc/open#\(string,out\))

* * *

[**OpenDocuments**() Returns a list of currently open Rhino
documents](/api/rhinocommon/rhino.rhinodoc/opendocuments#\(\))

* * *

[**OpenDocuments**(Boolean includeHeadless) Returns a list of currently open
Rhino documents](/api/rhinocommon/rhino.rhinodoc/opendocuments#\(boolean\))

* * *

[**OpenFile**(String path)
__](/api/rhinocommon/rhino.rhinodoc/openfile#\(string\))

* * *

[**OpenHeadless**(String file3dmPath) Opens a 3DM file into a new headless
RhinoDoc.](/api/rhinocommon/rhino.rhinodoc/openheadless#\(string\))

* * *

[**OpenHeadless**(String filePath, ArchivableDictionary options) Opens a file
into a new headless
RhinoDoc.](/api/rhinocommon/rhino.rhinodoc/openheadless#\(string,archivabledictionary\))

* * *

[**ReadFile**(String path, FileReadOptions options)
](/api/rhinocommon/rhino.rhinodoc/readfile#\(string,filereadoptions\))

* * *

[**ReadFileVersion**() Returns the file version of the current document. Use
this function to determine which version of Rhino last saved the
document.](/api/rhinocommon/rhino.rhinodoc/readfileversion#\(\))

* * *

[**Redo**() Redo the last action that was
"undone"](/api/rhinocommon/rhino.rhinodoc/redo#\(\))

* * *

[**RenderMeshes**(MeshType mt, ViewportInfo vp,Flags flags,PlugIn
plugin,DisplayPipelineAttributes attrs) Returns a set of non-object custom
render primitives for this
document.](/api/rhinocommon/rhino.rhinodoc/rendermeshes#\(meshtype,viewportinfo,ref,plugin,displaypipelineattributes\))

* * *

[**Save**() Save doc to disk using the document's
Path](/api/rhinocommon/rhino.rhinodoc/save#\(\))

* * *

[**SaveAs**(String file3dmPath,Int32 version,Boolean saveSmall,Boolean
saveTextures,Boolean saveGeometryOnly,Boolean savePluginData) Save doc as a
3dm to a specified
path](/api/rhinocommon/rhino.rhinodoc/saveas#\(string,int32,boolean,boolean,boolean,boolean\))

* * *

[**SaveAs**(String file3dmPath,Int32 version) Save doc as a 3dm to a specified
path](/api/rhinocommon/rhino.rhinodoc/saveas#\(string,int32\))

* * *

[**SaveAs**(String file3dmPath) Save doc as a 3dm to a specified path using
the current Rhino file
version](/api/rhinocommon/rhino.rhinodoc/saveas#\(string\))

* * *

[**SaveAsTemplate**(String file3dmTemplatePath,Int32 version) Save this
document as a template to a specific Rhino file
version](/api/rhinocommon/rhino.rhinodoc/saveastemplate#\(string,int32\))

* * *

[**SaveAsTemplate**(String file3dmTemplatePath) Save this document as a
template](/api/rhinocommon/rhino.rhinodoc/saveastemplate#\(string\))

* * *

[**SelectRenderContentInEditor**(RenderContentCollection collection,Boolean
append) Selects a collection of contents in any editors they appear
in.](/api/rhinocommon/rhino.rhinodoc/selectrendercontentineditor#\(rendercontentcollection,boolean\))

* * *

[**SetCustomMeshingParameters**(MeshingParameters mp) Set the custom meshing
parameters that this document will use. You must also modify the
MeshingParameterStyle property on the document to Custom if you want these
meshing parameters to be
used](/api/rhinocommon/rhino.rhinodoc/setcustommeshingparameters#\(meshingparameters\))

* * *

[**SetCustomUnitSystem**(Boolean modelUnits,String customUnitName,Double
metersPerCustomUnit,Boolean scale) Changes the unit system to custom units and
sets the custom unit
scale.](/api/rhinocommon/rhino.rhinodoc/setcustomunitsystem#\(boolean,string,double,boolean\))

* * *

[**SetGridDefaults**(ConstructionPlaneGridDefaults defaults)
](/api/rhinocommon/rhino.rhinodoc/setgriddefaults#\(constructionplanegriddefaults\))

* * *

[**SupportsRenderPrimitiveList**(ViewportInfo
viewport,DisplayPipelineAttributes attrs) __ Determines if custom render
meshes will be built for this document (i.e. - GH
meshes).](/api/rhinocommon/rhino.rhinodoc/supportsrenderprimitivelist#\(viewportinfo,displaypipelineattributes\))

* * *

[**TryGetRenderPrimitiveBoundingBox**(ViewportInfo
viewport,DisplayPipelineAttributes attrs, out BoundingBox boundingBox) __ Get
the bounding box for the custom render meshes associated with this document
(i.e. - GH
meshes).](/api/rhinocommon/rhino.rhinodoc/trygetrenderprimitiveboundingbox#\(viewportinfo,displaypipelineattributes,out\))

* * *

[**Undo**() Undo the last action](/api/rhinocommon/rhino.rhinodoc/undo#\(\))

* * *

[**Write3dmFile**(String path, FileWriteOptions options) Write information in
this document to a .3dm file. Note, the active document's name will not be
changed.](/api/rhinocommon/rhino.rhinodoc/write3dmfile#\(string,filewriteoptions\))

* * *

[**WriteFile**(String path, FileWriteOptions options) Write information in
this document to a file. Note, the active document's name will be changed to
that of the path
provided.](/api/rhinocommon/rhino.rhinodoc/writefile#\(string,filewriteoptions\))

* * *

_keyboard_arrow_down_

Events (35)

[**ActiveDocumentChanged** This event is raised when the active document used
by modeless user interface changes. On Mac Rhino this will get raised before
the <b>NewDocument</b> , <b>BeginOpenDocument</b> and <b>EndOpenDocument</b>
events. Mac Rhino will also raise this event with 0 for the document Id and a
None document pointer when the last document is closed. Windows Rhino will
raise this event after the <b>NewDocument</b> , <b>BeginOpenDocument</b> and
<b>EndOpenDocument</b> events when a new or existing model is
opened.](/api/rhinocommon/rhino.rhinodoc/activedocumentchanged#)

* * *

[**AddRhinoObject** Called if a new object is added to the
document.](/api/rhinocommon/rhino.rhinodoc/addrhinoobject#)

* * *

[**AfterTransformObjects** Called after objects are being
transformed](/api/rhinocommon/rhino.rhinodoc/aftertransformobjects#)

* * *

[**BeforeTransformObjects** Called before objects are being
transformed](/api/rhinocommon/rhino.rhinodoc/beforetransformobjects#)

* * *

[**BeginOpenDocument** This event is raised when the document open operation
begins. NOTE: On Windows, this event will be fired when a clipboard paste
operation occurs, as Rhino opens a .tmp file in the User's Local folder with
the contents of the pasted
document.](/api/rhinocommon/rhino.rhinodoc/beginopendocument#)

* * *

[**BeginSaveDocument** ](/api/rhinocommon/rhino.rhinodoc/beginsavedocument#)

* * *

[**CloseDocument** ](/api/rhinocommon/rhino.rhinodoc/closedocument#)

* * *

[**DeleteRhinoObject** Called if an object is deleted. At some later point the
object can be un-deleted.](/api/rhinocommon/rhino.rhinodoc/deleterhinoobject#)

* * *

[**DeselectAllObjects** Called when all objects are
deselected.](/api/rhinocommon/rhino.rhinodoc/deselectallobjects#)

* * *

[**DeselectObjects** Called when object(s) are
deselected.](/api/rhinocommon/rhino.rhinodoc/deselectobjects#)

* * *

[**DimensionStyleTableEvent** Called when any modification happens to a
document's dimension style
table.](/api/rhinocommon/rhino.rhinodoc/dimensionstyletableevent#)

* * *

[**DocumentPropertiesChanged**
](/api/rhinocommon/rhino.rhinodoc/documentpropertieschanged#)

* * *

[**EndOpenDocument** ](/api/rhinocommon/rhino.rhinodoc/endopendocument#)

* * *

[**EndOpenDocumentInitialiViewUpdate** __ This event is raised after
<b>EndOpenDocument</b> when the documents initial views have been created and
initialized.](/api/rhinocommon/rhino.rhinodoc/endopendocumentinitialiviewupdate#)

* * *

[**EndOpenDocumentInitialViewUpdate** This event is raised after
<b>EndOpenDocument</b> when the documents initial views have been created and
initialized.](/api/rhinocommon/rhino.rhinodoc/endopendocumentinitialviewupdate#)

* * *

[**EndSaveDocument** ](/api/rhinocommon/rhino.rhinodoc/endsavedocument#)

* * *

[**GroupTableEvent** Called when any modification happens to a document's
group table.](/api/rhinocommon/rhino.rhinodoc/grouptableevent#)

* * *

[**HatchPatternTableEvent** Called when any modification happens to a
document's hatch pattern
table.](/api/rhinocommon/rhino.rhinodoc/hatchpatterntableevent#)

* * *

[**InstanceDefinitionTableEvent** Called when any modification happens to a
document's instance definition
table.](/api/rhinocommon/rhino.rhinodoc/instancedefinitiontableevent#)

* * *

[**LayerTableEvent** Called when any modification happens to a document's
layer table.](/api/rhinocommon/rhino.rhinodoc/layertableevent#)

* * *

[**LightTableEvent** Called when any modification happens to a document's
light table.](/api/rhinocommon/rhino.rhinodoc/lighttableevent#)

* * *

[**LinetypeTableEvent** Called when any modification happens to a document's
linetype table.](/api/rhinocommon/rhino.rhinodoc/linetypetableevent#)

* * *

[**MaterialTableEvent** Called when any modification happens to a document's
material table.](/api/rhinocommon/rhino.rhinodoc/materialtableevent#)

* * *

[**ModifyObjectAttributes** Called when all object attributes are
changed.](/api/rhinocommon/rhino.rhinodoc/modifyobjectattributes#)

* * *

[**NewDocument** ](/api/rhinocommon/rhino.rhinodoc/newdocument#)

* * *

[**PurgeRhinoObject** Called if an object is being purged from a document. The
object will cease to exist
forever.](/api/rhinocommon/rhino.rhinodoc/purgerhinoobject#)

* * *

[**RenderEnvironmentTableEvent**
](/api/rhinocommon/rhino.rhinodoc/renderenvironmenttableevent#)

* * *

[**RenderMaterialsTableEvent**
](/api/rhinocommon/rhino.rhinodoc/rendermaterialstableevent#)

* * *

[**RenderTextureTableEvent** Called when the <b>RenderTextureTable</b> has
been loaded, is about to be cleared or has been cleared. See
<b>RenderContentTableEventType</b> for more
information.](/api/rhinocommon/rhino.rhinodoc/rendertexturetableevent#)

* * *

[**ReplaceRhinoObject** Called if an object is about to be replaced. If both
RhinoDoc.UndoActive() and RhinoDoc.RedoActive() return false, then immediately
after the ReplaceObject event, there will be a DeleteObject event followed by
an AddObject event. If either RhinoDoc.UndoActive() or RhinoDoc::RedoActive()
return true, then immediately after the ReplaceObject event, there will be a
DeleteObject event followed by an UndeleteObject
event.](/api/rhinocommon/rhino.rhinodoc/replacerhinoobject#)

* * *

[**SelectObjects** Called when object(s) are
selected.](/api/rhinocommon/rhino.rhinodoc/selectobjects#)

* * *

[**TextureMappingEvent** Called when any modification happens to a document
objects texture
mapping.](/api/rhinocommon/rhino.rhinodoc/texturemappingevent#)

* * *

[**UndeleteRhinoObject** Called if an object is un-
deleted.](/api/rhinocommon/rhino.rhinodoc/undeleterhinoobject#)

* * *

[**UnitsChangedWithScaling** Called when a change in the model units results
in a scaling operation on all of the objects in the document. This call is
made before any of the objects are scaled. A call to
RhinoDoc.DocumentPropertiesChanged
follows.](/api/rhinocommon/rhino.rhinodoc/unitschangedwithscaling#)

* * *

[**UserStringChanged** This event is raised when document user text strings
are changed](/api/rhinocommon/rhino.rhinodoc/userstringchanged#)

* * *

