# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:12:07 2018
@author: graham
Plotting the Fresnel coefecients and the reflection intensity
off of Silicon and a mirror
"""
import numpy as np
from numpy import pi, cos, arcsin, sin, arccos, tan
import matplotlib.pyplot as plt

#index of refraction of n1=air, n2=silicon at 1550nm
n_Air=1.0 
n_Si=3.4757 #Silicon at 1550 nm
n_Ag=0.14447+11.366j #Silver at 1550 nm

#incidence and transmittence angles. 
Theta_In=np.linspace(0,0.06*(pi/2),200)
Theta_In90=np.linspace(0,1*(pi/2),200)
#Theta_T=[arcsin((n1/n2)*sin(x)) for x in Theta_In]

deg=[(180./pi)*g for g in Theta_In]
deg90=[(180./pi)*g for g in Theta_In90]

alpha=[0,pi/4,pi/2]

def Fresnel(ThetaI,Alpha,N1,N2):
    SineT= np.sqrt(1-((N1/N2)*sin(ThetaI))**2) 
    Rs2=(N1*cos(ThetaI)-N2*SineT)/(N1*cos(ThetaI)+N2*SineT)
    Rp2=(N1*SineT-N2*cos(ThetaI))/(N1*SineT+N2*cos(ThetaI))
    A=-1.0*cos(Alpha)*Rp2
    B=sin(Alpha)*Rs2
    I=np.conj(A)*A+np.conj(B)*B
    if Alpha==pi/2:
        Ecc=arccos(B.real/sin(Alpha))
    else:
        Ecc=arccos(A.real/cos(Alpha))
    epsilon=tan(Ecc)
    return I,epsilon

Int_Ag=[]; Ep_Ag=[];Int_Ag90=[]; Ep_Ag90=[]
for q in alpha:
    I,E=Fresnel(Theta_In,q,n_Air,n_Ag)
    Int_Ag.append(I)
    Ep_Ag.append(E)
    I90,E90=Fresnel(Theta_In90,q,n_Air,n_Ag)
    Int_Ag90.append(I90)
    Ep_Ag90.append(E90)

Int_Si=[]; Ep_Si=[];Int_Si90=[]; Ep_Si90=[]
for q in alpha:
    I,E=Fresnel(Theta_In,q,n_Air,n_Si)
    Int_Si.append(I)
    Ep_Si.append(E)
    I90,E90=Fresnel(Theta_In90,q,n_Air,n_Si)
    Int_Si90.append(I90)
    Ep_Si90.append(E90)
    
                            #ploting the Silver Intesity
plt.figure(1)
p1,=plt.plot(deg,Int_Ag[0])
p2,=plt.plot(deg,Int_Ag[1])
p3,=plt.plot(deg,Int_Ag[2])
plt.title('Silver')
plt.ylabel('Normalized intensity [x$I_0$]',fontsize=12)
plt.xlabel('Incident angle [deg]',fontsize=12)
plt.legend((p1,p2,p3),('$p$-polarized','$45\\degree$ polarized','$s$-polarized'))
plt.grid(True)

ax12=plt.axes([0.24,0.18,0.25,0.25])
p11,=plt.plot(deg90,Int_Ag90[0])
p12,=plt.plot(deg90,Int_Ag90[1])
p13,=plt.plot(deg90,Int_Ag90[2])
plt.grid(True)

                            #ploting the Silicon Intensity
#plt.figure(2)
#p1,=plt.plot(deg,Int_Si[0])
#p2,=plt.plot(deg,Int_Si[1])
#p3,=plt.plot(deg,Int_Si[2])
#plt.title('Silicon')
#plt.ylabel('Normalized intensity [x$I_0$]',fontsize=12)
#plt.xlabel('Incident angle [deg]',fontsize=12)
#plt.legend((p1,p2,p3),('$p$-polarized','$45\\degree$ polarized','$s$-polarized'))
#plt.grid(True)
#
#ax22=plt.axes([0.21,0.17,0.25,0.25])
#p21,=plt.plot(deg90,Int_Si90[0])
#p22,=plt.plot(deg90,Int_Si90[1])
#p23,=plt.plot(deg90,Int_Si90[2])
#plt.grid(True)
#plt.tight_layout(True)
    
                            #ploting the silver Ellipticity
#plt.figure(3)
#ax21 =plt.subplot(231)
#ax21.plot(deg,Ep_Ag[0])
#plt.title('$p$-polarized')
#plt.ylabel('Ellipticity',fontsize=12)
#plt.grid(True)
#
#ax22= plt.subplot(232)
#ax22.plot(deg,Ep_Ag[1])
#plt.title('$45\\degree$ polarized')
#plt.grid(True)
#
#ax23 =plt.subplot(233)
#ax23.plot(deg,Ep_Ag[2])
#plt.title('$s$-polarized')
#plt.grid(True)
#
#ax24=plt.subplot(212)
#c0,=ax24.plot(deg90,Ep_Ag90[0])
#c1,=ax24.plot(deg90,Ep_Ag90[1])
#c2,=ax24.plot(deg90,Ep_Ag90[2])
#plt.ylabel('Ellipticity',fontsize=12)
#plt.xlabel('Incident angle [deg]',fontsize=12)
#plt.legend((c0,c1,c2),('$p$-polarized','$45\\degree$ polarized','$s$-polarized'))
#plt.grid(True)
#
#plt.tight_layout(True)

                            #ploting the Silicon Ellipticity
plt.figure(4)
ax41 =plt.subplot(231)
ax41.plot(deg,Ep_Si[0])
plt.title('$p$-polarized')
plt.ylabel('Ellipticity',fontsize=12)
plt.grid(True)

ax42= plt.subplot(232)
ax42.plot(deg,Ep_Si[1])
plt.title('$45\\degree$ polarized')
plt.grid(True)

ax43 =plt.subplot(233)
ax43.plot(deg,Ep_Si[2])
plt.title('$s$-polarized')
plt.grid(True)

ax44=plt.subplot(212)
c0,=ax44.plot(deg90,Ep_Si90[0])
c1,=ax44.plot(deg90,Ep_Si90[1])
c2,=ax44.plot(deg90,Ep_Si90[2])
plt.ylabel('Ellipticity',fontsize=12)
plt.xlabel('Incident angle [deg]',fontsize=12)
plt.legend((c0,c1,c2),('$p$-polarized','$45\\degree$ polarized','$s$-polarized'))
plt.grid(True)


plt.tight_layout(True)
plt.show()
