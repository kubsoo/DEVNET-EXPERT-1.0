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

# List of Materials

- [BOOK] [Network Programmability with YANG: The Structure of Network Automation with YANG, NETCONF, RESTCONF, and gNMI](https://learning.oreilly.com/library/view/network-programmability-with/9780135180471/)

- [CISCO DOCS] [Programmability Configuration Guide: Model-Driven Telemetry](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/1612/b_1612_programmability_cg/model_driven_telemetry.html)
- [YOUTUBE] [IOS-XE Model Driven Telemetry with gRPC Dial-Out](https://www.youtube.com/watch?v=p94yetSTXdc)
- [DOCS] [Data Center Telemetry and Network Automation Using gNMI and OpenConfig White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-744191.html)
- [BLOG] [Streaming Telemetry with Google Protocol Buffers](https://blogs.cisco.com/sp/streaming-telemetry-with-google-protocol-buffers)
- [GITHUB] [Cisco IOS XE - YANG based Model Driven Telemetry](https://github.com/jeremycohoe/cisco-ios-xe-mdt)
- [CISCO LIVE] [Advanced Topics in Cisco IOS Telemetry](https://www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/BRKSPG-2503.pdf)

<br></br>

# SNMP vs MDT

| Simple Network Management Protocol (SNMP) | Model Driven Telemetry (MDT)|
| ------------- | ------------- |
| Non Real-Time Information  | Real-Time Information |
| Poorly scalable  | Highly scalable  |
| Pull-Model  | Push-Model  |
| Non Automated  | Automation Ready/ Data-Model Driven  |

<br></br>
# Encoding Options

| Encoding | Description | Wire Efficiency | Other Considerations
| ------------- | ------------- | ------------- | ------------- |
| JSON  | Everything strings: keys and values | Low | Friendly. Human readable, easy for humans and code to parse
| GBP-KV  | String keys and binary values (except values that are strings) | Medium Low | Single .proto file for decoding. Can use GPB tooling
| GBP (-Compact)  | Everything binary (except values that are strings)  | High | Proto file per model

<br></br>
# Encoding Options

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
			<td>XML</td>
			<td>No</td>
			<td>No</td>
			<td>Key-Value Google Protocol Buffers (kvGPB)</td>
			<td>JSON_IETF</td>
			<td>No</td>
		</tr>
	</tbody>
</table>

