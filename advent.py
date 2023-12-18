from importlib.util import find_spec, LazyLoader, module_from_spec

import sys
from types import ModuleType

import typer


def lazy_import(name: str) -> ModuleType:
    name = f"solns.{name}"
    spec = find_spec(name)
    loader = LazyLoader(spec.loader)
    spec.loader = loader
    module = module_from_spec(spec)
    sys.modules[name] = module
    loader.exec_module(module)
    return module


def main(file_name: str, callable_name: str) -> None:
    module = lazy_import(file_name)
    callable = getattr(module, callable_name)
    callable()


if __name__ == "__main__":
    typer.run(main)
