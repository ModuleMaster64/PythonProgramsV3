import gifos
from datetime import datetime
import os
import shutil
import time

# Timestamp and version info
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
version = "v3.2.1"
build_id = datetime.utcnow().strftime('%Y%m%d%H%M%S')

# Create terminal canvas
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Boot-up sequence
boot_messages = [
    "Booting PythonProgramsV3 OS...",
    "Created by ModuleMaster64",
    f"Version: {version} | Build: {build_id}",
    "> Initializing modules",
    "> Loading plugins",
    "> Starting shell interface",
    "> Checking system integrity",
    "> Mounting virtual drives",
    "> Verifying dependencies",
    "> Establishing network link",
    "> Syncing environment variables",
    "> Scanning for updates",
    "> Applying security patches",
    "> Launching background services",
    "> Preparing user interface"
]

for i, msg in enumerate(boot_messages, start=1):
    t.gen_text(text=msg, row_num=i)
    time.sleep(0.5)

# Spinner animation (45 frames × 0.5s = ~22.5s)
spinner = ["|", "/", "-", "\\"]
spinner_row = len(boot_messages) + 1
for i in range(45):
    frame = spinner[i % len(spinner)]
    dots = "." * (i % 4)
    t.gen_text(text=f"> Finalizing startup{dots} {frame}", row_num=spinner_row)
    time.sleep(0.5)

# Simulated login sequence
login_row = spinner_row + 1
t.gen_text(text="Login: ModuleMaster64", row_num=login_row)
time.sleep(0.5)

t.gen_text(text="Password: **************", row_num=login_row + 1)
time.sleep(0.5)

auth_frames = ["Authenticating.", "Authenticating..", "Authenticating..."]
for frame in auth_frames:
    t.gen_text(text=frame, row_num=login_row + 2)
    time.sleep(0.5)

t.gen_text(text="Access granted!", row_num=login_row + 3)
time.sleep(0.5)

t.gen_text(text=f"System ready @ {timestamp}", row_num=login_row + 4)

# Generate GIF
t.gen_gif()

# Save to assets folder
os.makedirs("assets", exist_ok=True)
shutil.move("output.gif", "assets/terminal.gif")
