#!/usr/bin/env python

from enum import Enum
from setuptools import setup
from setuptools.command.install import install
import os
import json

# ░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░
# ░░                                          ░░
# ░░                                          ░░
# ░░    SIMBASHLOG NOTIFIER CONFIGURATION     ░░
# ░░                                          ░░
# ░░                                          ░░
# ░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░

class NotifierConfig(Enum):
    NAME = 'simbashlog-matrix-notifier'
    VERSION = '1.0.1'
    DESCRIPTION = 'simbashlog-notifier for matrix.org'
    AUTHOR = 'Fabian Fuchs'
    PYTHON_VERSION = '>=3.10'
    URL = 'https://github.com/fuchs-fabian/simbashlog-matrix-notifier'
    KEYWORDS = [
        'matrix',
    ]
    INSTALL_REQUIRES = [
        'matrix-notify @ git+https://github.com/fuchs-fabian/matrix-notify-py.git@v2.0.0',
    ]
    NOTIFY_HELPER_VERSION = '1.6.1'
    CONFIG_FILE_KEY_REPLACEMENTS = {
        #'old_config_file_key': 'new_config_file_key',
    }

    @classmethod
    def get_data_for_config_file(cls):
        return {
            # General
            'min_required_log_level': '6',                  # 0-7
            'show_in_console_sent_message': 'true',         # or 'false'
            # Header
            'show_in_header_pid': 'false',                  # or 'true'
            # Body
            'show_in_body_log_file_result': 'false',        # or 'true'
            'show_in_body_log_file_content': 'false',       # or 'true'
            'show_in_body_summary_for_pid': 'false',        # or 'true'
            'show_in_body_summary_for_log_file': 'false',   # or 'true'
            # Footer
            'show_in_footer_log_file_names': 'false',       # or 'true'
            'show_in_footer_host': 'false',                 # or 'true'
            'show_in_footer_notifier_name': 'true',         # or 'false'

            # Notifier specific
            'use_e2e': 'true',
            'room_id': '!xyz:matrix.org',
            'access_token': 'your_access_token_here',
            'homeserver_url': 'https://matrix-client.matrix.org',
        }

# ░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░
# ░░                                          ░░
# ░░                                          ░░
# ░░      DO NOT MODIFY ANYTHING BELOW!       ░░
# ░░                                          ░░
# ░░                                          ░░
# ░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░

class PostInstallCommand(install):
    CONFIG_PATH = os.path.expanduser(f'~/.config/simbashlog-notifier/{NotifierConfig.NAME.value}/config.json')

    def run(self):
        install.run(self)

        if os.path.exists(self.CONFIG_PATH):
            print(f"Configuration file already exists at '{self.CONFIG_PATH}'")
            self.update_config_file()
        else:
            self.create_config_file()

    def create_config_file(self):
        os.makedirs(os.path.dirname(self.CONFIG_PATH), exist_ok=True)

        new_config_data = NotifierConfig.get_data_for_config_file()

        with open(self.CONFIG_PATH, 'w') as config_file:
            json.dump(new_config_data, config_file, indent=4)

        print(f"Configuration file created at '{self.CONFIG_PATH}'")

    def update_config_file(self):
        with open(self.CONFIG_PATH, 'r') as config_file:
            current_config = json.load(config_file)

        config_data = NotifierConfig.get_data_for_config_file()

        for old_key, new_key in NotifierConfig.CONFIG_FILE_KEY_REPLACEMENTS.value.items():
            if old_key in current_config and new_key not in current_config:
                current_config[new_key] = current_config.pop(old_key)

        updated_config_data = {key: current_config.get(key, config_data[key]) for key in config_data.keys()}

        with open(self.CONFIG_PATH, 'w') as config_file:
            json.dump(updated_config_data, config_file, indent=4)

        print(f"Configuration file updated at '{self.CONFIG_PATH}'")

setup(
    name=NotifierConfig.NAME.value,
    version=NotifierConfig.VERSION.value,
    description=NotifierConfig.DESCRIPTION.value,
    author=NotifierConfig.AUTHOR.value,
    license='GPL-3.0-or-later',
    url=NotifierConfig.URL.value,
    keywords=[
        'simbashlog',
        'logging-framework',
        'notify',
        'notifier',
        *NotifierConfig.KEYWORDS.value
    ],
    platforms=['Linux'],
    python_requires=NotifierConfig.PYTHON_VERSION.value,
    install_requires=[
        f'simbashlog-notify-helper @ git+https://github.com/fuchs-fabian/simbashlog-notify-helper-py.git@v{NotifierConfig.NOTIFY_HELPER_VERSION.value}',
        *NotifierConfig.INSTALL_REQUIRES.value
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts': [
            '{}={}:main'.format(NotifierConfig.NAME.value, NotifierConfig.NAME.value.replace('-', '_')),
        ],
    },
)
