# START_GLOBALS
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.manis.compounds.WeirdElementTwo import WeirdElementTwo


# END_GLOBALS


class WeirdElementTwoReader(BaseStruct):

	# START_CLASS

	@classmethod
	def read_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		for chunk_sizes in instance.arg:
			chunk_sizes.keys = ()
		for elem_one in instance.arg:
			# print(mani_info)
			# print(stream.tell())
			elem_one.keys = Array.from_stream(stream, elem_one.context, arg=0, template=None, shape=(elem_one.countb,), dtype=WeirdElementTwo)
			# chunk_sizes.keys = WeirdElementTwo.from_stream(stream, instance.context, chunk_sizes, None)
			# print(elem_one)
			# print(elem_one.keys)
			# break
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def write_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		for elem_one in instance.arg:
			Array.to_stream(elem_one.keys, stream, instance.context, shape=(elem_one.countb,), dtype=WeirdElementTwo)
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def get_fields_str(cls, instance, indent=0):
		s = ''
		for mani_info in instance.arg:
			s += str(mani_info.keys)
		return s

