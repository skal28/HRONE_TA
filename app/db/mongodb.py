from motor.motor_asyncio import AsyncIOMotorClient

client = None
db = None

async def connect_db():
    global client, db
    client = AsyncIOMotorClient("mongodb+srv://agarwalharshit824:htAL2810@cluster0.5sia80h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["hrone_db"]

def get_db():
    if db is None:
        raise Exception("Database not initialized. Call connect_db() at startup.")
    return db