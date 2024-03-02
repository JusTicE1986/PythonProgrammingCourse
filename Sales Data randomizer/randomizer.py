import random
import csv
import time as t
import shutil
from datetime import datetime


def read_csv(file):
    list_of_rows = []
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            list_of_rows.append(row)
    return list_of_rows


def shuffle_list(list_of_rows):
    header = list_of_rows[0]
    list_of_rows.remove(header)
    random.shuffle(list_of_rows)
    return header, list_of_rows


def sleep_time(time):
    t.sleep(time)


def backup_original_csv(file):
    try:
        filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "_" + file.title()[file.title().find("/")+1:]
        shutil.copy(file, "./backup/" + filename)
        logging_message = f"{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}\tBackup of {filename} has been created successfull"
        logger_for_backups(logging_message)
    except OSError as e:
        logger_for_backups(f'OS error: {e}')


def write_new_csv(header, list_of_rows):
    try:
        with open("./sales_data.csv", "w", encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for row in list_of_rows:
                writer.writerow(row)
    except OSError as e:
        logger_for_backups(f'OS error: {e}')


def logger_for_backups(logmessage):
    with open("./backup/backuplogger.txt", "a", encoding="utf-8", newline='') as backuplog:
        backuplog.write(logmessage+"\n")


def input_convert(userinput_duration):
    try:
        int_userinput_duration = int(userinput_duration)
        return int_userinput_duration
    except ValueError as e:
        logger_for_backups(f'Value error: {e}')


if __name__ == "__main__":
    running = True
    sleep_time_input = input("Enter the duration between two shuffles: ")
    converted_sleep_time = input_convert(sleep_time_input)
    while running:
        backup_original_csv("./sales_data.csv")
        list_of_rows = read_csv("./sales_data.csv")
        header, list_of_rows = shuffle_list(list_of_rows)
        write_new_csv(header, list_of_rows)
        logger_for_backups("sales_data.csv")
        try:
            sleep_time(converted_sleep_time)
        except ValueError as e:
            logger_for_backups(f'Value error: {e}')



