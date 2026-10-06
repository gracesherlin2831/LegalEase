import os
import subprocess
import sys


def test_main_module_imports_from_backend_directory():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    backend_dir = os.path.join(root_dir, "backend")
    venv_python = os.path.join(root_dir, "venv", "Scripts", "python.exe")

    result = subprocess.run(
        [venv_python, "-c", "import main"],
        cwd=backend_dir,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr or result.stdout
