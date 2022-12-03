from distutils.core import setup
import py2exe

setup(
    name="py-exe", 
    console=['src\hello_world.py'], 
    options={ "py2exe": { "bundle_files": 1 } }
)