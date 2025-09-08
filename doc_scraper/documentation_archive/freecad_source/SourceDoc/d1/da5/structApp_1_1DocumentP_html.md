---
url: https://freecad.github.io/SourceDoc/d1/da5/structApp_1_1DocumentP.html
scraped_at: 2025-09-08T14:54:28.455616
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentP](../../d1/da5/structApp_1_1DocumentP.html)

[List of all members](../../df/dc6/structApp_1_1DocumentP-members.html) | Public Member Functions | Static Public Member Functions | Public Attributes

App::DocumentP Struct Reference

##  Public Member Functions  
  
---  
void | [addRecomputeLog](../../d1/da5/structApp_1_1DocumentP.html#aaf1f87bf25a914489c0b6a511f26637f) (const char *why, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
void | [addRecomputeLog](../../d1/da5/structApp_1_1DocumentP.html#a437eefa433d23b9672964e13a8bc9a6e) (const std::string &why, [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
void | [addRecomputeLog](../../d1/da5/structApp_1_1DocumentP.html#ae3969263ba43a8c8e9f3ebe393143523) ([DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) *returnCode)  
void | [clearDocument](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55) ()  
void | [clearRecomputeLog](../../d1/da5/structApp_1_1DocumentP.html#abe4686fb5139ebfdab04dabb67405c3a) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj=nullptr)  
|
[DocumentP](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c)
()  
const char * | [findRecomputeLog](../../d1/da5/structApp_1_1DocumentP.html#a806eec3926c51f0e5357e1ee86708bd6) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [topologicalSort](../../d1/da5/structApp_1_1DocumentP.html#a5a03a65c8fe65bb3dcabc29b448faf9a) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objects) const  
  
##  Static Public Member Functions  
  
---  
static void | [findAllPathsAt](../../d1/da5/structApp_1_1DocumentP.html#a028ece0723e817ca53c9b27ac1d3b555) (const std::vector< [Node](../../df/dd0/classNode.html) > &all_nodes, size_t id, std::vector< [Path](../../da/d2a/classApp_1_1Path.html) > &all_paths, [Path](../../da/d2a/classApp_1_1Path.html) tmp)  
static std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [partialTopologicalSort](../../d1/da5/structApp_1_1DocumentP.html#a9dec0045952043940b9ab4cfaf5a8dc7) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objects)  
  
##  Public Attributes  
  
---  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3)  
[Transaction](../../de/dbf/classApp_1_1Transaction.html) * | [activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b)  
[bool](../../d9/db9/classbool.html) | [committing](../../d1/da5/structApp_1_1DocumentP.html#ac660a92e93876ba22cfcb157dcbcc9a2)  
Py::Object | [DocumentPythonObject](../../d1/da5/structApp_1_1DocumentP.html#add40c1bb1337e43508a99b19d306083a)  
[int](../../d1/da0/classint.html) | [iTransactionMode](../../d1/da5/structApp_1_1DocumentP.html#a3ee50ce0db9761ddce2529bd0b56fad7)  
[int](../../d1/da0/classint.html) | [iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8)  
long | [lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217)  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106)  
std::unordered_map< long, [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3)  
std::unordered_map< std::string, [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886)  
[bool](../../d9/db9/classbool.html) | [opentransaction](../../d1/da5/structApp_1_1DocumentP.html#ac19ad2b3f83eb3acd874542e27f6607c)  
std::unordered_map< std::string, [bool](../../d9/db9/classbool.html) > | [partialLoadObjects](../../d1/da5/structApp_1_1DocumentP.html#a0ccc9352fd58548a8148a35736c00b2d)  
std::vector< [DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html) > | [pendingRemove](../../d1/da5/structApp_1_1DocumentP.html#a153a0ccd9556622fc7190fc6e9d81bc7)  
std::string | [programVersion](../../d1/da5/structApp_1_1DocumentP.html#a9395c4a4c0e81cab96512cdf700e1a48)  
[bool](../../d9/db9/classbool.html) | [rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b)  
std::bitset< 32 > | [StatusBits](../../d1/da5/structApp_1_1DocumentP.html#a22382776a74a5bc0c130d1136d2ec7d2)  
std::unordered_set< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [touchedObjs](../../d1/da5/structApp_1_1DocumentP.html#a7b3a34196818f63f6878c8026e3badc9)  
[bool](../../d9/db9/classbool.html) | [undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6)  
| document in the middle of undo or redo
[More...](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6)  
  
unsigned [int](../../d1/da0/classint.html) | [UndoMaxStackSize](../../d1/da5/structApp_1_1DocumentP.html#a6dc4ef7a82a38c93bc6348125fbb26b7)  
unsigned [int](../../d1/da0/classint.html) | [UndoMemSize](../../d1/da5/structApp_1_1DocumentP.html#a22dd5ded3943792598d2c96703a63a3c)  
  
## Constructor & Destructor Documentation

## ◆ DocumentP()

App::DocumentP::DocumentP  | ( | | ) |   
---|---|---|---|---  
  
References
[activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Document::Closable](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553affc4864219c40e54946a53110d9d3bc2),
[committing](../../d1/da5/structApp_1_1DocumentP.html#ac660a92e93876ba22cfcb157dcbcc9a2),
[iTransactionMode](../../d1/da5/structApp_1_1DocumentP.html#a3ee50ce0db9761ddce2529bd0b56fad7),
[iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8),
[App::Document::KeepTrailingDigits](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a844e41986bdfe3e2ff29054fc8aaeb55),
[lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[opentransaction](../../d1/da5/structApp_1_1DocumentP.html#ac19ad2b3f83eb3acd874542e27f6607c),
[App::Document::Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
[rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
[StatusBits](../../d1/da5/structApp_1_1DocumentP.html#a22382776a74a5bc0c130d1136d2ec7d2),
[undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6),
[UndoMaxStackSize](../../d1/da5/structApp_1_1DocumentP.html#a6dc4ef7a82a38c93bc6348125fbb26b7),
and
[UndoMemSize](../../d1/da5/structApp_1_1DocumentP.html#a22dd5ded3943792598d2c96703a63a3c).

## Member Function Documentation

## ◆ addRecomputeLog() [1/3]

void App::DocumentP::addRecomputeLog  | ( | const char *  | _why_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_  
| ) | |   
  
References
[addRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#aaf1f87bf25a914489c0b6a511f26637f).

Referenced by
[addRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#aaf1f87bf25a914489c0b6a511f26637f),
[App::Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526),
and
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d).

## ◆ addRecomputeLog() [2/3]

void App::DocumentP::addRecomputeLog  | ( | const std::string & | _why_ ,   
---|---|---|---  
|  | [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_  
| ) | |   
  
References
[addRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#aaf1f87bf25a914489c0b6a511f26637f).

## ◆ addRecomputeLog() [3/3]

void App::DocumentP::addRecomputeLog  | ( | [DocumentObjectExecReturn](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html) *  | _returnCode_| ) |   
---|---|---|---|---|---  
  
References
[App::DocumentObject::setStatus()](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815),
and
[App::DocumentObjectExecReturn::Which](../../d4/dea/classApp_1_1DocumentObjectExecReturn.html#a7a0b1845ef5e68fa193f040ce6a9578c).

## ◆ clearDocument()

void App::DocumentP::clearDocument  | ( | | ) |   
---|---|---|---|---  
  
References
[objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
and
[objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

Referenced by
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[App::Document::~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ clearRecomputeLog()

void App::DocumentP::clearRecomputeLog  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ = `nullptr`| ) |   
---|---|---|---|---|---  
  
Referenced by
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[App::Document::recomputeFeature()](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ findAllPathsAt()

| void DocumentP::findAllPathsAt  | ( | const std::vector< [Node](../../df/dd0/classNode.html) > & | _all_nodes_ ,   
---|---|---|---  
|  | size_t  | _id_ ,   
|  | std::vector< [Path](../../da/d2a/classApp_1_1Path.html) > & | _all_paths_ ,   
|  | [Path](../../da/d2a/classApp_1_1Path.html) | _tmp_  
| ) | |   
static  
  
References
[DraftVecUtils::find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
and
[findAllPathsAt()](../../d1/da5/structApp_1_1DocumentP.html#a028ece0723e817ca53c9b27ac1d3b555).

Referenced by
[findAllPathsAt()](../../d1/da5/structApp_1_1DocumentP.html#a028ece0723e817ca53c9b27ac1d3b555),
and
[App::Document::getPathsByOutList()](../../d8/d3e/classApp_1_1Document.html#a6c4fd3b7f7700be4e25980669d35a108).

## ◆ findRecomputeLog()

const char * App::DocumentP::findRecomputeLog  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
Referenced by
[App::Document::getErrorDescription()](../../d8/d3e/classApp_1_1Document.html#a48126d74c0d6bfcf4051bdbcf01840b7).

## ◆ partialTopologicalSort()

| std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > DocumentP::partialTopologicalSort  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objects_| ) |   
---|---|---|---|---|---  
static  
  
Does almost the same as
[topologicalSort()](../../d1/da5/structApp_1_1DocumentP.html#a5a03a65c8fe65bb3dcabc29b448faf9a)
until no object with an input degree of zero can be found. It then searches
for objects with an output degree of zero until neither an object with input
or output degree can be found. The remaining objects form one or multiple
cycles. An alternative to this method might be:
<https://en.wikipedia.org/wiki/Tarjan%E2%80%99s_strongly_connected_components_algorithm>

Referenced by
[App::Document::getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
and
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b).

## ◆ topologicalSort()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > DocumentP::topologicalSort  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objects_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[App::Document::topologicalSort()](../../d8/d3e/classApp_1_1Document.html#a2b52886a0a5853bbba52be579f8c1de3).

## Member Data Documentation

## ◆ activeObject

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::DocumentP::activeObject  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::getActiveObject()](../../d8/d3e/classApp_1_1Document.html#a88cb968643cc950f87ac7d9ec08558b2),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ activeUndoTransaction

[Transaction](../../de/dbf/classApp_1_1Transaction.html)*
App::DocumentP::activeUndoTransaction  
---  
  
Referenced by
[App::Document::abortTransaction()](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041),
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Document::addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02),
[App::Document::clearUndos()](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55),
[App::Document::commitTransaction()](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::getAvailableUndoNames()](../../d8/d3e/classApp_1_1Document.html#af22136a16daca121025484f1dc8865d5),
[App::Document::getAvailableUndos()](../../d8/d3e/classApp_1_1Document.html#acac169e323a61d08b4c48d31337ab672),
[App::Document::getTransactionID()](../../d8/d3e/classApp_1_1Document.html#a5225cf38810fc5cb88614651b7a7927c),
[App::Document::hasPendingTransaction()](../../d8/d3e/classApp_1_1Document.html#ab97646f7a46c3ea81b5a9f1df49810a1),
[App::Document::isTransactionEmpty()](../../d8/d3e/classApp_1_1Document.html#a150a71231a1d5695d6d7c220b5044e81),
[App::Document::onBeforeChangeProperty()](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb),
[App::Document::redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[App::Document::renameTransaction()](../../d8/d3e/classApp_1_1Document.html#a558ba4c9f9ba3652ff53273d95b8f575),
and
[App::Document::undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ committing

[bool](../../d9/db9/classbool.html) App::DocumentP::committing  
---  
  
Referenced by
[App::Document::abortTransaction()](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041),
[App::Document::clearUndos()](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55),
[App::Document::commitTransaction()](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
and
[App::Document::openTransaction()](../../d8/d3e/classApp_1_1Document.html#a8e5586f3164279fa8f4dcbfd42009688).

## ◆ DocumentPythonObject

Py::Object App::DocumentP::DocumentPythonObject  
---  
  
Referenced by
[App::Document::Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[App::Document::getPyObject()](../../d8/d3e/classApp_1_1Document.html#a3eafa7c3d20b42cb6c41d9623c2476c7),
and
[App::Document::~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ iTransactionMode

[int](../../d1/da0/classint.html) App::DocumentP::iTransactionMode  
---  
  
Referenced by
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
and
[App::Document::setTransactionMode()](../../d8/d3e/classApp_1_1Document.html#a0416181588536896bd37f98d851bd3ef).

## ◆ iUndoMode

[int](../../d1/da0/classint.html) App::DocumentP::iUndoMode  
---  
  
Referenced by
[App::Document::addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::getUndoMode()](../../d8/d3e/classApp_1_1Document.html#a613150506dd435ddaff24e068bfeb87f),
[App::Document::moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5),
[App::Document::redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[App::Document::setUndoMode()](../../d8/d3e/classApp_1_1Document.html#a4339c7121daa9a2b5627b53a584eafa5),
and
[App::Document::undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ lastObjectId

long App::DocumentP::lastObjectId  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ objectArray

std::vector<[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>
App::DocumentP::objectArray  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[App::Document::breakDependency()](../../d8/d3e/classApp_1_1Document.html#af9123db5f932f908555bd61c8db2fb53),
[clearDocument()](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[App::Document::countObjects()](../../d8/d3e/classApp_1_1Document.html#a0b050a2ce85d114c54c1a099ea4e80c4),
[App::Document::findObjects()](../../d8/d3e/classApp_1_1Document.html#a1ce3aa1d4d9e6448af5b0721c55614f2),
[App::Document::getDependingObjects()](../../d8/d3e/classApp_1_1Document.html#afbf82bb93c0dde39c082fa5c497d0c1a),
[App::Document::getLinksTo()](../../d8/d3e/classApp_1_1Document.html#a68fa1555a634a2da10ba434f64fbf2f2),
[App::Document::getMemSize()](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043),
[App::Document::getObjects()](../../d8/d3e/classApp_1_1Document.html#a9eb8bb2a620e09a4b164f019c3b3b07f),
[App::Document::getObjectsOfType()](../../d8/d3e/classApp_1_1Document.html#a021b2b66d4263ca1f0e9879e7bbd5ef4),
[App::Document::getObjectsWithExtension()](../../d8/d3e/classApp_1_1Document.html#ae8e6bb0f8690f2a30873507c96845067),
[App::Document::getPathsByOutList()](../../d8/d3e/classApp_1_1Document.html#a6c4fd3b7f7700be4e25980669d35a108),
[App::Document::getRootObjects()](../../d8/d3e/classApp_1_1Document.html#ad0d9b0148c764813dfc9d4dc103b458b),
[App::Document::getTouched()](../../d8/d3e/classApp_1_1Document.html#a5937372831728bf9703d2e97bc0f3b49),
[App::Document::isTouched()](../../d8/d3e/classApp_1_1Document.html#ac4b4943f002a0c5b6a07c86bdfca2af0),
[App::Document::mustExecute()](../../d8/d3e/classApp_1_1Document.html#aaaf7a0d2a67cc06d760a16c352117189),
[App::Document::purgeTouched()](../../d8/d3e/classApp_1_1Document.html#a722e7602c46544db160b2740f2dad7a1),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[App::Document::redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[App::Document::renameObjectIdentifiers()](../../d8/d3e/classApp_1_1Document.html#a4ee1ea277688bb08d607a83108434e8b),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
[App::Document::Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
[App::Document::topologicalSort()](../../d8/d3e/classApp_1_1Document.html#a2b52886a0a5853bbba52be579f8c1de3),
and
[App::Document::undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ objectIdMap

std::unordered_map<long,[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>
App::DocumentP::objectIdMap  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[clearDocument()](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[App::Document::getObjectByID()](../../d8/d3e/classApp_1_1Document.html#affd903adb0b7171d0a8005d4f68fed26),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ objectMap

std::unordered_map<std::string,[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>
App::DocumentP::objectMap  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[clearDocument()](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[App::Document::countObjectsOfType()](../../d8/d3e/classApp_1_1Document.html#a877e33cf978e77ccbce48015575c419a),
[App::Document::getInList()](../../d8/d3e/classApp_1_1Document.html#aea0ddc50d73293e7275afa6102d9d8e3),
[App::Document::getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[App::Document::getObjectName()](../../d8/d3e/classApp_1_1Document.html#abb019c18dfcdce538ecf3ed8723c7fd8),
[App::Document::getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[App::Document::isIn()](../../d8/d3e/classApp_1_1Document.html#af4495f21bf5ea0ba95e83a5572dcca18),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[App::Document::writeDependencyGraphViz()](../../d8/d3e/classApp_1_1Document.html#aa97d82747fbbc5eb56dccae567276eca).

## ◆ opentransaction

[bool](../../d9/db9/classbool.html) App::DocumentP::opentransaction  
---  
  
Referenced by
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c).

## ◆ partialLoadObjects

std::unordered_map<std::string, [bool](../../d9/db9/classbool.html)>
App::DocumentP::partialLoadObjects  
---  
  
Referenced by
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ pendingRemove

std::vector<[DocumentObjectT](../../d5/d07/classApp_1_1DocumentObjectT.html)>
App::DocumentP::pendingRemove  
---  
  
Referenced by
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
and
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ programVersion

std::string App::DocumentP::programVersion  
---  
  
Referenced by
[App::Document::getProgramVersion()](../../d8/d3e/classApp_1_1Document.html#a79010a627356fbd2e58ee59acb6979a8),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ rollback

[bool](../../d9/db9/classbool.html) App::DocumentP::rollback  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[App::Document::addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2),
[App::Document::moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5),
[App::Document::onBeforeChangeProperty()](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
and
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ StatusBits

std::bitset<32> App::DocumentP::StatusBits  
---  
  
Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
and
[App::Document::setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525).

## ◆ touchedObjs

std::unordered_set<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>
App::DocumentP::touchedObjs  
---  
  
Referenced by
[App::Document::addRecomputeObject()](../../d8/d3e/classApp_1_1Document.html#ae9cd6dab5c67b88e24bcfb54a15fc273),
[App::Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526),
[App::Document::readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
and
[App::Document::Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82).

## ◆ undoing

[bool](../../d9/db9/classbool.html) App::DocumentP::undoing  
---  
  
document in the middle of undo or redo

Referenced by
[App::Document::addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::Document::addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[App::Document::redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[App::Document::removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
and
[App::Document::undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ UndoMaxStackSize

unsigned [int](../../d1/da0/classint.html) App::DocumentP::UndoMaxStackSize  
---  
  
Referenced by
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::getMaxUndoStackSize()](../../d8/d3e/classApp_1_1Document.html#a84e4eaaf2f02eebb8327f8460954cc3f),
and
[App::Document::setMaxUndoStackSize()](../../d8/d3e/classApp_1_1Document.html#a3d450a34c7847d5bb3e645680fd87263).

## ◆ UndoMemSize

unsigned [int](../../d1/da0/classint.html) App::DocumentP::UndoMemSize  
---  
  
Referenced by
[DocumentP()](../../d1/da5/structApp_1_1DocumentP.html#a3dffeb9a2d965028e3548bdf828fed4c),
[App::Document::getUndoMemSize()](../../d8/d3e/classApp_1_1Document.html#aebe1ae8ccbb1e5b3b6506019d61c7eb9),
and
[App::Document::setUndoLimit()](../../d8/d3e/classApp_1_1Document.html#a8a2e90d8933a8c9fb9e7e340cc9e3b53).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/App/Document.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

