from pyghmi.ipmi import command
bmc='10.127.2.169'
user='root'
password='Huawei12#$'
ipmicmd = command.Command(bmc=bmc, userid=user, password=password)
ret = ipmicmd.get_power()
print ret