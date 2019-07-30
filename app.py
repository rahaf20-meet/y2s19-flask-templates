from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    # return "mlookhieh"
	food_fav = ["mlookhieh","upside down","pizza"]
	food_no = ["olives", "beans", "liver"]
	return render_template("index.html" ,food_fav=food_fav, food_no=food_no, opposite_day=opposite_day)

opposite_day = False;
if __name__ == '__main__':
   app.run(debug = True)
