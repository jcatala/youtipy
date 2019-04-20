# Easy (or not) py(music)player :musical_note: 

Here's a little program that allows you play songs (or anything) from YT via CLI

# Why ? 

* I wanted to do it.
* I just needed to get rid of Spotify and Youtube at work for listen to music.
* Need something minimalist that just do the work without a fatty GUI.
* Need something that (please) DO NOT DOWNLOAD the damn whole video.
* I wanted to do it.

Maybe its not the best implementation of the idea, but works for me, and I hope it works for you too.

Any new idea or request, just ask me please :D

# Installation:

* Dependencies:
	* `vlc player`
	* `pafy`
	* `subprocess` 	
	* `bs4 (BeautifulSoup)`
	* `requests`
	* `colorama`

* Clone & run
    * `git clone URL`
    * `cd URL` 
    * `python3 main.py`



* Usage example:
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
		# or
		$ >> fadd rick astley never gonna give you up
		```
	* print the current queue:
		```python
		$ >> queue
		```
	* skip the current song:
		```python
		$ >> next
		```
    * Quit:
        ```python
        $ >> quit
        ```



