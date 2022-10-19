import zipfile
import os


def Pack(workdir: str, ZipFilelist: list, ZipRoute: str):
    ori = os.getcwd()
    os.chdir(workdir)
    f = zipfile.ZipFile(ZipRoute, 'w', zipfile.ZIP_DEFLATED)
    for i in ZipFilelist:
        f.write(i)
    f.close()
    os.chdir(ori)