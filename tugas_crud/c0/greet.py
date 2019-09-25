import random
import os

class GreetServer(object):
    def __init__(self):
        pass

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)

    def send(self, command=None):
        input = command.split(" ")

        if input[0] == "LIST":
            return os.listdir('.')
        elif input[0] == "CREATE":
            try:
                open(input[1], 'a').close()
                return "file berhasil dibuat"
            except:
                return "file gagal dibuat"
        elif input[0] == "UPDATE":
            try:
                with open(input[1], "a") as fd:
                    fd.write("\n" + input[2])
                return "file berhasil diubah"
            except:
                return "file gagal diubah"
        elif input[0] == "READ":
            try:
                fd = os.open(input[1], os.O_RDWR)
                ret = os.read(fd, 10240)
                return ret.decode()
            except:
                return "file gagal dibaca"
        elif input[0] == "DELETE":
            try:
                os.remove(input[1])
                return "file berhasil dihapus"
            except:
                return "file gagal dihapus"
if __name__ == '__main__':
    k = GreetServer()
    print(k.get_greet('royyana'))
