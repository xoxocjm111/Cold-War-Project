from termcolor import colored
import os
import webbrowser
import textwrap
import time

url = 'https://github.com/xoxocjm111/History-Project'
#windows path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
version = '1.3.1'
about_me = 'Period 5 History Project ' f'Version {version}' ' Developed by Christopher McCormick :)'

def exit_timer():
   exit_status = 5
   while exit_status > 0:
      exit_status = exit_status - 1
      print(colored(f'Exiting in {exit_status}', 'blue'))
      time.sleep(1)
   if exit_status == 0:
      os.system('cls')
      exit()
      
def clear_reset():
   os.system('cls')
   os.system('python main.py')

os.system('cls')
print(colored("""
 _______ _             _____      _     _  __          __        
 |__   __| |           / ____|    | |   | | \ \        / /        
    | |  | |__   ___  | |     ___ | | __| |  \ \  /\  / /_ _ _ __ 
    | |  | '_ \ / _ \ | |    / _ \| |/ _` |   \ \/  \/ / _` | '__|
    | |  | | | |  __/ | |___| (_) | | (_| |    \  /\  / (_| | |   
    |_|  |_| |_|\___|  \_____\___/|_|\__,_|     \/  \/ \__,_|_|  """, 'blue'))


print('')
print(colored(f'Version: {version}', 'green'))  
print('')
print('')
print(colored('[1] Code Information (UPDATED REGULARLY)', 'blue'))
print('')
print(colored('[2] Rosa Parks and the Bus Boycotts', 'red'))
print('')
print(colored('[3] Little Rock 9', 'blue'))
print('')
print(colored('[4] March On Washington', 'red'))
print('')
print(colored('[5] About', 'blue'))
print('')
print(colored('[6] Exit', 'red'))
print('')

while True:

   user_input = int(input(colored('[!] Type Here: ', 'blue')))

   if user_input == 1:
      webbrowser.get(chrome_path).open(url)
      clear_reset()
      
   elif user_input == 2:
      os.system('cls')
      print(textwrap.fill((colored("""The Montgomery Bus Boycott was a civil rights protest in which African-Americans refused to ride city buses in Montgomery, Alabama to protest segregation of seats.
               The boycott took place from December 5, 1955 to December 20, 1956 and is considered the first large-scale American protest against apartheid. 
               Four days before the boycott began, Rosa Parks, an African-American woman, was arrested and fined for refusing to give up her bus seat to a white man. 
               The U.S. Supreme Court eventually ordered Montgomery to integrate its bus system, and one of the boycott's leaders named Martin Luther King Jr, 
               became a preacher. Prominent leader of the American civil rights movement.""", 'blue'))))
      print('')
      u_i = input(colored('[Y,N]Continue?: ', 'blue')).lower
      if u_i == 'y' or 'Y':
         os.system('python main.py')
      else:
         os.system('cls')
         exit()
   elif user_input == 3:
         os.system('cls')
         print(textwrap.fill((colored("""On September 4, 1957, nine African-American students attended Central High School in Little Rock, Arkansas. 
                          They made their way through crowds shouting obscenities and even throwing objects. 
                          When the students reached the front gate, the National Guard prevented them from entering the school and  forced them to return home. 
                          The students returned on September 29. This time they were protected by federal troops. 
                          Students can enter the school, eventually entering the High School. This group of students became known as "Little Rock Nine".""", 'blue'))))
   elif user_input == 4:
      os.system('cls')
      print(textwrap.fill(colored("""About 250,000 people are participating in  March on Washington for Jobs and Freedom. 
                                     Martin Luther King delivered his  closing address at the Lincoln Memorial, declaring, "I have a dream that one day this country will rise  and live  the true meaning of the creed: `We stand our ground. 
                                     These facts are self-evident: that all men are created equal.""", 'blue')))
   elif user_input == 5:
      os.system('cls')
      print('')
      print(colored(about_me, 'green'))
   else:
      exit_timer()
   print('')
   u_i = input(colored('[Y,N]Continue?: ', 'blue'))
   if u_i == 'y' or 'Y':
      os.system('python main.py')
   else:
      os.system('cls')
      exit()
   
   
#indents to make it 100 again just cuz lol :3