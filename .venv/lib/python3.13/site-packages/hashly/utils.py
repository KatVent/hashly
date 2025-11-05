import hashlib

def hash_text(text: str, algorithm: str) :
    try:
        hasher = hashlib.new(algorithm)
        hasher.update(text.encode("utf-8"))
        return hasher.hexdigest()
    except ValueError:
        raise ValueError(f"[-] Unsupported hash algorithm: {algorithm}")


def hash_file(path: str, algorithm: str = "sha256") -> str:
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


