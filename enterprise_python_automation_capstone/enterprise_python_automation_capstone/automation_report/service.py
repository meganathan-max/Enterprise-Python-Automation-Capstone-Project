import logging
from .data_processor import load_sales, calculate_metrics
from .pdf_generator import generate_pdf
logger = logging.getLogger(__name__)
def generate_report(input_path, output_path):
    logger.info("Loading %s", input_path); sales = load_sales(input_path)
    metrics = calculate_metrics(sales); logger.info("Processing %d records", len(sales))
    result = generate_pdf(sales, metrics, output_path); logger.info("Report generated: %s", result); return result
def validate_dataset(input_path):
    sales = load_sales(input_path); metrics = calculate_metrics(sales)
    return {"valid": True, "records": len(sales), "total_sales": metrics["total_sales"]}
