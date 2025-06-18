import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    print("parameters:", len(args))
    for age in args:
        print(f"{arg}: {len(age)}")

