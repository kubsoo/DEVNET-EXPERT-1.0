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

- `CISCO LIVE` [Use of Jinja2 templates with Ansible Playbook](https://fchaudhr.github.io/LTRDCN_1572/task3-vxlan-jinja2/)

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
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  
|  
|---- files  
|  
|---- handlers  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  
|  
|---- meta  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  
|  
|---- tasks  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  
|  
|---- templates  
|  
|---- tests  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ inventory    
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  
|  
|---- vars  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____ main.yml  

<br></br>

# Ansible Variables Precedence Order

1. **role defaults (defined in role/defaults/main.yml)**

2. inventory file or script group vars

3. inventory group_vars/all

4. **playbook group_vars/all**

5. inventory group_vars/*

6. playbook group_vars/*

7. inventory file or script host vars

8. inventory host_vars/*

9. playbook host_vars/*

10. host facts

11. play vars

12. play vars_prompt

13. play vars_files

14. **role vars (defined in role/vars/main.yml)**

15. block vars (only for tasks in block)

16. task vars (only for the task)

17. role (and include_role) params

18. include params

19. include_vars

20. set_facts / registered vars

21. extra vars (always win precedence)

<br></br>

<br></br>

# Loops

## Iterating over a simple list

```
- name: Add several users
  ansible.builtin.user:
    name: "{{ item }}"
    state: present
    groups: "wheel"
  loop:
     - testuser1
     - testuser2
```

## Iterating over a dictionary

```
- name: Using dict2items
  ansible.builtin.debug:
    msg: "{{ item.key }} - {{ item.value }}"
  loop: "{{ tag_data | dict2items }}"
  vars:
    tag_data:
      Environment: dev
      Application: payment
```


# Jinja2 templates

Jinja2 tags:

- **{{ }}**  : These double curly braces are the widely used tags in a template file and they are used for embedding variables and ultimately printing their value during code execution. For example, a simple syntax using the double curly braces is as shown: The **{{ webserver }}** is running on  **{{ nginx-version }}**

- **{%  %}** : These are mostly used for control statements such as loops and if-else statements.

- **{#  #}** : These denote comments that describe a task.


`example_template.j2`
```
This is jinja2 template
Apache webserver {{ version_number }} is running on {{ server }}

{% for item in routers %}
	{{ item }}
{% endfor %}
```

---
---
---
<br></br>
# LAB TASKS

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