'''simple class to push and put files to our nextcloud server at home
'''

import sys
import requests as rq
import subprocess
import os


import importlib.util # to check if package is installed
import keyring

import sys




class mytransfer(object):

    def __init__(self,
                user = 'pabloemma',
                url = 'https://casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/'):

 
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



if __name__ == "__main__":  

    nxt = mytransfer()
    nxt.upload_file(file_path_in = '/Users/klein/finnland.pdf',upload_dir= 'Temperature' )
    nxt.pull_file('Temperature','finnland.pdf','/Users/klein/scratch')