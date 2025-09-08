---
url: https://developer.rhino3d.com/guides/compute/compute-javascript-getting-started/
scraped_at: 2025-09-08T15:43:16.518825
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

[Calling Compute with
JavaScript](https://developer.rhino3d.com/guides/compute/compute-javascript-
getting-started/)

  * Setting up a Compute Project using JavaScript
  * The first use of Compute

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

Calling Compute with JavaScript

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Thursday, November 12, 2020)

By the end of this guide, you should have all the tools installed necessary
for using the [Rhino Compute](https://www.rhino3d.com/compute) through
JavaScript.

The libraries will run on on all major browsers as well as node.js.

## Setting up a Compute Project using JavaScript

There are a few client side tools which need to be referenced that are
essential to communicate with the Compute server. These include:

  * **rhino3dm.js** \- Is part of the Rhino3dm project. It is a Javascript wrapper and web assembly (WASM) for [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) which contains the functions to read and write Rhino Geometry Objects.

  * **compute-rhino3d.js** \- This is a work in progress package which is meant to add classes available in RhinoCommon, but not available through rhino3dm.js. Compute-rhino3d makes calls into the McNeel Cloud Compute server for these functions. It handles all the transaction authorizations and JSON data conversion.

In a browser based application `index.html` would look like this:

    
    
    <html>
      <head>
      <!-- stuff -->
      </head>
      <body>
          <!-- Import maps polyfill -->
          <!-- Remove this when import maps will be widely supported -->
          <script async src="https://unpkg.com/es-module-shims@1.10.0/dist/es-module-shims.js"></script>
    
          <script type="importmap">
              {
                  "imports": {
                      "rhino3dm":"https://unpkg.com/rhino3dm@8.4.0/rhino3dm.module.min.js",
                      "rhinocompute": "https://www.unpkg.com/compute-rhino3d@0.13.0-beta/compute.rhino3d.module.js"
                  }
              }
          </script>
    
          <script type="module" src="./script.js"></script>
      </body>
    </html>
    

In the script.js, import the libraries:

    
    
    // Import libraries
    
    import rhino3dm from 'rhino3dm'
    import { RhinoCompute } from 'rhinocompute'
    
    // Load rhino3dm
    const rhino = await rhino3dm()
    console.log('Loaded rhino3dm.')
    
    // Your code ...
    

For a node.js application, first install the libraries with npm:

`npm i rhino3dm compute-rhino3d`

Then reference them in your script:

    
    
    // Import libraries
    
    import rhino3dm from 'rhino3dm'
    import RhinoCompute from 'compute-rhino3d'
    
    // Load rhino3dm
    const rhino = await rhino3dm()
    console.log('Loaded rhino3dm.')
    

## The first use of Compute

Examples of using JavaScript to access compute can be found in the [Javascript
Sample repo](https://github.com/mcneel/rhino-developer-
samples/tree/8/compute/js)

# Next Steps

_Congratulations!_ You have the tools to use [Rhino Compute
server](https://www.rhino3d.com/compute). _Now what?_

  1. To see the transactional nature of Compute, read through [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js)
  2. See a list of the [2400+ API calls](https://compute.rhino3d.com/sdk) available for compute.rhino3d.com.
  3. Download the [Compute Samples repo from GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute).
  4. The libraries are still very new and changing rapidly. Give them a try or get involved. Ask any questions or share what you are working on the [Compute Discussion Forum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/compute-
javascript-getting-started/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/compute-
javascript-getting-started/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

