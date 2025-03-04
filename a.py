import DrEmpower_CyberGear as dr

# a= DrEmpower_CyberGear.read_data(16)
# print(a)
# dr.set_speed(1, 10, 23)
import serial
dr.init_data()
dr.set_angle(1, 0, 100, 27)
