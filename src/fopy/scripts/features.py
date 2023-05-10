from pathlib import Path

def newfeature(name):
    if not Path(f"{name}/").exists():
        Path(f"{name}/").mkdir()
        Path(f"{name}/__pycache__/").mkdir()
        Path(f"{name}/__init__.py").touch()
        Path(f"{name}/feature.py").write_text(
            """from fopy import Composer

            def select(composer):
                pass
            """
        )
    else:
        print("Directory already exists")
