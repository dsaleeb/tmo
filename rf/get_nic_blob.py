from rf.login import login


def get_nic_blob(un, pw, url, api=1, unit=1):
    """"
    (str) Network interfaces
    """
    rfo = login(un, pw, url)
    res = rfo.get(f"/redfish/v{api}/Systems/{unit}/EthernetInterfaces")
    members = res.dict['Members']
    for m in members:
        res = rfo.get(m['@odata.id'])
        print(f"Ethernet Interface {m['@odata.id']} MAC Address: {res.dict['MACAddress']}")
        print(f"Ethernet Interface {m['@odata.id']} IP4 Addresses: {res.dict['IPv4Addresses']}")
        print(f"Ethernet Interface {m['@odata.id']} Name: {res.dict['Name']}")
        print(f"Ethernet Interface {m['@odata.id']} Interface Enabled: {res.dict['InterfaceEnabled']}")
        print(f"Ethernet Interface {m['@odata.id']} Link Status: {res.dict['LinkStatus']}")
        print(f"Ethernet Interface {m['@odata.id']} Link State: {res.dict['Status']['State']}")
        print(f"Ethernet Interface {m['@odata.id']} Link Health: {res.dict['Status']['Health']}")
        print(f"Ethernet Interface {m['@odata.id']} Name Servers: {res.dict['NameServers']}")
        print(f"Ethernet Interface {m['@odata.id']} Speed Mbps: {res.dict['SpeedMbps']}")

    rfo.logout()



