from lutris.runners.runner import Runner
from lutris.util import system


class _sega_32x(Runner):
    human_name = "Sega 32x"
    description = "Runs Sega 32x Games"
    platforms = ['Sega 32x']
    runner_executable = '/mnt/data/emulators/emulator_scripts/sega_32x/scripts/32x_game.sh'
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
