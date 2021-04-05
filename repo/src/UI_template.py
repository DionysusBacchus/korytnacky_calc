#   Sample program using the UI class

import UI


#   Your function that evaluates the expression
def evaluate(expr):
    expr = "*vyhodnotené '"+expr + "'*"
    return expr


#   Your function that is called when the '=' button is pressed.
#   Must take exactly 1 string argument, which is the displayed expression.
def get_expr(expr):
    expr = evaluate(expr)

    # Function that sets the displayed expression
    window.set_expr(expr)


#   Creates UI object. DOESN'T create a window
window = UI.UI()

#   Sets the function to be called when the '=' button is pressed
window.set_submit_callback(get_expr)

#   Creates the window. It loops until window is close, so nothing past this line
#   will execute while the window is open.
window.start_loop()

#   DEAD CODE
