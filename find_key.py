import dotenv
import os

project_dir = os.path.dirname(os.path.realpath(__file__))
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)
api_key = os.getenv("API_KEY")


print("This program is not ready yet")