import sublime, sublime_plugin, subprocess, string, random, hashlib, struct, decimal

# For ST3
def plugin_loaded():
    global sett
    sett = sublime.load_settings("UniQTools.sublime-settings")

class UniqAlnumCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selection in self.view.sel():
			if len(selection) > 0:
				self.view.replace(edit, selection, self.alnum_from_string(self.view.substr(selection)))
			else:
				self.view.insert(edit, selection.begin(), self.alnum_generator())

	def alnum_generator(self):
		alnumSettings = sett.get("Alnum")
		length = alnumSettings.get("length", 25)
		if length < 1:
			length = 25
		length -= 1 # first character will be generated separately (newId)
		alphabet = string.ascii_lowercase + string.digits
		newId = random.choice(alphabet[:-10])
		rest = "".join(random.choice(alphabet) for x in range(length))
		return newId + rest

	def alnum_from_string(self, st):
		decimal.getcontext().prec = 60
		sh = hashlib.sha1(st).digest()
		byt = struct.unpack('20B', sh)

		val = 0
		for item in byt:
			val = (decimal.Decimal(val) * decimal.Decimal(256)) + decimal.Decimal(item)

		val,digit = divmod(val,26)
		alnum = chr(ord('a') + digit)
		alphabet = string.ascii_lowercase + string.digits

		for i in range(0, 24):
			val, digit = divmod(val, 36)
			alnum += alphabet[int(digit)]

		return alnum

class UniqPhpUnserializeCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		sel = self.view.sel()

		for region in sel:
			word = self.view.word(region)
			text = self.view.substr(word)

			cleanText = text.replace("'", "\\'")
			unserialized = subprocess.Popen(["php",
											 "-r",
											 "ini_set('display_errors', 1); var_export(unserialize('" + cleanText + "'));"],
											stdout=subprocess.PIPE).communicate()[0]

			if unserialized != "false" or text == 'b:0;':
				self.view.replace(edit, region, unserialized.decode("utf-8"))
			else:
				pass

class UniqPhpSerializeCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		sel = self.view.sel()

		for region in sel:
			word = self.view.word(region)
			text = self.view.substr(word)

			serialized = subprocess.Popen(["php",
											 "-r",
											 "ini_set('display_errors', 1); echo serialize(" + text + ");"],
											stdout=subprocess.PIPE).communicate()[0]

			self.view.replace(edit, region, serialized.decode("utf-8"))
