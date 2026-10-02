"""Navigate adjacent Firefox tabs regardless of its Ctrl+Tab preference."""

from talon import Context, actions

ctx = Context()
ctx.matches = """
os: linux
app: firefox
"""


@ctx.action_class("app")
class AppActions:
    def tab_next():
        actions.key("ctrl-pagedown")

    def tab_previous():
        actions.key("ctrl-pageup")
