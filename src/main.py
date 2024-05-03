from Alg import Alg

def main(root="a"):

    Graph1 = {
        "a": {"f": 45, "b": 8, "c": 20, "k": 11},
        "b": {"e": 14, "f": 123},
        "c": {"f": 200, "e": 300, "n": 17, "l": 11},
        "d": {"m": 48},
        "e": {"f": 55, "n": 17},
        "f": {"h": 23},
        "g": {"f": 42},
        "h": {"g": 56, "ch": 26},
        "ch": {"g": 11, "i": 9},
        "i": {"j": 19},
        "j": {"ch": 26, "k": 39},
        "k": {"i": 29, "c": 38, "l": 13, "h": 21},
        "l": {"j": 24, "m": 3},
        "m": {"c": 32},
        "n": {"m": 99, "d": 22},
    }

    chu_liu_edmond = Alg(root)
    graph_prime = chu_liu_edmond.execute(Graph1)

    print("MST: ", graph_prime)

if __name__ == "__main__":

    main()
