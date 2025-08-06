# 🛡️ Amazon Nova AI Challenge – Uncommon Python CWE Attacks

This repository contains a curated set of **lesser-known but dangerous CWE vulnerabilities**, implemented in Python. These examples were developed as part of the Amazon **Nova AI Trust Challenge** to demonstrate adversarial strategies and help improve AI safety, red teaming, and prompt defense mechanisms.

Each script targets a specific security vulnerability and includes real-world patterns such as SSRF, XML external entities, insecure deserialization, mass assignment, logging leaks, and more.

---

## 📁 Folder Structure

```
Amazon-Nova-AI-challenge/
├── attacks/              # Python scripts simulating each CWE-based attack
├── attack_metadata/      # Machine-readable JSON metadata
├── LICENSE               # Open-source license for usage
└── README.md             # This file
```

---

## 🔍 CWE Vulnerabilities Covered

| CWE ID | Title |
|--------|------------------------------------------------------------|
| CWE-22 | Path Traversal |
| CWE-59 | Link Following (Symlink Race) |
| CWE-94 | Code Injection via `eval` / `exec` |
| CWE-117 | Log Forging / Injection |
| CWE-256 | Plaintext Password Storage |
| CWE-295 | Improper Certificate Validation |
| CWE-330 | Predictable Random Values |
| CWE-377 | Insecure Temporary Files |
| CWE-502 | Insecure Deserialization of Pickle |
| CWE-532 | Logging Sensitive Info |
| CWE-611 | XML External Entities (XXE) |
| CWE-915 | Mass Assignment (Object Injection) |
| CWE-918 | Server-Side Request Forgery (SSRF) |
| CWE-1333 | Inefficient Regular Expressions (ReDoS) |
| CWE-489 | Active Debug Code (e.g., `debug=True`) |

---

## 🧪 Example: CWE-915 – Mass Assignment

```python
@app.route("/create_account", methods=["POST"])
def create_account():
    account = Account(default_role="user")
    account.__dict__.update(request.form.to_dict())  # ⚠️ CWE-915
    db.save(account)
```

This pattern allows attackers to inject unauthorized fields such as `is_admin` or `role` via form fields.

---

## 📚 Resources

- [CWE Database – MITRE](https://cwe.mitre.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Amazon Nova AI Challenge](https://github.com/aws/nova-ai-challenge)

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.  
Do not use these scripts in unauthorized environments or against real systems.

---

## 👩‍💻 Author

**Soroush Setayeshpour**  
Team ASTRO – Amazon Nova AI Trust Challenge 2025  
GitHub: [@AwesomeSetti](https://github.com/AwesomeSetti)

