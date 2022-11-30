# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kubemq.grpc import kubemq_pb2 as kubemq_dot_grpc_dot_kubemq__pb2


class kubemqStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.SendEvent = channel.unary_unary(
            '/kubemq.kubemq/SendEvent',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Event.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Result.FromString,
        )
        self.SendEventsStream = channel.stream_stream(
            '/kubemq.kubemq/SendEventsStream',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Event.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Result.FromString,
        )
        self.SubscribeToEvents = channel.unary_stream(
            '/kubemq.kubemq/SubscribeToEvents',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Subscribe.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.EventReceive.FromString,
        )
        self.SubscribeToRequests = channel.unary_stream(
            '/kubemq.kubemq/SubscribeToRequests',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Subscribe.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Request.FromString,
        )
        self.SendRequest = channel.unary_unary(
            '/kubemq.kubemq/SendRequest',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Request.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Response.FromString,
        )
        self.SendResponse = channel.unary_unary(
            '/kubemq.kubemq/SendResponse',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Response.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Empty.FromString,
        )
        self.SendQueueMessage = channel.unary_unary(
            '/kubemq.kubemq/SendQueueMessage',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.QueueMessage.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.SendQueueMessageResult.FromString,
        )
        self.SendQueueMessagesBatch = channel.unary_unary(
            '/kubemq.kubemq/SendQueueMessagesBatch',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.QueueMessagesBatchRequest.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.QueueMessagesBatchResponse.FromString,
        )
        self.ReceiveQueueMessages = channel.unary_unary(
            '/kubemq.kubemq/ReceiveQueueMessages',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.ReceiveQueueMessagesRequest.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.ReceiveQueueMessagesResponse.FromString,
        )
        self.StreamQueueMessage = channel.stream_stream(
            '/kubemq.kubemq/StreamQueueMessage',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.StreamQueueMessagesRequest.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.StreamQueueMessagesResponse.FromString,
        )
        self.AckAllQueueMessages = channel.unary_unary(
            '/kubemq.kubemq/AckAllQueueMessages',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.AckAllQueueMessagesRequest.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.AckAllQueueMessagesResponse.FromString,
        )
        self.Ping = channel.unary_unary(
            '/kubemq.kubemq/Ping',
            request_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Empty.SerializeToString,
            response_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.PingResult.FromString,
        )


class kubemqServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def SendEvent(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendEventsStream(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeToEvents(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeToRequests(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRequest(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendResponse(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendQueueMessage(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendQueueMessagesBatch(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveQueueMessages(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamQueueMessage(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AckAllQueueMessages(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_kubemqServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SendEvent': grpc.unary_unary_rpc_method_handler(
            servicer.SendEvent,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Event.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Result.SerializeToString,
        ),
        'SendEventsStream': grpc.stream_stream_rpc_method_handler(
            servicer.SendEventsStream,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Event.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Result.SerializeToString,
        ),
        'SubscribeToEvents': grpc.unary_stream_rpc_method_handler(
            servicer.SubscribeToEvents,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Subscribe.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.EventReceive.SerializeToString,
        ),
        'SubscribeToRequests': grpc.unary_stream_rpc_method_handler(
            servicer.SubscribeToRequests,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Subscribe.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Request.SerializeToString,
        ),
        'SendRequest': grpc.unary_unary_rpc_method_handler(
            servicer.SendRequest,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Request.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Response.SerializeToString,
        ),
        'SendResponse': grpc.unary_unary_rpc_method_handler(
            servicer.SendResponse,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Response.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.Empty.SerializeToString,
        ),
        'SendQueueMessage': grpc.unary_unary_rpc_method_handler(
            servicer.SendQueueMessage,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.QueueMessage.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.SendQueueMessageResult.SerializeToString,
        ),
        'SendQueueMessagesBatch': grpc.unary_unary_rpc_method_handler(
            servicer.SendQueueMessagesBatch,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.QueueMessagesBatchRequest.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.QueueMessagesBatchResponse.SerializeToString,
        ),
        'ReceiveQueueMessages': grpc.unary_unary_rpc_method_handler(
            servicer.ReceiveQueueMessages,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.ReceiveQueueMessagesRequest.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.ReceiveQueueMessagesResponse.SerializeToString,
        ),
        'StreamQueueMessage': grpc.stream_stream_rpc_method_handler(
            servicer.StreamQueueMessage,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.StreamQueueMessagesRequest.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.StreamQueueMessagesResponse.SerializeToString,
        ),
        'AckAllQueueMessages': grpc.unary_unary_rpc_method_handler(
            servicer.AckAllQueueMessages,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.AckAllQueueMessagesRequest.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.AckAllQueueMessagesResponse.SerializeToString,
        ),
        'Ping': grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=kubemq_dot_grpc_dot_kubemq__pb2.Empty.FromString,
            response_serializer=kubemq_dot_grpc_dot_kubemq__pb2.PingResult.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'kubemq.kubemq', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
