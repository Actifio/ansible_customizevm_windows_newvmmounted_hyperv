ansible_customize_windows_newvmmounted_hyperv
======================

This is an ansible role to perform customize Windows VM which was mounted with Actifio Hyper-VM VM as new VM.

This role covers sysprep, change network configuration and hostname and join AD domain if necessary. 

Requirements
--------------

Ansible >= 2.5 and PyWinrm module are required.

Required Windows 2016 or later for Hyper-V host and VM because of using Powershell direct feature. ( Issuing commands to Hyper-V host through WinRM then passing them to taget VM using Powershell direct. )

Sysprep response file must be located with source VM image if you want to do sysprep. 

Need to adjust pause seconds between tasks within tasks/main.yml for your environment.


Role Variables
--------------

Following variables are accepted/required for this role. 

| Variable Name    | Description | Required (Y/N) |
|------------------|---|---|
| tgt_vm_name      | Target VM name which will be customized with this role. | Y
| vmwin_switch     | Virtual switch name which will be connected the Target VM. | Y
| vmwin_cpu_count  | VM CPU count if need to change the configuration. | N
| vmwin_memory_size  | VM memory size if need to change the configuration. | N
| vmwin_memory_size_min  | VM minimum memory size with dynamic memory feature. (Need to specify this with vmwin_memory_size_max in order to enable) | N
| vmwin_memory_size_max  | VM maximum memory size with dynamic memory feature. (Need to specify this with vmwin_memory_size_max in order to enable) | N
| vmwin_adminuser      | Administrator user name of the target Windows VM. Default is 'Administrator' | Y
| vmwin_adminpassword  | Administrator user password of the target Windows VM. | Y
| vmwin_sysprep_respfile     | Sysprep response file path within VM. If not specify this value, the role will skip doing sysprep. | N
| vmwin_ip_address  | New IP address of the target Windows VM. | Y
| vmwin_ip_prefixlength  | New IP prefix length (netmask) of the target Windows VM. | Y
| vmwin_ip_gateway  | New IP gateway address of the target Windows VM. | Y
| vmwin_dns_address | New DNS server address of the target Windows VM. | N
| vmwin_ad_domain   | AD domain name which is joining. | N
| vmwin_ad_adminuser   | AD domain administrator user name. | N
| vmwin_ad_adminpassword   | AD domain administrator user password. | N

Example Playbook
----------------

### Customize Windows VM after mounting image as New VM by Actifio

```
- name: customize windows vm after mounting image as new vm by actifio
  hosts: "{{ host_group }}"
  roles:
    - ansible_customizevm_windows_newvmmounted_hyperv
  vars:
    tgt_vm_name: DemoWin2016
    vmwin_switch: InternalSW
    vmwin_adminpassword: password
    vmwin_sysprep_rspfile: C:\Windows\System32\Sysprep\Untitled.xml
    vmwin_ip_address: 192.168.10.10
    vmwin_ip_prefixlength: 24
    vmwin_ip_gateway: 192.168.10.1
    vmwin_dns_address: 192.168.10.1

```


License
-------

Copyright 2018 <Hiroshi Takeuchi hiroshi.takeuchi@actifio.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
