"""
Declan Brick
Matthew Bethea
2/17/21
MAE 343
Project 1
"""

#import here
import math


def mach(g,b,t):
    B = math.radians(b)
    T = math.radians(t)
    Mach = math.sqrt((2*math.tan(T)-2*(1/(math.tan(B)))/(g*math.tan(T)+math.tan(T)*math.cos(2*B)-2*math.sin(B)*math.sin(B)*(1/(math.tan(B))))))
    return Mach

def theta(g,M,B):
    
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
    Tan_Theta=2*(1/math.tan(math.radians(B)))*(M**2*(math.sin(math.radians(B)))**2-1)/(M**2*(g+math.cos(math.radians(2*B)))+2)
    
    #Now grabbing the actual angle
    Theta=math.degrees(math.atan(Tan_Theta))
    
    return Theta
    #this was verified using a Ti-84 to output the correct answer, but many want to change output decimal precision
    

def S_beta(M):

    #using the functions for finding Beta max (the maximum shock angle) supported by the maximum Theta (the maximum flow deflection
    Theta_max = M_Theta(M, (M_Beta(g,M)))

        #Strong Root for Beta function
        #This root will be between 90 and the theta max
        #F = the function
        #sA = Theta max
        #sB = 90
        #iteration is set automatically to 100

    #verifying
    if f(Ma)*f(Tm) >= 0:
        return None

    #setting bounds
    Old_A = Theta_max
    Old_B = float(90)

    #iterating to find the solution for beta
    for n in range(1, 100):
        
        new = Old_A - f(Old_A)*(Old_B - Old_A)/(f(Old_B)-f(Old_A))
        solvenew = f(new)
        
        if f(Old_A)*solvenew <0:
            
            Old_A = Old_A
            Old_B = new
            
        elif f(Old_A)*solvenew <0:
            
            Old_A = new
            Old_B = Old_B
            
        elif solvenew == 0:
            
            print("Number of iteration to solution: ", n)
            print("solution found: ")
            
        else:
            
            print("failed")
            return None

    return Old_A - f(Old_A)*(Old_B - Old_A)/(f(Old_B) - f(Old(A)))


def W_beta(f,Ma,Tm):

    #using the functions for finding Beta max (the maximum shock angle) supported by the maximum Theta (the maximum flow deflection
    Theta_max = M_Theta(M, (M_Beta(g,M)))

        #Strong Root for Beta function
        #This root will be between 90 and the theta max
        #F = the function
        #sA = Mach angle
        #sB = Theta max
        #iteration is set automatically to 100

    #verifying
    if f(Ma)*f(Tm) >= 0:
        return None

    #setting bounds
    Old_A = 
    Old_B = Theta_max

    #iterating to find the solution for beta
    for n in range(1, 100):
        
        new = Old_A - f(Old_A)*(Old_B - Old_A)/(f(Old_B)-f(Old_A))
        solvenew = f(new)
        
        if f(Old_A)*solvenew <0:
            
            Old_A = Old_A
            Old_B = new
            
        elif f(Old_A)*solvenew <0:
            
            Old_A = new
            Old_B = Old_B
            
        elif solvenew == 0:
            
            print("Number of iteration to solution: ", n)
            print("solution found: ")
            
        else:
            
            print("failed")
            return None

    return Old_A - f(Old_A)*(Old_B - Old_A)/(f(Old_B) - f(Old(A)))




def M_Beta(g,M):

    return results

def M_Theta(M,B):

    return results

def Mach_a():

    return results

functionMatrix = {
  "mach":mach,
  "theta":theta,
  "beta":beta,
}



print("Available Functions:")
for function in functionMatrix.keys():
  print(function)

chosen = input("Which Function Would You Like to run?").lower()
print(chosen)

g = float(input("Gamma: "))

if chosen in ["Mach","mach"]:
    b = float(input("Beta: "))
    t = float(input("Theta: "))
    print("Output =",functionMatrix[chosen](g,b,t))


"""
Mn1=M*math.sin(math.radians(Beta))
Mn2=((Mn1**2+(2/(gamma-1)))/((2*gamma/(gamma-1)*Mn1**2)-1))**0.5
M2=Mn2/(math.sin(math.radians(Beta-Theta)))
Pressure_Ratio=1+(Mn1**2-1)*(2*gamma/(gamma+1))
Density_Ratio=((gamma+1)*Mn1**2)/((gamma-1)*Mn1**2+2)
Temperature_ratio=Pressure_Ratio/Density_Ratio
"""
