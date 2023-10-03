from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox 
from urllib import response
import gdown
import requests
import urllib.request
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
from ttkthemes import ThemedTk, ThemedStyle

class botGuiApp:
    def __init__(self,root):
        self.root=root
        #define window icon
        self.root.iconbitmap(r"C:\Users\Adar\Documents\One piece project\\one piece logo.ico")
        
        # root window title and dimension
        self.root.title("One-piece download bot")
        
        #Set geometry (widthxheight)
        self.root.geometry('385x385')
        
        #define background image
        im = Image.open(r"C:\Users\Adar\Documents\One piece project\onepiece.jpg")
        bg = ImageTk.PhotoImage(im) 
        bg_label = tk.Label(self.root, image=bg)
        bg_label.image=bg
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #define input boxes
        self.e=tk.Entry(self.root,width=10,bg='light blue',borderwidth=3)
        self.e.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.e2=tk.Entry(self.root,width=10,bg='light blue',borderwidth=3)
        self.e2.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
        self.pathBox=tk.Entry(self.root,width=30,bg='light blue',borderwidth=3)
        self.pathBox.grid(row=3,column=1,columnspan=3,padx=10,pady=10)
        
        #define text next to input box
        self.labelDirFrom=tk.Label(self.root, text="From episode: ",bg='light blue', font=14)
        self.labelDirFrom.grid(row=0,column=0,padx=0,pady=0)
        self.labelDirTo=tk.Label(self.root, text="To episode: ",background='light blue' ,font=14)
        self.labelDirTo.grid(row=2,column=0,padx=0,pady=0)
        self.labelDirPath=tk.Label(self.root,text="browse: ",background='light blue',font=14)
        self.labelDirPath.grid(row=3,column=0,padx=0,pady=0)
      
        #define buttons
        self.browse_button=tk.Button(self.root,text="browse",background='light blue',command = lambda: browse())
        self.browse_button.grid(row=3,column=4,columnspan=1)
        self.download_button=tk.Button(self.root,text='download',background='light blue',command= lambda: start_download(self))
        self.download_button.grid(row=4,column=1,columnspan=1)
        
        def browse(): #browse folder
            dirname = filedialog.askdirectory()
            if dirname:
                self.pathBox.delete(0, tk.END)  # Clear the input box
                self.pathBox.insert(0, dirname)
        
        #download episodes 
        def start_download(self):
            folder=self.pathBox.get()
            print("this is the folder:" + folder)
            fro=int(self.e.get())
            to=int(self.e2.get())
            temp_url="https://animeisrael.website/watch/fulllink/op/fulllinkop-*.php"
            for i in range (fro,to+1):
                url=temp_url
                url=url.replace('*',str(i))                
                try:
                    response = urllib.request.urlopen(url)
                    page_content=response.read()
                    soup=BeautifulSoup(page_content,'html.parser')
                    iframe=soup.find('iframe')
                    if iframe:
                        video_url=iframe['src']
                        video_response=urllib.request.urlopen(video_url)
                        output=folder+'/'+'episode-'+str(i)+'.mp4'
                        video_url =video_url.replace('preview', 'view')
                        gdown.download(url=video_url, output=output, quiet=False, fuzzy=True,use_cookies=False)
                    else:
                        print('iframe element doesn"t exist')
                except Exception as e:
                    print(f'error: {str(e)}')
            
if __name__ == "__main__":
    root=tk.Tk()
    app=botGuiApp(root)
    root.mainloop()