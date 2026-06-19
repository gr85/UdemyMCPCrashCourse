import asyncio

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(".env"))

async def main():
    print("Hello from udemymcpcrashcourse!")


if __name__ == "__main__":
    asyncio.run(main())
