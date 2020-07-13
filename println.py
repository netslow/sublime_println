import sublime
import sublime_plugin
import re


class SurroundWithPrintCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				line = self.view.line(region)
				lineContents = self.view.substr(line)
				indent = re.findall(r'^\s*', lineContents)[0]
				resultText = indent+ 'print(' + lineContents.strip() + ')'
				self.view.replace(edit, line, resultText)
				(row,col) = self.view.rowcol(region.begin())
				self.view.run_command("goto_line", {"line": row+2})

