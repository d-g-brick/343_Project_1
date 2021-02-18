# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:50:47 2021

@author: Declan Brick
"""
def ThetaCalc(g,M,Beta):
    """
    Calculates flow deflection angle using Equation 1 in the Project Description

    Parameters
    ----------
    g : Float
        Ratio of specific heats
    M : Float
        Free Stream Mach Number before Shock
    Beta : Float
        Oblique Shock Angle, in degrees 

    Returns
    -------
    Theta: Float
        Flow Deflection Angle, in degrees

    """
    