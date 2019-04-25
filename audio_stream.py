import threading
import subprocess

import time

# AudioFiles
"""
class Download(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self._stop_event = threading.Event() # FOR STOP THE THREAD

    def run(self):
        pwd = os.getcwd()
        print(pwd)

    def stop(self):
        self._stop_event.set()
    def stopped(self):
        return self._stop_event.is_set()

"""


class Scheduler(threading.Thread):
    def __init__(self,Player):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event() # FOR STOP THE THREAD
        self.player = Player
        self.endflag = False
    def run(self):
        while True:
            if  len(self.player.check_queue())  > 0 and subprocess.run("pidof vlc > /dev/null 2>&1", shell=True).returncode != 0:
                # if there's something in the queue, and nothing is being played
                # pop one item and play it!
                self.player.next()
            time.sleep(5)
            if self.endflag == True:
                break
        print("Scheduler ended.")
    def stop(self):
        self._stop_event.set()
        self.endflag = True

    def stopped(self):
        return self._stop_event.is_set()






class Player:
    def __init__(self):
        self.queue = []
        self.play_th = ""
        self.pid = ""
        self.nowplaying = ""
        self.scheduler = Scheduler(self)
        self.scheduler.start()
    def next(self):
        # PAFY GETS BROKEN DUNNO WHY for the moment just get the video id from the URL !
        if len(self.queue) > 0:
            subprocess.Popen("kill $(pidof vlc) > /dev/null 2>&1", shell=True)   # Kill any instance of vlc for the next song
            popped = self.queue.pop(0)
            video_id = popped[1].split("v=")[1]
            #audio = pafy.new(url=popped[1])
            self.pid = subprocess.Popen("cvlc --novideo --play-and-exit https://www.youtube.com/embed/" + video_id + " 2> /dev/null", shell=True)
            self.nowplaying = popped[0]
            print("Now playing: ", self.nowplaying)
            time.sleep(1)
    def force_next(self):
        self.nowplaying = ""
        subprocess.Popen("kill $(pidof vlc) > /dev/null 2>&1", shell=True)
        time.sleep(2)
    def add_to_queue(self,name_url):
        self.push(name_url)
        print("\t" + name_url[0] + " Added !")
        #if len(self.queue) == 0: # Means that its the first video
            #self.queue.append(name_url)
            #self.play_th = Play(name_url)
            #self.play_th.start() # Start the player thread
            #self.play_th.stop()
            #audio = pafy.new(name_url[1])
            #video_id = audio.videoid
            #self.pid = subprocess.Popen("cvlc --novideo https://www.youtube.com/embed/" + video_id + " 2> /dev/null",shell=True)
            #self.nowplaying = audio.title
            #print("\tNow Playing : " + audio.title + " Enjoy !")
            #subprocess.Popen("kill $(pidof vlc)",shell=True)

    def push(self,name_url):
        self.queue.append(name_url)
    def check_queue(self):
        return self.queue
    def check_current(self):
        return self.nowplaying

    def pause_resume(self):
        try:
            subprocess.Popen("dbus-send --type=method_call --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause",shell=True)
            time.sleep(1)
            print("Paused / Resumed ...")
        except:
            print("Need \"dbus-send\" for pause the music :D ")



