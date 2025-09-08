---
url: https://freecad.github.io/SourceDoc/dc/d60/classApp_1_1DocumentT.html
scraped_at: 2025-09-08T14:54:29.402632
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [DocumentT](../../dc/d60/classApp_1_1DocumentT.html)

[List of all members](../../de/d38/classApp_1_1DocumentT-members.html) | Public Member Functions

App::DocumentT Class Reference

The [DocumentT](../../dc/d60/classApp_1_1DocumentT.html "The DocumentT class
is a helper class to store the name of a document.") class is a helper class
to store the name of a document.
[More...](../../dc/d60/classApp_1_1DocumentT.html#details)

`#include <DocumentObserver.h>`

##  Public Member Functions  
  
---  
|
[DocumentT](../../dc/d60/classApp_1_1DocumentT.html#a802d05772e92c4030cc8a9539aab6b48)
()  
|
[DocumentT](../../dc/d60/classApp_1_1DocumentT.html#ab4986862c864835c2b18d18307af6a1f)
(const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) &)  
|
[DocumentT](../../dc/d60/classApp_1_1DocumentT.html#aa7a848e0a66a84df7d5ab4072fcca40b)
(const std::string &)  
|
[DocumentT](../../dc/d60/classApp_1_1DocumentT.html#a11d9e948428451b69126a069fc3df207)
([Document](../../d8/d3e/classApp_1_1Document.html) *)  
[Document](../../d8/d3e/classApp_1_1Document.html) * | [getDocument](../../dc/d60/classApp_1_1DocumentT.html#a320fef7d6acc485cb077ff5acaad8c7b) () const  
const std::string & | [getDocumentName](../../dc/d60/classApp_1_1DocumentT.html#afe994716a910d5b29c8953737a9628c2) () const  
std::string | [getDocumentPython](../../dc/d60/classApp_1_1DocumentT.html#a91f967446cbdbc7ad71c3565304ef193) () const  
[bool](../../d9/db9/classbool.html) | [operator<](../../dc/d60/classApp_1_1DocumentT.html#ae51065daa7415254bdb178c6af189df3) (const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) &other) const  
void | [operator=](../../dc/d60/classApp_1_1DocumentT.html#af2d7a12ada933a7ac65f1bd82c50dfd2) (const [Document](../../d8/d3e/classApp_1_1Document.html) *)  
void | [operator=](../../dc/d60/classApp_1_1DocumentT.html#aebddd8597f9a15a0a549f949da33c98e) (const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) &)  
void | [operator=](../../dc/d60/classApp_1_1DocumentT.html#a66c0755cc9dfd1755bdeaabf976ecc0b) (const std::string &)  
[bool](../../d9/db9/classbool.html) | [operator==](../../dc/d60/classApp_1_1DocumentT.html#a98c1579af26adc0c05723fc5a5f0b9be) (const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) &other) const  
|
[~DocumentT](../../dc/d60/classApp_1_1DocumentT.html#ab36b86ce661402b763fd2d1d501eed2c)
()  
  
## Detailed Description

The [DocumentT](../../dc/d60/classApp_1_1DocumentT.html "The DocumentT class
is a helper class to store the name of a document.") class is a helper class
to store the name of a document.

This can be useful when you cannot rely on that the document still exists when
you have to access it.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ DocumentT() [1/4]

DocumentT::DocumentT  | ( | | ) |   
---|---|---|---|---  
  
Constructor

## ◆ DocumentT() [2/4]

DocumentT::DocumentT  | ( | [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ DocumentT() [3/4]

DocumentT::DocumentT  | ( | const std::string & | _name_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ DocumentT() [4/4]

DocumentT::DocumentT  | ( | const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
Constructor

## ◆ ~DocumentT()

DocumentT::~DocumentT  | ( | | ) |   
---|---|---|---|---  
  
Destructor

## Member Function Documentation

## ◆ getDocument()

[Document](../../d8/d3e/classApp_1_1Document.html) * DocumentT::getDocument  | ( | void  | | ) |  const  
---|---|---|---|---|---  
  
Get a pointer to the document or 0 if it doesn't exist any more.

References
[App::GetApplication()](../../dd/dc2/namespaceApp.html#a84dbe47fe47bf688ae33c4bc0b1296a4),
and
[App::Application::getDocument()](../../da/dbf/classApp_1_1Application.html#a17472bb3dfacd07074016c3bcc4a270d).

## ◆ getDocumentName()

const std::string & DocumentT::getDocumentName  | ( | | ) |  const  
---|---|---|---|---  
  
Get the name of the document.

## ◆ getDocumentPython()

std::string DocumentT::getDocumentPython  | ( | | ) |  const  
---|---|---|---|---  
  
Get the document as Python command.

## ◆ operator<()

[bool](../../d9/db9/classbool.html) App::DocumentT::operator< | ( | const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
## ◆ operator=() [1/3]

void DocumentT::operator=  | ( | const [Document](../../d8/d3e/classApp_1_1Document.html) *  | _doc_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [2/3]

void DocumentT::operator=  | ( | const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) & | _doc_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator=() [3/3]

void DocumentT::operator=  | ( | const std::string & | _name_| ) |   
---|---|---|---|---|---  
  
Assignment operator

## ◆ operator==()

[bool](../../d9/db9/classbool.html) App::DocumentT::operator==  | ( | const [DocumentT](../../dc/d60/classApp_1_1DocumentT.html) & | _other_| ) |  const  
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/DocumentObserver.h
  * FreeCAD/src/App/DocumentObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

