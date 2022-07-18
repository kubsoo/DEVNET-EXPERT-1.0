# DevNet Expert (v1.0) Lab Exam Topics

### 1.0 Software Design, Development, and Deployment - ``20%``
---
1.1 `Design` a solution based on an on-premises, hybrid, or public cloud deployment,considering these factors:
- 1.1.a Deployment: maintainability, modularity (e.g., containers, VM, orchestration, automation, components, and infrastructure requirements)
- 1.1.b Reliability: high availability and resiliency
- 1.1.c Performance: scalability, latency, and rate limiting
- 1.1.d Infrastructure: monitoring, observability, and metrics (e.g., instrument placement and instrument deployment)

<br>

### 2.0 Infrastructure as Code - ``30%``
---
2.1 `Create` a scalable solution for infrastructure automation (considering areas such as network impact, risk, and tool selection)

2.2 Build, manage, and operate a Python-based REST API with a web application framework (endpoints, HTTP request, and response)

2.3 Build, manage, and operate a Python-based CLI application to use a REST API

2.4 Consume and use a new REST API, given the documentation

2.5 `Create` a RESTCONF or NETCONF payload based on a given YANG module, and interpret the response

2.6 `Create` a NETCONF filter by using XPath

2.7 `Configure` network devices on an existing infrastructure by using NETCONF or RESTCONF, given YANG analysis tools

2.8 `Create` and use a role by utilizing Ansible to manage infrastructure, given support documentation [ANSIBLE](https://github.com/kubsoo/DEVNET-EXPERT-1.0/tree/master/2.0-Infrastructure_as_Code/Ansible)

- 2.8.a Loop control

- 2.8.b Conditionals

- 2.8.c Use of variables and templating

- 2.8.d Use of connection plug-ins such as network CLI, HTTPAPI, and NETCONF

2.9 Use Terraform to statefully manage infrastructure, given support documentation

- 2.9.a Loop control

- 2.9.b Resource graphs

- 2.9.c Use of variables

- 2.9.d Resource retrieval

- 2.9.e Resource provision

- 2.9.f Management of the state of provisioned resources

2.10 `Create` a basic Cisco NSO service package to meet given business and technical requirements. The service would generate a network configuration on the target device platforms using the "cisco-ios-cli" NED and be of type "python-and-template"

- 2.10.a `Create` a service template from a provided NSO device configuration

- 2.10.b `Create` a basic YANG module for the service containers (including lists, leaf lists, data types, leaf references, and single argument "when" and "must" conditions)

- 2.10.c `Create` basic actions to verify operational status of the service

- 2.10.d Monitor service status by reviewing the NCS Python VM log file

<br>

### 3.0 Network Programmability and Automation - ``25%``
---
3.1 Create, modify, and troubleshoot scripts by using Python libraries and SDK documentation to automate against APIs (ACI, AppDynamics, DNA Center, FDM, Intersight, IOS XE, Meraki, NSO, Webex)

3.2 Automate the configuration of a Cisco IOS XE network device (based on a provided architecture and configuration), including these components:

- 3.2.a Interfaces

- 3.2.b Static routes

- 3.2.c VLANs

- 3.2.d Access control lists

- 3.2.e BGP peering

- 3.2.f BGP and OSPF routing tables

- 3.2.g BGP and OSPF neighbors

3.3 Deploy an application on a Cisco IOS XE device by leveraging the technologies of Guest Shell and application hosting

3.4 Modify and troubleshoot an automated test by using pyATS to meet requirements

- 3.4.a Create a testbed file for connecting to Cisco IOS, IOS XE, or NX-OS devices

- 3.4.b Gather current configuration and operational state from devices using the Genie parsers and models included with pyATS

- 3.4.c Develop and execute test jobs and scripts using AEtest to verify network health

3.5 `Design` a model-driven telemetry solution based on given business and technical requirements by using gNMI dial-in, gRPC dial-out, and NETCONF dial-in [MDT](https://github.com/kubsoo/DEVNET-EXPERT-1.0/tree/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry)

3.6 `Create` YANG model-driven telemetry subscriptions [MDT](https://github.com/kubsoo/DEVNET-EXPERT-1.0/tree/master/3.0-Network_Programmability_and_Automation/Model-Driven-Telemetry)

- 3.6.a Identify model elements and cadence

- 3.6.b On-change or event drive

- 3.6.c Optimize frequency

- 3.6.d Dial-out subscription

- 3.6.e Secure telemetry streams

- 3.6.f Confirm data transmission

- 3.6.g Identify network issues and make changes

<br>

### 4.0 Containers - ``10%``
---
4.1 `Create` a Docker image (including Dockerfile)

- 4.1.a From a provided image

- 4.1.b Expose ports

- 4.1.c Add or copy files

- 4.1.d Run commands during image build

- 4.1.e Manipulate entry point and initial commands

- 4.1.f Establish working directories

- 4.1.g Environment variables as part of a definition to control an application

- 4.1.h Docker ignore file

- 4.1.i Volumes

4.2 Package and deploy a solution by using Docker Compose

- 4.2.a Deploy and manage containers

- 4.2.b Define services, networks, volumes, and links

4.3 Package and deploy a solution by using Kubernetes

- 4.3.a Use deployments, secrets, services, ingress, volumes, namespaces, and replicas

- 4.3.b Manage the lifecycle of pods (e.g., scale up, scale down, help status, logs)

- 4.3.c Monitor pods by building health checks)

- 4.3.d Use the kubectl interface

4.4 Create, consume, and troubleshoot a Docker host and bridge-based networks and integrate them with external networks


<br>

### 5.0 Security - ``15%``
---
5.1 Leverage OWASP secure coding practices into all solutions to meet given requirements

- 5.1.a Input validation

- 5.1.b Authentication and password management

- 5.1.c Access control

- 5.1.d Cryptographic practices

- 5.1.e Error handling and logging

- 5.1.f Communication security

5.2 `Create` a certificate signing request (CSR) by using OpenSSL; send CSR to a provided certificate authority; and use the certificate to secure a web application

5.3 Use OAuth2+ to obtain an authentication token

5.4 Use a secret management system to secure an application

5.5 Use tokens, headers, and secrets to secure a REST API