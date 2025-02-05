import os
import sys
def check_reboot():
	
def main():
	if check_reboot():
		print('Pending Reboot')
		sys.exit(1)
	print('everything ok')
	sys.exit(0)
main()
