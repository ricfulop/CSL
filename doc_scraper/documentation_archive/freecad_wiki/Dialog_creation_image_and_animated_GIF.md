---
url: https://wiki.freecad.org/Dialog_creation_image_and_animated_GIF
title: Dialog creation image and animated GIF
scraped_at: 2025-09-08 16:46:50
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Dialog with image (QLabel) and animated GIF (QMovie)

# Dialog creation image and animated GIF

  * [Page](/Dialog_creation_image_and_animated_GIF "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Dialog_creation_image_and_animated_GIF&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Dialog_creation_image_and_animated_GIF)
  * [Edit](/index.php?title=Dialog_creation_image_and_animated_GIF&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Dialog_creation_image_and_animated_GIF&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Dialog_creation_image_and_animated_GIF.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Dialog_creation_image_and_animated_GIF&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Dialog_creation_image_and_animated_GIF)
  * [Edit](/index.php?title=Dialog_creation_image_and_animated_GIF&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Dialog_creation_image_and_animated_GIF&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Dialog_creation_image_and_animated_GIF&action=history)

General

  * [What links here](/Special:WhatLinksHere/Dialog_creation_image_and_animated_GIF "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Dialog_creation_image_and_animated_GIF "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Dialog_creation_image_and_animated_GIF&oldid=1068420 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Dialog_creation_image_and_animated_GIF&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Dialog_creation_image_and_animated_GIF&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Dialog+creation+image+and+animated+GIF&action=page&filter=&language=en)This is
the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Dialog+creation+image+and+animated+GIF&language=&task=view "Start translation for this language")
  * [Deutsch](/Dialog_creation_image_and_animated_GIF/de "Dialogerstellung Bild und animierte GIF \(100% translated\)")
  * English
  * [français](/Dialog_creation_image_and_animated_GIF/fr "Création d'une fenêtre de dialogue pour image et GIF animé \(100% translated\)")
  * [italiano](/Dialog_creation_image_and_animated_GIF/it "Creare una finestra di dialogo per immagini e GIF animate \(100% translated\)")
  * [polski](/Dialog_creation_image_and_animated_GIF/pl "Tworzenie dialogu grafika i animowany GIF \(100% translated\)")

## Introduction

This is an example of [dialog creation](/Dialog_creation "Dialog creation")
with [PySide](/PySide "PySide").

In this example, the entire interface is defined in [Python](/Python
"Python"). Although this is possible for small interfaces, for larger
interfaces the recommendation is to create .ui files through Qt Designer, and
load these in the program.

## Dialog with image (QLabel) and animated GIF (QMovie)

    
    
    import PySide
    from PySide import QtGui ,QtCore
    from PySide.QtGui import QPixmap, QMovie, QLabel
    from PySide.QtCore import *
    class MyLabelPatience():
        label = QtGui.QLabel()
        label.setText("<img src=" + path_Name_Image + "><b><center>Wait please</center> \n\n<center>i search the fonts !\n\n</center></b>")
        # center screen
        ecran = FreeCADGui.getMainWindow().frameGeometry()
        xF = 250; yF = 120
        xW = (ecran.width()/2) - (xF/2)
        yW = (ecran.height()/2)- (yF/2)
        label.setGeometry(xW, yW, xF, yF)
        ####
        label.setStyleSheet("QLabel {background-color : #F0C300;font: 12pt; }");
        label.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))        # pas de bords (not border)
        ### un-comment for use ###############
        movie = QtGui.QMovie(path_Name_Image)    # anime le fichier Gif anime (decommenter)
        label.setMovie(movie)
        movie.start()
        ##################
    
    patience = MyLabelPatience().label
    patience.show()                    #show the image
    #patience.close()                   #close the Qlabel
    #MyLabelPatience().movie.start()    #start the animation (after patience.show())
    #MyLabelPatience().movie.stop()     #stop animation
    

[![](/images/5/55/Qlabel_Image00.png)](/index.php?title=File:Qlabel_Image00.png&filetimestamp=20190611092500&)

Example QLabel with image and text.

[![](/images/9/91/Qlabel_Image_Animee00.gif)](/index.php?title=File:Qlabel_Image_Animee00.gif&filetimestamp=20190611092411&)

Example QLabel with animated GIF.

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), 4, [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

