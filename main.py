from typing import Union

from fastapi import FastAPI
from dataapi import translate_text

app = FastAPI()


@app.get("/uz_en/{text}")
def uz_en(text):
    translate = translate_text(text)

    return {"translated_text": translate}
