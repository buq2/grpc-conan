import asyncio
import logging
import sys
import os

pth = os.path.join(os.path.dirname(__file__), '..', 'build','src')
sys.path.append(pth)

import grpc
import service_pb2
import service_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.NiceServiceStub(channel)
        response = await stub.SendMessage(service_pb2.Data(msg='you'))
    print("Greeter client received: " + response.msg)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
