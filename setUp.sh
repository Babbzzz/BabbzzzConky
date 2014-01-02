#! /bin/bash

CONKY_DIR="$HOME/temp"
CONKYRC_PATH="$CONKY_DIR/.conkyrc"
USERPWD_PATH="$CONKY_DIR/.conky/scripts/mail/userpwd.py"

width=800
height=600
email='myemail@mail.com'
user='myemail'
b64_email='myemail@mail.com'
b64_user='myemail'
b64_pswd=''
os_name=''
os_version=''

function get_dimensions_info(){
	read -p "Width: " width
	read -p "Heigth: " height
}

function get_email_info (){
	read -p "E-mail (eg: myemail@mail.com): " email
	user=$(echo $email | cut -d '@' -f 1)
	read -s -p "E-mail password: " pswd
	b64_email=$(echo -n $email | base64)
	b64_user=$(echo -n $user | base64)
	b64_pswd=$(echo -n $pswd | base64)
}

function get_os_info (){
	read -p "Operative System (eg: Ubuntu, Mint): " os_name
	read "Version: " os_version
}

cp -f ./.conkyrc $CONKYRC_PATH
cp -fr ./.conky "$CONKY_DIR/"

get_dimensions_info
get_email_info
get_os_info
sed -i "s/'YOUR EMAIL DOMAIN HERE'/$user/" $CONKYRC_PATH
sed -i "s/minimum_size.*/minimum_size $width $height/" $CONKYRC_PATH
sed -i "s/minimum_size.*/minimum_size $width $height/" $CONKYRC_PATH
sed -i "s/'YOUR OS'/$os_name/" $CONKYRC_PATH
sed -i "s/'YOUR OS VERSION'/$os_version/" $CONKYRC_PATH
sed -i "s/YOUR EMAIL PASS IN BASE64/$b64_pswd/" $USERPWD_PATH
sed -i "s/YOUR EMAIL IN BASE64 (with @gmail...)/$b64_email/" $USERPWD_PATH
sed -i "s/YOUR USER EMAIL IN BASE64 (without @gmail..)/$b64_user/" $USERPWD_PATH

