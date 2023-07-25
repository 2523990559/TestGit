import datetime
import os

def  get_now_time():
     return datetime.datetime.now()

#获取项目绝对路径
def  get_project_path():
    file_path=os.path.dirname(__file__)
    print(file_path)
    
if __name__=='__main__':
    #print(get_now_time())
    get_project_path()