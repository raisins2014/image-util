from PIL import Image
import os, sys

def convert(src, ext="png"):
    name, ex = os.path.splitext(src)
    dst = name + "." + ext
    if src != dst:
        try:
            Image.open(src).save(dst)
        except (IOError, ValueError):
            print("Cannot convert", src)
    return dst

def mv(src, dst_dir):
    name = os.path.split(src)[1]
    target = os.path.join(dst_dir, name)
    try:
        os.rename(src, target)
    except OSError:
        print("Cannot move", src, "to", target)
    return target

def convert_and_mv(src, dst_dir, ext="png"):
    return mv(convert(src, ext), dst_dir)

def convert_and_mv_all(fd, dst_dir, ext="png"):
    files = os.listdir(fd)
    files = [os.path.join(fd, f) for f in files]
    return [convert_and_mv(f, dst_dir, ext) for f in files]

def rename_all(fd, name):
    files = os.listdir(fd)
    files = [os.path.join(fd, f) for f in files]
    for i in range(len(files)):
        f = files[i]
        try:
            path, fn = os.path.split(f)
            n, ext = os.path.splitext(fn)
            target = os.path.join(path, name + " - " + str(i) + ext)
            os.rename(f, target)
        except FileNotFoundError:
            print(f,"does not exist")
            print(target)

if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = args[0]
    if cmd == "mv" and len(args) == 3:
        mv(args[1], args[2])
    elif cmd == "convert" and len(args) == 3:
        convert(args[1], args[2])
    elif cmd == "convert_all" and len(args) == 4:
        convert_and_mv_all(args[1], args[2], args[3])
    elif cmd == "rename_all" and len(args) == 3:
        rename_all(args[1], args[2])
    else:
        print("Invalid use case.")
