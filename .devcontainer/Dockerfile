ARG VARIANT="3"

FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

USER vscode
WORKDIR /home/vscode

RUN mkdir -p .config/git \
 && echo ".vscode/*" >> .config/git/ignore \
 && echo "*.code-workspace" >> .config/git/ignore \
 && echo ".history/" >> .config/git/ignore
