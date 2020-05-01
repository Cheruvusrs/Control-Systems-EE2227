# License
'''
Code by C.Sri Ram Saran
MAY 1st,2020
Released under GNU GPL
'''

import numpy as np
#if using termux
import subprocess
import shlex
#end if
R_C_1=9000.0
R_E_1=100.0
R_C_2=5000.0
R_F=640.0
R_E_2=100.0
R_C_3=600.0
h_f_e=100.0
r_o=10000000.0
I_C_1=0.0006
I_C_2=0.001
I_C_3=0.004
r_e_1=41.7
r_pi_2=2500.0
alpha1=0.99
g_m_2=0.04
r_e_3=6.25
r_o_3=25000.0
r_pi_3=625.0
g_m_3=160000.0
H=(R_E_2)*(R_E_1)/(R_E_2+R_F+R_E_1)# FEEDBACK GAIN
T_1=1/H# closed loop gain for large value of loop gain GH>>1
VOLTAGE_GAIN=-T_1*R_C_3
def r_parallel(a,b):# FUNCTION TO FIND PARALLEL RESISTANCE a||b
	
	return (a*b)/(a+b)

GAIN1=-alpha1*(r_parallel(R_C_1,r_pi_2))/(r_e_1+(r_parallel(R_E_1,(R_F+R_E_2))))#gain of first stage
GAIN2=-g_m_2*(r_parallel(R_C_2,(h_f_e+1)*(r_e_3+r_parallel(R_E_2,(R_F+R_E_1)))))#gain of second stage
GAIN3=1/(r_e_3+r_parallel(R_E_2,R_F+R_E_1))#gain of third stage
G=GAIN1*GAIN2*GAIN3# Forward gain
T=G/(1+G*H)#closed loop gain
VOLTAGE_GAIN=-T*R_C_3# voltage gain V_0/V_S
R_I=(h_f_e+1)*(r_e_1+r_parallel(R_E_1,R_F+R_E_2))#INPUT RESISTANCE OF G CIRCUIT
R_IN=R_I*(1+G*H)#INPUT RESISTANCE OF FEEDBACK AMPLIFIER
R_O=(r_parallel(R_E_2,R_E_1+R_F))+r_e_3+(R_C_2/(h_f_e+1))
R_OF=R_O*(1+G*H)# OUTPUT RESISTANCE OF FEEDBACK AMPLIFIER
R_OUT=(r_o_3+r_parallel(R_OF,r_pi_3+R_C_2)*(1+g_m_3*r_o_3*(r_pi_3/(r_pi_3+R_C_2))))/(1000000)# OUTPUT RESISTANCE OF CIRCUIT
print("forward path GAIN  (G):"+str(G)+"A/V")
print("feedback path GAIN  (H):"+str(H)+"ohm")
print("closed loop GAIN  (T):"+str(T)+"A/V")
print("VOLTAGE GAIN  (V_O/V_S):"+str(VOLTAGE_GAIN)+"V/V")
print("input resistance  (R_IN):"+str(R_IN)+"ohm")
print("output resistance  (R_OUT):"+str(R_OUT)+"ohm")
print("output resistance of feedback amplifier  (R_OF):"+str(R_OF)+"ohm")


