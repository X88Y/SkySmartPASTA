import getpass
UserName = '\\' + getpass.getuser()
dir_ssmart_data = "C:\\Users"+UserName+"\\AppData\\Local\\sky_logg_pass.txt"
login = input('Напишите ваш телефон/почту\n>')
password = input('Напишите ваш пароль\n>')


with open(dir_ssmart_data, "w", encoding='utf_8') as ssmartdata:
    auth_token = ssmartdata.write(login+'\n'+password)