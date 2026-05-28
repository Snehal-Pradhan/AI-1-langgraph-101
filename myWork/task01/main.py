import sys
from pathlib import Path
import warnings

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model

warnings.filterwarnings('ignore', message='LangSmith now uses UUID v7')

#response = model.invoke("What is LangChain?")
#response.pretty_print()
