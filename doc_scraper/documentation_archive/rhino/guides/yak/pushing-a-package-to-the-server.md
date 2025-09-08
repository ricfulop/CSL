---
url: https://developer.rhino3d.com/guides/yak/pushing-a-package-to-the-server
scraped_at: 2025-09-08T16:07:20.003712
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

[Pushing a Package to the
Server](https://developer.rhino3d.com/guides/yak/pushing-a-package-to-the-
server/)

  * Authentication
  * Push!
  * Troubleshooting
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

Pushing a Package to the Server

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Thursday, November 12, 2020)

See the [package server](https://developer.rhino3d.com/guides/yak/the-package-
server/) guide for more information about the McNeel public package server.

__Note __

Yak is cross-platform. The examples below are for Windows. For Mac, replace
the path to the Yak CLI tool with `"/Applications/Rhino
8.app/Contents/Resources/bin/yak"`.

## Authentication

Before you can push a package to the server, you need to authorize the Yak CLI
tool using your Rhino Account.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" login
    

A browser tab should open asking you to log in to Rhino Accounts (assuming you
are not already logged in). The next window will ask you to give “Yak” access
to your account.

  * **View basic info about you** : This scope is used to retrieve your name, locale and profile picture. This information will be used in the future, when the package database has a graphical interface.
  * **Verify your identity** : Used for authentication when querying package ownership.
  * **View your email address** : Your primary email address is stored so that you can be [added as an owner](../yak-cli-reference/#owner) of packages that others have published.

Once you’ve accepted, the browser window will close itself. Yak has retrieved
an OAuth token from Rhino Accounts and has stored this on your computer.

  * Mac - `~/.mcneel/yak.yml`
  * Windows - `%APPDATA%\McNeel\yak.yml`

__Note __

For security, the OAuth token is valid for a limited time only. Don’t be
surprised if the Yak CLI tool requires you to log in again after 30 days or
so.

## Push!

Now that you’re logged in, it’s possible to push a package to the server. I’ll
use the package created in the [previous guide](../creating-a-grasshopper-
plugin-package) as an example.

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" push marmoset-1.0.0-rh6_18-any.yak
    

This command doesn’t produce any output on success.

You can check that your package has been successfully pushed by searching for
it. You should see the name and version number of the package that you just
pushed. 🤞

    
    
    > "C:\Program Files\Rhino 8\System\Yak.exe" search --all --prerelease marmoset
    
    marmoset (1.0.0)
    

__Note __

If this is your first time, why not try pushing to the test server first?

    
    
    "C:\Program Files\Rhino 8\System\Yak.exe" push --source https://test.yak.rhino3d.com marmoset-1.0.0-rh6_18-any.yak
    
    "C:\Program Files\Rhino 8\System\Yak.exe" search --source https://test.yak.rhino3d.com --all --prerelease marmoset
    
    marmoset (1.0.0)
    

This server is wiped clean each night.

## Troubleshooting

There are a few reasons why pushing a package might not work.

  * Invalid `manifest.yml`

_The error message should be self explanatory. Fix it up and try again! You
can also try validating the YAML syntax itself with
a[linter](http://www.yamllint.com)._

  * The package name already exists, but you’re not an **owner**.

_Only package**owners** are permitted to push new versions of their packages.
When a user pushes the first version of a package, they become its **owner**.
Additional owners can be added with the [`owner`](../yak-cli-reference/#owner)
command._

  * The package version already exists.

_In order to prevent disruption to others who are using one of your packages,
it’s not possible to delete or overwrite versions. Roll the version number and
let your users know that there’s something new for them to try!_

  * Push something that you didn’t mean to?

_Use the[`yank` command](../yak-cli-reference/#yank) to unlist a specific
version._

## Related Topics

  * [The Package Server](https://developer.rhino3d.com/guides/yak/the-package-server/)
  * [Creating a Grasshopper Plug-in Package](https://developer.rhino3d.com/guides/yak/creating-a-grasshopper-plugin-package/)
  * [Creating a Rhino Plug-in Package](https://developer.rhino3d.com/guides/yak/creating-a-rhino-plugin-package/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/pushing-
a-package-to-the-server/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/pushing-
a-package-to-the-server/index.md) [
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

