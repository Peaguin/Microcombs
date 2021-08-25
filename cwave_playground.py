# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:50:28 2021

@author: Confotec
"""
import cwave
import time

cw = cwave.CWave()
cw.connect('192.168.202.41')

def writing(func, stop, step, *args):
    mylist = []
    for timing in range (0, stop, step):
        mylist.append(func(*args))
        time.sleep(step)
    return mylist
    
def data_logging(timeout, step= 1, d = 'opo', log = False, 
                 temp_setpoint = False, shutter_laser= False, 
                 shutter_laserOut = False, shutter_opoOut= False,
                 shutter_shg= False, shutter_shgOut= False, dial = False, laser= False,
                 galvo= False, etalon_offset= False, to_file=False):
    
    args = [log, d, temp_setpoint, shutter_laser, shutter_laserOut,
           shutter_opoOut, shutter_shg, shutter_shgOut, laser, galvo,
            etalon_offset, dial]
    # args = args[args[True]]

    if log is True:
        log = writing(cw.get_log(), timeout, step)
       
    if temp_setpoint is True:
        temp_setpoint = writing(cw.get_temperature_setpoint(), timeout, step, cwave.TemperatureChannel(d))
    
    if shutter_laser is True:
        shutter_laser = writing(cwave.CWave().get_shutter(cwave.ShutterChannel('las')), timeout, step)
        
    if shutter_laserOut is True:
        shutter_laserOut = writing(cwave.CWave().get_shutter(), timeout, step, cwave.ShutterChannel('las_out'))

    if shutter_opoOut is True:
        shutter_opoOut = writing(cwave.CWave().get_shutter(), timeout, step, cwave.ShutterChannel('opo_out'))
        
    if shutter_shg is True:
        shutter_shg = writing(cwave.CWave().get_shutter(), timeout, step, cwave.ShutterChannel('shg'))

    if shutter_shgOut is True:
        shutter_shgOut = writing(cwave.CWave().get_shutter(), timeout, step, cwave.ShutterChannel('shg_out'))

    if dial is True:
        dial = writing(cwave.CWave().get_dial_done(), timeout, step)

    if laser is True:
        laser = writing(cwave.CWave().get_laser(), timeout, step)
        
    if etalon_offset is True:
       etalon_offset = writing(cwave.CWave().get_etalon_offset(), timeout, step)
        
    if galvo is True:
        galvo = writing(cwave.CWave().get_galvo_position(), timeout, step)
  
    return args

#for value in range(0, 65535, 100):
#    cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, value)
 #   print('Manual Output Value: {} / {}%'.format(value, int(value/65535*100)))
  #  time.sleep(0.01)

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

cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, 0)
cw.set_piezo_mode(cwave.PiezoChannel.Opo, cwave.PiezoMode.Manual)
i = 0
cw.set_etalon_offset(0)
e_offset = cw.get_etalon_offset()

while i <= 15:
    for value in range(0, 40000, 500):
        cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, value)
        time.sleep(0.001)

    for value in range(40000, 0, -500):
        cw.set_piezo_manual_output(cwave.PiezoChannel.Opo, value)
        time.sleep(0.001)
    cw.set_etalon_offset(e_offset + i * 1500)
    time.sleep(0.001)
    
    if i == 15:
        cw.set_temperature_setpoint(cwave.TemperatureChannel.Opo, cw.get_mapping_temperature(cwave.MappingChannel.Opo, 1149.695))
        time.sleep(5)
    i += 1
    print(i)