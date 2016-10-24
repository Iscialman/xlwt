from ftplib import FTP
def ftpconnect() :
    ftp_server  = '10.25.7.121'
    server_port = 21
    ftp_user    = 'public'
    user_passwd = 'Wgsdd522'
    ftp         = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_server,21)
    ftp.login(ftp_user,user_passwd)
    return ftp
def downloadfile(filename) :
    remotepath  = "dnt/wx/"+filename
    ftp         = ftpconnect()
    print ftp.getwelcome()
    bufsize     = 1024
    localpath   = 'D:\\ribao\\'+filename
    fp          = open(localpath,'wb')
    ftp.retrbinary('RETR ' + remotepath , fp.write , bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

def uploadfile(path) :
    remotepath  = path
    ftp         = ftpconnetct()
    bufsize     = 1024
    localpath   = r'D:\WX'
    fp          = open(localpath,'rb')
    ftp.storbinary('STOR ' + remorepath , fp , bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()
downloadfile("proc.txt")
