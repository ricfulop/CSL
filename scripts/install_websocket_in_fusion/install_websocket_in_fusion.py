"""
Run this script IN FUSION to install websocket-client
Go to Tools -> Add-Ins -> Scripts and Add-Ins -> Scripts tab -> + -> Select this file -> Run
"""
def run(context):
    import adsk.core
    import subprocess
    import sys
    
    app = adsk.core.Application.get()
    ui = app.userInterface
    
    try:
        # Try to import websocket first
        try:
            import websocket
            ui.messageBox(
                "✅ WebSocket is already installed!\n\n" +
                "You can now use the Triple Lindy Live Loop.",
                "WebSocket Check"
            )
            return
        except ImportError:
            pass
            
        # Get Python executable path
        python_path = sys.executable
        
        ui.messageBox(
            f"Installing websocket-client...\n\n" +
            f"Python: {python_path}\n\n" +
            "This may take a moment.",
            "Installing WebSocket"
        )
        
        # Install websocket-client
        result = subprocess.run(
            [python_path, "-m", "pip", "install", "--user", "websocket-client"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            ui.messageBox(
                "✅ WebSocket installed successfully!\n\n" +
                "Please restart Fusion 360 for the changes to take effect.\n\n" +
                "After restart:\n" +
                "1. Run the Triple Lindy add-in\n" +
                "2. Start the daemon: python3 triple_lindy_daemon/daemon.py\n" +
                "3. Send commands: python3 triple_lindy_daemon/tl_client.py example",
                "Installation Complete"
            )
        else:
            ui.messageBox(
                f"Installation failed:\n\n{result.stderr}\n\n" +
                "Try running this in Terminal instead:\n" +
                f"{python_path} -m pip install --user websocket-client",
                "Installation Error"
            )
            
    except Exception as e:
        ui.messageBox(
            f"Error: {str(e)}\n\n" +
            "You may need to install manually.",
            "Installation Error"
        )
