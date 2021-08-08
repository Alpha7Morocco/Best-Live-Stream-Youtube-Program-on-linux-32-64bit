#for command

import os
from N4Tools import Design

#open window stream live
import tkinter as live
LiveStream = live.Tk()

LiveStream.title("Youtube StreamLive")
LiveStream.config(bg="white")
LiveStream.geometry('700x650')

#LiveStream.resizable("0,0")
# labels    title
labelWelcome=live.Label(LiveStream ,text=" Welcome To  streamLive Youtube",bg="white" ,fg="red", font=("foco",16))
labelWelcome.grid(row=0 , column=1, padx=5,pady=5, sticky="s")
#-------------------------------------------------------------------------
###  label and textbox variables VBR 
#label

labelVBR=live.Label(LiveStream ,text="Enter VBR : ",bg="red" ,fg="green", font=("foco",10))
labelVBR.grid(row=1 , column=0, padx=5,pady=5,sticky="w")
#textbox VBR

txtVBR=live.Text(LiveStream ,bg="green", width=30 , font=("foco",10) )
txtVBR["height"]=1
txtVBR.insert(1.1,"'VBR like : 1500k'")
txtVBR.grid(row=1,column=1, padx=5, pady=5,sticky="n" )

#funcions VBR

strVBR=live.StringVar(value=" ....................... ")

def VBR():
    strENTER=txtVBR.get("1.0","end")
    strVBR.set(  strENTER  + " Saved " )


lblVBRDone=live.Label(LiveStream, textvariable=strVBR , bg="blue" ,fg="white" )
lblVBRDone.grid(row=2, column=1, padx=10,pady=5 )

#buttom VBR
ButVBR=live.Button(LiveStream, text="Save" , font=("foco",10),command=VBR )
ButVBR.grid(row=1, column=2,padx=10,pady=5)

#------------------------------------------------------------------------
# textbox variables FPS

labelFPS=live.Label(LiveStream ,text="Enter FPS  : ",bg="red" ,fg="green", font=("foco",10))
labelFPS.grid(row=3 , column=0, padx=5,pady=5,sticky="w")

#textbox FPS
txtFPS=live.Text(LiveStream ,bg="green", width=30 , font=("foco",10) )
txtFPS["height"]=1
txtFPS.insert(1.1,"'FPS like : 24'")
txtFPS.grid(row=3,column=1, padx=5, pady=5,sticky="n" )

#funcions FPS

strFPS=live.StringVar(value=" ....................... ")

def FPS():
    strENTER=txtFPS.get("1.0","end")
    strFPS.set(  strENTER  + " Saved " )


lblFPSDone=live.Label(LiveStream, textvariable=strFPS , bg="blue" ,fg="white" )
lblFPSDone.grid(row=4, column=1, padx=10,pady=5 )
#buttom FPS
ButFPS=live.Button(LiveStream, text="Save" , font=("foco",10),command=FPS)
ButFPS.grid(row=3, column=2,padx=10,pady=5)


#---------------------------------------------------------------------
# textbox variables KEY

labelFPS=live.Label(LiveStream ,text="Enter KEY  : ",bg="red" ,fg="green", font=("foco",10))
labelFPS.grid(row=5 , column=0, padx=5,pady=5,sticky="w")


#textbox KEY
txtKEY=live.Text(LiveStream ,bg="green", width=30 , font=("foco",10) )
txtKEY["height"]=1
txtKEY.insert(1.1,"'KEY'")
txtKEY.grid(row=5,column=1, padx=5, pady=5,sticky="n" )

#funcions KEY

strKEY=live.StringVar(value=" ....................... ")

def KEY():
    strENTER=txtKEY.get("1.0","end")
    strKEY.set(  strENTER  + " Saved " )


lblKEYDone=live.Label(LiveStream, textvariable=strKEY , bg="blue" ,fg="white" )
lblKEYDone.grid(row=6, column=1, padx=10,pady=5 )
#buttom KEY
ButKEY=live.Button(LiveStream, text="Save" , font=("foco",10),command=KEY)
ButKEY.grid(row=5, column=2,padx=10,pady=5)
#----------------------------------------------------------------------
# textbox variables QUAL

labelFPS=live.Label(LiveStream ,text="Enter QUAL  : ",bg="red" ,fg="green", font=("foco",10))
labelFPS.grid(row=7 , column=0, padx=5,pady=5,sticky="w")


#textbox QUAL
txtQUAL=live.Text(LiveStream ,bg="green", width=30 , font=("foco",10) )
txtQUAL["height"]=1
txtQUAL.insert(1.1,"'medium'")
txtQUAL.grid(row=7,column=1, padx=5, pady=5,sticky="n" )

#funcions QUAL

strQUAL=live.StringVar(value=" ....................... ")

def QUAL():
    strENTER=txtQUAL.get("1.0","end")
    strQUAL.set(  strENTER  + " Saved " )


lblKEYDone=live.Label(LiveStream, textvariable=strQUAL , bg="blue" ,fg="white" )
lblKEYDone.grid(row=8, column=1, padx=10,pady=5 )

#buttom QUAL
ButQUAL=live.Button(LiveStream, text="Save" , font=("foco",10),command=QUAL)
ButQUAL.grid(row=7, column=2,padx=10,pady=5)


# textbox variables SOURCE

labelFPS=live.Label(LiveStream ,text="Enter SOURCE  : ",bg="red" ,fg="green", font=("foco",10))
labelFPS.grid(row=9 , column=0, padx=5,pady=5,sticky="w")


#textbox SOURCE
txtSOURCE=live.Text(LiveStream , width=30 ,bg="green", font=("foco",10) )
txtSOURCE["height"]=1
txtSOURCE.insert(1.1,"'File  /home/../*.mp4'")
txtSOURCE.grid(row=9,column=1, padx=5, pady=5,sticky="n" )

#funcions SOURCE

strSOURCE=live.StringVar(value=".............")

def SOURCE():
    strName=txtSOURCE.get("1.0","end")
    strSOURCE.set(strName + "Saved")


lblSOURCEDone=live.Label(LiveStream, textvariable=strSOURCE , bg="blue" ,fg="white" )
lblSOURCEDone.grid(row=10, column=1, padx=10,pady=5 )


#buttom SOURCE
ButSOURCE=live.Button(LiveStream, text="Save" , font=("foco",10),command=SOURCE)
ButSOURCE.grid(row=9, column=2,padx=10,pady=5)

#---------------------------------------------------------------------
# textbox variables YOUTUBE URL

labelFPS=live.Label(LiveStream ,text="Enter YOUTUBE URL  : ",bg="red" ,fg="green", font=("foco",10))
labelFPS.grid(row=11 , column=0, padx=5,pady=5,sticky="w")


#textbox YOUTUBE URL
txtURL=live.Text(LiveStream , width=30 ,bg="green", font=("foco",10) )
txtURL["height"]=1
txtURL.insert(1.1,"'rtmp://a.rtmp.youtube.com/live2'")
txtURL.grid(row=11,column=1, padx=5, pady=5,sticky="n" )

#funcions YOUTUBE_URL

strwel=live.StringVar(value="............")

def YOUTUBE_URL():
    strName=txtURL.get("1.0","end")
    strwel.set(strName + "Saved")


lblURLDone=live.Label(LiveStream, textvariable=strwel , bg="blue" ,fg="white" )
lblURLDone.grid(row=12, column=1, padx=10,pady=5 )


#buttom YOUTUBE URL
ButURL=live.Button(LiveStream, text="Save" , font=("foco",10), command=YOUTUBE_URL)
ButURL.grid(row=11, column=2,padx=10,pady=5)



















#! /bin/bash
#

# Diffusion youtube avec ffmpeg

# Configurer youtube avec une résolution 720p. La vidéo n'est pas scalée.

#VBR="1500k"                                    # Bitrate de la vidéo en sortie
#FPS="24"                                       # FPS de la vidéo en sortie
#QUAL="medium"                                  # Preset de qualité FFMPEG
#YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2"  # URL de base RTMP youtube


#SOURCE="/home/oussama/Music/mohamad/عُد إلى الله ولو أذنبت - أجمل خطبة تحفيزية جديدة للداعية _ محمود الحسنات 2020.mp4"              # Source UDP (voir les annonces SAP)
#KEY="a9wa-z59v-jyfs-umpy-a49y"                                     # Clé à récupérer sur l'event youtube

def nano():
    
    a=txtSOURCE.get("1.0","end")
    b=txtQUAL.get("1.0","end")
    c=txtKEY.get("1.0","end")
    d=txtFPS.get("1.0","end")
    e=txtVBR.get("1.0","end")
    f=txtURL.get("1.0","end")
    A='SOURCE='+a 
    B='QUAL='+b
    C='KEY='+c
    D='FPS='+d
    E='VBR='+e
    F='YOUTUBE_URL='+f
    
    
    
    
    
    
    
    text_file = open("MoodDiary.sh", "w")
    L = [A,B,C,D,E,F]
    text_file.writelines( L ) 
     
    text_file.write(str(         
'ffmpeg \
    -i  "$SOURCE" -deinterlace \
    -vcodec libx264 -pix_fmt yuv420p -preset $QUAL -r $FPS -g $(($FPS * 2)) -b:v $VBR \
    -acodec libmp3lame -ar 44100 -threads 6 -qscale 3 -b:a 712000 -bufsize 512k \
    -f flv "$YOUTUBE_URL/$KEY"'
    ))
    
    Error = False
    try:
        import Cython
    except:
        Error = True
       
    msg = '[$LGREEN]# Done...[$/]'
    if Error:msg = '[$LRED]# Error...[$/]'
    print(Design.Color().reader(msg))


    
    
def run()  :
       
    
    #text_file.write(str(B)) 
    
    
    
    #text_file.write(str(A))
    #text_file.close()
    command= ['sh MoodDiary.sh ']
    #os.chdir(Desktop/Easy-Work)
    for i in command:
        os.system(i) 
    

    
    
    Error = False
    try:
        import Cython
    except:
        Error = True
       
    msg = '[$LGREEN]# Done...[$/]'
    if Error:msg = '[$LRED]# Error...[$/]'
    print(Design.Color().reader(msg))



    









#commant= ls YOUTUBE_URL  >  .py
butstart=live.Button(LiveStream, text="Save All" , command=nano )
butstart.grid(row=13,column=2,padx=5,pady=5, sticky="n")


butstart=live.Button(LiveStream, text="Start" , command=run )
butstart.grid(row=14,column=1,padx=5,pady=5, sticky="n")







#buttom exit
butexit=live.Button(LiveStream, text="Exit" , command=LiveStream.destroy )
butexit.grid(row=13,column=1,padx=5,pady=5, sticky="n")

LiveStream.mainloop()