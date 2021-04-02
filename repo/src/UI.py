import tkinter as tk

class UI():
	root = None
	expr = None

	## 	Function called after submit button is pressed.
	#	Takes 1 argument representing the expression.
	submit_callback = None

	def __init__(self):
		global submit_callback
		submit_callback = None

	def submit_expr(self):
		global submit_callback
		if submit_callback is None:
			print("submit_callback not defined!")
		else:
			print("submitting")
			submit_callback(self.get_expr())

	def setup(self,root):
		canvas = tk.Canvas(height=300, width=400)
		canvas.grid(columnspan=3, rowspan=2)

		global expr
		expr = tk.StringVar()

		label = tk.Label(textvariable=expr)
		label.grid(row=0, column=1)

		expr.set("Jozko ma dlhe nohy")

		button = tk.Button(text="Submit",height=3,width=5,command=self.submit_expr)
		button.grid(row=1,column=1)

	def start_loop(self):
		global root
		root = tk.Tk()
		root.title('Calc')

		self.setup(root)

		root.mainloop()


	def set_expr(self,new_expr):
		print("SS")
		global expr
		expr.set(new_expr)

	def get_expr(self):
		global expr
		return expr.get()

	def define_submit_expr(self,foo):
		global submit_callback
		submit_callback = foo

	

