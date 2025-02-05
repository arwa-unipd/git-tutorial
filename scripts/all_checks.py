import os
import sys
def check_reboot():
	return os.path.exist('/run/reboot-required')
def main():
	if check_reboot():
		print('Pending Reboot')
		sys.exit(1)
	print('everything ok')
	sys.exit(0)
main()
