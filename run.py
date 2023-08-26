import os
import json
from flask import Flask,render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    """Creates route and view for index"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Creates route and view for about"""
    
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)

    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    """Creates route and view for each member of thorin company"""
    member = {}
    with open("data/company.json","r") as json_data:
            data = json.load(json_data)
            for obj in data:
                if obj["url"] == member_name:
                    member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods = ["GET", "POST"])
def contact():
    """Creates route and view for contact"""
    if request.method == "POST":
        # print(request.form.get("name")) #request.form is dictionary
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")
        ))
    return render_template("contact.html", page_title="Contact") #render tamplate 


@app.route("/careers")
def careers():
    """Creates route and view for careers"""
    return render_template("careers.html", page_title="Careers") #render tamplate 



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True) # True only for testing and dev, for production set it to False