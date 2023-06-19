# Задание 1
#Шаблон Factory Method:

from abc import ABC, abstractmethod


class SocialMediaAccount(ABC):
    @abstractmethod
    def post(self, content):
        pass


class FacebookAccount(SocialMediaAccount):
    def post(self, content):
        print("Posting on Facebook:", content)


class InstagramAccount(SocialMediaAccount):
    def post(self, content):
        print("Posting on Instagram:", content)


class TwitterAccount(SocialMediaAccount):
    def post(self, content):
        print("Posting on Twitter:", content)


class SocialMediaAccountFactory(ABC):
    @abstractmethod
    def create_account(self):
        pass


class FacebookAccountFactory(SocialMediaAccountFactory):
    def create_account(self):
        return FacebookAccount()


class InstagramAccountFactory(SocialMediaAccountFactory):
    def create_account(self):
        return InstagramAccount()


class TwitterAccountFactory(SocialMediaAccountFactory):
    def create_account(self):
        return TwitterAccount()


#Шаблон Proxy:


class SocialMediaAccountProxy(SocialMediaAccount):
    def __init__(self, account):
        self._account = account

    def post(self, content):
        if self._is_allowed():
            self._account.post(content)
        else:
            print("You are not allowed to post this content.")

    def _is_allowed(self):
        # Check if user is allowed to post
        return True  # or False
# Задание 2
class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)


class FileProxy(File):
    def __init__(self, filename):
        super().__init__(filename)
        self.read_attempts = 0
        self.access_allowed = True
        self.content_cache = None

    def read(self):
        if self.access_allowed:
            self.read_attempts += 1
            if not self.content_cache:
                self.content_cache = super().read()
            return self.content_cache
        else:
            print("Access denied.")

    def write(self, content):
        if self.access_allowed:
            super().write(content)
            self.content_cache = content
        else:
            print("Access denied.")

    def restrict_access(self):
        self.access_allowed = False

    def allow_access(self):
        self.access_allowed = True

    def get_read_attempts(self):
        return self.read_attempts

# Задание 3
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

class PowerOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.power_on()

    def undo(self):
        self.device.power_off()

    def redo(self):
        self.execute()

class PowerOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.power_off()

    def undo(self):
        self.device.power_on()

    def redo(self):
        self.execute()

class VolumeUpCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.volume_up()

    def undo(self):
        self.device.volume_down()

    def redo(self):
        self.execute()

class VolumeDownCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.volume_down()

    def undo(self):
        self.device.volume_up()

    def redo(self):
        self.execute()

class RemoteControl:
    def __init__(self):
        self.commands = [None] * 10
        self.undo_command = None
        self.redo_command = None

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if self.commands[slot]:
            self.undo_command = self.commands[slot]
            self.undo_command.execute()
            self.redo_command = None

    def undo_button(self):
        if self.undo_command:
            self.undo_command.undo()
            self.redo_command = self.undo_command
            self.undo_command = None

    def redo_button(self):
        if self.redo_command:
            self.redo_command.redo()
            self.undo_command = self.redo_command
            self.redo_command = None

class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass

class TV(Device):
    def power_on(self):
        print("TV is turned on")

    def power_off(self):
        print("TV is turned off")

    def volume_up(self):
        print("TV volume is increased")

    def volume_down(self):
        print("TV volume is decreased")