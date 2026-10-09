import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = os.getenv("DEFAULT_INPUT", str(BASE_DIR / "data" / "sales_data.csv"))
DEFAULT_OUTPUT = os.getenv("DEFAULT_OUTPUT", str(BASE_DIR / "reports" / "sales_report.pdf"))
REPORT_TITLE = os.getenv("REPORT_TITLE", "Enterprise Sales Report")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
