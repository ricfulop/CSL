---
url: https://developer.rhino3d.com/guides/yak/yak-cli-reference/
scraped_at: 2025-09-08T15:58:04.062263
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

[Yak Command Line Tool
Reference](https://developer.rhino3d.com/guides/yak/yak-cli-reference/)

  * Commands
    * Build
    * Install
    * List
    * Login
    * Push
    * Search
    * Spec
    * Uninstall
    * Yank
    * Unyank
    * Owner
  * Downloads
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Package Manager
Guides](https://developer.rhino3d.com/en/guides/yak/) /

Yak Command Line Tool Reference

by [Will Pearson](https://discourse.mcneel.com/u/will/) (Last updated:
Tuesday, July 29, 2025)

The Yak command line tool is included with Rhino 7 WIP. On Windows the tool is
located at `"C:\Program Files\Rhino 8\System\yak.exe"`. On macOS there is a
convenience script at `"/Applications/Rhino
8.app/Contents/Resources/bin/yak"`.

## Commands

### Build

  * _Since 0.2: Command added_
  * _Since 0.4: Supports multiple .gha files, .rhp files or anything else for that matter_
  * _Since 0.9: Appends distribution tag to filename and expands $version placeholder_
  * _Since 0.10.1: Adds`--platform` argument_

When run in a directory containing a valid `manifest.yaml` file, creates a
package containing all files in the directory.

    
    
    Usage: yak build [options]
    
    Options:
        --platform PLATFORM  The platform where the package will run ('win', 'mac' or 'any')
        -h, --help           Get help (equivalent to `yak help build`)
    

__Note __

A [distribution tag](../the-anatomy-of-a-package#distributions) (e.g.
`rh7-win`) is appended to the filename of the created package. The tag is
determined by inspecting the contents of the package during creation. The
`--platform=any` argument can be used if the author wants to publish a cross-
platform distribution, e.g. `rh7-any`. Only .rhp and .gha files can currently
be inspected. If a package contains none of these, it will have a distribution
tag of `any-any`.

### Install

  * _Since 0.1: Command added_
  * _Since 0.13.0: Supports installing local .yak files_

Installs a package (optionally with a specific version).

    
    
    Usage:
        yak install [--source=URL] <package> [<version>]
        yak install <package>
    

Where `<package>` is either the name of a package or the path to a local .yak
file.

### List

_Since 0.2_

Lists the packages installed on the machine.

    
    
    yak list
    

### Login

  * _Since 0.2: Command added_
  * _Since 0.10: User registered during login_

Authenticates with Rhino Accounts and stores a time-limited OAuth2 access
token so that the user can use commands which require authentication.

    
    
    Usage: yak login [options]
    
    Options:
        --ci              Generate a non-expiring API key and display it
        -s, --source URL  Package repository location [default: https://yak.rhino3d.com/].
        -h, --help        Get help (equivalent to `yak help login`)
    

On Windows, the token is stored in `%appdata%\McNeel\yak.yml`. On macOS, it is
stored in `~/.mcneel/yak.yml`.

During the first login, the user is registered on the server.

__Note __

In an automated build environment – e.g. a build machine, GitHub Actions, etc.
– the `yak` CLI tool can read the access token from the `YAK_TOKEN`
environment variable. Use the `--ci` flag to login and generate a token for
this purpose!

### Push

_Since 0.1_

Pushes a package to the server.

    
    
    yak push [--source=URL] <filename>
    

__Note __

Requires authentication.

### Search

  * _Since 0.1: Command added_
  * _Since 0.5: Adds`--all` and `--prerelease` flags_

Searches the server for packages which match `query`.

    
    
    Usage: yak search [options] <query>
    
      Options:
        --prerelease      Display prerelease package versions
        -a, --all         Display all package versions
        -s, --source URL  Package repository location
        -h, --help        Get help (equivalent to `yak help search`)
    

### Spec

  * _Since 0.2: Command added_
  * _Since 0.4: Adds support for inspecting .rhp files (RhinoCommon only)_

Creates a skeleton `manifest.yml` file based on the contents of the current
directory. When run in a directory containing a Grasshopper assembly (`.gha`)
or a RhinoCommon plug-in (`.rhp`) the file will be inspected and used to pre-
populate the `manifest.yml` file.

    
    
    yak spec
    

### Uninstall

_Since 0.1_

Uninstalls a package.

    
    
    yak uninstall <package>
    

### Yank

_Since 0.6_

Removes a version from the package index.

    
    
    yak yank <package> <version>
    

__Note __

Requires authentication.

Yanked versions do not appear in searches but can still be installed if the
exact package version is known. To all intents and purposes they are hidden.

It is not possible to re-push a package version that has been yanked. If you
find yourself in this situation, then simply roll the version number of your
package and push again.

If all versions of a package are removed, it will no longer show up in the
package index.

__Danger __

**Deleting a package from the McNeel server**

If you absolutely need to delete your package from the public server, please
email [support@mcneel.com](mailto:support@mcneel.com). Once a package has been
deleted, the name can no longer be used.

### Unyank

Works in the same way as the yank command, but in reverse!

### Owner

_Since 0.10_

Adds, removes of lists the owners of a package. Package owners can push new
versions of the package and (un)yank existing versions.

    
    
    Usage:
        yak owner add [--source=URL] <package> <email>
        yak owner remove [--source=URL] <package> <email>
        yak owner list [--source=URL] <package>
        
    Options:
        -h, --help
        -s, --source URL  Package repository location [default: https://yak.rhino3d.com/].
    

New owners can do everything that the original owner can do. Please bear this
in mind!

New owners must be registered on the server before they can be added to a
package. They can do this by running the
[`login`](https://developer.rhino3d.com/guides/yak/yak-cli-reference/#login)
command.

## Downloads

The `yak` CLI is available as a standalone executable for use in environments
where Rhino isn’t installed, such as on automated build machines.

  * <https://files.mcneel.com/yak/tools/0.13.0/yak.exe>
  * <https://files.mcneel.com/yak/tools/0.13.0/win-arm64/yak.exe>
  * <https://files.mcneel.com/yak/tools/0.13.0/mac/yak>
  * <https://files.mcneel.com/yak/tools/0.13.0/linux-x64/yak>
  * <https://files.mcneel.com/yak/tools/0.13.0/linux-arm64/yak>

## Related Topics

  * [Yak Guides and Tutorials](https://developer.rhino3d.com/guides/yak/)
  * [Anatomy of a Package](https://developer.rhino3d.com/guides/yak/the-anatomy-of-a-package/)
  * [The Package Manifest](https://developer.rhino3d.com/guides/yak/the-package-manifest/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/yak/yak-
cli-reference/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/yak/yak-
cli-reference/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

