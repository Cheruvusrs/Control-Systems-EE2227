#Code by C.Sri Ram Saran
#April 7th,2020
#Released under GNU GPL
import numpy as np
import math
import matplotlib.pyplot as plt
omega=np.linspace(-1000,1000,2000)# our desired range of omega values
from scipy import signal
zeros=[]#a this list contains zeros of G(s)
poles=[0]#a this list contains poles of G(s)
H_s=signal.ZerosPolesGain(zeros,poles,1) # feed zeros and poles as inputs to this function to get H_s which is a transfer function with GAIN=1
w,H=signal.freqresp(H_s,w=omega)#feed H_s and omega values as inputs to this funtion it will return frequency response H of H_s and w the range of omega values of H
s=1j*w#make s=jw substitution
GAIN=(np.pi*np.exp(-0.25*s))#enter the GAIN function which could be either constant or variable


H=H*GAIN#we multiply GAIN function with H(jw) to get our  desired final transfer functions frequency response
#finally H is the frequency response of our desired Transfer Function

	

plt.plot(H.real,H.imag) #plotting the nyquist plot of H(s) by taking Re{H} as x-axis parameter and Im{H} as y-axis parameter
plt.grid()

plt.xlim(-2,2)#limiting x-axis values
plt.xlabel("real axis")
plt.ylim(-2,2)#limiting y-axis values
plt.ylabel("imaginary axis")
plt.title("NYQUIST PLOT")
plt.show()
