class Message:
    text = ""


class InvalidCredentialsMessage(Message):
    text = "Invalid credentials"


class AlreadyExistMessage(Message):
    text = "username already exist"
