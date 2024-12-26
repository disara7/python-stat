import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

hours_studied=np.array([2,3,5,7,8,10])
exam_scores=np.array([60,70,80,85,90,95])
m,c=np.polyfit(hours_studied,exam_scores,1)
predicted_scores=m*hours_studied+c

print("Slope(m):",m)
print("Intercept(c):",c)
print("predicted_scores:", predicted_scores)