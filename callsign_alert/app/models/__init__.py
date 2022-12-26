import pkgutil
import inspect
import string

def import_submodules(package):
    """
    Import all submodules of the given package, and import all classes in each submodule.
    """
    class_names = []  # List to store class names
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        submodule = __import__(name)
        for variable_name in dir(submodule):
            if not variable_name.startswith(string.ascii_uppercase):
                # We only want to import public classes
                continue
            cls = getattr(submodule, variable_name)
            if inspect.isclass(cls):
                setattr(package, cls, cls)
                class_names.append(cls)

    package.__all__ = class_names

import_submodules(__import__(__name__))
