#User Defined Error
class Myerror(Exception):
    def __init__(self,msg):
        self.msg=msg
raise Myerror("its my error")


