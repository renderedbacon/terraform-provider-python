# CODE DERIVED FROM: https://github.com/rpcplugin/python/blob/master/rpcplugin/tls.py
# LICENSE (MIT): https://github.com/rpcplugin/python/blob/master/LICENSE
# DESCRIPTION: This module provides a function to generate a self-signed
# certificate and private key for use in mutual TLS (mTLS) communication.

from base64 import standard_b64decode, standard_b64encode
from datetime import UTC, datetime, timedelta
from os import environ
from random import randint

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from grpc import ServerCredentials, ssl_server_credentials


def generate_certificate():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
    basic_contraints = x509.BasicConstraints(ca=True, path_length=0)
    now = datetime.now(UTC)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(randint(0, 2**128 - 1))
        .not_valid_before(now - timedelta(seconds=30))
        .not_valid_after(now + timedelta(hours=262980))
        .add_extension(basic_contraints, False)
        .sign(key, hashes.SHA256(), default_backend())
    )
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
    key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return [key_pem, cert_pem]


def raw_base64_to_pem_cert(cert: str):
    # We'll first round-trip through the base64 library to normalize any
    # required padding, which not all server implementations include when
    # generating their raw base64 certs.

    encoded: str = standard_b64encode(standard_b64decode(cert + "==="))
    length: int = 64
    wrapped: list[str] = [
        "-----BEGIN CERTIFICATE-----\n",
        "\n".join(encoded[i : i + length] for i in range(0, len(encoded), length)),
        "n-----END CERTIFICATE-----\n",
    ]

    return "".join(wrapped)


def auto_mtls() -> tuple[ServerCredentials, str]:
    client_cert = environ["PLUGIN_CLIENT_CERT"]
    server_cert = generate_certificate()

    # The rpc protocol wants just a straight base64 encoding of
    # the server certificate, but the cryptography library doesn't have a
    # facility to produce that directly, so we'll extract the base64
    # characters out of the PEM encoding instead.
    cert_pem_lines = server_cert[1].decode("us-ascii").split("\n")
    cert_pem_lines = cert_pem_lines[1:-2]
    cert_b64 = "".join(cert_pem_lines)

    return (
        ssl_server_credentials(
            [server_cert],
            client_cert,
            require_client_auth=True,
        ),
        cert_b64,
    )
