#!/usr/bin/env python3
'''Async Generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yeilds random numbers 10 times with 1 sec delay
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
