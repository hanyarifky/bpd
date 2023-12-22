import os

def main():
    os.rename("./data_mahasiswa.txt", "./Mahasiswa_Reguler.txt")
    f = open("./Mahasiswa_Reguler.txt")
    print(f.name)
    print(f.closed)
    print(f.closed)
    print(f.closed)

if __name__ == "__main__":
    main()