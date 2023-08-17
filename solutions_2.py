from datetime import datetime
import os

def get_time_diff(start_time,end_time):
    try:
        if ":" in start_time:
            tim = start_time.split(":")
            start_hrs = tim[0]
            start_minutes = tim[1]
        else:
            start_hrs = start_time
            start_minutes = "00"
        if ":" in end_time:
            tim = end_time.split(":")
            end_hrs = tim[0]
            end_minutes = tim[1]
        else:
            end_hrs = end_time
            end_minutes = "00"

        if int(start_hrs) > int(end_hrs):
            end_hrs = str(int(end_hrs) + 12)

        start_time = f"{start_hrs}:{start_minutes}"
        end_time = f"{end_hrs}:{end_minutes}"

        # convert time string to datetime
        t1 = datetime.strptime(start_time, "%H:%M")

        t2 = datetime.strptime(end_time, "%H:%M")

        # get difference
        delta = t2 - t1
        return delta.seconds // 60 / 60
    except Exception as e:
        raise Exception(e)

def get_time_diff_for_each_file_data(data,each_file):
    try:
        print("Filename: ",each_file)
        for each in data:
            print(each, end=" ")
            time_intervals = each.split(",")
            time_spent = 0
            for each_interval in time_intervals:
                interval = each_interval.strip().split("-")
                start_time,end_time = interval[0],interval[1]
                time_spent += get_time_diff(start_time,end_time)
            print("Time Spent in office:",time_spent)
    except Exception as e:
        raise Exception(e)


for each_file in os.listdir("timesheets"):
    with open(f"timesheets//{each_file}") as f1:
        data = f1.read().splitlines()
        get_time_diff_for_each_file_data(data,each_file)

