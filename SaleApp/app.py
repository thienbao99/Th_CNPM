
from flask import Flask, render_template, request
import  dao
app = Flask(__name__)

@app.route("/")
def home():
    q = request.args.get("q")
    cates = dao.load_categories()
    cate_id = request.args.get("cate_id")
    return render_template("index.html", cates=cates, prods=dao.load_products(q=q, cate_id=cate_id))

@app.route("/product/<int:id>")
def details(id):
    return render_template("prod_detail.html", prod=dao.get_product_by_id(id))

if __name__ == "__main__":
    app.run(debug=True)
