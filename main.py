import subprocess
import signal
import sys
import time
from pathlib import Path


SCRIPT_1 = Path("/home/user/flask.py")
SCRIPT_2 = Path("/home/user/serial.py")


class ProcessManager:
    def __init__(self):
        self.processes = []

    def start_process(self, script_path):
        """Start a Python script as a subprocess."""
        proc = subprocess.Popen(
            [sys.executable, str(script_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"[INFO] Started {script_path.name} (PID={proc.pid})")
        self.processes.append(proc)

    def stop_all(self):
        """Terminate all running processes."""
        print("[INFO] Stopping all processes...")
        for proc in self.processes:
            if proc.poll() is None:
                proc.terminate()

        # Give them time to exit gracefully
        time.sleep(2)

        # Force kill if still alive
        for proc in self.processes:
            if proc.poll() is None:
                print(f"[WARN] Force killing PID={proc.pid}")
                proc.kill()

    def monitor(self):
        """Monitor processes and restart/exit logic."""
        try:
            while True:
                for proc in self.processes:
                    if proc.poll() is not None:
                        print(f"[ERROR] Process PID={proc.pid} exited with code {proc.returncode}")
                        self.stop_all()
                        sys.exit(1)

                time.sleep(1)

        except KeyboardInterrupt:
            print("\n[INFO] Keyboard interrupt received")
            self.stop_all()


def handle_signal(signum, frame):
    print(f"[INFO] Signal {signum} received, shutting down...")
    manager.stop_all()
    sys.exit(0)


if __name__ == "__main__":
    manager = ProcessManager()

    # Register signal handlers for clean shutdown
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    # Start both scripts
    manager.start_process(SCRIPT_1)
    manager.start_process(SCRIPT_2)

    # Monitor them
    manager.monitor()