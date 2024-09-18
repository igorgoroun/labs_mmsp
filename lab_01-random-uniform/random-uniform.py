from os import EX_OK

W_START: int = 5146
N: int = 10000
K_0: int = 13849
K_1: int = 25173
Q: int = 65536


def linear_generator():
    i = 0
    w = W_START
    while i < Q:
        new_w = (K_1 * w + K_0) % Q
        yield new_w/Q
        w = new_w
        if i + 1 < Q:
            i += 1
        else:
            i = 0


if __name__ == '__main__':
    gen = linear_generator()
    for n in range(N):
        print(next(gen))

    exit(EX_OK)

# (25173*61693+13849)%65536 = 5146
# 0.8387908935546875
# (5146, 54971)