##
# @file UI.py
#


import tkinter as tk

##
# 	@biref Class that creates a window with all UI elements for a calculator.
#	Window is displayed when the 'start_loop()' function is called.
class UI():
	# 	Root window
	root = None

	#	StringVar variable holding the displayed expression
	expr = None

	# 	External function called after submit button is pressed.
	#	Takes 1 argument representing the expression. Needs to be set using 'set_submit_callback()'.
	submit_callback = None

	def __init__(self):
		global submit_callback
		submit_callback = None

	##	Function called when the submit button is pressed.
	#	Calls the 'submit_callback()' function with the currently displayed expression.
	def submit_expr(self):
		global submit_callback
		if submit_callback is None:
			print("submit_callback not defined!")
		else:
			submit_callback(self.get_expr())


	##	Function creates a button with given text on given position in the grid.
	#	@param root Root window
	#	@param text Text of the button
	#	@param row Row in which the button will be placed
	#	@param col Column in which the button will be placed
	def create_button(self,root,text,row,col,**extra):
		b = tk.Button(root,text=text,width=4,height=2,activebackground="#0096c7",relief=tk.RAISED,**extra)
		b.grid(row=row,column=col)

	##	Function creates number buttons using 'create_button()'.
	#	@param root Root window
	def create_number_buttons(self,root,**extra):
		self.create_button(root, "0", 7, 0,**extra,command=self.b_0)
		self.create_button(root, "1", 6, 0,**extra,command=self.b_1)
		self.create_button(root, "2", 6, 1,**extra,command=self.b_2)
		self.create_button(root, "3", 6, 2,**extra,command=self.b_3)
		self.create_button(root, "4", 5, 0,**extra,command=self.b_4)
		self.create_button(root, "5", 5, 1,**extra,command=self.b_5)
		self.create_button(root, "6", 5, 2,**extra,command=self.b_6)
		self.create_button(root, "7", 4, 0,**extra,command=self.b_7)
		self.create_button(root, "8", 4, 1,**extra,command=self.b_8)
		self.create_button(root, "9", 4, 2,**extra,command=self.b_9)

	##	Function creates all buttons on the root window
	#	@param root Root window
	def create_buttons(self,root):
		num_but_color = "#02c39a"
		color_A = "#00a896"
		color_B = "#028090"
		color_C = "#e76f51"

		font = ("Ubuntu",16)

		self.create_number_buttons(root,font=font,bg=num_but_color)
		self.create_button(root,".",7,1,font=font,command=self.b_dot,bg=color_A)
		self.create_button(root, "Ans", 7, 2,font=font,command=self.b_ans,bg=color_A)

		self.create_button(root, "π", 3, 0,font=font,command=self.b_pi,bg=color_B)
		self.create_button(root, "e", 3, 1,font=font,command=self.b_e,bg=color_B)

		self.create_button(root,"(",4,3,font=font,command=self.b_left_br,bg=color_B)
		self.create_button(root,")",4,4,font=font,command=self.b_right_br,bg=color_B)
		self.create_button(root,"x",5,3,font=font,command=self.b_times,bg=color_A)
		self.create_button(root,"/",5,4,font=font,command=self.b_div,bg=color_A)
		self.create_button(root,"+",6,3,font=font,command=self.b_plus,bg=color_A)
		self.create_button(root,"-",6,4,font=font,command=self.b_minus,bg=color_A)
		self.create_button(root,"!",7,3,font=font,command=self.b_fact,bg=color_B)
		self.create_button(root,"|",7,4,font=font,command=self.b_abs,bg=color_B)

		self.create_button(root,"<-",4,5,font=font,command=self.b_back,bg=color_C)
		self.create_button(root,"AC",4,6,font=font,command=self.b_ac,bg=color_C)
		self.create_button(root,"%" ,5,5,font=font,command=self.b_mod,bg=color_B)
		self.create_button(root,"^" ,5,6,font=font,command=self.b_pow,bg=color_B)
		self.create_button(root,"√" ,6,5,font=font,command=self.b_sqrt,bg=color_B)
		self.create_button(root,"n√",6,6,font=font,command=self.b_nroot,bg=color_B)

		b_eq=tk.Button(root,command=self.submit_expr,text="=",width=10,height=2,font=font,bg=color_A,relief=tk.RAISED,activebackground="#0096c7")
		b_eq.grid(columnspan=2,row=7,column=5)

	##	Function initializes all the UI elements.
	# 	Called from 'start_loop'.
	#	@param root The root window.
	def setup(self,root):
		root.title('kalkulačka')
		root.resizable(False, False)

		# Color setup. Button colors are in 'create_buttons()'
		root.configure(bg="#0f4c5c")
		display_color = "#0f4c5c"	#	"#f0f3bd"
		display_text_color = "#b7e4c7"

		display_font = ("Ubuntu", 24)
		display_width = 500
		global expr
		expr = tk.StringVar()
		expr.set("-14x(-2.5)+7")

		display = tk.Label(root,textvariable=expr,font=display_font,bg=display_color,fg=display_text_color)
		display.configure(wraplength=display_width)
		display.grid(columnspan=8,rowspan=3,column=0,row=0,pady=40)

		self.create_buttons(root)


	## 	Function starts the mainloop and displays the window.
	#	Must be called after the UI object has been created.
	#	Function loops until the window is closed.
	def start_loop(self):
		global root
		root = tk.Tk()

		self.setup(root)

		root.mainloop()

	##	Function sets the displayed expression.
	#	@param new_expr New expression to be set.
	def set_expr(self,new_expr):
		global expr
		expr.set(new_expr)

	## Function returns the currently displayed expression.
	def get_expr(self):
		global expr
		return expr.get()

	## 	Function appends given string to the end of the displayed expression.
	#	@param add String to be appended.
	def append_expr(self,add):
		expr = self.get_expr()
		expr += add
		self.set_expr(expr)

	## Function sets the 'submit_callback' function.
	#	@param foo Function to be assigned to 'submit_callback'
	def set_submit_callback(self,foo):
		global submit_callback
		submit_callback = foo

	## @section button on-click functions
	def b_0(self):
		self.append_expr("0")

	def b_1(self):
		self.append_expr("1")

	def b_2(self):
		self.append_expr("2")

	def b_3(self):
		self.append_expr("3")

	def b_4(self):
		self.append_expr("4")

	def b_5(self):
		self.append_expr("5")

	def b_6(self):
		self.append_expr("6")

	def b_7(self):
		self.append_expr("7")

	def b_8(self):
		self.append_expr("8")

	def b_9(self):
		self.append_expr("9")

	def b_dot(self):
		self.append_expr(".")

	def b_ans(self):
		self.append_expr("Ans")

	def b_pi(self):
		self.append_expr("π")

	def b_e(self):
		self.append_expr("e")

	def b_left_br(self):
		self.append_expr("(")

	def b_right_br(self):
		self.append_expr(")")

	def b_times(self):
		self.append_expr("x")

	def b_div(self):
		self.append_expr("/")

	def b_plus(self):
		self.append_expr("+")

	def b_minus(self):
		self.append_expr("-")

	def b_fact(self):
		self.append_expr("!")

	def b_abs(self):
		self.append_expr("|")

	def b_back(self):
		expr = self.get_expr()
		expr = expr[0:-1]
		self.set_expr(expr)

	def b_ac(self):
		self.set_expr("")

	def b_mod(self):
		self.append_expr("%")

	def b_pow(self):
		self.append_expr("^")

	def b_sqrt(self):
		self.append_expr("√")

	def b_nroot(self):
		self.append_expr("√(")





