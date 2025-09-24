# Use the official Home Assistant Core image as base
FROM ghcr.io/home-assistant/home-assistant:stable

# Set timezone (optional, change to yours)
ENV TZ=America/Toronto

# Create a volume for configs (Render persistent disk can mount here)
VOLUME /config

# Expose Home Assistant’s default port
EXPOSE 8123

# Run Home Assistant
CMD [ "python3", "-m", "homeassistant", "--config", "/config" ]
