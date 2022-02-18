pi = 3.14

def volume_sphr(rr):
    V = ((4/3) * pi * rr**3)
    print(round(V))

if __name__ == "__main__":
    rr = int(input())
    volume_sphr(rr)