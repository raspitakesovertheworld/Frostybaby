from Tkinter import *
import random, tkMessageBox, time, os, pickle

global debug_on
debug_on = "true"

print os.name

try:
        os.listdir("/usr/")
except OSError:  
        os_flag = "windows"
    
try:
        os.listdir("c:")
except OSError: 
        os_flag = "linux"


if os_flag == "windows":
        global path
        path = "w:frostybaby/src/frosty_pack/"
#        print "we are on windows"
        global ps
        ps = path + "sounds/"
elif os_flag == "linux":
        global path
        path = "/media/disk/Frostybaby/src/frosty_pack/" 
#        print "we are on linux"
        global ps
        ps = path + "sounds/"
        

class App:
    def __init__(self,):

#create the windows...

#master1 is just fake, we withdraw it immediately. Close that root window to terminate the app
        global master1
        master1 = Tk()
        master1.wm_title("root window")
        master1.withdraw()
        
        global master
        master = Toplevel()
        master.wm_title("main window")
        self.centerwindow(master)

        global bach
        bach = Toplevel()
        bach.wm_title("Bachman window")
        self.centerwindow(bach)
        
        global sig
        sig = Toplevel()
        sig.wm_title("Signatures window")
        self.centerwindow(sig)
        
        global chords
        chords = Toplevel()
        chords.wm_title("Chords window")
        self.centerwindow(chords)
        
        global snowman
        snowman = Toplevel()
        snowman.wm_title("snowman window")
        self.centerwindow(snowman)
        
#main window

        w = Canvas(master, width=600, height=400)
        w2 = Canvas(master, width=100, height=100)
        w.pack()
        w2.pack()

#Bach window
        global bc1        
        bc1 = Canvas(bach, width=800, height=400)
        global bc2
        bc2 = Canvas(bach, width=100, height=100)
        bc1.pack()
        bc2.pack()

#Signature window
        global s1
        s1 = Canvas(sig, width=600, height=400)
        global s2
        s2 = Canvas(sig, width=100, height=100)
        s1.pack()
        s2.pack()

#Chords window
        global chr1
        chr1 = Canvas(chords, width=600, height=400)
        global chr2
        chr2 = Canvas(chords, width=100, height=100)
        chr1.pack()
        chr2.pack()


#snowman
        global snow1
        snow1 = Canvas(snowman, width=600, height=400)
        global snow2
        snow2 = Canvas(snowman, width=600, height=400)
        snow1.pack()
        snow2.pack()
        
#Just show main window

        sig.withdraw()
        bach.withdraw()
        chords.withdraw()
        snowman.withdraw()
        
        
        #master.label(master, text="Frostybaby V0.5 stable")

# here come the buttons and bindings!                       
        self.bachman_button = Button(w2, text="Do the Bach-man!", command=self.bachman)
        self.bachman_button.pack(side=TOP)
        
        self.snowman_button = Button(w2, text="Build Snowmen", command=self.snowman_draw)
        self.snowman_button.pack(side=TOP)
        
        self.chords_button = Button(w2, text="Train Chords", command=self.chords)
        self.chords_button.pack(side=TOP)

        self.sigs_button = Button(w2, text="Train Signatures", 
        command = lambda 
        arg1=s1 :
        self.signatures(arg1)
        )
        self.sigs_button.pack(side=TOP)

        var_toggle = IntVar()
        self.logging = Checkbutton(w2, text="logging enabled", var=var_toggle)
        self.logging.pack(side=TOP)
        
        self.quit_all_main = Button(w2, text="QUIT", fg="red", command=master1.destroy)
        self.quit_all_main.pack(side=TOP)
        
        self.quit_all_bach = Button(bc2, text="QUIT", fg="red", command=master1.destroy)
        self.quit_all_bach.pack(side=TOP)
        
        self.quit_all_sig = Button(s2, text="QUIT", fg="red", command=master1.destroy)
        self.quit_all_sig.pack(side=TOP)

        self.quit_all_chords = Button(chr2, text="QUIT", fg="red", command=master1.destroy)
        self.quit_all_chords.pack(side=TOP)

        self.quit_all_snowman = Button(snow2, text="QUIT", fg="red", command=master1.destroy)
        self.quit_all_snowman.pack(side=TOP)

        
        self.got_it_sig_button = Button(s2, text="Got it!", 
        command = lambda 
        arg2=s1 :
        self.got_it_sig(arg2)
        )  
        self.got_it_sig_button.pack(side=TOP)
        
        self.got_it_chr_button = Button(chr2, text="Got it!", command=self.got_it_chr)
        self.got_it_chr_button.pack(side=TOP)
        chords.bind("<space>", self.got_it_chr)
      
        self.got_it_bach_button = Button(bc2, text="Got it!", command=self.got_it_bach)  
        self.got_it_bach_button.pack(side=TOP)        
        bach.bind("<space>", self.got_it_bach)
        
    def centerwindow(self, window):    
        window.update()
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        w = window.winfo_width()
        h = window.winfo_height()
        newGeometry='+%d+%d' % ((sw/2)-(w/2), (sh/2)-(h/2))
        window.geometry(newGeometry=newGeometry)
        window.update()
 

    def bachman(self):
        
        master.withdraw()
        bach.deiconify()
        
        tkMessageBox.showinfo(message='Get ready!!')          
              
        bc1.img1 = PhotoImage(file=path+"images/Bach001.gif")
        bc1.img2 = PhotoImage(file=path+"images/Bach002.gif")
        bc1.img3 = PhotoImage(file=path+"images/Bach003.gif")
        bc1.img4 = PhotoImage(file=path+"images/Bach004.gif")
        bc1.img5 = PhotoImage(file=path+"images/Bach005.gif")
        bc1.img6 = PhotoImage(file=path+"images/Bach006.gif")
        bc1.img7 = PhotoImage(file=path+"images/Bach007.gif")
        bc1.img8 = PhotoImage(file=path+"images/Bach008.gif")
        bc1.img9 = PhotoImage(file=path+"images/Bach009.gif")
        bc1.img10 = PhotoImage(file=path+"images/Bach010.gif")
        bc1.img11 = PhotoImage(file=path+"images/Bach011.gif")
        bc1.img12 = PhotoImage(file=path+"images/Bach012.gif")
        bc1.img13 = PhotoImage(file=path+"images/Bach013.gif")
        bc1.img14 = PhotoImage(file=path+"images/Bach014.gif")
        bc1.img15 = PhotoImage(file=path+"images/Bach015.gif")
        bc1.img16 = PhotoImage(file=path+"images/Bach016.gif")
        bc1.img17 = PhotoImage(file=path+"images/Bach017.gif")
        bc1.img18 = PhotoImage(file=path+"images/Bach018.gif")
        
        
        bach_dict = {"1": bc1.img1, "2": bc1.img2, "3": bc1.img3, "4": bc1.img4, "5": bc1.img5, "6": bc1.img6, "7": bc1.img7, "8": bc1.img8, "9": bc1.img9, "10": bc1.img10, "11": bc1.img11, "12": bc1.img12, "13": bc1.img13, "14": bc1.img14, "15": bc1.img15, "16": bc1.img16, "17": bc1.img17, "18": bc1.img18}
        choice = random.choice(bach_dict.keys())
       
        bc1.create_image(700, 0, image=bach_dict[choice], anchor="ne")
     
# note the time
        global time_before
        time_before = time.time()
       
        global label
        label = choice
        
        
    def chords(self):    
        
        master.withdraw()
        chords.deiconify()
        
#       rand_nr = random.randint(0,33)
         
        chords_dict = {"C": ps+"C_triad.ogg", "D": ps+"D_triad.ogg", "E": ps+"E_triad.ogg", 
        "F": ps+"F_triad.ogg", "G": ps+"G_triad.ogg", "A": ps+"A_triad.ogg", "B": ps+"B_triad.ogg", "Cm": ps+"cm_triad.ogg", 
        "dm": ps+"dm_triad.ogg", "em": ps+"em_triad.ogg", "fm": ps+"fm_triad.ogg", "gm": ps+"gm_triad.ogg", 
        "am": ps+"am_triad.ogg", "bm": ps+"bm_triad.ogg", "C#": ps+"C#_triad.ogg", 
        "D#": ps+"D#_triad.ogg", "F#": ps+"F#_triad.ogg", "G#": ps+"G#_triad.ogg", "A#": ps+"A#_triad.ogg", 
        "c#m": ps+"c#m_triad.ogg", "d#m": ps+"d#m_triad.ogg", "f#m": ps+"f#m_triad.ogg", "g#m": ps+"g#m_triad.ogg", 
        "a#m": ps+"a#m_triad.ogg", "Db": ps+"Db_triad.ogg", "Eb": ps+"Eb_triad.ogg", "Gb": ps+"Gb_triad.ogg",
        "Ab": ps+"Ab_triad.ogg", "Bb": ps+"Bb_triad.ogg", "dbm": ps+"dbm_triad.ogg", "ebm": ps+"ebm_triad.ogg", 
        "gbm": ps+"gbm_triad.ogg", "abm": ps+"abm_triad.ogg", "bbm": ps+"bbm_triad.ogg" }
        choice = random.choice(chords_dict.keys())
        
        self.q_key(choice)     
        global time_before
        time_before = time.time()
        global label
        label = choice
        global sound_file
        sound_file = chords_dict[choice] 
          
    def snowman_draw(self):
        master.withdraw()
        snowman.deiconify()
        
        #user settings
        scale = 50
        
        
        startx = 100
        starty = 50
        line_width = 400
        for i in range(1,6):
            snow1.create_line(startx, starty+(i*scale), line_width, starty+(i*scale))
        
        #def draw_snowman(self, scale, start_head_enter, head_offset, belly_offset, foot_offset):
        start_head_enter = 2
        head_offset = 0
        belly_offset = 0
        foot_offset = 0
        
        active_head = "true"
        active_belly = "true"
        active_foot = "true"
        
        start_head = start_head_enter * scale/2
        ho = head_offset*scale/2
        bo = belly_offset*scale/2
        fo = foot_offset*scale/2
                    
        vertical_pos = line_width / 1.5
        
        #head
        if active_head == "true":
            snow1.create_oval(vertical_pos, starty+start_head+(0*scale/2)+ho, vertical_pos+scale, starty+start_head+(0*scale/2)+ho+scale, fill="black")
        
        #belly
        if active_belly == "true":        
            snow1.create_oval(vertical_pos, starty+start_head+(2*scale/2)+bo, vertical_pos+scale, starty+start_head+(2*scale/2)+bo+scale, fill="black")
        #foot
        if active_foot == "true":
            snow1.create_oval(vertical_pos, starty+start_head+(4*scale/2)+fo, vertical_pos+scale, starty+start_head+(4*scale/2)+fo+scale, fill="black")
            
            
    def q_key(self, key):   
        chr1.delete("all")
        font=('helvetica', 32)
        text_id = chr1.create_text(300, 200, text="Chord " +key, font=font)

    def log_it(self, file, log_line):    
        
        if debug_on == "false":
            #open file
            f=open(path+file, 'a')
            f.write(log_line)
            f.close()
            print "logging, debug_on = false"
        else:   
            print "no logging done, debug_on = true"
        
    def signatures(self, res):    
        master.withdraw()
        bach.withdraw()
        sig.deiconify()
        tkMessageBox.showinfo(message='Get ready!!')
        
        res.img0 = PhotoImage(file=path+"images/0.gif")
        res.img1 = PhotoImage(file=path+"images/1.gif")
        res.img2 = PhotoImage(file=path+"images/2.gif")
        res.img3 = PhotoImage(file=path+"images/3.gif")
        res.img4 = PhotoImage(file=path+"images/4.gif")
        res.img5 = PhotoImage(file=path+"images/5.gif")
        res.img6 = PhotoImage(file=path+"images/6.gif")
        res.img7 = PhotoImage(file=path+"images/7.gif")
        res.img8 = PhotoImage(file=path+"images/-7.gif")
        res.img9 = PhotoImage(file=path+"images/-6.gif")
        res.img10 = PhotoImage(file=path+"images/-5.gif")
        res.img11 = PhotoImage(file=path+"images/-4.gif")
        res.img12 = PhotoImage(file=path+"images/-3.gif")
        res.img13 = PhotoImage(file=path+"images/-2.gif")
        res.img14 = PhotoImage(file=path+"images/-1.gif")
 
        sig_dict = {"C": res.img0, "G": res.img1, "D": res.img2, "A": res.img3, "E": res.img4, "H": res.img5, "Fis": res.img6, "Cis": res.img7, "Ces": res.img8, "Ges": res.img9, "Des": res.img10, "As": res.img11, "Es": res.img12, "B": res.img13, "F": res.img14}
        choice = random.choice(sig_dict.keys())

        res.create_image(150, 0, image=sig_dict[choice], anchor="ne")
     
# note the time
        global time_before
        time_before = time.time()
       
        global label
        label = choice
       


#press space when you got it

    def got_it_sig(self, res2):
#Now the guy pushed the got it, time him
        global time_after
        time_after = time.time()
        latency = str(round(time_after - time_before, 3))
        messy = "It took you " + latency + " seconds!"
        tkMessageBox.showinfo(message=messy)
# log into file
        log_string = label + ", " + latency + ", " + str(time.strftime( '%Y%m%d')) + "\n"
        self.log_it("sig_log.csv", log_string)
        self.signatures(res2)   
             
    def got_it_chr(self, event):
#Now the guy pushed the got it, time him
        global time_after
        time_after = time.time()
        latency = str(round(time_after - time_before, 3))
        messy = "It took you " + latency + " seconds!"
        exec_obj = os.system("mplayer -ao jack -really-quiet "+sound_file + " &")
        tkMessageBox.showinfo(message=messy)
        log_string = label + ", " + latency + ", " + str(time.strftime( '%Y%m%d')) + "\n"
        self.log_it("chords_log.csv", log_string)
        self.chords()              
        
    def got_it_bach(self):
#Now the guy pushed the got it, time him
        global time_after
        time_after = time.time()
        latency = str(round(time_after - time_before, 3))
        messy = "It took you " + latency + " seconds!"
        tkMessageBox.showinfo(message=messy)
        log_string = label + ", " + latency + ", " + str(time.strftime( '%Y%m%d')) + "\n"
        self.log_it("bach_log.csv", log_string)
        self.bachman               
        
        
        
app = App()
mainloop()
