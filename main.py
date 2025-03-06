import shutil

def check_network_drive_space(drive_path):
    try:
        total, used, free = shutil.disk_usage(drive_path)
        total_gb = total // (2 ** 30)
        used_gb = used // (2 ** 30)
        free_gb = free // (2 ** 30)

        print(f"Drive: {drive_path}")
        print(f"Total space: {total_gb} GB")
        print(f"Used space: {used_gb} GB")
        print(f"Free space: {free_gb} GB")

    except FileNotFoundError:
        print(f"Network drive {drive_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace '\\xxx' with the network drive path
network_drive = r"\\vs-eed-cifs.efit.technion.ac.il\netd"  # Example: r"\\server\shared_folder"
check_network_drive_space(network_drive)
