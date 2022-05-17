from RNG_urandom import RNG_ur
from RNG_util_random import RNG_Java_Random

if __name__ == "__main__":
    print("Begin")
    j = 0
    try:
        ar= RNG_Java_Random()
        for i in ar.getNext():
            if i == 255:
                print(i)
    finally:
        ar.close()
        