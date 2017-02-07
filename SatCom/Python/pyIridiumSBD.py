import serial.tools.list_ports
import serial
from collections import deque
import sys
import time

EPOCH_TIME = 1399818235000

class IridiumSBDException(Exception):
	pass

class EmptyPacketBuffer(IridiumSBDException):
	pass

class IridiumSBD:
	def __init__(self, port_loc, baud, serial_arg):
		self.ser = serial.Serial(port=port_loc, baudrate=baud, **serial_arg)
		self.packet_queue = deque()
	
	def __enter__():
		self.ser.open()
		return self
	
	def __exit__():
		self.ser.close()
		
	def reset(mode=0):
		"""Resets input- or output-buffers.
		
		Parameters
			mode: int
				0 - neither
				1 - input
				2 - output
				3 - both
		Returns
			None
		"""
		if mode&1:
			self.ser.reset_input_buffer()
		if mode&2:
			self.ser.reset_output_buffer()
	
	def packet_clear_buffer(self):
		self.packet_queue.clear()
	
	def belay(self):
		try:
			return self.packet_queue.pop()
		except IndexError:
			raise EmptyPacketBuffer
	
	def enqueue(self, msg):
		self.packet_queue.append(msg)
	
	def transmit(msg):
		pass
	
	def buffer_state(self):
		return (self.ser.in_waiting,
				self.ser.out_waiting)
	
	def set_nonblocking(self):
		self.ser.nonblocking()
	
	@staticmethod
	def form_packet_size(iterable, size, inclusive=False):
		_packet = bytes(size)
	
	@staticmethod
	def list_baud():
		return serial.Serial.BAUDRATE
	
	@staticmethod
	def search_ports():
		return serial.tools.list_ports.grep()
	
	@staticmethod
	def list_ports():
		return serial.tools.list_ports.comports()
