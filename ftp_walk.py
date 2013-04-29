# -*- coding: UTF-8 -*-
from ftplib import FTP
import ftplib
import os
import sys
import re
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure
import chardet

filedict={}
dirlist=[]
filetotal=[]
def main():
    global dirlist
    global filetotal
    global filedict

##    c=Connection()
##  
##    try :
##            c= Connection('localhost',27017)
##            print " Connected successfully! "
##    except ConnectionFailure, e:
##            sys.stderr.write("Could not connect to MongoDB: %s " % e)
##            sys.exit(1)

    tname="张泳"        
    FTPIP= "10.66.28.222"
    FTPPORT= 2007
    USERNAME="zhangydownload"
    USERPWD="123456"
    
    ftp = FTP()
    ftp.connect(FTPIP,FTPPORT)
    ftp.login(USERNAME,USERPWD)
    print len(dirlist)
    g_dir=[]
##  获取根目录及其文件
    ftp.retrlines('MLSD', g_dir.append)
    for entry in g_dir:
        print len(dirlist)
     
        if entry[entry.find(" ")]!="/":
            if entry[5]=="d":
                dirlist.append(entry[entry.find(" ")+1:])
            elif entry[5]=="f":
                filetotal.append(entry[entry.find(" ")+1:])
    print len(filetotal)
    while len(dirlist)!=0:
   
##      下层总目录变量
      
        new_dir=[]
##        print len(dirlist)
        for td in dirlist: 
                ftp.cwd(td)
                new_file_temp=[]
##              相对目录  
                new_dir_re=[]
##              提取转换后的绝对目录
                new_dir_ab=[]                
##              获取相对目录
                ftp.retrlines('MLSD', new_dir_re.append)
                
                for entry in new_dir_re:
                 
                    if entry[entry.find(" ")]!="/":
                        if entry[5]=="d":
                            
                            new_dir.append(td+"/"+entry[entry.find(" ")+1:])
                        elif entry[5]=="f":
                            
                            filetotal.append(entry[entry.find(" ")+1:])
                            new_file_temp.append(entry[entry.find(" ")+1:])
                            filedict[entry[entry.find(" ")+1:]]=td
                print "子总文件数--------："
                print len(new_file_temp)
                ftp.cwd("/")    
        print "当前总文件数--------："
        print len(filetotal)
        dirlist=new_dir
    dbh=c["search"]
    ff = open("ftp1.txt", "w")
##
    for f in filetotal:
        ff.write(f+"\n")
    ff.close

        
main()

