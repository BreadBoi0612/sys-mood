from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn


def stat_bar(label, value, color):
    progress = Progress(
        TextColumn(f"[bold]{label}"),
        BarColumn(bar_width=25),
        TextColumn(f"{value:>5.1f}%"),
        expand=True
    )
    progress.add_task("", total=100, completed=value)

    return Panel(progress, border_style=color)


def network_panel(up, down):
    text = (
        f"[green]⬆ Upload[/green]: {up}\n"
        f"[cyan]⬇ Download[/cyan]: {down}"
    )
    return Panel(text, title="Network", border_style="magenta")
