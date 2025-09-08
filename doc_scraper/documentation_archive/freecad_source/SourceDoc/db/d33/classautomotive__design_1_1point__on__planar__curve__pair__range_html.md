---
url: https://freecad.github.io/SourceDoc/db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html
scraped_at: 2025-09-08T15:09:49.191348
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [point_on_planar_curve_pair_range](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html)

[List of all members](../../d5/d47/classautomotive__design_1_1point__on__planar__curve__pair__range-members.html) | Public Member Functions | Public Attributes

automotive_design.point_on_planar_curve_pair_range Class Reference

##  Public Member Functions  
  
---  
def | [lower_limit_pitch](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a9350b357a9d4d34e36da09f68b8aefb4) ()  
def | [lower_limit_roll](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#aa0caa32b59154a4c11b9043380dda5ff) ()  
def | [lower_limit_yaw](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#af8807552455d33091a4b43da33aa1df0) ()  
def | [range_on_pair_curve](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#adee52f5f9adfc49a7ffbb4ac0a0c33cc) ()  
def | [simple_pair_range_applies_to_pair](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a458051625516c1ed5c04da32bc48c57a) ()  
def | [upper_limit_pitch](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a736e81f82be0d2c7f88967d9f84d64e7) ()  
def | [upper_limit_roll](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a93c50cc3803e78b4993992f39336f993) ()  
def | [upper_limit_yaw](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a8fbda925d80b23e6c7c7b2e9829a90b3) ()  
def | [wr1](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#ad231174c4247442a30d150f2333c89f2) (self)  
def | [wr2](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a2dfbbb96845c420d91736dbc1b8b16a4) (self)  
def | [wr3](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a49899c46ed031e1bb67e6c6933b328d4) (self)  
def | [wr4](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3571d64eca0881b5a3afe44aa75f80a8) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
def | [applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a34d466ba4abfc972eddb7542a66e3865) ()  
  
##  Public Attributes  
  
---  
|
[lower_limit_pitch](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a921ac00bdf5329d5b5efcfa4a38203e6)  
|
[lower_limit_roll](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3edca02a95a75a5fc6605d981fc52062)  
|
[lower_limit_yaw](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a5675a7214548a6991adfff51f3f92c0e)  
|
[pair_curve](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a15852a8665246c9106d97e892dd84670)  
|
[range_on_pair_curve](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a364598cf94ad47708e58023f0f37441e)  
|
[simple_pair_range_applies_to_pair](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a18a368342f39eca14b7b036152dc7537)  
|
[upper_limit_pitch](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#aeca464a4094557abd8346079885654f0)  
|
[upper_limit_roll](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#aa11799c3ee0c422edeaedc916db4ef60)  
|
[upper_limit_yaw](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a5cc3f45d9a2ef481e2bcf020f27fac34)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
|
[applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a482e1ee88d0745baefe27406e3b45d03)  
  
## Detailed Description

    
    
    Entity point_on_planar_curve_pair_range definition.
    
        :param simple_pair_range_applies_to_pair
        :type simple_pair_range_applies_to_pair:point_on_planar_curve_pair
    
        :param range_on_pair_curve
        :type range_on_pair_curve:trimmed_curve
    
        :param lower_limit_yaw
        :type lower_limit_yaw:rotational_range_measure
    
        :param upper_limit_yaw
        :type upper_limit_yaw:rotational_range_measure
    
        :param lower_limit_pitch
        :type lower_limit_pitch:rotational_range_measure
    
        :param upper_limit_pitch
        :type upper_limit_pitch:rotational_range_measure
    
        :param lower_limit_roll
        :type lower_limit_roll:rotational_range_measure
    
        :param upper_limit_roll
        :type upper_limit_roll:rotational_range_measure

## Member Function Documentation

## ◆ lower_limit_pitch()

def automotive_design.point_on_planar_curve_pair_range.lower_limit_pitch  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._lower_limit_pitch,
automotive_design.spherical_pair_range._lower_limit_pitch,
automotive_design.point_on_surface_pair_range._lower_limit_pitch, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.spherical_pair_range.wr2()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#adef113e2cdb21b624349bef0871475c2),
[automotive_design.point_on_planar_curve_pair_range.wr3()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a49899c46ed031e1bb67e6c6933b328d4),
and
[automotive_design.point_on_surface_pair_range.wr3()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a50c1f1fe7e18a0879548fd66cdd437ee).

## ◆ lower_limit_roll()

def automotive_design.point_on_planar_curve_pair_range.lower_limit_roll  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._lower_limit_roll,
automotive_design.spherical_pair_range._lower_limit_roll,
automotive_design.point_on_surface_pair_range._lower_limit_roll, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.spherical_pair_range.wr3()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a95990a41d08a3acaf1a9696e83240438),
[automotive_design.point_on_planar_curve_pair_range.wr4()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3571d64eca0881b5a3afe44aa75f80a8),
and
[automotive_design.point_on_surface_pair_range.wr4()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a29f7e495cea61760ad1a4b6cf2651a8e).

## ◆ lower_limit_yaw()

def automotive_design.point_on_planar_curve_pair_range.lower_limit_yaw  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._lower_limit_yaw,
automotive_design.spherical_pair_range._lower_limit_yaw,
automotive_design.point_on_surface_pair_range._lower_limit_yaw, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.spherical_pair_range.wr1()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a0f44c40add01c6f470aad51fa557c46c),
[automotive_design.point_on_planar_curve_pair_range.wr2()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a2dfbbb96845c420d91736dbc1b8b16a4),
and
[automotive_design.point_on_surface_pair_range.wr2()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a70d032b3c2250f02a530292b6b4b3939).

## ◆ range_on_pair_curve()

def automotive_design.point_on_planar_curve_pair_range.range_on_pair_curve  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._range_on_pair_curve.

## ◆ simple_pair_range_applies_to_pair()

def automotive_design.point_on_planar_curve_pair_range.simple_pair_range_applies_to_pair  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.planar_curve_pair_range._simple_pair_range_applies_to_pair,
automotive_design.point_on_planar_curve_pair_range._simple_pair_range_applies_to_pair,
automotive_design.planar_pair_range._simple_pair_range_applies_to_pair,
automotive_design.cylindrical_pair_range._simple_pair_range_applies_to_pair,
automotive_design.universal_pair_range._simple_pair_range_applies_to_pair,
automotive_design.spherical_pair_range._simple_pair_range_applies_to_pair,
automotive_design.gear_pair_range._simple_pair_range_applies_to_pair,
automotive_design.screw_pair_range._simple_pair_range_applies_to_pair,
automotive_design.surface_pair_range._simple_pair_range_applies_to_pair,
automotive_design.rack_and_pinion_pair_range._simple_pair_range_applies_to_pair,
automotive_design.point_on_surface_pair_range._simple_pair_range_applies_to_pair,
automotive_design.prismatic_pair_range._simple_pair_range_applies_to_pair, and
automotive_design.revolute_pair_range._simple_pair_range_applies_to_pair.

## ◆ upper_limit_pitch()

def automotive_design.point_on_planar_curve_pair_range.upper_limit_pitch  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._upper_limit_pitch,
automotive_design.spherical_pair_range._upper_limit_pitch,
automotive_design.point_on_surface_pair_range._upper_limit_pitch, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.spherical_pair_range.wr2()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#adef113e2cdb21b624349bef0871475c2),
[automotive_design.point_on_planar_curve_pair_range.wr3()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a49899c46ed031e1bb67e6c6933b328d4),
and
[automotive_design.point_on_surface_pair_range.wr3()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a50c1f1fe7e18a0879548fd66cdd437ee).

## ◆ upper_limit_roll()

def automotive_design.point_on_planar_curve_pair_range.upper_limit_roll  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._upper_limit_roll,
automotive_design.spherical_pair_range._upper_limit_roll,
automotive_design.point_on_surface_pair_range._upper_limit_roll, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.spherical_pair_range.wr3()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a95990a41d08a3acaf1a9696e83240438),
[automotive_design.point_on_planar_curve_pair_range.wr4()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3571d64eca0881b5a3afe44aa75f80a8),
and
[automotive_design.point_on_surface_pair_range.wr4()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a29f7e495cea61760ad1a4b6cf2651a8e).

## ◆ upper_limit_yaw()

def automotive_design.point_on_planar_curve_pair_range.upper_limit_yaw  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_planar_curve_pair_range._upper_limit_yaw,
automotive_design.spherical_pair_range._upper_limit_yaw,
automotive_design.point_on_surface_pair_range._upper_limit_yaw, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.spherical_pair_range.wr1()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a0f44c40add01c6f470aad51fa557c46c),
[automotive_design.point_on_planar_curve_pair_range.wr2()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a2dfbbb96845c420d91736dbc1b8b16a4),
and
[automotive_design.point_on_surface_pair_range.wr2()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a70d032b3c2250f02a530292b6b4b3939).

## ◆ wr1()

def automotive_design.point_on_planar_curve_pair_range.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ wr2()

def automotive_design.point_on_planar_curve_pair_range.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.point_on_planar_curve_pair_range.lower_limit_yaw](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a5675a7214548a6991adfff51f3f92c0e),
[automotive_design.spherical_pair_range.lower_limit_yaw](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a8057e47c62aa43a2560c033cfe5e10f1),
[automotive_design.point_on_surface_pair_range.lower_limit_yaw](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a4d8f42113c17152252a61deeab7b40be),
[automotive_design.point_on_planar_curve_pair_range.upper_limit_yaw](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a5cc3f45d9a2ef481e2bcf020f27fac34),
[automotive_design.spherical_pair_range.upper_limit_yaw](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a638110a90065638aee44c517e21f3c0f),
and
[automotive_design.point_on_surface_pair_range.upper_limit_yaw](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a4eff54472d31c8c3c74983ec4efa7b8d).

## ◆ wr3()

def automotive_design.point_on_planar_curve_pair_range.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.point_on_planar_curve_pair_range.lower_limit_pitch](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a921ac00bdf5329d5b5efcfa4a38203e6),
[automotive_design.spherical_pair_range.lower_limit_pitch](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#aae4b4c13f0fb0005187a56e330f9dd57),
[automotive_design.point_on_surface_pair_range.lower_limit_pitch](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a64db57f1d95ebd04105a414d06d27b98),
[automotive_design.point_on_planar_curve_pair_range.upper_limit_pitch](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#aeca464a4094557abd8346079885654f0),
[automotive_design.spherical_pair_range.upper_limit_pitch](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#accfd262c7b3442c4827ffde5c54d26d3),
and
[automotive_design.point_on_surface_pair_range.upper_limit_pitch](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a1728bff4be35a6fe988da559e6c0326b).

## ◆ wr4()

def automotive_design.point_on_planar_curve_pair_range.wr4  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.point_on_planar_curve_pair_range.lower_limit_roll](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3edca02a95a75a5fc6605d981fc52062),
[automotive_design.spherical_pair_range.lower_limit_roll](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a77616ddc9c2c5e6245aaba596fbe417f),
[automotive_design.point_on_surface_pair_range.lower_limit_roll](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a0b352c2ba3347eb025047b84b24570af),
[automotive_design.point_on_planar_curve_pair_range.upper_limit_roll](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#aa11799c3ee0c422edeaedc916db4ef60),
[automotive_design.spherical_pair_range.upper_limit_roll](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#ad049e7be3f307627cd39110aa43541bb),
and
[automotive_design.point_on_surface_pair_range.upper_limit_roll](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#aec25fb35303ccb6be5a6ba071bc92c1b).

## Member Data Documentation

## ◆ lower_limit_pitch

automotive_design.point_on_planar_curve_pair_range.lower_limit_pitch  
---  
  
Referenced by
[automotive_design.spherical_pair_range.wr2()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#adef113e2cdb21b624349bef0871475c2),
[automotive_design.point_on_planar_curve_pair_range.wr3()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a49899c46ed031e1bb67e6c6933b328d4),
and
[automotive_design.point_on_surface_pair_range.wr3()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a50c1f1fe7e18a0879548fd66cdd437ee).

## ◆ lower_limit_roll

automotive_design.point_on_planar_curve_pair_range.lower_limit_roll  
---  
  
Referenced by
[automotive_design.spherical_pair_range.wr3()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a95990a41d08a3acaf1a9696e83240438),
[automotive_design.point_on_planar_curve_pair_range.wr4()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3571d64eca0881b5a3afe44aa75f80a8),
and
[automotive_design.point_on_surface_pair_range.wr4()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a29f7e495cea61760ad1a4b6cf2651a8e).

## ◆ lower_limit_yaw

automotive_design.point_on_planar_curve_pair_range.lower_limit_yaw  
---  
  
Referenced by
[automotive_design.spherical_pair_range.wr1()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a0f44c40add01c6f470aad51fa557c46c),
[automotive_design.point_on_planar_curve_pair_range.wr2()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a2dfbbb96845c420d91736dbc1b8b16a4),
and
[automotive_design.point_on_surface_pair_range.wr2()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a70d032b3c2250f02a530292b6b4b3939).

## ◆ pair_curve

automotive_design.point_on_planar_curve_pair_range.pair_curve  
---  
  
Referenced by
[automotive_design.point_on_planar_curve_pair.wr1()](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#acaf537b23b8ca4d04b0a3b8df4656a07).

## ◆ range_on_pair_curve

automotive_design.point_on_planar_curve_pair_range.range_on_pair_curve  
---  
  
## ◆ simple_pair_range_applies_to_pair

automotive_design.point_on_planar_curve_pair_range.simple_pair_range_applies_to_pair  
---  
  
## ◆ upper_limit_pitch

automotive_design.point_on_planar_curve_pair_range.upper_limit_pitch  
---  
  
Referenced by
[automotive_design.spherical_pair_range.wr2()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#adef113e2cdb21b624349bef0871475c2),
[automotive_design.point_on_planar_curve_pair_range.wr3()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a49899c46ed031e1bb67e6c6933b328d4),
and
[automotive_design.point_on_surface_pair_range.wr3()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a50c1f1fe7e18a0879548fd66cdd437ee).

## ◆ upper_limit_roll

automotive_design.point_on_planar_curve_pair_range.upper_limit_roll  
---  
  
Referenced by
[automotive_design.spherical_pair_range.wr3()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a95990a41d08a3acaf1a9696e83240438),
[automotive_design.point_on_planar_curve_pair_range.wr4()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a3571d64eca0881b5a3afe44aa75f80a8),
and
[automotive_design.point_on_surface_pair_range.wr4()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a29f7e495cea61760ad1a4b6cf2651a8e).

## ◆ upper_limit_yaw

automotive_design.point_on_planar_curve_pair_range.upper_limit_yaw  
---  
  
Referenced by
[automotive_design.spherical_pair_range.wr1()](../../db/d1a/classautomotive__design_1_1spherical__pair__range.html#a0f44c40add01c6f470aad51fa557c46c),
[automotive_design.point_on_planar_curve_pair_range.wr2()](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a2dfbbb96845c420d91736dbc1b8b16a4),
and
[automotive_design.point_on_surface_pair_range.wr2()](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a70d032b3c2250f02a530292b6b4b3939).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

