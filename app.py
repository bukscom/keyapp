from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    return render_template('index.html')

@app.route('/game',methods=["GET", "POST"])
def game():
    if request.method == "POST":
        keyv=request.form['key']
        team=request.form['teamname']
        
        print(keyv)
        if keyv== '!@#asutcmhack@T':
            
            return redirect("https://www.websudoku.com/")
        else:
            return "<center><h1>Invalid key</h1></center>"
       

    return render_template('index.html')
  


if __name__ == '__main__':
   app.run(debug = False)
