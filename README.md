The thing to store configs and run tests

# Human Centered Security and Evidence Management

Two overlapping goals:
1. Use plain english to ask questions about the site
   - Questions can then be mapped to NIST 800-53 controls
2. Automate evidence collection everywhere possible
   - Tag evidence with applicable control(s)

## Baseline
- Is SITE up?
- Does SITE enforce HTTPS?
   - Is SITE HSTS compliant?
- Are there any non-encrypted data flows? (SC-08(01) narrative)
- Does SITE build from infrastructure as code? (IaC, e.g. CloudFormation)
   - CM-02(02) Baseline configuration automation
- Is SITE on cloud.gov?
   - Inherit many controls

## ICAM (AC & IA families)
- Rolodex (user name, work email pulled from Login.gov authentication)
- Are all users Privileged? (from System Description)
- Is all authentication done via login.gov? (from System Description)
- Must privileged users employ phishing resistant MFA? (Policy)
- Must privileged users be identity proofed? (Policy)
- Are privileged users regularly audited? (Demonstrate how)
   - Can user privileges/accounts be removed/disabled quickly?
- Are privileged user operations logged?

## Per Custom Buildpack:
- How are security vulnerabilities discovered? (RA-05 Vulnerability monitoring)
- How are security updates applied? (SI-11 Flaw remediation)
