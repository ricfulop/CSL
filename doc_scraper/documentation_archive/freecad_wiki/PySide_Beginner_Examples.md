---
url: https://wiki.freecad.org/PySide_Beginner_Examples
title: PySide Beginner Examples
scraped_at: 2025-09-08 16:46:56
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Import statement
  * 3 Simplest Example
  * 4 Yes or No Query
  * 5 Enter Text Query
  * 6 More Than 2 Buttons

# PySide Beginner Examples

  * [Page](/PySide_Beginner_Examples "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:PySide_Beginner_Examples&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/PySide_Beginner_Examples)
  * [Edit](/index.php?title=PySide_Beginner_Examples&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_Beginner_Examples&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/PySide_Beginner_Examples.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=PySide_Beginner_Examples&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/PySide_Beginner_Examples)
  * [Edit](/index.php?title=PySide_Beginner_Examples&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_Beginner_Examples&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=PySide_Beginner_Examples&action=history)

General

  * [What links here](/Special:WhatLinksHere/PySide_Beginner_Examples "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/PySide_Beginner_Examples "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=PySide_Beginner_Examples&oldid=1619302 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=PySide_Beginner_Examples&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=PySide_Beginner_Examples&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
PySide+Beginner+Examples&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-PySide+Beginner+Examples&language=&task=view "Start translation for this language")
  * [Deutsch](/PySide_Beginner_Examples/de "PySide Beispiele für Anfänger \(100% translated\)")
  * English
  * [español](/PySide_Beginner_Examples/es "Ejemplos de principiantes en PySide \(58% translated\)")
  * [français](/PySide_Beginner_Examples/fr "PySide : Exemples pour débutants \(100% translated\)")
  * [italiano](/PySide_Beginner_Examples/it " Esempi di livello base di PySide \(100% translated\)")
  * [polski](/PySide_Beginner_Examples/pl "PySide przykłady dla początkujących \(100% translated\)")
  * [русский](/PySide_Beginner_Examples/ru "Примеры PySide для начинающих \(25% translated\)")

## Introduction

The purpose of this page is to cover beginner level examples of the
[PySide](/PySide "PySide") GUI manager (there are accompanying pages [PySide
Intermediate Examples](/PySide_Intermediate_Examples "PySide Intermediate
Examples") and [PySide Advanced Examples](/PySide_Advanced_Examples "PySide
Advanced Examples")).

Newcomers to GUI programming may stumble over the word "widget". Its meaning
outside of computing is usually given as:

> "a small gadget or mechanical device, especially one whose name is unknown
> or unspecified"

For GUI work such as PySide the term "widget" is most often used to refer to
the visible elements of the GUI - windows, dialogs, and input/output features.
All visible elements of PySide are called widgets, and, for those who are
interested, they all descend from a common parent class, QWidget. In addition
to the visible elements PySide also offers widgets for networking, XML,
multimedia, and database integration.

A widget that is not embedded in a parent widget is called a window and
usually windows have a frame and a title bar. The most common types of windows
are the "main window" (from the Class QMainWindow) and the various subclasses
of the dialog (from the Class QDialog). One big difference is that QDialog is
modal (i.e. the user can not do anything outside of the Dialog window while it
is open) and the QMainWindow is non-modal which allows the user to interact
with other windows in parallel.

This guide is a shortcut list for getting a PySide program working quickly
under FreeCAD, it isn't intended to teach Python or PySide. Some sites that do
that are:

  * [PySide tutorial](https://zetcode.com/gui/pysidetutorial/) at zetcode.com
  * [PySide/PyQt Tutorial](https://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) at PythonCentral.io
  * [PySide 1.0.7 Reference](https://srinikom.github.io/pyside-docs/) at Srinikom.github.io (note this is a reference, not a tutorial)

## Import statement

PySide is not loaded with Python by default, it must be requested prior to
using it. The following commands:

    
    
    from PySide import QtCore
    from PySide import QtGui
    

cause the 2 parts of PySide to be loaded:

  * QtGui holds classes for managing the Graphic User Interface.
  * QtCore holds classes that do not directly relate to the management of the GUI (e.g. timers and geometry).

Although it is possible to only import the one that is needed, generally they
are both needed and both imported.

The import statements are not repeated in the snippets below; it is assumed
that it is done at the beginning in each case.

## Simplest Example

The simplest interaction with PySide is to present a message to the user which
they can only accept:

    
    
    reply = QtGui.QMessageBox.information(None,"","Houston, we have a problem")
    

[![](/images/a/a6/PySideScreenSnapshot5.jpg)](/index.php?title=File:PySideScreenSnapshot5.jpg&filetimestamp=20150207183324&)

## Yes or No Query

The next most simple interaction is to ask for a yes/no answer:

    
    
    reply = QtGui.QMessageBox.question(None, "", "This is your chance to answer, what do you think?",
             QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
             # this is where the code relevant to a 'Yes' answer goes
             pass
    if reply == QtGui.QMessageBox.No:
             # this is where the code relevant to a 'No' answer goes
             pass
    

[![](/images/5/56/PySideScreenSnapshot6.jpg)](/index.php?title=File:PySideScreenSnapshot6.jpg&filetimestamp=20150207183336&)

## Enter Text Query

The next code snippet asks the user for a piece of text - note this can be any
key on the keyboard really:

    
    
    reply = QtGui.QInputDialog.getText(None, "Ouija Central","Enter your thoughts for the day:")
    if reply[1]:
    	# user clicked OK
    	replyText = reply[0]
    else:
    	# user clicked Cancel
    	replyText = reply[0] # which will be "" if they clicked Cancel
    

[![](/images/e/e9/PySideScreenSnapshot7.jpg)](/index.php?title=File:PySideScreenSnapshot7.jpg&filetimestamp=20150207183347&)

Remember that even if the user enters only digits, "1234" for example, they
are strings and must be converted to number representation with either of the
following:

    
    
    anInteger = int(userInput) # to convert to an integer from a string representation
    
    aFloat = float(userInput) # to convert to a float from a string representation
    

## More Than 2 Buttons

The final Beginner Level example is of how to build a dialog with an arbitrary
number of buttons. This example is programmatically too complex to be invoked
from a single Python statement so in some ways it should be on the next page
which is [PySide Intermediate Examples](/PySide_Intermediate_Examples "PySide
Intermediate Examples"). But on the other hand this is often all that is
needed without getting into complex GUI definitions, so the code is placed at
the end of this page rather than the beginning of the next.

    
    
    from PySide import QtGui, QtCore
    
    class MyButtons(QtGui.QDialog):
    	""""""
    	def __init__(self):
    		super(MyButtons, self).__init__()
    		self.initUI()
    	def initUI(self):      
    		option1Button = QtGui.QPushButton("Option 1")
    		option1Button.clicked.connect(self.onOption1)
    		option2Button = QtGui.QPushButton("Option 2")
    		option2Button.clicked.connect(self.onOption2)
    		option3Button = QtGui.QPushButton("Option 3")
    		option3Button.clicked.connect(self.onOption3)
    		option4Button = QtGui.QPushButton("Option 4")
    		option4Button.clicked.connect(self.onOption4)
    		option5Button = QtGui.QPushButton("Option 5")
    		option5Button.clicked.connect(self.onOption5)
    		#
    		buttonBox = QtGui.QDialogButtonBox()
    		buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
    		buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
    		buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
    		buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
    		buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
    		buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
    		#
    		mainLayout = QtGui.QVBoxLayout()
    		mainLayout.addWidget(buttonBox)
    		self.setLayout(mainLayout)
    		# define window		xLoc,yLoc,xDim,yDim
    		self.setGeometry(	250, 250, 0, 50)
    		self.setWindowTitle("Pick a Button")
    		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    	def onOption1(self):
    		self.retStatus = 1
    		self.close()
    	def onOption2(self):
    		self.retStatus = 2
    		self.close()
    	def onOption3(self):
    		self.retStatus = 3
    		self.close()
    	def onOption4(self):
    		self.retStatus = 4
    		self.close()
    	def onOption5(self):
    		self.retStatus = 5
    		self.close()
    
    def routine1():
    	print ('routine 1')
    
    form = MyButtons()
    form.exec_()
    if form.retStatus==1:
    	routine1()
    elif form.retStatus==2:
    	routine2()
    elif form.retStatus==3:
    	routine3()
    elif form.retStatus==4:
    	routine4()
    elif form.retStatus==5:
    	routine5()
    

Each piece of code under test would be in a function with the name
'routine1()', 'routine2()', etc. As many buttons as you can fit on the screen
may be used. Follow the patterns in the code sample and add extra buttons as
needed - the Dialog box will set it's width accordingly, up to the width of
the screen.

[![](/images/5/52/PySideScreenSnapshot8.jpg)](/index.php?title=File:PySideScreenSnapshot8.jpg&filetimestamp=20150228133709&)

There is a line of code:

    
    
    buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
    

which causes the buttons to be in a horizontal line. To put them into a
vertical line, change the line of code to read:

    
    
    buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
    

  

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples beginner, [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

