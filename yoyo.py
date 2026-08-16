class user:
    def __init__(self, username):
        self.username = username

    def greet(self):
        return(f"hello my name is {self.username}")

    def save_to_file(self):
        with open("users.txt", "a") as file:
            file.write(self.username + "\n")
        print(f"saved {self.username} to users.txt")

name1 = user("sai")
print(name1.greet())
name1.save_to_file()

name2 = user("ali")
print(name2.greet())
name2.save_to_file()