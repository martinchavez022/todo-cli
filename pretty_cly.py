from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def table_data_tasks(values: tuple) -> None:
    table = Table(title="TASKS", box=box.HORIZONTALS)

    table.add_column("TASKID", justify="center")
    table.add_column("TASK", style="bold royal_blue1")
    table.add_column("COMPLETED", justify="center")
    table.add_column("DATE", justify="center")

    for taskid, title, completed, created_at in values:
        table.add_row(str(taskid), title, str(completed), created_at) 
    console.print(table)

def table_data_habits(values: tuple) -> None:
    print(values)
    table = Table(title="HABITS", box=box.HORIZONTALS)

    table.add_column("HABITID", justify="center")
    table.add_column("HABIT", style="bold royal_blue1")
    table.add_column("DATE", justify="center")

    for habitid, title, created_at in values:
        table.add_row(str(habitid), title, created_at)
    console.print(table)
