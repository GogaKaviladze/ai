from app.db.session import engine
from sqlmodel import Session
from app import models
from app.core.security import get_password_hash


def init() -> None:
    models.SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if not session.exec(models.select(models.User)).first():
            admin = models.User(email="admin@hansabit.de", hashed_password=get_password_hash("ChangeMe!123"), is_superuser=True)
            session.add(admin)
        if not session.exec(models.select(models.Case)).first():
            cases = [
                models.Case(title="Automatisierung", description="Workflow Digitalisierung"),
                models.Case(title="Webplattform", description="Moderne Web App"),
                models.Case(title="Integration", description="API Anbindung"),
            ]
            session.add_all(cases)
        session.commit()


if __name__ == "__main__":
    init()
