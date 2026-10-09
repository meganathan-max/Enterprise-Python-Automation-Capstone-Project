from datetime import datetime
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from .config import REPORT_TITLE

def money(v): return f"₹{v:,.2f}"

def generate_pdf(sales, metrics, output_path, title=REPORT_TITLE):
    output = Path(output_path); output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=15*mm, bottomMargin=15*mm)
    styles = getSampleStyleSheet(); story = [Paragraph(title, styles["Title"]), Paragraph(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}", styles["Normal"]), Spacer(1,8)]
    rows = [["Metric","Value"],["Total records",str(metrics["record_count"])],["Total sales",money(metrics["total_sales"])],["Average transaction",money(metrics["average_transaction"])],["Total quantity",str(metrics["total_quantity"])],["Top product",metrics["top_product"]],["Top category",metrics["top_category"]]]
    story.append(Table(rows, colWidths=[75*mm,90*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1f2937")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.grey),("PADDING",(0,0),(-1,-1),6)])))
    story.append(Spacer(1,12))
    for heading, key in [("Sales by Category","sales_by_category"),("Sales by Product","sales_by_product")]:
        story.append(Paragraph(heading, styles["Heading2"]))
        data = [[heading.replace("Sales by ",""),"Sales"]] + [[k,money(v)] for k,v in metrics[key].items()]
        story.append(Table(data, colWidths=[90*mm,75*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#374151")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.grey),("PADDING",(0,0),(-1,-1),5)])))
        story.append(Spacer(1,12))
    story.append(Paragraph("Recent Transactions", styles["Heading2"]))
    recent = [["Date","Product","Qty","Total"]] + [[s.date,s.product,str(s.quantity),money(s.total)] for s in sales[-8:]]
    story.append(Table(recent, colWidths=[35*mm,70*mm,25*mm,45*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#374151")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.grey),("PADDING",(0,0),(-1,-1),5)])))
    doc.build(story); return output
