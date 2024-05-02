from grpc.aio import Server

from .tfplugin.tfplugin_pb2_grpc import ProviderServicer
from .tfplugin.tfplugin_pb2 import (
    ApplyResourceChange,
    CallFunction,
    ConfigureProvider,
    GetFunctions,
    GetMetadata,
    GetProviderSchema,
    ImportResourceState,
    MoveResourceState,
    PlanResourceChange,
    ReadDataSource,
    ReadResource,
    Schema,
    ServerCapabilities,
    StopProvider,
    UpgradeResourceState,
    ValidateDataResourceConfig,
    ValidateProviderConfig,
    ValidateResourceConfig,
)


class Provider(ProviderServicer):
    def __init__(self, rpc: Server):
        self.rpc = rpc
        super().__init__()

    async def GetMetadata(self, request: GetMetadata.Request, context) -> GetMetadata.Response:
        return GetMetadata.Response(
            server_capabilities=ServerCapabilities(
                plan_destroy=False,
                get_provider_schema_optional=False,
                parallelism=10,
                provider_version="0.1.0",
            ),
            diagnostics=[],
            data_sources=[],
            resources=[],
            functions=[],
        )

    async def GetProviderSchema(self, request: GetProviderSchema.Request, context) -> GetProviderSchema.Response:
        return GetProviderSchema.Response(
            provider=Schema(block=Schema.Block(attributes=[])),
        )

    async def ValidateProviderConfig(self, request: ValidateProviderConfig.Request, context) -> ValidateProviderConfig.Response:
        raise NotImplementedError()

    async def ValidateResourceConfig(self, request: ValidateResourceConfig.Request, context) -> ValidateResourceConfig.Response:
        raise NotImplementedError()

    async def ValidateDataResourceConfig(self, request: ValidateDataResourceConfig.Request, context) -> ValidateDataResourceConfig.Response:
        raise NotImplementedError()

    async def UpgradeResourceState(self, request: UpgradeResourceState.Request, context) -> UpgradeResourceState.Response:
        raise NotImplementedError()

    async def ConfigureProvider(self, request: ConfigureProvider.Request, context) -> ConfigureProvider.Response:
        raise NotImplementedError()

    async def ReadResource(self, request: ReadResource.Request, context) -> ReadResource.Response:
        raise NotImplementedError()

    async def PlanResourceChange(self, request: PlanResourceChange.Request, context) -> PlanResourceChange.Response:
        raise NotImplementedError()

    async def ApplyResourceChange(self, request: ApplyResourceChange.Request, context) -> ApplyResourceChange.Response:
        raise NotImplementedError()

    async def ImportResourceState(self, request: ImportResourceState.Request, context) -> ImportResourceState.Response:
        raise NotImplementedError()

    async def MoveResourceState(self, request: MoveResourceState.Request, context) -> MoveResourceState.Response:
        raise NotImplementedError()

    async def ReadDataSource(self, request: ReadDataSource.Request, context) -> ReadDataSource.Response:
        raise NotImplementedError()

    async def GetFunctions(self, request: GetFunctions.Request, context) -> GetFunctions.Response:
        raise NotImplementedError()

    async def CallFunction(self, request: CallFunction.Request, context) -> CallFunction.Response:
        raise NotImplementedError()

    async def StopProvider(self, request: StopProvider.Request, context) -> StopProvider.Response:
        # cleanup any outstanding work

        # stop the server
        await self.rpc.stop()

        # TODO: are there any errors that can be returned here?
        return StopProvider.Response()
