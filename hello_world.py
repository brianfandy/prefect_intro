from prefect import flow, task


@task
def create_message():
    msg = "Hello from Task"
    return(msg)


@flow
def hello_world():
    task_message = create_message()
    print(task_message)


hello_world()