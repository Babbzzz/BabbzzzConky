#!/usr/bin/python

def get_mail_password():
	encoded_pwd = 'YOUR EMAIL PASS IN BASE64'
	return encoded_pwd.decode('base64')

def get_mail_user():
	encoded_usr = 'YOUR EMAIL IN BASE64 (with @gmail...)'
	return encoded_usr.decode('base64')

def get_user_name():
	encoded_name = 'YOUR USER EMAIL IN BASE64 (without @gmail..)'
	return encoded_name.decode('base64')	
