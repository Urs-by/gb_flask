from fastapi import FastAPI, Request, Form
from models import Phonebook
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

phonebook_db: list[Phonebook] = [Phonebook(surname='Хой', name='Иван', base_phone_number=9754545454545, additional_phone_number=0),
                                  Phonebook(surname='КУЦ', name='Artur', base_phone_number=9754554545, additional_phone_number=123)]



@app.get("/", response_class=HTMLResponse)
@app.get('/index', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request})


# @app.get("/read", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse("/read.html", {"phonebook_db": phonebook_db,"request": request})


@app.get('/add', response_class=HTMLResponse)
async def add_item(request: Request):
    return templates.TemplateResponse("/add.html", {"request": request})


#
#
@app.post('/add', response_class=HTMLResponse)
async def create_record(record: Phonebook, request: Request):
    phonebook_db.append(record)

    return templates.TemplateResponse("/add.html", {"request": request, "phonebook": phonebook_db})
#
#
@app.get('/update', response_class=HTMLResponse)
async def add_item(request: Request):
    return templates.TemplateResponse("/update.html", {"request": request})


#
#
# @app.put('/update/{phone_number}')
# async def update_record(phone_number: int, record: Phonebook):
#     for i in phonebook:
#         if i.base_phone_number == phone_number or i.additional_phone_number == phone_number:
#             i.surname = record.surname
#             i.name = record.name
#             i.base_phone_number = record.base_phone_number
#             i.additional_phone_number = record.additional_phone_number
#         else:
#             return f'Запись с номером {phone_number} не существует'
#     return phonebook
#
#
@app.get('/delete', response_class=HTMLResponse)
async def add_item(request: Request):
    return templates.TemplateResponse("/delete.html", {"request": request})

#
# @app.delete('/delete')
# async def delete_record(phone_number: int):
#     for i in phonebook:
#         if i.base_phone_number == phone_number or i.additional_phone_number == phone_number:
#             phonebook.remove(i)
#             return phonebook
#     return f'Запись с номером {phone_number} не существует'
