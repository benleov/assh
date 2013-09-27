# -*- coding: utf-8 -*-

import sys
import optparse
import logging

from .utils import LOGGING_LEVELS
from .exceptions import ConfigError
from .advanced_ssh_config import AdvancedSshConfig


def main():
    parser = optparse.OptionParser(usage='%prog [-v] -h hostname -p port', version='%prog 1.0')
    parser.add_option('-H', '--hostname', dest='hostname', help='Host')
    parser.add_option('-p', '--port', dest='port', default=22)
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true')
    parser.add_option('-l', '--log_level', dest='log_level')
    parser.add_option('-u', '--update-sshconfig', dest='update_sshconfig', action='store_true')
    parser.add_option('--dry-run', action='store_true', dest='dry_run')
    (options, args) = parser.parse_args()

    logging_level = LOGGING_LEVELS.get(options.log_level, logging.ERROR)
    if options.verbose and logging_level == logging.ERROR:
        logging_level = logging.DEBUG
    logging.basicConfig(level=logging_level,
                        filename=None,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    log = logging.getLogger('')

    try:
        ssh = AdvancedSshConfig(hostname=options.hostname,
                                port=options.port,
                                verbose=options.verbose,
                                update_sshconfig=options.update_sshconfig,
                                dry_run=options.dry_run)
        if ssh.hostname:
            ssh.connect()
        elif not options.update_sshconfig:
            print 'Must specify a host!\n'
    except ConfigError as err:
        sys.stderr.write(err.message)
#    except Exception as err:
#        log.debug(err.__str__())


if __name__ == '__main__':
    main()
