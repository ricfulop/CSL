---
url: https://freecad.github.io/SourceDoc/d7/de5/structApp_1_1Meta_1_1Url.html
scraped_at: 2025-09-08T14:53:38.217849
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Meta](../../d9/dcf/namespaceApp_1_1Meta.html)
  * [Url](../../d7/de5/structApp_1_1Meta_1_1Url.html)

[List of all members](../../d8/d1f/structApp_1_1Meta_1_1Url-members.html) | Public Member Functions | Public Attributes

App::Meta::Url Struct Reference

A URL, including type information (e.g.
[More...](../../d7/de5/structApp_1_1Meta_1_1Url.html#details)

`#include <Metadata.h>`

##  Public Member Functions  
  
---  
|
[Url](../../d7/de5/structApp_1_1Meta_1_1Url.html#a97660faa6422e66b2d189df9b7e78ac1)
()=default  
|
[Url](../../d7/de5/structApp_1_1Meta_1_1Url.html#a29641a3c872008e5d3ed6ddb45461db9)
(const std::string &[location](../../d1/da0/classint.html),
[UrlType](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508a)
[type](../../d9/d98/classtype.html))  
|
[Url](../../d7/de5/structApp_1_1Meta_1_1Url.html#a1c80758310e4daf15c63d812fb387147)
(const XERCES_CPP_NAMESPACE::DOMElement *e)  
  
##  Public Attributes  
  
---  
std::string | [branch](../../d7/de5/structApp_1_1Meta_1_1Url.html#acc52673a932991ab549f05c90266d5d1)  
std::string | [location](../../d7/de5/structApp_1_1Meta_1_1Url.html#aa40afabdf8d53cdd4f29dd5594effeda)  
[UrlType](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508a) | [type](../../d7/de5/structApp_1_1Meta_1_1Url.html#ab01fceea6aa7ca8cd4e228c750f0c528)  
  
## Detailed Description

A URL, including type information (e.g.

website, repository, or bugtracker, in package.xml)

## Constructor & Destructor Documentation

## ◆ Url() [1/3]

| App::Meta::Url::Url  | ( | | ) |   
---|---|---|---|---  
default  
  
## ◆ Url() [2/3]

Meta::Url::Url  | ( | const std::string & | _location_ ,   
---|---|---|---  
|  | [UrlType](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508a) | _type_  
| ) | |   
  
## ◆ Url() [3/3]

| Meta::Url::Url  | ( | const XERCES_CPP_NAMESPACE::DOMElement *  | _e_| ) |   
---|---|---|---|---|---  
explicit  
  
References
[App::Meta::bugtracker](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508aa2f3e99196101a400c5db6be5fd25dfb6),
[App::Meta::documentation](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508aa55876228853abf632dec9346a4f372ec),
[App::Meta::readme](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508aa3905d7917f2b3429490b01cfb60d8f5b),
[App::Meta::repository](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508aab3f2035551f6e48c67489ace9f588f94),
[StrXUTF8::str](../../d7/d9a/classStrXUTF8.html#ab8f96bd3cf6c91dc259c03328034c44b),
and
[App::Meta::website](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508aad1befa03c79ca0b84ecc488dea96bc68).

## Member Data Documentation

## ◆ branch

std::string App::Meta::Url::branch  
---  
  
Referenced by
[Addon.Addon::set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
and
[Addon.Addon::verify_url_and_branch()](../../d8/d91/classAddon_1_1Addon.html#a920e70c1e01170868b69690eff7913e3).

## ◆ location

std::string App::Meta::Url::location  
---  
  
Referenced by
[draftguitools.gui_circulararray.CircularArray::Activated()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#add24faedacfd2c2ad7f159032c044931),
[draftguitools.gui_polararray.PolarArray::Activated()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#acc402dde8d5c1b007e3ac33f06340df6),
[automotive_design.revolved_area_solid::axis_line()](../../d4/ded/classautomotive__design_1_1revolved__area__solid.html#ae7714359aef57b10dc9d110c4c95109c),
[automotive_design.surface_of_revolution::axis_line()](../../dc/d07/classautomotive__design_1_1surface__of__revolution.html#ac11430bfca20d807bd7fbb1de4555324),
[automotive_design.revolved_face_solid::axis_line()](../../d2/d81/classautomotive__design_1_1revolved__face__solid.html#a88ba8cae1c9e693beda33bf96a0423ca),
[ifc2x3.ifcsurfaceofrevolution::axisline()](../../db/d1b/classifc2x3_1_1ifcsurfaceofrevolution.html#a0689126db6a08f9f1183f65515b53370),
[ifc2x3.ifcrevolvedareasolid::axisline()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#ad7a180e86495ea93d5acb25ffcc33ffa),
[ifc4.ifcsurfaceofrevolution::axisline()](../../d4/de7/classifc4_1_1ifcsurfaceofrevolution.html#adf527bd278ddce78734fc2b01bec7b37),
[ifc4.ifcrevolvedareasolid::axisline()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a45efcb80c8963331649e13f991ec7534),
[ifc4.ifcrevolvedareasolid::axisstartinxy()](../../d0/db3/classifc4_1_1ifcrevolvedareasolid.html#a76b11dffac1f3f7f53c5dfeef5227626),
[draftguitools.gui_circulararray.CircularArray::completed()](../../dc/dd7/classdraftguitools_1_1gui__circulararray_1_1CircularArray.html#abc4dc219237d7614302cefbc9599ac50),
[draftguitools.gui_polararray.PolarArray::completed()](../../dd/dc9/classdraftguitools_1_1gui__polararray_1_1PolarArray.html#adf72543f71963c7a5a4dee8db0ab1b00),
[ifc2x3.ifcplacement::dim()](../../dd/dfd/classifc2x3_1_1ifcplacement.html#ac4dbcef9f43207432d3fa6d838dbdfb7),
[ifc4.ifcplacement::dim()](../../d4/da3/classifc4_1_1ifcplacement.html#a4ff119d99b8ac53bebec7145128d0452),
[ifc2x3.ifcexternalreference::wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc4.ifcexternalreference::wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
and
[ifc2x3.ifcrevolvedareasolid::wr31()](../../d1/d86/classifc2x3_1_1ifcrevolvedareasolid.html#a16ccd5dc8889fd10923e40182318836b).

## ◆ type

[UrlType](../../d9/dcf/namespaceApp_1_1Meta.html#abf6b6993d92cf7756bb716cc02a8508a)
App::Meta::Url::type  
---  
  
Referenced by
[ArchProfile.ProfileTaskPanel::accept()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a2506d93eee0ae9e8570d71e066425999),
and
[ArchProfile.ProfileTaskPanel::retranslateUi()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a8b6ffa229d56acdd0aabe8fb92de728b).

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/Metadata.h
  * FreeCAD/src/App/Metadata.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

