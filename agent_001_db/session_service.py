from google.adk.sessions import DatabaseSessionService

db_url = "postgresql://postgres:password@localhost/postgres"
session_service = DatabaseSessionService(db_url=db_url)