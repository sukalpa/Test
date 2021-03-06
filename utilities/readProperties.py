import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\sukal\\PycharmProjects\\Test\\Configuration\\Config.ini")

class Readconfig:
    @staticmethod
    def baseurl():
        url = config.get('common info','URL')
        return url
    @staticmethod
    def username():
        username = config.get('common info','username')
        return username

    @staticmethod
    def password():
        password = config.get('common info', 'password')
        return password
