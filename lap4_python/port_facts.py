#(RFC 9293) TCP----- 16bits 
#(RFC 791) IPv4----- 32bits

Port=16
IPv4=32
possible_port=2**Port
possible_IPv4=2**IPv4
highest_port=possible_port-1

print(f"HPort : {highest_port} Port : {possible_port}  IPv4 : {possible_IPv4} ")