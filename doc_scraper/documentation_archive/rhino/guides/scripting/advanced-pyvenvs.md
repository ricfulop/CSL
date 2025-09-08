---
url: https://developer.rhino3d.com/guides/scripting/advanced-pyvenvs/#python-3-shell
scraped_at: 2025-09-08T16:05:46.372241
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

[Python Package
Environments](https://developer.rhino3d.com/guides/scripting/advanced-
pyvenvs/)

  * Package Conflicts
    * A) PIP Install Failure
    * B) Runtime Conflicts
  * Virtual Environments
    * “Virtual” Environments in Rhino
    * Default Environment
    * Custom Environments
    * Invalid Environments
    * Site-Packages
    * Python 3 Shell

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Python Package Environments

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Monday, October 7, 2024)

## Package Conflicts

Sometimes scripts need different versions of the same package either
intentionally or through nested dependencies. Imagine this scenario:

  * File _script_a.py_ requires _pkg_a_ version 1
  * File _script_b.py_ requires _pkg_b_ version 2 which is dependent on _pkg_a_ version 2 (newer than pkg_a of _script_a_)
  * On a clean Rhino, running _script_a_ installs and loads _pkg_a_ v1
  * On a clean Rhino, running _script_b_ installs and loads _pkg_b_ \+ _pkg_a_ v2

Here is a few ways that package version conflicts can happen:

### A) PIP Install Failure

Following the scenario above, if _script_a_ is executed successfully in a
Rhino session, running _script_b_ will probably fail when installing _pkg_b_.
Script Editor is using _pip_ to install packages. Since, by default, all the
packages for all the various scripts are installed in the same directory (as
python normally does), this creates a conflict when pip is trying to remove
_pkg_a_ v1 to install _pkg_a_ v2. Remember Rhino has already executed
_script_a_ , therefore _pkg_a_ libraries are loaded in memory and at least on
Windows, these library files are locked and can not be deleted while Rhino is
running.

Any pip install error will mark the environment as _Invalid_ and will cleanup
after Rhino is restarted.

### B) Runtime Conflicts

Following the scenario above, even if the two version of _pkg_a_ can be
installed at the same time, _pkg_a_ is already loaded in Python 3 runtime and
loading another version of this package (that is in the same directory) might
lead to runtime errors and unexpected behaviour.

## Virtual Environments

Tools like _pipenv_ and other environment managers for Python, normally solve
this problem by creating multiple **Virtual Environment** s. Each virtual
environment has a dedicated folder with its own `site-packages` (where pip
installs packages by default). Python core binaries are then linked into this
folder to create a fully functional Python environment. Following the scenario
above:

  * File _script_a.py_ requires _pkg_a_ version 1 - installed in _venv_a_
  * File _script_b.py_ requires _pkg_a_ version 2 through _pkg_b_ version 2 - installed in _venv_b_

So each script is created inside a unique virtual environment and are run
independently of each other:

![](https://developer.rhino3d.com/guides/scripting/advanced-pyvenvs/venvs-
python.jpg)

### “Virtual” Environments in Rhino

Virtual Environments (vnev) in Rhino are implemented differently. The main
reason is that in normal venvs, separate python processes run _script_a_ and
_script_b_ so there is no runtime conflict between these two processes. They
each have their own memory and python interpretter state.

In Rhino, however, both _script_a_ and _script_b_ are executed inside the same
process, same memory, and same python interpretter state. So we can not really
have true virtual environments unless you are running separate Rhino
processes:

![](https://developer.rhino3d.com/guides/scripting/advanced-pyvenvs/venvs-
rhino-conflict.jpg)

__Environments in Rhino __

Virtual Environments in Rhino are usually helpful in avoiding to reinstall
packages. If you are running a script with conflicting packages, pip has to
uninstall the existing to install new versions. This means that your scripts
keep uninstalling and reinstalling packages and will eventually overwrite each
other, corrupting the installed environment.

`venv` tag helps keeping these install packages separate and is great when
running scripts in separate Rhino processes:

![](https://developer.rhino3d.com/guides/scripting/advanced-pyvenvs/venvs-
rhino-noconflict.jpg)

Note that if you are running two scripts with two different versions of torch
library in the same Rhino instance you might/will run into runtime conflicts
as described above.

### Default Environment

By default, all python packages are installed to `site-envs/default-<unique-
id>` directory inside Python 3 runtime directory. This path is added to
`sys.path` and is the first path to be searched when importing installed
modules:

    
    
    /Users/*/.rhinocode/py39-rh8/site-envs/default-A6YRvqqN
    /Users/*/.rhinocode/py39-rh8/site-rhinoghpython
    /Users/*/.rhinocode/py39-rh8/site-rhinopython
    /Users/*/.rhinocode/py39-rh8/site-interop
    /Users/*/.rhinocode/py39-rh8/lib/python39.zip
    /Users/*/.rhinocode/py39-rh8/lib/python3.9
    

### Custom Environments

You can configure your script to install required packages in a custom
environment using `# venv: <environment-name>` tag. When running this example
script, Python 3 will create new folder `site-envs/my-pytorch-tools-<unique-
id>` to install pytorch v2.4.1 in that environment. `<unique-id>` is
automatically assigned to the environment to avoid conflicts:

    
    
    #! python 3
    # venv: my-pytorch-tools
    # r: torch==2.4.1
    
    import pytorch
    

This will ensure that the requirements for your package do not override any
existing installed packages for other scripts. If you are fixing the version
of a package in your script or use packages that might cause conflicts, it is
good practice to specify a unique name for this environment to avoid
conflicts.

### Invalid Environments

When a pip install error occurs, the target environment is marked as
_Invalid_. Therefore it is necesary to restart Rhino so editor can cleanup the
environment and start fresh.

### Site-Packages

As mentioned above, by default, all python packages are installed to `site-
envs/default-<unique-id>` directory. Sometimes it is necessary to install
packages under the default python `site-packages` folder. Normally this folder
is reserved for packages that Python 3 runtime inside of Rhino requires to
work e.g. `pip` itself.

There is a special environment id `site-packages`. This id can be used in your
scripts to force install packages into `site-packages` directory.

    
    
    #! python 3
    # venv: site-packages
    

In case any install errors occured, please run _Tools > Advanced > Reset
Python 3 (CPython) Runtime_ to reset the complete runtime and install a fresh
deployment of Python 3 with clean `site-packages` and `site-envs` directories.

### Python 3 Shell

When using Python 3 shell (from _Tools > Advanced > Open Python 3 Shell_), you
might want to manually install packages using _pip_. As the notes printed on
the shell describe, you would need to specify the `--target` option and point
`pip` to a specific environment under `site-envs` that you want to install the
packages to.

If `--target` is not specified, `pip` automatically installs packages under
`site-packages`.

![](https://developer.rhino3d.com/guides/scripting/advanced-pyvenvs/python-
shell-target.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/advanced-
pyvenvs/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/advanced-
pyvenvs/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

