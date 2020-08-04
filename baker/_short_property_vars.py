# From Imports
from gensing import tea, frosting

class _short_property_vars:

	@property
	def origin_(self):
		for store in self.__class__.stores_:
			if store is not None:
				return store.__callback__
		return self

	@property
	def chain_(self):
		return (store.__callback__ for store in self.__class__.stores_ if store is not None)

	@property
	def _capture(self):
		return self.__capture

	@_capture.setter
	def _capture(self, value):
		if value not in self._captures:
			raise TypeError(
				f'Sorry! Capture type "{value}" is not permitted! Choose from one of: [{(", ").join(self._captures)}]'
			)
		self.__capture = value

	@property
	def _print(self):
		return self.__print

	@_print.setter
	def _print(self, value):
		self.__print = bool(value)
		if value:
			self._str = True

	@property
	def _freezer(self):
		return self.__freezer

	@_freezer.setter
	def _freezer(self, value):
		try:
			self.__freezer
		except NameError:
			self.__freezer = value
		else:
			if self.__freezer != value:
				self.__freezer = value

	@property
	def _frosting(self):
		return self.__frosting

	@_frosting.setter
	def _frosting(self, value):
		self.__frosting = bool(value)
		if value:
			self._type = self._settings.defaults._type

	@property
	def _sudo(self):
		return self.__sudo

	@_sudo.setter
	def _sudo(self, value):
		if not isinstance(value, (dict, tea, frosting)):
			raise TypeError('Sorry! "_sudo" needs to be a tea, frosting, or dict-like object!')
		if len(value) > 1:
			raise ValueError('Sorry! The "_sudo" object can only have a single key-value item!')
		if (
			value and
			next(iter(value.keys())) not in ("i", "s")
		):
			raise ValueError('Sorry! The "_sudo" object can only take "i" or "s" as a key!')
		self.__sudo = value

	@property
	def _starter_kwargs(self):
		return self.__starter_args

	@_starter_kwargs.setter
	def _starter_kwargs(self, value):
		if not isinstance(value, (dict, tea, frosting)):
			raise TypeError('Sorry! "_starter_kwargs" needs to be a tea, frosting, or dict-like object!')
		self.__starter_kwargs = value

	@property
	def _regular_kwargs(self):
		return self.__regular_args

	@_regular_kwargs.setter
	def _regular_kwargs(self, value):
		if not isinstance(value, (dict, tea, frosting)):
			raise TypeError('Sorry! "_regular_kwargs" needs to be a tea, frosting, or dict-like object!')
		self.__regular_kwargs = value