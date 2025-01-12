import pytest
from zadanie_3.zadanie3 import log_event, EventHandler, DerivedHandler

# Testy dla log_event (singledispatch)

def test_log_event_registration():
    """Sprawdź, czy log_event obsługuje właściwe typy"""
    assert log_event.registry[str] is not None
    assert log_event.registry[int] is not None
    assert log_event.registry[dict] is not None

def test_log_event_unregistered_type():
    """Testuje podnoszenie wyjątku dla nieobsługiwanego typu"""
    with pytest.raises(NotImplementedError, match="Brak implementacji dla typu: <class 'float'>"):
        log_event(3.14)

# Testy dla EventHandler

def test_event_handler_str():
    """Sprawdź obsługę zdarzenia typu str"""
    handler = EventHandler()
    handler.handle_event("test")
    assert handler.event_count == 1

def test_event_handler_int():
    """Sprawdź obsługę zdarzenia typu int"""
    handler = EventHandler()
    handler.handle_event(42)
    assert handler.event_count == 1

def test_event_handler_list():
    """Sprawdź obsługę zdarzenia typu list"""
    handler = EventHandler()
    handler.handle_event(["a", "b", "c"])
    assert handler.event_count == 1

def test_event_handler_list():
    """Sprawdź obsługę zdarzenia typu list"""
    handler = EventHandler()
    handler.handle_event("test")
    handler.handle_event(42)
    handler.handle_event(["a", "b", "c"])
    assert handler.event_count == 3

def test_event_handler_unregistered_type():
    """Sprawdź wyjątek dla nieobsługiwanego typu"""
    handler = EventHandler()
    with pytest.raises(NotImplementedError, match="Nieobsługiwany typ zdarzenia: <class 'set'>"):
        handler.handle_event({1, 2, 3})

# Testy dla DerivedHandler

def test_derived_handler_int():
    """Sprawdź obsługę zdarzenia typu int w DerivedHandler"""
    derived_handler = DerivedHandler()
    derived_handler.handle_event(42)
    assert derived_handler.event_count == 1

def test_derived_handler_float():
    """Sprawdź obsługę zdarzenia typu float w DerivedHandler"""
    derived_handler = DerivedHandler()
    derived_handler.handle_event(3.14)
    assert derived_handler.event_count == 1
