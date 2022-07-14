# DevNet Expert (v1.0) Lab Exam Topics
3.5 `Design` a model-driven telemetry solution based on given business and technical requirements by using gNMI dial-in, gRPC dial-out, and NETCONF dial-in

3.6 `Create` YANG model-driven telemetry subscriptions
- 3.6.a Identify model elements and cadence
- 3.6.b On-change or event drive
- 3.6.c Optimize frequency
- 3.6.d Dial-out subscription
- 3.6.e Secure telemetry streams
- 3.6.f Confirm data transmission
- 3.6.g Identify network issues and make changes

<br></br>

# LAB SECTION

## IOS-XE gRPC dial-out using TIG (Telegraf + InfluxDB + Grafana ([setting up TIG docker container](https://github.com/jeremycohoe/cisco-ios-xe-mdt#docker-container-tig_mdt))
<br>

### - [Create gRPC dial-out subscriptions using NETCONF and ncclient](#1-create-grpc-dial-out-subscriptions-using-netconf-and-ncclient) 

### - [Create gRPC dial-out subscriptions using netmiko](#2-create-grpc-dial-out-subscriptions-using-netmiko) 

### - [Create gRPC dial-out subscriptions using ansible and network_cli module](#3-create-grpc-dial-out-subscriptions-using-ansible-and-network_cli-module)

### - [Create gRPC dial-out subscriptions using ansible and netconf module](#4-create-grpc-dial-out-subscriptions-using-ansible-and-netconf-module)

### - [Create gRPC dial-out subscriptions using restconf](#5-create-grpc-dial-out-subscriptions-using-restconf)

<br></br>

# List of Materials

- `BOOK` [Network Programmability with YANG: The Structure of Network Automation with YANG, NETCONF, RESTCONF, and gNMI](https://learning.oreilly.com/library/view/network-programmability-with/9780135180471/)

- `CISCO DOCS` [Programmability Configuration Guide: Model-Driven Telemetry](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/1612/b_1612_programmability_cg/model_driven_telemetry.html)
- `YOUTUBE` [IOS-XE Model Driven Telemetry with gRPC Dial-Out](https://www.youtube.com/watch?v=p94yetSTXdc)
- `DOCS` [Data Center Telemetry and Network Automation Using gNMI and OpenConfig White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-744191.html)
- `BLOG` [Streaming Telemetry with Google Protocol Buffers](https://blogs.cisco.com/sp/streaming-telemetry-with-google-protocol-buffers)
- `GITHUB` [Cisco IOS XE - YANG based Model Driven Telemetry](https://github.com/jeremycohoe/cisco-ios-xe-mdt)
- `CISCO LIVE` [Advanced Topics in Cisco IOS Telemetry](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/BRKSPG-2503.pdf)

<br></br>

# A Brief Introduction to Telemetry

To start with, in simple terms, Telemetry is the collection process of useful operational data. As per Wikipedia, Telemetry is an automated communications process by which measurements and other data are collected at remote or inaccessible points and transmitted to receiving equipment for monitoring. Telemetry word itself is derived from Greek roots: tele = remote, and metron = measure.

For the network management, Network operators have a long history of relying on Simple Network Management Protocol (SNMP). While SNMP is widely adopted for network monitoring, it was never used for configuration even though capability of configuration with snmp was always there. Operators have written automation scripts to handle day to day configuration tasks, but scripts are challenging for such tasks and difficult to manage.

Hence operators moved towards data model driven management. Network configuration is based on YANG data models pushed by protocols like netconf for example. Now just pushing the configuration doesn’t imply that configured service is running, there has to be a mechanism which can monitor services operational data at the same time as the configuration. This is where oper data models; which Telemetry uses to push information out of device; helps. Therefore, the configuration is YANG data model driven so must be the verification of service as well; as the case with Telemetry, in order to have the same object semantic. Hence the term is called Model Driven Telemetry or streaming Telemetry.

`SOURCE` [ASR9K Model Driven Telemetry Whitepaper](https://www.cisco.com/c/en/us/support/docs/routers/asr-9000-series-aggregation-services-routers/215321-asr9k-model-driven-telemetry-whitepaper.html)

<br></br>

# SNMP vs MDT

| Simple Network Management Protocol (SNMP) | Model Driven Telemetry (MDT)|
| ------------- | ------------- |
| Non Real-Time Information  | Real-Time Information |
| Poorly scalable  | Highly scalable  |
| Pull-Model  | Push-Model  |
| Non Automated  | Automation Ready/ Data-Model Driven  |


`SOURCE` [ASR9K Model Driven Telemetry Whitepaper](https://www.cisco.com/c/en/us/support/docs/routers/asr-9000-series-aggregation-services-routers/215321-asr9k-model-driven-telemetry-whitepaper.html)

<br></br>
# Supported Combination of protocols

<table>
	<tbody>
		<tr>
			<td>Transport Protocol</td>
			<td colspan="2"><strong>NETCONF</strong></td>
			<td colspan="2"><strong>gRPC</strong></td>
			<td colspan="2"><strong>gNMI</strong></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>Dial-In</td>
			<td>Dial-Out</td>
			<td>Dial-In</td>
			<td>Dial-Out</td>
			<td>Dial-In</td>
			<td>Dial-Out</td>
		</tr>
		<tr>
			<td colspan="9"><strong>Stream</strong></td>
		</tr>
		<tr>
			<td>yang-push</td>
			<td><strong>Yes</strong></td>
			<td>No</td>
			<td>No</td>
			<td><strong>Yes</strong></td>
			<td><strong>Yes</strong></td>
			<td>No</td>
		</tr>
        		<tr>
			<td>yang-notif-native</td>
			<td><strong>Yes</strong></td>
			<td>No</td>
			<td>No</td>
			<td><strong>Yes</strong></td>
			<td>No</td>
			<td>No</td>
		</tr>
        		<tr>
			<td><strong>Encodings</strong></td>
			<td><strong>XML</strong></td>
			<td>No</td>
			<td>No</td>
			<td><strong>Key-Value Google Protocol Buffers (kvGPB)</strong></td>
			<td><strong>JSON_IETF</strong></td>
			<td>No</td>
		</tr>
	</tbody>
</table>

<br></br>
# Dial-In and Dial-Out Model-Driven Telemetry

| Dial-In (Dynamic) | Dial-Out (Static or Configured) |
| ------------- | ------------- |
| Telemetry updates are sent to the initiator or subscriber  | Telemetry updates are sent to the specified receiver or collector |
| Life of the subscription is tied to the connection (session) that created it, and over which telemetry updates are sent. No change is observed in the running configuration | Subscription is created as part of the running configuration; it remains as the device configuration till the configuration is removed |
| Dial-in subscriptions need to be reinitiated after a reload, because established connections or sessions are killed during stateful switchover | Dial-out subscriptions are created as part of the device configuration, and they automatically reconnect to the receiver after a stateful switchover |
| Subscription ID is dynamically generated upon successful establishment of a subscription | Subscription ID is fixed and configured on the device as part of the configuration | 


<br></br>
# Encoding Options

| Encoding | Description | Wire Efficiency | Other Considerations
| ------------- | ------------- | ------------- | ------------- |
| JSON  | Everything strings: keys and values | Low | Friendly. Human readable, easy for humans and code to parse
| GBP-KV  | String keys and binary values (except values that are strings) | Medium Low | Single .proto file for decoding. Can use GPB tooling
| GBP (-Compact)  | Everything binary (except values that are strings)  | High | Proto file per model

`SOURCE` [https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/BRKSPG-2503.pdf](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/BRKSPG-2503.pdf) - slide 33

<br></br>
---
---
---
<br></br>
# LAB TASKS

`xpath`

- CPU utilization 5 seconds 

```
xpath : /process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds 
```

- Memory Statistic

```
xpath : /memory-ios-xe-oper:memory-statistics/memory-statistic
```
<br></br>

## 1. Create gRPC dial-out subscriptions using NETCONF and ncclient

`TASK` Create python script which configure gRPC dial-out telemetry subscriptions that sends CPU utilization (5 sec) and memory statistics data to receiver every 5 seconds using ncclient python library.

`SOLUTION` [grpc_dial_out_netconf.py](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/grpc_dial_out_netconf.py)
<br></br>

---
## 2. Create gRPC dial-out subscriptions using netmiko

`TASK` Create python script which configure gRPC dial-out telemetry subscriptions that sends CPU utilization (5 sec) and memory statistics data to receiver every 5 seconds using netmiko python library.

`SOLUTION` [grpc_dial_out_netmiko.py](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/grpc_dial_out_netmiko.py)
<br></br>

---
## 3. Create gRPC dial-out subscriptions using ansible and network_cli module

`TASK` Create ansible playbook which configure gRPC dial-out telemetry subscriptions that sends CPU utilization (5 sec) and memory statistics data to receiver every 5 seconds using network_cli module.

`SOLUTION` [playbook.yml](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/playbook.yml)
<br></br>

---
## 4. Create gRPC dial-out subscriptions using ansible and netconf module

`TASK` Create ansible playbook which configure gRPC dial-out telemetry subscriptions that sends CPU utilization (5 sec) and memory statistics data to receiver every 5 seconds using netconf module.

`SOLUTION` [playbook.yml](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/playbook_netconf.yml)
<br></br>

---
## 5. Create gRPC dial-out subscriptions using restconf

`TASK` Create python script which configure gRPC dial-out telemetry subscriptions that sends CPU utilization (5 sec) and memory statistics data to receiver every 5 seconds using requests python library.

`SOLUTION` [playbook.yml](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/restconf.py)
<br></br>