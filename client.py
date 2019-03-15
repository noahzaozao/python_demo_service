import logging

import grpc

import demo_pb2
import demo_pb2_grpc


def run():
    with grpc.insecure_channel('127.0.0.1:9090') as channel:
        client = demo_pb2_grpc.DemoServiceStub(channel)

        response = client.CreateOne(demo_pb2.RequestData(
            data="call create one from client",
        ))
        print(response.return_code, response.message, response.data)


        response = client.DeleteOne(demo_pb2.RequestData(
            data="call delete one from client",
        ))
        print(response.return_code, response.message, response.data)

        response = client.TransferOne(demo_pb2.RequestData(
            data="call get transfer one from client",
        ))
        print(response.return_code, response.message, response.data)

        response = client.GetCreateNotify(demo_pb2.RequestData(
            data="call create one from client",
        ))
        print(response.return_code, response.message, response.data)


if __name__ == '__main__':
    logging.basicConfig()
    run()
