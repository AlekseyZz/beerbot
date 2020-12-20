import datetime

import pendulum

from src.config import config

pendulum.set_locale(name = config["discord"]["interface"]["time_local"])


def duration_readable(seconds: int) -> str:
    """
    Функция для читаемого формата оставшегося времени

    :param seconds: Количество секунд
    :return: Строка с читаемым форматом времени
    """

    return pendulum.duration(seconds = seconds).in_words()


def timedelta_readable(time: datetime.datetime) -> str:
    """
    Функция для читаемого формата разницы времени

    :param time: Время
    :return:
    """

    delta_seconds: float = (datetime.datetime.now() - time).total_seconds()
    return pendulum.now().subtract(seconds = int(delta_seconds)).diff_for_humans()


def time_readable(time) -> str:
    """
    Функция для читаемого формата времени

    :param time: Время
    :return: Строка с читаемым форматом времени
    """

    return time.strftime(config["discord"]["interface"]["time_format"])
