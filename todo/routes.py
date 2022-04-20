from todo import app, render_template, request, redirect, url_for
from todo.models import TodoModel, db


@app.route('/')
def home_page():

    todo_list = TodoModel.query.all()
    completed_list = TodoModel.query.filter_by(is_completed=True)
    not_completed_list = TodoModel.query.filter_by(is_completed=False)
    return render_template('base.html',
                           todo_list=todo_list,
                           completed_list=completed_list,
                           not_completed_list=not_completed_list)


@app.route('/add', methods=['POST'])
def add():
    # add new item
    title = request.form.get("title")
    desc = request.form.get("desc")
    category = request.form.get("category")
    new_todo = TodoModel(title=title, category=category, desc=desc, is_completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home_page"))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    # update item
    task = TodoModel.query.filter_by(id=todo_id).first()
    task.is_completed = not task.is_completed
    db.session.commit()
    return redirect(url_for("home_page"))

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    #edit item
    task  = TodoModel.query.filter_by(id=todo_id).first()
    return render_template('base.html')


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # delete item
    task = TodoModel.query.filter_by(id=todo_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home_page"))
