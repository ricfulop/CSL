---
url: https://freecad.github.io/SourceDoc/d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html
scraped_at: 2025-09-08T14:53:22.142091
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AddonManagerTest](../../d9/dd4/namespaceAddonManagerTest.html)
  * [app](../../d0/d7d/namespaceAddonManagerTest_1_1app.html)
  * [test_macro](../../d9/db6/namespaceAddonManagerTest_1_1app_1_1test__macro.html)
  * [TestMacro](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html)

[List of all members](../../dd/da4/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro-members.html) | Public Member Functions | Public Attributes | Static Public Attributes

AddonManagerTest.app.test_macro.TestMacro Class Reference

##  Public Member Functions  
  
---  
[Macro](../../d1/dca/classaddonmanager__macro_1_1Macro.html) | [generate_macro](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad47b65fd23ca9eee68270fc91099c871) (self, Dict[[str](../../d9/d36/classstr.html), [str](../../d9/d36/classstr.html)] replacements={})  
os.PathLike | [generate_macro_file](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393) (self, Dict[[str](../../d9/d36/classstr.html), [str](../../d9/d36/classstr.html)] replacements={})  
def | [setUp](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a9199816c48a1ac29867c82512a7a6938) (self)  
def | [test_basic_metadata](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad38da426d4b95c5e23c9d9012e2bf4ad) (self)  
def | [test_other_files](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a26e199bdd6b800bb29cc1349a9fa837a) (self)  
def | [test_version_from_date](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ae6ea4b061fdea8e85107be6268619f72) (self)  
def | [test_version_from_float](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a5cb1d7204b13ae8e30b695b5b4163ec8) (self)  
def | [test_version_from_int](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad92f8b4236b2e27be2f0ca703a864100) (self)  
def | [test_version_from_string](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a08161956390adc2653e55c6bb3988b24) (self)  
def | [test_xpm](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a8106d8d9e905ecdf9cb56c2df1c74bbf) (self)  
  
##  Public Attributes  
  
---  
|
[test_dir](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a5de92e603b4cf077194d50de1598a4ba)  
  
##  Static Public Attributes  
  
---  
string | [MODULE](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#aa2367186d04f0b307040183ff06c76eb) = "test_macro"  
  
## Member Function Documentation

## ◆ generate_macro()

[Macro](../../d1/dca/classaddonmanager__macro_1_1Macro.html) AddonManagerTest.app.test_macro.TestMacro.generate_macro  | ( |  | _self_ ,   
---|---|---|---  
|  | Dict[[str](../../d9/d36/classstr.html),[str](../../d9/d36/classstr.html)]  | _replacements_ = `{}`  
| ) | |   
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro_file()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393).

Referenced by
[AddonManagerTest.app.test_macro.TestMacro.test_basic_metadata()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad38da426d4b95c5e23c9d9012e2bf4ad),
[AddonManagerTest.app.test_macro.TestMacro.test_other_files()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a26e199bdd6b800bb29cc1349a9fa837a),
and
[AddonManagerTest.app.test_macro.TestMacro.test_version_from_string()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a08161956390adc2653e55c6bb3988b24).

## ◆ generate_macro_file()

os.PathLike AddonManagerTest.app.test_macro.TestMacro.generate_macro_file  | ( |  | _self_ ,   
---|---|---|---  
|  | Dict[[str](../../d9/d36/classstr.html),[str](../../d9/d36/classstr.html)]  | _replacements_ = `{}`  
| ) | |   
  
References
[AddonManagerTest.app.test_addon.TestAddon.test_dir](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#acf716d788a9011fac60cf4878cca2c03),
[AddonManagerTest.app.test_macro.TestMacro.test_dir](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a5de92e603b4cf077194d50de1598a4ba),
[AddonManagerTest.app.test_utilities.TestUtilities.test_dir](../../dc/d08/classAddonManagerTest_1_1app_1_1test__utilities_1_1TestUtilities.html#ac282577ee2352bd96ab0dd0ddd32fae3),
[MeshTestsApp.NastranReader.test_dir](../../d4/d75/classMeshTestsApp_1_1NastranReader.html#aa1614b57001d9bff4d51c94d5313bfe9),
[OpenSCADTest.app.test_importCSG.TestImportCSG.test_dir](../../d3/db0/classOpenSCADTest_1_1app_1_1test__importCSG_1_1TestImportCSG.html#a78b7acda16372e5118337febd17f5ad4),
and
[Mod.Test.Metadata.TestMetadata.test_dir](../../de/d9a/classMod_1_1Test_1_1Metadata_1_1TestMetadata.html#a2b487966cc405275eeaa42828dd434e1).

Referenced by
[AddonManagerTest.app.test_macro.TestMacro.generate_macro()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad47b65fd23ca9eee68270fc91099c871),
[AddonManagerTest.app.test_macro.TestMacro.test_version_from_date()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ae6ea4b061fdea8e85107be6268619f72),
[AddonManagerTest.app.test_macro.TestMacro.test_version_from_float()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a5cb1d7204b13ae8e30b695b5b4163ec8),
[AddonManagerTest.app.test_macro.TestMacro.test_version_from_int()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad92f8b4236b2e27be2f0ca703a864100),
and
[AddonManagerTest.app.test_macro.TestMacro.test_xpm()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a8106d8d9e905ecdf9cb56c2df1c74bbf).

## ◆ setUp()

def AddonManagerTest.app.test_macro.TestMacro.setUp  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ test_basic_metadata()

def AddonManagerTest.app.test_macro.TestMacro.test_basic_metadata  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad47b65fd23ca9eee68270fc91099c871).

## ◆ test_other_files()

def AddonManagerTest.app.test_macro.TestMacro.test_other_files  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad47b65fd23ca9eee68270fc91099c871).

## ◆ test_version_from_date()

def AddonManagerTest.app.test_macro.TestMacro.test_version_from_date  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro_file()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393).

## ◆ test_version_from_float()

def AddonManagerTest.app.test_macro.TestMacro.test_version_from_float  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro_file()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393).

## ◆ test_version_from_int()

def AddonManagerTest.app.test_macro.TestMacro.test_version_from_int  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro_file()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393).

## ◆ test_version_from_string()

def AddonManagerTest.app.test_macro.TestMacro.test_version_from_string  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#ad47b65fd23ca9eee68270fc91099c871).

## ◆ test_xpm()

def AddonManagerTest.app.test_macro.TestMacro.test_xpm  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[AddonManagerTest.app.test_macro.TestMacro.generate_macro_file()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393).

## Member Data Documentation

## ◆ MODULE

| string AddonManagerTest.app.test_macro.TestMacro.MODULE = "test_macro"  
---  
static  
  
Referenced by
[PathTests.TestPathLog.TestPathLog.test00()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#ae5d52e0b883a9f6dd76684a67e73dd2d),
[PathTests.TestPathLog.TestPathLog.test10()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#a3c85d5500eb9a804c0e66ae2912af190),
[PathTests.TestPathLog.TestPathLog.test11()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#a09d0ed8e5d96a536b0b3e9d73ef515ff),
[PathTests.TestPathLog.TestPathLog.test12()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#ac9f0d554fafea0146bfbe61c4ac1d938),
[PathTests.TestPathLog.TestPathLog.test13()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#a6a150d007b5b1b575761257011f3edf5),
[PathTests.TestPathLog.TestPathLog.test14()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#a551e442160c2855b7b2bba56750377c8),
[PathTests.TestPathLog.TestPathLog.test51()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#a88157a349390900c71d0fbc362e9d3c0),
[PathTests.TestPathLog.TestPathLog.test60()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#adec169f2ea21dd7ff2f53324dedc0afd),
and
[PathTests.TestPathLog.TestPathLog.test61()](../../dc/d0c/classPathTests_1_1TestPathLog_1_1TestPathLog.html#aa04c2277a2d3624a2812bd880cbb0bd5).

## ◆ test_dir

AddonManagerTest.app.test_macro.TestMacro.test_dir  
---  
  
Referenced by
[AddonManagerTest.app.test_macro.TestMacro.generate_macro_file()](../../d1/d75/classAddonManagerTest_1_1app_1_1test__macro_1_1TestMacro.html#a59a0865e577603dc7cca0bc3e42e4393),
[AddonManagerTest.app.test_addon.TestAddon.test_contains_functions()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#ab9a97fa211c080e109d39c699ec68b8a),
[Mod.Test.Metadata.TestMetadata.test_content_types()](../../de/d9a/classMod_1_1Test_1_1Metadata_1_1TestMetadata.html#a9b0babd8e20ba1f3dc8aaf07c8a3cc25),
[Mod.Test.Metadata.TestMetadata.test_copy_constructor()](../../de/d9a/classMod_1_1Test_1_1Metadata_1_1TestMetadata.html#acde0c957442c03ee7400a8ef0433764c),
[AddonManagerTest.app.test_addon.TestAddon.test_create_from_macro()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#abd13305d54ad6810d6a5011e42d62cf7),
[AddonManagerTest.app.test_addon.TestAddon.test_display_name()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#aefdb4a966be4c740a048b3a31e0ad178),
[AddonManagerTest.app.test_utilities.TestUtilities.test_get_macro_version_from_file()](../../dc/d08/classAddonManagerTest_1_1app_1_1test__utilities_1_1TestUtilities.html#a793f9d18a8a316be7cd2149c214a99c2),
[OpenSCADTest.app.test_importCSG.TestImportCSG.test_import_surface()](../../d3/db0/classOpenSCADTest_1_1app_1_1test__importCSG_1_1TestImportCSG.html#a29ddacce7390886b84a1eab8beb9ae07),
[AddonManagerTest.app.test_addon.TestAddon.test_internal_workbench_list()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#a113554ba7b4e2a3cc29151274c9a2f63),
[AddonManagerTest.app.test_addon.TestAddon.test_metadata_loading()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#a5aa79915650354eda518999b6a8a98ad),
[OpenSCADTest.app.test_importCSG.TestImportCSG.test_open_csg()](../../d3/db0/classOpenSCADTest_1_1app_1_1test__importCSG_1_1TestImportCSG.html#af4b9608a2ddb87a4f1788d878ebd5c84),
[OpenSCADTest.app.test_importCSG.TestImportCSG.test_open_scad()](../../d3/db0/classOpenSCADTest_1_1app_1_1test__importCSG_1_1TestImportCSG.html#ac3f6a18176fc2141588593ef419da1b5),
[AddonManagerTest.app.test_addon.TestAddon.test_tag_extraction()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#afa72988d8ffb238a49d447f21805ddef),
[Mod.Test.Metadata.TestMetadata.test_toplevel_tags()](../../de/d9a/classMod_1_1Test_1_1Metadata_1_1TestMetadata.html#a410559c72c508f505c803b0a806a3bf8),
[AddonManagerTest.app.test_addon.TestAddon.test_version_check()](../../d4/dbc/classAddonManagerTest_1_1app_1_1test__addon_1_1TestAddon.html#a9d83f9c259b9b50a623debece1655378),
and
[Mod.Test.Metadata.TestMetadata.test_xml_constructor()](../../de/d9a/classMod_1_1Test_1_1Metadata_1_1TestMetadata.html#a9545c8a6ab1d099a38fbbee581238cef).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/AddonManager/AddonManagerTest/app/test_macro.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

