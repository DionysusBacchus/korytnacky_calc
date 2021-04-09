##
# @file UI.py
#

import tkinter as tk


##
# 	@biref Class that creates a window with all UI elements for a calculator.
#	Window is displayed when the 'start_loop()' function is called.
class UI():
	## 	Root window
	root = None

	##	tkinter.Text variable. The main display of the calculator.
	#	Holds the displayed expression.
	display = None

	##	StringVar variable holding the displayed hint
	hint = None

	##	Bool variable that inidcates whether the currently displayed expression is the result of prevoius calculation
	displaying_result = False

	## 	External function called after submit button is pressed.
	#	Takes 1 argument representing the expression. Needs to be set using 'set_submit_callback()'.
	submit_callback = None

	##	Dictionary mapping key symbols to functions. Used in 'key_pressed()'.
	#	Initialized in the constructor.
	key_handler = None

	error_messages = "Nulou se nedá dělit", "Neplatný vstup", "Chyba syntaxe"

	##	Constructor only initializes global variables. To create the window use 'start_loop()'.
	def __init__(self):
		self.key_handler = {
			"0": self.b_0,
			"1": self.b_1,
			"2": self.b_2,
			"3": self.b_3,
			"4": self.b_4,
			"5": self.b_5,
			"6": self.b_6,
			"7": self.b_7,
			"8": self.b_8,
			"9": self.b_9,
			"KP_0": self.b_0,
			"KP_1": self.b_1,
			"KP_2": self.b_2,
			"KP_3": self.b_3,
			"KP_4": self.b_4,
			"KP_5": self.b_5,
			"KP_6": self.b_6,
			"KP_7": self.b_7,
			"KP_8": self.b_8,
			"KP_9": self.b_9,
			"e": self.b_e,
			"p": self.b_pi,
			"comma": self.b_sepp,
			"period": self.b_dot,
			"KP_Decimal": self.b_dot,
			"a": self.b_ans,
			"A": self.b_ans,
			"parenleft": self.b_left_br,
			"parenright": self.b_right_br,
			"x": self.b_times,
			"asterisk": self.b_times,
			"KP_Multiply": self.b_times,
			"slash": self.b_div,
			"KP_Divide": self.b_div,
			"plus": self.b_plus,
			"KP_Add": self.b_plus,
			"minus": self.b_minus,
			"KP_Subtract": self.b_minus,
			"exclam": self.b_fact,
			"bar": self.b_abs,
			"percent": self.b_mod,
			"asciicircum": self.b_pow,
			"BackSpace": self.b_back,
			"Delete": self.b_ac,
			"Return": self.submit_expr,
			"equal": self.submit_expr,
			"KP_Enter": self.submit_expr,
			"Left": lambda: 1,
			"Right" : lambda: 1,
			"Up": lambda: 1,
			"Down": lambda: 1,
			"End": lambda: 1,
			"Home": lambda: 1,
			"KP_Left": lambda: 1,
			"KP_Right": lambda: 1,
			"KP_Up": lambda: 1,
			"KP_Down": lambda: 1,
			"KP_End": lambda: 1,
			"KP_Home": lambda: 1
		}

	##	Function called when the submit button is pressed.
	#	Calls the 'submit_callback()' function with the currently displayed expression.
	def submit_expr(self):
		if self.submit_callback is None:
			print("submit_callback not defined!")
		else:
			self.submit_callback(self.get_expr())
			self.displaying_result = True
		return "break"

	##	Function creates a button with given text on given position in the grid.
	#	@param root Root window
	#	@param text Text of the button
	#	@param row Row in which the button will be placed
	#	@param col Column in which the button will be placed
	#	@param hint_text Text to be displayed on the hint display when hovered over
	#	@param extra Optional arguments passed to tk.Button() constructor
	def create_button(self,root,text,row,col,hint_text="",**extra):
		b = tk.Button(root,text=text,width=4,height=2,activebackground="#b7e4c7",relief=tk.RAISED,**extra)
		b.grid(row=row,column=col)

		if hint_text != "":
			b.bind("<Enter>", lambda x: self.set_hint(hint_text))
			b.bind("<Leave>", lambda x: self.clear_hint())

	##	Function creates number buttons using 'create_button()'.
	#	@param root Root window
	#	@param l_col The left most column of the number buttons.
	#	@param extra Optional arguments passed to tk.Button() constructor
	def create_number_buttons(self,root,l_col,**extra):
		self.create_button(root, "0", 7, l_col,**extra,command=self.b_0)
		self.create_button(root, "1", 6, l_col,**extra,command=self.b_1)
		self.create_button(root, "2", 6, l_col+1,**extra,command=self.b_2)
		self.create_button(root, "3", 6, l_col+2,**extra,command=self.b_3)
		self.create_button(root, "4", 5, l_col,**extra,command=self.b_4)
		self.create_button(root, "5", 5, l_col+1,**extra,command=self.b_5)
		self.create_button(root, "6", 5, l_col+2,**extra,command=self.b_6)
		self.create_button(root, "7", 4, l_col,**extra,command=self.b_7)
		self.create_button(root, "8", 4, l_col+1,**extra,command=self.b_8)
		self.create_button(root, "9", 4, l_col+2,**extra,command=self.b_9)

	##	Function creates all buttons on the root window
	#	@param root Root window
	def create_buttons(self,root):
		num_but_color = "#02c39a"
		color_A = "#00a896"
		color_B = "#028090"
		color_C = "#e76f51"

		font = ("Ubuntu",16)

		self.create_number_buttons(root,2,font=font,bg=num_but_color)
		self.create_button(root,".",7,3,font=font,command=self.b_dot,hint_text="Desetinná tečka:     2.5", bg=color_A)
		self.create_button(root, "Ans", 7, 4,font=font,command=self.b_ans,hint_text="Poslední výsledek:     Ans*2", bg=color_A)

		self.create_button(root, "π", 3, 0,font=font,command=self.b_pi,hint_text="Pí:     3.141592653589793", bg=color_B)
		self.create_button(root, "e", 3, 1,font=font,command=self.b_e,hint_text="Eulerovo číslo:     2.718281828459045", bg=color_B)

		self.create_button(root,"%" ,6,0,font=font,command=self.b_mod,hint_text="Modulo:     8%3", bg=color_B)
		self.create_button(root, ",", 5, 1,font=font,command=self.b_sepp,hint_text="Oddělovač argumentú pro √(x,n)", bg=color_B)
		self.create_button(root,"^" ,4,1,font=font,command=self.b_pow,hint_text="Umocnění:     2^e", bg=color_A)
		self.create_button(root,"√" ,4,0,font=font,command=self.b_sqrt,hint_text="Odmocnina:     √81", bg=color_A)
		self.create_button(root,"√(x,n)",5,0,font=font,command=self.b_nroot,hint_text="Odmocnina n-tého řádu z x  √(x,n):     √(27,3)", bg=color_A)
		self.create_button(root,"!",6,1,font=font,command=self.b_fact,hint_text="Faktoriál:     5!", bg=color_B)
		self.create_button(root,"|",7,1,font=font,command=self.b_abs,hint_text="Absolutní hodnota:     |-8|", bg=color_B)

		self.create_button(root,"<-",3,5,font=font,command=self.b_back,hint_text="Smazat poslední znak",bg=color_C)
		self.create_button(root,"AC",3,6,font=font,command=self.b_ac,hint_text="Smazat všechno", bg=color_C)
		self.create_button(root, "(", 4, 5, font=font, command=self.b_left_br, bg=color_B)
		self.create_button(root, ")", 4, 6, font=font, command=self.b_right_br, bg=color_B)
		self.create_button(root,"x",5,5,font=font,command=self.b_times, bg=color_A)
		self.create_button(root,"/",5,6,font=font,command=self.b_div, bg=color_A)
		self.create_button(root,"+",6,5,font=font,command=self.b_plus, bg=color_A)
		self.create_button(root,"-",6,6,font=font,command=self.b_minus, bg=color_A)	
		b_eq=tk.Button(root,command=self.submit_expr,text="=",width=10,height=2,font=font,bg=num_but_color,relief=tk.RAISED,activebackground="#b7e4c7")
		b_eq.grid(columnspan=2,row=7,column=5)

	##	Function initializes all the UI elements.
	# 	Called from 'start_loop'.
	#	@param root The root window.
	def setup(self,root):
		root.title('kalkulačka')
		root.resizable(False, False)

		# Color setup. Button colors are in 'create_buttons()'
		root.configure(bg="#0f4c5c")
		display_color = "#0f4c5c"
		display_text_color = "#b7e4c7"
		hint_color = "#028090"
		hint_text_color = "#00a896"

		# Hint properties
		hint_font = ("Ubuntu", 18)
		hint_width = 500

		# Creating hint
		self.hint = tk.StringVar()
		hint_display = tk.Label(root,textvariable=self.hint,font=hint_font,bg=hint_color,fg=hint_text_color,width=36,wraplength=hint_width,anchor="w")
		hint_display.grid(row=0,column=0,columnspan=7,pady=10,padx=10)


		# Display properties
		display_font = ("Ubuntu", 24)

		# Creating display
		self.display = tk.Text(root,width=25,height=5,font=display_font,bg=display_color,fg=display_text_color)
		self.display.configure(insertwidth=3,insertbackground=display_text_color,highlightthickness=0)
		self.display.grid(columnspan=7,rowspan=2,column=0,row=1,pady=40)
		self.display.bind("<Key>",self.key_pressed)
		self.create_buttons(root)

		self.display.focus_set()



	## 	Function starts the mainloop and displays the window.
	#	Must be called after the UI object has been created.
	#	Function loops until the window is closed.
	def start_loop(self):
		self.root = tk.Tk()

		self.setup(self.root)

		self.root.mainloop()

	def key_pressed(self,evt):
		if evt.keysym in self.key_handler:
			return self.key_handler[evt.keysym]()
		return "break"

	##	Function sets the displayed hint.
	#	@param new_hint New hint to be set.
	def set_hint(self,new_hint):
		self.hint.set(new_hint)

	## 	Function sets the displayed hint to "".
	def clear_hint(self):
		self.hint.set("")

	##	Function sets the displayed expression.
	#	@param new_expr New expression to be set.
	def set_expr(self,new_expr):
		self.display.delete(1.0,"end")
		self.display.insert(tk.INSERT,new_expr)


	## Function returns the currently displayed expression.
	def get_expr(self):
		return self.display.get("1.0",tk.END)

	## 	Function appends given string to the end of the displayed expression.
	#	@param add String to be appended.
	def append_expr(self,add):
		self.display.insert(tk.INSERT,add)





	## 	Function sets the 'submit_callback' function.
	#	@param foo Function to be assigned to 'submit_callback'
	def set_submit_callback(self,foo):
		self.submit_callback = foo

	#	Function determines whither the displayed expression is an error message.
	def displaying_error(self):
		if self.get_expr()[:-1] in self.error_messages:
			return True
		return False

	##	Function modifies the displayed expression after evaluation according to parameters.
	#	If displayed expression is not a result, does nothing.
	#	By default, replaces result with "Ans".
	#	@param set_ans indicates whether the displayed result is to be replaced for "Ans" or "".
	#	@param insert_only indicates that the displayed result is to be cleared UNLESS the cursor is not at the end, in
	#		which case the result is left unchanged.
	#	@param insert_or_ans indicates that the displayed result is to be replaced for "Ans" UNLESS the cursor is not
	#		at the end, in which case the result is left unchanged.
	#	@param always_clear indicates whether the result is to be cleared regardless of what it is.
	def prepare_display(self,set_ans = True, insert_only = False, insert_or_ans = False, always_clear = False):
		if(not self.displaying_result):
			return

		self.displaying_result = False

		if (self.displaying_error() or always_clear):
			self.set_expr("")
			return


		if(insert_or_ans):
			if (self.display.index(tk.INSERT) == self.display.index("end-1c")):
				# Cursor is at the end
				self.set_expr("Ans")
			return


		if(insert_only):
			if(self.display.index(tk.INSERT) == self.display.index("end-1c")):
				# Cursor is at the end
				self.set_expr("")
			return


		if(set_ans):
			self.set_expr("Ans")



	## @section button on-click functions
	def b_0(self):
		self.prepare_display(insert_only=True)
		self.append_expr("0")
		return "break"

	def b_1(self):
		self.prepare_display(insert_only=True)
		self.append_expr("1")
		return "break"

	def b_2(self):
		self.prepare_display(insert_only=True)
		self.append_expr("2")
		return "break"

	def b_3(self):
		self.prepare_display(insert_only=True)
		self.append_expr("3")
		return "break"

	def b_4(self):
		self.prepare_display(insert_only=True)
		self.append_expr("4")
		return "break"

	def b_5(self):
		self.prepare_display(insert_only=True)
		self.append_expr("5")
		return "break"

	def b_6(self):
		self.prepare_display(insert_only=True)
		self.append_expr("6")
		return "break"

	def b_7(self):
		self.prepare_display(insert_only=True)
		self.append_expr("7")
		return "break"

	def b_8(self):
		self.prepare_display(insert_only=True)
		self.append_expr("8")
		return "break"

	def b_9(self):
		self.prepare_display(insert_only=True)
		self.append_expr("9")
		return "break"

	def b_dot(self):
		self.prepare_display(set_ans=False)
		self.append_expr(".")
		return "break"

	def b_ans(self):
		self.prepare_display(always_clear=True)
		self.append_expr("Ans")
		return "break"

	def b_pi(self):
		self.prepare_display(always_clear=True)
		self.append_expr("π")
		return "break"

	def b_e(self):
		self.prepare_display(always_clear=True)
		self.append_expr("e")
		return "break"

	def b_sepp(self):
		self.prepare_display(insert_only=True)
		self.append_expr(",")
		return "break"

	def b_left_br(self):
		self.prepare_display(insert_only=True)
		self.append_expr("(")
		return "break"

	def b_right_br(self):
		self.prepare_display(insert_only=True)
		self.append_expr(")")
		return "break"

	def b_times(self):
		self.prepare_display(insert_or_ans=True)
		self.append_expr("x")
		return "break"

	def b_div(self):
		self.prepare_display(insert_or_ans=True)
		self.append_expr("/")
		return "break"

	def b_plus(self):
		self.prepare_display(insert_or_ans=True)
		self.append_expr("+")
		return "break"

	def b_minus(self):
		self.prepare_display(insert_or_ans=True)
		self.append_expr("-")
		return "break"

	def b_fact(self):
		self.prepare_display()
		self.append_expr("!")
		return "break"

	def b_abs(self):
		self.prepare_display(always_clear=True)
		self.append_expr("||")
		self.display.mark_set(tk.INSERT, "insert-1c")
		return "break"

	def b_back(self):
		self.prepare_display(set_ans=False)
		last_3 = self.display.get("insert-3c","insert")
		if(last_3 == "Ans"):
			self.display.delete("insert-3c",tk.INSERT)
		else:
			self.display.delete("insert-1c")
		return "break"

	def b_ac(self):
		self.set_expr("")
		return "break"

	def b_mod(self):
		self.prepare_display(insert_or_ans=True)
		self.append_expr("%")
		return "break"

	def b_pow(self):
		self.prepare_display(insert_or_ans=True)
		self.append_expr("^()")
		self.display.mark_set(tk.INSERT, "insert-1c")
		return "break"

	def b_sqrt(self):
		self.prepare_display(always_clear=True)
		self.append_expr("√()")
		self.display.mark_set(tk.INSERT,"insert-1c")
		return "break"

	def b_nroot(self):
		self.prepare_display(always_clear=True)
		self.append_expr("√(,)")
		self.display.mark_set(tk.INSERT, "insert-2c")
		return "break"
