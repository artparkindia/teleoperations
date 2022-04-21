import os
import toml
import click
import signal
import asyncio
from pathlib import Path

class ExecuteProcess(object):
    def __init__(self, commands):
        self.commands = commands
        self.processes = {}
        self.terminate_status = False

    def terminate(self):
        self.terminate_status = True
        [
            process.terminate()
            for process in self.processes.values()
            if process.returncode is None
        ]
    
    def terminate_video(self):
        for name in ["ffmpeg", "ffplay"]:
            try:
               # iterating through each instance of the process
                for line in os.popen("ps -ef | grep " + name):
                    fields = line.split()
                    # extracting Process ID from the output
                    pid = fields[1]
                    # terminating process
                    os.kill(int(pid), signal.SIGKILL)
                print(f"{name} Process Successfully terminated")
            except:
                print(f"Error Encountered while killing {name}")

    async def execute(self):
        running = True 
        for name, command in self.commands.items():
            try:
                self.processes[name] = await asyncio.create_subprocess_exec(*command)
            except OSError as e:
                running = True 
                self.terminate()
        wait_list = [process.wait() for process in self.processes.values()]
        if running: #wait for process to die
            _, wait_list = await asyncio.wait(
                wait_list, return_when=asyncio.FIRST_COMPLETED
            )
            running = False
        if not self.terminate_status: #kill all other processes
            self.terminate()
            self.terminate_video()

def gather_processes(processes, mode):
    all_processes = {}
    for p in processes[mode]:
        all_processes[p] = processes[p]
    return all_processes

async def run(mode):
    processes = toml.load(os.environ["COMMON_CONFIG"])["processes"] 
    process_group = gather_processes(processes, mode)    
    executor = ExecuteProcess(process_group)
    await executor.execute()

@click.command()
@click.option("--mode", default="driver", help="driver/ robot")
def main_loop(mode):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(mode))
    loop.close()

if __name__ == "__main__":
    main_loop()
