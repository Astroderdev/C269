from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def load_html():
    print("HTML Pages Loaded!")
    return render_template('home.html')

if __name__ == '__main__':
    app.run()



