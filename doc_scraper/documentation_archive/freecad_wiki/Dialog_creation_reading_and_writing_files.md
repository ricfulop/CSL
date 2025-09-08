---
url: https://wiki.freecad.org/Dialog_creation_reading_and_writing_files
title: Dialog creation reading and writing files
scraped_at: 2025-09-08 16:46:46
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Dialog for writing to a file
  * 3 Dialog to read a file

# Dialog creation reading and writing files

  * [Page](/Dialog_creation_reading_and_writing_files "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Dialog_creation_reading_and_writing_files&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Dialog_creation_reading_and_writing_files)
  * [Edit](/index.php?title=Dialog_creation_reading_and_writing_files&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Dialog_creation_reading_and_writing_files&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Dialog_creation_reading_and_writing_files.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Dialog_creation_reading_and_writing_files&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Dialog_creation_reading_and_writing_files)
  * [Edit](/index.php?title=Dialog_creation_reading_and_writing_files&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Dialog_creation_reading_and_writing_files&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Dialog_creation_reading_and_writing_files&action=history)

General

  * [What links here](/Special:WhatLinksHere/Dialog_creation_reading_and_writing_files "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Dialog_creation_reading_and_writing_files "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Dialog_creation_reading_and_writing_files&oldid=1536427 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Dialog_creation_reading_and_writing_files&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Dialog_creation_reading_and_writing_files&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Dialog+creation+reading+and+writing+files&action=page&filter=&language=en)This
is the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Dialog+creation+reading+and+writing+files&language=&task=view "Start translation for this language")
  * [Deutsch](/Dialog_creation_reading_and_writing_files/de "Dialogerstellung Lesen und Schreiben von Dateien \(100% translated\)")
  * English
  * [français](/Dialog_creation_reading_and_writing_files/fr "Création d'une boîte de dialogue lecture et écriture de fichiers \(100% translated\)")
  * [italiano](/Dialog_creation_reading_and_writing_files/it "Creare una finestra di dialogo per leggere e scrivere file \(100% translated\)")
  * [polski](/Dialog_creation_reading_and_writing_files/pl "Tworzenie dialogów odczyt i zapis plików \(100% translated\)")

## Introduction

This is an example of [dialog creation](/Dialog_creation "Dialog creation")
with [PySide](/PySide "PySide").

In this example, the entire interface is defined in [Python](/Python
"Python"). Although this is possible for small interfaces, for larger
interfaces the recommendation is to create .ui files through Qt Designer, and
load these in the program.

## Dialog for writing to a file

Complete code:

    
    
    # -*- coding: utf-8 -*-
    import PySide
    from PySide import QtGui ,QtCore
    from PySide.QtGui import *
    from PySide.QtCore import *
    path = FreeCAD.ConfigGet("UserAppData")
    
    try:
        SaveName = QFileDialog.getSaveFileName(None,QString.fromLocal8Bit("Save a file txt"),path,             "*.txt") # PyQt4
    #                                                                     "here the text displayed on windows" "here the filter (extension)"   
    except Exception:
        SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path,             "*.txt") # PySide
    #                                                                     "here the text displayed on windows" "here the filter (extension)"   
    if SaveName == "":                                                            # if the name file are not selected then Abord process
        App.Console.PrintMessage("Process aborted"+"\n")
    else:                                                                         # if the name file are selected or created then 
        App.Console.PrintMessage("Registration of "+SaveName+"\n")                # text displayed to Report view (Menu > View > Report view checked)
        try:                                                                      # detect error ...
            file = open(SaveName, 'w')                                            # open the file selected to write (w)
            try:                                                                  # if error detected to write ...
                # here your code
                print("here your code")
                file.write(str(1)+"\n")                                           # write the number convert in text with (str())
                file.write("FreeCAD the best")                                    # write the the text with ("  ")
            except Exception:                                                     # if error detected to write
                App.Console.PrintError("Error write file "+"\n")                  # detect error ... display the text in red (PrintError)
            finally:                                                              # if error detected to write ... or not the file is closed
                file.close()                                                      # if error detected to write ... or not the file is closed
        except Exception:
            App.Console.PrintError("Error Open file "+SaveName+"\n")      # detect error ... display the text in red (PrintError)
    

## Dialog to read a file

Complete code:

    
    
    # -*- coding: utf-8 -*-
    import PySide
    from PySide import QtGui ,QtCore
    from PySide.QtGui import *
    from PySide.QtCore import *
    path = FreeCAD.ConfigGet("UserAppData")
    
    OpenName = ""
    try:
        OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Read a file txt"),path,             "*.txt") # PyQt4
    #                                                                     "here the text displayed on windows" "here the filter (extension)"   
    except Exception:
        OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a file txt", path,             "*.txt") #PySide
    #                                                                     "here the text displayed on windows" "here the filter (extension)"   
    if OpenName == "":                                                            # if the name file are not selected then Abord process
        App.Console.PrintMessage("Process aborted"+"\n")
    else:
        App.Console.PrintMessage("Read "+OpenName+"\n")                           # text displayed to Report view (Menu > View > Report view checked)
        try:                                                                      # detect error to read file
            file = open(OpenName, "r")                                            # open the file selected to read (r)  # (rb is binary)
            try:                                                                  # detect error ...
                # here your code
                print("here your code")
                op = OpenName.split("/")                                          # decode the path
                op2 = op[-1].split(".")                                           # decode the file name 
                nomF = op2[0]                                                     # the file name are isolated
    
                App.Console.PrintMessage(str(nomF)+"\n")                          # the file name are displayed
    
                for ligne in file:                                                # read the file
                    X  = ligne.rstrip('\n\r') #.split()                           # decode the line
                    print(X)                                                      # print the line in report view other method 
                                                                                  # (Menu > Edit > preferences... > Output window > Redirect internal Python output (and errors) to report view checked) 
            except Exception:                                                     # if error detected to read
                App.Console.PrintError("Error read file "+"\n")                   # detect error ... display the text in red (PrintError)
            finally:                                                              # if error detected to read ... or not error the file is closed
                file.close()                                                      # if error detected to read ... or not error the file is closed
        except Exception:                                                         # if one error detected to read file
            App.Console.PrintError("Error in Open the file "+OpenName+"\n")       # if one error detected ... display the text in red (PrintError)
    

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), 2, [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

