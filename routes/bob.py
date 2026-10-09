def register(app):

    @app.route("/bob")
    def bob():
        return "Hello from Bob"