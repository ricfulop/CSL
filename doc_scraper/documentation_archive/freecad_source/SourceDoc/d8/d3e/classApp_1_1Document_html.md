---
url: https://freecad.github.io/SourceDoc/d8/d3e/classApp_1_1Document.html
scraped_at: 2025-09-08T14:53:43.575614
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Document](../../d8/d3e/classApp_1_1Document.html)

[List of all members](../../d7/dec/classApp_1_1Document-members.html) | Public Types

App::Document Class Reference

The document class. [More...](../../d8/d3e/classApp_1_1Document.html#details)

`#include <Document.h>`

##  Public Types  
  
---  
enum | [Status](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553) {   
[SkipRecompute](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aecae1faa96484511bd35e20a0bcab282)
= 0 ,
[KeepTrailingDigits](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a844e41986bdfe3e2ff29054fc8aaeb55)
= 1 ,
[Closable](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553affc4864219c40e54946a53110d9d3bc2)
= 2 ,
[Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec)
= 3 ,  
[Recomputing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a35908c043062d1d561b96076a57b5b32)
= 4 ,
[PartialRestore](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aa85fb1ecccf6466736187e1826eab209)
= 5 ,
[Importing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3fcdf22c3e8c2aea788606a837c7d522)
= 6 ,
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf)
= 7 ,  
[AllowPartialRecompute](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a8bf799934fb81b4af0577ad152be9e93)
= 8 ,
[TempDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af2a790c9309723635970664f9ce29418)
= 9 ,
[RestoreError](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aad5db64342c0a663e0710bfd56df097c)
= 10 ,
[LinkStampChanged](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af9b330124dbe14c0e1b2087e73b814da)
= 11 ,  
[IgnoreErrorOnRecompute](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a0786076bef512cce0c26a011a6f2130b)
= 12  
}  
  
##  Public Member Functions  
  
---  
Object handling <br>  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [addObject](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771) (const char *sType, const char *pObjectName=nullptr, [bool](../../d9/db9/classbool.html) isNew=true, const char *viewType=nullptr, [bool](../../d9/db9/classbool.html) isPartial=false)  
| Add a feature of sType with sName (ASCII) to this document and set it
active.
[More...](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [addObjects](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4) (const char *sType, const std::vector< std::string > &objectNames, [bool](../../d9/db9/classbool.html) isNew=true)  
| Add an array of features of the given types and names.
[More...](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4)  
  
void | [removeObject](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33) (const char *sName)  
| Remove a feature out of the document.
[More...](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33)  
  
void | [addObject](../../d8/d3e/classApp_1_1Document.html#a77502422ab7bde4fb01ab4474fd930af) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, const char *pObjectName=nullptr)  
| Add an existing feature with sName (ASCII) to this document and set it
active.
[More...](../../d8/d3e/classApp_1_1Document.html#a77502422ab7bde4fb01ab4474fd930af)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [copyObject](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0) (const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [bool](../../d9/db9/classbool.html) recursive=false, [bool](../../d9/db9/classbool.html) returnAll=false)  
| Copy objects from another document to this document.
[More...](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [moveObject](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [bool](../../d9/db9/classbool.html) recursive=false)  
| Move an object from another document to this document If _recursive_ is true
then all objects this object depends on are moved as well.
[More...](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getActiveObject](../../d8/d3e/classApp_1_1Document.html#a88cb968643cc950f87ac7d9ec08558b2) (void) const  
| Returns the active Object of this document.
[More...](../../d8/d3e/classApp_1_1Document.html#a88cb968643cc950f87ac7d9ec08558b2)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getObject](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221) (const char *Name) const  
| Returns a Object of this document.
[More...](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221)  
  
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [getObjectByID](../../d8/d3e/classApp_1_1Document.html#affd903adb0b7171d0a8005d4f68fed26) (long id) const  
| Returns a Object of this document by its id.
[More...](../../d8/d3e/classApp_1_1Document.html#affd903adb0b7171d0a8005d4f68fed26)  
  
[bool](../../d9/db9/classbool.html) | [isIn](../../d8/d3e/classApp_1_1Document.html#af4495f21bf5ea0ba95e83a5572dcca18) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *pFeat) const  
| Returns true if the
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") is contained in this document.
[More...](../../d8/d3e/classApp_1_1Document.html#af4495f21bf5ea0ba95e83a5572dcca18)  
  
const char * | [getObjectName](../../d8/d3e/classApp_1_1Document.html#abb019c18dfcdce538ecf3ed8723c7fd8) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *pFeat) const  
| Returns a Name of an Object or 0.
[More...](../../d8/d3e/classApp_1_1Document.html#abb019c18dfcdce538ecf3ed8723c7fd8)  
  
std::string | [getUniqueObjectName](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9) (const char *Name) const  
| Returns a Name of an Object or 0.
[More...](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9)  
  
std::string | [getStandardObjectName](../../d8/d3e/classApp_1_1Document.html#a3d17fc869ebcefabfa83b1adb5665ec5) (const char *Name, [int](../../d1/da0/classint.html) d) const  
| Returns a name of the form prefix_number. d specifies the number of digits.
[More...](../../d8/d3e/classApp_1_1Document.html#a3d17fc869ebcefabfa83b1adb5665ec5)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getDependingObjects](../../d8/d3e/classApp_1_1Document.html#afbf82bb93c0dde39c082fa5c497d0c1a) () const  
| Returns a list of document's objects including the dependencies.
[More...](../../d8/d3e/classApp_1_1Document.html#afbf82bb93c0dde39c082fa5c497d0c1a)  
  
const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | [getObjects](../../d8/d3e/classApp_1_1Document.html#a9eb8bb2a620e09a4b164f019c3b3b07f) () const  
| Returns a list of all Objects.
[More...](../../d8/d3e/classApp_1_1Document.html#a9eb8bb2a620e09a4b164f019c3b3b07f)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getObjectsOfType](../../d8/d3e/classApp_1_1Document.html#a021b2b66d4263ca1f0e9879e7bbd5ef4) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId) const  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getObjectsWithExtension](../../d8/d3e/classApp_1_1Document.html#ae8e6bb0f8690f2a30873507c96845067) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId, [bool](../../d9/db9/classbool.html) derived=true) const  
| Returns all object with given extensions. If derived=true also all objects
with extensions derived from the given one.
[More...](../../d8/d3e/classApp_1_1Document.html#ae8e6bb0f8690f2a30873507c96845067)  
  
std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [findObjects](../../d8/d3e/classApp_1_1Document.html#a1ce3aa1d4d9e6448af5b0721c55614f2) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId, const char *objname, const char *label) const  
template<typename T >  
std::vector< T * > | [getObjectsOfType](../../d8/d3e/classApp_1_1Document.html#ad2e63817274934f5c148456ac593d8f0) () const  
| Returns an array with the correct types already.
[More...](../../d8/d3e/classApp_1_1Document.html#ad2e63817274934f5c148456ac593d8f0)  
  
[int](../../d1/da0/classint.html) | [countObjectsOfType](../../d8/d3e/classApp_1_1Document.html#a877e33cf978e77ccbce48015575c419a) (const [Base::Type](../../dc/dee/classBase_1_1Type.html) &typeId) const  
[int](../../d1/da0/classint.html) | [countObjects](../../d8/d3e/classApp_1_1Document.html#a0b050a2ce85d114c54c1a099ea4e80c4) (void) const  
| get the number of objects in the document
[More...](../../d8/d3e/classApp_1_1Document.html#a0b050a2ce85d114c54c1a099ea4e80c4)  
  
methods for modification and state handling  
void | [purgeTouched](../../d8/d3e/classApp_1_1Document.html#a722e7602c46544db160b2740f2dad7a1) ()  
| Remove all modifications. After this call The document becomes Valid again.
[More...](../../d8/d3e/classApp_1_1Document.html#a722e7602c46544db160b2740f2dad7a1)  
  
[bool](../../d9/db9/classbool.html) | [isTouched](../../d8/d3e/classApp_1_1Document.html#ac4b4943f002a0c5b6a07c86bdfca2af0) (void) const  
| check if there is any touched object in this document
[More...](../../d8/d3e/classApp_1_1Document.html#ac4b4943f002a0c5b6a07c86bdfca2af0)  
  
[bool](../../d9/db9/classbool.html) | [mustExecute](../../d8/d3e/classApp_1_1Document.html#aaaf7a0d2a67cc06d760a16c352117189) (void) const  
| check if there is any object must execute in this document
[More...](../../d8/d3e/classApp_1_1Document.html#aaaf7a0d2a67cc06d760a16c352117189)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getTouched](../../d8/d3e/classApp_1_1Document.html#a5937372831728bf9703d2e97bc0f3b49) (void) const  
| returns all touched objects
[More...](../../d8/d3e/classApp_1_1Document.html#a5937372831728bf9703d2e97bc0f3b49)  
  
void | [setClosable](../../d8/d3e/classApp_1_1Document.html#a1c567b02a884388035b005a0d7479e9b) ([bool](../../d9/db9/classbool.html))  
| set the document to be closable, this is on by default.
[More...](../../d8/d3e/classApp_1_1Document.html#a1c567b02a884388035b005a0d7479e9b)  
  
[bool](../../d9/db9/classbool.html) | [isClosable](../../d8/d3e/classApp_1_1Document.html#a5e0c6ac230060e945dc269b40bb86958) () const  
| check whether the document can be closed
[More...](../../d8/d3e/classApp_1_1Document.html#a5e0c6ac230060e945dc269b40bb86958)  
  
[int](../../d1/da0/classint.html) | [recompute](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs={}, [bool](../../d9/db9/classbool.html) force=false, [bool](../../d9/db9/classbool.html) *hasError=nullptr, [int](../../d1/da0/classint.html) options=0)  
| Recompute touched features and return the number of recalculated features.
[More...](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b)  
  
[bool](../../d9/db9/classbool.html) | [recomputeFeature](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *Feat, [bool](../../d9/db9/classbool.html) recursive=false)  
| Recompute only one feature.
[More...](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a)  
  
const char * | [getErrorDescription](../../d8/d3e/classApp_1_1Document.html#a48126d74c0d6bfcf4051bdbcf01840b7) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) const  
| get the text of the error of a specified object
[More...](../../d8/d3e/classApp_1_1Document.html#a48126d74c0d6bfcf4051bdbcf01840b7)  
  
[bool](../../d9/db9/classbool.html) | [testStatus](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87) ([Status](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553) pos) const  
| return the status bits
[More...](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87)  
  
void | [setStatus](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525) ([Status](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553) pos, [bool](../../d9/db9/classbool.html) on)  
| set the status bits
[More...](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525)  
  
methods for the UNDO REDO and Transaction handling  
Introduce a new concept of transaction ID. Each transaction must be unique
inside the document. Multiple transactions from different documents can be
grouped together with the same transaction ID. When undo,
[Gui](../../d9/dad/namespaceGui.html "The FreeCAD Graphical interface layer.")
component can query getAvailableUndo(id) to see if it is possible to undo with
a given ID. If there more than one undo transactions, meaning that there are
other transactions before the given ID. The
[Gui](../../d9/dad/namespaceGui.html "The FreeCAD Graphical interface layer.")
component shall ask user if they want to undo multiple steps. And if the user
agrees, call undo(id) to unroll all transaction before and including the the
one with the give ID. Same applies for redo. The new transaction ID describe
here is fully backward compatible. Calling the APIs with a default id=0 gives
the original behavior.  
void | [setUndoMode](../../d8/d3e/classApp_1_1Document.html#a4339c7121daa9a2b5627b53a584eafa5) ([int](../../d1/da0/classint.html) iMode)  
| switch the level of Undo/Redo
[More...](../../d8/d3e/classApp_1_1Document.html#a4339c7121daa9a2b5627b53a584eafa5)  
  
[int](../../d1/da0/classint.html) | [getUndoMode](../../d8/d3e/classApp_1_1Document.html#a613150506dd435ddaff24e068bfeb87f) (void) const  
| switch the level of Undo/Redo
[More...](../../d8/d3e/classApp_1_1Document.html#a613150506dd435ddaff24e068bfeb87f)  
  
void | [setTransactionMode](../../d8/d3e/classApp_1_1Document.html#a0416181588536896bd37f98d851bd3ef) ([int](../../d1/da0/classint.html) iMode)  
| switch the transaction mode
[More...](../../d8/d3e/classApp_1_1Document.html#a0416181588536896bd37f98d851bd3ef)  
  
void | [openTransaction](../../d8/d3e/classApp_1_1Document.html#a8e5586f3164279fa8f4dcbfd42009688) (const char *name=nullptr)  
| Open a new command Undo/Redo, an UTF-8 name can be specified.
[More...](../../d8/d3e/classApp_1_1Document.html#a8e5586f3164279fa8f4dcbfd42009688)  
  
void | [renameTransaction](../../d8/d3e/classApp_1_1Document.html#a558ba4c9f9ba3652ff53273d95b8f575) (const char *name, [int](../../d1/da0/classint.html) id)  
| Rename the current transaction if the id matches.
[More...](../../d8/d3e/classApp_1_1Document.html#a558ba4c9f9ba3652ff53273d95b8f575)  
  
void | [commitTransaction](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01) ()  
| Commit the Command transaction. Do nothing If there is no Command
transaction open.
[More...](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01)  
  
void | [abortTransaction](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041) ()  
| Abort the actually running transaction.
[More...](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041)  
  
[bool](../../d9/db9/classbool.html) | [hasPendingTransaction](../../d8/d3e/classApp_1_1Document.html#ab97646f7a46c3ea81b5a9f1df49810a1) () const  
| Check if a transaction is open.
[More...](../../d8/d3e/classApp_1_1Document.html#ab97646f7a46c3ea81b5a9f1df49810a1)  
  
[int](../../d1/da0/classint.html) | [getTransactionID](../../d8/d3e/classApp_1_1Document.html#a5225cf38810fc5cb88614651b7a7927c) ([bool](../../d9/db9/classbool.html) [undo](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078), unsigned pos=0) const  
| Return the undo/redo transaction ID starting from the back.
[More...](../../d8/d3e/classApp_1_1Document.html#a5225cf38810fc5cb88614651b7a7927c)  
  
[bool](../../d9/db9/classbool.html) | [isTransactionEmpty](../../d8/d3e/classApp_1_1Document.html#a150a71231a1d5695d6d7c220b5044e81) () const  
| Check if a transaction is open and its list is empty.
[More...](../../d8/d3e/classApp_1_1Document.html#a150a71231a1d5695d6d7c220b5044e81)  
  
void | [setUndoLimit](../../d8/d3e/classApp_1_1Document.html#a8a2e90d8933a8c9fb9e7e340cc9e3b53) (unsigned [int](../../d1/da0/classint.html) UndoMemSize=0)  
| Set the Undo limit in Byte!
[More...](../../d8/d3e/classApp_1_1Document.html#a8a2e90d8933a8c9fb9e7e340cc9e3b53)  
  
unsigned [int](../../d1/da0/classint.html) | [getUndoMemSize](../../d8/d3e/classApp_1_1Document.html#aebe1ae8ccbb1e5b3b6506019d61c7eb9) (void) const  
| Returns the actual memory consumption of the Undo redo stuff.
[More...](../../d8/d3e/classApp_1_1Document.html#aebe1ae8ccbb1e5b3b6506019d61c7eb9)  
  
void | [setMaxUndoStackSize](../../d8/d3e/classApp_1_1Document.html#a3d450a34c7847d5bb3e645680fd87263) (unsigned [int](../../d1/da0/classint.html) UndoMaxStackSize=20)  
| Set the Undo limit as stack size.
[More...](../../d8/d3e/classApp_1_1Document.html#a3d450a34c7847d5bb3e645680fd87263)  
  
unsigned [int](../../d1/da0/classint.html) | [getMaxUndoStackSize](../../d8/d3e/classApp_1_1Document.html#a84e4eaaf2f02eebb8327f8460954cc3f) (void) const  
| Set the Undo limit as stack size.
[More...](../../d8/d3e/classApp_1_1Document.html#a84e4eaaf2f02eebb8327f8460954cc3f)  
  
void | [clearUndos](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55) ()  
| Remove all stored Undos and Redos.
[More...](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55)  
  
[int](../../d1/da0/classint.html) | [getAvailableUndos](../../d8/d3e/classApp_1_1Document.html#acac169e323a61d08b4c48d31337ab672) ([int](../../d1/da0/classint.html) id=0) const  
| Returns the number of stored Undos. If greater than 0 Undo will be
effective.
[More...](../../d8/d3e/classApp_1_1Document.html#acac169e323a61d08b4c48d31337ab672)  
  
std::vector< std::string > | [getAvailableUndoNames](../../d8/d3e/classApp_1_1Document.html#af22136a16daca121025484f1dc8865d5) () const  
| Returns a list of the Undo names.
[More...](../../d8/d3e/classApp_1_1Document.html#af22136a16daca121025484f1dc8865d5)  
  
[bool](../../d9/db9/classbool.html) | [undo](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078) ([int](../../d1/da0/classint.html) id=0)  
| Will UNDO one step, returns False if no undo was done (Undos == 0).
[More...](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078)  
  
[int](../../d1/da0/classint.html) | [getAvailableRedos](../../d8/d3e/classApp_1_1Document.html#a58e3a99956098cd84095f0dd6faee615) ([int](../../d1/da0/classint.html) id=0) const  
| Returns the number of stored Redos. If greater than 0 Redo will be
effective.
[More...](../../d8/d3e/classApp_1_1Document.html#a58e3a99956098cd84095f0dd6faee615)  
  
std::vector< std::string > | [getAvailableRedoNames](../../d8/d3e/classApp_1_1Document.html#add7924621ee2b9d97b581d894ee38bac) () const  
| Returns a list of the Redo names.
[More...](../../d8/d3e/classApp_1_1Document.html#add7924621ee2b9d97b581d894ee38bac)  
  
[bool](../../d9/db9/classbool.html) | [redo](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003) ([int](../../d1/da0/classint.html) id=0)  
| Will REDO one step, returns False if no redo was done (Redos == 0).
[More...](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003)  
  
[bool](../../d9/db9/classbool.html) | [isPerformingTransaction](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2) () const  
| returns true if the document is in an
[Transaction](../../de/dbf/classApp_1_1Transaction.html "Represents a atomic
transaction of the document.") phase, e.g. currently performing a redo/undo or
rollback
[More...](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2)  
  
void | [addOrRemovePropertyOfObject](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02) ([TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *, [Property](../../d0/da9/classApp_1_1Property.html) *prop, [bool](../../d9/db9/classbool.html) add)  
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
  
  
##  Public Attributes  
  
---  
Properties  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81)  
| holds the long name of the document (utf-8 coded)
[More...](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae)  
| full qualified (with path) file name (utf-8 coded)
[More...](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [CreatedBy](../../d8/d3e/classApp_1_1Document.html#a6da238ba27b4d5dbd3861c8fd4ece5fe)  
| creators name (utf-8)
[More...](../../d8/d3e/classApp_1_1Document.html#a6da238ba27b4d5dbd3861c8fd4ece5fe)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [CreationDate](../../d8/d3e/classApp_1_1Document.html#ad699ff3487ec1cb353626db12f0b7a5e)  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [LastModifiedBy](../../d8/d3e/classApp_1_1Document.html#a854ee4bf3d52fe90ed93d91d92767f03)  
| user last modified the document
[More...](../../d8/d3e/classApp_1_1Document.html#a854ee4bf3d52fe90ed93d91d92767f03)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [LastModifiedDate](../../d8/d3e/classApp_1_1Document.html#a0a381c4d900a31c8cb7d4ef575176768)  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Company](../../d8/d3e/classApp_1_1Document.html#a0b47f89716092bd850cdf61e9e2d0dd7)  
| company name UTF8(optional)
[More...](../../d8/d3e/classApp_1_1Document.html#a0b47f89716092bd850cdf61e9e2d0dd7)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Comment](../../d8/d3e/classApp_1_1Document.html#ad015397935c7246a30af4e9422c470d8)  
| long comment or description (UTF8 with line breaks)
[More...](../../d8/d3e/classApp_1_1Document.html#ad015397935c7246a30af4e9422c470d8)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [Id](../../d8/d3e/classApp_1_1Document.html#ab5d5e73c8bdd011bf1a5737e924e5019)  
| Id e.g. [Part](../../da/d8d/classApp_1_1Part.html "Base class of all
geometric document objects.") number.
[More...](../../d8/d3e/classApp_1_1Document.html#ab5d5e73c8bdd011bf1a5737e924e5019)  
  
[PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html) | [Uid](../../d8/d3e/classApp_1_1Document.html#af3b3acc44a20bd990bf2e97f5116d3c6)  
| unique identifier of the document
[More...](../../d8/d3e/classApp_1_1Document.html#af3b3acc44a20bd990bf2e97f5116d3c6)  
  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [License](../../d8/d3e/classApp_1_1Document.html#a318812adbc89a1288160dc3baa7baa95)  
| License string Holds the short license string for the Item, e.g.
[More...](../../d8/d3e/classApp_1_1Document.html#a318812adbc89a1288160dc3baa7baa95)  
  
[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [LicenseURL](../../d8/d3e/classApp_1_1Document.html#a82b097da462899f58de239ebf1b602ed)  
| License description/contract URL.
[More...](../../d8/d3e/classApp_1_1Document.html#a82b097da462899f58de239ebf1b602ed)  
  
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html) | [Meta](../../d8/d3e/classApp_1_1Document.html#af75d7b6beaa8a7c3576c9b56d0c0b51e)  
| [Meta](../../d9/dcf/namespaceApp_1_1Meta.html) descriptions.
[More...](../../d8/d3e/classApp_1_1Document.html#af75d7b6beaa8a7c3576c9b56d0c0b51e)  
  
[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html) | [Material](../../d8/d3e/classApp_1_1Document.html#ab1bfd5f088f8e60c6b34c92b25410299)  
| [Material](../../da/d47/classApp_1_1Material.html "Material class.")
descriptions, used and defined in the
[Material](../../da/d47/classApp_1_1Material.html "Material class.") module.
[More...](../../d8/d3e/classApp_1_1Document.html#ab1bfd5f088f8e60c6b34c92b25410299)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [TransientDir](../../d8/d3e/classApp_1_1Document.html#ac90f8f59e978c2dbd5b043461852628f)  
| read-only name of the temp dir created when the document is opened
[More...](../../d8/d3e/classApp_1_1Document.html#ac90f8f59e978c2dbd5b043461852628f)  
  
[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html) | [Tip](../../d8/d3e/classApp_1_1Document.html#aba7262694bf2514f516c74bb90bb7de9)  
| Tip object of the document (if any)
[More...](../../d8/d3e/classApp_1_1Document.html#aba7262694bf2514f516c74bb90bb7de9)  
  
[PropertyString](../../dd/df8/classApp_1_1PropertyString.html) | [TipName](../../d8/d3e/classApp_1_1Document.html#a334536a52d758261510975cad0bcce64)  
| Tip object of the document (if any)
[More...](../../d8/d3e/classApp_1_1Document.html#a334536a52d758261510975cad0bcce64)  
  
[PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html) | [ShowHidden](../../d8/d3e/classApp_1_1Document.html#ad993906aa4a429aa7882fc17160cc65e)  
| Whether to show hidden items in TreeView.
[More...](../../d8/d3e/classApp_1_1Document.html#ad993906aa4a429aa7882fc17160cc65e)  
  
  
## File handling of the document  
  
---  
enum | [ExportStatus](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81db) { [NotExporting](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81dba2ccba4649e0148c3fbe078a631ed5049) , [Exporting](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81dba7e7c28bbc0d0fa1bbf3fd707cd96fdbd) }  
[bool](../../d9/db9/classbool.html) | [save](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c) (void)  
| Save the [Document](../../d8/d3e/classApp_1_1Document.html "The document
class.") under a new Name.
[More...](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c)  
  
[bool](../../d9/db9/classbool.html) | [saveAs](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee) (const char *file)  
[bool](../../d9/db9/classbool.html) | [saveCopy](../../d8/d3e/classApp_1_1Document.html#acbad1e96391e2f6067dfdf23a9bdb044) (const char *file) const  
void | [restore](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461) (const char *filename=nullptr, [bool](../../d9/db9/classbool.html) delaySignal=false, const std::vector< std::string > &objNames={})  
| Restore the document from the file in
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.")
[Path](../../da/d2a/classApp_1_1Path.html "Base class of all geometric
document objects.").
[More...](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461)  
  
[bool](../../d9/db9/classbool.html) | [afterRestore](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5) ([bool](../../d9/db9/classbool.html) checkPartial=false)  
[bool](../../d9/db9/classbool.html) | [afterRestore](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, [bool](../../d9/db9/classbool.html) checkPartial=false)  
[ExportStatus](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81db) | [isExporting](../../d8/d3e/classApp_1_1Document.html#a6d98568ff827987b0d4f734f0b0df135) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj) const  
void | [exportObjects](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, std::ostream &)  
void | [exportGraphviz](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122) (std::ostream &) const  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [importObjects](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [importLinks](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs={})  
| [Import](../../df/df2/namespaceImport.html) any externally linked objects.
[More...](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778)  
  
[bool](../../d9/db9/classbool.html) | [isSaved](../../d8/d3e/classApp_1_1Document.html#a730da4f4ddab904051e5f1a031577b27) () const  
| Opens the document from its file name.
[More...](../../d8/d3e/classApp_1_1Document.html#a730da4f4ddab904051e5f1a031577b27)  
  
const char * | [getName](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d) () const  
| Get the document name.
[More...](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d)  
  
const char * | [getProgramVersion](../../d8/d3e/classApp_1_1Document.html#a79010a627356fbd2e58ee59acb6979a8) () const  
| Get program version the project file was created with.
[More...](../../d8/d3e/classApp_1_1Document.html#a79010a627356fbd2e58ee59acb6979a8)  
  
const char * | [getFileName](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d) () const  
| Returned filename.
[More...](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d)  
  
virtual void | [Save](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0) ([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const override  
| This method is used to save properties to an XML document.
[More...](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0)  
  
virtual void | [Restore](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader) override  
| This method is used to restore properties from an XML document.
[More...](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82)  
  
unsigned [int](../../d1/da0/classint.html) | [getMemSize](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043) (void) const override  
| returns the complete document memory consumption, including all managed
DocObjects and Undo Redo.
[More...](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043)  
  
  
## dependency stuff  
  
---  
enum | [DependencyOption](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34) { [DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926) = 1 , [DepNoXLinked](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a76564d229c609eca9e50b9dab37f1e3c) = 2 , [DepNoCycle](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a203f88eb740201a9839da30f2831bc86) = 4 }  
| Option bit flags used by getDepenencyList()
[More...](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34)  
  
class | [Application](../../d8/d3e/classApp_1_1Document.html#a23f25bcc02a0e94c2f5a4188496b04d0)  
class | [TransactionalObject](../../d8/d3e/classApp_1_1Document.html#a1ff14d1b62b77c2e678ca9ead6cf0f1b)  
| because of transaction handling
[More...](../../d8/d3e/classApp_1_1Document.html#a1ff14d1b62b77c2e678ca9ead6cf0f1b)  
  
class | [DocumentObject](../../d8/d3e/classApp_1_1Document.html#a61c9afd284efef8868e6a15bfd7749b7)  
| The [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base
class of all Classes handled in the Document.") that will own the expression.
[More...](../../d8/d3e/classApp_1_1Document.html#a61c9afd284efef8868e6a15bfd7749b7)  
  
class | [Transaction](../../d8/d3e/classApp_1_1Document.html#a49982aa325e19f0956d42fde9132caa2)  
class | [TransactionDocumentObject](../../d8/d3e/classApp_1_1Document.html#a41f21ee729a6b717886e517dcfa6b771)  
void | [writeDependencyGraphViz](../../d8/d3e/classApp_1_1Document.html#aa97d82747fbbc5eb56dccae567276eca) (std::ostream &out)  
| write GraphViz file
[More...](../../d8/d3e/classApp_1_1Document.html#aa97d82747fbbc5eb56dccae567276eca)  
  
[bool](../../d9/db9/classbool.html) | [checkOnCycle](../../d8/d3e/classApp_1_1Document.html#a74fdb3db530cf4c3b0c8a85fb0a31313) (void)  
| checks if the graph is directed and has no cycles
[More...](../../d8/d3e/classApp_1_1Document.html#a74fdb3db530cf4c3b0c8a85fb0a31313)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getInList](../../d8/d3e/classApp_1_1Document.html#aea0ddc50d73293e7275afa6102d9d8e3) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *me) const  
| get a list of all objects linking to the given object
[More...](../../d8/d3e/classApp_1_1Document.html#aea0ddc50d73293e7275afa6102d9d8e3)  
  
std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > | [getDependentDocuments](../../d8/d3e/classApp_1_1Document.html#a2411038de4eb7e088f26cebb5725eb26) ([bool](../../d9/db9/classbool.html) sort=true)  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [topologicalSort](../../d8/d3e/classApp_1_1Document.html#a2b52886a0a5853bbba52be579f8c1de3) () const  
| get a list of topological sorted objects
(<https://en.wikipedia.org/wiki/Topological_sorting>)
[More...](../../d8/d3e/classApp_1_1Document.html#a2b52886a0a5853bbba52be579f8c1de3)  
  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getRootObjects](../../d8/d3e/classApp_1_1Document.html#ad0d9b0148c764813dfc9d4dc103b458b) () const  
| get all root objects (objects no other one reference too)
[More...](../../d8/d3e/classApp_1_1Document.html#ad0d9b0148c764813dfc9d4dc103b458b)  
  
std::vector< std::list< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > > | [getPathsByOutList](../../d8/d3e/classApp_1_1Document.html#a6c4fd3b7f7700be4e25980669d35a108) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *from, const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *to) const  
| get all possible paths from one object to another following the OutList
[More...](../../d8/d3e/classApp_1_1Document.html#a6c4fd3b7f7700be4e25980669d35a108)  
  
void | [getLinksTo](../../d8/d3e/classApp_1_1Document.html#a68fa1555a634a2da10ba434f64fbf2f2) (std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &links, const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj, [int](../../d1/da0/classint.html) options, [int](../../d1/da0/classint.html) maxCount=0, const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs={}) const  
| Return the links to a given object.
[More...](../../d8/d3e/classApp_1_1Document.html#a68fa1555a634a2da10ba434f64fbf2f2)  
  
[bool](../../d9/db9/classbool.html) | [hasLinksTo](../../d8/d3e/classApp_1_1Document.html#a6431188771ccb739c6e711968e423c91) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj) const  
| Check if there is any link to the given object.
[More...](../../d8/d3e/classApp_1_1Document.html#a6431188771ccb739c6e711968e423c91)  
  
void | [addRecomputeObject](../../d8/d3e/classApp_1_1Document.html#ae9cd6dab5c67b88e24bcfb54a15fc273) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj)  
| Called by objects during restore to ask for recompute.
[More...](../../d8/d3e/classApp_1_1Document.html#ae9cd6dab5c67b88e24bcfb54a15fc273)  
  
const std::string & | [getOldLabel](../../d8/d3e/classApp_1_1Document.html#a1ff3b7f5aeefa7af1449d0f23616d4fc) () const  
void | [renameObjectIdentifiers](../../d8/d3e/classApp_1_1Document.html#a4ee1ea277688bb08d607a83108434e8b) (const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > &paths, const std::function< [bool](../../d9/db9/classbool.html)(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)> &selector=[](const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) { return true;})  
| Function called to signal that an object identifier has been renamed.
[More...](../../d8/d3e/classApp_1_1Document.html#a4ee1ea277688bb08d607a83108434e8b)  
  
virtual [PyObject](../../df/d1b/classPyObject.html) * | [getPyObject](../../d8/d3e/classApp_1_1Document.html#a3eafa7c3d20b42cb6c41d9623c2476c7) (void) override  
| This method returns the Python wrapper for a C++ object.
[More...](../../d8/d3e/classApp_1_1Document.html#a3eafa7c3d20b42cb6c41d9623c2476c7)  
  
virtual std::string | [getFullName](../../d8/d3e/classApp_1_1Document.html#af007ba04581112132745321d40e89d75) () const override  
virtual | [~Document](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c) ()  
| Destruction.
[More...](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c)  
  
static std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getDependencyList](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &objs, [int](../../d1/da0/classint.html) options=0)  
| Get a complete list of all objects the given objects depend on.
[More...](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323)  
  
static std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > | [getDependentDocuments](../../d8/d3e/classApp_1_1Document.html#adb6cbc200401458d8b96701838e7db43) (std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > docs, [bool](../../d9/db9/classbool.html) sort)  
static [bool](../../d9/db9/classbool.html) | [isAnyRestoring](../../d8/d3e/classApp_1_1Document.html#ad76082433b2ec1d09d842514de7dfe38) ()  
| Indicate if there is any document restoring/importing.
[More...](../../d8/d3e/classApp_1_1Document.html#ad76082433b2ec1d09d842514de7dfe38)  
  
|
[Document](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b)
(const char *name="")  
| Construction.
[More...](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b)  
  
void | [breakDependency](../../d8/d3e/classApp_1_1Document.html#af9123db5f932f908555bd61c8db2fb53) ([DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *pcObject, [bool](../../d9/db9/classbool.html) clear)  
std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [readObjects](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d) ([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &reader)  
void | [writeObjects](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a) (const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &writer) const  
[bool](../../d9/db9/classbool.html) | [saveToFile](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d) (const char *filename) const  
void | [onBeforeChange](../../d8/d3e/classApp_1_1Document.html#a84bc36d18a86fca95c88aa31308f0bf3) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
| get called before the value is changed
[More...](../../d8/d3e/classApp_1_1Document.html#a84bc36d18a86fca95c88aa31308f0bf3)  
  
void | [onChanged](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a) (const [Property](../../d0/da9/classApp_1_1Property.html) *prop) override  
| get called by the container when a property has changed
[More...](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a)  
  
void | [onBeforeChangeProperty](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb) (const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *Who, const [Property](../../d0/da9/classApp_1_1Property.html) *What)  
| callback from the [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") objects before property will be changed
[More...](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb)  
  
void | [onChangedProperty](../../d8/d3e/classApp_1_1Document.html#aae4b353b22eaa76b58776756206af552) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *Who, const [Property](../../d0/da9/classApp_1_1Property.html) *What)  
| callback from the [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") objects after property was changed
[More...](../../d8/d3e/classApp_1_1Document.html#aae4b353b22eaa76b58776756206af552)  
  
std::string | [getTransientDirectoryName](../../d8/d3e/classApp_1_1Document.html#a787fa9500a9467131f2fb940083e4300) (const std::string &uuid, const std::string &filename) const  
  
## Signals of the document  
  
---  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalBeforeChange](../../d8/d3e/classApp_1_1Document.html#a3161138e6e5940b1c7bf9da50c75e220)  
| signal before changing an doc property
[More...](../../d8/d3e/classApp_1_1Document.html#a3161138e6e5940b1c7bf9da50c75e220)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChanged](../../d8/d3e/classApp_1_1Document.html#a5561f170a06f38fbd3897839dad67839)  
| signal on changed doc property
[More...](../../d8/d3e/classApp_1_1Document.html#a5561f170a06f38fbd3897839dad67839)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalNewObject](../../d8/d3e/classApp_1_1Document.html#aada9868b21dcc369ea1660667f97ae6b)  
| signal on new Object
[More...](../../d8/d3e/classApp_1_1Document.html#aada9868b21dcc369ea1660667f97ae6b)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalDeletedObject](../../d8/d3e/classApp_1_1Document.html#ad74af2d90beb3a3674e9a9d469ca7d82)  
| signal on deleted Object
[More...](../../d8/d3e/classApp_1_1Document.html#ad74af2d90beb3a3674e9a9d469ca7d82)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalBeforeChangeObject](../../d8/d3e/classApp_1_1Document.html#a1a324d850ff61d951de831c7918cf58c)  
| signal before changing an Object
[More...](../../d8/d3e/classApp_1_1Document.html#a1a324d850ff61d951de831c7918cf58c)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChangedObject](../../d8/d3e/classApp_1_1Document.html#a470e043516ad94f89aa8060bd61e51a5)  
| signal on changed Object
[More...](../../d8/d3e/classApp_1_1Document.html#a470e043516ad94f89aa8060bd61e51a5)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalTouchedObject](../../d8/d3e/classApp_1_1Document.html#aa4c629a9eec177a03529ddbb8e3e8904)  
| signal on manually called
[DocumentObject::touch()](../../d2/de4/classApp_1_1DocumentObject.html#a8949e65adb1315e37818719a058f4f40
"Set the property touched -> changed, cause recomputation in Update\(\)")
[More...](../../d8/d3e/classApp_1_1Document.html#aa4c629a9eec177a03529ddbb8e3e8904)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalRelabelObject](../../d8/d3e/classApp_1_1Document.html#add53d687e6a1753c5120b7cdec67d07a)  
| signal on relabeled Object
[More...](../../d8/d3e/classApp_1_1Document.html#add53d687e6a1753c5120b7cdec67d07a)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalActivatedObject](../../d8/d3e/classApp_1_1Document.html#a768443aa3ad2568e3d481b6e75c2afa4)  
| signal on activated Object
[More...](../../d8/d3e/classApp_1_1Document.html#a768443aa3ad2568e3d481b6e75c2afa4)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, [Transaction](../../de/dbf/classApp_1_1Transaction.html) *)> | [signalTransactionAppend](../../d8/d3e/classApp_1_1Document.html#aaf3477aebb1e4082388bb4852067d0ef)  
| signal on created object
[More...](../../d8/d3e/classApp_1_1Document.html#aaf3477aebb1e4082388bb4852067d0ef)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, [Transaction](../../de/dbf/classApp_1_1Transaction.html) *)> | [signalTransactionRemove](../../d8/d3e/classApp_1_1Document.html#a16185f8546d3013d545fc315e44d6d36)  
| signal on removed object
[More...](../../d8/d3e/classApp_1_1Document.html#a16185f8546d3013d545fc315e44d6d36)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalUndo](../../d8/d3e/classApp_1_1Document.html#a01b6644ff4f53f6d0a8fd101e0d57790)  
| signal on undo
[More...](../../d8/d3e/classApp_1_1Document.html#a01b6644ff4f53f6d0a8fd101e0d57790)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalRedo](../../d8/d3e/classApp_1_1Document.html#aad8731a029bc6b5fe0d2841a58647035)  
| signal on redo
[More...](../../d8/d3e/classApp_1_1Document.html#aad8731a029bc6b5fe0d2841a58647035)  
  
boost::signals2::signal< void([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &)> | [signalSaveDocument](../../d8/d3e/classApp_1_1Document.html#aa923177773d96f8494f550970908d179)  
| signal on load/save document this signal is given when the document gets
streamed.
[More...](../../d8/d3e/classApp_1_1Document.html#aa923177773d96f8494f550970908d179)  
  
boost::signals2::signal< void([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)> | [signalRestoreDocument](../../d8/d3e/classApp_1_1Document.html#a6ca7bad32ddd8c6cfd6088546d140848)  
boost::signals2::signal< void(const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &)> | [signalExportObjects](../../d8/d3e/classApp_1_1Document.html#a0797dc2071d46f4599b925b1d081f93f)  
boost::signals2::signal< void(const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &)> | [signalExportViewObjects](../../d8/d3e/classApp_1_1Document.html#ae6faa5b2cfe5d182e156e1cc1f937981)  
boost::signals2::signal< void(const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) &)> | [signalImportObjects](../../d8/d3e/classApp_1_1Document.html#a71ee0e5d774a93a47c7db5964906a38d)  
boost::signals2::signal< void(const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &, [Base::Reader](../../d1/d1f/classBase_1_1Reader.html) &, const std::map< std::string, std::string > &)> | [signalImportViewObjects](../../d8/d3e/classApp_1_1Document.html#a38702e1f0098ffae1da77091590d429e)  
boost::signals2::signal< void(const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &)> | [signalFinishImportObjects](../../d8/d3e/classApp_1_1Document.html#aebc7d06f469b48341bfd7c4561184ce7)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const std::string &)> | [signalStartSave](../../d8/d3e/classApp_1_1Document.html#a726c6d0ef527f9dfbbfc80e304caf254)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const std::string &)> | [signalFinishSave](../../d8/d3e/classApp_1_1Document.html#a0485e0c50848f1e240028db9e4e1f0fe)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalBeforeRecompute](../../d8/d3e/classApp_1_1Document.html#a67e257e6d0dd282a8779453179a1f5e8)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &)> | [signalRecomputed](../../d8/d3e/classApp_1_1Document.html#a43a9dc921cb2b60ec72b5907e27bac4f)  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalRecomputedObject](../../d8/d3e/classApp_1_1Document.html#a2f4410d341abe785473aaeea863b851f)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, std::string)> | [signalOpenTransaction](../../d8/d3e/classApp_1_1Document.html#a8fdf4a35e3c668506cc976ca68227fa8)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalCommitTransaction](../../d8/d3e/classApp_1_1Document.html#ad2ad5cccbdbe79c9dcbc3a5b8ec2649e)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalAbortTransaction](../../d8/d3e/classApp_1_1Document.html#a94ad3799113f1be05928b529b44543be)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > &)> | [signalSkipRecompute](../../d8/d3e/classApp_1_1Document.html#ad3041e3063a5c14765f790910b9f941e)  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalFinishRestoreObject](../../d8/d3e/classApp_1_1Document.html#aa97a6bafa4ab9469102554aa268a00ed)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChangePropertyEditor](../../d8/d3e/classApp_1_1Document.html#afadb4e1eea10edf5ee299642e7db4053)  
boost::signals2::signal< void(std::string)> | [signalLinkXsetValue](../../d8/d3e/classApp_1_1Document.html#aeb35d1014e79be9784efe087fe9c5113)  
void | [clearDocument](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb) ()  
  
##  Additional Inherited Members  
  
---  
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

The document class.

This is besides the [Application](../../da/dbf/classApp_1_1Application.html
"The Application The root of the whole application.") class the most important
class in FreeCAD It contains all the data of the opened, saved or newly
created FreeCAD [Document](../../d8/d3e/classApp_1_1Document.html "The
document class."). The [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") manage the Undo and Redo mechanism and the linking of
documents.

Note: the documents are not free objects. They are completely handled by the
[App::Application](../../da/dbf/classApp_1_1Application.html "The Application
The root of the whole application."). Only the
[Application](../../da/dbf/classApp_1_1Application.html "The Application The
root of the whole application.") can Open or destroy a document.

#  Exception handling

As the document is the main data structure of FreeCAD we have to take a close
look at how Exceptions affect the integrity of the
[App::Document](../../d8/d3e/classApp_1_1Document.html "The document class.").

#  Undo Redo an Transactions

Undo Redo handling is one of the major mechanism of a document in terms of
user friendliness and speed (no one will wait for Undo too long).

#  Graph and dependency handling

The FreeCAD document handles the dependencies of its DocumentObjects with an
adjacence list. This gives the opportunity to calculate the shortest recompute
path. Also, it enables more complicated dependencies beyond trees.

See also

    [App::Application](../../da/dbf/classApp_1_1Application.html "The Application The root of the whole application.")
     [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of all Classes handled in the Document.")

## Member Enumeration Documentation

## ◆ DependencyOption

enum
[App::Document::DependencyOption](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34)  
---  
  
Option bit flags used by getDepenencyList()

Enumerator  
---  
DepSort | Return topological sorted list.   
DepNoXLinked | Do no include object linked by [PropertyXLink](../../d2/de2/classApp_1_1PropertyXLink.html "Link to an \(sub\)object in the same or different document."), as it can handle external link.   
DepNoCycle | Raise exception on cycles.   
  
## ◆ ExportStatus

enum
[App::Document::ExportStatus](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81db)  
---  
  
Enumerator  
---  
NotExporting |   
Exporting |   
  
## ◆ Status

enum
[App::Document::Status](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553)  
---  
  
Enumerator  
---  
SkipRecompute |   
KeepTrailingDigits |   
Closable |   
Restoring |   
Recomputing |   
PartialRestore |   
Importing |   
PartialDoc |   
AllowPartialRecompute |   
TempDoc |   
RestoreError |   
LinkStampChanged |   
IgnoreErrorOnRecompute |   
  
## Constructor & Destructor Documentation

## ◆ ~Document()

| Document::~Document  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Destruction.

References
[App::DocumentP::clearDocument()](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55),
[clearUndos()](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55),
[Base::FileInfo::deleteDirectoryRecursive()](../../dd/d34/classBase_1_1FileInfo.html#a9b042f228fbabe4c34c357669189cca8),
[App::DocumentP::DocumentPythonObject](../../d1/da5/structApp_1_1DocumentP.html#add40c1bb1337e43508a99b19d306083a),
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
and
[TransientDir](../../d8/d3e/classApp_1_1Document.html#ac90f8f59e978c2dbd5b043461852628f).

## ◆ Document()

| Document::Document  | ( | const char *  | _name_ = `""`| ) |   
---|---|---|---|---|---  
protected  
  
Construction.

References
[Comment](../../d8/d3e/classApp_1_1Document.html#ad015397935c7246a30af4e9422c470d8),
[Company](../../d8/d3e/classApp_1_1Document.html#a0b47f89716092bd850cdf61e9e2d0dd7),
[CreatedBy](../../d8/d3e/classApp_1_1Document.html#a6da238ba27b4d5dbd3861c8fd4ece5fe),
[CreationDate](../../d8/d3e/classApp_1_1Document.html#ad699ff3487ec1cb353626db12f0b7a5e),
[Base::TimeInfo::currentDateTimeString()](../../df/d75/classBase_1_1TimeInfo.html#a395c874b184fdb4fc9ffc90fb4714371),
[App::DocumentP::DocumentPythonObject](../../d1/da5/structApp_1_1DocumentP.html#add40c1bb1337e43508a99b19d306083a),
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetASCII()](../../d4/d97/classParameterGrp.html#a5c579b580966bb5ddb8d07df2da9bc9c),
[ParameterGrp::GetInt()](../../d4/d97/classParameterGrp.html#a7057be6b17be9f72ef5c69c1b27696d5),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[Id](../../d8/d3e/classApp_1_1Document.html#ab5d5e73c8bdd011bf1a5737e924e5019),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
[LastModifiedBy](../../d8/d3e/classApp_1_1Document.html#a854ee4bf3d52fe90ed93d91d92767f03),
[LastModifiedDate](../../d8/d3e/classApp_1_1Document.html#a0a381c4d900a31c8cb7d4ef575176768),
[License](../../d8/d3e/classApp_1_1Document.html#a318812adbc89a1288160dc3baa7baa95),
[LicenseURL](../../d8/d3e/classApp_1_1Document.html#a82b097da462899f58de239ebf1b602ed),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[Meta](../../d8/d3e/classApp_1_1Document.html#af75d7b6beaa8a7c3576c9b56d0c0b51e),
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
[App::Prop_None](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a32c18d11cda25e1ac1b1692aa36423e0),
[App::Prop_ReadOnly](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a9bea209c7050543e2ceadef7ba0e9e75),
[App::Prop_Transient](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a6eefec5f03fa1d639e7fc26c5804ccf6),
[ShowHidden](../../d8/d3e/classApp_1_1Document.html#ad993906aa4a429aa7882fc17160cc65e),
[Tip](../../d8/d3e/classApp_1_1Document.html#aba7262694bf2514f516c74bb90bb7de9),
[TipName](../../d8/d3e/classApp_1_1Document.html#a334536a52d758261510975cad0bcce64),
[App::Property::touch()](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475),
[TransientDir](../../d8/d3e/classApp_1_1Document.html#ac90f8f59e978c2dbd5b043461852628f),
and
[Uid](../../d8/d3e/classApp_1_1Document.html#af3b3acc44a20bd990bf2e97f5116d3c6).

## Member Function Documentation

## ◆ abortTransaction()

void Document::abortTransaction  | ( | | ) |   
---|---|---|---|---  
  
Abort the actually running transaction.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Application::closeActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9),
[App::DocumentP::committing](../../d1/da5/structApp_1_1DocumentP.html#ac660a92e93876ba22cfcb157dcbcc9a2),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a),
and
[isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2).

Referenced by
[Gui::Document::abortCommand()](../../de/d4e/classGui_1_1Document.html#a092e0f7b11a5422c7672546e5c19cf7b).

## ◆ addObject() [1/2]

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * Document::addObject  | ( | const char *  | _sType_ ,   
---|---|---|---  
|  | const char *  | _pObjectName_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _isNew_ = `true`,   
|  | const char *  | _viewType_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _isPartial_ = `false`  
| ) | |   
  
Add a feature of sType with sName (ASCII) to this document and set it active.

Unicode names are set through the Label property.

Parameters

     sType| the type of created object   
---|---  
pObjectName| if nonNULL use that name otherwise generate a new unique name
based on the _sType_  
isNew| if false don't call the
`[DocumentObject::setupObject()](../../d2/de4/classApp_1_1DocumentObject.html#ac677fd52efeb2a6d1e5afd71dc896e7b
"get called after a brand new object was created")` callback (default is true)  
viewType| override object's view provider name  
isPartial| indicate if this object is meant to be partially loaded  
  
References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::addObjectDel()](../../de/dbf/classApp_1_1Transaction.html#aaa52509516281edac9af07edc57bb707),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[Base::Type::getTypeIfDerivedFrom()](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593),
[getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[App::DocumentObject::getViewProviderNameOverride()](../../d2/de4/classApp_1_1DocumentObject.html#ad4e5af68230646890aa61c051f7b9966),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
[App::DocumentP::lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
[App::DocumentObject::pcNameInDocument](../../d2/de4/classApp_1_1DocumentObject.html#a2e797e4bd0bfbf7ef4d3f12e220594eb),
[Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
[App::DocumentObject::setDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a043039f2703e2a1475e8476e031e8822),
[App::DocumentObject::setStatus()](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815),
[App::DocumentObject::setupObject()](../../d2/de4/classApp_1_1DocumentObject.html#ac677fd52efeb2a6d1e5afd71dc896e7b),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[signalActivatedObject](../../d8/d3e/classApp_1_1Document.html#a768443aa3ad2568e3d481b6e75c2afa4),
[signalNewObject](../../d8/d3e/classApp_1_1Document.html#aada9868b21dcc369ea1660667f97ae6b),
[signalTransactionAppend](../../d8/d3e/classApp_1_1Document.html#aaf3477aebb1e4082388bb4852067d0ef),
[App::DocumentP::StatusBits](../../d1/da5/structApp_1_1DocumentP.html#a22382776a74a5bc0c130d1136d2ec7d2),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

Referenced by
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[DraftUtils::DraftDxfRead::AddGraphics()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#aab6f7dceeb05ccd5adcc4001c19fab9c),
[Import::ImpExpDxfRead::AddGraphics()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#ac5ff22017799d55d19670d7760786b37),
[App::GroupExtension::addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[DraftUtils::DraftDxfRead::AddObject()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#aa5b12cf60ff8912314f410187655404c),
[Import::ImpExpDxfRead::AddObject()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#ac13e85924ca8c662789bbd02a2cfe889),
[ArchBuildingPart.BuildingPart::autogroup()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a45c3834ac8f02df7fc30569fc90c4285),
[Fem::createObjectByType()](../../dd/d72/namespaceFem.html#af3663ac69e66763d50fbbd579cb9024a),
[ReverseEngineeringGui::SegmentationManual::createSegment()](../../dc/d04/classReverseEngineeringGui_1_1SegmentationManual.html#a95ac22eb241f58d992ffe08f784eb5d0),
[PartGui::DlgProjectionOnSurface::DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a280d8ac8bf690484a268f54625c2c7e2),
[Sandbox::CustomAddObjectEvent::execute()](../../d0/d48/classSandbox_1_1CustomAddObjectEvent.html#abc5aa8dce6ec296e49e32847e95f689c),
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42),
[ArchPanel.NestTaskPanel::getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
[ArchPanel.NestTaskPanel::getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04),
[Part::ImportIgesParts()](../../d2/db9/namespacePart.html#a10322b892abc3b1779054dacf1a49e53),
[Part::ImportStepParts()](../../d2/db9/namespacePart.html#a4da179b4c198cc0c74884eb8693d1619),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[App::LinkBaseExtension::makeCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a89cc7109764a089298c635a71a86b49a),
[PartDesign::Body::onChanged()](../../dd/db8/classPartDesign_1_1Body.html#aef216a77e951705ba9b124bfb88ae533),
[DraftUtils::DraftDxfRead::OnReadText()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#a4a48ca0bc35d4c47fc4e374d8ee6bf25),
[Import::ImpExpDxfRead::OnReadText()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#afd452a8d1348c494bfcc4bb9e5d4b01c),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
[readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::LinkBaseExtension::setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
[Path::Area::showShape()](../../d8/dfc/classPath_1_1Area.html#ac20bf1933f3cb18e24b0892f378b761f),
[MeshGui::ViewProviderMesh::splitMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a3480f540c644cb38cd0a1ed1bc304d94),
[App::LinkBaseExtension::syncCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a4591b8c9e098285eceedfdc81e04381f),
and
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ addObject() [2/2]

void Document::addObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _pcObject_ ,   
---|---|---|---  
|  | const char *  | _pObjectName_ = `nullptr`  
| ) | |   
  
Add an existing feature with sName (ASCII) to this document and set it active.

Unicode names are set through the Label property. This is an overloaded
function of the function above and can be used to create a feature outside and
add it to the document afterwards.

Note

    The passed feature must not yet be added to a document, otherwise an exception is raised. 

References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::addObjectDel()](../../de/dbf/classApp_1_1Transaction.html#aaa52509516281edac9af07edc57bb707),
[App::DocumentObject::getDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a9a3e2b0468b67170df03c0e93cd752b2),
[Base::Type::getName()](../../dc/dee/classBase_1_1Type.html#a861a2f6bd2cd2c2df7846e202f0ce137),
[Base::Persistence::getTypeId()](../../d9/d25/classBase_1_1Persistence.html#ab2e99822ef5477d5454c87d11ea75596),
[getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[App::DocumentObject::getViewProviderNameOverride()](../../d2/de4/classApp_1_1DocumentObject.html#ad4e5af68230646890aa61c051f7b9966),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
[App::DocumentP::lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
[App::DocumentObject::pcNameInDocument](../../d2/de4/classApp_1_1DocumentObject.html#a2e797e4bd0bfbf7ef4d3f12e220594eb),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
[App::DocumentObject::setDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a043039f2703e2a1475e8476e031e8822),
[App::DocumentObject::setStatus()](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[signalActivatedObject](../../d8/d3e/classApp_1_1Document.html#a768443aa3ad2568e3d481b6e75c2afa4),
[signalNewObject](../../d8/d3e/classApp_1_1Document.html#aada9868b21dcc369ea1660667f97ae6b),
and
[signalTransactionAppend](../../d8/d3e/classApp_1_1Document.html#aaf3477aebb1e4082388bb4852067d0ef).

Referenced by
[ArchBuildingPart.BuildingPart::autogroup()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a45c3834ac8f02df7fc30569fc90c4285),
[ArchPanel.NestTaskPanel::getContainer()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad25ef9b5aade32a390de4a8bd34bafda),
and
[ArchPanel.NestTaskPanel::getShapes()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#a52edae24a9d124678d48b157749b5f04).

## ◆ addObjects()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::addObjects  | ( | const char *  | _sType_ ,   
---|---|---|---  
|  | const std::vector< std::string > & | _objectNames_ ,   
|  | [bool](../../d9/db9/classbool.html) | _isNew_ = `true`  
| ) | |   
  
Add an array of features of the given types and names.

Unicode names are set through the Label property.

Parameters

     sType| The type of created object   
---|---  
objectNames| A list of object names  
isNew| If false don't call the
`[DocumentObject::setupObject()](../../d2/de4/classApp_1_1DocumentObject.html#ac677fd52efeb2a6d1e5afd71dc896e7b
"get called after a brand new object was created")` callback (default is true)  
  
References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::addObjectDel()](../../de/dbf/classApp_1_1Transaction.html#aaa52509516281edac9af07edc57bb707),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[Base::Tools::getIdentifier()](../../d6/dda/structBase_1_1Tools.html#a49653de3f8677d06572f26f1f002641d),
[Base::Type::getTypeIfDerivedFrom()](../../dc/dee/classBase_1_1Type.html#ae69252049934864817d7932cc246a593),
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b),
[App::DocumentObject::getViewProviderNameOverride()](../../d2/de4/classApp_1_1DocumentObject.html#ad4e5af68230646890aa61c051f7b9966),
[KeepTrailingDigits](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a844e41986bdfe3e2ff29054fc8aaeb55),
[App::DocumentObject::Label](../../d2/de4/classApp_1_1DocumentObject.html#a7259f450fea1a74073e626115d46110d),
[App::DocumentP::lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
[App::DocumentObject::pcNameInDocument](../../d2/de4/classApp_1_1DocumentObject.html#a2e797e4bd0bfbf7ef4d3f12e220594eb),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
[App::DocumentObject::setDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a043039f2703e2a1475e8476e031e8822),
[App::DocumentObject::setStatus()](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815),
[App::DocumentObject::setupObject()](../../d2/de4/classApp_1_1DocumentObject.html#ac677fd52efeb2a6d1e5afd71dc896e7b),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[signalActivatedObject](../../d8/d3e/classApp_1_1Document.html#a768443aa3ad2568e3d481b6e75c2afa4),
[signalNewObject](../../d8/d3e/classApp_1_1Document.html#aada9868b21dcc369ea1660667f97ae6b),
[signalTransactionAppend](../../d8/d3e/classApp_1_1Document.html#aaf3477aebb1e4082388bb4852067d0ef),
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

## ◆ addOrRemovePropertyOfObject()

void Document::addOrRemovePropertyOfObject  | ( | [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [Property](../../d0/da9/classApp_1_1Property.html) *  | _prop_ ,   
|  | [bool](../../d9/db9/classbool.html) | _add_  
| ) | |   
  
References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::addOrRemoveProperty()](../../de/dbf/classApp_1_1Transaction.html#a13b0dfb6149502294662f69042e250d8),
[App::Application::getActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a320164bff61415b44f26af228fe99c6a),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[Importing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3fcdf22c3e8c2aea788606a837c7d522),
[isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2),
[App::DocumentP::iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8),
[Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
and
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87).

Referenced by
[Gui::ViewProviderDocumentObject::addDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a0b66cab9ff390bb91593786721612aef),
and
[Gui::ViewProviderDocumentObject::removeDynamicProperty()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a4d47313a825a2051c9a667ed4e7a1346).

## ◆ addRecomputeObject()

void Document::addRecomputeObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |   
---|---|---|---|---|---  
  
Called by objects during restore to ask for recompute.

References
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
and
[App::DocumentP::touchedObjs](../../d1/da5/structApp_1_1DocumentP.html#a7b3a34196818f63f6878c8026e3badc9).

## ◆ afterRestore() [1/2]

[bool](../../d9/db9/classbool.html) Document::afterRestore  | ( | [bool](../../d9/db9/classbool.html) | _checkPartial_ = `false`| ) |   
---|---|---|---|---|---  
  
References
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525),
[App::Application::signalFinishRestoreDocument](../../da/dbf/classApp_1_1Application.html#ac7b262994ef3ae8766bd3c7590185046),
and
[App::Application::signalPendingReloadDocument](../../da/dbf/classApp_1_1Application.html#a76ca7e016087a4114ed1779b2eaf0913).

Referenced by
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
and
[restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ afterRestore() [2/2]

[bool](../../d9/db9/classbool.html) Document::afterRestore  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objArray_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _checkPartial_ = `false`  
| ) | |   
  
References
[App::DocumentP::addRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#aaf1f87bf25a914489c0b6a511f26637f),
[DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926),
[App::PropertyExpressionEngine::ExecuteOnRestore](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a7c6612ebd51ad588fdc4e147f2e42329aa6aecd854e32277bf0cf78cea17d1cca),
[getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
[LinkStampChanged](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af9b330124dbe14c0e1b2087e73b814da),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[PartialRestore](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aa85fb1ecccf6466736187e1826eab209),
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525),
[signalFinishRestoreObject](../../d8/d3e/classApp_1_1Document.html#aa97a6bafa4ab9469102554aa268a00ed),
[App::DocumentObject::StdReturn](../../d2/de4/classApp_1_1DocumentObject.html#af53a1c6a086c5dfe228aaefeeb7316d2),
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
and
[App::DocumentP::touchedObjs](../../d1/da5/structApp_1_1DocumentP.html#a7b3a34196818f63f6878c8026e3badc9).

## ◆ breakDependency()

| void Document::breakDependency  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _pcObject_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _clear_  
| ) | |   
protected  
  
References
[App::PropertyLinkBase::breakLinks()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a3a7f63103cb074017ba1d159ada3cc44),
and
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5),
and
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ checkOnCycle()

[bool](../../d9/db9/classbool.html) Document::checkOnCycle  | ( | void  | | ) |   
---|---|---|---|---|---  
  
checks if the graph is directed and has no cycles

## ◆ clearDocument()

void Document::clearDocument  | ( | | ) |   
---|---|---|---|---  
  
References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[App::DocumentP::clearDocument()](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55),
[App::DocumentP::clearRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#abe4686fb5139ebfdab04dabb67405c3a),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::DocumentP::lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525),
[App::Application::signalDeleteDocument](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47),
and
[App::Application::signalNewDocument](../../da/dbf/classApp_1_1Application.html#a49425118433ce84229402407d5631ea4).

## ◆ clearUndos()

void Document::clearUndos  | ( | | ) |   
---|---|---|---|---  
  
Remove all stored Undos and Redos.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::DocumentP::committing](../../d1/da5/structApp_1_1DocumentP.html#ac660a92e93876ba22cfcb157dcbcc9a2),
and
[isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2).

Referenced by
[restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
[setUndoMode()](../../d8/d3e/classApp_1_1Document.html#a4339c7121daa9a2b5627b53a584eafa5),
and
[~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ commitTransaction()

void Document::commitTransaction  | ( | | ) |   
---|---|---|---|---  
  
Commit the Command transaction. Do nothing If there is no Command transaction
open.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Application::closeActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9),
[App::DocumentP::committing](../../d1/da5/structApp_1_1DocumentP.html#ac660a92e93876ba22cfcb157dcbcc9a2),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a),
and
[isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2).

Referenced by
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[PartGui::DlgExtrusion::apply()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a6428c7ac6585ad41ed9792aeea96d2f7),
and
[Gui::Document::commitCommand()](../../de/d4e/classGui_1_1Document.html#aaa70b6607b3ba6b402e0d289a992b45f).

## ◆ copyObject()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::copyObject  | ( | const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _returnAll_ = `false`  
| ) | |   
  
Copy objects from another document to this document.

Parameters

     recursive| if true, then all objects this object depends on are copied as well. By default _recursive_ is false.  
---|---  
returnAll| if true, return all copied objects including those auto included by
recursive searching. If false, then only return the copied object
corresponding to the input objects.  
  
Returns

    Returns the list of objects copied. 

References
[DepNoXLinked](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a76564d229c609eca9e50b9dab37f1e3c),
[DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926),
[exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
[getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
[App::Application::getTempFileName()](../../da/dbf/classApp_1_1Application.html#a6550097c7ee9c3857f8190954acfbf48),
[App::PropertyXLink::hasXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a9b5a3af810860e7117ad6f11e5d4c7e1),
[App::MergeDocuments::importObjects()](../../d6/d0c/classApp_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6),
[isSaved()](../../d8/d3e/classApp_1_1Document.html#a730da4f4ddab904051e5f1a031577b27),
[App::MergeDocuments::setVerbose()](../../d6/d0c/classApp_1_1MergeDocuments.html#aed8da7ec5b0b0acbc0ad0d0a7b029f62),
[TempDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af2a790c9309723635970664f9ce29418),
and
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
and
[moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5).

## ◆ countObjects()

[int](../../d1/da0/classint.html) Document::countObjects  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
get the number of objects in the document

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[StdCmdImport::activated()](../../d5/d4f/classStdCmdImport.html#a7ac453df0ea7389aa72fe651020ec1d4),
and
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8).

## ◆ countObjectsOfType()

[int](../../d1/da0/classint.html) Document::countObjectsOfType  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _typeId_| ) |  const  
---|---|---|---|---|---  
  
References
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

Referenced by
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
and
[PartDesignGui::Workbench::setupContextMenu()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#adf13eeb6b7f53fc0ce4c900cbca9712e).

## ◆ exportGraphviz()

void Document::exportGraphviz  | ( | std::ostream & | _out_| ) |  const  
---|---|---|---|---|---  
  
The GraphCreator class

This class creates the dependency graph for a document.

getId returns a canonical string for a
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.").

Parameters

     docObj| [Document](../../d8/d3e/classApp_1_1Document.html "The document class.") object to get an ID from   
---|---  
  
Returns

    A string

getId returns a canonical string for an
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html);

Parameters

     path|   
---|---  
  
Returns

    A string

setGraphAttributes Set graph attributes on a subgraph for a
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") node.

Parameters

     obj| [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of all Classes handled in the Document.")  
---|---  
  
setPropertyVertexAttributes Set vertex attributes for a
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") node in a graph.

Parameters

     g| Graph   
---|---  
vertex| [Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.") node  
name| Name of node  
  
addExpressionSubgraphIfNeeded Add a subgraph to the main graph if it is
needed, i.e. there are defined at least one expression in the document object,
or other objects are referencing properties in it.

Parameters

     obj| [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of all Classes handled in the Document.") to assess.   
---|---  
CSSubgraphs| Boolean if the GeoFeatureGroups are created as subgraphs  
  
add Add @docObj to the graph, including all expressions (and dependencies) it
includes.

Parameters

     docObj| The document object to add.   
---|---  
name| Name of node.  
  
References
[App::DocumentObject::ExpressionEngine](../../d2/de4/classApp_1_1DocumentObject.html#a6a7c9440e119a76b45860ff899322c37),
[DraftVecUtils::find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[App::PropertyExpressionEngine::getExpressions()](../../db/d34/classApp_1_1PropertyExpressionEngine.html#a190fbdce938ee9ddee37b1d04ab95e65),
[App::ExtensionContainer::getExtensionByType()](../../d6/d76/classApp_1_1ExtensionContainer.html#a0711e5ec3feeac1afc569569784a4994),
[App::GeoFeatureGroupExtension::getGroupOfObject()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a84e6f574148e38d1b1b7f65bfd749f13),
[App::GeoFeatureGroupExtension::getInvalidLinkObjects()](../../de/df0/classApp_1_1GeoFeatureGroupExtension.html#a391e01ee323c3d9c25c8d74aa8271ae2),
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::OriginFeature::getOrigin()](../../da/dfe/classApp_1_1OriginFeature.html#ae153618f0361a30dd55b8b0f21294cfa),
[App::DocumentObject::getOutList()](../../d2/de4/classApp_1_1DocumentObject.html#ab69981229233aa7c2fd32e378d2f2087),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[App::ExtensionContainer::hasExtension()](../../d6/d76/classApp_1_1ExtensionContainer.html#adae9aba02ce19d1611f1bb3447ee936e),
and
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127).

## ◆ exportObjects()

void Document::exportObjects  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _obj_ ,   
---|---|---|---  
|  | std::ostream & | _out_  
| ) | |   
  
References
[App::Application::Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc),
[Base::Uuid::createUuid()](../../d6/d43/classBase_1_1Uuid.html#a4f0fb93733c226a06e1401083b6071ec),
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
[App::Prop_Output](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a2f4f0fc70a512ce25e4c7ecb43a0eaa7),
[Base::ZipWriter::putNextEntry()](../../d9/df3/classBase_1_1ZipWriter.html#abb607a9c82879c6ead67f9dee234bd24),
[App::PropertyUUID::setValue()](../../d2/d6c/classApp_1_1PropertyUUID.html#ab6d9418f4d048c0d0070c9c45a9233d2),
[signalExportObjects](../../d8/d3e/classApp_1_1Document.html#a0797dc2071d46f4599b925b1d081f93f),
[Base::ZipWriter::Stream()](../../d9/df3/classBase_1_1ZipWriter.html#a37330d3d5bff097e58268aa7853abaa4),
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a),
and
[writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

Referenced by
[copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
and
[importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778).

## ◆ findObjects()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::findObjects  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _typeId_ ,   
---|---|---|---  
|  | const char *  | _objname_ ,   
|  | const char *  | _label_  
| ) | |  const  
  
References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[PartDesignGui::TaskPipeParameters::accept()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a3547d74f52eaf53d3ccd2f28aac74d06).

## ◆ getActiveObject()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * Document::getActiveObject  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns the active Object of this document.

References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3).

Referenced by
[Fem::createObjectByType()](../../dd/d72/namespaceFem.html#af3663ac69e66763d50fbbd579cb9024a),
[Gui::ViewProviderIndex::data()](../../d7/d9c/classGui_1_1ViewProviderIndex.html#a3c14909891014378c66da5b320b18214),
[Fem::getObjectByType()](../../dd/d72/namespaceFem.html#a1d62957fae198eb1c03b3ce2c2503c3c),
[Gui::Command::isActiveObjectValid()](../../d2/dff/classGui_1_1Command.html#a1c0803a1078df8cb2d3b3a20601c9b3c),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
and
[Fem::FemVTKTools::writeResult()](../../d6/d26/classFem_1_1FemVTKTools.html#afe10808623915c79b6e74786a6f6d0e3).

## ◆ getAvailableRedoNames()

std::vector< std::string > Document::getAvailableRedoNames  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of the Redo names.

Referenced by
[Gui::Document::getRedoVector()](../../de/d4e/classGui_1_1Document.html#a3967fd4d869f61a25cf3e82a9ff7f6e9).

## ◆ getAvailableRedos()

[int](../../d1/da0/classint.html) Document::getAvailableRedos  | ( | [int](../../d1/da0/classint.html) | _id_ = `0`| ) |  const  
---|---|---|---|---|---  
  
Returns the number of stored Redos. If greater than 0 Redo will be effective.

## ◆ getAvailableUndoNames()

std::vector< std::string > Document::getAvailableUndoNames  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of the Undo names.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
and
[App::Transaction::Name](../../de/dbf/classApp_1_1Transaction.html#a6245b49f541ec20247d3b46c18152f9a).

Referenced by
[Gui::Document::getUndoVector()](../../de/d4e/classGui_1_1Document.html#ac3cec04203b75d165fba4fe8305a2847).

## ◆ getAvailableUndos()

[int](../../d1/da0/classint.html) Document::getAvailableUndos  | ( | [int](../../d1/da0/classint.html) | _id_ = `0`| ) |  const  
---|---|---|---|---|---  
  
Returns the number of stored Undos. If greater than 0 Undo will be effective.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
and
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a).

## ◆ getDependencyList()

| std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getDependencyList  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _options_ = `0`  
| ) | |   
static  
  
Get a complete list of all objects the given objects depend on.

This function is defined as static because it accepts objects from different
documents, and the returned list will contain dependent objects from all
relevant documents

Parameters

     objs| input objects to query for dependency.   
---|---  
options| See DependencyOption  
  
References
[DepNoCycle](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a203f88eb740201a9839da30f2831bc86),
[DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926),
and
[App::DocumentP::partialTopologicalSort()](../../d1/da5/structApp_1_1DocumentP.html#a9dec0045952043940b9ab4cfaf5a8dc7).

Referenced by
[StdCmdDuplicateSelection::activated()](../../d4/d75/classStdCmdDuplicateSelection.html#a1ffe671eebc9f7e4c99740df06eaf0a9),
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526),
[copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
[Gui::MainWindow::createMimeDataFromSelection()](../../d5/d2f/classGui_1_1MainWindow.html#a1471665356b86fc81addf133db22c977),
[getDependingObjects()](../../d8/d3e/classApp_1_1Document.html#afbf82bb93c0dde39c082fa5c497d0c1a),
[App::LinkBaseExtension::getOnChangeCopyObjects()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a20adee6736980e9459b96c6306986d56),
[importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778),
[Import::ImportOCAF2::loadShapes()](../../d9/ddd/classImport_1_1ImportOCAF2.html#afa667a1c5c88cd6565d91740bf38ea61),
[moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
and
[Gui::ViewProviderLink::setupContextMenu()](../../d6/d59/classGui_1_1ViewProviderLink.html#a1e5de483828c97463a497ac82bc5df49).

## ◆ getDependentDocuments() [1/2]

std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > Document::getDependentDocuments  | ( | [bool](../../d9/db9/classbool.html) | _sort_ = `true`| ) |   
---|---|---|---|---|---  
  
References
[getDependentDocuments()](../../d8/d3e/classApp_1_1Document.html#a2411038de4eb7e088f26cebb5725eb26).

Referenced by
[Gui::MainWindow::closeAllDocuments()](../../d5/d2f/classGui_1_1MainWindow.html#a26025f09b536690547638795dfd37010),
[getDependentDocuments()](../../d8/d3e/classApp_1_1Document.html#a2411038de4eb7e088f26cebb5725eb26),
[App::Application::openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728),
[Gui::Document::save()](../../de/d4e/classGui_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
and
[Gui::Document::saveAll()](../../de/d4e/classGui_1_1Document.html#a855313ae529de818172eac8acd860157).

## ◆ getDependentDocuments() [2/2]

| std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > Document::getDependentDocuments  | ( | std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > | _docs_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _sort_  
| ) | |   
static  
  
References
[App::PropertyXLink::getDocumentOutList()](../../d2/de2/classApp_1_1PropertyXLink.html#af1f6b642c153368da2ec154538106914).

## ◆ getDependingObjects()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getDependingObjects  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of document's objects including the dependencies.

References
[getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
and
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ getErrorDescription()

const char * Document::getErrorDescription  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _Obj_| ) |  const  
---|---|---|---|---|---  
  
get the text of the error of a specified object

References
[App::DocumentP::findRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#a806eec3926c51f0e5357e1ee86708bd6).

Referenced by
[PartDesignGui::ViewProviderTransformed::recomputeFeature()](../../da/d71/classPartDesignGui_1_1ViewProviderTransformed.html#a14cb4d7a2487ad732593fed6ece13ca6),
and
[writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ getFileName()

const char * Document::getFileName  | ( | | ) |  const  
---|---|---|---|---  
  
Returned filename.

For saved document, this will be the content stored in property 'Filename'.
For unsaved temporary file, this will be the content of property
'TransientDir'.

References
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[TempDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af2a790c9309723635970664f9ce29418),
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
and
[TransientDir](../../d8/d3e/classApp_1_1Document.html#ac90f8f59e978c2dbd5b043461852628f).

Referenced by
[App::DocInfo::getDocPath()](../../d7/d23/classApp_1_1DocInfo.html#a9a066a626c84cb4c5ce152b9449b64f3),
and
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10).

## ◆ getFullName()

| std::string Document::getFullName  | ( | | ) |  const  
---|---|---|---|---  
overridevirtual  
  
Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a331110f1aeffb0a907ac2b74f78cc69d).

## ◆ getInList()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getInList  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _me_| ) |  const  
---|---|---|---|---|---  
  
get a list of all objects linking to the given object

References
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

## ◆ getLinksTo()

void Document::getLinksTo  | ( | std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _links_ ,   
---|---|---|---  
|  | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
|  | [int](../../d1/da0/classint.html) | _options_ ,   
|  | [int](../../d1/da0/classint.html) | _maxCount_ = `0`,   
|  | const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ = `{}`  
| ) | |  const  
  
Return the links to a given object.

Parameters

     links| holds the links found   
---|---  
obj| the linked object. If NULL, then all links are returned.  
option|  
  
See also

    [App::GetLinkOption](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330c)

Parameters

     maxCount| limit the number of links returned, 0 means no limit   
---|---  
objs| optional objects to search for, if empty, then all objects of this
document are searched.  
  
References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::GetLinkArrayElement](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330cad93eb1fee725f977b21ff4399d0c4716),
[App::GetLinkedObject](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330ca7213ae140b43b66edb12057b2a7aa44a),
[App::GetLinkExternal](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330ca429434c095faf38b91cba085cf5ae423),
[App::GetLinkRecursive](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330caf1d2af7865f9e1796cc3a5c1d9b2f429),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
and
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[hasLinksTo()](../../d8/d3e/classApp_1_1Document.html#a6431188771ccb739c6e711968e423c91),
and
[importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778).

## ◆ getMaxUndoStackSize()

unsigned [int](../../d1/da0/classint.html) Document::getMaxUndoStackSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Set the Undo limit as stack size.

References
[App::DocumentP::UndoMaxStackSize](../../d1/da5/structApp_1_1DocumentP.html#a6dc4ef7a82a38c93bc6348125fbb26b7).

## ◆ getMemSize()

| unsigned [int](../../d1/da0/classint.html) Document::getMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
returns the complete document memory consumption, including all managed
DocObjects and Undo Redo.

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694).

References
[App::PropertyContainer::getMemSize()](../../d5/d48/classApp_1_1PropertyContainer.html#a8c5a34456c147122cd31f15a1b3c5694),
[getUndoMemSize()](../../d8/d3e/classApp_1_1Document.html#aebe1ae8ccbb1e5b3b6506019d61c7eb9),
and
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ getName()

const char * Document::getName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document name.

Label is the visible name of a document shown e.g.

in the windows title or in the tree view. The label almost (but not always
e.g. if you manually change it) matches with the file name where the document
is stored to. In contrast to Label the method
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d
"Get the document name.") returns the internal name of the document that only
matches with Label when loading or creating a document because then both are
set to the same value. Since the internal name cannot be changed during
runtime it must differ from the Label after saving the document the first time
or saving it under a new file name. @ note More than one document can have the
same label name. @ note The internal is always guaranteed to be unique because
[Application::newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b)
checks for a document with the same name and makes it unique if needed. Hence
you cannot rely on that the internal name matches with the name you passed to
Application::newDoument(). You should use the method
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d
"Get the document name.") instead.

Referenced by
[MeshPartGui::Tessellation::accept()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#a222ec7598711d0c506f4897d9a996bd1),
[PartDesignGui::TaskShapeBinder::accept()](../../d0/d2a/classPartDesignGui_1_1TaskShapeBinder.html#a5881c04fc2f30c53555576224fab3d45),
[PartGui::FaceColors::Private::addFacesToSelection()](../../d4/d4b/classFaceColors_1_1Private.html#a9eb1efd1782f31dd3bad393299212f3b),
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[Gui::ViewProviderAnnotation::attach()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#ab50892bdc3b37f9da77b36cac3014cf6),
[Gui::ViewProviderOriginFeature::attach()](../../d9/d6a/classGui_1_1ViewProviderOriginFeature.html#aac32ddea00ce5374fa432bad0540355a),
[MeshGui::ViewProviderMesh::attach()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#adb9b6c0cd97337657aabd81bac13e35e),
[PointsGui::ViewProviderScattered::attach()](../../df/dca/classPointsGui_1_1ViewProviderScattered.html#ab6910e935629c8fe18fed5409c9521a0),
[PointsGui::ViewProviderStructured::attach()](../../d4/d20/classPointsGui_1_1ViewProviderStructured.html#aabe6e709079ef4dd2d44b687db5f1dd7),
[Gui::ViewProviderVRMLObject::attach()](../../d0/d55/classGui_1_1ViewProviderVRMLObject.html#a6325dc25a3b586202db6edaf20319937),
[RobotGui::ViewProviderRobotObject::attach()](../../d3/d9f/classRobotGui_1_1ViewProviderRobotObject.html#abfd62beacd9f9981515c67a20b27e813),
[RobotGui::ViewProviderTrajectory::attach()](../../d2/da2/classRobotGui_1_1ViewProviderTrajectory.html#ae0c77a17efe78de9f375f9382cc40da2),
[Gui::DAG::Model::contextMenuEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a929350aab7c7acb610a7d61bdcc644b6),
[App::PropertyXLink::copyTo()](../../d2/de2/classApp_1_1PropertyXLink.html#a19874848830f7ac84fa39aaec584723c),
[App::DocInfo::deinit()](../../d7/d23/classApp_1_1DocInfo.html#a1cdcac3cdb0e8967b2bcd1c3ebbb79ef),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[PartGui::DlgExtrusion::findShapes()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8976c72de1970766d8d2dc5391e34903),
[Gui::LinkInfo::getDocName()](../../d4/da4/classGui_1_1LinkInfo.html#a05c276830a5dbeb05b71c78176ae1d51),
[Gui::View3DInventorPy::getObjectInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a713b1bf47110fdea7202e2fd7c592ca0),
[Gui::View3DInventorPy::getObjectsInfo()](../../d3/df7/classGui_1_1View3DInventorPy.html#a2eff2f6d5d7072fa1b728eb307a215a1),
[App::PropertyLinkSubList::getPyReprString()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#ac644eeeab4af18d5ec980d4f9640fe3b),
[App::PropertyXLinkSubList::getPyReprString()](../../db/de6/classApp_1_1PropertyXLinkSubList.html#a49dc28e937c8ffb0a0739ee83deaeb0a),
[PartDesignGui::getReferencedSelection()](../../dc/d12/namespacePartDesignGui.html#a3f00fb1f14bb1e8917fe623cecd8ab59),
[Gui::SelectionSingleton::isSelected()](../../d4/dca/classGui_1_1SelectionSingleton.html#a821a5d7843e3c3c08e9d6244b4d21e1d),
[Gui::DAG::Model::mousePressEvent()](../../df/d26/classGui_1_1DAG_1_1Model.html#a5507e79687e92d89464f8b95181bb4e5),
[Spreadsheet::Sheet::observeDocument()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a20a52744c90006c6ab84b733e0e06ff7),
[SketcherGui::TaskSketcherConstraints::on_listWidgetConstraints_itemSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#a9dfd693a935f64423cc9106430776263),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemEntered()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a2e956e6abd25667f7e59514a401b0f42),
[SketcherGui::TaskSketcherElements::on_listWidgetElements_itemSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a56cc69945924032683b1845683b9873b),
[Gui::Application::onLastWindowClosed()](../../d9/da8/classGui_1_1Application.html#ab6fa833663f9f2e51031af52fe34865b),
[Gui::TreeWidget::onPreSelectTimer()](../../de/de0/classGui_1_1TreeWidget.html#a0af4d1e04d145e231b0682cf1519fd96),
[Gui::View3DInventor::onRename()](../../da/d75/classGui_1_1View3DInventor.html#aec79630804e9a7336455af443ea2b2a4),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[SketcherGui::TaskSketcherConstraints::onSelectionChanged()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#ad2aa1dfda961213561df408f2bad55df),
[SketcherGui::TaskSketcherElements::onSelectionChanged()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#afafa9c58f43f36216447d6c7df146cfc),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[Gui::Dialog::Placement::Placement()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a61902824aa6953c8333e8d319eab8374),
[TechDrawGui::MDIViewPage::preSelectionChanged()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a003eef537ec84dda708d22f2b57f6bcb),
[Gui::ElementColors::Private::Private()](../../d8/dc9/classElementColors_1_1Private.html#a666b8d911912be6e8e346fcb52592125),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[PartDesignGui::TaskDressUpParameters::referenceSelected()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a4cbc9c9a3ab11fc80333ddf36ad442aa),
[PartDesignGui::TaskPipeParameters::referenceSelected()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a0c0361901e8218cb0848f5c13d58bb3d),
[PartDesignGui::TaskPipeOrientation::referenceSelected()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#a37effe2b23a30b99a63c7184b2175f21),
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a),
[DrawSketchHandlerGenConstraint::releaseButton()](../../d7/dc2/classDrawSketchHandlerGenConstraint.html#a8c9d15e5c489ccb3f06cacaae622f0f3),
[DrawSketchHandlerCoincident::releaseButton()](../../d1/da0/classDrawSketchHandlerCoincident.html#a0aa30cef84692d6048db1607abb8b77f),
[SketcherGui::DrawSketchHandlerFillet::releaseButton()](../../d0/dd8/classSketcherGui_1_1DrawSketchHandlerFillet.html#a609c1d9a57b4231f9a9694381f17a084),
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[Gui::SelectionSingleton::sAddSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a611e09b40ed2a13cb570ad01f2a6e059),
[TechDrawGui::QGSPage::saveSvg()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a7c5dd2c51df61dba9689959c585870d2),
[Gui::SelectionObserver::SelectionObserver()](../../dc/d3c/classGui_1_1SelectionObserver.html#adfbfb276069ea43872dcaae8bdbbc472),
[Gui::DocumentItem::selectItems()](../../df/d15/classGui_1_1DocumentItem.html#a3c85e1bd74fe3545bb27098f5d72cf17),
[Gui::Application::setActiveDocument()](../../d9/da8/classGui_1_1Application.html#a689d6d547879b12ded7364fa0fb7953c),
[Gui::View3DInventorViewer::setDocument()](../../d5/d29/classGui_1_1View3DInventorViewer.html#ad30c5b6e0d48081fd0bcffba8b8f1b4a),
[TechDrawGui::ViewProviderViewPart::setEdit()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a758558e7e660c02f277bc621cb7e2e61),
[SketcherGui::ViewProviderSketch::setEditViewer()](../../dc/de2/classSketcherGui_1_1ViewProviderSketch.html#a7ecefc8f26a51435051a12a6fb73f333),
[PartDesignGui::TaskDressUpParameters::setSelection()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#afbe9ba507cb0b88b7ef7250c5901d975),
[TechDrawGui::MDIViewPage::setTreeToSceneSelect()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a8c4e132accc95406f63a7e555cb1cbfc),
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a3c1579420d89e9689ef90ae453a74b10),
[TechDrawGui::ViewProviderPage::showMDIViewPage()](../../d8/d21/classTechDrawGui_1_1ViewProviderPage.html#a73bc19f9c2666efa58194e253d2678a1),
[Gui::AutoSaver::slotCreateDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#ac494a904b86d92d32163dab8049b0d80),
[Gui::SelectionSingleton::slotDeletedObject()](../../d4/dca/classGui_1_1SelectionSingleton.html#a71d83e67e4de7417667efa24dc4c7ed5),
[Gui::Application::slotDeleteDocument()](../../d9/da8/classGui_1_1Application.html#a71271061511f12b53a3fb590f62b427f),
[Gui::AutoSaver::slotDeleteDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a2357480bca9603a4b3cfebbde5525898),
[Gui::ElementColors::slotDeleteDocument()](../../db/d21/classGui_1_1ElementColors.html#a68c3c6b2c036c91d3f209e189ea3731f),
[Gui::DocumentItem::slotNewObject()](../../df/d15/classGui_1_1DocumentItem.html#ad24f3e10a66bd80062501b2d47c01439),
[Gui::SelectionSingleton::sRemoveSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#af2933a9b72409431f7fd31d78ade3d5c),
[Gui::SelectionSingleton::sSetPreselection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a17d43ab4934b472aa7e9b5bf01127e25),
[Gui::SelectionSingleton::sUpdateSelection()](../../d4/dca/classGui_1_1SelectionSingleton.html#a33194bd56bf9dc3e9e893e8b7a66153b),
[PartDesignGui::TaskFeaturePick::TaskFeaturePick()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a6a91644eabfe77025b57d629f74ebbba),
[PartDesignGui::ViewProvider::unsetEdit()](../../d0/d29/classPartDesignGui_1_1ViewProvider.html#aeb01bc367ec2895032e0fcd1074528fb),
[Gui::ViewProviderInventorObject::updateData()](../../de/ded/classGui_1_1ViewProviderInventorObject.html#acbd38b5d36261642a881af5f20afe8b8),
[PartGui::DlgExtrusion::writeParametersToFeature()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8d059573a157c9f9128d55b3c9a9fcc1),
and
[~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ getObject()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * Document::getObject  | ( | const char *  | _Name_| ) |  const  
---|---|---|---|---|---  
  
Returns a Object of this document.

References
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

Referenced by
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PathGui::TaskDlgPathCompound::accept()](../../d0/d93/classPathGui_1_1TaskDlgPathCompound.html#a9b21fa4e4a95ed2b50942ac6c6adece6),
[SpreadsheetGui::DlgBindSheet::accept()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#ad6e5cb0995aaa1341a57bdb97ed49cbd),
[PartDesignGui::TaskFeaturePick::buildFeatures()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a10945e14aca2a56d0f5ac9e4b0064379),
[Gui::View3DInventorViewer::checkGroupOnTop()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a1d4b9b9b5d9604967758304ac274d931),
[App::ObjectIdentifier::String::checkImport()](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html#a8c71508a5ae7a8b7387e35abe09dac6f),
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::QGSPage::createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[TechDrawGui::TaskDetail::createDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a301980d3db23b9a4d960227c9c78fa03),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[TechDrawGui::TaskSectionView::createSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ac5902eeba616fd351e4de4546c7634de),
[TechDrawGui::TaskWeldingSymbol::createWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a687a7f75b421ef414ad8e8ae46dc7889),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[PartGui::DlgExtrusion::getAxisLink()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#af73d5a43aaa0f3dcee9dff9571f7d518),
[PartGui::DlgRevolution::getAxisLink()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a6a4ccdcedbf3ed5c9c022286a9d211f1),
[TechDrawGui::TaskDetail::getBaseFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a70796612105f92d7d31b7ebe973f3b59),
[TechDrawGui::TaskDetail::getDetailFeat()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a848187db5ab0062bae09709a958df329),
[PartDesignGui::TaskDraftParameters::getLine()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#ac4b37f7ab747d85db228cfc413131022),
[App::GroupExtension::getObject()](../../da/d3a/classApp_1_1GroupExtension.html#a334d367aa8c90d6ecf457792e37ca961),
[Gui::Command::getObject()](../../d2/dff/classGui_1_1Command.html#a6310ae38226900cd42902abe0ce74a9a),
[PartDesignGui::TaskDraftParameters::getPlane()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#a721ea370a65705cc8585ed07b1479839),
[PartDesignGui::getReferencedSelection()](../../dc/d12/namespacePartDesignGui.html#a3f00fb1f14bb1e8917fe623cecd8ab59),
[PartGui::getShapeFromStrings()](../../d5/d49/namespacePartGui.html#a5245fac5abffb33a9341c1523c829f3d),
[Gui::Document::getViewProviderByName()](../../de/d4e/classGui_1_1Document.html#ad3990595a406e1c0c7c6f7e29521f2d0),
[PartDesign::ProfileBased::handleChangedPropertyName()](../../d8/d2f/classPartDesign_1_1ProfileBased.html#afbb7de5553cfce71f0d90927bedb61c9),
[Gui::Command::hasObject()](../../d2/dff/classGui_1_1Command.html#a5791bd230f0af50a4b16ee97bc094f15),
[App::ObjectIdentifier::importSubNames()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a9b14787182eda284b142f3e90881e954),
[PartDesignGui::TaskTransformedParameters::indexesMoved()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#a3b5b194d9abce483eb434ae97ede1fac),
[TechDrawGui::TaskSectionView::isBaseValid()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a68e096d0dafe1c18a42596c5027a8dfe),
[TechDrawGui::TaskSectionView::isSectionValid()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#a88b53bce663338633b0d88beadd3d2b2),
[PartDesignGui::TaskSketchBasedParameters::onAddSelection()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#a21b691abf9e5be5455e3321bd7e5165a),
[PartGui::SectionCut::onCutXvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a4a305558bdd21a361634d0f5ad8ddc48),
[PartGui::SectionCut::onCutYvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#aa58ac87ff13537e2ac5f4d4453635d26),
[PartGui::SectionCut::onCutZvalueChanged()](../../de/dd6/classPartGui_1_1SectionCut.html#a7fae0b00d8375b23528539c3250eb336),
[PartGui::SectionCut::onFlipXclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a5fbc3a06b93ca2cc623e4c60b2d8b0cd),
[PartGui::SectionCut::onFlipYclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a086343100aa8f33a1f885130b13fa4ad),
[PartGui::SectionCut::onFlipZclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a56a8cd5a5ec5c2228e4d5a5f8a8c232a),
[PartGui::SectionCut::onRefreshCutPBclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a27de80c7c591178a8f37bef034294d8a),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[SketcherGui::DrawSketchHandlerCarbonCopy::onSelectionChanged()](../../d8/dcc/classSketcherGui_1_1DrawSketchHandlerCarbonCopy.html#a0abe4b682958afcce6e53de58d3225fa),
[SketcherGui::DrawSketchHandlerExternal::onSelectionChanged()](../../d5/d95/classSketcherGui_1_1DrawSketchHandlerExternal.html#aab1764f7bd2af3f2cf49a7131a443253),
[PartDesignGui::TaskTransformedParameters::originalSelected()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#adb918122e8572632cc17114506d98ccd),
[DrawingGui::OrthoViews::OrthoViews()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#ad9c99867cbd96fff40a1c05750e12033),
[readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[PartDesignGui::TaskPipeParameters::referenceSelected()](../../d5/dd6/classPartDesignGui_1_1TaskPipeParameters.html#a0c0361901e8218cb0848f5c13d58bb3d),
[PartDesignGui::TaskPipeOrientation::referenceSelected()](../../d8/df3/classPartDesignGui_1_1TaskPipeOrientation.html#a37effe2b23a30b99a63c7184b2175f21),
[PartDesignGui::TaskPipeScaling::referenceSelected()](../../d0/d7b/classPartDesignGui_1_1TaskPipeScaling.html#ac9f1c0754a7abf2a4e59c0218c73829a),
[App::ObjectIdentifier::resolve()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a8dfd88a7d54bc8d12a3747b5b35747ed),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[App::PropertyLink::Restore()](../../d4/d77/classApp_1_1PropertyLink.html#ac8b73884f15976a6f8c4ad68648fdbb4),
[App::PropertyLinkList::Restore()](../../d3/d8c/classApp_1_1PropertyLinkList.html#aa8e455005308c03a8311dd85e8816e2b),
[App::PropertyLinkSub::Restore()](../../d3/d76/classApp_1_1PropertyLinkSub.html#aab23a24b62b98c8cb5ddbf5cff4b00ae),
[App::PropertyLinkSubList::Restore()](../../d9/d92/classApp_1_1PropertyLinkSubList.html#a8fff6b4c7c062bc0d06d8024ada3329b),
[App::PropertyXLink::Restore()](../../d2/de2/classApp_1_1PropertyXLink.html#ac650cae512a69371cd69071ab6afc64c),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
[Gui::SelectionSingleton::setPreselect()](../../d4/dca/classGui_1_1SelectionSingleton.html#a4606b917610c1a4ba91821e5405973ab),
[PartDesignGui::TaskSketchBasedParameters::setUpToFace()](../../d1/d4b/classPartDesignGui_1_1TaskSketchBasedParameters.html#acd1f7bc55f973a0923ef8c31bf3e2ee5),
[App::PropertyXLink::setValue()](../../d2/de2/classApp_1_1PropertyXLink.html#a08df921d547d315b596fe24b593f8637),
and
[TechDrawGui::TaskLinkDim::updateDims()](../../d1/d54/classTechDrawGui_1_1TaskLinkDim.html#acff44dd09f905319bf7234cd9c0afd2e).

## ◆ getObjectByID()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * Document::getObjectByID  | ( | long  | _id_| ) |  const  
---|---|---|---|---|---  
  
Returns a Object of this document by its id.

References
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3).

Referenced by
[App::LinkBaseExtension::extensionExecute()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6b836b309b3fdb1f05be0c94d02ee693),
and
[moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5).

## ◆ getObjectName()

const char * Document::getObjectName  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _pFeat_| ) |  const  
---|---|---|---|---|---  
  
Returns a Name of an Object or 0.

References
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

## ◆ getObjects()

const std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & Document::getObjects  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of all Objects.

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[Gui::ViewProviderDocumentObject::findFrontRootOfType()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#a078851e515af6065c4daeaa5f2fc654f),
[PartDesignGui::ViewProviderDatum::getRelevantBoundBox()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#ab70e87f8a87a50222337b00c4ef6d945),
[getStandardObjectName()](../../d8/d3e/classApp_1_1Document.html#a3d17fc869ebcefabfa83b1adb5665ec5),
[Gui::DAG::Model::Model()](../../df/d26/classGui_1_1DAG_1_1Model.html#a81b067d165657725e854c9ce8e038fec),
[PartGui::SectionCut::onRefreshCutPBclicked()](../../de/dd6/classPartGui_1_1SectionCut.html#a27de80c7c591178a8f37bef034294d8a),
[PartGui::SectionCut::SectionCut()](../../de/dd6/classPartGui_1_1SectionCut.html#a4eab76cf60be067f8b0b55520d1d3f3f),
and
[Gui::TreeWidget::startItemSearch()](../../de/de0/classGui_1_1TreeWidget.html#a514d3093b96acbf0912338a906dfc8ac).

## ◆ getObjectsOfType() [1/2]

template<typename T >

std::vector< T * > Document::getObjectsOfType  
---  
  
Returns an array with the correct types already.

References
[getObjectsOfType()](../../d8/d3e/classApp_1_1Document.html#ad2e63817274934f5c148456ac593d8f0).

Referenced by
[getObjectsOfType()](../../d8/d3e/classApp_1_1Document.html#ad2e63817274934f5c148456ac593d8f0).

## ◆ getObjectsOfType() [2/2]

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getObjectsOfType  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _typeId_| ) |  const  
---|---|---|---|---|---  
  
References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[ReverseEngineeringGui::SegmentationManual::createSegment()](../../dc/d04/classReverseEngineeringGui_1_1SegmentationManual.html#a95ac22eb241f58d992ffe08f784eb5d0),
[SpreadsheetGui::DlgBindSheet::DlgBindSheet()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#accc9c51aedc023f92d7d5a21304b0b62),
[ReverseEngineeringGui::SegmentationManual::Private::findGeometry()](../../dc/dc5/classSegmentationManual_1_1Private.html#ab79497cfd7a37b25ceb430dabaadb41a),
[TechDrawGui::DrawGuiUtil::findPage()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a5e81d631634196d2c5fe0d083fd7cb9b),
[PartGui::DlgExtrusion::findShapes()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8976c72de1970766d8d2dc5391e34903),
[PartGui::DlgFilletEdges::findShapes()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a3bd2ba2fd4b83d69ee72ad80a4cae2e4),
[Fem::FemPostFilter::getInputData()](../../d8/d6f/classFem_1_1FemPostFilter.html#ae3dbe91d8a70d85554e49b2f9d3a079b),
[PartDesignGui::getPartFor()](../../dc/d12/namespacePartDesignGui.html#aa97e68f5d6560bdaaad701f3cfe50dc4),
[TechDrawGui::DrawGuiUtil::needPage()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a4c52b5348f0784d3c0679c33bf99804d),
[TechDrawGui::DrawGuiUtil::needView()](../../d3/d00/classTechDrawGui_1_1DrawGuiUtil.html#a6062f181af83a85f81e62e169db5402a),
[MeshGui::DlgEvaluateMeshImp::on_meshNameButton_activated()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ae54004188b150e536ff0d1a2fec6c314),
[MeshGui::DlgEvaluateMeshImp::refreshList()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a09df67f594d7ad5fa40960e816fc8f4a),
and
[FemGui::TaskFemConstraintFluidBoundary::TaskFemConstraintFluidBoundary()](../../d2/ddd/classFemGui_1_1TaskFemConstraintFluidBoundary.html#a8dc3dbab3cda8a07ed5f8d47cc6796b1).

## ◆ getObjectsWithExtension()

std::vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getObjectsWithExtension  | ( | const [Base::Type](../../dc/dee/classBase_1_1Type.html) & | _typeId_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _derived_ = `true`  
| ) | |  const  
  
Returns all object with given extensions. If derived=true also all objects
with extensions derived from the given one.

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ getOldLabel()

const std::string & App::Document::getOldLabel  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[App::RelabelDocumentExpressionVisitor::visit()](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#aa37c20588af574df4ceaa95468660f18).

## ◆ getPathsByOutList()

std::vector< std::list< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > > Document::getPathsByOutList  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _from_ ,   
---|---|---|---  
|  | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _to_  
| ) | |  const  
  
get all possible paths from one object to another following the OutList

References
[draftfunctions.array::array()](../../d2/d57/group__draftfunctions.html#gadf79960ae21167271a07cc16e0a58027),
[DraftVecUtils::find()](../../dc/dc3/group__DRAFTVECUTILS.html#gaf764683bba7871d8f3d64db4fb2a41a9),
[App::DocumentP::findAllPathsAt()](../../d1/da5/structApp_1_1DocumentP.html#a028ece0723e817ca53c9b27ac1d3b555),
and
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ getProgramVersion()

const char * Document::getProgramVersion  | ( | | ) |  const  
---|---|---|---|---  
  
Get program version the project file was created with.

References
[App::DocumentP::programVersion](../../d1/da5/structApp_1_1DocumentP.html#a9395c4a4c0e81cab96512cdf700e1a48).

## ◆ getPyObject()

| [PyObject](../../df/d1b/classPyObject.html) * Document::getPyObject  | ( | void  | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
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

References
[App::DocumentP::DocumentPythonObject](../../d1/da5/structApp_1_1DocumentP.html#add40c1bb1337e43508a99b19d306083a).

Referenced by
[App::Application::setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94).

## ◆ getRootObjects()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getRootObjects  | ( | | ) |  const  
---|---|---|---|---  
  
get all root objects (objects no other one reference too)

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ getStandardObjectName()

std::string Document::getStandardObjectName  | ( | const char *  | _Name_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _d_  
| ) | |  const  
  
Returns a name of the form prefix_number. d specifies the number of digits.

References
[getObjects()](../../d8/d3e/classApp_1_1Document.html#a9eb8bb2a620e09a4b164f019c3b3b07f),
and
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b).

## ◆ getTouched()

vector< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::getTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
returns all touched objects

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ getTransactionID()

[int](../../d1/da0/classint.html) Document::getTransactionID  | ( | [bool](../../d9/db9/classbool.html) | _undo_ ,   
---|---|---|---  
|  | unsigned  | _pos_ = `0`  
| ) | |  const  
  
Return the undo/redo transaction ID starting from the back.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a),
and
[undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ getTransientDirectoryName()

| std::string Document::getTransientDirectoryName  | ( | const std::string & | _uuid_ ,   
---|---|---|---  
|  | const std::string & | _filename_  
| ) | |  const  
protected  
  
References
[App::Application::getExecutableName()](../../da/dbf/classApp_1_1Application.html#aa4e204b1a63dd706b0132e4532360cdc),
and
[App::Application::getUserCachePath()](../../da/dbf/classApp_1_1Application.html#a902b031dddf45438919f61a5e8075b7f).

Referenced by
[onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a).

## ◆ getUndoMemSize()

unsigned [int](../../d1/da0/classint.html) Document::getUndoMemSize  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Returns the actual memory consumption of the Undo redo stuff.

References
[App::DocumentP::UndoMemSize](../../d1/da5/structApp_1_1DocumentP.html#a22dd5ded3943792598d2c96703a63a3c).

Referenced by
[getMemSize()](../../d8/d3e/classApp_1_1Document.html#a5a28fe2ed0a864dcd294f81bf2fa3043).

## ◆ getUndoMode()

[int](../../d1/da0/classint.html) Document::getUndoMode  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
switch the level of Undo/Redo

References
[App::DocumentP::iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8).

## ◆ getUniqueObjectName()

std::string Document::getUniqueObjectName  | ( | const char *  | _Name_| ) |  const  
---|---|---|---|---|---  
  
Returns a Name of an Object or 0.

References
[Base::Tools::getIdentifier()](../../d6/dda/structBase_1_1Tools.html#a49653de3f8677d06572f26f1f002641d),
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b),
[KeepTrailingDigits](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a844e41986bdfe3e2ff29054fc8aaeb55),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
and
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87).

Referenced by
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[TechDraw::DrawProjGroup::addProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#acfc4e756c8714973996318393180f483),
[TechDrawGui::TaskActiveView::createActiveView()](../../dd/dea/classTechDrawGui_1_1TaskActiveView.html#a06f867ac197d21160c2b15c19b71718d),
[TechDrawGui::TaskRichAnno::createAnnoFeature()](../../da/d63/classTechDrawGui_1_1TaskRichAnno.html#a22ed5de958ff1fc25c0e8252a1d94772),
[TechDrawGui::QGSPage::createBalloon()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#afa6582dc212925fd365ed71b38127d78),
[TechDrawGui::TaskDetail::createDetail()](../../d9/d7f/classTechDrawGui_1_1TaskDetail.html#a301980d3db23b9a4d960227c9c78fa03),
[TechDrawGui::TaskLeaderLine::createLeaderFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#aa373a025019c506efe972ffde78b7007),
[TechDrawGui::TaskSectionView::createSectionView()](../../d4/d65/classTechDrawGui_1_1TaskSectionView.html#ac5902eeba616fd351e4de4546c7634de),
[TechDrawGui::TaskWeldingSymbol::createWeldingSymbol()](../../db/d62/classTechDrawGui_1_1TaskWeldingSymbol.html#a687a7f75b421ef414ad8e8ae46dc7889),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5),
[DrawingGui::orthoview::orthoview()](../../db/df8/classDrawingGui_1_1orthoview.html#afc8be37cc7e9325e722e05f2736af13d),
and
[App::LinkBaseExtension::setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4).

## ◆ hasLinksTo()

[bool](../../d9/db9/classbool.html) Document::hasLinksTo  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
  
Check if there is any link to the given object.

References
[getLinksTo()](../../d8/d3e/classApp_1_1Document.html#a68fa1555a634a2da10ba434f64fbf2f2).

## ◆ hasPendingTransaction()

[bool](../../d9/db9/classbool.html) Document::hasPendingTransaction  | ( | | ) |  const  
---|---|---|---|---  
  
Check if a transaction is open.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b).

Referenced by
[Gui::Document::hasPendingCommand()](../../de/d4e/classGui_1_1Document.html#a24e0724bc68f0a5d1eaf141a3b75ed69).

## ◆ importLinks()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::importLinks  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ = `{}`| ) |   
---|---|---|---|---|---  
  
[Import](../../df/df2/namespaceImport.html) any externally linked objects.

Parameters

     objs| input list of objects. Only objects belonging to this document will be checked for external links. And all found external linked object will be imported to this document. [Link](../../df/d9b/classApp_1_1Link.html) type properties of those input objects will be automatically reassigned to the imported objects. Note that the link properties of other objects in the document but not included in the input list, will not be affected even if they point to some object beining imported. To import all objects, simply pass in all objects of this document.  
---|---  
  
Returns

    the list of imported objects 

References
[Base::FileInfo::deleteFile()](../../dd/d34/classBase_1_1FileInfo.html#aafd7a8df3d22c3e48523afe865115b9c),
[exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
[getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
[App::GetLinkExternal](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330ca429434c095faf38b91cba085cf5ae423),
[getLinksTo()](../../d8/d3e/classApp_1_1Document.html#a68fa1555a634a2da10ba434f64fbf2f2),
[App::MergeDocuments::getNameMap()](../../d6/d0c/classApp_1_1MergeDocuments.html#aaeb37ec63dcd5d3d2fedaaf4e9774a57),
[App::Application::getTempFileName()](../../da/dbf/classApp_1_1Application.html#a6550097c7ee9c3857f8190954acfbf48),
[App::Property::Immutable](../../d0/da9/classApp_1_1Property.html#a8aade5df6d747725f65d152be76c2014a59d0f940edf009b9ffbe01ed43d767cc),
[App::MergeDocuments::importObjects()](../../d6/d0c/classApp_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6),
and
[App::PartialObject](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3aadddc278250236b1498067f68f109203f).

## ◆ importObjects()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::importObjects  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_| ) |   
---|---|---|---|---|---  
  
References
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[Base::Uuid::createUuid()](../../d6/d43/classBase_1_1Uuid.html#a4f0fb93733c226a06e1401083b6071ec),
[Base::XMLReader::DocumentSchema](../../dc/d95/classBase_1_1XMLReader.html#a74af603513fa80d2be16b626f023223a),
[Base::XMLReader::FileVersion](../../dc/d95/classBase_1_1XMLReader.html#aa1e0b79c86e73f829e400840f52eaadf),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[Base::XMLReader::getAttributeAsUnsigned()](../../dc/d95/classBase_1_1XMLReader.html#ac384789d0b975c7caee3762a236d951c),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[App::ObjImporting](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3aabb8a5d126dfca90b5040aabe5973a079),
[Base::XMLReader::ProgramVersion](../../dc/d95/classBase_1_1XMLReader.html#a8de5cc0038e7b748554f9d82757e3c22),
[App::Prop_Hidden](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a292c9a5838da78cc873b94a5ed8f79c6),
[App::Prop_Output](../../dd/dc2/namespaceApp.html#ac0b635e73c879983949e16c13d8d0a48a2f4f0fc70a512ce25e4c7ecb43a0eaa7),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[App::PropertyUUID::setValue()](../../d2/d6c/classApp_1_1PropertyUUID.html#ab6d9418f4d048c0d0070c9c45a9233d2),
[signalFinishImportObjects](../../d8/d3e/classApp_1_1Document.html#aebc7d06f469b48341bfd7c4561184ce7),
and
[signalImportObjects](../../d8/d3e/classApp_1_1Document.html#a71ee0e5d774a93a47c7db5964906a38d).

Referenced by
[App::MergeDocuments::importObjects()](../../d6/d0c/classApp_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6),
and
[Gui::MergeDocuments::importObjects()](../../d5/d20/classGui_1_1MergeDocuments.html#a5595abca6c0ef7a2a760ef63eca6b4c6).

## ◆ isAnyRestoring()

| [bool](../../d9/db9/classbool.html) Document::isAnyRestoring  | ( | | ) |   
---|---|---|---|---  
static  
  
Indicate if there is any document restoring/importing.

Referenced by
[App::Application::isRestoring()](../../da/dbf/classApp_1_1Application.html#aa808751cb4b819afd2b2cab35c85cd1e),
[Gui::ViewProviderDocumentObject::onPropertyStatusChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#aa158bb0312285eb7672f123e8a1359de),
[App::LinkBaseExtension::setLink()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a2e8deb2b1594c12c3d8d46f423d71fe4),
and
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ isClosable()

[bool](../../d9/db9/classbool.html) Document::isClosable  | ( | | ) |  const  
---|---|---|---|---  
  
check whether the document can be closed

References
[Closable](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553affc4864219c40e54946a53110d9d3bc2),
and
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87).

## ◆ isExporting()

[Document::ExportStatus](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81db) Document::isExporting  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
  
References
[NotExporting](../../d8/d3e/classApp_1_1Document.html#a79e74915b6ed38e96cec08824fbc81dba2ccba4649e0148c3fbe078a631ed5049),
[DocExportStatus::objs](../../d6/ddb/structDocExportStatus.html#a60ac9f1c897dc5a40534c9b86e64695b),
and
[DocExportStatus::status](../../d6/ddb/structDocExportStatus.html#aded29f4cea5a5a9e8e04aacdb2ef37a7).

Referenced by
[writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

## ◆ isIn()

[bool](../../d9/db9/classbool.html) Document::isIn  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _pFeat_| ) |  const  
---|---|---|---|---|---  
  
Returns true if the
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of
all Classes handled in the Document.") is contained in this document.

References
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

Referenced by
[PartDesignGui::ComboLinks::getLink()](../../d8/df8/classPartDesignGui_1_1ComboLinks.html#a714b75c9a2c9395178fc21dfc82a24ff),
[PartDesignGui::TaskExtrudeParameters::getReferenceAxis()](../../d7/d0a/classPartDesignGui_1_1TaskExtrudeParameters.html#afe979e086d9b00ec0c5dce152180b17e),
[PartDesignGui::TaskHelixParameters::getReferenceAxis()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#a5300ff77122113e8bd182eaf761db892),
and
[PartDesignGui::TaskRevolutionParameters::getReferenceAxis()](../../de/d8f/classPartDesignGui_1_1TaskRevolutionParameters.html#ae93d24dcfea0ba9559c889738d3d3770).

## ◆ isPerformingTransaction()

[bool](../../d9/db9/classbool.html) Document::isPerformingTransaction  | ( | | ) |  const  
---|---|---|---|---  
  
returns true if the document is in an
[Transaction](../../de/dbf/classApp_1_1Transaction.html "Represents a atomic
transaction of the document.") phase, e.g. currently performing a redo/undo or
rollback

References
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

Referenced by
[abortTransaction()](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041),
[addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02),
[App::LinkBaseExtension::checkCopyOnChange()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a6521528d36c644c2b1de74a2f74d82c0),
[clearUndos()](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55),
[commitTransaction()](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01),
[openTransaction()](../../d8/d3e/classApp_1_1Document.html#a8e5586f3164279fa8f4dcbfd42009688),
and
[App::LinkBaseExtension::update()](../../da/dd9/classApp_1_1LinkBaseExtension.html#a9aff60c5c842380e08a280e666641979).

## ◆ isSaved()

[bool](../../d9/db9/classbool.html) Document::isSaved  | ( | | ) |  const  
---|---|---|---|---  
  
Opens the document from its file name.

Is the document already saved to a file?

References
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
and
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485).

Referenced by
[copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
and
[Import::ImportOCAF2::setMode()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a865601fce708b9141eb0bbf40b3e96f8).

## ◆ isTouched()

[bool](../../d9/db9/classbool.html) Document::isTouched  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
check if there is any touched object in this document

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ isTransactionEmpty()

[bool](../../d9/db9/classbool.html) Document::isTransactionEmpty  | ( | | ) |  const  
---|---|---|---|---  
  
Check if a transaction is open and its list is empty.

If no transaction is open true is returned.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b).

## ◆ moveObject()

[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * Document::moveObject  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `false`  
| ) | |   
  
Move an object from another document to this document If _recursive_ is true
then all objects this object depends on are moved as well.

By default _recursive_ is false. Returns the moved object itself or 0 if the
object is already part of this document..

References
[breakDependency()](../../d8/d3e/classApp_1_1Document.html#af9123db5f932f908555bd61c8db2fb53),
[copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
[DepNoXLinked](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a76564d229c609eca9e50b9dab37f1e3c),
[DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926),
[getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
[getObjectByID()](../../d8/d3e/classApp_1_1Document.html#affd903adb0b7171d0a8005d4f68fed26),
[getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[App::DocumentP::iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8),
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
and
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b).

Referenced by
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f).

## ◆ mustExecute()

[bool](../../d9/db9/classbool.html) Document::mustExecute  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
check if there is any object must execute in this document

References
[App::PropertyXLink::hasXLink()](../../d2/de2/classApp_1_1PropertyXLink.html#a9b5a3af810860e7117ad6f11e5d4c7e1),
and
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[StdCmdRefresh::isActive()](../../db/d0a/classStdCmdRefresh.html#aff2cd385d8a4bf5b2f5eaa9159e6d711),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
and
[Gui::Document::save()](../../de/d4e/classGui_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c).

## ◆ onBeforeChange()

| void Document::onBeforeChange  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
get called before the value is changed

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a7d84029e2929bf0974a48c564ded3057).

References
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
and
[signalBeforeChange](../../d8/d3e/classApp_1_1Document.html#a3161138e6e5940b1c7bf9da50c75e220).

Referenced by
[PathScripts.PathGui.QuantitySpinBox::updateProperty()](../../dc/de0/classPathScripts_1_1PathGui_1_1QuantitySpinBox.html#a8b9b202d7b495b666cb1f6b41ab2beb4).

## ◆ onBeforeChangeProperty()

| void Document::onBeforeChangeProperty  | ( | const [TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html) *  | _Who_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _What_  
| ) | |   
protected  
  
callback from the [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") objects before property will be changed

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::addObjectChange()](../../de/dbf/classApp_1_1Transaction.html#a49570b3477b90ad3f35dae121668ea87),
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[Base::BaseClass::isDerivedFrom()](../../df/d4d/classBase_1_1BaseClass.html#ac0aa6b7835ac8a11363cf54d84c5c127),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
and
[signalBeforeChangeObject](../../d8/d3e/classApp_1_1Document.html#a1a324d850ff61d951de831c7918cf58c).

## ◆ onChanged()

| void Document::onChanged  | ( | const [Property](../../d0/da9/classApp_1_1Property.html) *  | | ) |   
---|---|---|---|---|---  
overrideprotectedvirtual  
  
get called by the container when a property has changed

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#ab9705aa8b662b534f1a3a6c7b77f1a34).

References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::FileInfo::createDirectories()](../../dd/d34/classBase_1_1FileInfo.html#ae2b639e68c2acc94843eced585d3fb08),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::PropertyString::getStrValue()](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2),
[getTransientDirectoryName()](../../d8/d3e/classApp_1_1Document.html#a787fa9500a9467131f2fb940083e4300),
[App::PropertyUUID::getValueStr()](../../d2/d6c/classApp_1_1PropertyUUID.html#aaa0f9073d79e4846eb7f6266585b3c92),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
[Base::FileInfo::renameFile()](../../dd/d34/classBase_1_1FileInfo.html#ac5067c657858a93f81d2fbfdd4fdf8eb),
[App::PropertyUUID::setValue()](../../d2/d6c/classApp_1_1PropertyUUID.html#ab6d9418f4d048c0d0070c9c45a9233d2),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[ShowHidden](../../d8/d3e/classApp_1_1Document.html#ad993906aa4a429aa7882fc17160cc65e),
[signalChanged](../../d8/d3e/classApp_1_1Document.html#a5561f170a06f38fbd3897839dad67839),
[App::Application::signalRelabelDocument](../../da/dbf/classApp_1_1Application.html#a18013255316c0f5798925e87fc145f6f),
[App::Application::signalShowHidden](../../da/dbf/classApp_1_1Application.html#a5c4a9d78e70440dbcde1a8ec275aae51),
[TransientDir](../../d8/d3e/classApp_1_1Document.html#ac90f8f59e978c2dbd5b043461852628f),
[Uid](../../d8/d3e/classApp_1_1Document.html#af3b3acc44a20bd990bf2e97f5116d3c6),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[ArchStructure.CommandStructuralSystem::Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft::attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass::buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire::execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchBuildingPart.ViewProviderBuildingPart::updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut::updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet::updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel::updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer::updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy::updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ onChangedProperty()

| void Document::onChangedProperty  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _Who_ ,   
---|---|---|---  
|  | const [Property](../../d0/da9/classApp_1_1Property.html) *  | _What_  
| ) | |   
protected  
  
callback from the [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") objects after property was changed

References
[signalChangedObject](../../d8/d3e/classApp_1_1Document.html#a470e043516ad94f89aa8060bd61e51a5).

## ◆ openTransaction()

void Document::openTransaction  | ( | const char *  | _name_ = `nullptr`| ) |   
---|---|---|---|---|---  
  
Open a new command Undo/Redo, an UTF-8 name can be specified.

Parameters

     name| transaction name  
---|---  
  
This function calls App::Application::setActiveTransaction(name) instead to
setup a potential transaction which will only be created if there is actual
changes.

References
[App::DocumentP::committing](../../d1/da5/structApp_1_1DocumentP.html#ac660a92e93876ba22cfcb157dcbcc9a2),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[isPerformingTransaction()](../../d8/d3e/classApp_1_1Document.html#a8be98164cb0d3ed2861566581378e8a2),
and
[App::Application::setActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff).

Referenced by
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[PartGui::DlgExtrusion::apply()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a6428c7ac6585ad41ed9792aeea96d2f7),
[PartGui::DlgProjectionOnSurface::DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a280d8ac8bf690484a268f54625c2c7e2),
[PartDesignGui::getReferencedSelection()](../../dc/d12/namespacePartDesignGui.html#a3f00fb1f14bb1e8917fe623cecd8ab59),
[Gui::Document::openCommand()](../../de/d4e/classGui_1_1Document.html#a652117dfd07edad99558ffb8b3e3d6eb),
and
[DrawingGui::OrthoViews::OrthoViews()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#ad9c99867cbd96fff40a1c05750e12033).

## ◆ purgeTouched()

void Document::purgeTouched  | ( | | ) |   
---|---|---|---|---  
  
Remove all modifications. After this call The document becomes Valid again.

Remove all modifications. After this call The document becomes valid again.

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

## ◆ readObjects()

| std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::readObjects  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | _reader_| ) |   
---|---|---|---|---|---  
protected  
  
References
[Base::XMLReader::addName()](../../dc/d95/classBase_1_1XMLReader.html#a96a6be27f027068b5260c1df328faea4),
[addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[App::DocumentP::addRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#aaf1f87bf25a914489c0b6a511f26637f),
[Base::XMLReader::clearPartialRestoreDocumentObject()](../../dc/d95/classBase_1_1XMLReader.html#a050bbb542ef0f85cca44204fc1d961a2),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::XMLReader::doNameMapping()](../../dc/d95/classBase_1_1XMLReader.html#a1d431382d6f452a2a87cb9c7462d6e72),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[App::DocumentObject::getFullName()](../../d2/de4/classApp_1_1DocumentObject.html#ab9ad25e711d56a5d6c8ba0f7638a8a62),
[Base::XMLReader::getName()](../../dc/d95/classBase_1_1XMLReader.html#aa529233af401d7719226293c506792f8),
[getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[KeepTrailingDigits](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a844e41986bdfe3e2ff29054fc8aaeb55),
[App::DocumentP::lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[App::DocumentP::partialLoadObjects](../../d1/da5/structApp_1_1DocumentP.html#a0ccc9352fd58548a8148a35736c00b2d),
[App::PartialObject](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3aadddc278250236b1498067f68f109203f),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[App::ExtensionContainer::Restore()](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48),
[App::DocumentObject::setStatus()](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815),
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525),
[App::DocumentObject::testStatus()](../../d2/de4/classApp_1_1DocumentObject.html#ae2c0235780263905462da7d93c7f4120),
[Base::XMLReader::testStatus()](../../dc/d95/classBase_1_1XMLReader.html#a1f076d2b8f0c7ff3257cfa6fc595c06c),
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
and
[App::DocumentP::touchedObjs](../../d1/da5/structApp_1_1DocumentP.html#a7b3a34196818f63f6878c8026e3badc9).

Referenced by
[importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff),
and
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82).

## ◆ recompute()

[int](../../d1/da0/classint.html) Document::recompute  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _objs_ = `{}`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _force_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) *  | _hasError_ = `nullptr`,   
|  | [int](../../d1/da0/classint.html) | _options_ = `0`  
| ) | |   
  
Recompute touched features and return the number of recalculated features.

Parameters

     objs| specify a sub set of objects to recompute. If empty, then all object in this document is checked for recompute   
---|---  
  
References
[App::DocumentP::clearRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#abe4686fb5139ebfdab04dabb67405c3a),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[DepSort](../../d8/d3e/classApp_1_1Document.html#a93ba5547d6005d9fe78baa0a6f5f0e34a434619a08d5df25eeb3522b258263926),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[getDependencyList()](../../d8/d3e/classApp_1_1Document.html#a07ea2bb44ac29a4c0e89963ac28af323),
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
[mustExecute()](../../d8/d3e/classApp_1_1Document.html#aaaf7a0d2a67cc06d760a16c352117189),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[App::DocumentP::partialTopologicalSort()](../../d1/da5/structApp_1_1DocumentP.html#a9dec0045952043940b9ab4cfaf5a8dc7),
[App::DocumentP::pendingRemove](../../d1/da5/structApp_1_1DocumentP.html#a153a0ccd9556622fc7190fc6e9d81bc7),
[Recomputing](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a35908c043062d1d561b96076a57b5b32),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
[signalBeforeRecompute](../../d8/d3e/classApp_1_1Document.html#a67e257e6d0dd282a8779453179a1f5e8),
[signalRecomputed](../../d8/d3e/classApp_1_1Document.html#a43a9dc921cb2b60ec72b5907e27bac4f),
[signalRecomputedObject](../../d8/d3e/classApp_1_1Document.html#a2f4410d341abe785473aaeea863b851f),
[signalSkipRecompute](../../d8/d3e/classApp_1_1Document.html#ad3041e3063a5c14765f790910b9f941e),
[SkipRecompute](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aecae1faa96484511bd35e20a0bcab282),
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
[topologicalSort()](../../d8/d3e/classApp_1_1Document.html#a2b52886a0a5853bbba52be579f8c1de3),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

Referenced by
[Gui::Dialog::DlgMacroExecuteImp::accept()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#ab7da5ec611b1f01da76f8c3a3729be8d),
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
[Gui::TaskCSysDragger::accept()](../../d2/dff/classGui_1_1TaskCSysDragger.html#ad513cbcf32b69dc11ee35b96cc6a2a64),
[Gui::MacroCommand::activated()](../../dc/d65/classGui_1_1MacroCommand.html#a3e9f3632b6f802aff70a6fa7d55c4ae5),
[Gui::RecentMacrosAction::activateFile()](../../d2/df7/classGui_1_1RecentMacrosAction.html#af0c4e22ea6a1cc194a1e9f1f69e161ed),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[Sandbox::CustomRecomputeEvent::execute()](../../d8/d91/classSandbox_1_1CustomRecomputeEvent.html#a84c7685a04d334085dea4381ba4fb3fe),
[Gui::ManualAlignment::finish()](../../d7/d97/classGui_1_1ManualAlignment.html#ae517ad11cdc17420c4ec5e072f9fc5ea),
[SpreadsheetGui::SheetTableView::pasteClipboard()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a515807fe0797c9e6f83f28139009c68a),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[FemGui::TaskDlgPost::recompute()](../../dc/d22/classFemGui_1_1TaskDlgPost.html#a78cec4f51cde4277bafcd04fbeff2ca4),
[recomputeFeature()](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a),
[TechDrawGui::TaskGeomHatch::reject()](../../d4/dc9/classTechDrawGui_1_1TaskGeomHatch.html#a18ae3da7ea9b2d55123cd563ed408217),
[DrawingGui::OrthoViews::set_Axo()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a44065e1929ec75120970abd507badcae),
[DrawingGui::OrthoViews::set_Axo_scale()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a2cabe14b76954f8353d378fdf79aeb04),
[DrawingGui::OrthoViews::set_hidden()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#af4cc2f182c12a92d23450998c645cbb9),
[DrawingGui::OrthoViews::set_Ortho()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a12af8ee9afe277b0ed1609dced5bd198),
[DrawingGui::OrthoViews::set_smooth()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#a0b8f4ed039a067a174408627e439ef46),
[draftguitools.gui_trackers.arcTracker::setApertureAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#ae8184e1cc740890318e7ff1f47d6e39c),
[draftguitools.gui_trackers.arcTracker::setEndAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#ab89eccea794aaac46af78d966fc93936),
[draftguitools.gui_trackers.arcTracker::setStartAngle()](../../da/d31/classdraftguitools_1_1gui__trackers_1_1arcTracker.html#a34fd35c94ca62926f6c3e741fabfd8df),
[draftguitools.gui_trackers.bsplineTracker::update()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a780d90044fb459aa47487afc9d7979c9),
and
[draftguitools.gui_trackers.bezcurveTracker::update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63).

## ◆ recomputeFeature()

[bool](../../d9/db9/classbool.html) Document::recomputeFeature  | ( | [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _Feat_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _recursive_ = `false`  
| ) | |   
  
Recompute only one feature.

References
[App::DocumentP::clearRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#abe4686fb5139ebfdab04dabb67405c3a),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::DocumentObject::isValid()](../../d2/de4/classApp_1_1DocumentObject.html#ab12285411684f491cee2519c6e6e99ea),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
and
[signalRecomputedObject](../../d8/d3e/classApp_1_1Document.html#a2f4410d341abe785473aaeea863b851f).

Referenced by
[PartDesignGui::TaskDressUpParameters::addAllEdges()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a8b48e7bad7912d3f55e3466bae38ab80),
[PartDesignGui::TaskBoxPrimitives::onBoxHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a107f8b74cdb3bf1a45ed032a9aaf383d),
[PartDesignGui::TaskBoxPrimitives::onBoxLengthChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#abf84392ef886c69cd8a222960378acc5),
[PartDesignGui::TaskBoxPrimitives::onBoxWidthChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa371979bffbc04a3a8e1ad0a927cef13),
[PartDesignGui::TaskBoxPrimitives::onConeAngleChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a7728be961d4a469c0fcb7ec45aeb20af),
[PartDesignGui::TaskBoxPrimitives::onConeHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a436d997cc5ea0b81530da2cb38c1ca35),
[PartDesignGui::TaskBoxPrimitives::onConeRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa3ee11ef5378be9cb7953ddc8f7a584d),
[PartDesignGui::TaskBoxPrimitives::onConeRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a1fa0b97630162d71685b15ea1f566a50),
[PartDesignGui::TaskBoxPrimitives::onCylinderAngleChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a059ada94b80ad3d590e7d4a876873fd1),
[PartDesignGui::TaskBoxPrimitives::onCylinderHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a145b7ffb358a2329d635d9241f8fa33e),
[PartDesignGui::TaskBoxPrimitives::onCylinderRadiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a50f3f9f57898d01184274ec84003fe24),
[PartDesignGui::TaskBoxPrimitives::onCylinderXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86d82d270b60a8432e7d0dde84c18faf),
[PartDesignGui::TaskBoxPrimitives::onCylinderYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73f5a1b7f5cd33180352b92a06b78d53),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a9d43a4073114d3c77de0c3e83548e2c1),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a0fbf7eea3dc32497b8711a646862a8c1),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a73425d913722a9494da32e334929c6d5),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a46c8bb8b6d9f426492b669c354baea99),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#accbe8caafcb8faa22c9c7553aa3fda23),
[PartDesignGui::TaskBoxPrimitives::onEllipsoidRadius3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a35f2c2ddfe3b72affe6fb4545fab11e4),
[PartDesignGui::TaskBoxPrimitives::onPrismCircumradiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a8701cee98cd45d672cffe4010a21ba56),
[PartDesignGui::TaskBoxPrimitives::onPrismHeightChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab037232d561cffcd013f608ed88ce79f),
[PartDesignGui::TaskBoxPrimitives::onPrismPolygonChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a3a30191951932ad49bef38d08c4292fa),
[PartDesignGui::TaskBoxPrimitives::onPrismXSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23b3eea757a08d4b2736fedb9c929066),
[PartDesignGui::TaskBoxPrimitives::onPrismYSkewChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ab96618398004458953e2f5d0e1924d6a),
[PartDesignGui::TaskBooleanParameters::onSelectionChanged()](../../da/d7c/classPartDesignGui_1_1TaskBooleanParameters.html#a286d77193070c54d7c5dac98f2c83e55),
[PartDesignGui::TaskDraftParameters::onSelectionChanged()](../../d6/d74/classPartDesignGui_1_1TaskDraftParameters.html#a8ca0a7704f3a4427df5c4d99eaaf58ad),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa5bfc9f1b87ced6adf49875eba7e90a2),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a27858521e805c7390d3f9039c535cdcf),
[PartDesignGui::TaskBoxPrimitives::onSphereAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aea9a6950dd79c79bd8cb360b2b8c8784),
[PartDesignGui::TaskBoxPrimitives::onSphereRadiusChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a72d9233055fc77ee491dbc8f5587c09c),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ae2e874e2dad51362fd1a56aff1ba6880),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a600166782c2b17052d6236a2406a1439),
[PartDesignGui::TaskBoxPrimitives::onTorusAngle3Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a5a528983f97adab406c5123f6474f620),
[PartDesignGui::TaskBoxPrimitives::onTorusRadius1Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a10c0def5dec5ab5ea0c5705f8cf5768a),
[PartDesignGui::TaskBoxPrimitives::onTorusRadius2Changed()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#ac449268708c99e4c2f03997e3f9553be),
[PartDesignGui::TaskBoxPrimitives::onWedgeX2maxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a1f13f84786f7ef305f26838d9f7e2081),
[PartDesignGui::TaskBoxPrimitives::onWedgeX2minChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a86463e53d3b0a78c4080b51ba415c388),
[PartDesignGui::TaskBoxPrimitives::onWedgeXmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a66204103a06869337ca64985a9b8d6dc),
[PartDesignGui::TaskBoxPrimitives::onWedgeXminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa5c59aeea355f23727b8bdd8d1a515e5),
[PartDesignGui::TaskBoxPrimitives::onWedgeYmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#af07f3d7a82a59fdbfa665ddd905c3be5),
[PartDesignGui::TaskBoxPrimitives::onWedgeYminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa6fe7277dd6ab536363d7954a7d8c84b),
[PartDesignGui::TaskBoxPrimitives::onWedgeZ2maxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#af872884d5d9ecf66a5767b3ab9635383),
[PartDesignGui::TaskBoxPrimitives::onWedgeZ2minChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a57934914e027c65459bd684f13251463),
[PartDesignGui::TaskBoxPrimitives::onWedgeZmaxChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#aa944b296adfac1bcf2f85eaa84b36e89),
[PartDesignGui::TaskBoxPrimitives::onWedgeZminChanged()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a23f1c00dbdb3b7bbc85dc9728096fcc4),
[TechDrawGui::TaskBalloon::recomputeFeature()](../../d9/de3/classTechDrawGui_1_1TaskBalloon.html#af5cbff4b0e924e7d68f9d4009a4a25ba),
[TechDrawGui::TaskDimension::recomputeFeature()](../../d1/da4/classTechDrawGui_1_1TaskDimension.html#ace37001c57b503aa94c7785b465a688b),
[TechDrawGui::TaskLeaderLine::recomputeFeature()](../../db/d46/classTechDrawGui_1_1TaskLeaderLine.html#a530363359c703cdda6b183d978d05ef2),
and
[PartDesignGui::TaskDressUpParameters::referenceSelected()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a4cbc9c9a3ab11fc80333ddf36ad442aa).

## ◆ redo()

[bool](../../d9/db9/classbool.html) Document::redo  | ( | [int](../../d1/da0/classint.html) | _id_ = `0`| ) |   
---|---|---|---|---|---  
  
Will REDO one step, returns False if no redo was done (Redos == 0).

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a),
[App::DocumentP::iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8),
[App::Transaction::Name](../../de/dbf/classApp_1_1Transaction.html#a6245b49f541ec20247d3b46c18152f9a),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
[signalRedo](../../d8/d3e/classApp_1_1Document.html#aad8731a029bc6b5fe0d2841a58647035),
[Transaction](../../d8/d3e/classApp_1_1Document.html#a49982aa325e19f0956d42fde9132caa2),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

Referenced by
[redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
and
[Gui::Document::redo()](../../de/d4e/classGui_1_1Document.html#a88f1cb6c87e53dde4315c1d90d84bbaf).

## ◆ removeObject()

void Document::removeObject  | ( | const char *  | _sName_| ) |   
---|---|---|---|---|---  
  
Remove a feature out of the document.

Remove an object out of the document.

References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::addObjectChange()](../../de/dbf/classApp_1_1Transaction.html#a49570b3477b90ad3f35dae121668ea87),
[App::Transaction::addObjectNew()](../../de/dbf/classApp_1_1Transaction.html#a33d72374a75b0138c6a5c9d71c858cff),
[breakDependency()](../../d8/d3e/classApp_1_1Document.html#af9123db5f932f908555bd61c8db2fb53),
[getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::PropertyLink::getValue()](../../d4/d77/classApp_1_1PropertyLink.html#a1977d393d8e53d0e3d712c78ac851869),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
[App::DocumentP::pendingRemove](../../d1/da5/structApp_1_1DocumentP.html#a153a0ccd9556622fc7190fc6e9d81bc7),
[App::DocumentP::rollback](../../d1/da5/structApp_1_1DocumentP.html#a0c0cf821de8fb616df8b766a72099f0b),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[signalDeletedObject](../../d8/d3e/classApp_1_1Document.html#ad74af2d90beb3a3674e9a9d469ca7d82),
[signalTransactionRemove](../../d8/d3e/classApp_1_1Document.html#a16185f8546d3013d545fc315e44d6d36),
[Tip](../../d8/d3e/classApp_1_1Document.html#aba7262694bf2514f516c74bb90bb7de9),
[TipName](../../d8/d3e/classApp_1_1Document.html#a334536a52d758261510975cad0bcce64),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

Referenced by
[App::GroupExtension::addObject()](../../da/d3a/classApp_1_1GroupExtension.html#aded71f38e22199b9c1b09236517c77ea),
[DrawingGui::orthoview::deleteme()](../../db/df8/classDrawingGui_1_1orthoview.html#a28900b18478b6035f0761a8cad5ddac6),
[Sandbox::CustomRemoveObjectEvent::execute()](../../dd/d6c/classSandbox_1_1CustomRemoveObjectEvent.html#ab4b9935e352a08b939203580fc81ab17),
[moveObject()](../../d8/d3e/classApp_1_1Document.html#a8ddc7cae77b3a62194b0f02a18bd9fc5),
[FemGui::TaskFemConstraint::onButtonWizCancel()](../../df/d80/classFemGui_1_1TaskFemConstraint.html#a40568c82f18e70a3232e6d98acbeada8),
[App::OriginGroupExtension::onExtendedUnsetupObject()](../../da/d09/classApp_1_1OriginGroupExtension.html#a7d908f67bb05fe69e9c30add43aeae27),
and
[TechDraw::DrawProjGroup::removeProjection()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a23d2d0cb8a3447cdb912202f46f27aae).

## ◆ renameObjectIdentifiers()

void Document::renameObjectIdentifiers  | ( | const std::map< [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html), [App::ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) > & | _paths_ ,   
---|---|---|---  
|  | const std::function< [bool](../../d9/db9/classbool.html)(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *)> & | _selector_ = `[](const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *) { return true; }`  
| ) | |   
  
Function called to signal that an object identifier has been renamed.

Signal that object identifiers, typically a property or document object has
been renamed.

This function iterates through all document object in the document, and calls
its renameObjectIdentifiers functions.

Parameters

     paths| Map with current and new names   
---|---  
  
References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106).

Referenced by
[Spreadsheet::PropertySheet::insertColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a265014a33975e005189793fb75251c56),
[Spreadsheet::PropertySheet::insertRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#aa84f3f19aed8b5355d16cece5eb4a5d9),
[Spreadsheet::PropertySheet::removeColumns()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#ada4ceb76fd79dc130476fe307f77e0a1),
[Spreadsheet::PropertySheet::removeRows()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#a5ff589d68c79b8387678e38007f8733f),
and
[Spreadsheet::PropertySheet::setAlias()](../../de/d36/classSpreadsheet_1_1PropertySheet.html#adfe1772d3fe2f5cae99996963db17db2).

## ◆ renameTransaction()

void Document::renameTransaction  | ( | const char *  | _name_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _id_  
| ) | |   
  
Rename the current transaction if the id matches.

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a),
and
[App::Transaction::Name](../../de/dbf/classApp_1_1Transaction.html#a6245b49f541ec20247d3b46c18152f9a).

## ◆ Restore()

| void Document::Restore  | ( | [Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html) & | | ) |   
---|---|---|---|---|---  
overridevirtual  
  
This method is used to restore properties from an XML document.

It uses the XMLReader class, which bases on SAX, to read the in
[Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0
"This method is used to save properties to an XML document.") written
information. Again the Vector as an example:

void
[PropertyVector::Restore](../../d5/d2b/classApp_1_1PropertyVector.html#a4d5e9d4539891c5c0b7e04073378729c
"This method is used to restore properties from an XML
document.")([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html "The
XML reader class This is an important helper class for the store and retrieval
system of objects ...") &reader)

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
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944).

References
[addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::XMLReader::DocumentSchema](../../dc/d95/classBase_1_1XMLReader.html#a74af603513fa80d2be16b626f023223a),
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[Base::XMLReader::FileVersion](../../dc/d95/classBase_1_1XMLReader.html#aa1e0b79c86e73f829e400840f52eaadf),
[Base::XMLReader::getAttribute()](../../dc/d95/classBase_1_1XMLReader.html#a78b5d9a39d0bfbef09cacee62784a788),
[Base::XMLReader::getAttributeAsInteger()](../../dc/d95/classBase_1_1XMLReader.html#a575f139de19ea0e240bab02b57ce341c),
[Base::XMLReader::getAttributeAsUnsigned()](../../dc/d95/classBase_1_1XMLReader.html#ac384789d0b975c7caee3762a236d951c),
[getObject()](../../d8/d3e/classApp_1_1Document.html#a98b557356076f79a2e8f8aac6e84d221),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[Base::XMLReader::hasAttribute()](../../dc/d95/classBase_1_1XMLReader.html#aefe11ae58fde0a85db07e37426817910),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
[Base::ConsoleSingleton::Message()](../../df/dca/classBase_1_1ConsoleSingleton.html#a322664077d1c391e11e07ec903c99e25),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[Base::XMLReader::ProgramVersion](../../dc/d95/classBase_1_1XMLReader.html#a8de5cc0038e7b748554f9d82757e3c22),
[Base::XMLReader::readElement()](../../dc/d95/classBase_1_1XMLReader.html#acb64ef07ee635b9598dba87743ea910e),
[Base::XMLReader::readEndElement()](../../dc/d95/classBase_1_1XMLReader.html#a78b767c277907507951ab71aca3dd4d3),
[readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[App::PropertyContainer::Restore()](../../d5/d48/classApp_1_1PropertyContainer.html#a848d8973cd4d7353bcb3df985e861944),
[App::ExtensionContainer::Restore()](../../d6/d76/classApp_1_1ExtensionContainer.html#a004bf684691accc570954af96e2e3d48),
[App::DocumentObject::setStatus()](../../d2/de4/classApp_1_1DocumentObject.html#a1b07d5324990c1ff193ce4f2927a2815),
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525),
[App::PropertyLink::setValue()](../../d4/d77/classApp_1_1PropertyLink.html#a00199b3763755037794c2f2925a275e1),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[Tip](../../d8/d3e/classApp_1_1Document.html#aba7262694bf2514f516c74bb90bb7de9),
[TipName](../../d8/d3e/classApp_1_1Document.html#a334536a52d758261510975cad0bcce64),
and
[App::DocumentP::touchedObjs](../../d1/da5/structApp_1_1DocumentP.html#a7b3a34196818f63f6878c8026e3badc9).

Referenced by
[restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ restore()

void Document::restore  | ( | const char *  | _filename_ = `nullptr`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _delaySignal_ = `false`,   
|  | const std::vector< std::string > & | _objNames_ = `{}`  
| ) | |   
  
Restore the document from the file in
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.")
[Path](../../da/d2a/classApp_1_1Path.html "Base class of all geometric
document objects.").

References
[App::DocumentP::activeObject](../../d1/da5/structApp_1_1DocumentP.html#a4a939fdcc4b45893be06e4f452abe9d3),
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[App::DocumentP::clearDocument()](../../d1/da5/structApp_1_1DocumentP.html#abc362f5a9b7612e211ecaefbdb15ad55),
[App::DocumentP::clearRecomputeLog()](../../d1/da5/structApp_1_1DocumentP.html#abe4686fb5139ebfdab04dabb67405c3a),
[clearUndos()](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[App::Application::getActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0be953356bea8c16bd958433e3769dd9),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[Base::XMLReader::isValid()](../../dc/d95/classBase_1_1XMLReader.html#a8104be87d837faa87cfc73aeaa6fe7ed),
[App::DocumentP::lastObjectId](../../d1/da5/structApp_1_1DocumentP.html#a38f562dcaf64cf8c2b0ff9ee30741217),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::DocumentP::objectIdMap](../../d1/da5/structApp_1_1DocumentP.html#ac6e81d661475071cc92e2073da7546f3),
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[App::DocumentP::partialLoadObjects](../../d1/da5/structApp_1_1DocumentP.html#a0ccc9352fd58548a8148a35736c00b2d),
[PartialRestore](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aa85fb1ecccf6466736187e1826eab209),
[App::DocumentP::programVersion](../../d1/da5/structApp_1_1DocumentP.html#a9395c4a4c0e81cab96512cdf700e1a48),
[Base::XMLReader::ProgramVersion](../../dc/d95/classBase_1_1XMLReader.html#a8de5cc0038e7b748554f9d82757e3c22),
[Base::XMLReader::readFiles()](../../dc/d95/classBase_1_1XMLReader.html#a53b94bea9a61011f67ee6f5e98e53f16),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[RestoreError](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aad5db64342c0a663e0710bfd56df097c),
[Restoring](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a3ad0fd87f9bec83cb5d1b8096b3b09ec),
[App::Application::setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94),
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525),
[App::Application::signalDeleteDocument](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47),
[App::Application::signalNewDocument](../../da/dbf/classApp_1_1Application.html#a49425118433ce84229402407d5631ea4),
[signalRestoreDocument](../../d8/d3e/classApp_1_1Document.html#a6ca7bad32ddd8c6cfd6088546d140848),
[App::Application::signalStartRestoreDocument](../../da/dbf/classApp_1_1Application.html#a79b377bd369df1b15b2ae2b9181f7f75),
and
[Base::XMLReader::testStatus()](../../dc/d95/classBase_1_1XMLReader.html#a1f076d2b8f0c7ff3257cfa6fc595c06c).

Referenced by
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189).

## ◆ Save()

| void Document::Save  | ( | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | | ) |  const  
---|---|---|---|---|---  
overridevirtual  
  
This method is used to save properties to an XML document.

A good example you'll find in PropertyStandard.cpp, e.g. the vector:

void
[PropertyVector::Save](../../d5/d2b/classApp_1_1PropertyVector.html#aee8aca3fc2bc388fac3c529adbbb8a10
"This method is used to save properties to an XML document.") (Writer &writer)
const

{

writer << writer.ind() << "<PropertyVector valueX=\"" << _cVec.x <<

"\" valueY=\"" << _cVec.y <<

"\" valueZ=\"" << _cVec.z <<"\"/>" << endl;

}

The writer.ind() expression writes the indentation, just for pretty printing
of the XML. As you see, the writing of the XML document is not done with a DOM
implementation because of performance reasons. Therefore the programmer has to
take care that a valid XML document is written. This means closing tags and
writing UTF-8.

See also

    [Base::Writer](../../dd/d4d/classBase_1_1Writer.html "The Writer class This is an important helper class for the store and retrieval system of persistent o...")

Reimplemented from
[App::PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482).

References
[App::Application::Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc),
[Base::Writer::getFileVersion()](../../dd/d4d/classBase_1_1Writer.html#aaf8877bfc94b43f802bbe6b41fadf7ed),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[App::PropertyContainer::Save()](../../d5/d48/classApp_1_1PropertyContainer.html#a414b49d438e231f03a0e2fa573b02482),
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205),
and
[writeObjects()](../../d8/d3e/classApp_1_1Document.html#a39ddd779c668e3c3631f9c1aba46074a).

Referenced by
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
and
[saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ save()

[bool](../../d9/db9/classbool.html) Document::save  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Save the [Document](../../d8/d3e/classApp_1_1Document.html "The document
class.") under a new Name.

Save the document to the file in
[Property](../../d0/da9/classApp_1_1Property.html "Base class of all
properties This is the father of all properties.")
[Path](../../da/d2a/classApp_1_1Path.html "Base class of all geometric
document objects.")

References
[Base::TimeInfo::currentDateTimeString()](../../df/d75/classBase_1_1TimeInfo.html#a395c874b184fdb4fc9ffc90fb4714371),
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetASCII()](../../d4/d97/classParameterGrp.html#a5c579b580966bb5ddb8d07df2da9bc9c),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[App::DocumentObject::getNameInDocument()](../../d2/de4/classApp_1_1DocumentObject.html#a7a51cea9d048f0d1d7f7c02c07d787f1),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[App::PropertyLink::getValue()](../../d4/d77/classApp_1_1PropertyLink.html#a1977d393d8e53d0e3d712c78ac851869),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
[LastModifiedBy](../../d8/d3e/classApp_1_1Document.html#a854ee4bf3d52fe90ed93d91d92767f03),
[LastModifiedDate](../../d8/d3e/classApp_1_1Document.html#a0a381c4d900a31c8cb7d4ef575176768),
[PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[testStatus()](../../d8/d3e/classApp_1_1Document.html#adf6ecec51088dd87cd3f28b9765e4a87),
[Tip](../../d8/d3e/classApp_1_1Document.html#aba7262694bf2514f516c74bb90bb7de9),
and
[TipName](../../d8/d3e/classApp_1_1Document.html#a334536a52d758261510975cad0bcce64).

Referenced by
[Mod.Show.mTempoVis.TempoVis::modify()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a356b61cdf305ec299725a94d8854c54d),
[Mod.Show.mTempoVis.TempoVis::modifyVPProperty()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#aa63b8d331e9128477a94f01fbc77debe),
[draftguitools.gui_setstyle.Draft_SetStyle_TaskPanel::onSaveStyle()](../../df/d78/classdraftguitools_1_1gui__setstyle_1_1Draft__SetStyle__TaskPanel.html#a62078ac8e29f972f667a11bf889acd64),
[saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
and
[Mod.Show.mTempoVis.TempoVis::saveCamera()](../../d7/d98/classMod_1_1Show_1_1mTempoVis_1_1TempoVis.html#a5e350c94234cc5048fcf0c3c645b5b5f).

## ◆ saveAs()

[bool](../../d9/db9/classbool.html) Document::saveAs  | ( | const char *  | _file_| ) |   
---|---|---|---|---|---  
  
References
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[Base::FileInfo::fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[App::PropertyString::getStrValue()](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2),
[Label](../../d8/d3e/classApp_1_1Document.html#a195e9cb1707d0c92d938ec751d8b0a81),
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[App::Property::touch()](../../d0/da9/classApp_1_1Property.html#a9bec8b8a56b405be0dc5e1602b079475),
and
[Uid](../../d8/d3e/classApp_1_1Document.html#af3b3acc44a20bd990bf2e97f5116d3c6).

Referenced by
[PathScripts.PathToolBitCmd.CommandToolBitSave::Activated()](../../df/d30/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitSave.html#a47ec66f1759fa7000c0a90ba594732df),
[PathScripts.PathToolBitCmd.CommandToolBitSave::GetResources()](../../df/d30/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitSave.html#a521f4fdd27aaba4fc64e5d3bcd1720bb),
and
[PathScripts.PathToolBitCmd.CommandToolBitSave::IsActive()](../../df/d30/classPathScripts_1_1PathToolBitCmd_1_1CommandToolBitSave.html#a5e373c714627a6f37bb64497fe5767f4).

## ◆ saveCopy()

[bool](../../d9/db9/classbool.html) Document::saveCopy  | ( | const char *  | _file_| ) |  const  
---|---|---|---|---|---  
  
References
[FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[App::PropertyString::getStrValue()](../../dd/df8/classApp_1_1PropertyString.html#a7fdb947ab6f9552c1dd95a8e634c83c2),
and
[saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ saveToFile()

| [bool](../../d9/db9/classbool.html) Document::saveToFile  | ( | const char *  | _filename_| ) |  const  
---|---|---|---|---|---  
protected  
  
References
[App::BackupPolicy::apply()](../../d1/d16/classApp_1_1BackupPolicy.html#a20fc30df3fe18619c9def41360a8fbf7),
[Base::Uuid::createUuid()](../../d6/d43/classBase_1_1Uuid.html#a4f0fb93733c226a06e1401083b6071ec),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[ParameterGrp::GetASCII()](../../d4/d97/classParameterGrp.html#a5c579b580966bb5ddb8d07df2da9bc9c),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[ParameterGrp::GetInt()](../../d4/d97/classParameterGrp.html#a7057be6b17be9f72ef5c69c1b27696d5),
[App::Application::GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[Base::Writer::hasErrors()](../../dd/d4d/classBase_1_1Writer.html#a63b47ea7f6739149a2df8c4bf6344f3a),
[Base::ZipWriter::putNextEntry()](../../d9/df3/classBase_1_1ZipWriter.html#abb607a9c82879c6ead67f9dee234bd24),
[Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
[Base::ZipWriter::setComment()](../../d9/df3/classBase_1_1ZipWriter.html#a15c873494ac59c3bc50b0875eb34a1fd),
[App::BackupPolicy::setDateFormat()](../../d1/d16/classApp_1_1BackupPolicy.html#a072408f4ed89c724f7dec77c8290da64),
[Base::ZipWriter::setLevel()](../../d9/df3/classBase_1_1ZipWriter.html#a8e1bad6d8787aa75f5d5144ef166b16f),
[Base::Writer::setMode()](../../dd/d4d/classBase_1_1Writer.html#a3a26c2bb6285dcd29c97037cdda5042e),
[App::BackupPolicy::setNumberOfFiles()](../../d1/d16/classApp_1_1BackupPolicy.html#af669769e2db3375d2b7907ebc482495b),
[App::BackupPolicy::setPolicy()](../../d1/d16/classApp_1_1BackupPolicy.html#a938be6a33b9f1d4ee0b55ef7b1733d7f),
[signalFinishSave](../../d8/d3e/classApp_1_1Document.html#a0485e0c50848f1e240028db9e4e1f0fe),
[App::Application::signalSaveDocument](../../da/dbf/classApp_1_1Application.html#afbe487d60d38532c8802d9228d5e5a0b),
[signalSaveDocument](../../d8/d3e/classApp_1_1Document.html#aa923177773d96f8494f550970908d179),
[signalStartSave](../../d8/d3e/classApp_1_1Document.html#a726c6d0ef527f9dfbbfc80e304caf254),
[App::BackupPolicy::Standard](../../d1/d16/classApp_1_1BackupPolicy.html#a1cb10df777ed391db7bdd45dce3c7a4fa9632eed8c0a31099ad9a4f2805199050),
[Base::ZipWriter::Stream()](../../d9/df3/classBase_1_1ZipWriter.html#a37330d3d5bff097e58268aa7853abaa4),
[App::BackupPolicy::TimeStamp](../../d1/d16/classApp_1_1BackupPolicy.html#a1cb10df777ed391db7bdd45dce3c7a4fae4df4fb24bdbb50c8a7f4d14bec5d5a2),
[App::BackupPolicy::useBackupExtension()](../../d1/d16/classApp_1_1BackupPolicy.html#ace4c48378a2d6062edd0b00b26459e0a),
and
[Base::ZipWriter::writeFiles()](../../d9/df3/classBase_1_1ZipWriter.html#a473a5caab984aaff00f0b6dba44b6b0a).

Referenced by
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
and
[saveCopy()](../../d8/d3e/classApp_1_1Document.html#acbad1e96391e2f6067dfdf23a9bdb044).

## ◆ setClosable()

void Document::setClosable  | ( | [bool](../../d9/db9/classbool.html) | _c_| ) |   
---|---|---|---|---|---  
  
set the document to be closable, this is on by default.

References
[Closable](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553affc4864219c40e54946a53110d9d3bc2),
and
[setStatus()](../../d8/d3e/classApp_1_1Document.html#af20528b5ddb713121f4907b23290b525).

## ◆ setMaxUndoStackSize()

void Document::setMaxUndoStackSize  | ( | unsigned [int](../../d1/da0/classint.html) | _UndoMaxStackSize_ = `20`| ) |   
---|---|---|---|---|---  
  
Set the Undo limit as stack size.

References
[App::DocumentP::UndoMaxStackSize](../../d1/da5/structApp_1_1DocumentP.html#a6dc4ef7a82a38c93bc6348125fbb26b7).

## ◆ setStatus()

void Document::setStatus  | ( | [Status](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553) | _pos_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _on_  
| ) | |   
  
set the status bits

References
[App::DocumentP::StatusBits](../../d1/da5/structApp_1_1DocumentP.html#a22382776a74a5bc0c130d1136d2ec7d2).

Referenced by
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[TechDraw::DrawDimHelper::makeExtentDim()](../../db/d5a/classTechDraw_1_1DrawDimHelper.html#a80cb2086c17599fd498ea2b4401c743c),
[readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[setClosable()](../../d8/d3e/classApp_1_1Document.html#a1c567b02a884388035b005a0d7479e9b).

## ◆ setTransactionMode()

void Document::setTransactionMode  | ( | [int](../../d1/da0/classint.html) | _iMode_| ) |   
---|---|---|---|---|---  
  
switch the transaction mode

References
[App::DocumentP::iTransactionMode](../../d1/da5/structApp_1_1DocumentP.html#a3ee50ce0db9761ddce2529bd0b56fad7).

## ◆ setUndoLimit()

void Document::setUndoLimit  | ( | unsigned [int](../../d1/da0/classint.html) | _UndoMemSize_ = `0`| ) |   
---|---|---|---|---|---  
  
Set the Undo limit in Byte!

References
[App::DocumentP::UndoMemSize](../../d1/da5/structApp_1_1DocumentP.html#a22dd5ded3943792598d2c96703a63a3c).

## ◆ setUndoMode()

void Document::setUndoMode  | ( | [int](../../d1/da0/classint.html) | _iMode_| ) |   
---|---|---|---|---|---  
  
switch the level of Undo/Redo

References
[clearUndos()](../../d8/d3e/classApp_1_1Document.html#a8d2601689201b1fa157851f048d17d55),
and
[App::DocumentP::iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8).

## ◆ testStatus()

[bool](../../d9/db9/classbool.html) Document::testStatus  | ( | [Status](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553) | _pos_| ) |  const  
---|---|---|---|---|---  
  
return the status bits

Referenced by
[addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
[addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02),
[addRecomputeObject()](../../d8/d3e/classApp_1_1Document.html#ae9cd6dab5c67b88e24bcfb54a15fc273),
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526),
[copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
[TechDraw::DrawViewDetail::execute()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad719019d86300aa960ac853a0b5068ce),
[TechDraw::DrawViewSection::execute()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ab7e657c18db14b4054c3d3434141ffae),
[App::OriginGroupExtension::extensionOnChanged()](../../da/d09/classApp_1_1OriginGroupExtension.html#a41efd2721ff0ffe392111260757a8c42),
[getFileName()](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d),
[TechDraw::DrawViewPart::getSourceShape()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aeb0d7bbe7418b86053f38713d4c91fa9),
[TechDraw::DrawViewPart::getSourceShapeFused()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a259e1a941c8e6a0651089bfa4111e3bd),
[getUniqueObjectName()](../../d8/d3e/classApp_1_1Document.html#a8bc7c3b871147cf18529b0a1e9f44ac9),
[isClosable()](../../d8/d3e/classApp_1_1Document.html#a5e0c6ac230060e945dc269b40bb86958),
[readObjects()](../../d8/d3e/classApp_1_1Document.html#ac4fdad7a7a9f248ceae6be9b9df8fb9d),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
and
[PartDesignGui::ViewProviderBody::updateOriginDatumSize()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a3c7c680a5e55c6cc695c82c8b45935c0).

## ◆ topologicalSort()

std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Document::topologicalSort  | ( | | ) |  const  
---|---|---|---|---  
  
get a list of topological sorted objects
(<https://en.wikipedia.org/wiki/Topological_sorting>)

References
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
and
[App::DocumentP::topologicalSort()](../../d1/da5/structApp_1_1DocumentP.html#a5a03a65c8fe65bb3dcabc29b448faf9a).

Referenced by
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b).

## ◆ undo()

[bool](../../d9/db9/classbool.html) Document::undo  | ( | [int](../../d1/da0/classint.html) | _id_ = `0`| ) |   
---|---|---|---|---|---  
  
Will UNDO one step, returns False if no undo was done (Undos == 0).

References
[App::DocumentP::activeUndoTransaction](../../d1/da5/structApp_1_1DocumentP.html#a2a03a1cf066d80b04eeb3517ec6a919b),
[App::Transaction::getID()](../../de/dbf/classApp_1_1Transaction.html#a883839e0722bbe62ec52d22bd176483a),
[App::DocumentP::iUndoMode](../../d1/da5/structApp_1_1DocumentP.html#a80d344e0394903a276cbd724adf881c8),
[App::Transaction::Name](../../de/dbf/classApp_1_1Transaction.html#a6245b49f541ec20247d3b46c18152f9a),
[App::DocumentP::objectArray](../../d1/da5/structApp_1_1DocumentP.html#a5aa11defdaf93157853e30d434272106),
[signalUndo](../../d8/d3e/classApp_1_1Document.html#a01b6644ff4f53f6d0a8fd101e0d57790),
[Transaction](../../d8/d3e/classApp_1_1Document.html#a49982aa325e19f0956d42fde9132caa2),
[undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078),
and
[App::DocumentP::undoing](../../d1/da5/structApp_1_1DocumentP.html#abdea8c0a4be118998737e4db163285d6).

Referenced by
[getTransactionID()](../../d8/d3e/classApp_1_1Document.html#a5225cf38810fc5cb88614651b7a7927c),
[undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078),
and
[Gui::Document::undo()](../../de/d4e/classGui_1_1Document.html#a47526ed6083330d1248b4a3553f5aa33).

## ◆ writeDependencyGraphViz()

void Document::writeDependencyGraphViz  | ( | std::ostream & | _out_| ) |   
---|---|---|---|---|---  
  
write GraphViz file

References
[App::DocumentP::objectMap](../../d1/da5/structApp_1_1DocumentP.html#a556f764e680af92dee9980c66ae2c886).

## ◆ writeObjects()

| void Document::writeObjects  | ( | const std::vector< [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > & | _obj_ ,   
---|---|---|---  
|  | [Base::Writer](../../dd/d4d/classBase_1_1Writer.html) & | _writer_  
| ) | |  const  
protected  
  
References
[Base::Writer::decInd()](../../dd/d4d/classBase_1_1Writer.html#a30341c9a398093609d564137a7bb9c92),
[Base::Persistence::encodeAttribute()](../../d9/d25/classBase_1_1Persistence.html#af652aa772949cdb36c2c087761f548ec),
[getErrorDescription()](../../d8/d3e/classApp_1_1Document.html#a48126d74c0d6bfcf4051bdbcf01840b7),
[Base::Writer::incInd()](../../dd/d4d/classBase_1_1Writer.html#a43d778c305e03fe9d6e6def57ce738f5),
[Base::Writer::ind()](../../dd/d4d/classBase_1_1Writer.html#aca6713f264f65b0a0dac0ac013ab3368),
[isExporting()](../../d8/d3e/classApp_1_1Document.html#a6d98568ff827987b0d4f734f0b0df135),
[App::DocumentObject::OutListNoHidden](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0ca631f928853757f32d5b431dc80297bd0),
[App::DocumentObject::OutListNoXLinked](../../d2/de4/classApp_1_1DocumentObject.html#a3d4ac9a1c924dd25e080aff91d416c0caffbf55a4a6fc04cd65fad55182961c0f),
and
[Base::Writer::Stream()](../../dd/d4d/classBase_1_1Writer.html#ab9783b74c5f923aff65ecefcc0910205).

Referenced by
[exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
and
[Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0).

## Friends And Related Function Documentation

## ◆ Application

| [friend](../../d7/d23/classfriend.html) class
[Application](../../da/dbf/classApp_1_1Application.html)  
---  
friend  
  
## ◆ DocumentObject

| [friend](../../d7/d23/classfriend.html) class
[DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)  
---  
friend  
  
The [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class
of all Classes handled in the Document.") that will own the expression.

## ◆ Transaction

| [friend](../../d7/d23/classfriend.html) class
[Transaction](../../de/dbf/classApp_1_1Transaction.html)  
---  
friend  
  
Referenced by
[redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003),
and
[undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ TransactionalObject

| [friend](../../d7/d23/classfriend.html) class
[TransactionalObject](../../d8/d00/classApp_1_1TransactionalObject.html)  
---  
friend  
  
because of transaction handling

## ◆ TransactionDocumentObject

| [friend](../../d7/d23/classfriend.html) class
[TransactionDocumentObject](../../d2/dd9/classApp_1_1TransactionDocumentObject.html)  
---  
friend  
  
## Member Data Documentation

## ◆ Comment

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::Comment  
---  
  
long comment or description (UTF8 with line breaks)

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ Company

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::Company  
---  
  
company name UTF8(optional)

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ CreatedBy

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::CreatedBy  
---  
  
creators name (utf-8)

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ CreationDate

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::CreationDate  
---  
  
Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ FileName

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::FileName  
---  
  
full qualified (with path) file name (utf-8 coded)

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[getFileName()](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
[isSaved()](../../d8/d3e/classApp_1_1Document.html#a730da4f4ddab904051e5f1a031577b27),
[App::Application::openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
[saveCopy()](../../d8/d3e/classApp_1_1Document.html#acbad1e96391e2f6067dfdf23a9bdb044),
and
[Import::ImportOCAF2::setMode()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a865601fce708b9141eb0bbf40b3e96f8).

## ◆ Id

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::Id  
---  
  
Id e.g. [Part](../../da/d8d/classApp_1_1Part.html "Base class of all geometric
document objects.") number.

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ Label

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::Label  
---  
  
holds the long name of the document (utf-8 coded)

Referenced by
[Gui::Document::canClose()](../../de/d4e/classGui_1_1Document.html#a9d5a988c5980ecdafede499fa261d135),
[Gui::Document::createView()](../../de/d4e/classGui_1_1Document.html#a1235bbc0ddca0b8c9465d9d491d79541),
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[PartGui::DlgExtrusion::findShapes()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8976c72de1970766d8d2dc5391e34903),
[onBeforeChange()](../../d8/d3e/classApp_1_1Document.html#a84bc36d18a86fca95c88aa31308f0bf3),
[onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[Gui::MDIView::onRelabel()](../../df/d23/classGui_1_1MDIView.html#afcbfda847bb899e50b614fe491b76cf9),
[DrawingGui::DrawingView::onRelabel()](../../da/d65/classDrawingGui_1_1DrawingView.html#aa6defb7630d57ca8d919679b10ea424e),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee),
[Gui::DocumentItem::setData()](../../df/d15/classGui_1_1DocumentItem.html#a5326e93665664b6b41b5bbf1b3389cb6),
and
[App::RelabelDocumentExpressionVisitor::visit()](../../db/dfd/classApp_1_1RelabelDocumentExpressionVisitor.html#aa37c20588af574df4ceaa95468660f18).

## ◆ LastModifiedBy

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::LastModifiedBy  
---  
  
user last modified the document

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
and
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c).

## ◆ LastModifiedDate

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::LastModifiedDate  
---  
  
Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
and
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c).

## ◆ License

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::License  
---  
  
License string Holds the short license string for the Item, e.g.

CC-BY for the Creative Commons license suit.

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ LicenseURL

[App::PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::LicenseURL  
---  
  
License description/contract URL.

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ Material

[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html)
App::Document::Material  
---  
  
[Material](../../da/d47/classApp_1_1Material.html "Material class.")
descriptions, used and defined in the
[Material](../../da/d47/classApp_1_1Material.html "Material class.") module.

## ◆ Meta

[App::PropertyMap](../../db/d3f/classApp_1_1PropertyMap.html)
App::Document::Meta  
---  
  
[Meta](../../d9/dcf/namespaceApp_1_1Meta.html) descriptions.

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b).

## ◆ ShowHidden

[PropertyBool](../../dc/d81/classApp_1_1PropertyBool.html)
App::Document::ShowHidden  
---  
  
Whether to show hidden items in TreeView.

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[Gui::DocumentItem::setShowHidden()](../../df/d15/classGui_1_1DocumentItem.html#aabbf058f0836116ff32d800cf6c3244c),
and
[Gui::DocumentItem::showHidden()](../../df/d15/classGui_1_1DocumentItem.html#ab08d3106925612e8b9830623f2dc4864).

## ◆ signalAbortTransaction

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Document::signalAbortTransaction  
---  
  
## ◆ signalActivatedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalActivatedObject  
---  
  
signal on activated Object

Referenced by
[addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
and
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalBeforeChange

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Document::signalBeforeChange  
---  
  
signal before changing an doc property

Referenced by
[onBeforeChange()](../../d8/d3e/classApp_1_1Document.html#a84bc36d18a86fca95c88aa31308f0bf3).

## ◆ signalBeforeChangeObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Document::signalBeforeChangeObject  
---  
  
signal before changing an Object

Referenced by
[onBeforeChangeProperty()](../../d8/d3e/classApp_1_1Document.html#a92ee224a3cd40ef4da74e81d732c8fcb).

## ◆ signalBeforeRecompute

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Document::signalBeforeRecompute  
---  
  
Referenced by
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b).

## ◆ signalChanged

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Document::signalChanged  
---  
  
signal on changed doc property

Referenced by
[onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a).

## ◆ signalChangedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Document::signalChangedObject  
---  
  
signal on changed Object

Referenced by
[PartDesignGui::ViewProviderBody::attach()](../../dc/d5e/classPartDesignGui_1_1ViewProviderBody.html#a12e5a7b4da5cecd7fe82062ad9051176),
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[Gui::ViewProviderOriginGroupExtension::extensionAttach()](../../d6/dd1/classGui_1_1ViewProviderOriginGroupExtension.html#ae4e983b8437ebedcf3d8b82b3c4997ae),
[onChangedProperty()](../../d8/d3e/classApp_1_1Document.html#aae4b353b22eaa76b58776756206af552),
and
[FemGui::FunctionWidget::setViewProvider()](../../dc/d25/classFemGui_1_1FunctionWidget.html#a0083237a39c65525f04f5124c07ae2d6).

## ◆ signalChangePropertyEditor

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&,const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Document::signalChangePropertyEditor  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[Gui::ViewProviderDocumentObject::onPropertyStatusChanged()](../../d0/d48/classGui_1_1ViewProviderDocumentObject.html#aa158bb0312285eb7672f123e8a1359de).

## ◆ signalCommitTransaction

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Document::signalCommitTransaction  
---  
  
## ◆ signalDeletedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalDeletedObject  
---  
  
signal on deleted Object

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[TechDrawGui::MDIViewPage::MDIViewPage()](../../dd/d51/classTechDrawGui_1_1MDIViewPage.html#a5bfb8fa1e3810804cd8c7607f97a996b),
and
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ signalExportObjects

boost::signals2::signal<void (const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&,
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &)>
App::Document::signalExportObjects  
---  
  
Referenced by
[exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739).

## ◆ signalExportViewObjects

boost::signals2::signal<void (const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&,
[Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &)>
App::Document::signalExportViewObjects  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[App::MergeDocuments::SaveDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a7d869417fe3e849c3f9823172f55a02b).

## ◆ signalFinishImportObjects

boost::signals2::signal<void (const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&)>
App::Document::signalFinishImportObjects  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff).

## ◆ signalFinishRestoreObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalFinishRestoreObject  
---  
  
Referenced by
[afterRestore()](../../d8/d3e/classApp_1_1Document.html#a40aaba167afb4553a897ef687bb59526),
and
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalFinishSave

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const std::string&)>
App::Document::signalFinishSave  
---  
  
Referenced by
[saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ signalImportObjects

boost::signals2::signal<void (const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&,
[Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)&)>
App::Document::signalImportObjects  
---  
  
Referenced by
[importObjects()](../../d8/d3e/classApp_1_1Document.html#a485f13a74fdfa525109f7df11b7447ff).

## ◆ signalImportViewObjects

boost::signals2::signal<void (const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&,
[Base::Reader](../../d1/d1f/classBase_1_1Reader.html)&, const
std::map<std::string, std::string>&)> App::Document::signalImportViewObjects  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[App::MergeDocuments::RestoreDocFile()](../../d6/d0c/classApp_1_1MergeDocuments.html#a25d131d0fd066b21808a98c1d0830967).

## ◆ signalLinkXsetValue

boost::signals2::signal<void (std::string)> App::Document::signalLinkXsetValue  
---  
  
## ◆ signalNewObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalNewObject  
---  
  
signal on new Object

Referenced by
[addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
and
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalOpenTransaction

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, std::string)>
App::Document::signalOpenTransaction  
---  
  
## ◆ signalRecomputed

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&)>
App::Document::signalRecomputed  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[Gui::GraphvizView::GraphvizView()](../../dd/d86/classGui_1_1GraphvizView.html#a1e46d2a16a77346e54d76e9b8db662f7),
and
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b).

## ◆ signalRecomputedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalRecomputedObject  
---  
  
Referenced by
[PartDesign::SubShapeBinder::onChanged()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a525834748579d35e2e8ecbf9cd18bf3d),
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
and
[recomputeFeature()](../../d8/d3e/classApp_1_1Document.html#ab684fd8bc8a07f3c18a88e28fb86264a).

## ◆ signalRedo

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Document::signalRedo  
---  
  
signal on redo

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[Gui::GraphvizView::GraphvizView()](../../dd/d86/classGui_1_1GraphvizView.html#a1e46d2a16a77346e54d76e9b8db662f7),
and
[redo()](../../d8/d3e/classApp_1_1Document.html#ad08b3d0b0c6dc9078fac0ae381a90003).

## ◆ signalRelabelObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalRelabelObject  
---  
  
signal on relabeled Object

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalRestoreDocument

boost::signals2::signal<void
([Base::XMLReader](../../dc/d95/classBase_1_1XMLReader.html)&)>
App::Document::signalRestoreDocument  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ signalSaveDocument

boost::signals2::signal<void
([Base::Writer](../../dd/d4d/classBase_1_1Writer.html) &)>
App::Document::signalSaveDocument  
---  
  
signal on load/save document this signal is given when the document gets
streamed.

you can use this hook to write additional information in the file (like the
[Gui::Document](../../de/d4e/classGui_1_1Document.html "The Gui Document This
is the document on GUI level.") does).

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
and
[saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ signalSkipRecompute

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
std::vector<[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*>&)>
App::Document::signalSkipRecompute  
---  
  
Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b).

## ◆ signalStartSave

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const std::string&)>
App::Document::signalStartSave  
---  
  
Referenced by
[saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ signalTouchedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Document::signalTouchedObject  
---  
  
signal on manually called
[DocumentObject::touch()](../../d2/de4/classApp_1_1DocumentObject.html#a8949e65adb1315e37818719a058f4f40
"Set the property touched -> changed, cause recomputation in Update\(\)")

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalTransactionAppend

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&,
[Transaction](../../de/dbf/classApp_1_1Transaction.html)*)>
App::Document::signalTransactionAppend  
---  
  
signal on created object

Referenced by
[addObject()](../../d8/d3e/classApp_1_1Document.html#a69093ef0f34149c5cedb0838a845d771),
[addObjects()](../../d8/d3e/classApp_1_1Document.html#aa2e0734dcb6c3edffab184bb41de6fd4),
and
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalTransactionRemove

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&,
[Transaction](../../de/dbf/classApp_1_1Transaction.html)*)>
App::Document::signalTransactionRemove  
---  
  
signal on removed object

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33).

## ◆ signalUndo

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Document::signalUndo  
---  
  
signal on undo

Referenced by
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[Gui::GraphvizView::GraphvizView()](../../dd/d86/classGui_1_1GraphvizView.html#a1e46d2a16a77346e54d76e9b8db662f7),
and
[undo()](../../d8/d3e/classApp_1_1Document.html#ad52b1f7a49050202b18f081a61a42078).

## ◆ Tip

[PropertyLink](../../d4/d77/classApp_1_1PropertyLink.html) App::Document::Tip  
---  
  
Tip object of the document (if any)

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
and
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c).

## ◆ TipName

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::TipName  
---  
  
Tip object of the document (if any)

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[removeObject()](../../d8/d3e/classApp_1_1Document.html#a2a0d41a83aea02e5b45c9cab6b5a1b33),
[Restore()](../../d8/d3e/classApp_1_1Document.html#ae73cc157823eb7c79027fa778f6d6c82),
and
[save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c).

## ◆ TransientDir

[PropertyString](../../dd/df8/classApp_1_1PropertyString.html)
App::Document::TransientDir  
---  
  
read-only name of the temp dir created when the document is opened

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[getFileName()](../../d8/d3e/classApp_1_1Document.html#a6710d0e8dbf515ba6f04a0f6be31c21d),
[onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
[App::VRMLObject::RestoreDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a90cb824c6253de535ec16e1935455599),
[Sandbox::DocumentSaverThread::run()](../../d9/d1c/classSandbox_1_1DocumentSaverThread.html#a4eda162d7f2ad445c7e4ef89b8071ed6),
[App::VRMLObject::SaveDocFile()](../../df/df6/classApp_1_1VRMLObject.html#a5dc3cc5b304d0866d30a0ad975cc4ccd),
[Gui::AutoSaver::slotCreateDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#ac494a904b86d92d32163dab8049b0d80),
and
[~Document()](../../d8/d3e/classApp_1_1Document.html#ac2e3f62307dc22baac21ddc10fa1609c).

## ◆ Uid

[PropertyUUID](../../d2/d6c/classApp_1_1PropertyUUID.html) App::Document::Uid  
---  
  
unique identifier of the document

Referenced by
[Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
and
[saveAs()](../../d8/d3e/classApp_1_1Document.html#a99cf956cb95ce19b87c4ea7e1d5087ee).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Document.h
  * FreeCAD/src/App/Document.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

