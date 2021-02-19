"""
Declan Brick
Matthew Bethea
2/17/21
MAE 343
Project 1
"""

#import here
import math


def Theta(g,M,Beta):
    
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
    
    #Just writing rhs of Equation 1
    Tan_Theta=2*(1/math.tan(math.radians(Beta)))*(M**2*(math.sin(math.radians(Beta)))**2-1)/(M**2*(g+math.cos(math.radians(2*Beta)))+2)
    
    #Now grabbing the actual angle
    Theta=math.degrees(math.atan(Tan_Theta))
    
    return Theta
    #this was verified using a Ti-84 to output the correct answer, but many want to change output decimal precision
