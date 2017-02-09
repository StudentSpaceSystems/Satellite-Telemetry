import serial
import sys
import time
import datetime

def asctime(epoch_time, frmt="%d %m %Y, %H:%M:%S.%f"):
	return datetime.datetime.fromtimestamp(epoch_time).strftime(frmt)

def strtohex(ipt_str):
	ipt_str.encode('utf-8')	

def hextostr(bytestr):
	bytestr.decode('utf-8')

def run(ser, msg):
	print("Starting %s"%msg)
	time_map = [0, 0, 0]
	time_map[0] = time.time()
	credit_count = ser.write(msg)
	time_map[1] = time.time()
	out = ser.read_until(b'OK\r\n')
	time_map[2] = time.time()
	return time_map, out, credit_count

def confirm(msg="Continue (Y/N/R)? "):
	while True:
		a = input(msg)
		if a.upper()[0] == "Y":
			return True
		elif a.upper()[0] == "N":
			return False
		elif a.upper()[0] == "R":
			return None
if __name__ == '__main__':
	msg_list = [b'AT+CSQ\r',
				b'AT&KO\r',
				b'AT+SBDWT=MSG1-PRIMER\r',
				b'AT+SBDIX\r',
				b'AT+SBDWT=MSG2-SENDING FROM 40.1124220N-99.2288650E\r',
				b'AT+SBDIX\r',
				b'AT+SBDWT=MSG3-ASCII:TXRAW:\xF2\xF3\r',
				b'AT+SBDIX\r',
				b'AT+SBDWT=MSG4-Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse\r',
				b'AT+SBDIX\r',
				b'AT+SBDWT=MSG5-3PACKETTEST\xf4\x95\x5a\x4f\x88\xd9\xd2\xc4\xa1\x4b\xfa\xef\xf7\xea\x8a\x4c\x14\x9d\xd5\x2e\xc6\xfb\x55\x02\xfd\xd3\x94\xd2\x06\x40\x6a\x2a\xcf\x1d\x39\xb5\x4c\xdd\xcb\x3b\x59\x38\x5b\x55\xd1\xaa\x82\xb5\x20\x5c\xfd\xc7\x28\x3d\x6d\xa6\xae\x45\xbb\xdf\xc7\x2f\x31\xa2\x35\x48\xf2\x03\x05\x67\x5d\x07\xad\xe6\x86\xf2\xba\xc2\x40\xf2\x83\x64\x01\x95\xac\xcb\xe2\x13\x41\x60\xc2\x7b\x42\x98\x16\xd0\xb1\x1c\x5b\xb3\x62\x3d\x77\x14\xa1\x56\xb1\xbf\xf9\x7e\xf4\x39\xdf\x4e\x59\xea\xe8\r',
				b'AT+SBDIX\r']

	with serial.Serial(sys.argv[1], sys.argv[2], timeout=10) as ser:
		_BREAKOUT = False
		for msg in msg_list:
			while not _BREAKOUT:
				print(run(ser, msg), end='\n')
				resp = confirm()
				print()
				if resp is None:
					continue
				if resp is False:
					_BREAKOUT = True
				elif resp is True:
					break

	ser.close()
