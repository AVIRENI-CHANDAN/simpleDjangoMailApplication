class gmailCredentials:
    __mailid = ""#Please enter your gmail here.
    __mailpassword = ""#Please enter your gmail password here.
    __mailServer = "smtp.gmail.com"

    def getMailId(self):
        return self.__mailid
    
    def getMailPass(self):
        return self.__mailpassword
    
    def getMailServer(self):
        return self.__mailServer