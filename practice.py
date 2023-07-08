import cmd

class Console(cmd.Cmd):

	use_rawinput = False
	def do_greet(self, line):
		print("Welcome {}".format(line))
	def do_EOF(self, line):
		return True
	def do_hello(self, line):
		""" print hello word to the console"""
		print("Hello {}".format(line))
	#def postloop(self):
	#	print()

	prompt = ""
	intro = "just playing with the cmd"

if __name__ == "__main__":
	import sys
	input = open(sys.argv[1],'rt')
	try:
		Console(stdin=input).cmdloop()
	finally:
		input.close()
