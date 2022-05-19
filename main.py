from RNG_urandom import RNG_ur
from hash_container_question import Something
from RNG_J_random import RNG_Java_Random
from RNG_J_SecureRandom import RNG_Java_SecureRandom
from RNG_Middle_Square import RNG_Middle_Square
from RNG_P_ChainedAES import RNG_AES
from RNG_Random_RAM import RNG_RAM
import jpype as jp

jp.startJVM(jp.getDefaultJVMPath(), "-ea")

def run_j_random(n):
    container = {}
    ar = RNG_Java_Random()
    for i in ar.getNextN(n):
        container[i] = int(container.get(i,0) + 1)
    return Something(container)

def run_j_secure_random(n):
    container = {}
    ar = RNG_Java_SecureRandom()
    for i in ar.getNextN(n):
        container[i] = int(container.get(i,0) + 1)
    return Something(container)

def run_urandom(n):
    container = {}
    ar = RNG_ur()
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    return Something(container)

def run_middle_square(n):
    container = {}
    ar = RNG_Middle_Square(640)
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    return Something(container)

def run_chained_AES(n):
    container = {}
    ar = RNG_AES(b'\0'*16)
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    return Something(container)

def run_RAM(n):
    container = {}
    ar = RNG_RAM()
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    return Something(container)

if __name__ == "__main__":

    SAMPLE_SIZE = 1500

    print("Begin")
    urandom_result = run_urandom(SAMPLE_SIZE)
    print('urandom:', urandom_result.get_average())

    j_random_result = run_j_random(SAMPLE_SIZE)
    print('util.java:', j_random_result.get_average())

    j_secure_result = run_j_secure_random(SAMPLE_SIZE)
    print('security.Secure...:', j_secure_result.get_average())

    ms_result = run_middle_square(SAMPLE_SIZE)
    print('Middle Square:', ms_result.get_average())

    aes_result = run_chained_AES(SAMPLE_SIZE)
    print('AES:', aes_result.get_average())

    ram_result = run_RAM(SAMPLE_SIZE)
    # ram_result.print_all()
    print('RAM:', ram_result.get_average())
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # langs = [i for i in range(256)]
    # students = [cont.get(i, 0) for i in range(256)]
    # ax.bar(langs,students)
    # plt.savefig("nice.jpg")

    jp.shutdownJVM() 
    