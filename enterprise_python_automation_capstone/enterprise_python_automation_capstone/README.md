# Enterprise Python Automation Capstone

## Automated PDF Report Generator

Production-style Python automation application that reads sales CSV data, processes business metrics, generates a PDF report, supports recurring scheduling, and provides a clean CLI.

### Features
- End-to-end CSV -> processing -> PDF workflow
- CLI with argparse
- Scheduling with Python standard-library `sched`
- ReportLab PDF generation
- Validation and error handling
- Logging and environment configuration
- pytest tests
- `pyproject.toml` packaging
- Architecture documentation

### Structure
```text
enterprise_python_automation_capstone/
├── automation_report/
│   ├── __init__.py
│   ├── config.py
│   ├── data_processor.py
│   ├── pdf_generator.py
│   ├── scheduler.py
│   └── service.py
├── data/sales_data.csv
├── reports/
├── tests/
├── docs/architecture.md
├── main.py
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Install
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Run
```bash
python main.py generate
python main.py generate --input data/sales_data.csv --output reports/sales_report.pdf
python main.py validate
python main.py demo
python main.py schedule --interval 60
```

After `pip install -e .`, the CLI is also available as:
```bash
enterprise-report generate
```

### Test
```bash
pytest -q
```

### Report contents
The generated PDF includes total records, total sales, average transaction value, total quantity, top product/category, category and product sales tables, and recent transactions.

### Expected proof
Submit the GitHub repository plus a generated PDF and terminal execution log/video walkthrough. The project includes README usage instructions and an architecture diagram.
