from tqdm import tqdm
import argparse
import os

FILES_PER_SUBFOLDER = 1000


def resize_images(folder_path, new_size):

    square_size = f"{new_size}x{new_size}"
    new_path = f"./images{square_size}"

    folder_list = [
        folder
        for folder in os.listdir(folder_path)
        if os.path.isdir(f"{folder_path}/{folder}")
    ]

    if os.path.exists(new_path):
        print(f"New folder already exists")
        for folder in os.listdir(new_path):
            if len(os.listdir(f"{new_path}/{folder}")) == FILES_PER_SUBFOLDER:
                print(f"Skiping folder {folder}")
                folder_list.remove(folder)
            else:
                print(f"Incomplete convertion found in {folder}, removing it")
                os.system(f"rm -rf {new_path}/{folder}")
    else:
        os.mkdir(new_path)

    num_folders = len(folder_list)
    print(f"Discovered {num_folders} folders")

    for i, folder in enumerate(folder_list):
        print(f"=> {i+1}/{num_folders}")
        new_folder = f"{new_path}/{folder}"
        old_folder = f"{folder_path}/{folder}"
        os.mkdir(new_folder)
        for file in tqdm(os.listdir(old_folder)):
            cmd = f"convert -size 1024x1024 {old_folder}/{file} -resize {square_size} {new_folder}/{file}"
            # print(cmd)
            os.system(cmd)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Resize downloaded images with imagemagick",
    )
    parser.add_argument("new_size", type=int)
    args = parser.parse_args()

    new_size = args.new_size
    print(f"New size {new_size}x{new_size}\n")

    resize_images("./images1024x1024", new_size)


# ----------------------------------------------------------------------------
