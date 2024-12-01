'''
https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15

Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.

Output Format

In the text box, using the language of your choice, print the floating point/decimal value required. Do not leave any leading or trailing spaces.

For example, if your answer is 0.255. In python you can print using

print("0.255")

This is NOT the actual answer - just the format in which you should provide your answer.
'''

import numpy as np
from scipy import stats
py=np.array([15 , 12 , 8 ,  8 ,  7 ,  7 ,  7 ,  6 ,  5 ,  3])
hs = np.array([10  ,25  ,17 , 11 , 13 , 17 , 20 , 13 , 9 ,  15])
print(py,hs,stats.pearsonr(py, hs).statistic)

## without the libraries

x=[15 , 12 , 8 ,  8 ,  7 ,  7 ,  7 ,  6 ,  5 ,  3]
y = [10  ,25  ,17 , 11 , 13 , 17 , 20 , 13 , 9 ,  15]
mX = sum(x)/len(x)
mY = sum(y)/len(y)
cov = sum((a - mX) * (b - mY) for (a,b) in zip(x,y)) / len(x)
stdevX = (sum((a - mX)**2 for a in x)/len(x))**0.5
stdevY = (sum((b - mY)**2 for b in y)/len(y))**0.5
r = round(cov/(stdevX*stdevY),3)
print(f"{r:.3f}")
