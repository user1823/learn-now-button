from aqt import gui_hooks
from aqt.browser import Browser

from .config import config
from .learn_now import add_learn_now_button


def on_browser_menus_did_init(self: Browser) -> None:
    add_learn_now_button(self, shortcut=config.learn_shortcut)


def init() -> None:
    gui_hooks.browser_menus_did_init.append(on_browser_menus_did_init)
