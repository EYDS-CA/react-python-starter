import unittest
from flask.cli import FlaskGroup
from app import create_app, db
# from app.api.models import MODEL_NAME

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def create_db():
    db.create_all()
    db.session.commit()

# When data need to be seeded this is what we should use
@cli.command()
def seed_db():
    # db.session.add(MODEL_NAME(field_name='data to be seeded'))
    db.session.commit()


@cli.command()
def test():
    # Runs the tests without code coverage
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
