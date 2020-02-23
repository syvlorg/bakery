# From Imports
from nanite import check_type, fullpath
from toml import load

class Error(Exception):
	pass


class no_caps(Error):
	pass


class too_verbose(Error):
	pass


class _short_property_vars:

	@property
	def _type(self):
		return self.__type

	@_type.setter
	def _type(self, value):
		self.__type = check_type(
			_type=value,
			allowed_type_names=self._allowed_type_names,
		)

	@property
	def _capture(self):
		return self.__capture

	@_capture.setter
	def _capture(self, value):
		if value not in self._captures:
			raise no_caps(
				f'Sorry! Type "{value}" is not permitted! Choose from one of: [{(", ").join(self._captures)}]'
			)
		self.__capture = value

	@property
	def _frosting(self):
		return self.__frosting

	@_frosting.setter
	def _frosting(self, value):
		self.__frosting = bool(value)

	@property
	def _shell(self):
		return self.__shell

	@_shell.setter
	def _shell(self, value):
		self.__shell = bool(value)

	@property
	def _str(self):
		return self.__str

	@_str.setter
	def _str(self, value):
		self.__str = bool(value)

	@property
	def _ignore_stderr(self):
		return self.__ignore_stderr

	@_ignore_stderr.setter
	def _ignore_stderr(self, value):
		self.__ignore_stderr = bool(value)

	@property
	def _verbosity(self):
		return self.__verbosity

	@_verbosity.setter
	def _verbosity(self, value):
		_ = int(value)
		if not 0 <= value <= 2:
			raise too_verbose(
				"Sorry! No verbosity levels greater than 2 or less than 0!"
			)
		self.__verbosity = _

	@property
	def _from_file(self):
		return self.__from_file

	@_from_file.setter
	def _from_file(self, value):
		self.__from_file = load(fullpath(value)) if value else ""

	@property
	def _end_args(self):
		return self.__end_args

	@_end_args.setter
	def _end_args(self, value):
		# If the arg value is a string, we'll convert it into a list
		if isinstance(value, str):
			self.__end_args = [value]
		elif isinstance(value, (bytes, bytearray)):
			self.__end_args = [value.decode()]
		else:
			self.__end_args = value

	@property
	def _before_args(self):
		return self.__before_args

	@_before_args.setter
	def _before_args(self, value):
		# If the arg value is a string, we'll convert it into a list
		if isinstance(value, str):
			self.__before_args = [value]
		elif isinstance(value, (bytes, bytearray)):
			self.__before_args = [value.decode()]
		else:
			self.__before_args = value