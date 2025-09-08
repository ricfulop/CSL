---
url: https://freecad.github.io/SourceDoc/d7/dc3/group__workbench.html
scraped_at: 2025-09-08T14:51:30.701331
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Workbench Framework

[Core](../../d4/d68/group__CORE.html) » [Gui](../../df/dd1/group__GUI.html)

FreeCAD provides the possibility to have one or more workbenches for a module.

FreeCAD provides the possibility to have one or more workbenches for a module.

A workbench changes the appearance of the main window in that way that it
defines toolbars, items in the toolbox, menus or the context menu and dockable
windows that are shown to the user. The idea behind this concept is that the
user should see only the functions that are required for the task that they
are doing at this moment and not to show dozens of unneeded functions which
the user never uses.

#  Step by step

Here follows a short description of how your own workbench can be added to a
module.

##  Inherit either from Workbench or StdWorkbench

First you have to subclass either
[Workbench](../../d0/d97/classGui_1_1Workbench.html) or
[StdWorkbench](../../db/d0a/classGui_1_1StdWorkbench.html) and reimplement the
methods
[setupMenuBar()](../../d0/d97/classGui_1_1Workbench.html#a5669c13ee2759f8b779c5ebcdfc9ecfa),
[setupToolBars()](../../d0/d97/classGui_1_1Workbench.html#a2c4bc1bd254e668905bb54553e5705df),
[setupCommandBars()](../../d0/d97/classGui_1_1Workbench.html#acd15496593629bd4f65a0cfe5c637896)
and
[setupDockWindows()](../../d0/d97/classGui_1_1Workbench.html#a865cd438fc855d73e7ca1fa853ec1af6).

The difference between both classes is that these methods of Workbench are
pure virtual while StdWorkbench defines already the standard menus and
toolbars, such as the 'File', 'Edit', ..., 'Help' menus with their common
functions.

If your class derives from Workbench then you have to define your menus,
toolbars and toolbox items from scratch while deriving from StdWorkbench you
have the possibility to add your preferred functions or even remove some
unneeded functions.

class MyWorkbench : public StdWorkbench

{

...

protected:

MenuItem* setupMenuBar() const

{

MenuItem* root = StdWorkbench::setupMenuBar();

// your changes

return root;

}

ToolBarItem* setupToolBars() const

{

ToolBarItem* root = StdWorkbench::setupToolBars();

// your changes

return root;

}

ToolBarItem* setupCommandBars() const

{

ToolBarItem* root = StdWorkbench::setupCommandBars();

// your changes

return root;

}

};

or

class MyWorkbench : public [Workbench](../../da/d26/classWorkbench.html)

{

...

protected:

MenuItem* setupMenuBar() const

{

MenuItem* root = new MenuItem;

// setup from scratch

return root;

}

ToolBarItem* setupToolBars() const

{

ToolBarItem* root = new ToolBarItem;

// setup from scratch

return root;

}

ToolBarItem* setupCommandBars() const

{

ToolBarItem* root = new ToolBarItem;

// setup from scratch

return root;

}

};

##  Customizing the workbench

If you want to customize your workbench by adding or removing items you can
use the ToolBarItem class for customizing toolbars and the MenuItem class for
menus. Both classes behave basically the same. To add a new menu item you can
do it as follows

MenuItem* setupMenuBar() const

{

MenuItem* root = StdWorkbench::setupMenuBar();

// create a sub menu

MenuItem* mySub = new MenuItem; // note: no parent is given

mySub->setCommand( "My &Submenu" );

*mySub << "Std_Undo" << "Std_Redo";

// My menu

MenuItem* myMenu = new MenuItem( root );

myMenu->setCommand( "&My Menu" );

// fill up the menu with some command items

*myMenu << mySub << "Separator" << "Std_Cut" << "Std_Copy" << "Std_Paste" << "Separator" << "Std_Undo" << "Std_Redo";

}

Toolbars can be customized the same way unless that you shouldn't create
subitems (there are no subtoolbars).

##  Register your workbench

Once you have implemented your workbench class you have to register it to make
it known to the FreeCAD core system. You must make sure that the step of
registration is performed only once. A good place to do it is e.g. in the
global function initMODULEGui in AppMODULEGui.cpp where MODULE stands for the
name of your module. Just add the line

MODULEGui::MyWorkbench::init();

somewhere there.

##  Create an item for your workbench

Though your workbench has been registered now, at this stage you still cannot
invoke it yet. Therefore you must create an item in the list of all visible
workbenches. To perform this step you must open your InitGui.py (a Python
file) and do some adjustments. The file contains already a Python class
MODULEWorkbench that implements the Activate() method (it imports the needed
library). You can also implement the GetIcon() method to set your own icon for
your workbench, if not, the default FreeCAD icon is taken, and finally the
most important method GetClassName(). that represents the link between Python
and C++. This method must return the name of the associated C++ including
namespace. In this case it must the string "ModuleGui::MyWorkbench". At the
end you can change the line from

[Gui](../../d9/dad/namespaceGui.html "The FreeCAD Graphical interface
layer.").addWorkbench("MODULE design",MODULEWorkbench())

to

[Gui](../../d9/dad/namespaceGui.html "The FreeCAD Graphical interface
layer.").addWorkbench("My workbench",MODULEWorkbench())

or whatever you want.

Note

    You must make sure to choose a unique name for your workbench (in this example "My workbench"). Since FreeCAD doesn't provide a mechanism for this you have to care on your own.

#  More details and limitations

One of the key concepts of the workbench framework is to load a module at
runtime when the user needs some function that it provides. So, if the user
doesn't need a module it never gets loaded into RAM. This speeds up the
startup procedure of FreeCAD and saves memory.

At startup FreeCAD scans all module directories and invokes InitGui.py. So an
item for a workbench gets created. If the user clicks on such an item the
matching module gets loaded, the C++ workbench gets registered and activated.

The user is able to modify a workbench (Edit|Customize). E.g. they can add new
toolbars or items for the toolbox and add their preferred functions to them.
But the user only has full control over "their" own toolbars, the default
workbench items cannot be modified or even removed.

FreeCAD provides also the possibility to define pure Python workbenches. Such
workbenches are temporarily only and are lost after exiting the FreeCAD
session. But if you want to keep your Python workbench you can write a macro
and attach it with a user defined button or just perform the macro during the
next FreeCAD session. Here follows a short example of how to create and embed
a workbench in Python

w=[Workbench](../../da/d26/classWorkbench.html)() # creates a standard
workbench (the same as StdWorkbench in C++)

w.MenuText = "My Workbench" # the [text](../../de/d0e/namespacetext.html
"Provides the object code for the Text object.") that will appear in the combo
box

dir(w) # lists all available function of the object

FreeCADGui.addWorkbench(w) # Creates an item for our workbench now

# Note: We must first add the workbench to run some initialization code

# Then we are ready to customize the workbench

list = ["Std_Test1", "Std_Test2", "Std_Test3"] # creates a list of new
functions

w.appendMenu("Test functions", list) # creates a new menu with these functions

w.appendToolbar("Test", list) # ... and also a new toolbar

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

