import time

from talon import Module, actions, registry, scope, settings

mod = Module()
mod.setting(
    "dental_click_repeat_min_ms", type=int, default=100,
    desc="Minimum interval between dental clicks for repeat, in milliseconds",
)
mod.setting(
    "dental_click_repeat_max_ms", type=int, default=350,
    desc="Maximum interval between dental clicks for repeat, in milliseconds",
)

pending_click = None
current_modes = frozenset(scope.get("mode") or ())


def click_pair(previous, now, minimum, maximum):
    """Return the pending timestamp and whether this click completes a pair."""
    if previous is None:
        return now, False
    elapsed = now - previous
    if elapsed < minimum:
        return previous, False
    if elapsed <= maximum:
        return None, True
    return now, False


def on_update_contexts():
    global pending_click, current_modes
    modes = frozenset(scope.get("mode") or ())
    if modes != current_modes:
        pending_click = None
        current_modes = modes


registry.register("update_contexts", on_update_contexts)


@mod.action_class
class Actions:
    def dental_click_repeat():
        """Repeat the last command once after a pair of dental clicks."""
        global pending_click
        on_update_contexts()
        if "command" not in current_modes or "sleep" in current_modes:
            pending_click = None
            return
        minimum = settings.get("user.dental_click_repeat_min_ms") / 1000
        maximum = settings.get("user.dental_click_repeat_max_ms") / 1000
        if not 0 < minimum <= maximum:
            pending_click = None
            raise ValueError("Dental-click repeat requires 0 < minimum <= maximum")
        pending_click, repeat = click_pair(
            pending_click, time.monotonic(), minimum, maximum
        )
        if repeat:
            actions.core.repeat_command(1)
