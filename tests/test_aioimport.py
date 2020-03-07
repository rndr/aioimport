import asyncio

import aioimport

import tests.test_module as test_module


def test_cache_module():
    asyncio.get_event_loop().run_until_complete(
        aioimport.cache_module(test_module.__name__)
    )


def test_import_module():
    assert test_module is asyncio.get_event_loop().run_until_complete(
        aioimport.import_module(test_module.__name__)
    )
