# From Imports
from addict import Dict as D
from functools import partial
from gensing import tea, frosting
from itertools import chain
from nanite import (
	check_type,
	module_installed,
	fullpath,
	mixinport,
)
from os import environ
from textwrap import TextWrapper
from typing import (
	List,
	Tuple,
	Dict,
	MutableSequence as MS,
	Any,
	Generator,
	Union,
)

mixins: Generator[str, None, None] = (
	fullpath(f"{mixin}.py", f_back=2)
	for mixin in (
		"_create_command",
		"_funky_properties",
		"_long_property_vars",
		"_process_args_kwargs",
		"_return_output",
		"_run_frosting",
		"_set",
		"_short_property_vars",
		"baking_",
	)
)


class _milcery(*(mixinport(mixins))):

	"""
		Answer: https://stackoverflow.com/questions/26315584/apply-a-function-to-all-instances-of-a-class/26315625#26315625
		User: https://stackoverflow.com/users/625914/behzad-nouri
	"""

	def __init__(
		self,
		_program: str,
		*args,
		_ignore_check: bool = False,
		_baked_commands: Dict[str, Any] = None,
		_baked_settings: Dict[str, Any] = None,
		**kwargs,
	):
		"""
			_type can be any type, such as:
			* iter
			* list
			* tuple
			* set
			* frozenset

			A good way to debug commands is to see what the command actually was, using the "_str"
			keyword argument.
		"""
		self._program: str = _program
		self._ignore_check: bool = _ignore_check

		self._command = D({})
		self._command.baked = _baked_commands or D({})

		self._settings = D({})
		self._settings.baked = _baked_settings or D({})

		self._sub = D({})

		"""

		"""
		self._settings.defaults: Dict[str, Any] = {
			"_type": iter,
			"_capture": "stdout",
			"_shell": False,
			"_frosting": False,
			"_str": False,
			"_ignore_stderr": False,
			"_verbosity": int(environ.get("verbose_bakery", 0)),
			"_run_as": "",
			"_n_lines": D(
				{
					"ordinal": "first",
					"number": None,
					"std": "stdout",
				}
			),
			"_kwarg_one_dash": False,
			"_fixed_key": False,
			"_print": False,
			"_tiered": False,
			# This setting will use a single forward slash instead of a dash for options
			"_dos": False,
			# If set to True, _capture = "run" will wait for the process to finish before
			# returning an addict dictionary of values depending on "_return" and "_verbosity"
			# If set to False, _capture = "run" will return the sarge Pipeline object
			# If set to None, _capture = "run" will wait for the process to finish
			# before returning None
			"_wait": True,
			# If set to True, _capture set to "out", "err", or "both" will wait for user input
			"_block": False,
			"_timeout_stdout": None,
			"_timeout_stderr": None,
			"_buffer_size_stdout": 0,
			"_buffer_size_stderr": 0,
			"_chunk_size_stdout": -1,
			"_chunk_size_stderr": -1,
			"_input": None,
			"_posix": True,
			"_async": False,
			"_stop_threads": False,
		}

		self._settings.functions = (
			"frosting_",
			"f_",
			"print_",
		)

		self._shells: List[str] = [
			"zsh",
			"bash",
			"sh",
			"fish",
			"xonsh",
			"elvish",
			"tcsh",
			"powershell",
			"cmd",
		]
		self._shell = (
			True if self._program in self._shells else False
		)

		# Returns the default allowed types and adds "str" as well
		self._allowed_type_names: List[str] = check_type(
			lst=True
		) + ["str"]

		self._captures: Tuple[str] = (
			"stdout",
			"stderr",
			"both",
			"run",
		)

		# Update these
		self._return_categories: Tuple[str] = (
			"stdout",
			"stderr",
			"return_code",
			"return_codes",
			"command",
			"tea",
			"verbosity",
		)

		sa = kwargs.pop("_starter_args", [])
		ska = kwargs.pop("_starter_kwargs", dict())
		self._args = list(args) + list(
			[sa]
			if isinstance(sa, (str, bytes, bytearray))
			else list(sa)
		)
		kwargs.update(ska)
		self._kwargs = kwargs

	# DONE: Something's wrong with this, or returning the generator created by this
	# DONE: Always remember a generator is used up
	def _convert_to_generator(self, input):
		yield from input

	def _convert_to_type(self, input, _type):
		if isinstance(input, frosting):
			input = [
				TextWrapper(
					break_long_words = False,
				).fill(line) for line in input()[0].split("\n")
			][:-1]
		if _type.__name__ == "str":
			return " ".join(input)
		if _type.__name__ in ("generator", "iter"):
			return self._convert_to_generator(input)
		else:
			return _type(input)

	def _subcommand_check(self, subcommand):
		if subcommand in self._settings.functions:
			self._sub.function = subcommand
			self._sub.unprocessed = (
				"supercalifragilisticexpialidocious"
			)
		elif subcommand == "supercalifragilisticexpialidocious":
			self._sub.unprocessed = (
				"supercalifragilisticexpialidocious"
			)
		else:
			self._sub.unprocessed = subcommand
			self._sub.processed = subcommand.replace("_", "-")

	def __getattr__(self, subcommand):
		def inner(*args, **kwargs):
			try:
				self._subcommand_check(subcommand)
				self._set_and_process(*args, **kwargs)
				return self._return_frosted_output()
			finally:
				self._set(_reset=True)

		return inner

	def _set_and_process(self, *args, **kwargs):

		self._set(_setup=True)

		set_with_sub = partial(
			self._set, _subcommand=self._sub.unprocessed
		)

		self._args, self._kwargs = set_with_sub(
			*self._args, _calling=True, **self._kwargs,
		)

		args, kwargs = set_with_sub(
			*args, _calling=True, **kwargs,
		)

		set_with_sub(_final=True,)

		set_with_sub(_apply=True,)

		process_with_sub = partial(
			self._process_args_kwargs,
			_subcommand=self._sub.unprocessed,
		)

		process_with_sub(
			*self._args,
			_calling=True,
			_starter_regular="starter",
			**self._kwargs,
		)

		process_with_sub(
			*args,
			_calling=True,
			_starter_regular="regular",
			**kwargs,
		)

		process_with_sub(_final=True,)

	def add_types_(self, *args):
		self._allowed_type_names = (
			self._allowed_type_names + list(args)
		)

	def add_shells_(self, *args):
		self._shells = self._shells + list(args)

	def __deepcopy__(self):
		return self.__class__(
			_program,
			_baked_commands=D(self._command.baked),
			_baked_settings=D(self._settings.baked),
		)

	def __iter__(self):
		self.n = 0

		self._subcommand_check("supercalifragilisticexpialidocious")
		self._set_and_process()

		if isinstance(
			output := self._return_frosted_output(),
			dict,
		):
			self.__next_output = list(output["stderr" if self._capture == "stderr" else "stdout"])
		elif isinstance(output, (str, bytes, bytearray)):
			self.__next_output = [output]
		else:
			self.__next_output = list(output)

		return self

	def __next__(self):
		if self.n < len(self.__next_output):
			self.n += 1
			return self.__next_output[self.n - 1]
		else:
			raise StopIteration
