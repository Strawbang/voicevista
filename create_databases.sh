set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
  CREATE DATABASE voicevista;
  CREATE DATABASE kong;
EOSQL
