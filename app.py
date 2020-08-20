
from flask import Flask,jsonify,render_template
from boom.boom import load,calc_stats

app = Flask(__name__)


@app.route('/')
def hello():
    test_domain = 'http://behamrah.ir'
    res = load(test_domain, 100, 10, 0, 'GET', None, 'text/plain', None,quiet=True)
    data =calc_stats(res)
    return render_template('index.html',data=data)


@app.route('/<url>/<count>')
def boom(url,count):
    domain  =  "http://{}".format(url)
    print('domain:::::::::',domain)
    test_domain = 'https://google.com'
    res = load(domain, int(count), 10, 0, 'GET', None, 'text/plain', None,quiet=True)
    data =calc_stats(res)

    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run()