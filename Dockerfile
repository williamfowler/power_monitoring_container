# Use a base image that includes Python and is compatible with Raspberry Pi
FROM python:3.9

# Install required system packages
RUN apt-get update && apt-get install -y \
    i2c-tools \
    python3-dev \
    python3-pip \
    libffi-dev \
    libssl-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libbz2-dev \
    libsqlite3-dev \
    libz-dev \
    liblzma-dev \
    zlib1g-dev \
    build-essential \
    libudev-dev \
    libusb-1.0-0-dev \
    libpcap-dev \
    libgmp-dev \
    flex \
    bison \
    cmake \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# # Install required Python packages
RUN pip3 install adafruit-circuitpython-ina219 board RPi_GPIO

# Create a directory for the application
WORKDIR /app

# Copy the application code
COPY monitor_power.py .

# # Set the entry point to the Python script
# CMD ["python3", "monitor_power.py"]
CMD [ "sleep", "infinity" ]
