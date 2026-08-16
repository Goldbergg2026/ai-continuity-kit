# Security Policy

AI Continuity Kit is a documentation/template project. It should never contain real credentials or private user data.

## Never commit

- passwords;
- API/OAuth/Telegram tokens;
- private keys;
- cookies or session state;
- real `.env` files;
- secret-bearing configuration or backups;
- personal datasets that are not intentionally public.

Use placeholders such as `YOUR_TOKEN_HERE` only when an example needs to show structure.

## Personal deployments

Use a **private repository** for your real continuity data. Git history is durable: deleting a secret from the latest commit does not erase it from earlier history.

If a secret is committed accidentally:

1. revoke/rotate the secret first;
2. remove it from the repository/history as appropriate;
3. verify that dependent systems use the replacement;
4. document only a safe pointer or variable name, never the secret value.

## Reporting

If you find a security issue in this public template, open a GitHub issue only when doing so does not expose a secret or private data. Do not paste credentials into an issue.
