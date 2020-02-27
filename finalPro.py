class CertiManipulation:
    def __init__(self, window):
        self.window = window
        self.window.title("A simple GUI")
        self.window.title("CERTIFICATE MAKER")

        #self.window.geometry('512x512')
        #self.window.resizable(0,0)
        self.pic = PhotoImage('icon.png')
        #self.window.call('wm', 'iconphoto', self.window._w, PhotoImage(file='icon.png'))    
        
        self.AddCertiLabel = Label(self.window , text = "Add Certificate ---" , height = 2 , width = 25).grid(column = 0 , row = 0)
        self.AddCertiTemp = Button(self.window , text= "Browse Certificate Template"  , height = 2 , width = 25 , command = self.OpenCerti).grid(column = 1 , row = 0)
        self.AddImgLabel1 = Label(self.window , text = "Add Image 1 ---" , height = 2 , width = 25 ).grid(column = 0 , row = 2)
        self.AddImage1 = Button(self.window , text= "Browse Image 1 "  , height = 2 , width = 25, command = self.OpenImage1 ).grid(column = 1 , row = 2)
        self.AddImgLabel2 = Label(self.window , text = "Add Image 2 ---", height = 2 , width = 25 ).grid(column = 0 , row = 4)
        self.AddImage2 = Button(self.window , text= "Browse Image 2"  , height = 2 , width = 25, command = self.OpenImage2 ).grid(column = 1 , row = 4)
        

        self.stud = StringVar()
        self.tech1 = StringVar()
        self.tech2 = StringVar()
        self.des1 = StringVar()
        self.des2 = StringVar()
        
        
        
        self.NameOfStudLabel = Label(self.window , text = "Name Of Student ---" , height = 2 , width = 25 ).grid(column = 0 , row = 6)
        self.NameOfStudEntry = Entry(self.window,textvariable=self.stud).grid(column = 1 , row = 6)
        self.NameOfTeacherLabel1 = Label(self.window , text = "Name Of Teacher 1 ---" , height = 2 , width = 25 ).grid(column = 0 , row = 8)
        self.NameOfTeacherEntry1 = Entry(self.window , textvariable = self.tech1  ).grid(column = 1 , row = 8)
        self.NameOfTeacherLabel2 = Label(self.window , text = "Name Of Teacher 2 ---" , height = 2 , width = 25 ).grid(column = 0 , row = 10)
        self.NameOfTeacherEntry2 = Entry(self.window , textvariable = self.tech2  ).grid(column = 1 , row = 10)
        self.DesignationOfTeacherLabel1 = Label(self.window , text = "Designation Of Teacher 1 ---" , height = 2 , width = 25 ).grid(column = 0 , row = 12)
        self.DesignationOfTeacherEntry1 = Entry(self.window , textvariable = self.des1  ).grid(column = 1 , row = 12)
        self.DesignationOfTeacherLabel2 = self.AddCertiLabel = Label(self.window , text = "Designation Of Teacher 2 ---" , height = 2 , width = 25 ).grid(column = 0 , row = 14)
        self.DesignationOfTeacherEntry2 = Entry(self.window , textvariable = self.des2  ).grid(column = 1 , row = 14)
        
        self.Update = Button(self.window , text="Updation"  , height = 2 , width = 25 ,command=self.Updation).grid(column =1 , row = 16)
        
        self.Exit = Button(self.window , text="Exit"  , height = 2 , width = 25 ,command=self.window.destroy).grid(column =1 , row = 18)
    
    def BrowseFile(self):
        self.filename = filedialog.askopenfilename()
        return self.filename
    def OpenCerti(self):
        self.Certificate = cv2.imread(self.BrowseFile())
        self.label = Label(self.window, text = "")
        self.label.grid(column = 0 , row = 1)
        self.label.configure(text = "Image Added")
        #cv2.imshow('Certificate',self.Certificate)
    def OpenImage1(self):
        self.Image1 = cv2.imread(self.BrowseFile())
        self.label = Label(self.window, text = "")
        self.label.grid(column = 0 , row = 3)
        self.label.configure(text = "Image Added")
        #cv2.imshow('Image 1',self.Image1)
    def OpenImage2(self):
        self.Image2 = cv2.imread(self.BrowseFile())
        self.label = Label(self.window, text = "")
        self.label.grid(column = 0 , row = 5)
        self.label.configure(text = "Image Added")
        #cv2.imshow('Image 2',self.Image2)
    def PutText(self , img , text , pos , scale , thick):
        cv2.putText(img,text=text,org=pos, fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= scale,color=(0,0,0),thickness=thick,lineType=cv2.LINE_AA)
    def Updation(self):
        
        self.img1adjustX = 0
        self.img1adjustY = 0
        self.img2adjustX = 0
        self.img2adjustY = 0
        
        print("HEllo")
        print(self.NameOfStudEntry)
        #print(self.x)
        print(self.stud.get())
        
        #self.stud.get()
        #self.tech1.get()
        #self.des1.get()
        #self.tech2.get()
        #self.des2.get()
        
        cv2.putText(self.Certificate,text='',org=(340,288), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= 1,color=(0,0,0),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(self.Certificate,text='Teacher 1',org=(210,528), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= 0.5 , color=(0,0,0),thickness=1,lineType=cv2.LINE_AA)
        cv2.putText(self.Certificate,text='Designation 1',org=(210,553), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= 0.5 , color=(0,0,0),thickness=1,lineType=cv2.LINE_AA)
        cv2.putText(self.Certificate,text='Teacher 2',org=(570,528), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= 0.5 , color=(0,0,0),thickness=1,lineType=cv2.LINE_AA)
        cv2.putText(self.Certificate,text='Designation 2',org=(570,553), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= 0.5,color=(0,0,0),thickness=1,lineType=cv2.LINE_AA)
        
        
        self.Image1 = cv2.resize(self.Image1,(150,100)) # 0.1 -> resize ratio
        self.Image2 = cv2.resize(self.Image2,(150,100))
        
        
        #self.PutText(self.Certificate,"         Stud",(340,288),1,2)
        #self.PutText(self.Certificate,self.NameOFTeacherEntry1,(210,528),0.5,1)
        #self.PutText(self.Certificate,self.DesignationOfTeacherEntry1,(210,553),0.5,1)
        #self.PutText(self.Certificate,self.NameOFTeacherEntry2,(570,528),0.5,1)
        #self.PutText(self.Certificate,self.DesignationOfTeacherEntry2,570,553,0.5,1)
        self.Certificate[self.Certificate.shape[0]-self.Image1.shape[0]-115+self.img1adjustX:self.Certificate.shape[0]-115+self.img1adjustX,self.Certificate.shape[1]-self.Image1.shape[1]-450+self.img1adjustY:self.Certificate.shape[1]-450+self.img1adjustY] = self.Image1
        self.Certificate[self.Certificate.shape[0]-self.Image2.shape[0]-115+self.img2adjustX:self.Certificate.shape[0]-115+self.img2adjustX,self.Certificate.shape[1]-self.Image2.shape[1]-90+self.img2adjustY:self.Certificate.shape[1]-90+self.img2adjustY] = self.Image2
        
        cv2.imshow('Certificate',self.Certificate)
        cv2.imwrite('cert2.png',self.Certificate)

import os
def send_an_email(recipient,filename):
    
    fromaddr = "gshrey4@gmail.com"
    toaddr = recipient
    print(toaddr)
    filename='C:\\Users\\Shrey\\Downloads\\CertiMaker-master\\' + filename
    print(filename)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "certificate"
    body = "e-cerificate"

    msg.attach(MIMEText(body, 'plain'))
    print(filename)
    # filename="PrescriptionRaWhJNwByKR73v1V6mNpT3GDQpJ2sa1921012020.pdf"
    attachment = open(filename,'rb').read()
    image=MIMEImage(attachment,'png')
    msg.attach(image)
    

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Iostream1!")
#     print(typr)
#     print(msg)
    text = msg.as_string()
    
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


class Names():
    def __init__ (self , window):
        self.window = window
        self.window.title("A simple GUI")
        self.window.title("CERTIFICATE MAKER")
        
        #self.window.geometry('512x512')
        #self.window.resizable(0,0)
        
        self.AddCertiLabel = Label(self.window , text = "Add Certificate ---" , height = 2 , width = 25).grid(column = 0 , row = 0)
        self.AddCertiTemp = Button(self.window , text= "Browse Certificate Template"  , height = 2 , width = 25 , command = self.OpenCerti).grid(column = 1 , row = 0)
        self.AddFileLabel = Label(self.window , text = "Add File With Data ---" , height = 2 , width = 25 ).grid(column = 0 , row = 2)
        #self.AddFile = Button(self.window , text= "Browse File "  , height = 2 , width = 25, command = self.OpenFile ).grid(column = 1 , row = 2)
        
        self.Send = Button(self.window , text="Send Certificates"  , height = 2 , width = 25 ,command=self.sendCerti).grid(column =1 , row = 3)
        
        self.Exit = Button(self.window , text="Exit"  , height = 2 , width = 25 ,command=self.window.destroy).grid(column =1 , row = 4)
        
    def BrowseFile(self):
        self.filename = filedialog.askopenfilename()
        return self.filename
    
    def OpenCerti(self):
        self.Certificate = cv2.imread(self.BrowseFile())
        self.label = Label(self.window, text = "")
        self.label.grid(column = 0 , row = 1)
        self.label.configure(text = "Image Added")
        cv2.imshow('Certificate',self.Certificate)
    def OpenFile(self):
        self.file = self.BrowseFile()
        self.wb = xl.load_workbook(self.file)
        self.sheet = self.wb.active
        self.NameArr = []
        self.EmailArr = []
        self.col = 0
        self.name_col = 0
        self.email_col = 0
        for name in self.sheet.iter_cols(min_row = 1 , max_row = 1 , values_only = True ):
            self.col += 1
            if name == ('Name',) :
                self.name_col = self.col
            if name == ('Email Address',):
                self.email_col = self.col

        for value in self.sheet.iter_rows(min_row = 2 , min_col = self.name_col , max_col = self.name_col , values_only = True):
            self.NameArr.append(value[0])
        for value in self.sheet.iter_rows(min_row = 2 , min_col = self.email_col , max_col = self.email_col , values_only = True):
            self.EmailArr.append(value[0])
        return self.NameArr , self.EmailArr
            
    def sendCerti(self):
        self.NameArr , self.EmailArr = self.OpenFile()
        #self.PutText(self.Certificate,"         Stud",(340,288),1,2)
        self.length = len(self.NameArr)
#         self.Certitemp = self.Certificate
        for i in range(self.length):
            cv2.imwrite('cert3.png',self.Certificate)
            self.Certitemp = cv2.imread('C:\\Users\\Shrey\\Downloads\\CertiMaker-master\\cert3.png')
            cv2.putText(self.Certitemp,text=self.NameArr[i],org=(340,288), fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale= 1,color=(0,0,0),thickness=2,lineType=cv2.LINE_AA)
            cv2.imwrite('Hackathon2020.png',self.Certitemp)
            send_an_email(self.EmailArr[i],'Hackathon2020.png')
    
        
def AddingNames():
    window3 = Tk()
    obj2 = Names(window3)
    window3.mainloop()
        
def AddCertWin():
    window2 = Tk()
    obj = CertiManipulation(window2)
    window2.mainloop()

window = Tk()

window.title("CERTIFICATE MAKER")

window.geometry('512x512')
window.resizable(0,0)
pic = PhotoImage('icon.png')
window.call('wm', 'iconphoto', window._w, PhotoImage(file='icon.png'))

WelcomeText = Label(window,text="Welcome",font=("ArialBold",50)).pack()

AddNames = Button(window , text="Add Names" , height = 2 , width = 30 , command = AddingNames).pack()
AddCerti = Button(window , text="Add Certificate Template" , height = 2 , width = 30 , command = AddCertWin).pack()
Exit = Button(window , text="Exit" , height = 2 , width = 30 ,command=window.destroy).pack()

window.mainloop()
