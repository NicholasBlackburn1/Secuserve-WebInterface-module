import app
import time





def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            app.turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))

