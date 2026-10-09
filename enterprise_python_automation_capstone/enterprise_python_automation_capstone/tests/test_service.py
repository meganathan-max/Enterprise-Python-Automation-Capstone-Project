from automation_report.service import validate_dataset, generate_report
def test_validate():
    r=validate_dataset("data/sales_data.csv"); assert r["valid"] and r["records"]==15
def test_pdf(tmp_path):
    p=tmp_path/"report.pdf"; generate_report("data/sales_data.csv",p); assert p.exists() and p.stat().st_size>1000
