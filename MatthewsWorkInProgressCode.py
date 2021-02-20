"""
Declan Brick
Matthew Bethea
2/17/21
MAE 343
Project 1
"""

#import here
import math

def mach(gamma, Beta, Theta):
    
    B = math.radians(Beta)
    T = math.radians(Theta)
    g = gamma
    
    RMach = math.sqrt((-2*math.tan(T)-2*(1/(math.tan(B)))/(g*math.tan(T)+math.tan(T)*math.cos(2*B)-2*math.sin(B)*math.sin(B)*(1/(math.tan(B))))))
    
    return RMach


def theta(gamma, Mach, Beta):
    
    g = gamma
    M = Mach
    B = Beta
    
    """
    Calculates flow deflection angle using Equation 1 in the Project Description Parameters
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
    RTheta=math.degrees(math.atan(Tan_Theta))
    
    return RTheta
    #this was verified using a Ti-84 to output the correct answer, but many want to change output decimal precision


def beta(gamma, Mach, Theta):
    
    #using the functions for finding Beta max (the maximum shock angle) supported by the maximum Theta (the maximum flow deflection

    f = lambda B: (1/math.tan(2*(1/math.tan(math.radians(B)))*(((M**2)*(math.sin(math.radians(B))*math.sin(math.radians(B)))-1)/(((M**2)*(g+math.cos(2*math.radians(B))+2))))))-math.radians(Theta)
    
    g = gamma
    M = Mach
    
    RBeta = []
    
    BM = M_Beta(g,M)
    
    Theta_max = M_Theta(g, M, BM)
    
    Mach_angle = Mach_a(M)

        #Strong Root for Beta function
        #This root will be between 90 and the theta max
        #F = the function
        #sA = Theta max
        #sB = 90
        #iteration is set automatically to 100

    #setting bounds
    for c in range(1,2):
        if c == 1:
            Old_A = Theta_max
            Old_B = float(90)
            
        if c == 2:
            Old_A = Mach_angle
            Old_B = Theta_max
        
        #verifying
        if f(Old_A)*f(Old_B) >= 0:
            return None

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
                sBeta = Old_A - f(Old_A)*(Old_B - Old_A)/(f(Old_B) - f(Old(A)))
                print("Number of iteration to solution: ", n)
                print("solution found: ")
                RBeta.append(sBeta)
            else:
                
                print("failed")
                return None

    return RBeta



def M_Beta(g,M):
    
    f1 = 1+((g-1)/2)*(M**2)+((g+1)/16)*(M**4)
    f2 = math.sqrt((g+1)*f1)
    f3 = (((g+1)/4)*M**2+f2-1)
    f4 = math.sqrt((1/(g*(M**2)))*f3)
    BM = 1/math.sin(f4)
    
    return BM

def M_Theta(gamma, Mach, Beta):
    
    g = gamma
    M = math.radians(Mach)
    B = math.radians(Beta)
    
    top = (((M**2)*(math.sin(B-1)*math.sin(B-1)))*(1/math.tan(B)))
    bot = ((1/2)*(g+1)*(M**2)-(M**2)*(math.sin(B)*math.sin(B))+1)
    
    TM = 1/math.tan(top/bot)

    print("The maximum flow deflection is ")
    print(math.degrees(TM))
    
    return TM


def Mach_a(Mach):
    
    M = math.radians(Mach)
    
    mu = 1/(math.sin(1/M))
    
    return mu


#Main Code area

functionMatrix = {
  "Mach":mach,
  "Theta":theta,
  "Beta":beta,
}

lst = {
    "Mach":["gamma", "Beta", "Theta"],
       "Theta":["gamma", "Mach", "Beta"],
       "Beta":["gamma", "Mach", "theta"]
    }

ver = []

print("Available Functions:")
for function in functionMatrix.keys():
  print(function)

chosen = str(input("Which Function Would You Like to run?\n"))
print(chosen)

variableList = lst[chosen]
for var in variableList:
    ele = float(input(f"Please input {var}: "))
    ver.append(ele)

print(chosen, " = ", functionMatrix[chosen](*ver))



"""
Mn1=M*math.sin(math.radians(Beta))
Mn2=((Mn1**2+(2/(gamma-1)))/((2*gamma/(gamma-1)*Mn1**2)-1))**0.5
M2=Mn2/(math.sin(math.radians(Beta-Theta)))
Pressure_Ratio=1+(Mn1**2-1)*(2*gamma/(gamma+1))
Density_Ratio=((gamma+1)*Mn1**2)/((gamma-1)*Mn1**2+2)
Temperature_ratio=Pressure_Ratio/Density_Ratio
"""
