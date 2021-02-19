"""
Declan Brick
Matthew Bethea
2/17/21
MAE 343
Project 1
"""

#import here
import math


def Mach(g,B,T):
    Mach = ((2*math.tan(T)+2*(1/(math.tan(B)))/(g*math.tan(T)+math.tan(T)*math.cos(2*B)-2*math.sin(B)*math.sin(B)*(1/(math.tan(B))))))
    return Mach 

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
    

def Beta(f,M,T,N):
    if f(M)*f(T) >= 0:
        return None
    Old_M = M
    Old_T = T
    for n in range(1, N+1):
        store = Old_M - f(Old_M)*(Old_T - Old_M)/(f(Old_T)-f(Old_M))
        solvestore = f(store)
        if f(Old_M)*solvestore <0:
            Old_M = Old_M
            Old_T = store
        elif f(Old_T)*solvestore <0:
            Old_M = store
            Old_T = Old_T
        elif solvestore == 0:
            print("solution found")
        else:
            print("failed")
            return None
    return Old_M - f(Old_M)*(Old_T - Old_M)/(f(Old_T) - f(Old(M)))



functionMatrix = {
  "square":square,
  "cube":cube,
  "inverse":inverse,
}

print("Available Functions:")
for function in functionMatrix.keys():
  print(function)

chosen = input("Which Function Would You Like to run?").lower()
value = float(input("X: "))
print("Output =",functionMatrix[chosen](value))


"""
Mn1=M*math.sin(math.radians(Beta))
Mn2=((Mn1**2+(2/(gamma-1)))/((2*gamma/(gamma-1)*Mn1**2)-1))**0.5
M2=Mn2/(math.sin(math.radians(Beta-Theta)))
Pressure_Ratio=1+(Mn1**2-1)*(2*gamma/(gamma+1))
Density_Ratio=((gamma+1)*Mn1**2)/((gamma-1)*Mn1**2+2)
Temperature_ratio=Pressure_Ratio/Density_Ratio
"""
