try:
    from pystyle import *
    from colorama import *  
    import os
    import sys
    import datetime
    import asyncio
    import time

except:
    os.system("pip install pystyle colorama datetime asyncio") # if this doesnt work pip install manually
    
    
    
def setTitle(title: [any]=None):
  os.system("title "+title)

setTitle("[Template] made by 11gn") #just the console title change it to watever u want its also not needed
    
loadingpart = ("""
               
        
╦  ┌─┐┌─┐┌┬┐┬┌┐┌┌─┐  ╔╦╗┌─┐┌┬┐┌─┐┬  ┌─┐┌┬┐┌─┐
║  │ │├─┤ │││││││ ┬   ║ ├┤ │││├─┘│  ├─┤ │ ├┤ 
╩═╝└─┘┴ ┴─┴┘┴┘└┘└─┘   ╩ └─┘┴ ┴┴  ┴─┘┴ ┴ ┴ └─┘
       
        
        
        
               
               
""") # to change these go to https://patorjk.com/software/taag/ and find yours, loading isnt actually needed it just looks cool lol. same wit all the fonts js makes it look cooler lmao

mainpart  = f"""   
 ______               __     __     
/_  __/__ __ _  ___  / /__ _/ /____ 
 / / / -_)  ' \/ _ \/ / _ `/ __/ -_)
/_/  \__/_/_/_/ .__/_/\_,_/\__/\__/ 
             /_/                    

                                
"""

choice = """


"""


option = """

[1] Example 1   [6] Example 6 
[2] Example 2   [7] Example 7
[3] Example 3   [8] Example 8
[4] Example 4   [9] Example 9
[5] Example 5   [10] Discord Server REAL

""" # theres plenty different ways to make multitools but this is my way ! if u wanna create more just try and copy how its done there

#options part has to be there for it to work. u can change the name of it though.



print(Colorate.Horizontal(Colors.blue_to_purple, loadingpart))
time.sleep(3)
os.system('cls')
print(Colorate.Horizontal(Colors.red_to_blue, mainpart))

print(Colorate.Horizontal(Colors.blue_to_red, option)) #colors here
choice = int(input(Colorate.Horizontal(Colors.blue_to_purple,"->  ")))



if choice == 1:
    print("Used Example 1") # u make ur code here delete print and do your code also change example 1 on the mulktitool to wtv u like
elif choice == 2:
    print("Used Example 2") 
elif choice == 3:
    print("Used Example 3") 
elif choice == 4:
    print("Used Example 4")
elif choice == 5:
    print("Used Example 5") 
elif choice == 6:
    print("Used Example 6")
elif choice == 7:
    print("Used Example 7") 
elif choice == 8:
    print("Used Example 8") 
elif choice == 9:
    print("Used Example 9") 
elif choice == 10:
    print(f"{Fore.CYAN} JOIN DISCORD SERVER FOR UPDATES AND SNEAK PEEKS OF UPCOMING TOOLS  https://discord.gg/fWQahEPsJB")
else:
    print(f"{Fore.RED}Invalid choice. Please select a number between 1 and 10. {Fore.YELLOW} Please Restart The Program To Continue")





#YOU CAN CHANGE THE DESIGN OF THE MULTITOOL BTW!!!
