import os
from app import create_app, db
from app.models import User, Post, Comment

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    """Automatically import models in flask shell."""
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}


@app.cli.command()
def test():
    """Run unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
