#watch for every few min
from datetime import datetime
from time import sleep
import s_twitter 
import s_discord
import portal_interface 
print(datetime.now())

def check_interupts(browser):
	# get_twitter_interupts(browser)
	return 

def open_websites(browser):
	s_discord.openTab(browser)
	s_twitter.openTab(browser)
	return

def wait_11Sec():
	for i in range(5):
		print("{} seconds".format(i))
		sleep(1)


if __name__ == "__main__":
	while (1):
		#open browser
		portal_interface = portal_interface.openBrowser()
		open_websites(portal_interface)
		entryTime = datetime.now()
		check_interupts(portal_interface)
		
		wait_11Sec()
		

		#if stuck clean up
		seconds_elapsed = (datetime.now() - entryTime).total_seconds()
		print(seconds_elapsed)
		if seconds_elapsed < 10:
			sleep(10 - seconds_elapsed)
			#close browser
			portal_interface.close()
			break