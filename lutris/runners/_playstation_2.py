from lutris.runners.runner import Runner
from lutris.util import system


class _playstation_2(Runner):
    human_name = "Sony Playstation 2"
    description = "Runs PS2 Games"
    platforms = ['Sony Playstation 2']
    runner_executable = '/mnt/data/emulators/emulator_scripts/playstation_2/scripts/pcsx2_game.sh'
    #runner_executable = '/mnt/data/emulators/emulator_scripts/playstation_2/scripts/ps2_game_retro.sh'
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
