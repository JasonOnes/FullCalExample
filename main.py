from flask import Flask
from flask import request, render_template, jsonify, redirect
import json

app = Flask(__name__)

# can't leave comments in json for more event properties https://fullcalendar.io/docs/event_data/Event_Object/

@app.route('/')
def calendar():
    return render_template('json.html')


@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
   
    with open("events.json", "r") as input_data:
        #Is this where events get populated? It seems so
        return input_data.read()

@app.route('/lasagna', methods=['POST', 'GET'])
def show_las():
    if request.method == 'GET':
        return render_template('lasagna.html')
    else:
        if request.form['choice'] == "change":
            return render_template('change.html')
        elif request.form['choice'] == "delete":
            #TODO figure out how to delete event from json data
            # something like below perhaps
            '''
            with open("events.json", "w") as input_data:
                input_data.flush(title='lasagna')
            '''
            # javascript (?)
            # .fullCalendar( 'removeEvents' [, idOrFilter ] ) from https://fullcalendar.io/docs/event_data/removeEvents/
            return redirect('/')
        elif request.form['choice'] == "recipe":
            return render_template('recipe.html')


if __name__ == '__main__':
    app.debug = True
    app.run()