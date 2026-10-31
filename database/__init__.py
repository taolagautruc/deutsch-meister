import os
import importlib.util

_root_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "database.py"))
_spec = importlib.util.spec_from_file_location("root_database", _root_db_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

get_connection = _mod.get_connection
init_db = _mod.init_db
DB_NAME = _mod.DB_NAME
is_postgres = getattr(_mod, "is_postgres", lambda: False)

__all__ = ["get_connection", "init_db", "DB_NAME", "is_postgres"]
