from graphlib import TopologicalSorter


def main():
    toPrint = ''
    for i in range(ord('a'),ord('z')+1):
        toPrint += chr(i) + ' '
    print(toPrint)

if __name__ == "__main__":
    main()