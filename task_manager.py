from database import get_connection


class TaskManager:

    def add_task(self, title):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )

        conn.commit()
        conn.close()

    def view_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, title, completed FROM tasks"
        )

        tasks = cursor.fetchall()

        conn.close()

        if not tasks:
            print("No tasks found.")
            return

        for task_id, title, completed in tasks:
            status = " [DONE]" if completed else ""

            print(f"{task_id} - {title}{status}")

    def complete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET completed = 1
            WHERE id = ?
            """,
            (task_id,)
        )

        conn.commit()
        conn.close()

    def delete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()
        conn.close()