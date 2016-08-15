import sublime, sublime_plugin

import re

class GenDocCommand(sublime_plugin.TextCommand):

	def get_indentation_level(self, line):

		''' This one already has a docstring '''

		p = re.compile('(\t+?)')
		# m = p.match(line)
		# m.group('ab')
		matches = re.findall(p, line)
		# print()
			# print(numbers, '*', letters)

		return len(matches)

	def find_function_defs(self):
		""" Find function """
		return self.view.find_all('def\s+[a-zA-Z_0-9]+\(([a-z]+)\)*')

	def find_uncommented_defs(self):
		return self.view.find_all('def\s+[a-zA-Z_0-9]+\(([a-z_,\s]+)\)*:[\s\t]*[^\'\s\t]')

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

	def test_get_line(self):

		view = self.view

		for i in range(100):
			print("Line #%d = %s" % (i, self.get_line(i)))

	def print_regions(self):
		print("Printing regions ... ")
		view = self.view

		print("%d selections" % len(view.sel()))

		# Walk through each region in the selection  
		for region in view.sel():  
			# Only interested in empty regions, otherwise they may span multiple  
			# lines, which doesn't make sense for this command.  
			print("Region = ", str(region))
			if region.empty():  
				# Expand the region to the full line it resides on, excluding the newline  
				line = view.line(region)
				lineContents = view.substr(line)

				print("Line Region = " + str(line))
				print("Line = " + lineContents)

				startrow, startcol = view.rowcol(line.a)
				endrow, endcol = view.rowcol(line.b)

				print("r1, c1 = (%d, %d)" % (startrow, startcol))
				print("r2, c2 = (%d, %d)" % (endrow, endcol))
			else:
				print("Region not empty")

	def run(self, edit):
		view = self.view # Just to save some space

		print("Running gen_docs ... \n")

		func_defs = self.find_uncommented_defs()

		for i, f in enumerate(func_defs):
			# lines = self.view.lines(f)
			print("(%d) : %s" % (i, self.view.substr(f)))



		# self.test_get_line()

		# self.print_regions()

		# first_cursor = view.sel()[0]
		# (row, col) = view.rowcol(first_cursor.begin())
		# # mock_line = '		(row,col) = self.view.rowcol(self.view.sel()[0].begin())'
		# print("row = {}, col = {}".format(row, col))

		# line = view.substr(view.line(view.sel()[0]))

		# print(view.sel()[0].begin(), view.sel()[0].begin())
		# print("Current line = '%s'" % (line))
		# print(view.line(2))

		# # def_name = self.get_line_def(line)
		# # print("def_name = " + str(def_name))

		# # if def_name:
		# 	# print(def_name)

		# indent = self.get_indentation_level(line)
		# print("Indentation level = " + str(indent))

		# scope = self.find_scope(row)
		# print()
		
