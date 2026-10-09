def register(app):

    @app.route("/alice")
    def alice():
        return "Hello from Alice"