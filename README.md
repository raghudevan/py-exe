# Learn Py
Sample program which reads from some input & writes to some output. 

# Dependencies 
1. python3
2. py2exe
```
pip install py2exe
```

# Steps

1. Install python

2. To convert to an executable, install py2exe 
```
pip install py2exe
```

3. install setup dependencies (only one time)
```
python .\src\setup.py install
```

If you want to re-run this command, you'll have to delete the site-packages
```
rm -r PATH_TO_SITE_PACKAGES\site-packages\py_exe-0.0.0-py3.11.egg
```

4. Build the code (creation of executable)
```
python .\src\setup.py py2exe
```

This will create "hello_world.exe" inside directory called "dist"

5. Run the executable
```
.\dist\hello_world.exe
```

# Clean up

1. clean up build dir
```
rm -r .\build\
```

2. clean up dist dir
```
rm -r .\dist\
```

3. clean up output
```
rm output.txt
```