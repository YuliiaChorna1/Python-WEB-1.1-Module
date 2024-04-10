from abc import ABC, abstractmethod


class DBClient:
    
    def __init__(self, bd_iface):
        self.connection_info = bd_iface.connect("postgresql://weufyxhg")


class BDIFace(ABC):

    @abstractmethod
    def connect(self, url) -> str:
        pass


class TestDI(BDIFace):

    def connect(self, url) -> str:

        return "Connected to bd"


class MongoDI(BDIFace):

    def __init__(self) -> None:
        self.db = Mongo()

    def connect(self, url):

        self.db.send_checksum()
        self.db.connect(url)


class Mongo:

    def send_checksum():
        pass

    def connect():
        pass


class PostgresDI(BDIFace):

    def __init__(self):
        self.db = Postgres()

    def connect(self, url):
        self.db.auth()
        self.db.connect()


class Postgres:

    def connect(url):
        pass

    def auth():
        pass


# mongo = MongoDI()
# postgres = PostgresDI()
# client = DBClient()

fake_db = TestDI()
client = DBClient(fake_db)
if (client.connection_info != "Connected to bd"):
    assert()

