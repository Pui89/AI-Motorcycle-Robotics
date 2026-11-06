# Security Policy

## Scope

This repository is an early-stage software research scaffold. It is not connected to a physical motorcycle and must not be used as a vehicle-control system.

## Reporting a vulnerability

Please do not publish exploitable details in a public issue. Use GitHub's private vulnerability reporting feature if it is enabled for this repository. Otherwise contact the repository owner privately through an appropriate GitHub channel.

Include:
- affected file, component, or commit;
- impact and conditions required to reproduce;
- a minimal proof of concept that does not target real vehicles or people;
- suggested mitigation, if known.

Do not include secrets, personal data, or unsafe instructions.

## Security expectations

- Never commit tokens, passwords, private keys, or personal data.
- Review dependencies and licenses before adoption.
- Validate all external and simulated inputs.
- Keep permissions least-privilege and protect the default branch.
- Require review and passing checks before merging when repository settings permit.
- Treat generated/model-produced content as untrusted input.
- No physical vehicle, actuator, or safety-critical hardware testing is in scope.


## Automated verification

This repository currently contains project documentation and GitHub Actions workflow definitions rather than Python application source. The security workflow therefore scans the GitHub Actions workflow language and checks the current repository for common exposed-credential patterns. A successful scan is not hardware validation or proof of vehicle safety.
