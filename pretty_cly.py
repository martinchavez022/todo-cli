from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def table_data(values: tuple) -> None:
    table = Table(title="TASKS", box=box.HORIZONTALS)

    table.add_column("TASKID", justify="center")
    table.add_column("TASK", style="bold royal_blue1")
    table.add_column("COMPLETED", justify="center")
    table.add_column("DATE", justify="center")

    for taskid, title, completed, created_at in values:
        table.add_row(str(taskid), title, str(completed), created_at) 
    console.print(table)

