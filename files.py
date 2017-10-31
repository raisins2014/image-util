import os, sys

def mv_to(src, dst_dir):
    name = os.path.split(src)[1]
    target = os.path.join(dst_dir, name)
    try:
        os.rename(src, target)
    except OSError:
        print("Cannot move", src, "to", target)
    return target

def rename_all(fd, name):
    files = os.listdir(fd)
    files = [os.path.join(fd, f) for f in files]
    output = []
    for i in range(len(files)):
        f = files[i]
        try:
            path, fn = os.path.split(f)
            n, ext = os.path.splitext(fn)
            target = os.path.join(path, name + " - " + str(i) + ext)
            os.rename(f, target)
            output.append(target)
        except FileNotFoundError:
            print(f,"does not exist")
            print(target)
    return output

if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = args[0]
    if cmd == "mv_to" and len(args) == 3:
        mv_to(args[1], args[2])
    elif cmd == "rename_all" and len(args) == 3:
        rename_all(args[1], args[2])
    else:
        print("Invalid use case.")
