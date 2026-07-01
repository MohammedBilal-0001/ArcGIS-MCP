from encodings import search_function
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent)) 

from services.query_builder import SearchQueryBuilder
q = SearchQueryBuilder.build(
    query= "latakia",
    owner="hisemdar",
    item_type="Map"
)
print(q)