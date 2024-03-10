from stack import Stack


class PriorityTaskManager:
    """
    Manages tasks with priorities using a stack data structure.

    Attributes:
        tasks (Stack): The stack to store tasks with priorities.
    """

    def __init__(self) -> None:
        """Initializes the task manager using a stack."""
        self.tasks = Stack()

    def new_task(self, task: str, priority: int) -> None:
        """
        Adds a new task with the specified priority.

        Args:
            task (str): The task description.
            priority (int): The priority of the task.
        """
        self.tasks.push((priority, task))

    def remove_task(self) -> tuple:
        """
        Removes the task from the top of the stack.

        Returns:
            The task and its priority as a tuple, or None if the stack is empty.
        """
        return self.tasks.pop()

    def __str__(self) -> str:
        """
        Returns a string representation of tasks sorted by priority.

        Returns:
            A string representation of the sorted tasks.
        """

        def priority_key(task: tuple) -> int:
            return task[0]

        sorted_tasks = sorted(self.tasks.items, key=priority_key)

        task_str = ""
        current_priority = None
        for task_item in sorted_tasks:
            if task_item[0] != current_priority:
                if current_priority is not None:
                    task_str = task_str.strip('; ') + '\n'
                current_priority = task_item[0]
                task_str += f"{current_priority} — "

            task_str += task_item[1] + "; "

        return task_str.strip('; ')
