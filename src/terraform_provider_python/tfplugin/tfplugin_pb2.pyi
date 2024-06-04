from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class StringKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAIN: _ClassVar[StringKind]
    MARKDOWN: _ClassVar[StringKind]

PLAIN: StringKind
MARKDOWN: StringKind

class DynamicValue(_message.Message):
    __slots__ = ("msgpack", "json")
    MSGPACK_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    msgpack: bytes
    json: bytes
    def __init__(self, msgpack: bytes | None = ..., json: bytes | None = ...) -> None: ...

class Diagnostic(_message.Message):
    __slots__ = ("severity", "summary", "detail", "attribute")

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[Diagnostic.Severity]
        ERROR: _ClassVar[Diagnostic.Severity]
        WARNING: _ClassVar[Diagnostic.Severity]

    INVALID: Diagnostic.Severity
    ERROR: Diagnostic.Severity
    WARNING: Diagnostic.Severity
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    severity: Diagnostic.Severity
    summary: str
    detail: str
    attribute: AttributePath
    def __init__(
        self,
        severity: Diagnostic.Severity | str | None = ...,
        summary: str | None = ...,
        detail: str | None = ...,
        attribute: AttributePath | _Mapping | None = ...,
    ) -> None: ...

class FunctionError(_message.Message):
    __slots__ = ("text", "function_argument")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    text: str
    function_argument: int
    def __init__(self, text: str | None = ..., function_argument: int | None = ...) -> None: ...

class AttributePath(_message.Message):
    __slots__ = ("steps",)

    class Step(_message.Message):
        __slots__ = ("attribute_name", "element_key_string", "element_key_int")
        ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_KEY_STRING_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_KEY_INT_FIELD_NUMBER: _ClassVar[int]
        attribute_name: str
        element_key_string: str
        element_key_int: int
        def __init__(
            self,
            attribute_name: str | None = ...,
            element_key_string: str | None = ...,
            element_key_int: int | None = ...,
        ) -> None: ...

    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[AttributePath.Step]
    def __init__(self, steps: _Iterable[AttributePath.Step | _Mapping] | None = ...) -> None: ...

class StopProvider(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Response(_message.Message):
        __slots__ = ("Error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        Error: str
        def __init__(self, Error: str | None = ...) -> None: ...

    def __init__(self) -> None: ...

class RawState(_message.Message):
    __slots__ = ("json", "flatmap")

    class FlatmapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: str | None = ..., value: str | None = ...) -> None: ...

    JSON_FIELD_NUMBER: _ClassVar[int]
    FLATMAP_FIELD_NUMBER: _ClassVar[int]
    json: bytes
    flatmap: _containers.ScalarMap[str, str]
    def __init__(self, json: bytes | None = ..., flatmap: _Mapping[str, str] | None = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ("version", "block")

    class Block(_message.Message):
        __slots__ = ("version", "attributes", "block_types", "description", "description_kind", "deprecated")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        BLOCK_TYPES_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KIND_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        version: int
        attributes: _containers.RepeatedCompositeFieldContainer[Schema.Attribute]
        block_types: _containers.RepeatedCompositeFieldContainer[Schema.NestedBlock]
        description: str
        description_kind: StringKind
        deprecated: bool
        def __init__(
            self,
            version: int | None = ...,
            attributes: _Iterable[Schema.Attribute | _Mapping] | None = ...,
            block_types: _Iterable[Schema.NestedBlock | _Mapping] | None = ...,
            description: str | None = ...,
            description_kind: StringKind | str | None = ...,
            deprecated: bool = ...,
        ) -> None: ...

    class Attribute(_message.Message):
        __slots__ = (
            "name",
            "type",
            "nested_type",
            "description",
            "required",
            "optional",
            "computed",
            "sensitive",
            "description_kind",
            "deprecated",
        )
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NESTED_TYPE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_FIELD_NUMBER: _ClassVar[int]
        COMPUTED_FIELD_NUMBER: _ClassVar[int]
        SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KIND_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: bytes
        nested_type: Schema.Object
        description: str
        required: bool
        optional: bool
        computed: bool
        sensitive: bool
        description_kind: StringKind
        deprecated: bool
        def __init__(
            self,
            name: str | None = ...,
            type: bytes | None = ...,
            nested_type: Schema.Object | _Mapping | None = ...,
            description: str | None = ...,
            required: bool = ...,
            optional: bool = ...,
            computed: bool = ...,
            sensitive: bool = ...,
            description_kind: StringKind | str | None = ...,
            deprecated: bool = ...,
        ) -> None: ...

    class NestedBlock(_message.Message):
        __slots__ = ("type_name", "block", "nesting", "min_items", "max_items")

        class NestingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INVALID: _ClassVar[Schema.NestedBlock.NestingMode]
            SINGLE: _ClassVar[Schema.NestedBlock.NestingMode]
            LIST: _ClassVar[Schema.NestedBlock.NestingMode]
            SET: _ClassVar[Schema.NestedBlock.NestingMode]
            MAP: _ClassVar[Schema.NestedBlock.NestingMode]
            GROUP: _ClassVar[Schema.NestedBlock.NestingMode]

        INVALID: Schema.NestedBlock.NestingMode
        SINGLE: Schema.NestedBlock.NestingMode
        LIST: Schema.NestedBlock.NestingMode
        SET: Schema.NestedBlock.NestingMode
        MAP: Schema.NestedBlock.NestingMode
        GROUP: Schema.NestedBlock.NestingMode
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        BLOCK_FIELD_NUMBER: _ClassVar[int]
        NESTING_FIELD_NUMBER: _ClassVar[int]
        MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
        MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        block: Schema.Block
        nesting: Schema.NestedBlock.NestingMode
        min_items: int
        max_items: int
        def __init__(
            self,
            type_name: str | None = ...,
            block: Schema.Block | _Mapping | None = ...,
            nesting: Schema.NestedBlock.NestingMode | str | None = ...,
            min_items: int | None = ...,
            max_items: int | None = ...,
        ) -> None: ...

    class Object(_message.Message):
        __slots__ = ("attributes", "nesting", "min_items", "max_items")

        class NestingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INVALID: _ClassVar[Schema.Object.NestingMode]
            SINGLE: _ClassVar[Schema.Object.NestingMode]
            LIST: _ClassVar[Schema.Object.NestingMode]
            SET: _ClassVar[Schema.Object.NestingMode]
            MAP: _ClassVar[Schema.Object.NestingMode]

        INVALID: Schema.Object.NestingMode
        SINGLE: Schema.Object.NestingMode
        LIST: Schema.Object.NestingMode
        SET: Schema.Object.NestingMode
        MAP: Schema.Object.NestingMode
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        NESTING_FIELD_NUMBER: _ClassVar[int]
        MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
        MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
        attributes: _containers.RepeatedCompositeFieldContainer[Schema.Attribute]
        nesting: Schema.Object.NestingMode
        min_items: int
        max_items: int
        def __init__(
            self,
            attributes: _Iterable[Schema.Attribute | _Mapping] | None = ...,
            nesting: Schema.Object.NestingMode | str | None = ...,
            min_items: int | None = ...,
            max_items: int | None = ...,
        ) -> None: ...

    VERSION_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    version: int
    block: Schema.Block
    def __init__(self, version: int | None = ..., block: Schema.Block | _Mapping | None = ...) -> None: ...

class Function(_message.Message):
    __slots__ = (
        "parameters",
        "variadic_parameter",
        "summary",
        "description",
        "description_kind",
        "deprecation_message",
    )

    class Parameter(_message.Message):
        __slots__ = ("name", "type", "allow_null_value", "allow_unknown_values", "description", "description_kind")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_UNKNOWN_VALUES_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_KIND_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: bytes
        allow_null_value: bool
        allow_unknown_values: bool
        description: str
        description_kind: StringKind
        def __init__(
            self,
            name: str | None = ...,
            type: bytes | None = ...,
            allow_null_value: bool = ...,
            allow_unknown_values: bool = ...,
            description: str | None = ...,
            description_kind: StringKind | str | None = ...,
        ) -> None: ...

    class Return(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: bytes
        def __init__(self, type: bytes | None = ...) -> None: ...

    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    VARIADIC_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_KIND_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.RepeatedCompositeFieldContainer[Function.Parameter]
    variadic_parameter: Function.Parameter
    summary: str
    description: str
    description_kind: StringKind
    deprecation_message: str
    def __init__(
        self,
        parameters: _Iterable[Function.Parameter | _Mapping] | None = ...,
        variadic_parameter: Function.Parameter | _Mapping | None = ...,
        summary: str | None = ...,
        description: str | None = ...,
        description_kind: StringKind | str | None = ...,
        deprecation_message: str | None = ...,
        **kwargs,
    ) -> None: ...

class ServerCapabilities(_message.Message):
    __slots__ = ("plan_destroy", "get_provider_schema_optional", "move_resource_state")
    PLAN_DESTROY_FIELD_NUMBER: _ClassVar[int]
    GET_PROVIDER_SCHEMA_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    MOVE_RESOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
    plan_destroy: bool
    get_provider_schema_optional: bool
    move_resource_state: bool
    def __init__(self, plan_destroy: bool = ..., get_provider_schema_optional: bool = ..., move_resource_state: bool = ...) -> None: ...

class GetMetadata(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Response(_message.Message):
        __slots__ = ("server_capabilities", "diagnostics", "data_sources", "resources", "functions")
        SERVER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        server_capabilities: ServerCapabilities
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        data_sources: _containers.RepeatedCompositeFieldContainer[GetMetadata.DataSourceMetadata]
        resources: _containers.RepeatedCompositeFieldContainer[GetMetadata.ResourceMetadata]
        functions: _containers.RepeatedCompositeFieldContainer[GetMetadata.FunctionMetadata]
        def __init__(
            self,
            server_capabilities: ServerCapabilities | _Mapping | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
            data_sources: _Iterable[GetMetadata.DataSourceMetadata | _Mapping] | None = ...,
            resources: _Iterable[GetMetadata.ResourceMetadata | _Mapping] | None = ...,
            functions: _Iterable[GetMetadata.FunctionMetadata | _Mapping] | None = ...,
        ) -> None: ...

    class FunctionMetadata(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: str | None = ...) -> None: ...

    class DataSourceMetadata(_message.Message):
        __slots__ = ("type_name",)
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        def __init__(self, type_name: str | None = ...) -> None: ...

    class ResourceMetadata(_message.Message):
        __slots__ = ("type_name",)
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        def __init__(self, type_name: str | None = ...) -> None: ...

    def __init__(self) -> None: ...

class GetProviderSchema(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Response(_message.Message):
        __slots__ = (
            "provider",
            "resource_schemas",
            "data_source_schemas",
            "diagnostics",
            "provider_meta",
            "server_capabilities",
            "functions",
        )

        class ResourceSchemasEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Schema
            def __init__(self, key: str | None = ..., value: Schema | _Mapping | None = ...) -> None: ...

        class DataSourceSchemasEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Schema
            def __init__(self, key: str | None = ..., value: Schema | _Mapping | None = ...) -> None: ...

        class FunctionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Function
            def __init__(self, key: str | None = ..., value: Function | _Mapping | None = ...) -> None: ...

        PROVIDER_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
        DATA_SOURCE_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_META_FIELD_NUMBER: _ClassVar[int]
        SERVER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        provider: Schema
        resource_schemas: _containers.MessageMap[str, Schema]
        data_source_schemas: _containers.MessageMap[str, Schema]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        provider_meta: Schema
        server_capabilities: ServerCapabilities
        functions: _containers.MessageMap[str, Function]
        def __init__(
            self,
            provider: Schema | _Mapping | None = ...,
            resource_schemas: _Mapping[str, Schema] | None = ...,
            data_source_schemas: _Mapping[str, Schema] | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
            provider_meta: Schema | _Mapping | None = ...,
            server_capabilities: ServerCapabilities | _Mapping | None = ...,
            functions: _Mapping[str, Function] | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class ValidateProviderConfig(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("config",)
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        config: DynamicValue
        def __init__(self, config: DynamicValue | _Mapping | None = ...) -> None: ...

    class Response(_message.Message):
        __slots__ = ("diagnostics",)
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(self, diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...) -> None: ...

    def __init__(self) -> None: ...

class UpgradeResourceState(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "version", "raw_state")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        RAW_STATE_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        version: int
        raw_state: RawState
        def __init__(
            self,
            type_name: str | None = ...,
            version: int | None = ...,
            raw_state: RawState | _Mapping | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("upgraded_state", "diagnostics")
        UPGRADED_STATE_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        upgraded_state: DynamicValue
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(
            self,
            upgraded_state: DynamicValue | _Mapping | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class ValidateResourceConfig(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "config")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        config: DynamicValue
        def __init__(self, type_name: str | None = ..., config: DynamicValue | _Mapping | None = ...) -> None: ...

    class Response(_message.Message):
        __slots__ = ("diagnostics",)
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(self, diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...) -> None: ...

    def __init__(self) -> None: ...

class ValidateDataResourceConfig(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "config")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        config: DynamicValue
        def __init__(self, type_name: str | None = ..., config: DynamicValue | _Mapping | None = ...) -> None: ...

    class Response(_message.Message):
        __slots__ = ("diagnostics",)
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(self, diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...) -> None: ...

    def __init__(self) -> None: ...

class ConfigureProvider(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("terraform_version", "config")
        TERRAFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        terraform_version: str
        config: DynamicValue
        def __init__(self, terraform_version: str | None = ..., config: DynamicValue | _Mapping | None = ...) -> None: ...

    class Response(_message.Message):
        __slots__ = ("diagnostics",)
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(self, diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...) -> None: ...

    def __init__(self) -> None: ...

class ReadResource(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "current_state", "private", "provider_meta")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_META_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        current_state: DynamicValue
        private: bytes
        provider_meta: DynamicValue
        def __init__(
            self,
            type_name: str | None = ...,
            current_state: DynamicValue | _Mapping | None = ...,
            private: bytes | None = ...,
            provider_meta: DynamicValue | _Mapping | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("new_state", "diagnostics", "private")
        NEW_STATE_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_FIELD_NUMBER: _ClassVar[int]
        new_state: DynamicValue
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        private: bytes
        def __init__(
            self,
            new_state: DynamicValue | _Mapping | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
            private: bytes | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class PlanResourceChange(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "prior_state", "proposed_new_state", "config", "prior_private", "provider_meta")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        PRIOR_STATE_FIELD_NUMBER: _ClassVar[int]
        PROPOSED_NEW_STATE_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        PRIOR_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_META_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        prior_state: DynamicValue
        proposed_new_state: DynamicValue
        config: DynamicValue
        prior_private: bytes
        provider_meta: DynamicValue
        def __init__(
            self,
            type_name: str | None = ...,
            prior_state: DynamicValue | _Mapping | None = ...,
            proposed_new_state: DynamicValue | _Mapping | None = ...,
            config: DynamicValue | _Mapping | None = ...,
            prior_private: bytes | None = ...,
            provider_meta: DynamicValue | _Mapping | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("planned_state", "requires_replace", "planned_private", "diagnostics", "legacy_type_system")
        PLANNED_STATE_FIELD_NUMBER: _ClassVar[int]
        REQUIRES_REPLACE_FIELD_NUMBER: _ClassVar[int]
        PLANNED_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        LEGACY_TYPE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
        planned_state: DynamicValue
        requires_replace: _containers.RepeatedCompositeFieldContainer[AttributePath]
        planned_private: bytes
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        legacy_type_system: bool
        def __init__(
            self,
            planned_state: DynamicValue | _Mapping | None = ...,
            requires_replace: _Iterable[AttributePath | _Mapping] | None = ...,
            planned_private: bytes | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
            legacy_type_system: bool = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class ApplyResourceChange(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "prior_state", "planned_state", "config", "planned_private", "provider_meta")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        PRIOR_STATE_FIELD_NUMBER: _ClassVar[int]
        PLANNED_STATE_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        PLANNED_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_META_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        prior_state: DynamicValue
        planned_state: DynamicValue
        config: DynamicValue
        planned_private: bytes
        provider_meta: DynamicValue
        def __init__(
            self,
            type_name: str | None = ...,
            prior_state: DynamicValue | _Mapping | None = ...,
            planned_state: DynamicValue | _Mapping | None = ...,
            config: DynamicValue | _Mapping | None = ...,
            planned_private: bytes | None = ...,
            provider_meta: DynamicValue | _Mapping | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("new_state", "private", "diagnostics", "legacy_type_system")
        NEW_STATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        LEGACY_TYPE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
        new_state: DynamicValue
        private: bytes
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        legacy_type_system: bool
        def __init__(
            self,
            new_state: DynamicValue | _Mapping | None = ...,
            private: bytes | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
            legacy_type_system: bool = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class ImportResourceState(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "id")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        id: str
        def __init__(self, type_name: str | None = ..., id: str | None = ...) -> None: ...

    class ImportedResource(_message.Message):
        __slots__ = ("type_name", "state", "private")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        state: DynamicValue
        private: bytes
        def __init__(
            self,
            type_name: str | None = ...,
            state: DynamicValue | _Mapping | None = ...,
            private: bytes | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("imported_resources", "diagnostics")
        IMPORTED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        imported_resources: _containers.RepeatedCompositeFieldContainer[ImportResourceState.ImportedResource]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(
            self,
            imported_resources: _Iterable[ImportResourceState.ImportedResource | _Mapping] | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class MoveResourceState(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = (
            "source_provider_address",
            "source_type_name",
            "source_schema_version",
            "source_state",
            "target_type_name",
            "source_private",
        )
        SOURCE_PROVIDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        SOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
        TARGET_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        source_provider_address: str
        source_type_name: str
        source_schema_version: int
        source_state: RawState
        target_type_name: str
        source_private: bytes
        def __init__(
            self,
            source_provider_address: str | None = ...,
            source_type_name: str | None = ...,
            source_schema_version: int | None = ...,
            source_state: RawState | _Mapping | None = ...,
            target_type_name: str | None = ...,
            source_private: bytes | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("target_state", "diagnostics", "target_private")
        TARGET_STATE_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        TARGET_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        target_state: DynamicValue
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        target_private: bytes
        def __init__(
            self,
            target_state: DynamicValue | _Mapping | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
            target_private: bytes | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class ReadDataSource(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("type_name", "config", "provider_meta")
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_META_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        config: DynamicValue
        provider_meta: DynamicValue
        def __init__(
            self,
            type_name: str | None = ...,
            config: DynamicValue | _Mapping | None = ...,
            provider_meta: DynamicValue | _Mapping | None = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ("state", "diagnostics")
        STATE_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        state: DynamicValue
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(
            self,
            state: DynamicValue | _Mapping | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class GetFunctions(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Response(_message.Message):
        __slots__ = ("functions", "diagnostics")

        class FunctionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Function
            def __init__(self, key: str | None = ..., value: Function | _Mapping | None = ...) -> None: ...

        FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
        functions: _containers.MessageMap[str, Function]
        diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
        def __init__(
            self,
            functions: _Mapping[str, Function] | None = ...,
            diagnostics: _Iterable[Diagnostic | _Mapping] | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...

class CallFunction(_message.Message):
    __slots__ = ()

    class Request(_message.Message):
        __slots__ = ("name", "arguments")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        name: str
        arguments: _containers.RepeatedCompositeFieldContainer[DynamicValue]
        def __init__(self, name: str | None = ..., arguments: _Iterable[DynamicValue | _Mapping] | None = ...) -> None: ...

    class Response(_message.Message):
        __slots__ = ("result", "error")
        RESULT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        result: DynamicValue
        error: FunctionError
        def __init__(
            self,
            result: DynamicValue | _Mapping | None = ...,
            error: FunctionError | _Mapping | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...
