from db.db_manager import add_generated_data_to_db
from db.models import create_models

if __name__ == "__main__":
    create_models()
    add_generated_data_to_db()
