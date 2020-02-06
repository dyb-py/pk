class User:
    count=0
    def __init__(self,name,age,sex,phone,mail,password,addr=''):
        User.count+=1
        self.ids=self.count
        self.name=name
        self.age=age
        self.sex=sex
        self.phone=phone
        self.mail=mail
        self.pwd=password
        self.addr=addr

    # @classmethod
    # def create(cls,name,age,sex,phone,mail,password,addr=''): connector
    #     if len(phone)!=11:
    #         print('手机号需要11位')
    #     elif not phone.isalnum():
    #         print('请输入正确手机号')
