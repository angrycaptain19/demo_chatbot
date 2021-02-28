# Pull SDK image as base image
FROM rasa/rasa-sdk:2.3.1
# FROM rasa/rasa:1.10.10

# Use subdirectory as working directory
WORKDIR /app

# Change to root user to install dependencies
USER root

RUN apt update -y && apt install -y openssh-server
COPY docker/action-server/entrypoint.sh ./
RUN chmod +x entrypoint.sh

# Copy actions requirements
COPY requirements.txt ./
RUN /opt/venv/bin/python -m pip install --upgrade pip
# Install extra requirements for actions code
RUN pip install -r requirements.txt

# Copy actions code to working directory
COPY actions /app/actions

# Don't use root user to run code
# USER 1001
# RUN chmod +x entrypoint.sh

# Start the action server
# CMD ["run", "actions", "--debug"]

# service ssh start &&

# ENTRYPOINT ["./entrypoint.sh"]
# CMD ["service", "ssh", "start"]
# RUN service ssh start
# CMD ["start", "--actions", "actions", "service", "ssh", "start"]
# CMD start --actions actions && service ssh start 'daemon off;'
# CMD service ssh start && start --actions actions

# ENTRYPOINT ["./entrypoint.sh"]
# CMD ["start", "--actions", "actions"]

