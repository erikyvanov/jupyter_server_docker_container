from jupyter_server.serverapp import ServerApp
from jupyter_server.auth.security import set_password


def add_ignore_patterns(app: ServerApp):
    c = app.config

    c.FileContentsManager.ignore_patterns.extend([
        "*.key",
        "*.pem",
        "id_rsa",
        "id_ecdsa",
        "id_dsa",
        "*.pub",

        ".ssh",
        ".ssh/*",
        "ssh_config",
    ])
    app.log.info("Patterns of ignoring sensitive files configured.")


def set_trusted_origins(app: ServerApp):
    c = app.config

    c.ServerApp.trusted_origins = [
        "*",
        # "https://tunombrededominio.com", # Replace * with your domain
    ]
    app.log.info(
        f"trusted_origins: {c.ServerApp.trusted_origins}")


def allow_remote_access(app: ServerApp):
    c = app.config

    c.ServerApp.allow_remote_access = True
    app.log.info(
        f"allow_remote_access: {c.ServerApp.allow_remote_access}")


def set_server_ip(app: ServerApp):
    c = app.config

    c.ServerApp.ip = '0.0.0.0'
    app.log.info(f"ServerApp.ip configured: {c.ServerApp.ip}")


def set_jupyter_password(app: ServerApp):
    c = app.config

    set_password("password")
    app.log.info(
        "Password for Jupyter Server configured (stored hash).")


def set_restrictions(app: ServerApp):
    c = app.config

    c.ServerApp.allow_shutdown = False

    app.log.info(
        f"allow_shutdown: {c.ServerApp.allow_shutdown}")


def load_config(app: ServerApp):
    app.log.info(
        "Loading custom configuration for Jupyter Server...")

    add_ignore_patterns(app)
    set_trusted_origins(app)
    allow_remote_access(app)
    set_server_ip(app)
    set_jupyter_password(app)
    set_restrictions(app)


def initialize(app: ServerApp):
    load_config(app)


def main():
    initialize(ServerApp.instance())


main()
