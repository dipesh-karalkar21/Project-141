from flask import Flask, jsonify
import csv

all_articles = []
liked = []
not_liked = []

with open("articles.csv",encoding = "utf-8") as f:
    csvr = csv.reader(f)
    data = list(csvr)
    all_articles.append(data[1:])

app = Flask(__name__)

@app.route("/")
def getM():
    return jsonify({
        "Data" : all_articles[0],
        "status" : "success"
    }),201

@app.route("/liked",methods = ["POST"])
def getL():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked.append(movie)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/dliked",methods = ["POST"])
def getD():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    not_liked.append(movie)
    return jsonify({
        "status" : "success"
    }),201

app.run(debug = True)