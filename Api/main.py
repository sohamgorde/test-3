from fastapi import FastApi

app = fastapi(
    title = "fast api example"
    description = "this is an example of using fast api"
)

@app.get('/')

def default_route():
    return "you have reached the default route back end sever is lisening "

    @app.get ("/example")
    def get_example():