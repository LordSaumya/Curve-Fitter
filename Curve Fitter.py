#Curve Fitter by Saumya Shah
#11th December 2020

#Imports:
import numpy as np
import math as maths
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from sympy import *

#Functions:
    #Derivative:
def deriv(func):
    x = symbols("x")
    return(str(diff(func)).replace("exp","e^").replace("**5","\u2075").replace("**4","\u2074").replace("**3","\u00b3").replace("**2","\u00b2").replace("*",""))
    #Tests:
def test1(x, a, b, c, d): 
    return a * np.sin(b * x + c) + d
def test2(x, m, c): 
    return m * x + c
def test3(x,a,b,c):
    return a*x**2 + b*x + c
def test4(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
def test5(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e
def test6(x,a,b,c,d,e,f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
def test7(x,a,b,c,d):
    return a*maths.e**(b * x + c) + d
    #Graph
def graph(type,param):
    plt.scatter(x, y, color ='red', label ="data")
    newX = (np.linspace(max(x),min(x),500)).tolist()
    newY = []
    if (type == 1):
        for n in newX:
            newY.append(param[0] * np.sin(param[1] * n + param[2]) + param[3])
        optimFunc = ("%fsin(%fx + %f) + %f)"%(tuple(float(round(num, 3)) for num in param)))
    elif (type == 2):
        for n in newX:
            newY.append(param[0] * n + param[1])
            optimFunc = ("%fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    elif (type == 3):
        for n in newX:
            newY.append(param[0] * n**2 + param[1]*n + param[2])
        optimFunc = ("%fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    elif (type == 4):
        for n in newX:
            newY.append(param[0] * n**3 + param[1]*n**2 + param[2]*n + param[3])
        optimFunc = ("%fx\u00B3 + %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    elif (type == 5):
        for n in newX:
            newY.append(param[0] * n**4 + param[1]*n**3 + param[2]*n**2 + param[3]*n + param[4])
        optimFunc = ("%fx\u2074 + %fx\u00B3 + %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    elif (type == 6):
        for n in newX:
            newY.append(param[0] * n**5 + param[1]*n**4 + param[2]*n**3 + param[3]*n**2 + param[4]*n + param[5])
        optimFunc = ("%fx\u2075 + %fx\u2074 + %fx\u00B3 + %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    elif (type == 7):
        for n in newX:
            newY.append(param[0] * maths.exp(param[1] * n + param[2]) + param[3])
        optimFunc = ("%fe^(%fx + %f) + %f"%(tuple(float(round(num, 3)) for num in param)))
    plt.plot(newX,newY, '--', color ='blue', label ="optimised function (f(x) = %s)"%optimFunc)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)       
    plt.show()
def rvalue(type, param):
    predY = []
    if (type == 1):
        for n in x:
            predY.append(param[0] * np.sin(param[1] * n + param[2]) + param[3])
    elif (type == 2):
        for n in x:
            predY.append(param[0] * n + param[1])
    elif (type == 3):
        for n in x:
            predY.append(param[0] * n**2 + param[1]*n + param[2])
    elif (type == 4):
        for n in x:
            predY.append(param[0] * n**3 + param[1]*n**2 + param[2]*n + param[3])
    elif (type == 5):
        for n in x:
            predY.append(param[0] * n**4 + param[1]*n**3 + param[2]*n**2 + param[3]*n + param[4])
    elif (type == 6):
        for n in x:
            predY.append(param[0] * n**5 + param[1]*n**4 + param[2]*n**3 + param[3]*n**2 + param[4]*n + param[5])
    elif (type == 7):
        for n in x:
            predY.append(param[0] * maths.exp(param[1] * n + param[2]) + param[3])
    sqdiff = []
    for i in range(len(y)):
        sqdiff.append(float((predY[i] - y[i]) ** 2))
    avgsqdiff = sum(sqdiff)/len(sqdiff)
    rmse = float(round(maths.sqrt(avgsqdiff),3))
    print("Root Mean Squared Error: " + str(rmse))
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    print("Coefficient of Determination: " + str(r_squared))
#Variables:
x = []
y = []
ask = True

#Code:
if(int(input("How would you like to enter your data? Please enter 1 or 2.\n[1] Enter x data and y data separately\n[2] Enter datapoints individually\nType: ")) == 2):
    print("\nPlease enter your datapoints in this format: \n\n x,y\n\n(x and y MUST be numbers)\nIf you want to stop entering datapoints, type \"S\"")
    while (ask):
        inp = input("\nPlease enter a datapoint: ").replace(" ","")
        if (inp == "S"):
            ask = False
            break
        else:
            inp = inp.split(",")
            x.append(float(inp[0]))
            y.append(float(inp[1]))
else:
    print("\nPlease enter all of your data in this format:\n\na,b,c,...\n\n")
    xin = (input("Please enter all of your x data: ")).replace(" ","").split(",")
    for a in xin:
        x.append(float(a))
    yin = (input("\nPlease enter all of your y data: ")).replace(" ","").split(",")
    for b in yin:
        y.append(float(b))
func = int(input("\nWhich function would you like to fit to your data? Please enter a number between 1 and 7:\n[1] Sine wave\n[2] Linear function\n[3] Quadratic function\n[4] Cubic function\n[5] Quartic function\n[6] Quintic function\n[7] Exponential function\nType: ").replace(" ","")[0])
    #Sine Function
if (func == 1):
    ff = np.fft.fftfreq(len(np.array(x)), (np.array(x)[1]-np.array(x)[0]))
    Fyy = abs(np.fft.fft(y))
    p0=[np.std(y) * 2.**0.5,abs(ff[np.argmax(Fyy[1:])+1]),0,np.mean(y)]
    param, param_cov = curve_fit(test1, x, y,p0=p0, maxfev=10000)
    param = param.tolist()
    print("\n\nSine Function:\n")
    print("Function: %fsin(%fx + %f) + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*sin(%f*x+%f)+%f"%(tuple(round(num, 3) for num in param)))))
    #Linear Function
elif (func == 2):
    param, param_cov = curve_fit(test2, x, y, maxfev=10000)
    param = param.tolist()
    print("\n\nLinear Function:\n")
    print("Function: %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*x+%f"%(tuple(round(num, 3) for num in param)))))
    #Quadratic Function
elif (func == 3):
    param, param_cov = curve_fit(test3, x, y, maxfev=10000)
    param = param.tolist()
    print("\n\nQuadratic Function:\n")
    print("Function: %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*x**2+%f*x+%f"%(tuple(round(num, 3) for num in param)))))
    #Cubic Function
elif (func == 4):
    param, param_cov = curve_fit(test4, x, y, maxfev=10000)
    param = param.tolist()
    print("\n\nCubic Function:\n")
    print("Function: %fx\u00B3 + %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
    #Quartic Function
elif (func == 5):
    param, param_cov = curve_fit(test5, x, y, maxfev=10000)
    param = param.tolist()
    print("\n\nQuartic Function:\n")
    print("Function: %fx\u2074 + %fx\u00B3 + %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*x**4 + %f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
    #Quintic Function
elif (func == 6):
    param, param_cov = curve_fit(test6, x, y, maxfev=10000)
    param = param.tolist()
    print("\n\nQuintic Function:\n")
    print("Function: %fx\u2075 + %fx\u2074 + %fx\u00B3 + %fx\u00B2 + %fx + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*x**5 + %f*x**4 + %f*x**3 + %f*x**2 + %f*x + %f"%(tuple(round(num, 3) for num in param)))))
    #Exponential Function
elif (func == 7):
    param, param_cov = curve_fit(test7, x, y, maxfev=10000)
    param = param.tolist()
    print("\n\nExponential Function:\n")
    print("Function: %fe^(%fx + %f) + %f"%(tuple(float(round(num, 3)) for num in param)))
    print("Derivative: %s"%(deriv("%f*exp(%f*x + %f) + %f"%(tuple(round(num, 3) for num in param)))))
rvalue(func,param)
graph(func,param)
#Curve Fitter by Saumya Shah
#11th December 2020