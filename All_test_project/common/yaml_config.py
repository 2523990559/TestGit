# file=open("D:\TestGit\All_test_project\config\environment.yaml",encoding="utf-8")
# try:
#     a=file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()
# with open("D:\TestGit\All_test_project\config\environment.yaml",'r',encoding="utf-8") as file:
#  a=file.read()
#  for i in file.readlines():
#   print("-----")
#   print(i)

import yaml

class GetConf:
    def __init__(self):
        #with open的第一个参数填写environment.yaml的绝对路径
        with open("D:\TestGit\All_test_project\config\environment.yaml", "r",encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            #print(self.env)

    def get_username_password(self):
        return self.env['username'],self.env['password']
      
if __name__ == '__main__':
    print(GetConf().get_username_password())
   