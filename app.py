from flask import (Flask, g, render_template,
                   flash, redirect, url_for, request, abort)

import models
import forms

DEBUG = True
PORT = 8000
HOST = '127.0.0.1'

app = Flask(__name__)
app.secret_key = 'SHDKfjfknfjdjbuee89ksjnklanodeh2h@&*%$E$$T%TWFDSfreknf38'

@app.before_request
def before_request():
    """connect to database before each request"""
    g.db = models.DATABASE


@app.after_request
def after_request(response):
    """close database after each request"""
    g.db.close()
    return response


@app.route("/")
@app.route("/entries")
def index():
    posts = models.Post.select()
    return render_template("index.html", posts=posts)


@app.route("/entries/new", methods=("GET", "POST"))
def new():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(
            title=form.title.data,
            date=form.date.data,
            time_spent=form.time_spent.data,
            learned=form.learned.data,
            resources=form.resources.data
        ).save()
        flash("Post saved successfully!", "success")
        return redirect(url_for("index"))
    return render_template("new.html", form=form)


@app.route("/entries/<int:post_id>")
def detail(post_id):
    posts = models.Post.select().where(models.Post.post_id == post_id)
    return render_template("detail.html", posts=posts)


@app.route("/entries/<int:post_id>/edit", methods=("GET", "POST"))
def edit(post_id):
    post = models.Post.get(models.Post.post_id == post_id)
    posts = models.Post.select().where(models.Post.post_id == post_id)
    form = forms.PostForm()
    if request.method == 'GET':
        form.title.data = post.title
        form.date.data = post.date
        form.time_spent.data = post.time_spent
        form.learned.data = post.learned
        form.resources.data = post.resources
    if form.validate_on_submit():
        post.title = form.title.data
        post.date = form.date.data
        post.time_spent = form.time_spent.data
        post.learned = form.learned.data
        post.resources = form.resources.data
        post.save()
        flash("Post Updated!", "success")
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, post_id=post_id, posts=posts)


@app.route("/entries/<int:post_id>/delete", methods=["GET", "DELETE"])
def delete(post_id):
    models.Post.delete().where(models.Post.post_id == post_id).execute()
    return redirect(url_for("index"))


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
