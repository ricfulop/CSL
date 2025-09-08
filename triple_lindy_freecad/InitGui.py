"""
Triple Lindy FreeCAD Workbench
Provides file watching capability for CSL integration
"""
import FreeCADGui
import os
from pathlib import Path

class TripleLindyWorkbench(FreeCADGui.Workbench):
    """FreeCAD Workbench for Triple Lindy CSL integration."""
    
    def __init__(self):
        self.__class__.MenuText = "Triple Lindy"
        self.__class__.ToolTip = "CSL Integration for FreeCAD"
        # Icon path
        icon_path = Path(__file__).parent / "icons" / "triple_lindy.svg"
        if icon_path.exists():
            self.__class__.Icon = str(icon_path)
        else:
            # Fallback XPM icon
            self.__class__.Icon = """
                /* XPM */
                static char * triple_lindy_xpm[] = {
                "16 16 3 1",
                "   c None",
                ".  c #000000",
                "+  c #0066CC",
                "                ",
                "   ..........   ",
                "  .++++++++++.  ",
                " .++++++++++++. ",
                " .++..++++..++. ",
                " .++...++...++. ",
                " .++...++...++. ",
                " .++...++...++. ",
                " .++...++...++. ",
                " .++...++...++. ",
                " .++...++...++. ",
                " .++..++++..++. ",
                " .++++++++++++. ",
                "  .++++++++++.  ",
                "   ..........   ",
                "                "};
            """
    
    def Initialize(self):
        """Initialize the workbench."""
        import triple_lindy_commands
        
        # List of command names
        command_list = [
            "TripleLindyStart",
            "TripleLindyStop",
            "TripleLindyStatus",
            "TripleLindyTest",
            "TripleLindyClear",
            "TripleLindyHelp"
        ]
        
        # Create toolbar
        self.appendToolbar("Triple Lindy", command_list[:3])  # Main commands
        
        # Create menu
        self.appendMenu("Triple Lindy", command_list)
        
        FreeCAD.Console.PrintMessage("Triple Lindy Workbench initialized\n")
        FreeCAD.Console.PrintMessage("Use 'Triple Lindy Start' to begin file watching\n")
    
    def Activated(self):
        """Called when workbench is activated."""
        FreeCAD.Console.PrintMessage("Triple Lindy Workbench activated\n")
        FreeCAD.Console.PrintMessage("Commands: Start, Stop, Status, Test, Clear, Help\n")
    
    def Deactivated(self):
        """Called when workbench is deactivated."""
        # Stop watcher if running
        import triple_lindy_commands
        if hasattr(triple_lindy_commands, '_watcher') and triple_lindy_commands._watcher:
            triple_lindy_commands._watcher.stop()
    
    def ContextMenu(self, recipient):
        """Context menu."""
        self.appendContextMenu("Triple Lindy", ["TripleLindyStatus"])
    
    def GetClassName(self):
        return "Gui::PythonWorkbench"

# Register the workbench
FreeCADGui.addWorkbench(TripleLindyWorkbench())
