import shutil
import logging
import os
import time

# Set logging variables
logging_level = logging.DEBUG if 'DEBUG' in os.environ else logging.INFO
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging_level)

target_path = "H:\\"
src_dir = "M:\Videos\Сериалы\The.Orville"
files_limit = 3


def copy_file(src, dst):
    size = round(os.path.getsize(src) / 1024 / 1024, 2)
    logging.info(f"start file {src} of size {size} MB")

    start_time = int(time.time())
    shutil.copy(src, dst)
    end_time = int(time.time())

    duration = end_time - start_time
    speed = round(size / duration, 2)

    logging.info(f"end file {src}")
    logging.info(f"duration {duration} sec. Speed {speed} MB / sec")

    return size, duration


if __name__ == "__main__":
    logging.info("Start")

    src_files = [os.path.join(src_dir, file) for file in os.listdir(src_dir)
                 if os.path.isfile(os.path.join(src_dir, file))]
    src_files.sort()

    total_size = 0
    total_duration = 0
    for index, file in enumerate(src_files):
        if index == files_limit:
            break

        size, duration = copy_file(file, target_path)
        total_size += size
        total_duration += duration

    average_speed = round(total_size / total_duration, 2)
    logging.info(f"Average write speed is {average_speed} MB / sec")
    logging.info("End of work")
