# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfplugin.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0etfplugin.proto\x12\ttfplugin6"-\n\x0c\x44ynamicValue\x12\x0f\n\x07msgpack\x18\x01 \x01(\x0c\x12\x0c\n\x04json\x18\x02 \x01(\x0c"\xbd\x01\n\nDiagnostic\x12\x30\n\x08severity\x18\x01 \x01(\x0e\x32\x1e.tfplugin6.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12+\n\tattribute\x18\x04 \x01(\x0b\x32\x18.tfplugin6.AttributePath"/\n\x08Severity\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02"S\n\rFunctionError\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x11\x66unction_argument\x18\x02 \x01(\x03H\x00\x88\x01\x01\x42\x14\n\x12_function_argument"\xa4\x01\n\rAttributePath\x12,\n\x05steps\x18\x01 \x03(\x0b\x32\x1d.tfplugin6.AttributePath.Step\x1a\x65\n\x04Step\x12\x18\n\x0e\x61ttribute_name\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x65lement_key_string\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lement_key_int\x18\x03 \x01(\x03H\x00\x42\n\n\x08selector"4\n\x0cStopProvider\x1a\t\n\x07Request\x1a\x19\n\x08Response\x12\r\n\x05\x45rror\x18\x01 \x01(\t"{\n\x08RawState\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12\x31\n\x07\x66latmap\x18\x02 \x03(\x0b\x32 .tfplugin6.RawState.FlatmapEntry\x1a.\n\x0c\x46latmapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xf8\x07\n\x06Schema\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin6.Schema.Block\x1a\xd7\x01\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12/\n\nattributes\x18\x02 \x03(\x0b\x32\x1b.tfplugin6.Schema.Attribute\x12\x32\n\x0b\x62lock_types\x18\x03 \x03(\x0b\x32\x1d.tfplugin6.Schema.NestedBlock\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x05 \x01(\x0e\x32\x15.tfplugin6.StringKind\x12\x12\n\ndeprecated\x18\x06 \x01(\x08\x1a\xf9\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12-\n\x0bnested_type\x18\n \x01(\x0b\x32\x18.tfplugin6.Schema.Object\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x10\n\x08optional\x18\x05 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x06 \x01(\x08\x12\x11\n\tsensitive\x18\x07 \x01(\x08\x12/\n\x10\x64\x65scription_kind\x18\x08 \x01(\x0e\x32\x15.tfplugin6.StringKind\x12\x12\n\ndeprecated\x18\t \x01(\x08\x1a\xf9\x01\n\x0bNestedBlock\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin6.Schema.Block\x12:\n\x07nesting\x18\x03 \x01(\x0e\x32).tfplugin6.Schema.NestedBlock.NestingMode\x12\x11\n\tmin_items\x18\x04 \x01(\x03\x12\x11\n\tmax_items\x18\x05 \x01(\x03"M\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\x12\t\n\x05GROUP\x10\x05\x1a\xe2\x01\n\x06Object\x12/\n\nattributes\x18\x01 \x03(\x0b\x32\x1b.tfplugin6.Schema.Attribute\x12\x35\n\x07nesting\x18\x03 \x01(\x0e\x32$.tfplugin6.Schema.Object.NestingMode\x12\x15\n\tmin_items\x18\x04 \x01(\x03\x42\x02\x18\x01\x12\x15\n\tmax_items\x18\x05 \x01(\x03\x42\x02\x18\x01"B\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04"\xd8\x03\n\x08\x46unction\x12\x31\n\nparameters\x18\x01 \x03(\x0b\x32\x1d.tfplugin6.Function.Parameter\x12\x39\n\x12variadic_parameter\x18\x02 \x01(\x0b\x32\x1d.tfplugin6.Function.Parameter\x12*\n\x06return\x18\x03 \x01(\x0b\x32\x1a.tfplugin6.Function.Return\x12\x0f\n\x07summary\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x06 \x01(\x0e\x32\x15.tfplugin6.StringKind\x12\x1b\n\x13\x64\x65precation_message\x18\x07 \x01(\t\x1a\xa5\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x18\n\x10\x61llow_null_value\x18\x03 \x01(\x08\x12\x1c\n\x14\x61llow_unknown_values\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x06 \x01(\x0e\x32\x15.tfplugin6.StringKind\x1a\x16\n\x06Return\x12\x0c\n\x04type\x18\x01 \x01(\x0c"m\n\x12ServerCapabilities\x12\x14\n\x0cplan_destroy\x18\x01 \x01(\x08\x12$\n\x1cget_provider_schema_optional\x18\x02 \x01(\x08\x12\x1b\n\x13move_resource_state\x18\x03 \x01(\x08"\xb8\x03\n\x0bGetMetadata\x1a\t\n\x07Request\x1a\xab\x02\n\x08Response\x12:\n\x13server_capabilities\x18\x01 \x01(\x0b\x32\x1d.tfplugin6.ServerCapabilities\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12?\n\x0c\x64\x61ta_sources\x18\x03 \x03(\x0b\x32).tfplugin6.GetMetadata.DataSourceMetadata\x12:\n\tresources\x18\x04 \x03(\x0b\x32\'.tfplugin6.GetMetadata.ResourceMetadata\x12:\n\tfunctions\x18\x05 \x03(\x0b\x32\'.tfplugin6.GetMetadata.FunctionMetadata\x1a \n\x10\x46unctionMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\'\n\x12\x44\x61taSourceMetadata\x12\x11\n\ttype_name\x18\x01 \x01(\t\x1a%\n\x10ResourceMetadata\x12\x11\n\ttype_name\x18\x01 \x01(\t"\xbb\x05\n\x11GetProviderSchema\x1a\t\n\x07Request\x1a\x9a\x05\n\x08Response\x12#\n\x08provider\x18\x01 \x01(\x0b\x32\x11.tfplugin6.Schema\x12T\n\x10resource_schemas\x18\x02 \x03(\x0b\x32:.tfplugin6.GetProviderSchema.Response.ResourceSchemasEntry\x12Y\n\x13\x64\x61ta_source_schemas\x18\x03 \x03(\x0b\x32<.tfplugin6.GetProviderSchema.Response.DataSourceSchemasEntry\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12(\n\rprovider_meta\x18\x05 \x01(\x0b\x32\x11.tfplugin6.Schema\x12:\n\x13server_capabilities\x18\x06 \x01(\x0b\x32\x1d.tfplugin6.ServerCapabilities\x12G\n\tfunctions\x18\x07 \x03(\x0b\x32\x34.tfplugin6.GetProviderSchema.Response.FunctionsEntry\x1aI\n\x14ResourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin6.Schema:\x02\x38\x01\x1aK\n\x16\x44\x61taSourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin6.Schema:\x02\x38\x01\x1a\x45\n\x0e\x46unctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12"\n\x05value\x18\x02 \x01(\x0b\x32\x13.tfplugin6.Function:\x02\x38\x01"\x84\x01\n\x16ValidateProviderConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\xd6\x01\n\x14UpgradeResourceState\x1aU\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12&\n\traw_state\x18\x03 \x01(\x0b\x32\x13.tfplugin6.RawState\x1ag\n\x08Response\x12/\n\x0eupgraded_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\x97\x01\n\x16ValidateResourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\x9b\x01\n\x1aValidateDataResourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\x9a\x01\n\x11\x43onfigureProvider\x1aM\n\x07Request\x12\x19\n\x11terraform_version\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\x93\x02\n\x0cReadResource\x1a\x8d\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12.\n\rcurrent_state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12.\n\rprovider_meta\x18\x04 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1as\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12\x0f\n\x07private\x18\x03 \x01(\x0c"\xd8\x03\n\x12PlanResourceChange\x1a\xef\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x33\n\x12proposed_new_state\x18\x03 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x15\n\rprior_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\xcf\x01\n\x08Response\x12.\n\rplanned_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x32\n\x10requires_replace\x18\x02 \x03(\x0b\x32\x18.tfplugin6.AttributePath\x12\x17\n\x0fplanned_private\x18\x03 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x05 \x01(\x08"\x96\x03\n\x13\x41pplyResourceChange\x1a\xec\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12.\n\rplanned_state\x18\x03 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x17\n\x0fplanned_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\x8f\x01\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x0f\n\x07private\x18\x02 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x04 \x01(\x08"\xa5\x02\n\x13ImportResourceState\x1a(\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a^\n\x10ImportedResource\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1a\x83\x01\n\x08Response\x12K\n\x12imported_resources\x18\x01 \x03(\x0b\x32/.tfplugin6.ImportResourceState.ImportedResource\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\xd5\x02\n\x11MoveResourceState\x1a\xc0\x01\n\x07Request\x12\x1f\n\x17source_provider_address\x18\x01 \x01(\t\x12\x18\n\x10source_type_name\x18\x02 \x01(\t\x12\x1d\n\x15source_schema_version\x18\x03 \x01(\x03\x12)\n\x0csource_state\x18\x04 \x01(\x0b\x32\x13.tfplugin6.RawState\x12\x18\n\x10target_type_name\x18\x05 \x01(\t\x12\x16\n\x0esource_private\x18\x06 \x01(\x0c\x1a}\n\x08Response\x12-\n\x0ctarget_state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x12\x16\n\x0etarget_private\x18\x03 \x01(\x0c"\xe7\x01\n\x0eReadDataSource\x1au\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12.\n\rprovider_meta\x18\x03 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x1a^\n\x08Response\x12&\n\x05state\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic"\xdd\x01\n\x0cGetFunctions\x1a\t\n\x07Request\x1a\xc1\x01\n\x08Response\x12\x42\n\tfunctions\x18\x01 \x03(\x0b\x32/.tfplugin6.GetFunctions.Response.FunctionsEntry\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin6.Diagnostic\x1a\x45\n\x0e\x46unctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12"\n\x05value\x18\x02 \x01(\x0b\x32\x13.tfplugin6.Function:\x02\x38\x01"\xb1\x01\n\x0c\x43\x61llFunction\x1a\x43\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\targuments\x18\x02 \x03(\x0b\x32\x17.tfplugin6.DynamicValue\x1a\\\n\x08Response\x12\'\n\x06result\x18\x01 \x01(\x0b\x32\x17.tfplugin6.DynamicValue\x12\'\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x18.tfplugin6.FunctionError*%\n\nStringKind\x12\t\n\x05PLAIN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x32\xa4\x0c\n\x08Provider\x12N\n\x0bGetMetadata\x12\x1e.tfplugin6.GetMetadata.Request\x1a\x1f.tfplugin6.GetMetadata.Response\x12`\n\x11GetProviderSchema\x12$.tfplugin6.GetProviderSchema.Request\x1a%.tfplugin6.GetProviderSchema.Response\x12o\n\x16ValidateProviderConfig\x12).tfplugin6.ValidateProviderConfig.Request\x1a*.tfplugin6.ValidateProviderConfig.Response\x12o\n\x16ValidateResourceConfig\x12).tfplugin6.ValidateResourceConfig.Request\x1a*.tfplugin6.ValidateResourceConfig.Response\x12{\n\x1aValidateDataResourceConfig\x12-.tfplugin6.ValidateDataResourceConfig.Request\x1a..tfplugin6.ValidateDataResourceConfig.Response\x12i\n\x14UpgradeResourceState\x12\'.tfplugin6.UpgradeResourceState.Request\x1a(.tfplugin6.UpgradeResourceState.Response\x12`\n\x11\x43onfigureProvider\x12$.tfplugin6.ConfigureProvider.Request\x1a%.tfplugin6.ConfigureProvider.Response\x12Q\n\x0cReadResource\x12\x1f.tfplugin6.ReadResource.Request\x1a .tfplugin6.ReadResource.Response\x12\x63\n\x12PlanResourceChange\x12%.tfplugin6.PlanResourceChange.Request\x1a&.tfplugin6.PlanResourceChange.Response\x12\x66\n\x13\x41pplyResourceChange\x12&.tfplugin6.ApplyResourceChange.Request\x1a\'.tfplugin6.ApplyResourceChange.Response\x12\x66\n\x13ImportResourceState\x12&.tfplugin6.ImportResourceState.Request\x1a\'.tfplugin6.ImportResourceState.Response\x12`\n\x11MoveResourceState\x12$.tfplugin6.MoveResourceState.Request\x1a%.tfplugin6.MoveResourceState.Response\x12W\n\x0eReadDataSource\x12!.tfplugin6.ReadDataSource.Request\x1a".tfplugin6.ReadDataSource.Response\x12Q\n\x0cGetFunctions\x12\x1f.tfplugin6.GetFunctions.Request\x1a .tfplugin6.GetFunctions.Response\x12Q\n\x0c\x43\x61llFunction\x12\x1f.tfplugin6.CallFunction.Request\x1a .tfplugin6.CallFunction.Response\x12Q\n\x0cStopProvider\x12\x1f.tfplugin6.StopProvider.Request\x1a .tfplugin6.StopProvider.ResponseB1Z/github.com/opentofu/opentofu/internal/tfplugin6b\x06proto3'  # noqa: E501
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "tfplugin_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS is False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z/github.com/opentofu/opentofu/internal/tfplugin6"
    _globals["_RAWSTATE_FLATMAPENTRY"]._options = None
    _globals["_RAWSTATE_FLATMAPENTRY"]._serialized_options = b"8\001"
    _globals["_SCHEMA_OBJECT"].fields_by_name["min_items"]._options = None
    _globals["_SCHEMA_OBJECT"].fields_by_name["min_items"]._serialized_options = b"\030\001"
    _globals["_SCHEMA_OBJECT"].fields_by_name["max_items"]._options = None
    _globals["_SCHEMA_OBJECT"].fields_by_name["max_items"]._serialized_options = b"\030\001"
    _globals["_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY"]._options = None
    _globals["_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY"]._serialized_options = b"8\001"
    _globals["_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY"]._options = None
    _globals["_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY"]._serialized_options = b"8\001"
    _globals["_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY"]._options = None
    _globals["_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY"]._serialized_options = b"8\001"
    _globals["_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY"]._options = None
    _globals["_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY"]._serialized_options = b"8\001"
    _globals["_STRINGKIND"]._serialized_start = 6710
    _globals["_STRINGKIND"]._serialized_end = 6747
    _globals["_DYNAMICVALUE"]._serialized_start = 29
    _globals["_DYNAMICVALUE"]._serialized_end = 74
    _globals["_DIAGNOSTIC"]._serialized_start = 77
    _globals["_DIAGNOSTIC"]._serialized_end = 266
    _globals["_DIAGNOSTIC_SEVERITY"]._serialized_start = 219
    _globals["_DIAGNOSTIC_SEVERITY"]._serialized_end = 266
    _globals["_FUNCTIONERROR"]._serialized_start = 268
    _globals["_FUNCTIONERROR"]._serialized_end = 351
    _globals["_ATTRIBUTEPATH"]._serialized_start = 354
    _globals["_ATTRIBUTEPATH"]._serialized_end = 518
    _globals["_ATTRIBUTEPATH_STEP"]._serialized_start = 417
    _globals["_ATTRIBUTEPATH_STEP"]._serialized_end = 518
    _globals["_STOPPROVIDER"]._serialized_start = 520
    _globals["_STOPPROVIDER"]._serialized_end = 572
    _globals["_STOPPROVIDER_REQUEST"]._serialized_start = 536
    _globals["_STOPPROVIDER_REQUEST"]._serialized_end = 545
    _globals["_STOPPROVIDER_RESPONSE"]._serialized_start = 547
    _globals["_STOPPROVIDER_RESPONSE"]._serialized_end = 572
    _globals["_RAWSTATE"]._serialized_start = 574
    _globals["_RAWSTATE"]._serialized_end = 697
    _globals["_RAWSTATE_FLATMAPENTRY"]._serialized_start = 651
    _globals["_RAWSTATE_FLATMAPENTRY"]._serialized_end = 697
    _globals["_SCHEMA"]._serialized_start = 700
    _globals["_SCHEMA"]._serialized_end = 1716
    _globals["_SCHEMA_BLOCK"]._serialized_start = 768
    _globals["_SCHEMA_BLOCK"]._serialized_end = 983
    _globals["_SCHEMA_ATTRIBUTE"]._serialized_start = 986
    _globals["_SCHEMA_ATTRIBUTE"]._serialized_end = 1235
    _globals["_SCHEMA_NESTEDBLOCK"]._serialized_start = 1238
    _globals["_SCHEMA_NESTEDBLOCK"]._serialized_end = 1487
    _globals["_SCHEMA_NESTEDBLOCK_NESTINGMODE"]._serialized_start = 1410
    _globals["_SCHEMA_NESTEDBLOCK_NESTINGMODE"]._serialized_end = 1487
    _globals["_SCHEMA_OBJECT"]._serialized_start = 1490
    _globals["_SCHEMA_OBJECT"]._serialized_end = 1716
    _globals["_SCHEMA_OBJECT_NESTINGMODE"]._serialized_start = 1410
    _globals["_SCHEMA_OBJECT_NESTINGMODE"]._serialized_end = 1476
    _globals["_FUNCTION"]._serialized_start = 1719
    _globals["_FUNCTION"]._serialized_end = 2191
    _globals["_FUNCTION_PARAMETER"]._serialized_start = 2002
    _globals["_FUNCTION_PARAMETER"]._serialized_end = 2167
    _globals["_FUNCTION_RETURN"]._serialized_start = 2169
    _globals["_FUNCTION_RETURN"]._serialized_end = 2191
    _globals["_SERVERCAPABILITIES"]._serialized_start = 2193
    _globals["_SERVERCAPABILITIES"]._serialized_end = 2302
    _globals["_GETMETADATA"]._serialized_start = 2305
    _globals["_GETMETADATA"]._serialized_end = 2745
    _globals["_GETMETADATA_REQUEST"]._serialized_start = 536
    _globals["_GETMETADATA_REQUEST"]._serialized_end = 545
    _globals["_GETMETADATA_RESPONSE"]._serialized_start = 2332
    _globals["_GETMETADATA_RESPONSE"]._serialized_end = 2631
    _globals["_GETMETADATA_FUNCTIONMETADATA"]._serialized_start = 2633
    _globals["_GETMETADATA_FUNCTIONMETADATA"]._serialized_end = 2665
    _globals["_GETMETADATA_DATASOURCEMETADATA"]._serialized_start = 2667
    _globals["_GETMETADATA_DATASOURCEMETADATA"]._serialized_end = 2706
    _globals["_GETMETADATA_RESOURCEMETADATA"]._serialized_start = 2708
    _globals["_GETMETADATA_RESOURCEMETADATA"]._serialized_end = 2745
    _globals["_GETPROVIDERSCHEMA"]._serialized_start = 2748
    _globals["_GETPROVIDERSCHEMA"]._serialized_end = 3447
    _globals["_GETPROVIDERSCHEMA_REQUEST"]._serialized_start = 536
    _globals["_GETPROVIDERSCHEMA_REQUEST"]._serialized_end = 545
    _globals["_GETPROVIDERSCHEMA_RESPONSE"]._serialized_start = 2781
    _globals["_GETPROVIDERSCHEMA_RESPONSE"]._serialized_end = 3447
    _globals["_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY"]._serialized_start = 3226
    _globals["_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY"]._serialized_end = 3299
    _globals["_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY"]._serialized_start = 3301
    _globals["_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY"]._serialized_end = 3376
    _globals["_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY"]._serialized_start = 3378
    _globals["_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY"]._serialized_end = 3447
    _globals["_VALIDATEPROVIDERCONFIG"]._serialized_start = 3450
    _globals["_VALIDATEPROVIDERCONFIG"]._serialized_end = 3582
    _globals["_VALIDATEPROVIDERCONFIG_REQUEST"]._serialized_start = 3476
    _globals["_VALIDATEPROVIDERCONFIG_REQUEST"]._serialized_end = 3526
    _globals["_VALIDATEPROVIDERCONFIG_RESPONSE"]._serialized_start = 3528
    _globals["_VALIDATEPROVIDERCONFIG_RESPONSE"]._serialized_end = 3582
    _globals["_UPGRADERESOURCESTATE"]._serialized_start = 3585
    _globals["_UPGRADERESOURCESTATE"]._serialized_end = 3799
    _globals["_UPGRADERESOURCESTATE_REQUEST"]._serialized_start = 3609
    _globals["_UPGRADERESOURCESTATE_REQUEST"]._serialized_end = 3694
    _globals["_UPGRADERESOURCESTATE_RESPONSE"]._serialized_start = 3696
    _globals["_UPGRADERESOURCESTATE_RESPONSE"]._serialized_end = 3799
    _globals["_VALIDATERESOURCECONFIG"]._serialized_start = 3802
    _globals["_VALIDATERESOURCECONFIG"]._serialized_end = 3953
    _globals["_VALIDATERESOURCECONFIG_REQUEST"]._serialized_start = 3828
    _globals["_VALIDATERESOURCECONFIG_REQUEST"]._serialized_end = 3897
    _globals["_VALIDATERESOURCECONFIG_RESPONSE"]._serialized_start = 3899
    _globals["_VALIDATERESOURCECONFIG_RESPONSE"]._serialized_end = 3953
    _globals["_VALIDATEDATARESOURCECONFIG"]._serialized_start = 3956
    _globals["_VALIDATEDATARESOURCECONFIG"]._serialized_end = 4111
    _globals["_VALIDATEDATARESOURCECONFIG_REQUEST"]._serialized_start = 3828
    _globals["_VALIDATEDATARESOURCECONFIG_REQUEST"]._serialized_end = 3897
    _globals["_VALIDATEDATARESOURCECONFIG_RESPONSE"]._serialized_start = 3899
    _globals["_VALIDATEDATARESOURCECONFIG_RESPONSE"]._serialized_end = 3953
    _globals["_CONFIGUREPROVIDER"]._serialized_start = 4114
    _globals["_CONFIGUREPROVIDER"]._serialized_end = 4268
    _globals["_CONFIGUREPROVIDER_REQUEST"]._serialized_start = 4135
    _globals["_CONFIGUREPROVIDER_REQUEST"]._serialized_end = 4212
    _globals["_CONFIGUREPROVIDER_RESPONSE"]._serialized_start = 3899
    _globals["_CONFIGUREPROVIDER_RESPONSE"]._serialized_end = 3953
    _globals["_READRESOURCE"]._serialized_start = 4271
    _globals["_READRESOURCE"]._serialized_end = 4546
    _globals["_READRESOURCE_REQUEST"]._serialized_start = 4288
    _globals["_READRESOURCE_REQUEST"]._serialized_end = 4429
    _globals["_READRESOURCE_RESPONSE"]._serialized_start = 4431
    _globals["_READRESOURCE_RESPONSE"]._serialized_end = 4546
    _globals["_PLANRESOURCECHANGE"]._serialized_start = 4549
    _globals["_PLANRESOURCECHANGE"]._serialized_end = 5021
    _globals["_PLANRESOURCECHANGE_REQUEST"]._serialized_start = 4572
    _globals["_PLANRESOURCECHANGE_REQUEST"]._serialized_end = 4811
    _globals["_PLANRESOURCECHANGE_RESPONSE"]._serialized_start = 4814
    _globals["_PLANRESOURCECHANGE_RESPONSE"]._serialized_end = 5021
    _globals["_APPLYRESOURCECHANGE"]._serialized_start = 5024
    _globals["_APPLYRESOURCECHANGE"]._serialized_end = 5430
    _globals["_APPLYRESOURCECHANGE_REQUEST"]._serialized_start = 5048
    _globals["_APPLYRESOURCECHANGE_REQUEST"]._serialized_end = 5284
    _globals["_APPLYRESOURCECHANGE_RESPONSE"]._serialized_start = 5287
    _globals["_APPLYRESOURCECHANGE_RESPONSE"]._serialized_end = 5430
    _globals["_IMPORTRESOURCESTATE"]._serialized_start = 5433
    _globals["_IMPORTRESOURCESTATE"]._serialized_end = 5726
    _globals["_IMPORTRESOURCESTATE_REQUEST"]._serialized_start = 5456
    _globals["_IMPORTRESOURCESTATE_REQUEST"]._serialized_end = 5496
    _globals["_IMPORTRESOURCESTATE_IMPORTEDRESOURCE"]._serialized_start = 5498
    _globals["_IMPORTRESOURCESTATE_IMPORTEDRESOURCE"]._serialized_end = 5592
    _globals["_IMPORTRESOURCESTATE_RESPONSE"]._serialized_start = 5595
    _globals["_IMPORTRESOURCESTATE_RESPONSE"]._serialized_end = 5726
    _globals["_MOVERESOURCESTATE"]._serialized_start = 5729
    _globals["_MOVERESOURCESTATE"]._serialized_end = 6070
    _globals["_MOVERESOURCESTATE_REQUEST"]._serialized_start = 5751
    _globals["_MOVERESOURCESTATE_REQUEST"]._serialized_end = 5943
    _globals["_MOVERESOURCESTATE_RESPONSE"]._serialized_start = 5945
    _globals["_MOVERESOURCESTATE_RESPONSE"]._serialized_end = 6070
    _globals["_READDATASOURCE"]._serialized_start = 6073
    _globals["_READDATASOURCE"]._serialized_end = 6304
    _globals["_READDATASOURCE_REQUEST"]._serialized_start = 6091
    _globals["_READDATASOURCE_REQUEST"]._serialized_end = 6208
    _globals["_READDATASOURCE_RESPONSE"]._serialized_start = 6210
    _globals["_READDATASOURCE_RESPONSE"]._serialized_end = 6304
    _globals["_GETFUNCTIONS"]._serialized_start = 6307
    _globals["_GETFUNCTIONS"]._serialized_end = 6528
    _globals["_GETFUNCTIONS_REQUEST"]._serialized_start = 536
    _globals["_GETFUNCTIONS_REQUEST"]._serialized_end = 545
    _globals["_GETFUNCTIONS_RESPONSE"]._serialized_start = 6335
    _globals["_GETFUNCTIONS_RESPONSE"]._serialized_end = 6528
    _globals["_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY"]._serialized_start = 3378
    _globals["_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY"]._serialized_end = 3447
    _globals["_CALLFUNCTION"]._serialized_start = 6531
    _globals["_CALLFUNCTION"]._serialized_end = 6708
    _globals["_CALLFUNCTION_REQUEST"]._serialized_start = 6547
    _globals["_CALLFUNCTION_REQUEST"]._serialized_end = 6614
    _globals["_CALLFUNCTION_RESPONSE"]._serialized_start = 6616
    _globals["_CALLFUNCTION_RESPONSE"]._serialized_end = 6708
    _globals["_PROVIDER"]._serialized_start = 6750
    _globals["_PROVIDER"]._serialized_end = 8322
# @@protoc_insertion_point(module_scope)
