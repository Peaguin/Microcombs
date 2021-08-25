# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:50:28 2021

@author: Confotec
"""
import cwave
import time

cw = cwave.CWave()
cw.connect('192.168.202.41')

cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, 0)
cw.set_piezo_mode(cwave.PiezoChannel.Opo, cwave.PiezoMode.Manual)

for value in range(0, 15000, 100):
    cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, value)
    print('Manual Output Value: {} / {}%'.format(value, int(value/65535*100)))
    time.sleep(1)

for value in range(0, 15000, 100):
    cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, value)
    print('Manual Output Value: {} / {}%'.format(value, int(value/65535*100)))
#cw.set_etalon_offset(9000)
#print(cw.get_etalon_offset())
#time.sleep(5)
#cw.set_etalon_offset(11000)
#print(cw.get_etalon_offset())
# configure settings (100ms Period, Triangle, 20% to 70%):

# use signal generator on opo
#w.set_piezo_mode(cwave.PiezoChannel.Opo, cwave.PiezoMode.ExtRamp)
#for value in range(0, 65536, 5000):
#    cw.set_etalon_offset(value)
#    time.sleep(10)
#    print(cw.get_etalon_offset())
