import typer
from utils import hash_text, hash_file

app = typer.Typer(help ="Hash text or files using specific algorithms.")

def resolve_algorithm(md5: bool, sha1: bool, sha256: bool, sha512: bool) -> str:
    flags = [md5, sha1, sha256, sha512]
    names = ["md5", "sha1", "sha256", "sha512"]
    selected = [name for flag, name in zip(flags, names) if flag]
    if len(selected) > 1:
        raise typer.BadParameter("Please choose only one hash algorithm flag.")
    return selected[0] if selected else "sha256"  # default

@app.command()
def text(
    input: str,
    md5: bool = False,
    sha1: bool = False,
    sha256: bool = False,
    sha512: bool = False
):
    """Hash plain text using a chosen algorithm."""
    algorithm = resolve_algorithm(md5, sha1, sha256, sha512)
    result = hash_text(input, algorithm)
    typer.echo(f"{algorithm}: {result}")

@app.command()
def file(
    path: str,
    md5: bool = False,
    sha1: bool = False,
    sha256: bool = False,
    sha512: bool = False
):
    """Hash a file using a chosen algorithm."""
    algorithm = resolve_algorithm(md5, sha1, sha256, sha512)
    result = hash_file(path, algorithm)
    typer.echo(f"{algorithm}: {result}")

if __name__ == "__main__":
    app()
