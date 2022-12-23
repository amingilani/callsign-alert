#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import encrypted_secrets


def main():
    """Run administrative tasks."""
    try:
        encrypted_secrets.load_secrets()
    except encrypted_secrets.YAMLFormatException:
        print("\n\n\nMALFORMED YAML IN ENCRYPTED SECRETS\n\n\n")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'callsign_alert.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
