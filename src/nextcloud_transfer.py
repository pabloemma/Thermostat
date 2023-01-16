'''simple class to push and put files to our nextcloud server at home

In order to use keyring, first create an entry (use python3 keyring)
for nextcloud it would be as follows:
    keyring.set_password("nextcloud", "pabloemma", "the password for nextcloud")
    on linux you need to install kwallet with sudo apt install kwallet-manager and kwalletcli
    that probably requires dbus-python, which gets installed with pip3
    However dbus does not work with one of my raspi so it needs to have a
    password in a file. This file should be named in the init 

'''

import sys
import requests as rq
import subprocess
import os
from pathlib import Path

import importlib.util # to check if package is installed
import keyring

import sys




class mytransfer(object):

    def __init__(self,
                user = 'pabloemma',
                passfile = '/private/pass/mypass.txt',
                url = 'https://casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/'):

        # create the proper main path
        # determine the login dir, the passfile is then in ~/private/pass
        self.passfile = str(Path.home())+passfile 



        self.passwd = passwd = self.get_login_info(user)
        self.user = user
        self.creds = user+':'+passwd
        self.nextcloud_url = url
     

    def get_login_info(self,user):
        '''we are using the keyring library to deal with passwords, see
        https://pypi.org/project/keyring/
        '''

        # check if keyring s installed



        package_name = 'keyring'

        spec = importlib.util.find_spec(package_name)
        if spec is None:
            print(package_name +" is not installed")
            print("first intall it and try again, exiting")
            sys.exit(0)

        # lets get the password
        try:
            password = keyring.get_password('nextcloud', user)
            
        except:
            print("cannot find user",user)
            print("trying to find pass file")
            try:
                user, password = self.get_creds()
            except:
                print('can\'t do the credentials')
            
            
                sys.exit(0)

        return password


    def upload_file(self,file_path_in=None, upload_dir=None):
    
        if file_path_in is None or not os.path.exists(file_path_in):
            print("File '{}' cant be uploaded".format(file_path_in))
            return

        if upload_dir is None:
            print("upload_dir '{}' not found".format(upload_dir))
            return
           
        url = self.nextcloud_url+upload_dir+'/'
        command = 'curl --user '+self.creds+' -T '+file_path_in + ' '+url
    
        subprocess.Popen(command,shell=True)

        
    def pull_file(self,nextcloud_dir,nextcloud_filename,output_path):
        ''' get the file with the requests'''
        out_file = output_path+'/'+nextcloud_filename
        r = rq.get(self.nextcloud_url+nextcloud_dir+'/'+nextcloud_filename, auth=(self.user,self.passwd))
        

        if r.status_code == 200:
            with open(out_file,'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if(chunk):
                        f.write(chunk)

        f.close()

    def get_creds(self):
        ''' gets credentails from file if keyring does not work, the formta of the file is:
        nextcloud user pwd, where the first is the app which needs a pwd'''
        if not os.path.exists(self.passfile):
            print("File '{}' cant be found".format(self.passfile))
            sys.exit(0)
            
        else:
            f=open(self.passfile,'r')
            a =  f.readlines()
            b = a[0].split(' ')
            user = b[1]
            password = b[2].strip('\n')
            return user,password





if __name__ == "__main__":  

    nxt = mytransfer()
    nxt.upload_file(file_path_in = '/Users/klein/finnland.pdf',upload_dir= 'Temperature' )
    nxt.pull_file('Temperature','finnland.pdf','/Users/klein/scratch')