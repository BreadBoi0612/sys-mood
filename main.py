import time
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel

from monitor.stats import get_cpu, get_ram, get_disk
from monitor.mood import get_mood
from monitor.network import NetworkMonitor, format_speed
from monitor.ui import stat_bar, network_panel


layout = Layout()

layout.split_column(
    Layout(name="header", size=3),
    Layout(name="body")
)

layout["body"].split_row(
    Layout(name="cpu"),
    Layout(name="ram"),
    Layout(name="disk"),
    Layout(name="net", size=30),
)

netmon = NetworkMonitor()

with Live(layout, refresh_per_second=2, screen=True):
    while True:
        cpu = get_cpu()
        ram = get_ram()
        disk = get_disk()

        emoji, mood = get_mood(cpu, ram)

        up, down = netmon.get_speed()

        layout["header"].update(
            Panel(
                f"{emoji}  System Mood: [bold]{mood}[/bold]",
                border_style="cyan"
            )
        )

        layout["cpu"].update(stat_bar("CPU", cpu, "red"))
        layout["ram"].update(stat_bar("RAM", ram, "blue"))
        layout["disk"].update(stat_bar("DISK", disk, "green"))
        layout["net"].update(
            network_panel(
                format_speed(up),
                format_speed(down)
            )
        )

        time.sleep(1)
