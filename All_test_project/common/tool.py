import datetime
import os

def  get_now_time():
     return datetime.datetime.now()

#获取项目绝对路径
def  get_project_path():
    project_name="All_test_project"
    file_path=os.path.dirname(os.path.abspath(__file__))
    #print(file_path)
    return file_path[:file_path.find(project_name)+len(project_name)]


def sep(path,add_sep_before=False,add_sep_after=False):
    all_path=os.sep.join(path)
    #print('具体的值',all_path)
    if add_sep_after:
        all_path=all_path+os.sep   #在地址前面加上分隔符合
    if  add_sep_before:
         all_path=os.sep+all_path #在地址后面加上分隔符合  
    #print( '获取分隔符后面的地址',all_path)
    return  all_path

  
if __name__=='__main__':
    #print(get_now_time())
    get_project_path()
    sep()