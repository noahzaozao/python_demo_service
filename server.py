import logging
import time
from concurrent import futures

import grpc

import demo_pb2
import demo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DemoService(demo_pb2_grpc.DemoServiceServicer):

    def __init__(self):
        pass

    def CreateOne(self, request, context):

        print("C_2_S CreateOne: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C CreateOne: <<<<< ", response)

        return response

    def DeleteOne(self, request, context):

        print("C_2_S DeleteOne: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C DeleteOne: <<<<< ", response)

        return response

    def TransferOne(self, request, context):

        print("C_2_S TransferOne: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C TransferOne: <<<<< ", response)

        return response

    def GetCreateNotify(self, request, context):

        print("C_2_S GetCreateNotify: >>>>> ", request)

        response = demo_pb2.ResponseData(
            return_code=0,
            message="success",
            data=""
        )

        print("S_2_C GetCreateNotify: <<<<< ", response)

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServiceServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:9090')
    server.start()

    print("listen: 9090")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
