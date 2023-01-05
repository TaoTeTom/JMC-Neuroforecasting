import os
def count_file(path):
    count = 0
    # Iterate directory
    for file in os.scandir(path):
        if file.is_file():
            count += 1
    return count