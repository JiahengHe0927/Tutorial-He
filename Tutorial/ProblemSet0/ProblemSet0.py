# Comments

# Question 1 6+4*10
# Answer 1:46
#
# Correct.

# Question 2: (6+4)*10
# Answer 2:100
#
# Correct.

#Question 3:23.0 to the 5th power
#Answer 3:1.8721712305548575
#
# Wrong. The correct answer is 6436343.0
# Misunderstand the question. The question ask for the 5th power, not the 5th root.
# The operation should be 23.0**5, not 23.0**(1/5).

#Question 4:Positive root of the following equation: a. 34*x^2 + 68*x - 510 
#Answer 4:3.0
#
# Wrong. You should give the code for the answer, not just the answer. The correct code has three versions:
# 1. Use the formal directly. 
# >>> (-68 + (68**2 - 4 * 34 * (-510))**0.5) / (2 * 34)
# 3.0
# >>> (-68 - (68**2 - 4 * 34 * (-510))**0.5) / (2 * 34) 
# -5.0
#
# 2. Use the variable to store the values of a, b, and c, then use the quadratic formula to find the positive root.
# >>> import math
# >>> a = 34
# >>> b = 68
# >>> c = -510
# >>> (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
# 3.0
# >>> (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
# -5.0
#
# 3. Use the numpy library to find the roots of the equation.
# >>> import numpy as np
# >>> np.roots([34, 68, -510])
# array([-5.,  3.])

#Question 5:.cos(3.4)**2+math.sin(3.4)**2 
#Answer 5:1.0
#
# Wrong. The correct answer is: syntax error. 
# First, the .cos(3,4) has a . at the first, which is the syntax error. Second, the math module should be imported first before using the math functions.
# Hence, the correct form should be:
# >>> import math
# >>> math.cos(3.4)**2 + math.sin(3.4)**2
# 1.0