# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:50:21 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy_indexed as npi

asam = {}
normalpH = {}
basa = {}

#variabel pH
x = 0.0
while x <= 9:
    x = round(x,1)
    
    #derajat keanggotaan asam
    if (x <= 5):
        asam.update({x:1})
    elif (5 < x and x <= 5.5):
        asam.update({x:round((x-5.5) / (5-5.5), 1)})
    else:
        asam.update({x:0})
    
    #derajat keanggotaan normal
    if (5 < x and x <= 5.5):
        normalpH.update({x:(x-5) / (5.5-5)})
    elif (5.5 < x and x <= 7.5):
        normalpH.update({x:1})
    elif (7.5 < x and x < 8):
        normalpH.update({x:round((x-8) / (7.5-8), 1)})
    else:
        normalpH.update({x:0})
        
    #derajat keanggotaan basa
    if (x <= 7.5):
        basa.update({x:0})
    elif (7.5 < x and x <= 8):
        basa.update({x:round((x-7.5) / (8-7.5), 1)})
    else:
        basa.update({x:1})
    
    x += 0.1
    
plt.plot(list(asam.keys()), list(asam.values()))
plt.plot(list(normalpH.keys()), list(normalpH.values()))
plt.plot(list(basa.keys()), list(basa.values()))
plt.title("Variabel Sensor pH")
plt.xlabel("Data pH")
plt.ylabel("Derajat Keanggotaan")
plt.legend(['asam', 'normal', 'basa'])
plt.show()

#=============================================================================

rendah = {}
normalUltra = {}
tinggi = {}

#variabel ultrasonik
x = 0.0
while x <= 40:
    x = round(x,1)
    
    #derajat keanggotaan rendah
    if (x <= 8):
        rendah.update({x:1})
    elif (8 < x and x <= 16):
        rendah.update({x:round((x-16) / (8-16), 1)})
    else:
        rendah.update({x:0})
    
    #derajat keanggotaan normal
    if (8 < x and x <= 16):
        normalUltra.update({x:round((x-8) / (16-8), 1)})
    elif (16 < x and x <= 24):
        normalUltra.update({x:1})
    elif (24 < x and x < 32):
        normalUltra.update({x:round((x-32) / (24-32), 1)})
    else:
        normalUltra.update({x:0})
        
    #derajat keanggotaan basa
    if (x <= 24):
        tinggi.update({x:0})
    elif (24 < x and x < 32):
        tinggi.update({x:(x-24) / (32-24)})
    else:
        tinggi.update({x:1})
    
    x += 0.1
    
plt.plot(list(rendah.keys()), list(rendah.values()))
plt.plot(list(normalUltra.keys()), list(normalUltra.values()))
plt.plot(list(tinggi.keys()), list(tinggi.values()))
plt.title("Variabel Sensor Ultrasonik")
plt.xlabel("Ketinggian Air (cm)")
plt.ylabel("Derajat Keanggotaan")
plt.legend(['rendah', 'normal', 'tinggi'])
plt.show()

#=============================================================================

sebentarpH = {}
lamapH = {}
offpH = {}

#variabel output pH (pH Up)
x = 0.0
while x <= 30:
    x = round(x,1)
    
    #derajat keanggotaan sebentar
    if (x <= 10):
        sebentarpH.update({x:1})
    elif (10 < x and x <= 20):
        sebentarpH.update({x:(x-20) / (10-20)})
    else:
        sebentarpH.update({x:0})
    
    #derajat keanggotaan lama
    if (x <= 10):
        lamapH.update({x:0})
    elif (10 < x and x < 20):
        lamapH.update({x:(x-10) / (20-10)})
    else:
        lamapH.update({x:1})
    
    offpH.update({x:0})
    x += 0.1
    
plt.plot(list(sebentarpH.keys()), list(sebentarpH.values()))
plt.plot(list(lamapH.keys()), list(lamapH.values()))
plt.plot(list(offpH.keys()), list(offpH.values()))
plt.title("Variabel Output pH")
plt.xlabel("Waktu pH Up (detik)")
plt.ylabel("Derajat Keanggotaan")
plt.legend(['sebentar', 'lama', 'off'])
plt.show()

#=============================================================================

sebentarUltra = {}
lamaUltra = {}
offUltra = {}

#variabel output ultrasonik (buang air)
x = 0.0
while x <= 200:
    x = round(x,1)
    
    #derajat keanggotaan sebentar
    if (x <= 66):
        sebentarUltra.update({x:1})
    elif (66 < x and x <= 132):
        sebentarUltra.update({x:(x-132) / (66-132)})
    else:
        sebentarUltra.update({x:0})
    
    #derajat keanggotaan lama
    if (x <= 66):
        lamaUltra.update({x:0})
    elif (66 < x and x < 132):
        lamaUltra.update({x:(x-66) / (132-66)})
    else:
        lamaUltra.update({x:1})
    
    offUltra.update({x:0})
    x += 0.1
    
plt.plot(list(sebentarUltra.keys()), list(sebentarUltra.values()))
plt.plot(list(lamaUltra.keys()), list(lamaUltra.values()))
plt.plot(list(offUltra.keys()), list(offUltra.values()))
plt.title("Variabel Output Ultrasonik")
plt.xlabel("Waktu Buang Air (detik)")
plt.ylabel("Derajat Keanggotaan")
plt.legend(['sebentar', 'lama', 'off'])
plt.show()

#================================ Perhitungan ================================

rule = np.array([
        [asam, rendah, sebentarpH, offUltra],
        [asam, normalUltra, sebentarpH, offUltra],
        [asam, tinggi, lamapH, lamaUltra],
        [normalpH, rendah, offpH, offUltra],
        [normalpH, normalUltra, offpH, offUltra],
        [normalpH, tinggi, offpH, sebentarUltra],
        [basa, rendah, offpH, offUltra],
        [basa, normalUltra, offpH, offUltra],
        [basa, tinggi, offpH, lamaUltra],
        [normalpH, tinggi, sebentarpH, sebentarUltra]])
outRule = np.array([
           ['sebentarpH', 'offUltra'],
           ['sebentarpH', 'offUltra'],
           ['lamapH', 'lamaUltra'],
           ['offpH', 'offUltra'],
           ['offpH', 'offUltra'],
           ['offpH', 'sebentarUltra'],
           ['offpH', 'offUltra'],
           ['offpH', 'offUltra'],
           ['offpH', 'lamaUltra'],
           ['sebentarpH', 'sebentarUltra']])
uji = [5.2, 25]

#derajat keanggotaan data uji
antecedent = []
for i in range(rule.shape[0]):
    temp = []
    temp.append(rule[i][0].get(uji[0]))
    temp.append(rule[i][1].get(uji[1]))
    antecedent.append(temp)
antecedent = np.array(antecedent)
print('\nDerajat Keanggotaan Data Uji\n', antecedent)

#output rule
print('\nOutput Rule\n', outRule)

#cari minimum dari setiap antecedent
minAnt = np.min(antecedent, axis=1)
print('\nMin Antecedent\n', minAnt)
#outAnt = np.vstack((minAnt, outRule[:, 0:1].flatten(), outRule[:, 1:2].flatten()))
#print('\nMin Antecedent + Output\n', outAnt)

#cari maksimum dari setiap output rule
outpH = np.array(['sebentarpH', 'sebentarpH', 'lamapH', 'offpH', 'offpH',
                  'offpH', 'offpH', 'offpH', 'offpH', 'sebentarpH'])
grouppH = npi.group_by(outpH).split(minAnt)
maxpH = []
for el in grouppH:
    maxpH.append(np.max(el))
maxpH = np.array(maxpH)
print('\nGroup by Max Out pH\n', np.unique(outpH), '\n', maxpH)

outUltra = np.array(['offUltra', 'offUltra', 'lamaUltra', 'offUltra', 'offUltra',
                  'sebentarUltra', 'offUltra', 'offUltra', 'lamaUltra', 'sebentarUltra'])
groupUltra = npi.group_by(outUltra).split(minAnt)
maxUltra = []
for el in groupUltra:
    maxUltra.append(np.max(el))
maxUltra = np.array(maxUltra)
print('\nGroup by Max Out Ultra\n', np.unique(outUltra), '\n', maxUltra)

#defuzzyfikasi
dtpH = []
#dtpH.append(list(lamapH.keys())[list(lamapH.values()).index(maxUltra[0])])
#print(lamapH)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    