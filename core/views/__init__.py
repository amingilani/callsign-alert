import os
import importlib

files = (f.removesuffix('.py') for f in os.listdir() if f.endswith('.py') and not f.startswith('__'))

for file in files:
    model_module = importlib.import_module(file)
    globals()[model_module.__name__.split('.')[-1]] = model_module
