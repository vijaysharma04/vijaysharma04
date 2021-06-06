from tkinter import *
import pytube3

root = Tk()
root.geometry('600x500')
root.title('Yt Downloader')


def Downloader():
    url = pytube3(link.get())
    video = url.streams.first()
    video.download()
    Label(root,text='DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)




link = StringVar()

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 200, y = 60)

link_enter = Entry(root, width = 70,textvariable = link).place(x = 70, y = 90)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=210,y = 150)

root.mainloop()