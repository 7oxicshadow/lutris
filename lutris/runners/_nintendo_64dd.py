from lutris.runners.runner import Runner
from lutris.util import system


class _nintendo_64dd(Runner):
    human_name = "Nintendo 64DD"
    description = "Runs 64DD Games"
    platforms = ['Nintendo 64DD']
    runner_executable = '/mnt/data/emulators/emulator_scripts/nintendo_64dd/scripts/64dd_game.sh'
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
