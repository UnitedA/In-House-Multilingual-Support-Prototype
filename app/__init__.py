from flask import Flask

def create_app():
    """
    Create and configure an instance of the Flask application.
    
    This function sets up the Flask application by initializing an instance of Flask,
    registering the main blueprint for routing, and returning the configured app.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)  # Initialize a new Flask application instance
    
    from .routes import main  # Import the 'main' blueprint from the 'routes' module
    app.register_blueprint(main)  # Register the 'main' blueprint with the Flask application
    
    return app  # Return the configured Flask application instance
