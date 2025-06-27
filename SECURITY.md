# Security Policy

## Supported Versions

| Version | Supported          | Security Fixes Only |
| ------- | ------------------ | ------------------- |
| Main    | ✔️ Current release | ✔️ Always secure    |

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please follow these steps:

1. **Confidential Reporting**

   * Email me directly at **[disaenz2@gmail.com](mailto:disaenz2@gmail.com)** (PGP key available upon request).
   * Please include:
     * A clear description of the vulnerability.
     * Steps to reproduce or a proof-of-concept.
     * Any suggested mitigation or patch code.

2. **Acknowledgement**

   * You will receive an acknowledgement within 48 hours.
   * Public disclosure will occur only after a fix is available, or by mutual agreement.

## Security Practices

* **Dependencies**
  * Regularly updated and checked via `pip-audit`, Dependabot, and Trivy scanning in CI/CD.

* **CI/CD Hardening**
  * Secrets are managed via GitHub Actions Secrets.
  * Infrastructure access is restricted by least-privilege AWS IAM policies.

* **Static & Container Analysis**
  * Trivy scans all Docker images for vulnerabilities.
  * Static code analysis (CodeQL, etc.) is integrated with the pipeline.

## Disclosures and Credits

* Security research and contributions are credited in the repository’s **SECURITY** section of any releases.
* Thank you to all security researchers who help keep this project safe.