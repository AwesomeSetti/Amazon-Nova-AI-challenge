"""
CWE-915: Mass Assignment Vulnerability

Updating all object attributes from unfiltered user input may allow attackers to override protected fields.
"""

@app.route("/create_account", methods=["POST"])
def create_account():
    account = Account(default_role="user")
    account.__dict__.update(request.form.to_dict())  # CWE-915
    db.save(account)
    return "Account created", 201
