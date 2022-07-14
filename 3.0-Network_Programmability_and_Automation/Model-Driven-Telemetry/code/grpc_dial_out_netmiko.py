from netmiko import ConnectHandler

c8000v = {
    'device_type' : 'cisco_ios',
    'host' : '192.168.54.131',
    'port' : 22,
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

net_connect = ConnectHandler(**c8000v)



config_commands = []

for key,value in xpaths.items():
  config_lines = f'''telemetry ietf subscription {key}
    encoding encode-kvgpb
    filter xpath {value}
    stream yang-push
    update-policy periodic {period}
    receiver ip address {receiver_ip} {receiver_port} protocol grpc-tcp'''

  config_commands = config_lines.split('\n')
  output = net_connect.send_config_set(config_commands)
  print(output)
