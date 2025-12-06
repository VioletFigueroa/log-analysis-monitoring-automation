# Log Monitoring Workflow

![GitHub last commit](https://img.shields.io/github/last-commit/VioletFigueroa/log-analysis-monitoring-automation?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/VioletFigueroa/log-analysis-monitoring-automation?style=flat-square)
![License](https://img.shields.io/badge/license-Educational-blue?style=flat-square)

**Quick Links:** [Documentation](README.md) | [Security Policy](SECURITY.md) | [Contributing](CONTRIBUTING.md)

---

**How to view artifacts:** Open `Log Monitoring Workflow.pdf` for the formatted report or `Log Monitoring Workflow.md` for quick skim; code lives in `Log Monitoring Workflow.py` and `bashscript.sh`.

**Result snapshot:** Automated log collection + regex alerting reduced manual triage and produced weekly summaries for leadership.

**Quick review:**
- Docs: `Log Monitoring Workflow.pdf` → formatted findings
- Evidence/code: `Log Monitoring Workflow.py`, `bashscript.sh`
- Start with: `Log Monitoring Workflow.md` → flow overview and alert logic

## Overview
Automated log monitoring and analysis workflow combining Bash scripting and Python. This project demonstrates systematic approaches to log collection, parsing, analysis, and alerting for security monitoring and compliance purposes.

![Log monitoring workflow dashboard](./image1.png)

**Data handling:** Demo logs are synthetic/redacted; no production credentials or PII are stored in this repo.

## Objectives
- Develop automated log collection and aggregation
- Create log parsing and analysis pipelines
- Implement real-time alerting for security events
- Generate compliance and audit reports
- Enable rapid incident investigation capabilities

## Methodology
- Centralized log collection and storage
- Log parsing and normalization
- Event correlation and pattern detection
- Alert rule development and tuning
- Automated report generation
- Integration with security monitoring systems

## Key Findings
- Effective log processing techniques
- Common security event patterns
- Alert tuning and false positive reduction
- Log retention and compliance requirements
- Performance optimization for large-scale deployments

## Technologies Used
- Bash scripting - Log processing automation
- Python - Advanced parsing and analysis
- Regular expressions - Log pattern matching
- Text processing tools (grep, awk, sed)
- Systemd/cron - Job scheduling
- Log aggregation principles
- SIEM concepts and practices

## Lessons Learned
- Regex tuning and log normalization cut false positives; lightweight alerts stayed actionable.
- Clear separation of collection, parsing, and alerting made the workflow easy to extend to new log types.

## Files Included
- [Log Monitoring Workflow.md](Log%20Monitoring%20Workflow.md) - Workflow documentation in Markdown format
- [Log Monitoring Workflow.pdf](Log%20Monitoring%20Workflow.pdf) - Formatted report in PDF for printing and sharing
- [Log Monitoring Workflow.py](Log%20Monitoring%20Workflow.py) - Python implementation for log analysis and automation
- [bashscript.sh](bashscript.sh) - Bash automation scripts for log processing
- [log-monitoring-workflow.md](log-monitoring-workflow.md) - Extended documentation and implementation details
