# START_GLOBALS
from generated.formats.ovl.versions import *
from hashes import constants_jwe, constants_pz


# END_GLOBALS


class FileEntry:

	# START_CLASS

	def update_constants(self, ovl):
		"""Update the constants"""

		# update offset using the name buffer
		if is_jwe(ovl):
			constants = constants_jwe
		elif is_pz(ovl) or is_pz16(ovl):
			constants = constants_pz
		else:
			raise ValueError(f"Unsupported game {get_game(ovl)}")
		self.unkn_0 = constants.files_unkn_0.get(self.ext)
		self.unkn_1 = constants.files_unkn_1.get(self.ext)