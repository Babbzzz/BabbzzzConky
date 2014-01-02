#!/usr/bin/python
# -*- coding: utf-8 -*-

import imaplib
import os
import userpwd
from email.parser import HeaderParser

arch_notificados = os.getenv("HOME") + '/.conky/scripts/mail/notificados.dat'
osd_notifier = "~/.conky/scripts/OSD-notifier.py"

def filtrarNotificados(mailbox, id_list):
	with open(arch_notificados) as f:
		notificados = f.readlines()
	mails = []
	for nro in id_list:
		result, data = mailbox.fetch(nro, '(BODY.PEEK[HEADER.FIELDS (MESSAGE-ID SUBJECT FROM)])')
		msg = HeaderParser().parsestr(data[0][1])
		mails.append(msg)

		for mail in notificados:
			if (msg['Message-Id'] in mail) and (msg['From'] in mail) and (msg['Subject'] in mail):
				mails.pop()
				break
	return mails

def guardarNotificados(mailbox, mails):
	os.remove(arch_notificados)
	f = open(arch_notificados, "wb")
	for mail in mails:
		f.write (mail['Message-Id'] + " " + mail['From'] + " " + mail['Subject'] + "\n")
	f.close()

def notificar(mails):
	if len(mails)==1:
		sfrom = (mails[0]['From'][:37] + '...') if len(mails[0]['From']) > 40 else mails[0]['From']
		os.system(osd_notifier+" \"Nuevo Mensaje: "+userpwd.get_user_name()+ "\" "+"\"De:\n"+ sfrom +"\nAsunto:\n"+ mails[0]['Subject'] + "\"")
	elif len(mails)>1:
		os.system(osd_notifier+" \"Nuevos Mensajes: "+userpwd.get_user_name()+"\" \""+ str(count) + " nuevos mensajes.\"")


mailbox = imaplib.IMAP4_SSL('imap.gmail.com','993')
mailbox.login(userpwd.get_mail_user(), userpwd.get_mail_password())
mailbox.select()

result, data = mailbox.search(None, 'UnSeen')
ids = data[0]
id_list = ids.split()

mails = filtrarNotificados(mailbox, id_list)
if len(mails)>0:
	guardarNotificados(mailbox, mails)
count = len(id_list)

if count==0:
	print "Ninguno."
elif count==1:
	print str(count)+" nuevo."
else:
	print str(count)+" nuevos."

notificar(mails)
