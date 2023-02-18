import requests,re,rich,sys,os,json,time,datetime
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
from datetime import datetime
ses = requests.Session()
url = []

sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun)
jam = now.hour
menit = now.minute
detik = now.second
hari1 = now.strftime("%A")
date = '\nComment Created In\n     • '+str(hari1)+', '+str(tanggal)+'\n     • Jam '+str(jam)+' : '+str(menit)+' : '+str(detik)


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

def mulai(i,pesan):
	cook = open('.cookie.txt','r').read()
	took = open('.token.txt','r').read()
	link = url
	try:
		ok = ses.post(f'https://graph.facebook.com/{link}/comments/?&message={pesan}{date}&access_token={took}',cookies={'cookie':cook}).text
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
	ids = input(f"{x} [ {h}• {x}] Input Url : ")
	if 'post' in ids:
		url5 = ids.split('/')[5]
		url.append(url5)

	elif 'photo.php' in ids:
		url5 = ids.split('/')[3].split('=')[1].replace('&id','')
		url.append(url5)

	elif 'story.php' in ids:
		url5 = ids.split('/')[3].split('=')[1].replace('&id','')
		url.append(url5)

	elif 'fb://photo' in ids:
		url5 = ids.split('/')[3].split('?')[0]
		url.append(url5)

	elif 'videos' in ids:
		url5 = ids.split('/')[5]
		url.append(url5)

	elif 'groups' in ids:
		tok = ids.split('/')[4]
		tok1 = ids.split('/')[6]
		url5 = tok+'_'+tok1
		url.append(url5)
	else:
		print(f"{x} [ {m}• {x}] Maaf Link Yang Anda Masukan Belum Terdaftar")
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
	jum = int(input(f"{x} [ {h}• {x}] Input Jumlah Comments : "))
	pesan = input(f"{x} [ {h}• {x}] Input Text Comments : ")
	for i in range(jum):
		mulai(i,pesan)
		i+=1

if __name__=='__main__':
	gas()