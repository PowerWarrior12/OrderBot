from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup, KeyboardButton
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Оформить заказ'))
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отменить'))
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Показать заказы'))