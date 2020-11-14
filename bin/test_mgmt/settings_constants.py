from os import path

class SettingsConstants:
  APP_ROOT = "../codingame_test_runner.py"
  CONFIG_FILE_NAME = "config.yaml"
  BASE_DIR_NAME = "base_dir"
  TEST_CASES = "test_cases"
  ROOT_DIR = path.dirname(path.abspath(APP_ROOT))
  SETTINGS_PATH = path.join(ROOT_DIR, CONFIG_FILE_NAME)