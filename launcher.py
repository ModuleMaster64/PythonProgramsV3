import os, subprocess, time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
boot_time = time.time()

def login():
    console.print("[bold yellow]Welcome to PythonProgramsV3 OS[/bold yellow]")
    username = input("Username: ")
    password = input("Password: ")
    if username == "beau" and password == "v3rocks":
        console.print("[green]Access granted.[/green]\n")
        return True
    else:
        console.print("[red]Access denied.[/red]")
        return False

def discover_plugins():
    plugins = {}
    for file in os.listdir("plugins"):
        if file.endswith(".py"):
            name = file[:-3]
            plugins[name] = os.path.join("plugins", file)
    return plugins

def show_banner():
    console.print(Panel(f"🖥️ [bold cyan]PythonProgramsV3 OS[/bold cyan]\nCreated by [bold magenta]ModuleMaster64[/bold magenta]", expand=False))

def show_plugins_table(plugins):
    table = Table(title="Available Plugins")
    table.add_column("Command", style="green")
    table.add_column("Path", style="dim")
    for name, path in plugins.items():
        table.add_row(name, path)
    console.print(table)

def show_diagnostics():
    uptime = time.time() - boot_time
    console.print(f"🧪 Uptime: {int(uptime)} seconds")
    console.print("🧠 CPU Usage: 42% (simulated)")
    console.print("🧬 Memory Usage: 1.2 GB / 8 GB (simulated)")

def shell(plugins):
    while True:
        cmd = input("P3OS> ").strip().lower()
        if cmd == "exit":
            console.print("🛑 Shutting down...")
            break
        elif cmd == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            show_banner()
            show_plugins_table(plugins)
            show_diagnostics()
        elif cmd.startswith("run "):
            key = cmd[4:]
            if key in plugins:
                console.print(f"🚀 Launching {key}.py...\n")
                subprocess.run(["python", plugins[key]])
            else:
                console.print("❌ Unknown module.")
        elif cmd == "help":
            console.print("Commands: run [plugin], clear, exit")
        else:
            console.print("⚠️ Unknown command. Type 'help'.")

if __name__ == "__main__":
    if login():
        show_banner()
        plugins = discover_plugins()
        show_plugins_table(plugins)
        show_diagnostics()
        shell(plugins)
