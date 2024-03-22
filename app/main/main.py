import os
import shutil
from time import sleep
from datetime import datetime

# Configure these paths
SOURCE_DIR = r'C:\Users\SAYAN BHATTACHARYA\Documents\projects\Test_Folder'
DEST_DIR = r'C:\Users\SAYAN BHATTACHARYA\Documents\projects\Languages\Python\Automatic_File_Transfer_Load_Test\Test'
WAIT_TIME = 20 * 60  # 20 minutes in seconds


def get_pending_files(source_dir, transferred_files):
    all_files = {f for f in os.listdir(source_dir) if f.endswith('.txt')}
    # Return files that have not been transferred yet
    return list(all_files - transferred_files)


def batch_transfer_files(source_dir, dest_dir, initial_batch_length):
    transferred_files = set()
    batch_size = initial_batch_length

    while True:
        pending_files = get_pending_files(source_dir, transferred_files)
        if not pending_files:
            print("All files have been transferred.")
            break

        # Adjust batch_size if fewer files are left than the current batch_size
        current_batch = pending_files[:min(len(pending_files), batch_size)]
        print(f"Transferring batch of {len(current_batch)} files at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        for file in current_batch:
            shutil.copy(os.path.join(source_dir, file), os.path.join(dest_dir, file))
            transferred_files.add(file)

        print("Batch transfer completed. Waiting for the next batch transfer...")
        sleep(WAIT_TIME)

        # Optional: Adjust batch_size dynamically here based on conditions or inputs


if __name__ == "__main__":
    initial_batch_size = int(input("Enter the initial batch size: "))
    batch_transfer_files(SOURCE_DIR, DEST_DIR, initial_batch_size)
