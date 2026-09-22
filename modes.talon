mode: command
mode: dictation
-
^mixed mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
