import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = '.', help_command = None)
# this made me attract 100 gurls at my door 

colorama.init()
token = input("Token : ")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.GREEN}  ██╗    ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
{Fore.GREEN}  ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
{Fore.GREEN}  ██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
{Fore.GREEN}  ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
{Fore.GREEN}  ██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
{Fore.GREEN}  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝
{Fore.GREEN}                       H1 tools           
{Fore.GREEN}                       [1] Mass Dm                                            
''')
 fuck = input(f"{Fore.GREEN}Tool : ")
 if fuck == '1':
  input2 = input(f"{Fore.GREEN}What Do You want me to send? : ")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[EZ] Sent{Fore.WHITE} {input2} To {user}")

client.run(token, bot = False)
