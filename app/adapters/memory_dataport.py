from app.services.ports.mydataport import MyDataPort


class MemoryDataPort(MyDataPort):
    async def save(self, data: str) -> bool:
        return data == "true"
