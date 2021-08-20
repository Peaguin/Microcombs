# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:50:28 2021

@author: Confotec
"""
import cwave
import time

cw = cwave.CWave()
timeout_start = time.time()
cw.connect('localhost')
#shutter = cwave.ShutterChannel()

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

def dumb_writing():
