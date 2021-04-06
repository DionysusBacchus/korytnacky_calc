

import UI
import mathlib


window = UI.UI()

mathlib.set_set_expr(window.set_expr)

window.set_submit_callback(mathlib.submit)
window.start_loop()