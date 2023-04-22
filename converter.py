import sys
import os
from PIL import Image

current_directory = os.getcwd()

current_folder = sys.argv[1]

new_folder = sys.argv[2]

current_path = os.path.join(current_directory, current_folder)

new_path = os.path.join(current_directory, new_folder)
if not os.path.exists(new_path):
	os.mkdir(new_path)

for file_name in os.listdir(current_path):
	if file_name.endswith('.jpg'):
		with Image.open(os.path.join(current_path, file_name)) as img:
			new_file_name = os.path.splitext(file_name)[0] + '.png'
			img.save(os.path.join(new_path, new_file_name))