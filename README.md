A small repo of various image utility functions written in Python.

### Image conversion
To use `convert.py` run
```
python convert.py <cmd> <args>
```

#### Valid commands:
* `convert <file> <extension>`
* `convert_all <source dir> <dest dir> <ext>`

### File utilities
TO use `files.py` run
```
python files.py <cmd> <args>
```

#### Valid commands:
* `mv_to <file> <dest dir>`
* `rename_all <dir> <prefix>` - renames ith file in directory to "prefix - i" (perserves extension)
### Dependencies
* Python 3.x
* pillow

