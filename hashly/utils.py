import hashlib

def hash_text(string: str, algorithm: str) :
    try:
        hasher = hashlib.new(algorithm)
        hasher.update(string.encode("utf-8"))
        return hasher.hexdigest()
    except ValueError:
        raise ValueError(f"[-] Unsupported hash algorithm: {algorithm}")


def hash_file(path: str, algorithm: str) :
    """Lif algorithm == None :
        print("[!] No algorithm specified")
    else:??:::"""
    try:
        hasher = hashlib.new(algorithm)
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"[-] File not found: {path}")
    except ValueError:
        raise ValueError(f"[-] Unsupported hash algorithm: {algorithm}")


