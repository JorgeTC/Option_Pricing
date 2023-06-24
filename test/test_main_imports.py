import importlib.util
import sys
from contextlib import contextmanager
from pathlib import Path


def get_main_folder() -> Path:
    # Carpeta test
    path_file = Path(__file__).parent
    # Carpeta del proyecto
    path_file = path_file.parent
    # Carpeta mains
    path_file = path_file / "mains"

    return path_file


@contextmanager
def set_mains(mains_folder: Path):
    original_path = list(sys.path)
    sys.path.append(str(mains_folder))

    try:
        yield
    finally:
        sys.path = original_path


def test_import_main():
    mains_folder = get_main_folder()
    assert mains_folder.is_dir()

    all_mains = (file for file in mains_folder.rglob('*.py')
                 if file.name != '__init__.py')
    for main in all_mains:
        spec = importlib.util.spec_from_file_location(main.stem, main)
        foo = importlib.util.module_from_spec(spec)
        with set_mains(mains_folder):
            spec.loader.exec_module(foo)
