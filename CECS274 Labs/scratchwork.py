import matplotlib.pyplot as plt

V_gs = [0, 1.3, 1.4, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.3]

I_d = [0, 0, 0.0006, 0.003, 0.0053, 0.011, 0.023, 0.048, 0.105, 0.25, 0.45, 1.054, 1.96, 3.85, 7.55, 14.18, 15.03, 15.05, 15.07]
x = plt.figure()
plt.plot(V_gs , I_d)
plt.ylabel('Drain Current (mA)')
plt.xlabel('Gate Source Voltage (V)')
plt.show()