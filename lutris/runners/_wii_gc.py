from lutris.runners.runner import Runner
from lutris.util import system


class _wii_gc(Runner):
    human_name = "Nintendo Wii/GC"
    description = "Runs Nintendo Wii/GC Games"
    platforms = ['Nintendo GC/Wii']
    runner_executable = '/mnt/data/emulators/emulator_scripts/wii_gamecube/scripts/dolphin_game.sh'
    game_options = [{
        'option': 'main_file',
        'type': 'file',
        'label': 'Game executable or directory'
    }]
    runner_options = [
        {
            'option': 'fullscreen',
            'type': 'bool',
            'label': 'Fullscreen',
            'default': True
        }
    ]

    def play(self):
        """Run the game."""
        main_file = self.game_config.get('main_file') or ''
        if not system.path_exists(main_file):
            return {'error': 'FILE_NOT_FOUND', 'file': main_file}

        arguments = [self.get_executable()]

        arguments.append(main_file)
        
        return {"command": arguments}
