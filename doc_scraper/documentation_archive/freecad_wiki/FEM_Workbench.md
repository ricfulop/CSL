---
url: https://wiki.freecad.org/FEM_Workbench
title: FEM Workbench
scraped_at: 2025-09-08 16:44:05
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Workflow
  * 3 Menu: Model Toggle Menu: Model subsection
    * 3.1 Materials
    * 3.2 Element Geometry
    * 3.3 Electromagnetic boundary conditions
    * 3.4 Fluid boundary conditions
    * 3.5 Geometrical analysis features
    * 3.6 Mechanical boundary conditions and loads
    * 3.7 Thermal boundary conditions and loads
    * 3.8 Overwrite Constants
  * 4 Menu: Mesh
  * 5 Menu: Solve Toggle Menu: Solve subsection
    * 5.1 Mechanical equations
    * 5.2 Electromagnetic equations
  * 6 Menu: Results Toggle Menu: Results subsection
    * 6.1 Filter functions
    * 6.2 Data Visualizations
  * 7 Menu: Utilities
  * 8 Context Menu
  * 9 Obsolete tools
  * 10 Preferences
  * 11 Information
  * 12 Tutorials
  * 13 Extending the FEM Workbench
  * 14 Extending the FEM Workbench documentation

# FEM Workbench

  * [Page](/FEM_Workbench "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:FEM_Workbench&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/FEM_Workbench)
  * [Edit](/index.php?title=FEM_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=FEM_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/FEM_Workbench.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=FEM_Workbench&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/FEM_Workbench)
  * [Edit](/index.php?title=FEM_Workbench&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=FEM_Workbench&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=FEM_Workbench&action=history)

General

  * [What links here](/Special:WhatLinksHere/FEM_Workbench "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/FEM_Workbench "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=FEM_Workbench&oldid=1626780 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=FEM_Workbench&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=FEM_Workbench&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
FEM+Workbench&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-FEM+Workbench&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/FEM_Workbench/id "FEM Module \(0% translated\)")
  * [Deutsch](/FEM_Workbench/de "Arbeitsbereich FEM \(100% translated\)")
  * English
  * [Türkçe](/FEM_Workbench/tr "FEM Module \(1% translated\)")
  * [español](/FEM_Workbench/es "Ambiente de trabajo MEF \(27% translated\)")
  * [français](/FEM_Workbench/fr "Atelier FEM \(100% translated\)")
  * [hrvatski](/FEM_Workbench/hr "FEM Moduli \(0% translated\)")
  * [italiano](/FEM_Workbench/it "Ambiente FEM \(64% translated\)")
  * [polski](/FEM_Workbench/pl "Środowisko pracy MES \(100% translated\)")
  * [português](/FEM_Workbench/pt "O modulo FEM \(0% translated\)")
  * [português do Brasil](/FEM_Workbench/pt-br "Bancada de trabalho FEM \(28% translated\)")
  * [română](/FEM_Workbench/ro "Atelierul MEF \(21% translated\)")
  * [suomi](/FEM_Workbench/fi "FEM Workbench \(1% translated\)")
  * [svenska](/FEM_Workbench/sv "FEM Workbench/sv \(0% translated\)")
  * [čeština](/FEM_Workbench/cs "FEM Module \(0% translated\)")
  * [русский](/FEM_Workbench/ru "Верстак FEM \(30% translated\)")
  * [中文](/FEM_Workbench/zh "FEM 工作台 \(20% translated\)")
  * [中文（中国大陆）](/FEM_Workbench/zh-cn "FEM Workbench/zh-cn \(0% translated\)")
  * [日本語](/FEM_Workbench/ja "有限要素法ワークベンチ \(9% translated\)")
  * [한국어](/FEM_Workbench/ko "FEM 작업대 \(8% translated\)")

![](/images/6/6f/Arrow-left.svg) ![](/images/9/91/Workbench_Draft.svg) [Draft
Workbench](/Draft_Workbench "Draft Workbench")

![](/images/f/f8/Workbench_Inspection.svg) [Inspection
Workbench](/Inspection_Workbench "Inspection Workbench")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

[![](/images/8/87/Workbench_FEM.svg)](/index.php?title=File:Workbench_FEM.svg&filetimestamp=20240405093343&)FEM
workbench icon

## Introduction

The FEM Workbench provides a modern [finite element
analysis](https://en.wikipedia.org/wiki/Finite_element_analysis) (FEA)
workflow for FreeCAD. Mainly this means all tools to make an analysis are
combined into one graphical user interface (GUI).

[![](/images/thumb/1/1b/FEMWorkbench_modern_v2.png/400px-
FEMWorkbench_modern_v2.png)](/index.php?title=File:FEMWorkbench_modern_v2.png&filetimestamp=20250814071804&)

## Workflow

The steps to carry out a finite element analysis are:

  1. Preprocessing: setting up the analysis problem. 
     1. Modeling the geometry: creating the geometry with FreeCAD, or importing it from a different application.
     2. Creating an analysis. 
        1. Adding simulation constraints such as loads and fixed supports to the geometric model.
        2. Adding materials to the parts of the geometric model.
        3. Creating a finite element mesh for the geometrical model, or importing it from a different application.
  2. Solving: running an external solver from within FreeCAD.
  3. Postprocessing: visualizing the analysis results from within FreeCAD, or exporting the results so they can be postprocessed with another application.

The FEM Workbench can be used on Linux, Windows, and Mac OSX. Since the
workbench makes use of external solvers, the amount of manual setup will
depend on the operating system that you are using. See [FEM
Install](/FEM_Install "FEM Install") for instructions on setting up the
external tools.

[![](/images/3/31/FEM_Workbench_workflow.svg)](/index.php?title=File:FEM_Workbench_workflow.svg&filetimestamp=20190417210813&)

Workflow of the FEM Workbench; the workbench calls two external programs to
perform meshing of a solid object, and perform the actual solution of the
finite element problem

## Menu: Model

  * [![](/images/7/71/FEM_Analysis.svg)](/index.php?title=File:FEM_Analysis.svg&filetimestamp=20201127153951&) [Analysis container](/FEM_Analysis "FEM Analysis"): Creates a new container for a mechanical analysis.

### Materials

    

  * [![](/images/c/c3/FEM_MaterialSolid.svg)](/index.php?title=File:FEM_MaterialSolid.svg&filetimestamp=20241127174537&) [Material for solid](/FEM_MaterialSolid "FEM MaterialSolid"): Lets you select a solid material from the database.

    

  * [![](/images/7/71/FEM_MaterialFluid.svg)](/index.php?title=File:FEM_MaterialFluid.svg&filetimestamp=20241127174534&) [Material for fluid](/FEM_MaterialFluid "FEM MaterialFluid"): Lets you select a fluid material from the database.

    

  * [![](/images/8/86/FEM_MaterialMechanicalNonlinear.svg)](/index.php?title=File:FEM_MaterialMechanicalNonlinear.svg&filetimestamp=20241127174535&) [Nonlinear mechanical material](/FEM_MaterialMechanicalNonlinear "FEM MaterialMechanicalNonlinear"): Lets you add a nonlinear mechanical material model.

    

  * [![](/images/a/aa/FEM_MaterialReinforced.svg)](/index.php?title=File:FEM_MaterialReinforced.svg&filetimestamp=20241127174536&) [Reinforced material (concrete)](/FEM_MaterialReinforced "FEM MaterialReinforced"): Lets you select reinforced materials consisting of a matrix and a reinforcement from the database.

    

  * [![](/images/b/bb/FEM_MaterialEditor.svg)](/index.php?title=File:FEM_MaterialEditor.svg&filetimestamp=20220613100116&) [Material editor](/FEM_MaterialEditor "FEM MaterialEditor"): Lets you open the material editor to edit materials.

### Element Geometry

    

  * [![](/images/5/5f/FEM_ElementGeometry1D.svg)](/index.php?title=File:FEM_ElementGeometry1D.svg&filetimestamp=20240405093712&) [Beam cross section](/FEM_ElementGeometry1D "FEM ElementGeometry1D"): Used to define cross sections for beam elements.

    

  * [![](/images/a/a9/FEM_ElementRotation1D.svg)](/index.php?title=File:FEM_ElementRotation1D.svg&filetimestamp=20240405093737&) [Beam rotation](/FEM_ElementRotation1D "FEM ElementRotation1D"): Used to rotate cross sections of beam elements.

    

  * [![](/images/d/de/FEM_ElementGeometry2D.svg)](/index.php?title=File:FEM_ElementGeometry2D.svg&filetimestamp=20240405093724&) [Shell plate thickness](/FEM_ElementGeometry2D "FEM ElementGeometry2D"): Used to define shell element thickness.

    

  * [![](/images/4/40/FEM_ElementFluid1D.svg)](/index.php?title=File:FEM_ElementFluid1D.svg&filetimestamp=20240405093801&) [Fluid section for 1D flow](/FEM_ElementFluid1D "FEM ElementFluid1D"): Used to create fluid section element for pneumatic and hydraulic networks.

### Electromagnetic boundary conditions

    

  * [![](/images/3/35/FEM_ConstraintElectrostaticPotential.svg)](/index.php?title=File:FEM_ConstraintElectrostaticPotential.svg&filetimestamp=20241127174342&) [Electrostatic potential boundary condition](/FEM_ConstraintElectrostaticPotential "FEM ConstraintElectrostaticPotential"): Used to define electrostatic potential.

    

  * [![](/images/b/b9/FEM_ConstraintCurrentDensity.svg)](/index.php?title=File:FEM_ConstraintCurrentDensity.svg&filetimestamp=20240405093942&) [Current density boundary condition](/FEM_ConstraintCurrentDensity "FEM ConstraintCurrentDensity"): Used to define a current density. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

    

  * [![](/images/5/58/FEM_ConstraintMagnetization.svg)](/index.php?title=File:FEM_ConstraintMagnetization.svg&filetimestamp=20240405093815&) [Magnetization boundary condition](/FEM_ConstraintMagnetization "FEM ConstraintMagnetization"): Used to define a magnetization. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

    

  * [![](/images/d/db/FEM_ConstraintElectricChargeDensity.svg)](/index.php?title=File:FEM_ConstraintElectricChargeDensity.svg&filetimestamp=20250329180554&) [Electric charge density](/FEM_ElectricChargeDensity "FEM ElectricChargeDensity"): Used to define electric charge density load. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

### Fluid boundary conditions

    

  * [![](/images/9/92/FEM_ConstraintInitialFlowVelocity.svg)](/index.php?title=File:FEM_ConstraintInitialFlowVelocity.svg&filetimestamp=20241127174347&) [Initial flow velocity condition](/FEM_ConstraintInitialFlowVelocity "FEM ConstraintInitialFlowVelocity"): Used to define an initial flow velocity for a body (volume).

    

  * [![](/images/b/b9/FEM_ConstraintInitialPressure.svg)](/index.php?title=File:FEM_ConstraintInitialPressure.svg&filetimestamp=20241127174348&) [Initial pressure condition](/FEM_ConstraintInitialPressure "FEM ConstraintInitialPressure"): Used to define an initial pressure for a body (volume). [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

    

  * [![](/images/c/c2/FEM_ConstraintFlowVelocity.svg)](/index.php?title=File:FEM_ConstraintFlowVelocity.svg&filetimestamp=20241127174344&) [Flow velocity boundary condition](/FEM_ConstraintFlowVelocity "FEM ConstraintFlowVelocity"): Used to define a flow velocity as a boundary condition at an edge (2D) or face (3D).

### Geometrical analysis features

    

  * [![](/images/4/42/FEM_ConstraintPlaneRotation.svg)](/index.php?title=File:FEM_ConstraintPlaneRotation.svg&filetimestamp=20240405093850&) [Plane multi-point constraint](/FEM_ConstraintPlaneRotation "FEM ConstraintPlaneRotation"): Used to define a constraint for keeping the nodes on a planar surface on the same plane.

    

  * [![](/images/a/ae/FEM_ConstraintSectionPrint.svg)](/index.php?title=File:FEM_ConstraintSectionPrint.svg&filetimestamp=20241127174351&) [Section print feature](/FEM_ConstraintSectionPrint "FEM ConstraintSectionPrint"): Used to print the predefined facial output variables (forces and moments) to the data file.

    

  * [![](/images/1/18/FEM_ConstraintTransform.svg)](/index.php?title=File:FEM_ConstraintTransform.svg&filetimestamp=20240405093749&) [Local coordinate system](/FEM_ConstraintTransform "FEM ConstraintTransform"): Used to define a local coordinate system for a face.

### Mechanical boundary conditions and loads

    

  * [![](/images/3/37/FEM_ConstraintFixed.svg)](/index.php?title=File:FEM_ConstraintFixed.svg&filetimestamp=20241127174343&) [Fixed boundary condition](/FEM_ConstraintFixed "FEM ConstraintFixed"): Used to define a fixed boundary condition on point/edge/face(s).

    

  * [![](/images/6/63/FEM_ConstraintRigidBody.svg)](/index.php?title=File:FEM_ConstraintRigidBody.svg&filetimestamp=20240518110739&) [Rigid body constraint](/FEM_ConstraintRigidBody "FEM ConstraintRigidBody"): Used to apply the CalculiX's rigid body constraint that constrains the motion of the nodes of a selected geometrical entity to the motion of a reference point positioned by the user. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

    

  * [![](/images/9/96/FEM_ConstraintDisplacement.svg)](/index.php?title=File:FEM_ConstraintDisplacement.svg&filetimestamp=20241127174341&) [Displacement boundary condition](/FEM_ConstraintDisplacement "FEM ConstraintDisplacement"): Used to define a displacement boundary condition on point/edge/face(s).

    

  * [![](/images/c/cf/FEM_ConstraintContact.svg)](/index.php?title=File:FEM_ConstraintContact.svg&filetimestamp=20241127174340&) [Contact constraint](/FEM_ConstraintContact "FEM ConstraintContact"): Used to define a contact constraint between two faces.

    

  * [![](/images/2/23/FEM_ConstraintTie.svg)](/index.php?title=File:FEM_ConstraintTie.svg&filetimestamp=20240405093826&) [Tie constraint](/FEM_ConstraintTie "FEM ConstraintTie"): Used to define a tie constraint ("bonded contact") between two faces, or, [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0"), cyclic symmetry.

    

  * [![](/images/2/2f/FEM_ConstraintSpring.svg)](/index.php?title=File:FEM_ConstraintSpring.svg&filetimestamp=20241127174528&) [Spring](/FEM_ConstraintSpring "FEM ConstraintSpring"): Used to define a spring boundary condition. [introduced in 0.20](/Release_notes_0.20 "Release notes 0.20")

    

  * [![](/images/b/b9/FEM_ConstraintForce.svg)](/index.php?title=File:FEM_ConstraintForce.svg&filetimestamp=20201127154623&) [Force load](/FEM_ConstraintForce "FEM ConstraintForce"): Used to define a force in [N] applied uniformly to the selected geometric entity in the defined direction.

    

  * [![](/images/9/90/FEM_ConstraintPressure.svg)](/index.php?title=File:FEM_ConstraintPressure.svg&filetimestamp=20241127174349&) [Pressure load](/FEM_ConstraintPressure "FEM ConstraintPressure"): Used to define a pressure load.

    

  * [![](/images/1/1f/FEM_ConstraintCentrif.svg)](/index.php?title=File:FEM_ConstraintCentrif.svg&filetimestamp=20240405093838&) [Centrifugal load](/FEM_ConstraintCentrif "FEM ConstraintCentrif"): Used to define a centrifugal force body load. [introduced in 0.20](/Release_notes_0.20 "Release notes 0.20")

    

  * [![](/images/5/5f/FEM_ConstraintSelfWeight.svg)](/index.php?title=File:FEM_ConstraintSelfWeight.svg&filetimestamp=20241127174351&) [Gravity load](/FEM_ConstraintSelfWeight "FEM ConstraintSelfWeight"): Used to define a gravity acceleration acting on a model.

### Thermal boundary conditions and loads

    

  * [![](/images/3/3e/FEM_ConstraintInitialTemperature.svg)](/index.php?title=File:FEM_ConstraintInitialTemperature.svg&filetimestamp=20240405093910&) [Initial temperature](/FEM_ConstraintInitialTemperature "FEM ConstraintInitialTemperature"): Used to define the initial temperature of a body.

    

  * [![](/images/7/7e/FEM_ConstraintHeatflux.svg)](/index.php?title=File:FEM_ConstraintHeatflux.svg&filetimestamp=20241127174346&) [Heat flux load](/FEM_ConstraintHeatflux "FEM ConstraintHeatflux"): Used to define a heat flux load on a face(s).

    

  * [![](/images/0/0e/FEM_ConstraintTemperature.svg)](/index.php?title=File:FEM_ConstraintTemperature.svg&filetimestamp=20241127174528&) [Temperature boundary condition](/FEM_ConstraintTemperature "FEM ConstraintTemperature"): Used to define a temperature boundary condition on a point/edge/face(s).

    

  * [![](/images/9/9e/FEM_ConstraintBodyHeatSource.svg)](/index.php?title=File:FEM_ConstraintBodyHeatSource.svg&filetimestamp=20240405093953&) [Body heat source](/FEM_ConstraintBodyHeatSource "FEM ConstraintBodyHeatSource"): Used to define an internally generated body heat.

### Overwrite Constants

    

  * [![](/images/1/12/FEM_ConstantVacuumPermittivity.svg)](/index.php?title=File:FEM_ConstantVacuumPermittivity.svg&filetimestamp=20210224174136&) [Constant vacuum permittivity](/FEM_ConstantVacuumPermittivity "FEM ConstantVacuumPermittivity"): Used to overwrite the [permittivity of vacuum](https://en.wikipedia.org/wiki/Vacuum_permittivity) with a custom value.

## Menu: Mesh

  * [![](/images/1/15/FEM_MeshNetgenFromShape.svg)](/index.php?title=File:FEM_MeshNetgenFromShape.svg&filetimestamp=20241127174540&) [FEM mesh from shape by Netgen](/FEM_MeshNetgenFromShape "FEM MeshNetgenFromShape"): Generates a finite element mesh for a model using Netgen.

  * [![](/images/c/cc/FEM_MeshGmshFromShape.svg)](/index.php?title=File:FEM_MeshGmshFromShape.svg&filetimestamp=20241127174539&) [FEM mesh from shape by Gmsh](/FEM_MeshGmshFromShape "FEM MeshGmshFromShape"): Generates a finite element mesh for a model using Gmsh.

  * [![](/images/3/35/FEM_MeshBoundaryLayer.svg)](/index.php?title=File:FEM_MeshBoundaryLayer.svg&filetimestamp=20240405093531&) [FEM mesh boundary layer](/FEM_MeshBoundaryLayer "FEM MeshBoundaryLayer"): Creates anisotropic meshes for accurate calculations near boundaries.

  * [![](/images/2/2b/FEM_MeshRegion.svg)](/index.php?title=File:FEM_MeshRegion.svg&filetimestamp=20240405093602&) [FEM mesh region](/FEM_MeshRegion "FEM MeshRegion"): Creates a localized area(s) to mesh which highly optimizes analysis time.

  * [![](/images/0/04/FEM_MeshGroup.svg)](/index.php?title=File:FEM_MeshGroup.svg&filetimestamp=20240405093546&) [FEM mesh group](/FEM_MeshGroup "FEM MeshGroup"): Groups and labels elements of a mesh (vertex, edge, surface) together, useful for exporting the mesh to external solvers.

  * [![](/images/1/17/FEM_CreateElementsSet.svg)](/index.php?title=File:FEM_CreateElementsSet.svg&filetimestamp=20240714162546&) [Erase Elements](/FEM_CreateElementsSet "FEM CreateElementsSet"): Hides elements selected by a polygon from the mesh. [introduced in 1.0](/Release_notes_1.0 "Release notes 1.0")

  * [![](/images/5/56/FEM_FemMesh2Mesh.svg)](/index.php?title=File:FEM_FemMesh2Mesh.svg&filetimestamp=20201127172710&) [FEM mesh to mesh](/FEM_FemMesh2Mesh "FEM FemMesh2Mesh"): Converts surfaces of 3D elements or whole 2D elements of a selected FEM mesh to surface mesh.

## Menu: Solve

  * [![](/images/7/7d/FEM_SolverCalculixCcxtools.svg)](/index.php?title=File:FEM_SolverCalculixCcxtools.svg&filetimestamp=20250512143551&) [Solver CalculiX](/FEM_SolverCalculixCcxtools "FEM SolverCalculixCcxtools"): Creates a new solver for this analysis.

  * [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer"): Creates the solver controller for the Elmer solver.

  * [![](/images/d/db/FEM_SolverMystran.svg)](/index.php?title=File:FEM_SolverMystran.svg&filetimestamp=20240405093456&) [Solver Mystran](/FEM_SolverMystran "FEM SolverMystran"): Creates the solver controller for the MYSTRAN solver. [introduced in 0.20](/Release_notes_0.20 "Release notes 0.20")

  * [![](/images/d/dc/FEM_SolverZ88.svg)](/index.php?title=File:FEM_SolverZ88.svg&filetimestamp=20241127174551&) [Solver Z88](/FEM_SolverZ88 "FEM SolverZ88"): Creates the solver controller for the Z88 solver.

### Mechanical equations

    

  * [![](/images/8/8a/FEM_EquationElasticity.svg)](/index.php?title=File:FEM_EquationElasticity.svg&filetimestamp=20241127174531&) [Elasticity equation](/FEM_EquationElasticity "FEM EquationElasticity"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to perform linear mechanical analyses.

    

  * [![](/images/4/4e/FEM_EquationDeformation.svg)](/index.php?title=File:FEM_EquationDeformation.svg&filetimestamp=20241127174530&) [Deformation equation](/FEM_EquationDeformation "FEM EquationDeformation"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to perform nonlinear mechanical analyses (deformations). [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

### Electromagnetic equations

    

  * [![](/images/0/0b/FEM_EquationElectrostatic.svg)](/index.php?title=File:FEM_EquationElectrostatic.svg&filetimestamp=20240405093637&) [Electrostatic equation](/FEM_EquationElectrostatic "FEM EquationElectrostatic"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to perform electrostatic analyses.

    

  * [![](/images/e/ed/FEM_EquationElectricforce.svg)](/index.php?title=File:FEM_EquationElectricforce.svg&filetimestamp=20240405093658&) [Electricforce equation](/FEM_EquationElectricforce "FEM EquationElectricforce"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to calculate the electric force on surfaces.

    

  * [![](/images/4/49/FEM_EquationMagnetodynamic.svg)](/index.php?title=File:FEM_EquationMagnetodynamic.svg&filetimestamp=20240405093626&) [Magnetodynamic equation](/FEM_EquationMagnetodynamic "FEM EquationMagnetodynamic"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to calculate magnetodynamics. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

    

  * [![](/images/4/42/FEM_EquationMagnetodynamic2D.svg)](/index.php?title=File:FEM_EquationMagnetodynamic2D.svg&filetimestamp=20240405093613&) [Magnetodynamic 2D equation](/FEM_EquationMagnetodynamic2D "FEM EquationMagnetodynamic2D"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to calculate magnetodynamics in 2D. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

    

  * [![](/images/9/9d/FEM_EquationStaticCurrent.svg)](/index.php?title=File:FEM_EquationStaticCurrent.svg&filetimestamp=20250301105552&) [Static current equation](/FEM_EquationStaticCurrent "FEM EquationStaticCurrent"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to calculate static current conduction. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

  * [![](/images/5/5b/FEM_EquationFlow.svg)](/index.php?title=File:FEM_EquationFlow.svg&filetimestamp=20241127174532&) [Flow equation](/FEM_EquationFlow "FEM EquationFlow"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to perform flow analyses.

  * [![](/images/d/d5/FEM_EquationFlux.svg)](/index.php?title=File:FEM_EquationFlux.svg&filetimestamp=20240405093647&) [Flux equation](/FEM_EquationFlux "FEM EquationFlux"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to perform flux analyses.

  * [![](/images/a/a6/FEM_EquationHeat.svg)](/index.php?title=File:FEM_EquationHeat.svg&filetimestamp=20241127174532&) [Heat equation](/FEM_EquationHeat "FEM EquationHeat"): Equation for the [![](/images/4/47/FEM_SolverElmer.svg)](/index.php?title=File:FEM_SolverElmer.svg&filetimestamp=20241127174550&) [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") to perform heat transfer analyses.

  * [![](/images/3/38/FEM_SolverControl.svg)](/index.php?title=File:FEM_SolverControl.svg&filetimestamp=20240405093430&) [Solver job control](/FEM_SolverControl "FEM SolverControl"): Opens the menu to adjust and start the selected solver.

  * [![](/images/8/8e/FEM_SolverRun.svg)](/index.php?title=File:FEM_SolverRun.svg&filetimestamp=20240405093508&) [Run solver calculations](/FEM_SolverRun "FEM SolverRun"): Runs the selected solver of the active analysis.

## Menu: Results

  * [![](/images/5/53/FEM_ResultsPurge.svg)](/index.php?title=File:FEM_ResultsPurge.svg&filetimestamp=20241127174549&) [Purge results](/FEM_ResultsPurge "FEM ResultsPurge"): Deletes the results of the active analysis.

  * [![](/images/9/90/FEM_ResultShow.svg)](/index.php?title=File:FEM_ResultShow.svg&filetimestamp=20241127174549&) [Show result](/FEM_ResultShow "FEM ResultShow"): Used to display the result of an analysis. This dialog is not available for the [Solver Elmer](/FEM_SolverElmer "FEM SolverElmer") as this solver visualizes using the [Post pipeline from result](/FEM_PostPipelineFromResult "FEM PostPipelineFromResult") object only.

  * [![](/images/9/90/FEM_PostApplyChanges.svg)](/index.php?title=File:FEM_PostApplyChanges.svg&filetimestamp=20201127175526&) [Apply changes to pipeline](/FEM_PostApplyChanges "FEM PostApplyChanges"): Toggles if changes to pipelines and filters are applied immediately.

  * [![](/images/8/8f/FEM_PostPipelineFromResult.svg)](/index.php?title=File:FEM_PostPipelineFromResult.svg&filetimestamp=20241127174548&) [Post pipeline from result](/FEM_PostPipelineFromResult "FEM PostPipelineFromResult"): Used to add a new graphical representation of FEM analysis results (color scale and more display options).

  * [![](/images/2/22/FEM_PostBranchFilter.svg)](/index.php?title=File:FEM_PostBranchFilter.svg&filetimestamp=20250407090345&) [Pipeline branch](/FEM_PostBranchFilter "FEM PostBranchFilter"): Used to branch the results pipeline. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

  * [![](/images/6/61/FEM_PostFilterWarp.svg)](/index.php?title=File:FEM_PostFilterWarp.svg&filetimestamp=20241127174547&) [Warp filter](/FEM_PostFilterWarp "FEM PostFilterWarp"): Used to visualize the scaled deformed shape of the model.

  * [![](/images/1/1c/FEM_PostFilterClipScalar.svg)](/index.php?title=File:FEM_PostFilterClipScalar.svg&filetimestamp=20241127174543&) [Scalar clip filter](/FEM_PostFilterClipScalar "FEM PostFilterClipScalar"): Used to clip a field with a specified scalar value.

  * [![](/images/2/21/FEM_PostFilterCutFunction.svg)](/index.php?title=File:FEM_PostFilterCutFunction.svg&filetimestamp=20241127174544&) [Function cut filter](/FEM_PostFilterCutFunction "FEM PostFilterCutFunction"): Used to display the results on a plane, a sphere, a cylinder, or a box cutting through the model.

  * [![](/images/f/ff/FEM_PostFilterClipRegion.svg)](/index.php?title=File:FEM_PostFilterClipRegion.svg&filetimestamp=20241127174542&) [Region clip filter](/FEM_PostFilterClipRegion "FEM PostFilterClipRegion"): Used to clip a field with a plane, a sphere, a cylinder, or a box cutting through the model.

  * [![](/images/8/83/FEM_PostFilterContours.svg)](/index.php?title=File:FEM_PostFilterContours.svg&filetimestamp=20240405093518&) [Contours filter](/FEM_PostFilterContours "FEM PostFilterContours"): Used to display iso-lines (for analyses in 2D) or iso-contours. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

  * [![](/images/8/8c/FEM_PostFilterGlyph.svg)](/index.php?title=File:FEM_PostFilterGlyph.svg&filetimestamp=20250514123204&) [Glyph filter](/FEM_PostFilterGlyph "FEM PostFilterGlyph"): Used to create glyph (symbol) plots. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

  * [![](/images/c/c0/FEM_PostFilterDataAlongLine.svg)](/index.php?title=File:FEM_PostFilterDataAlongLine.svg&filetimestamp=20241127174544&) [Line clip filter](/FEM_PostFilterDataAlongLine "FEM PostFilterDataAlongLine"): Used to plot the values of a field along a specified line.

  * [![](/images/2/20/FEM_PostFilterLinearizedStresses.svg)](/index.php?title=File:FEM_PostFilterLinearizedStresses.svg&filetimestamp=20241127174546&) [Stress linearization plot](/FEM_PostFilterLinearizedStresses "FEM PostFilterLinearizedStresses"): Creates a stress linearization plot.

  * [![](/images/d/da/FEM_PostFilterDataAtPoint.svg)](/index.php?title=File:FEM_PostFilterDataAtPoint.svg&filetimestamp=20241127174545&) [Data at point clip filter](/FEM_PostFilterDataAtPoint "FEM PostFilterDataAtPoint"): Used to display value of a selected field at a given point.

  * [![](/images/a/a6/FEM_PostFilterCalculator.svg)](/index.php?title=File:FEM_PostFilterCalculator.svg&filetimestamp=20250407083543&) [Calculator filter](/FEM_PostFilterCalculator "FEM PostFilterCalculator"): Used to create custom fields by evaluating expressions operating on the existing fields. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

### Filter functions

    

  * [![](/images/0/05/FEM_PostCreateFunctionPlane.svg)](/index.php?title=File:FEM_PostCreateFunctionPlane.svg&filetimestamp=20230213105610&) [Plane](/FEM_PostCreateFunctionPlane "FEM PostCreateFunctionPlane"): Cuts the result mesh with a plane.

    

  * [![](/images/9/93/FEM_PostCreateFunctionSphere.svg)](/index.php?title=File:FEM_PostCreateFunctionSphere.svg&filetimestamp=20230213105650&) [Sphere](/FEM_PostCreateFunctionSphere "FEM PostCreateFunctionSphere"): Cuts the result mesh with a sphere.

    

  * [![](/images/f/f8/FEM_PostCreateFunctionCylinder.svg)](/index.php?title=File:FEM_PostCreateFunctionCylinder.svg&filetimestamp=20230309052901&) [Cylinder](/FEM_PostCreateFunctionCylinder "FEM PostCreateFunctionCylinder"): Cuts the result mesh with a cylinder. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

    

  * [![](/images/b/b0/FEM_PostCreateFunctionBox.svg)](/index.php?title=File:FEM_PostCreateFunctionBox.svg&filetimestamp=20230311125820&) [Box](/FEM_PostCreateFunctionBox "FEM PostCreateFunctionBox"): Cuts the result mesh with a box. [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")

### Data Visualizations

    

  * [![](/images/3/32/FEM_PostLineplot.svg)](/index.php?title=File:FEM_PostLineplot.svg&filetimestamp=20250626132317&) [Create Lineplot](/FEM_PostLineplot "FEM PostLineplot"): Creates a lineplot for a selected pipeline/filter. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

    

  * [![](/images/d/d7/FEM_PostHistogram.svg)](/index.php?title=File:FEM_PostHistogram.svg&filetimestamp=20250626132327&) [Create Histogram](/FEM_PostHistogram "FEM PostHistogram"): Creates a histogram for a selected pipeline/filter. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

    

  * [![](/images/4/4b/FEM_PostSpreadsheet.svg)](/index.php?title=File:FEM_PostSpreadsheet.svg&filetimestamp=20250626132336&) [Create Table](/FEM_PostSpreadsheet "FEM PostSpreadsheet"): Creates a table for a selected pipeline/filter. [introduced in 1.1](/Release_notes_1.1 "Release notes 1.1")

## Menu: Utilities

  * [![](/images/c/ca/FEM_ClippingPlaneAdd.svg)](/index.php?title=File:FEM_ClippingPlaneAdd.svg&filetimestamp=20241127174337&) [Clipping plane on face](/FEM_ClippingPlaneAdd "FEM ClippingPlaneAdd"): Adds a clipping plane for the whole model view.

  * [![](/images/2/2b/FEM_ClippingPlaneRemoveAll.svg)](/index.php?title=File:FEM_ClippingPlaneRemoveAll.svg&filetimestamp=20241127174338&) [Remove all clipping planes](/FEM_ClippingPlaneRemoveAll "FEM ClippingPlaneRemoveAll"): Removes all existing [clipping planes](/FEM_ClippingPlaneAdd "FEM ClippingPlaneAdd").

  * [![](/images/8/8b/FEM_Examples.svg)](/index.php?title=File:FEM_Examples.svg&filetimestamp=20200822023723&) [Open FEM examples](/FEM_Examples "FEM Examples"): Open the GUI to access FEM examples.

## Context Menu

  * [![](/images/c/c5/FEM_MeshClear.svg)](/index.php?title=File:FEM_MeshClear.svg&filetimestamp=20241127174537&) [Clear FEM mesh](/FEM_MeshClear "FEM MeshClear"): Deletes the mesh file from the FreeCAD file. Useful to make a FreeCAD file lighter.

  * [![](/images/4/4d/FEM_MeshDisplayInfo.svg)](/index.php?title=File:FEM_MeshDisplayInfo.svg&filetimestamp=20241127174538&) [Display FEM mesh info](/FEM_MeshDisplayInfo "FEM MeshDisplayInfo"): Displays basic statistics of existing mesh - number of nodes and elements of each type.

## Obsolete tools

  * [![](/images/7/7e/FEM_ConstraintFluidBoundary.svg)](/index.php?title=File:FEM_ConstraintFluidBoundary.svg&filetimestamp=20241127174345&) [Fluid boundary condition](/FEM_ConstraintFluidBoundary "FEM ConstraintFluidBoundary"): Used to define a fluid boundary condition. Did not have a solver. Not available in 1.0 and above.

  * [![](/images/6/69/FEM_ConstraintBearing.svg)](/index.php?title=File:FEM_ConstraintBearing.svg&filetimestamp=20241127174339&) [Constraint bearing](/FEM_ConstraintBearing "FEM ConstraintBearing"): Used to define a bearing constraint. Did not have a solver. Not available in 1.0 and above.

  * [![](/images/b/bf/FEM_ConstraintGear.svg)](/index.php?title=File:FEM_ConstraintGear.svg&filetimestamp=20241127174346&) [Constraint gear](/FEM_ConstraintGear "FEM ConstraintGear"): Used to define a gear constraint. Did not have a solver. Not available in 1.0 and above.

  * [![](/images/e/ef/FEM_ConstraintPulley.svg)](/index.php?title=File:FEM_ConstraintPulley.svg&filetimestamp=20241127174350&) [Constraint pulley](/FEM_ConstraintPulley "FEM ConstraintPulley"): Used to define a pulley constraint. Did not have a solver. Not available in 1.0 and above.

  * [![](/images/6/66/FEM_SolverCalculiX.svg)](/index.php?title=File:FEM_SolverCalculiX.svg&filetimestamp=20201127173254&) [Solver CalculiX (new framework)](/FEM_SolverCalculiX "FEM SolverCalculiX"): Same as the original framework [![](/images/7/7d/FEM_SolverCalculixCcxtools.svg)](/index.php?title=File:FEM_SolverCalculixCcxtools.svg&filetimestamp=20250512143551&) [Solver CalculiX](/FEM_SolverCalculixCcxtools "FEM SolverCalculixCcxtools") with extra checks. Tool was unfinished. Not available in 1.0 and above.

  * [![](/images/2/20/FEM_CreateNodesSet.svg)](/index.php?title=File:FEM_CreateNodesSet.svg&filetimestamp=20241127174529&) [Nodes set](/FEM_CreateNodesSet "FEM CreateNodesSet"): Creates/defines a node set from FEM mesh. Tool was unfinished and couldn't be used. Not available in 1.0 and above.

## Preferences

  * [![](/images/d/d5/Std_DlgPreferences.svg)](/index.php?title=File:Std_DlgPreferences.svg&filetimestamp=20240528092445&) [Preferences...](/FEM_Preferences "FEM Preferences"): Preferences available in FEM Tools.

## Information

The following pages explain different topics of the FEM Workbench.

[FEM Install](/FEM_Install "FEM Install"): a detailed description on how to
set up the external programs used in the workbench.

[FEM Geometry Preparation and Meshing](/FEM_Geometry_Preparation_and_Meshing
"FEM Geometry Preparation and Meshing"): tips regarding geometry preparation
for FEM and meshing.

[FEM Mesh](/FEM_Mesh "FEM Mesh"): details about meshes in the FEM workbench.

[FEM Solver](/FEM_Solver "FEM Solver"): further information on the different
solvers available in the workbench, and those that could be used in the
future.

[FEM CalculiX](/FEM_CalculiX "FEM CalculiX"): further information on CalculiX,
the default solver used in the workbench for structural analysis.

[FEM Concrete](/FEM_Concrete "FEM Concrete"): interesting information on the
topic of simulating concrete structures.

## Tutorials

Tutorial 1: [FEM CalculiX Cantilever 3D](/FEM_CalculiX_Cantilever_3D "FEM
CalculiX Cantilever 3D"); basic simply supported beam analysis.

Tutorial 2: [FEM Tutorial](/FEM_tutorial "FEM tutorial"); simple tension
analysis of a structure.

Tutorial 3: [FEM Tutorial Python](/FEM_Tutorial_Python "FEM Tutorial Python");
set up the cantilever example entirely through scripting in Python, including
the mesh.

Tutorial 4: [FEM Shear of a Composite Block](/FEM_Shear_of_a_Composite_Block
"FEM Shear of a Composite Block"); see the deformation of a block that is
comprised of two materials.

Tutorial 5: [Transient FEM analysis](/Transient_FEM_analysis "Transient FEM
analysis")

Tutorial 6: [Post-Processing of FEM Results with Paraview](/Post-
Processing_of_FEM_Results_with_Paraview "Post-Processing of FEM Results with
Paraview")

Tutorial 7: [FEM Example Capacitance Two
Balls](/FEM_Example_Capacitance_Two_Balls "FEM Example Capacitance Two
Balls"); Elmer's GUI tutorial 6 "Electrostatics Capacitance Two Balls" using
FEM Examples.

Coupled thermal mechanical analysis tutorials by
[openSIM](https://opensimsa.github.io/training.html)

Video tutorial 1: [FEM video for
beginner](https://forum.freecad.org/viewtopic.php?f=18&t=20499#p158353)
(including YouTube link)

Video tutorial 2: [FEM video for
beginner](https://forum.freecad.org/viewtopic.php?f=18&t=20499&start=10#p162321)
(including YouTube link)

Many video tutorials: [anisim Open Source Engineering
Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in
German)

## Extending the FEM Workbench

The FEM Workbench is under constant development. An objective of the project
is to find ways to easily interact with various FEM solvers, so that the end
user can streamline the process of creating, meshing, simulating, and
optimizing an engineering design problem, all within FreeCAD.

The following information is aimed at power users and developers who want to
extend the FEM Workbench in different ways. Familiarity with C++ and Python is
expected, and also some knowledge of the "document object" system used in
FreeCAD is necessary; this information is available in the [Power users
hub](/Power_users_hub "Power users hub") and the [Developer
hub](/Developer_hub "Developer hub"). Please notice that since FreeCAD is
under active development, some articles may be too old, and thus obsolete. The
most up to date information is discussed in the [FreeCAD
forums](https://forum.freecad.org/index.php), in the Development section. For
FEM discussions, advice or assistance in extending the workbench, the reader
should refer to the [FEM
subforum](https://forum.freecad.org/viewforum.php?f=18).

The following articles explain how the workbench can be extended, for example,
by adding new types of boundary conditions (constraints), or equations.

  * [Extend FEM Module](/Extend_FEM_Module "Extend FEM Module")
  * [Onboarding FEM Devs](/Onboarding_FEM_Devs "Onboarding FEM Devs") attempts to orient new devs on how to contribute to the FEM workbench.
  * [Add FEM Constraint Tutorial](/Add_FEM_Constraint_Tutorial "Add FEM Constraint Tutorial")
  * [Add FEM Equation Tutorial](/Add_FEM_Equation_Tutorial "Add FEM Equation Tutorial")

A developer's guide has been written to help power users in understanding the
complex FreeCAD codebase and the interactions between the core elements and
the individual workbenches. The book is hosted at github so multiple users can
contribute to it and keep it updated.

  * [Early preview of ebook: Module developer' guide to FreeCAD source](https://forum.freecad.org/viewtopic.php?t=17581) forum thread.
  * [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) github repository.

## Extending the FEM Workbench documentation

  * More information regarding extending or missing FEM documentation can be found in the forum: [FEM documentation missing on the Wiki](https://forum.freecad.org/viewtopic.php?f=18&t=20823)

  

![](/images/6/6f/Arrow-left.svg) ![](/images/9/91/Workbench_Draft.svg) [Draft
Workbench](/Draft_Workbench "Draft Workbench")

![](/images/f/f8/Workbench_Inspection.svg) [Inspection
Workbench](/Inspection_Workbench "Inspection Workbench")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/8/87/Workbench_FEM.svg)](/index.php?title=File:Workbench_FEM.svg&filetimestamp=20240405093343&)
FEM

  * [FEM Analysis](/FEM_Analysis "FEM Analysis")

  * **Materials:** [Solid](/FEM_MaterialSolid "FEM MaterialSolid"), [Fluid](/FEM_MaterialFluid "FEM MaterialFluid"), [Nonlinear mechanical](/FEM_MaterialMechanicalNonlinear "FEM MaterialMechanicalNonlinear"), [Reinforced (concrete)](/FEM_MaterialReinforced "FEM MaterialReinforced"); [Material editor](/FEM_MaterialEditor "FEM MaterialEditor")

  * **Element geometry:** [Beam (1D)](/FEM_ElementGeometry1D "FEM ElementGeometry1D"), [Beam rotation (1D)](/FEM_ElementRotation1D "FEM ElementRotation1D"), [Shell (2D)](/FEM_ElementGeometry2D "FEM ElementGeometry2D"), [Fluid flow (1D)](/FEM_ElementFluid1D "FEM ElementFluid1D")

* * *

**Constraints**

  * **Electromagnetic:** [Electrostatic potential](/FEM_ConstraintElectrostaticPotential "FEM ConstraintElectrostaticPotential"), [Current density](/FEM_ConstraintCurrentDensity "FEM ConstraintCurrentDensity"), [Magnetization](/FEM_ConstraintMagnetization "FEM ConstraintMagnetization")

  * **Fluid:** [Initial flow velocity](/FEM_ConstraintInitialFlowVelocity "FEM ConstraintInitialFlowVelocity"), [Initial pressure](/FEM_ConstraintInitialPressure "FEM ConstraintInitialPressure"), [Flow velocity](/FEM_ConstraintFlowVelocity "FEM ConstraintFlowVelocity")

  * **Geometrical:** [Plane rotation](/FEM_ConstraintPlaneRotation "FEM ConstraintPlaneRotation"), [Section print](/FEM_ConstraintSectionPrint "FEM ConstraintSectionPrint"), [Transform](/FEM_ConstraintTransform "FEM ConstraintTransform")

  * **Mechanical:** [Fixed](/FEM_ConstraintFixed "FEM ConstraintFixed"), [Displacement](/FEM_ConstraintDisplacement "FEM ConstraintDisplacement"), [Contact](/FEM_ConstraintContact "FEM ConstraintContact"), [Tie](/FEM_ConstraintTie "FEM ConstraintTie"), [Spring](/FEM_ConstraintSpring "FEM ConstraintSpring"), [Force](/FEM_ConstraintForce "FEM ConstraintForce"), [Pressure](/FEM_ConstraintPressure "FEM ConstraintPressure"), [Centrif](/FEM_ConstraintCentrif "FEM ConstraintCentrif"), [Self weight](/FEM_ConstraintSelfWeight "FEM ConstraintSelfWeight")

  * **Thermal:** [Initial temperature](/FEM_ConstraintInitialTemperature "FEM ConstraintInitialTemperature"), [Heat flux](/FEM_ConstraintHeatflux "FEM ConstraintHeatflux"), [Temperature](/FEM_ConstraintTemperature "FEM ConstraintTemperature"), [Body heat source](/FEM_ConstraintBodyHeatSource "FEM ConstraintBodyHeatSource")

  * **Overwrite Constants:** [Constant vacuum permittivity](/FEM_ConstantVacuumPermittivity "FEM ConstantVacuumPermittivity")

* * *

  * **Mesh:** [Mesh Netgen](/FEM_MeshNetgenFromShape "FEM MeshNetgenFromShape"), [Mesh GMSH](/FEM_MeshGmshFromShape "FEM MeshGmshFromShape"), [Mesh boundary layer](/FEM_MeshBoundaryLayer "FEM MeshBoundaryLayer"), [Mesh region](/FEM_MeshRegion "FEM MeshRegion"), [Mesh group](/FEM_MeshGroup "FEM MeshGroup"), [Nodes set](/FEM_CreateNodesSet "FEM CreateNodesSet"), [Mesh to mesh](/FEM_FemMesh2Mesh "FEM FemMesh2Mesh")

  * **Solve:** [CalculiX Standard](/FEM_SolverCalculixCcxtools "FEM SolverCalculixCcxtools"), [Elmer](/FEM_SolverElmer "FEM SolverElmer"), [Mystran](/FEM_SolverMystran "FEM SolverMystran"), [Z88](/FEM_SolverZ88 "FEM SolverZ88"); **Equations:** [Deformation](/FEM_EquationDeformation "FEM EquationDeformation"), [Elasticity](/FEM_EquationElasticity "FEM EquationElasticity"), [Electrostatic](/FEM_EquationElectrostatic "FEM EquationElectrostatic"), [Electricforce](/FEM_EquationElectricforce "FEM EquationElectricforce"), [Magnetodynamic](/FEM_EquationMagnetodynamic "FEM EquationMagnetodynamic"), [Magnetodynamic 2D](/FEM_EquationMagnetodynamic2D "FEM EquationMagnetodynamic2D"), [Flow](/FEM_EquationFlow "FEM EquationFlow"), [Flux](/FEM_EquationFlux "FEM EquationFlux"), [Heat](/FEM_EquationHeat "FEM EquationHeat"); **Solver:** [Solver control](/FEM_SolverControl "FEM SolverControl"), [Solver run](/FEM_SolverRun "FEM SolverRun")

  * **Results:** [Purge](/FEM_ResultsPurge "FEM ResultsPurge"), [Show](/FEM_ResultShow "FEM ResultShow"); **Postprocessing:** [Apply changes](/FEM_PostApplyChanges "FEM PostApplyChanges"), [Pipeline from result](/FEM_PostPipelineFromResult "FEM PostPipelineFromResult"), [Warp filter](/FEM_PostFilterWarp "FEM PostFilterWarp"), [Scalar clip filter](/FEM_PostFilterClipScalar "FEM PostFilterClipScalar"), [Function cut filter](/FEM_PostFilterCutFunction "FEM PostFilterCutFunction"), [Region clip filter](/FEM_PostFilterClipRegion "FEM PostFilterClipRegion"), [Contours filter](/FEM_PostFilterContours "FEM PostFilterContours"), [Line clip filter](/FEM_PostFilterDataAlongLine "FEM PostFilterDataAlongLine"), [Stress linearization plot](/FEM_PostFilterLinearizedStresses "FEM PostFilterLinearizedStresses"), [Data at point clip filter](/FEM_PostFilterDataAtPoint "FEM PostFilterDataAtPoint"), [Filter function plane](/FEM_PostCreateFunctionPlane "FEM PostCreateFunctionPlane"), [Filter function sphere](/FEM_PostCreateFunctionSphere "FEM PostCreateFunctionSphere"), [Filter function cylinder](/FEM_PostCreateFunctionCylinder "FEM PostCreateFunctionCylinder"), [Filter function box](/FEM_PostCreateFunctionBox "FEM PostCreateFunctionBox")

  * **Utilities:** [Clipping plane](/FEM_ClippingPlaneAdd "FEM ClippingPlaneAdd"), [Remove clipping planes](/FEM_ClippingPlaneRemoveAll "FEM ClippingPlaneRemoveAll"), [Open FEM examples](/FEM_Examples "FEM Examples"); [Mesh clear](/FEM_MeshClear "FEM MeshClear"), [Mesh display info](/FEM_MeshDisplayInfo "FEM MeshDisplayInfo")

* * *

  * **Additional:** [Preferences](/FEM_Preferences "FEM Preferences"); [FEM Install](/FEM_Install "FEM Install"), [FEM Mesh](/FEM_Mesh "FEM Mesh"), [FEM Solver](/FEM_Solver "FEM Solver"), [FEM CalculiX](/FEM_CalculiX "FEM CalculiX"), [FEM Concrete](/FEM_Concrete "FEM Concrete"); [FEM Element Types](/FEM_Element_Types "FEM Element Types")

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), FEM, [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

