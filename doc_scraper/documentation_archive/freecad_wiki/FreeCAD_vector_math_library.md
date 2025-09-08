---
url: https://wiki.freecad.org/FreeCAD_vector_math_library
title: FreeCAD vector math library
scraped_at: 2025-09-08 16:42:18
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Functions

# FreeCAD vector math library

  * [Page](/FreeCAD_vector_math_library "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:FreeCAD_vector_math_library&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/FreeCAD_vector_math_library)
  * [Edit](/index.php?title=FreeCAD_vector_math_library&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=FreeCAD_vector_math_library&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/FreeCAD_vector_math_library.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=FreeCAD_vector_math_library&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/FreeCAD_vector_math_library)
  * [Edit](/index.php?title=FreeCAD_vector_math_library&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=FreeCAD_vector_math_library&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=FreeCAD_vector_math_library&action=history)

General

  * [What links here](/Special:WhatLinksHere/FreeCAD_vector_math_library "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/FreeCAD_vector_math_library "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=FreeCAD_vector_math_library&oldid=1610030 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=FreeCAD_vector_math_library&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=FreeCAD_vector_math_library&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
FreeCAD+vector+math+library&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-FreeCAD+vector+math+library&language=&task=view "Start translation for this language")
  * [Deutsch](/FreeCAD_vector_math_library/de "FreeCAD Vektor Mathematische Bibliothek \(100% translated\)")
  * English
  * [Türkçe](/FreeCAD_vector_math_library/tr "FreeCAD vector math library/tr \(14% translated\)")
  * [español](/FreeCAD_vector_math_library/es "FreeCAD vector math library \(14% translated\)")
  * [français](/FreeCAD_vector_math_library/fr "Bibliothèque mathématique vectorielle de FreeCAD \(100% translated\)")
  * [italiano](/FreeCAD_vector_math_library/it "Libreria di matematica vettoriale di FreeCAD \(100% translated\)")
  * [polski](/FreeCAD_vector_math_library/pl "Biblioteka matematyczna FreeCAD dla wektorów \(100% translated\)")
  * [română](/FreeCAD_vector_math_library/ro "FreeCAD vector math library/ro \(14% translated\)")
  * [svenska](/FreeCAD_vector_math_library/sv "FreeCAD vector math library \(14% translated\)")
  * [čeština](/FreeCAD_vector_math_library/cs "FreeCAD vector math library \(14% translated\)")
  * [русский](/FreeCAD_vector_math_library/ru "Библиотека векторной математики FreeCAD \(14% translated\)")

## Introduction

This is a [Python](/Python "Python") module containing a couple of useful
functions to manipulate vectors. This library is included in the
[Draft_Workbench](/Draft_Workbench "Draft Workbench") and can be accessed like
this from the Python interpreter:

    
    
    import DraftVecUtils
    

Please note that this module was created a long time ago, when the `Vector`
class didn't have many of its methods. Now these operations can be done by the
Vector class itself.

Although the `DraftVecUtils` module still exists, and it is still used inside
the [Draft Workbench](/Draft_Workbench "Draft Workbench"), it is probably
better to use the `Vector` methods directly for new developments.

## Functions

Vectors are the building bricks of almost all 3D geometric operations, so it
is useful to know a bit about them to understand how these functions can be
useful to you. A couple of good pages to learn the basics of vector math:

  * <https://en.wikipedia.org/wiki/Vector_space>

    
    
    """Vector math library for FreeCAD"""
    
    import math
    import FreeCAD
     
    def add(first, other):
        """add(Vector,Vector) - adds two vectors"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return FreeCAD.Vector(first.x+other.x, first.y+other.y, first.z+other.z)
     
    def sub(first, other): 
        """sub(Vector,Vector) - subtracts second vector from first one"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return FreeCAD.Vector(first.x-other.x, first.y-other.y, first.z-other.z)
     
    def scale(first,scalar):
        """scale(Vector,Float) - scales (multiplies) a vector by a factor"""
        if isinstance(first,FreeCAD.Vector):
            return FreeCAD.Vector(first.x*scalar, first.y*scalar, first.z*scalar)
     
    def length(first):
        """lengh(Vector) - gives vector length"""
        if isinstance(first,FreeCAD.Vector):
            return math.sqrt(first.x*first.x + first.y*first.y + first.z*first.z)
     
    def dist(first, other):
        """dist(Vector,Vector) - returns the distance between both points/vectors"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return length(sub(first,other))
     
    def normalized(first):
        """normalized(Vector) - returns a unit vector"""
        if isinstance(first,FreeCAD.Vector):
            l=length(first)
            return FreeCAD.Vector(first.x/l, first.y/l, first.z/l)
     
    def dotproduct(first, other):
        """dotproduct(Vector,Vector) - returns the dot product of both vectors"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return (first.x*other.x + first.y*other.y + first.z*other.z)
     
    def crossproduct(first, other=FreeCAD.Vector(0,0,1)):
        """crossproduct(Vector,Vector) - returns the cross product of both vectors. 
        If only one is specified, cross product is made with vertical axis, thus returning its perpendicular in XY plane"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return FreeCAD.Vector(first.y*other.z - first.z*other.y, first.z*other.x - first.x*other.z, first.x*other.y - first.y*other.x)
     
    def angle(first, other=FreeCAD.Vector(1,0,0)):
        """angle(Vector,Vector) - returns the angle in radians between the two vectors. 
        If only one is given, angle is between the vector and the horizontal East direction"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return math.acos(dotproduct(normalized(first),normalized(other)))
     
    def project(first, other):
        """project(Vector,Vector): projects the first vector onto the second one"""
        if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
            return scale(other, dotproduct(first,other)/dotproduct(other,other))
    

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), FreeCAD vector math library (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

