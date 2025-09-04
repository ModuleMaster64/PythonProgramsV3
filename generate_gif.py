import gifos
import time

t = gifos.Terminal(width=480, height=300, font_size=14, xpad=10, ypad=10)

# Simulated typing with delays
def type_line(text, row, delay=0.04):
    for i in range(1, len(text) + 1):
        t.gen_text(text[:i], row_num=row)
        time.sleep(delay)

# Boot sequence
type_line("🖥️ Booting PythonProgramsV3 OS...", 1)
type_line("🧬 PY-V3 Kernel v1.0.3 initializing...", 2)
type_line("🔍 Performing system checks...", 3)
type_line("[██████████] 100%", 4)
type_line("✅ Modules verified", 5)
type_line("🔐 Authenticating user: ModuleMaster64", 6)
type_line("🔓 Access granted", 7)
t.gen_text("", row_num=8)

# Welcome message
type_line("👋 Welcome back, ModuleMaster64!", 9)
type_line("📦 PythonProgramsV3 is ready to launch", 10)
t.gen_text("────────────────────────────────────────────", row_num=11)

# Module list
type_line("Available Modules:", 12)
type_line("[1] 🎲 Dice Game", 13)
type_line("[2] ➕ Maths Quiz", 14)
type_line("[3] 🐉 Monster Duel", 15)
type_line("[4] 🔞 Age Checker", 16)
type_line("[5] 🔐 Password Generator", 17)
t.gen_text("", row_num=18)

# Blinking cursor illusion
type_line("> Enter your choice: _", 19)

# Generate GIF
t.gen_gif("assets/pythonprograms.gif")
