import sys
from datetime import date,datetime


class Insert:
    def __init__(self):
        print("insert class .....")


    def SaveData(self, data):
        self.data = data
        id=datetime.now()
        createdat=datetime.now().strftime(" %H:%M:%S")
        day=date.today()
        lastupdate=datetime.now().strftime(" %H:%M:%S")







    def ReadData(self):
        print("plese Enter data ..... if you want to break then please press 'cntr+D'")
        data = sys.stdin.read()

        print("do you want to verify data and then save it them please type 'vs+Enter'")
        print("if you want to save data them press 's+Enter'")
        print()
        SaveCheck = input("please insert your input....")

        if SaveCheck=='vs':
            print(data)
            print("if you want to save data them press 's+Enter'")
            SaveCheck1 = input("please insert your input....")
            if SaveCheck1=='s':
                print("saving the data....")


        elif SaveCheck=='s':
            print("saving the data....")
        else:
            print("please select option again for insert data  Thanks ")
