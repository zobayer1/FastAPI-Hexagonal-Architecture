from app.services.ports.mydataport import MyDataPort


class MemoryDataPort(MyDataPort):
    def save(self, data: str) -> bool:
        return data == "true"
