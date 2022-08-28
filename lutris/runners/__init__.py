"""Runner loaders"""
from collections import defaultdict

__all__ = [
    # Custom
    "_3do", "_3ds", "_amiga_500", "_amiga_cd32", "_amstrad_cpc464", "_arcade", "_arcade_vm", "_c64", "_laserdisc", "_neo_geo",
    "_nintendo_n64", "_nintendo_64dd", "_nintendo_nes", "_pc", "_playstation", "_ps3", "_psp", "_saturn", "_scummvm", "_sega_32x",
    "_sega_cd", "_sega_mastersystem", "_sega_megadrive", "_sinclair_zxspectrum", "_snes", "_switch", "_wii_gc",
    "_wii_u", "_xbox", "_playstation_2", "_triforce", "_gb_gba", "_dreamcast", "_model2", "_model3", "_nds", 
    "_xbox360", "_nintendo_virtualboy", "_sega_chihiro", "_dosbox", "_atomiswave_naomi","_hand_held","_jaguar","_philips_cd_i",
    "_amiga_cdtv","_pc_egs","_pc_steam", "_sega_gamegear"
]
ADDON_RUNNERS = {}
RUNNER_PLATFORMS = {}


class InvalidRunner(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class RunnerInstallationError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class NonInstallableRunnerError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def get_runner_module(runner_name):
    if runner_name not in __all__:
        raise InvalidRunner("Invalid runner name '%s'" % runner_name)
    return __import__("lutris.runners.%s" % runner_name, globals(), locals(), [runner_name], 0)


def import_runner(runner_name):
    """Dynamically import a runner class."""
    if runner_name in ADDON_RUNNERS:
        return ADDON_RUNNERS[runner_name]

    runner_module = get_runner_module(runner_name)
    if not runner_module:
        return None
    return getattr(runner_module, runner_name)


def import_task(runner, task):
    """Return a runner task."""
    runner_module = get_runner_module(runner)
    if not runner_module:
        return None
    return getattr(runner_module, task)


def get_installed(sort=True):
    """Return a list of installed runners (class instances)."""
    installed = []
    for runner_name in __all__:
        runner = import_runner(runner_name)()
        if runner.is_installed():
            installed.append(runner)
    return sorted(installed) if sort else installed


def inject_runners(runners):
    for runner_name in runners:
        ADDON_RUNNERS[runner_name] = runners[runner_name]
        __all__.append(runner_name)


def get_runner_names():
    return {
        runner: import_runner(runner)().human_name for runner in __all__
    }


def get_platforms():
    """Return a dictionary of all supported platforms with their runners"""
    platforms = defaultdict(list)
    for runner_name in __all__:
        runner = import_runner(runner_name)()
        for platform in runner.platforms:
            platforms[platform].append(runner_name)
    return platforms


RUNNER_NAMES = {}  # This needs to be initialized at startup with get_runner_names
