# Architecture

```text
CLI (argparse)
      |
      v
Service Layer
   /       \
  v         v
CSV/Data   PDF Generator
Processor      |
  |            v
  +-------> reports/*.pdf

Scheduler -> Service Layer
Config + Logging cross-cut all components
```

The application separates CLI, business processing, PDF generation, scheduling, and configuration. It can later be extended with APIs, cloud storage, email notifications, Docker, CI/CD, or an enterprise scheduler.
