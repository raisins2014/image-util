from PIL import Image
import os, sys

def convert(src, dst=None, ext="png"):
    if dst is None:
        dst = os.path.splitext(src)[0] + "." + ext
    else:
        dst = os.path.splitext(dst)[0] + "." + ext
    if src != dst:
        try:
            Image.open(src).save(dst)
        except (IOError, ValueError):
            print("Cannot convert", src)
    return dst

def convert_and_mv(src, dst_dir, ext="png"):
    name = os.path.split(src)[1]
    dst = os.path.join(dst_dir, name)
    return convert(src, dst, ext)

def convert_and_mv_all(fd, dst_dir, ext="png"):
    files = os.listdir(fd)
    files = [os.path.join(fd, f) for f in files]
    return [convert_and_mv(f, dst_dir, ext) for f in files]

if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = args[0]
    if cmd == "convert" and len(args) == 3:
        convert(args[1], ext=args[2])
    elif cmd == "convert_all" and len(args) == 4:
        convert_and_mv_all(args[1], args[2], ext=args[3])
    else:
        print("Invalid use case.")
