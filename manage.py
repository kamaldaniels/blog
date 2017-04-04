#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

    from djangae.core.management import execute_from_command_line, test_execute_from_command_line

    if "test" in sys.argv:
        # This prevents the local sandbox initializing when running tests
        test_execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(sys.argv)