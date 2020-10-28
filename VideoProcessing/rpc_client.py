import grpc
from proto import api2msl_pb2, api2msl_pb2_grpc

class RpcClient:
    def __init__(self, host, port):
        # self.channel = grpc.insecure_channel("localhost:" + str(port))
        self.channel = grpc.insecure_channel(host + ":" + str(port))
        self.stub = api2msl_pb2_grpc.Api2MslStub(self.channel)

    def service_request(self, buf):
        response = self.stub.GetJson(api2msl_pb2.BundleRequest(buf=buf))
        return response.json

    def close(self):
        self.channel.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()