*/## Observations
- Low Kp results in slow response
- Higher Kp reduces rise time but increases overshoot
- Very high Kp may cause oscillation/*


import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0
dt = 0.01
T = 10.0
steps = int(T/dt)

# PID gains
Kp = 2.0
Kd = 1.0
Ki = 0.0

# State
x = 0.0
v = 0.0
x_target = 10.0
integral = 0.0

# Logs
xs, vs, us, ts = [], [], [], []

for i in range(steps):
    t = i * dt
    error = x_target - x
    integral += error * dt

    u = Kp*error - Kd*v + Ki*integral
    a = u / m

    v += a * dt
    x += v * dt

    xs.append(x)
    vs.append(v)
    us.append(u)
    ts.append(t)

plt.plot(ts, xs, label="Position")
plt.axhline(x_target, linestyle="--", label="Target")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Position")
plt.savefig('plot.png') 

/* The plot is saved as 'plot.png' in the current directory. */

 
# Simulation parameters
m = 1.0
dt = 0.01
T = 10.0
steps = int(T / dt)

x_target = 10.0
Kd = 1.0
Ki = 0.0

Kp_list = [0.5, 2.0, 5.0]  # เปรียบเทียบหลายค่า
colors = ["blue", "green", "red"]

plt.figure()

for Kp, c in zip(Kp_list, colors):
    x = 0.0
    v = 0.0
    integral = 0.0

    xs = []
    ts = []

    for i in range(steps):
        t = i * dt
        error = x_target - x
        integral += error * dt

        u = Kp * error - Kd * v + Ki * integral
        a = u / m

        v += a * dt
        x += v * dt

        xs.append(x)
        ts.append(t)

    plt.plot(ts, xs, color=c, label=f"Kp = {Kp}")

plt.axhline(x_target, linestyle="--", color="black", label="Target")
plt.xlabel("Time [s]")
plt.ylabel("Position")
plt.title("Effect of Kp on Position Response")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('plot.png')
