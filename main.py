from elements import taiko_elements
import os

def all_files(osu_folder):
    skins = []
    number = 0
    skin_folder = osu_folder + "\\Skins"
    for folder in os.listdir(skin_folder):
        number += 1
        print(f"{number}. {folder}")
        skins.append(folder)

    return skins

def skin_source():
    skin = input("What skin do you want to copy from? (type the number) ")
    skin = int(skin)
    skin = skin - 1
    skin = skins[skin]

    return skin

def skin_destination():
    skin2 = input("What skin do you want to copy to? (type the number) ")
    skin2 = int(skin2)
    skin2 = skin2 - 1
    skin2 = skins[skin2]

    return skin2

osu_folder = input("Enter you osu folder path: ")
skins = all_files(osu_folder)

source_skin = skin_source()
dest_skin = skin_destination()
source_path = f"{osu_folder}\\Skins\\{source_skin}"
destination_path = f"{osu_folder}\\Skins\\{dest_skin}"

for file in os.listdir(source_path):
    if file in taiko_elements:
        s_path = f"{source_path}\\{file}"
        in_file = open(s_path, "rb")
        data = in_file.read()

        d_path = f"{destination_path}\\{file}"
        with open(d_path, "wb") as out:
            out.write(data)
        print(f"Copied {file}")




# C:\Users\HR Farmer\AppData\Local\osu!
# aristia = 51
# yep