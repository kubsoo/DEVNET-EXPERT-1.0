from ncclient import manager

c8000v = {
    'ip' : '192.168.54.131',
    'port' : 830,
    'username' : 'cisco',
    'password' : 'cisco'
}

period = 500
receiver_ip = '192.168.54.1'
receiver_port = 57500

xpaths = {
    1:'/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds',
    2: '/memory-ios-xe-oper:memory-statistics/memory-statistic'
}

m = manager.connect(host=c8000v['ip'], port=c8000v['port'], username=c8000v['username'],
                    password=c8000v['password'],hostkey_verify=False)


for key,value in xpaths.items():

    netconf_payload = f'''
    <config>
      <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
        <mdt-subscription>
          <subscription-id>{key}</subscription-id>
          <base>
            <stream>yang-push</stream>
            <encoding>encode-kvgpb</encoding>
            <period>{period}</period>
            <xpath>{value}</xpath>
          </base>
          <mdt-receivers>
            <address>{receiver_ip}</address>
            <port>{receiver_port}</port>
            <protocol>grpc-tcp</protocol>
          </mdt-receivers>
        </mdt-subscription>
      </mdt-config-data>
    </config>
    '''
    response = m.edit_config(netconf_payload, target="running")

    if response.ok:
        print(f"Subscription {key} created succesfully!")
