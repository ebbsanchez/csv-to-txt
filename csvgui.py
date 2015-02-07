from Tkinter import *
import tkFileDialog
import os, time, csv

class csvGui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
 
    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "csv:"
        self.inputText.grid(row=0, column=0)
        self.inputdisplay = Label(self)
        self.inputdisplay["text"] = "Choose csv"
        self.inputdisplay.grid(row=0, column=1, columnspan=6)
        self.askopen = Button(self)
        self.askopen["text"] = "..."
        self.askopen.grid(row=0,column=7)
        self.askopen["command"] = self.askopenMethod

        self.savedir = os.getcwd() 
        self.outputText = Label(self)
        self.outputText["text"] = "save to:"
        self.outputText.grid(row=1, column=0)
        self.outputdisplay = Label(self) 
        self.outputdisplay["text"] = self.savedir
        self.outputdisplay.grid(row=1, column=1, columnspan=6)
        self.asksave = Button(self)
        self.asksave["text"] = "..."
        self.asksave.grid(row=1,column=7)
        self.asksave["command"] = self.asksaveMethod
        
        self.start = Button(self)
        self.start["text"] = "Start"
        self.start.grid(row=2, column=1)
        self.start["command"] = self.startMethod
        #self.stop = Button(self)
        #self.stop["text"] = "Stop"
        #self.stop.grid(row=2, column=2)
        #self.stop["command"] = self.stopMethod
        #self.support = Button(self)
        #self.support["text"] = "Support"
        #self.support.grid(row=2, column=3)
        #self.support["command"] = self.supportMethod

        self.displayText = Label(self)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=3, column=0, columnspan=7)
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('all files', '.*'), ('.csv', '.csv')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.csv'
        options['parent'] = root
        options['title'] = 'Choose a csv file'

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Choose a directory'

    def askopenMethod(self):
        global filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.inputdisplay["text"] = filename
    def asksaveMethod(self):
        self.savedir = tkFileDialog.askdirectory(**self.dir_opt)
        self.outputdisplay["text"] = self.savedir
        
    def startMethod(self):
        if not self.inputdisplay["text"] == "Choose csv":
            

            svtime = time.strftime('%Y%m%d') 
            #csv name and make save dir
            csvdir = filename 
            savedir = os.path.join(self.savedir, svtime + '_' + os.path.split(filename)[1][0:-4]) 
            if not os.path.exists(savedir):
                os.makedirs(savedir)
            #write txt 
            f = open(csvdir, 'r')
            for row in csv.reader(f):
                print row
                tname, data = row[0], row[1]
                f2=open(os.path.join(savedir, tname) + '.txt', 'w')
                f2.write(data)
                f2.close
            f.close()
            self.displayText["text"] = "Done!!"
        else:
            self.displayText["text"] = "Choose csv first"
    def stopMethod(self):
        return None
    def supportMethod(self):
        return None

        
if __name__ == '__main__':
    root = Tk()
    app = csvGui(master=root)
    app.mainloop()
