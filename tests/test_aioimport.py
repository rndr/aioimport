import asyncio
import threading

import pytest

import aioimport


@pytest.mark.asyncio
async def test_import_module() -> None:
    async with aioimport.importer:
        import tests.helper_test_import_module_event_source as event_source

        task = asyncio.create_task(
            aioimport.import_module("tests.helper_test_import_module_long_import")
        )
        await asyncio.wait_for(event_source.start.wait(), timeout=5)
        event_source.end.set()
        await asyncio.wait_for(task, timeout=5)

        event = threading.Event()

        def check_import() -> None:
            import tests.helper_test_import_module_long_import

            assert tests.helper_test_import_module_long_import.done
            event.set()

        event_source.start.clear()
        event_source.end.clear()
        threading.Thread(target=check_import, daemon=True).start()
        event.wait(timeout=5)


@pytest.mark.asyncio
async def test_reload() -> None:
    async with aioimport.importer:
        import tests.helper_test_reload_data

        data1 = tests.helper_test_reload_data.data
        await aioimport.reload(tests.helper_test_reload_data)
        assert data1 is not tests.helper_test_reload_data.data
