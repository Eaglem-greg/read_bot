from aiogram.filters import Filter
from aiogram.types import CallbackQuery

class IsDigitCallbackData(Filter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data is None:
            return False
        return callback.data.isdigit()
    
class IsDelBookmarkCallbackData(Filter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data is None:
            return False
        return callback.data.endswith("del") and callback.data[:-3].isdigit()
    
    