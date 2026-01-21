from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards.bookmarks_kb import create_bookmarks_keyboard, create_edit_keyboard
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon import LEXICON

user_router = Router()

@user_router.message(CommandStart())
async def process_start_command(message: Message, db: dict):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in db["users"]:
        db["users"][message.from_user.id] = deepcopy(db.get("user_template"))

@user_router.message(Command(comands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])

@user_router.message(Command(commands="beginning"))
async def process_beginning_command(message: Message, book: dict, db: dict):
    db["users"][message.from_user.id]["page"] = 1
    text = book[1]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            "backward",
            f"1/{len(book)}",
            "forward"
        )
    )

@user_router.message(Command(commands="continue"))
async def process_continue_command(message: Message, book: dict, db: dict):
    text = book[db["users"][message.from_user.id]["page"]]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            "backward",
            f"{db["users"][message.from_user.id]['page']}/{len(book)}",
            "forward"
        )
    )