#!/usr/bin/env python3

# gurkan,2016
# license info: http://www.wtfpl.net/

username = "ilo-username"
password = 'ilo-password'

import hpilo

serverlist = [
"192.168.192.168",
"10.20.10.20" ]

def myprint(string):
  __builtins__.print("%s" % string,  end=";", flush=True)

for server in serverlist:
    try:
        ilo = hpilo.Ilo(server, username, password, timeout=300)
        getnetworksettings = ilo.get_network_settings()
        myprint(getnetworksettings["ip_address"])
        gethostdata = ilo.get_host_data()
        myprint(gethostdata[1]['Product Name'])
        myprint(ilo.get_server_name())
        getfwversion = ilo.get_fw_version()
        ilovers = getfwversion['management_processor']
        myprint(ilovers)
        myprint(getfwversion['firmware_version'])
        myprint(getnetworksettings["prim_dns_server"])
        myprint(getnetworksettings["sec_dns_server"])
        if ilovers != "iLO2":
            myprint(getnetworksettings["sntp_server1"])
            myprint(getnetworksettings["sntp_server2"])
        else:
            myprint("")
            myprint("")
        print(ilo.get_all_users(), end=";", flush=True)
        if ilovers == "iLO4":
            getglobalsettings = ilo.get_global_settings()
            myprint(getglobalsettings["alertmail_email_address"])
            myprint(getnetworksettings["domain_name"])
            myprint(getglobalsettings["alertmail_enable"])
        else:
            myprint("")
            myprint("")
            myprint("")
        myprint(ilo.get_snmp_im_settings()["snmp_address_1"])
        myprint(gethostdata[1]['Serial Number'])
        health = ilo.get_embedded_health()
        try:
            myprint(health["firmware_information"]["System ROM"])
        except KeyError:
            if ilovers == "iLO2":                
                myprint(gethostdata[0]["Date"])
            else:       
                try:
                    myprint(health["firmware_information"]["HP ProLiant System ROM"])
                except KeyError:
                    myprint(gethostdata[0]["Date"])
        except:
            myprint("cant found")
        for i in health['health_at_a_glance']:
            print(health['health_at_a_glance'][i]['status'], end="_", flush=True)
        print("")
    except Exception as e:
        print(e)

# https://gurkan.in/2016/10/11/generating-server-report-from-ilo-interface-hp-servers/
# https://www.reddit.com/r/sysadmin/comments/4l874f/thought_someone_could_use_this_so_i_made_a_post/