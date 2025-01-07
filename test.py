
# # Simpson's 1/3 rule
# # Define function to integrates
# def f(x):
#     return 1/(1+x**2)

# # Implement Simpson's 1/3 rule
# def Simpson13(X0,Xn,n):
#     # Calculating step size
#     h=(Xn - X0) / n
    
#     # Finding sum
#     integration = f(X0) + f(Xn)
    
#     for i in range(1,n):
#         k = X0 + (i*h)
        
#         if i % 2 == 0:
#             integration = integration + (2 *f(k))
#         else :
#             integration = integration + (4*f(k))
       
#     integration = integration * h/3
    
#     return integration

# #Lower_limit = float(input("Enter the lower limit of integration: "))            
# Upper_limit = (len(df['x1']))/2
# #Sub_interval =int(input("Enter the number of intervals: "))

# Result = Simpson13(1, Upper_limit, 1)
# print("Intergration result by Simpson 1/3 method is : %0.6f" %(Result));          
 

import pandas as pd

# Read the non-NaN values from the y2_difference_sheet.xlsx file
df = pd.read_excel("C:\\Users\\shrey\\Documents\\CODE\\CODE\\assets\\xlsx\\y2_difference_sheet.xlsx")

# Get the y2_difference values as a NumPy array
x2_difference_values = df['x2_difference'].values

# Apply Simpson's 1/3 rule
n = len(x2_difference_values)
h = 1  # Assuming unit spacing between points, change if necessary

integral = x2_difference_values[0] + x2_difference_values[-1]

for i in range(1, n-1):
    if i % 2 == 0:
        integral += 2 * x2_difference_values[i]
    else:
        integral += 4 * x2_difference_values[i]

integral *= h / 3

c_integral=(integral)/141

print(f"The integral calculated using Simpson's 1/3 rule is: {c_integral}")
