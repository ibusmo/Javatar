from .commands import *
from .core.event_handler import *
from .core import (
    DependencyManager,
    ProjectRestoration,
    StateProperty
)
from .utils import (
    Constant
)


def plugin_loaded():
    EventHandler().register_handler(
        on_change,
        (
            EventHandler().ON_NEW |
            EventHandler().ON_ACTIVATED |
            EventHandler().ON_LOAD |
            EventHandler().ON_POST_SAVE |
            EventHandler().ON_CLONE
        )
    )
    EventHandler().register_handler(
        on_project_stable,
        (
            EventHandler().ON_CLOSE |
            EventHandler().ON_NEW |
            EventHandler().ON_POST_WINDOW_COMMAND
        )
    )
    Constant.startup()


def on_project_stable(view_or_window=None, command_name=None, args=None):
    ProjectRestoration().save_state()


def on_change(view):
    DependencyManager().refresh_dependencies()
    StateProperty().refresh_library_paths()
    StateProperty().refresh_source_folders()
