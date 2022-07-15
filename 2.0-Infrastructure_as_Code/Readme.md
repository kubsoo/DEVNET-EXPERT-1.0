# DevNet Expert (v1.0) Lab Exam Topics
2.8 `Create` and use a role by utilizing Ansible to manage infrastructure, given support documentation
- 2.8.a Loop control
- 2.8.b Conditionals
- 2.8.c Use of variables and templating
- 2.8.d Use of connection plug-ins such as network CLI, HTTPAPI, and NETCONF

<br></br>

# LAB SECTION

## IOS-XE gRPC dial-out using TIG (Telegraf + InfluxDB + Grafana ([setting up TIG docker container](https://github.com/jeremycohoe/cisco-ios-xe-mdt#docker-container-tig_mdt))
<br>

### - [1. Create gRPC dial-out subscriptions using NETCONF and ncclient](#1-create-grpc-dial-out-subscriptions-using-netconf-and-ncclient) 

### - [2. Create gRPC dial-out subscriptions using netmiko](#2-create-grpc-dial-out-subscriptions-using-netmiko) 

### - [3. Create gRPC dial-out subscriptions using ansible and network_cli module](#3-create-grpc-dial-out-subscriptions-using-ansible-and-network_cli-module)

### - [4. Create gRPC dial-out subscriptions using ansible and netconf module](#4-create-grpc-dial-out-subscriptions-using-ansible-and-netconf-module)

### - [5. Create gRPC dial-out subscriptions using restconf](#5-create-grpc-dial-out-subscriptions-using-restconf)

### - [6. Create Dynamic Subscriptions for NETCONF Dial-In using YANGSuite]()

### - [7. Secure gRPC dial-out with TLS]()

<br></br>

# List of Materials

- `DOCS` [Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/)

- `DOCS` [Creating Roles](https://galaxy.ansible.com/docs/contributing/creating_role.html)

- `YOUTUBE` [Ansible Roles Explained](https://www.youtube.com/watch?v=Or6k2UcKeN4)

- `TRAINING` [Introduction to Ansible](https://developer.cisco.com/learning/modules/sdx-ansible-intro/ansible-02_ansible-intro/step/1)

- `VIDEO TRAINING` [Configuration Management and the Network](https://developer.cisco.com/video/net-prog-basics/05-netdevops)

- `CISCO LIVE` [Network Automation using YANG Models across XE, XR, & NX - Ansible Networking](http://yang.ciscolive.com/pod0/labs/lab2/lab2-m4)

- `BOOK` [Ansible: Up and Running, 3rd Edition](https://learning.oreilly.com/library/view/ansible-up-and/9781098109141/) 

<br></br>

# What is Ansible

Ansible is a software tool that provides simple but powerful automation for cross-platform computer support. It is primarily intended for IT professionals, who use it for application deployment, updates on workstations and servers, cloud provisioning, configuration management, intra-service orchestration, and nearly anything a systems administrator does on a weekly or daily basis. Ansible doesn't depend on agent software and has no additional security infrastructure, so it's easy to deploy.

Because Ansible is all about automation, it requires instructions to accomplish each job. With everything written down in simple script form, it's easy to do version control. The practical result of this is a major contribution to the "infrastructure as code" movement in IT: the idea that the maintenance of server and client infrastructure can and should be treated the same as software development, with repositories of self-documenting, proven, and executable solutions capable of running an organization regardless of staff changes.

While Ansible may be at the forefront of automation, systems administration, and DevOps, it's also useful to everyday users. Ansible allows you to configure not just one computer, but potentially a whole network of computers at once, and using it requires no programming skills. Instructions written for Ansible are human-readable. Whether you're entirely new to computers or an expert, Ansible files are easy to understand.

`SOURCE` [What is Ansible?](https://opensource.com/resources/what-ansible)

<br></br>

# Ansible Roles

- Roles helps to organize complex and large playbooks into reusable
components (file structures)

- Roles allows for separating components of playbooks: variables,
tasks, & templates etc into unique directories

- Grouping contents using Ansible roles makes code/automation
script sharing easier

### Roles Directory Structure

role_name

|---- defaults  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|_____ main.yml  
|  
|---- files  
|  
|---- handlers  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  
|  
|---- meta  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  



# Ansible Variables Precedence Order

**1. role defaults (defined in role/defaults/main.yml)**
2. inventory file or script group vars
3. inventory group_vars/all
**4. playbook group_vars/all**
5. inventory group_vars/*
6. playbook group_vars/*
7. inventory file or script host vars
8. inventory host_vars/*
9. playbook host_vars/*
10. host facts
11. play vars
12. play vars_prompt
13. play vars_files
**14. role vars (defined in role/vars/main.yml)**
15. block vars (only for tasks in block)
16. task vars (only for the task)
17. role (and include_role) params
18. include params
19. include_vars
20. set_facts / registered vars
21. extra vars (always win precedence)
<br></br>

# What is Ansible

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

`SOLUTION` [playbook-netconf.yml](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/playbook-netconf.yml)
<br></br>

---
## 5. Create gRPC dial-out subscriptions using restconf

`TASK` Create python script which configure gRPC dial-out telemetry subscriptions that sends CPU utilization (5 sec) and memory statistics data to receiver every 5 seconds using requests python library.

`SOLUTION` [restconf.py](https://github.com/kubsoo/DEVNET-EXPERT-1.0/blob/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry/code/restconf.py)
<br></br>