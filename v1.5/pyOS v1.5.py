import os
import datetime
import webbrowser
import time
import socket
import platform
import subprocess
import re





#print(platform.processor())



version = 'v1.5'
print('pyOS made by flightyfigment0')
try:
    with open("log.txt",'r') as f1:
        print('---------------------------------------')
        f1 = open('log.txt','r')
        print(f1.read())
        print("pyOS "+version+" Booting Up...")
        print("---------------------------------------")
except FileNotFoundError:
    print(" _ __  _   _  ___  ___ ")
    print("| '_ \| | | |/ _ \/ __|")
    print("| |_) | |_| | (_) \__ \ ")
    print("| .__/ \__, |\___/|___/")
    print("| |     __/ |          ")
    print("|_|    |___/          .")
    print('pyOS'+version+"Booting Up...")
   
time.sleep(5)
loop = 0
list_commands = ['signout', 'open', 'time', 'crash', 'cal', 'link', 'color', 'theentireshrekmoviescript', 'txt', 'edittxt', 'info','21']
username = 0

login_status = 0

def help_command():
    print(list_commands)

def check_existing_username(username):
    with open("users.txt", "r") as file:
        existing_usernames = file.readlines()
        existing_usernames = [name.strip() for name in existing_usernames]
        if username in existing_usernames:
            return True
        else:
            return False

def add_user(username):
    with open("users.txt", "a") as file:
        file.write(username + "\n")

def main():
    new_username = input("Enter your username: ")
    
    if check_existing_username(new_username):
        print("you are now logged into "+new_username)
        login_status = (1)
        beans = new_username
    else:
        newuser_answer = input("would ou like this to be a new account (y/n):")
        if newuser_answer == ('y') or newuser_answer == ('yes'):
            add_user(new_username)
            print("User", new_username, "added successfully!")
        else:
            print('no new account added ')
if __name__ == "__main__":
    username = main()


def login():
    if login_status == (0):
        main
    else:
        print("you are all ready logged in")


loop = 0
print('type help for commands')
while loop == 0:
    print('---------------------------------------------')
    command_line = input("")
    if command_line == "help":
        help_command()
    elif command_line == "signout":
        login_status = 0
        main()
   
    elif command_line == "open":
        print('current apps:')
        print('1.notepad, 2.browser(microsoftedge), 3.taskmanger, 4.files(file explorer), 5.word, 6.onenote, 7.mail(outlook), 9.blender')
        choosen_file = input("")
        if choosen_file == ('notepad'):
            os.system("/Windows/notepad.exe")
        elif choosen_file == ('browser'):
            os.system("\"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe\"")
        elif choosen_file == ('blender'):
            os.system("\"C:/Users/141301/AppData/Local/Temp/quit.blend\"")
        elif choosen_file == ('taskmanger') or choosen_file == ("tskmngr"):
            os.system("\"C:\Windows\System32\Taskmgr.exe\"")
        elif choosen_file == ('files'):
            os.system("\"C:\Windows\explorer.exe\"")
        elif choosen_file == ("word"):
            os.system("\"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk\"")
        elif choosen_file == ("onenote"):
            os.system("\"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk\"")
        elif choosen_file == ("mail") or ("outlook"):
            os.system("\"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook.lnk\"")
        # Add other file opening commands here
    elif command_line == ('time'):
    # Get the current time
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print(formatted_time)
    elif command_line == ('crash'):
        while loop == (0):
            current_time = datetime.datetime.now()


            formatted_time = current_time.strftime("%H:%M:%S")


        print(formatted_time)



    elif command_line == ("cal"):
        cal_input = input("what operation do you want: ")
        if cal_input == ('add'):
            varb1 = input("first number: ")
            varb2 = input("second number: ")
            answer = int(varb1) + int(varb2)
            print(answer)
        elif cal_input == ('sub'):
            varb1 = input("first number: ")
            varb2 = input("second number: ")
            answer = int(varb1) - int(varb2)
            print(answer)
        elif cal_input == ('multi'):
            varb1 = input("first number: ")
            varb2 = input("second number: ")
            answer = int(varb1) * int(varb2)
            print(answer)
        elif cal_input == ('divde'):
            varb1 = input("first number: ")
            varb2 = input("second number: ")
            answer = int(varb1) / int(varb2)
            print(answer)
    elif command_line == ('color'):
        chosen_color = input("what color do you want the text to be")
        if chosen_color == ('red'):
            os.system('color 4')
            print('hello world')
        elif chosen_color == ('blue'):
            os.system('color 1')
            print('hello world')
        elif chosen_color == ('green'):
            os.system('color 2')
            print('hello world')
        elif chosen_color == ('aqua'):
            os.system('color 3')
            print('hello world')
        elif chosen_color == ('purple'):
            os.system('color 5')
            print('hello world')
        elif chosen_color == ('white'):
            os.system('color 7')
            print('hello world')
        elif chosen_color == ('grey'):
            os.system('color 8')
            print('hello world')
        elif chosen_color == ('powershell_colors'):
            os.system('color 10')
            print('hello world')


    elif command_line == ('link'):
        link = input("")
        webbrowser.open(link)
    elif command_line == ('theentireshrekmoivescript'):
        f = open("shrek.txt","r")
        print(f.read())
    elif command_line == ("txt"):
        txtname = input('what do you want to call the new file: ')
        txt = open(str(txtname),"x")
    elif command_line == ("edittxt"):
        file = input("which file")
        edit = input("what text do you want to add: ")
        f = open(str(file), "a")
        f.write(edit)
        print('edit completed')
        f.close()
    elif command_line == ('info'):
        print("-----------------------------------------------------------------------------------")
        #print("Username: "+)
        processor = platform.processor()
        architecture = platform.architecture()[0]
        system = platform.system()        
        model = platform.processor()
        match = re.search(r'(i[0-9])-\d{4}', model)
        if match:
            cpu_model = match.group(1)
        else:
            cpu_model = "Unknown"
        print("Processor:", processor)
        print("CPU Model:", cpu_model)
        print("Architecture:", architecture)
        print("System:", system)
        print('Version '+version)
        print("device name:",socket.gethostname())
        print('pyOS made by flightyfigment0')
    elif command_line == ("logo"):
        edit = input("what text do you want to add: ")
        f = open('log.txt', "w")
        f.write(edit)
        print('edit completed')
        f.close()
    elif command_line == ('21'):
        total = 0
        print("Welcome to the game of 21!")
        print("You and the computer will take turns adding 1, 2, or 3 to a running total.")
        print("The player who reaches exactly 21 wins.")
        while total < 21:
            player_input = input("Enter 1, 2, or 3 to add to the total: ")
            try:
                player_choice = int(player_input)
                if player_choice < 1 or player_choice > 3:
                    print("Please enter a number between 1 and 3.")
                    continue
                total += player_choice
                print(f"Total: {total}")
                if total >= 21:
                    print("Congratulations! You win!")
                    break
                computer_choice = min(3, 4 - player_choice)  # Computer tries to make total a multiple of 4
                print(f"Computer chooses: {computer_choice}")
                total += computer_choice
                print(f"Total: {total}")
                if total >= 21:
                    print("Sorry, you lose! Better luck next time.")
                    break
            except ValueError:
                print("Please enter a valid number.")
        print("Game over.")
    elif command_line == (''):
        print('p')







        
        


    else:
        print("not a valid command")


































   