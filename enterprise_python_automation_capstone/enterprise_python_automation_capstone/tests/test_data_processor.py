import pytest
from automation_report.data_processor import Sale, load_sales, calculate_metrics
def test_total(): assert Sale("x","A","X",2,10).total==20
def test_load(): assert len(load_sales("data/sales_data.csv"))==15
def test_metrics():
    r=calculate_metrics([Sale("x","A","X",2,10),Sale("x","B","Y",1,30)])
    assert r["total_sales"]==50 and r["top_product"]=="B"
def test_missing():
    with pytest.raises(FileNotFoundError): load_sales("missing.csv")
def test_bad_header(tmp_path):
    p=tmp_path/"bad.csv"; p.write_text("date,product\n2026,A\n")
    with pytest.raises(ValueError): load_sales(p)
