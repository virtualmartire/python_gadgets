import pathlib
import os

def renamer(dirpath, basename, extension):
    # dirpath = the path of the directory in which the files are
    # basename = the noun to pre-pone to every counter (e.g. "image" in "image1", "image2", etc.)
    # extension = the original file extension

	dirpath_obj = pathlib.Path(dirpath)

	files_names = [elem.name for elem in dirpath_obj.glob("*.*")]
	
	counter = 1
	for file_name in files_names:
		oldpath = dirpath + "/" + file_name
		newpath = dirpath + "/" + basename + str(counter) + extension
		os.system("mv " + oldpath + " " + newpath)
		counter += 1