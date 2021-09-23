class Message:
    text = ""


class InvalidCredentialsMessage(Message):
    text = "Invalid credentials"


class AlreadyExistMessage(Message):
    text = "username already exist"


class SkillAddedSuccessfully(Message):
    text = "Skill Was Added Successfully"


class SkillUpdatedSuccessfully(Message):
    text = "Skill Was Updated"


class SkillDeletedSuccessfully(Message):
    text = "Skill Was Deleted"
