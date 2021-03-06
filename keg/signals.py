from __future__ import absolute_import
from __future__ import unicode_literals

from flask.signals import Namespace

_signals = Namespace()

# Call when application initializations is completed.
# Sender will be the application instance.
app_ready = _signals.signal('app-ready')
config_ready = _signals.signal('config-ready')
testing_run_start = _signals.signal('testing-run-start')
