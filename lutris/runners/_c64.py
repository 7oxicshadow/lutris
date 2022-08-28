from lutris.runners.runner import Runner
from lutris.util import system


class _c64(Runner):
    human_name = "Commodore 64"
    description = "Runs Commadore 64 Games"
    platforms = ['Commodore 64']
    runner_executable = '/mnt/data/emulators/emulator_scripts/commodore_64/scripts/vice_game.sh'
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
