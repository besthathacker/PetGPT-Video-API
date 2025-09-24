# Use the official Home Assistant Core image
FROM ghcr.io/home-assistant/home-assistant:stable

# Set timezone (change if needed)
ENV TZ=America/Toronto

# Expose the port (Render maps $PORT automatically)
EXPOSE 8123

# Start Home Assistant using Render's PORT env variable
CMD python3 -m homeassistant --config /config
