import os

# Возвращает список найденных файлов в определенной дериктории
def FindFilesWithEndInDirectory(dir:str, end:str):
    files = []
    for file in os.listdir(dir):
        if file.endswith(end):
            files.append(str(dir + "/" + file))
    return files

# Возвращает список всех файлов в дереве, начиная от 'start' - стартовая директория
def FilesInAllDrivers(start:str):
    tree = os.walk(start)
    paths = []
    for i in tree:
        # Адрес очередного каталога, Имена подкаталогов первого уровня для данного каталога, Имена файлов данного каталога
        catalog,under_catalog,files = i
        for file in files:
            paths.append(str(catalog + "/" + file))

    return paths

# Возвращает список найденных файлов в дереве, начиная от 'start' - стартовая директория с указанным окончанием
def FilesWithEndInAllDrivers(start:str, end:str):
    tree = os.walk(start)
    paths = []
    for i in tree:
        # Адрес очередного каталога, Имена подкаталогов первого уровня для данного каталога, Имена файлов данного каталога
        catalog,under_catalog,files = i
        for file in files:
            if file.endswith(end):
                paths.append(str(catalog + "\\" + file))

    return paths

# Возвращает имя файла, аргумент - путь к файлу
def getNameFromPath(path:str):
    answer = ''
    i = len(path)-1
    while path[i] != '\\':
        answer += path[i]
        i -= 1
    p = ''
    i = len(answer)-1
    while i >= 0:
        p += answer[i]
        i -= 1
    answer = p
    return answer
