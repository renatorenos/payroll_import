import settings
from connectOracle import utils

# Check if a connection to the database has occurred
print(utils.check_connection())

result = utils.sql_query("SELECT 1 FROM DUAL")
print(result)