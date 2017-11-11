#!/usr/bin/env python
import os
import sys

"""
    http://127.0.0.1:8080/admin/ account:admin/admin123456
"""

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

