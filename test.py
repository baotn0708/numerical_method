from scipy.special import gamma
import numpy as np
# Điểm cần tính giá trị hàm gamma
x = 1.05

# Tính giá trị hàm gamma tại x
gamma_value = gamma(x)

print(f"Gamma({x}) =", gamma_value)
t = np.linspace(1,2,int((2-1)/0.05)+1)

y = gamma(t)

t_sample = np.linspace(t[0],t[-1],5)
y_sample = gamma(t_sample)

