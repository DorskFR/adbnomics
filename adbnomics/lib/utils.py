import os


def check_if_folder_exists(folder: str):
    logfolder = folder or "logs"
    if not os.path.exists(logfolder):
        os.makedirs(logfolder)
