import sublime, sublime_plugin

import re

class GenDocCommand(sublime_plugin.TextCommand):

	def get_indentation_level(self, line):
		p = re.compile('(\t+?)')
		# m = p.match(line)
		# m.group('ab')
		matches = re.findall(p, line)
		# print()
			# print(numbers, '*', letters)

		return len(matches)

	def get_line_def(self, line):
		p = re.compile('def\s+[a-zA-Z_0-9]+\(([a-z]+)\)*') #TODO: Find official regex pattern
		matches = re.findall(p, line)
		print(matches)
		if len(matches):
			return matches[0]
		else:
			return None


	def find_scope(self, line_number):
		found = False
		indent = self.get_indentation_level(self.get_line(line_number))
		scope = [line_number]
		while not found and line_number > 0:

			line_number -= 1
			line_up = self.get_line(line_number)
			indent_up = self.get_indentation_level(line_up)

			print("line_number=%d"%line_number)
			print("line up = %s" % line_up)
			print("indent = %d" % indent_up)

			if indent_up != indent:
				print("Stop")
				break

			scope.append(line_up)

		return scope

	def get_line(self, line_number):
		view = self.view # Just to save some space
		line = view.substr(view.line(line_number))
		return line

	def run(self, edit):
		view = self.view # Just to save some space

		print("Hello\n")

		first_cursor = view.sel()[0]
		(row,col) = view.rowcol(first_cursor.begin())
		# mock_line = '		(row,col) = self.view.rowcol(self.view.sel()[0].begin())'
		print(str(self.view.sel()[0]))

		line = view.substr(view.line(view.sel()[0]))

		print(view.sel()[0].begin(), view.sel()[0].begin())
		print("Current line = '%s'" % (line))
		print(view.line(2))

		def_name = self.get_line_def(line)
		print("def_name = " + str(def_name))

		if def_name:
			print(def_name)

		# indent = self.get_indentation_level(line)
		# print("Indentation level = " + str(indent))

		# scope = self.find_scope(21)
		# print()
		
