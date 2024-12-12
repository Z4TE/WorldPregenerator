from mcrcon import MCRcon
import tqdm

server_address  = "localhost"
server_port     = "25575"
server_pass     = "specify a good password"

radius = 128; # in chunks

range = radius << 4
start = range * -1 + 1

for x in tqdm.tqdm(range(start, range, 16)):
    for y in tqdm.tqdm(range(start, range, 16), leave = False):
        # generate chunks
        with MCRcon(server_address, server_pass, server_port) as mcr:
            mcr.command(f"forceload add {x} {y}")
            mcr.command(f"forceload remove {x} {y}")
