"""
Student Space System code for satellite communcation using the RockBlock 7 over the Iridium satellite network
using pyRockBlock with manual modifications for python 3xx compliance
"""
import pyRockBlock.rockBlock as rb

if __name__ == '__main__':
	import argparse
	parse = argparse.ArgumentParser(description = "Student Space System transmission code for Satellite Communication using RockBlock7 over the Iridium satellite network")
	parse.add_argument("-d", "--device", help = "RockBlock UART file", required = True, type=str)
	parse.add_argument("-v", "--verbose", help = "verbose", action='store_true')
	args = parse.parse_args()
	
	GLOBAL_VERBOSITY = args.verbose
	GLOBAL_DEVICE = args.device
	rbTransmitter = rb.rockBlock(GLOBAL_DEVICE, None)
