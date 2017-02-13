
import os

def filepath():
    return os.path.dirname(__file__)

if __name__ == '__main__':
    file = filepath()
    print (file)