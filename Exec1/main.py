import os
from pathlib import Path


def list_file_n_owners(path):
    file_owners = []
    files = os.listdir(path)
    for fl in files:
        pathFile = Path(path+'/'+fl)
        if pathFile.is_file:
            file_owners.append(pathFile.owner())
    return files, file_owners


def group_owners(files, owners):
    dictio = {}
    for fl, owner in zip(files, owners):
        dictio[fl] = owner
    return dictio


def main(diretorio):
    files, owners = list_file_n_owners(diretorio)
    print(group_owners(files, owners))


if __name__ == "__main__":
    main('./Exec1/Teste')
