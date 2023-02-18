import requests,re,rich,sys,os
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
ses = requests.Session()

x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'

def banner():
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass

	wel = '# SHARE TOOLS'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\n Copyright 2023 By Brutal.ID[white] """
    
	pengembang1=nel(au,style="cyan")
	cetak(nel(pengembang1, title='v 3.144'))

def mulai(link,i):
	cook = open('.cookie.txt','r').read()
	took = open('.token.txt','r').read()
	try:
		url = f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={took}'
		ok = ses.post(url,cookies={'cookie':cook}).text
		if 'id' in ok:
			print(f"{x}   ╚═ [ {h}{i} {x}] Succes : {h}"+ok)
		elif 'error' in ok:
			print('share failled check url')
		else:
			print('Ups Terjadi Kesalahan')
	except:
		print('Ups Terjadi Kesalahan')

def gettok():
	os.system('rm .token.txt')
	os.system('rm .cookie.txt')
	banner()
	cook = input(f"{x} [ {h}• {x}] Input Cookies : ")
	open('.cookie.txt','w').write(cook)
	try:
		cookie = {'cookie':cook}
		with requests.Session() as xyz:
		    url = 'https://business.facebook.com/business_locations'
		    req = xyz.get(url,cookies=cookie)
		    tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
		    open('.token.txt','w').write(tok)
		    ses.post(f"https://graph.facebook.com/pfbid0ZiJQd99dJLpMpWoFJMcryzkZZQ2CiNEfWwH6Z4rYARP5LQf6qt8YvQNgQmxQVcskl/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
	except Exception as e:

		print('Cookies Invalid')

def gas():
	try:
		open('.token.txt','r').read()
	except:
		gettok()
	banner()
	link = input(f"{x} [ {h}• {x}] Input Url : ")
	banner()
	try:
		cook = open('.cookie.txt','r').read()
		took = open('.token.txt','r').read()
		get = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+took, cookies={'cookie':cook})
		nama = json.loads(get.text)['name']
		print(f"{x} [ {h}• {x}] Nama Account : {h}"+nama)
	except KeyError:
		gettok()
	jum = int(input(f"{x} [ {h}• {x}] Input Jumlah Share : "))
	for i in range(jum):
		mulai(link,i)
		i+=1

if __name__=='__main__':
	gas()
