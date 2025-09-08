---
url: https://wiki.freecad.org/PySide_Advanced_Examples
title: PySide Advanced Examples
scraped_at: 2025-09-08 16:47:04
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Create Reference to the Main Window
  * 3 Browse the Children of the Main Window
  * 4 Add New Widget Manually
  * 5 Add New Widget by Creating UI Object
  * 6 Loading the UI from a Qt Designer .ui File

# PySide Advanced Examples

  * [Page](/PySide_Advanced_Examples "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:PySide_Advanced_Examples&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/PySide_Advanced_Examples)
  * [Edit](/index.php?title=PySide_Advanced_Examples&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_Advanced_Examples&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/PySide_Advanced_Examples.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=PySide_Advanced_Examples&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/PySide_Advanced_Examples)
  * [Edit](/index.php?title=PySide_Advanced_Examples&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_Advanced_Examples&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=PySide_Advanced_Examples&action=history)

General

  * [What links here](/Special:WhatLinksHere/PySide_Advanced_Examples "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/PySide_Advanced_Examples "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=PySide_Advanced_Examples&oldid=1233929 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=PySide_Advanced_Examples&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=PySide_Advanced_Examples&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
PySide+Advanced+Examples&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-PySide+Advanced+Examples&language=&task=view "Start translation for this language")
  * [Deutsch](/PySide_Advanced_Examples/de "PySide Beispiele für Fortgeschrittene \(100% translated\)")
  * English
  * [français](/PySide_Advanced_Examples/fr "PySide : Exemples avancés \(100% translated\)")
  * [italiano](/PySide_Advanced_Examples/it " Esempi di PySide di livello avanzato \(35% translated\)")
  * [polski](/PySide_Advanced_Examples/pl "PySide Przykłady dla zaawansowanych \(6% translated\)")
  * [русский](/PySide_Advanced_Examples/ru "Сложные примеры PySide \(12% translated\)")

## Introduction

The purpose of this page is to cover advanced level examples of the
[PySide](/PySide "PySide") GUI manager (there are accompanying pages [PySide
Beginner Examples](/PySide_Beginner_Examples "PySide Beginner Examples") and
[PySide Intermediate Examples](/PySide_Intermediate_Examples "PySide
Intermediate Examples")).

By using the PySide module from inside FreeCAD, you have full control over its
interface. You can for example:

  * Add your own panels, widgets and toolbars
  * Add or hide elements to existing panels
  * Change, redirect or add connections between all those elements

## Create Reference to the Main Window

If you want to work on the FreeCAD interface, the very first thing to do is
create a reference to the FreeCAD main window:

    
    
    import sys
    from PySide import QtGui ,QtCore 
    app = QtGui.qApp
    mw = FreeCADGui.getMainWindow()
    

## Browse the Children of the Main Window

Then, you can for example browse through all the widgets of the interface:

    
    
    for child in mw.children():
       print('widget name = ', child.objectName(), ', widget type = ', child)
    

The widgets in a Qt interface are usually nested into "container" widgets, so
the children of our main window can themselves contain other children.
Depending on the widget type, there are a lot of things you can do. Check the
API documentation to see what is possible.

## Add New Widget Manually

Adding a new widget, for example a dockWidget (which can be placed in one of
FreeCAD's side panels) is easy:

    
    
    myWidget = QtGui.QDockWidget()
    mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myWidget)
    

You could then add stuff directly to your widget:

    
    
    myWidget.setObjectName("my Nice New Widget")
    myWidget.resize(QtCore.QSize(300,100)) # sets size of the widget
    label = QtGui.QLabel("Hello World", myWidget) # creates a label
    label.setGeometry(QtCore.QRect(2,50,200,24))  # sets its size
    label.setObjectName("myLabel") # sets its name, so it can be found by name
    

## Add New Widget by Creating UI Object

But a preferred method is to create a UI object which will do all of the setup
of your widget at once. The big advantage is that such an UI object can be
[created graphically](/Dialog_creation "Dialog creation") with the Qt Designer
program. A typical object generated by Qt Designer is like this:

    
    
    class myWidget_Ui(object):
      def setupUi(self, myWidget):
        myWidget.setObjectName("my Nice New Widget")
        myWidget.resize(QtCore.QSize(300,100).expandedTo(myWidget.minimumSizeHint())) # sets size of the widget
    
        self.label = QtGui.QLabel(myWidget) # creates a label
        self.label.setGeometry(QtCore.QRect(50,50,200,24)) # sets its size
        self.label.setObjectName("label") # sets its name, so it can be found by name
    
      def retranslateUi(self, draftToolbar): # built-in QT function that manages translations of widgets
        myWidget.setWindowTitle(QtGui.QApplication.translate("myWidget", "My Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("myWidget", "Welcome to my new widget!", None, QtGui.QApplication.UnicodeUTF8))
    

To use it, you just need to apply it to your freshly created widget like this:

    
    
    app = QtGui.qApp
    FCmw = app.activeWindow()
    myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
    myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
    myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
    FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
    

## Loading the UI from a Qt Designer .ui File

The key to loading a UI file successfully is to use the full path to the file.
As an example, the [Addon Manager](/Std_AddonMgr "Std AddonMgr") does it like
this:

    
    
    self.dialog = FreeCADGui.PySideUic.loadUi(os.path.join(os.path.dirname(__file__), "AddonManager.ui"))
    

  

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), advanced
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

