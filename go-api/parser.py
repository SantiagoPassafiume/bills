import json


def read_file(file):
    with open(file, "r") as f:
        lines = f.readlines()

    return lines


def parse_log(logs):
    for log in logs:
        get_fields(log)


def get_fields(log):
    fields = ["remip", "tunnelip", "user"]

    dictionary = {"remip": 0, "tunnelip": 0, "user": ""}

    for line in log.strip().split(" "):
        for field in fields:
            if field in line:
                new_line = line.split("=")[1]
                dictionary[field] = new_line
                print(dictionary)
                dictionary = {"remip": "", "tunnelip": "", "user": ""}
    print("\n")


if __name__ == "__main__":
    logs = read_file("logs.log")
    parsed_logs = parse_log(logs)
