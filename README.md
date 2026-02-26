### Personal 'to do' CLI app

#### **instalation**

1. install uv

```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. clone the repo
```console
https://github.com/martinchavez022/todo-cli.git
```

3. run he install script
```console
./install.sh
```

#### **use**

- help general information
```console
todo --help
```

- to show the task of the day
```console
todo show
```

- to show all the task
```console
todo show-all
```

- to show all the task already done
```console
todo show-completed
```

- to show are not done yet
```console
todo show-left
```

- to add a new task
```console
todo add --title "description of the task"
```
> This task was only avaible in the day to the command `todo show`

- to deactivate a task and not show
```console
todo delete --taskid {id of the task}
```

-- to mark as complete a task
```console
todo completed --taskid {id of the task}
```
