import logging

from artnet import daemon

log = logging.getLogger(__name__)


log.info("Running script %s" % __name__)
q = daemon.Poller("", "")
q.run()
