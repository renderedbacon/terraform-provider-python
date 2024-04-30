from json import dumps
from os import getpid
from random import randint
from signal import SIGINT, SIGTERM

from anyio import create_task_group, open_signal_receiver, run
from anyio.abc import TaskGroup, TaskStatus
from grpc.aio import server, Server
from grpc_health.v1.health import HealthServicer
from grpc_health.v1 import health_pb2
from grpc_health.v1.health_pb2_grpc import add_HealthServicer_to_server
from loguru import logger

from .provider import Provider
from .tfplugin.tfplugin_pb2_grpc import add_ProviderServicer_to_server


async def start_server(rpc: Server, task_group: TaskGroup, task_status: TaskStatus):
    task_status.started()

    # We need to build a health service to work with go-plugin
    health = HealthServicer()
    health.set("plugin", health_pb2.HealthCheckResponse.ServingStatus.Value("SERVING"))

    # add servicers to the server
    add_ProviderServicer_to_server(Provider(rpc), rpc)
    add_HealthServicer_to_server(health, rpc)

    # start the server (pick a random port)
    listen_addr: str = f"0.0.0.0:{randint(49152, 65535)}"
    rpc.add_insecure_port(listen_addr)
    await rpc.start()

    # Output information
    core_protocol_version = 1
    protocol_version = 6
    addr_network = "tcp"
    addr_string = listen_addr
    protocol_type = "grpc"
    # server_cert = "" # TODO: add support for mTLS in the future

    # print the information to stdout for the client (terraform) to read
    print(f"{core_protocol_version}|{protocol_version}|{addr_network}|{addr_string}|{protocol_type}", flush=True)

    pid: int = getpid()
    logger.debug(f"server strated on {listen_addr} (pid: {pid})")

    # show debug information for terraform provider reattach
    tf_reaatch_providers = {
        "registry.terraform.io/renderedbacon/python": {
            "Protocol": protocol_type,
            "ProtocolVersion": protocol_version,
            "Pid": pid,
            "Test": True,
            "Addr": {
                "Network": addr_network,
                "String": addr_string,
            },
        },
    }
    logger.debug(f"TF_REATTACH_PROVIDERS='{dumps(tf_reaatch_providers).replace(" ", "")}'")

    # wait for the server to stop
    await rpc.wait_for_termination()
    logger.trace("server stopped")

    # when server is stopped, make sure the task group is cancelled
    logger.trace("cancelling task group")
    task_group.cancel_scope.cancel()


async def handle_signals(rpc: Server):
    with open_signal_receiver(SIGINT, SIGTERM) as signals:
        async for sig in signals:
            logger.trace(f"stopping server (signal={sig})")
            await rpc.stop(grace=10)
            return


async def serve():
    rpc: Server = server()

    async with create_task_group() as task_group:
        await task_group.start(start_server, rpc, task_group)
        task_group.start_soon(handle_signals, rpc)


# start the rpc server
run(serve)
