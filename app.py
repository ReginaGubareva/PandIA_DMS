from flask import Flask
import base_analysis

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

app.add_url_rule('/br/water/consumer_type_description', view_func=base_analysis.br_water_consumer_type_description)
app.add_url_rule('/br/water/zonas_description', view_func=base_analysis.br_water_zone_description)
app.add_url_rule('/br/water/total', view_func=base_analysis.br_water_total_consumption)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


