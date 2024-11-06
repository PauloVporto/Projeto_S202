from database import Database
from avaliacao_crud import AvaliacaoCRUD
from cli import AvaliacaoCLI

db=Database("bolt://3.238.65.57:7687", "neo4j", "conferences-conversions-bath")

cli_db = AvaliacaoCRUD(db)

avalcli = AvaliacaoCLI(cli_db)
avalcli.run()

db.close()