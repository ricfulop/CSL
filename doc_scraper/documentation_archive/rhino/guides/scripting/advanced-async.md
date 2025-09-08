---
url: https://developer.rhino3d.com/guides/scripting/advanced-async/#c-asyncawait
scraped_at: 2025-09-08T16:05:55.813340
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Asynchronous
Execution](https://developer.rhino3d.com/guides/scripting/advanced-async/)

  * What is Asynchronous
  * Async in Script Editor
  * Asynchronous C#
  * Asynchronous Python
  * Show Progress
    * Python Progress
  * Async in Grasshopper
  * Advanced Async
    * C# Async/Await

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Asynchronous Execution

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Monday, August 19, 2024)

## What is Asynchronous

Normally, most operations in an application with a graphical user interface
(GUI), run on the _UI Thread_. That is the thread that starts the UI and
listens to the events like clicking buttons and moving the mouse. When you
click on a button, the code behind that button runs on the UI thread.

**Asynchronous (Async for short) operations run on Non-UI threads and do not
freeze the UI.**

If the task is time-consuming, the UI thread (now executing the task after
button click) can not respond to any other events. Therefore UI is _“Frozen”_
(not the Disney® movie) and unresponsive. Normally this is ok since you would
not want the user to change the document while the task is running. It is a
good idea to use Non-UI threads for time-consuming tasks and run them
_Asynchronously_.

## Async in Script Editor

In Rhino Script Editor, if a script is performing a time-consuming task,
clicking on the _Run_ button would cause Rhino UI to freeze for the duration
of the script. As we mentioned above this is ok. However, if your task does
not deal with the Rhino document (could be changed by the Rhino user while
your script is running), it could be made async. This would make Rhino UI
responsive while your script is running. It is also a good habit to show
progress while the task is running in the background:

  * In C#, add `// async:true` to the top of your script.
  * In Python, add `# async:true` to the top of your script.

When script is marked as `async: true` the Script Editor runs the full script
on a Non-UI thread. This is a feature of Rhino Script Editor and not the
scripting language. You can remove this line or set it to `false` to make the
script synchronous again.

## Asynchronous C#

The example C# script below completely freezes Rhino UI for about 2 seconds.
That the amount of time we are specifying in `Thread.Sleep` to simulate work.
This could be a long running computation or waiting to receive some data from
web:

    
    
    // #! csharp
    using System;
    using System.Threading;
    
    using Rhino;
    
    RhinoApp.WriteLine("Start Task");
    Thread.Sleep(2000); // simulate work
    RhinoApp.WriteLine("End Task");
    

By adding the line `// async:true`, we can force this complete script to run
on a Non-UI thread, keeping Rhino UI active so we can continue working while
the script is running:

    
    
    // #! csharp
    // async:true
    using System;
    using System.Threading;
    
    using Rhino;
    
    RhinoApp.WriteLine("Start Task");
    Thread.Sleep(2000); // simulate work
    RhinoApp.WriteLine("End Task");
    

Notice that this is the only change we made to the script. Also note that the
_Run_ button in Script Editor dashboard now shows a red arrow to represent the
async execution of this script:

![](https://developer.rhino3d.com/guides/scripting/advanced-async/editor-
csharp-async.png)

## Asynchronous Python

The example Python script below completely freezes Rhino UI for about 2
seconds. That the amount of time we are specifying in `time.sleep` to simulate
work. This could be a long running computation or waiting to receive some data
from web:

    
    
    #! python3
    import threading
    import time
    
    class Job(threading.Thread):
        def __init__(self, id, name, wait):
            super().__init__()
            self.id = id
            self.name = name
            self.wait = wait
    
        def run(self):
            print("Starting " + self.name)
            time.sleep(self.wait) # wait to simulate work
            print(f"Done {self.name}: {time.ctime(time.time())}")
    
    
    job1 = Job(1, "Job-1", 2)
    job1.start()
    job1.join()
    
    print("Complete")
    

By adding the line `# async:true`, we can force this complete script to run on
a Non-UI thread, keeping Rhino UI active so we can continue working while the
script is running (this is a feature of Rhino Script Editor and not Python
language):

    
    
    #! python3
    # async: true
    import threading
    import time
    
    class Job(threading.Thread):
        def __init__(self, id, name, wait):
            super().__init__()
            self.id = id
            self.name = name
            self.wait = wait
    
        def run(self):
            print("Starting " + self.name)
            time.sleep(self.wait) # wait to simulate work
            print(f"Done {self.name}: {time.ctime(time.time())}")
    
    
    job1 = Job(1, "Job-1", 2)
    job1.start()
    job1.join()
    
    print("Complete")
    

Notice that this is the only change we made to the script. Also note that the
_Run_ button in Script Editor dashboard now shows a red arrow to represent the
async execution of this script:

![](https://developer.rhino3d.com/guides/scripting/advanced-async/editor-
python-async.png)

## Show Progress

It is a good practice to show feedback on the progress of background tasks.
Rhino UI has a progress indicator on the status bar. This is an example of how
you can use this progress bar in your scripts. `Thread.Sleep` is used below to
simulate work:

    
    
    // #! csharp
    using System;
    using System.Threading;
    
    using Rhino;
    using Rhino.UI;
    using Eto.Forms;
    
    // setup the progress indicator with expected range, and a message
    StatusBar.ShowProgressMeter(0, 5, "Progress", embedLabel: true, showPercentComplete: false);
    RhinoApp.WriteLine("Start Task");
    for (int i = 0; i < 5; i++)
    {
        Thread.Sleep(1000); // simulate work
    
        // update progress
        StatusBar.UpdateProgressMeter("Progress", i, true);
        // since we are on the main thread here,
        // call this method to force Rhino UI to update
        Application.Instance.RunIteration();
    }
    
    // do not forget to hide the progress when done
    StatusBar.HideProgressMeter();
    RhinoApp.WriteLine("End Task");
    

![](https://developer.rhino3d.com/guides/scripting/advanced-async/editor-
csharp-progress-sync.png)

### Python Progress

In Python you can use `rhinoscriptsyntax` module to access the progress
indicator easier:

    
    
    import rhinoscriptsyntax as rs
    from Rhino import RhinoApp
    
    MAX = 1000
    rs.StatusBarProgressMeterShow("Progress", 0, MAX)
    
    for i in range(0, MAX):
        rs.StatusBarProgressMeterUpdate(i)
    
    rs.StatusBarProgressMeterHide()
    

## Async in Grasshopper

__Note __

`async: true` pattern is NOT SUPPORTED in Grasshopper, since it needs to wait
for the script to fully execute and set the output data before executing the
rest of component graph. We can however have background threads running
computations, and continuously trigger a Grasshopper solve to update the
results.

This is an example of a python script component that runs computation on
background thread. We use the _Trigger_ component is Grasshopper to recompute
this component on intervals and therefore update the geometry previews in
Rhino:

  * `RunScript` sets up the worked thread on the first run. It does not do anything on later runs except for outputing `"Training in Progress"` and the current state of compute mesh
  * `main_solve` is the solver function that is being executed by the worker thread. It updates the class variable `MyComponent.CURRENT_MESH` while running
  * `DrawViewportMeshes` is called by Grasshopper after each trigger and displays the current state of computed mesh in `MyComponent.CURRENT_MESH`

    
    
    import System
    import System.Drawing as SD
    import Rhino
    import Rhino.Geometry as G
    import Grasshopper
    import Grasshopper.Kernel as GHK
    import threading
    import time
    
    
    def main_solve():
        for r in range(10, 20):
            # wait represents compute work
            Rhino.RhinoApp.WriteLine("computing mesh")
            time.sleep(1)
    
            sphere = G.Sphere(G.Point3d.Origin, r)
            MyComponent.CURRENT_MESH = G.Mesh.CreateFromSphere(sphere, 10, 10)
            Rhino.RhinoApp.WriteLine("computed mesh")
    
        Rhino.RhinoApp.WriteLine("computed completed")
    
    
    class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
        SOVLE_STARTED = False
        CURRENT_MESH = None
    
        def RunScript(self):
            if MyComponent.SOVLE_STARTED:
                return ("Training in Progress", MyComponent.CURRENT_MESH)
            
            MyComponent.SOVLE_STARTED = True
            threading.Thread(target=main_solve).start()
            return ("Training in Progress", None)
            
        @property
        def ClippingBox(self):
            return G.BoundingBox(-30, -30, -30, 30, 30, 30)
    
        def DrawViewportMeshes(self, args: GHK.IGH_PreviewArgs):
            if d := getattr(args, "Display", None):
                if MyComponent.CURRENT_MESH:
                    d.DrawMeshWires(MyComponent.CURRENT_MESH, SD.Color.Blue, 2)
    

Notice that Rhino UI stays active during this background computation:

## Advanced Async

Sometime it is necessary to run operations on the UI thread before or after
completing a time-consuming operation. Remember that the `async:true`
mechanism mentioned above is for convenience and runs the complete script on a
Non-UI thread. Based on the script language, you can use the threading or
async features on the language to perform more complicated sync/async
operations.

This is an example C# script that runs on UI thread on parts **A** and **C**
of the script (blocking), and has a time-consuming operation on part **B**.
Rhino UI is frozen during the blocking portions, but is fully available
otherwise. Notice that:

  * Script specifies `// async: true`. **This means that the complete script is running on Non-UI thread.**

  * To make sure **parts A and C are running on UI thread** and can make changes to Rhino, we use `Application.Instance.Invoke`. This method is provided by Eto which is the UI framework Rhino >=8 uses, and ensures the given action runs on the UI thread.

  * On part B, script is calling `.GetAwaiter().GetResult()` on the `Task<int>` object created by`Task.Run` call. This is to ensure **execution waits for the task to complete** and we have the result before proceeding to part C. Also notice that calling `Application.Instance.RunIteration` is not necessary here and causes a crash if called.

    
    
    // #! csharp
    // async: true
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    using Rhino;
    using Rhino.UI;
    using Eto.Forms;
    
    // Part A: runs on UI thread (blocking)
    Application.Instance.Invoke(() => {
        // CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
        StatusBar.ShowProgressMeter(0, 5, "Progress", true, false);
    });
    
    // Part B: runs on Non-UI thread
    int result = Task.Run(() => {
        for (int i = 0; i < 5; i++)
        {
            Thread.Sleep(1 * 1000);
            StatusBar.UpdateProgressMeter("Progress", i, true);
            // DO NOT CALL THIS SINCE WE ARE NOT ON UI THREAD
            // Application.Instance.RunIteration();
        }
    
        return 42;
    }).GetAwaiter().GetResult();
    
    // Part C: runs on UI thread (blocking)
    Application.Instance.Invoke(() => {
        // CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
        RhinoApp.WriteLine($"Result: {result}");
        StatusBar.HideProgressMeter();
    });
    

You can also debug this script by placing breakpoints inside the scope of each
part. Notice how the first and last breakpoints are paused on `Thread 1` (main
and UI thread in Rhino), but the breakpoint on line 19 is paused on `Thread
15` which happens to be the thread used to run the task by dotnet runtime:

![](https://developer.rhino3d.com/guides/scripting/advanced-async/editor-
csharp-mixed-debug.png)

Here is a similar example in Python. Note that we are using
`rhinoscriptsyntax` to handle the progress indicator. `part_a` and `part_c`
functions are executed on the main UI thread, and the middle part is executed
on the new thread created in the script:

    
    
    #! python3
    # async: true
    import threading
    import time
    import rhinoscriptsyntax as rs
    
    from Rhino import RhinoApp
    from Eto.Forms import Application
    
    
    class Job(threading.Thread):
        def __init__(self, id, name):
            super().__init__()
            self.id = id
            self.name = name
            self.result = 0
    
        def run(self):
            thread_id = threading.current_thread().ident
            print(f"Starting {self.name} on Thread: {thread_id}")
            for i in range(5):
                time.sleep(1) # wait to simulate work
                rs.StatusBarProgressMeterUpdate(i)
            self.result = 42
            print(f"Done {self.name}: {time.ctime(time.time())}")
    
    
    def part_a():
        # CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
        thread_id = threading.current_thread().ident
        print(f"Thread: {thread_id}")
        rs.StatusBarProgressMeterShow("Progress", 0, 5)
    
    def part_c(result):
        # CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
        thread_id = threading.current_thread().ident
        print(f"Thread: {thread_id}")
        print(f"Result: {result}")
        rs.StatusBarProgressMeterHide()
    
    
    RhinoApp.ClearCommandHistoryWindow()
    Application.Instance.Invoke(part_a)
    
    job1 = Job(1, "Job-1")
    job1.start()
    job1.join()
    
    result = job1.result
    
    Application.Instance.Invoke(lambda: part_c(result))
    
    print("Complete")
    

Notice that the thread id matches for `part_a` and `part_c`, but the middle
section is executed on a thread with a different id. Also note that thread
identifiers are different from dotnet thread ids when using C#:

![](https://developer.rhino3d.com/guides/scripting/advanced-async/editor-
python-mixed-threadids.png)

### C# Async/Await

In C# (Rhino >= 8.12) you can use
[async/await](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-
programming/) for asynchronous programming. Here is an example of creating an
async function in the script editor:

    
    
    // #! csharp
    // async: true
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    async Task<int> Compute()
    {
        await Task.Delay(TimeSpan.FromMilliseconds(2000));
        return 42;
    }
    
    int result = await Compute();
    
    Console.WriteLine($"Result: {result}");
    

Notice that if we remove the `// async: true` line or set that to `false` the
editor shows an error on the `await` call in global scope:

![](https://developer.rhino3d.com/guides/scripting/advanced-async/editor-
csharp-await-error.png)

When running C# scripts, the editor recomposes the script into something that
looks like the example below. This is done so multiple instances of the same
script can be created, holding onto their own internal states, and executed
using different contexts. Notice that the main `__RunScript__` method is NOT
marked as _async_ :

    
    
    sealed class __RhinoCodeScript__ {
    public void __RunScript__(Rhino.Runtime.Code.Execution.RunContext __context__)
    {
            // YOUR SCRIPT IS EMBEDDED HERE
    }}
    

When using `await` in global scope, we need to mark the script as `// async:
true` to ensure `__RunScript__` is marked as `async` and returns a `Task`
instance so the editor can await the execution:

    
    
    sealed class __RhinoCodeScript__ {
    public async Task __RunScript__(Rhino.Runtime.Code.Execution.RunContext __context__)
    {
            async Task<int> Compute()
            {
                await Task.Delay(TimeSpan.FromMilliseconds(2000));
                return 42;
            }
    
            int result = await Compute();
    
            Console.WriteLine($"Result: {result}");
    }}
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/advanced-
async/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/advanced-
async/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

