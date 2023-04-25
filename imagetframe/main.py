"""made by LikiLik"""
""" version 1.0,i watch ut for new updates"""
#note to others:im all ears for any improvements in my code
#note to self:i need add rollback options for time,also needs to be multi threaded
import sys
import cv2
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import time_conv,vtime

from ui import main_ui


class Main(QDialog,main_ui.Ui_Dialog):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        #defining commonly used variables
        self.open_file=""
        self.save_frame_dir="frames"#if nothing selected then it will go to save frames on current folder
        #start video definition
        self.start_hrs_time=0
        self.start_min_time=0
        self.start_sec_time=0
        #end video definition
        self.end_hrs_time=0
        self.end_min_time=0
        self.end_sec_time=0
        #frame rate
        self.frame_rate=10
        #error functions
        self.message,self.error="",""
        #time frames
        self.start_frame="00:00:00"
        self.end_frame="00:00:00"
        self.final_end_frame="00:00:00"

        #defing events here
        self.process.clicked.connect(self.process_it)
        self.get_video.clicked.connect(self.got_video)
        self.save_frame.clicked.connect(self.save_dir)
        #if end timer is changed
        self.end_sec.valueChanged.connect(self.time_changed)
        self.end_hr.valueChanged.connect(self.time_changed)
        self.end_min.valueChanged.connect(self.time_changed)
        self.start_sec.valueChanged.connect(self.time_changed)
        self.start_hr.valueChanged.connect(self.time_changed)
        self.start_min.valueChanged.connect(self.time_changed)


#defing functions here
    def save_dir(self):
        dir_name=QFileDialog.getExistingDirectory(self,"select directory")
        print(dir_name)
        self.save_frame_dir=dir_name

    def warn(self):
        QMessageBox.warning(self,self.message,self.error)
        
    def time_changed(self,value):#gets called when spinboxes are called
        if  self.start_hr.value()==self.end_hr.value():
            if self.start_min.value()==self.end_min.value():
                self.start_sec.setMaximum(self.end_sec.value())
                if self.start_sec.value()>self.end_sec.value():
                    self.start_sec.setValue(0)
                    
            elif self.start_min.value()>self.end_min.value():
                self.start_min.setValue(0)
            else:
                self.start_sec.setMaximum(59)
                if self.start_sec.value()>60:
                    self.start_sec.setValue(0)
        elif self.start_hr.value()>self.end_hr.value():
            self.start_hr.setValue(0)
        else:
            self.start_min.setMaximum(59)
            if self.start_min.value()>60:
                self.start_min.setValue(0)
                
            self.start_sec.setMaximum(59)
            if self.start_sec.value()>60:
                self.start_sec.setValue(0)
        self.final_end_frame="{}:{}:{}".format(self.end_hr.value(),self.end_min.value(),self.end_sec.value())
        self.start_frame="{}:{}:{}".format(self.start_hr.value(),self.start_min.value(),self.start_sec.value())
        #print(self.final_end_frame)
        #print(self.start_frame)
        self.subtime(self.start_frame,self.final_end_frame)    
                    
                
                
                
                
       # self.end_hrs_time=self.end_hr.value()
        #self.end_min_time=self.end_sec.value()
        #self.end_sec_time=self.end_min.value()
        #self.start_hr.setMaximum(self.end_hrs_time)
        #self.start_sec.setMaximum(self.end_min_time)
        #self.start_min.setMaximum(self.end_sec_time)
        
        #write code that works when spinboxes are changed
    def got_video(self):
        video_path,_=QFileDialog.getOpenFileName(parent=None,caption="open file",filter="mp4 Files(*.mp4);;mkv Files(*.mkv);;3gp Files(*.3gp);;All files (*.*)")
        self.end_frame=vtime.get_video_duration_in_str(video_path)
        self.end_hrs_time,self.end_min_time,self.end_sec_time=time_conv.extract(self.end_frame)
        self.end_hr.setMaximum(self.end_hrs_time)
        self.end_min.setMaximum(self.end_min_time)
        self.end_sec.setMaximum(self.end_sec_time)
        self.label_15.setText("video time:"+self.end_frame)
        self.textBrowser.clear()
        
        #print(video_path)
        self.open_file=video_path
    
    def subtime(self,start,end):
        stime=time_conv.hms_to_ms(start)
        etime=time_conv.hms_to_ms(end)
        ftime=etime-stime
        str1=time_conv.convert_ms_to_hms(ftime)
        #print(str1)
        self.label_14.setText("total video length you selected:"+str1)

    def process_it(self):
        
        
        
        self.frame_rate=self.framerate.value()
        self.convert_video_to_frames(self.open_file,self.save_frame_dir,self.final_end_frame, self.frame_rate,self.start_frame)
    
    
    
    def convert_video_to_frames(self,video_path, storage_path, end_time, fps, start_time="00:00:00"):
    # Convert start and end times to milliseconds
        try:
            start_ms = sum(x * int(t) for x, t in zip([3600000, 60000, 1000], start_time.split(":")))
            end_ms = sum(x * int(t) for x, t in zip([3600000, 60000, 1000], end_time.split(":")))
        except ValueError:
            self.message,self.error="invalid time format","select correct format"
            self.warn()
            return
    
        # Create directory to store frames
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

        # Open video file
        cap = cv2.VideoCapture(video_path)

    # Check if video file was opened successfully
        if not cap.isOpened():
            self.message,self.error="error","error opening video file"
            self.warn()
            return

    # Get total video length in milliseconds
        total_ms = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps * 1000)

    # Convert total video length to hours, minutes, and seconds
        total_seconds = total_ms // 1000
        total_minutes, total_seconds = divmod(total_seconds, 60)
        total_hours, total_minutes = divmod(total_minutes, 60)

    # Print total video length in hours, minutes, and seconds
        #print("Total video length: {:02d}:{:02d}:{:02d}".format(total_hours, total_minutes, total_seconds))

    # Set video position to start time
        cap.set(cv2.CAP_PROP_POS_MSEC, start_ms)

    # Read frames and save PNG files
        frame_num = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

        # Check if current frame time exceeds end time
            current_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            if current_ms > end_ms:
                break

        # Save frame as PNG file
            filename = "frame_{}.png".format(frame_num)
            cv2.imwrite(os.path.join(storage_path, filename), frame)

        # Print progress
            stat=str("Saved frame {} at {} ms".format(frame_num, current_ms))
            self.textBrowser.append(stat)
            self.textBrowser.moveCursor(QTextCursor.End,QTextCursor.KeepAnchor)

            frame_num += 1

    # Release video file and close all windows
        cap.release()
        cv2.destroyAllWindows()
        

        

                

        
app=QApplication(sys.argv)
form=Main()
form.show()
app.exec()
