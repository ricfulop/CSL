---
url: https://lists.openscad.org/empathy/thread/RY3MSEAOT7AENNE3VMMODVJNW3Q6NJEN
scraped_at: 2025-09-08T16:28:29.699207
title: Untitled
---

[ ![](/empathy/images/logo.png) ]( https://lists.openscad.org/empathy)

____

Hi,

Guest

![Pic](/empathy/images/default.jpg)

__

Sign In

Remember Me

Sign In

[ Click here to sign up for new account. ](/register)

[ Forgot your password? ](/password/reset)

###
[discuss@lists.openscad.org](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

OpenSCAD general discussion Mailing-list

[View all
threads](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

###  svg export

![](https://www.gravatar.com/avatar/6fd350fef2eaff46c7298878d030e1ac?d=blank&s=100)

TO

Trevor Orr

Mon, Aug 25, 2025 3:59 PM

In the latest snapshot when exporting to svg there is a dialog box that  
pops up that allows you to specify fill and stroke colors. Is there a  
way to specify those colors on the command line?

\--  
Trevor Orr  
customcribboards.com  
541-490-2422

In the latest snapshot when exporting to svg there is a dialog box that pops
up that allows you to specify fill and stroke colors. Is there a way to
specify those colors on the command line? \-- Trevor Orr customcribboards.com
541-490-2422

![](https://www.gravatar.com/avatar/8bbe7cbd3a3037a147b510110972aa32?d=blank&s=100)

JL

Jamie Larkby-Lahet

Mon, Aug 25, 2025 4:32 PM

I've been wondering about (disabling) 3mf color on the commandline as well.  
though I'm getting used to the yellow.

On Mon, Aug 25, 2025, 11:00 Trevor Orr via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

In the latest snapshot when exporting to svg there is a dialog box that  
pops up that allows you to specify fill and stroke colors. Is there a  
way to specify those colors on the command line?

\--  
Trevor Orr  
customcribboards.com  
541-490-2422

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I've been wondering about (disabling) 3mf color on the commandline as well.
though I'm getting used to the yellow. On Mon, Aug 25, 2025, 11:00 Trevor Orr
via Discuss < discuss@lists.openscad.org> wrote: > In the latest snapshot when
exporting to svg there is a dialog box that > pops up that allows you to
specify fill and stroke colors. Is there a > way to specify those colors on
the command line? > > > \-- > Trevor Orr > customcribboards.com > 541-490-2422
> > _______________________________________________ > OpenSCAD mailing list >
To unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/605cbbee6fefc10271a27ee79bba5157?d=blank&s=100)

TP

Torsten Paul

Mon, Aug 25, 2025 7:26 PM

$ openscad-nightly --help-export

OpenSCAD version 2025.08.03.nightly

List of settings that can be given using the -O option using the  
format '<section>/<key>=value', e.g.:  
openscad -O export-pdf/paper-size=a6 -O export-pdf/show-grid=false

Section 'export-pdf':

  * paper-size (enum): [a6,a5,<a4>,a3,letter,legal,tabloid]
  * orientation (enum): [<portrait>,landscape,auto]
  * show-filename (bool): true/<false>
  * show-scale (bool): <true>/false
  * show-scale-message (bool): <true>/false
  * show-grid (bool): true/<false>
  * grid-size (double): 1.000000 : <10.000000> : 100.000000
  * add-meta-data (bool): <true>/false
  * meta-data-title (string): ""
  * meta-data-author (string): ""
  * meta-data-subject (string): ""
  * meta-data-keywords (string): ""
  * fill (bool): true/<false>
  * fill-color (string): "black"
  * stroke (bool): <true>/false
  * stroke-color (string): "black"
  * stroke-width (double): 0.000000 : <0.350000> : 999.000000   
Section 'export-3mf':

  * color-mode (enum): [<model>,none,selected-only]
  * unit (enum): [micron,<millimeter>,centimeter,meter,inch,foot]
  * color (string): "#f9d72c"
  * material-type (enum): [color,<basematerial>]
  * decimal-precision (int): 1 : <6> : 16
  * add-meta-data (bool): <true>/false
  * meta-data-title (string): ""
  * meta-data-designer (string): ""
  * meta-data-description (string): ""
  * meta-data-copyright (string): ""
  * meta-data-license-terms (string): ""
  * meta-data-rating (string): ""   
Section 'export-svg':

  * fill (bool): true/<false>
  * fill-color (string): "white"
  * stroke (bool): <true>/false
  * stroke-color (string): "black"
  * stroke-width (double): 0.000000 : <0.350000> : 999.000000

$ openscad-nightly --help-export OpenSCAD version 2025.08.03.nightly List of
settings that can be given using the -O option using the format
'<section>/<key>=value', e.g.: openscad -O export-pdf/paper-size=a6 -O export-
pdf/show-grid=false Section 'export-pdf': \- paper-size (enum):
[a6,a5,<a4>,a3,letter,legal,tabloid] \- orientation (enum):
[<portrait>,landscape,auto] \- show-filename (bool): true/<false> \- show-
scale (bool): <true>/false \- show-scale-message (bool): <true>/false \- show-
grid (bool): true/<false> \- grid-size (double): 1.000000 : <10.000000> :
100.000000 \- add-meta-data (bool): <true>/false \- meta-data-title (string):
"" \- meta-data-author (string): "" \- meta-data-subject (string): "" \- meta-
data-keywords (string): "" \- fill (bool): true/<false> \- fill-color
(string): "black" \- stroke (bool): <true>/false \- stroke-color (string):
"black" \- stroke-width (double): 0.000000 : <0.350000> : 999.000000 Section
'export-3mf': \- color-mode (enum): [<model>,none,selected-only] \- unit
(enum): [micron,<millimeter>,centimeter,meter,inch,foot] \- color (string):
"#f9d72c" \- material-type (enum): [color,<basematerial>] \- decimal-precision
(int): 1 : <6> : 16 \- add-meta-data (bool): <true>/false \- meta-data-title
(string): "" \- meta-data-designer (string): "" \- meta-data-description
(string): "" \- meta-data-copyright (string): "" \- meta-data-license-terms
(string): "" \- meta-data-rating (string): "" Section 'export-svg': \- fill
(bool): true/<false> \- fill-color (string): "white" \- stroke (bool):
<true>/false \- stroke-color (string): "black" \- stroke-width (double):
0.000000 : <0.350000> : 999.000000

![](https://www.gravatar.com/avatar/6fd350fef2eaff46c7298878d030e1ac?d=blank&s=100)

TO

Trevor Orr

Mon, Aug 25, 2025 9:12 PM

Great, thanks. That is exactly what I needed.

On Mon, Aug 25, 2025 at 12:26 PM Torsten Paul via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

$ openscad-nightly --help-export

OpenSCAD version 2025.08.03.nightly

List of settings that can be given using the -O option using the  
format '<section>/<key>=value', e.g.:  
openscad -O export-pdf/paper-size=a6 -O export-pdf/show-grid=false

Section 'export-pdf':  
\- paper-size (enum): [a6,a5,<a4>,a3,letter,legal,tabloid]  
\- orientation (enum): [<portrait>,landscape,auto]  
\- show-filename (bool): true/<false>  
\- show-scale (bool): <true>/false  
\- show-scale-message (bool): <true>/false  
\- show-grid (bool): true/<false>  
\- grid-size (double): 1.000000 : <10.000000> : 100.000000  
\- add-meta-data (bool): <true>/false  
\- meta-data-title (string): ""  
\- meta-data-author (string): ""  
\- meta-data-subject (string): ""  
\- meta-data-keywords (string): ""  
\- fill (bool): true/<false>  
\- fill-color (string): "black"  
\- stroke (bool): <true>/false  
\- stroke-color (string): "black"  
\- stroke-width (double): 0.000000 : <0.350000> : 999.000000  
Section 'export-3mf':  
\- color-mode (enum): [<model>,none,selected-only]  
\- unit (enum): [micron,<millimeter>,centimeter,meter,inch,foot]  
\- color (string): "#f9d72c"  
\- material-type (enum): [color,<basematerial>]  
\- decimal-precision (int): 1 : <6> : 16  
\- add-meta-data (bool): <true>/false  
\- meta-data-title (string): ""  
\- meta-data-designer (string): ""  
\- meta-data-description (string): ""  
\- meta-data-copyright (string): ""  
\- meta-data-license-terms (string): ""  
\- meta-data-rating (string): ""  
Section 'export-svg':  
\- fill (bool): true/<false>  
\- fill-color (string): "white"  
\- stroke (bool): <true>/false  
\- stroke-color (string): "black"  
\- stroke-width (double): 0.000000 : <0.350000> : 999.000000

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

\--  
Trevor Orr  
customcribboards.com  
541-490-2422

Great, thanks. That is exactly what I needed. On Mon, Aug 25, 2025 at 12:26 PM
Torsten Paul via Discuss < discuss@lists.openscad.org> wrote: > $ openscad-
nightly --help-export > > OpenSCAD version 2025.08.03.nightly > > List of
settings that can be given using the -O option using the > format
'<section>/<key>=value', e.g.: > openscad -O export-pdf/paper-size=a6 -O
export-pdf/show-grid=false > > Section 'export-pdf': > \- paper-size (enum):
[a6,a5,<a4>,a3,letter,legal,tabloid] > \- orientation (enum):
[<portrait>,landscape,auto] > \- show-filename (bool): true/<false> > \- show-
scale (bool): <true>/false > \- show-scale-message (bool): <true>/false > \-
show-grid (bool): true/<false> > \- grid-size (double): 1.000000 : <10.000000>
: 100.000000 > \- add-meta-data (bool): <true>/false > \- meta-data-title
(string): "" > \- meta-data-author (string): "" > \- meta-data-subject
(string): "" > \- meta-data-keywords (string): "" > \- fill (bool):
true/<false> > \- fill-color (string): "black" > \- stroke (bool):
<true>/false > \- stroke-color (string): "black" > \- stroke-width (double):
0.000000 : <0.350000> : 999.000000 > Section 'export-3mf': > \- color-mode
(enum): [<model>,none,selected-only] > \- unit (enum):
[micron,<millimeter>,centimeter,meter,inch,foot] > \- color (string):
"#f9d72c" > \- material-type (enum): [color,<basematerial>] > \- decimal-
precision (int): 1 : <6> : 16 > \- add-meta-data (bool): <true>/false > \-
meta-data-title (string): "" > \- meta-data-designer (string): "" > \- meta-
data-description (string): "" > \- meta-data-copyright (string): "" > \- meta-
data-license-terms (string): "" > \- meta-data-rating (string): "" > Section
'export-svg': > \- fill (bool): true/<false> > \- fill-color (string): "white"
> \- stroke (bool): <true>/false > \- stroke-color (string): "black" > \-
stroke-width (double): 0.000000 : <0.350000> : 999.000000 >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > \-- Trevor Orr
customcribboards.com 541-490-2422

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

