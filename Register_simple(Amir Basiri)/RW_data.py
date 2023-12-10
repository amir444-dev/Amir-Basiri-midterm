import json


def read_json():
    with open("info.json") as f:
        info = json.load(f)
    return info


def write_json(info):
    with open("info.json", 'w') as f:
        json.dump(info, f)


# -------------------------------------------------------------------

def check_read():
    with open("check.json") as f:
        check = json.load(f)
    return check


def check_write(check):
    with open("check.json", 'w') as f:
        json.dump(check, f)
