import multiprocessing
import time
import os
import pytest
from app import app


def run_server():
  """Target function for running the Flask server in a clean process."""
  # use_reloader=False prevents code monitoring from spawning loops in sub-processes
  app.run(port=5000, debug=False, use_reloader=False)


@pytest.fixture(scope="session", autouse=True)
def flask_server():
  """Spins up the Flask web app locally in a separate process automatically."""
  # Create a clean background thread/process running our Flask app instance
  proc = multiprocessing.Process(target=run_server)
  proc.start()

  # Give the background server a brief 1-second window to boot up and bind to port 5000
  time.sleep(1)

  yield  # This is the exact moment where all your Playwright test files execute!

  # Clean up: After all tests finish, terminate the background server safely
  proc.terminate()
  proc.join()

@pytest.fixture(scope="session")
def base_url():
    """Provides the home page URL, dynamically switching ports for local vs CI/CD."""
    # If running on GitHub Actions, use port 8000. Otherwise, default to 5000.
    if os.environ.get("GITHUB_ACTIONS") == "true":
      return "http://127.0.0.1:8000"
    return "http://127.0.0.1:5000"
