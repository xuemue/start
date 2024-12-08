#!/usr/bin/env python
"""Django's command-line utility for administrative aSatu (xuemu) tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aSatu.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Gagal import Django. Tolong Pastikan Semua Telah Terinstall dengan lengkap dan "
            "available on your PYTHONPATH environment variable? Did you "
            "Anda Lupa aktifkan virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
