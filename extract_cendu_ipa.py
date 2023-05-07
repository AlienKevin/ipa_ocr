import re
import shutil
import os

cendu_ipa_pattern = re.compile(r'成都<img src=\"([a-z0-9\/\-\.]+)\.gif\"/>')
title_pattern = re.compile(r'<d:entry id=\"[a-z0-9_]+\" d:title=\"([\u4e00-\u9fff]+)\">')
img_folder = "cendu_ipas/"

# Create the destination folder if it doesn't exist
if not os.path.exists(img_folder):
    os.makedirs(img_folder)
else:
    # Clear the folder contents if it already exists
    for filename in os.listdir(img_folder):
        file_path = os.path.join(img_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

with open("現代漢語方言大詞典.xml", "r") as input_file:
    lines = input_file.readlines()
    i = 0
    while i < len(lines):
        match = title_pattern.search(lines[i])
        if match:
            word = match.group(1)
            i += 4
            match = cendu_ipa_pattern.search(lines[i])
            if match:
                print("Processing {}".format(word))
                img_src = match.group(1) + ".gif"
                # Check if the source file exists
                if os.path.isfile(img_src):
                    shutil.copy(img_src, os.path.join(img_folder, "{}.gif".format(word)))
                    print("Copied {}".format(img_src))
                else:
                    print("Source image file {} does not exist.".format(img_src))
        i += 1
