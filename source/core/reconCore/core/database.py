# global variable
import json
import os.path
import traceback


def error(data):
    try:
        if "str" not in str(type(data)):
            try:
                data = data.decode()
                pass
            except Exception:
                data = f"{str(data)}"
                pass
        if not data.endswith("\n"):
            data = f"{data}\n"
        with open(f"{installlocation}/.data/.errors/error.log", "a") as stdout:
            stdout.write(data)
            stdout.close()
        return
    except Exception as e:
        print(e)



global path_to_datbase
installlocation = f'{os.getenv("HOME")}/.SuperSploit'
path_to_database = f"{installlocation}/.data/data.json"


class DatabaseManagment:

    def __init__(self):
        pass


    @classmethod
    def checkIntegration(cls) -> bool:
        with open(DatabaseManagment.get()["EXPLOIT"]) as file:
            data = file.read()
            file.close()
        if "integrated = True" in data:
            return True
        return False
    @classmethod
    def addVariableToDatabase(cls, data):
        if os.path.lexists(path_to_database):
            with open(path_to_database) as file:
                database = json.load(file)
                file.close()
            database[data.split(" ")[1]] = data.split(" ")[2]
            with open(path_to_database, "w") as file:
                file.write(json.dumps(database))

    @classmethod
    def findTerm(cls):
        term = None
        with open(f"{installlocation}/.data/.terminals", "r") as file:
            terms = file.read().split("\n")
            file.close()
        for x in terms:
            if x in os.listdir("/bin"):
                term = x
        return term

    @classmethod
    def directlyModify(cls, data: list):
        try:
            with open(f"{installlocation}/.data/data.json") as file:
                variables = json.load(file)
                file.close()
            if "exploit" in data[0]:
                variables["EXPLOIT"] = data[1]
            if "payload" in data[0]:
                variables["PAYLOAD"] = data[1]
            with open(f"{installlocation}/.data/data.json", "w") as file:
                file.write(json.dumps(variables))
                file.close()
        except Exception:
            error(traceback.format_exc())
            return

    @classmethod
    def get(cls):
        if os.path.lexists(path_to_database):
            with open(path_to_database) as file:
                data = json.load(file)
                file.close()
            return data

    @staticmethod
    def getExploits():
        exploits = []
        for x in os.listdir(f"{installlocation}/exploits/"):
            for i in os.listdir(f"{installlocation}/exploits/{x}"):
                exploits.append(f"{installlocation}/exploits/{x}/{i}")
        return exploits
    @staticmethod
    def getPayloads():
        exploits = []
        for x in os.listdir(f"{installlocation}/payloads/"):
            for i in os.listdir(f"{installlocation}/payloads/{x}"):
                exploits.append(f"{installlocation}/payloads/{x}/{i}")
        return exploits