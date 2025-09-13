import gifos
from datetime import datetime

timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

t.gen_text(text="Booting PythonProgramsV3 OS...", row_num=1)
t.gen_text(text="Created by ModuleMaster64", row_num=2)

t.gen_text(text="> Initializing modules", row_num=4)
t.gen_text(text="> Loading plugins", row_num=5)
t.gen_text(text="> Starting shell interface", row_num=6)

spinner = ["|", "/", "-", "\\"]
for i in range(12):
    frame = spinner[i % len(spinner)]
    t.gen_text(text=f"> Finalizing startup... {frame}", row_num=7 + i)

t.gen_text(text=f"System ready @ {timestamp}", row_num=20)
t.gen_gif("assets/terminal.gif", frame_duration=0.2)

