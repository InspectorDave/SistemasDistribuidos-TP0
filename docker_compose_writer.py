import sys

name_lines = "name: tp0"

services_line = "services:"

server_lines = "\
  server:\n\
    container_name: server\n\
    image: server:latest\n\
    entrypoint: python3 /main.py\n\
    environment:\n\
      - PYTHONUNBUFFERED=1\n\
      - LOGGING_LEVEL=DEBUG\n\
    networks:\n\
      - testing_net\n"

client_lines = "\
  client{client_number}:\n\
    container_name: client{client_number}\n\
    image: client:latest\n\
    entrypoint: /client\n\
    environment:\n\
      - CLI_ID={client_number}\n\
      - CLI_LOG_LEVEL=DEBUG\n\
    networks:\n\
      - testing_net\n\
    depends_on:\n\
      - server\n"

networks_lines = "\
networks:\n\
  testing_net:\n\
    ipam:\n\
      driver: default\n\
      config:\n\
        - subnet: 172.25.125.0/24\n"

file = open(sys.argv[1], "w")

file.write(f"{name_lines}\n")
file.write(f"{services_line}\n")
file.write(f"{server_lines}\n")
for i in range(0, int(sys.argv[2])):
    file.write(f"{client_lines.format(client_number=i+1)}\n")
file.write(f"{networks_lines}")
