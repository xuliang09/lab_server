#-*- coding: utf-8 -*-
import paramiko
import json
from  multiprocessing.pool import ThreadPool


def search_ip(ip, port, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=1)
    print('@'*30, ip, '@'*30, end='\n\n')
    for cmd in command:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        for line in stdout.readlines():
            print(line.strip())
    print('@'*90, end='\n\n\n')
    ssh.close()


if __name__=='__main__':
    config = json.load(open('config.json'))

    command = ['nvidia-smi']
    username = config['username']
    password = config['password']
    port = config['port']
    thread_num = config['thread_num']
    ipv4_mask = config['ipv4_mask']
    thread_pool = ThreadPool(thread_num)
    
    ipv4_mask_list = []
    for item in ipv4_mask.strip().split('.'):
        ipv4_mask_list.append((int(item), int(item) + 1) if item!='0' else (1, 256))

    print("starting to search IP...")
    for m in range(ipv4_mask_list[0][0], ipv4_mask_list[0][1]):
        for k in range(ipv4_mask_list[1][0], ipv4_mask_list[1][1]):
            for j in range(ipv4_mask_list[2][0], ipv4_mask_list[2][1]):
                for i in range(ipv4_mask_list[3][0], ipv4_mask_list[3][1]):
                    ip = '{}.{}.{}.{}'.format(m, k, j, i)
                    thread_pool.apply_async(search_ip, args=(ip, port, username, password, command))

    thread_pool.close()
    thread_pool.join()
