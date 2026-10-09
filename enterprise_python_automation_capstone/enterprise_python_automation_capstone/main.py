import argparse, logging
from automation_report.config import DEFAULT_INPUT, DEFAULT_OUTPUT, LOG_LEVEL
from automation_report.scheduler import ReportScheduler
from automation_report.service import generate_report, validate_dataset

def main():
    logging.basicConfig(level=getattr(logging,LOG_LEVEL.upper(),logging.INFO), format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    p=argparse.ArgumentParser(prog="enterprise-report",description="Enterprise automated PDF report generator")
    s=p.add_subparsers(dest="command",required=True)
    g=s.add_parser("generate"); g.add_argument("--input",default=DEFAULT_INPUT); g.add_argument("--output",default=DEFAULT_OUTPUT)
    v=s.add_parser("validate"); v.add_argument("--input",default=DEFAULT_INPUT)
    sc=s.add_parser("schedule"); sc.add_argument("--input",default=DEFAULT_INPUT); sc.add_argument("--output",default=DEFAULT_OUTPUT); sc.add_argument("--interval",type=int,default=60)
    s.add_parser("demo")
    a=p.parse_args()
    if a.command in ("generate","demo"):
        out=generate_report(a.input if a.command=="generate" else DEFAULT_INPUT,a.output if a.command=="generate" else DEFAULT_OUTPUT); print(f"Report generated: {out}")
    elif a.command=="validate":
        r=validate_dataset(a.input); print(f"Dataset valid: {r['valid']} | Records: {r['records']} | Total sales: ₹{r['total_sales']:,.2f}")
    elif a.command=="schedule":
        try: ReportScheduler(lambda: generate_report(a.input,a.output),a.interval).run()
        except KeyboardInterrupt: print("\nScheduler stopped.")
    return 0
if __name__=="__main__": raise SystemExit(main())
