"""
Bank Of America Transactions (CSV) Importer
"""
import csv
import datetime
import logging

from silverstrike.importers.import_statement import ImportStatement

logger = logging.getLogger(__name__)


def import_transactions(csv_path):
    lines = []
    with open(csv_path) as csv_file:
        csviter = csv.reader(csv_file, delimiter=",")
        next(csviter)  # First line is header
        for line in csviter:
            try:
                transaction_time = datetime.datetime.strptime(line[0], "%m/%d/%Y").date()
                lines.append(
                    ImportStatement(
                        notes=line[1],
                        account=line[2],
                        book_date=transaction_time,
                        transaction_date=transaction_time,
                        amount=float(line[4]),
                    )
                )
            except ValueError as e:
                logger.error("Error" + e)
                pass

    return lines