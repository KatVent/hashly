#import typer
import argparse
from sys import flags

from hashly.utils import hash_text, hash_file


def show_help():
    print("""
 +----------------------------------------+
 |       __  __           __    __        |
 |      / / / /___ ______/ /_  / /_  __   |
 |     / /_/ / __ `/ ___/ __ \/ / / / /   |
 |    / __  / /_/ (__  ) / / / / /_/ /    |
 |   /_/ /_/\__,_/____/_/ /_/_/\__, /     |
 |                            /____/      |
 +----------------------------------------+  by Katia Ventouri

 Usage: hashly <command> [option] <input>

 Command:
 string      Choose string to hash
 file        Choose file or path to hash

 Option:
 --md5           MD5 Algorithm   
 --sha1          SHA1 Algorithm   
 --sha256        SHA256 Algorithm   
 --sha512        SHA512 Algorithm

 Examples:   
 hashly string "Hello World" --md5
 hashly file file.txt
""")

def add_flags(p):
    p.add_argument("--md5", action="store_true", help="Use MD5")
    p.add_argument("--sha1", action="store_true", help="Use SHA1")
    p.add_argument("--sha256", action="store_true", help="Use SHA256")
    p.add_argument("--sha512", action="store_true", help="Use SHA512")

def check_algorithm(algorithms):
    flags = [md5, sha1, sha256, sha512]
    names = ["md5", "sha1", "sha256", "sha512"]
    selected = [name for flag, name in zip(flags, names) if flag]
    if len(selected) > 1:
        raise typer.BadParameter("Please choose only one hash algorithm flag.")
    return selected[0] if selected
"""flags=["md5", "sha1", "sha256", "sha512"]
    flag=0
    for algorithm in algorithms:
        
        if algorithm is True:

            print(f"[!] Unsupported hash algorithm: {algorithm}")
"""

def string_command(input: str, algorithm):
    check_algorithm(algorithm)
    pass

def file_command():
    pass

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', required=True)

    file_parser = subparsers.add_parser('file')
    file_parser.add_argument('input')
    add_flags(file_parser)
    file_parser.set_defaults(func=file_command)

    string_parser = subparsers.add_parser('string')
    string_parser.add_argument('input')
    add_flags(string_parser)
    string_parser.set_defaults(func=string_command)


    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
"""
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
    md5: bool = typer.Option(False, "--md5", help = "Use MD5"),
    sha1: bool = typer.Option(False, "--sha1", help = "Use SHA1"),
    sha256: bool = typer.Option(False, "--sha256", help = "Use SHA256"),
    sha512: bool = typer.Option(False, "--sha512", help = "Use SHA512")
):
    #Hash plain text using a chosen algorithm.
    algorithm = resolve_algorithm(md5, sha1, sha256, sha512)
    result = hash_text(input, algorithm)
    typer.echo(f"{algorithm}: {result}")

@app.command()
def file(
    path: str,
    md5: bool = typer.Option(False, "--md5", help="Use MD5"),
    sha1: bool = typer.Option(False, "--sha1", help="Use SHA1"),
    sha256: bool = typer.Option(False, "--sha256", help="Use SHA256"),
    sha512: bool = typer.Option(False, "--sha512", help="Use SHA512")
):
    #Hash a file using a chosen algorithm.
    algorithm = resolve_algorithm(md5, sha1, sha256, sha512)
    result = hash_file(path, algorithm)
    typer.echo(f"{algorithm}: {result}")

if __name__ == "__main__":
    app()
"""