import search_pyplayer
import banners
import audio_stream


from colorama import Fore, Back, Style
import sys
import subprocess




custom_player = audio_stream.Player()
last_search = dict()
banners.print_banner()
while True:
    try:
        cmd = input("$ >> ")
        if cmd == "help" or cmd == "h":
            banners.print_banner()
            print ("List of commands:\n\thelp: show this info message)")
            print ("\tsearch <query> : Search for \"query\" keyword on youtube")
            print ("\tadd <id> : Download the previusly searched \"id\" and add it to the queue")
            print ("\tfadd <name> : Force to add the first result of the queue with \"name\"")
            print ("\tplay <name> : Same as \"fadd\"")
            print ("\tqueue : Show the currently queue")
            print ("\tnext : Skip the current song")
            print("\tpause / resume: To pause or resume the player")
            print("\tq : quit")
        if "search" in cmd:
            result = search_pyplayer.search(cmd.strip().split("search ")[1])
            last_search = result
            for k in result:
                if int(k) % 2 == 0:
                    print(Fore.CYAN + "-> id : {} | Name : {}".format(k, result[k][0] ) )
                else:
                    print(Fore.GREEN + "-> id : {} | Name : {}".format(k, result[k][0] ) )
        elif "add" in cmd:
            id = int(cmd.strip("add "))
            url = last_search[id][1]
            custom_player.add_to_queue(last_search[id])
        elif "play" in cmd:
            song_name = cmd.split("play ")[1]
            result = search_pyplayer.search(song_name)
            custom_player.add_to_queue(result[0])
        elif "fadd" in cmd:
            song_name = cmd.split("fadd ")[1]
            result = search_pyplayer.search(song_name[1])
            custom_player.add_to_queue(result[0])
        elif "next" in cmd:
            #custom_player.next()
            print("Skipping ... ")
            custom_player.force_next()
        elif "queue" in cmd or "q" == cmd:
            print ("Current playing: ", custom_player.check_current())
            if len(custom_player.check_queue()) == 0:
                print(Fore.RED + "Empty queue ")
            else:
                c = 0
                for k in custom_player.check_queue():
                    if c % 2 == 0:
                        print("\t" * c + Fore.CYAN + " --> " + k[0])
                    else:
                        print("\t" * c + Fore.GREEN + " --> " + k[0])
                    c += 1
        elif "pause" in cmd or "resume" in cmd:
            custom_player.pause_resume()

        elif "exit" in cmd or "quit" in cmd:
            print("Closing, please wait ...")
            break
        print(Style.RESET_ALL)

    except KeyboardInterrupt as e:
        print ("Closing, please wait... ")
        subprocess.Popen("kill $(pidof vlc) > /dev/null 2>&1", shell=True)
        custom_player.scheduler.stop()
        sys.exit(-1)
    except:
        print ("Type help or h for help :D ")

subprocess.Popen("kill $(pidof vlc) > /dev/null 2>&1", shell=True)
custom_player.scheduler.stop()
