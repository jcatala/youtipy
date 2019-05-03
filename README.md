# youtiPy
# Easy (or not) py(music)player :musical_note: 

Here's a little program that allows you to play songs (or anything) from YT via CLI

# Why ? 

* I wanted to do it.
* I just needed to get rid of Spotify and Youtube at work for listen to music.
* Need something minimalist that just do the work without a fatty GUI.
* Need something that (please) DO NOT DOWNLOAD the damn whole video.
* I wanted to do it.

Maybe its not the best implementation of the idea, but works for me, and I hope it works for you too.

Any new idea or request, just ask me please :D


# Contents:  

* [Installation](https://github.com/jcatala/youtipy#installation)
* [Usage examples](https://github.com/jcatala/youtipy#usage-example)
* [TroubleShooting](https://github.com/jcatala/youtipy#troubleshooting)

# Installation:  

* Dependencies:  
	* `vlc player`
	* `bs4 (BeautifulSoup)`
	* `requests`
	* `colorama`
	* `youtube-dl`

* Clone & run  
    * `git clone https://github.com/jcatala/youtipy`
    * `cd youtipy`
	* for vlc:  
		* `sudo pacman -S vlc` arch
		* `apt install vlc` debian
    * `pip3 install -r requeriments.txt --user`
    * `python3 main.py`



# Usage example:  

* start the program:
	```bash
	python3 main.py 
	```
* search for song:
	```python
	$ >> search rick astley
	```
* add a song to the queue (From previusly searched term):
	```python
	$ >> add song_id
	```
* add song just with the name:
	```python
	$ >> play rick astley never gonna give you up
	```
* print the current queue:
	```python
	$ >> queue
	# or
	$ >> q
	```
* skip the current song:
	```python
	$ >> next
	```
* pause / resume the current song:
	```python
	$ >> pause
	$ >> resume
	```
* Quit:
    ```python
    $ >> quit
    ```


# Troubleshooting

* My music is not being played, This thing sucks! :
	* Try to check if cvlc lets you to stream any video, sometimes the lua script is outdated and crash with larger streams, if that is the case, do the following:  

		* copy the content of this [file](http://git.videolan.org/?p=vlc.git;a=blob_plain;f=share/lua/playlist/youtube.lua;hb=HEAD) in to:  
		* `/usr/lib64/vlc/lua/playlist/youtube.luac (arch)`  
		* `/usr/lib/i386-linux-gnu/vlc/lua/playlist/youtube.luac (ubuntu x86)`  
	Then, try again :D !
