import os

def main():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.py'):
                path = os.path.join(root, f)
                with open(path, 'rb') as fh:
                    data = fh.read()
                    if b'\x00' in data:
                        print("⚠ Null bytes detectados en:", path)

if __name__ == '__main__':
    main()
