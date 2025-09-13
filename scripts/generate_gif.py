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

t.gen_text(text="Booting PythonProgramsV3 OS...", row_num=1)
time.sleep(1.25)

t.gen_text(text="Created by ModuleMaster64", row_num=2)
time.sleep(1.25)

t.gen_text(text=f"Version: {version} | Build: {build_id}", row_num=3)
time.sleep(1.25)

t.gen_text(text="> Initializing modules", row_num=4)
time.sleep(1.25)

t.gen_text(text="> Loading plugins", row_num=5)
time.sleep(1.25)

t.gen_text(text="> Starting shell interface", row_num=6)
time.sleep(1.25)

t.gen_text(text="> Checking system integrity", row_num=7)
time.sleep(1.25)

t.gen_text(text="> Mounting virtual drives", row_num=8)
time.sleep(1.25)

t.gen_text(text="> Verifying dependencies", row_num=9)
time.sleep(1.25)

t.gen_text(text="> Establishing network link", row_num=10)
time.sleep(1.25)

t.gen_text(text="> Syncing environment variables", row_num=11)
time.sleep(1.25)

t.gen_text(text="> Scanning for updates", row_num=12)
time.sleep(1.25)

t.gen_text(text="> Applying security patches", row_num=13)
time.sleep(1.25)

t.gen_text(text="> Launching background services", row_num=14)
time.sleep(1.25)

t.gen_text(text="> Preparing user interface", row_num=15)
time.sleep(1.25)

# Spinner animation (22 frames × 1s = ~22s)
spinner = ["|", "/", "-", "\\"]
spinner_row = len(boot_messages) + 1
for i in range(22):
    frame = spinner[i % len(spinner)]
    dots = "." * (i % 4)
    t.gen_text(text=f"> Finalizing startup{dots} {frame}", row_num=spinner_row)
    time.sleep(1)

# Simulated login sequence
login_row = spinner_row + 1
t.gen_text(text="Login: ModuleMaster64", row_num=login_row)
time.sleep(1)

t.gen_text(text="Password: **************", row_num=login_row + 1)
time.sleep(1)

auth_frames = ["Authenticating.", "Authenticating..", "Authenticating..."]
for frame in auth_frames:
    t.gen_text(text=frame, row_num=login_row + 2)
    time.sleep(1)

t.gen_text(text="Access granted!", row_num=login_row + 3)
time.sleep(1)

t.gen_text(text=f"System ready @ {timestamp}", row_num=login_row + 4)

# Generate GIF
t.gen_gif()

# Save to assets folder
os.makedirs("assets", exist_ok=True)
shutil.move("output.gif", "assets/terminal.gif")
