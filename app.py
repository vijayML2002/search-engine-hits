from flask import Flask, request
from flask import render_template
from gui_utils import get_html_data
from gui_utils import keyword_recommendation

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def main_page():
   if request.method == "POST":
      keyword = request.form.get("search_key")
      rank, cosine_value = keyword_recommendation(keyword) 
      title, text, filename = get_html_data(rank)
      return render_template("search_page.html", length = len(title), title = title
               , text = text, file = filename, keyword = keyword, cosine = cosine_value)
   return render_template("search_page.html")

@app.route('/page/<page_name>', methods=["GET", "POST"])
def spage(page_name):
   return render_template(page_name)

if __name__ == '__main__':
   app.run(debug=True)
