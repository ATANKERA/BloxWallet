#!/usr/bin/python

from blox import walletfunction
from generators import bloxGenerator
import argparse
import sys, os, time, datetime, random, math, signal, threading, re
import logging
from faker import Faker
from models import User
from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError
from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode
from tabulate import tabulate


RUNNING_THREADS = []
TERMINATE_GRACEFULLY = False
DEFAULT_READ_PERCENTAGE = .95

#@todo: add checks for multi-region operations on single region schemas.

ACTION_UPLOADKEYS = "key upload"
ACTION_GETKEYS = "key download"
ACTION_NEWCOIN = "new coin crypto"

def signal_handler(sig, frame):
    global TERMINATE_GRACEFULLY
    grace_period = 15
    logging.info('Waiting at most %d seconds for threads to shutdown...', grace_period)
    TERMINATE_GRACEFULLY = True

    start = time.time()
    while threading.active_count() > 1:
        if (time.time() - start) > grace_period:
            logging.info("grace period has passed. killing threads.")
            os._exit(1)
        else:
            time.sleep(.1)

    logging.info("shutting down gracefully.")
    sys.exit(0)


DEFAULT_PARTITION_MAP = {
    "sshprivatekeys": env.getkeys[],
    "crytpcurrencies": env.getkeyvalues[],
    "sshpublickeys": env.getkeyspublic[]
}

# Create a connection to the blox database and populate a set of cities with rides, vehicles, and users.
def load_blox_data(conn_string, num_keys, num_pubkeys, echo_sql = False):
    if num_users <= 0 or num_rides <= 0 or num_vehicles <= 0:
        raise ValueError("The number of objects to generate must be > 0")

    start_time = time.time()
    with blox(conn_string, echo=echo_sql) as blox:
        engine = create_engine(conn_string, convert_unicode=True, echo=echo_sql)
        for city in cities:
            if TERMINATE_GRACEFULLY:
                logging.debug("terminating")
                break

            logging.info("accessing user keys for %s...", keys)
            logging.info("accessing currency %s...", values)

        upodate_data(conn_string, num_keys, num_pubkeys)

    return

# Generates evenly distributed load among the provided cities


def simulate_blox_load(conn_string, read_percentage, follower_reads, connection_duration_in_seconds, echo_sql = False):

    datagen = Faker()
    while True:
        logging.debug("creating a new connection to %s, which will reset in %d seconds", conn_string, connection_duration_in_seconds)
        try:
            with blox(conn_string, multi_region= use_multi_region, echo=echo_sql) as blox:
                timeout = time.time() + connection_duration_in_seconds #refresh connections so load can balance among cluster nodes even if the cluster size changes
                while True:

                    if TERMINATE_GRACEFULLY:
                        logging.debug("Terminating thread.")
                        return

                    if time.time() > timeout:
                        break

        except DBAPIError:
            logging.error("lost connection to the db. sleeping for 10 seconds")
            time.sleep(10)



def extract_zone_pairs_from_cli(pair_list):
    if pair_list is None:
        return {}

    zone_pairs = {}

    for zone_pair in pair_list:
        pair = zone_pair.split(":")
        if len(pair) < 1:
            pair = ["default"].append(pair[0])
        else:
            pair = [pair[0], ":".join(pair[1:])]  # if there are many colons convert this to only two items

        zone_pairs.setdefault(pair[0], "")
        zone_pairs[pair[0]] = pair[1]

    return zone_pairs


def set_query_parameter(url, param_name, param_value):
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)
    query_params[param_name] = [param_value]
    new_query_string = urlencode(query_params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query_string, fragment))

def setup_parser():
    parser = argparse.ArgumentParser(description='CLI for Blox.')
    subparsers = parser.add_subparsers(dest='subparser_name')

    ###########
    # GENERAL COMMANDS
    ##########
    parser.add_argument('--log-level', dest='log_level', default='info',
                        help='The log level ([debug|info|warning|error]) for blox messages. (default = info)')
    parser.add_argument('--app-name', dest='app_name', default='blox',
                        help='The name that can be used for filtering statements by client in the Admin UI.')
    parser.add_argument('--url', dest='conn_string', default='postgres://root@localhost:26257/blox?sslmode=disable',
                        help="connection string to blox database. Default is 'postgres://root@localhost:26257/blox?sslmode=disable'")
    parser.add_argument('--echo-sql', dest='echo_sql', action='store_true',
                        help='set this if you want to print all executed SQL statements')



