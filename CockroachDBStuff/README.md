# Blox

Blox is a way to track CryptoKeys for your server, built on top of the Movr project by Cockroach Labs.

## Getting started
First, [download CockroachDB](https://www.cockroachlabs.com/docs/stable/install-cockroachdb.html) and start a local cluster with `cockroach start --insecure --host localhost --background`

Then create the database `blox` with `cockroach sql --insecure --host localhost -e "create database blox;"`
