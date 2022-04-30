from aiogram import types
from aiogram.dispatcher import Dispatcher
import hashlib

async def inline_wikipedia_handler(query: types.InlineQuery):
    text = query.query or "echo"
    links = f"https://ru.wikipedia.org/wiki/{text}"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title="Wikipedia: ",
            url=links,
            input_message_content=types.InputMessageContent(
                message_text=links
            )
        )
    ]
    await query.answer(articles, cache_time=60, is_personal=True)

def registerr_handler_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_wikipedia_handler)
