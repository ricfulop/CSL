---
url: https://developer.rhino3d.com/guides/grasshopper/programming-task-capable-component/
scraped_at: 2025-09-08T15:41:39.115269
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

[Task Capable
Components](https://developer.rhino3d.com/guides/grasshopper/programming-task-
capable-component/)

  * Overview
  * The Interface
  * Example
  * Separate Methods
  * Implement the Interface

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Task Capable Components

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) and [Scott
Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated: Wednesday,
June 30, 2021)

## Overview

Grasshopper for Rhino allows you to develop multi-threaded components by way
of the new `IGH_TaskCapableComponent` interface. Benchmarks have shown that
Grasshopper can run significantly faster when using multi-threaded components.
Results may vary, as not all solutions can be computed in parallel.

## The Interface

When a component implements the `IGH_TaskCapableComponent` interface,
Grasshopper will notice and potentially call a full enumeration of
`SolveInstance` for the component twice in consecutive passes:

  1. The first pass is for collecting data and starting tasks to compute results
  2. The second pass is for using the results from the tasks to set outputs.

## Example

In this guide, we will convert a standard component into a task capable
component. In our example, the initial component code looks like this:

    
    
    public class FibonacciComponent : GH_Component
    {
      ...
      protected override void SolveInstance(IGH_DataAccess data)
      {
        const int max_steps = 46;
    
        int steps = 0;
        data.GetData(0, ref steps);
        if (steps < 0)
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Steps must be >= 0.");
          return;
        }
        if (steps > max_steps) // Prevent overflow...
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Error, $"Steps must be <= {max_steps}.");
          return;
        }
    
        int result;
        if (steps == 0)
          result = 0;
        else if (steps == 1)
          result = 1;
        else
        {
          int x = 0, y = 1, rc = 0;
          for (int i = 2; i <= steps; i++)
          {
            rc = x + y;
            x = y;
            y = rc;
          }
          result = rc;
        }
    
        data.SetData(0, result);
      }
      ...  
    }
    

## Separate Methods

Now you need to separate calculations into separate methods. Independent tasks
should not be directly accessing `IGH_DataAccess`, as that interface is not
thread safe. Thus, the we will want to break the current flow of a component’s
`SolveInstance` method into three distinct steps:

  1. Collect input data
  2. Compute results on given data
  3. Set output data

To implement _Step 2_ , we will break out the computation code into its own
method.

To start, create a public `SolveResults` class to hold the data for each
`SolveInstance` iteration. For this computation, our definition of
`SolveInstance` is very simple:

    
    
    public class SolveResults
    {
      public int Value { get; set; }
    }
    

Create a _Compute_ function that takes the input retrieved from
`IGH_DataAccess` and returns an instance of `SolveResults`.

    
    
    private static SolveResults ComputeFibonacci(int n)
    {
      SolveResults result = new SolveResults();
      if (n == 0)
        result.Value = 0;
      else if (n == 1)
        result.Value = 1;
      else
      {
        int x = 0, y = 1, rc = 0;
        for (int i = 2; i <= n; i++)
        {
          rc = x + y;
          x = y;
          y = rc;
        }
        result.Value = rc;
      }
      return result;
    }
    

## Implement the Interface

Now, we are ready to launch multiple tasks in the component.

Change the component’s inheritance from `GH_Component` to
`GH_TaskCapableComponent<T>`. In this example, modify the component from this:

`public class FibonacciComponent : GH_Component`

to this:

`public class FibonacciComponent :
GH_TaskCapableComponent<FibonacciComponent.SolveResults>`

Finally, modify `SolveInstance` to use tasks:

    
    
    protected override void SolveInstance(IGH_DataAccess data)
    {
      const int max_steps = 46;
    
      if (InPreSolve)
      {
        // First pass; collect input data
        int steps = 0;
        data.GetData(0, ref steps);
        if (steps < 0)
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Steps must be >= 0.");
          return;
        }
        if (steps > max_steps) // Prevent overflow...
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Error, $"Steps must be <= {max_steps}.");
          return;
        }
    
        // Queue up the task
        Task<SolveResults> task = Task.Run(() => ComputeFibonacci(steps), CancelToken);
        TaskList.Add(task);
        return;
      }
    
      if (!GetSolveResults(data, out SolveResults result))
      {
        // Compute right here; collect input data
        int steps = 0;
        data.GetData(0, ref steps);
        if (steps < 0)
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Steps must be >= 0.");
          return;
        }
        if (steps > max_steps) // Prevent overflow...
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Error, $"Steps must be <= {max_steps}.");
          return;
        }
    
        // Compute results on given data
        result = ComputeFibonacci(steps);
      }
    
      // Set output data
      if (result != null)
      {
        data.SetData(0, result.Value);
      }
    }
    

The full source code for this revision [can be seen
here](https://github.com/mcneel/rhino-developer-
samples/tree/7/grasshopper/cs/SampleGhTaskCapable).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/programming-
task-capable-component/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/programming-
task-capable-component/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

