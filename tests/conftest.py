import csv
import json

import pytest
from reportlab.pdfgen.canvas import Canvas


@pytest.fixture(scope='session')
def get_json_content():
    with open('../data/data.json') as json_content:
        content = json.load(json_content)['clients']

    yield content


@pytest.fixture(scope='session', autouse=True)
def create_pdf(get_json_content):
    canvas = Canvas("../data/test_files/content.pdf")
    strings_to_write = map(str, get_json_content)
    new_line_offset = 800
    for entry in strings_to_write:
        canvas.drawString(x=30, y=new_line_offset, text=entry)
        new_line_offset -= 20
    canvas.drawImage('../data/image.jpg', 100, 500, width=200, height=200)
    canvas.save()


@pytest.fixture(scope='session', autouse=True)
def create_csv(get_json_content):
    with open('../data/test_files/content.csv', 'w') as csvfile:
        fieldnames = ['name', 'orders', 'distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(get_json_content)
