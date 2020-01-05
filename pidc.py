#
# last update
#

import matplotlib.pyplot as plt

class pid_control():

	def __init__(self):

		self.kp = 1.0
		self.ki = 1.0
		self.kd = 1.0
		self.t = 1.0
		self.total_e = 0.0
		self.last_e = self.t
		self.u = self.t

	def set(self, p, i, d):
		self.kp = p
		self.ki = i
		self.kd = d

	def reset(self):
		self.total_e = 0.0
		self.last_e = self.t

	def run(self, n):

		e = self.t - n
		self.total_e += e
		self.u = self.kp*e + self.ki*self.total_e + self.kd*(e - self.last_e)
		self.last_e = e

		return self.u

def test(p, i, d):

	pid.kp = p
	pid.ki = i
	pid.kd = d
	pid.t = 100
	pid.reset()

	us = [1.0]
	u = 1.0

	for i in range(100):
		u = pid.run(u)
		us.append(u)

	return us

'''

pid = pid_control()
# 0.1 0.4 0.1
us_0 = test(0.01, 0.4, 0.1)
print(us_0)
us_1 = test(0.1, 0.4, 0.1)
print(us_1)
us_2 = test(0.4, 0.4, 0.1)
print(us_2)

xs = [x for x in range(101)]

plt.title("f 1 t 100")
plt.plot(xs, [100 for i in range(101)], color='Purple', label='target')
plt.plot(xs, us_0, color='Red'  , label='pid 0.01, 0.4, 0.1')
plt.plot(xs, us_1, color='Green', label='pid 0.1, 0.4, 0.1')
plt.plot(xs, us_2, color='Blue' , label='pid 0.4, 0.4, 0.1')
plt.legend()
plt.show()

'''
