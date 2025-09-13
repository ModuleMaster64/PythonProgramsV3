import gifos
from datetime import datetime
import os
import shutil
from PIL import Image, ImageSequence

# Timestamp and version info
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
version = "v3.2.1"
build_id = datetime.utcnow().strftime('%Y%m%d%H%M%S')

# Create terminal canvas
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Boot-up sequence
pad_frame("Booting PythonProgramsV3 OS...", row_num=1)
pad_frame("Created by ModuleMaster64", row_num=2)
pad_frame(f"Version: {version} | Build: {build_id}", row_num=3)
pad_frame("> Initializing modules", row_num=4)
pad_frame("> Loading plugins", row_num=5)
pad_frame("> Starting shell interface", row_num=6)
pad_frame("> Checking system integrity", row_num=7)
pad_frame("> Mounting virtual drives", row_num=8)
pad_frame("> Verifying dependencies", row_num=9)
pad_frame("> Establishing network link", row_num=10)
pad_frame("> Syncing environment variables", row_num=11)
pad_frame("> Scanning for updates", row_num=12)
pad_frame("> Applying security patches", row_num=13)
pad_frame("> Launching background services", row_num=14)
pad_frame("> Preparing user interface", row_num=15)

# Spinner animation
spinner = ["|", "/", "-", "\\"]
spinner_row = 16
for i in range(22):
    frame = spinner[i % len(spinner)]
    dots = "." * (i % 4)
    pad_frame(f"> Finalizing startup{dots} {frame}", row_num=spinner_row)

# Simulated login sequence
login_row = spinner_row + 1
pad_frame("Login: ModuleMaster64", row_num=login_row)
pad_frame("Password: **************", row_num=login_row + 1)

auth_frames = ["Authenticating.", "Authenticating..", "Authenticating..."]
for frame in auth_frames:
    pad_frame(frame, row_num=login_row + 2)

pad_frame("Access granted!", row_num=login_row + 3)
pad_frame(f"System ready @ {timestamp}", row_num=login_row + 4)
pad_frame("Welcome, ModuleMaster64", row_num=login_row + 5)

# Blinking cursor effect
cursor_row = login_row + 6
for i in range(6):
    blink = "_" if i % 2 == 0 else " "
    pad_frame(blink, row_num=cursor_row, repeats=6)

# Generate GIF
t.gen_gif()

# Save to assets folder
os.makedirs("assets", exist_ok=True)
shutil.move("output.gif", "assets/terminal.gif")

# Post-process with Pillow to slow down playback
original = Image.open("assets/terminal.gif")
frames = [frame.copy() for frame in ImageSequence.Iterator(original)]

frames[0].save(
    "assets/terminal_slow.gif",
    save_all=True,
    append_images=frames[1:],
    duration=1250,  # 1.25 seconds per frame
    loop=0
)
