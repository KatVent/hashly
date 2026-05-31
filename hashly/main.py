import argparse
import sys

from utils import hash_text, hash_file

def show_help():
    help_text = r"""
 +----------------------------------------+
 |       __  __           __    __        |
 |      / / / /___ ______/ /_  / /_  __   |
 |     / /_/ / __ `/ ___/ __ \/ / / / /   |
 |    / __  / /_/ (__  ) / / / / /_/ /    |
 |   /_/ /_/\__,_/____/_/ /_/_/\__, /     |
 |                            /____/      |
 +----------------------------------------+  by Katia Ventouri

 Usage: hashly [command] <input> --alg [choice] 

 Command:
 string      Choose string to hash
 file        Choose file or path to hash

 Choice:
 md5           MD5 Algorithm   
 sha1          SHA1 Algorithm   
 sha256        SHA256 Algorithm   
 sha512        SHA512 Algorithm

 Examples:   
 hashly string "Hello World" --alg md5
 hashly file file.txt --alg sha1
"""
    print(help_text)


def check_algorithm(algorithm):
    #choices = ["md5", "sha1", "sha256", "sha512"]
    choices = ['blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
     'sha512', 'shake_128', 'shake_256']
    if "--alg" not in sys.argv:
        raise ValueError("[!] Please use the flag --alg and one algorithm (md5, sha1, sha256, sha512).")
    #if algorithm[0] not in choices:
     #   raise ValueError("[!] Please you need to choose one hash algorithm.")
    if len(algorithm) != 1 or algorithm[0] not in choices:
        raise ValueError("[!] Please you need to choose one valid hash algorithm.")
    return algorithm[0]

    '''except IndexError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)


        if indx + 5 >= len(sys.argv):
            print("[!] Please you need to choose one hash algorithm.")
            sys.exit(1)

    alg = sys.argv[indx + 5]

    if len(algorithm)  == 0:
        print("[!] Please you need to choose one hash algorithm.")
        sys.exit(1)
    elif len(algorithm) > 1:
        print("[!] Please choose one hash algorithm.")
        sys.exit(1)'''


def string_command (args):
    try:
        hash_alg = check_algorithm(args.alg)
        result = hash_text(args.text, hash_alg)
        print(f"{hash_alg}: {result}")
    except ValueError as e:
        print(e)
        sys.exit(1)


def file_command(args):
    hash_alg = check_algorithm(args.alg)
    result = hash_file(args.path, hash_alg)
    print(f"{hash_alg}: {result}")

def main():

    # Show custom help test
    if len(sys.argv) == 1:
        return

    if sys.argv[1] in ("-h", "--help"):
        show_help()
        return


    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', required=True)

    file_parser = subparsers.add_parser('file')
    file_parser.add_argument('path', type=str)
    file_parser.add_argument("--alg", nargs="+")
    file_parser.set_defaults(func=file_command)

    string_parser = subparsers.add_parser('string')
    string_parser.add_argument('text', type=str)
    string_parser.add_argument("--alg", nargs="+")
    string_parser.set_defaults(func=string_command)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()