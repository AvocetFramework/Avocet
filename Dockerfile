# Use a lightweight stable Ubuntu base image
FROM ubuntu:24.04

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install core build dependencies, 32-bit multilib cross-compilers, and toolchains
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc-multilib \
    g++-multilib \
    nasm \
    python3-dev \
    python3-pip \
    make \
    clean \
    && rm -rf /var/lib/apt/lists/*

# Set up the internal working directory
WORKDIR /workspace

# Default command keeps the container active or runs a build check
CMD ["make", "clean", "&&", "make"]
