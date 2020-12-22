import tkinter
from tkinter import *
from tkinter import messagebox
#BASIC FUNCTIONS--------------------------------------------------------------------------------------------
def destroy():
    app.destroy()#exits program

def info():
    messagebox.showinfo('Information','Done by Moleena and Dhrumil \nCopyright Moleena and Dhrumil')#shows info
#NOTES GUI--------------------------------------------------------------------------------------------------
def callnote():
    n=notes1()
    n.callnote1()
class notes1():
    def callnote1(self):
        notes=Tk()#creates a new window
        notes.geometry("650x450")
        notes.resizable(width=False, height=False) 
        notes.title('Notes')
        self.message=Text(notes,)#message box
        self.message.grid(row='0',column='0')
        savebutton=Button(notes,text='SAVE',command=self.sav)#starts the save process
        savebutton.grid(row='1',column='0')
        notes.mainloop()
    def sav(self):
        z=self.message.get(1.0,END)#gets the string
        self.save(z)#redirects to save    
    def save(self,x1):    
        if messagebox.askyesno ('Save','Are you sure you want to save?\nIf old notes file is there it will be replaced ')==True:
            newfile=open('Notes.txt','w')#creates Notes.txt
            newfile.write(x1)#writes data
            messagebox.showinfo('Place','File saved in the same folder as the python file')
        else:
            pass    
        
#MAIN GUI---------------------------------------------------------------------------------------------------
app=Tk()
app.title('Parts of a Computer')
app.geometry('1200x1200')
#app.resizable(width=False, height=False)
#app.resizable(width=FALSE, height=FALSE)
heading=Label(app, text='Parts of a Computer' ,font=('Bookman Old Style', '35', 'bold italic'),fg='dark blue')
heading.grid(row='2',column='20')
ins1=Label(app, text='Click on the radio buttons below the pictures, to get the list of respective parts ' ,font=('Bahnschrift Light', '12', 'bold italic'),fg='brown')
ins1.grid(row='3',column='20')
space=Label(app, text='' ,font=('Arial', '12', 'bold italic'),fg='brown')
space.grid(row='4',column='20')
infoi=PhotoImage(file='photos\info.gif')
info=Button(app, text='INFO',command=info,cursor="hand2",image=infoi,relief='raised')#shows info
info.grid(row='2',column='10')
NOTES=Button(app, text='NOTES',command=callnote,cursor="hand2",relief='raised',bg='  ',fg='white')#shows info
NOTES.grid(row='2',column='15')
n=Label(app, text="Click on Notes to type your own notes",font=('Arial', '12', 'bold italic'))
n.grid(row='4',column='20')
exiti=PhotoImage(file='photos\\close_blue.gif')
exitbutton=Button(app,text='EXIT',command=destroy,cursor="hand2",image=exiti,relief='raised')#exits program
exitbutton.grid(row='2', column='30')
#IMAGES FOR DISPLAY BOX of list box1------------------------------------------------------------------------
vga1=PhotoImage(file='photos\\vga-cable-and-connector.gif')
ps21=PhotoImage(file='photos\\ps2.gif')
usb1=PhotoImage(file='photos\\USB.gif')
ethernet1=PhotoImage(file='photos\\eth.gif')
sp1=PhotoImage(file='photos\\serialport.gif')
lpt1=PhotoImage(file='photos\\lpt.gif')
spl1=PhotoImage(file='photos\\spl.gif')
joy=PhotoImage(file='photos\\joy.gif')
backi=PhotoImage(file='photos\\back.gif')
#Dictionaries of list box 1---------------------------------------------------------------------------------
list1d={0:'PS2',1:'USB',2:'ETHERNET',3:'Serial Port',4:'VGA',5:'LPT',6:'SPL',7:'Joystick Port'}
list1d2={'PS2':'The PS/2 connector is a 6-pin mini-DIN connector used for connecting some keyboards and mice to a PC compatible computer system.\nIts name comes from the IBM Personal System/2 series of personal computers, with which it was introduced in 1987.',
         'USB':'USB, short for Universal Serial Bus, is an industry standard developed in the mid-1990s that defines the cables, connectors and communications protocols used in a bus for\nconnection, communication, and power supply between computers and electronic devices \nUSB was designed to standardize the connection of computer peripherals ',
         'ETHERNET':'Ethernet is a family of computer networking technologies commonly used in Local Area Networks (LANs) and Metropolitan Area Networks (MANs)',
         'Serial Port':'A serial port is a general-purpose interface that can be used for almost any type of device, including modems, mice, and printers ',
         'VGA':'A Video Graphics Array (VGA) connector is a three-row 15-pin DE-15 connector. The 15-pin VGA connector is found on many video cards, computer monitors, and high definition television sets.\nOn laptop computers or other small devices, a mini-VGA port is sometimes used in place of the full-sized VGA connector.\nUsed to connect Monitor and Graphics Card which provides High speed video performance\nAlso known as Accelarated Graphics Port',
         'LPT':'LPT (Line Print Terminal) is the usual designation for a parallel port connection to a printer or other device on a personal computer. ',
         'SPL':'Speakers, Line In, Microphone\nYou can use the line-in connection on your sound card to connect a portable music player, microphone, or other audio input device to your computer.\nMost sound cards have at least one line-out port to connect speakers and a line-in port where you can connect an audio input device.',
         'Joystick Port':'The game port, originally introduced on the Game Control Adapter, is a device port that was found on IBM PC compatible and other computer systems throughout the 1980s and 1990s.\nIt was the traditional connector for joystick input and MIDI devices, until replaced by USB in the 21st century.'}
list1d3={'PS2':ps21,'USB':usb1,'ETHERNET':ethernet1,'Serial Port':sp1,'VGA':vga1,'LPT':lpt1,'SPL':spl1,'Joystick Port':joy}
#IMAGES FOR DISPLAY BOX of list box2------------------------------------------------------------------------
mb=PhotoImage(file='photos\\motherboard.gif')
pro1=PhotoImage(file='photos\\pror1.gif')
r1=PhotoImage(file='photos\\RAM.gif') 
opd=PhotoImage(file='photos\\od.gif')
ps=PhotoImage(file='photos\\PSU.gif')
#Dictionaries of list box 2---------------------------------------------------------------------------------
list2d={0:'Motherboard',1:'Processor',2:'RAM',3:'Optical Drive',4:'Power Supply'}
list2d2={'Motherboard':'A motherboard is the main printed circuit board (PCB) found in general purpose microcomputers and other expandable systems.\nIt holds and allows communication between many of the crucial electronic components of a system, such as the central processing unit (CPU) and memory.\nIt also provides connectors for other peripherals',
         'Processor':'A Processor is the electronic circuitry within a computer that carries out the instructions of a computer program by \nerforming the basic arithmetic, logical, control and input/output (I/O) operations specified by the instructions.',
         'RAM':'Random-access memory (RAM) is a form of computer data storage.\nA random-access memory device allows data items to be accessed (read or written) in almost the same amount of time, \nirrespective of the physical location of data inside the memory.\nIn today\'s technology, RAM takes the form of integrated circuits.',
         'Optical Drive':'In computing, an optical disc drive (ODD) is a disk drive that uses laser light or electromagnetic waves within or near the visible light spectrum\nIt is used for reading or writing data to or from optical discs.',
         'Power Supply':'A power supply unit (PSU) converts mains AC to low-voltage regulated DC power for the internal components of a computer.\nModern personal computers universally use switched-mode power supplies.\nSome power supplies have a manual switch for selecting input voltage, while others automatically adapt to the mains voltage.'} 
list2d3={'Motherboard':mb,'Processor':pro1,'RAM':r1,'Optical Drive':opd,'Power Supply':ps}
#IMAGES FOR DISPLAY BOX of list box3------------------------------------------------------------------------
osd=PhotoImage(file='photos\\osd.gif')
msd=PhotoImage(file='photos\\msd.gif')
fsd=PhotoImage(file='photos\\fsd.gif')
#Dictionaries of list box 3---------------------------------------------------------------------------------
list3d={0:'Optical Storage devices',1:'Magnetic Storage devices',2:'Flash Storage devices'}
list3d2={'Optical Storage devices':'Optical storage devices are any storage methods that use a laser to store and retrieve data from optical media.\nOptical storage media includes CD-ROM, DVD-ROM, DVD-RAM, WORM cartridges, erasable optical cartridges and removable mass storage media, which includes flash drives and removable disk',
         'Magnetic Storage devices':'Magnetic storage or magnetic recording is the storage of data on a magnetised medium.\nMagnetic storage uses different patterns of magnetisation in a magnetisable material to store data and is a form of non-volatile memory.\nThe information is accessed using one or more read/write heads.\nAs of 2013, magnetic storage media, primarily hard disks, are widely used to store computer data as well as audio and video signals.',
         'Flash Storage devices':'Flash memory is an electronic (solid-state) non-volatile computer storage medium that can be electrically erased and reprogrammed.\nThis type contains all Pen drives, SD Cards, Micro SD Cards and SSDs'}
list3d3={'Optical Storage devices':osd,'Magnetic Storage devices':msd,'Flash Storage devices':fsd}
#Secondary MENU FUNCTIONS-----------------------------------------------------------------------------------
class xyz:
    def __init__(self,listx,rld,rld1,rld2):
        self.listx=listx#listbox
        self.rld=rld#dictionary related to listbox
        self.rld1=rld1
        self.rld2=rld2
    def btfdbutton(self,):
        btfd=Button(app,text='GET DATA ABOUT PART',command=self.receive, bg='blue',fg='white')#creates button which on clicking redirects to receive
        btfd.grid(row='40',column='20')
    def receive(self,):
        items = self.listx.curselection()#gets index value of object selected as tuple
        obj=items[0]#selects first value of tuple
        x=display(obj,self.rld,self.rld1,self.rld2)#redirects to class display and also passes the index value of object selected in single form,related dictionary and 2ndrelarted dictionary
        x.display1()
#DISPLAY BOX FUNCTIONS---------------------------------------------------------------------------------------
class display():
        def __init__(self,obj1,rldd,rldd1,rldd2):
            self.obj1=obj1#GET VALUE OF LIST BOX ITEM
            self.rldd=rldd#GETS DICTIONARY OF LIST BOX 
            self.rldd1=rldd1#GETS 2nd DICTIONARY OF LIST BOX
            self.rldd2=rldd2#GETS 3rd DICTIONARY OF LIST BOX
            self.window=''#CREATES A NAMESAKE
        def display1(self,):    
            self.window=Toplevel()#using name sake we create a new window
            self.window.title(self.rldd[self.obj1])
            displaylabel=Label(self.window,text=self.rldd1[self.rldd[self.obj1]])#creates label with getting text from dictionary for respective index value
            displaylabel.grid(row='40',column='20')
            photolabel=Label(self.window, image=self.rldd2[self.rldd[self.obj1]])#creates label with getting image details from dictionary for respective index value
            photolabel.grid(row='40',column='10')
            backbutton=Button(self.window,text='BACK',command=self.back,cursor="hand2",image=backi)#exits program
            backbutton.grid(row='70', column='20')
        def back(self,):
            self.window.destroy()
        
        
#LISTBOX FUNCTIONS------------------------------------------------------------------------------------------
def list1():
    ins2=Label(app, text='Click on the part name on the below list and then click "GET DATA ABOUT PART" button' ,font=('Arial', '9', 'bold italic'),fg='blue')
    ins2.grid(row='30',column='20')
    lb1=Listbox(app,height=8,width=30)#creates listbox
    lb1.insert(0,'PS2')#value in listbox
    lb1.insert(1,'USB')
    lb1.insert(2,'Ethernet')
    lb1.insert(3,'Serial Port')
    lb1.insert(4,'VGA')
    lb1.insert(5,'LPT')
    lb1.insert(6,'Speakers, Line In and Microphone')
    lb1.insert(7,'Joystick or Game port')
    lb1.grid(row='40',column='10')
    x=xyz(lb1,list1d,list1d2,list1d3)#going to classxyz with passage of listbox and dictionary
    x.btfdbutton()#calling of button function
def list2():
    ins2=Label(app, text='Click on the part name on the below list and then click "GET DATA ABOUT PART" button' ,font=('Malgun Gothic', '10', 'bold italic'),fg='Green')
    ins2.grid(row='35',column='20')
    lb2=Listbox(app,height=8,width=30)#creates listbox 2
    lb2.insert(0,'Mother Board')#places value in listbox 
    lb2.insert(1,'Processor')
    lb2.insert(2,'RAM')
    lb2.insert(3,'Optical Drive')
    lb2.insert(4,'Power Supply')
    lb2.grid(row='40',column='10')
    y=xyz(lb2,list2d,list2d2,list2d3)#going to classxyz with passage of listbox and dictionary
    y.btfdbutton()
def list3():
    ins2=Label(app, text='Click on the part name on the below list and then click "GET DATA ABOUT PART" button' ,font=('Arial', '9', 'bold italic'),fg='blue')
    ins2.grid(row='35',column='20')
    lb3=Listbox(app,height=8,width=30)#creates listbox 2
    lb3.insert(0,'Optical Storage devices',)#places value in listbox
    lb3.insert(1,'Magnetic Storage devices',)
    lb3.insert(2,'Flash Storage devices')
    lb3.grid(row='40',column='10')
    z=xyz(lb3,list3d,list3d2,list3d3)#going to classxyz with passage of listbox and dictionary
    z.btfdbutton()
#Images-----------------------------------------------------------------------------------------------------
d1=PhotoImage(file='photos\\ports.gif')
d2=PhotoImage(file='photos\\pc-diagram.gif')
d3=PhotoImage(file='photos\\computer-memory-11-638.gif')
#Display in MAIN GUI----------------------------------------------------------------------------------------
image1=Label(app, image=d1)
image1.grid(row='10',column='10')
image1label=Label(app, text='Ports', font=('25'))
image1label.grid(row='20',column='10')
image2=Label(app, image=d2)
image2.grid(row='10',column='20')
image2label=Label(app, text='Internal Parts', font=('25'))
image2label.grid(row='20',column='20')
image3=Label(app, image=d3)
image3.grid(row='10',column='30')
image3label=Label(app, text='Storage', font=('25'))
image3label.grid(row='20',column='30')
#DIAGRAM CHOICE----------------------------------------------------------------------------------------------
rb1=Radiobutton(app, text='Ports', value=1,cursor="hand2",command=list1)
rb1.grid(row='30',column='10')
rb2=Radiobutton(app, text='Internal Parts', value=2,cursor="hand2",command=list2 )
rb2.grid(row='30',column='20')
rb3=Radiobutton(app, text='Storage', value=5,cursor="hand2",command=list3 )
rb3.grid(row='30',column='30')

#LOOP LINE--------------------------------------------------------------------------------------------------
app.mainloop()
