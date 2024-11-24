#!/usr/bin/env python3

'''
NOTES:

For more information:
- https://github.com/fuchs-fabian/matrix-notify-py
'''

import sys
from enum import Enum
import simbashlog_notify_helper as snh # type: ignore

# simbashlog-notifier specific imports
import matrix_notify as mn # type: ignore

SIMBASHLOG_NOTIFIER_NAME = "simbashlog-matrix-notifier"

class NotifierConfigField(Enum):
    # General
    MIN_REQUIRED_LOG_LEVEL = "min_required_log_level"
    SHOW_IN_CONSOLE_SENT_MESSAGE = "show_in_console_sent_message"
    # Header
    SHOW_IN_HEADER_PID = "show_in_header_pid"
    # Body
    SHOW_IN_BODY_LOG_FILE_RESULT = "show_in_body_log_file_result"
    SHOW_IN_BODY_LOG_FILE_CONTENT = "show_in_body_log_file_content"
    SHOW_IN_BODY_SUMMARY_FOR_PID = "show_in_body_summary_for_pid"
    SHOW_IN_BODY_SUMMARY_FOR_LOG_FILE = "show_in_body_summary_for_log_file"
    # Footer
    SHOW_IN_FOOTER_LOG_FILE_NAMES = "show_in_footer_log_file_names"
    SHOW_IN_FOOTER_HOST = "show_in_footer_host"
    SHOW_IN_FOOTER_NOTIFIER_NAME = "show_in_footer_notifier_name"

    # Notifier specific
    USE_E2E = "use_e2e"
    ROOM_ID = "room_id"
    ACCESS_TOKEN = "access_token"
    HOMESERVER_URL = "homeserver_url"

    def __str__(self):
        return self.value

def load_config() -> snh.NotifierConfig:
    try:
        config_data = snh.NotifierConfig.get_data(SIMBASHLOG_NOTIFIER_NAME, NotifierConfigField)
    except Exception as e:
        print(f"An error occurred while the config file was being processed:\n{e}")
        sys.exit(1)

    return snh.NotifierConfig(
        # General
        min_required_log_level=config_data[
            NotifierConfigField.MIN_REQUIRED_LOG_LEVEL.value
        ],
        show_in_console_sent_message=config_data[
            NotifierConfigField.SHOW_IN_CONSOLE_SENT_MESSAGE.value
        ].lower() == "true",

        # Header
        show_in_header_pid=config_data[
            NotifierConfigField.SHOW_IN_HEADER_PID.value
        ].lower() == "true",

        # Body
        show_in_body_log_file_result=config_data[
            NotifierConfigField.SHOW_IN_BODY_LOG_FILE_RESULT.value
        ].lower() == "true",
        show_in_body_log_file_content=config_data[
            NotifierConfigField.SHOW_IN_BODY_LOG_FILE_CONTENT.value
        ].lower() == "true",
        show_in_body_summary_for_pid=config_data[
            NotifierConfigField.SHOW_IN_BODY_SUMMARY_FOR_PID.value
        ].lower() == "true",
        show_in_body_summary_for_log_file=config_data[
            NotifierConfigField.SHOW_IN_BODY_SUMMARY_FOR_LOG_FILE.value
        ].lower() == "true",

        # Footer
        show_in_footer_log_file_names=config_data[
            NotifierConfigField.SHOW_IN_FOOTER_LOG_FILE_NAMES.value
        ].lower() == "true",
        show_in_footer_host=config_data[
            NotifierConfigField.SHOW_IN_FOOTER_HOST.value
        ].lower() == "true",
        show_in_footer_notifier_name=config_data[
            NotifierConfigField.SHOW_IN_FOOTER_NOTIFIER_NAME.value
        ].lower() == "true",

        # Notifier specific
        use_e2e=config_data[
            NotifierConfigField.USE_E2E.value
        ].lower() == "true",
        room_id=config_data[
            NotifierConfigField.ROOM_ID.value
        ],
        access_token=config_data[
            NotifierConfigField.ACCESS_TOKEN.value
        ],
        homeserver_url=config_data[
            NotifierConfigField.HOMESERVER_URL.value
        ]
    )

def get_min_required_log_level(config: snh.NotifierConfig) -> int:
    if config.min_required_log_level is not None:
        min_required_log_level = int(config.min_required_log_level)

        if not min_required_log_level in range(0, 8):
            print(f"Invalid minimum required log level'{min_required_log_level}'")
            sys.exit(1)

        return min_required_log_level

    return 7

def create_message(config: snh.NotifierConfig, stored_log_info: snh.StoredLogInfo) -> str:
    builder = snh.MessageBuilder(
        stored_log_info = stored_log_info,
        notifier_name = SIMBASHLOG_NOTIFIER_NAME,
        apply_heading = lambda content: mn.Helper.HTML.Tag.H3.format(content),
        apply_subheading = lambda content: mn.Helper.HTML.Tag.H4.format(content),
        apply_paragraph = lambda content: mn.Helper.HTML.Tag.PARAGRAPH.format(content),
        apply_code = lambda content: mn.Helper.HTML.Tag.CODE.format(content),
        apply_bold = lambda content: mn.Helper.HTML.Tag.BOLD.format(content),
        apply_italic = lambda content: mn.Helper.HTML.Tag.ITALIC.format(content)
    )

    builder.add_header(
        show_pid=config.show_in_header_pid
    ).add_body(
        show_log_file_result=config.show_in_body_log_file_result,
        show_log_file_content=config.show_in_body_log_file_content,
        show_summary_for_pid=config.show_in_body_summary_for_pid,
        show_summary_for_log_file=config.show_in_body_summary_for_log_file
    ).add_footer(
        show_log_file_names=config.show_in_footer_log_file_names,
        show_host=config.show_in_footer_host,
        show_notifier_name=config.show_in_footer_notifier_name
    )

    return builder.build()

def perform_action(config: snh.NotifierConfig, stored_log_info: snh.StoredLogInfo, message: str):
    notifier = mn.MatrixNotifier(
        room_id=config.room_id,
        access_token=config.access_token,
        homeserver_url=config.homeserver_url
    )

    html_message = mn.Helper.HTML.replace_spaces_and_new_lines(message)

    if config.show_in_console_sent_message:
            notifier.send(html_message, config.use_e2e)
    else:
        with snh.suppress_output():
            notifier.send(html_message, config.use_e2e)

# ░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░
# ░░                                          ░░
# ░░                                          ░░
# ░░      DO NOT MODIFY ANYTHING BELOW!       ░░
# ░░                                          ░░
# ░░                                          ░░
# ░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░

@snh.unexpected_exception_handler
def notify(config: snh.NotifierConfig, stored_log_info: snh.StoredLogInfo):
    # Check if there are any log entries
    if len(stored_log_info.data_df) == 0:
        print("No matching log entries found. Nothing to notify.")
        sys.exit(0)

    # Create message
    message = create_message(config, stored_log_info)

    # Perform action
    perform_action(config, message)

@snh.unexpected_exception_handler
def filter_log_data_by_min_required_log_level(config: snh.NotifierConfig, stored_log_info: snh.StoredLogInfo) -> None:
    min_required_log_level = get_min_required_log_level(config)

    if min_required_log_level == 7:
        return

    initial_count = len(stored_log_info.data_df)

    stored_log_info.data_df[snh.DataFrameField.SEVERITY_CODE.value] = stored_log_info.data_df[snh.LogField.LEVEL.value].apply(
        lambda level_name: snh.Severity.get_by_name(level_name).rfc_5424_numerical_code
    )

    stored_log_info.data_df.drop(
        stored_log_info.data_df[stored_log_info.data_df[snh.DataFrameField.SEVERITY_CODE.value] > min_required_log_level].index,
        inplace=True
    )

    stored_log_info.data_df.drop(columns=[snh.DataFrameField.SEVERITY_CODE.value], inplace=True)

    final_count = len(stored_log_info.data_df)

    # Set count for severity to 0 if the severity is greater than the minimum required log level
    for column in stored_log_info.summary_df.columns:
        try:
            if column == snh.DataFrameField.PID.value:
                continue

            severity_code = snh.Severity.get_by_name(column).rfc_5424_numerical_code
            if severity_code > min_required_log_level:
                stored_log_info.summary_df[column] = 0
        except AttributeError:
            continue

    if initial_count != final_count:
        print(f"Ignored {initial_count - final_count} log entries with severity greater than {min_required_log_level} (Original count: {initial_count} | Final count: {final_count})")

@snh.unexpected_exception_handler
def main():
    # Load configuration
    config = load_config()

    # Process command-line arguments
    stored_log_info = snh.process_arguments()

    # Filter log data by minimum required log level
    filter_log_data_by_min_required_log_level(config, stored_log_info)

    # Notify
    notify(config, stored_log_info)

if __name__ == "__main__":
    main()