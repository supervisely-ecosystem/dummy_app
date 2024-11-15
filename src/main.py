import os
from dotenv import load_dotenv

import supervisely as sly

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

slider = sly.app.widgets.Slider(value=42, min=0, max=100, step=1)
card = sly.app.widgets.Card("Slider Card", content=slider)
layout = sly.app.widgets.Container(widgets=[card])

app = sly.Application(layout=layout)
