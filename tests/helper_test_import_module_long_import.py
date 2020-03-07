import time

import tests.helper_test_import_module_event_source


tests.helper_test_import_module_event_source.start.set()

start = time.monotonic()
while not tests.helper_test_import_module_event_source.end.is_set():
    if time.monotonic() - start > 5:
        raise Exception("Timeout")
    time.sleep(0)
done = True
