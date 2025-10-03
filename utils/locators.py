import os
import configparser

current_file = os.path.abspath(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_file))
config = configparser.ConfigParser()

def locate_login() -> dict:
    ret = dict()
    file_path = "loginConfig.ini"
    login_path = os.path.join(parent_dir, file_path)
    config.read(login_path)
    ret["username"] = config["Account"]["username"]
    ret["password"] = config["Account"]["password"]
    return ret

def locate_cap() -> dict:
    ret = dict()
    file_path = "capConfig.ini"
    cap_path = os.path.join(parent_dir, file_path)
    config.read(cap_path)
    ret["package_name"] = config["Driver"]["package_name"]
    ret["activity"] = config["Driver"]["main_activity"]
    return ret

if __name__ == "__main__":
    cap = locate_cap()
    print(cap)
    log = locate_login()
    print(log)
    pass