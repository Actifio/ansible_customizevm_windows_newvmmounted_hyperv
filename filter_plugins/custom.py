# coding:utf-8
from ansible import errors

def ret_macaddress_from_getvmnetadpt ( output, switch ):
    mac = ""
    # pick lines including keyword
    line = [ s for s in output if switch in s ]
    if len(line) == 0:
        return mac
    # pick first line of result
    output_list = line[0].split()
    flag = 0
    for str in output_list:
        if flag != 0:
            mac = str[0:2] + "-" + str[2:4] + "-" + str[4:6] + "-" + str[6:8] + "-" + str[8:10] + "-" + str[10:12]
            return mac
        elif str == switch:
            flag = 1
        else:
            flag = 0

def ret_adapterindex ( output, keyword ):
    index = ""
    # pick lines including keyword
    line = [ s for s in output if keyword in s ]
    if len(line) == 0:
        return index
    # pick first line of result
    output_list = line[0].split()
    for str in output_list:
        if str == "Up" or str == "Down":
            return index
        else:
            index = str

class FilterModule(object):
    def filters(self):
        return {
            'ret_macaddress_from_getvmnetadpt': ret_macaddress_from_getvmnetadpt,
            'ret_adapterindex': ret_adapterindex
        }
