import subprocess
import os

if not os.path.exists("output"):
    os.mkdir("output")

combat_type_list = os.listdir("assets/image")
for combat_type in combat_type_list:
    # os.mkdir(f"output/{combat_type}")
    avatar_dir = f"assets/image/{combat_type}/avatar"
    splash_dir = f"assets/image/{combat_type}/splash"
    avatar_file_list = os.listdir(avatar_dir)
    splash_file_list = os.listdir(splash_dir)
    # os.mkdir(f"output/{combat_type}/avatar")
    for avatar_file in avatar_file_list:
        subprocess.run(
            [
                ".conda/python.exe", 
                "img2img_color.py",
                "--input", 
                f"assets/image/{combat_type}/avatar/{avatar_file}",
                "--output",
                f"output/{combat_type}/avatar/{avatar_file}"
            ]
        )
    # os.mkdir(f"output/{combat_type}/splash")
    for splash_file in splash_file_list:
        subprocess.run(
            [
                ".conda/python.exe", 
                "img2img_color.py",
                "--input", 
                f"assets/image/{combat_type}/splash/{splash_file}",
                "--output",
                f"output/{combat_type}/splash/{splash_file}"
            ]
        )
