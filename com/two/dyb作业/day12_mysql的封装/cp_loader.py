import  configparser,os


class CPTools:
    def get_config(self,section,option,path=r'.\config.ini',encoding='utf-8'):
        cp=configparser.ConfigParser()
        cp.read(path,encoding=encoding)
        return cp.get(section,option)

if __name__ == '__main__':
    path=r'.\config.ini'
    print(CPTools().get_config('DATA', 'user'))

