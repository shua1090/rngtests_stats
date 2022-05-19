from RNG_urandom import RNG_ur
from hash_container_question import Something
from RNG_J_random import RNG_Java_Random
from RNG_J_SecureRandom import RNG_Java_SecureRandom

def run_j_random(n):
    container = {}
    ar = RNG_Java_Random()
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    ar.close()
    return Something(container)

def run_j_secure_random(n):
    container = {}
    ar = RNG_Java_SecureRandom()
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    ar.close()
    return Something(container)

def run_urandom(n):
    container = {}
    ar = RNG_ur()
    for i in ar.getNextN(n):
        container[i] = container.get(i,0) + 1
    return Something(container)

if __name__ == "__main__":

    SAMPLE_SIZE = 1500

    print("Begin")
    urandom_result = run_urandom(SAMPLE_SIZE)
    print(urandom_result.get_average())


    j_random_result = run_j_random(SAMPLE_SIZE)
    print(j_random_result.get_average())
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # langs = [i for i in range(256)]
    # students = [cont.get(i, 0) for i in range(256)]
    # ax.bar(langs,students)
    # plt.savefig("nice.jpg")
    