import os


def check_if_folder_exists(folder: str):
    logfolder = folder or "logs"
    if not os.path.exists(logfolder):
        os.makedirs(logfolder)


def parse_code(series_code: str):
    elements = series_code.split(".")
    del elements[1]
    return ".".join(elements)
