import os
import sys

port = os.getenv("DJANGO_RUNSERVER_PORT", "8000")

if port is None:
    port = "8000"

def main():
    if len(sys.argv) == 1:
        sys.argv += ["runserver", port]
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc

if __name__ == "__main__":
    main()
