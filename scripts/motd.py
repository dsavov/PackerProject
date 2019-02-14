import datetime
import socket

filepath = "/etc/motd"
current_datetime = str(datetime.datetime.now())
hash_current_datetime = str(hash(datetime.datetime.now()))
hostname = socket.gethostname()    
ip_addr = socket.gethostbyname(hostname) 

try:
    with open(filepath, "w+") as outfile:
        outfile.write("current_datetime:" + current_datetime + "\n")
        outfile.write("hash_current_datetime:" + hash_current_datetime + "\n")
        outfile.write("hostname:" + hostname + "\n")
        outfile.write("ip_address:" + ip_addr + "\n")
except IOError:
    print("Couldn't open/create/write to file:" + filepath)
