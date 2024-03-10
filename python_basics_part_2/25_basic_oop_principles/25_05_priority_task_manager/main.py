from priority_task_manager import PriorityTaskManager

# Usage example
manager = PriorityTaskManager()

manager.new_task("clean up", 4)
manager.new_task("wash dishes", 4)
manager.new_task("rest", 1)
manager.new_task("eat", 2)
manager.new_task("submit homework", 2)

print(manager)
