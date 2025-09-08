---
url: https://freecad.github.io/SourceDoc/da/dbf/classApp_1_1Application.html
scraped_at: 2025-09-08T14:53:29.449308
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Application](../../da/dbf/classApp_1_1Application.html)

[List of all members](../../d6/d1c/classApp_1_1Application-members.html) | Classes

App::Application Class Reference

The [Application](../../da/dbf/classApp_1_1Application.html "The Application
The root of the whole application.") The root of the whole application.
[More...](../../da/dbf/classApp_1_1Application.html#details)

`#include <Application.h>`

##  Classes  
  
---  
class | [TransactionSignaller](../../dc/d13/classApp_1_1Application_1_1TransactionSignaller.html)  
| Helper class for [App::Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") to signal on close/abort transaction.
[More...](../../dc/d13/classApp_1_1Application_1_1TransactionSignaller.html#details)  
  
  
##  Public Member Functions  
  
---  
Application-wide trandaction setting  
[int](../../d1/da0/classint.html) | [setActiveTransaction](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff) (const char *name, [bool](../../d9/db9/classbool.html) persist=false)  
| Setup a pending application-wide active transaction.
[More...](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff)  
  
const char * | [getActiveTransaction](../../da/dbf/classApp_1_1Application.html#a320164bff61415b44f26af228fe99c6a) ([int](../../d1/da0/classint.html) *tid=nullptr) const  
| Return the current active transaction name and ID.
[More...](../../da/dbf/classApp_1_1Application.html#a320164bff61415b44f26af228fe99c6a)  
  
void | [closeActiveTransaction](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9) ([bool](../../d9/db9/classbool.html) abort=false, [int](../../d1/da0/classint.html) id=0)  
| Commit/abort current active transactions.
[More...](../../da/dbf/classApp_1_1Application.html#a65f9fb03ff7053cfb14dd230451ae0a9)  
  
methods for parameter handling  
[ParameterManager](../../db/daa/classParameterManager.html) & | [GetSystemParameter](../../da/dbf/classApp_1_1Application.html#add1090b4bede57bd4bd2dbf93825ff52) (void)  
| returns the system parameter
[More...](../../da/dbf/classApp_1_1Application.html#add1090b4bede57bd4bd2dbf93825ff52)  
  
[ParameterManager](../../db/daa/classParameterManager.html) & | [GetUserParameter](../../da/dbf/classApp_1_1Application.html#adb4f3ab9508bc0a64c2dbed546348c47) (void)  
| returns the user parameter
[More...](../../da/dbf/classApp_1_1Application.html#adb4f3ab9508bc0a64c2dbed546348c47)  
  
[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< [ParameterGrp](../../d4/d97/classParameterGrp.html) > | [GetParameterGroupByPath](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202) (const char *sName)  
| Gets a parameter group by a full qualified path It's an easy method to get a
group:
[More...](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202)  
  
[ParameterManager](../../db/daa/classParameterManager.html) * | [GetParameterSet](../../da/dbf/classApp_1_1Application.html#ac26e42f0b94ddec92b092a5176605e20) (const char *sName) const  
const std::map< std::string, [ParameterManager](../../db/daa/classParameterManager.html) * > & | [GetParameterSetList](../../da/dbf/classApp_1_1Application.html#ad4b8562aba1741a699837ad7082932d0) (void) const  
void | [AddParameterSet](../../da/dbf/classApp_1_1Application.html#aa13715c726bd363dbdb160b11459cfe4) (const char *sName)  
void | [RemoveParameterSet](../../da/dbf/classApp_1_1Application.html#aea22efe6d93557ac1cfca6c3433a0062) (const char *sName)  
methods for the open handler  
With this facility an [Application](../../da/dbf/classApp_1_1Application.html
"The Application The root of the whole application.") module can register an
ending (filetype) which it can handle to open. The ending and the module name
are stored and if the file type is opened the module gets loaded and needs to
register an OpenHandler class in the OpenHandlerFactorySingleton. After the
module is loaded, an OpenHandler of this type is created and the file gets
loaded.

See also

    OpenHandler 
     OpenHandlerFactorySingleton   
void | [addImportType](../../da/dbf/classApp_1_1Application.html#a86d839fa4b89602b727a18868a3a4356) (const char *[Type](../../dc/dee/classBase_1_1Type.html), const char *ModuleName)  
| Register an import filetype and a module name.
[More...](../../da/dbf/classApp_1_1Application.html#a86d839fa4b89602b727a18868a3a4356)  
  
void | [changeImportModule](../../da/dbf/classApp_1_1Application.html#a5eb43dd65a2cbf389d0b7300d1aba3fc) (const char *[Type](../../dc/dee/classBase_1_1Type.html), const char *OldModuleName, const char *NewModuleName)  
| Change the module name of a registered filetype.
[More...](../../da/dbf/classApp_1_1Application.html#a5eb43dd65a2cbf389d0b7300d1aba3fc)  
  
std::vector< std::string > | [getImportModules](../../da/dbf/classApp_1_1Application.html#a42a251c438c21d843c37eb417011ec65) (const char *[Type](../../dc/dee/classBase_1_1Type.html)) const  
| Return a list of modules that support the given filetype.
[More...](../../da/dbf/classApp_1_1Application.html#a42a251c438c21d843c37eb417011ec65)  
  
std::vector< std::string > | [getImportModules](../../da/dbf/classApp_1_1Application.html#aaad82f9d29c494521b8ad3dc4f3daaf8) () const  
| Return a list of all modules.
[More...](../../da/dbf/classApp_1_1Application.html#aaad82f9d29c494521b8ad3dc4f3daaf8)  
  
std::vector< std::string > | [getImportTypes](../../da/dbf/classApp_1_1Application.html#a08a0fd7c23b64e7964c6bea91a301f44) (const char *Module) const  
| Return a list of filetypes that are supported by a module.
[More...](../../da/dbf/classApp_1_1Application.html#a08a0fd7c23b64e7964c6bea91a301f44)  
  
std::vector< std::string > | [getImportTypes](../../da/dbf/classApp_1_1Application.html#aeb265694f9a224e97f57fdbf2093686a) (void) const  
| Return a list of all filetypes.
[More...](../../da/dbf/classApp_1_1Application.html#aeb265694f9a224e97f57fdbf2093686a)  
  
std::map< std::string, std::string > | [getImportFilters](../../da/dbf/classApp_1_1Application.html#a4ccdb78313a9c9af1a3f2fe088b7c4dd) (const char *[Type](../../dc/dee/classBase_1_1Type.html)) const  
| Return the import filters with modules of a given filetype.
[More...](../../da/dbf/classApp_1_1Application.html#a4ccdb78313a9c9af1a3f2fe088b7c4dd)  
  
std::map< std::string, std::string > | [getImportFilters](../../da/dbf/classApp_1_1Application.html#ad4bc5df5f98d3cec09f3a9ec672f3a75) (void) const  
| Return a list of all import filters.
[More...](../../da/dbf/classApp_1_1Application.html#ad4bc5df5f98d3cec09f3a9ec672f3a75)  
  
void | [addExportType](../../da/dbf/classApp_1_1Application.html#abf69fc8463ed5bc98a17b445e5ad7def) (const char *[Type](../../dc/dee/classBase_1_1Type.html), const char *ModuleName)  
| Register an export filetype and a module name.
[More...](../../da/dbf/classApp_1_1Application.html#abf69fc8463ed5bc98a17b445e5ad7def)  
  
void | [changeExportModule](../../da/dbf/classApp_1_1Application.html#a8f0d27130f852de8fc0c0a24a8290eb3) (const char *[Type](../../dc/dee/classBase_1_1Type.html), const char *OldModuleName, const char *NewModuleName)  
| Change the module name of a registered filetype.
[More...](../../da/dbf/classApp_1_1Application.html#a8f0d27130f852de8fc0c0a24a8290eb3)  
  
std::vector< std::string > | [getExportModules](../../da/dbf/classApp_1_1Application.html#ad2f5f9df9afe7f48a06c8d8c76070dad) (const char *[Type](../../dc/dee/classBase_1_1Type.html)) const  
| Return a list of modules that support the given filetype.
[More...](../../da/dbf/classApp_1_1Application.html#ad2f5f9df9afe7f48a06c8d8c76070dad)  
  
std::vector< std::string > | [getExportModules](../../da/dbf/classApp_1_1Application.html#af0591aa70e8706e23b6547dcb973b427) () const  
| Return a list of all modules.
[More...](../../da/dbf/classApp_1_1Application.html#af0591aa70e8706e23b6547dcb973b427)  
  
std::vector< std::string > | [getExportTypes](../../da/dbf/classApp_1_1Application.html#a7273ff797509b2b75730d88fce11a1d2) (const char *Module) const  
| Return a list of filetypes that are supported by a module.
[More...](../../da/dbf/classApp_1_1Application.html#a7273ff797509b2b75730d88fce11a1d2)  
  
std::vector< std::string > | [getExportTypes](../../da/dbf/classApp_1_1Application.html#a4b5b68bad78fc71221d836b909d8a8cf) (void) const  
| Return a list of all filetypes.
[More...](../../da/dbf/classApp_1_1Application.html#a4b5b68bad78fc71221d836b909d8a8cf)  
  
std::map< std::string, std::string > | [getExportFilters](../../da/dbf/classApp_1_1Application.html#a876f0ef59d39eaed17f22db53be42dc5) (const char *[Type](../../dc/dee/classBase_1_1Type.html)) const  
| Return the export filters with modules of a given filetype.
[More...](../../da/dbf/classApp_1_1Application.html#a876f0ef59d39eaed17f22db53be42dc5)  
  
std::map< std::string, std::string > | [getExportFilters](../../da/dbf/classApp_1_1Application.html#a5356e37a28740a0333fc86ade889b1f7) (void) const  
| Return a list of all export filters.
[More...](../../da/dbf/classApp_1_1Application.html#a5356e37a28740a0333fc86ade889b1f7)  
  
  
##  Static Public Member Functions  
  
---  
Application directories  
static std::string | [getHomePath](../../da/dbf/classApp_1_1Application.html#a541c26818151bcacd2cf16d29cb79c4e) ()  
static std::string | [getExecutableName](../../da/dbf/classApp_1_1Application.html#aa4e204b1a63dd706b0132e4532360cdc) ()  
static std::string | [getTempPath](../../da/dbf/classApp_1_1Application.html#a9d6fde1f997eed46a97428e42f655507) ()  
static std::string | [getTempFileName](../../da/dbf/classApp_1_1Application.html#a6550097c7ee9c3857f8190954acfbf48) (const char *FileName=nullptr)  
static std::string | [getUserCachePath](../../da/dbf/classApp_1_1Application.html#a902b031dddf45438919f61a5e8075b7f) ()  
static std::string | [getUserConfigPath](../../da/dbf/classApp_1_1Application.html#a8165f3d8d4be4a4100dcb09ef03571c9) ()  
static std::string | [getUserAppDataDir](../../da/dbf/classApp_1_1Application.html#a664e31c0ded7d88e2d70b7a301bb5bd4) ()  
static std::string | [getUserMacroDir](../../da/dbf/classApp_1_1Application.html#a4077a93dc9d5769cb2a0e7dbdd706a6c) ()  
static std::string | [getResourceDir](../../da/dbf/classApp_1_1Application.html#ae37d02f54b32fd354921d5312c753b7f) ()  
static std::string | [getLibraryDir](../../da/dbf/classApp_1_1Application.html#ac58ac6702c9bec7b933d4b9f6b79261f) ()  
static std::string | [getHelpDir](../../da/dbf/classApp_1_1Application.html#ac74c4e4304c59621348a11d4ccfddd1e) ()  
  
##  Public Attributes  
  
---  
Signals of the Application  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &, [bool](../../d9/db9/classbool.html))> | [signalNewDocument](../../da/dbf/classApp_1_1Application.html#a49425118433ce84229402407d5631ea4)  
| signal on new [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")
[More...](../../da/dbf/classApp_1_1Application.html#a49425118433ce84229402407d5631ea4)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalDeleteDocument](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47)  
| signal on document getting deleted
[More...](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47)  
  
boost::signals2::signal< void()> | [signalDeletedDocument](../../da/dbf/classApp_1_1Application.html#aef84fb43739719380174bb3ea016cbc3)  
| signal on already deleted [Document](../../d8/d3e/classApp_1_1Document.html
"The document class.")
[More...](../../da/dbf/classApp_1_1Application.html#aef84fb43739719380174bb3ea016cbc3)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalRelabelDocument](../../da/dbf/classApp_1_1Application.html#a18013255316c0f5798925e87fc145f6f)  
| signal on relabeling [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") (user name)
[More...](../../da/dbf/classApp_1_1Application.html#a18013255316c0f5798925e87fc145f6f)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalRenameDocument](../../da/dbf/classApp_1_1Application.html#abe4f8ab20f19201d26ca7307bc719614)  
| signal on renaming [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") (internal name)
[More...](../../da/dbf/classApp_1_1Application.html#abe4f8ab20f19201d26ca7307bc719614)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalActiveDocument](../../da/dbf/classApp_1_1Application.html#ad9cf4f57c0d4fda56d79ec91936efa39)  
| signal on activating [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")
[More...](../../da/dbf/classApp_1_1Application.html#ad9cf4f57c0d4fda56d79ec91936efa39)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalSaveDocument](../../da/dbf/classApp_1_1Application.html#afbe487d60d38532c8802d9228d5e5a0b)  
| signal on saving [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")
[More...](../../da/dbf/classApp_1_1Application.html#afbe487d60d38532c8802d9228d5e5a0b)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalStartRestoreDocument](../../da/dbf/classApp_1_1Application.html#a79b377bd369df1b15b2ae2b9181f7f75)  
| signal on starting to restore
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.")
[More...](../../da/dbf/classApp_1_1Application.html#a79b377bd369df1b15b2ae2b9181f7f75)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalFinishRestoreDocument](../../da/dbf/classApp_1_1Application.html#ac7b262994ef3ae8766bd3c7590185046)  
| signal on restoring [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")
[More...](../../da/dbf/classApp_1_1Application.html#ac7b262994ef3ae8766bd3c7590185046)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalPendingReloadDocument](../../da/dbf/classApp_1_1Application.html#a76ca7e016087a4114ed1779b2eaf0913)  
| signal on pending reloading of a partial
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.")
[More...](../../da/dbf/classApp_1_1Application.html#a76ca7e016087a4114ed1779b2eaf0913)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &, const std::string &)> | [signalStartSaveDocument](../../da/dbf/classApp_1_1Application.html#aa14789336dc85be7a56eaad3d073ebe9)  
| signal on starting to save [Document](../../d8/d3e/classApp_1_1Document.html
"The document class.")
[More...](../../da/dbf/classApp_1_1Application.html#aa14789336dc85be7a56eaad3d073ebe9)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &, const std::string &)> | [signalFinishSaveDocument](../../da/dbf/classApp_1_1Application.html#af928fa8c38791c140768aef047422a24)  
| signal on saved [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")
[More...](../../da/dbf/classApp_1_1Application.html#af928fa8c38791c140768aef047422a24)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalUndoDocument](../../da/dbf/classApp_1_1Application.html#a08b81cccde7cb8e4310499eef2a397de)  
| signal on undo in document
[More...](../../da/dbf/classApp_1_1Application.html#a08b81cccde7cb8e4310499eef2a397de)  
  
boost::signals2::signal< void()> | [signalUndo](../../da/dbf/classApp_1_1Application.html#af2a1bcc8264629db57aae3d2a3823fc1)  
| signal on application wide undo
[More...](../../da/dbf/classApp_1_1Application.html#af2a1bcc8264629db57aae3d2a3823fc1)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalRedoDocument](../../da/dbf/classApp_1_1Application.html#a63e3d1fd313c1be4e30c630d77120fa1)  
| signal on redo in document
[More...](../../da/dbf/classApp_1_1Application.html#a63e3d1fd313c1be4e30c630d77120fa1)  
  
boost::signals2::signal< void()> | [signalRedo](../../da/dbf/classApp_1_1Application.html#a68d7cb47380fc0a05e913d47eebda2bc)  
| signal on application wide redo
[More...](../../da/dbf/classApp_1_1Application.html#a68d7cb47380fc0a05e913d47eebda2bc)  
  
boost::signals2::signal< void([bool](../../d9/db9/classbool.html))> | [signalBeforeCloseTransaction](../../da/dbf/classApp_1_1Application.html#aec3b5b983aa9b5ef97a4558174656ad3)  
| signal before close/abort active transaction
[More...](../../da/dbf/classApp_1_1Application.html#aec3b5b983aa9b5ef97a4558174656ad3)  
  
boost::signals2::signal< void([bool](../../d9/db9/classbool.html))> | [signalCloseTransaction](../../da/dbf/classApp_1_1Application.html#a3ba1061bc88929931d0f8c4c09c8b717)  
| signal after close/abort active transaction
[More...](../../da/dbf/classApp_1_1Application.html#a3ba1061bc88929931d0f8c4c09c8b717)  
  
boost::signals2::signal< void(const [Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalShowHidden](../../da/dbf/classApp_1_1Application.html#a5c4a9d78e70440dbcde1a8ec275aae51)  
| signal on show hidden items
[More...](../../da/dbf/classApp_1_1Application.html#a5c4a9d78e70440dbcde1a8ec275aae51)  
  
boost::signals2::signal< void()> | [signalStartOpenDocument](../../da/dbf/classApp_1_1Application.html#a6bdfe9471899866c70a4556ec86cea6d)  
| signal on start opening document(s)
[More...](../../da/dbf/classApp_1_1Application.html#a6bdfe9471899866c70a4556ec86cea6d)  
  
boost::signals2::signal< void()> | [signalFinishOpenDocument](../../da/dbf/classApp_1_1Application.html#ad77e22504068699d121e7c51b10d72bb)  
| signal on finished opening document(s)
[More...](../../da/dbf/classApp_1_1Application.html#ad77e22504068699d121e7c51b10d72bb)  
  
Signals of the document  
This signals are an aggregation of all document. If you only the signal of a
special document connect to the document itself  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalBeforeChangeDocument](../../da/dbf/classApp_1_1Application.html#a0a74f8e0386bb7e164cc4e6c653822a9)  
| signal before change of doc property
[More...](../../da/dbf/classApp_1_1Application.html#a0a74f8e0386bb7e164cc4e6c653822a9)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChangedDocument](../../da/dbf/classApp_1_1Application.html#a85edc6708be468366ba00b701ef60adf)  
| signal on changed doc property
[More...](../../da/dbf/classApp_1_1Application.html#a85edc6708be468366ba00b701ef60adf)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalNewObject](../../da/dbf/classApp_1_1Application.html#a2be45dffee80c84ad63eb0e87cea6bec)  
| signal on new Object
[More...](../../da/dbf/classApp_1_1Application.html#a2be45dffee80c84ad63eb0e87cea6bec)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalDeletedObject](../../da/dbf/classApp_1_1Application.html#affb0434ff9fe9ed3542f6724d5c37491)  
| signal on deleted Object
[More...](../../da/dbf/classApp_1_1Application.html#affb0434ff9fe9ed3542f6724d5c37491)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalBeforeChangeObject](../../da/dbf/classApp_1_1Application.html#a754143d4cbf1aefe30920a12ee268d35)  
| signal on changed Object
[More...](../../da/dbf/classApp_1_1Application.html#a754143d4cbf1aefe30920a12ee268d35)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChangedObject](../../da/dbf/classApp_1_1Application.html#af3ea93d79c3c2496701f3ed583efbc10)  
| signal on changed Object
[More...](../../da/dbf/classApp_1_1Application.html#af3ea93d79c3c2496701f3ed583efbc10)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalRelabelObject](../../da/dbf/classApp_1_1Application.html#ae23606015f7036a4348df58c389ca66b)  
| signal on relabeled Object
[More...](../../da/dbf/classApp_1_1Application.html#ae23606015f7036a4348df58c389ca66b)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalActivatedObject](../../da/dbf/classApp_1_1Application.html#a7193d997f6d54f1369d17540f515a61c)  
| signal on activated Object
[More...](../../da/dbf/classApp_1_1Application.html#a7193d997f6d54f1369d17540f515a61c)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalBeforeRecomputeDocument](../../da/dbf/classApp_1_1Application.html#a9bfbc2bd635c57b114636bc16ead33f2)  
| signal before recomputed document
[More...](../../da/dbf/classApp_1_1Application.html#a9bfbc2bd635c57b114636bc16ead33f2)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalRecomputed](../../da/dbf/classApp_1_1Application.html#a70ddba55bf1fe563e216fc4453bbb8c4)  
| signal on recomputed document
[More...](../../da/dbf/classApp_1_1Application.html#a70ddba55bf1fe563e216fc4453bbb8c4)  
  
boost::signals2::signal< void(const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)> | [signalObjectRecomputed](../../da/dbf/classApp_1_1Application.html#a927030e1bc1089d482c68db63ea0e449)  
| signal on recomputed document object
[More...](../../da/dbf/classApp_1_1Application.html#a927030e1bc1089d482c68db63ea0e449)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, std::string)> | [signalOpenTransaction](../../da/dbf/classApp_1_1Application.html#a1fd7640f51ddc743d89e531324cdc4ec)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalCommitTransaction](../../da/dbf/classApp_1_1Application.html#a06ca57127575a3cbec2e6ed6d9346c17)  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)> | [signalAbortTransaction](../../da/dbf/classApp_1_1Application.html#a9262371d6632485a417c96036fd31831)  
Signals of property changes  
These signals are emitted on property additions or removal. The changed object
can be any sub-class of
[PropertyContainer](../../d5/d48/classApp_1_1PropertyContainer.html "Base
class of all classes with properties.").  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalAppendDynamicProperty](../../da/dbf/classApp_1_1Application.html#a38e4cf45b905fcaafc05d550ddb83fd9)  
| signal on adding a dynamic property
[More...](../../da/dbf/classApp_1_1Application.html#a38e4cf45b905fcaafc05d550ddb83fd9)  
  
boost::signals2::signal< void(const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalRemoveDynamicProperty](../../da/dbf/classApp_1_1Application.html#a7b56714fdb016b0b5fde4f03f77cbce0)  
| signal on about removing a dynamic property
[More...](../../da/dbf/classApp_1_1Application.html#a7b56714fdb016b0b5fde4f03f77cbce0)  
  
boost::signals2::signal< void(const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)> | [signalChangePropertyEditor](../../da/dbf/classApp_1_1Application.html#a118f31ab2a23e562862614a5de003803)  
| signal on about changing the editor mode of a property
[More...](../../da/dbf/classApp_1_1Application.html#a118f31ab2a23e562862614a5de003803)  
  
Signals of extension changes  
These signals are emitted on dynamic extension addition. Dynamic extensions
are the ones added by python (c++ ones are part of the class definition, hence
not dynamic) The extension in question is provided as parameter.  
boost::signals2::signal< void(const [App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) &, std::string extension)> | [signalBeforeAddingDynamicExtension](../../da/dbf/classApp_1_1Application.html#ae06d582b0bfb1e375c2365adf010eb2e)  
| signal before adding the extension
[More...](../../da/dbf/classApp_1_1Application.html#ae06d582b0bfb1e375c2365adf010eb2e)  
  
boost::signals2::signal< void(const [App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html) &, std::string extension)> | [signalAddedDynamicExtension](../../da/dbf/classApp_1_1Application.html#a883dd5fbe8d2daf0f34beee76baf8724)  
| signal after the extension was added
[More...](../../da/dbf/classApp_1_1Application.html#a883dd5fbe8d2daf0f34beee76baf8724)  
  
  
## methods for document handling  
  
---  
enum class | [PathMatchMode](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64) { [MatchAbsolute](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a36428e3269d38765c18772524848e118) = 0 , [MatchCanonical](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a14cdc18650f96f3d8305d33e09b1d961) = 1 , [MatchCanonicalWarning](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a598e2b0f31835f6560f3f4c1b302668c) = 2 }  
| [Path](../../da/d2a/classApp_1_1Path.html "Base class of all geometric
document objects.") matching mode for
[getDocumentByPath()](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0
"Retrieve a document based on file path.")
[More...](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [newDocument](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b) (const char *Name=nullptr, const char *UserName=nullptr, [bool](../../d9/db9/classbool.html) createView=true, [bool](../../d9/db9/classbool.html) tempDoc=false)  
| Creates a new document The first name is a the identifier and some kind of
an internal (english) name.
[More...](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b)  
  
[bool](../../d9/db9/classbool.html) | [closeDocument](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244) (const char *name)  
| Closes the document _name_ and removes it from the application.
[More...](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244)  
  
std::string | [getUniqueDocumentName](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030) (const char *Name, [bool](../../d9/db9/classbool.html) tempDoc=false) const  
| find a unique document name
[More...](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [openDocument](../../da/dbf/classApp_1_1Application.html#a4ad1dd5f7c7ea3e47e6ccee518ca437c) (const char *FileName=nullptr, [bool](../../d9/db9/classbool.html) createView=true)  
| Open an existing document from a file.
[More...](../../da/dbf/classApp_1_1Application.html#a4ad1dd5f7c7ea3e47e6ccee518ca437c)  
  
std::vector< [Document](../../d8/d3e/classApp_1_1Document.html) * > | [openDocuments](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728) (const std::vector< std::string > &filenames, const std::vector< std::string > *paths=nullptr, const std::vector< std::string > *labels=nullptr, std::vector< std::string > *errs=nullptr, [bool](../../d9/db9/classbool.html) createView=true)  
| Open multiple documents.
[More...](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [getActiveDocument](../../da/dbf/classApp_1_1Application.html#a0be953356bea8c16bd958433e3769dd9) (void) const  
| Retrieve the active document.
[More...](../../da/dbf/classApp_1_1Application.html#a0be953356bea8c16bd958433e3769dd9)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d) (const char *Name) const  
| Retrieve a named document.
[More...](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d)  
  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocumentByPath](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0) (const char *path, [PathMatchMode](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64) checkCanonical=[PathMatchMode::MatchAbsolute](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a36428e3269d38765c18772524848e118)) const  
| Retrieve a document based on file path.
[More...](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0)  
  
const char * | [getDocumentName](../../da/dbf/classApp_1_1Application.html#addd212cb16839fa79141255914e271b5) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) *) const  
| gets the (internal) name of the document
[More...](../../da/dbf/classApp_1_1Application.html#addd212cb16839fa79141255914e271b5)  
  
std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > | [getDocuments](../../da/dbf/classApp_1_1Application.html#a955aad8188b482bb46f74a46b1946e3a) () const  
| get a list of all documents in the application
[More...](../../da/dbf/classApp_1_1Application.html#a955aad8188b482bb46f74a46b1946e3a)  
  
void | [setActiveDocument](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94) ([App::Document](../../d8/d3e/classApp_1_1Document.html) *pDoc)  
| Set the active document.
[More...](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94)  
  
void | [setActiveDocument](../../da/dbf/classApp_1_1Application.html#a174f0735b517d40e0a625f6ed098a40f) (const char *Name)  
void | [closeAllDocuments](../../da/dbf/classApp_1_1Application.html#a22f6f5a39ad9e36089852674bf63b7fa) (void)  
| close all documents (without saving)
[More...](../../da/dbf/classApp_1_1Application.html#a22f6f5a39ad9e36089852674bf63b7fa)  
  
[int](../../d1/da0/classint.html) | [addPendingDocument](../../da/dbf/classApp_1_1Application.html#a19eb6e22125db0a37cd540e4076b8b41) (const char *FileName, const char *objName, [bool](../../d9/db9/classbool.html) allowPartial)  
| Add pending document to open together with the current opening document.
[More...](../../da/dbf/classApp_1_1Application.html#a19eb6e22125db0a37cd540e4076b8b41)  
  
[bool](../../d9/db9/classbool.html) | [isRestoring](../../da/dbf/classApp_1_1Application.html#aa808751cb4b819afd2b2cab35c85cd1e) () const  
| Indicate whether the application is opening (restoring) some document.
[More...](../../da/dbf/classApp_1_1Application.html#aa808751cb4b819afd2b2cab35c85cd1e)  
  
[bool](../../d9/db9/classbool.html) | [isClosingAll](../../da/dbf/classApp_1_1Application.html#a8c5ef30def8bbda806044577be5d8639) () const  
| Indicate the application is closing all document.
[More...](../../da/dbf/classApp_1_1Application.html#a8c5ef30def8bbda806044577be5d8639)  
  
  
## Link handling  
  
---  
class | [App::Document](../../da/dbf/classApp_1_1Application.html#aad182780c892ebd99ac37bf77c046668)  
[int](../../d1/da0/classint.html) | [checkLinkDepth](../../da/dbf/classApp_1_1Application.html#aa00c4e24b653bbd40afeab1d79aa092c) ([int](../../d1/da0/classint.html) depth, [bool](../../d9/db9/classbool.html) no_throw=true)  
| Check for link recursion depth.
[More...](../../da/dbf/classApp_1_1Application.html#aa00c4e24b653bbd40afeab1d79aa092c)  
  
std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > | [getLinksTo](../../da/dbf/classApp_1_1Application.html#a9b748f2221ed6e0da2e575c161712c62) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *, [int](../../d1/da0/classint.html) options, [int](../../d1/da0/classint.html) maxCount=0) const  
| Return the links to a given object.
[More...](../../da/dbf/classApp_1_1Application.html#a9b748f2221ed6e0da2e575c161712c62)  
  
[bool](../../d9/db9/classbool.html) | [hasLinksTo](../../da/dbf/classApp_1_1Application.html#aa4f4f5ff098b353d7b984e79e7760333) (const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *obj) const  
| Check if there is any link to the given object.
[More...](../../da/dbf/classApp_1_1Application.html#aa4f4f5ff098b353d7b984e79e7760333)  
  
void | [renameDocument](../../da/dbf/classApp_1_1Application.html#a4b3708bc7e111c2f20c499c9a441172c) (const char *OldName, const char *NewName)  
| get called by the document when the name is changing
[More...](../../da/dbf/classApp_1_1Application.html#a4b3708bc7e111c2f20c499c9a441172c)  
  
  
## member for parameter  
  
---  
class | [ApplicationObserver](../../da/dbf/classApp_1_1Application.html#a2df792cc6b669bda9d727d7189139bfe)  
  
## Private Init, Destruct an Access methods  
  
---  
class | [AutoTransaction](../../da/dbf/classApp_1_1Application.html#a89cd7780c5bb86cbdb1b954dc7e85e82)  
  
## Init, Destruct an Access methods  
  
---  
[Application](../../da/dbf/classApp_1_1Application.html) & | [GetApplication](../../da/dbf/classApp_1_1Application.html#a3dddbb5ede4b34aaf7beca233a238dc9) (void)  
| Singleton getter of the
[Application](../../da/dbf/classApp_1_1Application.html "The Application The
root of the whole application.").
[More...](../../da/dbf/classApp_1_1Application.html#a3dddbb5ede4b34aaf7beca233a238dc9)  
  
static void | [init](../../da/dbf/classApp_1_1Application.html#a5a044efb1e023bdba4afd35d262654d5) ([int](../../d1/da0/classint.html) argc, char **argv)  
static void | [initTypes](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1) (void)  
static void | [destruct](../../da/dbf/classApp_1_1Application.html#a2429ab2a8f4255a5ce2d970aa74ba7f3) (void)  
static void | [destructObserver](../../da/dbf/classApp_1_1Application.html#a8ba7d824857a33ccb20839ec0ae19e44) (void)  
static void | [processCmdLineFiles](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa) (void)  
static std::list< std::string > | [getCmdLineFiles](../../da/dbf/classApp_1_1Application.html#afc32584672ac65f92291272a3b5b7cf3) ()  
static std::list< std::string > | [processFiles](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939) (const std::list< std::string > &)  
static void | [runApplication](../../da/dbf/classApp_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c) (void)  
static std::map< std::string, std::string > & | [Config](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc) (void)  
static [int](../../d1/da0/classint.html) | [GetARGC](../../da/dbf/classApp_1_1Application.html#a5bcab552656f3e96717093669792fd9c) (void)  
static char ** | [GetARGV](../../da/dbf/classApp_1_1Application.html#a82888da170ef62ef1f9abf5939c454cd) (void)  
  
## I/O of the document  
  
---  
This slot gets connected to all App::Documents created  
void | [slotBeforeChangeDocument](../../da/dbf/classApp_1_1Application.html#a4220212a2b53e4b8d6301196b4952dc5) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)  
void | [slotChangedDocument](../../da/dbf/classApp_1_1Application.html#a452e6b15d130b6591f6ff866ac25af79) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)  
void | [slotNewObject](../../da/dbf/classApp_1_1Application.html#aa6835d277021785cdd0f9ae038472762) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)  
void | [slotDeletedObject](../../da/dbf/classApp_1_1Application.html#ad6e7f304a6bf2a014d75039b8caa8837) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)  
void | [slotBeforeChangeObject](../../da/dbf/classApp_1_1Application.html#a1f3693850c25e228c864936c8f184e69) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &Prop)  
void | [slotChangedObject](../../da/dbf/classApp_1_1Application.html#a0b5cc52e99eb30dc897959a050904559) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &Prop)  
void | [slotRelabelObject](../../da/dbf/classApp_1_1Application.html#a5a3dcdcb74979ab007577f3684598c5a) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)  
void | [slotActivatedObject](../../da/dbf/classApp_1_1Application.html#ad726ef79a1bd4f878bf325784581a047) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)  
void | [slotUndoDocument](../../da/dbf/classApp_1_1Application.html#a72d52b675d7da0a4bf6dad8c0ed713a8) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)  
void | [slotRedoDocument](../../da/dbf/classApp_1_1Application.html#a8f9128275989a896d2f6c55d5af4785b) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)  
void | [slotRecomputedObject](../../da/dbf/classApp_1_1Application.html#a0c4c8807007b3ec248e7e4afc3bb1567) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) &)  
void | [slotRecomputed](../../da/dbf/classApp_1_1Application.html#ac1a39ddbde61ec1b603e8f3dc35af59e) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)  
void | [slotBeforeRecompute](../../da/dbf/classApp_1_1Application.html#abe70fa9ac1b478b8af5bf70e9dadbd6b) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)  
void | [slotOpenTransaction](../../da/dbf/classApp_1_1Application.html#ae6d03ca955417ba7789ee4fc6333792b) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, std::string)  
void | [slotCommitTransaction](../../da/dbf/classApp_1_1Application.html#a0f5b88b7f15a92bcd03f01e77ba8bcb1) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)  
void | [slotAbortTransaction](../../da/dbf/classApp_1_1Application.html#a06e511b2cd5a4443818c668ebc9014b1) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &)  
void | [slotStartSaveDocument](../../da/dbf/classApp_1_1Application.html#ad4b9071ef9241b25392537dd269cd823) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const std::string &)  
void | [slotFinishSaveDocument](../../da/dbf/classApp_1_1Application.html#a609e60d2806e8728c7bdb47840ea2d48) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const std::string &)  
void | [slotChangePropertyEditor](../../da/dbf/classApp_1_1Application.html#a6cd9752f5d95bce3f2942f5c8be8ecd1) (const [App::Document](../../d8/d3e/classApp_1_1Document.html) &, const [App::Property](../../d0/da9/classApp_1_1Property.html) &)  
[App::Document](../../d8/d3e/classApp_1_1Document.html) * | [openDocumentPrivate](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189) (const char *FileName, const char *propFileName, const char *label, [bool](../../d9/db9/classbool.html) isMainDoc, [bool](../../d9/db9/classbool.html) createView, std::vector< std::string > &&objNames)  
| open single document only
[More...](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189)  
  
  
## Detailed Description

The [Application](../../da/dbf/classApp_1_1Application.html "The Application
The root of the whole application.") The root of the whole application.

See also

    [App::Document](../../d8/d3e/classApp_1_1Document.html "The document class.")

## Member Enumeration Documentation

## ◆ PathMatchMode

| enum class
[App::Application::PathMatchMode](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64)  
---  
strong  
  
[Path](../../da/d2a/classApp_1_1Path.html "Base class of all geometric
document objects.") matching mode for
[getDocumentByPath()](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0
"Retrieve a document based on file path.")

Enumerator  
---  
MatchAbsolute | Match by resolving to absolute file path.   
MatchCanonical | Match by absolute path first.  If not found then match by resolving to canonical file path where any intermediate '.' '..' and symlinks are resolved.   
MatchCanonicalWarning | Same as MatchCanonical, but if a document is found by canonical path match, which means the document can be resolved using two different absolute path, a warning is printed and the found document is not returned.  This is to allow the caller to intentionally load the same physical file as separate documents.   
  
## Member Function Documentation

## ◆ addExportType()

void Application::addExportType  | ( | const char *  | _Type_ ,   
---|---|---|---  
|  | const char *  | _ModuleName_  
| ) | |   
  
Register an export filetype and a module name.

References
[Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc).

## ◆ addImportType()

void Application::addImportType  | ( | const char *  | _Type_ ,   
---|---|---|---  
|  | const char *  | _ModuleName_  
| ) | |   
  
Register an import filetype and a module name.

References
[Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc).

## ◆ AddParameterSet()

void Application::AddParameterSet  | ( | const char *  | _sName_| ) |   
---|---|---|---|---|---  
  
## ◆ addPendingDocument()

[int](../../d1/da0/classint.html) Application::addPendingDocument  | ( | const char *  | _FileName_ ,   
---|---|---|---  
|  | const char *  | _objName_ ,   
|  | [bool](../../d9/db9/classbool.html) | _allowPartial_  
| ) | |   
  
Add pending document to open together with the current opening document.

Referenced by
[App::DocInfo::attach()](../../d7/d23/classApp_1_1DocInfo.html#abfdf47204bf7a84f4d19f3a04c5a4199),
and
[App::DocInfo::get()](../../d7/d23/classApp_1_1DocInfo.html#aaa708c0148a14d954611470e84dbaa5a).

## ◆ changeExportModule()

void Application::changeExportModule  | ( | const char *  | _Type_ ,   
---|---|---|---  
|  | const char *  | _OldModuleName_ ,   
|  | const char *  | _NewModuleName_  
| ) | |   
  
Change the module name of a registered filetype.

## ◆ changeImportModule()

void Application::changeImportModule  | ( | const char *  | _Type_ ,   
---|---|---|---  
|  | const char *  | _OldModuleName_ ,   
|  | const char *  | _NewModuleName_  
| ) | |   
  
Change the module name of a registered filetype.

## ◆ checkLinkDepth()

[int](../../d1/da0/classint.html) Application::checkLinkDepth  | ( | [int](../../d1/da0/classint.html) | _depth_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _no_throw_ = `true`  
| ) | |   
  
Check for link recursion depth.

Parameters

     depth| current depth   
---|---  
no_throw| whether to throw exception  
  
Returns

    Return the maximum remaining depth.

The function uses an internal count of all objects in all documents as the
limit of recursion depth.

Referenced by
[PartDesign::SubShapeBinder::getSubObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#afb7e01deac9646afcd5dc1b2aa07042b).

## ◆ closeActiveTransaction()

void Application::closeActiveTransaction  | ( | [bool](../../d9/db9/classbool.html) | _abort_ = `false`,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _id_ = `0`  
| ) | |   
  
Commit/abort current active transactions.

Parameters

     abort| whether to abort or commit the transactions  
---|---  
  
Bsides calling this function directly, it will be called by automatically if
1) any new transaction is created with a different ID, or 2) any transaction
with the current active transaction ID is either committed or aborted

Referenced by
[Gui::Command::abortCommand()](../../d2/dff/classGui_1_1Command.html#a43a34da69c9daaaa2f2c2c462a1479ea),
[App::Document::abortTransaction()](../../d8/d3e/classApp_1_1Document.html#a01f60ab9bc840c591e8f3b6f78e51041),
[Gui::ElementColors::Private::accept()](../../d8/dc9/classElementColors_1_1Private.html#a5704a7d026d4033d6f6b98086de77f53),
[PartDesignGui::DlgActiveBody::accept()](../../dc/dd5/classPartDesignGui_1_1DlgActiveBody.html#a1932d79f3d3669f8b2f576ead60d0ab7),
[App::TransactionLocker::activate()](../../df/d3c/classApp_1_1TransactionLocker.html#a1f96608a8ad20ffb50de613395430113),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[App::AutoTransaction::close()](../../dd/d19/classApp_1_1AutoTransaction.html#a78f86284384fbf21e95706b6e5dd3ddb),
[Gui::Command::commitCommand()](../../d2/dff/classGui_1_1Command.html#a36a42a5d17c1ff229c649d927f6c3faa),
[App::Document::commitTransaction()](../../d8/d3e/classApp_1_1Document.html#a1ebcf21ffc49ae09b241f2bcab6bfe01),
[TechDrawGui::QGIRichAnno::mouseDoubleClickEvent()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#ae314ffc101d4592c4a492f380ce72655),
[TechDrawGui::QGIViewAnnotation::mouseDoubleClickEvent()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#a0b2aec7a7e987b6deaca89c24d426c8d),
[Gui::ElementColors::Private::reset()](../../d8/dc9/classElementColors_1_1Private.html#a0afa4c51b89ebd4355b64c0392a498d8),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## ◆ closeAllDocuments()

void Application::closeAllDocuments  | ( | void  | | ) |   
---|---|---|---|---|---  
  
close all documents (without saving)

References
[closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244).

Referenced by
[Gui::MainWindow::closeAllDocuments()](../../d5/d2f/classGui_1_1MainWindow.html#a26025f09b536690547638795dfd37010),
[Gui::GUIApplication::commitData()](../../d2/da0/classGui_1_1GUIApplication.html#a27c9cbd221bf1ca50b1a91de37ff9031),
and
[Gui::Application::tryClose()](../../d9/da8/classGui_1_1Application.html#a530d999072674fac5a2ea1127a07a981).

## ◆ closeDocument()

[bool](../../d9/db9/classbool.html) Application::closeDocument  | ( | const char *  | _name_| ) |   
---|---|---|---|---|---  
  
Closes the document _name_ and removes it from the application.

References
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94),
[signalDeletedDocument](../../da/dbf/classApp_1_1Application.html#aef84fb43739719380174bb3ea016cbc3),
and
[signalDeleteDocument](../../da/dbf/classApp_1_1Application.html#aeea280bfd7007230846703a362c16a47).

Referenced by
[Gui::Dialog::DocumentRecovery::accept()](../../d2/da2/classGui_1_1Dialog_1_1DocumentRecovery.html#a70922db70921db97f90cd5a5420cdc08),
[closeAllDocuments()](../../da/dbf/classApp_1_1Application.html#a22f6f5a39ad9e36089852674bf63b7fa),
[openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
and
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

## ◆ Config()

| static std::map< std::string, std::string > & App::Application::Config  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[Gui::MainWindow::aboutImage()](../../d5/d2f/classGui_1_1MainWindow.html#a6b1c6dbe4ba1214f91463db90f651766),
[StdViewScreenShot::activated()](../../d9/da6/classStdViewScreenShot.html#a4229e4b93ce96f603dbfb3cdee194091),
[addExportType()](../../da/dbf/classApp_1_1Application.html#abf69fc8463ed5bc98a17b445e5ad7def),
[addImportType()](../../da/dbf/classApp_1_1Application.html#a86d839fa4b89602b727a18868a3a4356),
[Gui::RecentFilesAction::appendFile()](../../d0/d17/classGui_1_1RecentFilesAction.html#a14d0d42121986c2a14babf830504326f),
[Gui::RecentMacrosAction::appendFile()](../../d2/df7/classGui_1_1RecentMacrosAction.html#ae1d2230890f6029a2eed3aaef4840c0c),
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[Gui::SoFCOffscreenRenderer::createMIBA()](../../d9/dc4/classGui_1_1SoFCOffscreenRenderer.html#ab68f85a0a45a5ae53f50b87dffa480d1),
[App::Document::exportObjects()](../../d8/d3e/classApp_1_1Document.html#a7ebc166fbd54e4c0088cd06ad006e739),
[Gui::BitmapFactoryInst::instance()](../../dc/da1/classGui_1_1BitmapFactoryInst.html#a1f290ef0fa8fecac10e5d837308f9c63),
[Gui::Dialog::DlgGeneralImp::loadSettings()](../../df/ddc/classGui_1_1Dialog_1_1DlgGeneralImp.html#af5eac73c627e99f23296d0f7f2c34ae8),
[Gui::Dialog::DlgSettingsLazyLoadedImp::loadSettings()](../../de/d4f/classGui_1_1Dialog_1_1DlgSettingsLazyLoadedImp.html#ab0f7ae19d7b6b69a0f08109c559c9c06),
[StartGui::DlgStartPreferencesImp::loadSettings()](../../d9/d5e/classStartGui_1_1DlgStartPreferencesImp.html#a83a726bf6af6dbeb1e1734ee2c93f7ca),
[Gui::MainWindow::loadWindowSettings()](../../d5/d2f/classGui_1_1MainWindow.html#a00d4bad121cc286443a7f7f628f519f8),
[Gui::MainWindow::MainWindow()](../../d5/d2f/classGui_1_1MainWindow.html#a84c74efa977302744093e2027b0dd801),
[Gui::Dialog::AboutDialog::on_copyButton_clicked()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a907ddd1537ac512ba4859ee2fb4575a6),
[Gui::Dialog::ApplicationCache::periodicCheckOfSize()](../../db/df8/classGui_1_1Dialog_1_1ApplicationCache.html#ac06d6ef6d29ea51faa33fdfd3447ac78),
[processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[Gui::FileDialog::restoreLocation()](../../de/d93/classGui_1_1FileDialog.html#a5aedc90989870d2e5b2978a51b81e668),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[App::Metadata::satisfies()](../../db/dfe/classApp_1_1Metadata.html#a022c52baf660a45a8870dd2e7042f13c),
[App::Document::Save()](../../d8/d3e/classApp_1_1Document.html#ae34e6dd3d4959a4d0916d5055afb34a0),
[Gui::Thumbnail::SaveDocFile()](../../d3/d4d/classGui_1_1Thumbnail.html#a2c08e4f59778bc033417224a3b83028c),
[Gui::MainWindow::saveWindowSettings()](../../d5/d2f/classGui_1_1MainWindow.html#a6b93d3ef354e35fa3e45779e36926347),
[Gui::Dialog::AboutDialog::setupLabels()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a51644991a7be76018313df77bc001021),
[Gui::MainWindow::splashImage()](../../d5/d2f/classGui_1_1MainWindow.html#adc82dc82e0038c9275aad7370b7007f7),
[Gui::SplashObserver::SplashObserver()](../../d4/d46/classGui_1_1SplashObserver.html#a1c90fea7442c16e6ad438308b4c79b9d),
[Gui::MainWindow::startSplasher()](../../d5/d2f/classGui_1_1MainWindow.html#a582325552a23f1edf2320b39dfd84547),
[App::Metadata::supportsCurrentFreeCAD()](../../db/dfe/classApp_1_1Metadata.html#a5a2340d71416e32211e1a6d1da938fcb),
[Gui::Dialog::TextureMapping::TextureMapping()](../../d2/d56/classGui_1_1Dialog_1_1TextureMapping.html#a3ce062f559f812ae48aba8e944c96a59),
[Gui::Application::workbenches()](../../d9/da8/classGui_1_1Application.html#ac878d247d754de84bbda7d64e2121d2f),
and
[CDxfWrite::writeHeaderSection()](../../d6/d47/classCDxfWrite.html#a64e006e000c62912764021bc0e727ec3).

## ◆ destruct()

| void Application::destruct  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Type::destruct()](../../dc/dee/classBase_1_1Type.html#aeb333337bdff5ab1d455a8c0f8c516a4),
[destructObserver()](../../da/dbf/classApp_1_1Application.html#a8ba7d824857a33ccb20839ec0ae19e44),
[Base::InterpreterSingleton::finalize()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a36c342466389ab64392ca10ad6d4724c),
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
and
[ParameterManager::Terminate()](../../db/daa/classParameterManager.html#adac995cb7af038d0a11d2910ce089f1f).

## ◆ destructObserver()

| void Application::destructObserver  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::DetachObserver()](../../df/dca/classBase_1_1ConsoleSingleton.html#ad4de0de58604c504687caadd42059cd6).

Referenced by
[destruct()](../../da/dbf/classApp_1_1Application.html#a2429ab2a8f4255a5ce2d970aa74ba7f3),
[init()](../../da/dbf/classApp_1_1Application.html#a5a044efb1e023bdba4afd35d262654d5),
[Gui::Application::initApplication()](../../d9/da8/classGui_1_1Application.html#af7364610acb272a9be0e6296b64e1d83),
and
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c).

## ◆ getActiveDocument()

[Document](../../d8/d3e/classApp_1_1Document.html) * Application::getActiveDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Retrieve the active document.

Referenced by
[MeshGui::Segmentation::accept()](../../da/d24/classMeshGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[MeshGui::SegmentationBestFit::accept()](../../d8/dc7/classMeshGui_1_1SegmentationBestFit.html#a22c228aaefd47e1621d12b98efd38ad8),
[MeshPartGui::Tessellation::accept()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#a222ec7598711d0c506f4897d9a996bd1),
[PartGui::DlgBooleanOperation::accept()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a8d2d05821780caa8df3655ea6cb45b34),
[PartGui::DlgFilletEdges::accept()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#aa1cd2ae4ca0d1438188a366f36cdb552),
[PartGui::DlgRevolution::accept()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a92a90c8ff44e8e2f6774d0713d47bbbd),
[ReverseEngineeringGui::Segmentation::accept()](../../dc/d44/classReverseEngineeringGui_1_1Segmentation.html#aa8bbe59679630163416cf45257673284),
[StdCmdOpen::activated()](../../d8/d6a/classStdCmdOpen.html#a9c9f69468076298c2a265906b3594a9d),
[StdCmdMergeProjects::activated()](../../dc/d16/classStdCmdMergeProjects.html#a4044e49d39d63eb5cf4ee3885609642a),
[StdCmdDependencyGraph::activated()](../../d6/d34/classStdCmdDependencyGraph.html#a7df1908a23cee4220f929719c88ead24),
[StdCmdDuplicateSelection::activated()](../../d4/d75/classStdCmdDuplicateSelection.html#a1ffe671eebc9f7e4c99740df06eaf0a9),
[StdCmdSelectAll::activated()](../../d7/d6b/classStdCmdSelectAll.html#a202abf9e8903ce640f488dee93886a8e),
[StdCmdExpression::activated()](../../d2/dae/classStdCmdExpression.html#aa1e543b14716a409595cfc12ab619d28),
[StdCmdLinkMakeGroup::activated()](../../d8/db4/classStdCmdLinkMakeGroup.html#afbac678a966340088d0d13603d4865f0),
[StdCmdLinkMake::activated()](../../df/d19/classStdCmdLinkMake.html#a227d693344e3d5329aad38d5ece1606d),
[StdCmdLinkMakeRelative::activated()](../../d1/dc3/classStdCmdLinkMakeRelative.html#a17226f2227a0ad3b9fc8f39eec4577ed),
[StdCmdLinkImportAll::activated()](../../d1/d95/classStdCmdLinkImportAll.html#a589020e4cea9b86e1167d781473691a9),
[CmdSandboxMeshLoader::activated()](../../db/d92/classCmdSandboxMeshLoader.html#a32745b05600acc57d5f7f75dbb0c8715),
[PartGui::TaskMeasureLinear::buildDimension()](../../d7/ddf/classPartGui_1_1TaskMeasureLinear.html#ad770594bd530db44c7225b6995865174),
[PartGui::TaskMeasureAngular::buildDimension()](../../d7/dea/classPartGui_1_1TaskMeasureAngular.html#a6415acf0b23c450508d55d94363508e7),
[Cloud::Module::cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4),
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71),
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[Fem::createObjectByType()](../../dd/d72/namespaceFem.html#af3663ac69e66763d50fbbd579cb9024a),
[PartGui::DlgPrimitives::createPrimitive()](../../de/d66/classPartGui_1_1DlgPrimitives.html#a6c387f1ebf9f760ba3dab5fb13de91dc),
[SketcherGui::ConstraintView::deleteSelectedItems()](../../df/d7b/classSketcherGui_1_1ConstraintView.html#a889547f07246319b638484850553f0d8),
[SketcherGui::ElementView::deleteSelectedItems()](../../dd/d88/classSketcherGui_1_1ElementView.html#aef0f7256d4d6f95265d6c2c1f0ea17ac),
[PartGui::DlgProjectionOnSurface::DlgProjectionOnSurface()](../../d2/da4/classPartGui_1_1DlgProjectionOnSurface.html#a280d8ac8bf690484a268f54625c2c7e2),
[PartGui::evaluateAngularPreSelection()](../../d5/d49/namespacePartGui.html#af0dc1ad1549a7fac118db816447cb551),
[PartGui::evaluateLinearPreSelection()](../../d5/d49/namespacePartGui.html#acba3e20aed461c721a1db9f14b75ab69),
[PartGui::DlgExtrusion::findShapes()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a8976c72de1970766d8d2dc5391e34903),
[PartGui::DlgFilletEdges::findShapes()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a3bd2ba2fd4b83d69ee72ad80a4cae2e4),
[PartGui::DlgExtrusion::getAxisLink()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#af73d5a43aaa0f3dcee9dff9571f7d518),
[PartGui::DlgRevolution::getAxisLink()](../../d1/d83/classPartGui_1_1DlgRevolution.html#a6a4ccdcedbf3ed5c9c022286a9d211f1),
[Gui::SelectionSingleton::getDocument()](../../d4/dca/classGui_1_1SelectionSingleton.html#a98c2fdd9b3322c12877717c40e64ca98),
[Fem::getObjectByType()](../../dd/d72/namespaceFem.html#a1d62957fae198eb1c03b3ce2c2503c3c),
[Gui::Command::getObjectCmd()](../../d2/dff/classGui_1_1Command.html#a4335f72b8076a5ccb39a59694b8ddc01),
[MeshGui::MeshSelection::getObjects()](../../d2/d86/classMeshGui_1_1MeshSelection.html#a28460ca199aa44464490e0b41eb44cbd),
[PartGui::DlgRevolution::getShapesToRevolve()](../../d1/d83/classPartGui_1_1DlgRevolution.html#af847882d2e684d1f219a9353aec25281),
[Gui::Command::getUniqueObjectName()](../../d2/dff/classGui_1_1Command.html#ac13a62139080f7aeddd6df9ca2af8a36),
[Gui::MainWindow::insertFromMimeData()](../../d5/d2f/classGui_1_1MainWindow.html#a3b695bba64b1eead11c5bf3843c54790),
[StdCmdSelectAll::isActive()](../../d7/d6b/classStdCmdSelectAll.html#a9fe58b04432e657673c9bde710368dda),
[StdCmdLinkMakeGroup::isActive()](../../d8/db4/classStdCmdLinkMakeGroup.html#a01eda1c7f259608fe6358856cca15b79),
[StdCmdLinkMake::isActive()](../../df/d19/classStdCmdLinkMake.html#ab65869412bd6bd4b0859014dac4a006f),
[StdCmdLinkImportAll::isActive()](../../d1/d95/classStdCmdLinkImportAll.html#a061965b212d6f01f3fb4452aeb30a140),
[StdCmdSelectVisibleObjects::isActive()](../../dc/dac/classStdCmdSelectVisibleObjects.html#ac481b4c69da6efabf010b5be8f8be544),
[StdCmdToggleObjects::isActive()](../../d5/d4f/classStdCmdToggleObjects.html#a691fdaf83187c6247bcff7308d92810c),
[StdCmdShowObjects::isActive()](../../da/ded/classStdCmdShowObjects.html#ab4fd22e2436de4454005bb26004d614d),
[StdCmdHideObjects::isActive()](../../d5/d83/classStdCmdHideObjects.html#ace85617a4c94e3073b5fe5cd717d7e82),
[StdCmdMeasureDistance::isActive()](../../db/dfc/classStdCmdMeasureDistance.html#ae34eeedc376782cacdd1d9b6745864ad),
[Cloud::Module::LinkXSetValue()](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af),
[PartDesignGui::TaskFeaturePick::makeCopy()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a9e9b1a639025522ada407aaa6b19596e),
[MeshGui::DlgRegularSolidImp::on_createSolidButton_clicked()](../../d2/d14/classMeshGui_1_1DlgRegularSolidImp.html#abef574440e936e39b317fccf3653ea55),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[SpreadsheetGui::SheetTableView::pasteClipboard()](../../d5/d7d/classSpreadsheetGui_1_1SheetTableView.html#a515807fe0797c9e6f83f28139009c68a),
[Gui::Dialog::Placement::Placement()](../../d8/d6c/classGui_1_1Dialog_1_1Placement.html#a61902824aa6953c8333e8d319eab8374),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[PartGui::refreshDimensions()](../../d5/d49/namespacePartGui.html#a4b5c50d6eef4609933d5d488d2c6eb51),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
[Sandbox::DocumentThread::run()](../../dc/d85/classSandbox_1_1DocumentThread.html#aac7674529cc4f8effb2381d67d5a5337),
[Sandbox::DocumentTestThread::run()](../../d5/d8a/classSandbox_1_1DocumentTestThread.html#a27751a48ad75c90b8b678641eb975cde),
[Gui::TreeWidget::selectLinkedObject()](../../de/de0/classGui_1_1TreeWidget.html#af798259dba953fe31049a2fe74c048e4),
[Gui::QuantitySpinBox::setBoundToByName()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a6b7ec360dc439b034f4793f05c7d074a),
[PartDesignGui::TaskBoxPrimitives::setPrimitive()](../../d4/db4/classPartDesignGui_1_1TaskBoxPrimitives.html#a0dfd3009478f17d59285f4952f42abc2),
[Gui::TaskView::TaskWatcherCommandsEmptyDoc::shouldShow()](../../dc/d6d/classGui_1_1TaskView_1_1TaskWatcherCommandsEmptyDoc.html#ac4edf46cf0fb50d8ad8c1dbbda0a6517),
[Path::Area::showShape()](../../d8/dfc/classPath_1_1Area.html#ac20bf1933f3cb18e24b0892f378b761f),
[Gui::Application::sInsert()](../../d9/da8/classGui_1_1Application.html#aca6ab0f62cf4fb268ea9a87ce3cebaf2),
[Gui::Document::slotSkipRecompute()](../../de/d4e/classGui_1_1Document.html#a1857cda5f702ac9d619826d18e89c656),
[MeshGui::ViewProviderMesh::splitMesh()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a3480f540c644cb38cd0a1ed1bc304d94),
[DrawingGui::TaskOrthoViews::TaskOrthoViews()](../../d4/dd1/classDrawingGui_1_1TaskOrthoViews.html#ae82943a42dfe2bfe1a72ace25e2ddb96),
[InspectionGui::VisualInspection::VisualInspection()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#aa13e595beac41fb1b077d794cd7fc0bc),
and
[Fem::FemVTKTools::writeResult()](../../d6/d26/classFem_1_1FemVTKTools.html#afe10808623915c79b6e74786a6f6d0e3).

## ◆ getActiveTransaction()

const char * Application::getActiveTransaction  | ( | [int](../../d1/da0/classint.html) *  | _tid_ = `nullptr`| ) |  const  
---|---|---|---|---|---  
  
Return the current active transaction name and ID.

References
[App::Transaction::getLastID()](../../de/dbf/classApp_1_1Transaction.html#a40df9cf53bada527779dd522a9208e16).

Referenced by
[App::Document::addOrRemovePropertyOfObject()](../../d8/d3e/classApp_1_1Document.html#ac4060590326f48e4fb73a542d2bd6d02),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[Gui::Command::hasPendingCommand()](../../d2/dff/classGui_1_1Command.html#ab0ec199be441f0aec35cdb61c84e588e),
[setActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a78fddfc24e060908e047c5472857c3ff),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
[PartDesignGui::TaskDressUpParameters::setupTransaction()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a6f99d504a2dbb11111be017f2bfe4bbf),
[PartDesignGui::TaskTransformedParameters::setupTransaction()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#abf0df5b3ed2b19577b9bd4d6359c9c79),
[PartDesignGui::TaskDressUpParameters::TaskDressUpParameters()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#afbc2f79ef1b06de734eb9ad15a12537b),
and
[PartDesignGui::TaskTransformedParameters::TaskTransformedParameters()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#a36fed6044c781db8268f058ecba28867).

## ◆ GetARGC()

| static [int](../../d1/da0/classint.html) App::Application::GetARGC  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c).

## ◆ GetARGV()

| static char ** App::Application::GetARGV  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
Referenced by
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c).

## ◆ getCmdLineFiles()

| std::list< std::string > Application::getCmdLineFiles  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
and
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c).

## ◆ getDocument()

[App::Document](../../d8/d3e/classApp_1_1Document.html) * Application::getDocument  | ( | const char *  | _Name_| ) |  const  
---|---|---|---|---|---  
  
Retrieve a named document.

Referenced by
[DrawingGui::TaskDlgOrthoViews::accept()](../../d7/d7f/classDrawingGui_1_1TaskDlgOrthoViews.html#a560435454ff13375f2256abfd15d7928),
[PartGui::Mirroring::accept()](../../db/d41/classPartGui_1_1Mirroring.html#a65b4bef12c8f1db83eee1cd6799f2794),
[SpreadsheetGui::DlgBindSheet::accept()](../../d5/d0a/classSpreadsheetGui_1_1DlgBindSheet.html#ad6e5cb0995aaa1341a57bdb97ed49cbd),
[PartGui::DlgExtrusion::apply()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a6428c7ac6585ad41ed9792aeea96d2f7),
[PartDesignGui::TaskFeaturePick::buildFeatures()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#a10945e14aca2a56d0f5ac9e4b0064379),
[Gui::SoFCUnifiedSelection::doAction()](../../dd/d97/classGui_1_1SoFCUnifiedSelection.html#a6df6c46d47a0e7d092d2df18c2da9160),
[Gui::TreeWidget::dropEvent()](../../de/de0/classGui_1_1TreeWidget.html#a7325c526b4bf86a75fe2e7763a796a6f),
[App::PropertyLinkBase::exportSubName()](../../d6/d3b/classApp_1_1PropertyLinkBase.html#a08eab53abe5c11c895d4ecea426485ad),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[App::DocumentT::getDocument()](../../dc/d60/classApp_1_1DocumentT.html#a320fef7d6acc485cb077ff5acaad8c7b),
[App::DocumentObjectT::getDocument()](../../d5/d07/classApp_1_1DocumentObjectT.html#acadd08abfd3a0d947b8047ab70d4eb31),
[Gui::Application::getDocument()](../../d9/da8/classGui_1_1Application.html#aecd763cf165a068f2ddf1f44a7074b04),
[Gui::Command::getDocument()](../../d2/dff/classGui_1_1Command.html#a6cbacf22c3e1eaed5b5676ef4a84450f),
[Gui::SelectionSingleton::getDocument()](../../d4/dca/classGui_1_1SelectionSingleton.html#a98c2fdd9b3322c12877717c40e64ca98),
[App::ObjectIdentifier::getDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f),
[Gui::SelectionObject::getObject()](../../d1/d4e/classGui_1_1SelectionObject.html#ae875cfc45d62993fe0411425b8a22252),
[PartGui::getShapeFromStrings()](../../d5/d49/namespacePartGui.html#a5245fac5abffb33a9341c1523c829f3d),
[PartGui::DlgExtrusion::getShapesToExtrude()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a2e05cea8f2a72a8c3ec08d760416cc7a),
[App::PropertyXLink::Paste()](../../d2/de2/classApp_1_1PropertyXLink.html#a6d593eed6217cccfdad4a79a4c752c27),
[StdCmdExpression::pasteExpressions()](../../d2/dae/classStdCmdExpression.html#abab137615ab802f7688ff0b623022b9f),
[DrawingGui::TaskDlgOrthoViews::reject()](../../d7/d7f/classDrawingGui_1_1TaskDlgOrthoViews.html#ad768319194666b990da5cb889cb0f809),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
[Gui::QuantitySpinBox::setBoundToByName()](../../d6/d3e/classGui_1_1QuantitySpinBox.html#a6b7ec360dc439b034f4793f05c7d074a),
[Gui::SelectionSingleton::setVisible()](../../d4/dca/classGui_1_1SelectionSingleton.html#ab23ac3091ebd5ec52d897b3416a05e2d),
and
[Gui::Application::sInsert()](../../d9/da8/classGui_1_1Application.html#aca6ab0f62cf4fb268ea9a87ce3cebaf2).

## ◆ getDocumentByPath()

[Document](../../d8/d3e/classApp_1_1Document.html) * Application::getDocumentByPath  | ( | const char *  | _path_ ,   
---|---|---|---  
|  | [PathMatchMode](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64) | _checkCanonical_ = `[PathMatchMode::MatchAbsolute](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a36428e3269d38765c18772524848e118)`  
| ) | |  const  
  
Retrieve a document based on file path.

Parameters

     path| file path   
---|---  
checkCanonical| file path matching mode,  
  
See also

    [PathMatchMode](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64 "Path matching mode for getDocumentByPath\(\)"). 

Returns

    Return the document found by matching with the given path 

References
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[MatchAbsolute](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a36428e3269d38765c18772524848e118),
and
[MatchCanonical](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a14cdc18650f96f3d8305d33e09b1d961).

Referenced by
[openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
and
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

## ◆ getDocumentName()

const char * Application::getDocumentName  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |  const  
---|---|---|---|---|---  
  
gets the (internal) name of the document

Referenced by
[MeshGui::DlgEvaluateMeshImp::on_repairAllTogether_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a37ba0babe8914d5dce379504b9adf12e),
[MeshGui::DlgEvaluateMeshImp::on_repairDegeneratedButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#ab3cdbd594788a57c256755a837018d2f),
[MeshGui::DlgEvaluateMeshImp::on_repairDuplicatedFacesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aede555d793810d6cfc2632ecf409e5fa),
[MeshGui::DlgEvaluateMeshImp::on_repairDuplicatedPointsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aef057c023433bea4e835ee2e61dd0d17),
[MeshGui::DlgEvaluateMeshImp::on_repairFoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a492d611b70e28517f204bf25bf76184e),
[MeshGui::DlgEvaluateMeshImp::on_repairIndicesButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a3da19b67de1065f6efa4da4a159d9e97),
[MeshGui::DlgEvaluateMeshImp::on_repairNonmanifoldsButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a515dab5e6ea530b164559c860252bfae),
[MeshGui::DlgEvaluateMeshImp::on_repairOrientationButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a69c2e5330dbce392a37614ce7e27d7fe),
[MeshGui::DlgEvaluateMeshImp::on_repairSelfIntersectionButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#acd921ad6e7470851387f97162ff6e288),
[Gui::Document::saveAs()](../../de/d4e/classGui_1_1Document.html#ac2c94d85366e44a09c35563a3848c852),
and
[Gui::Document::saveCopy()](../../de/d4e/classGui_1_1Document.html#a27866ed0852198802f9889404d46dffb).

## ◆ getDocuments()

std::vector< [App::Document](../../d8/d3e/classApp_1_1Document.html) * > Application::getDocuments  | ( | | ) |  const  
---|---|---|---|---  
  
get a list of all documents in the application

Referenced by
[StdCmdToggleSelectability::activated()](../../d6/d27/classStdCmdToggleSelectability.html#a0ce2e8138a2c546adb161b8804521a28),
[Gui::MainWindow::closeAllDocuments()](../../d5/d2f/classGui_1_1MainWindow.html#a26025f09b536690547638795dfd37010),
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[App::ObjectIdentifier::getDocument()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a83e646e86cdcb6d173503a01121ad91f),
[Gui::Dialog::DlgPropertyLink::init()](../../da/d23/classGui_1_1Dialog_1_1DlgPropertyLink.html#a0f9c31263c267be5f9d378e4f49cfa8a),
[StdCmdCloseAllWindows::isActive()](../../d2/d0e/classStdCmdCloseAllWindows.html#acbe95e7c32a0c76b3333a8f1905191e2),
[Cloud::Module::LinkXSetValue()](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af),
[Gui::Document::saveAll()](../../de/d4e/classGui_1_1Document.html#a855313ae529de818172eac8acd860157),
[PartGui::DlgSettings3DViewPart::saveSettings()](../../d2/d45/classPartGui_1_1DlgSettings3DViewPart.html#ae256735cc3da90df3b8c481c60d28f72),
and
[Attacher::AttachEngine::verifyReferencesAreSafe()](../../d2/d85/classAttacher_1_1AttachEngine.html#ac8843a2175ebae4cc4d23f006d61abe1).

## ◆ getExecutableName()

| std::string Application::getExecutableName  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::Dialog::DocumentRecoveryHandler::checkForPreviousCrashes()](../../d9/d92/classGui_1_1Dialog_1_1DocumentRecoveryHandler.html#ab730fb9e0f542787859e891006695f0d),
[Gui::StdCmdDownloadOnlineHelp::createAction()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#ac421cbffbd352e8ad273711b52fa1602),
[Gui::SoFCOffscreenRenderer::createMIBA()](../../d9/dc4/classGui_1_1SoFCOffscreenRenderer.html#ab68f85a0a45a5ae53f50b87dffa480d1),
[App::Document::getTransientDirectoryName()](../../d8/d3e/classApp_1_1Document.html#a787fa9500a9467131f2fb940083e4300),
[Gui::StdCmdDownloadOnlineHelp::languageChange()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#ae12919c96eb90a42290f06041bd5742a),
[Gui::Dialog::AboutDialog::on_copyButton_clicked()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a907ddd1537ac512ba4859ee2fb4575a6),
[Gui::Dialog::ApplicationCache::periodicCheckOfSize()](../../db/df8/classGui_1_1Dialog_1_1ApplicationCache.html#ac06d6ef6d29ea51faa33fdfd3447ac78),
[Gui::GUISingleApplication::Private::Private()](../../de/d95/classGUISingleApplication_1_1Private.html#a310d2577b4af09e88fc22b3beeef4687),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
and
[Gui::SoFCOffscreenRenderer::writeToImageFile()](../../d9/dc4/classGui_1_1SoFCOffscreenRenderer.html#a9492ac7c39b49b35f6ce5ed674f8bf4a).

## ◆ getExportFilters() [1/2]

std::map< std::string, std::string > Application::getExportFilters  | ( | const char *  | _Type_| ) |  const  
---|---|---|---|---|---  
  
Return the export filters with modules of a given filetype.

Referenced by
[StdCmdExport::activated()](../../dd/d65/classStdCmdExport.html#a7ee127d8eac7ec03ab328a47bc3fc36f),
and
[Gui::SelectModule::exportHandler()](../../d6/d0e/classGui_1_1SelectModule.html#aa6a2edac4ac56e97e23e41e04afdb17a).

## ◆ getExportFilters() [2/2]

std::map< std::string, std::string > Application::getExportFilters  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Return a list of all export filters.

## ◆ getExportModules() [1/2]

std::vector< std::string > Application::getExportModules  | ( | | ) |  const  
---|---|---|---|---  
  
Return a list of all modules.

## ◆ getExportModules() [2/2]

std::vector< std::string > Application::getExportModules  | ( | const char *  | _Type_| ) |  const  
---|---|---|---|---|---  
  
Return a list of modules that support the given filetype.

Referenced by
[processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa).

## ◆ getExportTypes() [1/2]

std::vector< std::string > Application::getExportTypes  | ( | const char *  | _Module_| ) |  const  
---|---|---|---|---|---  
  
Return a list of filetypes that are supported by a module.

## ◆ getExportTypes() [2/2]

std::vector< std::string > Application::getExportTypes  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Return a list of all filetypes.

## ◆ getHelpDir()

| std::string Application::getHelpDir  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::Dialog::DlgOnlineHelpImp::getStartpage()](../../da/d32/classGui_1_1Dialog_1_1DlgOnlineHelpImp.html#a4263b85505557c9e34cebed05c16d7a8),
[Gui::Dialog::AboutDialog::showCollectionInformation()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#acf4864f4f05375f3b5d52104f749a7bb),
[Gui::Dialog::AboutDialog::showLibraryInformation()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a5102f630fff98802fae8aa1b85f089ef),
and
[Gui::Dialog::AboutDialog::showLicenseInformation()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#affe4f4e11404f74d9ab2642e2e928b5e).

## ◆ getHomePath()

| std::string Application::getHomePath  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::MainWindow::aboutImage()](../../d5/d2f/classGui_1_1MainWindow.html#a6b1c6dbe4ba1214f91463db90f651766),
[Gui::Dialog::DlgMacroExecuteImp::accept()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#ab7da5ec611b1f01da76f8c3a3729be8d),
[Gui::MacroCommand::activated()](../../dc/d65/classGui_1_1MacroCommand.html#a3e9f3632b6f802aff70a6fa7d55c4ae5),
[Gui::StdCmdDownloadOnlineHelp::activated()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#a29c4d53cfdd555b2a313eaa38cfa18be),
[Gui::Dialog::DlgCustomActionsImp::DlgCustomActionsImp()](../../df/dc6/classGui_1_1Dialog_1_1DlgCustomActionsImp.html#ab23956d9fabc61bb78b88e3655094fd3),
[Gui::Dialog::DlgMacroExecuteImp::fillUpList()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a2189cb1e6d331adf9e84e40b59d33f74),
[Gui::BitmapFactoryInst::instance()](../../dc/da1/classGui_1_1BitmapFactoryInst.html#a1f290ef0fa8fecac10e5d837308f9c63),
[Gui::PyResource::load()](../../df/d89/classGui_1_1PyResource.html#a368de62b9482044648e313edb8dc634c),
[Gui::Dialog::DlgMacroExecuteImp::on_editButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a319f0ec12fa8e8b8d05d0dba510b5e95),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::Application::sAddIconPath()](../../d9/da8/classGui_1_1Application.html#a61e9e966f2ca7b8ac49606b0eba41c29),
[Gui::Application::sAddLangPath()](../../d9/da8/classGui_1_1Application.html#af06212156d42febdea6d4b6b14fd9947),
[Gui::Application::sAddResPath()](../../d9/da8/classGui_1_1Application.html#aa51facd83fba0b61ec9d5a8448eb1e93),
and
[Gui::MainWindow::splashImage()](../../d5/d2f/classGui_1_1MainWindow.html#adc82dc82e0038c9275aad7370b7007f7).

## ◆ getImportFilters() [1/2]

std::map< std::string, std::string > Application::getImportFilters  | ( | const char *  | _Type_| ) |  const  
---|---|---|---|---|---  
  
Return the import filters with modules of a given filetype.

Referenced by
[StdCmdOpen::activated()](../../d8/d6a/classStdCmdOpen.html#a9c9f69468076298c2a265906b3594a9d),
[StdCmdImport::activated()](../../d5/d4f/classStdCmdImport.html#a7ac453df0ea7389aa72fe651020ec1d4),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
and
[Gui::SelectModule::importHandler()](../../d6/d0e/classGui_1_1SelectModule.html#a15ea1522b5f3d6a78ae7d58a70b12cac).

## ◆ getImportFilters() [2/2]

std::map< std::string, std::string > Application::getImportFilters  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Return a list of all import filters.

## ◆ getImportModules() [1/2]

std::vector< std::string > Application::getImportModules  | ( | | ) |  const  
---|---|---|---|---  
  
Return a list of all modules.

## ◆ getImportModules() [2/2]

std::vector< std::string > Application::getImportModules  | ( | const char *  | _Type_| ) |  const  
---|---|---|---|---|---  
  
Return a list of modules that support the given filetype.

Referenced by
[Gui::MainWindow::loadUrls()](../../d5/d2f/classGui_1_1MainWindow.html#ac49add8806641195abfd2d92d738fb35),
[processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
and
[Gui::Application::sLoadFile()](../../d9/da8/classGui_1_1Application.html#ac274116543bbd50d4cd21c20f69799ec).

## ◆ getImportTypes() [1/2]

std::vector< std::string > Application::getImportTypes  | ( | const char *  | _Module_| ) |  const  
---|---|---|---|---|---  
  
Return a list of filetypes that are supported by a module.

Referenced by
[StdCmdOpen::activated()](../../d8/d6a/classStdCmdOpen.html#a9c9f69468076298c2a265906b3594a9d),
and
[StdCmdImport::activated()](../../d5/d4f/classStdCmdImport.html#a7ac453df0ea7389aa72fe651020ec1d4).

## ◆ getImportTypes() [2/2]

std::vector< std::string > Application::getImportTypes  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Return a list of all filetypes.

## ◆ getLibraryDir()

| std::string Application::getLibraryDir  | ( | | ) |   
---|---|---|---|---  
static  
  
## ◆ getLinksTo()

std::set< [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * > Application::getLinksTo  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _options_ ,   
|  | [int](../../d1/da0/classint.html) | _maxCount_ = `0`  
| ) | |  const  
  
Return the links to a given object.

Parameters

     obj| the linked object. If NULL, then all links are returned.   
---|---  
option|  
  
See also

    [App::GetLinkOption](../../dd/dc2/namespaceApp.html#ace2f0a252fd455b93b75461d2642330c)

Parameters

     maxCount| limit the number of links returned, 0 means no limit   
---|---  
  
Referenced by
[hasLinksTo()](../../da/dbf/classApp_1_1Application.html#aa4f4f5ff098b353d7b984e79e7760333).

## ◆ GetParameterGroupByPath()

[Base::Reference](../../df/dbe/classBase_1_1Reference.html)< [ParameterGrp](../../d4/d97/classParameterGrp.html) > Application::GetParameterGroupByPath  | ( | const char *  | _sName_| ) |   
---|---|---|---|---|---  
  
Gets a parameter group by a full qualified path It's an easy method to get a
group:

// getting standard parameter

[ParameterGrp::handle](../../df/dbe/classBase_1_1Reference.html) hGrp =
[App::GetApplication](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4
"Singleton getter of the
Application.")().[GetParameterGroupByPath](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202
"Gets a parameter group by a full qualified path It's an easy method to get a
group:")("User parameter:BaseApp/Preferences/Mod/Raytracing");

std::string cDir =
hGrp->[GetASCII](../../d4/d97/classParameterGrp.html#a5c579b580966bb5ddb8d07df2da9bc9c
"read a string values")("ProjectPath", "");

std::string cCameraName =
hGrp->[GetASCII](../../d4/d97/classParameterGrp.html#a5c579b580966bb5ddb8d07df2da9bc9c
"read a string values")("CameraName", "TempCamera.inc");

Referenced by
[Gui::Dialog::DlgCheckableMessageBox::accept()](../../d0/d87/classGui_1_1Dialog_1_1DlgCheckableMessageBox.html#a2feb2580a89d4004efb978cc96042de1),
[Gui::Dialog::DlgAddProperty::accept()](../../d3/d89/classGui_1_1Dialog_1_1DlgAddProperty.html#abec1eb0c6613b0f93b760bac73a92f9d),
[Gui::TaskCSysDragger::accept()](../../d2/dff/classGui_1_1TaskCSysDragger.html#ad513cbcf32b69dc11ee35b96cc6a2a64),
[Gui::MacroCommand::activated()](../../dc/d65/classGui_1_1MacroCommand.html#a3e9f3632b6f802aff70a6fa7d55c4ae5),
[StdCmdNew::activated()](../../de/d84/classStdCmdNew.html#ae3eaf48d823742fb35168adb3782e10e),
[StdCmdOnlineHelpWebsite::activated()](../../d4/deb/classStdCmdOnlineHelpWebsite.html#a268524af31ba69a4d5fa17cbe97b540e),
[StdCmdFreeCADDonation::activated()](../../df/d75/classStdCmdFreeCADDonation.html#a37bb706a588e398582f072936657c101),
[StdCmdFreeCADWebsite::activated()](../../d1/dbf/classStdCmdFreeCADWebsite.html#a811f6ab69e70ecd31a0cc9ea4ca5b357),
[StdCmdFreeCADUserHub::activated()](../../d8/d7b/classStdCmdFreeCADUserHub.html#aa2252487d5a42f523e1e754f9522dc8b),
[StdCmdFreeCADPowerUserHub::activated()](../../de/ddc/classStdCmdFreeCADPowerUserHub.html#a3487025baa2320871c16b57a259e9fd4),
[StdCmdFreeCADForum::activated()](../../d7/dc7/classStdCmdFreeCADForum.html#a971e9a86cc67c715fc2512617526164d),
[StdCmdFreeCADFAQ::activated()](../../db/de1/classStdCmdFreeCADFAQ.html#ad329f82fae81e6fe87cc985676cf32c1),
[StdCmdReportBug::activated()](../../d2/d08/classStdCmdReportBug.html#a25057718f0c6c0c070677a3eb643146f),
[StdCmdUserEditMode::activated()](../../df/dc4/classStdCmdUserEditMode.html#aeccc0e148478ec602547c2a42d805603),
[StdCmdViewHome::activated()](../../d1/dbe/classStdCmdViewHome.html#af90d22dbd4e4b6d3882f22901111a268),
[StdViewScreenShot::activated()](../../d9/da6/classStdViewScreenShot.html#a4229e4b93ce96f603dbfb3cdee194091),
[Gui::StdCmdDownloadOnlineHelp::activated()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#a29c4d53cfdd555b2a313eaa38cfa18be),
[CmdSketcherConstrainHorizontal::activated()](../../d4/dd5/classCmdSketcherConstrainHorizontal.html#adc766562bb486afb5941fc9bade87c59),
[CmdSketcherConstrainVertical::activated()](../../d7/d37/classCmdSketcherConstrainVertical.html#a0f174c055305b510bc2b3ce16eb6e80b),
[CmdSketcherConstrainLock::activated()](../../d9/dc2/classCmdSketcherConstrainLock.html#a337b578fd38e4359b3177138a91a9162),
[CmdSketcherConstrainBlock::activated()](../../d9/d19/classCmdSketcherConstrainBlock.html#a9aae799a29f3aac8783c1f99d1ebb21e),
[CmdSketcherConstrainCoincident::activated()](../../d0/d76/classCmdSketcherConstrainCoincident.html#a52a709fffac7be283b7b50f8687e8602),
[CmdSketcherConstrainDistance::activated()](../../d4/de5/classCmdSketcherConstrainDistance.html#a24031613fd513a79165dfec1d75d6ecb),
[CmdSketcherConstrainPointOnObject::activated()](../../d2/d39/classCmdSketcherConstrainPointOnObject.html#aa6f7ed1adb19f60b65703fafe91fdda9),
[CmdSketcherConstrainDistanceX::activated()](../../de/d7a/classCmdSketcherConstrainDistanceX.html#a175608d3c6099fc7504de3b5641a01c0),
[CmdSketcherConstrainDistanceY::activated()](../../da/d3d/classCmdSketcherConstrainDistanceY.html#a59b776e3be604ff1686d112c0f82334b),
[CmdSketcherConstrainParallel::activated()](../../d3/df0/classCmdSketcherConstrainParallel.html#a4c2b4c186452210ed3e69fb1c5f1afe6),
[CmdSketcherConstrainPerpendicular::activated()](../../d6/df0/classCmdSketcherConstrainPerpendicular.html#ae4b39128a2a69168a71c214a6632f6fa),
[CmdSketcherConstrainTangent::activated()](../../d8/d80/classCmdSketcherConstrainTangent.html#a49b68ec579dfa3ac0410539e34096f90),
[CmdSketcherConstrainRadius::activated()](../../d2/d16/classCmdSketcherConstrainRadius.html#a210220527e41b3ad828269b80a359354),
[CmdSketcherConstrainDiameter::activated()](../../da/dbe/classCmdSketcherConstrainDiameter.html#af5d04e1e2fa404f140625af1b917f186),
[CmdSketcherConstrainRadiam::activated()](../../d6/d18/classCmdSketcherConstrainRadiam.html#aee6c0c85caaecf9e7bcd99dff1efd6bc),
[CmdSketcherConstrainAngle::activated()](../../dc/dd6/classCmdSketcherConstrainAngle.html#a0d48a74c0960a5a240c1a39137f070a3),
[CmdSketcherConstrainEqual::activated()](../../de/dbe/classCmdSketcherConstrainEqual.html#ac247e0d1e55a27e0e40c204965f758be),
[CmdSketcherConstrainSymmetric::activated()](../../d5/d1d/classCmdSketcherConstrainSymmetric.html#afc33b5d3e672956b47801982de4611ef),
[Gui::Application::activateWorkbench()](../../d9/da8/classGui_1_1Application.html#ac3b3b8a91ba204c6180dab0dccc1a6d8),
[Gui::MainWindow::activateWorkbench()](../../d5/d2f/classGui_1_1MainWindow.html#ab24a7f3051844c6a244c10d2740186af),
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
[Gui::RecentFilesAction::appendFile()](../../d0/d17/classGui_1_1RecentFilesAction.html#a14d0d42121986c2a14babf830504326f),
[Gui::RecentMacrosAction::appendFile()](../../d2/df7/classGui_1_1RecentMacrosAction.html#ae1d2230890f6029a2eed3aaef4840c0c),
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[CmdSketcherConstrainLock::applyConstraint()](../../d9/dc2/classCmdSketcherConstrainLock.html#aa27c938f88973099b74d9474476d4254),
[Gui::NS::AwaitingMoveState::AwaitingMoveState()](../../d2/d54/classGui_1_1NS_1_1AwaitingMoveState.html#a61493dec20c2ae2a95a4fd6424ac9dac),
[Cloud::Module::cloudSave()](../../d9/d80/classCloud_1_1Module.html#a6849376c6a9d04c93cd195d3c6bd9f71),
[StdCmdUserEditMode::createAction()](../../df/dc4/classStdCmdUserEditMode.html#a9a04dfe92a1d8532aac74d357d1554a0),
[PartGui::ViewProvider2DObjectGrid::createGrid()](../../d9/d42/classPartGui_1_1ViewProvider2DObjectGrid.html#a6872b82ce1aa46b6532e864681e262ae),
[Gui::CreateViewStdCommands()](../../d9/dad/namespaceGui.html#ab5e7782b94bb96ba8a98e08d74956107),
[SketcherGui::CurveConverter::CurveConverter()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#aedc47aa90240b39482d98c65c03197b3),
[Gui::View3DInventor::customEvent()](../../da/d75/classGui_1_1View3DInventor.html#aaecd3db84b1c65974ddf1bc692d25686),
[ConstraintItem::data()](../../d3/d0f/classConstraintItem.html#a58e0ecc1824934b77e25bc0b319b6c51),
[Gui::ViewProviderOrigin::defaultSize()](../../d5/d7f/classGui_1_1ViewProviderOrigin.html#adca2fcce2ef313802ec2cec78e63b8cd),
[Gui::Dialog::DlgAddProperty::DlgAddProperty()](../../d3/d89/classGui_1_1Dialog_1_1DlgAddProperty.html#a54a1e5a0ea475b11a47a9a7ba164f89f),
[MeshGui::DlgEvaluateMeshImp::DlgEvaluateMeshImp()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a227fd7deeb9c1d8d1bfc3df0fdf04ebe),
[Gui::Dialog::DlgExpressionInput::DlgExpressionInput()](../../d5/d26/classGui_1_1Dialog_1_1DlgExpressionInput.html#aa41178b425873712e0c599430c5e79b8),
[PartGui::DlgSettings3DViewPart::DlgSettings3DViewPart()](../../d2/d45/classPartGui_1_1DlgSettings3DViewPart.html#ac8882cf73baa4e10a00d60743c83fc94),
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
[App::Document::Document()](../../d8/d3e/classApp_1_1Document.html#a82834e591e305efb55dcf48d89ae246b),
[FemGui::ViewProviderFemPostObject::doubleClicked()](../../db/d73/classFemGui_1_1ViewProviderFemPostObject.html#abe833e8299e59bd079273f4c30af4067),
[DraftUtils::DraftDxfRead::DraftDxfRead()](../../d2/d66/classDraftUtils_1_1DraftDxfRead.html#af78eba53c556dfeb7713c9dd026dc7ac),
[DrawingGui::DrawingView::DrawingView()](../../da/d65/classDrawingGui_1_1DrawingView.html#a19edc61e67a465cb0d4ceefd9c1b178d),
[NaviCubeImplementation::drawNaviCube()](../../df/dc9/classNaviCubeImplementation.html#aa3cad37e2c46d6c4e0793b2a79deb41f),
[Gui::ElementColors::ElementColors()](../../db/d21/classGui_1_1ElementColors.html#a7d0d5836a9361c145408b75cf8b0b33c),
[Gui::GraphvizView::exportGraph()](../../dd/d86/classGui_1_1GraphvizView.html#ae5fbd071a327ae9c5f54a9d4e5aa2f3c),
[App::Document::exportGraphviz()](../../d8/d3e/classApp_1_1Document.html#a8fcd387d89a13b87dabc05187bfd5122),
[Import::ExportOCAF2::ExportOCAF2()](../../d1/d6e/classImport_1_1ExportOCAF2.html#a3b2589d3096f2857273bd28d202bc8c5),
[Gui::Application::exportTo()](../../d9/da8/classGui_1_1Application.html#a276a5171d44ac9162f39a69fc92f137f),
[MeshGui::ViewProviderMesh::faceInfoCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#ae3d2f360b9f432962521c1bb1b77dd98),
[FemGui::FemSettings::FemSettings()](../../d6/da2/classFemGui_1_1FemSettings.html#a730ba2d9a2451445be745e58626e37fb),
[Gui::GestureNavigationStyle::GestureNavigationStyle()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#a9f197c9d7a89cb591fc817412d25bfec),
[Gui::NS::GestureState::GestureState()](../../db/d04/classGui_1_1NS_1_1GestureState.html#ad0ae304b135bd8fe413df565c4448087),
[Gui::ViewProviderGeometryObject::getBoundColor()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a43255dc03cfdd04da7ca9aaa18b849c4),
[PathGui::ViewProviderPath::getBoundColor()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a98a3ef4085a9babf25db6f74aa95bdc0),
[Spreadsheet::Sheet::getCharsFromPrefs()](../../d0/da8/classSpreadsheet_1_1Sheet.html#a144aba1b77f58bcd343d16c12d4df49c),
[SketcherGui::DrawSketchHandler::getCrosshairColor()](../../d9/d8a/classSketcherGui_1_1DrawSketchHandler.html#aee5f939e05c1c004e3b9283eb61d2f4f),
[Path::Toolpath::getCycleTime()](../../d6/d0c/classPath_1_1Toolpath.html#a6adb7debbb92c2d09e8b280b00003696),
[Gui::View3DInventorViewer::getInternalTextureFormat()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a882176ea9124318dd3ce496fc7b17d8e),
[TechDrawGui::QGVPage::getNavStyleParameter()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#a570eac4558e88d4b0ec3240f8ed038b9),
[Gui::View3DInventorViewer::getNumSamples()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a6050256d66524b3d32df9a9cce727924),
[Part::Feature::getSubObject()](../../d7/d7e/classPart_1_1Feature.html#adf8612028b19407896b5ba0e1fab0d5d),
[Gui::GraphicsView3D::GraphicsView3D()](../../df/d0b/classGui_1_1GraphicsView3D.html#ad33d0c8f32b37ee2eff8e67494289edc),
[Gui::GraphvizView::GraphvizView()](../../dd/d86/classGui_1_1GraphvizView.html#a1e46d2a16a77346e54d76e9b8db662f7),
[ImageGui::ImageView::ImageView()](../../d3/d75/classImageGui_1_1ImageView.html#aecd00c2699b113e2128509f5b96b49af),
[Gui::Application::importFrom()](../../d9/da8/classGui_1_1Application.html#a8d8a9ad9495f79b4813c2b97d2e33e86),
[Import::ImportOCAF2::ImportOCAF2()](../../d9/ddd/classImport_1_1ImportOCAF2.html#a1778a18213d37ff08892e030cb9cbd2c),
[Gui::NavigationStyle::initialize()](../../d2/d1c/classGui_1_1NavigationStyle.html#ae9a47b566e2c72e5b474475d301d2e5c),
[TechDrawGui::QGVNavStyle::initialize()](../../dc/d63/classTechDrawGui_1_1QGVNavStyle.html#a3662e8d7a0946306e47d2ea776aa2ca8),
[Inspection::InspectActualShape::InspectActualShape()](../../d8/d95/classInspection_1_1InspectActualShape.html#a56bdfb58a9bb2d1912bb223440fecfb9),
[Gui::ExpressionParameter::isCaseSensitive()](../../d2/d65/classGui_1_1ExpressionParameter.html#a528c43fcabf892dedbf8bab3265fd287),
[Gui::ExpressionParameter::isExactMatch()](../../d2/d65/classGui_1_1ExpressionParameter.html#a7bf15544e79409f20762d0df6ef6ab58),
[Gui::PreferencePackManager::isVisible()](../../d9/d11/classGui_1_1PreferencePackManager.html#a376d5716cb006d990ab52034998d2a56),
[Gui::MacroCommand::load()](../../dc/d65/classGui_1_1MacroCommand.html#a38220fcdafbccc6ff4257e1f9bf12173),
[Gui::Dialog::DlgWorkbenchesImp::load_disabled_workbenches()](../../d5/dc3/classGui_1_1Dialog_1_1DlgWorkbenchesImp.html#a3e1e793eacef9c26b22110d514e75842),
[Gui::Dialog::DlgWorkbenchesImp::load_enabled_workbenches()](../../d5/dc3/classGui_1_1Dialog_1_1DlgWorkbenchesImp.html#a69dbee07a043de2bd8ff4a989c16cce6),
[SketcherGui::SketcherGeneralWidget::loadOrderingOrder()](../../da/d36/classSketcherGui_1_1SketcherGeneralWidget.html#abaccb1953066ce56215206edfa8ea3d7),
[PartGui::ViewProviderPartExt::loadParameter()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#ac9b18640b083f65180c44c787ed4b240),
[Gui::Dialog::DlgGeneralImp::loadSettings()](../../df/ddc/classGui_1_1Dialog_1_1DlgGeneralImp.html#af5eac73c627e99f23296d0f7f2c34ae8),
[Gui::Dialog::DlgSettings3DViewImp::loadSettings()](../../df/d5c/classGui_1_1Dialog_1_1DlgSettings3DViewImp.html#a574045628488a5e5c1f565ebf2eebeec),
[Gui::Dialog::DlgSettingsLazyLoadedImp::loadSettings()](../../de/d4f/classGui_1_1Dialog_1_1DlgSettingsLazyLoadedImp.html#ab0f7ae19d7b6b69a0f08109c559c9c06),
[Gui::Dialog::DlgSettingsNavigation::loadSettings()](../../d4/de0/classGui_1_1Dialog_1_1DlgSettingsNavigation.html#a535eb9332f21990bd1099737af28e64e),
[Gui::Dialog::DlgSettingsSelection::loadSettings()](../../d4/d5d/classGui_1_1Dialog_1_1DlgSettingsSelection.html#a9b86969c8e6fa23be753da78aac60c03),
[Gui::Dialog::DlgSettingsUnitsImp::loadSettings()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#a7127945a0e61f55905a60f534f9aca72),
[FemGui::DlgSettingsFemCcxImp::loadSettings()](../../d2/d94/classFemGui_1_1DlgSettingsFemCcxImp.html#a5a3abd11b879a224f64bc3a136334778),
[FemGui::DlgSettingsFemExportAbaqusImp::loadSettings()](../../db/d26/classFemGui_1_1DlgSettingsFemExportAbaqusImp.html#a539c0e78fac3f6a6205b8f68c1b3e956),
[FemGui::DlgSettingsFemInOutVtkImp::loadSettings()](../../d6/d41/classFemGui_1_1DlgSettingsFemInOutVtkImp.html#a258a296199b758be3ad7adb0d708d6e4),
[FemGui::DlgSettingsFemZ88Imp::loadSettings()](../../d0/d44/classFemGui_1_1DlgSettingsFemZ88Imp.html#aaa7449040a132a88d74a7fd62607864d),
[InspectionGui::VisualInspection::loadSettings()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#a81be250d84f75296fbe4a4a26272f5f9),
[MeshGui::DlgSettingsImportExport::loadSettings()](../../d4/d21/classMeshGui_1_1DlgSettingsImportExport.html#ac86b335632ce0ebd73b0994e6e59b491),
[SketcherGui::SketcherSettingsDisplay::loadSettings()](../../d5/d61/classSketcherGui_1_1SketcherSettingsDisplay.html#a2526ebf1418c7eb5364a58ce570a53bc),
[SpreadsheetGui::DlgSettingsImp::loadSettings()](../../d0/d5b/classSpreadsheetGui_1_1DlgSettingsImp.html#a51fbec6882ed7386443273d2f8888a14),
[StartGui::DlgStartPreferencesImp::loadSettings()](../../d9/d5e/classStartGui_1_1DlgStartPreferencesImp.html#a83a726bf6af6dbeb1e1734ee2c93f7ca),
[Gui::MacroManager::MacroManager()](../../d8/dc6/classGui_1_1MacroManager.html#a8edd22e269321504a4cbc24abb9e0043),
[NaviCubeImplementation::NaviCubeImplementation()](../../df/dc9/classNaviCubeImplementation.html#acee51772b372c1463da029f32da4ff12),
[Gui::Dialog::DlgMacroExecuteImp::on_createButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a47eb382b837c65c8e46d41158aeb0b80),
[Gui::Dialog::DlgMacroExecuteImp::on_duplicateButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#ae0df9f58ffc728ac2e5739c615183c54),
[Gui::Dialog::DlgMacroExecuteImp::on_renameButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a1a9680d49cf27716db1db489c384456e),
[Gui::Dialog::DlgMacroExecuteImp::on_toolbarButton_clicked()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#a1607697dc3b346332ce658cdc277df6e),
[SketcherGui::TaskSketcherConstraints::on_visibilityButton_trackingaction_changed()](../../db/d43/classSketcherGui_1_1TaskSketcherConstraints.html#aa06f1bf71fe9212649eee1baf167acc8),
[PathGui::ViewProviderPath::onChanged()](../../db/d31/classPathGui_1_1ViewProviderPath.html#ac6bc90e9c178290fc1ecf742e31ac167),
[PartDesignGui::ViewProviderSubShapeBinder::onChanged()](../../d1/da6/classPartDesignGui_1_1ViewProviderSubShapeBinder.html#acfc66960894369715fed17de459c679d),
[Gui::GestureNavigationStyle::onRollGesture()](../../dd/df8/classGui_1_1GestureNavigationStyle.html#aea1942b7bbfc657cbfe2ae892811b802),
[Gui::TaskCSysDragger::open()](../../d2/dff/classGui_1_1TaskCSysDragger.html#a733509ee8c725c67aac59bb4945f4978),
[Gui::Application::open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728),
[SketcherGui::DrawSketchHandlerLineSet::pressButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#aeee22456b9d6c86500b37dca09b6bca0),
[TechDrawGui::QGVPage::Private::Private()](../../d8/d45/classQGVPage_1_1Private.html#a1a30d738251acaf2c30286e03ee87ab4),
[Gui::RecentFilesAction::Private::Private()](../../de/de4/classRecentFilesAction_1_1Private.html#a98620a9fe8680c05d704e96b252eae10),
[SketcherGui::DrawSketchHandlerBSpline::quit()](../../d7/d7f/classSketcherGui_1_1DrawSketchHandlerBSpline.html#a8b5fd97ce504c7b619c37613dd3af747),
[SketcherGui::DrawSketchHandlerLineSet::quit()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a7d171bbac7b931fdc150ed95ae2f4ec4),
[App::Document::recompute()](../../d8/d3e/classApp_1_1Document.html#a3b2d7f9cc354b48ab8f0373c6d37c73b),
[Gui::Dialog::DlgCheckableMessageBox::reject()](../../d0/d87/classGui_1_1Dialog_1_1DlgCheckableMessageBox.html#a552381ce14d73c84342f0d6130958e64),
[SketcherGui::TaskDlgEditSketch::reject()](../../d3/dcd/classSketcherGui_1_1TaskDlgEditSketch.html#a6f218dd08d57e05911ecd833c4219e16),
[DrawSketchHandlerBSplineInsertKnot::releaseButton()](../../d2/df2/classDrawSketchHandlerBSplineInsertKnot.html#ad1bd5e637ff894fb66b09fcf914bd49b),
[SketcherGui::DrawSketchHandlerArc::releaseButton()](../../d4/d83/classSketcherGui_1_1DrawSketchHandlerArc.html#ab283932a602b4b135259d8ec565cbe1a),
[SketcherGui::DrawSketchHandler3PointArc::releaseButton()](../../d3/d84/classSketcherGui_1_1DrawSketchHandler3PointArc.html#ad9123e0df6dfcbca72fb0a45e63bb822),
[SketcherGui::DrawSketchHandlerArcOfEllipse::releaseButton()](../../d4/d0e/classSketcherGui_1_1DrawSketchHandlerArcOfEllipse.html#ae0f1ecd2fac7f0ee7d7b57610009dc1d),
[SketcherGui::DrawSketchHandlerCircle::releaseButton()](../../db/daa/classSketcherGui_1_1DrawSketchHandlerCircle.html#aac71ee5f645be6cc4b0ac8cb49777b67),
[SketcherGui::DrawSketchHandler3PointCircle::releaseButton()](../../db/dbc/classSketcherGui_1_1DrawSketchHandler3PointCircle.html#a3393a6d51aed0b745e44e60f55e4c96a),
[SketcherGui::DrawSketchHandlerEllipse::releaseButton()](../../d7/daa/classSketcherGui_1_1DrawSketchHandlerEllipse.html#a10c67cd8401d37015b58a5d7b0f95507),
[SketcherGui::DrawSketchHandlerExtend::releaseButton()](../../db/dc7/classSketcherGui_1_1DrawSketchHandlerExtend.html#a3e947849d6dc89b7f93e87a1ebd9b160),
[SketcherGui::DrawSketchHandlerLine::releaseButton()](../../dd/d65/classSketcherGui_1_1DrawSketchHandlerLine.html#a9ee080f22c2c3bf2f6e826f4cc36f91a),
[SketcherGui::DrawSketchHandlerLineSet::releaseButton()](../../d9/db3/classSketcherGui_1_1DrawSketchHandlerLineSet.html#a040aa2a8cc28c52db550115a16ef693c),
[SketcherGui::DrawSketchHandlerPoint::releaseButton()](../../df/da1/classSketcherGui_1_1DrawSketchHandlerPoint.html#a733f6bcea854c88e77f73e0a1b377f53),
[SketcherGui::DrawSketchHandlerRegularPolygon::releaseButton()](../../db/d5f/classSketcherGui_1_1DrawSketchHandlerRegularPolygon.html#a676a473ddbfd8fd7f2e214ffc43352b5),
[SketcherGui::DrawSketchHandlerBox::releaseButton()](../../dc/d09/classSketcherGui_1_1DrawSketchHandlerBox.html#a1ee8ff08af23b1ad1d9fd48170889315),
[SketcherGui::DrawSketchHandlerOblong::releaseButton()](../../dc/dac/classSketcherGui_1_1DrawSketchHandlerOblong.html#a8e2b792d2ce80795c2808e6276bdd6dc),
[SketcherGui::DrawSketchHandlerSlot::releaseButton()](../../d5/dd5/classSketcherGui_1_1DrawSketchHandlerSlot.html#aa93e01a33ed89216e53c3c8886b21a35),
[SketcherGui::DrawSketchHandlerArcOfHyperbola::releaseButton()](../../d0/dcd/classSketcherGui_1_1DrawSketchHandlerArcOfHyperbola.html#a691e8ff0661b5c0f36bd5ad8c8fe8fa3),
[SketcherGui::DrawSketchHandlerArcOfParabola::releaseButton()](../../d3/dd4/classSketcherGui_1_1DrawSketchHandlerArcOfParabola.html#a17a69b223beded8cad2a7319ef4cffe6),
[Part::PropertyPartShape::RestoreDocFile()](../../d7/d28/classPart_1_1PropertyPartShape.html#a4863dc4e56fd41546d7cae6422435f4f),
[Gui::MDIView::restorePrinterSettings()](../../df/d23/classGui_1_1MDIView.html#a135ed4509fd3d0faff9e3792a4b2709c),
[Gui::GraphvizWorker::run()](../../d3/d6c/classGui_1_1GraphvizWorker.html#a4036bf725d01af1aaa1c0a86dc5a1717),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::MacroCommand::save()](../../dc/d65/classGui_1_1MacroCommand.html#a07b15a91f8c947d8e43c778b96fc29be),
[Gui::Document::Save()](../../de/d4e/classGui_1_1Document.html#a17dba40a2ef0e606900ad09fadca20f5),
[App::Document::save()](../../d8/d3e/classApp_1_1Document.html#a8e41f8db87626e8e86763ab704d8424c),
[Part::PropertyPartShape::SaveDocFile()](../../d7/d28/classPart_1_1PropertyPartShape.html#a0a5d9ad2a3ed87aa769ab8e36f51d2f2),
[Gui::AutoSaver::saveDocument()](../../d6/d8b/classGui_1_1AutoSaver.html#a6820c336cb0be4164736f27729fed059),
[SketcherGui::SketcherGeneralWidget::saveOrderingOrder()](../../da/d36/classSketcherGui_1_1SketcherGeneralWidget.html#ac8b4725880d37ac8803ab2025ae04756),
[MeshPartGui::Tessellation::saveParameters()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#a950e7955e55513fd72059876c1ab6537),
[Gui::View3DInventorViewer::savePicture()](../../d5/d29/classGui_1_1View3DInventorViewer.html#a2664c98220d9380bf3fdd5f4d50bc77a),
[Gui::MDIView::savePrinterSettings()](../../df/d23/classGui_1_1MDIView.html#a6012eee5639b188ffff2dae80e339f3d),
[Gui::Dialog::DlgGeneralImp::saveSettings()](../../df/ddc/classGui_1_1Dialog_1_1DlgGeneralImp.html#a054778b82a6ff33f124c108794c91406),
[Gui::Dialog::DlgSettings3DViewImp::saveSettings()](../../df/d5c/classGui_1_1Dialog_1_1DlgSettings3DViewImp.html#ac07c76a16e7ab82abb8e77404144b69e),
[Gui::Dialog::DlgSettingsLazyLoadedImp::saveSettings()](../../de/d4f/classGui_1_1Dialog_1_1DlgSettingsLazyLoadedImp.html#ada42a820640d42d6e46729c1b73d9bac),
[Gui::Dialog::DlgSettingsNavigation::saveSettings()](../../d4/de0/classGui_1_1Dialog_1_1DlgSettingsNavigation.html#a168e9a3b3629b885d7ffa64121c1dd09),
[Gui::Dialog::DlgSettingsSelection::saveSettings()](../../d4/d5d/classGui_1_1Dialog_1_1DlgSettingsSelection.html#a98f8de4617916643583919e3fd818203),
[Gui::Dialog::DlgSettingsUnitsImp::saveSettings()](../../d0/df7/classGui_1_1Dialog_1_1DlgSettingsUnitsImp.html#a8d256a71443e4ab9de3df9e072c2f67e),
[FemGui::DlgSettingsFemCcxImp::saveSettings()](../../d2/d94/classFemGui_1_1DlgSettingsFemCcxImp.html#ae607c1620f41abfc9487040e2473f72b),
[FemGui::DlgSettingsFemExportAbaqusImp::saveSettings()](../../db/d26/classFemGui_1_1DlgSettingsFemExportAbaqusImp.html#a63a7a2d9e7ded9d35a0274f27d2c47d7),
[FemGui::DlgSettingsFemInOutVtkImp::saveSettings()](../../d6/d41/classFemGui_1_1DlgSettingsFemInOutVtkImp.html#a810bfcf32f44db4aa7abd2e4bd58c456),
[FemGui::DlgSettingsFemZ88Imp::saveSettings()](../../d0/d44/classFemGui_1_1DlgSettingsFemZ88Imp.html#acdfb03628db3f2f9f88b52e1d055b28e),
[InspectionGui::VisualInspection::saveSettings()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#a9967250b51cfede16509f732267a3a05),
[MeshGui::DlgSettingsImportExport::saveSettings()](../../d4/d21/classMeshGui_1_1DlgSettingsImportExport.html#aedf19f8cce93c37815ffefc51672fb61),
[SketcherGui::SketcherSettingsDisplay::saveSettings()](../../d5/d61/classSketcherGui_1_1SketcherSettingsDisplay.html#a04418f6bfdcbae598016136aea871b37),
[SpreadsheetGui::DlgSettingsImp::saveSettings()](../../d0/d5b/classSpreadsheetGui_1_1DlgSettingsImp.html#afdbc7410a997a233169d609bfb229b9a),
[StartGui::DlgStartPreferencesImp::saveSettings()](../../d9/d5e/classStartGui_1_1DlgStartPreferencesImp.html#a034f5c13b680f49515b8c4024410a4e0),
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d),
[Gui::SelectionSingleton::selStackPush()](../../d4/dca/classGui_1_1SelectionSingleton.html#a32204ef30c2905001311162bedf9683b),
[Gui::WindowParameter::setGroupName()](../../d4/dcc/classGui_1_1WindowParameter.html#a5826bc7e6fda502ba30fcaa7612f6ac6),
[Gui::DocumentObjectItem::setHighlight()](../../d1/d4d/classGui_1_1DocumentObjectItem.html#a1b3b74393af139fe9c6e19adf547a0a5),
[Import::ImpExpDxfRead::setOptions()](../../d5/d55/classImport_1_1ImpExpDxfRead.html#a7d7496f6f28b4cae569ea398a3caf0aa),
[Import::ImpExpDxfWrite::setOptions()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a5b5bdf5be5fb367ff4b83701eb1ee520),
[Gui::StatefulLabel::setParameterGroup()](../../d8/d55/classGui_1_1StatefulLabel.html#a993db8f4a3b78c34b628eb4ee7c66b1e),
[Gui::InputField::setParamGrpPath()](../../da/dfa/classGui_1_1InputField.html#a947ef07166a61c3f7f8e33373255dd8f),
[Gui::Dialog::DlgCheckableMessageBox::setPrefEntry()](../../d0/d87/classGui_1_1Dialog_1_1DlgCheckableMessageBox.html#abf34f61db90f44e8c086590e7c3cc0ab),
[Gui::Dialog::DlgCustomKeyboardImp::setShortcutOfCurrentAction()](../../df/d9c/classGui_1_1Dialog_1_1DlgCustomKeyboardImp.html#a8b3bbca8079e57e54ff511a79263ad79),
[Gui::AbstractSplitView::setupSettings()](../../d1/d0b/classGui_1_1AbstractSplitView.html#a76ecde0106d10edd50dff4f8bf8c448d),
[Gui::Application::sGetMarkerIndex()](../../d9/da8/classGui_1_1Application.html#ac0d20b8eb675a3b6be74823f114dd3f7),
[SpreadsheetGui::SheetModel::SheetModel()](../../d0/d8b/classSpreadsheetGui_1_1SheetModel.html#aca374b8f387985ec3756f86f3cac2c45),
[Gui::Dialog::DlgPreferencePackManagementImp::showAddonManager()](../../d0/d65/classGui_1_1Dialog_1_1DlgPreferencePackManagementImp.html#a9c097069536d1d5f1af0cd939e3afa96),
[Gui::MainWindow::showDocumentation()](../../d5/d2f/classGui_1_1MainWindow.html#ab6d315d78f9057c6b070d99659230999),
[Gui::Dialog::DlgCheckableMessageBox::showMessage()](../../d0/d87/classGui_1_1Dialog_1_1DlgCheckableMessageBox.html#addb852e97624672dfef73e541d14fd1a),
[PartDesignGui::TaskHelixParameters::showPreview()](../../d1/d56/classPartDesignGui_1_1TaskHelixParameters.html#ae53892b6ae50a7deeea724ff4ae68da8),
[Gui::DocumentItem::slotInEdit()](../../df/d15/classGui_1_1DocumentItem.html#ad880ce9b26515b35a71c07cf38b61012),
[Gui::SplitView3DInventor::SplitView3DInventor()](../../da/d73/classGui_1_1SplitView3DInventor.html#ac6e97f0b7618f77a3a700db0c4ef9fc8),
[Gui::StatefulLabel::StatefulLabel()](../../d8/d55/classGui_1_1StatefulLabel.html#a9b627760a5b1c14738bc1dff671b62cf),
[StdCmdRefresh::StdCmdRefresh()](../../db/d0a/classStdCmdRefresh.html#a5b0fc256867be12f18e8094a981f5a05),
[SketcherGui::TaskDlgEditSketch::TaskDlgEditSketch()](../../d3/dcd/classSketcherGui_1_1TaskDlgEditSketch.html#a3ca9004fd45d10a7aec0d3e4d2e7fdf9),
[SketcherGui::TaskSketcherElements::TaskSketcherElements()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#a58295f4cd0ec5cf69b7c36cdf9c49e12),
[MeshPartGui::Tessellation::Tessellation()](../../d7/d65/classMeshPartGui_1_1Tessellation.html#aa719fb5ab9267b9897d641cec0cb2177),
[Gui::PreferencePackManager::toggleVisibility()](../../d9/d11/classGui_1_1PreferencePackManager.html#aa9f63fe5ef337a93dd3f68b25e1076fe),
[Gui::TreeParams::TreeParams()](../../d0/dc9/classGui_1_1TreeParams.html#a5295206bb6c787328f8f01fa04af7bba),
[SketcherGui::tryAutoRecompute()](../../d6/d44/namespaceSketcherGui.html#a02b71618e9dafc472091eadac35e6ff2),
[InspectionGui::ViewProviderInspection::updateData()](../../dc/db4/classInspectionGui_1_1ViewProviderInspection.html#ac5f772cc4c7e81322756730808d61239),
[SketcherGui::TaskSketcherSolverAdvanced::updateDefaultMethodParameters()](../../df/ddd/classSketcherGui_1_1TaskSketcherSolverAdvanced.html#ac37da4d8d5afa35c58c06d383bd803e3),
[SketcherGui::TaskSketcherSolverAdvanced::updateRedundantMethodParameters()](../../df/ddd/classSketcherGui_1_1TaskSketcherSolverAdvanced.html#a591f48eb94248472ce63493a493e7897),
[Gui::View3DInventor::View3DInventor()](../../da/d75/classGui_1_1View3DInventor.html#ac60eed69033bfadaa166619bc01f8956),
[Gui::View3DInventorPy::viewDefaultOrientation()](../../d3/df7/classGui_1_1View3DInventorPy.html#a05d613ada1896468d7fe16177560b184),
[Gui::ViewParams::ViewParams()](../../d3/d88/classGui_1_1ViewParams.html#a6d3fd098b5f3a3b421768c2130693e4e),
[Gui::ViewProviderAnnotation::ViewProviderAnnotation()](../../d3/d71/classGui_1_1ViewProviderAnnotation.html#ad25cbd6aa21673a4176f2dec681e1c8b),
[PartDesignGui::ViewProviderDatum::ViewProviderDatum()](../../d4/dc1/classPartDesignGui_1_1ViewProviderDatum.html#adf0685fe5a17533d5150eee8e625d03a),
[PartDesignGui::ViewProviderDatumCoordinateSystem::ViewProviderDatumCoordinateSystem()](../../d7/d4d/classPartDesignGui_1_1ViewProviderDatumCoordinateSystem.html#a53832f895c08903546a696bd6e667100),
[Gui::ViewProviderGeometryObject::ViewProviderGeometryObject()](../../db/d77/classGui_1_1ViewProviderGeometryObject.html#a2b9a89fc4a6101419f4783032d3edfcb),
[PartGui::ViewProviderPartExt::ViewProviderPartExt()](../../d6/d68/classPartGui_1_1ViewProviderPartExt.html#a23b298ac6903dab7daea05b120e34aed),
[PathGui::ViewProviderPath::ViewProviderPath()](../../db/d31/classPathGui_1_1ViewProviderPath.html#a28e01da414d201e60d2d8f9e39ae78bb),
[PartDesignGui::ViewProviderShapeBinder::ViewProviderShapeBinder()](../../d1/d70/classPartDesignGui_1_1ViewProviderShapeBinder.html#a530772439eebfaf7678a3442bb62fd31),
[Path::PathSegmentWalker::walk()](../../d0/d7b/classPath_1_1PathSegmentWalker.html#a2d2253be4424a16caf28ec136b658dc6),
[SandboxGui::Workbench::Workbench()](../../d2/db3/classSandboxGui_1_1Workbench.html#a052a62fb11c36380d04283bff6d47582),
[Fem::FemMesh::write()](../../d3/d2e/classFem_1_1FemMesh.html#aae76fd7da094c3497f08daafa044afc0),
[SketcherGui::CurveConverter::~CurveConverter()](../../d9/d49/classSketcherGui_1_1CurveConverter.html#ac4b31b0695f009bdc0e6464928d87c37),
[MeshGui::DlgEvaluateMeshImp::~DlgEvaluateMeshImp()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#aa8526e54d9a2899a144997c41b9bfe06),
[NaviCubeImplementation::~NaviCubeImplementation()](../../df/dc9/classNaviCubeImplementation.html#aa84bddf0834589682f482c0b30a753b1),
and
[SketcherGui::TaskSketcherElements::~TaskSketcherElements()](../../d0/d62/classSketcherGui_1_1TaskSketcherElements.html#aa0e3dd4f5f02d32c7d8fe6457331cc31).

## ◆ GetParameterSet()

[ParameterManager](../../db/daa/classParameterManager.html) * Application::GetParameterSet  | ( | const char *  | _sName_| ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Gui::RecentFilesAction::appendFile()](../../d0/d17/classGui_1_1RecentFilesAction.html#a14d0d42121986c2a14babf830504326f),
[Gui::RecentMacrosAction::appendFile()](../../d2/df7/classGui_1_1RecentMacrosAction.html#ae1d2230890f6029a2eed3aaef4840c0c),
[Gui::Dialog::DlgParameterImp::DlgParameterImp()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a43821f49385b7671bcef4e035a4e8ded),
[Gui::Dialog::DlgParameterImp::on_buttonSaveToDisk_clicked()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a16d6dfb8eac2ee5b7eed5766c002890e),
and
[Gui::Dialog::DlgParameterImp::onChangeParameterSet()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a5c3b0d0bc86b49af2db5dd89379c377f).

## ◆ GetParameterSetList()

const std::map< std::string, [ParameterManager](../../db/daa/classParameterManager.html) * > & Application::GetParameterSetList  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Referenced by
[Gui::Dialog::DlgParameterImp::DlgParameterImp()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a43821f49385b7671bcef4e035a4e8ded).

## ◆ getResourceDir()

| std::string Application::getResourceDir  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[RobotGui::Workbench::activated()](../../d9/dcb/classRobotGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced),
[TechDraw::Preferences::bitmapFill()](../../d6/dde/classTechDraw_1_1Preferences.html#aaa59c01070e04cb1f547cc0d0fca41b8),
[TechDraw::Preferences::defaultTemplate()](../../d6/dde/classTechDraw_1_1Preferences.html#aa2ba4e5c813143e90316673e9073e586),
[TechDraw::Preferences::defaultTemplateDir()](../../d6/dde/classTechDraw_1_1Preferences.html#abe38defbf2f6314b882b30707b5bde06),
[Drawing::FeaturePage::execute()](../../db/d0f/classDrawing_1_1FeaturePage.html#a627d1bb2272e95e3251b77aa74fa1059),
[TechDraw::DrawSVGTemplate::execute()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a2fc830b1c295c6c929676310ce001625),
[TechDraw::DrawSVGTemplate::getEditableTextsFromTemplate()](../../d4/ddb/classTechDraw_1_1DrawSVGTemplate.html#a5d4fd489066be062afb816f45960c214),
[Drawing::FeaturePage::getEditableTextsFromTemplate()](../../db/d0f/classDrawing_1_1FeaturePage.html#af1b06dab1d22245e410d1a251f5eda96),
[TechDraw::Preferences::lineGroupFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a9c538c5e2ad7c65962a5dd44dd26b17c),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[TechDraw::Preferences::patFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a603db0a17ac567dd7dc8b20fbe51c609),
[Gui::PreferencePackManager::PreferencePackManager()](../../d9/d11/classGui_1_1PreferencePackManager.html#abb2d4e9ce7887dacce75f880d0f14420),
[TechDraw::DrawTileWeld::prefSymbol()](../../d5/d3d/classTechDraw_1_1DrawTileWeld.html#a30af8983377cf0a69d228e6103e302aa),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[RaytracingGui::ViewProviderLux::setEdit()](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a559d010dd9902addb4de84170aac9f51),
[RaytracingGui::ViewProviderPovray::setEdit()](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a76685922c30f4f6a92a74fafcc800fa2),
[Import::ImpExpDxfWrite::setOptions()](../../dc/d2d/classImport_1_1ImpExpDxfWrite.html#a5b5bdf5be5fb367ff4b83701eb1ee520),
[TechDrawGui::SymbolChooser::setUiPrimary()](../../d2/d51/classTechDrawGui_1_1SymbolChooser.html#ab44a5314c19a15e46d509b1651901d83),
[Gui::Dialog::DlgPreferencePackManagementImp::showEvent()](../../d0/d65/classGui_1_1Dialog_1_1DlgPreferencePackManagementImp.html#a0ea7aeaec23e71117ce5413611e8e721),
[TechDraw::Preferences::svgFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a7948f1f445732b3f5720eaa35de03d8d),
[Gui::PreferencePackManager::templateFiles()](../../d9/d11/classGui_1_1PreferencePackManager.html#aef585677004289372394030ed5335213),
and
[TechDrawGui::PreferencesGui::weldingDirectory()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ae8f758711778daab1558370f25fa519f).

## ◆ GetSystemParameter()

[ParameterManager](../../db/daa/classParameterManager.html) & Application::GetSystemParameter  | ( | void  | | ) |   
---|---|---|---|---|---  
  
returns the system parameter

## ◆ getTempFileName()

| std::string Application::getTempFileName  | ( | const char *  | _FileName_ = `nullptr`| ) |   
---|---|---|---|---|---  
static  
  
References
[Base::FileInfo::getTempFileName()](../../dd/d34/classBase_1_1FileInfo.html#a8378231b746bc06c6d1e35ca68837b74),
and
[getTempPath()](../../da/dbf/classApp_1_1Application.html#a9d6fde1f997eed46a97428e42f655507).

Referenced by
[StdCmdDuplicateSelection::activated()](../../d4/d75/classStdCmdDuplicateSelection.html#a1ffe671eebc9f7e4c99740df06eaf0a9),
[App::Document::copyObject()](../../d8/d3e/classApp_1_1Document.html#ad932e5f34f7912d08b738238eba61aa0),
[Gui::MainWindow::createMimeDataFromSelection()](../../d5/d2f/classGui_1_1MainWindow.html#a1471665356b86fc81addf133db22c977),
[App::Document::importLinks()](../../d8/d3e/classApp_1_1Document.html#a9b93f764b381acd188cd8af6a43b2778),
[MeshPartGui::Mesh2ShapeGmsh::Mesh2ShapeGmsh()](../../db/d4d/classMeshPartGui_1_1Mesh2ShapeGmsh.html#af6f3c975ec59c3d0ff8541df09908f3b),
[MeshGui::RemeshGmsh::RemeshGmsh()](../../dd/d1b/classMeshGui_1_1RemeshGmsh.html#ae9a09acf503079bb7847c10c08092408),
[Fem::FemMesh::RestoreDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a0d087a665305a95b22c0b16b751cd5b1),
[Fem::PropertyPostDataObject::RestoreDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a1cb303cd061a1ff3deec7afece5a1d9e),
[Fem::FemMesh::SaveDocFile()](../../d3/d2e/classFem_1_1FemMesh.html#a879fc2d7f331b9cb54e05424ecf62d87),
and
[Fem::PropertyPostDataObject::SaveDocFile()](../../d0/da8/classFem_1_1PropertyPostDataObject.html#a3ed0c0500e1d89813d4d6854ce5b388b).

## ◆ getTempPath()

| std::string Application::getTempPath  | ( | | ) |   
---|---|---|---|---  
static  
  
Returns the temporary directory. By default, this is set to the system's
temporary directory but can be customized by the user.

Referenced by
[getTempFileName()](../../da/dbf/classApp_1_1Application.html#a6550097c7ee9c3857f8190954acfbf48).

## ◆ getUniqueDocumentName()

std::string Application::getUniqueDocumentName  | ( | const char *  | _Name_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _tempDoc_ = `false`  
| ) | |  const  
  
find a unique document name

References
[Base::Tools::getIdentifier()](../../d6/dda/structBase_1_1Tools.html#a49653de3f8677d06572f26f1f002641d),
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b),
and
[App::Document::TempDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af2a790c9309723635970664f9ce29418).

Referenced by
[Cloud::Module::LinkXSetValue()](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af),
and
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ getUserAppDataDir()

| std::string Application::getUserAppDataDir  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::PreferencePack::apply()](../../d3/d54/classGui_1_1PreferencePack.html#ad5cbfc85d280322a52250e42b0dfbcf2),
[WebGui::BrowserView::BrowserView()](../../db/d47/classWebGui_1_1BrowserView.html#a82c10563f152e9af1f020d012c0f6ede),
[Gui::PreferencePackManager::configBackups()](../../d9/d11/classGui_1_1PreferencePackManager.html#a3122a0735d56d0ee57db3f5fc9cdd56a),
[Gui::PreferencePackManager::deleteUserPack()](../../d9/d11/classGui_1_1PreferencePackManager.html#a6d07cd0e60c01f7f31fa4a3d1c62a6c7),
[WebGui::FcCookieJar::FcCookieJar()](../../da/d30/classWebGui_1_1FcCookieJar.html#a574284936a1d4a14e15688ef32e36583),
[Gui::BitmapFactoryInst::instance()](../../dc/da1/classGui_1_1BitmapFactoryInst.html#a1f290ef0fa8fecac10e5d837308f9c63),
[Gui::Dialog::AboutDialog::on_copyButton_clicked()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a907ddd1537ac512ba4859ee2fb4575a6),
[Drawing::FeaturePage::onDocumentRestored()](../../db/d0f/classDrawing_1_1FeaturePage.html#a61eac4ef2bdbdf694742017fe94a545e),
[Raytracing::LuxProject::onDocumentRestored()](../../d5/de6/classRaytracing_1_1LuxProject.html#af2f620cf5c7c096d24b4ad220123c909),
[Raytracing::RayProject::onDocumentRestored()](../../d2/d89/classRaytracing_1_1RayProject.html#a9d83bff4b32c1801a8ba907221d45295),
[Gui::PreferencePackManager::PreferencePackManager()](../../d9/d11/classGui_1_1PreferencePackManager.html#abb2d4e9ce7887dacce75f880d0f14420),
[Gui::PythonConsoleP::PythonConsoleP()](../../d8/de2/structGui_1_1PythonConsoleP.html#a9ff241badca5ea3c8024016832066315),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
[Gui::PreferencePackManager::save()](../../d9/d11/classGui_1_1PreferencePackManager.html#aee5aeff2da8d329471da39b2741bffa8),
[RaytracingGui::ViewProviderLux::setEdit()](../../d4/d95/classRaytracingGui_1_1ViewProviderLux.html#a559d010dd9902addb4de84170aac9f51),
[RaytracingGui::ViewProviderPovray::setEdit()](../../d4/d94/classRaytracingGui_1_1ViewProviderPovray.html#a76685922c30f4f6a92a74fafcc800fa2),
[Gui::Dialog::DlgPreferencePackManagementImp::showEvent()](../../d0/d65/classGui_1_1Dialog_1_1DlgPreferencePackManagementImp.html#a0ea7aeaec23e71117ce5413611e8e721),
and
[Gui::PreferencePackManager::templateFiles()](../../d9/d11/classGui_1_1PreferencePackManager.html#aef585677004289372394030ed5335213).

## ◆ getUserCachePath()

| std::string Application::getUserCachePath  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::Dialog::DocumentRecoveryHandler::checkForPreviousCrashes()](../../d9/d92/classGui_1_1Dialog_1_1DocumentRecoveryHandler.html#ab730fb9e0f542787859e891006695f0d),
[Gui::Dialog::DlgSettingsCacheDirectory::DlgSettingsCacheDirectory()](../../df/dfb/classGui_1_1Dialog_1_1DlgSettingsCacheDirectory.html#a7ffd5b27feda47e68e7de9bc340ce064),
[Gui::Dialog::DlgEditFileIncludePropertyExternal::Do()](../../d8/d45/classGui_1_1Dialog_1_1DlgEditFileIncludePropertyExternal.html#ace09d54687de7aa93c318fba862bd3bc),
[App::Document::getTransientDirectoryName()](../../d8/d3e/classApp_1_1Document.html#a787fa9500a9467131f2fb940083e4300),
[Gui::Dialog::DocumentRecovery::onDeleteSection()](../../d2/da2/classGui_1_1Dialog_1_1DocumentRecovery.html#a8a5bf0e053f2363b4f4afe97d3ad55b1),
[Gui::Dialog::ApplicationCache::performAction()](../../db/df8/classGui_1_1Dialog_1_1ApplicationCache.html#a10e1cafe854a412951e0c01924448801),
[Gui::Application::runApplication()](../../d9/da8/classGui_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c),
and
[Gui::Dialog::ApplicationCache::size()](../../db/df8/classGui_1_1Dialog_1_1ApplicationCache.html#aecc073050dc32e82d2954017e8f70848).

## ◆ getUserConfigPath()

| std::string Application::getUserConfigPath  | ( | | ) |   
---|---|---|---|---  
static  
  
## ◆ getUserMacroDir()

| std::string Application::getUserMacroDir  | ( | | ) |   
---|---|---|---|---  
static  
  
Referenced by
[Gui::MacroCommand::activated()](../../dc/d65/classGui_1_1MacroCommand.html#a3e9f3632b6f802aff70a6fa7d55c4ae5),
[Gui::Dialog::DlgCustomActionsImp::DlgCustomActionsImp()](../../df/dc6/classGui_1_1Dialog_1_1DlgCustomActionsImp.html#ab23956d9fabc61bb78b88e3655094fd3),
[Gui::Dialog::DlgMacroExecuteImp::DlgMacroExecuteImp()](../../dd/df2/classGui_1_1Dialog_1_1DlgMacroExecuteImp.html#afc58872ba1cb56a0c8ef7d6bed7b8c5e),
[Gui::Dialog::DlgMacroRecordImp::DlgMacroRecordImp()](../../d9/d25/classGui_1_1Dialog_1_1DlgMacroRecordImp.html#ad8423c6999d594d701df213a35112d50),
and
[Gui::PythonConsole::onSaveHistoryAs()](../../d2/da0/classGui_1_1PythonConsole.html#ace933fc956f876c9c9ddde01f5dff8e1).

## ◆ GetUserParameter()

[ParameterManager](../../db/daa/classParameterManager.html) & Application::GetUserParameter  | ( | void  | | ) |   
---|---|---|---|---|---  
  
returns the user parameter

Referenced by
[Gui::Dialog::DlgRevertToBackupConfigImp::accept()](../../d1/d47/classGui_1_1Dialog_1_1DlgRevertToBackupConfigImp.html#adb85fea9a78b916a6ca589464b3007e0),
[StdCmdImport::activated()](../../d5/d4f/classStdCmdImport.html#a7ac453df0ea7389aa72fe651020ec1d4),
[StdCmdExport::activated()](../../dd/d65/classStdCmdExport.html#a7ee127d8eac7ec03ab328a47bc3fc36f),
[StdViewScreenShot::activated()](../../d9/da6/classStdViewScreenShot.html#a4229e4b93ce96f603dbfb3cdee194091),
[CmdViewMeasureToggleAll::activated()](../../d7/d0e/classCmdViewMeasureToggleAll.html#a5b2bbcf182b849a6be359f1f5fb504af),
[Gui::StdCmdDownloadOnlineHelp::activated()](../../dc/d22/classGui_1_1StdCmdDownloadOnlineHelp.html#a29c4d53cfdd555b2a313eaa38cfa18be),
[PartGui::addLinearDimensions()](../../d5/d49/namespacePartGui.html#a1b63ea4c6302e6e76d21720c4623a6e3),
[TechDraw::DrawPage::AllowPageOverride()](../../d9/d5a/classTechDraw_1_1DrawPage.html#ab4645dcb288829a050358f596dbb1d1d),
[TechDraw::Preferences::altDecimals()](../../d6/dde/classTechDraw_1_1Preferences.html#aed14ed7fe88ef232c69e52bb5f957eaa),
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[PartGui::DlgExtrusion::apply()](../../d1/d4b/classPartGui_1_1DlgExtrusion.html#a6428c7ac6585ad41ed9792aeea96d2f7),
[Gui::PreferencePack::apply()](../../d3/d54/classGui_1_1PreferencePack.html#ad5cbfc85d280322a52250e42b0dfbcf2),
[TechDraw::Preferences::ASMEGap()](../../d6/dde/classTechDraw_1_1Preferences.html#aecffc9ba10487518872f919f0f8bf7a0),
[TechDraw::Preferences::balloonArrow()](../../d6/dde/classTechDraw_1_1Preferences.html#a337fd37ca4390303bf06adaeebf558b5),
[TechDraw::Preferences::bitmapFill()](../../d6/dde/classTechDraw_1_1Preferences.html#aaa59c01070e04cb1f547cc0d0fca41b8),
[Part::Boolean::Boolean()](../../da/d3a/classPart_1_1Boolean.html#a9acbc8d83926e3900765a64a34381244),
[PartDesign::Boolean::Boolean()](../../d2/d81/classPartDesign_1_1Boolean.html#ac032e9c86b0a2605c320402f47850319),
[TechDrawGui::PreferencesGui::centerColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#afa9514533dd681343e756446ff37ef8e),
[Gui::Dialog::DlgParameterImp::closeEvent()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#af52e249eb275c4977cf730fb10702004),
[Gui::MainWindow::confirmSave()](../../d5/d2f/classGui_1_1MainWindow.html#ade721b01893ce6e04306499df7fabf29),
[TechDrawGui::QGISVGTemplate::createClickHandles()](../../d4/d36/classTechDrawGui_1_1QGISVGTemplate.html#a2bcf2fb5e0c80557b727afaaadbb2777),
[TechDraw::DrawViewDetail::debugDetail()](../../d5/d7b/classTechDraw_1_1DrawViewDetail.html#ad82f2fbd33f1b6ab46e0b30dd7537508),
[TechDraw::DrawViewSection::debugSection()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#ac3b56b8c545035dd0fbe619e8df883a0),
[TechDraw::Preferences::defaultTemplate()](../../d6/dde/classTechDraw_1_1Preferences.html#aa2ba4e5c813143e90316673e9073e586),
[TechDraw::Preferences::defaultTemplateDir()](../../d6/dde/classTechDraw_1_1Preferences.html#abe38defbf2f6314b882b30707b5bde06),
[TechDrawGui::PreferencesGui::dimArrowSize()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a965e760d48556150cf375d97de65b604),
[TechDrawGui::PreferencesGui::dimArrowStyle()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#af875059bdec087f6f38046ac843c197c),
[TechDrawGui::PreferencesGui::dimColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a95a094ff75737586e1173090a1a4c8ea),
[TechDraw::Preferences::dimFontSizeMM()](../../d6/dde/classTechDraw_1_1Preferences.html#a91048b4c4b5cefa67fadb64ce3576eaa),
[Gui::DialogOptions::dontUseNativeColorDialog()](../../d5/df8/classGui_1_1DialogOptions.html#a4fbf98872667ba60d6faf318cd43dade),
[Gui::DialogOptions::dontUseNativeFileDialog()](../../d5/df8/classGui_1_1DialogOptions.html#a953ac2f7f5c417a9054dbd23defec9e3),
[TechDraw::DrawPage::DrawPage()](../../d9/d5a/classTechDraw_1_1DrawPage.html#a47a086fa134ba2f9e4f6a8121cb25ad2),
[TechDraw::DrawProjGroup::DrawProjGroup()](../../d4/d7c/classTechDraw_1_1DrawProjGroup.html#a95eaa24063c3912a0b99d429ce8dfcc2),
[TechDrawGui::QGIViewPart::drawViewPart()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#add7c40ff3fc3fcc84308bb29225f8cc9),
[TechDrawGui::PreferencesGui::edgeFuzz()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#aab033230710229f6405cbbf193bd7738),
[PartGui::ensure3dDimensionVisible()](../../d5/d49/namespacePartGui.html#a77e39920a64fdcb983254f95455bbcda),
[PartGui::ensureSomeDimensionVisible()](../../d5/d49/namespacePartGui.html#a079380194214302c0400d0a7374f8d05),
[Gui::MainWindow::event()](../../d5/d2f/classGui_1_1MainWindow.html#a1fc58409d671b9fd7d46ad1958af3b39),
[Part::Boolean::execute()](../../da/d3a/classPart_1_1Boolean.html#ab93d1734459a414d09ccec9df8df7831),
[Part::MultiCommon::execute()](../../d1/df7/classPart_1_1MultiCommon.html#ab89bf89ceaef91d77ba170a7e548040d),
[Part::MultiFuse::execute()](../../df/dbc/classPart_1_1MultiFuse.html#affac0f86cba2c15642f4d8a64a01c337),
[PartDesign::FeatureAddSub::FeatureAddSub()](../../d0/dd5/classPartDesign_1_1FeatureAddSub.html#aeb55c4edc7be4b3e7d20879b6162ebef),
[TechDraw::Preferences::formatSpec()](../../d6/dde/classTechDraw_1_1Preferences.html#a796da8a517d117644fd74e7260625c78),
[TechDrawGui::QGSPage::getBackgroundColor()](../../d2/d16/classTechDrawGui_1_1QGSPage.html#a0d838100a744b8e5d9cb709a7d876d5e),
[TechDrawGui::QGVPage::getBackgroundColor()](../../dd/dba/classTechDrawGui_1_1QGVPage.html#ac122949057daa3c4f5ecaea257efc67d),
[TechDrawGui::QGICenterLine::getCenterStyle()](../../d5/d69/classTechDrawGui_1_1QGICenterLine.html#a9229f19a387db364119435785dae13d0),
[TechDrawGui::TaskCenterLine::getCenterStyle()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a8886f8d0446520131b26f00e138e0af9),
[TechDrawGui::QGICMark::getCMarkColor()](../../d0/de9/classTechDrawGui_1_1QGICMark.html#a12656505be177e459609f8501cdeef0f),
[Gui::WindowParameter::getDefaultParameter()](../../d4/dcc/classGui_1_1WindowParameter.html#aaed5e4e6b43a9a46978a82581f4bb0ae),
[TechDraw::DrawLeaderLine::getDefAuto()](../../da/d1b/classTechDraw_1_1DrawLeaderLine.html#a2c2fd75cd10f8a2df5ef83697cafb5d8),
[TechDraw::LineFormat::getDefEdgeStyle()](../../d6/d5f/classTechDraw_1_1LineFormat.html#a6fc20929e9c9eabaa0d1a8719a8176f6),
[TechDrawGui::TaskCenterLine::getExtendBy()](../../d5/df5/classTechDrawGui_1_1TaskCenterLine.html#a67b4c1556e4e123450869cf7722a2958),
[TechDrawGui::QGIEdge::getHiddenColor()](../../dd/d6c/classTechDrawGui_1_1QGIEdge.html#ab102e238463840921d3f6e2f73fc815c),
[TechDrawGui::QGIEdge::getHiddenStyle()](../../dd/d6c/classTechDrawGui_1_1QGIEdge.html#a185bce3e2cbdd9099bd7adaf65470178),
[TechDrawGui::QGICMark::getMarkFuzz()](../../d0/de9/classTechDrawGui_1_1QGICMark.html#a93535e822689a5811d6d9b642c7a8e5e),
[TechDrawGui::Rez::getParameter()](../../d2/df3/classTechDrawGui_1_1Rez.html#a25ca8f266e3ccac3d5e59c90f1982432),
[TechDraw::DrawViewSection::getParameters()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a67beb353938e343cc5a31cf6a3acbfa5),
[TechDrawGui::QGIFace::getParameters()](../../d9/d59/classTechDrawGui_1_1QGIFace.html#a554cfb77c3958f6e6a16abb211d731fb),
[TechDrawGui::ViewProviderViewSection::getParameters()](../../d2/df0/classTechDrawGui_1_1ViewProviderViewSection.html#a8df1d57ca5c99b2d2a16f980618fd6a0),
[TechDrawGui::QGCustomText::getParmGroup()](../../d8/d42/classTechDrawGui_1_1QGCustomText.html#aedc7f1f371ca660592aa66468dca55a6),
[TechDrawGui::QGIPrimPath::getParmGroup()](../../dd/dc6/classTechDrawGui_1_1QGIPrimPath.html#a85a831c6f7c159d4c5be2f09e2d52ca6),
[TechDrawGui::QGIView::getParmGroupCol()](../../d1/d99/classTechDrawGui_1_1QGIView.html#a6f0b41360028f79f3974cd86b1ec9dd7),
[TechDrawGui::QGIDatumLabel::getPrecision()](../../d7/d0c/classTechDrawGui_1_1QGIDatumLabel.html#a56fc799073be6ccf0e45e538d1db75fe),
[TechDraw::DrawViewDimension::getPrefix()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a5556000b2fe9425f2abe2c87066426c0),
[TechDrawGui::QGISectionLine::getPrefSectionStandard()](../../dd/db1/classTechDrawGui_1_1QGISectionLine.html#aeada5cdc1d51dd073e314c27516c6ed8),
[TechDrawGui::QGITile::getSymbolFactor()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#aa8689dffd4b0850d58283d2ae6a3eaad),
[TechDrawGui::QGITile::getSymbolHeight()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a393b7345466a17b76e377e4ad590db4c),
[TechDrawGui::QGITile::getSymbolWidth()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#a1e3bd90e4f4358a29024bddb48f7e003),
[TechDrawGui::QGITile::getTileColor()](../../d6/d9b/classTechDrawGui_1_1QGITile.html#afe064c54983e107c72dfb37cb7b0aaf6),
[TechDrawGui::QGIDatumLabel::getTolAdjust()](../../d7/d0c/classTechDrawGui_1_1QGIDatumLabel.html#aae493518422b105e733ae8a132d0afe7),
[TechDrawGui::QGTracker::getTrackerColor()](../../da/d66/classTechDrawGui_1_1QGTracker.html#af07805427c57fbf5b0e24e96d04110f2),
[TechDrawGui::QGTracker::getTrackerWeight()](../../da/d66/classTechDrawGui_1_1QGTracker.html#aabaa753841fb22e47562b103f74789b3),
[TechDraw::DrawPage::GlobalUpdateDrawings()](../../d9/d5a/classTechDraw_1_1DrawPage.html#afbfbc377754f6f7e5fa86b24c7485615),
[PartGui::TaskCheckGeometryResults::goCheck()](../../d6/de5/classPartGui_1_1TaskCheckGeometryResults.html#aa4a2798e3f0d1217a8469bfd11093ac2),
[PartGui::goDimensionAngularNoTask()](../../d5/d49/namespacePartGui.html#a22a4e967d614ba7959dc90e89f6e76dc),
[TechDrawGui::PreferencesGui::gridColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a22bf50d673de79886edae8313ebef8a4),
[TechDrawGui::PreferencesGui::gridSpacing()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ac2417ad0a695fb273c9e7d1b28ebc2c9),
[TechDraw::DrawViewPart::handleFaces()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a0709490805aceaaed42cadb4bf1de00c),
[TechDrawGui::QGVPage::Private::init()](../../d8/d45/classQGVPage_1_1Private.html#ac463926f0a0f867803ab1ccb6e8c535c),
[TechDrawGui::QGVNavStyle::initialize()](../../dc/d63/classTechDrawGui_1_1QGVNavStyle.html#a3662e8d7a0946306e47d2ea776aa2ca8),
[TechDraw::DrawUtil::isCrazy()](../../da/d23/classTechDraw_1_1DrawUtil.html#ae600fe4a2fc97d4c5a1729597b606061),
[TechDraw::Preferences::ISOGap()](../../d6/dde/classTechDraw_1_1Preferences.html#a834d379c52173d767da1d879788fee19),
[PartDesignGui::TaskFeaturePick::isSingleSelectionEnabled()](../../d9/ddd/classPartDesignGui_1_1TaskFeaturePick.html#ab76c46f25e0df2563fa646892db56d70),
[TechDraw::Preferences::keepPagesUpToDate()](../../d6/dde/classTechDraw_1_1Preferences.html#ac20a6b1730aa1a1094b8f1fb6acf8242),
[TechDraw::Preferences::labelFont()](../../d6/dde/classTechDraw_1_1Preferences.html#abd7474067baf3458921a102e549c6103),
[TechDraw::Preferences::labelFontSizeMM()](../../d6/dde/classTechDraw_1_1Preferences.html#ac239376cf0ff092680f97d193925ee61),
[TechDrawGui::PreferencesGui::leaderColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#a317d02efc5f1a2fa44ba56ba821e0a8a),
[TechDraw::Preferences::lineGroup()](../../d6/dde/classTechDraw_1_1Preferences.html#a3280d6aec62c632d6afffee04902bfe4),
[PartGui::DlgImportExportIges::loadSettings()](../../df/d6d/classPartGui_1_1DlgImportExportIges.html#abc65b8d849e8fe5872007c73ba125176),
[PartGui::DlgImportExportStep::loadSettings()](../../d9/d15/classPartGui_1_1DlgImportExportStep.html#aed99052f9f9792e6e753e0474e60fcac),
[Gui::DockWindowManager::loadState()](../../d9/d72/classGui_1_1DockWindowManager.html#a64e54f3ead86cbe7da017692ae84ae03),
[Gui::MainWindow::MainWindow()](../../d5/d2f/classGui_1_1MainWindow.html#a84c74efa977302744093e2027b0dd801),
[TechDraw::Preferences::mattingStyle()](../../d6/dde/classTechDraw_1_1Preferences.html#a0472459f6797d0c9439e3fc2bd1b781d),
[Gui::DAG::Model::Model()](../../df/d26/classGui_1_1DAG_1_1Model.html#a81b067d165657725e854c9ce8e038fec),
[Part::MultiCommon::MultiCommon()](../../d1/df7/classPart_1_1MultiCommon.html#a92cede506f5bff5155073b720dc0b16f),
[Part::MultiFuse::MultiFuse()](../../df/dbc/classPart_1_1MultiFuse.html#a4920bfcdce11fc706efa2d09417a153a),
[TechDraw::Preferences::normalColor()](../../d6/dde/classTechDraw_1_1Preferences.html#adb6c09529cd68c3282cf99c8a301020e),
[Gui::Dialog::DlgParameterImp::onChangeParameterSet()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a5c3b0d0bc86b49af2db5dd89379c377f),
[TechDraw::Preferences::patFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a603db0a17ac567dd7dc8b20fbe51c609),
[TechDraw::ShapeExtractor::prefAdd2d()](../../d6/d47/classTechDraw_1_1ShapeExtractor.html#af82fed64f839cb888bb403cca2e4dfc6),
[TechDrawGui::QGIPrimPath::prefCapStyle()](../../dd/dc6/classTechDrawGui_1_1QGIPrimPath.html#a12957a965247c4744bbf93cfdfd35a91),
[TechDraw::DrawViewSection::prefCutSurface()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#a9b5ca9c16a1bee8bddcfc5c8de052447),
[TechDrawGui::QGIViewPart::prefFaceEdges()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#ac6ae36f1506244d9d99a6a18be45b0ad),
[TechDraw::DrawGeomHatch::prefGeomHatchColor()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a40d7be42405ae1d1cd4709fea43e3d2e),
[TechDraw::DrawGeomHatch::prefGeomHatchName()](../../d1/de2/classTechDraw_1_1DrawGeomHatch.html#a1bc76a218a0af36e77b55421172c2479),
[TechDraw::DrawViewPart::prefHardHid()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#abdd33ea7dc0ca36c9b22908e705d3f97),
[TechDraw::DrawViewPart::prefHardViz()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a22d34984e9866153a73daff6c6813117),
[TechDrawGui::ViewProviderViewPart::prefHighlightColor()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aace0358ec81505b5e3bda84919495805),
[TechDrawGui::ViewProviderViewPart::prefHighlightStyle()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#a17a280663ac08cc08bd22ee646509ce1),
[TechDraw::DrawViewPart::prefIsoCount()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#ab1d7ed5654dfa2741fefb01b4587ddec),
[TechDraw::DrawViewPart::prefIsoHid()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6f51b57de5c8e44872cd9ae69652b046),
[TechDraw::DrawViewPart::prefIsoViz()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a3023178054a6fc7b92e0b838906b9b1b),
[TechDraw::DrawViewBalloon::prefKinkLength()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a2e143483c2f5bd07be9914d8b829a8da),
[TechDrawGui::QGIViewBalloon::prefOrthoPyramid()](../../d0/d29/classTechDrawGui_1_1QGIViewBalloon.html#afed01f2391b6a07c0094634f609a173c),
[TechDrawGui::QGIViewPart::prefPrintCenters()](../../dd/d9d/classTechDrawGui_1_1QGIViewPart.html#a329af2fd9bdf1d1375a8f74ebbe58345),
[TechDraw::DrawView::prefScale()](../../d6/d1c/classTechDraw_1_1DrawView.html#afc0e7db7510d676055bc131cffc0b59c),
[TechDraw::DrawView::prefScaleType()](../../d6/d1c/classTechDraw_1_1DrawView.html#a35241b6aa1cca5e1609f29f055adbd4d),
[TechDraw::DrawViewPart::prefSeamHid()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a6999950a1da11842c435223cb17cb91e),
[TechDraw::DrawViewPart::prefSeamViz()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a5768ee86cbed0c1d64d7416e7c08e557),
[TechDraw::DrawViewBalloon::prefShape()](../../d1/d91/classTechDraw_1_1DrawViewBalloon.html#a58debd0316676b0f50864671e60ef06f),
[TechDraw::DrawViewPart::prefSmoothHid()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#a372f275b439b1c6b5868dfec5a2d8c6f),
[TechDraw::DrawViewPart::prefSmoothViz()](../../d7/dc3/classTechDraw_1_1DrawViewPart.html#aa6f8b1a57c2bbd3269d200919772627b),
[TechDrawGui::ViewProviderDimension::prefStandardAndStyle()](../../d8/d4e/classTechDrawGui_1_1ViewProviderDimension.html#a9ff4deacbe21dd5625eda279c9b2843c),
[TechDraw::DrawHatch::prefSvgHatchColor()](../../d0/d97/classTechDraw_1_1DrawHatch.html#aeca1a29638d429cb325d49d144c58662),
[TechDrawGui::ViewProviderWeld::prefTileTextAdjust()](../../dc/dbe/classTechDrawGui_1_1ViewProviderWeld.html#a01a3423081140f40cac62d82ba654d13),
[TechDraw::Preferences::preselectColor()](../../d6/dde/classTechDraw_1_1Preferences.html#a51bfd9c397346caf1de29c09e62cb902),
[TechDraw::Preferences::projectionAngle()](../../d6/dde/classTechDraw_1_1Preferences.html#aa98413e2dde281a55de86d233f4a9c99),
[TechDraw::CosmeticVertex::restoreCosmetic()](../../dc/d6a/classTechDraw_1_1CosmeticVertex.html#a3701364c9bdbd0f809090999afa54c36),
[Gui::FileDialog::restoreLocation()](../../de/d93/classGui_1_1FileDialog.html#a5aedc90989870d2e5b2978a51b81e668),
[Gui::ToolBarManager::restoreState()](../../db/da9/classGui_1_1ToolBarManager.html#a71ef82438acd1fa6a86e659ada9f0bfe),
[Gui::MacroManager::run()](../../d8/dc6/classGui_1_1MacroManager.html#afd22c56a284e48a4df19fa0df503826b),
[Gui::FileDialog::saveLocation()](../../de/d93/classGui_1_1FileDialog.html#a0db32ff01648257814244361faebd25c),
[PartGui::DlgImportExportIges::saveSettings()](../../df/d6d/classPartGui_1_1DlgImportExportIges.html#aaba9925117f2c35b938161a92732444b),
[PartGui::DlgImportExportStep::saveSettings()](../../d9/d15/classPartGui_1_1DlgImportExportStep.html#a6f490eb6982475954f3eedda20819643),
[Gui::DockWindowManager::saveState()](../../d9/d72/classGui_1_1DockWindowManager.html#a5afbc0d0bd891ca995fc3d20ac3e4c33),
[Gui::ToolBarManager::saveState()](../../db/da9/classGui_1_1ToolBarManager.html#a50b72951bbf26580ecf88a6ff49ed568),
[TechDrawGui::PreferencesGui::sectionLineColor()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#aa8528664be8ce3842047229819c6ab3b),
[TechDrawGui::PreferencesGui::sectionLineStyle()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ad261a250da626c65ae8d5633185f6c13),
[TechDraw::Preferences::selectColor()](../../d6/dde/classTechDraw_1_1Preferences.html#a4aa75b1352c633d046ec12ab0929df6a),
[Gui::DockWindowManager::setup()](../../d9/d72/classGui_1_1DockWindowManager.html#ac7496ebe8ee92e01198321e0be661064),
[Gui::ToolBarManager::setup()](../../db/da9/classGui_1_1ToolBarManager.html#a87d9657f2799118a3628789f4c88ca4b),
[Gui::StdWorkbench::setupDockWindows()](../../db/d0a/classGui_1_1StdWorkbench.html#a88c74a40b7a275fb0c7fa93688f82afe),
[PartDesign::SubShapeBinder::setupObject()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#a788801f841b2c6dfcb6493aa6a69aacd),
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e),
[Gui::Dialog::DlgParameterImp::showEvent()](../../d7/de1/classGui_1_1Dialog_1_1DlgParameterImp.html#a3081f7505441b21fd97389214f148c91),
[TechDrawGui::PreferencesGui::showGrid()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#acea2bff0741878d42af798245f473ad2),
[TechDraw::DrawViewSection::showSectionEdges()](../../d3/d1e/classTechDraw_1_1DrawViewSection.html#acb5ca664fd416324aee88d74c4021a2f),
[TechDraw::DrawViewDimension::showUnits()](../../d8/d89/classTechDraw_1_1DrawViewDimension.html#a20e6dbfd79b07cd7ee5b94c9e7311ec4),
[Gui::MainWindow::startSplasher()](../../d5/d2f/classGui_1_1MainWindow.html#a582325552a23f1edf2320b39dfd84547),
[TechDraw::Preferences::svgFile()](../../d6/dde/classTechDraw_1_1Preferences.html#a7948f1f445732b3f5720eaa35de03d8d),
[PartGui::TaskCheckGeometryDialog::TaskCheckGeometryDialog()](../../dd/d83/classPartGui_1_1TaskCheckGeometryDialog.html#a1ea8f5354ec8cdf84523c2948270697f),
[PartGui::toggle3d()](../../d5/d49/namespacePartGui.html#ade2339bbfb908ff2c05fe0bb2c30d646),
[PartGui::toggleDelta()](../../d5/d49/namespacePartGui.html#a2056372c3d37e5fabd709d22921a7bbd),
[PartDesign::Transformed::Transformed()](../../dd/de1/classPartDesign_1_1Transformed.html#abefdee4b026b49930de1c6b0c9789d33),
[TechDraw::Preferences::vertexColor()](../../d6/dde/classTechDraw_1_1Preferences.html#acb17c87d06ccdb555bf7a1dc1a0a4372),
[TechDraw::Preferences::vertexScale()](../../d6/dde/classTechDraw_1_1Preferences.html#a661288784380acea3ca33188181fcf04),
[TechDrawGui::ViewProviderViewPart::ViewProviderViewPart()](../../d4/d93/classTechDrawGui_1_1ViewProviderViewPart.html#aa788186aa3b1edf4937b903368b9a626),
and
[TechDrawGui::PreferencesGui::weldingDirectory()](../../d9/d1a/classTechDrawGui_1_1PreferencesGui.html#ae8f758711778daab1558370f25fa519f).

## ◆ hasLinksTo()

[bool](../../d9/db9/classbool.html) Application::hasLinksTo  | ( | const [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _obj_| ) |  const  
---|---|---|---|---|---  
  
Check if there is any link to the given object.

References
[getLinksTo()](../../da/dbf/classApp_1_1Application.html#a9b748f2221ed6e0da2e575c161712c62).

Referenced by
[StdCmdLinkSelectAllLinks::isActive()](../../df/dd6/classStdCmdLinkSelectAllLinks.html#a99b0745849f9e8263b01c310e968a73d).

## ◆ init()

| void Application::init  | ( | [int](../../d1/da0/classint.html) | _argc_ ,   
---|---|---|---  
|  | char **  | _argv_  
| ) | |   
static  
  
References
[destructObserver()](../../da/dbf/classApp_1_1Application.html#a8ba7d824857a33ccb20839ec0ae19e44),
and
[initTypes()](../../da/dbf/classApp_1_1Application.html#a7fd51c3ba729d368d8f150a720af49e1).

Referenced by
[DocumentObject.DocumentObject::onChanged()](../../d7/dae/classDocumentObject_1_1DocumentObject.html#a3ddd3f88d14a83a2e41491680fb9b882).

## ◆ initTypes()

| void Application::initTypes  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Persistence::getClassTypeId()](../../d9/d25/classBase_1_1Persistence.html#aafa03b0c10b4f57d997555881be0ed56),
[Base::BaseClass::init()](../../df/d4d/classBase_1_1BaseClass.html#a212586b53f566dcb0e17626699be60a7),
[Base::Type::init()](../../dc/dee/classBase_1_1Type.html#a55b0a9918023eafb441abf1678c8185c),
[Base::Exception::init()](../../d8/df7/classBase_1_1Exception.html#aa5f325f865abb611f5fd93277905f978),
and
[Base::Persistence::init()](../../d9/d25/classBase_1_1Persistence.html#a4e9f73ac099dd794f6c87946f61cee0e).

Referenced by
[init()](../../da/dbf/classApp_1_1Application.html#a5a044efb1e023bdba4afd35d262654d5).

## ◆ isClosingAll()

[bool](../../d9/db9/classbool.html) Application::isClosingAll  | ( | | ) |  const  
---|---|---|---|---  
  
Indicate the application is closing all document.

## ◆ isRestoring()

[bool](../../d9/db9/classbool.html) Application::isRestoring  | ( | | ) |  const  
---|---|---|---|---  
  
Indicate whether the application is opening (restoring) some document.

References
[App::Document::isAnyRestoring()](../../d8/d3e/classApp_1_1Document.html#ad76082433b2ec1d09d842514de7dfe38).

Referenced by
[App::PropertyXLink::setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e).

## ◆ newDocument()

[Document](../../d8/d3e/classApp_1_1Document.html) * Application::newDocument  | ( | const char *  | _Name_ = `nullptr`,   
---|---|---|---  
|  | const char *  | _UserName_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _createView_ = `true`,   
|  | [bool](../../d9/db9/classbool.html) | _tempDoc_ = `false`  
| ) | |   
  
Creates a new document The first name is a the identifier and some kind of an
internal (english) name.

It has to be like an identifier in a programming language, with no spaces and
not starting with a number. This name gets also forced to be unique in this
[Application](../../da/dbf/classApp_1_1Application.html "The Application The
root of the whole application."). You can avoid the renaming by using
[getUniqueDocumentName()](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030
"find a unique document name") to get a unique name before calling
newDoucument(). The second name is a UTF8 name of any kind. It's that name
normally shown to the user and stored in the App::Document::Name property.

References
[draftgeoutils.faces::bind()](../../d9/dfd/group__draftgeoutils.html#ga6589f3a751c4ddd5c4f02b95ee2139c7),
[getUniqueDocumentName()](../../da/dbf/classApp_1_1Application.html#a59cb1d32f2baee9436cbee0ab4253030),
[Base::Tools::getUniqueName()](../../d6/dda/structBase_1_1Tools.html#a2e5fcd4db818dbcce127c0695ffe937b),
[setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94),
[signalNewDocument](../../da/dbf/classApp_1_1Application.html#a49425118433ce84229402407d5631ea4),
[slotAbortTransaction()](../../da/dbf/classApp_1_1Application.html#a06e511b2cd5a4443818c668ebc9014b1),
[slotActivatedObject()](../../da/dbf/classApp_1_1Application.html#ad726ef79a1bd4f878bf325784581a047),
[slotBeforeChangeDocument()](../../da/dbf/classApp_1_1Application.html#a4220212a2b53e4b8d6301196b4952dc5),
[slotBeforeChangeObject()](../../da/dbf/classApp_1_1Application.html#a1f3693850c25e228c864936c8f184e69),
[slotBeforeRecompute()](../../da/dbf/classApp_1_1Application.html#abe70fa9ac1b478b8af5bf70e9dadbd6b),
[slotChangedDocument()](../../da/dbf/classApp_1_1Application.html#a452e6b15d130b6591f6ff866ac25af79),
[slotChangedObject()](../../da/dbf/classApp_1_1Application.html#a0b5cc52e99eb30dc897959a050904559),
[slotChangePropertyEditor()](../../da/dbf/classApp_1_1Application.html#a6cd9752f5d95bce3f2942f5c8be8ecd1),
[slotCommitTransaction()](../../da/dbf/classApp_1_1Application.html#a0f5b88b7f15a92bcd03f01e77ba8bcb1),
[slotDeletedObject()](../../da/dbf/classApp_1_1Application.html#ad6e7f304a6bf2a014d75039b8caa8837),
[slotFinishSaveDocument()](../../da/dbf/classApp_1_1Application.html#a609e60d2806e8728c7bdb47840ea2d48),
[slotNewObject()](../../da/dbf/classApp_1_1Application.html#aa6835d277021785cdd0f9ae038472762),
[slotOpenTransaction()](../../da/dbf/classApp_1_1Application.html#ae6d03ca955417ba7789ee4fc6333792b),
[slotRecomputed()](../../da/dbf/classApp_1_1Application.html#ac1a39ddbde61ec1b603e8f3dc35af59e),
[slotRecomputedObject()](../../da/dbf/classApp_1_1Application.html#a0c4c8807007b3ec248e7e4afc3bb1567),
[slotRedoDocument()](../../da/dbf/classApp_1_1Application.html#a8f9128275989a896d2f6c55d5af4785b),
[slotRelabelObject()](../../da/dbf/classApp_1_1Application.html#a5a3dcdcb74979ab007577f3684598c5a),
[slotStartSaveDocument()](../../da/dbf/classApp_1_1Application.html#ad4b9071ef9241b25392537dd269cd823),
[slotUndoDocument()](../../da/dbf/classApp_1_1Application.html#a72d52b675d7da0a4bf6dad8c0ed713a8),
and
[App::Document::TempDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553af2a790c9309723635970664f9ce29418).

Referenced by
[Fem::createObjectByType()](../../dd/d72/namespaceFem.html#af3663ac69e66763d50fbbd579cb9024a),
[Fem::getObjectByType()](../../dd/d72/namespaceFem.html#a1d62957fae198eb1c03b3ce2c2503c3c),
[Gui::MainWindow::insertFromMimeData()](../../d5/d2f/classGui_1_1MainWindow.html#a3b695bba64b1eead11c5bf3843c54790),
[Cloud::Module::LinkXSetValue()](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af),
[openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[Fem::FemVTKTools::readResult()](../../d6/d26/classFem_1_1FemVTKTools.html#a4a7eb62a28318f76ae647e81b8832f7d),
[Path::Area::showShape()](../../d8/dfc/classPath_1_1Area.html#ac20bf1933f3cb18e24b0892f378b761f),
[Gui::Application::sInsert()](../../d9/da8/classGui_1_1Application.html#aca6ab0f62cf4fb268ea9a87ce3cebaf2),
[Gui::Application::sOpen()](../../d9/da8/classGui_1_1Application.html#a3402c81d1a56dbb72d84e74047fc53e8),
and
[PartDesign::SubShapeBinder::update()](../../d3/dd1/classPartDesign_1_1SubShapeBinder.html#ab7ddbeeecc00741237f9ec49aab91d83).

## ◆ openDocument()

[Document](../../d8/d3e/classApp_1_1Document.html) * Application::openDocument  | ( | const char *  | _FileName_ = `nullptr`,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _createView_ = `true`  
| ) | |   
  
Open an existing document from a file.

References
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

Referenced by
[processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[Gui::Application::reopen()](../../d9/da8/classGui_1_1Application.html#a7a21dfd4379a11fd6babb3a2a14d4b1a),
and
[App::PropertyXLink::setAllowPartial()](../../d2/de2/classApp_1_1PropertyXLink.html#af69aa75e548072c713a0b180cadab17e).

## ◆ openDocumentPrivate()

| [Document](../../d8/d3e/classApp_1_1Document.html) * Application::openDocumentPrivate  | ( | const char *  | _FileName_ ,   
---|---|---|---  
|  | const char *  | _propFileName_ ,   
|  | const char *  | _label_ ,   
|  | [bool](../../d9/db9/classbool.html) | _isMainDoc_ ,   
|  | [bool](../../d9/db9/classbool.html) | _createView_ ,   
|  | std::vector< std::string > && | _objNames_  
| ) | |   
protected  
  
open single document only

References
[closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244),
[Base::FileInfo::exists()](../../dd/d34/classBase_1_1FileInfo.html#a47d49db8cb8797153885c4d5b7b0911f),
[App::Document::FileName](../../d8/d3e/classApp_1_1Document.html#a7f765b6bfef0aef1825c0f3fa36de9ae),
[Base::FileInfo::fileNamePure()](../../dd/d34/classBase_1_1FileInfo.html#aee95cfa273dadbe71b450f3b834a4894),
[Base::FileInfo::filePath()](../../dd/d34/classBase_1_1FileInfo.html#ae4e3ea54dca3fa6a47cc90a5d83a6987),
[getDocumentByPath()](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0),
[App::Document::getName()](../../d8/d3e/classApp_1_1Document.html#a5d15901e2510f1d20fd30045b542916d),
[App::PropertyString::getValue()](../../dd/df8/classApp_1_1PropertyString.html#a5d15a90861479d5557f46d87cd30f485),
[MatchCanonicalWarning](../../da/dbf/classApp_1_1Application.html#a254ca67fbc136c5c251862737a59dd64a598e2b0f31835f6560f3f4c1b302668c),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b),
[App::Document::PartialDoc](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553a42f5fe7eeacbd5101377ac0823f09ccf),
[App::PartialObject](../../dd/dc2/namespaceApp.html#a6ea56730deb62adcdfb038475dab9d3aadddc278250236b1498067f68f109203f),
[App::Document::PartialRestore](../../d8/d3e/classApp_1_1Document.html#a855dc0d75b717ed9dc70050a790fa553aa85fb1ecccf6466736187e1826eab209),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

Referenced by
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

## ◆ openDocuments()

std::vector< [Document](../../d8/d3e/classApp_1_1Document.html) * > Application::openDocuments  | ( | const std::vector< std::string > & | _filenames_ ,   
---|---|---|---  
|  | const std::vector< std::string > *  | _paths_ = `nullptr`,   
|  | const std::vector< std::string > *  | _labels_ = `nullptr`,   
|  | std::vector< std::string > *  | _errs_ = `nullptr`,   
|  | [bool](../../d9/db9/classbool.html) | _createView_ = `true`  
| ) | |   
  
Open multiple documents.

Parameters

     filenames| input file names   
---|---  
paths| optional input file path in case it is different from filenames (mainly
used during recovery).  
labels| optional label assign to document (mainly used during recovery).  
errs| optional output error message corresponding to each input file name. If
errs is given, this function will catch all
[Base::Exception](../../d8/df7/classBase_1_1Exception.html) and save the error
message inside. Otherwise, it will throw on exception when opening the input
files.  
createView| whether to signal [Gui](../../d9/dad/namespaceGui.html "The
FreeCAD Graphical interface layer.") module to create view on restore.  
  
Returns

    Return opened document object corresponding to each input file name, which maybe NULL if failed.

This function will also open any external referenced files.

References
[closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[ParameterGrp::GetBool()](../../d4/d97/classParameterGrp.html#a603e85aad05116d3331f865715297d08),
[App::Document::getDependentDocuments()](../../d8/d3e/classApp_1_1Document.html#a2411038de4eb7e088f26cebb5725eb26),
[getDocumentByPath()](../../da/dbf/classApp_1_1Application.html#abc280d24a20b5b20b7e394b3536a0ad0),
[GetParameterGroupByPath()](../../da/dbf/classApp_1_1Application.html#a9bd30a8f3640e241a55ffe51f565f202),
[draftfunctions.move::move()](../../d2/d57/group__draftfunctions.html#gaba90180fe5a79e13cb43a1fcda667a2f),
[Base::SequencerLauncher::next()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a),
[openDocumentPrivate()](../../da/dbf/classApp_1_1Application.html#afe5553eafcf137315a416cff84733189),
[App::PropertyXLink::restoreDocument()](../../d2/de2/classApp_1_1PropertyXLink.html#a5ef57584d28afeba3785b8d5dada73b5),
[setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94),
[signalFinishOpenDocument](../../da/dbf/classApp_1_1Application.html#ad77e22504068699d121e7c51b10d72bb),
and
[signalStartOpenDocument](../../da/dbf/classApp_1_1Application.html#a6bdfe9471899866c70a4556ec86cea6d).

Referenced by
[Gui::Dialog::DocumentRecovery::accept()](../../d2/da2/classGui_1_1Dialog_1_1DocumentRecovery.html#a70922db70921db97f90cd5a5420cdc08),
and
[openDocument()](../../da/dbf/classApp_1_1Application.html#a4ad1dd5f7c7ea3e47e6ccee518ca437c).

## ◆ processCmdLineFiles()

| void Application::processCmdLineFiles  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::Tools::escapeEncodeFilename()](../../d6/dda/structBase_1_1Tools.html#a8bc9d995425fdc0f2e54c1782d10a431),
[Base::FileInfo::extension()](../../dd/d34/classBase_1_1FileInfo.html#afb9db1389fb6645d1f423ce0871468b5),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[getCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#afc32584672ac65f92291272a3b5b7cf3),
[getExportModules()](../../da/dbf/classApp_1_1Application.html#ad2f5f9df9afe7f48a06c8d8c76070dad),
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9),
[Base::InterpreterSingleton::loadModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af59e1b874f05bcb2792ec395788578be),
[processFiles()](../../da/dbf/classApp_1_1Application.html#aa7cdc351aad94d3d76c75175bc81f939),
[Base::InterpreterSingleton::runString()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a2cabac4e610e966ebc33a1e1aa5d94b6),
[Base::InterpreterSingleton::runStringArg()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#afff9e462cde2ead702ab1ff0f5ddbbad),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[runApplication()](../../da/dbf/classApp_1_1Application.html#addc0109cdd4dfa4bf1d102212b5edd0c).

## ◆ processFiles()

| std::list< std::string > Application::processFiles  | ( | const std::list< std::string > & | _files_| ) |   
---|---|---|---|---|---  
static  
  
References
[Base::InterpreterSingleton::addPythonPath()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a71c5ca5d92e31196d1d1736a12a988bc),
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::ConsoleSingleton::Error()](../../df/dca/classBase_1_1ConsoleSingleton.html#a93702f1cca400a9fa8ab7576211a2644),
[Base::Tools::escapedUnicodeFromUtf8()](../../d6/dda/structBase_1_1Tools.html#a2cfe13d9b5c340ec5dc8a7b34fff8645),
[Base::Tools::escapeEncodeFilename()](../../d6/dda/structBase_1_1Tools.html#a8bc9d995425fdc0f2e54c1782d10a431),
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
[getImportModules()](../../da/dbf/classApp_1_1Application.html#a42a251c438c21d843c37eb417011ec65),
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9),
[Base::InterpreterSingleton::loadModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af59e1b874f05bcb2792ec395788578be),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[openDocument()](../../da/dbf/classApp_1_1Application.html#a4ad1dd5f7c7ea3e47e6ccee518ca437c),
[Base::InterpreterSingleton::runFile()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#ae05d01943aa268be77244fa1e98e88f0),
[Base::InterpreterSingleton::runStringArg()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#afff9e462cde2ead702ab1ff0f5ddbbad),
and
[Base::ConsoleSingleton::Warning()](../../df/dca/classBase_1_1ConsoleSingleton.html#a844216fdc8593ce5b53b42c3f963e326).

Referenced by
[processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa).

## ◆ RemoveParameterSet()

void Application::RemoveParameterSet  | ( | const char *  | _sName_| ) |   
---|---|---|---|---|---  
  
## ◆ renameDocument()

| void Application::renameDocument  | ( | const char *  | _OldName_ ,   
---|---|---|---  
|  | const char *  | _NewName_  
| ) | |   
protected  
  
get called by the document when the name is changing

References
[signalRenameDocument](../../da/dbf/classApp_1_1Application.html#abe4f8ab20f19201d26ca7307bc719614).

## ◆ runApplication()

| void Application::runApplication  | ( | void  | | ) |   
---|---|---|---|---|---  
static  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9),
[Base::ConsoleSingleton::Log()](../../df/dca/classBase_1_1ConsoleSingleton.html#aceeee19e61fdce99692897f996fa4964),
[processCmdLineFiles()](../../da/dbf/classApp_1_1Application.html#a1d47b63939965f9c2e73331447272dfa),
[Base::InterpreterSingleton::runCommandLine()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a5f7f8312974b7d1a819fa4a23f0da464),
[Base::InterpreterSingleton::runString()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#a2cabac4e610e966ebc33a1e1aa5d94b6),
and
[Base::ScriptFactory()](../../db/d07/namespaceBase.html#ad538daa5cac7fdc4527737c1b51918f3).

## ◆ setActiveDocument() [1/2]

void Application::setActiveDocument  | ( | [App::Document](../../d8/d3e/classApp_1_1Document.html) *  | _pDoc_| ) |   
---|---|---|---|---|---  
  
Set the active document.

References
[App::Document::getPyObject()](../../d8/d3e/classApp_1_1Document.html#a3eafa7c3d20b42cb6c41d9623c2476c7),
and
[signalActiveDocument](../../da/dbf/classApp_1_1Application.html#ad9cf4f57c0d4fda56d79ec91936efa39).

Referenced by
[closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244),
[Gui::TreeWidget::contextMenuEvent()](../../de/de0/classGui_1_1TreeWidget.html#a1973cd275eac94af842ffd66ab4fbadd),
[Cloud::Module::LinkXSetValue()](../../d9/d80/classCloud_1_1Module.html#acf7fd5b771d0b2cf507790830b99a3af),
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b),
[Gui::TreeWidget::onReloadDoc()](../../de/de0/classGui_1_1TreeWidget.html#aa829bae01b16d52a20a4e32bbb899704),
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a174f0735b517d40e0a625f6ed098a40f).

## ◆ setActiveDocument() [2/2]

void Application::setActiveDocument  | ( | const char *  | _Name_| ) |   
---|---|---|---|---|---  
  
References
[setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94).

## ◆ setActiveTransaction()

[int](../../d1/da0/classint.html) Application::setActiveTransaction  | ( | const char *  | _name_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _persist_ = `false`  
| ) | |   
  
Setup a pending application-wide active transaction.

Parameters

     name| new transaction name   
---|---  
persist| by default, if the calling code is inside any invocation of a
command, it will be auto closed once all command within the current stack
exists. To disable auto closing, set persist=true  
  
Returns

    The new transaction ID.

Call this function to setup an application-wide transaction. All current
pending transactions of opening documents will be committed first. However, no
new transaction is created by this call. Any subsequent changes in any current
opening document will auto create a transaction with the given name and ID. If
more than one document is changed, the transactions will share the same ID,
and will be undo/redo together.

References
[getActiveTransaction()](../../da/dbf/classApp_1_1Application.html#a320164bff61415b44f26af228fe99c6a),
[App::Transaction::getNewID()](../../de/dbf/classApp_1_1Transaction.html#addd5e67511d134c5faf11d907a7187d2),
and
[App::AutoTransaction::setEnable()](../../dd/d19/classApp_1_1AutoTransaction.html#a239a24d16e7a12deecd08b102212a6d2).

Referenced by
[PartDesignGui::DlgActiveBody::accept()](../../dc/dd5/classPartDesignGui_1_1DlgActiveBody.html#a1932d79f3d3669f8b2f576ead60d0ab7),
[Gui::ElementColors::Private::apply()](../../d8/dc9/classElementColors_1_1Private.html#a66e40ead78f26aa47dc150184afb9a06),
[Gui::ExpressionBinding::apply()](../../dc/d5a/classGui_1_1ExpressionBinding.html#a0f027ccb09e2a67dd2aba44d35edb2d2),
[Gui::TreeWidgetEditDelegate::createEditor()](../../db/d6e/classGui_1_1TreeWidgetEditDelegate.html#ad2db8c1dd8e1914745c0a1b7fc111484),
[TechDrawGui::QGIRichAnno::mouseDoubleClickEvent()](../../d0/d89/classTechDrawGui_1_1QGIRichAnno.html#ae314ffc101d4592c4a492f380ce72655),
[TechDrawGui::QGIViewAnnotation::mouseDoubleClickEvent()](../../d4/d5b/classTechDrawGui_1_1QGIViewAnnotation.html#a0b2aec7a7e987b6deaca89c24d426c8d),
[TechDrawGui::TaskDlgProjGroup::open()](../../df/df7/classTechDrawGui_1_1TaskDlgProjGroup.html#a3148996aff434f83002f9cbe3a402aaf),
[Gui::Command::openCommand()](../../d2/dff/classGui_1_1Command.html#adbb84c03f5c6b7c99277fa5ae781471a),
[App::Document::openTransaction()](../../d8/d3e/classApp_1_1Document.html#a8e5586f3164279fa8f4dcbfd42009688),
[Gui::ExpressionBinding::setExpression()](../../dc/d5a/classGui_1_1ExpressionBinding.html#ab4b4f84605e7bf21c036c6a9a09fbb2f),
[PartDesignGui::TaskDressUpParameters::setupTransaction()](../../d2/da8/classPartDesignGui_1_1TaskDressUpParameters.html#a6f99d504a2dbb11111be017f2bfe4bbf),
[PartDesignGui::TaskTransformedParameters::setupTransaction()](../../d3/d24/classPartDesignGui_1_1TaskTransformedParameters.html#abf0df5b3ed2b19577b9bd4d6359c9c79),
and
[App::PropertyString::setValue()](../../dd/df8/classApp_1_1PropertyString.html#a6468ae106c1aa686df12fd03655b2c1e).

## ◆ slotAbortTransaction()

| void Application::slotAbortTransaction  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _d_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalAbortTransaction](../../da/dbf/classApp_1_1Application.html#a9262371d6632485a417c96036fd31831).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotActivatedObject()

| void Application::slotActivatedObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _O_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalActivatedObject](../../da/dbf/classApp_1_1Application.html#a7193d997f6d54f1369d17540f515a61c).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotBeforeChangeDocument()

| void Application::slotBeforeChangeDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_  
| ) | |   
protected  
  
References
[signalBeforeChangeDocument](../../da/dbf/classApp_1_1Application.html#a0a74f8e0386bb7e164cc4e6c653822a9).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotBeforeChangeObject()

| void Application::slotBeforeChangeObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _O_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _Prop_  
| ) | |   
protected  
  
References
[signalBeforeChangeObject](../../da/dbf/classApp_1_1Application.html#a754143d4cbf1aefe30920a12ee268d35).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotBeforeRecompute()

| void Application::slotBeforeRecompute  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalBeforeRecomputeDocument](../../da/dbf/classApp_1_1Application.html#a9bfbc2bd635c57b114636bc16ead33f2).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotChangedDocument()

| void Application::slotChangedDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_  
| ) | |   
protected  
  
References
[signalChangedDocument](../../da/dbf/classApp_1_1Application.html#a85edc6708be468366ba00b701ef60adf).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotChangedObject()

| void Application::slotChangedObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _O_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _Prop_  
| ) | |   
protected  
  
References
[signalChangedObject](../../da/dbf/classApp_1_1Application.html#af3ea93d79c3c2496701f3ed583efbc10).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotChangePropertyEditor()

| void Application::slotChangePropertyEditor  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_ ,   
---|---|---|---  
|  | const [App::Property](../../d0/da9/classApp_1_1Property.html) & | _prop_  
| ) | |   
protected  
  
References
[signalChangePropertyEditor](../../da/dbf/classApp_1_1Application.html#a118f31ab2a23e562862614a5de003803).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotCommitTransaction()

| void Application::slotCommitTransaction  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _d_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalCommitTransaction](../../da/dbf/classApp_1_1Application.html#a06ca57127575a3cbec2e6ed6d9346c17).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotDeletedObject()

| void Application::slotDeletedObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _O_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalDeletedObject](../../da/dbf/classApp_1_1Application.html#affb0434ff9fe9ed3542f6724d5c37491).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotFinishSaveDocument()

| void Application::slotFinishSaveDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_ ,   
---|---|---|---  
|  | const std::string & | _filename_  
| ) | |   
protected  
  
References
[signalFinishSaveDocument](../../da/dbf/classApp_1_1Application.html#af928fa8c38791c140768aef047422a24).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotNewObject()

| void Application::slotNewObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _O_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalNewObject](../../da/dbf/classApp_1_1Application.html#a2be45dffee80c84ad63eb0e87cea6bec).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotOpenTransaction()

| void Application::slotOpenTransaction  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _d_ ,   
---|---|---|---  
|  | std::string  | _s_  
| ) | |   
protected  
  
References
[signalOpenTransaction](../../da/dbf/classApp_1_1Application.html#a1fd7640f51ddc743d89e531324cdc4ec).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotRecomputed()

| void Application::slotRecomputed  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalRecomputed](../../da/dbf/classApp_1_1Application.html#a70ddba55bf1fe563e216fc4453bbb8c4).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotRecomputedObject()

| void Application::slotRecomputedObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _obj_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalObjectRecomputed](../../da/dbf/classApp_1_1Application.html#a927030e1bc1089d482c68db63ea0e449).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotRedoDocument()

| void Application::slotRedoDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _d_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalRedoDocument](../../da/dbf/classApp_1_1Application.html#a63e3d1fd313c1be4e30c630d77120fa1).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotRelabelObject()

| void Application::slotRelabelObject  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) & | _O_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalRelabelObject](../../da/dbf/classApp_1_1Application.html#ae23606015f7036a4348df58c389ca66b).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotStartSaveDocument()

| void Application::slotStartSaveDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _doc_ ,   
---|---|---|---  
|  | const std::string & | _filename_  
| ) | |   
protected  
  
References
[signalStartSaveDocument](../../da/dbf/classApp_1_1Application.html#aa14789336dc85be7a56eaad3d073ebe9).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## ◆ slotUndoDocument()

| void Application::slotUndoDocument  | ( | const [App::Document](../../d8/d3e/classApp_1_1Document.html) & | _d_| ) |   
---|---|---|---|---|---  
protected  
  
References
[signalUndoDocument](../../da/dbf/classApp_1_1Application.html#a08b81cccde7cb8e4310499eef2a397de).

Referenced by
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b).

## Friends And Related Function Documentation

## ◆ App::Document

| [friend](../../d7/d23/classfriend.html) class
[App::Document](../../d8/d3e/classApp_1_1Document.html)  
---  
friend  
  
## ◆ ApplicationObserver

| [friend](../../d7/d23/classfriend.html) class ApplicationObserver  
---  
friend  
  
## ◆ AutoTransaction

| [friend](../../d7/d23/classfriend.html) class
[AutoTransaction](../../dd/d19/classApp_1_1AutoTransaction.html)  
---  
friend  
  
## ◆ GetApplication

| [Application](../../da/dbf/classApp_1_1Application.html) & GetApplication  | ( | void  | | ) |   
---|---|---|---|---|---  
friend  
  
Singleton getter of the
[Application](../../da/dbf/classApp_1_1Application.html "The Application The
root of the whole application.").

Referenced by
[App::Application::TransactionSignaller::TransactionSignaller()](../../dc/d13/classApp_1_1Application_1_1TransactionSignaller.html#a76fdc61ffaddbe87d16b9c153ebd52b1),
and
[App::Application::TransactionSignaller::~TransactionSignaller()](../../dc/d13/classApp_1_1Application_1_1TransactionSignaller.html#a1f32327336057334e85f616aeb14ca7d).

## Member Data Documentation

## ◆ signalAbortTransaction

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalAbortTransaction  
---  
  
Referenced by
[slotAbortTransaction()](../../da/dbf/classApp_1_1Application.html#a06e511b2cd5a4443818c668ebc9014b1).

## ◆ signalActivatedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Application::signalActivatedObject  
---  
  
signal on activated Object

Referenced by
[slotActivatedObject()](../../da/dbf/classApp_1_1Application.html#ad726ef79a1bd4f878bf325784581a047).

## ◆ signalActiveDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalActiveDocument  
---  
  
signal on activating [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")

Referenced by
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[App::DocumentObserver::DocumentObserver()](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71),
[setActiveDocument()](../../da/dbf/classApp_1_1Application.html#a0fc854f2fe5aa39deebf4f8f436e5f94),
and
[Gui::TaskView::TaskView::TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#aa4e4f7cddfbcf1ddfc35ce4cec275b73).

## ◆ signalAddedDynamicExtension

boost::signals2::signal<void (const
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)&,
std::string extension)> App::Application::signalAddedDynamicExtension  
---  
  
signal after the extension was added

## ◆ signalAppendDynamicProperty

boost::signals2::signal<void (const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalAppendDynamicProperty  
---  
  
signal on adding a dynamic property

Referenced by
[App::DynamicProperty::addDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a7b2c4e60658c8e9481d478affbe5f88e),
and
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34).

## ◆ signalBeforeAddingDynamicExtension

boost::signals2::signal<void (const
[App::ExtensionContainer](../../d6/d76/classApp_1_1ExtensionContainer.html)&,
std::string extension)> App::Application::signalBeforeAddingDynamicExtension  
---  
  
signal before adding the extension

## ◆ signalBeforeChangeDocument

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalBeforeChangeDocument  
---  
  
signal before change of doc property

Referenced by
[slotBeforeChangeDocument()](../../da/dbf/classApp_1_1Application.html#a4220212a2b53e4b8d6301196b4952dc5).

## ◆ signalBeforeChangeObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalBeforeChangeObject  
---  
  
signal on changed Object

Referenced by
[slotBeforeChangeObject()](../../da/dbf/classApp_1_1Application.html#a1f3693850c25e228c864936c8f184e69).

## ◆ signalBeforeCloseTransaction

boost::signals2::signal<void ([bool](../../d9/db9/classbool.html))>
App::Application::signalBeforeCloseTransaction  
---  
  
signal before close/abort active transaction

## ◆ signalBeforeRecomputeDocument

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalBeforeRecomputeDocument  
---  
  
signal before recomputed document

Referenced by
[slotBeforeRecompute()](../../da/dbf/classApp_1_1Application.html#abe70fa9ac1b478b8af5bf70e9dadbd6b).

## ◆ signalChangedDocument

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalChangedDocument  
---  
  
signal on changed doc property

Referenced by
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
and
[slotChangedDocument()](../../da/dbf/classApp_1_1Application.html#a452e6b15d130b6591f6ff866ac25af79).

## ◆ signalChangedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalChangedObject  
---  
  
signal on changed Object

Referenced by
[PartGui::DlgBooleanOperation::DlgBooleanOperation()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a9d9f1182519df949d604569a6a3e0f3d),
[ShapeCache::init()](../../d5/d4b/structShapeCache.html#a6928c42f75e712eb958a0624a0a1c04d),
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[slotChangedObject()](../../da/dbf/classApp_1_1Application.html#a0b5cc52e99eb30dc897959a050904559),
and
[MeshGui::MeshFillHole::startEditing()](../../d5/d4f/classMeshGui_1_1MeshFillHole.html#a611c571141e0f653b195fcc94e68a191).

## ◆ signalChangePropertyEditor

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalChangePropertyEditor  
---  
  
signal on about changing the editor mode of a property

Referenced by
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[slotChangePropertyEditor()](../../da/dbf/classApp_1_1Application.html#a6cd9752f5d95bce3f2942f5c8be8ecd1),
and
[PartDesignGui::TaskHoleParameters::TaskHoleParameters()](../../db/d4a/classPartDesignGui_1_1TaskHoleParameters.html#aed07ebf7cad6b7cff0c7597137c91662).

## ◆ signalCloseTransaction

boost::signals2::signal<void ([bool](../../d9/db9/classbool.html))>
App::Application::signalCloseTransaction  
---  
  
signal after close/abort active transaction

## ◆ signalCommitTransaction

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalCommitTransaction  
---  
  
Referenced by
[slotCommitTransaction()](../../da/dbf/classApp_1_1Application.html#a0f5b88b7f15a92bcd03f01e77ba8bcb1).

## ◆ signalDeletedDocument

boost::signals2::signal<void ()> App::Application::signalDeletedDocument  
---  
  
signal on already deleted [Document](../../d8/d3e/classApp_1_1Document.html
"The document class.")

Referenced by
[closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244),
and
[Gui::TaskView::TaskView::TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#aa4e4f7cddfbcf1ddfc35ce4cec275b73).

## ◆ signalDeletedObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Application::signalDeletedObject  
---  
  
signal on deleted Object

Referenced by
[PartGui::DlgFilletEdges::DlgFilletEdges()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a16463a511a5a288028ef96edb2b3aef6),
[ShapeCache::init()](../../d5/d4b/structShapeCache.html#a6928c42f75e712eb958a0624a0a1c04d),
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[Gui::SelectionSingleton::SelectionSingleton()](../../d4/dca/classGui_1_1SelectionSingleton.html#a7d8f654b071cb1d530bb39dadc49620f),
and
[slotDeletedObject()](../../da/dbf/classApp_1_1Application.html#ad6e7f304a6bf2a014d75039b8caa8837).

## ◆ signalDeleteDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalDeleteDocument  
---  
  
signal on document getting deleted

Referenced by
[PartDesignGui::Workbench::activated()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced),
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[closeDocument()](../../da/dbf/classApp_1_1Application.html#a7816f767a8b2cca4cc46fdca1bc57244),
[PartGui::DlgFilletEdges::DlgFilletEdges()](../../d0/d29/classPartGui_1_1DlgFilletEdges.html#a16463a511a5a288028ef96edb2b3aef6),
[App::DocumentObserver::DocumentObserver()](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71),
[ShapeCache::init()](../../d5/d4b/structShapeCache.html#a6928c42f75e712eb958a0624a0a1c04d),
[MeasureInfo::MeasureInfo()](../../d5/dbd/structMeasureInfo.html#ac636bdb4aa3543a855c824696196b5c3),
[DrawingGui::OrthoViews::OrthoViews()](../../dc/d41/classDrawingGui_1_1OrthoViews.html#ad9c99867cbd96fff40a1c05750e12033),
[Gui::DocumentWeakPtrT::Private::Private()](../../df/db9/classDocumentWeakPtrT_1_1Private.html#ab5c208ca0616f4cd278925efa1c31e04),
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461),
and
[App::DocumentObjectWeakPtrT::Private::set()](../../d8/de6/classDocumentObjectWeakPtrT_1_1Private.html#a1d60074d4be26a28fa02bc5792df3835).

## ◆ signalFinishOpenDocument

boost::signals2::signal<void ()> App::Application::signalFinishOpenDocument  
---  
  
signal on finished opening document(s)

Referenced by
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

## ◆ signalFinishRestoreDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalFinishRestoreDocument  
---  
  
signal on restoring [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")

Referenced by
[PartDesignGui::Workbench::activated()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced),
[App::Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5),
[Cloud::Module::cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4),
and
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1).

## ◆ signalFinishSaveDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&, const std::string&)>
App::Application::signalFinishSaveDocument  
---  
  
signal on saved [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")

Referenced by
[slotFinishSaveDocument()](../../da/dbf/classApp_1_1Application.html#a609e60d2806e8728c7bdb47840ea2d48).

## ◆ signalNewDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&,
[bool](../../d9/db9/classbool.html))> App::Application::signalNewDocument  
---  
  
signal on new [Document](../../d8/d3e/classApp_1_1Document.html "The document
class.")

Referenced by
[PartDesignGui::Workbench::activated()](../../d4/d0c/classPartDesignGui_1_1Workbench.html#a0d32868fa25b4fc619def407fd8abced),
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[App::Document::clearDocument()](../../d8/d3e/classApp_1_1Document.html#a7dbed73a3305f1a23c3ba98eaa8bbcbb),
[App::DocumentObserver::DocumentObserver()](../../d5/d52/classApp_1_1DocumentObserver.html#a413aef62f11ee673feff12fb7968cd71),
[newDocument()](../../da/dbf/classApp_1_1Application.html#ace9191c9425f6bc69f5d55d79b22589b),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ signalNewObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Application::signalNewObject  
---  
  
signal on new Object

Referenced by
[PartGui::DlgBooleanOperation::DlgBooleanOperation()](../../d0/d2b/classPartGui_1_1DlgBooleanOperation.html#a9d9f1182519df949d604569a6a3e0f3d),
and
[slotNewObject()](../../da/dbf/classApp_1_1Application.html#aa6835d277021785cdd0f9ae038472762).

## ◆ signalObjectRecomputed

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Application::signalObjectRecomputed  
---  
  
signal on recomputed document object

Referenced by
[slotRecomputedObject()](../../da/dbf/classApp_1_1Application.html#a0c4c8807007b3ec248e7e4afc3bb1567).

## ◆ signalOpenTransaction

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&, std::string)>
App::Application::signalOpenTransaction  
---  
  
Referenced by
[slotOpenTransaction()](../../da/dbf/classApp_1_1Application.html#ae6d03ca955417ba7789ee4fc6333792b).

## ◆ signalPendingReloadDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalPendingReloadDocument  
---  
  
signal on pending reloading of a partial
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.")

Referenced by
[App::Document::afterRestore()](../../d8/d3e/classApp_1_1Document.html#ae614a451288199cde7cc752cd0b000f5).

## ◆ signalRecomputed

boost::signals2::signal<void (const
[App::Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalRecomputed  
---  
  
signal on recomputed document

Referenced by
[slotRecomputed()](../../da/dbf/classApp_1_1Application.html#ac1a39ddbde61ec1b603e8f3dc35af59e).

## ◆ signalRedo

boost::signals2::signal<void ()> App::Application::signalRedo  
---  
  
signal on application wide redo

Referenced by
[Gui::Document::redo()](../../de/d4e/classGui_1_1Document.html#a88f1cb6c87e53dde4315c1d90d84bbaf).

## ◆ signalRedoDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalRedoDocument  
---  
  
signal on redo in document

Referenced by
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[slotRedoDocument()](../../da/dbf/classApp_1_1Application.html#a8f9128275989a896d2f6c55d5af4785b),
and
[Gui::TaskView::TaskView::TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#aa4e4f7cddfbcf1ddfc35ce4cec275b73).

## ◆ signalRelabelDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalRelabelDocument  
---  
  
signal on relabeling [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") (user name)

Referenced by
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a),
and
[App::PropertyExpressionContainer::PropertyExpressionContainer()](../../db/da0/classApp_1_1PropertyExpressionContainer.html#ad2a31b1f155cff49ba56cd43bfa0c6da).

## ◆ signalRelabelObject

boost::signals2::signal<void (const
[App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)&)>
App::Application::signalRelabelObject  
---  
  
signal on relabeled Object

Referenced by
[slotRelabelObject()](../../da/dbf/classApp_1_1Application.html#a5a3dcdcb74979ab007577f3684598c5a).

## ◆ signalRemoveDynamicProperty

boost::signals2::signal<void (const
[App::Property](../../d0/da9/classApp_1_1Property.html)&)>
App::Application::signalRemoveDynamicProperty  
---  
  
signal on about removing a dynamic property

Referenced by
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
and
[App::DynamicProperty::removeDynamicProperty()](../../d5/d76/classApp_1_1DynamicProperty.html#a8e4c6ca6912ea2f53be583ba0ff7d7b6).

## ◆ signalRenameDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalRenameDocument  
---  
  
signal on renaming [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.") (internal name)

Referenced by
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
and
[renameDocument()](../../da/dbf/classApp_1_1Application.html#a4b3708bc7e111c2f20c499c9a441172c).

## ◆ signalSaveDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalSaveDocument  
---  
  
signal on saving [Document](../../d8/d3e/classApp_1_1Document.html "The
document class.")

Referenced by
[App::Document::saveToFile()](../../d8/d3e/classApp_1_1Document.html#a3146b0eacd6ff04482041f56547a554d).

## ◆ signalShowHidden

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalShowHidden  
---  
  
signal on show hidden items

Referenced by
[Gui::Application::Application()](../../d9/da8/classGui_1_1Application.html#aaaba6487282e43abbe7aab88a88669dd),
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[App::Document::onChanged()](../../d8/d3e/classApp_1_1Document.html#ab0259fb189ab0c44b820d72b2d9fe17a).

## ◆ signalStartOpenDocument

boost::signals2::signal<void ()> App::Application::signalStartOpenDocument  
---  
  
signal on start opening document(s)

Referenced by
[openDocuments()](../../da/dbf/classApp_1_1Application.html#a42dadb0dd240c779c75ca4cf36a8a728).

## ◆ signalStartRestoreDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalStartRestoreDocument  
---  
  
signal on starting to restore
[Document](../../d8/d3e/classApp_1_1Document.html "The document class.")

Referenced by
[Cloud::Module::cloudRestore()](../../d9/d80/classCloud_1_1Module.html#aa40c76175c8f2a0eed92b8a81696a7c4),
[Gui::Document::Document()](../../de/d4e/classGui_1_1Document.html#a8fb2aeb623377f2d4797f30e22d7a0b1),
and
[App::Document::restore()](../../d8/d3e/classApp_1_1Document.html#a90df26ded43652e65791d5f1cdd68461).

## ◆ signalStartSaveDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&, const std::string&)>
App::Application::signalStartSaveDocument  
---  
  
signal on starting to save [Document](../../d8/d3e/classApp_1_1Document.html
"The document class.")

Referenced by
[slotStartSaveDocument()](../../da/dbf/classApp_1_1Application.html#ad4b9071ef9241b25392537dd269cd823).

## ◆ signalUndo

boost::signals2::signal<void ()> App::Application::signalUndo  
---  
  
signal on application wide undo

Referenced by
[Gui::Document::undo()](../../de/d4e/classGui_1_1Document.html#a47526ed6083330d1248b4a3553f5aa33).

## ◆ signalUndoDocument

boost::signals2::signal<void (const
[Document](../../d8/d3e/classApp_1_1Document.html)&)>
App::Application::signalUndoDocument  
---  
  
signal on undo in document

Referenced by
[Gui::PropertyView::PropertyView()](../../d8/d18/classGui_1_1PropertyView.html#acd6596af6b2698118772d24f96a7cc34),
[slotUndoDocument()](../../da/dbf/classApp_1_1Application.html#a72d52b675d7da0a4bf6dad8c0ed713a8),
and
[Gui::TaskView::TaskView::TaskView()](../../d9/dc0/classGui_1_1TaskView_1_1TaskView.html#aa4e4f7cddfbcf1ddfc35ce4cec275b73).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Application.h
  * FreeCAD/src/App/Application.cpp
  * FreeCAD/src/App/ApplicationPy.cpp
  * FreeCAD/src/App/AutoTransaction.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

