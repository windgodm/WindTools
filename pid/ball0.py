#
# last update
#

import matplotlib.pyplot as plt
from pidc import pid_control

class Mul(object):
	"""docstring for ClassName"""
	def __init__(self):

		# env
		self.g = 10.0
		self.wind_froce = 0.0
		self.mu = 0.01

		# ball
		self.m = 1.0
		self.gg = self.m*self.g # G=mg
		self.position = 0.0
		self.v = 0.0
		self.a = 0.0

	def run(self, dt=0.001):

		ff = self.mu*self.gg # f=mu*G

		if self.v == 0 and (abs(self.wind_froce) <= ff):
			# 静止且受力小于最大摩擦力
			fall = 0
		else:
			if self.v == 0:
				if self.wind_froce > 0:
					# 静止状态，摩擦力和受力方向相反
					ff = -ff
			elif self.v > 0:
				# 运动状态，摩擦力和速度方向相反
				ff = -ff

			fall = self.wind_froce + ff

		self.a = fall / self.m
		self.v += self.a*dt
		self.position += self.v*dt

		return self.position

	def wind(self, froce):

		self.wind_froce = froce

def test(p, i, d, epochs):

	# init env
	mul = Mul()

	# init pid
	pid = pid_control()
	pid.set(p, i, d)
	pid.t = 50.0
	pid.reset()

	# init data
	ps = [0.0]
	wfs = [0.0]

	# test
	p = 0.0
	for i in range(epochs):
		u = pid.run(p) # pid

		mul.wind(u) # env ctrl

		p = mul.run() # env update
		ps.append(p) # data

	return ps

epochs = 100000

'''
target = 10
test(0.02, 0.0000001, 15.5, epochs) 22.75s
test(0.03, 0.0000001, 85.5, epochs) 18.85s
test(0.04, 0.0000001, 141, epochs) 16.95s
'''
ps0 = test(0.02, 0.0000001, 15.5, epochs)
ps1 = test(0.03, 0.0000001, 85.5, epochs)
ps2 = test(0.04, 0.0000001, 141, epochs)

plt.plot([0, 100], [50.0, 50.0], color='purple')
plt.plot([x*0.001 for x in range(epochs+1)], ps0, color='g')
plt.plot([x*0.001 for x in range(epochs+1)], ps1, color='b')
plt.plot([x*0.001 for x in range(epochs+1)], ps2, color='r')
plt.show()
