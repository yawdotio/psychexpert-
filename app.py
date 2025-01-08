from flask import Flask, request, render_template
from inference import MoodStressFact, MoodStressEngine

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mood_stress():
    if request.method == 'POST':
        mood = request.form['mood']
        sleep = int(request.form['sleep'])
        activity = int(request.form['activity'])
        major_event = request.form['major_event'] == 'yes'

        # print inputs for debugging
        print(f'Mood: {mood}, Sleep: {sleep}, Activity: {activity}, Major Event: {major_event}')
        
        # Run the engine
        engine = MoodStressEngine()
        engine.reset()
        engine.declare(MoodStressFact(mood=mood, sleep=sleep, activity=activity, major_event=major_event))
        engine.run()

        # Collect Results
        results = {fact['stress']: fact['mood_state'] for fact in engine.facts.values() if 'stress' in fact}
        print(engine.facts.values())
        return render_template('results.html', results=results)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)