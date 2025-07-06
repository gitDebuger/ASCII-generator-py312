from characters import All_Characters
import os
import wget

if not os.path.exists("assets/image"):
    os.mkdir("assets/image")

for character_list in All_Characters:
    combat_type = character_list[0].combat_type.name
    first_dir = f"assets/image/{combat_type}"
    avatar_dir = f"{first_dir}/avatar"
    splash_dir = f"{first_dir}/splash"
    os.mkdir(first_dir)
    os.mkdir(avatar_dir)
    os.mkdir(splash_dir)
    for character in character_list:
        print(f"\nDownloading {character.name}")
        file_type = ".gif" if character.avatar.endswith(".gif") else ".png"
        wget.download(character.avatar, f"{avatar_dir}/{character.name}{file_type}")
        wget.download(character.splash, f"{splash_dir}/{character.name}{file_type}")

print("\nDownload Complete")
