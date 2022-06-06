import tomli
import tomli_w
from pathlib import Path


template_path = Path("C:\\develop\\MyPython\\micropython-stubs\\publish\\template")


def create_project(package_path: Path, name: str, version: str = "0.0.1", description: str = "MicroPython stubs"):
    """
    create or update/overwrite a `pyproject.toml` file by combining a template file
    with the given parameters.
    and updating it with the pyi files included
    """
    # package_path = Path("C:\\develop\\MyPython\\micropython-stubs\\publish\\micropython-esp32-generic-stubs")
    
    # TODO: do not overwrite existing pyproject.toml but read and apply changes to it

    # read the template pyproject.toml file
    with open(template_path / "pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)

    # update the name , version and description of the package
    pyproject["tool"]["poetry"]["name"] = name
    pyproject["tool"]["poetry"]["version"] = version
    pyproject["tool"]["poetry"]["description"] = description

    folders = ["micropython-v1_18-esp32"]
    # add the modules to the package
    for folder_name in folders:
        folder = package_path / folder_name
        # find packages using __init__ files
        for p in folder.rglob("**/__init__.py"):
            # add the module to the package
            # fixme : only accounts for one level of packages
            pyproject["tool"]["poetry"]["packages"] += [{"from": folder_name, "include": p.parent.name}]
        # now find other stub files directly in the folder
        for p in folder.glob("*.pyi"):
            pyproject["tool"]["poetry"]["packages"] += [{"from": folder_name, "include": p.name}]

    try:
        # check if the result is a valid toml file
        tomli.loads(tomli_w.dumps(pyproject))
    except tomli.TOMLDecodeError as e:
        print("Could not create a valid TOML file")
        raise (e)

    with open(package_path / "pyproject.toml", "wb") as output:
        tomli_w.dump(pyproject, output)
