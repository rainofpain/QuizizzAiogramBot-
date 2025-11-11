import aiogram.fsm.state as state
import aiogram.fsm.context as context
import aiogram.types as types
import json

from config import dispatcher
from keyboards import yes_or_no_keyboard

test2 = json.load(open("static/json/test_2.json"))    

class Test2(state.StatesGroup):
    question_1 = state.State()
    question_2 = state.State()
    question_3 = state.State()  
    question_4 = state.State()
    question_5 = state.State()

@dispatcher.message(Test2.question_1)
async def test2_question_1_state(message: types.Message, state: context.FSMContext):
    await state.update_data(question_1 = message.text)
    for value in test2["questions"]["2"].keys():
        if value == "text":
            await message.answer(text = f"Питання 2: ")
            await message.answer(text = f"{test2["questions"]["2"][f"{value}"]}")
        if value == "answers":
            for answer in test2["questions"]["2"][f"{value}"]:
                await message.answer(text = f"{answer}")
    await message.answer(text = "Введіть вашу відповідь: ")
    await state.set_state(Test2.question_2)
    
@dispatcher.message(Test2.question_2)
async def test2_question_2_state(message: types.Message, state: context.FSMContext):
    await state.update_data(question_2 = message.text)
    for value in test2["questions"]["3"].keys():
        if value == "text":
            await message.answer(text = f"Питання 3: ")
            await message.answer(text = f"{test2["questions"]["3"][f"{value}"]}")
        if value == "answers":
            for answer in test2["questions"]["3"][f"{value}"]:
                await message.answer(text = f"{answer}")
    await message.answer(text = "Введіть вашу відповідь: ")
    await state.set_state(Test2.question_3)

@dispatcher.message(Test2.question_3)
async def test2_question_3_state(message: types.Message, state: context.FSMContext):
    await state.update_data(question_3 = message.text)
    for value in test2["questions"]["4"].keys():
        if value == "text":
            await message.answer(text = f"Питання 4: ")
            await message.answer(text = f"{test2["questions"]["4"][f"{value}"]}")
        if value == "answers":
            for answer in test2["questions"]["4"][f"{value}"]:
                await message.answer(text = f"{answer}")
    await message.answer(text = "Введіть вашу відповідь: ")
    await state.set_state(Test2.question_4)

@dispatcher.message(Test2.question_4)
async def test2_question_4_state(message: types.Message, state: context.FSMContext):
    await state.update_data(question_4 = message.text)
    for value in test2["questions"]["5"].keys():
        if value == "text":
            await message.answer(text = f"Питання 5: ")
            await message.answer(text = f"{test2["questions"]["5"][f"{value}"]}")
        if value == "answers":
            for answer in test2["questions"]["5"][f"{value}"]:
                await message.answer(text = f"{answer}")
    await message.answer(text = "Введіть вашу відповідь: ")
    await state.set_state(Test2.question_5)

@dispatcher.message(Test2.question_5)
async def test2_question_5_state(message: types.Message, state: context.FSMContext):
    await state.update_data(question_5 = message.text)
    answers = await state.get_data()

    correct_answers = 0

    for key in test2["questions"].keys():
        if test2["questions"][f"{key}"]["correct"].lower() == answers[f"question_{key}"].lower():
            correct_answers += 1
    await message.answer(text = f"Вірних відповідей: {correct_answers}")
    await message.answer(text = "Бажаєте подивитись свої помилки?", reply_markup = yes_or_no_keyboard)
    await state.clear()
    
    

    


    
        