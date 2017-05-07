from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def story():
    return render_template("new_story.html")


@app.route("/", methods=["POST"])
def story_result():
    story_title = request.form['story_title']
    user_story = request.form['user_story']
    acceptance_criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation_time = request.form['estimation_time']
    selected = request.form['selected']

    with open("result.txt", "a") as file:
        file.write(str(story_title + "\t"))
        file.write(str(user_story + "\t"))
        file.write(str(acceptance_criteria + "\t"))
        file.write(str(business_value + "\t"))
        file.write(str(estimation_time + "\t"))
        file.write(str(selected + "\n"))
    return render_template("new_story.html")


@app.route("/stats", methods=["POST", "GET"])
def statistics():
    with open("result.txt", "r") as file:
        result_list = file.read().splitlines()
        result_list = [item.split('\t') for item in result_list]
        lengths = len(result_list)

    return render_template("stats.html", result_list=result_list, lengths=lengths)


if __name__ == "__main__":
    app.run()
