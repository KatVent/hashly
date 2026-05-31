import hashlib
import sys
def hash_string(string: str, algorithm: str) :
    hasher = hashlib.new(algorithm)
    hasher.update(string.encode("utf-8"))
    return hasher.hexdigest()


def hash_file(path: str, algorithm: str) :
    try:
        hasher = hashlib.new(algorithm)
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"[-] File not found: {path}")
        sys.exit(1)
