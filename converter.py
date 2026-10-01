import csv
import json 

def read_csv(file_path):

    """ Read a cav file into a list of dicts. """
    try:
        with open (file_path,"r",newline="",encoding="utf-8") as file:
            reader =  csv.DictReader(file)
            return list(reader)
    except FileNotFoundError as error:
        print(f"[ERROR] File not found: ({file_path}): {error}")
        return []
    except Exception as error:
        print(f"[ERROR] Failed to read csv:({file_path}): {error}")
        return []
def write_csv (file_path,rows,fieldnames):

    """ write dicts to a csv file. """

    if not rows:
        rows = []
    try:
        with open (file_path,"w",newline="",encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames= fieldnames,extrasaction= "ignore")
            writer.writeheader()
            writer.writerows(rows)
        return True
    except Exception as error:
        print(f"[ERROR] Failed to write csv: ({file_path}): {error}")
        return False

def write_json (file_path,data):
    """ write data to json file. """
    try:
        with open (file_path,"w",encoding="utf-8") as file:
            json.dump(data,file,indent= 4,ensure_ascii=False)
        return True
    except Exception as error:
        print(f"[ERROR] Failed to write json: ({file_path}): {error}")
        return False
def read_json(file_path):

    """ Read a json file. """
    try:
        with open (file_path,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as error:
        print(f"[ERROR] File not  found: ({file_path}) {error}")
        return []
    except json.JSONDecodeError as error:
        print(f"[ERROR] json invalid format ({file_path}): {error}")
        return []
    
