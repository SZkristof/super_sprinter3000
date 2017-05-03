from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def story():
    return render_template("story.html")


@app.route("/", methods=["POST"])
def story_result():
    story_title = request.form['story_title']
    user_story = request.form['user_story']
    acceptance_criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation_time = request.form['estimation_time']
    with open("result.txt", "rb") as file:
        file.write(str("story_title: " + story_title + ","))
        file.write(str("user_story: " + user_story + ","))
        file.write(str("acceptance_criteria: " + acceptance_criteria + ","))
        file.write(str("business_value: " + business_value + ","))
        file.write(str("estimation_time: " + estimation_time + ","))

if __name__ == "__main__":
    app.run()
