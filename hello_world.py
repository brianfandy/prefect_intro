from prefect import flow


@task
def create_message():
    msg = ""


@flow
def hello_world():
    print("hello from prefect")


hello_world()