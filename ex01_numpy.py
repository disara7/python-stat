import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

hours_studied=np.array([2,3,4,5,6])
exam_scores=np.array([65,78,83,89,92])

slope,intercept=np.polyfit(hours_studied,exam_scores,1)
predicted_scores=slope*hours_studied+intercept

plt.scatter(hours_studied,exam_scores, label='Data')
plt.plot(hours_studied,predicted_scores,color='red',label='Best Fit Line')
plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.legend()
plt.show()