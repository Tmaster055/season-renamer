import os
import re

def main():
    # Ask user for folder path
    folder = input("Please enter the path to the folder with the files: ").strip()

    # Regex for files: Name - SxxExx - Rest
    pattern = re.compile(r"(.*) - S\d{2}E\d{3}(.*)(\.mp4)", re.IGNORECASE)

    try:
        files = sorted(os.listdir(folder))
    except FileNotFoundError:
        print("❌ Folder not found. Please check the path.")
        return

    episode_counter = 1
    rename_plan = []

    print("\n📋 Preview of new filenames:\n")

    for filename in files:
        match = pattern.match(filename)
        if match:
            show_name = match.group(1).strip()
            rest = match.group(2).strip()
            extension = match.group(3)

            # Always three-digit episode numbers
            #print(rest)
            if rest:
                new_filename = f"{show_name} - S01E{episode_counter:03d} {rest}{extension}"
            else:
                new_filename = f"{show_name} - S01E{episode_counter:03d}{extension}"

            print(f"{filename}  --->  {new_filename}")

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)
            rename_plan.append((old_path, new_path))

            episode_counter += 1

    if not rename_plan:
        print("\n⚠️ No matching files found.")
        return

    # Confirmation
    choice = input("\n❓ Do you want to rename the files? (y/n): ").strip().lower()
    if choice == "y":
        for old_path, new_path in rename_plan:
            os.rename(old_path, new_path)
        print("\n✅ All files have been renamed!")
    else:
        print("\n❌ Canceled, no files were changed.")

if __name__ == "__main__":
    main()
