import logging, sched, time
logger = logging.getLogger(__name__)
class ReportScheduler:
    def __init__(self, task, interval_seconds):
        if interval_seconds < 1: raise ValueError("interval_seconds must be at least 1")
        self.task, self.interval, self.scheduler, self.running = task, interval_seconds, sched.scheduler(time.time,time.sleep), False
    def _run_once(self):
        if not self.running: return
        try: self.task()
        except Exception: logger.exception("Scheduled report execution failed")
        self.scheduler.enter(self.interval, 1, self._run_once)
    def run(self):
        self.running=True; self.scheduler.enter(0,1,self._run_once); self.scheduler.run()
    def stop(self): self.running=False
