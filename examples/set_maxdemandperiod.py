""" Simple example set max demand period
(c) 2016 EKM Metering.
"""
from ekmmeters import *

my_port_name = "/dev/ttyS0"
my_meter_address = "300001162"

ekm_set_log(ekm_print_log)
port = SerialPort(my_port_name)

if (port.initPort() == True):
    my_meter = V4Meter(my_meter_address)
    my_meter.attachPort(port)
else:
    print "Cannot open port"
    exit()

if my_meter.setMaxDemandPeriod(MaxDemandPeriod.At_15_Minutes):
    if my_meter.request():
        mdp_str = my_meter.getField(Field.Max_Demand_Period)
        if mdp_str == str(MaxDemandPeriod.At_15_Minutes):
            print "15 Minutes"
        if mdp_str == str(MaxDemandPeriod.At_30_Minutes):
            print "30 Minutes"
        if mdp_str == str(MaxDemandPeriod.At_60_Minutes):
            print "60 Minutes"