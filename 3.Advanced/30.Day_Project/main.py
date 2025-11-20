import argparse
from utils import organize_files, rename_files

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--organize", action="store_true")
    p.add_argument("--rename")
    args = p.parse_args()

    if args.organize:
        organize_files(args.source)
    if args.rename:
        rename_files(args.source, args.rename)

if __name__ == "__main__":
    main()
