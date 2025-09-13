import gifos
from datetime import datetime
import os
import shutil
import time

# Timestamp for boot message
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
version = "v3.2.1"
build_id = datetime.utcnow().strftime('%Y%m%d%H%M%S')

# Create terminal canvas
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Boot-up sequence
t.gen_text(text="Booting PythonProgramsV3 OS...", row_num=1)
time.sleep(0.3)
t.gen_text(text="Created by ModuleMaster64", row_num=2)
time.sleep(0.3)
t.gen_text(text=f"Version: {version} | Build: {build_id}", row_num=3)
time.sleep(0.3)

t.gen_text(text="> Initializing modules", row_num=4)
time.sleep(0.3)
t.gen_text(text="> Loading plugins", row_num=5)
time.sleep(0.3)
t.gen_text(text="> Starting shell interface", row_num=6)
time.sleep(0.3)

# Spinner animation
spinner = ["|", "/", "-", "\\"]
for i in range(12):
    frame = spinner[i % len(spinner)]
    dots = "." * (i % 4)
    t.gen_text(text=f"> Finalizing startup{dots} {frame}", row_num=7 + i)
    time.sleep(0.2)

# Simulated login sequence
t.gen_text(text="Login: ModuleMaster64", row_num=20)
time.sleep(0.3)
t.gen_text(text="Password: **************", row_num=21)
time.sleep(0.3)

auth_frames = ["Authenticating.", "Authenticating..", "Authenticating..."]
for i, frame in enumerate(auth_frames):
    t.gen_text(text=frame, row_num=22 + i)
    time.sleep(0.3)

t.gen_text(text="Access granted ✅", row_num=25)
time.sleep(0.3)
t.gen_text(text=f"System ready @ {timestamp}", row_num=26)

# Generate GIF (default output: output.gif)
t.gen_gif()

# Move to assets folder with correct name
os.makedirs("assets", exist_ok=True)
shutil.move("output.gif", "assets/terminal.gif")
