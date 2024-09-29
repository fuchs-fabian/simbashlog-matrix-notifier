# `simbashlog-example-notifier`: Template for a `simbashlog`-notifier

<p align="center">
  <a href="./LICENSE">
    <img alt="GPL-3.0 License" src="https://img.shields.io/badge/GitHub-GPL--3.0-informational">
  </a>
</p>

<div align="center">
  <table>
    <tr>
      <td>
        <!--
        TODO: Replace the URL with the URL of the repository.
        -->
        <a href="https://github.com/fuchs-fabian/simbashlog-example-notifier">
          <img src="https://github-readme-stats.vercel.app/api/pin/?username=fuchs-fabian&repo=simbashlog-example-notifier&theme=holi&hide_border=true&border_radius=10" alt="Template repository simbashlog-example-notifier"/>
        </a>
      </td>
    </tr>
  </table>
</div>

## Description

<!--
TODO: Describe the purpose of the notifier.
-->

This is a template for creating a Python notifier for `simbashlog`.

## Getting Started

> It is possible that `pip` is not yet installed. If this is not the case, you will be prompted to install it. Confirm the installation.

### Installation with `pip` (GitHub)

<!--
TODO: Replace the URL with the URL of the repository.
-->

```bash
pip install git+https://github.com/fuchs-fabian/simbashlog-example-notifier
```

### Installation with `pip` (Local)

Download the repository and navigate to the directory containing the [`setup.py`](setup.py) file.

```bash
pip install .
```

### Check Installation

```bash
pip list
```

<!--
TODO: Replace `simbashlog-example-notifier` with the name of the package defined in the `setup.py` file.
-->

```bash
pip show simbashlog-example-notifier
```

### Configuration

After installation, you will find the configuration file under:

<!--
TODO: Replace `simbashlog-example-notifier` with the name of the package defined in the `setup.py` file.
-->

```plain
~/.config/simbashlog-notifier/simbashlog-example-notifier/config.json
```

This configuration file is used by default if no other custom configuration file is specified.

It looks as follows:

<!--
TODO: Replace with the actual content of the configuration file.
-->

```json
{
    "min_required_log_level": "6",
    "show_in_console_sent_message": "true",
    "show_in_header_pid": "false",
    "show_in_body_log_file_result": "false",
    "show_in_body_log_file_content": "false",
    "show_in_body_summary_for_pid": "false",
    "show_in_body_summary_for_log_file": "false",
    "show_in_footer_log_file_names": "false",
    "show_in_footer_host": "false",
    "show_in_footer_notifier_name": "true",
    "example_key": "example_value"
}
```

### Usage

<!--
TODO: Replace `simbashlog-example-notifier` with the name of the package defined in the `setup.py` file.
-->

```plain
usage: simbashlog-example-notifier [-h] [--config CONFIG] [--pid PID] [--log-level LOG_LEVEL] [--message MESSAGE]
                                   [--log-file LOG_FILE] [--json-log-file JSON_LOG_FILE]

Notifier for simbashlog.

options:
  -h, --help            show this help message and exit
  --config CONFIG       Path to a custom config file.
  --pid PID             The used process ID.
  --log-level LOG_LEVEL
                        The used log level (sourced simbashlog) / severity number (simbashlog called with arguments).
  --message MESSAGE     The logged message (simbashlog called with arguments).
  --log-file LOG_FILE   The created *.log file.
  --json-log-file JSON_LOG_FILE
                        The created *_log.json file.
```

### Uninstallation

<!--
TODO: Replace `simbashlog-example-notifier` with the name of the package defined in the `setup.py` file.
-->

```bash
pip uninstall simbashlog-example-notifier
```

## Bugs, Suggestions, Feedback, and Needed Support

> If you have any bugs, suggestions or feedback, feel free to create an issue or create a pull request with your changes.

## Support `simbashlog`

If you like `simbashlog`'s ecosystem, you think it is useful and saves you a lot of work and nerves and lets you sleep better, please give it a star and consider donating.

<a href="https://www.paypal.com/donate/?hosted_button_id=4G9X8TDNYYNKG" target="_blank">
  <!--
    https://github.com/stefan-niedermann/paypal-donate-button
  -->
  <img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" style="height: 90px; width: 217px;" alt="Donate with PayPal"/>
</a>

---

> This script is a component of [`simbashlog`](https://github.com/fuchs-fabian/simbashlog) ([LICENSE](https://github.com/fuchs-fabian/simbashlog/blob/main/LICENSE)).
>
> The core of this notifier is [`simbashlog-notify-helper-py`](https://github.com/fuchs-fabian/simbashlog-notify-helper-py) ([LICENSE](https://github.com/fuchs-fabian/simbashlog-notify-helper-py/blob/main/LICENSE)).
>
> *Copyright (C) 2024 Fabian Fuchs*
