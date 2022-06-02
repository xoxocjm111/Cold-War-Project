from termcolor import colored
import os
import webbrowser
import textwrap
import time

url = 'https://github.com/xoxocjm111/Cold-War-Project'
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
   os.system('python coldwar.py')

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
print(colored('[2] The Cuban Missile Crisis', 'red'))
print('')
print(colored('[3] The Bay of Pigs', 'blue'))
print('')
print(colored('[4] NATO', 'red'))
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
      print(textwrap.fill((colored("""During the Cuban Missile Crisis of October 1962, U.S. 
                                      and  Soviet leaders were tense political and military for 13 days over the stationing of Soviet nuclear-armed missiles in Cuba, just 90 miles from the U.S.
                                      coast. Engaged in a conflict. Tension build tramendicily over the next few days and citizens were expecting the worst.
                                      They practiced nuclear bombing drills and frightened everyone in the U.S. 
                                      It took the U.S a few days to then settle the tension by moving their nuclear missiles from Turkey, back to the U.S.""", 'blue'))))
      print('')
      u_i = input(colored('[Y,N]Continue?: ', 'blue')).lower
      if u_i == 'y' or 'Y':
         os.system('python coldwar.py')
      else:
         os.system('cls')
         exit()
   elif user_input == 3:
         os.system('cls')
         print(textwrap.fill((colored("""In 1959, Fidel Castro came to power in an armed uprising that defeated Cuban dictator Fulgencio Batista. 
                                         The US government did not trust Castro and did not trust its relationship with Soviet leader Nikita Khrushchev. 
                                         Prior to his inauguration, John F. Kennedy was briefed on a plan by the Central Intelligence Agency (CIA) developed during the Eisenhower administration to train Cuban asylum seekers to invade their hometown.
                                         The plan called for Cuban people and elements of the Cuban army to support the invasion. The ultimate goal was to overthrow  Castro and establish a non-communist government friendly to the United States.".""", 'blue'))))
   elif user_input == 4:
      os.system('cls')
      print(textwrap.fill(colored("""The North Atlantic Treaty Organization was established in 1949 by the United States, Canada, and several Western European countries to provide collective security to the Soviet Union. 
                                     NATO was the first peacetime military alliance formed by the United States  outside  the Western Hemisphere.""", 'blue')))
   elif user_input == 5:
      os.system('cls')
      print('')
      print(colored(about_me, 'green'))
   else:
      exit_timer()
   print('')
   u_i = input(colored('[Y,N]Continue?: ', 'blue'))
   if u_i == 'y' or 'Y':
      os.system('python coldwar.py')
   else:
      os.system('cls')
      exit()
   
   
#indents to make it 100 again just cuz lol :3
